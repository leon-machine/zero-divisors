"""Tests for tp/deposits.py: what counts as a change since the deposited version."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tp import deposits as D  # noqa: E402


class FakeBase(D.Baseline):
    def __init__(self, body):           # no file: a deposited body given directly
        self.code, self.entry, self.envs = "T99", {}, {}
        self.body = D.normalise(body)
        self.body_uncited = D.normalise(body, drop_cited=True)


DEPOSIT = r"""
\begin{proposition}[The cones fold]\label{prop:fold}
For $a = e_t + \lambda e_r$ the light cone folds onto $e_r$ (Proposition~\ref{prop:degen}).
\end{proposition}
\begin{table}[htbp]\centering\small
\caption{The ledger.}
\end{table}
"""


class DepositTests(unittest.TestCase):
    def setUp(self):
        self.b = FakeBase(DEPOSIT)

    def test_reference_rewrites_do_not_count(self):
        cur = r"For $a = e_t + \lambda e_r$ the light cone folds onto $e_r$ (Proposition \claimref{x.degeneration})."
        self.assertIs(self.b.contains(cur), True)

    def test_layout_and_float_commands_do_not_count(self):
        self.assertIs(self.b.contains(r"\centering \emph{The ledger.}"), True)

    def test_added_citation_in_parentheses_is_citations_only(self):
        cur = (r"For $a = e_t + \lambda e_r$ (orthogonal vectors anticommute, \claimref{std.anti}) "
               r"the light cone folds onto $e_r$ (Proposition \claimref{x.degeneration}).")
        self.assertEqual(self.b.contains(cur), "cited")

    def test_a_change_of_wording_counts(self):
        cur = r"For $a = e_t + \lambda e_r$ the light cone of the gravitational field folds onto $e_r$."
        self.assertIs(self.b.contains(cur), False)

    def test_a_change_of_mathematics_counts(self):
        cur = r"For $a = e_t - \lambda e_r$ the light cone folds onto $e_r$."
        self.assertIs(self.b.contains(cur), False)

    def test_summary_sentence(self):
        ch = {"version": "1.0", "summary": {"statements": 2, "proofs_only": 1, "revised": 3, "added": 0,
                                            "added_cited": 4, "removed": 0, "citations": 0,
                                            "corrected": 1, "changed": 0, "reworded": 2}}
        self.assertEqual(D.summary_sentence(ch), "Since the deposited version 1.0: 1 result corrected, "
                         "2 reworded (wording, notation or citations only) and 4 cited results added.")
        ch["summary"] = dict.fromkeys(ch["summary"], 0)
        self.assertEqual(D.summary_sentence(ch), "No result differs from the deposited version 1.0.")

    def test_small_or_cited(self):
        dep = r"The pair is null by Proposition~\ref{prop:a}, so $Q(x) = 0$."
        self.assertTrue(D._small_or_cited(dep, r"The pair is null by Proposition \claimref{x.a}, so $Q(x) = 0$."))
        self.assertTrue(D._small_or_cited(dep, r"The pair is null by Proposition \claimref{x.a} (and Lemma "
                                               r"\claimref{x.b}), so $Q(x) = 0$."))
        self.assertFalse(D._small_or_cited(dep, r"The pair is null by Proposition \claimref{x.a}, so $Q(x) = 1$."))
        self.assertFalse(D._small_or_cited(dep, r"The pair is null only on the horizon of the Schwarzschild "
                                                r"field, by Proposition \claimref{x.a}, so $Q(x) = 0$."))

if __name__ == "__main__":
    unittest.main()
