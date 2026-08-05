import os
import shutil
from datetime import datetime
def backup_directory(source_dir, backup_parent="./backups"):
    if not os.path.exists(source_dir):
        print("ERROR: source directory not found!.")
        return False
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    dest_dir = os.path.join(backup_parent,f"backup_{timestamp}")
    try:
        shutil.copytree(source_dir,dest_dir)
        print(f"Backup successful! Saved to: {dest_dir}")
        return True
    except(OSError,shutil.Error) as e:
        print(f"failed to copy directory: {e}")
        return False
