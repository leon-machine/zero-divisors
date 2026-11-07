---
id: synthesis.imported-adler-bell-jackiw-axial-anomaly
kind: claim
version: 2
title: 'Imported: the axial anomaly (Adler 1969; Bell and Jackiw 1969)'
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
- name: Claude Opus 5.5
  role: 'consistency pass, unit principle (U4): the bare unit of the mass term written as I_4'
  version: 2
  source: maintainer pass 2026-11-07 (consistency)
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
  source_formal: |-
    Units $\hbar = c = 1$, signature $(+,-,-,-)$, $\alpha = e^{2}/(4\pi)$. For a Dirac fermion of mass $m$ and charge $e$ coupled to the electromagnetic field $F$, with the axial current $j^{5}_{\mu} = \bar\psi\gamma_{\mu}\gamma_{5}\psi$ and the pseudoscalar density $j^{5} = \bar\psi\gamma_{5}\psi$ (index reading of the sources), the one-loop triangle graph with one axial and two vector vertices cannot be made to conserve the vector current and to satisfy the naive axial Ward identity at once; keeping the vector current conserved,
    \[
    \partial^{\mu}j^{5}_{\mu} = 2im\,j^{5} + \frac{\alpha}{4\pi}\,\epsilon_{\xi\sigma\tau\rho}F^{\xi\sigma}F^{\tau\rho}
    \]
    \cite{Adler1969} (in the form of \cite{Adler2004}, eq. (1), with bare $m$ and $\alpha$). The anomalous term is proportional to $E\cdot B$, the pseudoscalar part of the square of the field-strength bivector. In the $\sigma$-model the same term removes the conflict between partial conservation of the axial current and the observed rate of $\pi^{0} \to \gamma\gamma$ \cite{BellJackiw1969}.
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 1 -> 2. Restated by U4: the bare unit i in the mass term 2im j^5 of the formal level and the one-liner (missed by the bare-unit detector, which does not flag i followed by a letter) is the field theory''s unit, a number multiplying the bilinear, so by U1 it is I_4 (numbers in span{1, I_4}; gamma_5 read as the chirality x -> I_4 x I_4 of the store''s one-loop electrodynamics); the source''s form (the formal level as first stored) moves to extraction.source_formal, and the sources write i for I_4. Status, links and what is imported unchanged.'
---

## formal
Units $\hbar = c = 1$, signature $(+,-,-,-)$, $\alpha = e^{2}/(4\pi)$. Numbers, the bilinears $j^{5}_{\mu}$ and $j^{5}$ among them, are read in $\mathrm{span}\{1, I_{4}\}$, the field theory's unit (on Clifford products the right unit $x \mapsto xI_{4}$), and $\gamma_{5}$ is the chirality $x \mapsto I_{4}xI_{4}$ of the store's one-loop electrodynamics (the left $I_{4}$ inside the product, the right one the unit); the sources write $i$ for $I_{4}$. For a Dirac fermion of mass $m$ and charge $e$ coupled to the electromagnetic field $F$, with the axial current $j^{5}_{\mu} = \bar\psi\gamma_{\mu}\gamma_{5}\psi$ and the pseudoscalar density $j^{5} = \bar\psi\gamma_{5}\psi$ (index reading of the sources), the one-loop triangle graph with one axial and two vector vertices cannot be made to conserve the vector current and to satisfy the naive axial Ward identity at once; keeping the vector current conserved,
\[
\partial^{\mu}j^{5}_{\mu} = 2I_{4}m\,j^{5} + \frac{\alpha}{4\pi}\,\epsilon_{\xi\sigma\tau\rho}F^{\xi\sigma}F^{\tau\rho}
\]
\cite{Adler1969} (in the form of \cite{Adler2004}, eq. (1), with bare $m$ and $\alpha$). The anomalous term is proportional to $E\cdot B$, the pseudoscalar part of the square of the field-strength bivector. In the $\sigma$-model the same term removes the conflict between partial conservation of the axial current and the observed rate of $\pi^{0} \to \gamma\gamma$ \cite{BellJackiw1969}.

## technical
The axial anomaly is the failure of the classical conservation law of the axial current of a massless fermion in the quantum theory. Adler computed the triangle graph with one axial and two vector vertices in spinor electrodynamics and showed that, when the vector current is kept conserved (as gauge invariance requires), the divergence of the axial current acquires a term proportional to the electromagnetic field contracted with its dual, $E\cdot B$, with coefficient $\alpha/(4\pi)$ in the normalisation $\epsilon FF$. Bell and Jackiw found the same term in the $\sigma$-model and showed that it accounts for the decay of the neutral pion into two photons, which the naive current algebra forbids.

## lay
Some symmetries of the classical equations of particle physics do not survive in the quantum theory. The best known case concerns the difference between left-handed and right-handed particles: in 1969 Adler, and Bell and Jackiw, found that quantum effects of light break this balance by an amount set by the electric and magnetic fields together, and that this explains why a neutral pion decays into two photons. The series takes this result from the literature.

## one-liner
The axial anomaly (Adler; Bell and Jackiw 1969): with the vector current conserved, $\partial\cdot j^{5} = 2I_{4}m\,j^{5} + (\alpha/4\pi)\epsilon FF$ from the triangle graph, proportional to $E\cdot B$; it explains $\pi^{0} \to \gamma\gamma$.
