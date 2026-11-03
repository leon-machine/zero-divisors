---
id: synthesis.imported-replica-wormhole-two-saddle-purity
kind: claim
version: 1
title: 'Imported: in the end-of-the-world-brane model the radiation''s purity is the disconnected saddle plus the replica wormhole, $1/k + Z_{2}/Z_{1}^{2}$, and the planar microcanonical spectrum is Page''s (Penington, Shenker, Stanford and Yang 2019)'
status: imported
region: synthesis
subject: entropy
tags: [entanglement, quantum-gravity, dictionaries]
proposed_by:
  kind: ai
  session: maintainer-2026-10-26
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
imported_from:
- citation: 'G. Penington, S. H. Shenker, D. Stanford and Z. Yang, Replica wormholes and the black hole interior, arXiv:1911.11977 (2019; v2 2020), Sec. 2.2, Eqs. (2.13)-(2.15), and Sec. 2.5.1.'
  key: PSSY2019
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: >-
      New imported Fact, created at Leon's decision of 2026-10-26 so that the replica-wormhole reading of
      synthesis.eviction-keeps-one-replica-saddle cites a stored Fact. Checked against the source on
      2026-10-26 (arXiv abstract page, v2 of 15 April 2020, and the full text): the section titles (2.2
      "Computation of the purity", 2.5 "Summation of planar geometries", 2.5.1 "Microcanonical ensemble:
      Page's result"), Eq. (2.13) as the sum of the disconnected and connected geometries giving
      $1/k + Z_2/Z_1^2$, Eq. (2.14) $Z_n \propto e^{S_0}$ (disk topology, Euler characteristic one), Eq. (2.15)
      $k^{-1} + e^{-S_0}$ marked schematic, the statement that the purity is $1/k$ when $k$ is small, the state $k^{-1/2}\sum_i \ket{\psi_i}_B\ket{i}_R$ of Sec. 2.1, Eq. (2.5), and in
      Sec. 2.5.1 the sentence that the resolvent equations (2.38) "are precisely the same ones found by Page for
      the entanglement spectrum of a subsystem of dimension $k$ in a random state of total dimension $ke^{S}$,
      in the planar approximation", with $S = \log m - m/2n$. The arXiv page lists no journal reference; a
      journal version was not checked. A bare $i$ does not occur; the statement is about an imported Hilbert
      space (the brane and radiation states), so no geometric-algebra unit is involved.
---

## formal
In the two-dimensional Jackiw-Teitelboim gravity model of an evaporating black hole whose interior ends on an end-of-the-world brane with $k$ mutually orthogonal internal states, each entangled with one state of a radiation system $R$, the state is $\ket{\Psi} = k^{-1/2}\sum_{i = 1}^{k}\ket{\psi_{i}}_{B}\ket{i}_{R}$ (Eq. (2.5)). Let $Z_{n}$ be the gravitational path integral on a disk-topology geometry whose boundary carries $n$ alternating asymptotic and brane segments; $kZ_{1}$ is the factor that normalises $\rho_{R}$. The gravitational computation of the purity of $\rho_{R}$ sums two geometries, the disconnected one (two disks) and the connected one (the replica wormhole):
\[
\operatorname{Tr}\rho_{R}^{2} = \frac{kZ_{1}^{2} + k^{2}Z_{2}}{(kZ_{1})^{2}} = \frac{1}{k} + \frac{Z_{2}}{Z_{1}^{2}} \qquad \text{(Eq. (2.13))},
\]
and since $Z_{n} \propto e^{S_{0}}$ for every $n$ (Eq. (2.14)), schematically $\operatorname{Tr}\rho_{R}^{2} = k^{-1} + e^{-S_{0}}$ (Eq. (2.15)): the disconnected saddle dominates for small $k$, the replica wormhole for $k$ large against $e^{S_{0}}$. Summing the planar geometries in the microcanonical ensemble of entropy $S$ (Sec. 2.5.1), the resolvent of $\rho_{R}$ obeys the equations found by Page for the entanglement spectrum of a subsystem of dimension $k$ in a random pure state of total dimension $ke^{S}$, so the von Neumann entropy follows Page's curve, $S(\rho_{R}) \simeq \log m - m/2n$ with $m = \min(k, e^{S})$, $n = \max(k, e^{S})$. \emph{Provenance:} \cite{PSSY2019}, Sec. 2.2 and Sec. 2.5.1.

## technical
Penington, Shenker, Stanford and Yang computed the entropy of Hawking radiation in a toy model of an evaporating black hole by the replica trick, letting the gravitational path integral include geometries that connect the replicas. For the purity, the second Renyi quantity, only two geometries contribute: the disconnected one, which gives $1/k$ for $k$ radiation states, and the replica wormhole, which gives $Z_{2}/Z_{1}^{2}$, of order $e^{-S_{0}}$ with $S_{0}$ the black hole's entropy. Their sum switches dominance at the Page time. Summing all planar geometries in the microcanonical ensemble reproduces exactly Page's random-state formula for the entanglement spectrum, so the island computation reproduces the Page-typical branch, including its subleading shape, in this model.

## lay
In 2019 four physicists showed how the entropy of a black hole's radiation can follow Page's curve, rising and then falling, when the calculation includes wormholes joining copies of the black hole. In the simplest measure of mixing two shapes of spacetime contribute, one dominating early and one late, and the full sum reproduces exactly the formula Page found for a randomly chosen quantum state. The series uses this to compare its own account of information return with the wormhole calculation.

## one-liner
In the end-of-the-world-brane model the radiation's purity is $1/k + Z_{2}/Z_{1}^{2}$, schematically $k^{-1} + e^{-S_{0}}$ (disconnected saddle plus replica wormhole), and the planar microcanonical sum reproduces Page's random-state spectrum (Penington, Shenker, Stanford and Yang 2019).
