"""Sharing: plain text for link previews, and the per-result share pages (built only with a public address)."""
import os
import tempfile
import unittest

from tp import site


class ShareTest(unittest.TestCase):
    def test_plain_tex(self):
        self.assertEqual(site._plain_tex(r"null vector of $\Cl(p,q)$, $\frac{1}{2} \neq \infty$"),
                         "null vector of Cl(p,q), 1/2 ≠ ∞")

    def test_site_url(self):
        self.assertEqual(site._site_url({}), "")
        self.assertEqual(site._site_url({"site_url": "https://a.org"}), "https://a.org/")

    def test_share_pages(self):
        nodes = [{"id": "a.b", "title": "A result", "one_liner": r"$v^2 = 0$ for $v \neq 0$", "kind": "claim"},
                 {"id": "note.x", "title": "A note", "kind": "note"}]
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(site._share_pages(d, nodes, ""), 0)
            self.assertFalse(os.path.exists(os.path.join(d, "r")))
            self.assertEqual(site._share_pages(d, nodes, "https://a.org/"), 1)
            page = open(os.path.join(d, "r", "a.b.html"), encoding="utf-8").read()
            self.assertIn('og:title" content="A result"', page)
            self.assertIn("v^2 = 0 for v ≠ 0", page)
            self.assertIn("https://a.org/#a.b", page)
            self.assertIn("https://a.org/img/share.jpg", page)
            site._share_pages(d, nodes, "")
            self.assertFalse(os.path.exists(os.path.join(d, "r")))


if __name__ == "__main__":
    unittest.main()
