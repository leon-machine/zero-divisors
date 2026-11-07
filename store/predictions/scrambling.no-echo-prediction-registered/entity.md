---
id: scrambling.no-echo-prediction-registered
kind: prediction
version: 2
title: The no-echo prediction, registered
status: live
region: scrambling
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T08, deposited version
review: typed
derivations:
- name: basis
  uses:
  - interior.imported-equivalence-einstein-equations@3
  assumes:
  - singularity.c1-curvature-cutoff@4
locators:
  paper: T08
  number: Rec 7.1
  label: rec:echo
  line: 941
extraction:
  maintainer_pass_2026_10_22:
    by: ai-maintainer-pass
    note: 'A4/V4 follow-up: added the maintainer assumes edge to Postulate (C1), singularity.c1-curvature-cutoff, since the prediction places the quantum structure at r_c = (2M)^(1/3), which is (C1); formal cites it, technical and one-liner name it.'
  source_formal: "The framework's quantum structure lies at the stretched singularity, $r_c = (2M)^{1/3}$ in Planck units: deep inside the hole, at Planck curvature, and nowhere near the horizon, which remains exactly the smooth vacuum horizon of classical general relativity (the exterior dictionary is exact, \\cite[Fact 2.1]{ButlerT6}). The registered prediction: post-merger ringdown is the Kerr quasinormal spectrum of general relativity with \\emph{no} modification, and in particular no echo train at the Planck-structure delay $\\tau_{\\mathrm{echo}} \\approx 8M\\ln(M/m_P)$ (the delay at which near-horizon structure at Planck distance would reflect \\cite{CardosoPani2017}), of order tens to hundreds of milliseconds for stellar-mass remnants ($35$ ms at $10\\,M_\\odot$, $0.1$ to $0.25$ s for remnants of $30$ to $70\\,M_\\odot$): within the sensitivity band of existing detectors. A single statistically confirmed echo train would refute the framework's localisation of quantum structure. The prediction is stated so that it can fail."
  env: record
  context_refs:
  - interior.imported-equivalence-einstein-equations
  typing:
    by: ai-typing-pass
    note: Kept the basis edge to the imported exterior equivalence with the Einstein equations, the premise
      that the horizon is the classical one; the Kerr quasinormal spectrum it predicts is classical but
      no imported Kerr ringdown claim is in the store, so no standard route is recorded.
kill_condition:
  threshold: One statistically confirmed echo train at the Planck-structure delay
  data_source: gravitational-wave catalogues
  registered: 2026-09 (T8 record; confronted in the T17 stance table, August 2026)
observations:
- date: 2026-09
  dataset: GWTC-4.0 (O4a) echo searches
  result: LVK's four echo searches over GWTC-4.0 find no evidence for post-merger echoes, and an independent
    O4a search with neural posterior estimation also finds none. GW250114's ringdown agrees with general
    relativity.
  verdict: consistent
  source: LVK, GWTC-4.0 Tests of GR III, arXiv:2603.19021 (2026); Luo and Piao, arXiv:2609.18337 (2026);
    arXiv:2610.09503 (2026)
- date: 2026-08
  dataset: GWTC-4.0 echo searches
  result: 'Gravitational-wave catalogues: through GWTC-4.0, four catalogues and four search methods report
    no significant echo train; early tentative claims did not survive reanalysis.'
  verdict: consistent
  source: T17 stance table, row 1
subject: entropy
tags: [live-prediction, kerr, horizons]
about:
- obj.scrambling.stretched-singularity
---

## formal
The framework's quantum structure lies at the stretched singularity, $r_c = (2M)^{1/3}$ in Planck units, by Postulate \claimref{singularity.c1-curvature-cutoff} (C1): deep inside the hole, at Planck curvature, and nowhere near the horizon, which remains exactly the smooth vacuum horizon of classical general relativity (the exterior dictionary is exact, \cite[Fact 2.1]{ButlerT6}). The registered prediction: post-merger ringdown is the Kerr quasinormal spectrum of general relativity with \emph{no} modification, and in particular no echo train at the Planck-structure delay $\tau_{\mathrm{echo}} \approx 8M\ln(M/m_P)$ (the delay at which near-horizon structure at Planck distance would reflect \cite{CardosoPani2017}), of order tens to hundreds of milliseconds for stellar-mass remnants ($35$ ms at $10\,M_\odot$, $0.1$ to $0.25$ s for remnants of $30$ to $70\,M_\odot$): within the sensitivity band of existing detectors. A single statistically confirmed echo train would refute the framework's localisation of quantum structure. The prediction is stated so that it can fail.

## technical
Under Postulate (C1), the framework places its quantum structure at the stretched singularity $r_c = (2M)^{1/3}$, at Planck curvature deep inside the hole, while the horizon remains the smooth vacuum horizon of general relativity because the exterior dictionary is exact. The registered prediction is that post-merger ringdown is the unmodified Kerr quasinormal spectrum.

In particular there is no echo train at the Planck-structure delay $\tau_{\mathrm{echo}} \approx 8M\ln(M/m_P)$, about 35 ms at $10\,\Msun$ and 0.1 to 0.25 s for remnants of 30 to $70\,\Msun$, within the band of existing detectors. One statistically confirmed echo train would refute the framework's localisation of quantum structure.

## lay
If quantum effects altered a black hole's surface, merging black holes would ring with faint repeated echoes a fraction of a second after the main signal. This framework puts its quantum structure deep inside the hole instead, so it predicts no echoes: the ringing should be exactly as general relativity says. A single confirmed echo would refute it.

## one-liner
Under Postulate (C1), which puts the quantum structure at the stretched singularity, post-merger ringdown is the unmodified Kerr quasinormal spectrum, with no echo train at the delay $8M\ln(M/m_P)$.
