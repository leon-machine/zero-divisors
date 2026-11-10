---
id: dark-matter.contact-mechanism-returns-r3
kind: claim
version: 3
title: The contact mechanism returns R3
status: proved
region: dark-matter
subject: dark-matter
tags: [counting-rules, dark-matter-ratio]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14, deposited version
review: typed
derivations:
- name: main
  uses:
  - dark-matter.direction-nesting-adds-algebra@3
  - dark-matter.nesting@3
  - dark-matter.projection-every-towers-content-dilutes-ones@3
  assumes:
  - dark-matter.r1-equal-mass-per-quantum@1
  - dark-matter.r2-one-quantum-per-unit-ball@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_five_dimensional_count
- kind: check
  ref: check.py::check_side_is_immaterial
- kind: check
  ref: check.py::check_three_dimensional_sheets
- kind: check
  ref: check.py::check_total_and_alternatives
locators:
  paper: T14
  number: Prop 7.12
  label: prop:thickness
  line: 895
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the one-sided slab count 1/V_4 and f_5D = 8/(3 pi), the side choice through the two omega components of Cl(1,4), the downward count V_2/V_3 and O solving to s = 1, the total and its alternatives. Version 2 -> 3.'
  env: proposition
  context_refs:
  - dark-matter.unit-ball-rule
  unresolved_refs:
  - rem:scope
  eqrefs: 1
  typing:
    by: ai-typing-pass
    added:
    - dark-matter.r1-equal-mass-per-quantum
    - dark-matter.r2-one-quantum-per-unit-ball
    note: 'Added R1 and R2 as assumptions since the statement is under them; the clauses C, I, S and O
      are not store entities and stay unedged; the unit-ball rule is not edged because its total is the
      comparison the mechanism reproduces and that rule itself rests on R3, which the mechanism replaces.
      Levels pass: lay now names R1 and R2 and the reciprocity clause O, which it had dropped.'
---

## formal
Under R1, R2 and the clauses C, I, S and O:
\begin{enumerate}
\item[(i)] a five-dimensional tower's matter sources this world through exactly one cell radius of its extra direction, so $f_{5\mathrm{D}} = \tfrac{V_{3}}{V_{4}}$;
\item[(ii)] a three-dimensional tower's sheets are one cell radius apart, so $f_{3\mathrm{D}} = \tfrac{V_{3}}{V_{2}}$;
\item[(iii)] hence the mechanism returns R3: its unit is the cell radius R2 chose, its one side is S, which supplies a factor one half against the two-sided count, and the equality of its two thicknesses is O. The spacing $d_{b}$ cancels and the total is Proposition \claimref{dark-matter.unit-ball-rule}'s.
\end{enumerate}

## technical
Assume equal mass per quantum, one quantum per unit ball, and four clauses: contact (a quantum sources a world when its cell meets that world's space), indivisibility (it then counts whole), side (it sources on one side only, the side named by the sign of $\omega$) and reciprocity. For a five-dimensional tower with our space the hyperplane $x_{4} = 0$, the quanta at height $h$ that source our world are those with $0 \le h \le 1$ on their side, giving $\int_{0}^{1} dh/V_{4} = 1/V_{4}$ per unit three-volume, so $f_{5\mathrm{D}} = V_{3}/V_{4}$. For a three-dimensional tower the count runs downward on its own plane, giving $\rho_{\mathrm{us}}/\rho_{3\mathrm{D}} = V_{2}/V_{3}$, and reciprocity forces its sheets to be one cell radius apart, so $f_{3\mathrm{D}} = V_{3}/V_{2}$.

So the mechanism returns the one-cell-per-unshared-direction rule: its unit is the cell radius of the unit-ball premise, the side clause supplies the factor one half against two-sided contact, and reciprocity is the equality of the two thicknesses. The spacing $d_{b}$ cancels and the total is the unit-ball rule's.

## lay
The rule for how much a hidden world's matter weighs on ours contained a free choice: how thick a slice of the hidden direction counts. This result shows that a simple contact picture fixes it, assuming equal mass per particle (R1) and one particle per unit ball (R2): a hidden particle counts if its small cell touches our space, it counts in full, it acts from one side only, and the counting works the same way in both directions (reciprocity). Under those assumptions the thickness comes out as exactly one cell, the value the rule had assumed (R3).

## one-liner
Under equal mass per quantum, one quantum per unit ball and the contact, indivisibility, side and reciprocity clauses, counting cells that meet our space gives shares $V_{3}/V_{4}$ and $V_{3}/V_{2}$, returning the one-cell thickness rule with the spacing cancelling.
