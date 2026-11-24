# Fix round, run 2026-11-24-three-routes (role: fixer in colony/BRIEF.md)

Blind referees have reviewed every proposal. Their reports are `colony/runs/2026-11-24-three-routes/verify/R-P.md`,
`R-G.md` and `R-H.md`. Your message names the report that covers your proposals. Read only the sections for
proposals YOU filed, plus the closing "Overlaps and conflicts" section.

For each of your proposals:
1. Apply every fix the referee lists, in place in `proposals/<id>/`, at every level (title, one-liner,
   formal, technical, lay, proof, check). SOUND needs nothing beyond style fixes.
2. OVERSTATED: restate to the referee's weaker true statement at every level, including the title. Do not
   add a caveat to an unchanged claim. If you think the referee is wrong, rebut only with a computation,
   written into your fixes file.
3. Numerical (floating point) results never appear in formal, one-liner, technical or lay text as
   established; at most in the proof text, labelled computed and reproducible.
4. Conditions: every named hypothesis the result needs appears in the title or one-liner.
5. Weak checks (the referee shows a perturbation that still passes): strengthen the check so that the
   perturbation fails.
6. Overlaps: do not merge across authors. Where the referee recommends cross-citing a proposal filed
   alongside, cite it in text only ("filed alongside, <id>"); proposal ids are not store ids, so never put
   them in `uses`.
7. Pins to versions that exist only as proposals fail validation: keep the stored pin and list the repin
   under "Repin on acceptance" in your fixes file.
8. Maintainer-only items (assumes edges, new imported or postulate entities, retirements, status
   promotions): do not do them; list them under "Decisions for Leon".
9. Store text must not mention attackers, referees, siblings, other agents, the colony or the run. State
   the mathematical content. Changelog and session metadata may keep the run name.
10. House style: no em dashes; never "honest"/"honestly"; never "load-bearing"; Q(v) for the square of a
    vector; macros only from store/notation.yaml; no imaginary unit where a pseudoscalar does the work.
11. Cross-links from the bridge pass (`findings/bridges.md`, the entries your message names): where one
    corrects a sentence in your proposal, correct it; where it is a lead, do NOT pursue it now: record it
    under "Next steps" in your fixes file.
12. After each proposal run ONLY `python3 colony/runcheck.py proposals/<id>/check.py`. Never run check4.py
    or validate_draft, and never kill other processes: the orchestrator runs both centrally afterwards and
    returns failures. Do not commit, push or switch branches; never edit `store/`; never spawn agents.

Write `colony/runs/2026-11-24-three-routes/findings/fixes-<your name>.md`: per proposal, the verdict, what
changed, the runcheck result, "check4: pending (orchestrator)"; then "Repin on acceptance", "Next steps" and
"Decisions for Leon". Your final reply is that file's content in brief: per proposal the verdict and what
changed, anything you rebutted and with what computation, and the decisions for Leon.
