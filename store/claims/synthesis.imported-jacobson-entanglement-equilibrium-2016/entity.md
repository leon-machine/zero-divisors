---
id: synthesis.imported-jacobson-entanglement-equilibrium-2016
kind: claim
version: 2
title: 'Imported: entanglement equilibrium and the Einstein equation (Jacobson 2016)'
status: imported
region: synthesis
subject: einstein
tags: [entanglement, curvature-and-field-equations, modular-theory, classical-theorem]
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
imported_from:
- citation: 'T. Jacobson, Entanglement equilibrium and the Einstein equation, Phys. Rev. Lett. 116 (2016), 201101.'
  key: Jacobson2016
  doi: 10.1103/PhysRevLett.116.201101
extraction:
  maintainer_pass_gtg:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: d-dimensional GTG (the d-dimensional clause of the definition): spacetime is a gravitational field on flat R^{1,d-1}, the geodesic ball is taken in the normal gauge hb(x0) = 1, Omega(x0) = 0 about a point of the background, the Einstein tensor is that of the field strength; the imported content and its sign convention unchanged. Fix (referee GR2, 2026-10-23): flat R^{d-1,1} with the product of the declared (-,+,...,+); the GTG parenthetical now names the geodesic ball of the derived metric described in a normal gauge, with the leading-order clause dropped, so the ball is not read as a flat one.'
  note: >-
    Imported for the result that tests the entanglement-equilibrium route on the boundary-mode
    algebra, where its tensor step was the hypothesis (J16). Bibliographic data checked against the
    arXiv and publisher listings on 2026-10-22. The statement (the maximal vacuum entanglement
    hypothesis, the fixed-volume area variation with the factor 1/(d^2 - 1), the conformal Killing
    modular Hamiltonian, the passage to the tensor equation with Lambda an integration constant, G =
    1/(4 eta), and the conjecture needed for nonconformal fields) was checked against the arXiv
    text, 1505.04753v4. The explicit form K = 2 pi times the integral of (l^2 - r^2)/(2l) T_00 is
    the value of the conformal Killing generator on the ball at t = 0, a reconstruction consistent
    with the paper rather than its displayed formula.
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Created by the maintainer pass so that the entanglement-equilibrium result can pin Jacobson''s argument instead of the hypothesis (J16) cited from memory; verified (see note).'
---

## formal
Units $\hbar = c = 1$, spacetime dimension $d$, signature $(-,+,\ldots,+)$ with the round sphere of positive scalar curvature. Spacetime is a gravitational field $(\hb, \Omega)$ on flat $\R^{d-1,1}$, with the product of the declared signature (the $d$-dimensional clause of Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), and the geometric quantities below are those of its derived metric, read through Fact \claimref{synthesis.imported-gtg-dictionary}. About any point and for any unit timelike vector $u$, let $B$ be a small geodesic ball of radius $\ell$ in the slice orthogonal to $u$ (in Gauge Theory Gravity: the geodesic ball of the derived metric, described in a gauge with $\hb(x_0) = 1$, $\Omega(x_0) = 0$ about a point $x_0$ of the background, the frame transported along straight background rays), compared with a maximally symmetric reference geometry and the vacuum of the quantum fields. Suppose (a) the ultraviolet entanglement across $\partial B$ has a finite universal area density $\eta$; (b) the fields are conformal, so that the modular Hamiltonian of the vacuum on the causal diamond of $B$ is $2\pi$ times the generator $H_{\zeta}$ of its conformal Killing flow, whence for first-order variations $\delta S_{\mathrm{matter}} = 2\pi\,\delta\langle H_{\zeta}\rangle = 2\pi\,\Omega_{d-2}\ell^{d}\,\delta\langle T_{00}\rangle/(d^{2} - 1)$ to leading order in $\ell$; while geometrically, at fixed volume, $\delta A|_{V} = -\Omega_{d-2}\ell^{d}\,G_{00}/(d^{2} - 1)$. Then the total entanglement $\eta\,\delta A|_{V} + \delta S_{\mathrm{matter}}$ is stationary for every such ball, at every point and for every $u$, if and only if
\[
G_{ab} + \Lambda g_{ab} \;=\; \frac{2\pi}{\eta}\,\delta\langle T_{ab}\rangle ,
\]
with $\Lambda$ a constant fixed by no part of the argument (it enters as an integration constant through the contracted Bianchi identity and conservation): Einstein's equation with $G = 1/(4\eta)$. The passage from the $00$ component for every $u$ at every point to the tensor equation is part of the argument. For nonconformal fields the same conclusion holds modulo a stated conjecture on $\delta\langle K\rangle$. \emph{Provenance:} \cite{Jacobson2016}.

## technical
Jacobson's maximal vacuum entanglement hypothesis says that the entanglement entropy of a small geodesic ball is maximal, at fixed volume, in a locally maximally symmetric vacuum of geometry and quantum fields. In Gauge Theory Gravity, in any dimension $d$, the ball is taken about a point of the flat background in the normal gauge of the gravitational field. Varying the gravitational and matter fields together to first order, the area term changes by $\eta\,\delta A|_{V} = -\eta\,\Omega_{d-2}\ell^{d}G_{00}/(d^{2} - 1)$ and, for conformal fields, the matter term by $2\pi\,\Omega_{d-2}\ell^{d}\,\delta\langle T_{00}\rangle/(d^{2} - 1)$, using the conformal Killing modular Hamiltonian of the ball's causal diamond. Stationarity for all balls, at all points and in all frames, holds exactly when $G_{ab} + \Lambda g_{ab} = (2\pi/\eta)\,\delta\langle T_{ab}\rangle$, with $\Lambda$ an integration constant: Einstein's equation with $G = 1/(4\eta)$. Nonconformal fields need an additional conjecture.

## lay
In 2016 Ted Jacobson showed that Einstein's equations follow if empty space is as entangled as it can be. Take any small ball of space; the quantum fields inside are entangled with those outside, by an amount proportional to the ball's surface area, plus a contribution from any matter present. Requiring that this total entanglement is at a maximum, for every small ball at every place and as seen by every observer, turns out to be the same as requiring Einstein's equations. This is a known result taken from the literature.

## one-liner
For conformal fields, stationarity of the total entanglement $\eta\,\delta A|_{V} + \delta S_{\mathrm{matter}}$ of every small geodesic ball at fixed volume, at every point and in every frame, is equivalent to $G_{ab} + \Lambda g_{ab} = (2\pi/\eta)\,\delta\langle T_{ab}\rangle$ with $\Lambda$ undetermined (Jacobson 2016).
