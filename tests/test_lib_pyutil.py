"""lib/pyutil.py: get_or_set behaves as dict.setdefault."""
import os
import sys
import unittest

LIB = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "lib")
if LIB not in sys.path:
    sys.path.insert(0, LIB)

import pyutil  # noqa: E402


class GetOrSet(unittest.TestCase):
    def test_matches_setdefault(self):
        a, b = {}, {}
        for k, v in [(1, []), (1, ["x"]), ((2, 3), set()), ("s", 0), (1, None)]:
            self.assertEqual(pyutil.get_or_set(a, k, v), b.setdefault(k, v))
        self.assertEqual(a, b)
        self.assertEqual(sorted(map(str, a)), sorted(map(str, b)))

    def test_returns_the_stored_object(self):
        d = {}
        pyutil.get_or_set(d, 7, []).append(1)
        pyutil.get_or_set(d, 7, []).append(2)
        self.assertEqual(d, {7: [1, 2]})
        self.assertIs(type(next(iter(d))), int)


if __name__ == "__main__":
    unittest.main()
