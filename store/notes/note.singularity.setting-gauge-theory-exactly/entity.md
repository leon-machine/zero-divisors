---
id: note.singularity.setting-gauge-theory-exactly
kind: note
version: 2
title: The gauge theory, exactly
status: setting
subject: einstein
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
comments_on:
- singularity.imported-equivalence-einstein-equations
locators:
  paper: T05
  number: Setting
  section: 'Step 1: locate the failure'
  line: 1299
  subsection: The gauge theory, exactly
extraction:
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Brought to the store convention of obj.synthesis.gtg-flat-spacetime-gauge-fields: the background field strength is written R, the curvature operator is the store-sign R(B) = -R(hb(B)) and the contractions act on it; the torsion equation and the rotation law are written with the adjoint hb^T (the series hb is the map Lasenby, Doran and Gull write with an underbar); the field equation carries the store sign, with the one flip against Doran-Lasenby ch. 14 stated; the dangling eqref was removed.'
---

## formal
In GTG, gravity is a pair of gauge fields on flat spacetime: the position-dependent linear map $\hb(a)$ on vectors, gauging local frame rescalings, and the connection bivector $\Omega(a)$, gauging local Lorentz rotations \cite{LDG1998} (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}). The covariant derivative and the field strength are
\begin{equation}
D_a M \;=\; a\cdot\nabla M + \Omega(a) \times M, \qquad
R(a \wedge b) \;=\; a\cdot\nabla\,\Omega(b) - b\cdot\nabla\,\Omega(a) + \Omega(a) \times \Omega(b),
\end{equation}
with $A \times B := \tfrac12(AB - BA)$ the commutator product, so that $[D_a, D_b]M = R(a \wedge b) \times M$. The curvature operator on physical bivectors is $\mathcal{R}(B) = -R(\hb(B))$, in the store's curvature sign: Lasenby, Doran and Gull \cite{LDG1998} and \cite[Ch.~14]{DoranLasenby2003} use $R(\hb(B))$, and this single overall sign is the only difference. Contracting once and twice with the vector derivative gives the Ricci and scalar curvatures, $\mathcal{R}(b) = \partial_a \cdot \mathcal{R}(a \wedge b)$ and $\mathcal{R} = \partial_a \cdot \mathcal{R}(a)$, and the field equations of the theory are
\begin{equation}
\mathcal{R}(a) - \tfrac12\, a\, \mathcal{R} \;=\; -8\pi\, T(a), \qquad
D \wedge \hb^{T}(a) \;=\; \hb^{T}(\nabla \wedge a) ,
\end{equation}
where $\hb^{T}$ is the adjoint, $a \cdot \hb^{T}(b) = \hb(a) \cdot b$. The first is Einstein's equation in bivector-contracted vector form, with $T(a)$ the matter stress-energy (in the sign of \cite{LDG1998} it reads $+8\pi T(a)$); the second is the vanishing of torsion, which determines $\Omega$ algebraically from $\hb$ and its derivatives, so that $\hb$ carries the theory's entire dynamical content. The metric every observer measures is
\begin{equation}
g(a,b) \;=\; \hb^{-1}(a) \cdot \hb^{-1}(b),
\end{equation}
and the inverse in that formula is where the theory can fail: the geometric reading of the theory exists exactly where $\hb$ is invertible. The theory's two gauge freedoms act by
\begin{equation}
\hb(a) \;\mapsto\; \hb(\tilde U a U), \quad\text{equivalently}\quad \hb^{T}(a) \;\mapsto\; U\,\hb^{T}(a)\,\tilde U, \qquad
\Omega(a) \;\mapsto\; U\,\Omega(a)\,\tilde U - 2\,(a\cdot\nabla U)\,\tilde U
\end{equation}
for a rotor field $U$ (rotation gauge), together with the position-gauge displacements, which act by pullback \cite{LDG1998}; the curvature transforms covariantly under both, $\mathcal{R}(B) \mapsto U\,\mathcal{R}(\tilde U B U)\,\tilde U$ under the rotation gauge, so every scalar built from it is gauge-invariant. Every operation in these displays is interior to $\Cl(1,3)$: nothing invokes a curved manifold beyond the flat background.

## technical
pending

## lay
pending

## one-liner
pending
