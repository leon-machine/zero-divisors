---
id: synthesis.imported-string-gas-thermal-spectrum-and-conversion
kind: claim
version: 1
title: 'Imported: the string-gas thermal spectrum (Brandenberger 2015)'
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
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: 'R. H. Brandenberger, String gas cosmology after Planck, Class. Quantum Grav. 32 (2015), 234002; arXiv:1505.02381.'
  key: Brandenberger2015
  locator: 'eqs. (2) and (4) to (8)'
  doi: 10.1088/0264-9381/32/23/234002
extraction:
  note: >-
    Imported so that synthesis.holographic-thermal-fluctuations-fall-short-in-the-descent-window can
    pin the conversion of thermal fluctuations into the Bardeen potential that it cited. Checked on
    2026-11-01 against arXiv:1505.02381 (abstract page and PDF): title, author, DOI, and eqs. (2)
    <|Phi(k)|^2> = 16 pi^2 G^2 k^-4 <delta T^0_0(k) delta T^0_0(k)>, (4) <delta rho^2> = T^2
    C_V/R^6, (5) C_V = 2 (R^2/l_s^3)/(T(1 - T/T_H)), (6) P_Phi = k^3 |Phi(k)|^2/(2 pi^2), (7) P_Phi
    = (l_pl/l_s)^4 (T(k)/T_H)/(1 - T(k)/T_H), (8) n_s - 1 = (1 - T(k)/T_H)^-1 k d(T(k)/T_H)/dk. The
    journal volume is inferred from the DOI. The original computation (Nayeri, Brandenberger and
    Vafa 2006) is cited from memory, not checked. The combined form 8 G^2 k^-4 <delta rho^2> at R =
    1/k is eqs. (2) and (6) read with the position-space variance at that radius, up to factors of
    order one, as the source uses them.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created by the maintainer pass of 2026-11-01 (Leon approved the import of the string-gas spectrum and conversion formulas as routine Facts).'
---

## formal
In string-gas cosmology, at the time a comoving scale $k$ leaves the Hubble length at the end of the quasi-static Hagedorn phase, with Einstein gravity and a sudden transition, the Bardeen potential $\Phi$ of a perturbed FLRW field (a gravitational field on flat spacetime, Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) is sourced by the energy-density fluctuations: $\langle|\Phi(k)|^{2}\rangle = 16\pi^{2}G^{2}k^{-4}\langle\delta T^{0}{}_{0}(k)\,\delta T^{0}{}_{0}(k)\rangle$. Thermal fluctuations in a sphere of radius $R$ have $\langle\delta\rho^{2}\rangle = T^{2}C_{V}/R^{6}$, and a string gas has the area-law heat capacity $C_{V} \approx 2(R^{2}/l_{s}^{3})/(T(1 - T/T_{H}))$. With $P_{\Phi}(k) = k^{3}|\Phi(k)|^{2}/(2\pi^{2})$ and $R = 1/k$ this gives
\[
P_{\Phi}(k) = \Bigl(\frac{l_{pl}}{l_{s}}\Bigr)^{4}\frac{T(k)/T_{H}}{1 - T(k)/T_{H}},
\qquad
n_{s} - 1 = \Bigl(1 - \frac{T(k)}{T_{H}}\Bigr)^{-1} k\,\frac{d(T(k)/T_{H})}{dk},
\]
scale invariant at fixed temperature, with a red tilt when the temperature at exit falls with $k$. In the combined form used for other heat capacities, $P_{\Phi} = 8G^{2}k^{-4}\langle\delta\rho^{2}\rangle$ at $R = 1/k$ up to factors of order one. \emph{Provenance:} \cite{Brandenberger2015} (eqs. (2), (4) to (8)).

## technical
String-gas cosmology replaces inflation by a hot phase near the string Hagedorn temperature. The primordial perturbations are thermal: the energy in a region of size $R$ fluctuates by an amount set by the heat capacity, and a gas of strings has a heat capacity growing as the area $R^{2}$ rather than the volume. Converted into the gravitational potential when the scale leaves the Hubble length, these fluctuations give a spectrum independent of scale at fixed temperature, with amplitude set by the ratio of Planck to string length and by how close the temperature is to the Hagedorn value, and a slightly red tilt if the temperature drops as larger scales exit.

## lay
One alternative to inflation imagines the early universe as a hot gas of strings. Its heat fluctuations, turned into ripples of gravity as the universe starts to expand normally, come out with almost the same strength on every scale, as observed, because the gas stores energy in proportion to the surface area of a region rather than its volume.

## one-liner
With $C_{V} \approx 2(R^{2}/l_{s}^{3})/(T(1 - T/T_{H}))$ thermal fluctuations give $P_{\Phi} = (l_{pl}/l_{s})^{4}(T/T_{H})/(1 - T/T_{H})$ and $n_{s} - 1 = (1 - T/T_{H})^{-1}k\,d(T/T_{H})/dk$ (Brandenberger 2015).
