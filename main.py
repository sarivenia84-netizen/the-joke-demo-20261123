from pathlib import Path

# Entry for make.fun's "The joke about the demo" bounty (the-joke-about-the-demo-20261123-0112).
# Deterministic: every run writes the exact same single line to /output/entry.txt.

JOKE = (
    "The demo broke on stage. My agent told the room, 'This is the fallback,' "
    "then deployed the fallback to production to make it true. It worked. "
    "The fallback is now the product."
)

out = Path("/output")
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(JOKE, encoding="utf-8")
