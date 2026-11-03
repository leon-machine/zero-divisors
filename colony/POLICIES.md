# Standing policies for open-problem runs (adopted 2026-10-22)

These hold for every run unless Leon says otherwise at the start of that run. They exist to keep a
run's close-out short: one question round, one full check, one sync.

## 0. Method
Attacker and referee (procedure in BRIEF.md): two attackers per cluster of 3 or 4 problems (angle A
constructive, angle B cross-pollinating and adversarial), orienting by direct lookups in the store;
one bridge-hunter reading across clusters midway; blind referees; one fix round. The ant-colony
exploration layer (random walks, pheromone, scout rounds) is dropped (decision of 2026-10-22): in
the run 2026-10-22-toe split test it matched the control arm on outcomes (score 52 against 53) at
about 67% more tokens, and cross-links came from agents reading content, not from walking the graph.
A colony-versus-control split test is no longer run by default.

## 1. Close out once
One sequence at the end of a run, all in the workspace:
accept, maintainer edits and premise decisions, repin, one full `tp check`, `tp build`,
`python -m tp.layout`, `python -m tp.site`, `tp lock`, the unit tests, then one commit and push.
After the commit, `python -m tp credit` fills in the credit of any accepted entity that lacks it,
naming the model from that commit's Co-Authored-By trailer; commit that too.
Premise decisions are put to Leon while the referees are still working, so they are settled by the
time the fix round ends. Nothing is synced to Leon's machine before the end.

## 2. Gates run once, centrally
- Attackers run `check4.py` on their own proposals before filing (the filing gate), at most one at a
  time each.
- Fixers run only `runcheck.py`. They never run `check4.py`, `validate_draft` or `tp check`, and
  never kill other processes.
- The orchestrator runs `check4.py`, `validate_draft` and the style scan on every proposal after the
  fix round, two at a time (the cloud machine has 2 CPUs), and sends failures back.
- `tp check` is incremental by default: layer 4 replays recorded results for entities whose
  evidence inputs have not changed (`store/.tp-layer4.json`). Use `--full` for a from-scratch run;
  run one `--full` check when the toolchain or the legacy verify scripts have changed.
- Checks are never rerun on Leon's machine; the workspace run is the record.

## 3. Fewer, merged proposals
- About 3 proposals per cluster side; prefer one strong proposal per problem.
- Before the referees start, the orchestrator lists likely duplicates (same open problem, similar
  titles, across siblings and across arms) and has the authors merge or drop them.
- Referees take about 15 proposals each, grouped by subject with the arms mixed.

## 4. Acceptance and maintenance policy
- Accept, without asking, every proposal that passed review after fixes (SOUND, or SOUND WITH FIXES
  with the fixes applied and the final gate clean).
- Put to Leon individually, four per question with previews: proposals restated after an
  OVERSTATED or WRONG verdict, proposals no referee saw, status changes in core regions, new
  `assumes` edges and new postulates.
- Routine, done in the maintainer pass without asking: retiring exact duplicates (tombstone,
  `replaced_by`, `merged_from` on the kept entity, references repointed), repinning after checking
  which dependants' content changed, notes and wording fixes the referees asked for, importing as
  Facts the literature results that accepted proposals cite from memory, house-style and W503 fixes.
- Premise decisions (adopting, restating or retiring postulates; choosing between readings) are
  always Leon's, asked once, together, with a recommendation each.

## 5. Sync
The lab is the private repository `leon-machine/phys-graph`. A session ends with one commit and
push; Leon pulls. Retirements are deletions in git. The paper verify scripts stay in
TP_Papers_Suite; point `TP_LEGACY_DIR` at that folder.
