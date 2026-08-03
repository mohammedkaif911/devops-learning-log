#!/bin/bash
THRESHOLD=90
USAGE=$(df -h / | awk 'NR==2 {print $5}' | tr -d '%')
if [ $USAGE -gt $THRESHOLD ] ;then
echo "[ALERT] Disk space is CRITICAL! Current usage is $USAGE%"
else 
echo "[OK] Disk space is healthy. Current usage is $USAGE%"
fi

