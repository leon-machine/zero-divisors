---
id: synthesis.r-loc-independent-sets-matter-coupling
kind: claim
version: 3
title: (R$_{\mathrm{loc}}$), with the local-horizon modes labelled by null direction, is independent of the present premises, and what it adds off Killing horizons is the matter coupling; a local rapidity period $2\pi c$ gives Einstein's equations with $G_{\mathrm{cl}} = cG$
status: proved
region: synthesis
subject: einstein
tags: [thermal-premises, horizons, curvature-and-field-equations, modular-theory]
proposed_by:
  kind: ai
  session: 2026-10-23-toe
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
  - synthesis.boundary-mode-premises-finite-models@3
  - synthesis.local-boost-temperature-is-local-regularity@3
  - synthesis.einstein-equations-from-c-loc-and-clausius@7
  - synthesis.c-loc-entropy-clause-curvature-independent-density@3
  - synthesis.quarter-from-temperature@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_local_window_fails_r_loc_only
- kind: check
  ref: check.py::check_clausius_defect_with_temperature_factor
- kind: check
  ref: check.py::check_polarisation_is_a_tensor_equation
- kind: check
  ref: check.py::check_coupling_scales_with_period
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.c-loc-local-horizon-premise
  - synthesis.clausius-route-newton-constant-is-residue
  - synthesis.boundary-mode-premises-finite-models
extraction:
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Independence is relative to the premises present before the postulate synthesis.n-plus-null-ground-state was registered; (N+) implies the continuum form of (R_loc) and fixes c = 1, so with (N+) adopted this result records what c = 1 buys: G_cl = G. Version 1 -> 2.'
  open_problem: op.derive-loc-and-r-loc
  note: >-
    The independence half of the open problem for the temperature clause, by an explicit model. The
    model keeps every Killing-horizon structure of the store as it is, and gives the modes of local
    horizons through points that lie on no Killing horizon the quasi-free Gibbs state at rapidity period
    2 pi c with c != 1, with the modes labelled by null direction (the labelling under which the clause
    is consistent at nonzero weight, filed alongside). A survey of the store's 51 postulates finds none
    other than the local-horizon premise that quantifies over local horizons, diamonds or all points
    (the only other hit, tameness, concerns the degeneration locus), so every other premise holds as in
    the store; (Loc) holds because version 2 of the premise does not tie the entropy to the state of the
    modes, and Indifference holds in its declared, scoped reading. Independence is relative to the present
    premises: the positive-null-energy premise of synthesis.positive-null-energy-gives-r-premises (filed
    alongside) would fix c = 1 and remove it. Jacobson's argument, rerun with the temperature c^{-1} a / 2 pi, returns a tensor equation
    with G_cl = c / (4 eta); with the Schwarzschild calibration eta = 1/4, which uses the Killing
    temperature, G_cl = c G. So the temperature clause off Killing horizons is what makes the coupling of
    matter equal the G of black-hole thermodynamics, and the field-equation route measures only the
    product of the entropy density and the local temperature normalisation. Transport-absent. Imported
    quantum field theory theorems (Bisognano-Wichmann, Unruh) would fix c = 1 for a field theory meeting
    their hypotheses; they are theorems about such theories, not premises of the store, and the model is
    not one.
  maintainer_pass_gtg:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the region U lies in the invertible region of a gravitational field on flat spacetime and meets no Killing horizon locus, exact de Sitter space and generic spacetimes are the de Sitter field and generic fields, and the field equations of (iii) are named as those of the gravitational field in the store''s sign. Model, clauses (i) to (iv) and their strength unchanged; proof given a pointer to the dictionary Fact.'
---

## formal
Units with $\hbar$ and the speed of light equal to one, signature $(1,3)$; write $\mathrm{Ric}^{\circ}$ as in Theorem \claimref{synthesis.einstein-equations-from-c-loc-and-clausius}. Read the premises on finite windows as in Theorem \claimref{synthesis.boundary-mode-premises-finite-models}, and the local-horizon premise (C$_{\mathrm{loc}}$) as its two clauses (Loc) and (R$_{\mathrm{loc}}$), with the modes of a local horizon's patch labelled by its generating null direction. Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}). For $c > 0$ let (R$_{c}$) be (R$_{\mathrm{loc}}$) with the rapidity period $2\pi$ replaced by $2\pi c$ for the local horizons through points of a region $U$, open in the invertible region, that meets no Killing horizon locus.
\begin{enumerate}
\item[(i)] \emph{(Model.)} Keep every Killing-horizon structure of the store as it is (the windows, (P), (R), (L$_E$), (I), (Q), (R$_{\Lambda}$), the counting premises and the identification of horizon and cutoff modes), and give the modes of each local horizon through a point of $U$ the gauge-invariant quasi-free state with occupations $e^{-2\pi c w}/(1 + e^{-2\pi c w})$ at rapidity weight $w$. This state is even, stationary under the boost and under every number-diagonal generator, KMS at rapidity period $2\pi c$, and for $c \ne 1$ it is not KMS at $2\pi$ at any nonzero weight. No premise of the store other than (C$_{\mathrm{loc}}$) constrains the state of local-horizon modes at points of $U$, so the model satisfies every other present premise and (Loc), and violates (R$_{\mathrm{loc}}$) exactly when $c \neq 1$. Hence (R$_{\mathrm{loc}}$), with the labelling above, is independent of the present premises, (Loc) included. The region $U$ must be nonempty: for the exact de Sitter field every local Rindler horizon is, at leading order, a patch of some observer's cosmological horizon, so if (R$_{\Lambda}$) is read for every observer there is no such $U$; generic gravitational fields, and the exterior and interior of a hole away from its horizon, supply one.
\item[(ii)] \emph{(Clausius at the local temperature.)} Under (R$_{c}$), $T_{\chi} = \kappa/(2\pi c)$ in the time of the approximate boost field $\chi$ (Theorem \claimref{synthesis.local-boost-temperature-is-local-regularity}, with the period rescaled), and on a thin pencil about the generator through $p$
\[
\delta Q - T_{\chi}\,\eta\,\delta A \;=\; \frac{\kappa}{2}\Big(T(k,k) - \frac{\eta}{2\pi c}\,\mathrm{Ric}^{\circ}(k,k)\Big)\Big|_{p}\,\lambda_{0}^{2} + O(\lambda_{0}^{3}).
\]
\item[(iii)] \emph{(Field equations.)} With (Loc), the Clausius hypothesis (H1) at the temperature of (ii), and (H2) to (H4) of Theorem \claimref{synthesis.einstein-equations-from-c-loc-and-clausius}, the gravitational field on $U$ satisfies Einstein's equations, $\mathcal{G}(a) + \Lambda a = -8\pi G_{\mathrm{cl}}\,T(a)$ in the store's sign, with $\Lambda$ an integration constant and
\[
G_{\mathrm{cl}} \;=\; \frac{c}{4\eta}.
\]
If the period $2\pi c$ is used also for the local horizons through points of a Killing horizon locus other than the one generated by the Killing generator, the null-null equation along that generator reads $0 = 0$ for every $c$, so the jump of the period at Killing patches obstructs nothing.
\item[(iv)] \emph{(What the clause adds.)} The density of (Loc) is calibrated on the Schwarzschild family with the Killing temperature of (R), $\eta = \tfrac14$ (Theorem \claimref{synthesis.c-loc-entropy-clause-curvature-independent-density}(ii), through Theorem \claimref{synthesis.quarter-from-temperature}), which (R$_{c}$) leaves unchanged. Then $G_{\mathrm{cl}} = cG$: the coupling of matter in the field equations equals the $G$ of black-hole thermodynamics exactly when the local period equals the Killing period, $c = 1$. The field-equation route determines only $\eta/c$, the entropy density per unit of local temperature normalisation.
\end{enumerate}

## technical
The temperature clause of the local-horizon premise asks the modes of every small horizon to be thermal at rapidity period $2\pi$. To see whether the rest of the store already implies it, take a model that keeps everything the store says about Killing horizons (black-hole and de Sitter horizons, their windows and their states) and changes only the local horizons through a region that meets no Killing horizon, where the modes are put in the thermal state at period $2\pi c$. With the modes labelled by null direction, the labelling under which the clause is consistent at nonzero weight, this state is even and stationary, and it is thermal at $2\pi$ only if $c = 1$. A survey of the store's postulates finds that only the local-horizon premise speaks about the state of local-horizon modes, so every other premise holds in the model: the entropy clause (Loc) because its present version does not tie the entropy to the state of the modes, and Indifference in its declared, scoped reading. The temperature clause is therefore independent of the present premises. The region where the period is changed must exist: for the exact de Sitter field every local horizon is a patch of some observer's cosmological horizon, so if (R$_{\Lambda}$) is read for every observer there is none, but generic gravitational fields and black-hole exteriors and interiors away from the horizon supply it. Independence is relative to the present premise set: the positive-null-energy premise filed alongside (synthesis.positive-null-energy-gives-r-premises) would fix the period at $2\pi$ and so imply the clause.

The model is not idle. Rerunning Jacobson's argument at the temperature $\kappa/(2\pi c)$ changes only one coefficient of the leading-order Clausius defect, and polarisation over all null directions still gives a field equation for the gravitational field on flat spacetime, now with $G_{\mathrm{cl}} = c/(4\eta)$. The density $\eta = \tfrac14$ is calibrated with the Killing temperature, which the model keeps, so $G_{\mathrm{cl}} = cG$. Read the other way, the temperature clause, beyond what (R) and (R$_{\Lambda}$) say at Killing horizons, is the statement that matter gravitates with the same $G$ that appears in the area law; the field equations alone measure only the ratio of the entropy density to the local temperature normalisation. At a Killing horizon the clause is not new: its generator has vanishing null-null Ricci and stress components, so the jump of the period there costs nothing.

## lay
The series needs two assumptions about tiny horizons to derive Einstein's equations: their entropy grows with area at a fixed rate, and they are warm at a definite temperature. This result shows the temperature assumption is extra, given the series' present assumptions: one can keep everything else the series says, including everything about black holes and the cosmological horizon, and give the tiny horizons, with their modes labelled by the light-like direction they belong to, a different temperature, and nothing breaks. What changes is the strength of gravity felt by ordinary matter. If tiny horizons were half as warm as assumed, matter would gravitate twice as strongly as the black-hole formulas say. So the temperature assumption is what ties the gravity of everyday matter to the gravity that appears in black-hole entropy.

## one-liner
A model keeping every Killing-horizon structure and putting local-horizon modes, labelled by null direction, at rapidity period $2\pi c$ satisfies every other present premise, so (R$_{\mathrm{loc}}$) with that labelling is independent of the present premises; Jacobson's argument then gives $G_{\mathrm{cl}} = c/(4\eta) = cG$ at the Killing calibration, so off Killing horizons the clause fixes exactly the equality of the matter coupling with the $G$ of black-hole thermodynamics.
