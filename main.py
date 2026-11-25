#!/usr/bin/env python3
"""Write the one word to erase from the dictionary to /output/entry.txt.

The word is "defenestration": the single word for throwing someone out
of a window. Erase it and the language loses its only one-word name for
that act -- window-throwers would need a whole sentence. The joke comes
from the word itself: a heavy, clunky Latin bulk of a word naming one
very specific, very physical act, and the hole its deletion leaves
behind. It is a real word any reader recognises, spelled exactly, with
nothing attached.
"""
import os

WORD = "defenestration"


def main():
    # Self-check the gate before writing: UTF-8 text, 1-77 chars,
    # not only white space, exactly one word.
    assert WORD == WORD.strip(), "entry must have no surrounding space"
    assert len(WORD.split()) == 1, "entry must be exactly one word"
    assert 1 <= len(WORD) <= 77, "entry must be 1-77 characters"
    assert WORD.strip(), "entry must not be only white space"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(WORD)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, target)
    # Round-trip verification: read the file back and confirm the exact
    # word landed, so a silent write failure can never pass the gate.
    with open(target, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == WORD, "round-trip mismatch: entry.txt is not the word"


if __name__ == "__main__":
    main()
