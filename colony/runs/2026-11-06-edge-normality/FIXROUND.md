# Fix round, run 2026-11-06-edge-normality (role: fixer in colony/BRIEF.md)

Blind referees have reviewed every proposal: verify/P.md (physics: the two op.r-premises-external proposals)
and verify/G.md (algebra: the three scalars-session proposals). Read only the sections for proposals YOU filed,
plus the closing "Overlaps and conflicts" section of your report.

For each of your proposals:
1. Apply every fix the referee lists, in place in `proposals/<id>/`, at every level (title, one-liner, formal,
   technical, lay, proof, check). SOUND needs nothing beyond style fixes.
2. OVERSTATED: restate to the referee's weaker true statement at every level, including the title. Do not add a
   caveat to an unchanged claim. If you think the referee is wrong, rebut only with a computation, written into your
   fixes file.
3. Where the referee recommends merging, dropping or turning a proposal into a note: do it if the store schema
   allows it (a note uses `comments_on`; check an existing note in store/notes for the format and run validate_draft
   on it); to drop a proposal, move its folder to colony/runs/2026-11-06-edge-normality/work/<you>/dropped/ and say so.
4. Literature the referee verified gets cited by name in the text; literature from memory stays flagged.
5. Weak checks: strengthen so the referee's perturbations fail. Exact arithmetic only.
6. Conditions: every hypothesis the result needs appears in the title or one-liner when the referee asks.

Leon's decisions this run (colony/runs/2026-11-06-edge-normality/DECISIONS.md) bind the physics fixers: (N+) stays
the postulate; the sign of i is NOT fixed by convention (it is an open datum (N+) assumes), so no proposal may state
i = I_4 as adopted.

Run ONLY `python3 colony/runcheck.py proposals/<id>/check.py`; never check4.py, validate_draft (except on a new note
draft) or tp check: the orchestrator reruns the gates centrally and returns failures. One process at a time; never kill
other processes. Write colony/runs/2026-11-06-edge-normality/findings/fixes-<you>.md with "check4: pending
(orchestrator)". Do not edit store/, commit, or spawn agents.
