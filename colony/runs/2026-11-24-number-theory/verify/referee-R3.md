# Referee report R3, run 2026-11-24-number-theory

Blind referee. Read: REFEREE-R3.md, colony/BRIEF.md (standards, Role: referee), `git diff HEAD`, the new
folders under store/claims/, and the stored entities each item cites. Not read: findings/, work/,
verify/scratch-R2/, RUN.md, REPORT.md, verify/referee-R1.md. Nothing under store/ was edited. Scratch:
verify/scratch-R3/ (nt_tests.py, stolz_small.py, perturbed copies p1-p3_check.py, c1-c2_check.py).

Checks run (`colony/runcheck.py`, one at a time): the new definite-side result, character-sums, order result,
lens-space walls v3, three-rungs. All PASS. Perturbations: definite-side check fails when the m = 6 residue is moved
to 4 (p1), when the n = 5 residue is moved to 3 (p2), and when the listed values are altered (p3); character-sums
check fails when w(-3) is set to 4 (c1) and when 1/60 is set to 1/50 (c2). So the checks are not vacuous.

## Summary of verdicts

| Item | Verdict |
|---|---|
| 1a Stolz import | SOUND WITH FIXES (the value at m = 4 mod 8 is UNCLEAR at the level read) |
| 1b Hurwitz import | SOUND WITH FIXES (minor) |
| 1c class number formula at 0 | SOUND |
| 1d divisor-sum formula at -1 | SOUND WITH FIXES (range at D = 1; locator) |
| 2 definite-side rung count, every n | SOUND WITH FIXES (missing tameness; an uncited bound; the m = 4 mod 8 dependence not flagged) |
| 3a lens-space walls v3 | SOUND WITH FIXES (clause (4) left stale) |
| 3b window-energy v2 | SOUND WITH FIXES (technical level left stale) |
| 3c additive-weights note | SOUND |
| 4a character sums | SOUND |
| 4b order result | SOUND WITH FIXES (clause (iv) still draws a rung bound with no edge; ambiguous "cited result" in the proof) |

No circular dependence found: the cone of the order result (22 entities) does not contain the lens-space result; the
cone of the thermal-test result does not contain window-energy beyond its uses edge (the remark is not used).

---

## 1a. synthesis.imported-stolz-level-of-real-projective-spaces-under-the-quarter-turn

**What I looked up (reading level: secondary only; the paper was not read).**
- Bibliographic data confirmed from the publisher's page (DOI 10.1007/BF02564700) and mathdoc/EuDML metadata: S. Stolz,
  The level of real projective spaces, Comment. Math. Helv. 64 (1989), no. 4, 661-674; Zbl 0697.55009. Correct.
- The zbMATH review (reviewer A. Pfister), read through the MaRDI portal mirror (Item Q911096): for m >= 2, values
  m + 1 (m = 0, 2), m + 2 (m = 1, 3, 4, 5, 7), m + 3 (m = 6) modulo 8. The review attributes one bound to
  vector bundles and a theorem of Crabb on the cohomotopy Euler class and the other to Adams's E2-term
  computation, and says that the two bounds coincide except for m = 4 modulo 8, yet lists m + 2 there. It gives
  no further argument for that case. I could not tell from it which bound is the weaker one at m = 4 mod 8.
- Furuta, Kametani, Matsue, Minami, Geom. Topol. Monogr. 10 (2007) 155-166 (pages and DOI 10.2140/gtm.2007.10.155
  confirmed on msp.org): Definition 2.1 takes the level as the least n with an equivariant map to S^{n-1} (matching
  the entry's normalisation), and Example 2.2(ii) gives the same three cases for S(C^m)/<i^2> with involution from i,
  with no range stated and no caveat. The entry's description of both is accurate.
- My attempt to reach the full text through an open archive was refused by the session's network policy; not retried.

**Mathematics.** The equivalence of the two formulations is right: F(J v) = -F(v) forces F(-v) = F(v), J induces a
free involution on RP^{2m-1} (J has no real eigenvalue), and the normalisation "least k with a map to S^{k-1}"
matches Dai-Lam and FKMM. J(v) = v . B is the quarter turn in each plane (e1 -> e2, e2 -> -e1), a complex
structure, conjugate to multiplication by i. Small cases recomputed (scratch stolz_small.py, exact integers):
m = 2, F(q) = conj(q) j q is pure imaginary, odd under left multiplication by i, |F| = |q|^2, so s(2) <= 3, agreeing
with the stored 3; m = 1, z -> z^2 is odd under the quarter turn, and S^1 connected forbids k = 1, so the least k is
2, not the formula's 3. The range m >= 2 is therefore needed and correctly imposed.

**Defect (serious for item 2).** The formal level asserts m + 2 at m = 4 mod 8 without qualification; only the
extraction note mentions the review's remark. The single new concrete consequence downstream (closing L^7(4) at 6,
m = 4) sits exactly in that residue. Fixes:
- In `## formal`, after the displayed cases, add: "The published review of the paper reports that the paper's
  lower and upper bounds do not coincide for $m \equiv 4 \pmod 8$, while it lists the value $m + 2$ there; how the
  paper settles that case was not seen."
- In the first `imported_from` locator, replace "taken from the published review of the paper" with "taken from
  the zbMATH review (Zbl 0697.55009, by A. Pfister)".
- In the one-liner, after "the paper not read", add "; the case $m \equiv 4$ modulo $8$ as listed, the review noting
  that the paper's bounds differ there".
Is the import stronger than needed? It is used for all m, so no; but its use at m = 4 mod 8 is the point to watch.

## 1b. synthesis.imported-hurwitz-zeta-values-and-dirichlet-l-functions-as-hurwitz-sums

**Recomputed (scratch nt_tests.py, mpmath continuation).** zeta(0, a) = 1/2 - a and zeta(-1, a) = -B_2(a)/2 at
a = 1/3, 1/2, 3/4, 1 agree to 15 digits; (iii) at s = 0, -1 against mpmath's Dirichlet series for chi_{-4},
chi_{-23}, chi_5, chi_12 agrees; (iv) removing the factor at 2 from chi_5 (period 10) agrees at s = 0, -1, 1/2, 2.
The general formula zeta(1 - k, a) = -B_k(a)/k with B_1(a) = a - 1/2 is right; continuation to s = 1 when
sum chi(a) = 0 is right.

**Literature.** Hurwitz, Z. Math. Phys. 27 (1882) 86-101 with the given title: confirmed through the bibliography
of Oswald and Steuding, arXiv:1506.00856 (secondary). Apostol, ch. 12: not checked online; I believe it right.

**Minor fixes.**
- (iv): "for all $s$ by continuation" -> "for all $s \ne 1$ by continuation" (for a principal chi both sides have a
  pole at 1). Also "If $\chi$ is completely multiplicative" -> "If $\chi$ as in (iii) is completely multiplicative"
  (periodicity is what gives the continuation).

## 1c. synthesis.imported-class-number-formula-at-zero-for-negative-discriminants

**Recomputed.** For all 611 fundamental D in [-2000, -3]: L(0, chi_D) from (iii) of 1b equals 2h/w with h counted
as reduced forms under the entry's exact definition and w counted as solutions of the entry's norm forms. 0 failures.
Kronecker symbol has period |D| and chi_D(-1) = -1 on the first 80. Non-fundamental D (-12, -16, -27, -28) fail, as
the entry's exclusion requires. The definition of fundamental discriminant and of "reduced" are the standard ones.

**Literature.** Dirichlet, J. Reine Angew. Math. 19 (1839) 324-369; 21 (1840) 1-12, 134-155: confirmed from mathdoc
and EuDML metadata (title pages, not the text). Davenport, GTM 74, 2nd ed. 1980, ch. 6 and 9: not checked online.
Remark only: Davenport's ch. 6 gives the finite form h = -(w/2|D|) sum a chi(a) directly, which is L(0) = 2h/w by
(iii) of 1b since sum chi = 0; the passage through the functional equation is one route, not the only one. No fix
required. Verdict SOUND.

## 1d. synthesis.imported-zeta-of-a-real-quadratic-field-at-minus-one-as-a-divisor-sum

**Recomputed.** For all 909 fundamental D in [2, 3000], L(-1, chi_D) from the Bernoulli sum equals
-(1/5) sum sigma((D - b^2)/4). 0 failures. Non-fundamental D (20, 45, 48) fail, as the exclusion requires.

**Defect (range).** D = 1 is counted as a fundamental discriminant in some standard sources (for example in Cohen's
computational conventions), and there the formula is false: the sum is empty while L(-1, chi_1) = zeta(-1) = -1/12.
Fix in `## formal`: "Let $D > 0$ be a fundamental discriminant" -> "Let $D > 1$ be a fundamental discriminant
($D \equiv 1 \pmod 4$ squarefree, or $D = 4d$ with $d \equiv 2, 3 \pmod 4$ squarefree)"; same change ("$D > 1$") in
the one-liner.

**Literature (secondary or metadata).** Cohen, Math. Ann. 217 (1975) 271-285: confirmed (mathdoc). Zagier,
Enseign. Math. (2) 22 (1976): volume confirmed from his own copy and MaRDI; pages 55-95 not confirmed. His paper
derives an elementary formula for zeta_K(-1) in its section 2 and credits the general result to Siegel; the copy I
saw was too garbled to confirm the constant 1/60, which my computation confirms instead. Siegel's entry in
Zagier's bibliography reads Nachr. Akad. Wiss. Gottingen Math.-Phys. Kl. II, Nr. 10 (1969) 87-102. Fix: in the
Siegel citation, "Kl. II (1969), 87--102" -> "Kl. II, Nr. 10 (1969), 87--102". The note's admission that it is not
verified which source states the formula in this form is accurate; on what I saw, Zagier 1976 section 2 is the
closest locator; suggest adding it to his locator ("\S 2").

## 2. synthesis.definite-side-rung-count-on-every-quarter-turn-lens-wall-is-the-level

**Derivation.** Clause (1) of the dimension-five result at v1 is exactly the index form used, with
2m - 1 = 2n + 1, m = n + 1 >= 2, so the import's range covers every n >= 1. Residue translation checked: m = 0, 2
<-> n = 7, 1; m = 6 <-> n = 5; values for n = 1..8: 3, 5, 6, 7, 9, 9, 9, 11 (recomputed). k_+ = e(L) on a definite
side is from that result's opening paragraph (clauses (1), (3) of the two-rung result). Clause (ii): clause (2) of
the wall-rung result is sufficiency with no condition on the side, so k <= e(L) on every side is right; the lower
bound 1 + ceil(n/2) is clause (2) of the lens-space result at v3, pinned @3, correct. Clause (iii): arithmetic
checked ((3,3), (5,5), (6,6), (8,7), (9,9) for m = 2..6; excess >= 2 from n = 6). Clause (iv) is worded as a
remark and claims nothing. Status "proved" (given an import) matches the store's convention for the dimension-five
result (proved given the Steenrod Fact), and the title and one-liner say "given Stolz".

**Defects.**
1. Tameness missing. k_+ is defined for tame walls, and every result it rests on (dimension-five, two-rung,
   wall-rung, lens-space) carries `assumes: sheaf.tameness@1`; this one has no `assumes` and no level mentions
   tameness. Decision for Leon: add `assumes: [sheaf.tameness@1]` to the derivation. Text fixes: in the one-liner,
   "Given the imported theorem of Stolz," -> "Assuming tameness and given the imported theorem of Stolz,"; in the
   technical level, last sentence, add "and assumes the tame-wall setting".
2. Uncited bound in (ii). "with the stored bound $k \ge 4$ for $n \ge 2$" cites nothing and that result is not in
   `uses`; it is clause (3) of synthesis.three-rungs-do-not-complete-the-quarter-turn-lens-walls-on-any-side, and at
   n = 2 it is conditional on the spin class (L2). Replace with "with $k \ge 4$ for $n \ge 2$ (clause (3) of
   \claimref{synthesis.three-rungs-do-not-complete-the-quarter-turn-lens-walls-on-any-side}, conditional at $n = 2$
   on the spin class (L2) there)", and add that result to `uses` at its current version, or drop the two windows
   from (ii).
3. The m = 4 mod 8 dependence is not flagged. The closure of the stored window on L^7(4) at 6 (n = 3, m = 4) and the
   optimality of the explicit maps at n = 3 are the residue where the review says Stolz's two bounds differ. The
   check cannot test this: replacing m + 2 by m + 1 at m = 4 mod 8 keeps every stored-bound comparison in the check
   true (the stored window is 5 <= k <= 6); only the hard-coded 6 would fail. Fixes: in (i), after "closes at $6$",
   add "(the case $n + 1 \equiv 4 \pmod 8$ of (St), where the review of Stolz's paper notes that the paper's two
   bounds differ; see the imported Fact)"; same parenthesis after "closing the stored window on $L^{7}(4)$ at $6$" in
   the one-liner; in the lay level, "The classical question was settled in every dimension in 1989." -> "A theorem
   of 1989, taken here from accounts of it rather than from the paper, answers the classical question in every
   dimension."
   Note for the maintainer: if the gap at m = 4 mod 8 is on the upper side (true value m + 2, upper bound m + 3),
   m = 4 is settled anyway by the stored explicit map (6 = m + 2) and only m = 12, 20, ... depend on the unseen
   argument; if it is on the lower side, m = 4 is exactly the stored open window. The review does not say which.
4. Tag `hyperbolic-plane` looks misplaced (no hyperbolic plane appears); harmless.

## 3a. synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height, v2 -> v3

**Restated clause (2)** is correct: 2^{ceil(n/2)} = 2^{floor((n+1)/2)}, agreeing with the stored lattice values
1,1,2,2,3,3,4,4 (n = 1..8) and with the order result's clause (ii); the examples 3, 4, 5 on L^7, L^11, L^15 and 2 at
n = 1 hold. Technical, lay and one-liner are consistent. The new proof paragraph is right (phi loses a factor
J - 1; dividing by chi - 1 recovers it).

**Circularity.** None. The order result's `uses` are now the cohomology theorem and std-algebra.complex-numbers
only; its cone (22 entities) does not contain this result; its checks call no premise on it. Its clause (iii) is a
pointer (but see 4b on its clause (iv)).

**Dependant three-rungs @3.** It uses only clause (1) (unchanged) for its comparison "that bound gives three" at
n = 3, 4; 1 + ceil(3/2) = 1 + ceil(4/2) = 3, so the comparison is still true at v3. Repin sound.

**Defects.**
1. Clause (4) left stale. It says "$k(\Sig) \geq r$ grows without bound" on $L^{4r-1}(4)$, i.e. n = 2r - 1 odd,
   where the restated (2) now gives 1 + r. Replace "while $k(\Sig) \geq r$ grows without bound" with "while
   $k(\Sig) \geq r + 1$ grows without bound". The amendment note's "clauses (1), (3), (4) ... are unchanged" then
   needs "(4) with the bound $r + 1$ in place of $r$".
2. The amendment `defect` says the old bound "was not sharp at odd n", which reads as a claim about the rung count.
   Replace "and the bound 1 + floor(n/2) was not sharp at odd n" with "and the bound 1 + floor(n/2) was one less, at
   odd n, than what the obstruction of clause (1) gives". `evidence` is absent (the brief's format has it); suggest
   "evidence: check.py::check_order_of_one_minus_chi_squared_in_the_stored_k_ring_is_two_to_the_ceiling_of_n_over_two
   of the order result (n up to 40)".

## 3b. synthesis.window-energy-tests-with-free-spacing-admit-twists-half-third-and-quarter, v1 -> v2

No statement circularity: the thermal-test result uses clauses of this theorem, not Remark 1, and Remark 1 is
explicitly outside the theorem with no edge. The thermal-test repin @2 is fine. Formal remark and one-liner are
accurate.

**Defects.**
1. Technical level left stale: it still ends "Whether further points exist without the parity clause is examined
   by a numerical scan only, not proved." Replace with "There are no further points, with or without the parity
   clause: a later result proves it by certified enclosures." The amendment `defect` should then read "...and the
   technical level, the lay level and the one-liner repeated the weaker wording".
2. Lay: "at least three sets qualify, not one (and no more: a later result proves that there is no fourth)" ->
   "exactly three sets qualify, not one (that there is no fourth is proved in a later result)".

## 3c. synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear (note only)

Checked the counterexample: |e2 + e3 + e4 + 2e5|^2 = 7, e1 orthogonal, so the bivector squares to -7. If both lay in
a 4-space similar to c times standard Q^4, their Gram determinant would be c^2 |Im(conj(a) b)|^2, a sum of three
rational squares, and 7 is not (7 mod 8). The cited clause (v) of the size-from-four result exists and says this;
that result's clause (iii) rests on clause (iii) here. New wording accurate. Verdict SOUND. (Q^{2^l} for more than
two modes means l >= 3, so e5 exists.)

## 4a. synthesis.character-sums-over-the-twist-fibres-of-an-array-are-dirichlet-l-values

Clause-by-clause citations are right: (i) uses 1b(ii); (ii) uses 1b(iii) with f = 2M (the import's period-f
statement covers a character of the odd residues); (v) uses 1b(iv) for the Euler factors (primes dividing 2M not D),
1c and 1d. All instance values in (v) recomputed: 1, 2, 4, 4/3, 4, 0 (D = -7, -15, -23); L(-1) = -1, -2, -2/5, -2;
energy sums 1/4, 1/3, 6/25, 6/13. The check calls premise() on each import in the functions that use it. The
formal still labels clauses "proved given (H1)", which is now an imported Fact: consistent. The check's Euler-factor
code handles only the primes 2 and 3, enough for its CASES. Verdict SOUND. (If 1d is restricted to D > 1, the
cross-reference needs no change.)

## 4b. synthesis.order-of-the-doubled-dying-line-...-valuation-in-the-ring-of-the-quarter-turn

Clause (iii) is now a pointer and says so; the renamed check function computes arithmetic only and calls no premise,
correctly. Remaining defects:
1. Clause (iv), last sentence, still draws a rung bound from clause (1) of the lens-space result, with no edge (an
   edge would make a cycle, since the lens-space result now uses this one). Replace "If $K(L^{2n+1}(N))$ is that
   quotient ring with $\chi^{N/2}$ the complexified dying line (classical, not stored for $N \ne 4$), clause (1) of
   the result cited in (iii) gives $k(\Sig) \ge 1 + \lceil 2n/N \rceil$ on walls with cross-section $L^{2n+1}(N)$:
   the bound from complex K-theory weakens as the turn gets finer." with "Remark, not part of this result: if
   $K(L^{2n+1}(N))$ is that quotient ring (classical, not stored for $N \ne 4$), clause (1) of the result cited in
   (iii) would give $k(\Sig) \ge 1 + \lceil 2n/N \rceil$ on walls with cross-section $L^{2n+1}(N)$, so the bound from
   complex K-theory weakens as the turn gets finer." Same in the proof's last sentence.
2. Proof (iii) and (iv): "clause (1) of the cited result" now follows a paragraph that cites the cohomology theorem,
   so "the cited result" reads as that theorem. Replace with "clause (1) of
   \claimref{synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height}" in proof (iii), and "the result
   named in (iii)" in proof (iv).
3. The note's first sentence ("dividing the relation by chi - 1 first gives the exact order") is fine; the later
   "so the bound 1 + floor((n+1)/2) holds for every n" should add "(stated in the lens-space result, v3)".

## Across

House style: no em or en dashes, no "honest", "load-bearing", "clever" in the diff or the new folders. Agent and run
names appear only in credit and amendment metadata, as the brief's format prescribes. `outside_ga`: the four imports
`imported`, accurate; the new derived result `other`, acceptable. Untracked REFEREE-R2.md, REFEREE-R3.md and
scratch-R2/ are run files, not store content. Nothing in the diff that should not be there.

## For the maintainer only

1. Whether to add `assumes: sheaf.tameness@1` to the new definite-side result (item 2, defect 1).
2. Whether to rely on the m = 4 mod 8 case of Stolz (closure of L^7(4) at 6) before someone reads the paper
   (Comment. Math. Helv. is open access through the Gottingen digital library); at minimum flag it as proposed.
3. Whether to add the three-rungs result to the new result's `uses` or drop the indefinite-side windows from (ii).
4. Whether to restrict 1d to D > 1 (recommended; a counterexample at D = 1 under one common convention).
