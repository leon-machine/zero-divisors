---
id: synthesis.imported-quasi-spin-pairing-and-top-condensation
kind: claim
version: 1
title: 'Imported: the quasi-spin (seniority) solution of the degenerate pairing model (Kerman 1961), with energies $-\tfrac{G}{4}(n - v)(2\Omega - n - v + 2)$; the Nambu-Jona-Lasinio relation $m_{\sigma} = 2m$ (1961); and top-quark condensation (Bardeen, Hill and Lindner 1990), whose leading prediction $m_{h} = 2m_{t}$ two-condensate models lower to $125$ GeV (Osipov et al. 2019)'
status: imported
region: synthesis
subject: quantum-fields
tags: [pairing-and-bogoliubov, mass-generation, symmetry-breaking, classical-theorem]
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
imported_from:
- citation: 'A. K. Kerman, Pairing forces and nuclear collective motion, Ann. Phys. (NY) 12 (1961), 300.'
  key: Kerman1961
- citation: 'B. K. Agrawal and B. Maheshwari, Pairing, quasi-spin and seniority, arXiv:2006.03909, Section 5.2, equations (67), (77) and (78).'
  key: AgrawalMaheshwari2020
- citation: 'Y. Nambu and G. Jona-Lasinio, Dynamical model of elementary particles based on an analogy with superconductivity. I, Phys. Rev. 122 (1961), 345--358.'
  key: NambuJonaLasinio1961
  doi: 10.1103/PhysRev.122.345
- citation: 'W. A. Bardeen, C. T. Hill and M. Lindner, Minimal dynamical symmetry breaking of the standard model, Phys. Rev. D 41 (1990), 1647.'
  key: BardeenHillLindner1990
  doi: 10.1103/PhysRevD.41.1647
- citation: 'A. A. Osipov, B. Hiller, A. H. Blin, F. Palanca, J. Moreira and M. Sampaio, Top condensation model: a step towards the correct prediction of the Higgs mass, arXiv:1906.09579.'
  key: Osipov2019
  doi: 10.1140/epjc/s10052-020-08716-y
extraction:
  note: >-
    Imported so that the tower pairing-gap result can pin the pairing solution and the composite-Higgs literature it
    compares with instead of citing them from memory. Checked on 2026-11-01: the energy formula of (i) and the
    pairing-energy difference against Agrawal and Maheshwari, arXiv:2006.03909, Section 5.2 (H = -G S^+ S^-, (67);
    S^+ S^- = (1/4)(N - v)(2 Omega - N - v + 2), (77); E(n, v) - E(n, 0) = (G/4) v (2 Omega - v + 2), (78)); Kerman's
    reference (Ann. Phys. (NY) 12 (1961) 300) against the bibliography of arXiv:1401.7512, which gives no title (the
    title here is from memory); the bibliographic data of Nambu-Jona-Lasinio I and of Bardeen-Hill-Lindner against
    their INSPIRE records; arXiv:1906.09579 against its abstract page (title, authors, DOI; a model with
    SU(2)_L x U(1)_R symmetric four-fermion interactions breaking the electroweak symmetry through top and bottom
    condensates, giving a Higgs mass in accord with experiment, an improvement on the earlier m_h = 2 m_t, with
    anomalous U(1)_A breaking modifying the Nambu sum rule at next-to-leading order in 1/N_c). Cited from memory, not
    checked: the content of Nambu-Jona-Lasinio and of Bardeen-Hill-Lindner beyond the titles (the relation
    m_sigma = 2m at leading order, and m_h = 2 m_t at large N_c in top condensation), and the attribution of the
    quasi-spin method to Kerman beyond the bibliographic entry.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created by the maintainer pass of 2026-11-01 (Kerman''s quasi-spin solution, the NJL relation m_sigma = 2m, Bardeen-Hill-Lindner and arXiv:1906.09579 as a Fact, by Leon''s list of imports).'
---

## formal
\begin{enumerate}
\item[(i)] \emph{(Quasi-spin solution of degenerate pairing.)} For fermions in one level of pair degeneracy $\Omega$ with the pairing Hamiltonian $H = -GS^{+}S^{-}$, $S^{+} = \sum_{m > 0}a^{*}_{m}a^{*}_{\bar m}$ and $S^{-} = (S^{+})^{*}$, the operators $S^{\pm}$ and $S_{z} = \tfrac12(\hat N - \Omega)$ form an $\su(2)$ (quasi-spin), and the energies are $E(n, v) = -\tfrac{G}{4}(n - v)(2\Omega - n - v + 2)$ for $n$ particles of seniority $v$ (the number of unpaired particles); so a state of $p$ pairs with $v = 0$ has $E = -Gp(\Omega - p + 1)$ and breaking one pair costs $E(n, 2) - E(n, 0) = G\Omega$ \cite{Kerman1961, AgrawalMaheshwari2020}.
\item[(ii)] \emph{(Nambu and Jona-Lasinio.)} In the four-fermion model with dynamical mass $m$, at leading order the scalar ($\sigma$) bound state lies at $m_{\sigma} = 2m$, the threshold of pair breaking, beside the massless pseudoscalar \cite{NambuJonaLasinio1961}.
\item[(iii)] \emph{(Top condensation.)} If the electroweak symmetry is broken by a top-quark condensate, the composite Higgs boson has $m_{h} = 2m_{t}$ at leading order in $1/N_{c}$, lowered by gauge and Higgs corrections \cite{BardeenHillLindner1990}; a model with top and bottom condensates and anomalous $U(1)_{A}$ breaking obtains a composite Higgs mass in accord with the measured $125$ GeV \cite{Osipov2019}.
\end{enumerate}

## technical
Kerman's quasi-spin method solves the pairing model of nuclear physics exactly if all the levels are degenerate: the pair creation and annihilation operators form an $\su(2)$, so the energies follow from the Casimir and depend only on the particle number and the seniority, the number of unpaired particles. Breaking one pair costs the pairing strength times the pair degeneracy. Nambu and Jona-Lasinio found the particle-physics analogue: a fermion that gets its mass dynamically has a scalar partner at twice its mass. Assuming the top quark is the sole constituent, this gives the classic top-condensation prediction of a Higgs at twice the top mass, which more elaborate models with several condensates bring down to the observed value.

## lay
When particles pair up, as electrons do in a superconductor and nucleons in a nucleus, it costs a definite energy to break a pair, and for the simplest model this is known exactly. Particle physicists borrowed the idea: if the Higgs boson were a bound pair of top quarks, the simplest estimate puts it at twice the top's mass, far heavier than observed, though models with several kinds of pairs can bring it down. The series takes these results as given.

## one-liner
Degenerate pairing by quasi-spin: $E(n, v) = -\tfrac{G}{4}(n - v)(2\Omega - n - v + 2)$, pair-breaking gap $G\Omega$ (Kerman 1961); NJL $m_{\sigma} = 2m$; top condensation $m_{h} = 2m_{t}$ at leading order (Bardeen-Hill-Lindner), lowered to $125$ GeV with two condensates (Osipov et al.).
