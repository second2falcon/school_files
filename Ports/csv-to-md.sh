#!/bin/bash

# The input CSV file
csv_file="input.csv"

# The output markdown file
md_file="output.md"

# Remove the output file if it exists
if [ -f "$md_file" ]; then
  rm "$md_file"
fi

# Create the header of the markdown file
echo "| $(head -n 1 "$csv_file" | tr ',' '|') |" > "$md_file"
echo "| --- | --- |" >> "$md_file"

# Loop through the remaining lines of the CSV file and convert each line to a markdown row
tail -n +2 "$csv_file" | while read line; do
  echo "| $(echo "$line" | tr ',' '|') |" >> "$md_file"
done

