# Maintainer pass after run 2026-11-10-phase1 (acting for Leon, the maintainer)

Leon has accepted the eight proposals of the run (now in `store/claims/`) and
approved the maintainer edits below (colony/runs/2026-11-10-phase1/DECISIONS.md, items 0 to 8). You are the one maintainer agent. Edit `store/` directly in
LAB = /home/claude/phys-graph. Never touch the user's computer; never spawn agents; never commit or push; do not delete
files with shell removal commands (retirements are done as the rules below say, and the orchestrator removes folders).

Background to read: DECISIONS.md; the referee reports verify/R1.md, R2.md (overlap rulings, "for the maintainer"
and "Only Leon can decide" items); the fixers' notes findings/fixes-*.md; findings/bridges.md.

## Rules
- Read `CONTRIBUTING.md`, `docs/CONTRIBUTING-rules.md`, `store/conventions.md`; copy the format of existing entities.
- Changing an existing entity: version + 1, keep every file in its folder (orig-proof-main.tex in particular), add a
  `maintainer_pass` entry under `extraction` with a key not already present (for example `maintainer_pass_2026_11_10`)
  with `by: maintainer-2026-11-10`, `date: '2026-11-10'` and a one-sentence note of what changed and why; keep
  `proposed_by` and `credit`. Add a credit entry {name: Claude Fable 5.2, role: <what changed>, version: <new>,
  source: maintainer pass of 2026-11-10} if the change is substantive (statement, premise wording, a bound), not for
  notes.
- An entity accepted in this run (version 1, or the two at version 4) edited only in its extraction note, uses/assumes
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
- Write colony/runs/2026-11-10-phase1/maintainer-<your name>.md: every entity changed (old -> new version, one line
  each), dependants whose CONTENT may be affected (not only pins), and anything not done and why. Your final reply is
  a short summary of that file including your layers 1-3 result.

The eight accepted entities: synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate (the
base), synthesis.chsh-over-the-rationals-pure-states-on-a-circle-and-the-pell-records,
synthesis.three-party-trade-off-of-chsh-values-and-the-local-value-two,
synthesis.signatures-in-which-commuting-observables-exceed-the-chsh-value-two,
synthesis.chsh-with-parity-even-observables-needs-two-modes-per-party-and-no-klein-twist,
synthesis.chsh-bound-needs-positivity-across-settings-and-anticommutation-holds-only-on-the-state,
synthesis.no-spin-independent-modulus-level-set-gives-the-area-law-exactly-on-slow-kerr,
synthesis.stretched-horizon-count-on-kerr-is-a-multiple-of-the-area-by-construction.

## Tasks
1. New postulate (decisions 1 and 5): id synthesis.premise-positivity-of-values, status postulate, copying the format
   of synthesis.premise-minimal-non-commutativity but NOT part of the foundation layer F1 to F4 (say so). Statement:
   hypothesis (P) exactly as the base's formal level words it (values are given by a state, a k-linear omega with
   omega(1) = 1, omega(x x-dagger) >= 0 and omega(x-dagger) = omega(x), dagger the blade inverse), stated relative to
   the split of the generators into square +1 and square -1 that defines the modes (the null pairs e_k, f_k); in
   indefinite signature another split gives another adjoint (cite the base's clause (vi)). Record its cost and what it
   does: it is what turns the operator identity into Tsirelson's bound (base clause (iii)); without it the value 4
   occurs (base clause (v) and the positivity counter-model); it extends the stored definition of a state from
   elements to functionals. Levels written; lay level plain. Then give each of the six entanglement entities an
   `assumes` edge to it (pinned @1) and replace their "to become an assumes edge" sentences; where a check then has an
   untouched premise, record it under untouched_premises in coverage.yaml.
2. New open problem (decisions 2 and 5), in store/open_problems.yaml, status open, kind research, area chosen by the
   file's conventions (clifford-structure or one-relation): op.positivity-of-values. Statement: derive (P) from the
   series' structure (for example from the record-chain account of measurement and a derived Born rule), or show it
   independent of the other premises. Known: the six results and the counter-model; the operator identity needs only
   F1 to F3; the bound is attained only with sqrt 2 adjoined and F4 is not needed. Attack items: (a) derive (P), or an
   independence proof over the full premise set (the counter-model is a functional on one algebra, not a model of the
   whole store); (b) which stored premise supplies the split that defines the adjoint in indefinite signature (the
   flag as datum, dark-matter.premise-flag-as-datum, is the candidate); (c) whether parity-odd elements are
   observables: both settings are recorded side by side (parity-even observables need two modes per party; the
   one-mode Klein-twisted realisation uses parity-odd elements, which the descent's parity average erases); (d) the
   Born weights from (P) and sharpness on a primitive idempotent, in place of the imported envariance argument
   (one-relation.imported-envariance-born-rule): argued for one state in the base, general statement open; (e) whether
   the pure-state values of the sector that meet the denominator law are the running maxima for every denominator
   (computed to 1200). Success: (P) derived or shown independent, with the split and the observables settled.
3. Kerr (decisions 3 and 8; verify/R2.md "Only Leon can decide" items 3 and 5 are decided as below):
   - synthesis.kerr-ring-count-misses-area-law: version + 1, correcting its last sentence as the referee words it
     (the small-spin sentence is wrong for rho_c < a, where the locus passes through the disc; the correct condition is
     a < rho_c with sqrt(rho_c^2 - a^2) > r_-), citing the modulus level-set result for the small-spin regime; an
     amendments entry.
   - Scope notes (no premise change): singularity.c1-curvature-cutoff and synthesis.c1-c2-forms-forced-one-number: the
     class of placements called forced fails on Kerr at both ends of the spin range (cite the two new results and the
     ring result); scrambling.mode-count and singularity.stretched-singularity-count: the wordings "accrual rate
     nu/T_H" and "keeps the horizon's clock" are Schwarzschild coincidences: on Kerr the three forms differ (ratios
     M/s, M r_+/(2 s^2), 1), cite the stretched-horizon result's clause.
   - pred.boundary-mode-density: a note that the Kerr entropy neither meets nor probes its kill condition (a horizon
     placement cannot fail; the literal cutoff placement fails at both ends of the spin range).
   - op.kerr-ring: restate `why` (the Kerr entropy is not an external test of the density), mark attack item 2 as
     answered with the two results, qualify the superradiance sentence in `known` (it concerns bosons and extending the
     state to the exterior; for the fermionic horizon modes the stored I-state theorem gives a state in every channel;
     argued, since Kerr is outside the scope of (N+)), add a dated "(10 November.)" paragraph, and an attack item: the
     inner-locus factor three (no single rho_0 serves the cutoff calibration and the horizon value; computed).
4. Window reading (decision 4): synthesis.window-reading-array-killing-energy: one scope sentence in the formal
   statement that the reading equates mean Killing energy only (version + 1, credit entry): the array's entropy
   (1/2) ln 2 and the continuum's rate times the window (pi/6 per component) are different objects and the reading
   does not equate them; energy variance differs too. op.residue-killing-weights: a new attack item: which object's
   entropy the count compares with A/4 (the array's Gibbs entropy, or an entropy constructed from the light ray's
   continuum modes), with the evidence from colony/runs/2026-11-10-phase1/findings/bridges.md (Job 1) restated without
   run names: the energy match is a fixed-point identity at window length equal to the thermal period.
5. Cross-references: in the eight new entities replace every "intended citation / sibling" sentence by a reference to
   the stored id; the stretched-horizon result already cites the modulus result. Add to
   note.singularity.monogamy-firewalls-small-corrections-theorem a sentence naming the three-party trade-off result as
   the inequality behind its use of monogamy, with the caveats that result states (same settings, parity-odd elements).
6. Other open problems, one dated sentence each where the content bears: op.residue-killing-weights (item 4 above);
   op.island-dictionary (the stored pair state at equal weights saturates the CHSH bound at suitable settings; on the
   stored thermal weights the pair's maximum is 2 sqrt(2 - r^2)); op.qft-structural-inputs is NOT touched.
Do not import literature Facts (prior art stays cited, with its checked or from-memory flags). Do not touch the
foundation postulates F1 to F4. Write colony/runs/2026-11-10-phase1/maintainer-M.md.
