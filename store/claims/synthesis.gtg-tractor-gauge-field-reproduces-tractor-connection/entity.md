---
id: synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection
kind: claim
version: 1
title: The tractor connection as a rotation-gauge field of the conformal model on flat spacetime
status: proved
region: synthesis
subject: einstein
tags: [tractors, gauge-fields, conformal-model, curvature-and-field-equations]
proposed_by:
  kind: ai
  session: maintainer-2026-10-23-gtg
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
  - interior.imported-tractor-connection@3
  - interior.scale-tractor-leaves-cone@8
  - mass.de-sitter-scale-frozen-point@6
  - synthesis.imported-gtg-dictionary@2
  - dark-energy.stelle-west-vector-frozen-point@6
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_gauge_field_reproduces_stored_connection
- kind: check
  ref: check.py::check_scale_tractor_parallel_iff_einstein
- kind: check
  ref: check.py::check_flat_de_sitter_scale_tractor_is_parallel_frozen_point
- kind: check
  ref: check.py::check_field_strength_spacetime_block_is_weyl
- kind: check
  ref: check.py::check_stelle_west_reduction_is_macdowell_mansouri_connection
extraction:
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: synthesis.imported-gtg-dictionary repinned 1 -> 2 after reviewing its correction of the component reading in clause (iv) to R(g_mu ^ g_nu) = -R(e_mu ^ e_nu), agreeing with the store''s sign R(B) = -R(hb(B)) the clause already stated, with GA wording in (ii) and (iv); the translation rules are unchanged; the use here holds as cited.'
  note: >-
    The store's own transcription of the tractor connection into Gauge Theory Gravity: the
    connection becomes a Cl(2,4)-bivector-valued rotation-gauge field on flat spacetime, the
    Lorentz part being the gravitational Omega, the soldering part the frame hb^{-1}(a) and the
    special-conformal part the Schouten map. No source carrying the normal tractor connection as a
    gauge field on flat spacetime was found (searched 2026-10-23: Bailey-Eastwood-Gover 1994 and
    Attard-Francois 2017 work on a curved conformal manifold; Lasenby-Hobson 2016 and Hobson-Lasenby
    2021 gauge the Weyl and conformal groups on Minkowski spacetime by other routes), so this is a
    proved claim of the store resting on the imported connection, not an import. The curvature sign
    is the store's (de Sitter Ric = Lambda g), with P = (Lambda/6) id on an Einstein field, matching
    interior.scale-tractor-leaves-cone.
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Created by Leon''s decision of 2026-10-23 to carry tractors as a flat-space Cl(2,4) gauge field with an exact check; the tractor-language results are restated against it. Fixes (referee GR2, 2026-10-23): the gauge group is the parabolic stabiliser of the line of n_0, the canonical tractor X (not of n_inf); Lambda := 6 rho defined before use in (ii) and in the proof; technical level says the checks cover the algebraic content (check 4 only the algebraic part of the field strength).'
---

## formal
Let $(\hb, \Omega)$ be a gravitational field on flat spacetime with invertible region $U$, derived metric $g$ and curvature operator $\mathcal{R}$ in the store's sign (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), and let $\Sch(A) = \tfrac12\bigl(\mathcal{R}(A) - \tfrac16 A\,\mathcal{R}\bigr)$ be its Schouten map (Fact \claimref{synthesis.imported-gtg-dictionary}). Adjoin to the spacetime vectors of $\Cl(1,3)$ the hyperbolic plane spanned by the null vectors $\nO$, $\nInf$ with $\nO \cdot \nInf = 1$, so that the vectors of $\Cl(2,4)$ are written $V = \sigma\,\nInf + \mu + \rho\,\nO$ with $\mu$ a physical vector and $Q(V) = 2\sigma\rho + Q(\mu)$. Define the \emph{tractor gauge field} and its covariant derivative
\[
\Omega_{T}(a) \;=\; \Omega(a) \;-\; \nInf \wedge \hb^{-1}(a) \;+\; \nO \wedge \Sch\bigl(\hb^{-1}(a)\bigr), \qquad
D^{T}_{a} V \;=\; a \cdot \nabla V + \Omega_{T}(a) \times V .
\]
Then on $U$, with $A = \hb^{-1}(a)$:
\begin{enumerate}
\item[(i)] $D^{T}_{a}$ is the tractor connection of Fact \claimref{interior.imported-tractor-connection} in the splitting of $g$: its slots are $(a \cdot \nabla\sigma - \mu \cdot A,\ D_{a}\mu + \rho A - \sigma\,\Sch(A),\ a \cdot \nabla\rho + \Sch(A) \cdot \mu)$, and it preserves $Q$, the tractor metric;
\item[(ii)] the section $I = \nInf + \rho\,\nO$ is $D^{T}$-parallel if and only if $\rho$ is constant and $\Sch = \rho\,\mathrm{id}$, that is, with $\Lambda := 6\rho$, the field is Einstein, $\mathcal{R}(a) = \Lambda a$; then $Q(I) = \Lambda/3$ (Theorem \claimref{interior.scale-tractor-leaves-cone});
\item[(iii)] on flat spacetime ($\hb = 1$, $\Omega = 0$, $\Sch = 0$) the scale tractor of $\sigma(x) = 1 - \Lambda Q(x)/12$, $V(x) = \sigma(x)\,\nInf - \tfrac{\Lambda}{6}x + \tfrac{\Lambda}{6}\nO$, is $D^{T}$-parallel with $Q(V) = \Lambda/3$, and $V(0) = \nInf + \tfrac{\Lambda}{6}\nO$ is the frozen point $I_{\Lambda}$ (Lemma \claimref{mass.de-sitter-scale-frozen-point});
\item[(iv)] the part of the field strength of $\Omega_{T}$ that involves no derivative of the frame or of $\Sch$, $-\mathcal{R}(A \wedge B) + \Theta(A) \times \Theta(B)$ with $\Theta(A) = -\nInf \wedge A + \nO \wedge \Sch(A)$, has spacetime block $-\mathcal{W}(A \wedge B)$, the Weyl curvature, and no other block; the derivative terms are the torsion ($\nInf$ block, zero for the torsion-free field) and the Cotton term ($\nO$ block). On de Sitter space this part vanishes;
\item[(v)] on an Einstein field with $\Lambda \neq 0$, $\Sch = \tfrac{\Lambda}{6}\mathrm{id}$ and $\Omega_{T}(a) = \Omega(a) + \hb^{-1}(a) \wedge W$ with $W = \nInf - \tfrac{\Lambda}{6}\nO = V/Q(V)$ for the Stelle-West vector $V = \nO - \tfrac{3}{\Lambda}I$ of Lemma \claimref{dark-energy.stelle-west-vector-frozen-point}, $Q(V) = -3/\Lambda = -\ell^{2}$: then $D^{T}_{a}V = \hb^{-1}(a)$ (the soldering form) for constant $V$ components, $\Omega_{T}(a) \times I = \Omega(a) \times I = 0$, and $\Theta(A) \times \Theta(B) = \tfrac{\Lambda}{3}A \wedge B = \ell^{-2}A \wedge B$, so restricted to $I^{\perp}$ the tractor gauge field is the MacDowell-Mansouri connection $\Omega(a) - \hb^{-1}(a) \wedge V/\ell^{2}$, whose Lorentz curvature block is $-(\mathcal{R}(B) - \ell^{-2}B)$.
\end{enumerate}
The tractor connection is therefore a rotation-gauge field of the conformal model $\Cl(2,4)$ on flat spacetime, gauged by the rotors of the parabolic subgroup stabilising the line of the canonical tractor $\nO$ (Lorentz rotations, the dilation generated by $\nO \wedge \nInf$, and the special-conformal rotors generated by $\nO \wedge y$ for spacetime vectors $y$), with the gauge law $\Omega_{T} \mapsto U\Omega_{T}\tilde U - 2(a \cdot \nabla U)\tilde U$ of the gravitational $\Omega$.

## technical
Gauge Theory Gravity carries the tractor connection as one more gauge field on flat spacetime. Adjoin the null pair $\nO$, $\nInf$ of the conformal model to the spacetime vectors and write a tractor as $\sigma\nInf + \mu + \rho\nO$. The field $\Omega_{T}(a) = \Omega(a) - \nInf \wedge \hb^{-1}(a) + \nO \wedge \Sch(\hb^{-1}(a))$ is a bivector of $\Cl(2,4)$ for each direction: its Lorentz part is the gravitational connection, its soldering part the frame vector $\hb^{-1}(a)$, and its special-conformal part the Schouten map.

Acting by the commutator product, it reproduces the stored tractor connection slot by slot and preserves the tractor metric. The scale tractor $\nInf + \rho\nO$ is parallel exactly for Einstein fields with $\Lambda = 6\rho$, with squared norm $\Lambda/3$. On flat spacetime the de Sitter scale tractor is parallel and equals the frozen point at the origin. The algebraic part of the field strength is minus the Weyl curvature, so it vanishes on de Sitter space. Restricted to the complement of the frozen point it is the MacDowell-Mansouri connection $\Omega(a) - \hb^{-1}(a) \wedge V/\ell^{2}$, whose covariant derivative of the Stelle-West vector is the soldering form. The algebraic content of all five statements is checked in exact arithmetic (for (iv), only the algebraic part of the field strength; its decomposition of the derivative terms is proved in the text).

## lay
The series uses a construction called the tractor connection, which normally lives on a curved spacetime. This result shows that it can equally be written on flat spacetime, as a field that turns directions in a six-dimensional extension of spacetime from point to point, built from the gravitational fields themselves. Written this way it reproduces the stored formulas exactly, picks out the same special direction (the frozen point) for spacetimes with a cosmological constant, and its strength is the part of curvature that is unchanged by rescaling lengths.

## one-liner
On flat spacetime the tractor connection is the $\Cl(2,4)$ gauge field $\Omega_{T}(a) = \Omega(a) - \nInf \wedge \hb^{-1}(a) + \nO \wedge \Sch(\hb^{-1}(a))$: it reproduces the stored connection, its parallel scale tractor is the Einstein condition with $Q(I) = \Lambda/3$, and its algebraic field strength is minus the Weyl curvature.
