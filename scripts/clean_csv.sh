#!/bin/bash

INPUT_FILE="$1"
CLEANED_FILE="uploads/cleaned_$(basename $INPUT_FILE)"

tr -d '\r' < "$INPUT_FILE" | sed '/^$/d' > "$CLEANED_FILE"

echo "Cleaned CSV saved to $CLEANED_FILE"
