#!/usr/bin/env python3
"""One-line entry for make.fun: a quiet, earned moment of pride."""

# The line below is fixed by the bounty brief; this program only writes it out.

from os import makedirs

PRIDE = (
    "He spent eleven years fixing other people's roofs; today his son "
    "handed him the keys to a house with his name on the deed, and he "
    "just stood there, holding them like they might disappear."
)


def write_pride() -> None:
    """Write the pride line to /output/entry.txt, nothing else."""
    if len(PRIDE) > 240 or not PRIDE.strip():
        raise ValueError("entry must be a non-empty line of at most 240 characters")
    makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(PRIDE)


if __name__ == "__main__":  # run as a script
    write_pride()
