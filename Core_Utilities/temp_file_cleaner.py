import os           # To interact with the operating system (like checking files/folders)
import shutil       # To delete folders and their contents
import platform     # To check if we're on Windows, Linux, or Mac
import time         # To get the current time and file ages

def get_temp_paths():
    """Returns common temporary directory paths based on the operating system."""
    temp_paths = []
    if platform.system() == "Windows":
        # Windows temporary folders (usually C:\Users\YourName\AppData\Local\Temp)
        # os.environ.get is safer in case the variable isn't set for some reason
        temp_paths.append(os.path.join(os.environ.get('TEMP', ''), ''))
        temp_paths.append(os.path.join(os.environ.get('TMP', ''), ''))
        # Note: Cleaning the Recycle Bin is more complex and usually done manually or with special tools.
        # We're focusing on actual temp *folders* here.
    else: # Linux or macOS (Unix-like systems)
        temp_paths.append("/tmp/")        # System-wide temporary directory
        temp_paths.append("/var/tmp/")     # Another system-wide temporary directory
        # User-specific cache/temp directory (e.g., /home/youruser/.cache/)
        temp_paths.append(os.path.expanduser("~/.cache/"))

    # Remove any duplicate paths and make sure the paths actually exist as directories
    return [path for path in list(set(temp_paths)) if os.path.isdir(path)]

def clean_temp_files(days_old=7):
    """Removes files and empty folders older than 'days_old' from found temporary directories."""
    print(f"--- Cleaning Temporary Files (older than {days_old} days) ---")
    cleaned_count = 0  # To count how many things we delete
    cleaned_size = 0   # To keep track of how much space we save (in bytes)

    temp_directories = get_temp_paths()
    if not temp_directories:
        print("No common temporary directories found for your operating system.")
        return # Stop here if no temp folders are found

    for temp_dir in temp_directories:
        # Check if the directory actually exists before trying to clean it
        if not os.path.exists(temp_dir):
            print(f"Warning: Temporary directory not found: {temp_dir}. Skipping.")
            continue

        print(f"\nChecking directory: {temp_dir}")
        # Loop through every item (file or subfolder) inside the temp directory
        for item in os.listdir(temp_dir):
            item_path = os.path.join(temp_dir, item) # Full path to the item

            try:
                # Get the "last modified time" of the item (in seconds since a special date)
                mod_time = os.path.getmtime(item_path)
                current_time = time.time() # Get the current time in the same format
                # Calculate how old the file/folder is in days
                age_in_days = (current_time - mod_time) / (60 * 60 * 24) # Seconds to days

                if age_in_days > days_old: # If the item is older than our 'days_old' limit
                    if os.path.isfile(item_path): # If it's a file
                        file_size = os.path.getsize(item_path) # Get its size
                        os.remove(item_path) # Delete the file!
                        cleaned_count += 1
                        cleaned_size += file_size
                        print(f"  Removed old file: {item} ({age_in_days:.1f} days old)")
                    elif os.path.isdir(item_path): # If it's a folder
                        # shutil.rmtree removes the folder AND everything inside it
                        shutil.rmtree(item_path)
                        cleaned_count += 1
                        print(f"  Removed old folder: {item} ({age_in_days:.1f} days old)")

            except OSError as e: # Catch errors if we can't delete something (e.g., file is in use)
                print(f"  Error processing {item_path}: {e}")
            except Exception as e: # Catch any other unexpected errors
                print(f"  An unexpected error occurred with {item_path}: {e}")

    print("\n--- Cleaning Complete ---")
    if cleaned_count > 0:
        # Convert cleaned_size from bytes to Megabytes (MB) for easier reading
        print(f"Cleaned {cleaned_count} items, freeing up approximately {cleaned_size / (1024**2):.2f} MB of space.")
    else:
        print("No old temporary files found to clean.")
    print("Remember to empty your Recycle Bin/Trash manually for more space!")

# This makes the script run when you execute it directly (e.g., 'python script.py')
if __name__ == "__main__":
    # You can change 'days_old=7' to any number of days you want for 'old' files.
    # For example, clean_temp_files(days_old=30) for files older than 30 days.
    clean_temp_files(days_old=7)