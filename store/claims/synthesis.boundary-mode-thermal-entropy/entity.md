---
id: synthesis.boundary-mode-thermal-entropy
kind: claim
version: 2
title: The thermal entropy of one boundary mode, and its maximum at zero weight
status: proved
region: synthesis
subject: entropy
tags: [boundary-modes, mode-counting, thermal-premises]
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
  - singularity.rate-discharge-hypothesis-iii@4
  assumes:
  - singularity.p-univalence@2
  - singularity.r-regularity-fixed-locus@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_mode_entropy
- kind: proof
  derivation: main
extraction:
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 1 -> 2.'
  flow_note: phase flow e^{-i omega t} on the modes (the T05 Thm 7.16 sense); x is the weight in units of the temperature.
  note: Part of the attempt (22 October 2026) to settle the calibration residue of T08. The capacity convention credits every fermionic mode with ln 2 nats; this result says exactly when a mode at the series' temperature carries that much.
---

## formal
Assume (P) (Premise \claimref{singularity.p-univalence}) and (R) (Premise \claimref{singularity.r-regularity-fixed-locus}), so that a boundary mode of Killing weight $\omega$ has the marginal $\operatorname{diag}(1 - n, n)$ with $n = 1/(e^{x} + 1)$, $x = 2\pi\omega/\kappa$ (Theorem \claimref{singularity.rate-discharge-hypothesis-iii}). Its von Neumann entropy is
\[
s(x) \;=\; -n\ln n - (1 - n)\ln(1 - n) \;=\; \ln\bigl(1 + e^{-x}\bigr) + \frac{x}{e^{x} + 1} ,
\]
an even function with $s'(x) = -x\,n(1 - n)$, so that $s$ is strictly decreasing in $|x|$, $s(0) = \ln 2$ and $s(x) \to 0$ as $|x| \to \infty$. Hence $s \le \ln 2$, with equality exactly at zero weight: the capacity $\ln 2$ that the singularity paper credits to every fermionic mode is the mode's thermal entropy exactly when the mode has zero Killing weight, the one mode at which (R) fixes the occupancy $n = \tfrac12$ without fixing a temperature. At the first nonzero weight of the s-wave convention, $\omega = \kappa$ ($x = 2\pi$), $s = 0.01358\ldots$, under two per cent of $\ln 2$.

## technical
At the series' temperature a boundary mode is a fermion in a Fermi-Dirac state, and its entropy is the familiar $s(x) = \ln(1 + e^{-x}) + x/(e^{x} + 1)$, with $x$ the mode's Killing energy in units of the temperature. That entropy is largest, $\ln 2$, for a mode of zero energy, which is maximally mixed, and falls off quickly: a mode with energy equal to the surface gravity carries under two per cent of $\ln 2$. The singularity paper's capacity convention credits every mode with $\ln 2$. That is a mode's actual thermal entropy only when the mode has zero weight.

## lay
Each quantum mode on the boundary of a black hole holds at most one bit of information. At the hole's temperature, a mode actually holds a full bit only if it carries no energy, so that it is as likely full as empty. A mode with even a modest energy holds almost nothing: at the lowest energy the usual convention assigns, it holds less than a fiftieth of a bit.

## one-liner
Under (P) and (R), at the series' temperature a boundary mode of weight $\omega$ carries $s = \ln(1 + e^{-x}) + x/(e^{x} + 1)$ nats, $x = 2\pi\omega/\kappa$, which is $\ln 2$ exactly when $\omega = 0$.
