---
id: synthesis.imported-free-field-spin-statistics-and-guido-longo-theorem
kind: claim
version: 1
title: 'Imported: free-field spin-statistics and the Guido-Longo theorem'
status: imported
region: synthesis
subject: quantum-fields
tags: [modular-theory, car-algebra, classical-theorem, superselection]
proposed_by:
  kind: ai
  session: maintainer-2026-11-01
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
imported_from:
- citation: 'W. Pauli, The connection between spin and statistics, Phys. Rev. 58 (1940), 716--722.'
  key: Pauli1940
  doi: 10.1103/PhysRev.58.716
- citation: 'D. Guido and R. Longo, An algebraic spin and statistics theorem, Commun. Math. Phys. 172 (1995), 517, arXiv:funct-an/9406005, Theorem 2.11 and Proposition 2.4.'
  key: GuidoLongo1995
  doi: 10.1007/BF02101806
- citation: 'A. Shalabi, M. H. Zambianco and T. R. Perche, The effect of curvature on local observables in quantum field theory, arXiv:2412.12294, equation (11).'
  key: Shalabi2024
- citation: 'R. F. Streater and A. S. Wightman, PCT, Spin and Statistics, and All That, Benjamin (1964).'
  key: StreaterWightman1964
extraction:
  note: >-
    Imported so that the locality result and the modular-period result can pin the two-point function, Pauli's
    argument and the Guido-Longo theorem instead of citing them from memory. Checked on 2026-11-01: the bibliographic
    data of Pauli 1940 (Phys. Rev. 58, 716-722, DOI) and of Guido-Longo (Commun. Math. Phys. 172, 517, 1995, DOI)
    against their INSPIRE records; Guido-Longo against arXiv:funct-an/9406005 v2: Theorem 2.11 (Spin and Statistics)
    holds for a modular covariant pre-cosheaf of field algebras as in Theorem 2.10, which requires the Reeh-Schlieder
    property for spacelike cones and normal (Bose and Fermi) commutation relations, and concludes Gamma = U(2 pi),
    displayed as equation (2.11) (the source uses the number 2.11 for both); Proposition 2.4 derives a positive-energy
    representation of the covering of the Poincare group from modular covariance, Reeh-Schlieder and normal
    commutation relations, so positivity of the energy is derived, not assumed. The massless Wightman function of (i)
    against Shalabi, Zambianco and Perche, arXiv:2412.12294, equation (11) (written there in the mostly-plus
    signature as 1/(4 pi^2(-(t - i eps)^2 + r^2))), which in the store's signature is the form stated. Cited from
    memory, not checked: the content of Pauli's paper beyond the title (the free-field argument of (ii)) and
    Streater-Wightman as a general reference.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created by the maintainer pass of 2026-11-01 (Guido-Longo and the massless two-point function D+ with its spacelike evenness, with Pauli''s free-field argument, as a Fact, by Leon''s list of imports).'
---

## formal
Signature $(+,-,-,-)$.
\begin{enumerate}
\item[(i)] \emph{(The massless two-point function.)} The vacuum two-point function of the free massless scalar field is $D_{+}(\xi) = -\dfrac{1}{4\pi^{2}\bigl(Q(\xi) - i0\,\xi_{0}\bigr)}$; on the open spacelike set $\{Q(\xi) < 0\}$ it is the real function $-1/(4\pi^{2}Q(\xi))$, even under $\xi \to -\xi$ \cite{Shalabi2024, StreaterWightman1964}.
\item[(ii)] \emph{(Pauli's argument.)} For a free field whose particle and antiparticle parts carry a polarisation sum that is a polynomial $P(k)$ homogeneous of degree $d$, the commutator or anticommutator at spacelike separation is a multiple of $(1 \pm (-1)^{d})P(\partial)D_{+}$; with positive metric, locality forces commutators for integer spin and anticommutators for half-integer spin \cite{Pauli1940}.
\item[(iii)] \emph{(Guido and Longo.)} Let a net of field algebras on the spacelike cones of Minkowski space have the Reeh-Schlieder property and normal commutation relations (Bose and Fermi parts graded by a self-adjoint unitary $\Gamma$ fixing the vacuum), and be modular covariant: the modular group of the vacuum for each wedge algebra acts as the wedge's boosts, rescaled by $-2\pi$. Then the net carries a positive-energy representation $U$ of the covering group of the Poincar\'e group, and $\Gamma = U(2\pi)$ \cite{GuidoLongo1995}.
\end{enumerate}

## technical
The free massless field's vacuum correlation is $-1/(4\pi^{2})$ over the spacetime interval with a small imaginary shift fixing the analytic continuation; at spacelike separation it is real and even. Pauli used this to show that a free field of integer spin must commute and one of half-integer spin must anticommute at spacelike separation if the state space has positive norm, the free-field form of the spin-statistics connection. Guido and Longo proved an algebraic version for interacting fields: if the vacuum's modular flow on each wedge is the wedge's boost (modular covariance), and the net has the Reeh-Schlieder property and normal commutation relations, then the operator grading Bose and Fermi fields is the rotation by $2\pi$; positive energy follows and need not be assumed.

## lay
Particles of whole-number spin behave as bosons and those of half-number spin as fermions. For free particles this follows from a short argument of Pauli using the standard formula for how a field's values at two points are correlated. For interacting fields Guido and Longo proved it from a property of the vacuum: that its natural flow in each wedge of spacetime is the geometric boost. The series takes these results as given.

## one-liner
$D_{+}(\xi) = -1/(4\pi^{2}(Q(\xi) - i0\,\xi_{0}))$, real and even at spacelike $\xi$; Pauli's free-field spin-statistics argument; and Guido-Longo: modular covariance, Reeh-Schlieder and normal commutation relations give $\Gamma = U(2\pi)$ with positive energy derived.
