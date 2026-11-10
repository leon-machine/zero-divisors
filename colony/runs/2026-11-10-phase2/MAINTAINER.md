# Maintainer pass after run 2026-11-10-phase2 (acting for Leon, the maintainer)

The twelve proposals of the run are in `store/claims/` on branch run/2026-11-10-phase2, and Leon approved the edits
below (colony/runs/2026-11-10-phase2/DECISIONS.md). Two maintainer agents with disjoint files: MB (positivity and the
Born rule) and MN (the number N and the window reading). Edit `store/` directly in LAB = /home/claude/phys-graph. Never
touch the user's computer; never spawn agents; never commit or push; no shell removal commands (a retirement is done as
colony/runs/2026-11-09-bridges/MAINTAINER.md did it for an imported Fact: read how, follow it, and leave folder removal
to the orchestrator, listing it in your report).

Background to read: DECISIONS.md; verify/R1.md, R2.md, R3.md (overlap rulings and "for the maintainer" items); the
fixers' notes findings/fixes-*.md; findings/bridges.md; findings/attack-*.md sections "Decisions for Leon".

## Rules
- Read `CONTRIBUTING.md`, `docs/CONTRIBUTING-rules.md`, `store/conventions.md`; copy the format of existing entities.
- Changing an existing entity: version + 1, keep every file in its folder (orig-proof-main.tex in particular), add a
  `maintainer_pass` entry under `extraction` with a key not already present (for example `maintainer_pass_2026_11_10`)
  with `by: maintainer-2026-11-10`, `date: '2026-11-10'` and a one-sentence note of what changed and why; keep
  `proposed_by` and `credit`. Add a credit entry {name: Claude Fable 5.2, role: <what changed>, version: <new>,
  source: maintainer pass of 2026-11-10} if the change is substantive (statement, premise wording, a bound), not for
  notes.
- An entity accepted in this run (version 1) edited only in its extraction note, uses/assumes
  edges or citations stays at its version if `tp check` layers 1-3 accept that; otherwise bump.
- assumes edges: the list `assumes:` under the derivation, pinned `id@version` (see
  store/claims/dark-energy.imported-walls-sphere-theorem/entity.md). When an in-statement hypothesis becomes an
  imported Fact, cite the Fact and keep the hypothesis's label in the text. If a check then has an untouched premise,
  record it under `untouched_premises` in coverage.yaml as earlier passes did.
- House style: no em dashes; never "honest"/"honestly"/"load-bearing"; Q(v); macros only from store/notation.yaml; no
  agent, run or method names in store text (`by:` fields excepted).
- After changing a check: `PYTHONDONTWRITEBYTECODE=1 python3 colony/runcheck.py <folder>/check.py` and
  `python3 colony/check4.py <folder>` (one at a time; 2 CPUs shared).
- Validation after your edits: `PYTHONDONTWRITEBYTECODE=1 python3 -m tp check --store store --layers 1,2,3 --keep-going
  --author leon 2>&1 | tail -40`; fix every error or new warning on YOUR files. Do not run the full check, `tp repin`, `tp lock` or `tp build` (the orchestrator does).
- Write colony/runs/2026-11-10-phase2/maintainer-<your name>.md: every entity changed (old -> new version, one line
  each), dependants whose CONTENT may be affected (not only pins), and anything not done and why. Your final reply is
  a short summary of that file including your layers 1-3 result.
- Where an instruction below turns out to be false to the mathematics as stored, do not force it: do the true weaker
  edit, and report the difference for Leon.

## MB: positivity and the Born rule
The six: synthesis.born-weights-under-positivity-a-state-sharp-on-an-atom-is-its-trace-functional (base),
synthesis.positivity-of-values-is-additivity-of-non-negative-weights-on-effects,
synthesis.splits-adapted-to-the-null-pairs-and-the-states-common-to-all-of-them,
synthesis.local-weights-give-the-chsh-bound-and-do-not-fix-positivity-of-values,
synthesis.records-keep-even-states-even-only-for-parity-homogeneous-observables,
synthesis.no-two-valued-weights-on-the-atoms-of-two-modes-the-even-subalgebra-admits-them.
B1. Citations among the six: every "intended citation" sentence left in an extraction note or text becomes a uses edge
    and claimref where the cited result is used in a proof step, or a lineage entry where it is comparison only (R1
    "Structure and overlaps"). Add the assumes edge synthesis.premise-positivity-of-values at its current version to
    each of the six that uses (P) and lacks it (records in particular).
B2. Leon's decision 4, replace the import. one-relation.measure-indifference-borns-rule-located rests on
    one-relation.imported-envariance-born-rule. Read both, their proofs and the base. New version of the
    measure-indifference result in which the in-store route (under (P), a state sharp on an atom is the scalar-part
    functional, base clause (iii)) takes the place of the imported envariance argument. Say at every level: this is
    not a derivation of the Born rule; the non-contextuality assumption (linearity of values across non-commuting
    elements) is relocated into (P), not removed; sharpness on an atom is assumed; physical states are not shown to
    be sharp. State exactly what the new route covers (which algebra, which states and projectors) against what the
    stored proposition claims (the squared-norm measure on the conserved Dirac density under indifference). If the
    new route does not cover the stored statement as worded, narrow the statement to what it covers, keep the
    envariance argument named as prior art (Zurek) in lineage and text, and report the gap plainly. Then retire the
    imported Fact if nothing else rests on it (check with neighbourhood and a text search of store/ for its id,
    including notes, open problems and tombstones); if something else does, leave it and report.
B3. The stored (P) premise synthesis.premise-positivity-of-values: the first sentence of "What it costs, and what it
    leaves open" ("... cannot be dropped ...") is too strong (local-weights result, R1 finding 3): restate with "in
    the one-mode realisation, local weights already give the bound; positivity across settings is what the box
    violates", citing the local-weights result; the same for the two other stored phrases listed in the local-weights
    extraction note (the title of the stored box theorem among them: retitle only if the id rules allow; ids never
    change). Add to the premise a pointer to the effects result (what (P) says in terms of weights) and to the splits
    result (the split is fixed by the stored null pairs as vectors).
B4. op.positivity-of-values in store/open_problems.yaml: record what is now settled (weights under (P) and sharpness;
    (P) is additivity of non-negative weights on effects; the parity average creates no positivity; no two-valued
    weights on rational atoms of two modes; local weights do not fix (P); the split is fixed by the null pairs) and
    what stays open (a derivation of (P) or of sharpness from the measurement premises; which observables are
    physical: the record reading is a reading, recorded side by side with the stationary-implies-even theorem; Gleason
    over Q in size 4 undecided). Keep it open. Follow the file's format for `known` and attack items.
B5. Update one-relation.record-chain-votes-measurement-without-collapse and any other dependant only if its CONTENT
    is affected by B2; report rather than edit where unsure.

## MN: the number N and the window reading
The six: synthesis.exponential-reading-of-the-tower-is-the-iterated-fock-functor-not-the-ascent (base),
synthesis.invariant-forms-on-the-fock-module-and-the-pair-counts-of-a-next-level,
synthesis.number-n-free-at-fixed-d-term-level-on-the-stored-relations,
synthesis.antiperiodic-array-against-the-light-ray-continuum-at-window-length-r (base),
synthesis.light-ray-continuum-is-the-twist-integral-of-arrays-and-window-values-are-twist-averages,
synthesis.window-energy-tests-with-free-spacing-admit-twists-half-third-and-quarter.
N1. Citations among them as in B1.
N2. Leon's decision 1. New versions of standard-model.why-large and refuted.the-number-n-is-a-mystery-of-largeness:
    the exponential reading (3, 8, 256, 2^256) is the iterated Fock construction, not a step of the proved ascent;
    it is one of at least two counting rules (the second, from the invariant forms: 3, 4, 8, 128, 2^127), and nothing
    stored selects one (argued); the base count three is a complex count on the (2,4) space against a real count on
    Cl(3,3); the horizon count is of registered units, a comparison of sizes only; N stays a registered free input
    (cite synthesis.number-n-registered-free-input and the N-free result). Keep each entity's kind and status rules
    (a refuted.* entity stays what it is; change the wording of what the reading supports). Check
    standard-model.largeness-number-universes-boundary-modes, standard-model.trichotomy-what-kind-number and
    refuted.the-number-n-is-a-coincidence-dirac for sentences that now overstate; edit only those sentences.
    No new open problem.
N3. Leon's decision 2. Version 3 of synthesis.window-reading-array-killing-energy: the energy equalities hold at a
    window of exactly one thermal period and at spacing kappa (R3 maintainer note: "What it is for (i)" and
    refutation condition (b)); the array is the twist one-half fibre of the light-ray continuum, not a
    Killing-invariant subsystem, and non-invariant subalgebras can carry the same occupations for any twist and
    select none; the antiperiodic condition and the spacing are inputs of (Q), not derived; cite the three window
    results. Then check every dependant of the window reading (cone) for content affected and report.
N4. Leon's decision 3. In store/open_problems.yaml close attack item 4 of op.residue-killing-weights in the file's
    own format for a closed item: the count compares the array's own Gibbs entropy with A/4; the continuum's
    entropy never enters; the counterfactual residue 3/(4 pi) per unit of two components is recorded as NOT adopted,
    citing the window base clause (v). The problem itself stays open. pred.boundary-mode-density is not changed;
    confirm its kill condition is not met and say so in your report.
N5. op.counted-mode-energy and op.residue-killing-weights `known` fields: add one line each on what the window
    results settle, if the file's format has a place for it.
