---
id: scrambling.no-echo-prediction-registered
kind: prediction
version: 3
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
- name: Claude Fable 5.2
  role: 'basis restated: field equations under (FS), the identification of (C_loc), a stated no-reflection reading and the local form of (N+); (C1) removed from the basis'
  version: 3
  source: 'maintainer pass of 2026-11-11 (run 2026-11-11-contradictions)'
amendments:
- version: 3
  kind: restatement
  defect: 'the prediction rested on (C1) alone and said the quantum structure is nowhere near the horizon, while (C1) is scoped to a Schwarzschild calibration and (C_loc) places the same modes on the horizon; its one uses edge asserted no field equation'
review: typed
derivations:
- name: basis
  uses:
  - interior.imported-equivalence-einstein-equations@3
  - synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part@5
  assumes:
  - synthesis.field-space-premise-parallel-frozen-point@2
  - synthesis.c-loc-local-horizon-premise@6
  - synthesis.n-plus-null-ground-state@12
locators:
  paper: T08
  number: Rec 7.1
  label: rec:echo
  line: 941
extraction:
  maintainer_pass_2026_11_11:
    by: maintainer-2026-11-11
    date: '2026-11-11'
    note: 'Version 2 -> 3, at Leon''s decision of 11 November 2026 ((FS) supplies the field equations). Basis edges: uses the imported Einstein equivalence and the frame equation of the frozen-point functional; assumes (FS), (C_loc) and (N+); the assumes edge to (C1) is removed. The predicted spectrum, the delay and the kill threshold are unchanged. The no-reflection reading is stated as a reading; the cited reflectivity paper was checked by its abstract only.'
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
The registered prediction: post-merger ringdown is the Kerr quasinormal spectrum of general relativity with \emph{no} modification, and in particular no echo train at the Planck-structure delay $\tau_{\mathrm{echo}} \approx 8M\ln(M/m_P)$ (the delay at which near-horizon structure at Planck distance would reflect \cite{CardosoPani2017}), of order tens to hundreds of milliseconds for stellar-mass remnants ($35$ ms at $10\,M_\odot$, $0.1$ to $0.25$ s for remnants of $30$ to $70\,M_\odot$): within the sensitivity band of existing detectors. The prediction is stated so that it can fail.

\emph{Basis.} (1) \emph{The field equations at and across the future horizon.} The gravitational field obeys Einstein's equations with a constant $\Lambda$, from the stored action on the field space of Premise \claimref{synthesis.field-space-premise-parallel-frozen-point} (FS) (Theorem \claimref{synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part}), read on the invertible region through the equivalence of Fact \claimref{interior.imported-equivalence-einstein-equations}; the quasinormal spectrum uses the ingoing condition at the future horizon, which is the regularity of the classical field there. (2) \emph{No structure at the horizon beyond the matter fields.} By the identification clause of Premise \claimref{synthesis.c-loc-local-horizon-premise} the modes on a horizon's light rays are the matter field on those light rays, and the modes that Postulates (C1) and (C2) place at the curvature cutoff are the same set described a second time (its paragraph ``One mode set, per light ray''). (3) \emph{Reading, stated and not derived.} The horizon's modes impose no reflecting condition on classical perturbations of the gravitational field. This does not follow from (2) as written: clause (R$_{\mathrm{loc}}$) of that premise makes the modes thermal before a crossing, and a flux reflectivity equal to the Boltzmann factor $e^{-\hbar|\omega|/kT_{H}}$ has been derived in the literature from detailed balance and the fluctuation-dissipation theorem at a horizon (Oshita, Wang and Afshordi, arXiv:1905.00464, JCAP 04 (2020) 016; abstract checked on 11 November 2026), with echoes as its consequence; the reading excludes it. (4) \emph{A state regular across the horizon.} The local form of Premise \claimref{synthesis.n-plus-null-ground-state} at the points of the horizon's generators, argued there at leading order.

\emph{What an echo would refute.} A single statistically confirmed echo train would refute the field equations at the horizon, and so (FS) with the stored action (its refutation condition (b)), or the reading (3). It does not bear on the Schwarzschild calibration of the count by Postulates (C1) and (C2).

\emph{Note (the earlier basis, 2026-11-11).} Until version 2 the prediction rested on Postulate \claimref{singularity.c1-curvature-cutoff} (C1) alone, with the wording that the quantum structure lies at the stretched singularity ``and nowhere near the horizon''. (C1) is now read as a calibration of the count on the Schwarzschild family only, and by (2) the same modes are on the horizon, on Schwarzschild and on Kerr alike; that wording is withdrawn and (C1) is no longer in the basis. With this basis the prediction is general relativity's own: it registers that the series predicts no departure from general relativity at the horizon, and a null result does not distinguish the series from general relativity. The deposited text (T8, Record 7.1) is kept under source\_formal.

## technical
The registered prediction is that post-merger ringdown is the unmodified Kerr quasinormal spectrum, with no echo train at the Planck-structure delay $\tau_{\mathrm{echo}} \approx 8M\ln(M/m_P)$, about 35 ms at $10\,\Msun$ and 0.1 to 0.25 s for remnants of 30 to $70\,\Msun$, within the band of existing detectors.

Its basis has four parts: Einstein's equations at and across the future horizon, from the stored action under the field-space premise (FS); the horizon's modes being the matter field on its light rays (the local-horizon premise), so that no further structure sits at the horizon; the stated reading that these modes reflect no classical perturbation, which excludes the thermal reflectivity proposed in the literature; and a state regular across the horizon (the local form of (N$_{+}$)). One statistically confirmed echo train would refute the field equations at the horizon or that reading.

The prediction is shared with general relativity. Until version 2 it rested on Postulate (C1) and said the quantum structure was nowhere near the horizon; that wording is withdrawn.

## lay
If quantum effects altered a black hole's surface, merging black holes would ring with faint repeated echoes a fraction of a second after the main signal. In this framework gravity obeys Einstein's equations right through the horizon, and nothing sits at the horizon except the ordinary matter fields, which are taken not to reflect gravitational waves. So it predicts no echoes: the ringing should be exactly as general relativity says. A single confirmed echo would refute that. The prediction is the same as general relativity's.

## one-liner
Post-merger ringdown is the unmodified Kerr quasinormal spectrum, with no echo train at the delay $8M\ln(M/m_P)$: under (FS) with the stored action the field equations hold across the horizon, and under (C$_{\mathrm{loc}}$) the horizon's modes are the matter field on its light rays, read as imposing no reflection; a prediction shared with general relativity.
