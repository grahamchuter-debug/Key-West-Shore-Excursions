#!/usr/bin/env python3
"""Download hero and content images from Unsplash (Unsplash License)."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMAGES = ROOT / "images"

CUSTOM_IMAGES: frozenset[str] = frozenset({
    "hero-key-west.png",  # site-provided Duval Street hero
    "key-west-intro.png",  # site-provided Southernmost Point
    "southernmost-point.png",
    "duval-street.png",
    "conch-train.png",
    "key-west-sunset-sailing.png",
    "key-west-cruise-port.png",
})

DOWNLOADS: list[tuple[str, str, int]] = [
    ("best-key-west-excursions.png", "Q0HR_nrDkB8", 1920),
    ("one-day-key-west.png", "vYXrNeIpm3w", 1920),
    ("walk-from-port.png", "PsgyWVeJjOA", 1920),
    ("hemingway-house.png", "WOyBhxyB8KI", 1920),
    ("conch-train.png", "PsgyWVeJjOA", 1920),
    ("key-west-trolley.png", "PsgyWVeJjOA", 1920),
    ("key-west-snorkelling.png", "uTgKYNhuKOk", 1920),
    ("key-west-dolphin.png", "BUIEgc7J0eo", 1920),
    ("key-west-sunset-sailing.png", "YZ8Jc6TiH2A", 1920),
    ("dry-tortugas.png", "vYXrNeIpm3w", 1920),
    ("key-west-family.png", "PsgyWVeJjOA", 1920),
    ("key-west-faq.png", "Q0HR_nrDkB8", 1920),
    ("key-west-intro.png", "vYXrNeIpm3w", 1920),
]


def download(filename: str, slug: str, width: int) -> bool:
    dest = IMAGES / filename
    url = f"https://unsplash.com/photos/{slug}/download?force=true&w={width}"
    print(f"  {filename} <- {slug}")
    result = subprocess.run(
        ["curl", "-fsSL", "-o", str(dest), url],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"    FAILED: {result.stderr.strip()}", file=sys.stderr)
        return False
    size = dest.stat().st_size
    if size < 10_000:
        print(f"    WARNING: small file ({size} bytes)", file=sys.stderr)
    print(f"    OK ({size // 1024} KB)")
    return True


def main() -> None:
    IMAGES.mkdir(parents=True, exist_ok=True)
    print("Downloading Key West images from Unsplash…")
    if CUSTOM_IMAGES:
        print(f"  Skipping custom (add your own): {', '.join(sorted(CUSTOM_IMAGES))}")
    failed = 0
    for filename, slug, width in DOWNLOADS:
        if filename in CUSTOM_IMAGES:
            continue
        if not download(filename, slug, width):
            failed += 1
    if failed:
        raise SystemExit(f"{failed} download(s) failed.")
    print("Done.")


if __name__ == "__main__":
    main()
