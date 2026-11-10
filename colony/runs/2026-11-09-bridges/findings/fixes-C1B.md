# Fixes C1B, run 2026-11-09-bridges (fix round, part one)

Proposal: synthesis.finite-normaliser-averages-leave-the-haar-moments-at-order-four-and-on-a-parity-sector
(referee R2, SOUND WITH FIXES). Id unchanged. Edited in place: entity.md, proof-main.tex, check.py, coverage.yaml.

1. Title: "Stabiliser-family averages leave the Haar moments at order four, and on parity sectors" (no
   "normaliser", no "order three" as headline; under 90 characters).
2. Clause (ii) and overlap ruling: kept with its counting proof, relabelled a special case, and stated as the
   blade-state case (W = V_A) of the quarter-turn design statement, named in plain text as intended citation
   (synthesis.quarter-turn-rotors-of-the-even-subalgebra-form-a-state-design-of-order-three; a proposal cannot be
   cited, so there is no claimref and no uses edge). To be turned into a claimref by the maintainer once stored.
3. Clause (iv): third sector moment now proved for every m (pair count (E - 2)(E/2 - 1) on the even strings of
   V_A, fraction 1/((D/2+1)(D/4+1))), closed form (dA^2 + dB^2 + 3D + 4)/((D+2)(D+4)); check adds the closed
   form for a, b <= 4 and the pair count for a <= 3. Fourth sector moment stays computed (m <= 4).
4. Clause (iii) upgraded to proved, after verifying the referee's step myself: the quotient
   N(c, r)/prod_{j=2c-r+1..2c}(2^j + 1) has power of two r(c-r) + rc - r(r-1)/2 - 2cr + r(r-1)/2 = -r^2 and
   tends to 2^{-r^2}/phi_r = 2^{-r(r-1)/2}/prod_{j<=r}(2^j - 1); with the tuple count this is the Gaussian
   binomial, and the sum has at most n terms. The finite-size sum over spanned subspaces is now in the statement
   and is checked against the count by rank at seven sizes (192/17 at a = b' = 2, n = 4; G_6 = 2825). The values
   "fourth moment exceeds Haar" stay computed (a + b' <= 8).
5. One-liner, technical, lay: "exceed at order four for every split of at most eight modes (computed)".
6. Clause (v): added the floor(m/2) size-class orbits 3; 15; 28 + 35; 45 + 210 and that bivector turns fail for
   odd m >= 5 too; proof now says the symmetric group is transitive on each size. Check adds 45 + 210 at m = 5.
7. Closing paragraph: "could be replaced by (ii)" replaced by "the number is reproduced by (ii); deriving the Haar
   value needs the state-independent average of the design statement and invariance of the measure, at powers of
   two only". Technical no longer says "the whole parity-preserving group".
8. One-orbit remark: now says no clause uses it and names the three classical inputs (Witt's extension theorem,
   generation of Sp(2m,2) by transvections, sign flips).

Defect (f) (`uses` lists the three eviction theorems and Page as comparison targets): left as filed, maintainer's
call as the referee says; the extraction note now states they are not premises of a proof step. Removing them
would need the check's premise() calls removed as well.

Bridge links.
- B3 (floor(m/2) orbits; 45 + 210 at ten generators): folded into (v) and the check. My findings sentence on a
  "Bott-type dependence through e_v^2" is restricted accordingly: the failure of bivector turns does not depend
  on the parity of m; only the existence of real unit-norm quarter turns for every class does. The su(16) over
  so(10) reading of 45 + 210 is not put in the entity (it is the bridge-hunter's, argued).
- B4 (test number): the q counts at twelve directions are 528 (q = 1) and 495 (q = 0), confirmed and added to the
  check and to (v) as counts. That these are the orbits of the real quarter turns at m = 6 is NOT checked (stated
  so in the clause); the prediction 495 + 528 stays argued.
- B6 (the descent is the parity average): one sentence in the extraction note, as a reading put to the
  maintainer; no clause changed. It strengthens decision 3 (sector values are the relevant column if the
  comparisons are read after the descent).

runcheck: all five functions pass. Style scan (em dash, banned words): clean.

# Fix round, part two

Proposal: synthesis.mass-terms-are-pair-terms-of-the-arrays-and-only-the-charge-separates-majorana-from-dirac
(referee R1, SOUND WITH FIXES). Id unchanged. Edited in place: entity.md, proof-main.tex, check.py, coverage.yaml.

1. Title: "Mass terms as pair terms on four tower modes: the charge separating Majorana from Dirac" (87
   characters; four-mode scope, no "only"). Clause (iii) now says S and D also differ by array structure and by
   rank (S alone gives a mass to two of the four modes, D to all four) and are not equivalent under
   automorphisms preserving the mode space; check adds the two rank statements.
2. Clause (ii): "among the six charges listed"; added the general statement that a diagonal charge commutes with
   D exactly on the family q = (alpha, beta, -beta, -alpha) and S then has charge alpha + beta (proof line and a
   check on seven sample charges, four on the family and three off it).
3. Gap theorem: the sentence now says an explicit bilinear term has vanishing compression on the fixed-charge
   sectors and is not part of H_4; that vanishing compression is not absence of effect (H_4 plus a mass term
   mixes sectors); and that clause (iii) of the gap theorem ties the gap to the mean-field mass of the paired
   array, a self pair term in this vocabulary, with nothing stored identifying that array with the neutral
   singlet or G with a scale. "Sees no mass term at all", "is not the Majorana scale" and "bears on neither"
   are gone from note, technical and reading.
4. Clause (i): the stored one-array block is itself a self pair term (L charge -2, N_a - N_c charge 0), with a
   check; and "every mass term is a pair term" beyond the stored block is flagged as the definition used.
5. Extraction note: cross-reference by name to
   synthesis.order-four-elements-with-square-the-grading-and-the-majorana-element (the opposite number is the
   mode-level image of B - L; the Z4 parity of T is its reduction modulo 4). Plain text, no claimref (a proposal
   cannot cite a proposal); maintainer to convert once both are stored.
6. One-liner: "differs, among the block's charges, by its charge 2 ... (and by rank)".

Bridge link B1: folded into the reading (argued) and the note: every mass form on the sixteen has odd Clifford
grade, so the row "N: -2 on both" corresponds to the order-four element, and the row "L" to that element times
the centre of su(2)_L, under which a Dirac (doublet) form is even and T stays odd; the charge-dependence of
(iii) gets the invariant form "class of the order-four element modulo the unbroken gauge group". Labelled
argued; nothing about the sixteen is computed in this proposal's check (it is a four-mode check), and the
order-four element is not a stored entity.

K != 0 extension (C1A's): ADDED as part of clause (iv) after verifying it myself, by a route that does not use
C1A's script: ad_N is +1 on creators and -1 on annihilators, so ad_H has diagonal blocks K, -K and off-diagonal
blocks -Omega, Omega; the cross terms cancel in the square and ad_H^2 = K^2 - Omega^2. Hence
(ad^2 - K^2)^2 - (M^2 + 2m^2)(ad^2 - K^2) + m^4 = 0, mode energies sqrt(K^2 + x^2). Check added on all eight
mode operators at fifteen rational (K, m, M). I did not open work/C1A/x4.py. Clause (iv) is now "proved" without
the K = 0 restriction; the credit sentence for C1A's first record is in the note without agent names.

runcheck: all four functions pass. Style scan clean.

For Leon (from the referee): whether the stored gap theorem should carry a note that its clause (iii) is a
statement about a self pair term.

check4: pending (orchestrator)
