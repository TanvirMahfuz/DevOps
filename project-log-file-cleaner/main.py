import os
import shutil
from datetime import datetime, timedelta

def clean_logs(log_directory, backup_directory="backup_logs", days_old=7):
    """
    Copies all .log files to a backup directory and deletes logs older than X days.
    """
    
    # Ensure absolute paths
    log_directory = os.path.abspath(log_directory)
    backup_directory = os.path.abspath(backup_directory)

    # Create backup directory if it doesn't exist
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)
        print(f"[+] Created backup directory: {backup_directory}")

    # Time threshold
    cutoff_time = datetime.now() - timedelta(days=days_old)

    # Iterate through files
    for file in os.listdir(log_directory):
        if file.endswith(".log"):
            full_path = os.path.join(log_directory, file)

            # Copy file to backup
            shutil.copy2(full_path, backup_directory)
            print(f"[+] Backed up: {file}")

            # Check if file is older than X days
            modified_time = datetime.fromtimestamp(os.path.getmtime(full_path))
            if modified_time < cutoff_time:
                os.remove(full_path)
                print(f"[-] Deleted old log: {file}")

    print("\n🎉 Done! Backup complete & old logs removed.")


if __name__ == "__main__":
    # Example usage
    # clean_logs(log_directory="./logs", backup_directory="./backup_logs", days_old=7)
    file = open("requirements.txt",'w')
    file.close()
