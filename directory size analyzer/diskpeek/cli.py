# -------------------------------
# Directory Size Analyzer Script
# Author: @tanvirmahfuz22
# Version: 1.0
# -------------------------------
import os
import sys

RESET = "\033[0m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
skip_dirs = []

def human_readable(size, decimal_places=2):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.{decimal_places}f} {unit}"
        size /= 1024
    return f"{size:.{decimal_places}f} PB"

def get_file_size(filepath):
    try:
        return os.path.getsize(filepath) if os.path.isfile(filepath) else 0
    except (OSError, FileNotFoundError):
        return 0

def print_dir(root, dir_sizes, level=0):

    if any(skip in root.split(os.sep) for skip in skip_dirs):
        return

    indent = "  " * level
    size = dir_sizes.get(root, 0) 
    print(f"{indent}{CYAN}Directory: {root}{RESET} | {YELLOW}Size: {human_readable(size)}{RESET}")

    for f in os.listdir(root):
        fp = os.path.join(root, f)
        if os.path.isfile(fp):
            print(f"{indent}  {GREEN}File: {f}{RESET} | {YELLOW}Size: {human_readable(get_file_size(fp))}{RESET}")
    
    for d in os.listdir(root):
        dp = os.path.join(root, d)
        if os.path.isdir(dp):
            print_dir(dp, dir_sizes, level + 1)

def directory_analyzer(directory=""):
    if directory == "":
        directory = os.getcwd()

    if not os.path.exists(directory):
        print("The directory is invalid")
        return

    dir_sizes = {}  

    for root, dirs, files in os.walk(directory, topdown=False):
        if any(skip in root.split(os.sep) for skip in skip_dirs):
            continue

        files = [f for f in files if all(skip not in root.split(os.sep) for skip in skip_dirs)]

        total = sum(get_file_size(os.path.join(root, f)) for f in files)

        for d in dirs:
            subdir_path = os.path.join(root, d)
            if subdir_path in dir_sizes:
                total += dir_sizes[subdir_path]

        dir_sizes[root] = total

    print_dir(directory,dir_sizes)

def main():
    global skip_dirs
    if len(sys.argv) < 2:
        directory = ""
    else:
        directory = sys.argv[1]
        skip_dirs = sys.argv[2:] if len(sys.argv) > 2 else []

    directory_analyzer(directory)
