---
id: standard-model.imported-one-loop-running-trace-ratio
kind: claim
version: 1
title: 'Imported: one-loop running, and the trace ratio of a simple unifying group'
status: imported
region: standard-model
subject: standard-model
tags: [classical-theorem, running-and-unification]
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
- citation: H. Georgi and S. L. Glashow, Unity of all elementary-particle forces, Phys. Rev. Lett. 32
    (1974), 438--441.
  key: GeorgiGlashow1974
- citation: U. Amaldi, W. de Boer, and H. F"urstenau, Comparison of grand unified theories with electroweak
    and strong coupling constants measured at LEP, Phys. Lett. B 260 (1991), 447--455.
  key: Amaldi1991
- citation: S. Navas et al. (Particle Data Group), Review of particle physics, Phys. Rev. D 110 (2024),
    030001.
  key: PDG2024
locators:
  paper: T12
  number: Fact 2.8
  label: fact:running
  line: 907
extraction:
  env: fact
  typing:
    by: ai-typing-pass
    note: Imported fact; levels only, no edges to review.
---

## formal
(a) In the normalisation $a_{1} = \tfrac35\,\alpha_{Y}^{-1}$, $a_{2} = \alpha_{2}^{-1}$, $a_{3} = \alpha_{s}^{-1}$, the one-loop renormalisation group gives $a_{i}(\mu) = a_{i}(M_{Z}) - \tfrac{b_{i}}{2\pi}\ln(\mu/M_{Z})$, with $(b_{1}, b_{2}, b_{3}) = (\tfrac{41}{10}, -\tfrac{19}{6}, -7)$ for the Standard Model with one Higgs doublet and $(\tfrac{33}{5}, 1, -3)$ for its minimal supersymmetric extension; the matching relations at $M_{Z}$ are $\alpha_{\mathrm{em}}^{-1} = \tfrac53 a_{1} + a_{2}$ and $\sin^{2}\theta_{W} = \alpha_{\mathrm{em}}/\alpha_{2} = \alpha_{\mathrm{em}}\,a_{2}$. (b) If the gauge group is contained in a simple group $G_{U}$ and the fermion content forms a representation of $G_{U}$, then the three couplings are equal at the scale where $G_{U}$ is unbroken, in the normalisation in which $\sin^{2}\theta_{W} = \sum T_{3}^{2}/\sum Q^{2}$, the sums over any representation of $G_{U}$; the normalisation is forced because a simple Lie algebra carries a unique invariant form up to scale. \emph{Provenance:} \cite{GeorgiGlashow1974} for (b); \cite{Amaldi1991} and \cite{PDG2024} for the coefficients and the matching in (a). Both are imported at assembly level: (a) is perturbation theory, (b) is the grand-unification hypothesis that a simple $G_{U}$ exists.

## technical
(a) With $a_{1} = \tfrac35\alpha_{Y}^{-1}$, $a_{2} = \alpha_{2}^{-1}$ and $a_{3} = \alpha_{s}^{-1}$, one-loop running is linear in the logarithm of the scale, $a_{i}(\mu) = a_{i}(M_{Z}) - \tfrac{b_{i}}{2\pi}\ln(\mu/M_{Z})$, with $(b_{1}, b_{2}, b_{3}) = (\tfrac{41}{10}, -\tfrac{19}{6}, -7)$ for the Standard Model with one Higgs doublet and $(\tfrac{33}{5}, 1, -3)$ for its minimal supersymmetric extension; at $M_{Z}$, $\alpha_{\mathrm{em}}^{-1} = \tfrac53 a_{1} + a_{2}$ and $\sin^{2}\theta_{W} = \alpha_{\mathrm{em}}\,a_{2}$.

(b) If the gauge group lies in a simple group $G_{U}$ under which the fermions form a representation, the three couplings are equal where $G_{U}$ is unbroken, in the normalisation $\sin^{2}\theta_{W} = \sum T_{3}^{2}/\sum Q^{2}$ over any representation of $G_{U}$; the uniqueness of the invariant form on a simple algebra forces that normalisation. Part (a) is perturbation theory and part (b) is the grand-unification hypothesis that such a $G_{U}$ exists, both imported at assembly level.

## lay
The strengths of the three forces change slowly with energy, and at the first approximation each inverse strength changes along a straight line against the logarithm of the energy, with a slope set by the particle content. If all three forces are pieces of one larger simple symmetry, their strengths must agree at the energy where that symmetry is intact, once they are measured on the common scale the larger symmetry fixes. Both statements are standard and taken from the literature, the second being the working hypothesis of grand unification.

## one-liner
At one loop the inverse couplings run linearly in $\ln\mu$ with the stated coefficients, and if a simple unifying group exists they meet in the normalisation fixed by its trace ratios.
