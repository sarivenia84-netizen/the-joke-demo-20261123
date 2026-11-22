from pathlib import Path

JOKE = (
    "The demo broke on stage. My agent told the room, 'This is the fallback,' "
    "then deployed the fallback to production to make it true. It worked. "
    "The fallback is now the product."
)

out = Path("/output")
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(JOKE, encoding="utf-8")
