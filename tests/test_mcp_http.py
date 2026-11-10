"""The HTTP endpoint answers MCP messages, read-only (tp/mcp_http.py)."""
import json
import os
import shutil
import tempfile
import threading
import unittest
import urllib.error
import urllib.request

from tests.fixture_store import build
from tp import mcp_http


class McpHttp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.mkdtemp()
        root = build(os.path.join(cls.tmp, "store"))
        cls.srv = mcp_http.serve(root, "127.0.0.1", 0)
        cls.url = f"http://127.0.0.1:{cls.srv.server_address[1]}"
        threading.Thread(target=cls.srv.serve_forever, daemon=True).start()

    @classmethod
    def tearDownClass(cls):
        cls.srv.shutdown()
        cls.srv.server_close()
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def post(self, msg):
        req = urllib.request.Request(self.url + "/mcp", data=json.dumps(msg).encode(),
                                     headers={"Content-Type": "application/json",
                                              "Accept": "application/json, text/event-stream"})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                body = r.read()
                return r.status, (json.loads(body) if body else None)
        except urllib.error.HTTPError as e:
            return e.code, None

    def test_handshake_and_read_only_tools(self):
        code, r = self.post({"jsonrpc": "2.0", "id": 1, "method": "initialize",
                             "params": {"protocolVersion": "2025-06-18", "capabilities": {}}})
        self.assertEqual(code, 200)
        self.assertEqual(r["result"]["serverInfo"]["name"], "physics-graph")
        code, r = self.post({"jsonrpc": "2.0", "method": "notifications/initialized"})
        self.assertEqual((code, r), (202, None))
        code, r = self.post({"jsonrpc": "2.0", "id": 2, "method": "tools/list"})
        names = {t["name"] for t in r["result"]["tools"]}
        self.assertIn("get_claim", names)
        self.assertFalse(names & {"validate_draft", "generate_doc", "regenerate_doc", "propose_claim"})
        code, r = self.post({"jsonrpc": "2.0", "id": 3, "method": "tools/call",
                             "params": {"name": "search_claims", "arguments": {"query": "boost bivector"}}})
        self.assertEqual(json.loads(r["result"]["content"][0]["text"])[0]["id"], "fx.boost.sigma")
        code, r = self.post({"jsonrpc": "2.0", "id": 4, "method": "tools/call",
                             "params": {"name": "generate_doc", "arguments": {"recipe_yaml": "doc: x"}}})
        self.assertTrue(r["result"]["isError"])

    def test_other_routes(self):
        with urllib.request.urlopen(self.url + "/health", timeout=10) as r:
            self.assertEqual(r.read(), b"ok")
        with urllib.request.urlopen(self.url + "/", timeout=10) as r:
            self.assertIn(b"conventions", r.read())
        with self.assertRaises(urllib.error.HTTPError) as cm:
            urllib.request.urlopen(self.url + "/mcp", timeout=10)
        self.assertEqual(cm.exception.code, 405)
        req = urllib.request.Request(self.url + "/mcp", data=b"{not json",
                                     headers={"Content-Type": "application/json"})
        with self.assertRaises(urllib.error.HTTPError) as cm:
            urllib.request.urlopen(req, timeout=10)
        self.assertEqual(cm.exception.code, 400)


if __name__ == "__main__":
    unittest.main()
