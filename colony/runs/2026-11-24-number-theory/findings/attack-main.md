# Findings, run 2026-11-24-number-theory (single attacker)

Labels: proved / computed / argued / conjectured. Kill conditions are those of RUN.md, registered before computing.

## A. op.positivity-of-values, "more than two modes"

Routes considered. (1) The open problem's own: put any two rational vectors in a four-space similar to the
standard one, then use the stored two-mode theorem pairwise; needs the Hasse-Minkowski import. (2) From the
algebra core: reflections carry coordinate four-spaces to other four-spaces isometrically, so the two-mode
theorem applies on every reflected coordinate four-space; induct on the support of a vector. (3) Own: quaternionic
lines H.alpha in H^m as the family of good four-spaces, closing up under "a quadratic form vanishing on enough
lines is zero".

Choice: (2), after (1) was killed. (3) was abandoned: the known zeros inside a quaternionic line are too thin
to force a quadratic form to vanish at the first step.

- A1 FIRED (proved). The first step is false. In a four-space similar to the standard one two vectors are
  rational quaternions up to scale, so -(u ^ w)^2 = (u.u)(w.w) - (u.w)^2 is a sum of three rational squares;
  for e_1 and e_2+e_3+e_4+2e_5 it is 7, which is not. The obstruction is at the prime 2. (Argued, not filed:
  the condition is also sufficient for n >= 8, by Hasse-Minkowski; triples of vectors fail generically at
  every prime, so no pairwise or triplewise route through such four-spaces can work.)
- A2 did not fire (proved). For r with support S, |S| >= 5, and four indices T in S: take r' in Q^T with
  r'.r' = r.r (four squares), u = r - r', W = -u Q^T u^{-1}. Then r is in W, W carries the standard form, and
  the vectors of W of smaller support fill at least four distinct hyperplanes. A quadratic form vanishing on
  three distinct hyperplanes is zero. Induction on |S| gives linearity for every n >= 4.
- A3 did not fire. The only arithmetic input is Lagrange's theorem, proved in the store in a page (proposal on
  the squares of the even subalgebra of Cl(3,0)). The Hasse-Minkowski import named in the open problem is true
  (every positive definite rational form of dimension >= 4 represents every positive rational: Serre, A Course in
  Arithmetic, ch. IV, from memory) and is not needed.

Proposals: synthesis.additive-weights-on-the-rational-projectors-are-linear-for-every-number-of-modes;
synthesis.positive-rationals-are-the-squares-of-the-even-subalgebra-of-cl-three.
Dependence to keep in view: everything beyond linear algebra is the stored two-mode theorem. Prior art
(Mushtari's Problem G) is unread; no priority claimed.
Next step: n = 3 is untouched (Q^3 has the Godsil-Zaks colouring on unit vectors; on all rational rays the
question is open here). Other ordered fields: over a field with two orderings the squares of the even
subalgebra give the totally positive elements only.

## B. Horizon arrays

- B1 did not fire (proved, signs machine-verified). The thermal test on the ground conic vanishes only at
  twists 1/4, 1/3, 1/2. Short windows by an exponential bound; the rest by integer interval arithmetic with
  first and second derivatives. |T| between the zeros is 1e-4 to 2e-3, which is why a scan could not decide it.
  Proposal: synthesis.thermal-test-on-the-ground-conic-holds-at-exactly-three-points.
- B2 did not fire (proved given classical hypotheses). Character sums over the twist fibres are 2L(0, chi)
  (spectral asymmetries 1 - 2 delta) and -L(-1, chi)/M (sea energies). Cross-checked against class numbers and
  the divisor-sum formula. A dictionary; no constraint. Observation (computed): for chi_D with chi_D(2) = +1
  (D = -7, -15, -23) the fibre sum vanishes, because the fibres have odd numerators only: the fibres see the
  L-function with its factor at 2 removed. Proposal:
  synthesis.character-sums-over-the-twist-fibres-of-an-array-are-dirichlet-l-values.
- B3 FIRED as expected (argued). Invariance of the sea under the whole modular group of the window is generated
  by r -> 1/r (stored: holds at the Hawking point for the antiperiodic array) and the one-window flow (stored:
  the 24 and 12 recurrences). Nothing new follows; nothing filed.
  One remark for op.residue-killing-weights (argued, not filed, a reading): at the Hawking point the partition
  value of n stored arrays is 2^(n/2) (S = (n/2) ln 2 with zero mean energy), rational exactly for even n.
  Under a premise that a registered unit has a rational partition value at the Hawking point, the least unit is
  two arrays. That premise is not stored and would be Leon's to adopt; without it this is a restatement of
  "Z = 2, E = 0, S = ln 2, like a zero-weight mode", which is stored. The same sqrt(2) is the number the stored
  CHSH element needs adjoined to reach its largest value; no connection is claimed.

## C. op.wall-class-invariant

- C1 did not fire (proved). ord(1 - chi^2) = 2^ceil(n/2) in the stored K-ring for every n, because the question
  reduces to divisibility of 2^m by (J - 1)^n in Z[J] and 2 = J (J - 1)^2. The stored bound becomes
  k >= 1 + ceil(n/2) for all n (conditional as before on the lambda-operations). For the 2^a-th turn the order is
  2^ceil(2n/2^a). Proposal: synthesis.order-of-the-doubled-dying-line-on-quarter-turn-lens-walls-is-a-valuation-
  in-the-ring-of-the-quarter-turn.
- C2 FIRED (computed, with a classical formula cited from memory). The reduced spectral asymmetries twisted by
  characters pair to integers with 2^m (chi^2 - 1) exactly from m = ceil(n/2), n <= 8 (work/main/eta_pairing.py):
  a third route to the same order, and no more than complex K-theory. A real refinement needs a spin structure;
  L^5(4) has w_2 != 0. The route to remove q_1 on L^5(4) is closed.
- C3 (prior art). Stolz 1989: the least k with a quarter-turn-odd map S^(2m-1) -> S^(k-1) is m+1 (m = 0, 2 mod 8),
  m+2 (m = 1, 3, 4, 5, 7), m+3 (m = 6). With m = n+1 this is the definite-side rung count of the L^(2n+1)(4)
  walls by the stored reduction. Agrees with the stored 3 (n = 1), 5 (n = 2, derived in the store) and 6 (n = 3).
  Source read: the statement as quoted in arXiv:0903.4462, Example 2.2; Stolz's paper itself not read.

## D. Order and completion

- D1 did not fire (proved). Q has exactly one ordering and its positive cone is {x x~ : x != 0} for x in the even
  subalgebra of Cl_Q(3,0); three components do not suffice. So over the rational foundation the "ordered field"
  of (P) is no further datum. Filed as clauses (iii), (iv) of the four-squares proposal.
- Not filed (argued, classical): the ring Z[1/2] generated by the tower has two completions, the reals and the
  2-adic numbers (Ostrowski), and only the first can be ordered, so the order used by (P) and the completion F4
  select the same one. The selector of op.outcome-selector-premises reads rungs as binary digits of a real
  number; the reversed reading is a 2-adic integer, which has no order to compare with a weight. Recorded as a
  remark only.

## Withdrawn
The survey's sentence that Euler products belong to the three algebras without zero divisors: false as stated
(split algebras have them too). Nothing filed.

## Unexpected links
- The number 7 appears twice for one reason: it needs four squares. That is why three components of the even
  subalgebra do not give the order (D), and why a pair of rational vectors can miss every quaternionic
  four-space (A). Both are the prime 2.
- Three routes to 2^ceil(n/2) on the lens walls: the valuation in Z[J], direct lattice computation, twisted
  spectral asymmetries.

## Decisions for Leon
1. Import Stolz's level theorem as a Fact for the definite-side rung counts of all quarter-turn lens walls, or
   leave it as prior art in a note (as now).
2. If anything is to be built on the L-value dictionary: import (H1)-(H3) as Facts.
3. Whether to adopt the rational-partition-value reading for the count unit (B3 remark). Recommendation: no;
   it is a premise chosen knowing the answer.
4. Maintainer edits that follow from acceptance: op.positivity-of-values (the "more than two modes" item done,
   n = 3 and other fields left); op.wall-class-invariant (bound for all n; the asymmetry route closed; Stolz);
   Remark 1 of the window-energy theorem (now a theorem, by a pointer); the note of the two-mode theorem (its
   "first step" sentence is false).
