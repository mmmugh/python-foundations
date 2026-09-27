"""Render the PNG icons from their SVG sources.

    python3 scripts/make_icons.py

The PNGs are committed, so the build never needs this and nothing outside
macOS does either: qlmanage is macOS's Quick Look, and it is the only
rasteriser this project can assume. Run it after editing either SVG.

Two icons, because they are not the same drawing:

    favicon.png          32x32   a fallback for anything that will not take
                                 the SVG
    apple-touch-icon.png 180x180 the iOS home screen, square cornered because
                                 iOS applies its own rounded mask

The output is checked rather than trusted. Quick Look renders an SVG it cannot
parse as its *source text* instead, which produces a perfectly valid PNG of the
wrong thing; that happened here once and a favicon nobody can see is a hard
thing to notice. So each render is decoded and its middle pixel compared to the
color the tile is supposed to be.
"""

import hashlib
import shutil
import struct
import subprocess
import sys
import tempfile
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WEB = ROOT / "web"
STAMP = WEB / "icons.sha256"

TILE = (0x1F, 0x6F, 0x4A)          # --accent, the background of both icons
ICONS = [("favicon.svg", "favicon.png", 32),
         ("apple-touch-icon.svg", "apple-touch-icon.png", 180)]


def decode(path):
    """(width, height, rows) for an 8-bit RGBA PNG. Enough to look at a pixel."""
    data = path.read_bytes()
    pos, idat, w, h = 8, b"", 0, 0
    while pos < len(data):
        length = struct.unpack(">I", data[pos:pos + 4])[0]
        kind, body = data[pos + 4:pos + 8], data[pos + 8:pos + 8 + length]
        if kind == b"IHDR":
            w, h, depth, color = struct.unpack(">IIBB", body[:10])
            if (depth, color) != (8, 6):
                sys.exit(f"{path.name}: expected 8-bit RGBA, got depth {depth} type {color}")
        elif kind == b"IDAT":
            idat += body
        pos += 12 + length

    raw, rows, stride = zlib.decompress(idat), [], w * 4
    prev, at = bytearray(stride), 0
    for _ in range(h):
        kind = raw[at]; at += 1
        line = bytearray(raw[at:at + stride]); at += stride
        for i in range(stride):
            a = line[i - 4] if i >= 4 else 0
            b = prev[i]
            c = prev[i - 4] if i >= 4 else 0
            if kind == 1:   line[i] = (line[i] + a) & 255
            elif kind == 2: line[i] = (line[i] + b) & 255
            elif kind == 3: line[i] = (line[i] + (a + b) // 2) & 255
            elif kind == 4:
                p = a + b - c
                pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                line[i] = (line[i] + (a if pa <= pb and pa <= pc
                                      else b if pb <= pc else c)) & 255
        rows.append(bytes(line)); prev = line
    return w, h, rows


def near(pixel, want, slack=24):
    return all(abs(a - b) <= slack for a, b in zip(pixel, want))


def render(source, target, size):
    if not shutil.which("qlmanage"):
        sys.exit("qlmanage not found: this script only runs on macOS. The PNGs "
                 "are committed, so a build does not need it.")
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(["qlmanage", "-t", "-s", str(size), "-o", tmp, str(WEB / source)],
                       capture_output=True, check=False)
        made = Path(tmp) / f"{source}.png"
        if not made.exists():
            sys.exit(f"qlmanage produced nothing for {source}")
        shutil.copyfile(made, WEB / target)

    width, height, rows = decode(WEB / target)
    if (width, height) != (size, size):
        sys.exit(f"{target}: expected {size}x{size}, got {width}x{height}")

    # A corner inset from the edge: inside the tile for the square icon, and
    # inside the rounded one too. If Quick Look fell back to rendering the SVG
    # as source text this is white, not the tile color.
    x = y = max(2, size // 6)
    at = rows[y][x * 4:x * 4 + 3]
    if not near(tuple(at), TILE):
        sys.exit(f"{target}: pixel ({x},{y}) is rgb{tuple(at)}, expected about "
                 f"rgb{TILE}. Quick Look probably rendered the SVG as text, "
                 f"which means the SVG is not well-formed.")
    print(f"  {target:<22} {size}x{size}  {(WEB / target).stat().st_size:,} bytes")


def main():
    for source, target, size in ICONS:
        render(source, target, size)

    # What the PNGs were made from, so build.py can say when they are stale.
    STAMP.write_text("".join(
        f"{hashlib.sha256((WEB / s).read_bytes()).hexdigest()}  {s}\n"
        for s, _, _ in ICONS))
    print(f"  {STAMP.name:<22} records what these were rendered from")


if __name__ == "__main__":
    main()
