#!/usr/bin/env python3
"""Write the 27 Nov 2026 front-page image (v2) to /output/entry.png.

Reads the base64 PNG stored beside this file (entry.png.b64), decodes
it with the standard library only, and writes the bytes to
/output/entry.png. The program uses no network and is deterministic:
the same input always produces the same bytes. The output is verified
against the expected SHA-256; any mismatch exits non-zero.
"""

import base64
import hashlib
import os
import sys

EXPECTED_SHA256 = "20cf7d20995ee5a71b3893ad07ca6c52f7c6a3bfcea2c87a8bfd301f1c8ca23d"


def decode_entry():
    # Deterministic: no timestamps, no randomness, no network anywhere.
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "entry.png.b64")
    with open(path, "r", encoding="ascii") as fh:
        text = "".join(fh.read().split())
    return base64.b64decode(text)


def main():
    data = decode_entry()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.png", "wb") as fh:
        fh.write(data)
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        print("SHA mismatch: got %s, expected %s" % (digest, EXPECTED_SHA256),
              file=sys.stderr)
        return 1
    print("wrote /output/entry.png (%d bytes, sha256 %s)"
          % (len(data), digest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
