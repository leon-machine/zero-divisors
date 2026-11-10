# Maintainer pass after run 2026-11-09-solvable (acting for Leon, the maintainer)

Leon has accepted all fifteen proposals of the run (now in `store/claims/`) and approved the maintainer edits below
(colony/runs/2026-11-09-solvable/DECISIONS.md and his close-out answers). You are one of two maintainer agents, each
owning a disjoint set of files (your message lists yours). Edit `store/` directly in LAB = /home/claude/phys-graph. Never
touch the user's computer; never spawn agents; never commit or push.

Background to read: the referee reports colony/runs/2026-11-09-solvable/verify/R1.md and R2.md (overlap rulings and the
maintainer items), the fixers' notes findings/fixes-*.md ("for the maintainer" items), FIXROUND.md and DECISIONS.md.

## Rules
- Read `CONTRIBUTING.md`, `docs/CONTRIBUTING-rules.md`, `store/conventions.md`; copy the format of existing entities.
- Changing an existing entity: version + 1, keep every file in its folder (orig-proof-main.tex in particular), add a
  `maintainer_pass` entry under `extraction` (use a distinct key such as `maintainer_pass_2026_11_09` if one exists) with
  `by: maintainer-2026-11-09`, `date: '2026-11-09'` and a one-sentence note of what changed and why; keep `proposed_by` and
  `credit`. Add a credit entry {name: Claude Opus 5.5, role: <what changed>, version: <new>, source: maintainer pass of
  2026-11-09} if the change is substantive (premise wording), not for notes.
- A new entity accepted today (version 1) edited only in its extraction note or derivations (assumes edges, citations)
  stays at version 1 only if `tp check` layers 1-3 accept that; otherwise bump to 2.
- assumes edges: the list `assumes:` under the derivation, pinned `id@version` (see store/claims/dark-energy.imported-walls-sphere-theorem/entity.md).
- House style: no em dashes; never "honest"/"honestly"/"load-bearing"; Q(v); macros only from store/notation.yaml; no
  agent, run or method names in store text (`by:` fields excepted).
- After changing a check: `PYTHONDONTWRITEBYTECODE=1 python3 colony/runcheck.py <folder>/check.py` and
  `python3 colony/check4.py <folder>` (one at a time; 2 CPUs shared).
- Validation after your edits: `PYTHONDONTWRITEBYTECODE=1 python3 -m tp check --store store --layers 1,2,3 --keep-going
  --author leon 2>&1 | tail -40`; fix every error or new warning on YOUR files; ignore findings that are only the other
  agent's. Do not run the full check, `tp repin`, `tp lock` or `tp build` (the orchestrator does).
- Write colony/runs/2026-11-09-solvable/maintainer-<your name>.md: every entity changed (old -> new version, one line
  each), dependants whose CONTENT may be affected (not only pins), and anything not done and why. Your final reply is a
  short summary of that file.

## M1: premises and stored entities
1. hawking.joint-j3-s-wave-reduction: narrow to spin 2 (the graviton's channels) and the current-boson identification;
   spins 0, 1/2 and 1 now follow from synthesis.horizon-channels-of-scalar-dirac-and-maxwell-fields-are-two-dimensional
   (cite it; channel-reduction clause only). List dependants whose content changes.
2. standard-model.slot-module-hypothesis clause (f): restate as "the ten slot and pair Majoranas (slots Klein-twisted)
   are distinct directions of one group of signed directions (F2) and (F3), the sign bit acting as -1", citing
   synthesis.joint-clifford-clause-is-an-instance-of-the-signed-direction-postulates and the Klein-convention result;
   flag the identification of the direction labels with F1's distinctions as a reading. List dependants.
3. synthesis.mass-ordered-dressing-cannot-spoil-koide: correct the last sentence of (iv) (it already covers D2 > D3 > D1).
4. dark-matter.stored-asymmetry-charge-not-number: pi N^2/ln 2 counts registered units; the light rays number
   2 pi N^2/(c ln 2) (wording; conclusions unaffected).
5. dark-matter.r2-one-quantum-per-unit-ball (or R2's id; find it): "(2, 3 or 4)" reads "(under P3, 2, 3 or 4)".
6. P3 (find its id): add a note: its lowest-causal clause follows from Premise U at residues 1 and 7 and is independent
   of the descent at residues 3 and 5 (synthesis.bott-shifted-model-leaves-the-odd-towers-dimension-free).
7. synthesis.lens-space-wall-rung-count-sees-the-integral-twist: limit the lay sentence "on an indefinite side the simple
   twist class sets the price" to dimension 3 (on lens walls of dimension 5 and more it fails:
   synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial).
8. synthesis.rung-unit-second-free-number: a note citing synthesis.d-term-level-free-at-fixed-n (no content change).

## M2: the fifteen new entities and the open problems
1. assumes edges (Leon approved): add (Q) v3 (singularity.q-joint-quasi-freeness-s-wave@3; check the id) and the window
   reading (synthesis.window-reading-array-killing-energy@1) to
   synthesis.one-window-parity-recurrence-of-the-light-ray-sea-needs-twenty-four-arrays and
   synthesis.light-ray-recurrence-test-verdict-on-generations-is-set-by-the-scalar-content; (Q), C2 (check its id and
   version) and the window reading to synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping;
   Premise U (dark-tower-matter.u-transposition-rule, check the version) to
   synthesis.bott-shifted-model-leaves-the-odd-towers-dimension-free. Remove the corresponding "assumes edge for the
   maintainer" sentences from their extraction notes. Each fixer's notes name these.
2. Cross-references among siblings (the referees' overlap rulings; proposals could not cite each other): replace each
   "intended citation ... sibling" sentence in the new entities' extraction notes by a plain cross-reference to the now
   stored id. Do not restructure proofs or checks.
3. store/open_problems.yaml (header comment gives the format): for each problem a dated "(9 November.)" paragraph in
   `known` with \claimref to the new entities, attack items marked done or restated, `entities` lists extended, `source`
   extended with "the 9 November results and Leon's decisions". Problems stay partial unless settled outright:
   - op.wall-class-invariant: item 1 answered negatively (k > ht on lens walls from dimension 5, unbounded excess; both
     results; they rest on classical lens-space facts cited from memory); add an attack item "derive the lens-space
     cohomology rings, q1 and the K-ring in the store (Leon's decision: derive, not import)". The dim <= 3 table item
     stays (it needs a Fact; note Leon's no-import decision).
   - op.helicity-per-boundary-mode: channel reduction proved for spins 0, 1/2, 1 (horizon channels result); spin 2 open;
     correct the known text: potentials go as 1 - 2M/r for spins 0 and 1, as sqrt(1 - 2M/r) for spin 1/2; J3 narrowed.
   - op.odd-towers: item 1 already answered in the store (dark-tower-matter.constituents-field,
     dark-tower-matter.where-mass-begins, the three- and five-dimensional content entities): mark it done.
   - op.qft-non-abelian-gauge-fields: Virasoro relations on the band (the Virasoro attack item done, band domain only);
     Higgs-sector BRST: the differential and 't Hooft-Feynman gauge with a stationary vacuum, and BRST does not fix the
     breaking pattern (the potential does); the Higgs-sector item restated to the interacting theory.
   - op.hypothesis-s: the sign-bit item done; clause (f) restated (M1 does the premise).
   - op.gram-square-and-face-space: item 1 closed negatively for QCD-type dressing (middle-mass bound); the
     selectivity account for quarks dropped unless a dressing law favouring the heaviest quark is proposed.
   - op.counted-mode-energy and op.qft-structural-inputs: the recurrence test stated (24 arrays, a choice independent of
     the cone by two models; verdicts under the two readings); Leon's decision: a test, not a premise; the "78" case is a
     reading, not a stored result.
   - op.window-p3: split by residue (1, 7 from Premise U; 3, 5 independent: the window there an input); the pairing-reading
     item stays.
   - op.thickness-deposit-rule: item 1 done on the orbit reading of licensing; the fit moves to the asymmetry eps
     (T = 1 + 4/eps reaches 5.364 at eps about 0.917).
   - op.residue-killing-weights: the residue needs a mean of two arrays per unit and fixes no grouping (replaces the
     "N copies" form); the count unit stays a decision.
   - op.pair-sector-current: item 3 done: the 126 weight is free on the stored relations, so the second family's factor 3
     is an input of the record.
   - op.rung-unit: xi G free at fixed N (model pair), consistent with the register.
   Validate the YAML (python3 -c "import yaml; yaml.safe_load(open('store/open_problems.yaml'))").
