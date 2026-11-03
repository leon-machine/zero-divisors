# Run 2026-10-22-toe: what is specific to this run

LAB = /home/claude/lab/transport_lab (run every tool from there). Run name: 2026-10-22-toe.
`export TP_COLONY_RUN=2026-10-22-toe` before using colony/ant.py.
Run folder: colony/runs/2026-10-22-toe/ (findings/, work/<your-name>/, verify/).

## The goal
Leon wants progress toward one theory: in particular a quantum field theory, built from the
series' own objects, from which Einstein's equations can be derived, and fewer postulates
underneath everything. His stance (respect it): gravity is transport, not a quantised field;
there is no graviton; GR and QM are two readings of one algebraic relation, so look for
derivations that read one structure two ways rather than "quantising gravity". Cross-pollinate:
a result in one subject that supplies a premise, a technique or an obstruction in another is
exactly what is wanted.

## Targets
- `problems.md` (full statements; grep `## <id>` and read ~40 lines) and `problems_index.md`
  (one line each, with the arm). 55 targets: the 39 store open problems (`op.*`), 11 premise
  targets (`pr.*`: derive a postulate, show two equivalent, weaken one, or prove independence
  with a model), and 5 Einstein targets (`ein.*`).
- Many `op.*` problems already have accepted work in the store from the first run (listed under
  "already in store"). Start from that; do not redo it. The first run's report is
  `colony/runs/2026-10-22-pilot/REPORT.md` (you may read it; it is public history).
- For `pr.*` and `ein.*` targets use the target id itself in `extraction.open_problem`.

## Two angles per cluster
Each cluster of targets has two attackers working at the same time:
- Angle A (constructive): the problem's own routes and the most direct derivation; aims to prove.
- Angle B (cross-pollinating and adversarial): imports structure from other subjects, looks for
  counter-models, independence proofs and refutations; a clean no-go is a success.
Both may file proposals. Before filing, run `python3 colony/labcli.py list_proposals '{}'` and
`ls proposals/` so you never file the same result twice; read your sibling's findings file
(`findings/attack-<cluster>-<A|B>.md`, written as you go) at least once midway and at the end,
and build on it rather than duplicating it. Write your own findings file early and update it.

## Filing gate (both arms)
A proposal counts only if `python3 colony/check4.py proposals/<id>` exits 0 (an E401 for a missing
legacy script is environmental and acceptable) AND validate_draft is ok. Exact arithmetic only in
checks (no floats, float(), math, random, integer true division), `import GA`, premise() inside
each check function for the premises it uses. Numerical work goes in the proof text. Corrected
entities keep every file of the folder they replace (orig-proof-main.tex in particular).
Do not create postulate or imported entities and do not add or remove `assumes` edges: if your
result needs one, say so in findings as a decision for Leon.

## Arms
- COLONY arm: you have the colony (colony/ant.py walk/lay/food/trails/larder/show/echo/near) and
  the scout findings in this run's findings/ (scout-*.md). Use them per BRIEF.md.
- CONTROL arm: you work without the colony. Do NOT run colony/ant.py, and do NOT read
  pheromones.jsonl, food.jsonl or any scout-*.md file. Use labcli.py (search_claims, cone,
  neighbourhood, get_claim, get_proof, find_text), runcheck.py and check4.py. Otherwise identical.

## Colony attackers: fairness rule for the split test
The control arm ran first, and its proposals are already in `proposals/`. You may list proposal ids and
titles (to avoid duplicates), and you may read in full any proposal whose `extraction.open_problem` is a
COLONY-arm target. Do NOT open the contents (entity.md, proofs, check.py) of proposals filed against
CONTROL-arm targets, and do not read findings/attack-K*.md. If a colony brief cites a control-arm
proposal, treat the citation as a title only.
