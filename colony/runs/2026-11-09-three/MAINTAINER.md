# Maintainer pass after run 2026-11-09-three (acting for Leon, the maintainer)

Leon has accepted all three proposals of the run (now in `store/claims/`) and approved the maintainer edits below
(colony/runs/2026-11-09-three/DECISIONS.md and his close-out answers). You are the one maintainer agent. Edit `store/` directly in LAB = /home/claude/phys-graph. Never
touch the user's computer; never spawn agents; never commit or push.

Background to read: the referee reports colony/runs/2026-11-09-three/verify/R1.md (overlap rulings and the
maintainer items), the fixers' notes findings/fixes-*.md ("for the maintainer" items), FIXROUND.md and DECISIONS.md.

## Rules
- Read `CONTRIBUTING.md`, `docs/CONTRIBUTING-rules.md`, `store/conventions.md`; copy the format of existing entities.
- Changing an existing entity: version + 1, keep every file in its folder (orig-proof-main.tex in particular), add a
  `maintainer_pass` entry under `extraction` (use a distinct key such as `maintainer_pass_2026_11_09` if one exists) with
  `by: maintainer-2026-11-09`, `date: '2026-11-09'` and a one-sentence note of what changed and why; keep `proposed_by` and
  `credit`. Add a credit entry {name: Claude Fable 5.2, role: <what changed>, version: <new>, source: maintainer pass of
  2026-11-09} if the change is substantive (premise wording), not for notes.
- A new entity accepted today (version 1) edited only in its extraction note or derivations (assumes edges, citations)
  stays at version 1 only if `tp check` layers 1-3 accept that; otherwise bump to 2.
- assumes edges: the list `assumes:` under the derivation, pinned `id@version` (see store/claims/dark-energy.imported-walls-sphere-theorem/entity.md).
- House style: no em dashes; never "honest"/"honestly"/"load-bearing"; Q(v); macros only from store/notation.yaml; no
  agent, run or method names in store text (`by:` fields excepted).
- After changing a check: `PYTHONDONTWRITEBYTECODE=1 python3 colony/runcheck.py <folder>/check.py` and
  `python3 colony/check4.py <folder>` (one at a time; 2 CPUs shared).
- Validation after your edits: `PYTHONDONTWRITEBYTECODE=1 python3 -m tp check --store store --layers 1,2,3 --keep-going
  --author leon 2>&1 | tail -40`; fix every error or new warning on YOUR files;  Do not run the full check, `tp repin`, `tp lock` or `tp build` (the orchestrator does).
- Write colony/runs/2026-11-09-three/maintainer-<your name>.md: every entity changed (old -> new version, one line
  each), dependants whose CONTENT may be affected (not only pins), and anything not done and why. Your final reply is a
  short summary of that file.

## M: the tasks (Leon's decisions are in DECISIONS.md, numbered as below)
Use a `maintainer_pass` key distinct from any existing one (for example `maintainer_pass_2026_11_09b`) where an entity
already carries one from this morning's pass.

1. New imported Fact (decision 1): the Atiyah-Hirzebruch filtration for complex K-theory of a finite CW complex, in the
   form the lens-space proof uses under the name (AH) (read
   store/claims/synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure for the exact
   statement used; state the Fact generally and briefly). Copy the format of an existing imported entity (for example
   synthesis.imported-witten-global-su2-anomaly); provenance Atiyah-Hirzebruch 1961 and Atiyah, K-Theory (1967), flagged
   as cited from memory and not checked against the source. Then cite it (uses/assumes as the format requires) from the
   lens-space cohomology entity in place of the in-statement hypothesis (AH), keeping clause labels; the lambda-operations,
   the spin class q1 and the cellular background (G) stay in-statement hypotheses (decision 2).
2. The two conditional lens results, synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial and
   synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height: version + 1; cite the new cohomology entity for
   exactly the hypotheses its extraction note says it discharges (the first: its cohomology-ring hypothesis discharged,
   still conditional on q1; the second: Sq^1 replaced by the direct x^2 = 0 and the K-ring now a stored theorem given the
   new Fact, still conditional on the lambda-operations if it uses them: read both carefully and say exactly what remains).
   Keep orig-proof-main.tex and every stored file.
3. hawking.joint-j3-s-wave-reduction (decisions 3 and 5): version + 1. Channel-reduction clause kept as premise for
   even-parity spin 2 only (odd parity is derived, given its stated hypotheses, in
   synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional; cite it); "s-wave reduction"
   reworded to "each partial-wave channel, l >= |s|" wherever the postulate's text says it (the id stays); add the sentence
   that the identification of channels with current bosons of the arrays is not one array tower per helicity channel
   (not injective), citing synthesis.capacity-and-sakharov-readings-leave-the-generation-number-free. List dependants
   whose CONTENT changes and fix the wording of those that quote the old clause.
4. Killing-frame scope (decision 4): one sentence in
   synthesis.horizon-channels-of-scalar-dirac-and-maxwell-fields-are-two-dimensional (version + 1): the vanishing of the
   potential at the horizon is a statement in the static (Killing) frame and its null coordinates; in Kruskal-type
   coordinates the coupling at the horizon is nonzero. The spin-2 entity already says it.
5. Cross-references among the three new entities: replace each "intended citation ... sibling" sentence in their
   extraction notes by a plain cross-reference to the stored id (the generation entity names the spin-2 one). The spin-2
   id is kept (the referee's rename suggestion B4 is not applied; ids are stable).
6. store/open_problems.yaml (header comment gives the format); dated "(9 November, second pass.)" paragraphs in `known`,
   attack items marked or restated, `entities` and `source` extended:
   - op.wall-class-invariant: the cohomology rings, Bockstein, stable tangent class and (given the new Fact) the K-ring
     are derived; q1 and the lambda-operations are not; item 4 restated to what remains. New attack item: on a definite
     side the exact rung count as an equivariant (Borsuk-Ulam) index, k = 1 + least j with a Z2-equivariant map from the
     double cover to S^j (argued; first computation the primary obstruction in twisted integral H^3). Success clause
     sharpened (decision 7): "k as a function of the ring data of a (2a = beta x), or a pair of walls with isomorphic
     data and different k". Known: no counterexample among lens spaces, products and projectivised flat bundles
     (findings/attack-B.md, T1).
   - op.helicity-per-boundary-mode: spin 2 odd parity derived for l >= 2 in the static frame, equivalent to the vacuum
     equations on a channel of nonzero frequency; even parity one way (Zerilli equation in the span of the linearised
     equations, sampled), converse and tensor-harmonic facts cited; one superpotential, horizon values; item 1 restated
     to: the even-parity converse, the cited harmonic-analysis inputs, l = 0, 1 and regular charts. J3 narrowed.
   - op.qft-structural-inputs: the capacity and Sakharov leads closed negatively (the new entity): capacity rule cannot
     be met for helicity 1, 2 at any n_g; Sakharov zero moves with xi_R, the gauge parameter and the graviton; quartic
     coefficient vanishes at n_g = 1; independence argued (2 of the cone's 24 postulates audited); J3 not injective.
     Attack item 1 keeps: a premise or dynamics fixing n_g, or a two-model proof over the full joint cone.
   - Three NEW problems (decision 6), status open, kind research, written in the store's style with why/known/attack/
     success, using findings/bridges.md (sections N1, N3 and C4, C1) for content and entity ids (check every id exists):
     (a) op.order-four-anomaly-and-sixteen (area standard-model or walls, choose by the format): is there an order-four
     symmetry of the slot module whose square is the grading and which the descent preserves, and does consistency on
     RP^5 walls force sixteen components per generation; note an index theorem would be imported or derived.
     (b) op.dark-tower-running (area dark-matter): the one-loop running coefficients applied to the dark towers' gauge
     algebras: asymptotic freedom and confinement per tower.
     (c) op.curvature-coupling-across-subjects (area einstein or quantum-fields): xi_R in the Sakharov weight
     (B = 16 n_g - 48 + N_S(1 - 6 xi_R)), the Kasner tilt fit and the doublets' open datum: one value or three fields.
   Validate the YAML (python3 -c "import yaml; yaml.safe_load(open('store/open_problems.yaml'))").
Write colony/runs/2026-11-09-three/maintainer-M.md as the rules say.
