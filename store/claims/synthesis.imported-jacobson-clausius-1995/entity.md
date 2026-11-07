---
id: synthesis.imported-jacobson-clausius-1995
kind: claim
version: 3
title: 'Imported: Einstein''s equation as an equation of state (Jacobson 1995)'
status: imported
region: synthesis
subject: einstein
tags: [curvature-and-field-equations, horizons, hawking-temperature, classical-theorem]
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
- name: Claude Opus 5.5
  role: 'consistency pass, the signature of the displayed tensor equation stated'
  version: 3
  source: maintainer pass 2026-11-07 (consistency)
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: 'T. Jacobson, Thermodynamics of spacetime: the Einstein equation of state, Phys. Rev. Lett. 75 (1995), 1260--1263.'
  key: Jacobson1995
  doi: 10.1103/PhysRevLett.75.1260
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The displayed R_ab - R g_ab/2 + Lambda g_ab = (2 pi/eta) T_ab is the source''s form in signature (-,+,+,+); in (+,-,-,-) with the same round-sphere-positive tensor the Lambda term changes sign; checked exactly on de Sitter (v/r03_checks.py); the store-sign GA form was already right.'
  note: >-
    Imported for the results that map the Clausius route to Einstein's equations onto the store.
    Bibliographic data checked against the arXiv and publisher listings on 2026-10-22. The
    hypotheses and the conclusion as stated (entropy eta times area, Unruh temperature, heat as
    boost-energy flux, local Rindler horizons whose generators have vanishing expansion and shear at
    the point, Raychaudhuri focusing, conservation and the contracted Bianchi identity, Lambda
    undetermined, G = 1/(4 eta)) were checked against the arXiv text, gr-qc/9504004.
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Created by the maintainer pass so that the Clausius-route results can pin Jacobson''s theorem instead of stating it as a hypothesis cited from memory; verified (see note).'
  maintainer_pass_gtg:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: points and null directions are those of the invertible region of a gravitational field on flat spacetime, the local Rindler horizon is read in a normal gauge at the point (hb(x0) = 1, Omega(x0) = 0), the null-null equation is k.T(k) = -(eta/2 pi) k.R(k) with the store-sign curvature operator (R_ab k^a k^b of the source is Ric^o), and Einstein''s equation is G(a) + Lambda a = -(2 pi/eta) T(a) in the store''s sign, the source''s tensor form kept as a reading. Hypotheses and conclusion unchanged.'
---

## formal
Units $\hbar = c = 1$. Let $(\hb, \Omega)$ be a gravitational field on flat spacetime with derived metric $g$ (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}). Suppose that through every point $p$ of its invertible region and for every future physically null direction $k$ at $p$ ($Q(\hb^{-1}(k)) = 0$; components $k^{a}$), the local Rindler horizon (the past horizon of a small spacelike two-surface through $p$ whose null normals $k$ have vanishing expansion and shear at $p$; in a normal gauge at $p$, $\hb(p) = 1$ and $\Omega(p) = 0$, it is at leading order a piece of the null hyperplane through $p$ orthogonal to $k$) satisfies:
\begin{enumerate}
\item[(a)] its temperature is the Unruh temperature $T = a/2\pi$ of the boost flow $\chi^{a}$ of acceleration $a$;
\item[(b)] its entropy is $\eta$ per unit area, $\delta S = \eta\,\delta A$, with $\eta$ one universal constant;
\item[(c)] the Clausius relation $\delta Q = T\,\delta S$ holds, with $\delta Q = \int T_{ab}\chi^{a}\,d\Sigma^{b}$ the boost energy of matter crossing it, and $\delta A$ given by the focusing of the generators through the Raychaudhuri equation.
\end{enumerate}
Then $T_{ab}k^{a}k^{b} = (\eta/2\pi)R_{ab}k^{a}k^{b}$ for every null $k^{a}$, with $R_{ab}$ the Ricci tensor of the round-sphere-positive convention, that is $k \cdot T(k) = -(\eta/2\pi)\,k \cdot \mathcal{R}(k)$ for every physical null $k$ in the store's sign of the curvature operator; and with the conservation of $T$ ($\nabla^{a}T_{ab} = 0$) and the contracted Bianchi identity, in the signature $(-,+,+,+)$ of the source,
\[
R_{ab} - \tfrac12 R\,g_{ab} + \Lambda g_{ab} \;=\; \frac{2\pi}{\eta}\,T_{ab},
\]
with $\Lambda$ an undetermined constant: Einstein's equation with $G = 1/(4\eta)$, which for the gravitational field reads $\mathcal{G}(a) + \Lambda a = -(2\pi/\eta)\,T(a)$ in the store's sign. \emph{Provenance:} \cite{Jacobson1995}.

## technical
Jacobson derived Einstein's equation from thermodynamics; in Gauge Theory Gravity it is the field equation of the gravitational field $(\hb, \Omega)$ on flat spacetime. Through every point and in every physically null direction, consider a small local Rindler horizon whose generators are momentarily neither expanding nor shearing. Assume that it has the Unruh temperature of the accelerated observers just inside it, that its entropy is a universal constant $\eta$ times its area, and that the heat crossing it, the boost energy of matter, obeys $\delta Q = T\,\delta S$. The Raychaudhuri equation turns the area change into the Ricci map of the field strength along the null direction, so the Clausius relation for all null directions gives $T_{ab}k^{a}k^{b} = (\eta/2\pi)R_{ab}k^{a}k^{b}$, that is $k \cdot T(k) = -(\eta/2\pi)\,k \cdot \mathcal{R}(k)$ in the store's sign. Energy conservation and the Bianchi identity then give Einstein's equation, $\mathcal{G}(a) + \Lambda a = -(2\pi/\eta)T(a)$, with Newton's constant $1/(4\eta)$ and a cosmological constant left undetermined as an integration constant.

## lay
In 1995 Ted Jacobson showed that Einstein's equations can be read as a law of thermodynamics. If every small patch of horizon, as seen by an accelerating observer, has a temperature set by the acceleration and an entropy proportional to its area, and if heat crossing it changes its entropy by heat divided by temperature, then the gravitational field must obey exactly Einstein's equations, read here as the equations of a field on flat spacetime. The strength of gravity is fixed by the entropy per area, and the cosmological constant is left free. This is a known result taken from the literature.

## one-liner
If every local Rindler horizon has the Unruh temperature, entropy $\eta$ per area and obeys $\delta Q = T\,\delta S$ for the matter's boost-energy flux, then $G_{ab} + \Lambda g_{ab} = (2\pi/\eta)T_{ab}$ with $\Lambda$ undetermined (Jacobson 1995), the field equation $\mathcal{G}(a) + \Lambda a = -(2\pi/\eta)T(a)$ of the gravitational field in the store's sign.
