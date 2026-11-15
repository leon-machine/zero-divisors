# Maintainer pass after run 2026-11-12-asymmetry (acting for Leon, the maintainer)

Leon has accepted the run's four proposals (now in store/claims/):
  synthesis.exchange-of-set-and-clear-is-inner-and-fixed-by-no-integer-state
  synthesis.baryon-number-centraliser-in-the-five-mode-algebra
  synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them
  synthesis.flag-conjugate-antilinear-on-one-chirality-and-conjugation-reverses-jarlskog
and made four decisions on 12 November 2026:
  D1. Apply the referee's correction to clause (3) of
      synthesis.cpt-conjugation-pseudoscalar-rotor-times-complex-conjugation (text in verify/R1.md, section G).
  D2. The asymmetry inherited from the descent, the charge Q = epsilon N, is named as B - L (not baryon number).
      Consequences he accepted: the registered baryons per unit entropy then derive from a free (B - L) value
      through the anomalous weak equilibrium, conditional on that equilibrium; the mirror share f_2 = 1 no longer
      follows from the copy theorem and becomes an open item.
  D3. The anomalous weak process (B + L violated, B - L conserved) and its equilibrium coefficient are NOT imported
      now. Register an attack item to derive or source the process and to fix the number of light doublets
      (28/79 for one doublet, which the stored check of dark-tower-matter.mirrors-composition uses; 8/23 for two,
      which the stored bidoublet needs). Do not change that stored check.
  D4. The stored CPT conjugation acts on the family (Yukawa) terms by the adjoint reading: the premise's action
      clause is restricted so the conjugation takes each family term to its adjoint; it is then a symmetry that
      also reverses the arrow, consistent with a non-zero Jarlskog invariant.
The open problem op.matter-asymmetry-origin stays OPEN (referee, section F): record what the run established and
what is missing.

You are one of two maintainer agents with disjoint entity ownership (your message lists yours). Edit store/ directly
in LAB = /home/claude/phys-graph (branch run/2026-11-12-asymmetry). Never spawn agents, never commit or push, never
touch anything outside LAB. Read verify/R1.md, findings/attack-AA.md, findings/attack-AB.md, findings/fixes-*.md of
this run for the material (you are not blind).

## Rules
- Read CONTRIBUTING.md, docs/CONTRIBUTING-rules.md and `python3 colony/labcli.py conventions '{}'`; copy the format
  of existing entities of the same kind.
- Changing an existing entity: version + 1; keep every file in its folder (orig-proof-main.tex in particular); add
  an `amendments` entry {version, kind: correction | restatement, defect, evidence?} and a credit entry
  {name: Claude Fable 5.2, role: <what changed>, version: <new>, source: maintainer pass 2026-11-12 (asymmetry)},
  keeping every existing credit entry unchanged; add under `extraction` an entry
  `maintainer_pass_2026_11_12: {by: maintainer-2026-11-12, date: '2026-11-12', note: <one or two sentences>}`.
  Keep `proposed_by` as it is. A wording-only change keeps the version.
- Change the least that carries the decision. Do not strengthen any statement. Where a decision makes a stored
  sentence conditional, say on what. Label argued as argued.
- House style: no em dashes; never "honest"/"honestly"; never "load-bearing"; Q(v) for the square of a vector;
  macros only from store/notation.yaml; no mention of agents, runs or method names in store text (changelog `by:`
  and `source:` fields excepted). Geometric algebra language; declare outside_ga where needed.
- Exact arithmetic in any check you touch; after changing a check run `python3 colony/runcheck.py <folder>/check.py`
  then `python3 colony/check4.py <folder>` (one at a time; 2 CPUs; never kill other processes).
- Validation: after your edits run
  `python3 -m tp check --store store --layers 1,2,3 --keep-going --author leon 2>&1 | tail -40`
  and fix every error or new warning on YOUR entities (pin warnings on dependants of entities whose version you
  raised are expected: list them, do not repin). The other agent is editing other entities at the same time; ignore
  findings that are only theirs. Do not run the full check, `tp repin`, `tp lock`, `tp build` or the site build.
- Write colony/runs/2026-11-12-asymmetry/maintainer-<your name>.md: every entity changed with old -> new version and
  one line each; dependants whose CONTENT (not just pins) may be affected, with what you think should happen to
  each; anything you could not do and why. Your final reply: a short summary of that file.
