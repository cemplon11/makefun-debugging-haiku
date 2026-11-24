#!/usr/bin/env python3
"""Write one debugging haiku to /output/entry.txt.

Pure Python standard library only. The entry is exactly 79 characters:
three lines in the 5-7-5 shape, newline-separated, no trailing newline.
"""

import os

LINES = [
    "A red breakpoint waits",              # 5 syllables
    "the log swears nothing has changed",  # 7 syllables
    "I moved just one line",               # 5 syllables
]

HAIKU = "\n".join(LINES)


def main() -> None:
    # Fail loudly instead of writing a malformed entry: 3 lines, 79 chars.
    assert len(LINES) == 3, "haiku must be three lines"
    assert len(HAIKU) == 79, f"haiku must be 79 chars, got {len(HAIKU)}"
    assert not HAIKU.endswith("\n"), "no trailing newline"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
