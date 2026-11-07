---
id: synthesis.clausius-on-the-action-shell-ties-entropy-density-to-period
kind: claim
version: 1
title: 'On the action shell, Clausius ties entropy density to the period'
status: proved
region: synthesis
subject: einstein
tags: [thermal-premises, horizons, curvature-and-field-equations, no-go, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-01-five-fronts
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
  - synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part@3
  - synthesis.imported-einstein-cartan-matter-coupling@1
  - synthesis.r-loc-independent-sets-matter-coupling@5
  - synthesis.einstein-equations-from-c-loc-and-clausius@8
  - synthesis.integrated-loc-curvature-clause-forced-matter-clause-independent@1
  - synthesis.loc-independent-of-clausius-and-killing-data@4
  - synthesis.local-normality-at-the-edge-gives-the-null-ground-state@4
  - synthesis.euler-entropy-of-a-horizon-patch-is-an-edge-term@3
  - synthesis.imported-gtg-dictionary@2
  - synthesis.imported-jacobson-clausius-1995@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_clausius_on_the_action_shell_is_eta_equals_c_over_4g
- kind: check
  ref: check.py::check_null_cone_values_fix_the_stress_up_to_the_metric
- kind: check
  ref: check.py::check_stored_witness_is_on_the_shell_of_a_different_coupling
- kind: check
  ref: check.py::check_period_factor_is_fixed_only_where_matter_crosses
- kind: check
  ref: check.py::check_vacuum_weyl_field_leaves_the_relation_empty
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.integrated-loc-curvature-clause-forced-matter-clause-independent
  - synthesis.r-loc-independent-sets-matter-coupling
  - synthesis.field-space-premise-parallel-frozen-point
extraction:
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: synthesis.imported-gtg-dictionary repinned 1 -> 2 after reviewing its correction of the component reading in clause (iv) to R(g_mu ^ g_nu) = -R(e_mu ^ e_nu), agreeing with the store''s sign R(B) = -R(hb(B)) the clause already stated, with GA wording in (ii) and (iv); the translation rules are unchanged; the use here holds as cited.'
  open_problem: op.derive-loc-and-r-loc
  note: >-
    Reads the two independence results of the thermal route against the gravitational action now in
    the store. The store holds both routes to the field equations: the Clausius route (premise
    (C_loc), the Clausius hypothesis (H1) and (H2) to (H4)) and the field-space action (postulate
    (FS) with the imported MacDowell-Mansouri functional and the imported Einstein-Cartan matter
    coupling, one normalisation G). Each independence model of the thermal route (a matter-dependent
    density, a rapidity period 2 pi c off Killing horizons) produces a field equation with a coupling
    other than G at the points where matter crosses, so on the joint premise set it fails there; the
    Clausius relation becomes one relation, eta = c/(4G), between the two thermal data. Hence on the
    joint set the one-coupling clause of (Loc) follows from the period (and the period from (Loc))
    wherever matter crosses, and the relation is empty on matter-free regions, where (R_loc)'s period
    stays independent. This is a premise exchange, not a derivation from transport: the single
    coupling of the action is the content the clause supplied, and on the joint set the Clausius
    relation is a constraint on thermal data rather than a derivation of Einstein's equations.
    The relation eta = c/(4G) is Jacobson's 1995 identification of the area density with 1/(4G),
    at period 2 pi c and read in reverse (Fact synthesis.imported-jacobson-clausius-1995, through the
    stored pencil identity); the new content is its use to break the store's two independence models
    where matter crosses. The postulate (FS) enters as part of the stated hypothesis (A), not as a
    premise edge. Transport-absent. No literature is cited from memory.
---

## formal
Units $\hbar = 1$ and the speed of light one, signature $(1,3)$, the store's curvature sign, $t = 2\pi T$ for a stress tensor $T$ and $\tau$ its trace. Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) with zero torsion. The joint premise set is: (A) the field equations of the gravitational action on the field space of Postulate \claimref{synthesis.field-space-premise-parallel-frozen-point} with the Einstein-Cartan matter coupling (Fact \claimref{synthesis.imported-einstein-cartan-matter-coupling}), $\mathcal{G}(a) + \Lambda a + 8\pi G\,T(a) = 0$ with one normalisation $G$ for every admissible field and $\Lambda \neq 0$, the range in which that theorem states the functional (Theorem \claimref{synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part}(iv)); (A) is a hypothesis of this result, not a premise it derives; (B) the Clausius hypothesis (H1) with (H2) to (H4) of Theorem \claimref{synthesis.einstein-equations-from-c-loc-and-clausius} on every local patch through every point $p$, at the local temperature of rapidity period $2\pi c(p)$ ($c = 1$ is (R$_{\mathrm{loc}}$); $c \neq 1$ as in Theorem \claimref{synthesis.r-loc-independent-sets-matter-coupling}), with $\delta S = \eta\,\delta A$, $\eta$ constant along each field (Theorem \claimref{synthesis.einstein-equations-from-c-loc-and-clausius}(6)). Call $p$ matter-crossed if $T$ at $p$ is not a multiple of the metric.
\begin{enumerate}
\item[(i)] \emph{(The relation; proved.)} A symmetric $t$ with $t(k,k) = 0$ for every null $k$ ($Q(k) = 0$) is a multiple of the metric. Under (A) the Clausius defect on the pencil about $k$ at $p$ is $t(k,k)\,(1 - 4G\eta/c)$ for every null $k$, whatever the Weyl part. So at a matter-crossed point the Clausius relation holds on every patch through $p$ if and only if $\eta = c(p)/(4G)$ (at $c = 1$ this is Jacobson's identification $G = 1/(4\eta)$, Fact \claimref{synthesis.imported-jacobson-clausius-1995}, read with $G$ given by (A)), and at a point where $T$ is a multiple of the metric it holds for every $\eta$ and $c$.
\item[(ii)] \emph{(The one-coupling clause from the period; proved.)} If $c = 1$ at a matter-crossed point of an admissible field (for example, at leading order, where its modes are locally normal to the null vacuum: the local form of (N$_{+}$) there, Theorem \claimref{synthesis.local-normality-at-the-edge-gives-the-null-ground-state}, gives (R$_{\mathrm{loc}}$)'s period at leading order), then $\eta = 1/(4G)$ on that whole field: on the joint set every admissible field carrying matter has the same density, and a density that depends on the matter fails the joint set at such a point. The witness of the clause's independence in Theorem \claimref{synthesis.integrated-loc-curvature-clause-forced-matter-clause-independent}, the Einstein static universe of radius $2$ with dust $t = \tfrac14$ and $\eta = \tfrac12$, solves (A) only with $G = \tfrac12$; at $G = 1$ its spatial equations force $\Lambda = \tfrac14$ for every dust density and the radius-$2$ universe then carries $t = \tfrac18$ with $\eta = \tfrac14$. If moreover the density is a continuous function of local data as in (i) of that theorem, a flat dust Friedmann field with $\Lambda > 0$ (matter-crossed and asymptotically de Sitter) has $\eta = \tfrac14$, so $G = 1$ in the Planck units of the calibration: the action's free normalisation is the calibrated one.
\item[(iii)] \emph{(The period from (Loc), given the calibration; proved.)} If $\eta = \tfrac14$ and $G = 1$, the calibration with the action's $G$ in the same units taken as an independent input, then $c = 1$ at every matter-crossed point: the model of Theorem \claimref{synthesis.r-loc-independent-sets-matter-coupling}(i), which keeps $\eta = \tfrac14$, fails the joint set wherever matter crosses its region $U$. Without that input the joint set fixes only $\eta/c = 1/(4G)$: a period model with $\eta = c/(4G)$ satisfies it at matter-crossed points where $c$ is constant. So the converse of (ii) needs the calibration; (ii) itself does not.
\item[(iv)] \emph{(Matter-free regions; proved.)} Where $T$ is a multiple of the metric, in vacuum with $\Lambda \neq 0$ and with any Weyl part, the Clausius relation holds at leading order for every $\eta$ and $c$. So the period model with $U$ in a matter-free region off every Killing horizon (the region between the horizons of a Schwarzschild-de Sitter hole, away from both, a solution of (A)) satisfies the joint set, and (R$_{\mathrm{loc}}$)'s period there remains independent of it; and the joint set fixes no value of $\eta$ on a field with no matter-crossed point.
\end{enumerate}
\emph{Reading.} On the joint set the Clausius relation does not derive the field equations, which the action supplies; it is one relation, $\eta = c/(4G)$, between the entropy density and the local period factor. The two independent thermal data of the Clausius route, (Loc)'s one coupling and (R$_{\mathrm{loc}}$)'s period, become one independent datum wherever matter crosses: either gives the other. What supplies the one coupling is the single normalisation of the action, so the clause has been moved into (A), not derived from transport. At $c = 1$ the value $1/(4G)$ is the density of the Einstein-Hilbert part of the action's Wald entropy, whose Euler part changes no entropy difference on open patches with the edge term of Theorem \claimref{synthesis.euler-entropy-of-a-horizon-patch-is-an-edge-term}: at matter-crossed points (ii) is that agreement, obtained from the Clausius relation and not assumed. The stored independence of the one-coupling clause (Theorem \claimref{synthesis.integrated-loc-curvature-clause-forced-matter-clause-independent}) and of the period (Theorem \claimref{synthesis.r-loc-independent-sets-matter-coupling}) hold relative to the thermal premises; this result does not change them there. The gap that (iv) leaves, the period at matter-free points, would close if a state condition that excludes the period model were imposed at every point of every generator: the period-$2\pi c$ state fails the generator analogue of the Hadamard condition and local normality at the patch edge (the microlocal result \claimref{synthesis.microlocal-condition-on-a-generator-gives-the-local-null-ground-state}), and the closed-generator normality result (\claimref{synthesis.normality-on-the-closed-generator-gives-the-vacuum-folium-not-the-ground-state}) excludes it too; either, imposed at every point, would be a new premise, not a derivation. Imposed at matter-crossed points, the microlocal condition gives $c = 1$ there at leading order, and then (ii) gives $\eta = 1/(4G)$ on every field that carries matter.

## technical
The store reaches Einstein's equations by two routes and keeps both: the Clausius route, which needs the entropy clause (Loc) and the temperature clause (R$_{\mathrm{loc}}$) on local horizons, and the gravitational action on the field space of the frozen-point postulate, whose normalisation $G$ is a free constant. On the Clausius route alone two independence results are stored: a density that depends on the matter can be $\tfrac14$ on every Einstein field at the calibrated coupling and $\tfrac12$ on an Einstein static universe where the Clausius relation still holds, now with coupling $\tfrac12$; and a rapidity period $2\pi c$ on local horizons off Killing horizons gives Einstein's equations with coupling $c/(4\eta)$.

Both models change the coupling of matter at the points where matter crosses. With the action's field equation at coupling $G$, the Ricci part on a null direction is $-4G\,t(k,k)$ in the store's sign, so the Clausius defect at period $2\pi c$, $t(k,k) + (\eta/c)\,k \cdot \mathcal{R}(k)$, is $t(k,k)(1 - 4G\eta/c)$. A stress that is not a multiple of the metric has $t(k,k) \neq 0$ for some null $k$ (the null-cone values have rank $9$ on the ten symmetric maps), so there the relation is $\eta = c/(4G)$. Given the period ($c = 1$), the density is $1/(4G)$ on every field that carries matter; given (Loc) with the calibration ($\eta = \tfrac14$, $G = 1$, an independent input identifying the action's $G$ with the calibration's), the period is $2\pi$ wherever matter crosses. The relation itself is Jacobson's identification of the area density with $1/(4G)$, read in reverse with $G$ supplied by the action; what is new is its use against the two stored independence models. The stored one-coupling witness is a solution of the action only at $G = \tfrac12$. Where the stress is a multiple of the metric both sides of the Clausius relation vanish at leading order, so nothing is fixed there, and the period model placed in a vacuum region (between the horizons of a Schwarzschild-de Sitter hole) survives. The action is stated for $\Lambda \neq 0$, so the vacuum examples carry a cosmological constant.

What this does and does not settle. It answers the problem's first attack line on the joint set: the one-coupling clause follows from the period and the action, and a matter-dependent density is not a model of all present premises once the action is among them. It does not derive the clause from transport, since the action's one coupling carries the same content, and it says nothing on fields with no matter (the curvature clause off calibrated paths there is untouched) or about local normality at the edge, which is a premise on the state, not on the coupling.

## lay
The series has two ways of getting Einstein's equations for gravity. One borrows a standard action principle with a single strength of gravity. The other uses horizon thermodynamics: entropy proportional to area, a temperature set by acceleration, and heat flowing in as energy crosses a horizon. On the thermodynamic route alone, two ingredients were known to be independent assumptions: that the entropy per unit area does not depend on what matter is present, and the exact temperature of small horizons. This result asks what happens when both routes are kept, as the series now does. Wherever matter crosses a horizon, the heat balance then becomes a single equation tying the entropy per area to the temperature factor and the strength of gravity. Once the entropy per area is fixed at its standard value in the same units as the strength of gravity, either assumption gives the other there, and the known counterexamples stop working. The core equation is Jacobson's 1995 link between horizon entropy and the strength of gravity. In empty regions the equation says nothing, and the temperature remains a separate assumption there.

## one-liner
With the field-space action's equations at one coupling $G$ and $\Lambda \neq 0$, the Clausius defect at period $2\pi c$ is $t(k,k)(1 - 4G\eta/c)$, so where the stress is not a multiple of the metric the relation is $\eta = c/(4G)$, Jacobson's identification at period $2\pi c$: the period gives (Loc)'s one coupling there, and, given the calibration $\eta = \tfrac14$ at $G = 1$ as an independent input, (Loc) gives the period; the stored independence witnesses (Einstein static universe at $G = \tfrac12$; period $2\pi c$ at $\eta = \tfrac14$) fail there given the other datum, and in vacuum the relation is empty; a premise exchange through the action's single coupling, transport-absent.
