---
id: synthesis.curvature-only-tractor-actions-are-macdowell-mansouri
kind: claim
version: 3
title: 'Curvature-only tractor actions: MacDowell-Mansouri is unique under parity'
status: proved
region: synthesis
subject: einstein
tags: [tractors, gauge-fields, curvature-and-field-equations, forcing-and-uniqueness]
proposed_by:
  kind: ai
  session: 2026-10-31-gravity-action
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
  - dark-energy.frozen-point-makes-stelle-west-vector@7
  - synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection@1
  - dark-energy.imported-macdowell-mansouri-theorem-stelle-west@4
  - synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part@4
  - synthesis.imported-einstein-cartan-matter-coupling@1
  - synthesis.imported-chern-weil-and-chern-simons-forms@1
  - synthesis.imported-lovelock-cartan-four-forms-and-holst-term@1
  - synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_pure_transport_admits_only_the_chern_weil_density
- kind: check
  ref: check.py::check_frozen_point_alone_admits_only_the_chern_weil_density
- kind: check
  ref: check.py::check_frozen_point_and_canonical_tractor_give_three_and_one_odd
- kind: check
  ref: check.py::check_frame_equations_of_the_two_non_topological_densities
- kind: check
  ref: check.py::check_which_hypotheses_do_the_work
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part
  - synthesis.series-wald-entropy-changes-without-flux-on-local-horizons
  - synthesis.positive-structure-and-natural-scale-actions-do-not-select-the-almost-einstein-scale
extraction:
  maintainer_pass_pin_review_2:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review (second-round close-out): synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared 3 -> 4 repinned; its change is the two-form and four-form definitions written in GA, the forms kept as readings and proved equal (notation).'
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review (second round): synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part repinned 3 -> 4 after reviewing its restatement (formal setting restated (A(a) = Omega(a) - (Lambda/3) hb^-1(a) ^ V, l^2 = 3/|Lambda| dropped)); clauses (i) to (iv), the store sign and the frame equation, cited here, are unchanged, and the use here holds as cited.'
  open_problem: op.derive-gravitational-action
  maintainer_pass_2026_11_01:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2 -> 3, at Leon''s decision of 2026-11-01: clause (vi) is reworded so that the no-inverse-frame hypothesis (P) forces the reduction for slots that are functions of (hb, Omega), that is under the premise (T) that the tractor gauge field is assembled from (hb, Omega) and no further field, since an independent special-conformal slot also satisfies (P); the slot step is cited (text only, to keep the graph acyclic) as proved in clause (i) of synthesis.inverse-frame-free-tractor-gauge-field-preserves-a-frozen-point, and the invariant form of the field space as the new premise synthesis.field-space-premise-parallel-frozen-point. The note and technical level say the same. Clauses (i) to (v) are unchanged.'
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Version 1 -> 2: the literature cited from memory now points to the imported Facts approved by Leon (Chern-Weil and Chern-Simons forms, for the topological clauses; Mardones-Zanelli and Holst, for the vacuum inertness of the Holst term and the Barbero-Immirzi readings), and the Weyl-square result is now a premise (uses), since clause (i) states its value on the normal tractor connection. Statement unchanged.'
  note: >-
    Shrinks import (b) of the open problem (that the action has the MacDowell-Mansouri form) to stated
    hypotheses on a local action of the Cl(2,4) gauge field: no inverse frame, curvature-only (derivatives
    enter only through the field strength; the frozen point and the canonical tractor enter algebraically),
    reduction of the connection by the frozen point (forced on the tractor gauge field by the no-inverse-frame
    hypothesis for slots that are functions of (hb, Omega), clause (vi)), and invariance under the combined spacetime and internal parity (equivalently,
    the density is odd under the internal reflection with the spacetime orientation fixed). In this reading
    what carries Einstein's equations is the field space (connections preserving I), not the integrand.
    Import (a) (that there is a local action) and import (c) (the matter coupling) are untouched, and the
    normalisation (Newton's constant) stays free. The classification is finite linear algebra over the
    rationals; it is comparable with the Lovelock-Cartan classification (Mardones and Zanelli 1991,
    \claimref{synthesis.imported-lovelock-cartan-four-forms-and-holst-term}(a); their list also has torsion-squared and exact terms, so the comparison is not term by term), and the
    Holst term is Holst 1996 (\claimref{synthesis.imported-lovelock-cartan-four-forms-and-holst-term}(b)). Transport-convenient: the counts are those of the de Sitter or
    anti-de Sitter and Lorentz algebras with the Stelle-West vector, and X enters only through V. Consequence for
    the Clausius route: inside the curvature-only class the Euler term cannot be removed from the bulk density,
    so excluding it from horizon entropy needs an edge (boundary) term at the cut or leaving the class.
---

## formal
Work in $\Cl(2,4)$ with $\nO = \tfrac12(e_{4} + e_{5})$, $\nInf = e_{4} - e_{5}$ as in Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}, $\Lambda \neq 0$, frozen point $I = \nInf + \tfrac{\Lambda}{6}\nO$ with $Q(I) = \Lambda/3$, canonical tractor $X = \nO$ and Stelle-West vector $V = X - \tfrac{3}{\Lambda}I$ with $Q(V) = -3/\Lambda$, $\ip{I}{V} = 0$ (Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector}); $W = \{I, V\}^{\perp}$, a copy of the spacetime vectors. A gauge field $A$ is a bivector-valued one-form on flat spacetime with values in a Lie algebra $\mathfrak{g}$ of bivectors, $F = dA + \tfrac12[A, A]$ its field strength (commutator product), $F \wedge G$ the wedge of forms with the values multiplied. Call a four-form density $L$ \emph{admissible} if (P) it is a polynomial in the components of the fields, formed with wedge products only (no inverse frame, so no Hodge dual and no contraction with $\hb$); (C) it depends on $A$ only through $F$ and on the data $I$, $X$ (or $V$) algebraically; (G) it is invariant under $\mathfrak{g}$ acting on all values at once. Then $L = B(F \wedge F)$ for a $\mathfrak{g}$-invariant symmetric bilinear form $B$ on the values. For $w \in W$ the \emph{internal reflection} acts on the values by $u \mapsto wuw^{-1}$ with the spacetime orientation fixed; since the integral of a four-form changes sign under orientation reversal, a density odd under the internal reflection is even under the \emph{combined parity} (orientation reversal with the internal reflection, the frame identifying the two), under which Einstein-Hilbert is even and the Holst term odd. With $i_{6}$ the unit pseudoscalar:
\begin{enumerate}
\item[(i)] \emph{(Pure transport and one datum; proved.)} For $\mathfrak{g} = \so(2,4)$ with no datum, and for the parabolic algebra of the line of $X$, the invariant forms are the multiples of $K(F, G) = \langle FG\rangle_{0}$: $L$ is the Chern-Weil density $\langle F \wedge F\rangle_{0}$, closed, with identically vanishing Euler-Lagrange derivative. With $X$ alone, invariance under the stabiliser of $X$ and the field strength unrestricted (forms on all bivectors), there are two invariant forms and none is odd under the internal reflection. On $\Lambda^{2}(X^{\perp})$ (the values of the field strength of a connection valued in the stabiliser of $X$, and of the normal torsion-free tractor connection) there are two invariant forms, exactly one internally odd, $\epsilon_{X}$; for a connection valued in the stabiliser of $X$ both are Chern-Weil, while on the normal tractor connection $\epsilon(I, X, F, F)$ is the Weyl square (Theorem \claimref{synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared}(iii)).
\item[(ii)] \emph{(The frozen point alone; proved.)} For $A$ valued in the stabiliser of $I$ ($\so(1,4)$ for $\Lambda > 0$, $\so(2,3)$ for $\Lambda < 0$; this is $\Lambda^{2}(I^{\perp})$), the invariant forms are again the multiples of $K$: topological.
\item[(iii)] \emph{(Frozen point and canonical tractor; proved.)} For $A$ in the stabiliser of $I$ and invariance under it acting on $(A, V)$ (equivalently, at $V$ fixed, under the Lorentz algebra stabilising $I$ and $V$), the invariant forms are a three-dimensional space with basis $K$, $H(F, G) = \langle (F \wedge I \wedge V)(G \wedge I \wedge V)\rangle_{0}$ and $M(F, G) = \langle (F \wedge G \wedge I \wedge V)\,i_{6}\rangle_{0} = \epsilon(I, V, F, G) = \epsilon(I, X, F, G)$. Under the internal reflection in a vector of $W$, $K$ and $H$ are even and $M$ is odd; the internally odd invariant forms are the multiples of $M$. So under the combined parity $M$ is even and $K$, $H$ are odd. Of the three only $K$ is invariant under the whole stabiliser of $I$, so only $K$ is a Chern-Weil density.
\item[(iv)] \emph{(Field equations; proved.)} In the gauge $V$ constant the general connection preserving $I$ is $A(a) = \Omega(a) + \hb^{-1}(a) \wedge V/Q(V)$, the field variable for every field (on Einstein fields it is the connection of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}(v)). The frame variation of $\int M(F \wedge F)$ is, as a linear map of the curvature at a point, of rank $10$ on the algebraic curvature tensors with kernel the Weyl part (the frame equation of Theorem \claimref{synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part}); the frame variation of $\int H(F \wedge F)$ vanishes on every curvature obeying the first Bianchi identity (torsion zero) and has rank $16$ on general curvature two-forms. So $H$ is not topological but changes no frame equation without torsion.
\item[(v)] \emph{(Consequence.)} An admissible action on the series' data is $\kappa M + \kappa' H + \kappa'' K$; invariant under the combined parity it is $\kappa\,\epsilon(I, X, F, F)$, the frozen-point MacDowell-Mansouri functional $Q(I)^{-1}\int\epsilon(I, V, F, F)$ of Fact \claimref{dark-energy.imported-macdowell-mansouri-theorem-stelle-west} up to the free normalisation $\kappa$. Without the parity hypothesis uniqueness is equivalent to torsion-free coupling: on torsion-free fields the frame equation is that of $\kappa M$ (that torsion-free fields still solve the connection equation without spin is the Holst result, Fact \claimref{synthesis.imported-lovelock-cartan-four-forms-and-holst-term}(b), not checked here), but under the Einstein-Cartan coupling of Fact \claimref{synthesis.imported-einstein-cartan-matter-coupling} torsion is proportional to the spin density, so with spinning matter $\kappa'$ is physical (it enters the spin-spin contact term, as the Barbero-Immirzi parameter; the readings recorded in Fact \claimref{synthesis.imported-lovelock-cartan-four-forms-and-holst-term}). Writing the Lorentz block $F_{W} = -R + \tfrac{\Lambda}{3}e \wedge e$, $Q(I)^{-1}M(F_{W}, F_{W}) = \tfrac{3}{\Lambda}M(R, R) - 2M(R, e \wedge e) + \tfrac{\Lambda}{3}M(e \wedge e, e \wedge e)$: Euler, Einstein-Hilbert and volume terms in fixed ratio, so the cosmological constant of the field equations is the frozen point's and the Euler term is present; since $M$ spans the internally odd admissible densities, no admissible counterterm removes it inside the class (the Lorentz Euler density $M(R, R)$ depends on $DV$ through $R$, so it is not admissible under (C)).
\item[(vi)] \emph{(Which hypotheses do the work; proved, the slot step argued by degree counting and proved under (T) in Theorem \claimref{synthesis.inverse-frame-free-tractor-gauge-field-preserves-a-frozen-point}(i).)} Dropping (C), so that $V$ also enters through $DV$ (the soldering form), adds two invariants $B'(e \wedge e, F)$ (Einstein-Hilbert and Holst type) and one $e^{4}$ (volume): six in all, and the Euler, Einstein-Hilbert and volume coefficients become independent. Dropping the reduction (letting $F$ range over all bivectors with $I$, $V$ algebraic) gives six invariant forms. Hypothesis (P) forces the reduction for slots that are functions of $(\hb, \Omega)$, that is under the premise (T) that the tractor gauge field is assembled from $(\hb, \Omega)$ and no further field: the only polynomial, Lorentz-covariant, inverse-frame-free special-conformal slot built from them is $\rho\,\hb^{-1}(a)$ with $\rho$ constant (the Lorentz commutant on $W$ is one-dimensional), and with it $\nInf + \rho\nO$ is parallel: the reduction datum is a frozen point with $\Lambda = 6\rho$, and the normal tractor connection, whose slot is the Schouten map, lies outside (P). Without (T) the forcing fails: a special-conformal slot that is a field of its own also satisfies (P) and preserves no tractor (Theorem \claimref{synthesis.inverse-frame-free-tractor-gauge-field-preserves-a-frozen-point}(iv)). So the field space of connections preserving $I$, not the integrand, is what (P) supplies under (T); in invariant form that field space is Premise \claimref{synthesis.field-space-premise-parallel-frozen-point}.
\end{enumerate}

## technical
The open problem asks whether transport fixes the frozen-point MacDowell-Mansouri functional among the invariant four-forms of the $\Cl(2,4)$ tractor gauge field. This result answers it as a classification, with the hypotheses stated. Admissible densities are polynomial, use no inverse frame (no Hodge dual), depend on the gauge field only through its field strength $F$, take the frozen point $I$ and the canonical tractor $X$ algebraically, and are gauge invariant. In four dimensions they are $B(F \wedge F)$ for an invariant symmetric form $B$, and the invariant forms are computed in exact arithmetic. Parity below means the combined spacetime and internal parity, under which Einstein-Hilbert is even and the Holst term odd; at the level of the forms it is oddness under the internal reflection alone.

Pure transport (all of $\so(2,4)$, or the parabolic algebra of $X$) and the frozen point alone each admit only the Killing form, whose density is the Chern-Weil form, closed and without field equations. With the canonical tractor alone and the field strength unrestricted there is no internally odd density; on the subspace where the field strength annihilates $X$ there is one, which on the normal tractor connection is the Weyl square. With the connection reduced by $I$ and both data present the space is three-dimensional: the Chern-Weil form, a Holst-type form $H$ built from the Lorentz block, and $\epsilon(I, X, F, F)$, which equals $\epsilon(I, V, F, F)$. Only the last is parity-invariant. Its frame equation is the stored Einstein equation with cosmological constant (rank 10, Weyl kernel). The Holst-type form is not topological, but its frame equation vanishes whenever the curvature obeys the first Bianchi identity, so it changes nothing without torsion; under the Einstein-Cartan coupling spinning matter sources torsion and its coefficient becomes physical.

So, inside the curvature-only class with the reduction by $I$, parity selects the MacDowell-Mansouri functional up to its normalisation, which stays free; without parity, uniqueness holds exactly when the coupling is torsion-free. Inside the class its Euler, Einstein-Hilbert and volume terms come in fixed ratio: the field equations' $\Lambda$ is the frozen point's, and the Euler term cannot be cancelled. Allowing the soldering form $DV$ as a separate ingredient adds three invariants and frees those ratios. Not reducing by $I$ gives six invariant forms. No inverse frame forces the reduction for slots built from the two gauge fields $(\hb, \Omega)$ alone (an independent special-conformal field would also be inverse-frame-free), since the only admissible special-conformal slot built from them is a constant multiple of the frame, which makes a constant scale tractor, a frozen point, parallel.

## lay
The series borrows a formula for the action of gravity, the rule from which Einstein's equations follow. This result asks which rules of the same general kind could be built from the series' own ingredients: its six-dimensional connection, its frozen point and its canonical direction. Rules built from the connection alone, or with the frozen point alone, have no effect on the equations. With the connection tied to the frozen point and the canonical direction added, there are exactly two rules with effect. One is the borrowed formula. The other has no effect unless matter spins. Requiring the rule to respect mirror symmetry of space and of the internal directions together keeps only the borrowed formula, up to its overall strength, which is still not fixed.

## one-liner
Admissible actions of the $\Cl(2,4)$ gauge field (polynomial, inverse-frame-free, depending on the field only through $F$, with the frozen point $I$ and canonical tractor $X$ algebraic, gauge invariant) are $B(F \wedge F)$; for $\so(2,4)$, the parabolic algebra or $I$ alone only the Chern-Weil density remains, and with $X$ alone and $F$ unrestricted none is odd under the internal reflection (on $F \cdot X = 0$ one is, the Weyl square on the normal connection); with the connection reduced by $I$ and $X$ added, the invariant forms are spanned by $K$, a Holst-type $H$ and $\epsilon(I, X, F, F)$, the last the only one invariant under the combined spacetime and internal parity (rank-10 Einstein frame equation), while $H$'s frame equation vanishes without torsion and is physical with spin under Einstein-Cartan; so, inside this class and given that parity, the frozen-point MacDowell-Mansouri functional is unique up to normalisation, its Euler term cannot be cancelled inside the class, and dropping the curvature-only hypothesis frees the Euler, Einstein-Hilbert and volume coefficients.
