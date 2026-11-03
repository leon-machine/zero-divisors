---
id: correspondence.imported-weyl-commutes-duality
kind: claim
version: 2
title: 'Imported: Weyl commutes with duality'
status: imported
region: correspondence
subject: einstein
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
  source: authorship disclosure of T09, deposited version
review: typed
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: R. Penrose and W. Rindler, Spinors and Space-Time, Vols. 1--2, Cambridge University Press
    (1984, 1986).
  key: PenroseRindler86
locators:
  paper: T09
  number: Fact 6.2
  label: fact:weylstar
  line: 791
extraction:
  typing:
    by: ai-typing-pass
    note: 'Imported classical result; levels only.'
  env: fact
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the Weyl curvature operator on two-forms is the Weyl map W of the field strength on physical bivectors, and the Hodge star is multiplication by the pseudoscalar I, so the Fact reads W(IB) = I W(B) at every point of the invertible region; the manifold form is kept as the equivalent reading (the statement is pointwise). Content unchanged.'
---

## formal
For a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), at every point of its invertible region the Weyl map $\mathcal{W}$, the trace-free part of the curvature operator $\mathcal{R}$ on physical bivectors, commutes with duality: $\mathcal{W}(IB) = I\,\mathcal{W}(B)$ for every bivector $B$, where $I$ is the pseudoscalar of $\Cl(1,3)$ and multiplication by $I$ is, up to the sign convention of the star, the Hodge star on the two-forms of the derived metric. The statement is pointwise; equivalently, on an oriented Lorentzian $4$-manifold the Weyl curvature operator on $2$-forms commutes with the Hodge star. \emph{Provenance:} classical $4$-dimensional curvature decomposition; \cite{PenroseRindler86}.

## technical
For a gravitational field on flat spacetime, let $\mathcal{W}$ be the Weyl part of its field strength, a linear map on bivectors, and let duality be multiplication by the pseudoscalar $I$, which is the Hodge star of the derived metric up to its sign convention. Then $\mathcal{W}(IB) = I\,\mathcal{W}(B)$ at every point where $\hb$ is invertible: in curved-spacetime language, on an oriented Lorentzian four-manifold the Weyl operator on two-forms commutes with the Hodge star, $\mathcal{W}\star = \star\mathcal{W}$. This is part of the classical decomposition of curvature in four dimensions, imported from Penrose and Rindler.

## lay
In four dimensions, the part of the gravitational field strength responsible for tidal forces and gravitational waves respects a natural symmetry that exchanges electric-type and magnetic-type components. This is a standard result of relativity, imported here.

## one-liner
The Weyl map of the gravitational field strength commutes with duality, $\mathcal{W}(IB) = I\,\mathcal{W}(B)$: on an oriented Lorentzian four-manifold the Weyl operator on two-forms commutes with the Hodge star.
