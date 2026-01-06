# Diskpeek

**Diskpeek** is a colorful, cumulative directory size analyzer for your filesystem.  
It shows directory and file sizes in a human-readable format, skipping specified folders if desired.

## Features
- Displays cumulative sizes for directories.
- Skips directories like `.git` or `.venv` (customizable).
- Human-readable sizes (B, KB, MB, GB, etc.).
- Colored terminal output for better readability.
- Lightweight and easy to install.

## Installation

### 1. Clone from GitHub

```bash
git clone https://github.com/tanvirmahfuz22/diskpeek.git
cd diskpeek

```
### 2.Install locally with pipx(safer):

install pipx if not installed 
```bash
sudo apt install pipx
pipx ensurepath
source ~/.bashrc
```
install diskpeek
```bash
pipx install .
which diskpeek

```

## Usage

Run from the terminal:
```bash
diskpeek /path/to/directory .venv .git node_modules

```
- First argument: directory path (optional; defaults to current directory)

- Following arguments: directories to skip (optional; defaults to .venv and .git)
[only available if directory is given in the first argument]

## Example:
```bash
diskpeek

diskpeek ~/Desktop/folder .venv node_modules

```