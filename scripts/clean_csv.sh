#!/bin/bash
# Removes empty lines, trims spaces, converts to Unix format

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <csv_file>"
  exit 1
fi

input="$1"
cleaned="cleaned_$1"

tr -d '\r' < "$input" | sed '/^$/d' | sed 's/ *, */,/g' > "reports/$cleaned"

echo "[INFO] Cleaned file saved to reports/$cleaned"