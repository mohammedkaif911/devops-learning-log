#!/bin/bash

# 1. Parameter Validation: Ensure the user passed the folder to backup as an argument
if [ $# -lt 1 ]; then
    echo "Error: Missing source directory parameter."
    echo "Usage: $0 [directory_to_backup]"
    exit 1
fi

# 2. Assign variables
SOURCE_DIR=$1
BACKUP_PARENT="./backups"

# 3. Check if the source directory actually exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory '$SOURCE_DIR' does not exist!"
    exit 1
fi

# 4. Generate a unique timestamp (Year-Month-Day_Hour-Minute-Second)
TIMESTAMP=$(date +%Y-%m-%d_%H-%M-%S)

# Define our unique target backup directory
DEST_DIR="$BACKUP_PARENT/backup_$TIMESTAMP"

echo "[START] Initiating secure backup of '$SOURCE_DIR' to '$DEST_DIR'..."

# 5. Create the backups directory structure
mkdir -p "$DEST_DIR"

# 6. Execute recursive copy operation
cp -r "$SOURCE_DIR"/* "$DEST_DIR/"

echo "[SUCCESS] Backup complete. Archive saved at: $DEST_DIR"