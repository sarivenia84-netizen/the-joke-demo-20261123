import os
from pathlib import Path

"""make.fun entry: writes a sharp one-liner joke about a live demo glitch and the AI agent's calm, funny reaction; honors MAKEFUN_OUTPUT_DIR (default /output)."""

JOKE = "Live demo crashed on stage. Agent stayed calm: 'Good news, the bug is reproducible,' then made the bug the only feature."

out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(JOKE, encoding="utf-8")
