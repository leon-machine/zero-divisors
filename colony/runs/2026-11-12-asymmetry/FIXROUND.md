# Fix round, run 2026-11-12-asymmetry

You are the original attacker, resumed as fixer (colony/BRIEF.md, "Role: fixer"). The blind referee's report is
colony/runs/2026-11-12-asymmetry/verify/R1.md. Read the section for each of your proposals and sections A to G.

- Apply every fix the referee lists, in place in proposals/<id>/ (entity.md at every level, proof-main.tex, check.py,
  coverage.yaml). A proposal judged OVERSTATED is restated to the referee's true weaker statement on every level,
  including the title and, if the title no longer fits the id, say so in your fixes file (do not rename the folder;
  the orchestrator decides).
- Overlap (section A): the referee says proposals 2 and 3 stand as two, trimmed, with cross-references. AA trims the
  clause of proposal 2 that duplicates proposal 1; AB trims clauses of proposal 3 that restate proposal 2 and cites
  it in the note instead (not as a uses edge unless the proof needs it).
- Checks that test less than the clause: tighten them or lower the clause's label; a check that is arithmetic on a
  pinned literal must be described as such in coverage.yaml or replaced by a computation.
- Literature cited from memory stays labelled so in the formal level where a clause depends on it. Do not create
  imported entities: list them under "Decisions for Leon".
- The 28/79 against 8/23 point (one Higgs doublet against two): state both values, which one the store's check uses,
  and that the choice is the maintainer's; do not pick silently.
- Do not rely on the defective sentence of synthesis.cpt-conjugation-pseudoscalar-rotor-times-complex-conjugation
  clause (3) (section G); the correction to that stored claim is a maintainer edit, not yours.
- Rebut only with a computation.
- Run ONLY `python3 colony/runcheck.py proposals/<id>/check.py`. Never check4.py, validate_draft or tp check: the
  orchestrator runs those centrally afterwards. Do not commit.
- Write colony/runs/2026-11-12-asymmetry/findings/fixes-<AA|AB>.md: per proposal, each referee fix and what you did,
  anything rebutted with the computation, and "check4: pending (orchestrator)".
Final message: three or four lines: what changed per proposal, anything rebutted, anything left for the maintainer.
