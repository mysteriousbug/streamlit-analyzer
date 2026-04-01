# Risk Rating Anomalies Detection Script

## Overview
This Python script identifies applications that have **similar/identical parameter values** but **different risk ratings (GRAM)**, flagging potential inconsistencies in risk assessment.

## Features
- **Similarity scoring** across 9 parameters with configurable tolerances
- **Smart comparison logic**: Exact matches for categorical fields, tolerance-based for numeric
- **Configurable thresholds**: Adjust minimum similarity % and numeric tolerances
- **Detailed output**: Shows matching parameters and risk rating differences
- **Excel export**: Results formatted with auto-sized columns and frozen headers

## Parameters Analyzed
1. Business Criticality (1-5 scale, categorical)
2. Security BIA (1-5 scale)
3. IBS (Yes/No)
4. Obsolete Hardware up until 2025 (0-3000)
5. Obsolete OS up until 2025 (0-2000)
6. Obsolete Software up until 2025 (0-1000)
7. Security Vulnerability Exception Count (0-50000)
8. Network Access Controls (NAC) Impact (Yes/No)
9. Malware Controls Count - Unsupported (0-200)

**Risk Rating Column**: Current Residual Risk Rating (GRAM) - O&T

## Installation
```bash
pip install pandas openpyxl
```

## Usage

### Basic Usage
```bash
python risk_rating_anomalies.py applications.xlsx
```
Creates: `anomalies_output.xlsx` with minimum 75% similarity threshold

### Custom Output File
```bash
python risk_rating_anomalies.py applications.xlsx my_anomalies.xlsx
```

### Custom Similarity Threshold
```bash
python risk_rating_anomalies.py applications.xlsx anomalies.xlsx 80
```
Sets minimum similarity to 80%

## How It Works

### Similarity Calculation
- **Categorical fields** (Business Criticality, IBS, NAC Impact): Must match exactly
- **Numeric fields**: Match if within configured tolerance
- **Score**: (Matching parameters / Total parameters) × 100

### Default Tolerances
| Parameter | Tolerance |
|-----------|-----------|
| Security BIA | 0 (exact) |
| Obsolete Hardware | ±50 |
| Obsolete OS | ±50 |
| Obsolete Software | ±25 |
| Security Vulnerabilities | ±500 |
| Malware Controls | ±10 |

### Anomaly Detection
Pairs are flagged if:
1. Similarity score ≥ threshold (default 75%)
2. Different risk ratings
3. No missing values in either row

## Output Format

| Column | Description |
|--------|-------------|
| Application 1 | Name/ID of first app |
| Application 2 | Name/ID of second app |
| Similarity Score (%) | How similar the parameters are |
| Matching Parameters | Which parameters matched |
| Risk Rating 1 | GRAM rating for first app |
| Risk Rating 2 | GRAM rating for second app |
| Row 1 | Excel row number for first app |
| Row 2 | Excel row number for second app |

Results are sorted by similarity score (highest first).

## Customization

Edit the `find_anomalies()` function to adjust:

**Tolerances** (lines 74-82):
```python
tolerances = {
    'Security BIA': 0,
    'Obsolete Hardware up until 2025': 50,  # Change this
    # ...
}
```

**Minimum Similarity** (line 108):
```python
find_anomalies(df, min_similarity=75.0)  # Change threshold
```

## Example Scenario

**Input Data:**
| App | Business Crit | Security BIA | Hardware | GRAM |
|-----|---------------|--------------|----------|------|
| App A | 4-High | 4 | 150 | 1A |
| App B | 4-High | 4 | 155 | 2B |

**Output:**
- Similarity: 75% (3 matching / 4 key params)
- **Flagged**: Both apps are nearly identical but have different risk ratings (1A vs 2B)
- Action: Review risk assessment methodology

## Error Handling
- Missing columns: Script exits with error listing required columns
- Missing data: Rows with NaN values are skipped in comparison
- File not found: Clear error message with path

## Performance
- Compares all pairs: O(n²) complexity
- 1000 applications: ~500K comparisons (typically <5 seconds)
- 10000 applications: ~50M comparisons (~2-3 minutes)

For very large datasets (>50K rows), consider:
- Filtering to smaller subsets by business unit
- Increasing min_similarity threshold
- Pre-filtering by risk rating band
