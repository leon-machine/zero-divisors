---
id: synthesis.canonical-part-of-a-spinor-on-a-null-plane
kind: claim
version: 1
title: 'Canonical part of a spinor on a null plane'
status: proved
region: synthesis
subject: quantum-fields
tags: [null-directions, spinor-modules, idempotents]
proposed_by:
  kind: ai
  session: maintainer-2026-11-07
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: split out of synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays and synthesis.slot-module-light-ray-arrays-are-weyl-components so that their users rest only on the algebra
  source: maintainer pass 2026-11-07
review: draft
derivations:
- name: main
  uses:
  - field-theory.second-quantisation@6
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_projectors_are_complementary_dirac_self_adjoint_idempotents
- kind: check
  ref: check.py::check_flux_through_the_plane_is_twice_the_norm_of_the_canonical_part
- kind: check
  ref: check.py::check_canonical_part_is_two_complex_channels
- kind: check
  ref: check.py::check_mass_terms_enter_only_the_constraint
- kind: check
  ref: check.py::check_covariant_maps_are_right_multiplications
- kind: proof
  derivation: main
extraction:
  note: >-
    The algebraic content of two results, collected so that results which need only the algebra do
    not inherit the premises of the rest: clause (i) of
    synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays (the projectors and the flux
    identity, with the dimension count of its clause (iii) for the two complex channels) and clause (i)
    of synthesis.slot-module-light-ray-arrays-are-weyl-components (mass terms reach only the
    constraint). Pure algebra in Cl(1,3) on top of the field theory's projector and Dirac mass term; no
    thermal, counting or matter premise. Transport-absent. Literature cited from memory, as
    orientation only: the good component of light-front quantisation and the mass independence of the
    null-plane data (Kogut and Soper 1970).
  maintainer_pass_clause_split:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Referee fixes of 7 November 2026, folded into version 1: (iv) and its technical and one-liner forms now say that the constraint fixes Lambda(k) psi only up to its value at one end of each generator, so the free data are Lambda(m) psi with that one boundary value per generator (the light-front zero mode, an omission inherited from the source); and that with an internal index a covariant mass term is a matrix of right multiplications. Created at Leon''s decision of 7 November 2026 to split the algebraic clauses out of the light-ray and slot-module results, so that synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes, which cites them only for these clauses, no longer inherits Premise (Q), the slot-module hypothesis or the dark-matter counting premises through them. Clauses (i) to (iii) here are clause (i) of the light-ray result split in three (the projectors, the flux, the two complex channels), and clause (iv) is clause (i) of the slot-module result, with a computed form of its step that Lorentz-covariant mass terms act from the right. Proofs moved from those results; the checks are copied from their check functions, with the two-channel and right-multiplier computations added.'
---

## formal
Work in the spacetime algebra $\Cl(1,3)$, $\gamma_{0}^{2} = 1$, $\gamma_{i}^{2} = -1$, with $I_{4} = \gamma_{0}\gamma_{1}\gamma_{2}\gamma_{3}$ and $\sigma_{3} = \gamma_{3}\gamma_{0}$. Let $k = \gamma_{0} + \gamma_{3}$ and $m = \gamma_{0} - \gamma_{3}$, so $Q(k) = Q(m) = 0$ and $\ip{k}{m} = 2$; let $N_{k} = \{x : \ip{x}{k} = 0\}$ be the null plane whose generators run along $k$ (any future null direction is carried to this one by a rotor, and $m$ is then the second null direction of the plane of $k$ and $\gamma_{0}$); let $B = \gamma_{3}\gamma_{0}$ ($B^{2} = 1$) and $\Lambda(a) = a\gamma_{0}/(2a_{0})$ (Theorem \claimref{field-theory.second-quantisation}(1)). Spinors are even multivectors $\psi \in \Cl^{+}(1,3)$ (real dimension $8$), on which a rotor $R$ acts by $\psi \mapsto R\psi$; $L_{X}\psi = X\psi$, and $J_{\psi} = \psi\gamma_{0}\tilde{\psi}$ is the Dirac current. Then:
\begin{enumerate}
\item[(i)] \emph{(The projectors.)} $\Lambda(k) = \tfrac12 k\gamma_{0} = \tfrac12(1 + B) = \tfrac14 km$ and $\Lambda(m) = \tfrac12 m\gamma_{0} = \tfrac12(1 - B) = \tfrac14 mk$ are complementary idempotents, $\Lambda(k) + \Lambda(m) = 1$, $\Lambda(k)\Lambda(m) = \Lambda(m)\Lambda(k) = 0$, each self-adjoint for the Dirac adjoint ($\gamma_{0}\tilde{\Lambda}\gamma_{0} = \Lambda$). On $\Cl^{+}(1,3)$, $L_{\Lambda(m)}$ projects onto $\ker L_{m}$, the $(-1)$-eigenspace of $L_{B}$, and $L_{\Lambda(k)}$ onto $\ker L_{k}$, the $(+1)$-eigenspace; each has real dimension $4$.
\item[(ii)] \emph{(The flux.)} $J_{\psi}\cdot k = 2\,|\Lambda(m)\psi|^{2}$ and $J_{\psi}\cdot m = 2\,|\Lambda(k)\psi|^{2}$, the squared Euclidean norm in the blade basis $1$, $\gamma_{\mu}\gamma_{\nu}$ ($\mu < \nu$), $I_{4}$. So the flux of the current through $N_{k}$ vanishes identically on the image of $\Lambda(k)$ and is positive definite on the image of $\Lambda(m)$: the part of a spinor field that carries its current through $N_{k}$, its canonical part on $N_{k}$, is $\Lambda(m)\psi$. The image of $\Lambda(k)$ is the spinor of plane waves of momentum $k$ (Theorem \claimref{field-theory.second-quantisation}(1)); its canonical data live on $N_{m}$.
\item[(iii)] \emph{(Two complex channels.)} $L_{I_{4}}$ and Hestenes' unit $R_{I_{4}\sigma_{3}}$, $\psi \mapsto \psi I_{4}\sigma_{3}$, each square to $-1$ and commute with $L_{B}$, so the image $V_{\Lambda}$ of $\Lambda(m)$ (and likewise that of $\Lambda(k)$) is invariant under both and is a complex vector space of dimension $2$ under either unit: the canonical part is two complex channels.
\item[(iv)] \emph{(Mass terms reach only the constraint.)} Every vector splits as $a = \tfrac12 m\,\ip{k}{a} + \tfrac12 k\,\ip{m}{a} + a_{\perp}$ with $a_{\perp}$ orthogonal to $k$ and $m$, so $k\nabla = 2\Lambda(k)(k\cdot\nabla) + k\nabla_{\perp}$ contains no derivative off $N_{k}$; $k$ anticommutes with $\gamma_{1}$ and $\gamma_{2}$ and $k\Lambda(k) = 0$, so $k\psi X = k\Lambda(m)\psi X$ for every multivector $X$ acting from the right, and $L_{k}$ is injective on the image of $\Lambda(m)$. The linear maps $\Cl^{+}(1,3) \to \Cl(1,3)$ that commute with left multiplication by every even element are exactly the right multiplications, so every Lorentz-covariant mass term, of Dirac or of Majorana type, acts from the right (with an internal index, a matrix of right multiplications), and on $N_{k}$ it enters only the equation that fixes $\Lambda(k)\psi$ along each generator from $\Lambda(m)\psi$ (up to its value at one end of each generator): the free data on $N_{k}$ are $\Lambda(m)\psi$, together with that one boundary value of $\Lambda(k)\psi$ per generator, for every mass matrix.
\end{enumerate}
These are identities in $\Cl(1,3)$; they use no thermal, counting or matter premise.

## technical
On a null plane, with generators along $k$ and second null direction $m$, the flux of a spinor's Dirac current through the plane is twice the squared norm of $\Lambda(m)\psi$, where $\Lambda(m) = m\gamma_{0}/2 = mk/4$ is one of the two complementary idempotents of the plane of $k$ and $m$. That half of the spinor, of real dimension four, is its canonical part on the plane; the other half, the spinor of plane waves moving along $k$, carries no flux through it. Both the field theory's unit $I_{4}$ and Hestenes' unit preserve the canonical part, which is therefore two complex channels under either. Multiplying a spinor field equation by $k$ on the left removes every derivative off the plane, and since Lorentz-covariant mass terms are right multiplications in the spacetime algebra, the mass enters only the equation that fixes the other half from the canonical part, up to one boundary value per generator: the free data on the plane are the canonical part, with that boundary value, whatever the masses. All of this is algebra; it is the common ground of the light-ray count of arrays, the slot module's Weyl-component count and the restriction of Hadamard states to null planes, none of whose further premises it needs.

## lay
A spin-one-half field, such as the electron's, has eight real components at each point. On a surface swept out by light rays, only four of them carry the field across the surface; the other four describe waves running along the light rays themselves and carry nothing through it. The four that count form two complex channels, and the particle's mass does not change which four they are: the mass only ties the other four to them. This result proves these facts by direct algebra, so that later results can use them without taking on any further assumptions.

## one-liner
In $\Cl(1,3)$, on a null plane with generators along $k$ and second null direction $m$, $\Lambda(m) = m\gamma_{0}/2 = mk/4$ is a Dirac-self-adjoint idempotent with $J_{\psi}\cdot k = 2|\Lambda(m)\psi|^{2}$, so the canonical part of a spinor there is $\Lambda(m)\psi$, real dimension $4$, two complex channels under $I_{4}$ or Hestenes' unit, and since Lorentz-covariant mass terms act from the right it is, with one boundary value of the other half per generator, the free data on the plane for every mass.
