# Maintainer pass after run 2026-10-22-toe (acting for Leon, the maintainer)

Leon has accepted all 105 proposals (now in `store/`) and asked for the maintainer edits and
premise decisions from `colony/runs/2026-10-22-toe/REPORT.md` to be carried out. You are one of
four maintainer agents, each owning a disjoint set of entities (your message lists yours). Edit
`store/` directly in the cloud workspace LAB = /home/claude/lab/transport_lab. Never touch the
user's computer; never spawn agents.

## Rules
- Read `CONTRIBUTING.md`, `store/conventions.md`, and copy the format of existing entities of the
  same kind (postulates: grep `status: postulate`; imported Facts: grep `status: imported`;
  retirements: `store/tombstones.yaml`; open problems: `store/open_problems.yaml`, header comment).
- Changing an existing entity: version + 1, keep every file in its folder (orig-proof-main.tex in
  particular), and add a `correction` (or `maintainer_pass`) entry under `extraction` with
  `by: maintainer-2026-10-22`, date `'2026-10-22'`, and a one-sentence note of what changed and why.
  Keep `proposed_by` as it is.
- New entities: `proposed_by: {kind: maintainer, session: maintainer-2026-10-22}` if the schema
  allows that kind, else copy what existing maintainer-made entities use; `ai_involved: 'yes'`.
  New imported Facts state the source precisely and say "cited from memory, not checked against
  the source" in the extraction note unless you verified it with WebSearch/WebFetch (you may).
- New postulates: formal statement, what it is for, which results use it, and (Tier C style, as in
  existing Tier C postulates if any) a refutation condition: what observation or result would show
  it false. Do not overclaim what follows from it: a postulate plus a cited theorem is a conditional
  result, and if no store entity proves the conditional, say it is not proved in the store.
- House style: no em dashes; never "honest"/"honestly"; never "load-bearing"; Q(v) for the square
  of a vector; macros only from store/notation.yaml; no mention of agents, scouts, colony or runs
  in store text (changelog `by:` fields excepted).
- Exact arithmetic in any check you touch; after changing a check run
  `python3 colony/runcheck.py <folder>/check.py` and `python3 colony/check4.py <folder>`
  (one at a time; the machine has 2 CPUs).
- Validation: after your edits run `python3 -m tp check --store store --layers 1,2,3 --keep-going
  --author leon 2>&1 | tail -40` and fix every error or new warning on YOUR entities. Other agents
  are editing other entities at the same time, so ignore findings that are only theirs. Do not run
  the full six-layer check; the orchestrator does that once at the end, then repins, locks and
  rebuilds.
- Do not run `tp repin`, `tp lock` or `tp build`.
- Write `colony/runs/2026-10-22-toe/maintainer-<your name>.md`: every entity created, changed or
  retired, with old -> new version and one line each; dependants whose CONTENT might be affected by
  a change (not just pins), and anything you could not do and why. Your final reply is that file.
