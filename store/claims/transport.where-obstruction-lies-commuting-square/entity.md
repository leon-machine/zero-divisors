---
id: transport.where-obstruction-lies-commuting-square
kind: claim
version: 4
title: Where the obstruction lies, and the commuting square
status: proved
region: transport
subject: zero-divisors
tags: [obstruction-types, transport-algorithm]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T01, deposited version
review: typed
about:
- obj.transport.obstruction-types
derivations:
- name: main
  uses:
  - transport.ascent-renders-grade-involution-inner@3
  - transport.centre@4
  - transport.classification-real-clifford-algebras@3
  - transport.corner-even-subalgebra@4
  - transport.even-subalgebra-one-dimensional-extension@4
  - transport.existence-classification-type-c@4
  - transport.matrix-units-peirce-isomorphism@3
  - transport.rule-1-morita-trivial@5
  - transport.rule-2-ideal-fusion-sharp-form@4
  - transport.sign@3
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T01.py
  tags:
  - num:5.14
- kind: check
  ref: check.py::check_exactly_one_extension_obstructed
- kind: check
  ref: check.py::check_ideals_exchanged_by_grade_involution_inner_after_repair
- kind: check
  ref: check.py::check_ideals_are_copies_of_a
- kind: check
  ref: check.py::check_opposite_sign_repair_is_rule_one_ascent
- kind: check
  ref: check.py::check_same_sign_repair_definite_two_residues_away
locators:
  paper: T01
  number: Thm 5.14
  label: thm:extension
  line: 1293
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: on every even (p,q) with n <= 8 exactly one one-dimensional extension is type C (2 mod 4 spacelike, 0 mod 4 timelike), the other has centre C; ideals copy A via e_i nu (omega); grade involution inner after repair; opposite-sign repair a hyperbolic plane with ladder pairs and Mat_2 corners; same-sign repair definite, two residues away. Version 2 -> 3. Wording fix (Leon 2026-10-23): (c) displays the ladder pair as f = (1/2)(u +- w), f* = (1/2)(u -+ w) with u the adjoined generator of square +1 and w that of square -1, for the earlier (1/2)(nu +- e_{n+1}), right only in the spacelike case (formal). Check strengthened: eps_+ idempotent; anticommutation over all ordered pairs; timelike Cl(q,p) squares of e_i nu for every i with the case count (7) pinned; size limit and blade lists moved to module level. Version 3 -> 4.'
  env: theorem
  typing:
    by: ai-typing-pass
    note: 'Edges kept: every premise is invoked in the proof of one of the four clauses.'
---

## formal
Let $A = \Cl(p,q)$ with $n = p + q$ even, and let $A_s = \Cl(p,q{+}1)$ and $A_t = \Cl(p{+}1,q)$ be its spacelike and timelike one-dimensional extensions.
\begin{enumerate}
\item[(a)] Exactly one of $A_s$, $A_t$ carries the type-C obstruction: $A_s$ if $p - q \equiv 2 \pmod 4$, $A_t$ if $p - q \equiv 0 \pmod 4$. The other has complex type: its volume element is central with square $-1$, its centre is $\C$, and it is simple.
\item[(b)] Each of the two ideals of the obstructed extension is a copy of $A$: $\varepsilon_\pm A_s \cong \Cl^0(p,q{+}1) \cong A$ in the first case, $\varepsilon_\pm A_t \cong \Cl^0(p{+}1,q) \cong \Cl(q,p) \cong A$ in the second (the last isomorphism because the residues $0$ and $4$ are fixed by negation mod $8$).
\item[(c)] The Rule 2 repair of the obstructed extension by a generator of the opposite sign is $\Cl(p{+}1,q{+}1)$, the Rule 1 ascent of $A$: the two adjoined generators $e_{n+1}$ (the extension) and $\nu$ (the repair) span a hyperbolic plane, the null vectors $f = \tfrac12(u \pm w)$, $f^* = \tfrac12(u \mp w)$, with $u$ the adjoined generator of square $+1$ and $w$ that of square $-1$ (both combinations are null; the opposite signs make $ff^* + f^*f = 1$) are the ladder pair of Theorem \claimref{transport.rule-1-morita-trivial}, and the two amplifications agree: $\Mat_2(\Cl^0(\text{extension})) = \Mat_2(A)$. The residue returns to $d$.
\item[(d)] The Rule 2 repair by a generator of the same sign is $\Cl(p,q{+}2)$ or $\Cl(p{+}2,q)$, isomorphic to $\Cl(p{+}1,q{+}1)$ as an algebra, at residue $d \mp 2$; the adjoined plane is definite and carries no null vector, so this adjunction is not the Rule 1 ascent of (c), although the algebra it produces is isomorphic to one.
\end{enumerate}

## technical
Let $A = \Cl(p,q)$ with $n = p + q$ even, with spacelike extension $A_s = \Cl(p, q+1)$ and timelike extension $A_t = \Cl(p+1, q)$. Exactly one of them carries the type-C obstruction: $A_s$ if $p - q \equiv 2 \pmod 4$, $A_t$ if $p - q \equiv 0 \pmod 4$; the other has a central volume element of square $-1$, centre $\C$, and is simple. Each of the two ideals of the obstructed extension is a copy of $A$.

Repairing the obstructed extension by a generator of the opposite sign gives $\Cl(p+1, q+1)$, the Rule 1 ascent of $A$: the extension and repair generators span a hyperbolic plane, their null combinations are the ladder pair, and $\Mat_2(\Cl^0(\text{extension})) = \Mat_2(A)$, back at residue $d$. A same-sign repair gives $\Cl(p, q+2)$ or $\Cl(p+2, q)$, isomorphic as an algebra to $\Cl(p+1, q+1)$ but at residue $d \mp 2$; its adjoined plane is definite and carries no null vector, so it is not the Rule 1 ascent.

## lay
Adding one new direction to an even-dimensional Clifford algebra breaks it into two pieces for exactly one of the two choices, space or time, depending on where it sits in the cycle of eight. Each piece is a copy of the original. Repairing the break with a direction of the opposite kind lands exactly on the standard one-plane enlargement of the original, so the two routes form a commuting square; repairing it with a direction of the same kind gives an isomorphic algebra at a different place in the cycle.

## one-liner
For even-dimensional $\Cl(p,q)$ exactly one one-dimensional extension is type C, its ideals are copies of $\Cl(p,q)$, and its opposite-sign repair is the Rule 1 ascent $\Cl(p+1, q+1)$, closing a commuting square.
