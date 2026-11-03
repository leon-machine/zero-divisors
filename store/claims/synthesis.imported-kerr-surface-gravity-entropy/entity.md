---
id: synthesis.imported-kerr-surface-gravity-entropy
kind: claim
version: 2
title: 'Imported: the surface gravity and the Bekenstein-Hawking entropy of the Kerr horizon'
status: imported
region: synthesis
subject: entropy
tags: [kerr, horizons, hawking-temperature, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-10-22
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
- citation: 'J. M. Bardeen, B. Carter and S. W. Hawking, The four laws of black hole mechanics, Commun. Math. Phys. 31 (1973), 161--170.'
  key: BCH1973
  doi: 10.1007/BF01645742
- citation: 'S. W. Hawking, Particle creation by black holes, Commun. Math. Phys. 43 (1975), 199--220.'
  key: Hawking1975
- citation: 'J. D. Bekenstein, Black holes and entropy, Phys. Rev. D 7 (1973), 2333--2346.'
  key: Bekenstein1973
- citation: 'B. Carter, Global structure of the Kerr family of gravitational fields, Phys. Rev. 174 (1968), 1559--1571.'
  key: Carter1968
extraction:
  note: >-
    Imported for the result that reads the Schwarzschild counting rule on Kerr. Bardeen-Carter-
    Hawking 1973 (title, journal, pages, DOI, and that it relates horizon area and surface gravity
    to entropy and temperature in a mass formula for stationary axisymmetric black holes) was
    checked against the publisher's listing; the explicit formulas are cited from memory, not
    checked against the source. They are internally consistent: r_+^2 + a^2 = 2 M r_+ and r_+ - r_-
    = 2 sqrt(M^2 - a^2) turn the first form of kappa_+ into the second.
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Created by the maintainer pass so that the Kerr counting result can pin the two classical Kerr facts it cited from memory; partly verified (see note).'
  maintainer_pass_gtg:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the Kerr field on flat spacetime in the Kerr-Schild gauge; the horizon is the locus r = r_+, a Killing horizon of K = hb^{-1}(d_t + Omega_H d_phi) with (K.D)K = kappa_+ K; the area is that of a cross-section in the Kerr-Schild chart. Values, first law, temperature and entropy unchanged.'
---

## formal
Units $G = c = \hbar = 1$. For the Kerr gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) of mass $M$ and angular momentum $J = aM$, $0 \le a < M$, in the Kerr-Schild gauge (Fact \claimref{interior.imported-kerr-schild-form-kerr-gauge}), with horizon loci at $r_{\pm} = M \pm \sqrt{M^{2} - a^{2}}$, the event horizon locus $r = r_{+}$ is a Killing horizon of $K = \hb^{-1}(\partial_{t} + \Omega_{H}\partial_{\phi})$, $\Omega_{H} = a/(r_{+}^{2} + a^{2})$: $Q(K) = 0$ there, $K$ is normal to it, and $(K \cdot D)K = \kappa_{+} K$ with
\[
\kappa_{+} \;=\; \frac{r_{+} - r_{-}}{2(r_{+}^{2} + a^{2})} \;=\; \frac{\sqrt{M^{2} - a^{2}}}{2Mr_{+}}, \qquad A_{+} \;=\; 4\pi(r_{+}^{2} + a^{2}) \;=\; 8\pi Mr_{+},
\]
its surface gravity and the area of a horizon cross-section in the Kerr-Schild chart. Nearby stationary black holes obey $\delta M = \frac{\kappa_{+}}{8\pi}\,\delta A_{+} + \Omega_{H}\,\delta J$, the horizon radiates at the temperature $T_{H} = \kappa_{+}/2\pi$, and the Bekenstein-Hawking entropy of the Kerr horizon is $S = A_{+}/4$. \emph{Provenance:} \cite{BCH1973, Hawking1975, Bekenstein1973, Carter1968}, read in Gauge Theory Gravity through Fact \claimref{synthesis.imported-gtg-dictionary}(vi).

## technical
A rotating (Kerr) black hole of mass $M$ and spin parameter $a = J/M < M$ is, in Gauge Theory Gravity, a gravitational field on flat spacetime, carried in the Kerr-Schild gauge. Its outer horizon locus $r_{+} = M + \sqrt{M^{2} - a^{2}}$ is a Killing horizon of $K = \hb^{-1}(\partial_t + \Omega_H\partial_\phi)$, the combination of time translation and rotation at the horizon's angular velocity. Its surface gravity, $(K \cdot D)K = \kappa_{+}K$, is $\kappa_{+} = (r_{+} - r_{-})/(2(r_{+}^{2} + a^{2}))$ and the area of a cross-section is $4\pi(r_{+}^{2} + a^{2})$. The first law of black-hole mechanics and Hawking's temperature $\kappa_{+}/2\pi$ give the Bekenstein-Hawking entropy, a quarter of the horizon area in Planck units.

## lay
A spinning black hole's horizon has a definite surface gravity, which sets its temperature, and a definite area. As for a non-rotating black hole, its entropy is a quarter of that area measured in the smallest natural units of area. These are standard results of black-hole physics from the 1970s, taken here from the literature.

## one-liner
The Kerr field's horizon locus has surface gravity $\kappa_{+} = (r_{+} - r_{-})/(2(r_{+}^{2} + a^{2}))$, cross-section area $A_{+} = 4\pi(r_{+}^{2} + a^{2})$ and Bekenstein-Hawking entropy $A_{+}/4$.
