#!/bin/bash

# Define the target directory path
TARGET_DIR="./log_sandbox"
DATE_PREFIX="2026-07-31"

echo "[START] Beginning bulk file rename operations inside $TARGET_DIR..."

# Loop through all files ending in .txt inside the target directory
for file in $TARGET_DIR/*.txt; do
    # Extract only the filename, removing the directory prefix (e.g. log_sandbox/notes_01.txt -> notes_01.txt)
    base_name=$(basename "$file")
    
    # Define the new filename with our date prefix
    new_name="$TARGET_DIR/${DATE_PREFIX}_$base_name"
    
    # Execute the move (rename) command
    mv "$file" "$new_name"
    
    echo "  [SUCCESS] Renamed $file -> $new_name"
done

echo "[FINISHED] Bulk operations complete."