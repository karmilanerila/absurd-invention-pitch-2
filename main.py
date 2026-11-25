"""One-Sentence Absurd Invention Pitch.

Writes a single absurd-invention pitch to /output/entry.txt.
Stdlib only. No network, no temp files.
"""

import os


PITCH = (
    "The CrumbCourt 9000 hauls every toast crumb before a tiny tribunal "
    "and sentences the guiltiest crumb to sweep the counter clean "
    "before breakfast is allowed to begin."
)

MAX_CHARS = 220


def check_single_sentence(text):
    """One clean sentence: no newline, exactly one terminal full stop."""
    if "\n" in text or "\r" in text:
        raise SystemExit("pitch must be a single line")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("pitch must be exactly one sentence")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = PITCH.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit("pitch must be 1 to 220 characters, got %d" % len(text))
    check_single_sentence(text)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(text.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
