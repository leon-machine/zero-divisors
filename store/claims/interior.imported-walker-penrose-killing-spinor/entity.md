---
id: interior.imported-walker-penrose-killing-spinor
kind: claim
version: 2
title: 'Imported: the Walker-Penrose Killing spinor'
status: imported
region: interior
subject: interior
tags: [classical-theorem, kerr]
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
- citation: M. Walker and R. Penrose, On quadratic first integrals of the geodesic equations for type
    $22$ spacetimes, Commun. Math. Phys. 18 (1970), 265--274.
  key: WalkerPenrose1970
- citation: B. Carter, Global structure of the Kerr family of gravitational fields, Phys. Rev. 174 (1968),
    1559--1571.
  key: Carter1968
locators:
  paper: T06
  number: Fact 6.7
  label: fact:wp
  line: 868
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Group F (found by the language check''s bare-unit detector): nothing replaced; the i stays and is declared outside_ga (imported): the Kerr invariant r - ia cos(theta) is quoted as Walker and Penrose state it; the series'' reading of the factor as R + R I is given in interior.complex-scale-inverse-cube-killing-spinor.'
  typing:
    by: ai-typing-pass
    note: 'Imported fact with no derivation; nothing to edge.'
  env: fact
  context_refs:
  - interior.complex-scale-inverse-cube-killing-spinor
  - interior.imported-kerr-curvature
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement: type-D vacuum is read as a vacuum gravitational field (hb, Omega) on flat spacetime whose Weyl map is of type D; the Killing spinor and conformal Killing-Yano tensor are taken for the covariant derivative D; geodesic motion is free fall with D-parallel velocity; Psi_2 is a component of the Weyl map. Imported content unchanged.'
outside_ga:
  kind: imported
  why: 'the Kerr invariant r - ia cos(theta) is quoted as Walker and Penrose state it; the series'' reading of the factor as R + R I is given in interior.complex-scale-inverse-cube-killing-spinor'
---

## formal
Every type-D vacuum gravitational field $(\hb, \Omega)$ on flat spacetime ($\mathcal{R}(a) = 0$, with Weyl map $\mathcal{W}$ of Petrov type D; Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) admits a valence-two Killing spinor $\chi$ for the covariant derivative $D$, unique up to constant scale, whose square yields a conformal Killing-Yano tensor; for Kerr its scalar invariant is proportional to $r - ia\cos\theta$, and Carter's quartic constant of free-fall motion (worldlines of $D$-parallel velocity, the geodesics of the derived metric) is the associated quadratic first integral; for type-D vacua the Weyl scalar (a component of $\mathcal{W}$ on the bivectors of a principal null tetrad) and the spinor invariant are related by $\Psi_2 \propto \chi^{-3}$, the constant fixed by normalisation. \emph{Provenance:} the Killing spinor and the quadratic integral are Walker-Penrose \cite{WalkerPenrose1970}, the constant of motion Carter \cite{Carter1968}; the $\Psi_2 \propto \chi^{-3}$ relation is the standard type-$\{22\}$ statement descending from \cite{WalkerPenrose1970}, and for Kerr the corresponding statement about the framework's own scale $\mathfrak M$ is derived in Proposition \claimref{interior.complex-scale-inverse-cube-killing-spinor} from Fact \claimref{interior.imported-kerr-curvature} and the Killing-spinor scalar above, with no appeal to this clause and none to the imported normalisation; the script checks that derivation.

## technical
Every type-D vacuum gravitational field on flat spacetime, one whose Weyl map is of Petrov type D, admits a valence-two Killing spinor $\chi$ for the covariant derivative $D$, unique up to constant scale, whose square yields a conformal Killing-Yano tensor. For Kerr its scalar invariant is proportional to $r - ia\cos\theta$, and Carter's quartic constant of free-fall motion is the associated quadratic first integral. For type-D vacua the Weyl scalar and the spinor invariant are related by $\Psi_2 \propto \chi^{-3}$, with the constant fixed by normalisation. These results are imported from Walker and Penrose and from Carter.

## lay
Rotating black holes have a hidden symmetry, which gives orbits an extra conserved quantity discovered by Carter. That symmetry comes from a special spinor field, whose basic invariant is a simple complex combination of the radius and the angle. This is a classical result taken from the literature.

## one-liner
Type-D vacua carry a Killing spinor, unique up to scale, whose Kerr invariant is proportional to $r - ia\cos\theta$, which yields Carter's constant and satisfies $\Psi_2 \propto \chi^{-3}$; imported from the literature.
