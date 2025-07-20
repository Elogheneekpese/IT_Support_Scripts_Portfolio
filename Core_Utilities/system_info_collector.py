import platform
import psutil # This is a special tool we need to install!
import datetime

def get_system_info():
    print("\n--- Gathering System Information ---")

    # 1. Operating System Info (Like knowing if it's Windows 10, macOS Ventura, etc.)
    print(f"Operating System: {platform.system()} {platform.release()} ({platform.version()})")
    print(f"Machine Type: {platform.machine()}") # 64-bit, etc.
    print(f"Hostname: {platform.node()}") # The computer's name on the network

    # 2. CPU Info (The computer's brain)
    # psutil.cpu_count(logical=False) tells you how many physical "brains" it has
    print(f"\nCPU Cores (Physical): {psutil.cpu_count(logical=False)}")
    # psutil.cpu_count(logical=True) tells you how many "thinking paths" it has (threads)
    print(f"CPU Cores (Logical/Threads): {psutil.cpu_count(logical=True)}")
    # psutil.cpu_percent() tells you how busy the brain is right now (in percentage)
    print(f"Current CPU Usage: {psutil.cpu_percent()}%")

    # 3. RAM Info (The computer's short-term memory)
    ram = psutil.virtual_memory()
    # ram.total is the total memory, we convert it from bytes to Gigabytes (GB)
    print(f"\nTotal RAM: {ram.total / (1024**3):.2f} GB")
    # ram.available is how much memory is free
    print(f"Available RAM: {ram.available / (1024**3):.2f} GB")
    # ram.percent is what percentage of memory is being used
    print(f"Used RAM: {ram.percent}%")

    # 4. Disk Info (The computer's long-term storage, like a hard drive or SSD)
    if platform.system() == "Windows":
        disk_path = "C:" # On Windows, your main drive is usually C:
    else: # On Linux or macOS, the main drive is usually called '/' (root)
        disk_path = "/"
    disk = psutil.disk_usage(disk_path)
    print(f"\nDisk ({disk_path}) - Total: {disk.total / (1024**3):.2f} GB")
    print(f"Disk ({disk_path}) - Used: {disk.used / (1024**3):.2f} GB")
    print(f"Disk ({disk_path}) - Free: {disk.free / (1024**3):.2f} GB")
    print(f"Disk ({disk_path}) - Used Percent: {disk.percent}%")

    # 5. Last Boot Time (When the computer was last turned on)
    boot_time_seconds = psutil.boot_time() # This gives you a weird number (seconds since a long time ago)
    # We use datetime to turn that weird number into a human-readable date and time
    print(f"\nLast Boot Time: {datetime.datetime.fromtimestamp(boot_time_seconds).strftime('%Y-%m-%d %H:%M:%S')}")

    print("\n--- End of System Information ---")

# This line makes sure the 'get_system_info()' function runs when you type 'python system_info_collector.py'
if __name__ == "__main__":
    get_system_info()