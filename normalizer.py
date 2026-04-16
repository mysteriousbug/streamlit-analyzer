"""Normalize raw extracted tables into MetricRow objects.

Raw tables come in as list-of-lists from format-specific extractors.
This module handles the common logic: header detection, column mapping,
and row parsing.
"""

from __future__ import annotations

import re
from typing import Optional

from models import (
    MetricRow,
    MonthValue,
    TableType,
    parse_month_label,
    parse_percentage,
    parse_threshold,
    repair_threshold_from_neighbor,
)

# Column header aliases - map variations to canonical names
_HEADER_ALIASES = {
    "id": {"id", "metric id", "kci id", "kri id", "ref id"},
    "metric_name": {"metric name", "metric", "kci name", "kri name", "description"},
    "threshold": {"threshold", "thresholds", "tolerance", "rag threshold"},
    "frequency": {"freq", "frequency", "cadence"},
    "reason": {"reason for breach", "reason", "breach reason", "root cause"},
    "progress": {"progress", "remediation", "mitigation", "action", "status update"},
    "ref": {"m7 / err ref", "m7/err ref", "m7 ref", "err ref", "m7", "err", "reference"},
}


def _normalize_header(h: str) -> str:
    return re.sub(r"\s+", " ", (h or "").strip().lower())


def _map_columns(headers: list[str]) -> dict:
    """Return {canonical_name: column_index} for recognized headers.

    Unrecognized headers that look like month labels are stored under
    'month_columns' as [(index, original_label, parsed_date), ...].
    """
    mapping = {"month_columns": []}
    for idx, raw in enumerate(headers):
        h = _normalize_header(raw)
        if not h:
            continue
        matched = False
        for canonical, aliases in _HEADER_ALIASES.items():
            if h in aliases or any(alias in h for alias in aliases):
                # Prefer first match, don't overwrite
                if canonical not in mapping:
                    mapping[canonical] = idx
                    matched = True
                    break
        if matched:
            continue
        # Try as a month label
        parsed = parse_month_label(raw)
        if parsed is not None:
            mapping["month_columns"].append((idx, raw, parsed))
    return mapping


def _is_header_row(row: list[str]) -> bool:
    """Heuristic: a header row contains 'id' and 'metric' keywords."""
    joined = " ".join(_normalize_header(c) for c in row)
    has_id = bool(re.search(r"\bid\b", joined))
    has_metric = "metric" in joined or "kci" in joined or "kri" in joined
    return has_id and has_metric


def find_header_row(table: list[list[str]]) -> Optional[int]:
    """Return index of the header row, or None."""
    for i, row in enumerate(table[:5]):  # Headers are near the top
        if _is_header_row(row):
            return i
    return None


def normalize_table(
    raw_table: list[list[str]],
    table_type: TableType,
    source_file: str,
    domain: str,
    subdomain: str,
) -> list[MetricRow]:
    """Convert a raw table (list of rows of strings) into MetricRow objects."""
    if not raw_table:
        return []

    header_idx = find_header_row(raw_table)
    if header_idx is None:
        return []

    headers = raw_table[header_idx]
    col_map = _map_columns(headers)

    # Require at least ID and metric name columns
    if "id" not in col_map or "metric_name" not in col_map:
        return []

    rows = []
    for raw_row in raw_table[header_idx + 1 :]:
        # Pad short rows
        row = list(raw_row) + [""] * (len(headers) - len(raw_row))

        def cell(key: str) -> str:
            idx = col_map.get(key)
            if idx is None or idx >= len(row):
                return ""
            return (row[idx] or "").strip()

        metric_id = cell("id")
        metric_name = cell("metric_name")
        # Skip empty or summary rows
        if not metric_id and not metric_name:
            continue
        if not metric_id or len(metric_id) < 2:
            continue

        threshold_text = cell("threshold")
        threshold = parse_threshold(threshold_text)
        # If parsing failed, try to recover from adjacent Freq cell
        # (common with PDF extractors that split threshold text across cells)
        if not threshold.parse_ok:
            freq_text = cell("frequency")
            repaired = repair_threshold_from_neighbor(threshold_text, freq_text)
            if repaired != threshold_text:
                threshold = parse_threshold(repaired)

        months = []
        for idx, label, date in col_map["month_columns"]:
            if idx < len(row):
                raw_val = row[idx]
                months.append(
                    MonthValue(
                        month=date,
                        label=label,
                        value=parse_percentage(raw_val),
                        raw=str(raw_val),
                    )
                )

        rows.append(
            MetricRow(
                source_file=source_file,
                domain=domain,
                subdomain=subdomain,
                table_type=table_type,
                metric_id=metric_id,
                metric_name=metric_name,
                threshold=threshold,
                frequency=cell("frequency"),
                months=months,
                reason=cell("reason"),
                progress=cell("progress"),
                ref=cell("ref"),
            )
        )
    return rows
