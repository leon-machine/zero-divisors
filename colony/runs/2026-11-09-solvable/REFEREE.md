# Referee brief, run 2026-11-09-solvable

You are an independent referee for proposals filed against the Transport Lab store (a claim graph of a research
programme on Clifford-algebra zero divisors as a bridge between GR and quantum theory, written in geometric algebra).
LAB = /home/claude/phys-graph. Work only there and in `colony/runs/2026-11-09-solvable/verify/work-<your-name>/`.
Never spawn agents, never commit or push, never edit store/ or proposals/.

Blindness: do NOT read `colony/runs/*/findings/`, `colony/runs/*/work/`, RUN.md, or the other referee's report. Judge each
proposal on its own text, its premises in the store and its check.

Tools: `python3 colony/labcli.py get_claim|get_proof|search_claims|find_text|cone|neighbourhood|conventions|notation|get_open_problem '<json>'`;
`PYTHONDONTWRITEBYTECODE=1 python3 colony/runcheck.py proposals/<id>/check.py`; `lib/GA.py` (exact Clifford algebra over
Fractions). check4 has been run centrally on every proposal; logs are `colony/runs/2026-11-09-solvable/verify/check4_<id>.log`;
do not rerun check4. WebSearch/WebFetch are allowed to check literature; say what you verified and what you could not. One
heavy process at a time (2 CPUs shared with the other referee).

For each proposal: (1) check every proof step; confirm each cited store entity says what is needed at the pinned version;
(2) run and read the check, make at least two targeted perturbations and confirm it fails, recompute one key number by your
own route; (3) hunt hidden hypotheses, overclaiming at title/one-liner/lay level, "proved" where only argued, literature
misquoted or cited from memory, circularity (use `cone`), classical results presented as new, duplicates of stored entities
and of each other; for an independence proof: are both models models of the FULL premise set at the pinned versions (list
it with `cone`; a premise missing from the audit is a defect), and does the moved quantity really differ; (4) verdict:
SOUND; SOUND WITH FIXES (exact fixes); OVERSTATED (the true weaker statement at every level); WRONG (counterexample or
failing step); UNCLEAR (what decides it).

House style: no em dashes; never "honest"/"honestly"; never "load-bearing"; Q(v) for the square of a vector; macros only
from store/notation.yaml. Leon's rules (check as fixes): everything in geometric algebra; results derived, not imported
(literature as prior art only); no imaginary unit where a GA unit can stand (store/conventions.md, unit principle).

Write your report to colony/runs/2026-11-09-solvable/verify/<your-name>.md with a summary table (id, verdict, one-line
reason), then per proposal the exact fixes. Also rule on duplicates and overlaps within your set.

## Referee R1: topology, horizon modes, gauge sector, Koide
- synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial
- synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height
- synthesis.horizon-channels-of-scalar-dirac-and-maxwell-fields-are-two-dimensional
- synthesis.field-level-brst-of-the-two-doublets-and-the-thooft-feynman-gauge
- synthesis.higgs-sector-brst-does-not-fix-the-breaking-pattern-of-two-doublets
- synthesis.gauge-factor-sugawara-parts-satisfy-virasoro-relations-on-the-band
- synthesis.koide-middle-mass-bound-closes-the-remaining-quark-dressing-class
- synthesis.joint-clifford-clause-is-an-instance-of-the-signed-direction-postulates
Points to settle:
1. Walls (two proposals on op.wall-class-invariant): the spin-class obstruction q1(L + L) = 2y^2 on L^{2m+1}(4) and the
   K-theory obstruction 2^{k-1}(1 - xi) = 0 with k >= 1 + floor(n/2): re-derive one key value each (the lens-space rings are
   cited from memory: say so if the proofs need them as imports); is "k(Sigma) <= 2 forces L + L stably trivial" proved from
   the stored necessity clause (synthesis.wall-rung-count-is-height-of-dying-line-class)? Are the explicit walls tame with the
   stated physical signatures? Overlap: both give k >= 3 on L^7(4); keep both?
2. J3 (horizon channels of scalar, Dirac and Maxwell fields): the separation in the static GTG gauge of the stored
   Schwarzschild Fact, the Dirac radial operator and its potentials lambda^2 f/r^2 +- lambda sqrt f (3M - r)/r^3, the spin-1/2
   decay e^{kappa r_*} (order sqrt f) against e^{2 kappa r_*} for spins 0 and 1; is completeness of spinor harmonics cited from
   memory and marked; is spin 2 excluded at every level; is "not uniform in l" stated; is the result stated per boost-weight
   zero channel? Does it contradict the stored postulate hawking.joint-j3-s-wave-reduction or the problem's known text?
3. Higgs-sector BRST (two proposals): nilpotency of s phi with the doublets as even elements of Cl(3,0); the stationarity
   condition for the free part; Goldstone rank 0, 3, 4; the two quartics; rank 3 on the rung lift boundary. Rule on overlap
   between the two and say what each should keep.
4. Virasoro relations of the Sugawara parts on the band: is the domain stated (no Virasoro algebra on finite windows: the
   trace of a commutator vanishes); are the central values 32/7, 2, 1, 1 and 52/7 central charges on the band exactly; is
   Goddard-Kent-Olive cited as prior art; does any vacuum-constant clause (-c_f/24 summing to -16/24 per generation) hold.
5. Koide middle-mass bound: re-derive (17/2 - 6 sqrt 2); the stored masses used; is the claim that the stored lemma (iv)
   already covers the class D2 > D3 > D1 (contradicting its formal statement) correct?
6. The joint Clifford clause as an instance of the signed-direction postulates: the group of order 2^11 of the ten slot and pair
   Majoranas with -1; Cl_Z(5,5) faithful on V; signature forced; the adjoint as the group inverse (commutant Q on Q^32); does
   the clause really ask nothing beyond F1-F3 (what does the Klein twist contribute)?

## Referee R2: generations and independence proofs
- synthesis.one-window-parity-recurrence-of-the-light-ray-sea-needs-twenty-four-arrays
- synthesis.light-ray-recurrence-test-verdict-on-generations-is-set-by-the-scalar-content
- synthesis.bott-shifted-model-leaves-the-odd-towers-dimension-free
- synthesis.no-rule-p2-licenses-gives-the-thickness-of-r3
- synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping
- synthesis.georgi-jarlskog-weight-free-on-the-stored-relations
- synthesis.d-term-level-free-at-fixed-n
Points to settle:
1. The recurrence pair (op.counted-mode-energy, op.qft-structural-inputs): re-derive U = e^{2 pi J n/24} Gamma on a window and
   "U = Gamma iff 24 | n"; the table c = 16 n_g + 2 n_V + n_s + 2 eps and its verdicts (two doublets: passes at n_g = 1, 4,
   fails at 3). Scope: the stored postulate hawking.joint-j3-s-wave-reduction (J3) and hawking.helicity-lift-joints-itemised lie
   in the past cone of synthesis.null-ordering-of-counted-units-is-zeta-symmetric; under J3 the integer-weight fields are read
   as currents of the arrays. Does either proposal's CAR-only scope, or its additive counting of bosons on top of the arrays,
   conflict with J3 (double counting, or eps = 1 under J3's graviton)? Is "the condition is a choice" proved (a second model)
   or argued; would synthesis.slot-module-...-leaves-the-generation-number-free (find it by search) supply the second model?
   Prior art: J. Wang arXiv:2312.14928, Garcia-Etxebarria and Montero arXiv:1808.00009: verify and check nothing is
   presented as new that is not. Overlap between the two: rule.
2. Window (Bott-shifted model): Cl(p+8, q) = A (x) Mat(16, R) with A a faithful copy of Cl(p, q); every selector unchanged;
   both models satisfy the full premise set except P3. Specifically: dark-tower-matter.u-transposition-rule (U3) may be
   missing from the audit: at (10,1) there are b = 6 pairs but the real Witt index is 2, four pairs would need a complex
   unit and the field R has none; at (12,1) H supplies it. If U3 fails on the shifted model, the independence is only for
   some residues: state the true weaker statement.
3. Thickness: the definition of a "licensed" rule (equating only objects in one symmetry orbit) is a reading: is it
   flagged as such at every level; the cell Gram ranks 3, 2, 4; the share 8/(3 pi) in (5/6, 8/9).
4. Residue: 22 of the 231 groupings with eight units qualify; no single ladder pair carries ln 2; the light-ray count
   2 pi N^2/(c ln 2) and the correction to dark-matter.stored-asymmetry-charge-not-number; J3 lies in the cone (via
   capacity-per-mode (iii)): does J3 fix the grouping?
5. Georgi-Jarlskog weight: the map h_mu leaves every stored relation fixed; the three exact models (factor 3, 2, 37/19);
   are postulates (EW), (U) used though not in uses (hidden premises)?
6. xi G: two frames at equal G, Lambda, N, g, g', kappa give different xi G; is the list of stored relations mixing the
   Planck and weak scales complete (search yourself); is the toy W = kappa N^2 branch, excluded by the record, a valid model
   for independence (the premise set, not the record, is what a model must satisfy: say whether the proposal says so).
7. Method: for every independence proof, the full premise cone at the pinned versions must be audited in both models.
