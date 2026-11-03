---
id: dark-tower-matter.where-mass-begins
kind: claim
version: 2
title: Where mass begins in each causal tower
status: proved
region: dark-tower-matter
subject: dark-matter
tags: [mass-generation, null-directions]
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
  - dark-tower-matter.adjoint-norm@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_T14c.py
  tags:
  - id:B4
  - id:B5
  - id:B6
  - id:B7
- kind: check
  ref: check.py::check_dimensions_three_four_pair_law
- kind: check
  ref: check.py::check_dimension_five_single_law
- kind: check
  ref: check.py::check_momenta_in_one_half_space
locators:
  paper: T14c
  number: Thm 3.5
  label: thm:onset
  line: 359
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: mass laws m^2 = 2 <x x^dag>_0 (n = 3, 4) and (1/2) <x x^dag>_0 (n = 5) as polynomial identities in the six causal towers, alternation and nonempty massless cone, half-space law Q(e_t) j.e_t = <psi psi^dag>_0. Version 1 -> 2.'
  env: theorem
  typing:
    by: ai-typing-pass
    added:
    - obj.dark-tower-matter.ideals-fields-momentum
    note: 'Kept the norm lemma, cited for nonnegativity and the half-cone; added the definition as about.
      Levels pass: levels written from scratch, keeping every condition and level qualifier of the formal
      statement.'
about:
- obj.dark-tower-matter.ideals-fields-momentum
---

## formal
Let $\psi, \psi_{1}, \psi_{2} \in S$ in a causal tower of dimension $n$.
\begin{enumerate}
\item[(i)] For $n = 3$ and $n = 4$ the reversion pairing is alternating, $\rev{\psi}\psi = 0$, every single constituent's momentum is null, and
\[
m^{2}\bigl(j(\psi_{1}) + j(\psi_{2})\bigr) \;=\; 2\,\ip{xx^{\dagger}}_{0}, \qquad x = \rev{\psi}_{1}\psi_{2}.
\]
Mass begins at two constituents; it vanishes exactly when $\rev{\psi}_{1}\psi_{2} = 0$.
\item[(ii)] For $n = 5$ the reversion pairing is not alternating, and
\[
m^{2}\bigl(j(\psi)\bigr) \;=\; \tfrac{1}{2}\,\ip{xx^{\dagger}}_{0}, \qquad x = \rev{\psi}\psi,
\]
which vanishes on a nonzero proper cone in $S$. Mass begins at one constituent.
\end{enumerate}
In every causal tower the total momentum of any number of constituents is timelike or null, never spacelike.

## technical
For constituents $\psi, \psi_1, \psi_2$ in the spinor ideal $S$ of a causal tower of dimension $n$: when $n = 3$ or $4$ the reversion pairing is alternating, $\rev{\psi}\psi = 0$, every single constituent's momentum is null, and $m^2(j(\psi_1) + j(\psi_2)) = 2\langle xx^\dagger\rangle_0$ with $x = \rev{\psi}_1\psi_2$, so mass begins at two constituents and vanishes exactly when $\rev{\psi}_1\psi_2 = 0$. When $n = 5$ the pairing is not alternating, and $m^2(j(\psi)) = \tfrac12\langle xx^\dagger\rangle_0$ with $x = \rev{\psi}\psi$, which vanishes on a nonzero proper cone in $S$: mass begins at one constituent.

In every causal tower the total momentum of any number of constituents is timelike or null, never spacelike.

## lay
A single constituent in a three- or four-dimensional tower always moves like light; mass appears only when two combine, and then only if they are not aligned in a particular way. In five dimensions a single constituent can already be massive. In every tower with a time direction, collections of constituents never move faster than light.

## one-liner
Mass begins at two constituents in dimensions three and four, where the reversion pairing is alternating, and at one constituent in dimension five, and total momenta are never spacelike.
