#!/usr/bin/env python3
"""
create_data_dirs.py

Creates a ../data directory with subdirectories:
  - raw
  - intermediate
  - models
when run from the scripts/ directory.
"""

from pathlib import Path


def create_dirs():
    # Resolve the path to this script, then get its parent folder (scripts/)
    script_path = Path(__file__).resolve()
    script_dir = script_path.parent

    # Define the data directory as ../data relative to scripts/
    data_dir = (script_dir / ".." / "data").resolve()

    # Create the data directory if it doesn't exist
    data_dir.mkdir(parents=True, exist_ok=True)

    # Subdirectories to create under data/
    subdirs = ["raw", "intermediate", "models"]

    for sub in subdirs:
        dir_path = data_dir / sub
        dir_path.mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    create_dirs()