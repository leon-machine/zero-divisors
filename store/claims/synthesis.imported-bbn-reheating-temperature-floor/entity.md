---
id: synthesis.imported-bbn-reheating-temperature-floor
kind: claim
version: 1
title: 'Imported: big-bang nucleosynthesis bounds the reheating temperature below by a few MeV (Hasegawa et al. 2019)'
status: imported
region: synthesis
subject: dark-energy
tags: [confronted-with-data, matter-asymmetry]
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
- citation: 'T. Hasegawa, N. Hiroshima, K. Kohri, R. S. L. Hansen, T. Tram and S. Hannestad, MeV-scale reheating temperature and thermalization of oscillating neutrinos by radiative and hadronic decays of massive particles, J. Cosmol. Astropart. Phys. 2019, no. 12, 012 (2019).'
  key: Hasegawa2019
  doi: 10.1088/1475-7516/2019/12/012
extraction:
  note: >-
    Imported so that synthesis.finite-range-descent-deposit-cannot-seed-cmb can pin the lowest
    reheating temperature it uses (1 MeV, as a weaker form of this floor) instead of citing it
    from memory. Checked on 2026-10-23 against the abstract of arXiv:1908.10189: authors, DOI
    10.1088/1475-7516/2019/12/012, and the conservative bounds T_RH >~ 1.8 MeV for radiative and
    T_RH >~ 4-5 MeV for hadronic decays, for decaying particles of mass 10 GeV to 100 TeV, from
    consistency of the light-element abundances, with neutrino self-interactions and
    oscillations included in the thermalisation.
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Created by the maintainer pass (the fix round asked for the nucleosynthesis floor on reheating, cited from memory by the finite-range descent result, to be imported as a Fact).'
---

## formal
If the radiation-dominated universe is produced by the decay of a massive particle, of mass between $10$ GeV and $100$ TeV, into Standard-Model radiation at reheating temperature $T_{\mathrm{RH}}$, then consistency of the predicted light-element abundances with the observed ones, with the thermalisation of the oscillating, self-interacting neutrinos computed, requires $T_{\mathrm{RH}} \gtrsim 1.8$ MeV when the decay is radiative and $T_{\mathrm{RH}} \gtrsim 4$ to $5$ MeV when it is hadronic (conservative bounds). In particular any epoch of radiation domination from which nucleosynthesis proceeds in the standard way begins at a temperature above $1$ MeV. \emph{Provenance:} \cite{Hasegawa2019} (abstract and main results).

## technical
Nucleosynthesis needs a thermal bath of photons, electrons and three nearly thermal neutrino species at temperatures of about one MeV. If that bath was produced late, by the decay of a long-lived particle, the neutrinos may not reach thermal equilibrium, which changes the neutron-proton ratio and the expansion rate and spoils the light-element abundances. Requiring the abundances to agree with observation gives a lower bound on the reheating temperature of a few MeV, at least $1.8$ MeV for radiative and $4$ to $5$ MeV for hadronic decays. The store uses the weaker statement that the descended phase's radiation era starts above $1$ MeV.

## lay
The lightest chemical elements were made in the first few minutes, and the amounts observed today only come out right if the universe was already hot and filled with radiation, including neutrinos, at temperatures of a few million electronvolts. So whatever started the hot universe must have done so above that temperature.

## one-liner
Nucleosynthesis requires the reheating temperature of the radiation era to exceed $1.8$ MeV (radiative decays) or $4$ to $5$ MeV (hadronic decays), so above $1$ MeV in any case (Hasegawa et al. 2019).
