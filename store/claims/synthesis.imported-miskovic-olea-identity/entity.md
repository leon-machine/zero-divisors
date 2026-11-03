---
id: synthesis.imported-miskovic-olea-identity
kind: claim
version: 3
title: 'Imported: on shell the Euler-regularised anti-de Sitter action is the Weyl-squared action (Miskovic-Olea)'
status: imported
region: synthesis
subject: dark-energy
tags: [cosmological-constant, curvature-and-field-equations, classical-theorem]
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
- citation: 'O. Miskovic and R. Olea, Topological regularization and self-duality in four-dimensional anti-de Sitter gravity, Phys. Rev. D 79 (2009), 124020; arXiv:0902.2082.'
  key: MiskovicOlea2009
extraction:
  maintainer_pass_2:
    by: maintainer-2026-10-24
    date: '2026-10-24'
    note: 'Gauge Theory Gravity wording pass at Leon''s request (2026-10-24): curved-spacetime and conformally-flat wording restated in terms of the gravitational field on flat spacetime (a nonvanishing gravitational field; the Weyl part of the field strength vanishes, the conformally flat derived metric kept as a reading; global content read on an atlas of flat charts patched by gauge transformations). Wording only; statements, proofs'' arguments and checks unchanged. Version 2 -> 3. Referee fixes to the GTG wording pass (2026-10-24): ''a gravitational field of nonvanishing field strength'' (gauge-independent) in place of ''a nonvanishing gravitational field''; global content read on several charts of flat spacetime, each with its own gravitational field, glued by displacement and rotation gauge transformations (complexified charts for the half-flat manifold, the conformal compactification for a conformal boundary); ''not carried by the store''s one-chart fields'' in place of ''no single gravitational field carries''; equivalence statements weakened where the old text was weaker; remaining curved-spacetime phrases in lay text restated. Wording only.'
  note: >-
    Recorded as the literature counterpart (anti-de Sitter, Lorentzian) of the de Sitter Euclidean
    instanton identity proved in synthesis.promoted-norm-weyl-clock-flat-weight, which cites it as
    prior work, not as a premise. The statement was checked against the arXiv text (Eqs. (5) to (7)
    and the sentence that the action is on-shell equivalent to conformal gravity because every trace
    of the Weyl tensor vanishes); the journal reference is cited from memory, not checked against
    the source.
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Created by the maintainer pass to record the Miskovic-Olea identity that the de Sitter instanton result cites as known; verified against the arXiv text except the journal reference.'
  flags:
  - 'beyond one flat chart: the conformal boundary of anti-de Sitter space (holographic counterterms) and the global Euler integral'
  maintainer_pass_gtg:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity (MIXED): the shifted curvature R(B) + l^{-2} B and the Weyl part W(B) of the curvature operator (same form in the store''s sign, checked against the Weyl formula of the dictionary with R(a) = Lambda a); the integrand in GA with det(hb)^{-1} d^4x. The conformal boundary of AdS (holographic renormalisation) and the global Euler integral carry the Section 14 flag and a flags entry. Provenance unchanged.'
---

## formal
In four dimensions, for a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) with negative cosmological constant $\Lambda = -3/\ell^{2}$, add to the Einstein-Hilbert action the Euler (Gauss-Bonnet) term with the coupling fixed at $\alpha = \ell^{2}/(64\pi G)$, the value at which the action takes the MacDowell-Mansouri form, quadratic in the shifted curvature $\mathcal{R}(B) + \ell^{-2}B$ (in the source's components, $R^{\alpha\beta}{}_{\mu\nu} + \ell^{-2}\delta^{[\alpha\beta]}_{[\mu\nu]}$). On solutions of the field equations (fields with $\mathcal{R}(a) = \Lambda a$, Einstein spaces with this $\Lambda$) that combination is the Weyl part of the curvature operator, $\mathcal{W}(B) = \mathcal{R}(B) + \ell^{-2}B$ (in components $W^{\alpha\beta}{}_{\mu\nu} = R^{\alpha\beta}{}_{\mu\nu} + \ell^{-2}\delta^{[\alpha\beta]}_{[\mu\nu]}$), so the action is on shell equal to the conformal-gravity action
\[
I \;=\; \frac{\ell^{2}}{64\pi G}\int_{M}d^{4}x\,\sqrt{-g}\;W_{\mu\nu\alpha\beta}W^{\mu\nu\alpha\beta} \;=\; \frac{\ell^{2}}{64\pi G}\int \det(\hb)^{-1}\,2\langle\mathcal{W}(a \wedge b)\,\mathcal{W}(\partial_b \wedge \partial_a)\rangle\,d^{4}x,
\]
every trace of $\mathcal{W}$ vanishing. The same coupling reproduces the counterterms of holographic renormalisation. \emph{Provenance:} \cite{MiskovicOlea2009}, in their sign conventions (the shifted combination has the same form in the store's sign, since anti-de Sitter space has $\mathcal{R}(B) = -\ell^{-2}B$ there).

\emph{Beyond one flat chart.} The conformal boundary of anti-de Sitter space, at which holographic renormalisation and its counterterms live, and the integral of the Euler term over the whole of $M$ are global and are not carried by a single gravitational field $(\hb, \Omega)$ on flat spacetime; the statements above that hold on the invertible region are in GTG, and the conformal boundary and the global integral are read on the manifold assembled from the derived metric's charts (the conformal boundary natively in the conformal model $\Cl(2,4)$).

## technical
Mišković and Olea showed that adding the Euler density to the action of four-dimensional anti-de Sitter gravity, with its coupling fixed at $\ell^{2}/(64\pi G)$, regularises the action exactly as holographic renormalisation does. At that coupling the action is the MacDowell-Mansouri square of the field strength shifted by its anti-de Sitter value, $\mathcal{R}(B) + \ell^{-2}B$; for a gravitational field on flat spacetime solving the field equations with the matching cosmological constant the shifted curvature is the Weyl part $\mathcal{W}$, so the action equals $(\ell^{2}/64\pi G)\int W^{2}$, the action of conformal gravity. Its conformal boundary, where the counterterms live, is global: no single gravitational field on flat spacetime carries it, so that part is read on the conformal compactification, in the conformal model $\Cl(2,4)$; the rescaling that reaches the boundary is a dilation of $\hb$, not a gauge transformation.

## lay
One form of Einstein's theory with a negative cosmological constant includes an extra term that only depends on the overall shape of space. Mišković and Olea showed that for every solution of the theory this action equals the action of a different theory, conformal gravity, which only measures how the gravitational field distorts shapes tidally. This is a known result taken from the literature.

## one-liner
For four-dimensional anti-de Sitter gravity with the Euler term at coupling $\ell^{2}/(64\pi G)$, the action on Einstein solutions equals the conformal-gravity action $(\ell^{2}/64\pi G)\int\sqrt{-g}\,W^{2}$, with $\mathcal{W}(B) = \mathcal{R}(B) + \ell^{-2}B$ the Weyl part of the field strength (Mišković-Olea).
