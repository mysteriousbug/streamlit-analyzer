# Risk Metrics Analyzer

Pure-Python pipeline that reads monthly risk-metric documents (PPTX, PDF, XLSX) and produces a consolidated breach report.

## What it does

- Walks a folder of monthly risk-metric files
- Finds tables of type `Breached KCI`, `Previous Breached KCI - monitoring`, `Previous Amber KRI - monitoring`, or `Amber KCI` within each file
- Parses the threshold string (e.g. `Green < 3%, Amber 3% < x < 5%, Red > 5%`) into numeric bands
- Classifies each month's value as Green / Amber / Red
- Flags metrics that are currently Amber/Red or trending worse
- Produces two outputs: a colour-coded Excel workbook and a summary PPTX

## Install

```bash
pip install -r requirements.txt
```

Python 3.10+. No AI/LLM dependencies.

## Folder layout for input

Organize input files so the top-level folder name under `--input` is the domain:

```
monthly_files/
├── DLP/
│   ├── DLP_WebAppSec_Feb2026.pptx
│   └── DLP_Endpoint_Feb2026.pdf
├── Governance/
│   └── GOV_Feb2026.pdf
└── TPSA/
    └── TPSA_Feb2026.xlsx
```

The domain is taken from the first folder segment under the input root. The subdomain is taken from the slide title (PPTX), the page's top-line text (PDF), or the sheet name (XLSX).

## Usage

```bash
# Run on real data
python analyze.py --input /path/to/monthly_files --output ./reports

# Test with sample data first
python generate_samples.py
python analyze.py --input sample_data --output output
```

Add `-v` for debug logging.

## Outputs

**`risk_metrics_report.xlsx`**
- `Summary` sheet — headline counts, breakdown by subdomain, top breach reasons
- `Flagged Metrics` sheet — one row per Amber/Red/worsening metric, colour-coded by status
- `Raw Extracted` sheet — every metric extracted, with each month's cell coloured by its status. Use this sheet to verify extraction against source files.

**`risk_metrics_summary.pptx`**
- Headline slide with breach counts
- One slide for Red breaches (if any)
- One slide for Amber breaches (if any)
- Top root-cause themes slide

## How it handles the four table types

Tables are identified by matching the heading text immediately above them against the four known labels. The matching is case- and whitespace-insensitive, and "Previous Breached KCI" is checked before "Breached KCI" so it doesn't match prematurely. In XLSX, where tables don't have an implicit "above" heading, the scanner looks for any cell matching a table-type label and takes the block of rows below it.

## Extending

**New threshold formats.** Edit `parse_threshold()` in `models.py`. The current implementation finds `green <op> <num>` and `red <op> <num>` anywhere in the string; direction (higher-is-worse vs lower-is-worse) is inferred from the operators. If your team uses "R" / "A" / "G" instead of full names, or uses numeric bands without labels, add patterns there.

**New column aliases.** Edit `_HEADER_ALIASES` in `normalizer.py` if your actual files use different column names (e.g. "KCI Identifier" instead of "ID").

**New month label formats.** Edit `parse_month_label()` in `models.py`. It currently handles `December'25`, `Jan-26`, `Feb 2026`, etc.

**PDF extraction quirks.** `pdfplumber` occasionally splits wide cells' text across adjacent cells or merges cell contents. When extraction is wrong, first look at the `Raw Extracted` sheet to see what came through. Tune `find_tables()` settings in `extractors/pdf_extractor.py` — pdfplumber takes keyword args like `vertical_strategy`, `horizontal_strategy`, `snap_tolerance` that often fix table-detection issues.

## Architecture

```
analyze.py                  CLI, file walking, dispatch
├── extractors/
│   ├── pptx_extractor.py   python-pptx: slide → tables
│   ├── pdf_extractor.py    pdfplumber: page → tables
│   └── xlsx_extractor.py   openpyxl: sheet → tables
├── normalizer.py           Raw table → MetricRow (header mapping, row parsing)
├── models.py               Dataclasses, threshold parser, month parser
└── report.py               MetricRow list → Excel + PPTX
```

The format-specific extractors are responsible only for **finding tables and identifying their type**. All downstream logic (header detection, threshold parsing, classification, trend analysis, reporting) is shared. Adding a new input format (e.g. DOCX) means writing one new extractor and nothing else.
