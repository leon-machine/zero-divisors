# Maintainer pass after run 2026-11-18-navigate (acting for Leon, the maintainer)

LAB = /home/claude/phys-graph (branch run/2026-11-18-navigate). Leon accepted the run's three results (now in
store/claims/) and decided on 18 November 2026:
  D3. "Fix everything now": amend the imported Fact dark-matter.imported-massless-graviton-production-rate (done by the
      orchestrator: it is now version 4; read it) and restate the numbers in its four direct users in this pull request.

You own exactly these four entities (their entity.md, proof-main.tex, check.py, coverage.yaml):
  dark-matter.seeding-gravity-floor-dark-towers-temperature
  dark-matter.coefficients-floors-they-give-what-gravity
  synthesis.seeding-remainder-excludes-perturbative-pati-salam
  synthesis.untuned-fit-caps-lightest-heavy-neutrino
and, for quoted numbers only, the entities downstream of them (see "Dependants" below). Do not touch anything else:
not the Fact, not the three new results, not store/open_problems.yaml, not store/conventions.md, not
transport.obstructions-are-moved-never-destroyed (the orchestrator owns those). Never spawn agents, never commit or
push, never touch anything outside LAB. You are not blind: read
store/claims/synthesis.gravitational-pair-production-from-the-operator-source-at-first-order/ (entity.md,
proof-main.tex), the Fact at version 4, and colony/runs/2026-11-18-navigate/verify/R1.md and R2.md (section B).

## The new coefficients (exact; from clause (v) of the new result)
Rate per volume of creation events (each event creates two quanta), Gamma = alpha T^8 / Mbar_P^4, from a bath of
(4 real scalars, 45 chiral fermions, 12 vectors), curvature couplings zero, tree level:
  one real scalar            alpha = 5789 pi^3 / 82944000   = 2.1640e-3
  one chiral (Weyl) fermion  alpha = 16087 pi^3 / 82944000  = 6.0137e-3   (a Dirac fermion: twice, 1.2027e-2)
  one real massless vector   alpha = 16087 pi^3 / 20736000  = 2.4055e-2
  a copy of the Standard Model's content (4, 45, 12): 1519247 pi^3 / 82944000 = 0.56793
  nine massless vectors: 9 x 2.4055e-2 = 0.21649;  the four odd towers' 2 + 2 + 9 + 9 = 22 vectors: 0.52920
General formula: alpha_j = (pi^3/17280) [ (c_j (N_s + 12 N_v) + 5 tau_j sum_i tau_i)/225 + 49 c_j N_w/4800 ], c = 1, 3, 12
for a real scalar, a chiral fermion, a real massless vector; tau = (1 - 6 xi)^2 on scalars, 0 otherwise.
The old values were 1.9e-4 (scalar), 1.1e-3 (fermion, Weyl-or-Dirac bracket), 2.3e-3 (vector); the old bracket for the
mirror was c = 0.053 to 0.078 and for nine vectors 0.021. The Weyl-or-Dirac bracket is gone: the 45 are chiral and
weighted once. The old "factor between counting particles and pairs" is now definite: Gamma counts events, the number
of quanta created is 2 Gamma.

## What to do in each of the four
- Recompute every number that depends on the coefficients, with exact rational arithmetic where the stored check does
  so and with the stored rounding conventions elsewhere; read the stored check.py first and change its inputs, not its
  method. Keep every formula that is symbolic in c unchanged (for example xi_floor = 9.6e-4 c^(1/4) ...; the thresholds
  c* = 13.49 and c > 63.7 and 3.9e12 are conditions on c and do not change; what changes is which contents meet
  them, the margins, and every number computed from a content's c).
- Where a stored sentence carried the Weyl-or-Dirac bracket (two ends of a range), give the single value and say the
  bracket is closed by the derived weights. Where the stored text has a factor 2 or 2^(1/4) "bracket of the imported
  rate" for pairs against particles, keep the stored convention if the conclusion depends on it and say what it is
  now (events of two quanta); do not silently change a conclusion by changing a convention.
- If a qualitative conclusion changes (an exclusion that no longer holds, a margin that closes, an inequality that
  flips), STOP on that clause: restate it truthfully to the weaker statement, and list it under "Conclusions that
  changed" in your report. Do not rescue a conclusion. Do not strengthen any statement.
- Cite the rate as "the rate of Theorem \claimref{synthesis.gravitational-pair-production-from-the-operator-source-at-first-order}(v)
  (Fact \claimref{dark-matter.imported-massless-graviton-production-rate} for the published values)". In `derivations`
  repin the Fact to @4 and add `synthesis.gravitational-pair-production-from-the-operator-source-at-first-order@1` under
  `uses`; in check.py call premise() for it where the coefficients are taken. The new result holds under its hypothesis
  (OS) and equally on the standard account (its Reading); say once, where the rate is introduced, "under that
  theorem's hypothesis (OS), or on the standard account of the Fact".
- All four levels (formal, technical, lay, one-liner) must agree; numbers never appear above the proof text without
  being in the proof or the check.
- Entity bookkeeping for each changed entity: version + 1; keep every file in its folder (orig-proof-main.tex in
  particular); add an `amendments` entry {version: <new>, kind: restatement, defect: <what was wrong, at least 30
  characters>, evidence: check.py::<a check function of the entity>}; add a credit entry {name: Claude Fable 5.2,
  role: <what changed>, version: <new>, source: 'maintainer pass of 2026-11-18 (run 2026-11-18-navigate)'}, keeping
  every existing credit entry unchanged; add under `extraction` an entry
  `maintainer_pass_2026_11_18: {by: maintainer-2026-11-18, date: '2026-11-18', note: <one or two sentences>}`. Keep
  `proposed_by`. Remove nothing else from the front matter.
- House style: no em dashes; never "honest"/"honestly"; never "load-bearing"; Q(v) for the square of a vector; only
  macros from store/notation.yaml; no agent, run or method names in the statements and proofs.
- check.py rules: exact arithmetic only (no float literals, float(), math, random, int true division), `import GA`,
  premise() per premise used, perturbing integer literals must break the check. If the stored check uses decimal
  approximations of pi^3 as rationals, follow its practice and say so in the docstring.

## Dependants
The Fact's future cone has about 30 entities (listed in `python3 colony/labcli.py get_open_problem
'{"id":"op.graviton-rate-as-classical-field-process"}'`, field `known`; or `python3 colony/labcli.py cone
'{"id":"dark-matter.imported-massless-graviton-production-rate","direction":"future","limit":60}'`). For each one that
is not one of your four: grep its entity.md and proof for numbers that come from the four (old values to look for
include 0.053, 0.078, 0.021, 0.051, 0.312, 3.5e-4, 2.8 and 3.2e-4, eta' 19 to 26, 1.8 to 2.7e-15, "3 to 5" x 10^4,
31.9 to 36.2, 1.9 to 2.2e16, 5900, f_J > 32, 8.2 GeV, 4.0 and 2.5, 1400-fold, and the per-species 1.9e-4, 1.1e-3,
2.3e-3; also the predictions pred.no-dark-radiation, pred.no-indirect-dark-signals, pred.dimmed-evaporation-bursts and
their sentence pointing at the open problem). Where such a number is quoted, correct it with the same bookkeeping
(version + 1, amendments kind restatement if the formal statement changes, otherwise kind correction; a pure repin
needs nothing from you). Where an entity only cites one of the four without quoting a changed number, leave it: the
orchestrator repins. Where a prediction's sentence says the rate "is flagged" or "holds conditionally on an input from
outside the series", reword it to say the rate is now derived in the store (cite the theorem) with corrected
coefficients; do not change a prediction's kill condition, threshold or status. List every dependant you looked at in
your report with one of: changed (what), cites only, not affected.

## Checks you may run
- `python3 colony/runcheck.py store/claims/<id>/check.py` for each entity whose check you changed.
- `python -m tp check --store store --layers 1-3 --keep-going --author leon` once at the end (layers 1 to 3 only;
  do not run layer 4, check4.py or validate_draft; the orchestrator runs the full check). Stale-pin findings on
  dependants of the entities you changed are expected and are the orchestrator's to repin; report them, do not fix.
- Never kill other processes. The machine has 2 CPUs.

## Report
Write colony/runs/2026-11-18-navigate/maintainer-M1.md: for each of the four, old and new version, every number
changed (old -> new) with the computation, and "Conclusions that changed" (or "none"); the dependants table; the
layer 1 to 3 result; anything you could not decide. Return a short summary as your final message.
