"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry is one short rant about the self-checkout machine accusing
# the shopper of stealing his own milk: the joke is the machine treating
# an ordinary shopper like a criminal in front of strangers, escalating
# from a calm report to an indignant denial. Inside the 400-character
# gate, five short sentences, one concrete annoyance, no filler.
# Revision note: re-read the gate after running; entry must stay
# 1-400 characters, UTF-8, not only whitespace, one text, no newline.
import os

TEXT = (
    "The self-checkout machine has accused me of stealing my own milk "
    "three times in one transaction. 'Unexpected item in the bagging "
    "area.' The item is the milk I just scanned. The bagging area is "
    "where the milk goes. I am not a criminal \u2014 I am a man buying "
    "cereal while a robot yells at me in front of strangers."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
