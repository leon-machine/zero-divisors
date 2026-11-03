---
id: synthesis.imported-twistor-equation-integrability-petrov-n-or-o
kind: claim
version: 1
title: 'Imported: the integrability condition of the twistor equation, $\Psi_{ABCD}\omega^{D} = 0$, restricts the Weyl curvature at every point where a nonzero solution exists to Petrov type N (with $\omega$ a repeated principal spinor) or O (Penrose; Penrose and Rindler; Gasperin and Pais)'
status: imported
region: synthesis
subject: conformal-spacetime
tags: [conformal-spinors, tractors, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-11-01
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
- citation: 'R. Penrose and W. Rindler, Spinors and Space-Time, vol. 2: Spinor and Twistor Methods in Space-Time Geometry, Cambridge University Press (1986).'
  key: PenroseRindler1986
  locator: 'Ch. 6'
- citation: 'E. Gasperin and F. Pais, Twistor initial data characterisation of pp-waves, arXiv:2404.05883.'
  key: GasperinPais2024
  doi: 10.1088/1361-6382/ad3b5e
extraction:
  note: >-
    Imported so that the result on parallel conformal spinors of the attachment can pin the standard
    integrability condition of the twistor equation instead of citing it. Checked on 2026-11-01 against the
    arXiv text of Gasperin and Pais, 2404.05883 (opening section, after the definition of a valence-1 Killing
    spinor, Eq. (1)): the integrability condition of the twistor equation is Psi_ABCD kappa^D = 0, which
    "restricts the spacetime to be of Petrov type N or O"; the DOI from the arXiv record (the journal, Classical
    and Quantum Gravity, inferred from the DOI prefix, not checked). Cited from memory, not checked: Penrose and
    Rindler vol. 2, Ch. 6 (local twistor curvature and the integrability of the twistor equation). The algebraic
    step (a nonzero spinor annihilated by the Weyl spinor is a repeated principal spinor of multiplicity four)
    is re-derived in the citing result.
---

## formal
Let $(\hb, \Omega)$ be a gravitational field on four-dimensional flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) whose derived metric is smooth, and read its Weyl curvature $\mathcal{W}$ in two-spinor form as the Weyl spinor $\Psi_{ABCD}$ (a reading, as in Fact \claimref{synthesis.imported-gtg-dictionary}). The twistor equation for a spinor field $\omega^{A}$ is $\nabla_{A'}^{(A}\omega^{B)} = 0$; its integrability condition is $\Psi_{ABCD}\,\omega^{D} = 0$. Hence at every point where a nonzero solution exists, either $\Psi_{ABCD} = 0$ (Petrov type O) or $\Psi_{ABCD} = \Psi_{4}\,o_{A}o_{B}o_{C}o_{D}$ with $\omega$ proportional to $o$ (Petrov type N, $\omega$ the fourfold repeated principal spinor): the twistor equation restricts the field to Petrov type N or O. \emph{Provenance:} \cite[Ch.~6]{PenroseRindler1986}; \cite{GasperinPais2024}.

## technical
Twistors on a curved background are the solutions of the twistor equation, and they exist in full number only where the Weyl curvature vanishes. The obstruction is the integrability condition, the Weyl spinor contracted with the twistor's primary part, which must vanish. A nonzero spinor annihilated by the Weyl spinor is a principal spinor of multiplicity four, so at any point where a nonzero solution exists the Weyl curvature is of Petrov type N, with that spinor as its repeated principal spinor, or vanishes (type O). This is standard twistor theory (Penrose; Penrose and Rindler, vol. 2), stated, for example, by Gasperin and Pais.

## lay
Twistors, the objects from which the series builds its quantum states, can be carried consistently through a gravitational field only where a certain part of the field, the part that describes tidal stretching and gravitational waves, is either absent or of the special form of a pure gravitational wave. This standard result of twistor theory is taken from the literature.

## one-liner
The integrability condition of the twistor equation, $\Psi_{ABCD}\omega^{D} = 0$, forces the Weyl curvature at every point with a nonzero solution to be of Petrov type N (with $\omega$ the repeated principal spinor) or O (Penrose and Rindler 1986; Gasperin and Pais 2024).
