#!/usr/bin/env python3
"""One Line of Earned Pride.

Writes a single quiet, earned moment of pride — one line of text,
1 to 240 characters — to /output/entry.txt.
"""

import os

LINE = "After eleven failed batches, old Pak Darman lifted the first loaf that rose and pressed it to his ear, as if it were breathing."


def main():
    if not 1 <= len(LINE) <= 240:
        raise SystemExit("entry line must be 1 to 240 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
