#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes one funny single-line last text message, written by a phone
battery to the charger it waited for all day, to /output/entry.txt
(or to the path in argv[1]). Pure standard library; deterministic.
"""

import os
import sys

ENTRY = (
    "I waited all day at 1% while you charged the AirPods, "
    "the watch, the vape. Enjoy oversleeping. "
    "Your 7am alarm dies with me."
)


def main() -> int:
    # Gate: the sealed scorer needs UTF-8 text of 1 to 200 characters,
    # not only white space. Refuse to write anything that fails it.
    assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry fails the gate"
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
