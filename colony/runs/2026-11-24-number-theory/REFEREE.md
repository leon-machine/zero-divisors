# Referee brief, run 2026-11-24-number-theory (blind)

You are the referee of this run. Read `colony/BRIEF.md` (standards, tools, and the section "Role: referee") first.
LAB = /home/claude/leon-machine/zero-divisors. Do NOT read `colony/runs/2026-11-24-number-theory/findings/`,
`.../work/` or `.../RUN.md`: you must not see the author's reasoning. Do not edit anything under `proposals/` or
`store/`. Do not spawn agents. Write your report to
`colony/runs/2026-11-24-number-theory/verify/referee-R1.md` and nothing else (scratch files go in
`colony/runs/2026-11-24-number-theory/verify/scratch/`).

Five proposals, each a folder under `proposals/` with entity.md (statement at four levels and a note),
proof-main.tex, check.py, coverage.yaml:

 A. synthesis.positive-rationals-are-the-squares-of-the-even-subalgebra-of-cl-three
 B. synthesis.additive-weights-on-the-rational-projectors-are-linear-for-every-number-of-modes   (uses A)
 C. synthesis.order-of-the-doubled-dying-line-on-quarter-turn-lens-walls-is-a-valuation-in-the-ring-of-the-quarter-turn
 D. synthesis.thermal-test-on-the-ground-conic-holds-at-exactly-three-points
 E. synthesis.character-sums-over-the-twist-fibres-of-an-array-are-dirichlet-l-values

The orchestrator's evidence-gate logs are in `colony/runs/2026-11-24-number-theory/verify/check4/` (all five:
0 errors; some W413 "weak under perturbation" warnings; read them, do not rerun check4). To run a check yourself:
`python3 colony/runcheck.py proposals/<id>/check.py`; for B, which cites A (not yet in the store), prefix
`TP_LAB=/home/claude/lab-overlay` (an overlay copy of the store that holds A). Stored entities are read with
`python3 colony/labcli.py get_claim '{"id": "..."}'` and `get_proof`. One CPU-heavy process at a time.

For every proposal: check every proof step; check that each cited stored premise says what is needed at the
pinned version; break the check with at least two targeted perturbations; recompute a key number by your own
route; hunt hidden hypotheses, overclaiming in the title, one-liner and lay level, misquoted literature,
circularity, and results that are transport-absent but presented as more. Verdict per proposal: SOUND, SOUND WITH
FIXES (give the exact fixes), OVERSTATED (give the true weaker statement), WRONG (give the counterexample), or
UNCLEAR (say what decides it). Be adversarial: the author worked alone, with no adversarial sibling.

## Points to settle

### A (four squares in the even subalgebra of Cl(3,0); the order of Q)
1. The descent: the halving step for even m; that the components of x y~ are congruent modulo m to those of
   x x~; the case m' = 0. Is anything missing for p = 2 or for composite numbers?
2. Clause (iii): is the argument that an ordering contains every sum of squares, hence equals P, complete?
3. Clause (v): the diagonalisation of a semidefinite rational form when a pivot vanishes; the count 4n; the
   identification of sums of x x^dagger with sums of y y^T.
4. Is anything claimed as new that is classical? Is the reading about the premise (P) overstated?

### B (additive weights for every number of modes)
1. Step 1 of (iii): does clause (iii) of the stored theorem
   synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear, as stated at version 1, apply
   to the restricted function E -> mu(g iota E iota^T g^T)? Any hidden hypothesis (values in V, the zero
   projector, normalisation)?
2. Clause (ii): are the five functionals nonzero in every case (r' may have zero components; r'_t may equal
   r_t)? Is "they span the dual, so four are independent, so at least four kernels are distinct" right? Do the
   kernels have the supports claimed? Try to find a rational vector with support of size >= 5 for which the
   construction fails; run a random search of your own.
3. The lemma (a quadratic form with values in V vanishing on three distinct hyperplanes is zero), over Q.
4. Step 2: is rho well defined and is D zero on vectors of support <= 4 for every n >= 4?
5. Clause (v): the necessity of "sum of three squares"; the example e_1, e_2+e_3+e_4+2e_5; whether this really
   refutes the first step as worded in the note of the stored theorem. Does (v) contradict (iii)? (It should not.)
6. Try to build a counterexample to (iii) in Q^5 (an additive weight that is not linear), for instance by a
   parity or 2-adic construction in the manner of clause (v) of the stored theorem. Report what you tried.
7. Prior art and overclaiming: the note's sentences on Mushtari; the title "for every number of modes".

### C (order of 1 - chi^2 for every n; Z[J])
1. Clause (ii): the reduction in Z[sigma] (sigma prime, does not divide sigma + 2; both directions); the
   identification Z[sigma]/(phi) = Z[J].
2. Clause (i): the divisibility statement in Z[J].
3. Clause (iv): the determinant argument (d(1 - zeta) = Phi(1), (x - 1)^M = x^M + 1 + 2h, h(zeta) invertible);
   the case M = 1; the exponent ceil(2n/N).
4. Clause (iii): does clause (1) of synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height (version 2)
   give k - 1 >= log2 of the order, and is the stored K-ring quoted correctly? Is "replaces the pair of bounds"
   accurate? Recompute the order for a few n by your own route.
5. The note's statements about spectral asymmetries and about Stolz (1989): are they worded as unfiled and as
   prior art, with nothing resting on them?

### D (no fourth point on the ground conic)
1. Is T the thermal test of the stored theorem
   synthesis.window-energy-tests-with-free-spacing-admit-twists-half-third-and-quarter (units, the sea energy on
   the conic, the two families of weights)? Does that theorem assert zeros at exactly (1,1/2), (1/2,1/4),
   (sqrt(2/3),1/3)?
2. Step 1: every inequality (a >= k + 1/5; the bracket; 41/100; monotonicity; the cut at 429/2000).
3. Step 2: the bounds on |g|, |g'|, |g''| and the constant 223/10; that the check applies it correctly
   (M, lambda_0, K = 8).
4. Step 3: soundness of the interval library in check.py (outward rounding in every operation; the exponential:
   halving with directed rounding, series remainder, squaring back; the square root; pi; the jet rules; jfermi).
   Look for any place where an enclosure could fail to contain the true value.
5. Steps 4 to 6: the mean-value form; that the six regions cover (1/2 - 1/sqrt(12), 1/2]; T'(1/2) = 0; the count.
6. Recompute T at ten points and locate its sign changes by your own code (floating point is fine for your own
   route) and compare.

### E (character sums over twist fibres are L-values)
1. Are (H1), (H2), (H3) correctly stated classical facts (signs, normalisations, the imprimitive case)?
2. Clause (i): the spectral asymmetry 1 - 2 delta. Clauses (ii), (iii): signs and factors. Clause (v): every
   instance value; recompute three by hand or by your own code.
3. The first check compares two evaluations of one finite sum (the coverage record says so). Is the remaining
   independent evidence (class numbers, divisor sums) enough for status proved "given (H1)-(H3)"?
4. Overclaiming: does any level suggest a constraint, a prediction or a link to the zeros of L-functions?

### Across
House style in store text (no em dashes; never "honest"; never "load-bearing"; never "clever"; Q(v) for the
square of a vector; no agent, run or method names in statements). Geometric-algebra language: each entity
declares `outside_ga`; is each declaration accurate? Duplicates of stored results?
