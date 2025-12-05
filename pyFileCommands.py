import subprocess
import os
import datetime
import shutil
import argparse

def run_cmd(cmd,capture=True):
    return subprocess.run(cmd, shell=True, capture_output=capture,text=True)

def check_venv():
    return (hasattr(os,"environ") and (os.environ.get("VIRTUAL_ENV") or os.environ.get("CONDA_DEFAULT_ENV")))

def freeze_to_file(filename):
    run_cmd(f'pip freeze > {filename}',capture=False)

def parse_requirements(filename, only_packages=False, only_versions= False):
    with open(filename,"r") as f:
        lines = f.read().splitlines()

    parsed = []
    for line in lines:
        if "==" in line:
            pkg,ver = line.split("==")
            if only_packages and only_versions:
                parsed.append(f"{pkg} : {ver}")
            elif (only_packages):
                parsed.append(pkg)
            elif only_versions:
                parsed.append(ver)
            else:
                parsed.append(line)
    return parsed

def main():
    parser = argparse.ArgumentParser(description="Advanced pip freeze tool")
    parser.add_argument("--save", action="store_true", help="Save pip freeze to requirements.txt")
    parser.add_argument("--timestamp", action="store_true", help="Save freeze output to timestamped file")
    parser.add_argument("--backup", action="store_true", help="Backup requirements.txt before saving")
    parser.add_argument("--list", action="store_true", help="List files in current directory")
    parser.add_argument("--packages", action="store_true", help="Print only package names")
    parser.add_argument("--versions", action="store_true", help="Print only versions")
    args = parser.parse_args()

    if not check_venv():
        print("⚠️  Not inside a virtual environment! Freeze might include global packages.")
        print("Continue anyway...\n")

    if args.list:
        files = run_cmd("ls")
        print(files.stdout)

    filename = "requirements.txt"
    if args.backup and os.path.exists(filename):
        shutil.copy(filename, "requirements_backup.txt")
        print("📦 Backup created: requirements_backup.txt")
    
    if args.timestamp:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"requirements_{timestamp}.txt"

    if args.save or args.timestamp:
        print(f"📌 Saving pip freeze to {filename}")
        freeze_to_file(filename)

    if args.packages or args.versions:
        if not os.path.exists("requirements.txt"):
            print("❌ requirements.txt not found!")
        else:
            parsed = parse_requirements("requirements.txt",
                                        only_packages=args.packages,
                                        only_versions=args.versions)
            print("\n".join(parsed))

if __name__ == "__main__":
    main()