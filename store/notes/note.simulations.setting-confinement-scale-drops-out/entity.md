---
id: note.simulations.setting-confinement-scale-drops-out
kind: note
version: 1
title: The confinement scale drops out
status: setting
subject: dark-matter
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14b, deposited version
comments_on:
- simulations.confinement-scale-does-not-matter
- simulations.imported-low-energy-scattering-two-dimensions
- simulations.effective-cross-section-sheet-matter
locators:
  paper: T14b
  number: Setting
  section: Self-interaction within a sheet
  line: 208
  subsection: The confinement scale drops out
---

## formal
\textbf{How it is computed.} (i) is Fact \claimref{simulations.imported-low-energy-scattering-two-dimensions} evaluated at $ka = 0.0050$ and $ka = 2.4 \times 10^{-13}$, with $\mu = m/2$; the script computes the Bessel functions by their series and the partial-wave sum to $m = \pm 1$. (ii) is Proposition \claimref{simulations.effective-cross-section-sheet-matter} with $s = 3.5$ cm solved for $\lambda$. (iii) With the s-wave alone $\lambda = 4\sin^{2}\delta_{0}/k$, so $\lambda < 4.8 \times 10^{-12}$ fm gives $\delta_{0} < 1.7 \times 10^{-7}$; in the logarithmic form $\lambda \approx \pi^{2}/\bigl(k(\ln(ka/2) + \gamma_{E})^{2}\bigr)$, so the bound requires $|\ln(ka/2) + \gamma_{E}| > 9.3 \times 10^{6}$, that is $a < 10^{-4.0 \times 10^{6}}$ fm. These are floating-point evaluations, checked in the script (Section \ref{sec:verification}); nothing below depends on their digits beyond the first.

## technical
pending

## lay
pending

## one-liner
pending
