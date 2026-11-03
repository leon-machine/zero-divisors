---
id: rule2.where-obstruction-sits-commuting-square
kind: claim
version: 5
title: Where the obstruction sits, and the commuting square
status: proved
region: rule2
subject: completion
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
  source: 'authorship disclosure of T17-rule2, the series'' standard disclaimer'
review: typed
about:
- obj.transport.obstruction-types
derivations:
- name: main
  uses:
  - rule2.even-subalgebra-one-dimensional-extension@4
  - rule2.imported-classification-centre-type-c@3
  - rule2.imported-rule-2-matrix-units-forgotten@3
  - transport.rule-1-morita-trivial@5
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T17_rule2.py
  tags:
  - label:thm:extension
- kind: check
  ref: check.py::check_exactly_one_extension_obstructed
- kind: check
  ref: check.py::check_ideals_are_copies_of_a
- kind: check
  ref: check.py::check_opposite_sign_repair_is_rule_one_ascent
- kind: check
  ref: check.py::check_same_sign_repair_definite_two_residues_away
locators:
  paper: T17-rule2
  number: Thm 2.2
  label: thm:extension
  line: 129
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: for every even (p,q) with n <= 6: exactly one obstructed extension, its ideals copies of A via explicit generators, the opposite-sign repair as the Rule 1 ascent with ladder pair and matrix units, and the definite same-sign repair two residues away. Version 3 -> 4. Check strengthened: eps_+ idempotency and the bare-generator squares (e_i nu)^2 = -s e_i^2 for all i pinned; rank cap moved to module level. Version 4 -> 5.'
  env: theorem
  typing:
    by: ai-typing-pass
    note: 'All four premises are invoked in the proof and kept; the paper presents the theorem as its
      own contribution, so there is no standard route. Linked equivalent_to transport.where-obstruction-lies-commuting-square:
      the companion note restates it.'
equivalent_to:
- transport.where-obstruction-lies-commuting-square@4
---

## formal
Let $A = \Cl(p,q)$ with $n = p + q$ even, and let $A_s = \Cl(p,q{+}1)$ and $A_t = \Cl(p{+}1,q)$ be its spacelike and timelike one-dimensional extensions.
\begin{enumerate}
\item[(a)] Exactly one of $A_s$, $A_t$ carries the type-C obstruction: $A_s$ if $p - q \equiv 2 \pmod 4$, $A_t$ if $p - q \equiv 0 \pmod 4$. The other has complex type: its volume element is central with square $-1$, its centre is $\C$, and it is simple.
\item[(b)] Each of the two ideals of the obstructed extension is a copy of $A$: $\varepsilon_\pm A_s \cong \Cl^0(p,q{+}1) \cong A$ in the first case, $\varepsilon_\pm A_t \cong \Cl^0(p{+}1,q) \cong \Cl(q,p) \cong A$ in the second (the last isomorphism because the residues $0$ and $4$ are fixed by negation mod $8$).
\item[(c)] The Rule 2 repair of the obstructed extension by a generator of the opposite sign is $\Cl(p{+}1,q{+}1)$, the Rule 1 ascent of $A$: the two adjoined generators $e_{n+1}$ (the extension) and $\nu$ (the repair) span a hyperbolic plane, the null vectors $f = \tfrac12(\nu \pm e_{n+1})$, $f^* = \tfrac12(\nu \mp e_{n+1})$ (signs chosen so that each is null) are the ladder pair of Fact \claimref{transport.rule-1-morita-trivial}, and the two amplifications agree: $\Mat_2(\Cl^0(\text{extension})) = \Mat_2(A)$. The residue returns to $d$.
\item[(d)] The Rule 2 repair by a generator of the same sign is $\Cl(p,q{+}2)$ or $\Cl(p{+}2,q)$, isomorphic to $\Cl(p{+}1,q{+}1)$ as an algebra, at residue $d \mp 2$; the adjoined plane is definite, carries no null vector, and admits no Rule 1 reading.
\end{enumerate}

## technical
Let $A = \Cl(p,q)$ with $n = p + q$ even, and compare its two one-dimensional extensions, the spacelike $A_s = \Cl(p,q{+}1)$ and the timelike $A_t = \Cl(p{+}1,q)$. Exactly one of them carries the type-C obstruction: $A_s$ when $p - q \equiv 2 \pmod 4$ and $A_t$ when $p - q \equiv 0 \pmod 4$. The other is of complex type, with central volume element of square $-1$ and centre $\C$, and is simple. Each of the two ideals $\varepsilon_\pm$ of the obstructed extension is isomorphic to the even subalgebra of that extension, which is in turn a copy of $A$.

Repairing the obstructed extension by Rule 2 with a generator $\nu$ of the opposite sign gives $\Cl(p{+}1,q{+}1)$, the Rule 1 ascent of $A$: the extension direction $e_{n+1}$ and $\nu$ span a hyperbolic plane, the null vectors $\frac12(\nu \pm e_{n+1})$ form the Rule 1 ladder pair, and the two amplifications agree, $\Mat_2(\Cl^0(\text{extension})) = \Mat_2(A)$, with the residue back at $d$. A repair by a generator of the same sign gives $\Cl(p,q{+}2)$ or $\Cl(p{+}2,q)$, isomorphic to $\Cl(p{+}1,q{+}1)$ as an algebra but at residue $d \mp 2$; its adjoined plane is definite, has no null vector, and admits no Rule 1 reading.

## lay
Take a geometry with an even number of dimensions and add one more direction, either of space or of time. Exactly one of the two choices produces an algebra that splits into two independent halves, and each half turns out to be a copy of the original algebra. Repairing that split by adding a further direction of the opposite kind lands on the same enlarged algebra as the series' other repair rule, so here the two rules agree. Adding a further direction of the same kind gives an algebra of the same shape, but it cannot be read as the other rule, because the added plane contains no light-like direction.

## one-liner
For even-dimensional $\Cl(p,q)$, exactly one of its two one-dimensional extensions carries type C, its ideals are copies of $\Cl(p,q)$, and its opposite-sign Rule 2 repair is the Rule 1 ascent $\Cl(p{+}1,q{+}1)$, while the same-sign repair is isomorphic as an algebra but admits no Rule 1 reading.
