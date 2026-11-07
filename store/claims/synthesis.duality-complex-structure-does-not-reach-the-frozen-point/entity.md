---
id: synthesis.duality-complex-structure-does-not-reach-the-frozen-point
kind: claim
version: 2
title: 'The duality complex structure does not reach the frozen point'
status: proved
region: synthesis
subject: einstein
tags: [chirality, tractors, frozen-point, gauge-fields, forcing-and-uniqueness]
proposed_by:
  kind: ai
  session: 2026-11-01-field-space
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - correspondence.lorentzian-duality-complex-structure@4
  - synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared@2
  - synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection@1
  - dark-energy.frozen-point-makes-stelle-west-vector@5
  - synthesis.imported-conformal-gravity-bach-equations-and-conformal-gauge-form@1
  - synthesis.frozen-point-reduces-the-connection-only-when-infinitely-stiff@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_duality_is_the_lorentz_commutant
- kind: check
  ref: check.py::check_frozen_point_pairing_is_the_duality_pairing
- kind: check
  ref: check.py::check_chiral_slot_hessian
- kind: check
  ref: check.py::check_schouten_slot_is_stationary_for_every_chirality
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - correspondence.lorentzian-duality-complex-structure
  - synthesis.curvature-only-tractor-actions-are-macdowell-mansouri
  - synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared
extraction:
  open_problem: op.derive-gravitational-action
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 1 -> 2: the citation of the infinite-stiffness result for the case tau = 0 is now a claimref and a uses edge (that result does not depend on this one), with an untouched_premises record in coverage.yaml; the Reading names the field-space premise synthesis.field-space-premise-parallel-frozen-point by claimref (text only). Statement unchanged.'
  note: >-
    Outside idea tested: self-dual field spaces (Plebanski 1977, Ashtekar 1986, Jacobson and Smolin; cited from
    memory), where a self-dual projection of the connection, with simplicity constraints, picks the field
    space. The series has the needed structure: the stored Hodge star on spacetime bivectors is multiplication
    by the spacetime pseudoscalar and squares to -1. Question: can it act on the field space of the frozen-point
    functional, the stabiliser of I, or select it? Results: the commutant of the adjoint action is spanned by 1
    and J on so(1,3), and is the scalars on stab(I) (de Sitter, anti-de Sitter and Poincare types, rho = 3/7,
    -2/5, 0), on the parabolic algebra of the line of X and on so(2,4): no complex structure exists on any of
    them (standard: only the Lorentz algebra is complex), so the duality acts only on the Lorentz algebra, which
    the normal tractor and the I-reduced field spaces share, and distinguishes neither. On the Lorentz block the
    frozen-point pairing is eps_X = -K( . , J . ); the chiral (self-dual) pairings are eps_X + tau K at
    tau = +-j. With the special-conformal slot varied (unreduced field, no field equation presupposed), the
    Killing pairing does not see the symmetric slot, the antisymmetric block has determinant
    -4096 (1 + tau^2)^3, and on torsion-free fields both gradients vanish at the Schouten map: every chirality,
    the self-dual one included, returns the normal tractor slot (conformal gravity plus a Pontryagin-type
    term), at the chiral values up to a free antisymmetric slot that leaves the equations unchanged. The tau = 0 case is \claimref{synthesis.frozen-point-reduces-the-connection-only-when-infinitely-stiff}(iii); only the chiral extension is claimed. Plebanski and Ashtekar take an independent Lorentz connection
    and frame as input, the first-order field space, adopted not derived. Negative: the duality complex
    structure does not supply the reduction by the frozen point. Transport-absent (the series' objects serve
    only as notation for standard facts).
---

## formal
Work in $\Cl(2,4)$ in the chart of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection} with $X = \nO$ and $I = \nInf + \rho\nO$ (Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector} for $\rho = \Lambda/6 \neq 0$). Let $i_{4} = e_{0}e_{1}e_{2}e_{3}$ and $J(B) = i_{4}B$ on spacetime bivectors, the Hodge star of Lemma \claimref{correspondence.lorentzian-duality-complex-structure}. For a Lie algebra $\mathfrak{g}$ of bivectors (commutator product) its commutant is the set of linear maps $T$ of $\mathfrak{g}$ with $T[x, y] = [x, Ty]$ for all $x, y$; a complex structure on $\mathfrak{g}$ making it a complex Lie algebra lies in it.
\begin{enumerate}
\item[(i)] \emph{(Duality is the Lorentz commutant; proved, standard.)} The commutant of $\so(1,3)$ is spanned by $\id$ and $J$, with $J^{2} = -\id$. The commutant of the stabiliser of $I$ (ten-dimensional) is $\mathbb{R}\,\id$ for every $\rho$, of de Sitter, anti-de Sitter and Poincar\'e type, and so are those of the parabolic algebra stabilising the line of $X$ (eleven-dimensional, the algebra that gauges the tractor field) and of $\so(2,4)$. Hence none of these carries a complex structure commuting with its bracket, and $J$ preserves neither the stabiliser of $I$ nor the parabolic algebra. This is the standard fact that $\so(1,3) \cong \mathfrak{sl}(2, \mathbb{C})$ is a complex Lie algebra and the others are not.
\item[(ii)] \emph{(The frozen-point pairing is the duality pairing; proved.)} On spacetime bivectors $\epsilon_{X}(B, B') := \epsilon(I, X, B, B') = -\langle B\,i_{4}\,B'\rangle_{0} = -K(B, JB')$ with $K(B, B') = \langle BB'\rangle_{0}$, for every $\rho$. With a formal unit $j$, $j^{2} = -1$, the pairings $\epsilon_{X} + \tau K$ at $\tau = \pm j$ are $\pm j K(B, (1 \pm jJ)B')$, the self-dual and anti-self-dual pairings.
\item[(iii)] \emph{(Slot Hessian of the chiral family; proved.)} Vary the special-conformal slot $S$ of the unreduced field $\Omega - \nInf \wedge \hb^{-1} + \nO \wedge S$ (frame components, $\hb = 1$ at a point), whose spacetime block is $-\mathcal{R} + T_{S}$. The Hessian of $K(T_{S} \wedge T_{S})$ vanishes on the symmetric slot (lowered indices), the symmetric and antisymmetric slots decouple for both pairings, the Hessian of $\epsilon_{X}$ has rank sixteen, and on the antisymmetric slot $\det(H_{\epsilon} + \tau H_{K}) = -4096\,(1 + \tau^{2})^{3}$. So the slot Hessian of $\epsilon_{X} + \tau K$ is nondegenerate for every real $\tau$ and degenerate exactly at the chiral values $\tau = \pm j$, with a complex kernel of dimension three in the antisymmetric slot.
\item[(iv)] \emph{(Every chirality returns the Schouten slot; proved, standard in content.)} At $\tau = 0$ the Schouten slot is the unique stationary slot of $\epsilon_{X}$ (Theorem \claimref{synthesis.frozen-point-reduces-the-connection-only-when-infinitely-stiff}(iii)); the extension claimed here is to the chiral family. For torsion-free $\Omega$ the slot gradient of $K(F \wedge F)$ also vanishes at the Schouten slot $S = \Sch$. Hence $\Sch$ is a stationary slot of $\epsilon_{X} + \tau K$ for every $\tau$: the only one for real $\tau$, and at $\tau = \pm j$ the only one up to a free antisymmetric slot in the kernel of (iii), which leaves the density and its equations unchanged (the connection, not the equations, is undetermined there). At $\Sch$ the spacetime block is $-\mathcal{W}$ and the density is $\tfrac14 W_{abcd}W^{abcd} + \tau K(\mathcal{W} \wedge \mathcal{W})$, the Weyl square plus $\tau$ times the Pontryagin-type density of the Weyl curvature, the standard statement that the chiral Weyl square is the Weyl square plus a Pontryagin term. With torsion the $K$ gradient at the corresponding Schouten slot does not vanish.
\end{enumerate}
\emph{Reading.} Self-dual (Ashtekar, Plebanski) field spaces are built from a self-dual projection of a Lorentz connection, with an independent Lorentz connection and frame (or two-forms reducing to one) as input: they take the first-order field space as given rather than derive it, and their simplicity and reality conditions are not analysed here. In the series the projection is the stored Hodge star, and by (i) it acts only on the Lorentz algebra, which is present in the normal tractor setting and in the reduced one alike, so it distinguishes neither the parabolic (normal tractor) field space nor the connections preserving $I$. Applied to the frozen-point integrand with the slot varied, every chirality returns the normal tractor slot, (iv): the duality complex structure does not supply the reduction by the frozen point, which the store records as Premise \claimref{synthesis.field-space-premise-parallel-frozen-point}. The result is transport-absent: the series' objects enter only as notation for standard Lie-theoretic and curvature facts.

## technical
Self-dual formulations of gravity (Ashtekar's variables, Plebanski's action) pick their field space by projecting a Lorentz connection onto its self-dual half. The series has the needed complex structure: the Hodge star on spacetime bivectors is multiplication by the spacetime pseudoscalar $i_{4}$, with square $-1$. Could it act on the larger algebras where the frozen point lives, or select the connections that preserve $I$?

It cannot. The maps commuting with the bracket of $\so(1,3)$ are spanned by the identity and $J$; for the ten-dimensional stabiliser of the frozen point (de Sitter, anti-de Sitter or Poincar\'e type), for the eleven-dimensional parabolic algebra that gauges the tractor field and for $\so(2,4)$ they are only the multiples of the identity, so no complex structure exists there (standard: only the Lorentz algebra is complex). The duality therefore lives on the Lorentz algebra, common to the normal and the reduced field spaces, and distinguishes neither. On the Lorentz block the frozen-point pairing is $\epsilon_{X} = -K(\cdot, J\,\cdot)$, so its self-dual version is the pairing $\epsilon_{X} + \tau K$ at $\tau = \pm j$. With the special-conformal slot varied, the Killing part is blind to the symmetric slot, the antisymmetric slot has determinant $-4096(1 + \tau^{2})^{3}$, and on torsion-free fields the Schouten map is stationary for every $\tau$. So the self-dual integrand gives conformal gravity plus a Pontryagin-type term, as the real one does; at the chiral values three complex antisymmetric slot components are left free without changing the equations. Plebanski's and Ashtekar's formulations take an independent Lorentz connection and frame as input, the first-order field space, so they adopt it rather than derive it. Transport-absent: standard facts in the series' notation.

## lay
A popular reformulation of gravity splits the field into two mirror-image halves using an operation that, applied twice, gives minus one, like multiplying by the imaginary unit. The series has exactly that operation. This result asks whether it could explain which version of the gravitational field the series' action should be applied to. It finds that the operation only makes sense for ordinary spacetime rotations, which every candidate version contains, not for the larger symmetries that tell the versions apart, and that using the mirror-image half of the action changes nothing about the choice: the action still prefers the series' own transport, which gives a different theory (conformal gravity) rather than Einstein's.

## one-liner
The commutant of the bracket is $\langle\id, J\rangle$ on $\so(1,3)$ ($J$ the stored Hodge star, multiplication by $i_{4}$) but only $\mathbb{R}\,\id$ on the stabiliser of the frozen point (all three types), on the parabolic algebra and on $\so(2,4)$ (standard), so the duality acts only on the Lorentz algebra and distinguishes neither the parabolic (normal tractor) nor the $I$-reduced field space; on the Lorentz block $\epsilon_{X} = -K(\cdot, J\cdot)$, and with the special-conformal slot varied the family $\epsilon_{X} + \tau K$ has antisymmetric slot determinant $-4096(1+\tau^{2})^{3}$ and, on torsion-free fields, the Schouten slot as stationary point for every $\tau$, self-dual included (at the chiral values up to a free antisymmetric slot that leaves the equations unchanged; $\tau = 0$ is Theorem \claimref{synthesis.frozen-point-reduces-the-connection-only-when-infinitely-stiff}(iii)): the duality complex structure does not supply the reduction by the frozen point; Plebanski and Ashtekar take the first-order field space as input; transport-absent.
