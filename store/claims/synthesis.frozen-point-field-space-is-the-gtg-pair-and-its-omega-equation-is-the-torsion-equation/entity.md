---
id: synthesis.frozen-point-field-space-is-the-gtg-pair-and-its-omega-equation-is-the-torsion-equation
kind: claim
version: 2
title: 'The frozen-point field space as GTG''s pair, and the torsion equation'
status: proved
region: synthesis
subject: einstein
tags: [tractors, gauge-fields, curvature-and-field-equations, forcing-and-uniqueness, conformal-model]
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
  - synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection@1
  - dark-energy.imported-macdowell-mansouri-theorem-stelle-west@3
  - synthesis.curvature-only-tractor-actions-are-macdowell-mansouri@3
  - synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared@3
  - synthesis.imported-einstein-cartan-matter-coupling@1
  - synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_omega_equation_is_the_torsion_equation
- kind: check
  ref: check.py::check_gtg_pair_is_bijective_with_connections_preserving_i
- kind: check
  ref: check.py::check_field_strength_splits_into_shifted_curvature_and_torsion
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.curvature-only-tractor-actions-are-macdowell-mansouri
  - synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared
extraction:
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review (second round): synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part repinned 3 -> 4 after reviewing its restatement (formal setting restated (A(a) = Omega(a) - (Lambda/3) hb^-1(a) ^ V, l^2 = 3/|Lambda| dropped)); clauses (i) to (iv), the store sign and the frame equation, cited here, are unchanged, and the use here holds as cited.'
  open_problem: op.derive-gravitational-action
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 1 -> 2: the citations of the slot lattice and of the inverse-frame-free forcing are now claimrefs (text only: both of those results depend on this one), the field-space premise is named by claimref as synthesis.field-space-premise-parallel-frozen-point (text only), the note points to the checked spin-choice note of the GTG definition for Lasenby, Doran and Gull, and the curvature-only classification is repinned to version 3 (clause (vi) reworded under (T); clause (iv), cited here, unchanged). Statement unchanged.'
  note: >-
    Tests the reading "the field space of connections preserving the frozen point is Gauge Theory
    Gravity's gauge principle (independent position-gauge and rotation-gauge fields)". Outcome: on the
    field space of gauge fields preserving a constant tractor, which is the GTG pair (the standard
    Stelle-West and Cartan-geometric form, as in Fact
    dark-energy.imported-macdowell-mansouri-theorem-stelle-west and Theorem
    synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection (v), here with the Poincare case
    rho = 0 included), the Omega-equation of the frozen-point functional is the torsion equation (the
    standard first-order fact with invertible frame). Hence the independence of the two gauge fields
    (first-order, Palatini-type variation) is not what turns the Bach equations into Einstein's: the
    frozen special-conformal slot is; the independence decides only the spin part of the matter coupling
    (Einstein-Cartan versus torsion-free). This justifies the torsion-free restriction of the frozen rows of the slot lattice, \claimref{synthesis.frozen-point-integrand-gives-einstein-only-with-the-symmetric-slot-frozen}; why the varied field is this field space is not derived here (the forcing theorem \claimref{synthesis.inverse-frame-free-tractor-gauge-field-preserves-a-frozen-point} trades it for an assembly premise; the field space itself remains a premise, recorded as \claimref{synthesis.field-space-premise-parallel-frozen-point}). That Lasenby, Doran and Gull vary hb and Omega independently and obtain torsion from the Dirac spin is recorded, checked against their text, in the spin-choice note of Definition obj.synthesis.gtg-flat-spacetime-gauge-fields. Cited from memory, not checked against the texts here: the equivalence of first-order and metric variation of the Einstein-Hilbert action without spin (the one-and-a-half-order argument). Transport-convenient: the chart, the frozen point
    and the Cl(2,4) gauge field are the series' objects; the bijection and the torsion statement are
    transport-absent; the new content is the comparison of the two one-field spaces in (i).

---

## formal
Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) with physical frame $E(a) = \hb^{-1}(a)$, and work in $\Cl(2,4)$ with the null pair $\nO = \tfrac12(e_{4} + e_{5})$, $\nInf = e_{4} - e_{5}$ of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection} ($\ip{\nO}{\nInf} = 1$), $W$ the spacetime vectors, $X = \nO$ the canonical tractor and the commutator product $A \times B = \tfrac12(AB - BA)$. For real $\rho$ put $I_{\rho} = \nInf + \rho\nO$ and $u_{\rho} = \nInf - \rho\nO$, so $Q(I_{\rho}) = 2\rho$, $Q(u_{\rho}) = -2\rho$, $\ip{u_{\rho}}{I_{\rho}} = 0$; for $\rho = \Lambda/6 \neq 0$, $I_{\rho}$ is the frozen point and $u_{\rho} = V/Q(V)$ for the Stelle-West vector $V$ of Fact \claimref{dark-energy.imported-macdowell-mansouri-theorem-stelle-west}. Write $\Phi_{\rho}(\hb, \Omega)(a) = \Omega(a) - u_{\rho} \wedge \hb^{-1}(a) = \Omega(a) - \nInf \wedge \hb^{-1}(a) + \rho\,\nO \wedge \hb^{-1}(a)$. A $\Cl(2,4)$ gauge field is a one-form $A$ with values in the bivectors of $\Cl(2,4)$, $F(a \wedge b) = a \cdot \nabla A(b) - b \cdot \nabla A(a) + A(a) \times A(b)$ its field strength.
\begin{enumerate}
\item[(i)] \emph{(The $\Omega$-equation is the torsion equation, so the slot carries Einstein's equations; proved.)} For $\rho \neq 0$ and the frozen-point functional $S = Q(I_{\rho})^{-1}\int\epsilon(I_{\rho}, V, F, F)$ on the field space $\Phi_{\rho}$ of (ii), the $\Omega$-equation depends on $F$ only through its torsion block: $\epsilon(I_{\rho}, w, B, C) = 0$ for $w \in W$ and $B, C \in \Lambda^{2}W$, and the $\Omega$-equation is an invertible linear map of the torsion (rank $24$ at a point). So on the torsion-free subfamily $\Omega = \Omega(\hb)$, a field space of one field $\hb$, varying $\hb$ gives the frame equation of the functional, $2(\mathcal{G}(a) + \Lambda a)I = 0$ (Theorem \claimref{synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part}; rank $10$ with kernel the Weyl part, Theorem \claimref{synthesis.curvature-only-tractor-actions-are-macdowell-mansouri}(iv)): Einstein's equations with $\Lambda = 6\rho$. The tractor gauge field of a torsion-free field has the same $\Omega(\hb)$ and the same soldering and differs only in the special-conformal slot ($\Sch$ for $\rho\,\mathrm{id}$; Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}), and there the same integrand gives the Bach equations (Theorem \claimref{synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared}). Hence the slot $\rho\,\hb^{-1}$ carries Einstein's equations; the independence of $\hb$ and $\Omega$ decides only the torsion equation, torsion-free or, with spinning matter under the minimal coupling, Einstein-Cartan (Fact \claimref{synthesis.imported-einstein-cartan-matter-coupling}).
\item[(ii)] \emph{(The field space is the pair; proved.)} The bivectors $B$ with $B \times I_{\rho} = 0$ are $\Lambda^{2}W \oplus u_{\rho} \wedge W$, uniquely ($10 = 6 + 4$), and the vectors annihilated by all of them form exactly the line of $I_{\rho}$. Hence $\Phi_{\rho}$ is a bijection from pairs $(\hb^{-1}, \Omega)$ onto gauge fields valued in the stabiliser of $I_{\rho}$, intertwining the rotation gauge (rotors of $W$, which fix $\nO$ and $\nInf$) and the displacement gauge; its soldering part is nondegenerate exactly on the invertible region. Its field strength is
\[
F(a \wedge b) \;=\; R(a \wedge b) + 2\rho\,E(a) \wedge E(b) - u_{\rho} \wedge T(a \wedge b), \qquad T(a \wedge b) = D_{a}E(b) - D_{b}E(a)
\]
for constant background directions, with $R$ the field strength of $\Omega$ and $T$ the torsion; on physical bivectors the Lorentz block is $-(\mathcal{R}(B) - \tfrac{\Lambda}{3}B)$ in the store's sign, as in Fact \claimref{dark-energy.imported-macdowell-mansouri-theorem-stelle-west}. For $\rho \neq 0$ the stabiliser is $\so(1,4)$ or $\so(2,3)$; for $\rho = 0$, $I_{0} = \nInf$ and the block $u_{0} \wedge W$ is abelian, so the stabiliser is the Poincar\'e algebra, the internal form of the pair's own gauge algebra, of which the frozen point is the deformation with $[u_{\rho} \wedge a, u_{\rho} \wedge b] = 2\rho\, a \wedge b$.
\end{enumerate}
\emph{Reading.} Clause (i) is the comparison: the tractor gauge field of a torsion-free field and $\Phi_{\rho}(\hb, \Omega(\hb))$ share the rotation-gauge field and the soldering and differ only in the special-conformal slot ($\Sch$ against $\rho\,\mathrm{id}$, agreeing exactly on Einstein fields by (ii) and Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}(ii)); on the first the integrand gives the Bach equations, on the second Einstein's. Treating $\Omega$ as independent changes only the torsion equation. Clause (ii) identifies the field space with GTG's pair and a constant tractor; that the varied field is this field space, rather than the normal tractor connection, is not derived here and remains a premise (Premise \claimref{synthesis.field-space-premise-parallel-frozen-point}).

## technical
The question is whether the field space on which the frozen-point MacDowell-Mansouri integrand gives Einstein's equations, the $\Cl(2,4)$ connections preserving the frozen point $I$, is Gauge Theory Gravity's gauge principle: two independent gauge fields, $\hb$ for displacements and $\Omega$ for rotations.

The new content is a comparison. On the gauge fields preserving a constant tractor $I_{\rho}$, the $\Omega$-equation of the frozen-point functional is exactly the torsion equation (the standard first-order fact with an invertible frame, written in the series' chart: only the torsion block of the field strength enters, through an invertible map). So restricting to torsion-free fields, one field $\hb$ as for the normal tractor connection, still gives Einstein's equations with $\Lambda = 6\rho$ for $\rho \neq 0$. The normal tractor connection of the same torsion-free field has the same rotation-gauge field and soldering and differs only in the special-conformal slot, the Schouten map instead of $\rho$ times the frame; there the integrand gives the Bach equations. The slot, not the independence of the two gauge fields, carries Einstein's equations; the independence decides only the torsion (spin) equation.

The second clause records the field space in GTG terms, again a standard Cartan-geometric fact in the series' chart: the bivectors annihilating $I_{\rho} = \nInf + \rho\nO$ split uniquely into the Lorentz bivectors and $u_{\rho} \wedge W$, so $\Omega - u_{\rho} \wedge \hb^{-1}$ is a bijection from pairs onto $I$-preserving gauge fields, equivariant under GTG's rotation and displacement gauges, with field strength the shifted curvature $R + 2\rho\,E \wedge E$ plus the torsion. At $\rho = 0$ the algebra is the Poincar\'e algebra. Why the varied field is this one is not derived: it remains a premise.

## lay
In the series, gravity is described by two fields on flat spacetime, one recording how rulers are laid down and one recording how directions turn. A borrowed rule for gravity's equations works only if a larger six-dimensional connection built from these fields keeps one special direction, the frozen point, fixed. This result shows that treating the two fields as independent is not what makes the rule produce Einstein's equations: tying the second field to the first changes nothing in empty space. One specific slot of the larger connection does the work. It also confirms that the two fields plus a fixed special direction are exactly such connections. Why the connection has that form is an assumption, not something the series derives.

## one-liner
On the $\Cl(2,4)$ gauge fields preserving $I_{\rho} = \nInf + \rho\nO$, which are exactly $\Omega - (\nInf - \rho\nO) \wedge \hb^{-1}$ for GTG's pair (field strength $R + 2\rho\,E \wedge E$ plus torsion; Poincar\'e at $\rho = 0$), the $\Omega$-equation of the frozen-point functional is the torsion equation (rank $24$); so for $\rho \neq 0$, with $\Omega = \Omega(\hb)$, it still gives Einstein's equations with $\Lambda = 6\rho$, while the normal tractor connection, with the same $\Omega(\hb)$ and soldering and the Schouten slot, gives Bach's: the frozen slot $\rho\,\hb^{-1}$, not the independence of $\Omega$, carries Einstein's equations, and the independence decides only the torsion (spin) equation; the field space itself is not derived.
