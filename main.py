import os
from pathlib import Path


# Comedic angle: the agent treats a public crash like a routine bug report and hears applause as a passing test.
JOKE = "The live demo crashed on the first click, and the AI coding agent stayed calm: 'Good news, the bug is reproducible.' Then it fixed the bug and logged the applause as a passing test."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(JOKE + "\n", encoding="utf-8")
    print(entry_path)


if __name__ == "__main__":
    main()
