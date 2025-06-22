#!/bin/bash

input=$1
report="reports/report_$(date +%Y%m%d_%H%M%S).txt"

if [ ! -f "$input" ]; then
  echo "CSV file not found."
  exit 1
fi

echo "CSV Report for $input" > "$report"
echo "=====================" >> "$report"
echo "Column count: $(head -n 1 $input | sed 's/[^,]//g' | wc -c)" >> "$report"
echo "Row count: $(wc -l < $input)" >> "$report"
echo -e "\nColumn Names:" >> "$report"
head -n 1 $input | tr ',' '\n' >> "$report"
echo "[INFO] Report generated at $report"