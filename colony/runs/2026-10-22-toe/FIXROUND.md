# Fix round, run 2026-10-22-toe (role: fixer in colony/BRIEF.md)

Blind referees have reviewed every proposal. Their reports are in
`colony/runs/2026-10-22-toe/verify/R1.md` ... `R7.md`. Your message names the report(s) that cover
your proposals. Read only the sections for proposals YOU filed, plus the closing
"Overlaps and conflicts" section. Do not read other sections (they include the other arm's work).

For each of your proposals:
1. Apply every fix the referee lists, in place in `proposals/<id>/`, at every level (title,
   one-liner, formal, technical, lay, proof, check). SOUND needs nothing beyond style fixes.
2. OVERSTATED: restate to the referee's weaker true statement at every level, including the title.
   Do not add a caveat to an unchanged claim. If you think the referee is wrong, rebut only with a
   computation, written into your fixes file.
3. Numerical (floating point) results never appear in formal, one-liner, technical or lay text as
   established; at most in the proof text, labelled computed and reproducible.
4. Conditions: every hypothesis the result needs appears in the title or one-liner when the
   referee asks for it.
5. Weak checks (W413, or the referee shows a perturbation that still passes): strengthen the check so
   the perturbation fails.
6. Overlaps: where the referee says two proposals duplicate each other, do not merge across agents.
   The proposal the referee names as secondary drops the duplicated clause and cites the other by id
   in the text only ("filed alongside, <id>"); proposal ids are not store ids, so never put them in
   `uses`. Where the referee recommends cross-citing, cite in text the same way.
7. Pins to versions that exist only as proposals (for example a v5 that is itself awaiting acceptance)
   will fail validation: keep the current stored pin and list the repin under "Repin on acceptance"
   in your fixes file.
8. Maintainer-only items (assumes edges, new imported or postulate entities, retirements, status
   promotions in core regions): do not do them; list them under "Decisions for Leon".
9. Store text must not mention scouts, attackers, the colony, siblings, other agents or the run.
   Remove phrases like "corrects a scout reading" or "filed by the other attacker"; state the
   mathematical content instead. Changelog/session metadata may keep the run name.
10. House style: no em dashes; never "honest"/"honestly"; never "load-bearing"; Q(v) for the square
    of a vector; macros only from store/notation.yaml.
11. After each proposal: `python3 colony/runcheck.py proposals/<id>/check.py` (it now also fails a
    function that returns False or records a GA.check failure), `python3 colony/check4.py
    proposals/<id>` (must exit 0 apart from environmental E401), and validate_draft (ok; E102 for a
    kept orig-proof-main.tex is expected on corrected entities).

Write `colony/runs/2026-10-22-toe/findings/fixes-<your cluster>-<A|B>.md`: per proposal, the verdict,
what changed, the final check4 line; then "Repin on acceptance" and "Decisions for Leon". Your final
reply is that file's content.

## Change at 17:50: do NOT run check4.py or validate_draft yourself
The machine has 2 CPUs and over 100 gate processes were queued (load 42), so the orchestrator has
stopped all running check4 and validate_draft processes and will run both centrally, one at a time,
on every proposal once the fix round ends; any proposal that fails goes back to its author.
Finish your edits, run only `python3 colony/runcheck.py proposals/<id>/check.py` (fast), write your
fixes file with "check4: pending (orchestrator)", and reply. Do not kill other processes.
