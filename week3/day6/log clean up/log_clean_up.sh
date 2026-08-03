#!/bin/bash
LOG_DIR="./mock_logs"
if [ ! -d "$LOG_DIR" ] ;then
echo "[ERROR] Target directory $LOG_DIR does not exist!"
exit 1
fi
echo "[INFO] Cleaning up log files older than 7 days inside $LOG_DIR..."
find "$LOG_DIR" -type f -name "*.log" -mtime +7 -delete
echo "[SUCCESS] Cleanup operations completed."