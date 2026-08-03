#!/bin/bash
if pgrep -x "nginx" >/dev/null; then
echo "[INFO] Nginx web daemon is active and healthy."
else
echo "[ALERT] Nginx is OFFLINE! Launching automated self-healing..."
if sudo systemctl start nginx; then
echo "[SUCCESS] Self-healing complete. Nginx service restarted."
else
echo "[CRITICAL] Self-healing FAILED! Check Nginx configuration or system logs."
fi
fi