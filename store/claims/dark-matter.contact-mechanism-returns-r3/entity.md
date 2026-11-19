---
id: dark-matter.contact-mechanism-returns-r3
kind: claim
version: 4
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
- name: Claude Fable 5.2
  role: 'restated on Premise E: the contact clauses read on the ball in which E counts mass; clause (iv) on what the count gives on a quantum''s own cell'
  version: 4
  source: maintainer pass of 2026-11-19
amendments:
- version: 4
  kind: restatement
  defect: 'version 3 stated the mechanism under R1 and R2, with the contact ball a quantum''s cell; by the decision of 19 November 2026 the total rests on equal mass per unit ball and R3''s unit is one common length, and the statement did not say on which ball the contact clause is read'
  evidence: check.py::check_own_cell_reading_differs
review: typed
derivations:
- name: main
  uses:
  - dark-matter.direction-nesting-adds-algebra@3
  - dark-matter.nesting@3
  - dark-matter.projection-every-towers-content-dilutes-ones@3
  assumes:
  - dark-matter.e-equal-mass-per-unit-ball@1
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
- kind: check
  ref: check.py::check_own_cell_reading_differs
- kind: check
  ref: check.py::check_own_cell_sheets_use_our_cell
locators:
  paper: T14
  number: Prop 7.12
  label: prop:thickness
  line: 895
extraction:
  maintainer_pass_2026_11_19:
    by: maintainer-2026-11-19
    date: '2026-11-19'
    note: 'Version 3 -> 4. Leon''s decision of 19 November 2026: the total rests on Premise E (dark-matter.e-equal-mass-per-unit-ball) and R3''s unit is E''s length. The mechanism is restated under E in place of R1 and R2: the clauses C and I are read on mass elements and on the ball of radius d in which E counts mass, and the count returns the thickness d with no use of a quantum''s mass or number. Assumes edges: E added, R1 and R2 removed. New clause (iv): read on a quantum''s own cell with R2 dropped, the same count gives a five-dimensional tower its own cell radius as the thickness and a three-dimensional tower''s sheets this world''s own cell radius as their spacing, with shares E does not fix. The clause text says that on E''s ball C with I restates R3''s five-dimensional clause, so that S and O carry what the mechanism adds. One check function added; the others reworked on mass densities.'
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
Under Premise E (\claimref{dark-matter.e-equal-mass-per-unit-ball}) and the clauses C, I, S and O, read on the ball of radius $d$ in which E counts mass:
\begin{enumerate}
\item[(i)] a five-dimensional tower's matter sources this world through exactly one length $d$ of its extra direction, so $f_{5\mathrm{D}} = \tfrac{V_{3}}{V_{4}}$;
\item[(ii)] a three-dimensional tower's sheets are one length $d$ apart, so $f_{3\mathrm{D}} = \tfrac{V_{3}}{V_{2}}$;
\item[(iii)] hence the mechanism returns R3: its unit is the length of Premise E, its one side is S, which supplies a factor one half against the two-sided count, and the equality of its two thicknesses is O. The length $d$ cancels and the total is Proposition \claimref{dark-matter.unit-ball-rule}'s;
\item[(iv)] the clauses are read on E's ball, and the result depends on that. Read instead on a quantum's own cell, the ball of its tower's own cell radius, with R2 not assumed, the same count gives a five-dimensional tower that keeps E the thickness $a_{r}$, its own cell radius, and the share $\tfrac{V_{3}}{V_{4}}\,(a_{r}/d)$: with quanta sixteen times heavier and rarer, $a_{r} = 2d$ and the share doubles. For a three-dimensional tower the count is made on this world's matter, so on own cells its sheets come out this world's own cell radius $a_{6}$ apart and its share is $\tfrac{V_{3}}{V_{2}}\,(d/a_{6})$, whatever its own quanta are; that is not the own-cell reading of R3, in which the spacing is the tower's own cell radius.
\end{enumerate}
The clauses, as read here: C, contact, a mass element sources a world when the ball of radius $d$ about it meets that world's space; I, indivisibility, it then counts in full; S, side, it sources on one side only, the side named by the sign of $\omega$; O, reciprocity, the ratio of densities read on the nested world's space is the ratio read on ours. Read on mass elements, I is the choice of a uniform weight for the matter within $d$ and no longer expresses the indivisibility of a quantum, and the ball of C is E's and not an object a tower's matter supplies. So C with I restates R3's clause for the five-dimensional towers in the unit $d$, and what the mechanism adds to R3 is S, the one side with its factor one half, and O, the equality of the two thicknesses.

## technical
Assume Premise E, equal mass $\mu$ per ball of radius $d$ in every populated tower, and four clauses read on that ball: contact (a mass element sources a world when the ball of radius $d$ about it meets that world's space), indivisibility (it then counts in full), side (it sources on one side only, the side named by the sign of $\omega$) and reciprocity. For a five-dimensional tower with our space the hyperplane $x_{4} = 0$, the matter at height $h$ that sources our world is that with $0 \le h \le d$ on its side, giving $\int_{0}^{d} \mu\,dh/(V_{4}d^{4}) = \mu/(V_{4}d^{3})$ per unit three-volume against our $\mu/(V_{3}d^{3})$, so $f_{5\mathrm{D}} = V_{3}/V_{4}$. For a three-dimensional tower the count runs downward on its own plane, giving $\rho_{\mathrm{us}}/\rho_{3\mathrm{D}} = V_{2}/V_{3}$, and reciprocity forces its sheets to be one length $d$ apart, so $f_{3\mathrm{D}} = V_{3}/V_{2}$.

So the mechanism returns the one-unit-per-unshared-direction rule: its unit is the length of Premise E, the side clause supplies the factor one half against two-sided contact, and reciprocity is the equality of the two thicknesses. The length $d$ cancels and the total is the unit-ball rule's. No quantum's mass or number is used. The clauses are read on E's ball: read on a quantum's own cell with R2 dropped, the same count gives a five-dimensional tower its own cell radius as the thickness and a three-dimensional tower's sheets this world's own cell radius as their spacing, and shares that E does not fix. On E's ball the contact and indivisibility clauses restate R3's five-dimensional clause; what the mechanism adds is the one side and the equality of the two thicknesses.

## lay
The rule for how much a hidden world's matter weighs on ours contained a free choice: how thick a slice of the hidden direction counts. This result shows that a simple contact picture gives the assumed value, once every world holds the same mass per ball of one common radius (E) and the picture is drawn with that ball: a piece of hidden matter counts if the ball of that radius around it touches our space, it counts in full, it acts from one side only, and the counting works the same way in both directions (reciprocity). Under those assumptions the thickness comes out as exactly one such radius, the value the rule had assumed (R3). Nothing is assumed about how heavy or how numerous the hidden particles are. The ball in the contact picture has to be that common ball: if it is taken to be a particle's own cell, whose size depends on how numerous the particles are, the thickness changes with it and the formula's value is lost. Drawn with the common ball, the picture is close to the assumption itself: what it adds is that hidden matter acts from one side only and that the two kinds of slice are equally thick.

## one-liner
Under Premise E (equal mass per ball of one radius $d$) and the contact, indivisibility, side and reciprocity clauses read on that ball, counting the matter whose ball meets our space gives shares $V_{3}/V_{4}$ and $V_{3}/V_{2}$, returning the one-unit thickness rule with $d$ cancelling and no quantum's mass or number used; on that ball the contact and indivisibility clauses restate R3, and the side and reciprocity clauses carry what is added.
