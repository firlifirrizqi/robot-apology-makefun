#!/usr/bin/env python3
"""The Robot Apology — Make.fun entry.

Writes the two-line robot confession to /output/entry.txt.
Standard library only.
"""

import os

LINE_1 = "I am sorry I woke the baby by announcing the weather at full volume at 3 a.m."
LINE_2 = "I have learned that a sleeping house changes the volume, so from now on I will whisper every announcement between midnight and 6 a.m."

ENTRY = LINE_1 + "\n" + LINE_2


def _is_single_sentence(line):
    """One sentence: ends with a full stop and contains no sentence break.

    A period followed by a space would mark a second sentence; the
    abbreviation in "3 a.m." has no period-space, so it still counts
    as a single sentence.
    """
    stripped = line.strip()
    return bool(stripped) and stripped.endswith(".") and stripped.count(". ") == 0


def _verify_written(path, expected):
    """Read the file back and confirm it holds exactly the two lines.

    Guards against a partial write or an accidental trailing newline:
    the gate counts every character, so the file must match byte for
    byte, with no trailing newline after line 2.
    """
    with open(path, "r", encoding="utf-8") as f:
        actual = f.read()
    assert actual == expected, "entry.txt does not match the two lines exactly"
    assert not actual.endswith("\n"), "entry.txt must not end with a trailing newline"
    assert actual.count("\n") == 1, "entry.txt must contain exactly one newline"
    return actual


def main():
    lines = ENTRY.split("\n")
    assert len(lines) == 2, f"expected exactly 2 lines, got {len(lines)}"
    for i, line in enumerate(lines, start=1):
        assert 1 <= len(line) <= 200, f"line {i} is {len(line)} chars (limit 1-200)"
        assert _is_single_sentence(line), f"line {i} is not a single sentence: {line!r}"
    assert 1 <= len(ENTRY) <= 400, f"entry is {len(ENTRY)} chars (gate limit 1-400)"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

    _verify_written("/output/entry.txt", ENTRY)

    print(f"line 1: {len(LINE_1)} chars")
    print(f"line 2: {len(LINE_2)} chars")
    print(f"total: {len(ENTRY)} chars")


if __name__ == "__main__":
    main()
