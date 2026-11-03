---
id: std-algebra.bivector-exponential
kind: claim
version: 1
title: Exponentials of bivectors with scalar square
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- rotors-and-stabilisers
- null-directions
proposed_by:
  kind: ai
  session: algebra-core-2026-10-26
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: typed
trust: ai-proposed
about:
- obj.std-algebra.rotor
derivations:
- name: main
  uses:
  - std-algebra.involution-properties@1
  - std-algebra.vector-squares@1
  - std-algebra.orthogonal-anticommute@1
  - std-algebra.inverse-of-vector@1
  - std-algebra.product-decomposition@1
  - std-algebra.exterior-isomorphism@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_powers_collapse
- kind: check
  ref: check.py::check_closed_forms_are_rotors
locators:
  sources:
  - key: DoranLasenby2003
    locator: 'Ch. 4 (foundations of geometric algebra: rotors, versors)'
  - key: HestenesSobczyk1984
    locator: Ch. 3 (versors, rotors and the bivector algebra)
extraction:
  referee_fixes: '2026-10-26: simple bivectors: (a^b)^2 = B(a,b)^2 - Q(a)Q(b) proved directly; every bivector simple for n <= 3 proved via exterior-isomorphism; the angle absorbed into an unnormalised b stated explicitly (referee part 1, point 7).'
  by: algebra-core-2026-10-26
---

## formal
Let $A \in \Cl^{2}(V, Q)$ with $A^{2} = \lambda \in \R$ (true for every simple bivector $A = a \wedge b$, and for every bivector when $n \le 3$). Then $A^{2k} = \lambda^{k}$, $A^{2k+1} = \lambda^{k} A$, and $e^{A} = \sum_k A^{k}/k!$ is
\begin{equation}
e^{A} =
\begin{cases}
\cos\theta + \dfrac{\sin\theta}{\theta} A, & \lambda = -\theta^{2} < 0,\\[6pt]
\cosh\theta + \dfrac{\sinh\theta}{\theta} A, & \lambda = \theta^{2} > 0,\\[6pt]
1 + A, & \lambda = 0 .
\end{cases}
\end{equation}
In each case $e^{A} (e^{A})^{\sim} = e^{A} e^{-A} = 1$. For orthogonal $a, b$ with $Q(a) \ne 0$, $e^{\phi\, \hat{a}\hat{b}}$ (unit $\hat{a}, \hat{b}$, or $\hat{b}$ null) is the product of two invertible vectors, hence a rotor (\claimref{obj.std-algebra.rotor}): a rotation when $(a \wedge b)^{2} < 0$, a boost when $> 0$, and a null rotation or translation when $= 0$.

## technical
When a bivector squares to a number, its exponential series collapses to two terms. A negative square gives the trigonometric form (a rotation), a positive square the hyperbolic form (a boost), and a zero square, a null bivector, gives exactly $1 + A$ (a null rotation, or a translation in a degenerate algebra). The exponential's reverse is its inverse, and for a simple bivector it is a product of two vectors, so it is a rotor.

## lay
Turning by an angle in a plane is the exponential of the plane piece times the angle, just as $e^{i\theta}$ turns by $\theta$ in the complex plane. Planes whose square is positive give boosts instead of rotations, and planes containing a zero-length direction give the simplest motions of all, written exactly as one plus the plane piece.

## one-liner
If $A^{2} = \lambda \in \R$ then $e^{A}$ is $\cos\theta + \frac{\sin\theta}{\theta}A$, $\cosh\theta + \frac{\sinh\theta}{\theta}A$ or $1 + A$, a rotor with $e^{A}\widetilde{e^{A}} = 1$.
