"""Main CLI: walk a folder, extract metrics, produce reports.

Usage:
    python analyze.py --input /path/to/monthly/files --output /path/to/reports
    python analyze.py --input ./sample_data --output ./output
"""

from __future__ import annotations

import argparse
import logging
import sys
import traceback
from pathlib import Path

from extractors.pdf_extractor import extract_from_pdf
from extractors.pptx_extractor import extract_from_pptx
from extractors.xlsx_extractor import extract_from_xlsx
from models import MetricRow
from report import write_excel_report, write_pptx_summary

log = logging.getLogger("analyze")


def infer_domain_from_path(path: Path, input_root: Path) -> str:
    """Infer domain from folder structure: input_root/DOMAIN/.../file.ext

    If the file is directly in input_root, use filename stem.
    """
    try:
        rel = path.relative_to(input_root)
    except ValueError:
        return path.parent.name
    if len(rel.parts) > 1:
        return rel.parts[0]
    return path.stem


def extract_file(path: Path, domain: str) -> list[MetricRow]:
    """Dispatch to the right extractor based on file extension."""
    ext = path.suffix.lower()
    try:
        if ext == ".pptx":
            return extract_from_pptx(path, domain_hint=domain)
        if ext == ".pdf":
            return extract_from_pdf(path, domain_hint=domain)
        if ext in (".xlsx", ".xlsm"):
            return extract_from_xlsx(path, domain_hint=domain)
        log.debug("Skipping unsupported file: %s", path)
        return []
    except Exception as e:
        log.error("Failed to extract %s: %s", path, e)
        log.debug(traceback.format_exc())
        return []


def walk_input(input_dir: Path) -> list[Path]:
    """Find all supported files, skipping temp and hidden files."""
    exts = {".pptx", ".pdf", ".xlsx", ".xlsm"}
    files = []
    for p in input_dir.rglob("*"):
        if not p.is_file():
            continue
        if p.name.startswith("~$") or p.name.startswith("."):
            continue
        if p.suffix.lower() in exts:
            files.append(p)
    return sorted(files)


def main():
    ap = argparse.ArgumentParser(description="Risk metrics analyzer")
    ap.add_argument("--input", required=True, type=Path, help="Input folder")
    ap.add_argument("--output", required=True, type=Path, help="Output folder")
    ap.add_argument("--verbose", "-v", action="store_true")
    args = ap.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s %(name)s: %(message)s",
    )
    # Silence noisy third-party loggers
    for noisy in ("pdfminer", "pdfplumber", "PIL"):
        logging.getLogger(noisy).setLevel(logging.WARNING)

    input_dir = args.input.resolve()
    output_dir = args.output.resolve()

    if not input_dir.is_dir():
        log.error("Input folder does not exist: %s", input_dir)
        sys.exit(1)
    output_dir.mkdir(parents=True, exist_ok=True)

    files = walk_input(input_dir)
    log.info("Found %d files to process", len(files))

    all_metrics: list[MetricRow] = []
    for f in files:
        domain = infer_domain_from_path(f, input_dir)
        log.info("Processing %s (domain=%s)", f.name, domain)
        metrics = extract_file(f, domain)
        log.info("  → extracted %d metric rows", len(metrics))
        all_metrics.extend(metrics)

    log.info("Total metrics extracted: %d", len(all_metrics))
    flagged = [m for m in all_metrics if m.is_flagged()]
    log.info("Flagged (Amber/Red/Worsening): %d", len(flagged))

    # Warn about metrics whose threshold failed to parse (extraction likely bad)
    failed_parse = [m for m in all_metrics if not m.threshold.parse_ok]
    if failed_parse:
        log.warning(
            "%d metrics had unparseable thresholds (cannot classify). "
            "Check the 'Raw Extracted' sheet for these IDs: %s",
            len(failed_parse),
            ", ".join(m.metric_id for m in failed_parse[:10]),
        )

    # Warn about suspiciously large values - a percentage metric shouldn't
    # exceed ~100% in most cases. Values above 100 likely indicate cell-merge
    # corruption in PDF extraction.
    suspicious = []
    for m in all_metrics:
        for mv in m.months:
            if mv.value is not None and mv.value > 100:
                suspicious.append((m.metric_id, mv.label, mv.value))
    if suspicious:
        log.warning(
            "%d suspicious values (>100) detected - likely PDF cell-merge "
            "corruption. Verify these: %s",
            len(suspicious),
            "; ".join(f"{mid} {lbl}={v}" for mid, lbl, v in suspicious[:5]),
        )

    excel_path = output_dir / "risk_metrics_report.xlsx"
    pptx_path = output_dir / "risk_metrics_summary.pptx"

    write_excel_report(all_metrics, excel_path)
    write_pptx_summary(all_metrics, pptx_path)

    log.info("Wrote %s", excel_path)
    log.info("Wrote %s", pptx_path)


if __name__ == "__main__":
    main()
