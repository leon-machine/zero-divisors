---
id: synthesis.euler-term-horizon-entropy-shift
kind: claim
version: 4
title: 'The Euler term shifts horizon entropy by a topological constant'
status: proved
region: synthesis
subject: entropy
tags: [horizons, curvature-and-field-equations, cosmological-constant, no-go, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-10-22-toe
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
  - dark-energy.imported-macdowell-mansouri-theorem-stelle-west@3
  - dark-energy.frozen-point-makes-stelle-west-vector@5
  - synthesis.imported-gibbons-hawking-entropy@3
  - synthesis.de-sitter-entropy-pi-n-squared@5
  - dark-energy.wall-counterterm@4
  - synthesis.imported-wald-noether-charge-entropy@3
  - synthesis.imported-chern-gauss-bonnet@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_euler_shift
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.de-sitter-entropy-pi-n-squared
  - dark-energy.wall-counterterm
extraction:
  maintainer_pass_2:
    by: maintainer-2026-10-24
    date: '2026-10-24'
    note: 'Gauge Theory Gravity wording pass at Leon''s request (2026-10-24): curved-spacetime and conformally-flat wording restated in terms of the gravitational field on flat spacetime (a nonvanishing gravitational field; the Weyl part of the field strength vanishes, the conformally flat derived metric kept as a reading; global content read on an atlas of flat charts patched by gauge transformations). Wording only; statements, proofs'' arguments and checks unchanged. Version 3 -> 4. Referee fixes to the GTG wording pass (2026-10-24): ''a gravitational field of nonvanishing field strength'' (gauge-independent) in place of ''a nonvanishing gravitational field''; global content read on several charts of flat spacetime, each with its own gravitational field, glued by displacement and rotation gauge transformations (complexified charts for the half-flat manifold, the conformal compactification for a conformal boundary); ''not carried by the store''s one-chart fields'' in place of ''no single gravitational field carries''; equivalence statements weakened where the old text was weaker; remaining curved-spacetime phrases in lay text restated. Wording only.'
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Maintainer pass: the Jacobson-Myers form of the Wald entropy and the Gauss-Bonnet-Chern theorem, cited from memory, are now the imported Facts synthesis.imported-wald-noether-charge-entropy and synthesis.imported-chern-gauss-bonnet, added to uses and cited in the statement, proof and check; (W), that horizon entropy is the Wald entropy, stays the stated reading and the title keeps it. Version 1 -> 2.'
  open_problem: ein.series-action-area-law
  note: >-
    Settles what the series' own action supplies for the area law and isolates what it does not. The area density comes from the Einstein-Cartan term of the MacDowell-Mansouri square; the zero of the de Sitter entropy is a per-horizon additive constant, -3 pi chi/(2 Lambda G), which no first law or Clausius relation between closed cuts of one topology can detect and which only positivity of a count or a topology-changing amplitude can decide. Whether it affects a Clausius relation imposed on small open patches with moving edges, as in Jacobson's local derivation, is open: there its variation is an edge term. Novelty: that the MacDowell-Mansouri action gives the de Sitter horizon zero entropy, and that a Gauss-Bonnet term weights instantons by exp(-c chi), are known in the literature (cited from memory); the content specific to the series is that its own action, reached from the frozen point, carries the term with this coefficient. Filed alongside, synthesis.sds-clausius-fixes-area-constant, which takes the value of the constant from clause (ii) here and keeps the Clausius bookkeeping on the Schwarzschild-de Sitter family. Hypothesis (W) is the reading that horizon entropy is the Wald entropy; that the Wald entropy of a Gauss-Bonnet term is the Jacobson-Myers functional is the imported Fact synthesis.imported-wald-noether-charge-entropy, and the Gauss-Bonnet-Chern theorem used for the topological value is the imported Fact synthesis.imported-chern-gauss-bonnet. The Nariai nucleation rate exp(-pi/(Lambda G)) is R. Bousso and S. W. Hawking, Phys. Rev. D 54 (1996) 6312 (cited from memory); the anti-de Sitter Euler counterterm of R. Aros, M. Contreras, R. Olea, R. Troncoso and J. Zanelli (Phys. Rev. Lett. 84 (2000) 1647, cited from memory) is the Lambda < 0 branch of the same square, where the shift is positive. Transport-absent: the frozen point supplies the action (Theorem dark-energy.frozen-point-makes-stelle-west-vector), nothing else of the transport structure is used.
  flags:
  - 'beyond one flat chart: the closed Euclidean instantons S^4 and S^2 x S^2 (on-shell actions, Euler characteristic, nucleation)'
  maintainer_pass_gtg:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity (MIXED): F named as the Lorentz block of the field strength of the MacDowell-Mansouri gauge field; algebraic curvature tensors as curvature operators R(B); R and E_4 given their GTG readings (store sign; E_4 sign-independent); (W) evaluated on a cross-section of the horizon locus per Leon 2026-10-23 (DICTIONARY, Bifurcation surfaces) with the note sentence; the closed Euclidean instantons S^4 and S^2 x S^2 of (iii) carry the Section 14 flag and a flags entry. Clauses (i)-(iii) unchanged; proof given a pointer.'
---

## formal
Take the gravitational action of the gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) to be the MacDowell-Mansouri functional of Fact \claimref{dark-energy.imported-macdowell-mansouri-theorem-stelle-west}, the Cartan curvature $F$ being the Lorentz block of the field strength of its $SO(1,4)$ (respectively $SO(2,3)$) gauge field, which the series reaches from the frozen point (Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector}(iii)), with $\ell^{2} = 3/|\Lambda|$, the sign of the $\ell^{-2}e\wedge e$ term fixed by requiring the Cartan curvature $F$ to vanish on the de Sitter (respectively anti-de Sitter) model, and the overall constant fixed by normalising its Einstein-Cartan term to the Einstein-Hilbert Lagrangian with Newton constant $G$.
\begin{enumerate}
\item[(i)] \emph{(The coefficient.)} For every algebraic curvature tensor, that is every curvature operator $\mathcal{R}(B)$ on bivectors with the algebraic symmetries, in Lorentzian and in Euclidean signature and on both branches,
\[
\ell^{2}\,\epsilon_{abcd}F^{ab}\wedge F^{cd} \;=\; -4\,s\,\bigl(R - 2\Lambda + \alpha E_{4}\bigr)\,\mathrm{vol}, \qquad \alpha = -\frac{3}{4\Lambda}, \qquad E_{4} = R_{abcd}R^{abcd} - 4R_{ab}R^{ab} + R^{2},
\]
with $s = \operatorname{sign}\Lambda$, $R$ the scalar curvature ($\mathcal{R}$ in the store's sign, $4\Lambda$ on the model) and $E_{4}$ the Euler density, $E_{4} = -2\langle\mathcal{R}(a \wedge b)\,I\,\mathcal{R}(I\partial_b \wedge \partial_a)\rangle$ in either sign. So the series' Lagrangian is $(R - 2\Lambda + \alpha E_{4})/16\pi G$: the Euler density enters with $\alpha = -3/4\Lambda$, negative for $\Lambda > 0$, and $\alpha$ is already fixed by the vanishing of the square on the model.
\item[(ii)] \emph{(The shift, and its invisibility.)} Assume (W): the entropy of a Killing horizon, evaluated on a cross-section $\Sigma$ of the horizon locus in the chart, on which the Killing field $K$ is null and normal to the horizon with $(K \cdot D)K = \kappa K$ (the boost flow is the flow of $K$, which carries cross-sections to cross-sections), is the Wald entropy of this Lagrangian, which by Fact \claimref{synthesis.imported-wald-noether-charge-entropy}(c) is the Jacobson-Myers functional $S[\Sigma] = \frac{1}{4G}\int_{\Sigma}\bigl(1 + 2\alpha\,{}^{(2)}\!R\bigr)\,dA$. Then
\[
S[\Sigma] \;=\; \frac{A(\Sigma)}{4G} \;-\; \frac{3\pi\,\chi(\Sigma)}{2\Lambda G} ,
\]
and the second term is constant on closed cuts of one topology; on an open cut it has zero first variation under deformations that vanish with their gradient at the edge, and in general its variation is an edge term. So every relation that compares the entropy of two closed cuts of one topology (a first law along a family of horizons, Hawking's integral of $dM/T$, a Clausius relation summed over a closed cut) is the same for the series' action as for the Einstein-Hilbert action, and the area density it uses is supplied by the Einstein-Cartan term of the series' own square. For open patches whose deformation does not vanish at the edge, the case of a local Clausius relation on a small patch, the edge term is generally nonzero and its effect is not settled here.
\item[(iii)] \emph{(Where it is visible.)} In units of $\pi/\Lambda G$, with $\Lambda > 0$: the de Sitter horizon has entropy $3$ under Einstein-Hilbert and $0$ under the series' action (the value $\pi N^{2}$ of Proposition \claimref{synthesis.de-sitter-entropy-pi-n-squared} and the zero); the Nariai geometry, with two horizons of area $4\pi/\Lambda$, has $2$ and $-4$; every Schwarzschild-de Sitter black-hole horizon has entropy below $-2$ under the series' action. The on-shell Euclidean actions computed from the curvature of $S^{4}$ and $S^{2}\times S^{2}$ are $-3$ and $-2$ (Einstein-Hilbert) and $0$ and $+4$ (series), minus the horizon sums in each case. Hence the exponent $S_{\mathrm{Nariai}} - S_{\mathrm{dS}}$ of black-hole nucleation in de Sitter space is $-1$ for Einstein-Hilbert and $-4$ for the series' action: the Euler term multiplies the suppression exponent by four. For $\Lambda < 0$ the shift $-3\pi\chi/2\Lambda G$ is positive.
\end{enumerate}

The bifurcation surface itself, where the boost flow has its fixed points, lies beyond one flat chart (it is the meeting of the four regions of the maximal extension); the chart contains the future horizon, on whose cross-sections the area, the surface gravity and the boost flow are those stated.

\emph{Beyond one flat chart.} The closed Euclidean instantons $S^{4}$ and $S^{2}\times S^{2}$ of (iii), whose on-shell actions and Euler characteristics enter the nucleation exponent, are global and are not carried by a single gravitational field $(\hb, \Omega)$ on flat spacetime; the statements above that hold on the invertible region are in GTG, and the closed instantons are read on the manifold assembled from the derived metric's charts.

## technical
The series' gravitational action, for a gravitational field on flat spacetime, is the square of the de Sitter field strength. Expanding it gives the Einstein-Hilbert term, the cosmological term and the Euler (Gauss-Bonnet) density, with coefficient $-3/4\Lambda$ relative to the Einstein-Hilbert term; that coefficient is forced, since the square must vanish on de Sitter space. Assuming that horizon entropy is Wald's Noether-charge entropy, the Euler density adds to every horizon a constant fixed by the topology of its cross-section, $-3\pi\chi/2\Lambda G$, which for a sphere is exactly minus the Gibbons-Hawking entropy of de Sitter space: hence the zero. That constant does not change when a closed horizon cross-section is deformed, so no first law, no Clausius relation between closed cuts and no integral of $dM/T$ can detect it; the area density they use comes from the Einstein-Cartan term of the series' own action. On a small open patch whose edge moves, the extra term contributes an edge term, and whether that matters for a local heat law is left open. The constant is visible only where topology changes: the Euclidean actions confirm the horizon sums, and the rate at which de Sitter space nucleates a pair of black holes, $e^{-\pi/\Lambda G}$ in Einstein's theory, becomes $e^{-4\pi/\Lambda G}$. Every black-hole horizon in de Sitter space gets negative entropy, so if horizon entropy is to be the logarithm of a count, the constant has to be removed. The cross-sections are those of the horizon locus in one flat chart, the bifurcation surface itself lying beyond it; the closed Euclidean instantons are global: no single gravitational field on flat spacetime carries them, so that part is read on several charts of flat spacetime (charts of Euclidean $\R^{4}$), each carrying its own gravitational field, glued on overlaps by displacement and rotation gauge transformations.

## lay
The series writes gravity's action in a compact geometric form. Expanded, that form contains Einstein's usual action plus an extra term that only knows the shape of space in the coarsest, topological sense. Under the standard rule for reading entropy off an action, the extra term subtracts a fixed amount from the entropy of every horizon, which is why the de Sitter horizon comes out with zero entropy. Because the amount never changes when a whole horizon grows or shrinks, every law about the entropy change of a whole horizon works exactly as in Einstein's theory. Whether the same holds for the heat law on tiny patches of horizon, which is how Einstein's equations have been derived from thermodynamics, is not settled here. The extra term shows up only when space changes its topology, for example when empty space spontaneously creates a pair of black holes: the series' action makes that four times less likely in the exponent.

## one-liner
Assuming Wald entropy, the Euler term of the series' MacDowell-Mansouri action (coefficient $-3/4\Lambda$) shifts every horizon by $-3\pi\chi/2\Lambda G$: invisible to every first law or Clausius relation between closed cuts of one topology, it zeroes the de Sitter entropy, makes Schwarzschild-de Sitter horizons negative, and quadruples the Nariai nucleation exponent.
