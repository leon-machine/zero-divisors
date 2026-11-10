"""What an outside AI meets: check-one, brief summaries, and the pages that need no JavaScript."""
import io
import os
import shutil
import tempfile
import unittest
from contextlib import redirect_stdout

from tests.fixture_store import build
from tp import checkone, static_pages
from tp.mcp_server import Lab


class AiAccess(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.root = build(os.path.join(self.tmp, "store"))
        open(os.path.join(self.root, "conventions.md"), "w").write("# Conventions\n")
        self.lab = Lab(self.root)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_check_one(self):
        lines = []
        self.assertEqual(checkone.run(self.root, "fx.null.square-zero", out=lines.append), 0)
        self.assertTrue(any(l.strip().startswith("pass") for l in lines), lines)
        self.assertEqual(lines[-1], "all 1 checks passed")
        self.assertEqual(checkone.run(self.root, "fx.nope", out=lines.append), 2)
        got = self.lab.get_claim("fx.null.square-zero")["derived"]["check_command"]
        self.assertEqual(got, "python -m tp check-one fx.null.square-zero --store store")

    def test_brief_summaries(self):
        hit = self.lab.search_claims("boost bivector")[0]
        self.assertEqual(hit["id"], "fx.boost.sigma")
        self.assertNotIn("used_by_ids", hit)
        self.assertNotIn("rests_on_foundation", hit)
        full = self.lab.search_claims("boost bivector", fields=["rests_on"])[0]
        self.assertEqual(set(full), {"id", "rests_on"})

    def test_static_pages(self):
        site = os.path.join(self.tmp, "site")
        os.makedirs(site)
        n = static_pages.write(site, self.lab, "https://example.org/", "https://mcp.example.org/mcp")
        self.assertGreater(n, 3)
        page = open(os.path.join(site, "results", "fx.boost.sigma.html"), encoding="utf-8").read()
        self.assertIn("<h1>", page)
        self.assertIn('href="fx.witt.car.html"', page)          # a premise, as a link
        self.assertIn("check-one fx.boost.sigma", page)
        self.assertIn('rel="canonical" href="https://example.org/results/fx.boost.sigma.html"', page)
        self.assertNotIn("http-equiv=\"refresh\"", page)
        llms = open(os.path.join(site, "llms.txt"), encoding="utf-8").read()
        self.assertTrue(llms.startswith("# Zero Divisors: Physics Graph"))
        self.assertIn("https://mcp.example.org/mcp", llms)
        self.assertIn("subjects/algebra.md", llms)
        self.assertTrue(os.path.exists(os.path.join(site, "subjects", "algebra.md")))
        self.assertIn("example.org/results/fx.boost.sigma.html",
                      open(os.path.join(site, "sitemap.xml"), encoding="utf-8").read())
        # without a public address: relative links, no sitemap
        static_pages.write(site, self.lab, "", "")
        self.assertFalse(os.path.exists(os.path.join(site, "sitemap.xml")))
        self.assertNotIn("canonical", open(os.path.join(site, "results", "fx.boost.sigma.html"),
                                           encoding="utf-8").read())


if __name__ == "__main__":
    unittest.main()
