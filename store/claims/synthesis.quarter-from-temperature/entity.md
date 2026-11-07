---
id: synthesis.quarter-from-temperature
kind: claim
version: 1
title: The quarter from the series' temperature, by Hawking's argument
status: proved
region: synthesis
subject: entropy
tags: [hawking-temperature, mode-counting, recovers-known-physics]
proposed_by:
  kind: ai
  session: residue-2026-10-22
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
derivations:
- name: main
  uses:
  - singularity.rate-discharge-hypothesis-iii@6
  - singularity.plane-rate@4
  assumes:
  - singularity.p-univalence@2
  - singularity.r-regularity-fixed-locus@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_quarter
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - scrambling.residue-each-convention
  - singularity.area-law-test
extraction:
  note: T08 records that deriving the calibration residue is equivalent to deriving Bekenstein-Hawking's quarter. This result shows the quarter is not an independent input once (R) fixes the temperature and the boundary modes are taken to be the hole's thermodynamic system; it is Hawking's own argument, run on the series' temperature.
---

## formal
Assume (P) (Premise \claimref{singularity.p-univalence}) and (R) (Premise \claimref{singularity.r-regularity-fixed-locus}), so that the boundary modes of a Schwarzschild hole of mass $M$ are thermal at $T(M) = \kappa/2\pi = 1/8\pi M$ (Theorem \claimref{singularity.rate-discharge-hypothesis-iii}, Proposition \claimref{singularity.plane-rate}). Suppose, as Hawking did, that the hole is a thermodynamic system along the Schwarzschild family at this temperature: its internal energy is $M$ (not the boundary modes' Killing energy, which is below $TS = M/2$), its entropy $S(M)$ obeys the Clausius relation $dS = dM/T$, and $S \to 0$ as $M \to 0$. Then
\[
S(M) \;=\; \int_{0}^{M} 8\pi M'\,dM' \;=\; 4\pi M^{2} \;=\; \frac{A}{4}, \qquad A = 16\pi M^{2},
\]
the Bekenstein-Hawking entropy with its quarter, and no calibration enters. Equivalently, along the family $dM = (\kappa/8\pi)\,dA$ identically, so $dS = dA/4$. The quarter is fixed by the period of (R), $2\pi/\kappa$, and by nothing else: had (R) fixed a period $p$ in place of $2\pi/\kappa$, the entropy would be $S = (p\kappa/2\pi)\,A/4$.

## technical
The singularity paper fixes the black hole's temperature at $1/8\pi M$, given its regularity premise (R). If the hole is an ordinary thermodynamic system at that temperature, its mass the internal energy and its entropy changing by $dM/T$ when the mass changes, then integrating gives exactly $4\pi M^{2}$, a quarter of the horizon area. This is Hawking's original argument for the quarter, run on the series' own temperature, and it is standard physics rather than a new result. What it shows for the series is that the quarter is not a separate calibration: it is fixed by the period in (R). It does not say which modes carry the entropy. A different period would rescale the entropy by the same factor.

## lay
The famous factor of one quarter in a black hole's entropy is not an extra number the framework has to supply. Once the framework fixes the hole's temperature, as it does under one smoothness assumption, the ordinary law linking heat, energy and entropy gives the entropy as a quarter of the horizon's area, provided the hole behaves as an ordinary thermodynamic system; this is Hawking's argument, and it does not by itself say which modes carry the entropy.

## one-liner
Under (P), (R) and the Clausius relation for the hole (Hawking's argument), $S = \int dM/T = 4\pi M^{2} = A/4$: the quarter is fixed by the period of (R).
