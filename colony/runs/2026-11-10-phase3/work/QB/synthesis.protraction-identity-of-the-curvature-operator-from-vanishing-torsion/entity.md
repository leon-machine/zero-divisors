---
id: synthesis.protraction-identity-of-the-curvature-operator-from-vanishing-torsion
kind: claim
version: 1
title: 'Protraction identity of the curvature operator from vanishing torsion'
status: proved
region: synthesis
subject: einstein
tags: [curvature-and-field-equations, gauge-fields, classical-theorem, recovers-known-physics]
proposed_by:
  kind: ai
  session: 2026-11-10-phase3
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-10-phase3
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses: []
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_cyclic_trivector_determines_the_protraction_for_every_bivector_map
- kind: check
  ref: check.py::check_cyclic_trivector_is_the_covariant_curl_of_the_torsion
- kind: check
  ref: check.py::check_protraction_vanishes_on_torsion_free_fields
- kind: check
  ref: check.py::check_kernel_of_the_protraction_is_the_space_of_algebraic_curvature_maps
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.vacuum-polarisation-kernel-on-a-gravitational-field-has-the-flat-leading-part-and-no-weyl-term-of-degree-four
extraction:
  open_problem: op.qft-loops-and-renormalisation
  note: >-
    Answers the attack item of op.qft-loops-and-renormalisation that asks for the protraction identity of the
    curvature operator to be derived from vanishing torsion. The identity is the first Bianchi identity of a
    torsion-free field. It rests on the definition of the gravitational field alone (clauses (b), (c) and (f)); no
    stored result and no reading of the derived metric is used. Where the store uses the identity without deriving
    it: as a stated hypothesis of
    synthesis.vacuum-polarisation-kernel-on-a-gravitational-field-has-the-flat-leading-part-and-no-weyl-term-of-degree-four
    (clause (ii), the contraction of the transport rotor's derivative); as a condition imposed to define algebraic
    Weyl maps in the checks of correspondence.no-real-lorentzian-vacuum-half-flat,
    interior.filtration-cauchy-horizon-read-literature and
    synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared; and through the pair symmetry in
    pairing.loop-classes-are-weyl-components, which cites it as a property of the Riemann tensor read through the
    imported dictionary. Those entities are not changed here; repointing them is a maintainer decision.
    Classical, and transport-absent: this is the derivation of Lasenby, Doran and Gull, Gravity, gauge theories and
    geometric algebra (1998), Section 5, equations (5.1) to (5.6) of the arXiv text gr-qc/0405033 (checked on the
    web on 10 November 2026 through a text-extraction tool: D wedge D wedge of a multivector vanishes by their
    equation (4.40), then a protraction and a contraction), rewritten in the store's conventions (the store's hb is
    their underbarred map, the curvature operator has the opposite sign). What is added to that derivation:
    the form with torsion, clause (ii), and the explicit inversion of clause (i), which make the dependence on
    the torsion equation exact and give a control for the check; and the exact rank computations of clause (iv).
    Clause (iv) is computed in dimensions three, four and five; the general dimension count and the pair symmetry
    in every dimension are classical (the algebraic curvature tensors) and cited, not proved. Sign and convention
    tests: the check runs on the library's Schwarzschild and de Sitter fields with the stored values 2M/r^3 and
    scalar curvature 4 Lambda. Not addressed: the second (differential) Bianchi identity; fields with torsion
    beyond clause (ii); the degenerate region where hb is not invertible.
---

## formal
Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), in four dimensions or, by the definition's last clause, on the vectors of $\Cl(p,q)$ with $d = p + q \geq 3$, on its invertible region, with $\hb$ twice and $\Omega$ once continuously differentiable. Write $D_{\mu} = D_{e_{\mu}}$, $g_{\mu} = \hb^{-1}(e_{\mu})$, $g^{\mu} = \hb^{T}(e^{\mu})$, $D = g^{\mu}D_{\mu}$, and let $\partial_{a}$ denote the derivative with respect to a physical vector argument $a$. The \emph{torsion bivectors} are $\Theta^{\mu} = D\wedge g^{\mu} = g^{\lambda}\wedge D_{\lambda}g^{\mu}$; the torsion equation of clause (f) of the definition, $D\wedge\hb^{T}(a) = \hb^{T}(\nabla\wedge a)$ for all vector fields $a$, holds exactly when $\Theta^{\mu} = 0$ for every $\mu$. For a linear map $M$ from bivectors to bivectors and a vector $c$ put
\[
P_{M}(c) = \partial_{a}\wedge M(a\wedge c), \qquad C_{M}(c) = \partial_{b}\wedge\partial_{a}\wedge\bigl(M(a\wedge b)\cdot c\bigr), \qquad E_{M} = \partial_{c}\wedge P_{M}(c),
\]
the \emph{protraction} of $M$ (a trivector), its \emph{cyclic trivector}, and a four-vector.
\begin{enumerate}
\item[(i)] \emph{(Algebra; proved, for every $M$, every dimension and signature.)} $C_{M}(c) = 2P_{M}(c) - c\cdot E_{M}$ and $\partial_{c}\wedge C_{M}(c) = -2E_{M}$, hence
\[
P_{M}(c) = \tfrac12\,C_{M}(c) - \tfrac14\,c\cdot\bigl(\partial_{e}\wedge C_{M}(e)\bigr) .
\]
So $P_{M} = 0$ exactly when $C_{M} = 0$, and $C_{M} = 0$ exactly when $M(x\wedge y)\cdot z + M(y\wedge z)\cdot x + M(z\wedge x)\cdot y = 0$ for all vectors $x, y, z$.
\item[(ii)] \emph{(Every field; proved.)} For the curvature operator $\mathcal{R}(B) = -R(\hb(B))$ of the definition, clause (c),
\[
\tfrac12\,C_{\mathcal{R}}(g^{\mu}) = D\wedge\Theta^{\mu} - \Theta^{\nu}\wedge D_{\nu}g^{\mu} .
\]
\item[(iii)] \emph{(The protraction identity; proved.)} If the torsion vanishes, then for every physical vector $b$
\[
\partial_{a}\wedge\mathcal{R}(a\wedge b) = 0, \qquad\text{equivalently}\qquad \mathcal{R}(a\wedge b)\cdot c + \mathcal{R}(b\wedge c)\cdot a + \mathcal{R}(c\wedge a)\cdot b = 0 ,
\]
and therefore $\partial_{a}\,\mathcal{R}(a\wedge b) = \mathcal{R}(b)$: the geometric contraction of the curvature operator is the Ricci vector, with no trivector part.
\item[(iv)] \emph{(The kernel of the protraction; computed for $d = 3, 4, 5$.)} In signatures $(1,2)$, $(1,3)$, $(2,2)$ and $(1,4)$ the linear map $M \mapsto P_{M}$ has rank $3$, $16$, $16$, $50$ and its kernel has dimension $6$, $20$, $20$, $50$, that is $d^{2}(d^{2}-1)/12$; every map of the kernel is symmetric, $\langle A\,M(B)\rangle_{0} = \langle M(A)\,B\rangle_{0}$, and its Ricci map $M(b) = \partial_{a}\cdot M(a\wedge b)$ is then symmetric. So in these dimensions the curvature operator of a torsion-free field is symmetric. Symmetry does not give the identity: in $\Cl(1,3)$ the map $B \mapsto I B$, $I$ the pseudoscalar, is symmetric and has $P(c) = -3\,I c$. In every dimension the kernel is the space of algebraic curvature tensors and the pair symmetry is classical; that general statement is cited, not proved here.
\end{enumerate}
This is the first Bianchi identity of a torsion-free field in the form used by the store's Gauge Theory Gravity results. It is classical: the derivation follows Lasenby, Doran and Gull \cite[Section 5]{LDG1998} in the store's conventions.

## technical
The store's results on gravitational fields use the fact that, for a torsion-free field, wedging the curvature operator with the derivative of its own argument gives zero. Several results assumed this or imposed it as a condition; none derived it. The derivation needs only the definition of the gravitational field. The torsion of a field is the covariant curl of its coframe vectors $g^{\mu} = \hb^{T}(e^{\mu})$. Taking the covariant curl a second time and using that the commutator of two covariant derivatives is the field strength gives, for every field, an exact formula: the totally antisymmetrised curvature, a trivector for each vector, equals the covariant curl of the torsion minus a term linear in the torsion. A short piece of algebra, valid for every linear map of bivectors in every dimension, then inverts the relation between that trivector and the protraction $\partial_{a}\wedge\mathcal{R}(a\wedge b)$, using only that a four-vector is reproduced four times by contracting and wedging back. So when the torsion vanishes the protraction vanishes, the cyclic sum $\mathcal{R}(a\wedge b)\cdot c + \mathcal{R}(b\wedge c)\cdot a + \mathcal{R}(c\wedge a)\cdot b$ vanishes, and the full geometric contraction $\partial_{a}\mathcal{R}(a\wedge b)$ is the Ricci vector alone. With torsion the identity fails in general, by the formula of clause (ii). Exact rank computations in dimensions three, four and five show that the maps with vanishing protraction form a space of dimension $d^{2}(d^{2}-1)/12$ inside the symmetric maps, twenty in four dimensions, one fewer than the symmetric maps: the duality map $B \mapsto IB$ is symmetric and violates the identity. The result is the first Bianchi identity, derived as in Lasenby, Doran and Gull's paper in the store's sign and naming conventions; it is not new mathematics.

## lay
In this formulation gravity is carried by two fields on flat spacetime, and what is usually called curvature is the strength of one of them. For gravity without the twisting that spinning matter would source (vanishing torsion), the curvature obeys a symmetry rule known since the nineteenth century as the first Bianchi identity. Many results in the collection rely on this rule, but it had been taken for granted and not shown inside the collection. Here it is derived, assuming only vanishing torsion and the definition of the two fields: differentiating the no-twisting condition once more turns it into a statement about the curvature, and a few lines of algebra bring that statement to the form the other results use. The same computation shows exactly how the rule fails when twisting is present. Exact computer checks confirm each step on sample fields, including the fields of a black hole and of an expanding universe. This is known mathematics written in the collection's own language, not a new discovery.

## one-liner
Assuming vanishing torsion, the curvature operator of a gravitational field obeys $\partial_{a}\wedge\mathcal{R}(a\wedge b) = 0$, so $\partial_{a}\mathcal{R}(a\wedge b)$ is the Ricci vector; for every field $\tfrac12 C_{\mathcal{R}}(g^{\mu}) = D\wedge\Theta^{\mu} - \Theta^{\nu}\wedge D_{\nu}g^{\mu}$ with $\Theta^{\mu} = D\wedge g^{\mu}$ the torsion, and the protraction is recovered from the cyclic trivector $C$ by exact algebra (the first Bianchi identity, classical, derived from the definition as in Lasenby, Doran and Gull).
