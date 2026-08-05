import os

def bulk_rename(date_prefix, *files):
    # 'files' is a tuple of file paths!
    print(f"[START] Renaming files with prefix: {date_prefix}")
    
    for f in files:
        # Check if the file actually exists on the disk:
        if os.path.exists(f):
            # Your Job: 
            # 1. Extract the folder path of the file: dir_name = os.path.dirname(f)
            dir_name = os.path.dirname(f)
            # 2. Extract the raw filename: base_name = os.path.basename(f)
            base_name = os.path.basename(f)
            # 3. Create the new name path: new_name = os.path.join(dir_name, f"{date_prefix}_{base_name}")
            new_name = os.path.join(dir_name, f"{date_prefix}_{base_name}")
            # 4. Run the rename command: os.rename(f, new_name)
            os.rename(f,new_name)
            # 5. Print a success message!
            print("Name changes succesfully")
        else:
            print(f"[WARNING] File not found: {f}")