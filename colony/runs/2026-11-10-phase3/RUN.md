# Run 2026-11-10-phase3: what is specific to this run

LAB = /home/claude/phys-graph (branch run/2026-11-10-phase3, from main after phases 1 and 2 were merged). Run folder:
colony/runs/2026-11-10-phase3/ (findings/, work/<name>/, verify/). Read colony/BRIEF.md and colony/POLICIES.md; this
file overrides them. Baseline: baseline.log (0 errors, 0 warnings). Read the REPORT.md of
colony/runs/2026-11-10-phase1 and colony/runs/2026-11-10-phase2 first.

## Goal
Leon approved phase 3 of the theory action plan of 10 November: exposure, holes and consolidation. Four independent
targets; none is expected to give a headline result, each removes a weakness. A negative result, a no-go or an
independence proof with exact checks is a full result. Do not inflate: a statement of exposure is not a derivation.
Find the stored entities yourself (labcli search_claims / find_text, then read store/claims/<id>/ directly); ids below
are starting points and may be incomplete.

## Cluster D: dark energy exposure (one attacker, DA; no pair: this is a statement, not a derivation)
The series predicts w = -1 exactly under the field-space premise (frozen point fixing Lambda; pred.* entities on dark
energy; subject dark-energy.*; synthesis.number-n-registered-free-input; the Henneaux-Teitelboim promotion). Data:
DES full analysis, June 2026, arXiv 2605.27221 (2.2 to 3.2 sigma for evolving dark energy by data combination); DESI
DR2. Check both on the web and any later release; quote numbers with their source.
- D1. State the stored prediction exactly (which entity, its kill condition as stored) and propose its form as a
  region in the (w0, wa) plane: the point (-1, 0), with the significance at which the series counts it refuted. The
  significance is Leon's decision; draft the registration text for a default of five sigma from two independent
  surveys and say what would change at other thresholds.
- D2. Trace what falls with it: list with `cone` every stored result that assumes the field-space premise or the
  frozen point, grouped by subject, and say for each group whether it falls, survives with a restated premise, or is
  untouched.
- D3. The one stored alternative, the Henneaux-Teitelboim promotion: does it permit any evolution of the dark energy
  density (it makes Lambda an integration constant: w = -1 still)? Prove the statement in the stored setting (GTG,
  geometric algebra) or cite the stored result that does. If no stored structure permits w different from -1, say
  so plainly: the series has no fallback. Search the store for anything else that could give evolution (a rolling
  modulus, the descent's deposit, the tower).
Output: at most 2 proposals (for example "exposure cone of w = -1" as an audited result; "the promoted action gives
w = -1 exactly"), the rest findings. The update of the prediction's registered kill condition is maintainer-only:
draft it in findings.

## Cluster S: the primordial spectrum (attackers SA constructive, SB adversarial)
The graph records no mechanism for the measured spectrum. Stored partial results: a sudden descent gives a feature, not
a tilt; Kasner modes are blue at tree level; the measured tilt is reached only with a fitted curvature coupling
(search: spectrum, tilt, Kasner, descent, n_s, primordial, perturbation).
- S1. List every stored structure that could source perturbations: the descent's deposit, the pre-descent Kasner
  stage, the tower's pairing modes, the boundary modes (horizon arrays, the de Sitter mode count), the frozen point's
  moduli, anything else found.
- S2. For each: the spectral index it gives with NO fitted number, by exact computation in GTG/GA where a mode
  equation is stored or derivable (power-law backgrounds give Bessel indices: exact rational arithmetic on the index),
  or a proof that it gives no spectrum (no long-wavelength modes, wrong statistics, no coupling to curvature
  perturbations).
- S3. Conclude: one surviving candidate with its first computation, or a no-go over the stored structures with the
  list audited. Pre-registered kill: no structure gives a red tilt (n_s < 1, measured about 0.965) without a fitted
  number; then the series needs a new premise, which is Leon's decision. A red tilt obtained by choosing a parameter
  is a fit, not a result: say which parameter and its stored status.
SB adversarial: for each candidate SA keeps, find the hidden fitted number or the missing step (amplitude, statistics,
conversion to curvature perturbations, the horizon problem without inflation); for each SA kills, check the kill is
not an artefact of tree level or of the gauge; look-elsewhere accounting if several structures are tried; check
whether the de Sitter boundary modes give a scale-invariant spectrum by the stored thermal state and whether that is
already the standard de Sitter result in disguise (prior art on the web).

## Cluster M: dark-matter premise reduction (attackers MA constructive, MB adversarial)
The dark-matter subject holds 23 of the graph's postulates and supports essentially one fitted ratio, 5.364
(subject dark-matter.*; postulates have status postulate; the ratio result and slices/dark-tower entities).
- M1. Build the dependency table of the dark-matter postulates: which results use which (labcli cone/neighbourhood
  over every dark-matter postulate), which postulates are used by nothing or by one result only, which are used
  outside the subject.
- M2. For each postulate: a derivation from the others plus the foundation (then it is a theorem and can be retired
  as a postulate), or a model where it fails and the rest hold (then it is independent), or "undecided" with what
  decides it. Exact checks where a finite model exists; "argued" where not.
- M3. Equivalences: postulates that say the same thing in different words or differ only by convention; propose
  merges. Postulates that are definitions or conventions in disguise: say so.
Pre-registered kill: none is redundant; then the count stands as the cost of the fit and is recorded as such.
MB adversarial: test every derivation MA offers for circularity through the cone; test every "equivalent" pair for a
separating model; check whether the ratio 5.364 moves if a supposedly redundant postulate is dropped; count the fit
truthfully (postulates per fitted number, and how many of the postulates were added after the number was known:
versions and dates in the entities). Retirements and merges of postulates are maintainer-only: list them as
decisions for Leon. Split the 23 between MA and MB early so each postulate has one owner and one challenger.

## Cluster Q: quantum field theory scope (attackers QA and QB, each constructive on its own items and adversarial on
the other's)
No route to a non-perturbative interacting theory exists in the graph; this cluster completes what is perturbative
and records the limit.
- Q1 (QA). The one-loop electron self-energy and vertex by extension of distributions (Epstein-Glaser style, as the
  stored vacuum polarisation: find it and copy its method and conventions), in geometric algebra (no Dirac matrices
  where the store uses GA; declare outside_ga where it does not), with the Ward identity between vertex and
  self-energy checked exactly on the extended distributions and the freedom (finite renormalisations) counted. First
  computation: the scaling degrees and the number of free constants for each.
- Q2 (QB). The local-covariance Fact imported on 10 November (search: local covariance, Hollands-Wald, curved-field
  freedom): use it to reduce the curved-field renormalisation freedom to constants and close the clause left
  argued in the stored curved-field result; say exactly which clause and what the Fact supplies.
- Q3 (QB). The protraction identity (the curl of the vierbein/gauge field vanishing in the form used by the stored
  GTG results) derived in the algebra core from vanishing torsion: find where it is assumed but not stored
  (docs/ALGEBRA_CORE.md and the GTG entities), state it, prove it, exact check on a sample of gauge fields.
- Q4 (QA, findings; a note is maintainer-only): what a full theory would need that the series lacks (a covariant
  regulator, or a continuum limit of the rotor lattice; constructive results in low dimension as prior art), so later
  runs do not reopen it. Draft the note text.
Adversarial halves: QB tests Q1 (is the Ward identity checked or imposed; gauge parameter dependence; infrared
regularisation hidden in the extension; whether the GA form adds anything to the textbook result); QA tests Q2 and
Q3 (does the Fact as imported cover the stored class of fields and states; is the protraction identity already
stored under another name; is the proof a restatement of a definition).

## Gaps to record (maintainer at close-out; attackers only report what they meet)
New open-problem entries, subject to Leon's confirmation: strong CP, matter asymmetry, quantised graviton. A
literature check of the experimental status of gravity-mediated entanglement for the stored gravity-entangles
prediction (DA does this on the web as a side task: what has been measured, at what sensitivity, with sources).

## Bridge
One bridge-hunter midway (for example: the de Sitter boundary modes in S against the window results of phase 2; the
dark-matter postulates against the dark-energy exposure cone; local covariance against the horizon states; the
protraction identity against the dark-matter slices).

## Gate and rules
As colony/runs/2026-11-10-phase2/RUN.md "Gate and rules", verbatim with this run's name and verify folder
colony/runs/2026-11-10-phase3/verify/final; the lessons listed there apply before filing. In addition, from phase 2's
referees: cite stored results that already hold part of the statement (search before claiming novelty); a check must
be able to fail (no identities as checks); when a referee or sibling is right, restate rather than defend. Credit
{name: Claude Fable 5.2, role: proposal and drafting, source: run 2026-11-10-phase3}. Up to 3 proposals per attacker
(2 for DA). 2 CPUs are shared by seven attackers: keep scripts light, one gate process at a time per agent, guard
large powers, never kill other processes, no shell removal commands; do not edit store/, commit, push, switch branch
or spawn agents. Findings: findings/attack-<name>.md (DA, SA, SB, MA, MB, QA, QB), kill conditions pre-registered
before computing, kept current, ending with "Unexpected links" and "Decisions for Leon".
