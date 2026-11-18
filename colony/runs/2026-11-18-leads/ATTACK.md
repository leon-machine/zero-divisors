# Attacker brief, run 2026-11-18-leads

Read in this order: colony/BRIEF.md (sections Tools, Standards, Role: attacker), colony/POLICIES.md, this run's
RUN.md, then your cluster's section below. The previous run's results are stored and merged; its reasoning is in
colony/runs/2026-11-18-navigate/ (REPORT.md, findings/attack-main.md, verify/R1.md to R3.md). Read what bears on
your cluster before computing: several of your leads were written there.

You work both angles: try to prove, and try as hard to refute or to show independence. For each lead of your
cluster you end with exactly one of: a filed proposal; a negative or independence result with its computation in
the findings; "out of reach" with the reason and the first step someone would need. Do not skip a lead silently.

Orientation is by lookup: `python3 colony/labcli.py get_open_problem '{"id":"op...."}'`, `get_claim`, `get_proof`,
`search_claims`, `find_text`, `cone`. Do not read whole files you do not need.

Filing: at most three proposals. A proposal is a claim (proposition, theorem, or a correction of a stored entity
that keeps every stored file) with entity.md at four levels, proof-main.tex, check.py in exact arithmetic with
`import GA`, coverage.yaml; `validate_draft` ok and `check4.py` exit 0 before `propose_claim`. A helper that builds
the draft json from the three files is colony/runs/2026-11-18-navigate/work/main/mkdraft.py (read it; copy and
adapt). Session name: 2026-11-18-leads. Work files go in colony/runs/2026-11-18-leads/work/<cluster>/, findings in
colony/runs/2026-11-18-leads/findings/attack-<cluster>.md. A filed proposal cannot be overwritten by propose_claim;
to change it edit the files in place under proposals/<id>/.

Standards that referees enforced last time, so meet them now:
- Theorem and Proof only for what the proof proves. Anything quoted from the literature from memory is flagged as
  such in the text and is not used in a proof step; if a step needs it, say the result is conditional on it.
- State every hypothesis in the statement; no clause stronger than its proof; a toy model's conclusion is not
  carried to the full theory without saying it is argued.
- Checks must fail when a stored number is perturbed; sample grids and constants at module level.
- Geometric algebra throughout (spacetime algebra, gauge theory gravity): no bare imaginary unit; pseudoscalars
  and bivectors instead. Where a computation is outside the algebra, declare it in coverage.yaml.
- House style: no em dashes; never "honest", "honestly", "load-bearing"; Q(v) for the square of a vector; declared
  macros only (store/notation.yaml); no agent, run or method names in store text.

Final reply (under 400 words): per lead, what was established (proved, computed, argued, refuted, out of reach),
proposal ids, kill conditions and outcomes, links to other clusters' problems you noticed, decisions that only
Leon can make.

## Cluster W: walls
Start: `get_open_problem op.eigenbundle-class-of-degenerations`, `get_claim` and `get_proof` of
synthesis.strict-completions-exist-exactly-when-the-signature-does-not-jump, then synthesis.wall-class-one-rung-
obstruction, sheaf.wall-class, synthesis.kerr-ring-double-cover-data,
synthesis.kerr-ring-blow-up-forced-cover-fixed-order,
synthesis.kerr-ring-connection-limit-null-rotation-winding-three, std-algebra.periodicity.
Leads:
1. m = 3: multiplication by the position vector on the least module of Cl(3,0) (dimension four). Show in an exact
   model that the positive eigenbundle over the two-sphere is not stably trivial as a real bundle, or find that it
   is. (It is a complex line bundle of degree one read as a real plane bundle; what has to be exact is an invariant
   that survives stabilisation, for instance the second Stiefel-Whitney class computed from a clutching function
   or from a cell model. If only the unstable statement is reachable, say so.) Consequence to state: no completion
   with a fixed exterior form on the same module, and on which larger modules it reappears.
2. Tame walls: compute the relative class of the eigenbundles of a tame corank-one wall and compare with
   (w(Sigma), w_1(L)) of the stored theorem and with the stored lens-space rung counts. Agreement, disagreement, or
   the new class is strictly coarser or finer: each is a result. If they agree, draft the restatement of
   sheaf.wall-class clause (c) so that it no longer cites the refuted conjecture.
3. Kerr ring: is the forced double cover the degree-one class of the two-dimensional example [[x,y],[y,-x]]? Is
   the winding number three an invariant of a completion, or only stable modulo two (or not an invariant at all)?
   Kill condition to register: the stored winding is defined for a connection, not a form, and no completion
   statement applies to it.
4. Sufficiency over a contractible base with an isolated degeneration (fourth attack item).
5. Two claims from the impact assessment, to test and not to assume: (a) a degeneration of even rank jump with
   equal residues modulo eight (x times the identity in rank four) is invisible to the tower classification, and
   what that means for any stored statement that reads walls off the tower's residues; (b) the link to
   op.order-four-anomaly-and-sixteen through real K-theory: is there one, or is it a resemblance.

## Cluster G: the gravitational field
Start: `get_open_problem op.gravitational-field-at-null-momentum`; the two stored results of 18 November
(synthesis.gravitational-pair-production-from-the-operator-source-at-first-order,
synthesis.field-slaved-to-an-operator-source-does-not-commute-at-spacelike-separation); store/conventions.md,
section "Gravity and the graviton"; field-theory.operator-newtonian-coupling;
field-theory.no-canonical-commutation-relations-tower; the cutoff premises (find_text "(C1)");
pred.gravity-entangles-standard-phase and pred.dimmed-evaporation-bursts.
Leads:
1. State the condition: does any stored premise, or the unitarity behind the registered prediction, imply
   commutation of the field with matter observables at spacelike separation? A list of what the store does and
   does not imply, with the entities, is the result.
2. The localisation floor: do (C1), (C2) or the finite count of boundary modes bound localisation so that the
   lattice model's failure cannot be observed? Derive a bound, or give a counter-model inside the stored premises.
   Register before computing what "cannot be observed" means quantitatively (a signalling probability against the
   detector's size and the coupling).
3. Repeat the lattice model with a constraint: instantaneous part fixed by a constraint, observables dressed, first
   order. Does the dressed observable commute at spacelike separation where the bare one did not? Exact arithmetic.
4. The free part: is it the two null-momentum components (count them in the stored Einstein-map kernel: 6 at null
   momentum against 4 gauge), and what does each option do to the burst baseline's term g? Give the basis of
   pred.dimmed-evaporation-bursts under each option; do not choose.
5. The trace-free channel item of op.einstein-from-the-field-theory: what the operator-source result does and does
   not say about it.

## Cluster H: heating, couplings, scrambling
Start: clause (v) and the channel weights of synthesis.gravitational-pair-production-from-the-operator-source-at-
first-order; `get_open_problem op.curvature-coupling-across-subjects` and
synthesis.no-single-curvature-coupling-serves-the-sakharov-zero-and-the-kasner-tilt;
synthesis.weyl-flat-variations-carry-only-the-stress-trace-and-the-whole-stress-clause-is-the-trace-free-channel
clause (v); scrambling.spreading-law-chaos-bound-saturated, scrambling.return-delay-scrambling-log-recovered,
synthesis.affine-cell-boost-spreads-without-scrambling.
Leads:
1. The curvature coupling in the heating: the scalar weights carry tau = (1 - 6 xi)^2. Which stored xi applies to
   which scalar of the bath and of the dark content (rung-field doublets at tree level 0, attachment module at the
   conformal value, the tilt window near 1.5)? Compute the rate coefficients and the floor's dependence across the
   stored values; say whether any stored conclusion that uses the rate (the floor, the Pati-Salam exclusion, the
   untuned fit) moves by more than its stated margin, and whether the heating constrains the open datum. The
   floor's entities are being restated by another agent: report numbers in the findings, propose a new result if
   there is one, do not correct those entities.
2. The trace part of the fermion channel at next order: size it. Either compute the leading correction to the
   chiral-fermion coefficient from the stored trace statement, or show it is of higher order in the coupling than
   anything the store uses and say which order.
3. Scrambling: is the spreading half of scrambling.spreading-law-chaos-bound-saturated proved by the stored
   synthesis result, on what scope exactly, and what remains an estimate? Draft the correction that restates the
   first on the proved scope (a status change is flagged for Leon, so state the case plainly) and say what open
   problem should hold the second.

## Cluster L1: horizons
Start: colony/runs/2026-11-16-anomaly/LEADS.md and REPORT.md (the leads of 16 November on these two problems);
`get_open_problem op.which-capacity` and `op.helicity-per-boundary-mode`; then the entities they list.
Leads:
1. op.which-capacity, two horizons: in the Schwarzschild-de Sitter field compute the tube points the adopted clause
   fixes for each horizon's wedge and decide between per-observer and per-horizon assignment, or show the clause
   does not decide.
2. op.which-capacity, Schwarzschild: is a finite rho selected by the symmetries commuting with the horizon's boost?
3. op.helicity-per-boundary-mode: the remaining spin-2 item (read the restated item; the odd-parity reduction is
   stored) and the partial-wave identification from the fuzzy sphere. Take the one the leads of 16 November call
   nearest.
Cross-link to test: the operator-source result counts two undetermined components at null momentum; the horizon
channels of the linearised gravitational field are stored as two-dimensional. Same two, or a coincidence?

## Cluster L2: values
Start: colony/runs/2026-11-16-anomaly/LEADS.md and REPORT.md; `get_open_problem op.positivity-of-values`; the
entities it lists.
Leads:
1. The Gleason-type item: are non-negative additive weights on the projectors with rational coefficients of two
   modes (size four over Q) restrictions of linear functionals? Prove, or give an exact counter-model.
2. The running-maxima item: pure-state values meeting the denominator law with equality. Prove the pattern, or find
   the first failure, or bound where a failure can occur.
3. Parity-odd observables: sharpen the choice (what each setting costs), without choosing.
4. Independence of (P): what a proof would need beyond the stored counter-model; attempt it.
Cross-link to test: the lattice model of 18 November has a matter algebra Cl(1,1) with commuting numbers; does
positivity of values on it constrain the slaved field's commutator, or is it silent?
