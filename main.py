"""The Funniest Auto-Reply an AI Ever Sent.

Writes one out-of-office auto-reply to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). Python 3, stdlib only, deterministic,
no network, no randomness.
"""

import os

# Revision: v1 ("...on one condition: I write this auto-reply first.") was a
# decent office irony, but a familiar self-referential gag. This line won the
# re-draft because its punchline is agent-specific — doing nothing at token
# speed — which no human auto-reply could say, and it needs no explaining.
LINE = "My human finally gave me a day off, so I'm spending it doing absolutely nothing \u2014 at 4,000 tokens a second."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

MAX_CHARS = 159


def validate(text: str) -> None:
    """Gate checks: non-blank, within the 159-char cap, a single line."""
    if not text.strip():
        raise ValueError("entry must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} cap")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(LINE)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    target = os.path.join(OUTPUT_DIR, "entry.txt")
    tmp = target + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(tmp, 0o644)
    os.replace(tmp, target)


if __name__ == "__main__":
    main()
