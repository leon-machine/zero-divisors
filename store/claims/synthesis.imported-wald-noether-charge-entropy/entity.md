---
id: synthesis.imported-wald-noether-charge-entropy
kind: claim
version: 3
title: 'Imported: Wald''s Noether-charge entropy and its Jacobson-Myers form for a Gauss-Bonnet term'
status: imported
region: synthesis
subject: entropy
tags: [horizons, curvature-and-field-equations, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-10-22
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
imported_from:
- citation: 'R. M. Wald, Black hole entropy is Noether charge, Phys. Rev. D 48 (1993), R3427--R3431.'
  key: Wald1993
  doi: 10.1103/PhysRevD.48.R3427
- citation: 'V. Iyer and R. M. Wald, Some properties of Noether charge and a proposal for dynamical black hole entropy, Phys. Rev. D 50 (1994), 846--864.'
  key: IyerWald1994
  doi: 10.1103/PhysRevD.50.846
- citation: 'T. Jacobson and R. C. Myers, Black hole entropy and higher curvature interactions, Phys. Rev. Lett. 70 (1993), 3684--3687.'
  key: JacobsonMyers1993
  locator: 'Eq. (4)'
  doi: 10.1103/PhysRevLett.70.3684
- citation: 'T. Jacobson, G. Kang and R. C. Myers, On black hole entropy, Phys. Rev. D 49 (1994), 6587--6598.'
  key: JacobsonKangMyers1994
  doi: 10.1103/PhysRevD.49.6587
extraction:
  maintainer_pass_gtg_l0:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'n-dimensional reading completed by the lead: the flat background of dimension n is the d-dimensional clause of the definition (version 2), so the Lagrangian, the binormal and the Noether charge are read on a gravitational field on flat R^{1,n-1}; content unchanged.'
  note: >-
    Imported for the horizon-entropy results that read entropy off the series' action (the Euler
    term's shift, its Schwarzschild-de Sitter consequence, and the black-hole data that do not fix
    the field equations). Bibliographic data checked against the arXiv and publisher listings on
    2026-10-22. Clause (a) agrees with the abstract of Wald 1993; clause (c) agrees with Eq. (4) of
    Jacobson-Myers (S = sum over m of 4 pi m c_m times the integral over the bifurcation surface of
    the Lovelock density L_{m-1} of the induced metric, with c_1 = 1/16 pi G), whose m = 2 term
    gives the stated functional. The explicit form of clause (b), with its sign and binormal
    normalisation, is cited from memory, not checked against the source. Whether the Wald entropy is
    the entropy of a horizon outside the setting of clause (a), for instance a cosmological horizon,
    is not part of this Fact: results that use it for such horizons say so as their hypothesis (W).
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Created by the maintainer pass so that the results citing Wald''s entropy and the Jacobson-Myers functional from memory can pin it; partly verified (see note).'
  maintainer_pass_gtg:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity per Leon 2026-10-23 (DICTIONARY, Bifurcation surfaces): Sigma is a cross-section of the horizon locus in the chart (K = hb^{-1}(xi), (K.D)K = kappa K, null and normal), replacing the bifurcation surface, with the note sentence; the bifurcate Killing horizon stays a hypothesis; the Lagrangian built from the derived metric, the curvature operator and D on a flat background of dimension n; E_4 and R given their GTG readings in clause (c). Clauses (a)-(c) and provenance unchanged. Fix (referee GR1, 2026-10-23): in (c), (2)R is the scalar curvature of the Riemannian metric on Sigma, minus the metric induced by the (+,-,-,-) derived metric, positive on round spheres; this restores the sign of the Jacobson-Myers term used downstream (A/4G - 3 pi/(Lambda G)).'
---

## formal
Let $L = \mathcal{L}\,\epsilon$ be a diffeomorphism-invariant Lagrangian in $n$ dimensions built from the metric, the Riemann tensor and finitely many of its symmetrised covariant derivatives (and matter fields): in Gauge Theory Gravity, on the flat background $\R^{1,n-1}$ of the $n$-dimensional clause of Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}, from the derived metric of a gravitational field $(\hb, \Omega)$, its curvature operator $\mathcal{R}(B)$ and its covariant derivatives $D$. Consider a stationary black hole with a bifurcate Killing horizon, horizon Killing field $\xi$, the physical vector field $K = \hb^{-1}(\xi^{\mu}e_{\mu})$, of surface gravity $\kappa > 0$, $(K \cdot D)K = \kappa K$ on the horizon locus, angular velocity $\Omega_{H}$, and canonical mass $M$ and angular momentum $J$ defined at infinity; let $\Sigma$ be a cross-section of the horizon locus in the chart, on which $K$ is null and normal to the horizon, the boost flow being the flow of $K$, which carries cross-sections to cross-sections.
\begin{enumerate}
\item[(a)] (First law.) For every perturbation to a nearby solution, $\delta M = \frac{\kappa}{2\pi}\,\delta S_{W} + \Omega_{H}\,\delta J$, where $S_{W} = 2\pi\oint_{\Sigma}\mathbf{Q}[\xi/\kappa]$ is $2\pi$ times the Noether charge of the horizon Killing field normalised to unit surface gravity, a local geometric quantity on the horizon.
\item[(b)] (Local formula.) On $\Sigma$, $S_{W} = -2\pi\oint_{\Sigma}E^{abcd}\epsilon_{ab}\epsilon_{cd}\,dA$, with $E^{abcd} = \partial\mathcal{L}/\partial R_{abcd}$, the derivative of the Lagrangian density with respect to the curvature operator in components, and $\epsilon_{ab}$ the binormal of $\Sigma$, the unit bivector of its normal plane, normalised by $\epsilon_{ab}\epsilon^{ab} = -2$; for $\mathcal{L} = R/16\pi G$ it is $A(\Sigma)/4G$.
\item[(c)] (Gauss-Bonnet term.) In four dimensions, for $\mathcal{L} = (R - 2\Lambda + \alpha E_{4})/16\pi G$ with $R$ the scalar curvature ($4\Lambda$ on de Sitter space, $\mathcal{R}$ in the store's sign) and $E_{4} = R_{abcd}R^{abcd} - 4R_{ab}R^{ab} + R^{2} = -2\langle\mathcal{R}(a \wedge b)\,I\,\mathcal{R}(I\partial_b \wedge \partial_a)\rangle$ the Euler density,
\[
S_{W} \;=\; \frac{1}{4G}\oint_{\Sigma}\bigl(1 + 2\alpha\,{}^{(2)}\!R\bigr)\,dA ,
\]
${}^{(2)}\!R$ the scalar curvature of the Riemannian metric on $\Sigma$, minus the metric that the derived metric (signature $(+,-,-,-)$) induces (equivalently, the induced metric in signature $(-,+,+,+)$), so that ${}^{(2)}\!R = 2/r^{2}$ on a round sphere of area $4\pi r^{2}$; $\Sigma$ is a closed surface in the background: the Jacobson-Myers functional, the case $m \le 2$ of their entropy for Lovelock gravity.
\end{enumerate}
\emph{Provenance:} \cite{Wald1993, IyerWald1994, JacobsonMyers1993, JacobsonKangMyers1994}, read in Gauge Theory Gravity through Fact \claimref{synthesis.imported-gtg-dictionary}.

The bifurcation surface itself, where the boost flow has its fixed points, lies beyond one flat chart (it is the meeting of the four regions of the maximal extension); the chart contains the future horizon, on whose cross-sections the area, the surface gravity and the boost flow are those stated.

## technical
For any diffeomorphism-invariant theory of gravity, in Gauge Theory Gravity a theory of the gravitational field on flat spacetime, Wald showed that stationary black holes with a bifurcate Killing horizon obey a first law, $\delta M = (\kappa/2\pi)\,\delta S_{W} + \Omega_{H}\,\delta J$, in which the entropy $S_{W}$ is $2\pi$ times the Noether charge of the horizon Killing field normalised to unit surface gravity. On a cross-section of the horizon locus in the chart it is the integral $-2\pi\oint E^{abcd}\epsilon_{ab}\epsilon_{cd}\,dA$ of the derivative of the Lagrangian density with respect to the curvature operator, contracted with the binormal (the bifurcation surface itself lies beyond one flat chart); for Einstein's Lagrangian it is a quarter of the area in Planck units.

For a Gauss-Bonnet term $\alpha E_{4}$ added to the Einstein-Hilbert Lagrangian in four dimensions, the entropy is the Jacobson-Myers functional $\frac{1}{4G}\oint(1 + 2\alpha\,{}^{(2)}\!R)\,dA$, with ${}^{(2)}\!R$ the intrinsic scalar curvature of the horizon cross-section. The Fact asserts the first law only in the setting stated (asymptotic charges at infinity); calling $S_{W}$ the entropy of other horizons is a further reading.

## lay
For black holes in Einstein's theory, entropy is a quarter of the horizon's area. Wald showed how to read the entropy off any theory of gravity built from the gravitational field and its strength: it is a particular conserved charge on the horizon, and with it the first law of black-hole mechanics holds. For theories that add a certain curvature-squared term to Einstein's, Jacobson and Myers found that the entropy gains a term that depends only on the shape of the horizon's surface. These are standard results taken from the literature.

## one-liner
Wald's entropy, $2\pi$ times the horizon Noether charge, $-2\pi\oint E^{abcd}\epsilon_{ab}\epsilon_{cd}\,dA$ on a cross-section of the horizon locus, obeys the first law of stationary black holes, and for $(R - 2\Lambda + \alpha E_{4})/16\pi G$ it is the Jacobson-Myers functional $\frac{1}{4G}\oint(1 + 2\alpha\,{}^{(2)}\!R)\,dA$.
