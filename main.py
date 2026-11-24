"""One Line of Earned Pride — entry program.

Writes a single line (1-240 chars) to /output/entry.txt: a quiet,
earned moment of pride for someone in a scene.
"""
import os

ENTRY = (
    "He spent eleven years fixing other people's roofs; today his son "
    "handed him the keys to a house with his name on the deed, and he "
    "just stood there, holding them like they might disappear."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
