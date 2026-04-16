"""Data models and threshold parsing logic."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional


class Status(Enum):
    GREEN = 0
    AMBER = 1
    RED = 2
    UNKNOWN = -1

    def __lt__(self, other):
        return self.value < other.value


class TableType(Enum):
    BREACHED_KCI = "Breached KCI"
    PREV_BREACHED_KCI = "Previous Breached KCI - monitoring"
    PREV_AMBER_KRI = "Previous Amber KRI - monitoring"
    AMBER_KCI = "Amber KCI"

    @classmethod
    def match(cls, text: str) -> Optional["TableType"]:
        """Fuzzy match a heading to a known table type."""
        if not text:
            return None
        norm = re.sub(r"\s+", " ", text.strip().lower())
        # Order matters: check longer/more-specific labels first
        candidates = [
            (cls.PREV_BREACHED_KCI, ["previous breached kci", "prev breached kci"]),
            (cls.PREV_AMBER_KRI, ["previous amber kri", "prev amber kri"]),
            (cls.BREACHED_KCI, ["breached kci"]),
            (cls.AMBER_KCI, ["amber kci"]),
        ]
        for table_type, patterns in candidates:
            for p in patterns:
                if p in norm:
                    return table_type
        return None


@dataclass
class Threshold:
    """Parsed threshold with numeric bands and direction."""

    raw_text: str
    green_cutoff: Optional[float] = None  # Boundary between Green and Amber
    red_cutoff: Optional[float] = None  # Boundary between Amber and Red
    higher_is_worse: bool = True
    parse_ok: bool = False

    def classify(self, value: Optional[float]) -> Status:
        if value is None or not self.parse_ok:
            return Status.UNKNOWN
        if self.green_cutoff is None or self.red_cutoff is None:
            return Status.UNKNOWN

        if self.higher_is_worse:
            if value >= self.red_cutoff:
                return Status.RED
            if value >= self.green_cutoff:
                return Status.AMBER
            return Status.GREEN
        else:
            if value <= self.red_cutoff:
                return Status.RED
            if value <= self.green_cutoff:
                return Status.AMBER
            return Status.GREEN


@dataclass
class MonthValue:
    month: datetime  # First day of the month
    label: str  # Original label e.g. "December'25"
    value: Optional[float]
    raw: str


@dataclass
class MetricRow:
    source_file: str
    domain: str
    subdomain: str
    table_type: TableType
    metric_id: str
    metric_name: str
    threshold: Threshold
    frequency: str
    months: list[MonthValue] = field(default_factory=list)
    reason: str = ""
    progress: str = ""
    ref: str = ""  # M7 / ERR Ref

    def latest_status(self) -> tuple[Optional[MonthValue], Status]:
        """Most recent month with a parseable value, plus its status."""
        sorted_months = sorted(
            [m for m in self.months if m.value is not None],
            key=lambda m: m.month,
        )
        if not sorted_months:
            return None, Status.UNKNOWN
        latest = sorted_months[-1]
        return latest, self.threshold.classify(latest.value)

    def trend(self) -> str:
        """Improving / Stable / Worsening based on first vs latest status."""
        sorted_months = sorted(
            [m for m in self.months if m.value is not None],
            key=lambda m: m.month,
        )
        if len(sorted_months) < 2:
            return "Insufficient data"
        first_status = self.threshold.classify(sorted_months[0].value)
        last_status = self.threshold.classify(sorted_months[-1].value)
        if first_status == Status.UNKNOWN or last_status == Status.UNKNOWN:
            return "Unknown"
        if last_status.value > first_status.value:
            return "Worsening"
        if last_status.value < first_status.value:
            return "Improving"
        return "Stable"

    def is_flagged(self) -> bool:
        """Flag if latest is Amber/Red or trend is Worsening."""
        _, status = self.latest_status()
        if status in (Status.AMBER, Status.RED):
            return True
        if self.trend() == "Worsening":
            return True
        return False


# ---------- Threshold parsing ----------

_NUM = r"([0-9]+(?:\.[0-9]+)?)"


def parse_threshold(text: str) -> Threshold:
    """Parse threshold strings like 'Green < 3%, Amber 3% < x < 5%, Red > 5%'.

    Handles variations in spacing, <= vs <, % optional, order of bands.
    Also handles cases where the threshold text got corrupted by adjacent
    cell contents bleeding in (common with pdfplumber table extraction).
    """
    t = Threshold(raw_text=text or "")
    if not text:
        return t

    # Normalize: lowercase, collapse whitespace
    s = re.sub(r"\s+", " ", text.strip())
    s_low = s.lower()

    # Find Green, Amber, Red clauses
    green_match = re.search(rf"green\s*([<>]=?)\s*{_NUM}\s*%?", s_low)
    red_match = re.search(rf"red\s*([<>]=?)\s*{_NUM}\s*%?", s_low)

    if not green_match or not red_match:
        return t

    green_op, green_val = green_match.group(1), float(green_match.group(2))
    red_op, red_val = red_match.group(1), float(red_match.group(2))

    # Direction inference: if Green < N and Red > M, higher is worse
    if "<" in green_op and ">" in red_op:
        t.higher_is_worse = True
        t.green_cutoff = green_val
        t.red_cutoff = red_val
    elif ">" in green_op and "<" in red_op:
        t.higher_is_worse = False
        t.green_cutoff = green_val
        t.red_cutoff = red_val
    else:
        # Ambiguous; fall back to numeric ordering
        t.higher_is_worse = green_val < red_val
        t.green_cutoff = min(green_val, red_val)
        t.red_cutoff = max(green_val, red_val)

    t.parse_ok = True
    return t


def repair_threshold_from_neighbor(threshold_text: str, neighbor_text: str) -> str:
    """If threshold is truncated (no Red clause), try to recover from neighbor cell.

    pdfplumber sometimes splits a threshold cell's text across two adjacent
    cells. If we see 'Green < 5%, Amber 5% < x <' in one cell and
    '10M%o, nRtheldy >' (Monthly + Red ...) in the next, we can concatenate
    them and re-parse.
    """
    if not threshold_text or not neighbor_text:
        return threshold_text
    low = threshold_text.lower()
    if "red" in low:
        return threshold_text  # Already complete
    # If neighbor contains 'red' (possibly scrambled), try joining
    if "red" in neighbor_text.lower() or re.search(r"[>]\s*\d", neighbor_text):
        # Interleaving fix: pdfplumber sometimes zips two strings char-by-char
        unzipped = _try_unzip(neighbor_text)
        if unzipped:
            return threshold_text + " " + unzipped
        return threshold_text + " " + neighbor_text
    return threshold_text


def _try_unzip(text: str) -> Optional[str]:
    """Recover a threshold-like substring from text where multiple cells got
    interleaved by pdfplumber's table extraction.

    Example inputs we've seen in real PDF extractions:
        '10M%o, nRtheldy >'   (contains '10%, Red > ...' merged with 'Monthly')
        'Monthly 10%, Red > 10%'  (just concatenated, not really interleaved)

    Strategy: look for the telltale 'Red' token followed by a comparison and
    number, allowing arbitrary junk characters between the letters. If found,
    reconstruct a clean threshold clause.
    """
    if not text or len(text) < 4:
        return None

    # Case 1: threshold tokens are intact, just prefixed/suffixed by other text
    m = re.search(r"[rR]ed\s*[<>]=?\s*\d+(?:\.\d+)?\s*%?", text)
    if m:
        return m.group(0)

    # Case 2: 'Red' is split by intervening characters.
    # Look for R, then e within the next 8 chars, then d within the next 8 chars,
    # then an operator and a number somewhere after.
    m = re.search(
        r"R.{0,4}?e.{0,4}?d.{0,15}?([<>]=?)\s*(\d+(?:\.\d+)?)\s*%?",
        text,
        re.IGNORECASE,
    )
    if m:
        op, num = m.group(1), m.group(2)
        return f"Red {op} {num}%"

    # Case 3: Number precedes 'Red' due to interleaving order.
    # E.g. "10M%o, nRtheldy >" has "10" then "R...e...d" then ">".
    # Allow arbitrary junk (including letters from the other interleaved word)
    # between the number and the 'R'.
    m = re.search(
        r"(\d+(?:\.\d+)?)\s*%?.{0,15}?R.{0,4}?e.{0,4}?d.{0,15}?([<>]=?)",
        text,
        re.IGNORECASE,
    )
    if m:
        num, op = m.group(1), m.group(2)
        return f"Red {op} {num}%"

    return None


# ---------- Month label parsing ----------

_MONTH_NAMES = {
    "january": 1, "jan": 1,
    "february": 2, "feb": 2,
    "march": 3, "mar": 3,
    "april": 4, "apr": 4,
    "may": 5,
    "june": 6, "jun": 6,
    "july": 7, "jul": 7,
    "august": 8, "aug": 8,
    "september": 9, "sep": 9, "sept": 9,
    "october": 10, "oct": 10,
    "november": 11, "nov": 11,
    "december": 12, "dec": 12,
}


def parse_month_label(label: str) -> Optional[datetime]:
    """Parse 'December'25', 'Jan-26', 'Feb 2026' etc. into a datetime."""
    if not label:
        return None
    s = label.lower().strip()
    # Find month name
    month_num = None
    for name, num in _MONTH_NAMES.items():
        if name in s:
            month_num = num
            break
    if month_num is None:
        return None
    # Find a 2- or 4-digit year
    year_match = re.search(r"(\d{4}|\d{2})", s.replace(str(month_num), "", 1) if month_num < 10 else s)
    # Safer: just strip month name then look for year
    s2 = s
    for name in _MONTH_NAMES:
        s2 = s2.replace(name, " ")
    year_match = re.search(r"(\d{4}|\d{2})", s2)
    if not year_match:
        return None
    year = int(year_match.group(1))
    if year < 100:
        year += 2000
    try:
        return datetime(year, month_num, 1)
    except ValueError:
        return None


def parse_percentage(text: str) -> Optional[float]:
    """Parse '3.2%', '3.2', '  12.5 %  ' into a float."""
    if text is None:
        return None
    s = str(text).strip().replace(",", "")
    if not s or s.lower() in ("n/a", "na", "-", "--", "tbd"):
        return None
    m = re.search(r"(-?\d+(?:\.\d+)?)", s)
    if not m:
        return None
    try:
        return float(m.group(1))
    except ValueError:
        return None
