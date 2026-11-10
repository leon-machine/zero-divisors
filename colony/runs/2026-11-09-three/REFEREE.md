# Referee brief, run 2026-11-09-three

You are an independent referee for proposals filed against the Transport Lab store (a claim graph of a research
programme on Clifford-algebra zero divisors as a bridge between GR and quantum theory, written in geometric algebra).
LAB = /home/claude/phys-graph. Work only there and in `colony/runs/2026-11-09-three/verify/work-<your-name>/`.
Never spawn agents, never commit or push, never edit store/ or proposals/.

Blindness: do NOT read `colony/runs/*/findings/`, `colony/runs/*/work/`, RUN.md, or the other referee's report. Judge each
proposal on its own text, its premises in the store and its check.

Tools: `python3 colony/labcli.py get_claim|get_proof|search_claims|find_text|cone|neighbourhood|conventions|notation|get_open_problem '<json>'`;
`PYTHONDONTWRITEBYTECODE=1 python3 colony/runcheck.py proposals/<id>/check.py`; `lib/GA.py` (exact Clifford algebra over
Fractions). check4 has been run centrally on every proposal; logs are `colony/runs/2026-11-09-three/verify/final/check4-<id>.log`;
do not rerun check4. WebSearch/WebFetch are allowed to check literature; say what you verified and what you could not. One
heavy process at a time (2 CPUs).

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

Write your report to colony/runs/2026-11-09-three/verify/<your-name>.md with a summary table (id, verdict, one-line
reason), then per proposal the exact fixes. Also rule on duplicates and overlaps within your set.

## Referee R1: the three proposals of this run
- synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure
- synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional
- synthesis.capacity-and-sakharov-readings-leave-the-generation-number-free

Specific points to settle.
Cohomology of the quarter-turn lens spaces: is the equivariant diagonal a chain map in general or only verified for
k <= 9 (is "proved" earned for all n, or is there an induction that the finite check supports)? Is the cup coefficient 6
against 1 derived or pattern-read? Is "given general cellular cohomology as stated background" a hidden import under
Leon's derive-not-import rule (say exactly what is assumed)? The K-ring: which half is proved, what the cited
Atiyah-Hirzebruch filtration supplies, and whether the counting argument 4^n is valid (extension problems). Does the
note on which hypotheses of synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial and
synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height are discharged match those entities at their
stored versions? What is said about the spin class q1 (not derived): is that plain at every level?
Linearised gravitational field at the horizon: clause (1) is an identity in r at three angles and in the angle at two
radii, not a joint identity: does that suffice for a rational function of the stated degrees (state the degree
bound needed), or is "computed" the right label and is it used as "proved" downstream? Is the linearisation in GTG
correct (first-order rotation-gauge field from the torsion-free condition, first-order Ricci vector)? Recompute the
Regge-Wheeler potential and V/f at r = 2M for l = 2 by your own route, and the Zerilli value. Even parity: is the
one-directional status, the l >= 2 scope, and the Killing-frame scope stated at title, one-liner, statement and lay
level? Is the intertwiner kernel claim right (sign of d_t^2 = +c^2, c = lam(lam+1)/(3M))? Literature cited from
memory (Regge-Wheeler, Zerilli, Moncrief, Chandrasekhar): check on the web where you can.
Capacity and Sakharov readings: does the stored quasi-spin theorem
(synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins) say what the proof needs at the pinned
version? Is B = 16 n_g + 8(1 - 6 xi_R) + 12(alpha - 5) what
synthesis.series-content-induces-a-newton-coupling-only-through-an-unfixed-cut-off and
synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations give (recompute)? Is the
independence "argued" or proved (two models of the full premise set), and is that label plain at every level? Is the
look-elsewhere table presented without overclaiming? Does the title claim more than the content (it shows two readings
do not fix n_g, not that nothing can)?
