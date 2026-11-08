---
id: std-algebra.bivector-lie-algebra
kind: claim
version: 1
title: Bivectors form the Lie algebra of the orthogonal group
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- rotors-and-stabilisers
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
- obj.std-algebra.grade-projection
- obj.std-algebra.rotor
derivations:
- name: main
  uses:
  - std-algebra.grade-decomposition@2
  - std-algebra.involution-properties@1
  - std-algebra.z2-grading@1
  - std-algebra.vector-squares@1
  - primer.centre@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_commutators_and_skewness
locators:
  sources:
  - key: DoranLasenby2003
    locator: 'Ch. 4 (foundations of geometric algebra: rotors, versors)'
  - key: HestenesSobczyk1984
    locator: Ch. 3 (versors, rotors and the bivector algebra)
extraction:
  by: algebra-core-2026-10-26
---

## formal
For $A, C \in \Cl^{2}(V, Q)$ and $x \in V$, with the commutator product $A \times X = \tfrac12(AX - XA)$:
\begin{equation}
A \times C = \langle A C \rangle_2 \in \Cl^{2}, \qquad A \times x = \langle A x \rangle_1 \in V, \qquad B(A \times x, y) + B(x, A \times y) = 0 .
\end{equation}
So $\Cl^{2}$ is a Lie algebra under $\times$, and $A \mapsto (x \mapsto A \times x)$ is a Lie algebra homomorphism $\Cl^{2} \to \so(V, Q)$, the skew-adjoint maps of $(V, Q)$. When $(V, Q)$ is nondegenerate it is an isomorphism, so $\dim \so(V, Q) = \binom{n}{2}$. The scalar part is cyclic: $\langle X Y \rangle_0 = \langle Y X \rangle_0$.

## technical
Half the commutator of two bivectors is again a bivector, and half the commutator of a bivector with a vector is a vector. The second map is skew with respect to the polar form, so each bivector generates an infinitesimal isometry. In a nondegenerate space every infinitesimal isometry arises this way, from exactly one bivector: the bivectors are the Lie algebra of the rotation group.

## lay
Oriented plane pieces describe small rotations: each plane piece turns arrows a little within its plane. Every small rotation of a nondegenerate space comes from exactly one plane piece, and combining small rotations corresponds to a simple product of plane pieces.

## one-liner
$\Cl^{2}$ is closed under $A \times C = \langle AC \rangle_2$, acts skew-adjointly on $V$ by $A \times x = \langle Ax \rangle_1$, and is isomorphic to $\so(V,Q)$ when $Q$ is nondegenerate.
