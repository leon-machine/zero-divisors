---
id: synthesis.field-equation-linear-in-the-curvature-with-a-conserved-source-is-einsteins
kind: claim
version: 1
title: "A field equation linear in the curvature with a conserved source is Einstein's"
status: proved
region: synthesis
subject: einstein
tags: [curvature-and-field-equations, gauge-fields]
proposed_by:
  kind: ai
  session: 2026-11-26-null-plane
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction (the request to derive the imported field equation, the choice of this route, and the instruction to state everything in geometric algebra)
- name: Claude Fable 5.2
  role: proposal, proof and drafting
  source: session 2026-11-26-null-plane
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.null-plane-data-of-the-first-order-gravitational-field-are-the-shear-of-the-generators@1
  - synthesis.weyl-flat-variations-carry-only-the-stress-trace-and-the-whole-stress-clause-is-the-trace-free-channel@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_operators_with_the_cyclic_identity_are_twenty_and_symmetric
- kind: check
  ref: check.py::check_covariant_linear_maps_of_curvature_operators_are_ricci_and_scalar
- kind: check
  ref: check.py::check_bianchi_identities_on_a_field_that_is_not_weak
- kind: check
  ref: check.py::check_divergence_of_the_two_parameter_family
- kind: check
  ref: check.py::check_first_order_limit_is_the_stored_einstein_map
lineage:
  motivated_by:
  - synthesis.imported-einstein-cartan-matter-coupling
  - synthesis.imported-lovelock-and-anderson-duchamp-natural-lagrangians
  - synthesis.einstein-equations-from-c-loc-and-clausius
extraction:
  open_problem: op.einstein-from-the-field-theory
  note: >-
    Filed against op.einstein-from-the-field-theory as a route that states the whole-stress clause and derives
    the rest, on the maintainer's instruction of 26 November 2026 to derive the field equation that the store
    imports (synthesis.imported-einstein-cartan-matter-coupling, clause (a)). It is not a derivation from
    nothing, and none is claimed: two conditions are assumed and named in clause (vi), (Q) that the equation is
    one affine function of the curvature operator at every point, of nothing else, covariant under the rotation
    gauge, and (C) that its source is the matter's stress map, conserved, with a trace of nonvanishing gradient
    for some matter. The constant rests in addition on hypothesis (N) of the first-order result, the matching to
    the stored Newtonian coupling, read at Lambda = 0. The field equation in clause (f) of the stored definition
    is not used: only its clauses (i) to (e) and its torsion equation are. (C) is the
    whole-stress clause, which the open problem says a route must derive or state: it is stated. Everything else
    is proved in the entity from the stored definition of the gravitational field: the two identities of the
    curvature, their contraction, the count of covariant linear maps (an exact finite computation), and the
    selection of the Einstein map; the constant is taken from the first-order result stored with this one, which
    takes it from the stored Newtonian coupling. No imported Fact is a premise. The store holds Lovelock's
    theorem as an imported Fact (synthesis.imported-lovelock-and-anderson-duchamp-natural-lagrangians); it is
    stronger than clause (iv), since it does not assume that the expression is linear in the curvature, and it is
    not derived here: condition (Q) is exactly what it would remove. The equation obtained is clause (f) of the
    stored definition, with G restored, and the frame equation of the imported Einstein-Cartan Fact for matter
    without spin; the torsion equation is taken from the definition, so the connection equation of that Fact
    (its clause (b), the coupling of spin to torsion) is not covered. Decisions for the maintainer: (1) whether
    the stored results that cite the imported frame equation for matter without spin are to cite this result,
    with (Q) and (C) then among their conditions; (2) whether (Q) and (C) are to be registered as postulates or
    kept as hypotheses local to this result (they are kept local here, and no assumes edge is declared); (3)
    whether the open problem takes this result under its work in store, with an attack item for removing (Q),
    that is, for deriving Lovelock's theorem in the store. Prior art, not premises, cited from memory and not
    read for this entity: the argument from the contracted identity and conservation to the field equation (A.
    Einstein, 1915; in the form used here it is the standard textbook derivation); the two identities (L.
    Bianchi, 1902; G. Ricci); uniqueness without linearity (E. Cartan, 1922; H. Weyl, 1922; D. Lovelock, 1971);
    the gauge-theory form of the curvature and its identities (A. Lasenby, C. Doran and S. Gull, 1998). No
    novelty is claimed; what is new to the store is that the statement and its proof are held in the store's
    language with exact checks and without an import. Ledger: transport-absent.
---

## formal
Units $\hbar = c = 1$. Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) obeying the torsion equation of its clause (f), which fixes $\Omega$ from $\hb$; only its clauses (i) to (e) and that torsion equation are used, and the field equation of clause (f) is not assumed anywhere. Notation: the derivative $A \cdot D = D_{\hb(A)}$ along a physical vector, the curvature operator $\mathcal{R}$ on physical bivectors in the store's sign, its Ricci map $\mathcal{R}(b) = \partial_{a} \cdot \mathcal{R}(a \wedge b)$, scalar $\mathcal{R} = \partial_{a} \cdot \mathcal{R}(a)$ and Einstein map $\mathcal{G}(a) = \mathcal{R}(a) - \tfrac12 a\,\mathcal{R}$. For a field $M$ of linear maps of physical vectors or bivectors put $(A \cdot D\,M)(X) = A \cdot D\bigl(M(X)\bigr) - M(A \cdot D\,X)$, again a field of linear maps, and for a field of maps of vectors $(\operatorname{div} M)(C) = \partial_{A} \cdot \bigl((A \cdot D\,M)(C)\bigr)$, its divergence.
\begin{enumerate}
\item[(i)] \emph{(The two identities of the curvature; proved from the Definition.)} For physical vectors $A, B, C$:
\[
\mathcal{R}(A \wedge B) \cdot C + \mathcal{R}(B \wedge C) \cdot A + \mathcal{R}(C \wedge A) \cdot B = 0, \qquad (A \cdot D\,\mathcal{R})(B \wedge C) + (B \cdot D\,\mathcal{R})(C \wedge A) + (C \cdot D\,\mathcal{R})(A \wedge B) = 0 .
\]
\item[(ii)] \emph{(The curvature operators; proved.)} The linear maps of the bivectors that satisfy the first identity of (i) form a space $\mathcal{K}$ of dimension twenty, carried into itself by the rotors, $\mathcal{R} \mapsto R\,\mathcal{R}(\tilde R\,\cdot\,R)\,\tilde R$. Each of them is symmetric, $B_{1} \cdot \mathcal{R}(B_{2}) = B_{2} \cdot \mathcal{R}(B_{1})$, and has a symmetric Ricci map. Every element of $\mathcal{K}$ is the curvature operator at a point of some gravitational field.
\item[(iii)] \emph{(The contracted identity; proved.)} $\operatorname{div}\mathcal{R}(C) = \tfrac12\,C \cdot D\,\mathcal{R}$, the Ricci map on the left and the scalar on the right; so $\operatorname{div}\mathcal{G} = 0$ for every gravitational field obeying the torsion equation.
\item[(iv)] \emph{(The covariant linear expressions; proved.)} The linear maps $\Phi$ from $\mathcal{K}$ to the linear maps of the vectors that commute with the rotors, $\Phi\bigl(R\,\mathcal{R}(\tilde R\,\cdot\,R)\,\tilde R\bigr) = R\,\Phi(\mathcal{R})(\tilde R\,\cdot\,R)\,\tilde R$, form a space of dimension two, spanned by the Ricci map and the identity times the scalar. The linear maps of the vectors that commute with every rotor are the multiples of the identity. So an expression $F$ with values in the linear maps of the physical vectors that is one and the same affine function of the curvature operator at every point, depending on no other quantity (not on the position, nor on $\hb$ or $\Omega$ otherwise than through $\mathcal{R}$), and covariant under the rotation gauge, is
\[
F(a) = \alpha\,\mathcal{R}(a) + \beta\,a\,\mathcal{R} + \lambda\,a
\]
with three constants.
\item[(v)] \emph{(Its divergence and trace; proved.)} $\operatorname{div}F(C) = (\tfrac12\alpha + \beta)\,C \cdot D\,\mathcal{R}$ and $\partial_{a} \cdot F(a) = (\alpha + 4\beta)\,\mathcal{R} + 4\lambda$. The divergence vanishes for every field exactly when $\beta = -\tfrac12\alpha$, that is, when $F = \alpha\,\mathcal{G} + \lambda\,\id$.
\item[(vi)] \emph{(The field equation; proved, given (Q) and (C).)} Assume: (Q) the field equation of gravity is $F(a) = -\kappa\,T(a)$ with $F$ as in (iv), the same affine function of the curvature operator at every point and of nothing else, $T$ the stress map of the matter and $\kappa \neq 0$ a constant; (C) the stress map of every matter has zero divergence, $\operatorname{div}T = 0$, and the equation admits matter whose stress has a trace with a gradient that does not vanish identically. Then $\alpha \neq 0$, $\beta = -\tfrac12\alpha$, and the equation is
\[
\mathcal{G}(a) + \Lambda\,a = -\frac{\kappa}{\alpha}\,T(a), \qquad \Lambda = \lambda/\alpha .
\]
\item[(vii)] \emph{(The constant; proved, given (vi), the first-order result and its hypothesis (N).)} About the flat field the Einstein map is at first order the stored first-order Einstein map $\mathcal{E}[h]$ (Theorem \claimref{synthesis.null-plane-data-of-the-first-order-gravitational-field-are-the-shear-of-the-generators}(iv)), so at $\lambda = 0$, where the flat field is the solution without matter, the equation of (vi) is $\mathcal{E}[h] = -(\kappa/\alpha)\,T$ at first order; it satisfies the conditions (L), (D), (V) of clause (v) of that theorem, and by its clause (vi), under its hypothesis (N) that the interaction of two bodies at rest is the stored Newtonian coupling, $\kappa/\alpha = 8\pi G$. The ratio is identified at $\lambda = 0$; $\kappa/\alpha$ and $\Lambda$ are independent constants of the equation, and the same value is taken when $\Lambda \neq 0$, where it is Newton's constant in the regime in which $\Lambda$ times the square of the distances is negligible. Hence
\[
\mathcal{G}(a) + \Lambda\,a = -8\pi G\,T(a) ,
\]
with $\Lambda$ a constant that these conditions do not fix: clause (f) of the Definition, with $G$ restored.
\end{enumerate}
\emph{Reading (argued).} \emph{What is derived and what is assumed.} Given a gravitational field in the sense of the Definition, with the torsion equation, the two identities of its curvature, their contraction and the list of covariant linear expressions are theorems of the store. What selects the Einstein map among the expressions of (iv) is that its divergence vanishes identically, so that the equation can hold with a conserved source; what fixes its constant is the matching to Newton's law, hypothesis (N) of the first-order result. Beyond that matching two things are assumed. (Q) says that the equation is of second order in $\hb$ and linear in the second derivatives in the strongest sense, linear in the curvature operator, with coefficients that are constants; an expression of second order that is not linear in the curvature is excluded by assumption, not by proof, and the theorem that would exclude it in four dimensions is the imported Fact \claimref{synthesis.imported-lovelock-and-anderson-duchamp-natural-lagrangians}. (C) is the whole-stress clause: the source of the gravitational field is the whole stress map of the matter and nothing else, and that map is conserved. Neither is derived from the series' structure here. \emph{The other routes.} Theorem \claimref{synthesis.einstein-equations-from-c-loc-and-clausius} reaches the same equation, also with $\Lambda$ undetermined, from the local-horizon premise in place of (Q); the two routes share the clause that the whole stress is the source. This route uses no horizon, no temperature and no entropy. \emph{Limits.} Matter without spin, the torsion equation being taken from the Definition. $\Lambda$ is not fixed. Nothing here says why the equation of gravity should be local, of second order, or linear in the curvature; the result says that once it is, with a conserved source, nothing is left to choose but Newton's constant and $\Lambda$.

## technical
The store imports the field equation of gravity. This result derives it from the stored definition of the gravitational field under two named conditions, in geometric algebra throughout.

From the definition, with the torsion equation: commuting covariant derivatives gives the curvature, and the Jacobi identity for those commutators gives the two identities of the curvature, the algebraic one (a cyclic sum of $\mathcal{R}(A \wedge B) \cdot C$ vanishes) and the differential one (a cyclic sum of covariant derivatives of $\mathcal{R}$ vanishes). Contracting the second twice gives the divergence of the Ricci map as half the gradient of the scalar, so the Einstein map has no divergence.

The linear maps of the bivectors obeying the algebraic identity form a space of dimension twenty, every element of which is symmetric and occurs as the curvature of some field at a point. An exact computation counts the linear maps from that space to the linear maps of vectors that commute with the rotors: there are two, the Ricci map and the identity times the scalar. So any expression that is linear in the curvature operator and covariant is a combination of those two and of the identity.

If the field equation is such an expression set equal to a multiple of the matter's stress map, and the stress map is conserved with a trace whose gradient does not vanish identically, the combination must have no divergence, and it is the Einstein map plus a multiple of the identity. Its first order is the stored first-order equation, whose constant is fixed by matching the stored Newtonian coupling. The result is $\mathcal{G}(a) + \Lambda a = -8\pi G\,T(a)$ with $\Lambda$ free.

Assumed, not derived: that the equation is linear in the curvature operator with constant coefficients, that its source is the whole conserved stress map, and that its static weak limit is Newton's law. The field equation of the stored definition is not used. The second is the whole-stress clause of the open problem on Einstein's equations. The first is what Lovelock's theorem, imported in the store, would remove. Matter with spin is not covered.

Ledger: transport-absent. This is the standard derivation of the field equation from the contracted identity, stated in the series' variables with exact checks and no import.

## lay
Einstein's equation says how matter bends spacetime. Until now the series took that equation from the literature. This result rebuilds it from the series' own description of gravity, given two assumptions that are stated openly.

The description of gravity in the series already contains a quantity, the curvature, that measures how much gravity there is at each point. Two facts about the curvature follow from the description itself, and they are proved here. One of them has a consequence that matters: there is exactly one way of combining the pieces of the curvature whose total flow in and out of every small region balances exactly.

Matter has the same property. Energy and momentum are conserved: what flows into a region flows out or stays. So if gravity's equation is to say "some combination of the curvature equals the energy and momentum of matter", the combination must be the one that balances. A computer count, done with exact arithmetic, shows that the simple combinations are very few, and that only one balances. That one is Einstein's.

Newton's law of attraction then fixes the strength of the coupling. One number is left free, the cosmological constant.

The two assumptions are these. First, that gravity's equation uses the curvature in the simplest possible way, without squaring it or differentiating it further. Second, that the source of gravity is all of the energy and momentum of matter and nothing else. Neither is proved here. With them, there is no freedom left.

## one-liner
From the stored definition of the gravitational field with the torsion equation: the curvature operator obeys the cyclic identity and its differential companion, the operators obeying the first form a space of dimension twenty, the linear maps from it to maps of vectors that commute with the rotors are exactly the Ricci map and $\id$ times the scalar (an exact count), and the contracted identity gives $\operatorname{div}\mathcal{G} = 0$; so, given (Q) a field equation affine in the curvature operator and (C) a conserved stress map as its whole source, the equation is $\mathcal{G}(a) + \Lambda a = -8\pi G\,T(a)$, with the constant from matching the stored Newtonian coupling and $\Lambda$ free, and no imported Fact as a premise.
