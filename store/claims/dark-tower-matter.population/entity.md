---
id: dark-tower-matter.population
kind: claim
version: 3
title: How the odd towers could be populated
status: proved
region: dark-tower-matter
subject: dark-matter
tags: [matter-asymmetry, open-problem]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T14c, the series'' standard disclaimer'
- name: Claude Opus 5.5
  role: 'restated to the deposited text of T14c version 1.0 (10.5281/zenodo.24403592)'
  version: 3
  source: maintainer pass of 2026-11-20
review: typed
derivations:
- name: main
  uses:
  - dark-tower-matter.imported-towers-their-types@4
  - dark-tower-matter.survival-sheets@6
  - dark-tower-matter.five-dimensional-towers@6
  - dark-tower-matter.imported-unit-ball-rule@5
  assumes:
  - dark-matter.e-equal-mass-per-unit-ball@1
  - dark-matter.r2-one-quantum-per-unit-ball@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
locators:
  paper: T14c
  number: Obs 9.5
  label: prop:population
  line: 803
extraction:
  maintainer_pass:
    by: maintainer-2026-11-20
    date: '2026-11-20'
    note: 'The formal level restated: T14c deposited as version 1.0 on 20 November 2026 (10.5281/zenodo.24403592), after an independent review: the density to be filled is E''s (was R2''s); renumbered Observation 9.5. Version 2 -> 3. The technical level restated: as the formal level. The lay level restated: as the formal level. The one-liner level restated: as the formal level.'
  env: proposition
  context_refs:
  - dark-tower-matter.five-dimensional-towers
  - dark-tower-matter.imported-towers-their-types
  - dark-tower-matter.survival-sheets
  flags:
  - no proof environment found
  typing:
    by: ai-typing-pass
    added:
    - dark-matter.r2-one-quantum-per-unit-ball
    - dark-tower-matter.five-dimensional-towers
    - dark-tower-matter.imported-towers-their-types
    - dark-tower-matter.imported-unit-ball-rule
    - dark-tower-matter.survival-sheets
    note: 'E107 fix: the assembly-level proposition has no proof environment and states its premises inline
      (the towers fact, survival on sheets, the five-dimensional towers), so those, the unit-ball shares
      and R2 itself were made its edges with a cites-only proof file. Levels pass: levels written from
      scratch, keeping every condition and level qualifier of the formal statement.'
---

## formal
The odd towers carry no asymmetry (Fact \claimref{dark-tower-matter.imported-towers-their-types}). Their matter is therefore symmetric, and the number of quanta that fills E's density must be either a count deposited by the descent and protected from annihilation by kinematics or weakness (Computations \claimref{dark-tower-matter.survival-sheets}, \claimref{dark-tower-matter.five-dimensional-towers}(vi)), or, in the five-dimensional towers, a weak-coupling freeze-out with the coupling tied to the deposit temperature. Neither is derived. Assembly level.

## technical
At assembly level, given E. The odd towers carry no asymmetry, so their matter is symmetric, and the number of quanta that fills E's density must come either from a count deposited by the descent and protected from annihilation by kinematics or weakness (survival on sheets, or the neutral-species branch of the five-dimensional towers), or, in the five-dimensional towers, from a weak-coupling freeze-out with the coupling tied to the deposit temperature. Neither mechanism is derived.

## lay
The odd-dimensional dark towers cannot store a surplus of matter over antimatter, so their matter and antimatter must survive in equal numbers. At assembly level, whatever density the dark-matter paper's premise E asks of them, that survival needs either a deposited population that something keeps from annihilating, or a freeze-out at weak coupling. The series derives neither.

## one-liner
At assembly level and given E, the odd towers' symmetric matter can fill E's density only by a protected deposited count or a weak-coupling freeze-out, and neither is derived.
