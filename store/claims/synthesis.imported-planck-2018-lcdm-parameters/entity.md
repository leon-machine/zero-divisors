---
id: synthesis.imported-planck-2018-lcdm-parameters
kind: claim
version: 2
title: 'Imported: the base-$\Lambda$CDM parameters of Planck 2018 (Planck Collaboration 2020) and the radiation density they imply'
status: imported
region: synthesis
subject: dark-energy
tags: [confronted-with-data, cosmological-constant, recovers-known-physics]
proposed_by:
  kind: ai
  session: maintainer-2026-10-23
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
imported_from:
- citation: 'N. Aghanim et al. (Planck Collaboration), Planck 2018 results. VI. Cosmological parameters, Astron. Astrophys. 641 (2020), A6.'
  key: Planck2018
  doi: 10.1051/0004-6361/201833910
- citation: 'D. J. Fixsen, The temperature of the cosmic microwave background, Astrophys. J. 707 (2009), 916--920.'
  key: Fixsen2009
extraction:
  note: >-
    Imported so that synthesis.finite-range-descent-deposit-cannot-seed-cmb can pin its record
    inputs instead of citing them from memory. Checked on 2026-10-23 against the source: the
    abstract of arXiv:1807.06209 (H_0 = 67.4 +- 0.5, Omega_m = 0.315 +- 0.007, n_s = 0.965 +-
    0.004), Table 2 of the A&A version, column TT,TE,EE+lowE+lensing (ln(10^10 A_s) = 3.044 +-
    0.014, 10^9 A_s = 2.100 +- 0.030, n_s = 0.9649 +- 0.0042, H_0 = 67.36 +- 0.54, Omega_m =
    0.3153 +- 0.0073), and Section 2.1 of the paper (A_s defined at the pivot k = 0.05 Mpc^-1;
    three neutrino species; T_0 = 2.7255 K, citing Fixsen 2009). The radiation density is not a
    Planck parameter: it is computed here from T_0 by the standard blackbody formula with the
    standard neutrino factor at N_eff = 3.046 (formula and N_eff from memory; arithmetic redone in
    floating point), giving Omega_r h^2 = 4.18 x 10^-5. Fixsen 2009 bibliographic data and the
    DOI of the Planck paper are from memory (the DOI is consistent with the A&A article number
    aa33910-18).
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Created by the maintainer pass (the fix round asked for the Planck record values that the finite-range descent result cites from memory to be imported as a Fact).'
  maintainer_pass_five_fronts:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2: the baryon and cold dark matter densities Omega_b h^2 = 0.02237 +- 0.00015 and Omega_c h^2 = 0.1200 +- 0.0012 added (Leon approved their import), so that synthesis.adiabatic-deposit-modulation-is-a-time-shift can pin them; checked on 2026-11-01 against Table 1 of the A&A version (base LCDM from TT,TE,EE+lowE+lensing, Plik column; the CamSpec and combined columns give 0.02229, 0.02233 and 0.1197, 0.1198). The other values are unchanged.'
---

## formal
In the base six-parameter $\Lambda$CDM model fitted to the Planck 2018 temperature, polarisation and lensing data (TT,TE,EE+lowE+lensing, 68\% limits), with three neutrino species (two massless and one of mass $0.06$ eV) and CMB temperature $T_{0} = 2.7255$ K \cite{Fixsen2009}: the Hubble constant is $H_{0} = 67.36 \pm 0.54$ km s$^{-1}$ Mpc$^{-1}$ (quoted in the abstract as $67.4 \pm 0.5$), the matter density parameter $\Omega_{m} = 0.3153 \pm 0.0073$ (quoted in the abstract as $0.315 \pm 0.007$), the amplitude of the primordial curvature perturbations at the pivot $k_{*} = 0.05$ Mpc$^{-1}$ is $\ln(10^{10}A_{s}) = 3.044 \pm 0.014$, that is $A_{s} = (2.100 \pm 0.030) \times 10^{-9}$, the scalar spectral index is $n_{s} = 0.9649 \pm 0.0042$, the physical baryon density $\Omega_{b}h^{2} = 0.02237 \pm 0.00015$ and the physical cold dark matter density $\Omega_{c}h^{2} = 0.1200 \pm 0.0012$ (Table 1 of the A\&A version, the Plik column); the model is spatially flat, $\Omega_{\Lambda} = 1 - \Omega_{m} - \Omega_{r}$. The radiation density these imply, photons at $T_{0}$ with three neutrino species relativistic at $N_{\mathrm{eff}} = 3.046$, is $\Omega_{r}h^{2} = \Omega_{\gamma}h^{2}\bigl(1 + \tfrac78(\tfrac{4}{11})^{4/3}N_{\mathrm{eff}}\bigr) = 4.18 \times 10^{-5}$ with $\Omega_{\gamma}h^{2} = 2.47 \times 10^{-5}$, so $\Omega_{r} = 9.2 \times 10^{-5}$ at $h = 0.674$. \emph{Provenance:} \cite{Planck2018} (abstract, Section 2.1, Tables 1 and 2); \cite{Fixsen2009} for $T_{0}$; the radiation density is the standard computation from $T_{0}$, not a Planck parameter.

## technical
These are the standard values of the cosmological parameters from the Planck satellite's final data release, in the six-parameter model with a cosmological constant and cold dark matter: the expansion rate today, the matter fraction, the amplitude and tilt of the primordial curvature perturbations at the pivot scale $0.05$ Mpc$^{-1}$, and a spatially flat universe. The present radiation density, photons and three relativistic neutrino species, follows from the measured temperature of the background radiation. The store uses them as record inputs in horizon arithmetic: how far outside the Hubble length the pivot scale lay at an early epoch, and what amplitude a primordial source must supply.

## lay
The Planck satellite mapped the cosmic microwave background, the afterglow of the early universe, and from it measured the basic numbers of the standard cosmological model: how fast the universe is expanding today, how much matter it holds, and how strong and how tilted the primordial ripples were. These are the reference values the framework's results compare against.

## one-liner
Planck 2018 base $\Lambda$CDM: $H_{0} = 67.4 \pm 0.5$ km s$^{-1}$ Mpc$^{-1}$, $\Omega_{m} = 0.315 \pm 0.007$, $A_{s} = (2.100 \pm 0.030) \times 10^{-9}$ at $k_{*} = 0.05$ Mpc$^{-1}$, $n_{s} = 0.9649 \pm 0.0042$, $\Omega_{b}h^{2} = 0.02237$, $\Omega_{c}h^{2} = 0.1200$, with $T_{0} = 2.7255$ K giving $\Omega_{r} = 9.2 \times 10^{-5}$.
