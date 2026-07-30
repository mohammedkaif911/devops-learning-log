import os

def check_disk_space():
    # os.statvfs gets statistics for the root '/' filesystem
    st = os.statvfs('/')
    # Calculate free space in Gigabytes
    free_gb = (st.f_bavail * st.f_frsize) / (1024**3)
    return free_gb

def check_ram_usage():
    # Read the Linux kernel's virtual memory file directly
    with open('/proc/meminfo', 'r') as f:
        lines = f.readlines()
    
    # Extract Total and Free memory in Kilobytes
    mem_total = int(lines[0].split()[1])
    mem_free = int(lines[1].split()[1])
    
    # Calculate active RAM usage percentage
    used_percent = ((mem_total - mem_free) / mem_total) * 100
    return used_percent

def check_cpu_load():
    # Read the Linux kernel's system load averages
    with open('/proc/loadavg', 'r') as f:
        load = f.read().split()[0]
    return float(load)

def run_system_audit():
    print("=========================================")
    print("★ SRE ACTIVE SYSTEM AUDIT & DIAGNOSTICS ★")
    print("=========================================\n")
    
    # 1. Audit Disk
    free_disk = check_disk_space()
    print(f"[DISK] Available Storage: {free_disk:.2f} GB")
    if free_disk < 10.0:
        print("  ⚠️ ALERT: Root storage is below 10GB safety threshold!")
    else:
        print("  ✓ Storage health: OK")
        
    # 2. Audit RAM
    ram_usage = check_ram_usage()
    print(f"[RAM] Active Memory Usage: {ram_usage:.2f}%")
    if ram_usage > 90.0:
        print("  ⚠️ ALERT: System RAM usage is critically high!")
    else:
        print("  ✓ Memory health: OK")
        
    # 3. Audit CPU
    cpu_load = check_cpu_load()
    print(f"[CPU] Active System Load (1-min avg): {cpu_load}")
    if cpu_load > 4.0:
        print("  ⚠️ ALERT: CPU queue is experiencing high contention!")
    else:
        print("  ✓ CPU health: OK")
        
    print("\n=========================================")

if __name__ == "__main__":
    run_system_audit()