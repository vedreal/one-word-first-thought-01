"""One Word, First Thought — make.fun entry.

The bounty asks for exactly one word: the first word that comes to mind.
This program writes that single word to /output/entry.txt.

The chosen word is "Lethologica" — the name for the tip-of-the-tongue
state, the moment you cannot retrieve the word you want. It is the
contest's own premise turned into a punchline: asked for the first word
that comes to mind, the entry answers with the word for not being able
to think of the word. From Greek lethe (forgetfulness, oblivion) +
logos (word); earliest known reference in Dorland's Illustrated Medical
Dictionary, 1914. Surprising, vivid (everyone knows the feeling), and
carrying a spark of wit that rewards a second look.
"""

import os

# The entry: exactly one word, 11 characters, UTF-8.
WORD = "Lethologica"


def output_path() -> str:
    """Return the directory the entry file is written to."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate_entry(path: str) -> None:
    """Self-check the written entry against the bounty gate.

    The gate: /output/entry.txt must be UTF-8 text of 1 to 24
    characters, not only white space, and exactly one word.
    Raises ValueError if any condition fails.
    """
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    if not text or text.isspace():
        raise ValueError("entry is empty or only whitespace")
    if not 1 <= len(text) <= 24:
        raise ValueError(f"entry is {len(text)} characters, gate allows 1-24")
    if len(text.split()) != 1:
        raise ValueError("entry must be exactly one word")


def write_entry() -> str:
    """Write the word to entry.txt and return the path written."""
    path = os.path.join(output_path(), "entry.txt")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    return path


if __name__ == "__main__":
    written = write_entry()
    validate_entry(written)
    print(f"Wrote {WORD!r} to {written} ({len(WORD)} characters)")
