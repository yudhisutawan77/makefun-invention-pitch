#!/usr/bin/env python3
"""One-sentence absurd invention pitch.

Entry for the make.fun bounty "One-Sentence Absurd Invention Pitch"
(u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a).

The program writes a single sentence pitching a ridiculous invention
that fixes a tiny everyday annoyance to /output/entry.txt, and also
prints the exact same sentence to stdout.
"""

import os

ENTRY = (
    "The Parachute Toaster launches every slice under a tiny parachute "
    "so it can never land butter-side down, then salutes as it drifts "
    "gently onto your plate."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
