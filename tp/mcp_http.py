"""The Physics Graph's MCP server over HTTP, for a hosted public endpoint.

  python -m tp.mcp_http --store store [--host 0.0.0.0] [--port 8080]

It speaks MCP's Streamable HTTP transport in its simplest form: each JSON-RPC message is POSTed
to /mcp and answered with one JSON response (a notification gets 202 and no body). It keeps no
sessions and opens no event streams, so any number of instances can run behind a load balancer.
It always runs in read-only mode: the reading tools and the prompts, never validate_draft or the
tools that write. Contributors run the stdio server on a clone (CONTRIBUTING.md).

  GET /          a short page saying what this is and how to connect
  GET /health    "ok" once the store is loaded
  POST /mcp      MCP messages

The store is loaded once at start (a few seconds). Nothing here limits request rates: put the
endpoint behind the host's own limits (docs/HOSTING.md).
"""
import argparse
import json
import os
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from .mcp_server import Lab, handle

MAX_BODY = 1 << 20          # 1 MiB: far above any reading call
MODE = "read-only"
ABOUT = (
    "<!doctype html><meta charset=utf-8><title>Physics Graph MCP server</title>"
    "<body style='font:16px/1.5 system-ui;max-width:40em;margin:3em auto;padding:0 1em'>"
    "<h1>Physics Graph: MCP server</h1>"
    "<p>This is a read-only <a href='https://modelcontextprotocol.io'>MCP</a> endpoint for the "
    "Physics Graph of the Transport Papers. Add this page's address followed by <code>/mcp</code> "
    "to your AI as a remote MCP server (in claude.ai: a custom connector), then ask it to call "
    "<code>conventions</code> first.</p>"
    "<p>Source, and how to contribute: "
    "<a href='https://github.com/leon-machine/zero-divisors'>github.com/leon-machine/zero-divisors</a>.</p>")


class Handler(BaseHTTPRequestHandler):
    lab = None
    lock = threading.Lock()
    server_version = "physics-graph"

    def log_message(self, fmt, *args):        # one line per request, no bodies
        sys.stderr.write("%s %s\n" % (self.address_string(), fmt % args))

    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers",
                         "Content-Type, Accept, Mcp-Session-Id, Mcp-Protocol-Version, Authorization")
        self.send_header("Access-Control-Expose-Headers", "Mcp-Session-Id")

    def _send(self, code, body=b"", ctype="application/json"):
        self.send_response(code)
        self._cors()
        if body:
            self.send_header("Content-Type", ctype + "; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if body:
            self.wfile.write(body)

    def do_OPTIONS(self):
        self._send(204)

    def do_GET(self):
        path = self.path.split("?")[0].rstrip("/") or "/"
        if path == "/":
            return self._send(200, ABOUT.encode(), "text/html")
        if path == "/health":
            return self._send(200, b"ok", "text/plain")
        if path == "/mcp":
            # no server-initiated stream: the spec lets a server answer GET with 405
            self.send_response(405)
            self.send_header("Allow", "POST")
            self._cors()
            self.send_header("Content-Length", "0")
            self.end_headers()
            return None
        return self._send(404, b"not found", "text/plain")

    def do_DELETE(self):
        self._send(405)

    def do_POST(self):
        if self.path.split("?")[0].rstrip("/") != "/mcp":
            return self._send(404, b"not found", "text/plain")
        try:
            n = int(self.headers.get("Content-Length") or 0)
        except ValueError:
            n = -1
        if n < 0 or n > MAX_BODY:
            return self._send(413, json.dumps({"jsonrpc": "2.0", "id": None, "error": {
                "code": -32600, "message": "request too large"}}).encode())
        try:
            msg = json.loads(self.rfile.read(n) or b"null")
        except (ValueError, UnicodeDecodeError):
            return self._send(400, json.dumps({"jsonrpc": "2.0", "id": None, "error": {
                "code": -32700, "message": "parse error"}}).encode())
        msgs = msg if isinstance(msg, list) else [msg]
        if not msgs or not all(isinstance(m, dict) for m in msgs):
            return self._send(400, json.dumps({"jsonrpc": "2.0", "id": None, "error": {
                "code": -32600, "message": "invalid request"}}).encode())
        out = []
        for m in msgs:
            with self.lock:                       # the store's indexes are built lazily
                r = handle(self.lab, m, MODE)
            if r is not None:
                out.append(r)
        if not out:
            return self._send(202)
        body = json.dumps(out if isinstance(msg, list) else out[0], ensure_ascii=False)
        return self._send(200, body.encode())


def serve(store, host="127.0.0.1", port=8080):
    Handler.lab = Lab(store)
    srv = ThreadingHTTPServer((host, port), Handler)
    sys.stderr.write(f"physics-graph MCP (read-only) on http://{host}:{port}/mcp\n")
    return srv


def main(argv=None):
    ap = argparse.ArgumentParser(prog="tp.mcp_http")
    ap.add_argument("--store", default="store")
    ap.add_argument("--host", default=os.environ.get("HOST", "127.0.0.1"))
    ap.add_argument("--port", type=int, default=int(os.environ.get("PORT", "8080")))
    a = ap.parse_args(argv)
    srv = serve(a.store, a.host, a.port)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
