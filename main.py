"""One-line museum placard for an ordinary office artifact.

Writes a single dry curator's label to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when run locally).
"""

import os

ENTRY = (
    "Stapler, c. 1997. Bent steel, one jammed staple. Donated by "
    "Accounts after 28 years of faithful service and a single act "
    "of quiet revenge. Please do not touch. Gallery 3, Shelf B."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
