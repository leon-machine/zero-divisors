# Fixes A, run 2026-11-09-three (referee R1, verdicts SOUND WITH FIXES on both proposals)

Edited in place in proposals/<id>/ (entity.md, proof-main.tex, check.py, coverage.yaml). Only runcheck was run.

## synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure
runcheck: 7/7 pass (one check function added).
- A1 applied. The false parenthetical in proof (3) is removed. The correct identity (g (x) g - 1) T = N (x) 1 - 1 (x) N
  is displayed, and the check asserts that the filed form (with N (x) g - 1 (x) N) is false for group order above 2.
- A2 applied. Proof (3) now says there are exactly four parity cases and displays the four identities in Z[G x G],
  with a three-line argument for general order. New check function check_four_group_ring_identities verifies them
  for orders 2, 3, 4, 5, 6, 8; the k <= 9 run is kept as a control. entity.md checked_by and coverage.yaml updated.
- A3 applied. One-liner opens "Given standard cellular cohomology and obstruction theory (stated background)"; lay
  has the sentence on the assumed textbook machinery; one-liner says "the Bockstein of Z2 -> Z4 -> Z2 vanishes".
- A4 applied. (G) now lists the algebraic Kuenneth theorem and naturality of the cup product under cellular
  inclusions; clause (6) and proof (6) say the reduced group is F^2 and F^{2n+2} = 0.
- A5 applied. Clause (3) has "(up to the sign convention of the cup product)"; the proof notes the Koszul value -6.
- A6 applied. (K1) renamed (AH) at every level and in the proof; the extraction note's parenthesis rewritten as the
  referee words it. (AH) and q1 stay in-statement hypotheses, as "This run" directs.
- A7 applied. Extraction note: Atiyah's section number marked not verified; Kobayashi and Sugawara added for order
  four (year and pages not verified); Mahammed for general order; Kambe marked as odd primes to the referee's
  knowledge. All still from memory.
- A8 applied. Orders computed and stated for n <= 14 (check extended; values 32, 32, 64, 64, 128, 128 for n = 9..14
  continue 2^{floor((n+1)/2)}).
Added per override 1: the note says (G), (AH), the spin class and the lambda-operations are hypotheses and that
deriving them is an open item.

## synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional
runcheck: 5/5 pass. Run time of the whole check is now about 45 s (the grid takes about 40 s); the mutation test
will multiply the grid's time by up to eight, so check4 may take five to six minutes. Nothing was reduced.
- B1 applied in full. Part (b) of check_odd_parity_linearised_ricci is the 144-case grid: six jet monomials for h0
  and six for h1, data (S, S') = (1, 0) and (0, 1), three polar angles (cot = 4/3, 12/5, -8/15), L = 7/2 and 6, as
  identities of rational functions of sqrt f; every component compared including the vanishing ones; 84 nonzero
  components pinned. The generic-jet points and the two identities in tan(theta/2) are kept as controls. Proof (1)
  has the degree-bound paragraph (degree at most one in L; sin(theta) times each coefficient a polynomial of degree
  at most two in cot(theta), by the phi-rescaling homogeneity and derivative order two) and the homogeneity in M.
  Clause (1) relabelled "proved, given the degree bound (argued) and the homogeneity in M"; "It is not established as
  a single identity" and the "generic ... for all such functions" phrase are deleted in favour of "on a basis".
  Extraction note and technical level follow.
- B2 applied. "Three values of L decide every L" is gone; the proof says two values of L at each angle.
- B3 applied, with a shorter title than the referee's: the suggested title is over the 90-character limit (E124).
  Title now: "Odd-parity gravity channels, l >= 2, are 2D at the static-frame horizon; even one way" (85 characters).
  Lay has the static-observer sentence.
- B4 not applied by me (ids are not renamed in this round, per "This run"); the extraction note says the id names
  the field as a whole, the title carries the scope, and renaming is left to the maintainer.
- B5 applied by adding one sentence in clause (4): W and lambda here are not the W = sqrt f / r and the sphere
  eigenvalue of the lower-spin theorem. The symbols were not renamed.
- B6 applied. coverage.yaml: the function is kind exact, now with the grid as its first clause and the degree bound
  listed under omits as the proof's.
- B7 applied. Extraction note adds Glampedakis, Johnson and Kennefick (Phys. Rev. D 96, 024036, 2017) and
  Chandrasekhar (1984) as prior art for clause (4), and cites Doran and Lasenby sections 13.4 to 13.6 for the
  setting with chapter 14 for applications.
- B8 no change required (optional strengthening not done: the even-parity span test over Q(sqrt f) would be about
  forty times the cost of one grid row).
Added per override 1: the note says (C1) to (C3) stay hypotheses of the statement and deriving them is an open item.
Also: clause (5) now reads "given (C1), (C2) and (1)".

## Rebuttals
None.

## Not verified by me
The degree bound of B1 is the referee's argument, written out in the proof and labelled argued; I did not test it
beyond the two tan(theta/2) identities, which are consistent with it. The referee's joint symbolic metric
computation is the independent confirmation of clause (1); it is outside GA and not part of the proposal.

check4: pending (orchestrator)
