---
id: synthesis.imported-luscher-mack-conformal-energy-on-the-einstein-static-field
kind: claim
version: 1
title: 'Imported: a conformally invariant quantum field theory on Minkowski space extends to the universal covering of its conformal compactification, the Einstein static field $\mathbb{R}\times S^{3}$, with the universal covering of the conformal group acting, and its conformal energy $\tfrac12(P_{0} + K_{0})$ is the energy of the unit Einstein static field (L\"uscher and Mack 1975)'
status: imported
region: synthesis
subject: quantum-fields
tags: [conformal-model, representation-theory, classical-theorem]
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
- citation: 'M. L\"uscher and G. Mack, Global conformal invariance in quantum field theory, Commun. Math. Phys. 41 (1975), 203--234.'
  key: LuscherMack1975
  doi: 10.1007/BF01608988
extraction:
  note: >-
    Imported so that the result on the attachment's modules and the Sakharov weights can pin the identification
    of conformal energy with energy on the unit Einstein static field instead of citing it from memory.
    Checked on 2026-11-01: the bibliographic data (authors, title, Commun. Math. Phys. 41 (1975) 203-234, DOI
    10.1007/BF01608988) against the Crossref record; the content statement that, from Euclidean conformal
    invariance, Luscher and Mack establish invariance of the theory continued to the universal covering of
    compactified Minkowski space under the universal covering of the conformal group (global conformal
    invariance), against the secondary account in arXiv:hep-th/0403191, Sec. 1.1, which also writes the
    generator of conformal time translations with spectrum bounded below. Cited from memory, not checked
    against the source: the explicit identification of the conformal Hamiltonian (P_0 + K_0)/2 with the time
    translation of the unit Einstein static field, and the nonnegativity of its spectrum (the latter is
    proved in the store's conformal model, synthesis.positive-conformal-energy-gives-positive-null-translations).
  flags:
  - 'beyond one flat chart: the Einstein static field R x S^3 and the universal covering of compactified Minkowski space are global; the conformal embedding of Minkowski space is stated on one chart'
---

## formal
Let a quantum field theory on Minkowski space (the flat gravitational field, $\hb = 1$, $\Omega = 0$; Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) satisfy the Wightman axioms and be conformally invariant, in the sense that its Euclidean Green functions are invariant under the Euclidean conformal group. Then (L\"uscher and Mack) the theory extends to the universal covering $\widetilde{M}$ of compactified Minkowski space, on which the universal covering of the conformal group $\mathrm{SO}(2,4)$ acts by a unitary representation on the state space; $\widetilde{M}$ carries the derived metric of the Einstein static field $\mathbb{R} \times S^{3}$ of unit radius, conformal to Minkowski space on the image of the embedding. The conformal energy $H = \tfrac12(P_{0} + K_{0})$, the combination of the time translation $P_{0}$ and the special conformal generator $K_{0}$ of Minkowski space, generates the time translations of $\mathbb{R} \times S^{3}$: it is the energy of the theory on the unit Einstein static field, and its spectrum is bounded below. \emph{Provenance:} \cite{LuscherMack1975}. \emph{Beyond one flat chart.} $\widetilde{M}$ and the Einstein static field are global and are read on several charts of flat spacetime, each with its own gravitational field, glued by gauge transformations; the conformal embedding of Minkowski space into one of them is stated on one chart.

## technical
A conformally invariant field theory on Minkowski space does not live only on Minkowski space: its natural home is the universal covering of the conformal compactification, which is the Einstein static universe, a cylinder $\mathbb{R} \times S^{3}$. L\"uscher and Mack showed that, given Euclidean conformal invariance, the Minkowski theory extends there, with the whole covering group of the conformal group acting unitarily. Under this embedding the time translation of the cylinder of unit radius is the conformal Hamiltonian $\tfrac12(P_{0} + K_{0})$ of Minkowski space, so the conformal energy of a state on Minkowski space is its energy on the unit Einstein static field.

## lay
Theories that look the same at every scale can be moved, without losing information, from ordinary flat spacetime onto a closed universe shaped like a cylinder whose cross-section is a three-dimensional sphere. L\"uscher and Mack showed how. On that cylinder an ordinary energy is defined, and it corresponds to a particular combination of energy and a rescaling-type symmetry in flat spacetime. This is taken from the literature.

## one-liner
A conformally invariant quantum field theory on Minkowski space extends to the universal covering of its conformal compactification, the Einstein static field $\mathbb{R} \times S^{3}$, with the covering conformal group acting unitarily, and its conformal energy $\tfrac12(P_{0} + K_{0})$ is the energy on the unit Einstein static field (L\"uscher and Mack 1975).
