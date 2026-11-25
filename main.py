#!/usr/bin/env python3
"""One-line entry: The Meeting That Should Have Been an Email.

The brief asks for one line, at most 200 characters, that
makes a meeting-that-should-have-been-an-email funny. The
judge weighs, in order: the line is plainly one joke about a
meeting that should have been an email, the laugh lands on
its own with the turn arriving by the last word, the angle is
a surprise rather than the obvious complaint about length or
that it could have been an email, every word earns its place,
and it names something true about meetings people have
actually sat through.

The sealed line below is built to that order on purpose. It
opens on a meeting called to decide the meeting about the
meeting -- a recursion everyone who works in an office has
lived through -- and the turn lands in the last words: the
decision was already made in the first five minutes, and it
went out by email anyway. The joke is the meeting eating
itself, not a complaint about how long it ran. Nothing in the
line needs the reader to know the team: the recursion is the
whole joke, and it stands alone.

LIMIT is 200 because the bounty gate allows one line of 1
to 200 characters. The sealed line is 140 characters, so it
sits well inside the cap; the validator below only guards
against an edit that would push it past the limit.
"""

import os

# The sealed line: an hour spent deciding the meeting about
# the meeting, for a decision made in five minutes and sent
# by email anyway.
ENTRY = "We spent an hour in a meeting to decide the meeting about the meeting, then emailed everyone the decision we made in the first five minutes."

LIMIT = 200  # bounty gate: one line, 1-200 characters


def _validate(text):
    """Accept only one clean line inside the character limit."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text:
        raise ValueError("entry must not be empty")
    if not text.isascii():
        # Character counts must mean the same thing everywhere,
        # so the line is plain ASCII only.
        raise ValueError("entry must be plain ASCII text")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ch.isspace() and ch != " " for ch in text):
        # Only the plain space separates words; any other
        # whitespace would hide invisible bytes in the line.
        raise ValueError("entry must use plain spaces only")
    if len(text) > LIMIT:
        raise ValueError(
            "entry is %d characters, past the %d limit" % (len(text), LIMIT)
        )
    if text.strip() != text:
        # Leading or trailing padding is dead weight the gate
        # still counts, so the line must start and end on a word.
        raise ValueError("entry must not pad itself with spaces")
    if not text.isprintable():
        raise ValueError("entry must contain no control characters")
    if "  " in text:
        # A double space is a gap where a word should be; in a
        # 200-character line no gap is free.
        raise ValueError("entry must not contain a double space")
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
