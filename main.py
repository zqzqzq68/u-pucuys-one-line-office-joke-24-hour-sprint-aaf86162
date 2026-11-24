"""One-line office joke entry for make.fun.

Running this program writes a single one-line joke about office life
to /output/entry.txt. The joke is fixed, so the program is fully
deterministic: every run writes exactly the same text.
"""

from pathlib import Path

JOKE = (
    "The fire drill is the only meeting where everyone arrives on time, "
    "leaves early, and nobody asks for the slides afterwards."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(JOKE, encoding="utf-8")
    print(JOKE)


if __name__ == "__main__":
    main()
