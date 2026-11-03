# colony/

Tools and run records for attacking the store's open problems. The method is attacker and
referee (BRIEF.md, read by every agent); the standing rules for every run (method, one close-out,
central gates, proposal caps, acceptance policy, sync) are POLICIES.md. The ant-colony exploration
used in the first two runs was dropped on 2026-10-22 (POLICIES.md section 0); ant.py is kept for the
run ledger (`ant.py ledger`) and to read old trail maps.

- ant.py      the outcome ledger (`ledger add|summary`); also the retired walk, pheromone and
              split-test commands, kept for reading the 2026-10-22 runs
- labcli.py   every MCP tool of the lab from the shell
- runcheck.py run a check.py against the store (a function fails if it raises, returns False
              or records a GA.check failure)
- check4.py   the maintainer's evidence layer on one proposal, as `tp accept` runs it
- runs/<run>/ one folder per run: pheromones.jsonl, food.jsonl, round.txt, arms.json,
              ledger.jsonl, findings/, verify/, work/

Paths are relative to the lab folder (override with TP_LAB). Pick a run with
TP_COLONY_RUN=<run>; otherwise the newest run is used.

runs/2026-10-22-pilot is the first run; runs/2026-10-22-toe is the second (split test, 55
targets) and its RUN.md, REFEREE.md, FIXROUND.md and MAINTAINER.md are the templates for new runs.
A new run: `python3 colony/ant.py init <run>` creates the folder and its ledger; copy RUN.md,
REFEREE.md, FIXROUND.md and MAINTAINER.md from runs/2026-10-22-toe as templates.
