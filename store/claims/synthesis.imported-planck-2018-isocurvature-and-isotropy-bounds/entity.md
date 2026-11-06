---
id: synthesis.imported-planck-2018-isocurvature-and-isotropy-bounds
kind: claim
version: 1
title: 'Imported: Planck 2018 isocurvature and isotropy bounds'
status: imported
region: synthesis
subject: dark-energy
tags: [confronted-with-data]
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
- citation: 'Y. Akrami et al. (Planck Collaboration), Planck 2018 results. X. Constraints on inflation, Astron. Astrophys. 641 (2020), A10; arXiv:1807.06211.'
  key: Planck2018X
  locator: 'abstract; Sections 9 and 10'
  doi: 10.1051/0004-6361/201833887
extraction:
  note: >-
    Imported so that synthesis.adiabatic-deposit-modulation-is-a-time-shift can pin the isocurvature
    bound, and the two Kasner-mode results the statistical isotropy of the record, which they cited.
    Checked on 2026-11-01 against arXiv:1807.06211 (abstract page and PDF): title, collaboration,
    DOI; the abstract's statement that for correlated mixed adiabatic and isocurvature models the
    non-adiabatic contribution to the observed CMB temperature variance is constrained to 1.3, 1.7
    and 1.7 percent at 95 percent confidence for cold dark matter, neutrino density and neutrino
    velocity; Section 9 (isocurvature) and Section 10 (anisotropic models of inflation, with the
    quadrupolar modulation in 10.2 and the dipolar in 10.1); the abstract's statements that the
    polarisation data improve the constraints on a small statistically anisotropic quadrupolar
    modulation and do not support physical models of a scale-dependent dipolar modulation. Not
    checked (the PDF text available ended before Section 9): the numerical bound on the quadrupolar
    amplitude g_*, recorded only as of order one percent from memory, and the uncorrelated
    isocurvature fractions. The journal volume and article number are from memory, consistent with
    the DOI.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created by the maintainer pass of 2026-11-01 (Leon approved the import of the Planck 2018 isocurvature bounds and statistical isotropy as routine Facts).'
---

## formal
In the base model with power-law spectra, Planck 2018 temperature and polarisation data constrain correlated mixtures of the adiabatic mode with one isocurvature mode: the non-adiabatic contribution to the observed CMB temperature variance is below $1.3\%$ for cold-dark-matter density isocurvature, $1.7\%$ for neutrino density isocurvature and $1.7\%$ for neutrino velocity isocurvature, at $95\%$ confidence (Section 9). The data show no evidence of statistical anisotropy of the primordial fluctuations: a small quadrupolar modulation of the primordial power spectrum, $\mathcal{P}(\mathbf{k}) = \mathcal{P}(k)(1 + g_{*}(\hat{\mathbf{k}}\cdot\hat{\mathbf{d}})^{2})$, is constrained (Section 10.2; $|g_{*}|$ at the level of a few times $10^{-2}$, not checked here), and physical models of a scale-dependent dipolar modulation are not supported by the polarisation data (Section 10.1). So the measured primordial spectrum has the same index in every direction to that precision. \emph{Provenance:} \cite{Planck2018X} (abstract, Sections 9 and 10).

## technical
Besides the amplitude and tilt of the primordial spectrum, the Planck data test two of its properties. One is adiabaticity: perturbations in which every component fluctuates together, against modes in which the dark matter or the neutrinos fluctuate relative to the photons; such isocurvature modes can supply at most a percent or two of the temperature variance. The other is statistical isotropy: a dependence of the primordial power on direction, quadrupolar or dipolar, is not seen. A primordial source must produce an adiabatic, isotropic spectrum to that accuracy.

## lay
The Planck satellite's final data show that the primordial ripples are of the kind in which all the ingredients of the universe fluctuate together, with any other kind contributing at most one or two percent, and that the ripples look the same in every direction on the sky.

## one-liner
Planck 2018: non-adiabatic share of the temperature variance below $1.3\%$ (CDM), $1.7\%$ (neutrino density), $1.7\%$ (neutrino velocity) at $95\%$ CL, and no quadrupolar or dipolar anisotropy of the primordial spectrum.
