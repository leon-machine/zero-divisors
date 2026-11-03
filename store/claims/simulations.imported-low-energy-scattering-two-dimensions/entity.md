---
id: simulations.imported-low-energy-scattering-two-dimensions
kind: claim
version: 1
title: 'Imported: low-energy scattering in two dimensions'
status: imported
region: simulations
subject: dark-matter
tags: [classical-theorem, halos-and-clusters]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14b, deposited version
review: typed
imported_from:
- citation: S. K. Adhikari, Quantum scattering in two dimensions, Am. J. Phys. 54 (1986) 362.
  key: Adhikari1986
locators:
  paper: T14b
  number: Fact 3.2
  label: fact:2d
  line: 195
extraction:
  typing:
    by: ai-typing-pass
    note: Imported textbook scattering result; levels only, no edges to review.
  env: fact
---

## formal
For elastic scattering in two dimensions by a hard disk of radius $a$, the partial-wave phase shifts are $\tan\delta_{m} = J_{m}(ka)/Y_{m}(ka)$ and the total cross-section is the length $\lambda = (4/k)\sum_{m=-\infty}^{\infty}\sin^{2}\delta_{m}$. As $ka \to 0$ only $m = 0$ survives, with $\delta_{0} \to \pi/\bigl(2(\ln(ka/2) + \gamma_{E})\bigr)$; the same logarithmic form holds for any short-range interaction with two-dimensional scattering length of order $a$. \emph{Provenance:} \cite{Adhikari1986}.

## technical
For elastic scattering in two dimensions by a hard disk of radius $a$, the partial-wave phase shifts satisfy $\tan\delta_{m} = J_{m}(ka)/Y_{m}(ka)$, and the total cross-section is a length, $\lambda = (4/k)\sum_{m}\sin^{2}\delta_{m}$. As $ka \to 0$ only the s-wave survives, with $\delta_{0} \to \pi/\bigl(2(\ln(ka/2) + \gamma_{E})\bigr)$, so the radius enters only logarithmically. The same logarithmic form holds for any short-range interaction whose two-dimensional scattering length is of order $a$.

## lay
In a flat, two-dimensional world a particle's target size for collisions is a length rather than an area. At low energies this length depends on the particle's actual size only through a logarithm, so even a very tiny particle remains a surprisingly large target. This is a standard result of quantum scattering theory.

## one-liner
In two dimensions, low-energy scattering by a disk of radius $a$ is pure s-wave with $\delta_{0} \to \pi/\bigl(2(\ln(ka/2) + \gamma_{E})\bigr)$, so the cross-section length depends on $a$ only logarithmically.
