---
id: standard-model.imported-proton-condition
kind: claim
version: 1
title: 'Imported: the proton condition'
status: imported
region: standard-model
subject: standard-model
tags: [classical-theorem, running-and-unification, confronted-with-data]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T12, deposited version
review: typed
imported_from:
- citation: 'S. Bertolini, L. Di Luzio and M. Malinsk''y, Intermediate mass scales in the non-supersymmetric
    $SO(10)$ grand unification: a reappraisal, Phys. Rev. D 80 (2009) 015013, arXiv:0903.4049.'
  key: BertoliniDiLuzioMalinsky2009
- citation: Super-Kamiokande Collaboration (A. Takenaka et al.), Search for proton decay via $p to e^+pi^0$
    and $p to mu^+pi^0$ with an enlarged fiducial volume in Super-Kamiokande I-IV, Phys. Rev. D 102 (2020)
    112011, arXiv:2010.16098.
  key: SuperK2020
locators:
  paper: T12
  number: Fact 8.21
  label: fact:proton
  line: 1497
extraction:
  env: fact
  typing:
    by: ai-typing-pass
    note: Imported fact; levels only, no edges to review.
---

## formal
Gauge-boson exchange at the unification scale gives $p \to e^{+}\pi^{0}$ with lifetime
\[
\tau_{p} \;\simeq\; 1.6 \times 10^{33}\ \text{yr} \times \left[\frac{1}{5.2}\,\frac{\alpha_{U}^{-1}}{45}\Bigl(\frac{M_{U}}{10^{15}\ \text{GeV}}\Bigr)^{2}\right]^{2},
\]
and the Super-Kamiokande limit is $\tau_{p}/B(p \to e^{+}\pi^{0}) > 2.4 \times 10^{34}$ yr at $90$ percent confidence. A spectrum meets the \emph{proton condition} if its $\tau_{p}$ exceeds the limit, that is if
\[
\frac{\alpha_{U}^{-1}}{45}\Bigl(\frac{M_{U}}{10^{15}\ \text{GeV}}\Bigr)^{2} \;>\; 5.2\sqrt{15} \;\approx\; 20.1,
\]
which is $M_{U} > 4.5 \times 10^{15}$ GeV at $\alpha_{U}^{-1} = 45$ and $M_{U} > 5.9 \times 10^{15}$ GeV at $\alpha_{U}^{-1} = 25.7$. \emph{Provenance:} the lifetime normalisation is that of Bertolini, Di Luzio and Malinsky \cite{BertoliniDiLuzioMalinsky2009}, scaled to the limit of \cite{SuperK2020}; assembly level, the hadronic matrix elements moving the bound on $M_{U}$ by a factor of order two.

## technical
Gauge-boson exchange at the unification scale gives $p \to e^{+}\pi^{0}$ with $\tau_{p} \simeq 1.6 \times 10^{33}\ \text{yr} \times \bigl[\tfrac{1}{5.2}\tfrac{\alpha_{U}^{-1}}{45}(M_{U}/10^{15}\ \text{GeV})^{2}\bigr]^{2}$, to be compared with the Super-Kamiokande limit $\tau_{p}/B(p \to e^{+}\pi^{0}) > 2.4 \times 10^{34}$ yr at $90$ percent confidence.

A spectrum meets the proton condition when $\tfrac{\alpha_{U}^{-1}}{45}(M_{U}/10^{15}\ \text{GeV})^{2} > 5.2\sqrt{15} \approx 20.1$, which is $M_{U} > 4.5 \times 10^{15}$ GeV at $\alpha_{U}^{-1} = 45$ and $M_{U} > 5.9 \times 10^{15}$ GeV at $\alpha_{U}^{-1} = 25.7$. The normalisation is imported at assembly level, and the hadronic matrix elements move the bound on $M_{U}$ by a factor of order two.

## lay
Grand unified theories predict that protons eventually decay, at a rate that falls steeply as the unification energy rises. Experiments have not seen proton decay and set a lower limit on the proton's lifetime. Combining a standard estimate of the decay rate with that limit gives a minimum unification energy of a few times ten to the fifteen GeV, and a candidate spectrum passes the proton condition if it unifies above it. The estimate is taken from the literature and is uncertain by about a factor of two.

## one-liner
A unification spectrum meets the proton condition when $\tfrac{\alpha_{U}^{-1}}{45}(M_{U}/10^{15}\ \text{GeV})^{2}$ exceeds about $20.1$, the Super-Kamiokande bound on $p \to e^{+}\pi^{0}$.
