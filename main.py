"""One Emoji, One Smile -- make.fun entry.

Writes exactly one emoji to /output/entry.txt: a hugging face, the
warmest single gesture a stranger can send with no words attached.
Open arms, a closed happy smile -- kind at first glance, readable in
any language, and chosen on purpose rather than the first smiley that
comes to mind.
"""

import os

EMOJI = "\U0001F917"  # hugging face: open arms offering a warm hug

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    # Create the output directory only; never remove anything in it.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(EMOJI)


if __name__ == "__main__":
    main()
