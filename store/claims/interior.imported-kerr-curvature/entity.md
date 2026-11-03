---
id: interior.imported-kerr-curvature
kind: claim
version: 2
title: 'Imported: the Kerr curvature'
status: imported
region: interior
subject: interior
tags: [classical-theorem, kerr, curvature-and-field-equations]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T06, deposited version
review: typed
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: C. Doran and A. Lasenby, Geometric Algebra for Physicists, Cambridge University Press (2003).
  key: DoranLasenby2003
  locator: Ch.~14
- citation: B. Carter, Global structure of the Kerr family of gravitational fields, Phys. Rev. 174 (1968),
    1559--1571.
  key: Carter1968
locators:
  paper: T06
  number: Fact 6.3
  label: fact:kerrcurv
  line: 801
extraction:
  typing:
    by: ai-typing-pass
    note: 'Imported fact with no derivation; nothing to edge.'
  env: fact
  context_refs:
  - interior.imported-schwarzschild-curvature-spectrum
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement: the curvature operator is named as the field strength R(B) of the Kerr gravitational field (hb, Omega) on flat spacetime, in the store sign of the definition object; the singular set of the maximal extension is restated as the ring r = 0, theta = pi/2 of the flat background where hb fails. Formula unchanged.'
---

## formal
In the conventions of Fact \claimref{interior.imported-schwarzschild-curvature-spectrum}, which are the store's curvature sign of Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}, the curvature operator of the Kerr gravitational field $(\hb, \Omega)$ on flat spacetime (its field strength, a linear map on physical bivectors) is
\[
\mathcal{R}(B) \;=\; \frac{M}{2}\,\bigl(r - I a\cos\theta\bigr)^{-3}\,\bigl(B + 3\,\sigma_r B\sigma_r\bigr),
\]
where $\sigma_r$ is the unit bivector of the principal planes (the plane pair singled out by the two principal congruences of physically null vectors), $I$ is the pseudoscalar of $\Cl(1,3)$, the inverse cube is taken in the commutative subalgebra $\R \oplus \R I$, and $(r,\theta)$ are oblate spheroidal coordinates on the flat background in which the singular set is the ring $r = 0$, $\theta = \pi/2$, where $\hb$ is undefined (it is unimodular wherever it is defined) and the field strength diverges. \emph{Provenance:} Doran-Lasenby \cite[Ch.~14]{DoranLasenby2003}; the type-D form is classical \cite{Carter1968}.

## technical
In the conventions of the imported Schwarzschild curvature spectrum, which carry the store's curvature sign, the Kerr gravitational field on flat spacetime has field strength $\mathcal{R}(B) = \tfrac{M}{2}(r - Ia\cos\theta)^{-3}(B + 3\sigma_r B\sigma_r)$ on physical bivectors, with $\sigma_r$ the unit bivector of the principal planes singled out by the two principal null congruences and $I$ the pseudoscalar of $\Cl(1,3)$. The inverse cube is taken in the commutative subalgebra $\R \oplus \R I$, and $(r, \theta)$ are oblate spheroidal coordinates on the flat background in which the singular set is the ring $r = 0$, $\theta = \pi/2$, where the gauge field $\hb$ is undefined. The result is imported from the geometric-algebra treatment of Kerr; the type-D form is classical.

## lay
This is the standard description of the strength of the gravitational field around a rotating black hole, the quantity that plays the part of spacetime curvature, written in the language of geometric algebra on a flat background. The strength of the curvature is controlled by a single complex number built from the radius and the angle from the rotation axis. The result is taken from the literature.

## one-liner
The Kerr field strength on physical bivectors is $\mathcal{R}(B) = \tfrac{M}{2}(r - Ia\cos\theta)^{-3}(B + 3\sigma_r B\sigma_r)$, with the inverse cube taken in $\R \oplus \R I$; imported from the literature.
