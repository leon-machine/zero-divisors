# colony/

Tools for attacking the store's open problems. The method is attacker and referee (BRIEF.md, read
by every agent); the standing rules for every run (method, one close-out, central gates, proposal
caps, acceptance policy, sync) are POLICIES.md. The ant-colony exploration used in the first two
runs was dropped on 2026-10-22 (POLICIES.md section 0) and its code removed; ant.py keeps the
name and does two small jobs.

- ant.py      `init <run>` makes a run folder; `ledger add|summary` records each problem's outcome,
              tokens, main proposal and referee verdict, and totals them
- labcli.py   every MCP tool of the lab from the shell
- runcheck.py run a check.py against the store (a function fails if it raises, returns False
              or records a GA.check failure)
- check4.py   the maintainer's evidence layer on one proposal, as `tp accept` runs it
- runs/<run>/ one folder per run: ledger.jsonl, findings/, verify/, work/, and the run's
              RUN.md, REFEREE.md, FIXROUND.md, MAINTAINER.md and REPORT.md

Paths are relative to the lab folder (override with TP_LAB). Pick a run with
TP_COLONY_RUN=<run>; otherwise the newest run is used.

runs/2026-10-22-toe holds the templates for new runs: RUN.md, REFEREE.md, FIXROUND.md and
MAINTAINER.md, and REPORT.md as the model report. A new run: `python3 colony/ant.py init <run>`,
then copy those four files from runs/2026-10-22-toe and edit them.
