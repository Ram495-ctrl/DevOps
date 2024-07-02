import os
import shutil
import sys
import datetime

def backup_files(source_dir, dest_dir):
    # Check if the source directory exists

    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return
    
    # Check if the destination directory exists
    if not os.path.exists(dest_dir):
        print(f"Destination directory '{dest_dir}' does not exist.")
        return

    # Get the list of files in the source directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_file = os.path.join(root, file)
            dest_file = os.path.join(dest_dir, file)

            # Check if the destination file already exists
            if os.path.exists(dest_file):
                # Append a timestamp to the file name
                timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                file_name, file_extension = os.path.splitext(file)
                dest_file = os.path.join(dest_dir, f"{file_name}_{timestamp}{file_extension}")

            # Copy the file
            try:
                shutil.copy2(source_file, dest_file)
                print(f"Copied '{source_file}' to '{dest_file}'")
            except Exception as e:
                print(f"Failed to copy '{source_file}' to '{dest_file}': {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
    else:
        source_dir = sys.argv[1]
        dest_dir = sys.argv[2]
        backup_files(source_dir, dest_dir)

########python backup.py /path/to/source_directory /path/to/destination_directory
