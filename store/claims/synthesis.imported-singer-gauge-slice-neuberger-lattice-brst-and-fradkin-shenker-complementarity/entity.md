---
id: synthesis.imported-singer-gauge-slice-neuberger-lattice-brst-and-fradkin-shenker-complementarity
kind: claim
version: 1
title: 'Imported: no continuous gauge-fixing condition exists for a non-abelian gauge field on the three- or four-sphere (Singer 1978); a lattice BRST gauge fixing of a compact gauge group gives a vanishing partition function and expectation values 0/0, the Gribov copies cancelling in pairs with the signs of the Faddeev-Popov determinant (Neuberger 1987); and with Higgs fields of fixed length in the fundamental representation the Higgs and confinement regions of a lattice gauge theory are analytically connected (Fradkin and Shenker 1979)'
status: imported
region: synthesis
subject: quantum-fields
tags: [gauge-fields, no-go, classical-theorem]
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
- citation: 'I. M. Singer, Some remarks on the Gribov ambiguity, Commun. Math. Phys. 60 (1978), no. 1, 7--12.'
  key: Singer1978
- citation: 'G. Esposito, D. N. Pelliccia and F. Zaccaria, Gribov problem for gauge theories: a pedagogical introduction, arXiv:hep-th/0404240.'
  key: EspositoPellicciaZaccaria2004
  doi: 10.1142/S0219887804000216
  locator: 'the paragraph citing Singer: for SU(N) on S^3 or S^4 no gauge-fixing condition compatible with the asymptotic conditions exists; no global cross-section of the Yang-Mills bundle'
- citation: 'H. Neuberger, Nonperturbative BRS invariance and the Gribov problem, Phys. Lett. B 183 (1987), 337--340.'
  key: Neuberger1987
- citation: 'A. C. Kalloniatis, L. von Smekal and A. G. Williams, Curci-Ferrari mass and the Neuberger problem, arXiv:hep-lat/0501016.'
  key: KalloniatisVonSmekalWilliams2005
  doi: 10.1016/j.physletb.2005.01.061
  locator: 'introduction: the lattice BRST partition function and the integrals of BRST-invariant observables are topological invariants, the Euler character of SU(n), which vanishes, so expectation values are 0/0'
- citation: 'E. Fradkin and S. H. Shenker, Phase diagrams of lattice gauge theories with Higgs fields, Phys. Rev. D 19 (1979), 3682--3697.'
  key: FradkinShenker1979
  doi: 10.1103/PhysRevD.19.3682
extraction:
  note: >-
    Imported so that the result on Gribov copies and the perimeter law of the weak rotor lattice can pin these
    sources instead of citing them from memory. Checked on 2026-11-02: Singer, journal volume and issue (60, no. 1)
    from the Project Euclid record of "Some remarks on the Gribov ambiguity", and the content (for SU(N) on S^3 or S^4
    no gauge-fixing condition compatible with the asymptotic conditions; no global cross-section) against the
    pedagogical review arXiv:hep-th/0404240 (which prints the volume as 64, against the Project Euclid record);
    Neuberger, the journal reference (Phys. Lett. B 183 (1987) 337) and the content (the vanishing lattice BRST
    partition function, Gribov copies summed with alternating signs of the Faddeev-Popov determinant, expectation
    values 0/0, the Euler character of SU(n)) against arXiv:hep-lat/0501016; Fradkin and Shenker, journal, volume,
    first page and year against the APS record and the content (fixed-length Higgs fields in the fundamental
    representation: Higgs and confining phases analytically connected; a boundary possible for other
    representations; a free-charge phase) against its abstract. Not checked: the page ranges of Singer and Neuberger
    and of Fradkin-Shenker beyond the first page, and the title of Neuberger 1987 (from memory). The extension from
    SU(n) to every compact connected Lie group of positive dimension (Euler characteristic zero) is standard topology,
    not taken from the sources.
  maintainer_pass:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Created by the maintainer pass of 2026-11-02 (Neuberger 1987, Fradkin-Shenker 1979 and Singer 1978 as a Fact, by Leon''s list of routine imports).'
---

## formal
\begin{enumerate}
\item[(i)] \emph{(No continuous gauge slice.)} For the gauge group $SU(N)$, $N \ge 2$, on the three-sphere or the four-sphere (a compactified spatial slice or a compactified Euclidean spacetime), the space of connections does not admit a continuous gauge-fixing condition: there is no global continuous section of the bundle of connections over the gauge orbits, so every continuous gauge condition has Gribov copies \cite{Singer1978, EspositoPellicciaZaccaria2004}.
\item[(ii)] \emph{(Lattice BRST gives 0/0.)} On a finite lattice with a compact gauge group, the BRST gauge-fixed integral of a BRST-invariant observable is a topological invariant: the Gribov copies on each orbit are summed with the signs of the Faddeev-Popov determinant, giving the Euler characteristic of the gauge group, which is zero for $SU(n)$ (and for every compact connected Lie group of positive dimension); so the partition function vanishes and expectation values are $0/0$ \cite{Neuberger1987, KalloniatisVonSmekalWilliams2005}.
\item[(iii)] \emph{(Complementarity.)} In a lattice gauge theory with Higgs fields of fixed length in the fundamental representation of the gauge group, the Higgs region and the confinement region of the phase diagram are analytically connected, with no phase boundary between them; for Higgs fields in other representations (the adjoint, or charge two for $U(1)$) a boundary can exist; a free-charge phase is generally present \cite{FradkinShenker1979}.
\end{enumerate}

## technical
These are the standard non-perturbative limits of gauge fixing and the standard phase structure of lattice gauge theories with Higgs fields. Singer showed that Gribov's observation is topological: on the three- or four-sphere no continuous condition picks one representative from every gauge orbit of a non-abelian field. Neuberger showed that a BRST gauge fixing on the lattice fails globally: summing over the Gribov copies with the signs of their Faddeev-Popov determinants gives the Euler characteristic of the compact gauge group, zero, so the partition function and every expectation value become $0/0$. Fradkin and Shenker showed that with a Higgs field in the fundamental representation the Higgs and confining regimes of a lattice gauge theory are one phase: no sharp order parameter separates them.

## lay
Describing the force fields of particle physics involves a redundancy, and the usual ways of removing it work only for weak fields. Singer proved that no smooth way of removing it works everywhere; Neuberger showed that the standard bookkeeping, done on a lattice of spacetime points, gives zero divided by zero; and Fradkin and Shenker showed that a force field with a Higgs field of the simplest kind has no sharp boundary between a regime where its charges are confined and one where its particles are massive. The series takes these results from the literature.

## one-liner
Singer 1978: no continuous gauge slice for $SU(N)$ on $S^{3}$ or $S^{4}$; Neuberger 1987: lattice BRST partition function is the Euler characteristic of the compact group, zero, so expectation values are $0/0$; Fradkin-Shenker 1979: with fundamental Higgs fields the Higgs and confinement regions are analytically connected.
