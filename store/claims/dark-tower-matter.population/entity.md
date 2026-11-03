---
id: dark-tower-matter.population
kind: claim
version: 2
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
review: typed
derivations:
- name: main
  uses:
  - dark-tower-matter.imported-towers-their-types@4
  - dark-tower-matter.survival-sheets@5
  - dark-tower-matter.five-dimensional-towers@4
  - dark-tower-matter.imported-unit-ball-rule@4
  assumes:
  - dark-matter.r2-one-quantum-per-unit-ball@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
locators:
  paper: T14c
  number: Prop 9.5
  label: prop:population
  line: 838
extraction:
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
The odd towers carry no asymmetry (Fact \claimref{dark-tower-matter.imported-towers-their-types}). Their matter is therefore symmetric, and R2's density must be either a count deposited by the descent and protected from annihilation by kinematics or weakness (Propositions \claimref{dark-tower-matter.survival-sheets}, \claimref{dark-tower-matter.five-dimensional-towers}(vi)), or, in the five-dimensional towers, a weak-coupling freeze-out with the coupling tied to the deposit temperature. Neither is derived. Assembly level.

## technical
At assembly level, given R2. The odd towers carry no asymmetry, so their matter is symmetric, and R2's density must come either from a count deposited by the descent and protected from annihilation by kinematics or weakness (survival on sheets, or the neutral-species branch of the five-dimensional towers), or, in the five-dimensional towers, from a weak-coupling freeze-out with the coupling tied to the deposit temperature. Neither mechanism is derived.

## lay
The odd-dimensional dark towers cannot store a surplus of matter over antimatter, so their matter and antimatter must survive in equal numbers. At assembly level, if the unit-ball density premise R2 holds, that survival needs either a deposited population that something keeps from annihilating, or a freeze-out at weak coupling. The series derives neither.

## one-liner
At assembly level, given R2, the odd towers' symmetric matter needs a protected deposited count or a weak-coupling freeze-out, and neither is derived.
