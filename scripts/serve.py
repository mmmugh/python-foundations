"""Serve the built site, with content types a phone will believe.

    python3 scripts/serve.py [port]

python3 -m http.server sends plain text as "text/plain" with no charset, which
leaves the browser to guess the encoding. On a phone that guess is often
Latin-1, and a UTF-8 em dash arrives as "a-EUR-". The quizzes are written in
pure ASCII so this cannot bite them, but saying the charset costs one line and
means the next file added does not have to be.
"""

import http.server
import sys
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent / "site"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8731


class Handler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        ".txt": "text/plain; charset=utf-8",
        ".html": "text/html; charset=utf-8",
        ".css": "text/css; charset=utf-8",
        ".js": "text/javascript; charset=utf-8",
        ".mjs": "text/javascript; charset=utf-8",
        ".py": "text/plain; charset=utf-8",
        ".wasm": "application/wasm",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(SITE), **kwargs)

    def log_message(self, fmt, *args):
        pass                      # one line per asset is noise, not information


if not SITE.exists():
    sys.exit("site/ does not exist yet — run: python3 build.py --check")

# Threaded, not the plain TCPServer this used to be: that serves one request
# at a time, so a single reader on a slow link stalls everyone else for as long
# as their copy of the 9.6 MB runtime takes. Measured before the change: one
# client that stopped reading blocked every other request until it went away.
http.server.ThreadingHTTPServer.allow_reuse_address = True
with http.server.ThreadingHTTPServer(("", PORT), Handler) as server:
    print(f"serving {SITE} on http://localhost:{PORT}/  (ctrl-c to stop)")
    server.serve_forever()
