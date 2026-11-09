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

check4: pending (orchestrator)
