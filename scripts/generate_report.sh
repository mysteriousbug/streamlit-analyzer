#!/bin/bash

INPUT_FILE="$1"
REPORT_FILE="reports/report_$(date +%s).txt"

echo "Report for $INPUT_FILE" > "$REPORT_FILE"
echo "----------------------" >> "$REPORT_FILE"
head -n 1 "$INPUT_FILE" >> "$REPORT_FILE"
echo "Total Rows: $(wc -l < $INPUT_FILE)" >> "$REPORT_FILE"

echo "Report saved to $REPORT_FILE"
#xxx333
