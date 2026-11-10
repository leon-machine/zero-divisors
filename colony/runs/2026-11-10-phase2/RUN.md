# Run 2026-11-10-phase2: what is specific to this run

LAB = /home/claude/phys-graph (branch run/2026-11-10-phase2, stacked on run/2026-11-10-phase1, whose results are in the
store). Run folder: colony/runs/2026-11-10-phase2/ (findings/, work/<name>/, verify/). Read colony/BRIEF.md and
colony/POLICIES.md; this file overrides them. Baseline: baseline.log (0 errors, 0 warnings). Read the previous run's
colony/runs/2026-11-10-phase1/REPORT.md, DECISIONS.md and findings/bridges.md first.

## Goal
Leon approved phase 2 of the theory action plan of 10 November, with the window-reading entropy question added. Three
targets. A negative result or an independence proof established with exact checks is a full result; the plan expects
negatives on N and possibly on the Born rule. The standard on overclaiming is strict: these are headline topics.

## Cluster B: the positivity postulate and the Born rule (attackers BA constructive, BB adversarial)
Phase 1 showed the foundation gives the CHSH operator identity but not Tsirelson's bound, which needs positivity of
values; Leon adopted synthesis.premise-positivity-of-values ((P): values are given by a k-linear omega with omega(1) = 1,
omega(x x-dagger) >= 0, omega(x-dagger) = omega(x), dagger the blade inverse, relative to the split defining the modes).
Open problem op.positivity-of-values (store/open_problems.yaml; read it in full). Stored measurement account:
one-relation.record-chain-votes-measurement-without-collapse, one-relation.measure-indifference-borns-rule-located,
one-relation.imported-envariance-born-rule (imported, Zurek), the premises scrambling.indifference-structural-premise-series
and synthesis.indifference-is-curie-plus-single-valuedness, one-relation.recording-irreversible-stated-so-it-can,
one-relation.recorded-sectors-superselected-premise, one-relation.supervenience-stated-so-it-can-be,
singularity.descent-parity-average, singularity.p-univalence; the base CHSH result
synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate and the counter-model
synthesis.chsh-bound-needs-positivity-across-settings-and-anticommutation-holds-only-on-the-state; the mode split
synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product.
- B1. The Born weights from (P). Prove in the algebra: a functional satisfying (P) that is sharp on a primitive
  idempotent P (omega(P) = 1) is omega(x) = <P x>_0 suitably normalised, so the weight of an outcome projector E in
  that state is the scalar part of the product, the squared norm. State exactly what is assumed (which algebras have
  primitive idempotents of the needed kind over Q and over the completion; what "sharp" means; uniqueness), and whether
  this replaces the imported envariance argument or only relocates its content into (P) (linearity of omega across
  incompatible elements is the non-contextuality assumption of Gleason-type theorems: say so, and say which
  Gleason-type statement holds in the stored finite algebras and which fails, for example in matrix size 2).
- B2. (P) against the stored measurement premises. Is (P) derivable from indifference plus the record-chain premises,
  or from the descent's structure (the parity average is a conditional expectation: does positivity of conditional
  expectations give (P) for descended states)? Or is it independent: two models of the stored premise set (list it
  with `cone` over the measurement results), one with (P) and one without, differing on a stored statement. The phase 1
  counter-model is a functional on one algebra, not a model of the whole store: make the independence statement
  precise and say what it is independent OF.
- B3. Audit the four measurement premises (indifference, irreversible recording, superselection of recorded sectors,
  supervenience) for independence among themselves: for each, a derivation from the others or a model where it fails
  and the rest hold. Finite models with exact checks where possible; "argued" where not.
- B4 (findings unless a result drops out): which stored premise supplies the split that defines the adjoint in
  indefinite signature (dark-matter.premise-flag-as-datum is the candidate named in the open problem); whether
  parity-odd elements can be observables under the stored univalence and parity-average results.
BB adversarial: show B1 is circular (does it assume the trace form that it derives); find a state satisfying (P) that
is not of Born form (mixed states are fine: the claim is about sharp ones; test non-uniqueness, signature dependence,
the rational field); Kochen-Specker/Gleason in the stored algebras; whether "derive (P) from the descent" fails because
the descent's map is only defined on states already assumed positive.

## Cluster N: the number N (attackers NA constructive, NB adversarial)
N = M_P/H, about 10^61, carries the cosmological constant and gravity's weakness and is a registered free input
(synthesis.number-n-registered-free-input). The only stored explanation of its size is an exponential reading of the
tower (each level's objects the fermionic pairs of the level above; counts 3, 8, 256, 2^256), which is conjectured and
unproved: standard-model.why-large, refuted.the-number-n-is-a-mystery-of-largeness,
refuted.the-number-n-is-a-coincidence-dirac, standard-model.largeness-number-universes-boundary-modes,
standard-model.trichotomy-what-kind-number; the proved tower: tower.fock-module-one-qubit-per-rung,
rungs.imported-tower-one-qubit-per-rung and the tower.* results; the horizon count synthesis.de-sitter-mode-count
(about pi N^2 / ln 2 = 4.8 x 10^122 modes).
- N1. State the exponential reading as a precise mathematical claim about the stored tower (what the objects of a
  level are, what "fermionic pairs of the level above" means in the stored algebra, what is counted). If several
  precise readings are possible, state each.
- N2. Decide it against the proved tower: construct the levels exactly (verify 3 -> 8 -> 256 by computation in GA.py or
  exact combinatorics, and say what 2^256 would be), or show where the construction fails or is not canonical. First
  computation: the count at the second level against the claimed 8.
- N3. Either way: an independence statement for N with the method of the 9 November runs: a rescaling or a pair of
  models of the stored premise set (list it with `cone` over the results that mention N) that moves N and fixes every
  stored relation; say exactly which stored relations involve N and that each is preserved. Upgrade the trichotomy
  result's "observation level" reading to a proved independence if it can be, or say why not.
- N4 (findings): if the reading holds in some form, where 4.8 x 10^122 falls and whether anything in the store selects
  it; if it fails, exactly what in standard-model.why-large and the two refuted.* entities should be restated.
NB adversarial: show the reading is numerology (the sequence 3, 8, 256 depends on choices: which pairs, which level
is first, real or complex counting); find an alternative reading with equal claim that gives different counts; test
whether the independence of N survives the promoted action (Henneaux-Teitelboim) and the rung-unit register (v/M_P a
law, v/H initial data).

## Cluster W: which entropy the count compares with A/4 (attackers WA constructive, WB adversarial)
Phase 1 finding (findings/bridges.md, Job 1; recorded as an attack item on op.residue-killing-weights): the window
reading synthesis.window-reading-array-killing-energy (version 2, scoped to mean energy) matches a CAR array to a light
ray's continuum for mean Killing energy only. The array's Gibbs entropy is (1/2) ln 2
(synthesis.half-integer-weight-array-carries-half-ln2, synthesis.counted-unit-energy-at-half-offset); the continuum's
entropy rate times one window is pi/6 per chiral complex component; the store says the continuum has no window entropy
(synthesis.clausius-is-window-first-law-plus-boost-charge-conservation, synthesis.positive-null-energy-gives-r-premises).
Also: (Q) singularity.q-joint-quasi-freeness-s-wave, synthesis.null-ordering-of-counted-units-is-zeta-symmetric,
scrambling.residue-each-convention, synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping,
synthesis.array-ln2-is-zero-mode-doublet-one-tower, hawking.i-state-continuum, pred.boundary-mode-density,
op.residue-killing-weights, op.counted-mode-energy.
- W1. Make the comparison exact: the array as a chiral complex fermion on an antiperiodic circle of length equal to the
  thermal period (the square torus): its partition function, energy, entropy and energy variance in closed form
  (theta/eta at the self-dual point; exact statements with the stored theta-function Fact
  synthesis.imported-theta-function-identities if needed), against the continuum's extensive values for a window of
  r thermal periods; prove the energy match is the fixed-point identity at r = 1 and give the entropy difference as a
  function of r (the bridge-hunter's values: -0.1770 at r = 1, -0.0197 at r = 2). Exact arithmetic in checks; numerical
  integration only in proof text.
- W2. The construction the window reading's own refutation condition asks for: build the array from the continuum modes
  of a light ray over one window (a compression, a restriction to a window with a boundary condition, or the
  discretisation the reading intends), and compute the entropy of the constructed object. Does any natural
  construction give (1/2) ln 2, or pi/6, or neither; is the choice of boundary condition (antiperiodic at the thermal
  period) derived from (Q)/(N+) or put in by hand.
- W3. What the area law's S is in the store: an absolute entropy (the count's N_epoch ln 2 = S_BH) or only differences
  (the Clausius route). Decide from the stored statements which results use the absolute value, and state the
  consequence precisely: if the counted entropy is the array's Gibbs entropy, the count is internally consistent and
  the continuum plays no role in the entropy; if the continuum's entropy were demanded, the residue would change from
  1/(4 ln 2) to 3/(4 pi) units per Planck area per component (check this number and its dependence on the
  two-array unit). Say whether pred.boundary-mode-density is affected, with its kill condition quoted.
- W4 (findings): what premise would have to be added to equate entropies as well as energies, and whether any stored
  result silently assumes it (audit the results that assume the window reading: list them with `cone`).
WB adversarial: show the mismatch is real for the count (find a stored result that uses the continuum's entropy over a
window, or the array's energy variance, beyond mean energy); or show it is a category mistake at every use; test
whether a different window length or ordering convention changes the verdict; test the two-array unit.

## Bridge
One bridge-hunter midway: (P) and thermal states (KMS states are positive: does (P) for horizon arrays follow from (Q)
or (N+)); the Born weights and the array's Gibbs weights; N and the mode count pi N^2/ln 2 against the entropy
normalisation of cluster W (a change of unit per Planck area would change the count of modes for given N); the parity
average in B and the even thermal states in W.

## Gate and rules
As BRIEF.md and the previous run (colony/runs/2026-11-10-phase1/RUN.md "Gate and rules" applies verbatim with this
run's name and verify folder colony/runs/2026-11-10-phase2/verify/final): check4 exits 0 with no warnings; validate_one
ok; register with propose_claim; a proposal cannot cite another proposal; titles at most 90 characters (E124);
coverage kinds exact, complete, sampled, partial. Everything in geometric algebra (declare outside_ga otherwise, for
example kind complex-analysis for theta functions, with the unit written as a GA pseudoscalar where the store does so);
results derived, not imported, with literature as prior art checked on the web where possible and flagged where from
memory; new postulates and imported Facts are maintainer-only (list them as decisions for Leon). Lessons to apply
before filing: sampled checks support "computed", not "proved", unless the proof has a degree or basis argument;
independence and "no stored premise" claims are "argued" unless audited over the full joint cone; scope and conditions
at title, one-liner, technical and lay levels alike (W503: say "under", "given" or "assuming" at every plain level);
define every symbol once and never reuse a letter for two things; one base result per topic that siblings name as the
intended citation, without re-proving it; test signs and conventions against the store. House style: no em dashes;
never "honest"/"honestly"/"load-bearing"; Q(v) for squares; no agent or run names in store text. Credit
{name: Claude Fable 5.2, role: proposal and drafting, source: run 2026-11-10-phase2}. Up to 3 proposals per attacker,
one per target preferred; siblings read each other's findings midway and never file the same result; agree early who
files the base statement of a topic (the constructive attacker by default). labcli is slow: read entity files directly
under store/ for content; use labcli for cone, validate and propose. Run checks with PYTHONDONTWRITEBYTECODE=1. One
gate process at a time per agent (2 CPUs shared by six attackers: keep scripts light); never kill other processes; no
shell removal commands; do not edit store/, commit, push, switch branch or spawn agents. sympy is not available.
Findings: findings/attack-<name>.md (BA, BB, NA, NB, WA, WB), kill conditions pre-registered before computing, kept
current, ending with "Unexpected links" and "Decisions for Leon".
