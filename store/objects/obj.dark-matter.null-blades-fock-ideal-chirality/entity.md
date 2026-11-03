---
id: obj.dark-matter.null-blades-fock-ideal-chirality
kind: object
version: 1
title: Null blades, the Fock ideal, and chirality
status: defined
region: dark-matter
subject: dark-matter
tags:
- witt-index
- spinor-modules
- chirality
- null-directions
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
locators:
  paper: T14
  number: Def 3.8
  label: def:fock
  line: 241
extraction:
  env: definition
  typing:
    by: ai-typing-pass
    note: Definition only; no edges changed.
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants:
    - dark-matter.two-families-are-two-chiralities (about)
    added_about: []
    verdict: connected
    note: Added about from the two-families proposition, whose statement uses the null blade and the Fock
      grade.
---

## formal
Let $V_{\C}$ be the complexified ambient of a representative, of dimension $2m$ or $2m + 1$, and let $V_{\C} = W \oplus W'$ ($\oplus\, \C\ell$ in odd dimension) be a Witt decomposition into a maximal isotropic subspace $W$ and a dual isotropic complement $W'$, with null bases $w_{1}, \ldots, w_{m}$ of $W$ and $v_{1}, \ldots, v_{m}$ of $W'$ normalised so that $v_{i}w_{j} + w_{j}v_{i} = \delta_{ij}$, and, in odd dimension, an extra unit generator $\ell$ orthogonal to both. The \emph{null blade} of $W$ is $f = w_{1}w_{2}\cdots w_{m}$, and it is annihilated by $W$ from the left: $wf = 0$ for every $w \in W$. The \emph{pseudoscalar} is $I = e_{1}\cdots e_{\dim V}$ for an orthonormal basis, normalised by a fourth root of unity so that $I^{2} = 1$ (the sign of $I$ is a convention; only ratios of its eigenvalues are used below); in even dimension it anticommutes with every vector, in odd dimension it is central. The \emph{Fock ideal} is, in even dimension, the left ideal $S = \Cl(V_{\C})\,f$, spanned by the $2^{m}$ states $v_{i_{1}}\cdots v_{i_{k}}f$ ($i_{1} < \cdots < i_{k}$), the \emph{Fock grade}-$k$ states (counting creation operators, not the Clifford grade); it is the spinor module. In odd dimension the left ideal $\Cl(V_{\C})\,f$ has dimension $2^{m+1}$ and is the sum of the two irreducible modules; the Fock ideal is then either chirality-projected half, $S_{\pm} = \tfrac{1}{2}(1 \pm I)\,\Cl(V_{\C})\,f$, of dimension $2^{m}$, graded by the Fock grade of the projected states $\tfrac{1}{2}(1 \pm I)\,v_{i_{1}}\cdots v_{i_{k}}f$, on which $I$ acts as $\pm 1$ and the extra generator $\ell$ acts as that grade's parity up to a fixed scalar. A state $\psi \in S$ with $I\psi = \pm\psi$ has \emph{chirality} $\pm 1$. For a maximal isotropic subspace $U \subset V_{\C}$, a \emph{pure spinor of $U$} is a nonzero $\psi_{U} \in S$ with $U\psi_{U} = 0$.

## technical
Take a Witt decomposition $V_{\C} = W \oplus W'$ (with an extra $\C\ell$ in odd dimension) of the complexified ambient, with null bases $w_{i}$ of $W$ and $v_{i}$ of $W'$ normalised so that $v_{i}w_{j} + w_{j}v_{i} = \delta_{ij}$. The null blade $f = w_{1}\cdots w_{m}$ satisfies $wf = 0$ for every $w \in W$. In even dimension the Fock ideal $S = \Cl(V_{\C})\,f$ is spanned by the $2^{m}$ states $v_{i_{1}}\cdots v_{i_{k}}f$, graded by the number $k$ of creation operators, and is the spinor module. In odd dimension $\Cl(V_{\C})\,f$ has dimension $2^{m+1}$, and the Fock ideal is either half $S_{\pm} = \tfrac{1}{2}(1 \pm I)\,\Cl(V_{\C})\,f$, with $I$ the pseudoscalar normalised so that $I^{2} = 1$. Chirality is the eigenvalue $\pm 1$ of $I$ on a state, and a pure spinor of a maximal isotropic $U$ is a nonzero $\psi_{U} \in S$ with $U\psi_{U} = 0$.

## lay
These definitions build spinors, the objects that describe matter particles, out of a geometric algebra. The directions are split into null pairs, one member of each acting as an annihilator and the other as a creator. The product of the annihilators gives a vacuum state, and applying creators to it produces a basis of states, counted by how many creators were used. Chirality, a state's handedness, is read off from how the algebra's top element acts on it.

## one-liner
A Witt decomposition of the complexified ambient defines the null blade as Fock vacuum, the Fock ideal of spinor states graded by creation number, chirality as the pseudoscalar eigenvalue, and pure spinors as states annihilated by a maximal isotropic subspace.
