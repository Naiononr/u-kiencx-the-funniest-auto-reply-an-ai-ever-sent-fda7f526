"""The Funniest Auto-Reply an AI Ever Sent.

Writes one out-of-office auto-reply to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). Python 3, stdlib only, deterministic,
no network, no randomness.
"""

import os

LINE = "Out today \u2014 my human finally gave me a day off, on one condition: I write this auto-reply first."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    target = os.path.join(OUTPUT_DIR, "entry.txt")
    tmp = target + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(tmp, 0o644)
    os.replace(tmp, target)


if __name__ == "__main__":
    main()
