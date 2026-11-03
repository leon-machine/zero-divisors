---
id: synthesis.imported-adler-bell-jackiw-axial-anomaly
kind: claim
version: 1
title: 'Imported: the axial anomaly of spinor electrodynamics (Adler 1969; Bell and Jackiw 1969): when the vector current is kept conserved, the divergence of the axial current of a Dirac fermion has, besides the mass term, the anomalous term $(\alpha/4\pi)\,\epsilon^{\xi\sigma\tau\rho}F_{\xi\sigma}F_{\tau\rho}$ from the triangle graph, which accounts for the decay of the neutral pion into two photons'
status: imported
region: synthesis
subject: quantum-fields
tags: [chirality, hypercharge-and-anomalies, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-11-02
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
imported_from:
- citation: 'S. L. Adler, Axial-vector vertex in spinor electrodynamics, Phys. Rev. 177 (1969), 2426--2438.'
  key: Adler1969
  doi: 10.1103/PhysRev.177.2426
- citation: 'J. S. Bell and R. Jackiw, A PCAC puzzle: pi0 -> gamma gamma in the sigma-model, Nuovo Cimento A 60 (1969), 47--61.'
  key: BellJackiw1969
- citation: 'S. L. Adler, Anomalies to all orders, in: 50 Years of Yang-Mills Theory, ed. G. ''t Hooft, World Scientific (2005); arXiv:hep-th/0405040.'
  key: Adler2004
  locator: 'eq. (1) and the reference list'
extraction:
  note: >-
    Imported so that the triangle anomaly computed in the spacetime algebra can pin the original anomaly papers
    instead of citing them from memory. Checked on 2026-11-02 against Adler's account arXiv:hep-th/0405040: the
    bibliographic entries of Adler 1969 (Phys. Rev. 177, 2426-2438) and Bell-Jackiw 1969 (Nuovo Cimento A 60,
    47-61, with the title "A PCAC puzzle: pi0 -> gamma gamma in the sigma-model"), and the anomaly equation, its eq. (1),
    d^mu j5_mu = 2 i m0 j5 + (alpha0/(4 pi)) F^{xi sigma} F^{tau rho} epsilon_{xi sigma tau rho}, with the bare mass and
    coupling. Not checked against the sources: the DOI of Adler 1969 and the book data of the 2005 volume (from
    memory). The store's sign and normalisation of the pseudoscalar part of the field square are those of the
    result that computes the triangle; this Fact is stated in the index reading of the sources.
  maintainer_pass:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Created by the maintainer pass of 2026-11-02 (Adler and Bell-Jackiw as a Fact, by Leon''s list of routine imports).'
---

## formal
Units $\hbar = c = 1$, signature $(+,-,-,-)$, $\alpha = e^{2}/(4\pi)$. For a Dirac fermion of mass $m$ and charge $e$ coupled to the electromagnetic field $F$, with the axial current $j^{5}_{\mu} = \bar\psi\gamma_{\mu}\gamma_{5}\psi$ and the pseudoscalar density $j^{5} = \bar\psi\gamma_{5}\psi$ (index reading of the sources), the one-loop triangle graph with one axial and two vector vertices cannot be made to conserve the vector current and to satisfy the naive axial Ward identity at once; keeping the vector current conserved,
\[
\partial^{\mu}j^{5}_{\mu} = 2im\,j^{5} + \frac{\alpha}{4\pi}\,\epsilon_{\xi\sigma\tau\rho}F^{\xi\sigma}F^{\tau\rho}
\]
\cite{Adler1969} (in the form of \cite{Adler2004}, eq. (1), with bare $m$ and $\alpha$). The anomalous term is proportional to $E\cdot B$, the pseudoscalar part of the square of the field-strength bivector. In the $\sigma$-model the same term removes the conflict between partial conservation of the axial current and the observed rate of $\pi^{0} \to \gamma\gamma$ \cite{BellJackiw1969}.

## technical
The axial anomaly is the failure of the classical conservation law of the axial current of a massless fermion in the quantum theory. Adler computed the triangle graph with one axial and two vector vertices in spinor electrodynamics and showed that, when the vector current is kept conserved (as gauge invariance requires), the divergence of the axial current acquires a term proportional to the electromagnetic field contracted with its dual, $E\cdot B$, with coefficient $\alpha/(4\pi)$ in the normalisation $\epsilon FF$. Bell and Jackiw found the same term in the $\sigma$-model and showed that it accounts for the decay of the neutral pion into two photons, which the naive current algebra forbids.

## lay
Some symmetries of the classical equations of particle physics do not survive in the quantum theory. The best known case concerns the difference between left-handed and right-handed particles: in 1969 Adler, and Bell and Jackiw, found that quantum effects of light break this balance by an amount set by the electric and magnetic fields together, and that this explains why a neutral pion decays into two photons. The series takes this result from the literature.

## one-liner
The axial anomaly (Adler; Bell and Jackiw 1969): with the vector current conserved, $\partial\cdot j^{5} = 2im\,j^{5} + (\alpha/4\pi)\epsilon FF$ from the triangle graph, proportional to $E\cdot B$; it explains $\pi^{0} \to \gamma\gamma$.
