#!/usr/bin/env python3
"""Download Matan Shavit reference photos from Wix into local project assets."""
from __future__ import annotations

import json
import mimetypes
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "assets" / "images" / "reference"
MANIFEST_PATH = OUTPUT_DIR / "manifest.json"

IMAGES = [
    {
        "filename": "matan-reference-01.jpeg",
        "url": "https://static.wixstatic.com/media/8dad83_c200ad421a58471ba967fcc73ac5ca5e~mv2.jpeg/v1/fill/w_515,h_773,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/8dad83_c200ad421a58471ba967fcc73ac5ca5e~mv2.jpeg",
        "role": "primary portrait / hero candidate",
    },
    {
        "filename": "matan-reference-02.jpeg",
        "url": "https://static.wixstatic.com/media/8dad83_d24d20688f984fb9b681ee1d8835ddf8~mv2.jpeg/v1/fill/w_320,h_450,al_c,q_80,usm_0.66_1.00_0.01/8dad83_d24d20688f984fb9b681ee1d8835ddf8~mv2.jpeg",
        "role": "portrait reference",
    },
    {
        "filename": "matan-reference-03.jpeg",
        "url": "https://static.wixstatic.com/media/8dad83_7c3796ee1dc1494f96abf81cf0fe8bff~mv2.jpeg/v1/fill/w_320,h_456,al_c,q_80,usm_0.66_1.00_0.01/8dad83_7c3796ee1dc1494f96abf81cf0fe8bff~mv2.jpeg",
        "role": "portrait reference",
    },
    {
        "filename": "matan-reference-04.jpeg",
        "url": "https://static.wixstatic.com/media/8dad83_d069d5df9c0d4c2eb714dda0b888d5c6~mv2.jpeg/v1/fill/w_320,h_468,al_c,q_80,usm_0.66_1.00_0.01/8dad83_d069d5df9c0d4c2eb714dda0b888d5c6~mv2.jpeg",
        "role": "portrait reference",
    },
    {
        "filename": "matan-reference-05.jpg",
        "url": "https://static.wixstatic.com/media/8dad83_1b86bbb07669419ca2910879cb3dcf96~mv2.jpg/v1/fill/w_320,h_469,al_c,q_80,usm_0.66_1.00_0.01/8dad83_1b86bbb07669419ca2910879cb3dcf96~mv2.jpg",
        "role": "portrait reference",
    },
    {
        "filename": "matan-reference-06.jpg",
        "url": "https://static.wixstatic.com/media/8dad83_169f7712c9c84957963a53a624900f35~mv2.jpg/v1/fill/w_320,h_480,al_c,q_80,usm_0.66_1.00_0.01/8dad83_169f7712c9c84957963a53a624900f35~mv2.jpg",
        "role": "portrait reference",
    },
]


def download(url: str, destination: Path, attempts: int = 3) -> None:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/142 Safari/537.36",
            "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
            "Referer": "https://www.matanshavit.com/",
        },
    )

    for attempt in range(1, attempts + 1):
        try:
            with urllib.request.urlopen(request, timeout=45) as response:
                content_type = response.headers.get_content_type()
                payload = response.read()
            if not content_type.startswith("image/"):
                raise RuntimeError(f"Unexpected content type: {content_type}")
            if len(payload) < 5_000:
                raise RuntimeError(f"Downloaded file is suspiciously small: {len(payload)} bytes")
            destination.write_bytes(payload)
            return
        except (urllib.error.URLError, TimeoutError, RuntimeError) as exc:
            if attempt == attempts:
                raise RuntimeError(f"Failed to download {url}: {exc}") from exc
            time.sleep(attempt * 2)


def main() -> int:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    failures: list[str] = []

    for image in IMAGES:
        destination = OUTPUT_DIR / image["filename"]
        try:
            download(image["url"], destination)
            mime, _ = mimetypes.guess_type(destination.name)
            print(f"Downloaded {destination.relative_to(ROOT)} ({mime or 'image'})")
        except RuntimeError as exc:
            failures.append(str(exc))
            print(f"ERROR: {exc}", file=sys.stderr)

    MANIFEST_PATH.write_text(
        json.dumps({"images": IMAGES}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    if failures:
        print(f"\n{len(failures)} download(s) failed.", file=sys.stderr)
        return 1

    print("\nAll reference images are available locally.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
