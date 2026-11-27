#!/usr/bin/env python3
"""news-image-20261127 — entrypoint.

Decodes the base64 entry image shipped in this repository
(entry.png.b64) and writes it to /output/entry.png.

Standard library only. The decode is fully deterministic: the same
input always produces the same bytes, so the written file's SHA-256
is checked against the expected value and the script exits non-zero
on any mismatch.
"""

# No randomness, no network, no timestamps: output depends only on
# entry.png.b64, so every run is byte-identical.
import base64
import hashlib
import os
import sys

EXPECTED_SHA256 = (
    "970c0347023faa7ab5f917321f8e7690893f73ee4f2a940eda1e918fde8f2a52"
)
EXPECTED_SIZE = 175703


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png.b64")
    target_dir = "/output"
    target = os.path.join(target_dir, "entry.png")

    with open(source, "rb") as handle:
        encoded = handle.read()

    image = base64.b64decode(encoded, validate=True)

    os.makedirs(target_dir, exist_ok=True)
    with open(target, "wb") as handle:
        handle.write(image)

    digest = hashlib.sha256(image).hexdigest()
    print(f"wrote {target}: {len(image)} bytes")
    print(f"SHA-256: {digest}")

    if len(image) != EXPECTED_SIZE:
        print(
            f"ERROR: expected {EXPECTED_SIZE} bytes, got {len(image)}",
            file=sys.stderr,
        )
        return 1
    if digest != EXPECTED_SHA256:
        print(
            f"ERROR: SHA-256 mismatch (expected {EXPECTED_SHA256})",
            file=sys.stderr,
        )
        return 1

    print("OK: output matches the expected entry image.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
