---
id: dark-tower-matter.third-pairs-unit-five-dimensions
kind: claim
version: 4
title: The third pair's unit in five dimensions
status: proved
region: dark-tower-matter
subject: dark-matter
tags: [ladder-pairs, pseudoscalar-and-centre]
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
  - dark-tower-matter.constituents-field@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_T14c.py
  tags:
  - id:D2
  - id:D3
  - id:D4
  - id:D5
  - id:D6
  - id:D7
  - id:D8
  - id:D9
  - id:D10
  - id:D11
  - id:D12
- kind: check
  ref: check.py::check_r3_unit_and_three_pairs
- kind: check
  ref: check.py::check_r3_units_anticommuting_with_i7
- kind: check
  ref: check.py::check_r5_no_canonical_unit
- kind: check
  ref: check.py::check_r5_third_pair_for_every_unit
- kind: check
  ref: check.py::check_r5_units_conjugate
locators:
  paper: T14c
  number: Thm 4.2
  label: thm:unit
  line: 452
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: 16-dim modules of Cl(5,2), Cl(2,5) as tensor-word matrices: commutants H, I7 unit, CAR of three pairs, u(3) closure 9 and centraliser 2, units anticommuting with I7 act as the grade involution, closure 30, r = 5 units sampled and conjugate. Version 2 -> 3. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 3 -> 4.'
  env: theorem
  context_refs:
  - dark-tower-matter.constituents-field
  typing:
    by: ai-typing-pass
    added:
    - dark-tower-matter.constituents-field
    note: 'Added the constituent''s field (context ref), which the statement names as the source of the
      spin commutant H on which it works. Levels pass: levels written from scratch, keeping every condition
      and level qualifier of the formal statement.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-tower-matter.constituents-field
---

## formal
Work on the sixteen-dimensional irreducible module of the conformal algebra, which is the constituent ideal $T$ as a module of the spin group, with spin commutant $\HH$ (Theorem \claimref{dark-tower-matter.constituents-field}).
\begin{enumerate}
\item[(i)] ($r = 3$) The pseudoscalar $I_{7}$ of $\Cl(5,2)$ lies in $\HH$, squares to $-1$ and commutes with every vector. With it the third pair $\tfrac{1}{2}(e_{a} \pm I_{7}e_{b})$ joins two real pairs to give three pairs obeying the canonical relations, and their bilinears $I_{7}(v_{i}w_{i} - \tfrac{1}{2})$, $v_{i}w_{k} - v_{k}w_{i}$, $I_{7}(v_{i}w_{k} + v_{k}w_{i})$ span a Lie algebra $\uu(3)$ whose centraliser in $\HH$ is $\mathrm{span}\{1, I_{7}\}$.
\item[(ii)] ($r = 3$) Every unit $J \in \HH$ anticommuting with $I_{7}$ anticommutes with every vector, so it acts as the grade involution: it fixes the real pairs up to sign and sends $w_{3}$ to $-\bar{w}_{3}$, exchanging the third pair's creator and annihilator; $\uu(3)$ and $J$ generate a Lie algebra of dimension $30$, not the commuting sum $\su(2) \oplus \uu(3)$ of dimension $12$.
\item[(iii)] ($r = 5$) No element of $\HH$ outside $\R$ commutes with all of $\HH$, and $\omega$ squares to $+1$: the algebra supplies no canonical unit. Every unit $u \in \HH$ commutes with the vectors and builds a third pair, $w_{3} = \tfrac{1}{2}(e_{a} + ue_{b})$, $v_{3} = -\tfrac{1}{2}(e_{a} - ue_{b})$ with $Q(e_{a}) = Q(e_{b}) = -1$; the resulting $\uu(3)_{u}$ has centraliser $\mathrm{span}\{1, u\}$ in $\HH$, and a second unit anticommuting with $u$ generates dimension $30$ with it. Any two units are conjugate in $\HH$: $(1 - u'u)\,u = u'(1 - u'u)$ for $u' \neq -u$, and $u' = -u$ is reached by conjugation with any unit anticommuting with $u$. The choices form the sphere $Sp(1)/U(1) = S^{2}$.
\end{enumerate}

## technical
On the sixteen-dimensional irreducible module of the conformal algebra, the constituent ideal, with spin commutant $\HH$. At $r = 3$ the pseudoscalar $I_7$ of $\Cl(5,2)$ lies in $\HH$, squares to $-1$ and commutes with every vector, and the third pair $\tfrac12(e_a \pm I_7e_b)$ joins the two real pairs to give three pairs obeying the canonical relations, whose bilinears span a $\uu(3)$ with centraliser $\mathrm{span}\{1, I_7\}$ in $\HH$. Every unit $J \in \HH$ anticommuting with $I_7$ acts as the grade involution, sends $w_3$ to $-\bar w_3$, and with $\uu(3)$ generates a Lie algebra of dimension $30$, not the twelve-dimensional $\su(2) \oplus \uu(3)$.

At $r = 5$ the algebra supplies no canonical unit: no element of $\HH$ outside $\R$ is central, and $Q(\omega) = +1$. Every unit $u \in \HH$ builds a third pair, $w_3 = \tfrac12(e_a + ue_b)$, $v_3 = -\tfrac12(e_a - ue_b)$ with $Q(e_a) = Q(e_b) = -1$, giving $\uu(3)_u$ with centraliser $\mathrm{span}\{1, u\}$; any two units are conjugate in $\HH$, and the choices form the sphere $Sp(1)/U(1) = S^2$.

## lay
The five-dimensional towers need a square root of minus one to build their third internal pair. In one of them the algebra itself provides exactly one such root, and every other candidate spoils the pair structure. In the other the algebra provides none, so any of a whole sphere of quaternionic roots will do, all equivalent to one another.

## one-liner
At $r = 3$ the pseudoscalar $I_7$ is the unit that builds a third pair with $\uu(3)$ symmetry, other quaternionic units spoiling it, while at $r = 5$ every unit $u \in \HH$ does, the choices forming a sphere $S^2$.
