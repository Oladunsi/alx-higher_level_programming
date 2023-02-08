#!/usr/bin/python3

# 1-write_file.py
# Oke Oladunsi Samuel 
"""Defines a text file line-counting function."""


def write_file(filename="", words=""):
    """Return the number of lines in a text file."""
    letters = len(words)
    with open(filename, "w+", encoding="utf-8") as f:
        f.write(words)
        f.close()
    return letters
