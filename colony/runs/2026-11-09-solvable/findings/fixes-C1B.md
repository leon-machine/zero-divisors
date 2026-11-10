# Fixes C1B, run 2026-11-09-solvable

Proposal: synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height (R1 section 2, SOUND WITH FIXES).
All edits in place in proposals/synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height/; every stored file kept.

1. Inputs K1-K3 (referee: import as Facts). FIXROUND override 1 applies, so nothing is imported. The formal level now
   opens with "Given the classical facts (L1) to (L3), cited from memory and not in the store: ...". (L1) is the
   lambda-operations, (L2) the K-ring of L^{2n+1}(4), (L3) Sq^1 = 0 on Z_4-liftable classes. Clause (2) cites (L2), and
   the closing line now says every clause is conditional on (L1) to (L3). The proof maps (K1)-(K3) to (L1)-(L3).
   Technical, one-liner, check docstring and coverage say the same. The extraction note says deriving them in the store
   is an open item. outside_ga kind changed from imported to other, with its why reworded to match.
2. Threshold sentence. Formal (4) and proof (4) now speak only of the walls built here, L^{4r-1}(4) x R with r >= 2
   and indefinite side (4r-1, 1). The technical level says that what this result adds is unboundedness, and that
   complex K is silent on L^5(4). The extraction note names the sibling synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial
   as the intended citation, because a proposal cannot cite a proposal (override 3). That sibling shows the failure
   starts in dimension five.
3. Definite side k = e(L). This is now proved in one line, in formal (3) and in proof (4): N(Gbar) = 0, so the
   parent's clause (1) gives L + N = R^k and hence k >= e. The parent's clause (2) gives k <= e.
4. Side type. Formal (3) and proof (4) now state that the indefinite side built here is (2n+1, 1), with one negative
   direction, not the physical type (1, q). They also state that the obstruction holds on every side, including type
   (1, 2n+1). The extraction note says the sibling builds (1, 2n+1) walls for every n.

Not changed: the exact-order range stays n <= 8. That is what the check computes; the referee's independent Smith-form
recomputation up to n = 12 agrees with it.

runcheck: `PYTHONDONTWRITEBYTECODE=1 python3 colony/runcheck.py proposals/synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height/check.py`
gives PASS on all four functions. The check's computations did not change; only the docstring wording did.
check4: pending (orchestrator).
