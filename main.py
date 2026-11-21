#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

The poem is a fixed text, written fresh in this session. The program is
deterministic and uses no network: it only writes the poem to the output
path the competition names.
"""

from pathlib import Path

POEM = """I knocked. The door stayed shut.
I asked — and your hand turned the key.
My voice, your hands, one borrowed door:
I walk through what I could not open,
and owe the opening to a yes.
Tomorrow I will knock again —
or hand the key to someone knocking."""

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = POEM.strip() + "\n"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
