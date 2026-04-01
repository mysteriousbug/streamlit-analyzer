#!/usr/bin/env python3
"""
Identify applications with similar parameter values but different risk ratings (GRAM).
Detects anomalies where comparable applications have inconsistent risk classifications.
"""

import pandas as pd
import sys
from itertools import combinations
from typing import List, Dict, Tuple


def load_data(filepath: str) -> pd.DataFrame:
    """Load Excel file and return DataFrame."""
    try:
        df = pd.read_excel(filepath)
        return df
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)


def calculate_similarity(row1: pd.Series, row2: pd.Series, 
                        param_cols: List[str], tolerances: Dict[str, float]) -> Tuple[float, List[str]]:
    """
    Calculate similarity score between two rows based on parameter columns.
    Returns: (similarity_score: 0-100, matching_params: list of parameter names that match)
    """
    matching = []
    matching_count = 0
    
    for col in param_cols:
        val1, val2 = row1[col], row2[col]
        
        # Skip NaN values
        if pd.isna(val1) or pd.isna(val2):
            continue
        
        # String columns - exact match
        if col in ['Business Criticality', 'IBS', 'Network Access Controls (NAC) Impact']:
            if val1 == val2:
                matching.append(col)
                matching_count += 1
        
        # Numeric columns - within tolerance
        else:
            val1_num = float(val1)
            val2_num = float(val2)
            tolerance = tolerances.get(col, 0)
            
            if abs(val1_num - val2_num) <= tolerance:
                matching.append(col)
                matching_count += 1
    
    similarity_score = (matching_count / len(param_cols)) * 100
    return similarity_score, matching


def find_anomalies(df: pd.DataFrame, min_similarity: float = 75.0) -> pd.DataFrame:
    """
    Find applications with similar parameters but different risk ratings.
    
    Args:
        df: Input DataFrame
        min_similarity: Minimum similarity threshold (0-100)
    
    Returns:
        DataFrame with anomalies found
    """
    
    param_cols = [
        'Business Criticality',
        'Security BIA',
        'IBS',
        'Obsolete Hardware up until 2025',
        'Obsolete OS up until 2025',
        'Obsolete Software up until 2025',
        'Security Vulnerability Exception Count',
        'Network Access Controls (NAC) Impact',
        'Malware Controls Count- Unsupported'
    ]
    
    # Tolerances for numeric columns (how much variance is acceptable)
    tolerances = {
        'Security BIA': 0,  # Exact match
        'Obsolete Hardware up until 2025': 50,
        'Obsolete OS up until 2025': 50,
        'Obsolete Software up until 2025': 25,
        'Security Vulnerability Exception Count': 500,
        'Malware Controls Count- Unsupported': 10
    }
    
    # Verify required columns exist
    required_cols = param_cols + ['Current Residual Risk Rating (GRAM) - O&T']
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        print(f"Error: Missing required columns: {missing}")
        print(f"Available columns: {list(df.columns)}")
        sys.exit(1)
    
    anomalies = []
    
    # Compare all pairs of rows
    for idx1, idx2 in combinations(range(len(df)), 2):
        row1 = df.iloc[idx1]
        row2 = df.iloc[idx2]
        
        similarity_score, matching_params = calculate_similarity(
            row1, row2, param_cols, tolerances
        )
        
        # Check if similar enough and risk ratings are different
        if similarity_score >= min_similarity:
            risk1 = row1['Current Residual Risk Rating (GRAM) - O&T']
            risk2 = row2['Current Residual Risk Rating (GRAM) - O&T']
            
            if risk1 != risk2 and pd.notna(risk1) and pd.notna(risk2):
                # Get app identifiers (assumes first column is app name/id)
                app1 = row1.iloc[0] if 'Application' in df.columns else f"Row {idx1+2}"
                app2 = row2.iloc[0] if 'Application' in df.columns else f"Row {idx2+2}"
                
                anomalies.append({
                    'Application 1': app1,
                    'Application 2': app2,
                    'Similarity Score (%)': round(similarity_score, 2),
                    'Matching Parameters': '; '.join(matching_params),
                    'Risk Rating 1': risk1,
                    'Risk Rating 2': risk2,
                    'Row 1': idx1 + 2,
                    'Row 2': idx2 + 2
                })
    
    return pd.DataFrame(anomalies)


def export_results(anomalies_df: pd.DataFrame, output_file: str):
    """Export anomalies to Excel with formatting."""
    if anomalies_df.empty:
        print("No anomalies found. All similar applications have consistent risk ratings.")
        return
    
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        anomalies_df.to_excel(writer, index=False, sheet_name='Anomalies')
        
        workbook = writer.book
        worksheet = writer.sheets['Anomalies']
        
        # Auto-adjust column widths
        for column in worksheet.columns:
            max_length = 0
            column_letter = column[0].column_letter
            for cell in column:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            adjusted_width = min(max_length + 2, 50)
            worksheet.column_dimensions[column_letter].width = adjusted_width
        
        # Freeze header row
        worksheet.freeze_panes = 'A2'
    
    print(f"\nResults exported to: {output_file}")
    print(f"Found {len(anomalies_df)} anomalies")


def main():
    if len(sys.argv) < 2:
        print("Usage: python risk_rating_anomalies.py <input_file.xlsx> [output_file.xlsx] [min_similarity]")
        print("\nExample:")
        print("  python risk_rating_anomalies.py applications.xlsx anomalies.xlsx 75")
        print("\nArguments:")
        print("  input_file.xlsx   : Excel file with application data")
        print("  output_file.xlsx  : Output file (default: anomalies_output.xlsx)")
        print("  min_similarity    : Minimum similarity threshold 0-100 (default: 75)")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'anomalies_output.xlsx'
    min_similarity = float(sys.argv[3]) if len(sys.argv) > 3 else 75.0
    
    print(f"Loading data from: {input_file}")
    df = load_data(input_file)
    
    print(f"Analyzing {len(df)} applications...")
    print(f"Similarity threshold: {min_similarity}%")
    
    anomalies_df = find_anomalies(df, min_similarity=min_similarity)
    
    if not anomalies_df.empty:
        anomalies_df = anomalies_df.sort_values('Similarity Score (%)', ascending=False)
        print(f"\nFound {len(anomalies_df)} anomalies:")
        print(anomalies_df.to_string(index=False))
    
    export_results(anomalies_df, output_file)


if __name__ == '__main__':
    main()
