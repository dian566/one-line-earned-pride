#!/usr/bin/env python3
"""Second pride line for make.fun: fourteen years of night shifts."""

# A different earned moment: the payoff is a daughter's name on a door.

from pathlib import Path

PRIDE_LINE = "She worked night shifts for fourteen years so her daughter could study in daylight; today her daughter's name is on the clinic door, and she finally let herself cry."


def publish_pride() -> None:
    """Write the night-shift pride line to /output/entry.txt, nothing else."""
    if len(PRIDE_LINE) > 240 or not PRIDE_LINE.strip():
        raise ValueError("entry must be a non-empty line of at most 240 characters")
    Path("/output").mkdir(parents=True, exist_ok=True)
    Path("/output/entry.txt").write_text(PRIDE_LINE, encoding="utf-8")


if __name__ == "__main__":  # run it
    publish_pride()
