---
id: dark-matter.imported-induced-equations-hypersurface
kind: claim
version: 2
title: 'Imported: the induced equations on a hypersurface'
status: imported
region: dark-matter
subject: dark-matter
tags: [classical-theorem, curvature-and-field-equations]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14, deposited version
review: typed
imported_from:
- citation: T. Shiromizu, K. Maeda and M. Sasaki, The Einstein equations on the 3-brane world, Phys. Rev.
    D 62, 024012 (2000).
  key: SMS2000
  locator: eq.~(15)
locators:
  paper: T14
  number: Fact 7.21
  label: fact:sms
  line: 1062
extraction:
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: five-dimensional GTG (the d-dimensional clause of the definition): the bulk is a gravitational field on flat R^{1,4}, the hypersurface a timelike hypersurface of the flat background with unit physical normal, the induced metric and Einstein tensor read from hb^{-1} restricted to it, the bulk Weyl tensor the trace-free part of the five-dimensional field strength; the imported term unchanged. Fix (referee GR2, 2026-10-23, WRONG as restated): the source signature is declared, flat R^{4,1} in (-,+,+,+,+) with Q(n) = +1, so the displayed Shiromizu-Maeda-Sasaki term holds as written (in the store sign (+,-,-,-,-) it would read T_mu nu - (T_nn + T/4) g_mu nu).'
  env: fact
  typing:
    by: ai-typing-pass
    note: Imported; levels only.
---

## formal
Let a gravitational field $(\hb, \Omega)$ on flat $\R^{4,1}$, in the signature $(-,+,+,+,+)$ of the source (the $d$-dimensional clause of Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}, $d = 5$, with the product of that signature) obey the five-dimensional field equations, read on its derived metric as $G_{ab} = \kappa_{5}^{2}T_{ab}$, and let $\Sigma$ be a timelike hypersurface of the flat background with unit physical normal $n$ (a physical vector, $Q(n) = +1$, orthogonal to $\hb^{-1}$ of the tangent directions of $\Sigma$). Then the Einstein tensor of the metric that $\hb^{-1}$ induces on $\Sigma$ contains, from the bulk stress tensor, the term
\[
\frac{2\kappa_{5}^{2}}{3}\Bigl[\,T_{\mu\nu} + \bigl(T_{ab}n^{a}n^{b} - \tfrac{1}{4}T\bigr)g_{\mu\nu}\Bigr],
\]
with $T = g^{ab}T_{ab}$ the trace (in Gauge Theory Gravity $T_{ab}n^{a}n^{b} = n \cdot T(n)$ and $T = \partial_a \cdot T(a)$), together with terms quadratic in the hypersurface's own extrinsic curvature, the projected $D$-derivative of $n$, and the projected bulk Weyl curvature $\mathcal{W}$, the trace-free part of the five-dimensional field strength. \emph{Provenance:} \cite[eq.~(15)]{SMS2000}, read in five-dimensional Gauge Theory Gravity through the frame formalism, which holds in every dimension.

## technical
Let a five-dimensional gravitational field on flat $\R^{4,1}$, in the signature $(-,+,+,+,+)$ of the source, obey $G_{ab} = \kappa_{5}^{2}T_{ab}$ for its derived metric, and take a timelike hypersurface of the flat background with unit physical normal $n$. The Einstein tensor of the metric induced on the hypersurface contains, from the bulk stress tensor, the term $\tfrac{2\kappa_{5}^{2}}{3}\bigl[T_{\mu\nu} + \bigl(T_{ab}n^{a}n^{b} - \tfrac{1}{4}T\bigr)g_{\mu\nu}\bigr]$, with $T$ the bulk trace. The remaining terms are quadratic in the hypersurface's own extrinsic curvature or come from the projected bulk Weyl curvature. This is the Shiromizu-Maeda-Sasaki form of the induced equations, read in five-dimensional Gauge Theory Gravity.

## lay
If our world is a thin slice inside a five-dimensional space, gravity there can still be described as fields on a flat five-dimensional background. Einstein's equations for those fields imply modified equations on the slice. This imported result says how matter spread through the larger space shows up as a source of gravity on the slice, alongside extra terms from the slice's own bending and from the tidal part of the five-dimensional field.

## one-liner
For a five-dimensional gravitational field on flat $\R^{4,1}$ (signature $(-,+,+,+,+)$) obeying Einstein's equations, the bulk stress tensor enters the Einstein tensor induced on a timelike hypersurface as $\tfrac{2\kappa_{5}^{2}}{3}[T_{\mu\nu} + (T_{ab}n^{a}n^{b} - \tfrac{1}{4}T)g_{\mu\nu}]$, with extrinsic-curvature and projected Weyl terms.
