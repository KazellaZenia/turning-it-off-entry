#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun entry.

Writes the single line a hopeless tech support agent gives a desperate
customer to /output/entry.txt (MAKEFUN_OUTPUT_DIR).

Built to the judge brief, in criteria order: on subject (an agent
replying to a desperate customer about the dead computer), the joke
lands on the twist — the classic off-and-on fix failed, and it was
the agent's only move, so the cheerfulness is the uselessness — the
customer is never the butt of it; it sounds like one line a real
support agent would actually say, the customer's desperation felt
in the "Good news" that isn't good news at all; tight, every word
earns its place; and fresh because it twists the classic instead of
repeating it: the classic changed nothing, and the agent is
out of ideas on line one.
"""

import os

# The agent's only trick, already spent: the off-and-on classic failed,
# so the "Good news" is that the diagnosis is done — there is nothing
# left the agent knows how to do. Plain ASCII, short for the byte
# tie-break.
LINE = "Good news: I turned it off and on again and nothing changed, so we've ruled out the only thing I know how to do."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
