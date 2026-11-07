---
id: synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part
kind: claim
version: 4
title: 'The MacDowell-Mansouri principle fixes the trace-free part'
status: proved
region: synthesis
subject: einstein
tags: [tractors, curvature-and-field-equations, forcing-and-uniqueness, conformal-model]
proposed_by:
  kind: ai
  session: 2026-10-31-all-open
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: 'consistency pass, the curvature-sign line made the store sign that its formulas use'
  version: 3
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'GA rewrite (declared outside_ga)'
  version: 3
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'GTG proof of (i)-(iii): frame equation E(a) = 2 d_b ^ F(I(a ^ b)) = 2(G(a) + Lambda a) I from the curvature operator; exact checks'
  version: 3
  source: maintainer pass 2026-11-07 (GTG proofs)
- name: Claude Opus 5.5
  role: 'GTG review (referee F2): GA readings of the formal setup (Ricci, Schouten and Lorentz-block maps); pins'
  version: 3
  source: maintainer pass 2026-11-07 (GTG review fixes)
- name: Claude Opus 5.5
  role: 'formal setting restated at Leon''s second-round decisions: A(a) = Omega(a) - (Lambda/3) hb^-1(a) ^ V, right on both branches'
  version: 4
  source: maintainer pass 2026-11-07 (decisions, second round)
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - dark-energy.imported-macdowell-mansouri-theorem-stelle-west@4
  - dark-energy.frozen-point-makes-stelle-west-vector@7
  - synthesis.series-wald-entropy-changes-without-flux-on-local-horizons@3
  - synthesis.positive-structure-and-natural-scale-actions-do-not-select-the-almost-einstein-scale@4
  - synthesis.einstein-condition-is-infinity-vacuum-incidence@4
  - synthesis.infinity-vacuum-incidence-is-a-property-of-the-scale@4
  - synthesis.imported-gtg-dictionary@2
  - synthesis.imported-einstein-cartan-matter-coupling@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_frame_equation_is_twice_the_dual_of_einstein_plus_lambda
- kind: check
  ref: check.py::check_frame_identity_on_the_spanning_set
- kind: check
  ref: check.py::check_kernel_is_the_weyl_part_and_rank_is_ten
- kind: check
  ref: check.py::check_dilation_restriction_is_the_yamabe_trace
- kind: check
  ref: check.py::check_on_shell_schouten_is_the_stored_tractor_derivative
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_gtg_frame_trivector_is_twice_dual_einstein_plus_lambda
- kind: check
  ref: check.py::check_gtg_frame_equation_on_gauge_fields_and_dilation_trace
lineage:
  motivated_by:
  - synthesis.positive-structure-and-natural-scale-actions-do-not-select-the-almost-einstein-scale
  - synthesis.infinity-vacuum-incidence-is-a-property-of-the-scale
  - synthesis.einstein-equations-from-c-loc-and-clausius
  - synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection
extraction:
  maintainer_pass_decisions_2:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 3 -> 4. Leon''s second-round answer 1 (REPORT.md For Leon item 2, fix-F2.md): the formal setting drops "l^2 = 3/|Lambda|" and writes A(a) = Omega(a) - (Lambda/3) hb^-1(a) ^ V (that is Omega(a) + hb^-1(a) ^ V/Q(V), so that D_aV = hb^-1(a) on both branches), the texts proposed in fix-F2.md; the proof''s one display of the Cartan connection follows (l no longer defined). Exact check (GA.py, Cl(2,4)): with Q(V) = -3/Lambda, the translational part of A(a) acting on V, (-(Lambda/3) u ^ V) x V, equals u for u = e0, e1 and e2 - (5/3) e3 at Lambda = 3, -3, 3/4 and -12 (V = e_-, e_+, 2 e_-, e_+/2), and so does (u ^ V/Q(V)) x V; the old -u ^ V/l^2 with l^2 = 3/|Lambda| gives -u at Lambda = -3 and -12. Clauses (i) to (iv) are unaffected (the Lorentz block is quadratic in 1/l^2); no check encodes l. Pin review (second round): synthesis.positive-structure-and-natural-scale-actions-do-not-select-the-almost-einstein-scale repinned 3 -> 4 after reviewing its restatement (formal (iii) restated (the null vector of the (t + x1)^2 counter-model is e0 - e1)); clauses (i), (ii) and (iv), cited here, are unchanged, and the use here holds as cited.'
  maintainer_pass_gtg_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Referee F2 review. (1) The formal display A(a) = Omega(a) - hb^{-1}(a) ^ V/l^2 with l^2 = 3/|Lambda| has the wrong sign on the anti-de Sitter branch: with Q(V) = -3/Lambda, D_a V = -(Q(V)/l^2) hb^{-1}(a) = (3/(Lambda l^2)) hb^{-1}(a), which is +hb^{-1}(a) for Lambda > 0 and -hb^{-1}(a) for Lambda < 0 (computed by hand from (A ^ V) . V = Q(V) A; the referee found the same on both branches with the engine). The Lorentz block (A ^ V) x (B ^ V)/l^4 = (Lambda/3) A ^ B is quadratic in 1/l^2 and the same on both branches, so clauses (i) to (iv) and the checks are unaffected; the display on the anti-de Sitter branch is the Stelle-West connection of -V. It is a sign in the formal statement and is listed for Leon with the proposed text, not applied. (2) Optional language finding applied: the formal setup now defines the Ricci, scalar, Einstein and Schouten maps and J in GA and the Lorentz block as the operator F(B) = calR(B) - (Lambda/3) B, with the index definitions kept as the component reading (notation only; the proof computes with exactly these maps, E(a) = 2 d_b ^ F(I(a ^ b)) = 2(G(a) + Lambda a) I). (3) Six stale pins repinned after review: dark-energy.frozen-point-makes-stelle-west-vector 5 -> 6 (formal unchanged; (ii) and (iii) as cited), series-wald-entropy-changes-without-flux-on-local-horizons 2 -> 3 (formal unchanged), positive-structure-and-natural-scale-actions-do-not-select-the-almost-einstein-scale 2 -> 3 (decided restatement A3: the sign of sqrt|g| calR = 6 phi Box phi and of the Euler-Lagrange equation in (ii); this result cites only the trace calR = 4 Lambda of (ii), which is unchanged, so the use holds), einstein-condition-is-infinity-vacuum-incidence 3 -> 4 (the unit I_7 named; clause (7) as quoted), infinity-vacuum-incidence-is-a-property-of-the-scale 3 -> 4 (GA rewrite; the quoted component form of (4) is still its reading), synthesis.imported-gtg-dictionary 1 -> 2 (component sign of (iv) stated; the store-sign definitions used hold). No check changed. Version kept at 3.'
  maintainer_pass_gtg_proof:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Proof of (i) to (iii) rewritten in GTG: the frame equation as the trivector-valued function E(a) = 2 d_b ^ F(I(a ^ b)) of the curvature operator F = calR - (Lambda/3) id, with the GA identities d_b ^ calR(I(a ^ b)) = calG(a) I (Weyl part by W(IB) = I W(B) and trace-freeness, Kulkarni-Nomizu part on the ten basis symmetric maps) and d_b ^ (I(a ^ b)) = -3 a I, so E(a) = 2(calG(a) + Lambda a) I; rank 10 because E factors through the Einstein map; the dilation trace d_a ^ E(a) = 2(4 Lambda - calR) I. (iv) and the Reading unchanged; the three-form and index computation kept as a labelled reading. Checked exactly: check_gtg_frame_trivector_is_twice_dual_einstein_plus_lambda (identity operator; the ten Kulkarni-Nomizu operators; Weyl duality and d_b ^ W(I(a ^ b)) = 0 on the Weyl operators of Schwarzschild, Kasner and a non-vacuum synchronous gauge field; the component three-form of the Fact equals 2 d_b ^ F(I(a ^ b)) and 2(G + Lambda) I on the three sample curvatures at three Lambda) and check_gtg_frame_equation_on_gauge_fields_and_dilation_trace (de Sitter gauge field: E = 0 at its Lambda, not at Lambda + 1; rank 10 on the Ricci part; d_a ^ E(a) = 2(4 Lambda - calR) I on FLRW and Schwarzschild gauge fields). Version kept at 3 (already above the lock in this run). outside_ga removed: the formal is GA-primary with the components as labelled readings, and the proof and rank count are now in GA.'
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Declared outside_ga (other) and left in its language: The result is stated and proved in the MacDowell-Mansouri curvature components F_{abcd} = R_{abcd} - (Lambda/3)(g_ac g_bd - g_ad g_bc), the four-forms epsilon_{abcd} e^b ^ F^{cd} and the tractor slots; the GTG operator F(B) = -(R(B) - B/l^2) is their reading (dictionary row 13), and the rank counts are made on the components.'
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The convention line said Riemann positive on spheres in signature (1,3), but F_abcd = R_abcd - (Lambda/3)(gg - gg) vanishing on de Sitter, the vacuum Ric = Lambda g, Sch = (Lambda/6) g and clause (7) all need the store sign (R_abcd minus the round-sphere-positive components); checked exactly on de Sitter (v/r03_checks.py); identity (i) itself holds in either sign.'
  open_problem: op.scale-selection-principle
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Uses edge added to the new imported Fact synthesis.imported-einstein-cartan-matter-coupling, which proof (iv) now cites for the matter coupling in place of the citation from memory; content unchanged. Version 1 -> 2.'
  note: >-
    Answers the restated problem's first alternative only given an imported action principle, that is, with
    Einstein's equations adopted as a variational premise; a principle derived from the series' objects remains
    open, and the result is transport-absent. The principle is already in the store, from the
    dark-energy part of the series: the MacDowell-Mansouri functional in its frozen-point form (the frozen
    point supplies the reduction to the de Sitter group and the prefactor, the canonical tractor the
    Stelle-West slot). Its field space is the whole pair (hb, Omega). The frame variation is exactly twice the
    dual of G(a) + Lambda a, rank ten on the curvature at a point with kernel the Weyl tensors, so the nine
    trace-free conditions are imposed; restricted to pure dilations of the frame it is the single Yamabe trace,
    which is the stored scale-only no-go read as the same functional with the conformal class frozen. With a
    matter functional the field equations are clause (7) of the incidence theorem and the on-shell Schouten
    tensor reproduces the stored derivative of the scale tractor; in vacuum the Schouten slot is Lambda g/6,
    that of the Stelle-West Cartan connection, so the scale tractor is parallel. The functional is imported
    (MacDowell-Mansouri 1977, Stelle-West 1980) and the result is transport-absent; the matter coupling of the
    Einstein-Cartan functional is cited from memory (Kibble 1961; Sciama 1964; Hehl, von der Heyde, Kerlick
    and Nester 1976; Lasenby, Doran and Gull 1998 for Gauge Theory Gravity). Comparison with the Clausius
    route: same field equations, different entropy, since the Wald entropy of this action carries the Euler
    term that (Loc) excludes. Cross-subject: the principle comes from the dark-energy and frozen-point results,
    not from the Einstein-route claims the problem lists.
---

## formal
Units $c = 1$, signature $(1,3)$ (store), the store's curvature sign (the components $R_{abcd}$ are minus those of the round-sphere-positive Riemann tensor, so that de Sitter space has $\Ric = \Lambda g$ and $F_{abcd} = 0$), read from the field strength of a gravitational field $(\hb, \Omega)$ on flat spacetime with derived metric $g$ (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}); the Ricci map $\Ric(b) = \partial_{a}\cdot\mathcal{R}(a\wedge b)$ and scalar $\mathcal{R} = \partial_{a}\cdot\Ric(a)$, the Einstein map $\mathcal{G}(a) = \Ric(a) - \tfrac12 a\,\mathcal{R}$, the Schouten map $\Sch(a) = \tfrac12(\Ric(a) - \tfrac{\mathcal{R}}{6}a)$ and $J = \partial_{a}\cdot\Sch(a)$ (Fact \claimref{synthesis.imported-gtg-dictionary}; in components $\Ric_{bd} = g^{ac}R_{abcd}$, $\mathcal{R} = g^{bd}\Ric_{bd}$, $\Sch = \tfrac12(\Ric - \tfrac{\mathcal{R}}{6}g)$, $J = g^{ab}\Sch_{ab}$). Let $\Lambda \neq 0$, and let $S_{\mathrm{MM}}$ be the series' MacDowell-Mansouri functional of the de Sitter (anti-de Sitter) connection $A(a) = \Omega(a) - \tfrac{\Lambda}{3}\,\hb^{-1}(a)\wedge V$ (that is $\Omega(a) + \hb^{-1}(a)\wedge V/Q(V)$, so that $D_{a}V = \hb^{-1}(a)$ on both branches) (Fact \claimref{dark-energy.imported-macdowell-mansouri-theorem-stelle-west}), in the frozen-point presentation $S \sim Q(I)^{-1}\int\epsilon(I, V, F, F)$ of Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector}(iii), whose field space is the whole pair $(\hb, \Omega)$ with $Q(I) = \Lambda/3$ and $Q(V) = -3/\Lambda$ fixed. Its Lorentz block is the operator $F(B) = \mathcal{R}(B) - \tfrac{\Lambda}{3}B$ on bivectors (in components $F_{abcd} = R_{abcd} - \tfrac{\Lambda}{3}(g_{ac}g_{bd} - g_{ad}g_{bc})$), as in Theorem \claimref{synthesis.series-wald-entropy-changes-without-flux-on-local-horizons}. At a point, with an orthonormal frame $e_{a}$ of $g$, reciprocal frame $e^{a}$, pseudoscalar $I = e_{0}e_{1}e_{2}e_{3}$, $\epsilon_{abcd}$ defined by $e_{a}\wedge e_{b}\wedge e_{c}\wedge e_{d} = \epsilon_{abcd}\,I$ and $F^{cd} = \tfrac12 F^{cd}{}_{ef}\,e^{e}\wedge e^{f}$:
\begin{enumerate}
\item[(i)] \emph{(The frame equation; proved.)} The variation of $S_{\mathrm{MM}}$ with respect to the frame $\hb^{-1}$ is the trivector-valued linear function $E(a) = 2\big(\mathcal{G}(a) + \Lambda a\big)I$. In components (a labelled reading), the three-form of the Fact's second Euler-Lagrange equation is
\[
E_{a} := \epsilon_{abcd}\,e^{b}\wedge F^{cd} = 2\,\big(\mathcal{G}(e_{a}) + \Lambda e_{a}\big)\,I .
\]
\item[(ii)] \emph{(Ten conditions; proved.)} As a linear map on the twenty-dimensional space of algebraic curvature tensors at a point, $R \mapsto (E_{a})$ has rank $10$ and kernel exactly the Weyl tensors: it is injective on the Ricci part, and the nine trace-free components of $\Ric$ enter as nine independent conditions. In particular a vacuum stationary point has $\Ric = \Lambda g$: the trace-free part vanishes.
\item[(iii)] \emph{(Restricted to dilations: the one equation of the scale-only no-go; proved.)} If the frame is varied only by pure dilations, $\delta\hb^{-1}(a) = \delta w\,\hb^{-1}(a)$ at fixed conformal class, the frame equation is contracted with the frame: $e^{a}\wedge E_{a} = 2(4\Lambda - \mathcal{R})\,I$, a map of rank $1$ on the curvature, the single trace equation $\mathcal{R} = 4\Lambda$ (the Yamabe equation of Theorem \claimref{synthesis.positive-structure-and-natural-scale-actions-do-not-select-the-almost-einstein-scale}(ii)). The one equation of every scale-only principle and the ten of this one come from the same functional; the nine trace-free conditions are supplied exactly by varying the conformal class.
\item[(iv)] \emph{(With matter; the algebra proved, the coupling standard.)} Add a matter functional $S_{m}[\hb, \psi]$ whose frame variation defines $T$, with $S_{\mathrm{MM}}$ normalised so that the frame equation reads $\mathcal{G}(a) + \Lambda a + 8\pi G\,T(a) = 0$ ($G$ the normalisation constant of the functional, a free constant, as $1/(4\eta)$ is on the Clausius route). This is exactly clause (7) of Theorem \claimref{synthesis.einstein-condition-is-infinity-vacuum-incidence}, $\Ric + 8\pi G\,T = (\Lambda + 4\pi G\,\tau)\,g$, $\tau = g^{ab}T_{ab}$. On shell
\[
\Sch = \tfrac{\Lambda}{6}\,g - 4\pi G\,\big(T - \tfrac{\tau}{3}\,g\big), \qquad \Sch^{\circ} = -4\pi G\,T^{\circ}, \qquad \Lambda = 6\cdot\tfrac{J}{4} - 2\pi G\,\tau ,
\]
which is the content of $\nabla_{a}I' = 4\pi G\,(0, T^{\circ}_{ab}, \tfrac{1}{12}\nabla_{a}\tau)$ with $\rho_{I'} = J/4$ in Theorem \claimref{synthesis.infinity-vacuum-incidence-is-a-property-of-the-scale}(4). In vacuum $\Sch = \tfrac{\Lambda}{6}g$, the Schouten slot of the Stelle-West Cartan connection, so the scale tractor $I'$ is parallel: the own-ray incidence of the infinity vacua (Theorem \claimref{synthesis.einstein-condition-is-infinity-vacuum-incidence}) is the vacuum case of the field equations of $S_{\mathrm{MM}} + S_{m}$, and with matter the stored derivative of the scale tractor is a law, because $T$ is given by $S_{m}$ independently of the vacuum field.
\end{enumerate}
\emph{Reading.} $S_{\mathrm{MM}}$ is a dynamical principle for the whole gauge field, not for the scale within a fixed conformal class: its field space is every pair $(\hb, \Omega)$, its field equations are second-order equations with an independently given source, and its zero set is not the parallel-tractor condition, so it is not a rewording of that condition. It is imported (MacDowell-Mansouri, Stelle-West), and the series supplies only its frozen-point presentation, in which the frozen point enters as the constant prefactor $1/Q(I) = 3/\Lambda$; adopting it is adopting Einstein's equations as a variational premise. So it answers the question of a principle for the whole gauge field only given that imported action principle: transport-absent, and a principle derived from the series' objects, from which the incidence would follow rather than being assumed in variational form, remains open. The Stelle-West field $V$ here is a variable of the action ($Q(V) = -3/\Lambda$, $\ip{V}{I} = 0$), not a selected point. Compared with the Clausius route of Theorem \claimref{synthesis.einstein-equations-from-c-loc-and-clausius}, the two principles give the same field equations (the Euler term of $S_{\mathrm{MM}}$ is topological in four dimensions), with $\Lambda$ a parameter of the functional here and an integration constant there, and they differ in the entropy: the Wald entropy of $S_{\mathrm{MM}}$ on a local edge carries the Euler density $-\tfrac{3}{4\Lambda}$ times the Cartan curvature of the edge plane, which the clause (Loc) excludes (Theorem \claimref{synthesis.series-wald-entropy-changes-without-flux-on-local-horizons}). The statements hold for $\Lambda \neq 0$; at $\Lambda = 0$ the curvature-squared presentation has a pole and the functional is the Einstein-Cartan limit of Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector}, with the same frame equation at $\Lambda = 0$. With spinning matter the torsion equation of the Fact is sourced by the spin density and its contact term enters $T$; the trace-free count of (ii) is unchanged.

## technical
The open problem asks for a principle of the series for the whole gravitational gauge field, not for the scale inside a fixed conformal class, whose field equations fix the trace-free part of the curvature, so that the Einstein condition (the own-ray incidence of the infinity vacua, equivalently a parallel scale tractor) follows rather than being restated. Given an imported action principle, the store already contains one, in the dark-energy part of the series: the MacDowell-Mansouri functional (MacDowell-Mansouri, Stelle-West), the square of the de Sitter curvature seen from the frozen point, with the Stelle-West vector built from the frozen point and the canonical tractor. It varies $\hb$ and $\Omega$ together.

The frame variation of that functional, as a three-form, is exactly twice the dual of $\mathcal{G}(a) + \Lambda a$. As a linear map of the curvature at a point it has rank ten and kernel the Weyl tensors, so it imposes the nine trace-free conditions and the trace. Restricting the variation to pure dilations of the frame contracts it with the frame and leaves only the trace, the Yamabe equation: the stored no-go for scale-only principles is this same functional with the conformal class frozen, and the missing nine conditions are exactly what varying the class supplies. With a matter functional the field equations are the store's clause (7), and on shell the Schouten tensor is $\tfrac{\Lambda}{6}g - 4\pi G(T - \tfrac{\tau}{3}g)$, which is the stored formula for the derivative of the scale tractor; in vacuum it is the Schouten slot of the Stelle-West connection, so the scale tractor is parallel. The principle is imported, with the standard Einstein-Cartan matter coupling, and transport-absent: adopting it adopts Einstein's equations as a variational premise, so a principle derived from the series' objects remains open. It agrees with the Clausius route on the field equations and disagrees on the entropy, since its Wald entropy carries the Euler term that (Loc) excludes. The algebra is checked exactly in $\Cl(1,3)$ on fixed rational curvature tensors and on a spanning set of the curvature space.

## lay
Einstein's equations say how matter bends spacetime, and ten numbers per point must match. Earlier work showed that any rule which only adjusts the overall size of rulers, keeping the light cones fixed, yields just one of the ten. This result points out that the series already holds, borrowed from the literature, a rule that adjusts everything: the MacDowell-Mansouri action, which the series writes as the square of the curvature seen from its frozen point. Varying it gives all ten equations, with matter entering as an independent source, and when matter is absent it reproduces exactly the series' geometric statement of Einstein's condition. Freezing the light cones in this same action leaves only the one equation found before. The action is taken from the literature rather than derived from the series' transport, and it disagrees with the series' entropy premise about one geometric term in horizon entropy.

## one-liner
The imported MacDowell-Mansouri functional, in the series' frozen-point form $S \sim Q(I)^{-1}\int\epsilon(I, V, F, F)$, varies the whole field $(\hb, \Omega)$; its frame equation is $E(a) = 2(\mathcal{G}(a) + \Lambda a)I$ (components: $\epsilon_{abcd}e^{b}\wedge F^{cd}$), rank $10$ on the curvature with kernel the Weyl part, so it fixes the trace-free part, while its restriction to pure dilations is the single Yamabe trace of the scale-only no-go; with the standard (imported) Einstein-Cartan matter coupling and an independent source it gives clause (7), on shell $\Sch = \tfrac{\Lambda}{6}g - 4\pi G(T - \tfrac{\tau}{3}g)$, the stored derivative of the scale tractor, and in vacuum the infinity-vacuum incidence. It settles the search for such a principle only given this imported action principle (Einstein's equations as a variational premise); transport-absent, and its Wald entropy carries the Euler term that (Loc) excludes.
