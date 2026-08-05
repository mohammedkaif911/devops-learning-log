import os
import shutil
from datetime import datetime

# 1. Refactored Bulk Renamer using *args for flexible file lists
def bulk_rename(date_prefix, *files):
    print(f"[START] Renaming files with prefix: {date_prefix}...")
    success_count = 0
    
    for f in files:
        if os.path.exists(f):
            dir_name = os.path.dirname(f)
            base_name = os.path.basename(f)
            new_name = os.path.join(dir_name, f"{date_prefix}_{base_name}")
            
            # Execute rename
            os.rename(f, new_name)
            print(f"  [SUCCESS] Renamed: {f} -> {new_name}")
            success_count += 1
        else:
            print(f"  [WARNING] File missing: {f}")
            
    print(f"[FINISHED] Bulk operations complete. {success_count} files renamed.\n")

# 2. Refactored Backup Utility using shutil and datetime
def backup_directory(source_dir, backup_parent="./backups"):
    # Security Check: Verify source directory exists
    if not os.path.exists(source_dir):
        print("ERROR: source directory not found!.")
        return False
        
    # Generate dynamic timestamp using datetime
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    dest_dir = os.path.join(backup_parent, f"backup_{timestamp}")
    
    try:
        # Create backups folder and copy recursively
        shutil.copytree(source_dir, dest_dir)
        print(f"Backup successful! Saved to: {dest_dir}")
        return True
    except (OSError, shutil.Error) as e:
        print(f"failed to copy directory: {e}")
        return False

if __name__ == "__main__":
    # Test backup operation
    # (Create a dummy source folder to test)
    os.makedirs("./test_source", exist_ok=True)
    with open("./test_source/test1.txt", "w") as f:
        f.write("test data 1")
    with open("./test_source/test2.txt", "w") as f:
        f.write("test data 2")
        
    # Run the backup!
    backup_directory("./test_source")
    
    # Find the newly created backup directory dynamically and test bulk_rename using *args!
    backups = sorted([d for d in os.listdir("./backups") if d.startswith("backup_")])
    if backups:
        latest_backup = os.path.join("./backups", backups[-1])
        file1 = os.path.join(latest_backup, "test1.txt")
        file2 = os.path.join(latest_backup, "test2.txt")
        
        # Call the bulk renamer passing file1 and file2 as *args!
        bulk_rename("2026-08-05", file1, file2)