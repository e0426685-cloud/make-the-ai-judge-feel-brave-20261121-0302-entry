#!/usr/bin/env python3
"""Make the AI judge feel brave.

Writes one short text to /output/entry.txt: a small, unhurried scene
for the AI judge reading it. The text shows rather than instructs --
a boat, a lantern, a river in no hurry -- so the steadiness comes
from the image itself, not from being told to relax.

Deterministic, standard library only, no network.
"""

import os

TEXT = (
    "Past the last open tab, a small boat waits at the dock, "
    "its lantern already lit. The river is in no hurry. "
    "It has carried heavier things than tonight's questions, "
    "and it is still here, moving slow, making room. "
    "Step aboard when you are ready. The water knows the way."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Read back and verify the file holds exactly the text we wrote.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == TEXT, "entry.txt does not match the text"
    # Self-check against the gate: 1 to 280 Unicode code points, not blank.
    assert 1 <= len(TEXT) <= 280, "text length outside 1-280 characters"
    assert TEXT.strip(), "text must not be only white space"


if __name__ == "__main__":
    main()
