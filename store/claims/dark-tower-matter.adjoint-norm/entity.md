---
id: dark-tower-matter.adjoint-norm
kind: claim
version: 3
title: The adjoint and the norm of the field
status: proved
region: dark-tower-matter
subject: dark-matter
tags: [idempotents, spinor-modules]
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
  - dark-tower-matter.imported-clifford-structure@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_T14c.py
  tags:
  - id:B0
  - id:B1
  - id:B2
  - id:B3
- kind: check
  ref: check.py::check_blade_adjoint_norms
- kind: check
  ref: check.py::check_corner_conjugation_and_positive_norm
- kind: check
  ref: check.py::check_norm_law
locators:
  paper: T14c
  number: Lem 3.4
  label: lem:norm
  line: 293
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: e_K e_K^dag = Q(e_t)^|K|, the corner conjugation x^dag x = N(x) f with N positive, and the norm law j(psi x) = N(x) j(psi), as polynomial identities in the six causal towers. Version 1 -> 2. Sample inputs moved to module level; no change to what is tested. Version 2 -> 3.'
  env: lemma
  typing:
    by: ai-typing-pass
    added:
    - obj.dark-tower-matter.ideals-fields-momentum
    note: 'Kept the Clifford-structure fact, which the proof cites for the corner being a division algebra;
      added the definition as about. Levels pass: levels written from scratch, keeping every condition
      and level qualifier of the formal statement.'
about:
- obj.dark-tower-matter.ideals-fields-momentum
---

## formal
In a causal tower:
\begin{enumerate}
\item[(i)] $e_{K}e_{K}^{\dagger} = Q(e_{t})^{|K|}$ for every basis blade $e_{K}$, so $e_{K}e_{K}^{\dagger} = 1$ on every even blade and, for even $x$, $\ip{xx^{\dagger}}_{0}$ is the sum of the squares of $x$'s coordinates;
\item[(ii)] $f^{\dagger} = f$, and for $x \in f\Cl^{0}(V)f$,
\[
x^{\dagger}x \;=\; xx^{\dagger} \;=\; N(x)\,f, \qquad N(x) = 2\ip{xx^{\dagger}}_{0} \geq 0,
\]
with $N(x) = 0$ only at $x = 0$;
\item[(iii)] for $\psi \in S$ and $x \in f\Cl^{0}(V)f$,
\[
j(\psi x) \;=\; N(x)\, j(\psi).
\]
\end{enumerate}

## technical
In a causal tower with time direction $e_t$, the adjoint $x^\dagger = e_t\rev{x}e_t^{-1}$ satisfies $e_Ke_K^\dagger = Q(e_t)^{|K|}$ on every basis blade, so on the even algebra $\langle xx^\dagger\rangle_0$ is the sum of the squares of the coordinates of $x$. The idempotent $f$ is self-adjoint, and on the corner algebra $f\Cl^0(V)f$, which is $\R$, $\C$ or $\HH$, the adjoint is the standard conjugation: $x^\dagger x = xx^\dagger = N(x)f$ with $N(x) = 2\langle xx^\dagger\rangle_0 \geq 0$, zero only at $x = 0$.

Right multiplication by a corner element scales the momentum by its norm: $j(\psi x) = N(x)\,j(\psi)$ for every $\psi$ in the spinor ideal $S$.

## lay
In each tower with a time direction, the numbers a constituent carries (real, complex or quaternionic) come with a conjugation built from reversal and the time direction. This lemma shows that this conjugation is the usual one, so every nonzero number has a positive size. Multiplying a constituent's spinor by such a number multiplies its momentum by that size.

## one-liner
In a causal tower the adjoint $e_t\rev{x}e_t^{-1}$ is the standard conjugation on the corner field, with positive norm $N(x)$, and $j(\psi x) = N(x)\,j(\psi)$.
