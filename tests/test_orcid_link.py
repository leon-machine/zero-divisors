"""tp.orcid_link: a contribution's ORCID record must list the pull request's GitHub account.
ORCID itself is not called: a stand-in returns each record's website links."""
import shutil
import unittest

from tests.test_validator import StoreCase, E
from tp import orcid_link as L
from tp.model import load_store, write_lock

ME, CO = "0000-0002-1825-0097", "0000-0001-5109-3700"


class LinksAccount(unittest.TestCase):
    def test_profile_forms(self):
        for u in ("https://github.com/Ada-L", "http://www.github.com/ada-l/", "github.com/ada-l"):
            self.assertTrue(L.links_account([u], "ada-l"), u)

    def test_not_the_profile(self):
        for u in ("https://github.com/ada-l/repo", "https://github.com/ada-lx",
                  "https://gitlab.com/ada-l", "https://example.org/github.com/ada-l"):
            self.assertFalse(L.links_account([u], "ada-l"), u)

    def test_urls_read_from_orcid_json(self):
        doc = {"researcher-url": [{"url-name": "GitHub", "url": {"value": "https://github.com/ada-l"},
                                   "visibility": "public"}], "path": "/x/researcher-urls"}
        self.assertEqual(list(L._urls(doc)), ["https://github.com/ada-l"])


class Check(StoreCase):
    def contribute(self, credit):
        write_lock(load_store(self.root))
        shutil.copytree(self.folder("fx.boost.sigma"), E(self.root, "claims", "fx.boost.sigma-two"))
        self.edit("fx.boost.sigma-two", "id: fx.boost.sigma", "id: fx.boost.sigma-two")
        self.edit("fx.boost.sigma-two", "ai_involved: 'no'\n", "ai_involved: 'no'\ncredit:\n" + credit)

    def run_check(self, records, author="ada-l"):
        def fetch(oid):
            if oid not in records:
                raise OSError(f"ORCID has no public record {oid}")
            return records[oid]
        return [c for c, _, _ in L.check(load_store(self.root), author, fetch)]

    ADA = f"- name: Ada L\n  role: the result\n  orcid: {ME}\n- name: Claude Opus 5.5\n  role: drafting\n"

    def test_linked_passes(self):
        self.contribute(self.ADA)
        self.assertEqual(self.run_check({ME: ["https://github.com/ada-l"]}), [])

    def test_E611_record_does_not_list_the_account(self):
        self.contribute(self.ADA)
        self.assertEqual(self.run_check({ME: ["https://github.com/someone-else"]}), ["E611"])

    def test_E612_orcid_unreachable(self):
        self.contribute(self.ADA)
        self.assertEqual(self.run_check({}), ["E612"])

    def test_W613_unverified_coauthor(self):
        self.contribute(self.ADA + f"- name: Co Author\n  role: a lemma\n  orcid: {CO}\n")
        self.assertEqual(self.run_check({ME: ["https://github.com/ada-l"], CO: []}), ["W613"])

    def test_maintainer_not_checked(self):
        self.contribute(self.ADA)
        self.assertEqual(self.run_check({}, author="leon"), [])

    def test_nothing_new_nothing_checked(self):
        write_lock(load_store(self.root))
        self.assertEqual(self.run_check({}), [])


if __name__ == "__main__":
    unittest.main()
