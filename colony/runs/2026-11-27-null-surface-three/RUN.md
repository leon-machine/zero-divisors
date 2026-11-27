# Run 2026-11-27-null-surface-three

LAB = /home/claude/zero-divisors (branch run/2026-11-27-null-surface-three, already checked out).
Read colony/BRIEF.md (standards) first. This file overrides it where they differ.

## Goal
Three new results, one per attacker, each extending the two entries merged on 26 November:

- R1 `store/claims/synthesis.null-plane-data-of-the-first-order-gravitational-field-are-the-shear-of-the-generators/`
- R2 `store/claims/synthesis.field-equation-linear-in-the-curvature-with-a-conserved-source-is-einsteins/`

Read both in full (entity.md, proof-main.tex, check.py) before anything else: they are the format,
the notation, the sign conventions and the toolkit you must reuse. Their check.py files contain
working exact-arithmetic helpers (symbol of the symplectic current, first-order Einstein map,
exact field solves, Riccati equation on a field that is not weak, Bianchi identities) and show how
lib/gtg.py is used (`field_from_hbinv`, `Field.curvature()`, `curvature_jet()`, `cov_phys`,
`torsion_free()`, `hb_matrix()`, `ricci`, `einstein`, `Jet`).

Targets:
- attacker `stress`: the second-order stress of the first-order gravitational field as a source.
- attacker `corner`: the corner area as the generator of the relative boost of a null-plane pair.
- attacker `shear`: null-surface data at any field strength; the focusing equation integrated.

The idea for all three was prompted by V. Chandrasekaran, arXiv:2611.34924 (reference key
`Chandrasekaran2026`, already in store/references.yaml). You may fetch it for orientation
(https://arxiv.org/abs/2611.34924). The maintainer's instruction: use the graph's own results and
methods first; the paper is a guide to what to look for, never a derivation to copy. Derive
everything inside the entity from stored results and the stored definition
`obj.synthesis.gtg-flat-spacetime-gauge-fields`. Each entity carries a short "Source of the idea"
paragraph that says the work was prompted by that paper and credits the classical origin of the
idea (cite real literature; flag anything cited from memory in your findings file).

## How results are filed in this run (differs from BRIEF.md)
This run lands as one pull request, as on 26 November. So you DO write directly into the store, but
only inside ONE new folder that you own: `store/claims/<your-new-id>/` with `entity.md`,
`proof-main.tex`, `check.py`. Follow CONTRIBUTING.md and copy the structure of R1/R2 exactly
(front matter, four levels formal/technical/lay/one-liner, extraction note listing decisions for
the maintainer). `proposed_by.session` and the credit `source` are `2026-11-27-null-surface-three`;
credit `Leon Butler` (direction) and `Claude Fable 5.2` (proposal, proof and drafting).
Pin premises as `id@version` under `derivations[].uses`, and call `premise("id")` (from
`tp_premise`) inside each check function for each premise that function relies on.

You must not: edit any other store file (exception: you may APPEND a reference entry to
`store/references.yaml` with `cat >>`, never rewrite it; check the key does not exist first);
edit `store/open_problems.yaml`; run git commit, push, checkout, stash or reset; run the
full-store `python -m tp check`; spawn agents; kill processes; touch anything outside LAB except
/home/claude/scratch/<your-name>/.

Scratch scripts go in `colony/runs/2026-11-27-null-surface-three/work/<your-name>/`.
Keep `colony/runs/2026-11-27-null-surface-three/findings/attack-<your-name>.md` current.

## Gates you run on your own entity (2 CPUs shared by three attackers: one process at a time each)
    python -m tp.lint <id> --store store
    python -m tp.checkone <id> --store store
    python -m tp.mutants <id> --store store      # slow; run when the checks are final
All three must be clean before you report. A W413 (weak check) from the mutation test means a check
function does not notice when its integer literals are perturbed: pin counted or computed values.

## Language rules (the maintainer's standing rules; lint enforces several)
- Everything in real geometric algebra; gravity in Gauge Theory Gravity (gauge fields h-bar and
  Omega on flat spacetime, physical vectors, rotors, the commutator product). Never "curved
  spacetime". No tensor-index or Christoffel arguments (a labelled parenthetical translation for
  readers is allowed). No bare imaginary unit i anywhere a pseudoscalar or bivector can do the work
  (I_4, or the unit bivector of the plane concerned); where truly impossible, declare `outside_ga`.
- Derive in GA inside the entity; literature is cited as prior art, never as a premise, unless it
  is already a stored imported Fact that you pin and name as imported.
- No em dashes. Never "honest"/"honestly", never "load-bearing". Q(v) for the square of a vector.
  Macros only from store/notation.yaml. No agent, run or method names in store text.
- Theorem/Proof only for what is proved in the entity. Every hypothesis is named and stated in the
  formal statement, as R1 does with (L), (D), (V), (N) and R2 with (Q), (C), (N).
- The stored Definition's clause (f) contains the field equation. If you need the vacuum field
  equation, say so as a named hypothesis or pin R2; do not use it silently.
- If a clause concerns a closed or periodic setting, include the "Beyond one flat chart" sentence
  and the `extraction.flags` entry the way R1 clause (vii) does.
- check.py: exact arithmetic only (Fractions, GA.py, lib/gtg.py jets). No floats, no `/` true
  division on ints, no math/random. Functions return bool and report through `GA.check(label, ok)`.
- Title at most 90 characters, a name for the result and not its statement.

## Standards
- Pre-register your kill condition in the findings file BEFORE computing. A refutation or a weaker
  true statement is a full result: file what is true, at the strength it is true, and say plainly
  what failed. Never inflate. Label each clause proved / computed / argued.
- Search the store before proving anything, so you do not duplicate a stored result:
  `python3 colony/labcli.py search_claims '{"query": "..."}'`, `find_text`, `get_claim`, `cone`,
  or grep under store/claims. Name near-duplicates in the findings file.
- State in the extraction note which open problem the result bears on and what it does NOT settle.

## What to return to the orchestrator (your final message)
1. The new entity id and one paragraph on what is proved, clause by clause, with hypotheses.
2. What failed or was weaker than hoped, and the kill condition's outcome.
3. Gate results (lint, checkone, mutants) copied from the tool output.
4. References appended. Decisions for the maintainer. Anything cited from memory.
