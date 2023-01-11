#!/usr/bin/python3
# 0-read_file.py
# @sayuki2117
"""Text file-reading function defined."""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
