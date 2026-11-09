# Referee brief, run 2026-11-09-bridges

You are an independent referee for proposals filed against the Transport Lab store (a claim graph of a research
programme on Clifford-algebra zero divisors as a bridge between GR and quantum theory, written in geometric algebra).
LAB = /home/claude/phys-graph. Work only there and in `colony/runs/2026-11-09-bridges/verify/work-<your-name>/`.
Never spawn agents, never commit or push, never edit store/ or proposals/.

Blindness: do NOT read `colony/runs/*/findings/`, `colony/runs/*/work/`, RUN.md, or the other referee's report. Judge each
proposal on its own text, its premises in the store and its check.

Tools: `python3 colony/labcli.py get_claim|get_proof|search_claims|find_text|cone|neighbourhood|conventions|notation|get_open_problem '<json>'`;
`PYTHONDONTWRITEBYTECODE=1 python3 colony/runcheck.py proposals/<id>/check.py`; `lib/GA.py` (exact Clifford algebra over
Fractions). check4 has been run centrally on every proposal; logs are `colony/runs/2026-11-09-bridges/verify/final/check4-<id>.log`;
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

Write your report to colony/runs/2026-11-09-bridges/verify/<your-name>.md with a summary table (id, verdict, one-line
reason), then per proposal the exact fixes. Also rule on duplicates and overlaps within your set.

Lessons of the previous round, apply them as tests: a sampled check supports "computed", not "proved", unless the
proof carries a degree bound or a basis argument; an independence or "no stored premise" claim is "argued" unless audited
over the full joint cone; scope (frame, range of n or l, hypotheses, conditional inputs) must appear in title, one-liner,
statement and lay level alike; literature cited from memory must be flagged and, where you can, checked on the web.

## Referee R1: lens-space rung counts, the curved-field kernel, the order-four element, mass terms
- synthesis.definite-side-rung-count-on-the-quarter-turn-lens-wall-of-dimension-five
- synthesis.three-rungs-do-not-complete-the-quarter-turn-lens-walls-on-any-side
- synthesis.vacuum-polarisation-kernel-on-a-gravitational-field-has-the-flat-leading-part-and-no-weyl-term-of-degree-four
- synthesis.order-four-elements-with-square-the-grading-and-the-majorana-element
- synthesis.mass-terms-are-pair-terms-of-the-arrays-and-only-the-charge-separates-majorana-from-dirac

Specific points to settle.
Rung count on L^5(4): verify the explicit odd map and its norm identity by your own computation (is Q(F) nonzero on the
whole sphere, is F(Jv) = -F(v) with J the quarter turn, are there five components); is the reduction k = e(L) = least k
with an odd map really the stored clause at its pinned version; the lower bound (no odd map into R^4 minus 0): check the
Thom-space/Steenrod argument step by step, recompute Sq^2 on the relevant classes, and try an independent route (for
example: four components iff a quaternionic line bundle is trivial; a map to S^4 through CP^2); is "conditional on
classical inputs" plain at every level and are those inputs stated exactly; the general bound k <= ceil(3(n+1)/2); the
"argued" secondary-obstruction formula must not be stated as a result. Check the literature on the level/coindex of
lens spaces or projective spaces with involution (Pfister-Stolz, Stolz) on the web if you can.
Three rungs: is "three rungs force L + L stably trivial when twisted H^2 vanishes" proved from stored clauses; the twisted
cohomology computation; which cases rest on the stored K-ring alone and which on the spin class q1 (not imported: must be
labelled conditional); consistency of the two rung proposals with each other and with the stored
synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial and
synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height at their current versions.
Curved-field kernel: status is "proved" while several checks are sampled: is a basis or degree argument present; is the
rotor cancellation exact; is the Taylor datum quoted correctly from the stored bulk Hadamard theorem at its pinned
version; does the Weyl contraction vanish in general or only on the samples (prove or find a counterexample); "the
freedom is the flat one" is claimed pointwise: test it against the remark that on a fixed field d_mu(c(x) F^{mu nu}) is
transverse for every smooth c, so the Ward-preserving freedom is a function space without a local-covariance input; is
the result about the parametrix kernel or about a state's kernel, and is that plain; are the scaling-degree rules cited
from memory stated exactly; vanishing torsion stated.
Order-four element: verify in Cl(10,0) that the pseudoscalar squares to -1, commutes with bivectors, and that the stored
Majorana element (standard-model.majorana-element at its current version) is odd under it; check every sentence about
Dirac mass terms: all mass forms on the sixteen have odd Clifford grade (grades 1, 3, 5), so they all anticommute with
the pseudoscalar; a sentence saying a Dirac term keeps it is false unless it says "modulo the Standard Model group"
(the product with the centre of su(2)_L); is the Klein twist clause right; is "no stage where it is an unbroken
non-gauge symmetry" labelled argued; nothing about the mod-16 statement may be asserted as stored or proved.
Mass terms as pair terms: read it together with the order-four proposal: its charge table (number opposite on the two
arrays; charge 2 separating Majorana from Dirac) and the order-four proposal's statements must be one consistent
structure; is "every mass is a pair term" a statement about the stored block at its pinned version; the K = 0 seesaw
relation x^2 - Mx - m^2 = 0 (recompute); is the claim about the fixed-charge gap theorem a correct reading of the stored
theorem; the statement that the 3 | n_g verdict is unchanged: proved or argued.

## Referee R2: finite averages, dark-tower coefficients, the curvature coupling
- synthesis.quarter-turn-rotors-of-the-even-subalgebra-form-a-state-design-of-order-three
- synthesis.finite-normaliser-averages-leave-the-haar-moments-at-order-four-and-on-a-parity-sector
- synthesis.field-strength-heat-kernel-coefficients-of-the-dark-towers-fix-no-scale-ratio
- synthesis.no-single-curvature-coupling-serves-the-sakharov-zero-and-the-kasner-tilt

Specific points to settle.
The two finite-average proposals overlap: rule on what each should keep (suggested: the first is the general design
statement with its exact order; the second keeps the fourth-moment excess, the parity-sector value and the failure of
bivector turns alone) and on any contradiction between them (the first reports a mode-partition mean purity 2/3 at four
generators, the second sector values and group sizes: reconcile exactly). First: is the group finite and is transitivity
proved for all N or checked for small N (Witt's theorem cited: say exactly what is assumed); recompute the second and
third moments by your own route on a small case (Cl(1,3): group of order 24; Cl(6,0): 11520); "proved given the imported
all-moment Fact": check that Fact's statement at its stored version; scope: I^2 = -1 only, generators include grades
above two from eight generators on (on ten generators bivector turns alone have orbits 45 + 210 on the 255 classes, so
are not a design: is the scope sentence adequate at every level); which stored dependants can really drop their Haar
import (second moment only), and that Page's mean entropy and the all-moment comparison cannot. Second: the fourth
moment exceeds Haar: recompute one value (13/20 against 22/35 at one mode against one); the parity-sector mean purity
(dA + dB)/(dA dB + 2): proof and one recomputation; the counts 2, 5, 16, 67, 374 against Catalan numbers are computed
and their identification with subspace counts is unproved: labelled so; the sentence on a "Bott-type dependence on the
parity of m" should be restricted (bivector-turn orbits on even classes number floor(m/2) for every m: 3; 15; 28+35;
45+210); no stored result is contradicted: verify against the two eviction results it names.
Dark towers: are these beta coefficients or heat-kernel numbers (the stored heat-kernel Fact has a logarithm only in four
dimensions): is the title and every level scoped so; recompute (d - 26)/6 and the table entries -55/6, -59/6, 32/9, 16/9,
-29/3, -31/3 from the stored content entities; "fix no scale ratio" is an independence-type claim: argued or proved, and
labelled; three-dimensional confinement by the Chern-Simons level: is that the stored statement.
Curvature coupling: recompute B over the tilt window and the zero in n_g; "three different objects" (attachment module
xi = 1/6 by its spectrum; rung doublets xi = 0 at tree level in the store; the tilt's scalar not a stored field): check
each against the stored entities at their versions; the one-field arithmetic (index 3 - sqrt(1 + 4(n_g - 3)/n_h); first
hit n_h = 14, n_g = 32) recomputed and presented as a tested hypothesis, not asserted; "no single coupling serves" in the
title: is it a theorem or a reading; numerology risk: the answer three was known in advance.
