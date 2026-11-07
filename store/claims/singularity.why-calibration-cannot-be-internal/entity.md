---
id: singularity.why-calibration-cannot-be-internal
kind: claim
version: 6
title: Why the calibration cannot be internal
status: proved
region: singularity
subject: thermality
tags: [no-go, undetermined-input, hawking-temperature, thermal-premises]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
review: typed
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - singularity.connection-bivector-computed@5
  - singularity.euclidean-section-period@6
  - singularity.solution-where-divergence-lies@4
  - singularity.unipotent-ray@4
  - transport.transport-algorithm@3
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:7.25
- kind: check
  ref: check.py::check_only_finite_rate_is_the_horizon_rate
- kind: check
  ref: check.py::check_cross_section_area_null_normal_killing
- kind: check
  ref: check.py::check_invertible_unimodular_nondegenerate_at_horizon
- kind: check
  ref: check.py::check_period_is_eight_pi_m
locators:
  paper: T05
  number: Prop 7.25
  label: prop:horizon
  line: 1932
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the radial connection rate squares to M/(2r^3) with a pole at r = 0 while (K.D)K = K/(4M) at the horizon, the PG cross-section of area 16 pi M^2 with K null, normal and flowing by t-translation, and hb invertible, unimodular and nondegenerate at the horizon, in GA. Version 5 -> 6.'
  maintainer_pass_2026_10_22:
    by: ai-maintainer-pass
    note: 'Folded-state-selection (R) fix: the formal level''s (R) now carries a claimref to T05''s premise singularity.r-regularity-fixed-locus, so it is not read as the folded note''s regularity premise.'
  source_formal: "The only finite rate the Schwarzschild geometry supplies to the boost flow is the surface gravity $\\kappa = 1/4M$, a horizon quantity: on the singular side the connection rate diverges as $\\sqrt{M/2r^{3}}$ (Proposition \\claimref{singularity.connection-bivector-computed}(3)) and offers no finite period to be identified with $2\\pi$. The locus at which (R) applies is the fixed locus of the boost flow, the bifurcation surface at $r = 2M$, and there, by Propositions \\claimref{singularity.unipotent-ray} and \\claimref{singularity.solution-where-divergence-lies}(3), the gauge field is invertible and unimodular and division does not fail. Hence the transport principle, being a theory of the loci where division fails, makes no statement at the locus where the temperature is calibrated, and no strengthening of the framework's statements at the singular boundary can supply (R)."
  env: proposition
  context_refs:
  - singularity.connection-bivector-computed
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
  typing:
    by: ai-typing-pass
    removed:
    - singularity.rate-discharge-hypothesis-iii
    added:
    - singularity.connection-bivector-computed
    note: Kept the transport-algorithm edge because the proof rests on the algorithm's first step classifying
      the horizon as a locus where division does not fail; removed the rate theorem (mentioned only as
      the user of the section's period) and added the connection-rate proposition the statement cites.
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    cited:
    - singularity.connection-bivector-computed
    - transport.transport-algorithm
  flow_note: rotor flow exp(lambda sigma/2) (T05 Thm 6.3, T08 Lem 4.2). The rate kappa and the fixed locus
    (the bifurcation surface) belong to the Killing boost, the geometric rotor flow; the period 2 pi it
    is compared with is that of the phase flow, its continuation.
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 4
    note: 'The two boost flows: flow_note recorded.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity per Leon 2026-10-23 (DICTIONARY, Bifurcation surfaces): the locus where (R) applies is the horizon locus r = 2M in the Painleve-Gullstrand chart, on a cross-section of area 16 pi M^2 with (K.D)K = kappa K; the bifurcation surface itself noted as beyond one flat chart. Same conclusion; proof given a one-sentence pointer. Fix (Leon 2026-10-23, referee GR1): the regularity wording "equivalently, the state is regular across the horizon locus" replaced by "for a state that is KMS for the Killing flow, this is also the period at which it is regular across the horizon locus in the PG chart"; clauses, scope and status unchanged.'
---

## formal
The only finite rate the Schwarzschild gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) supplies to the boost flow is the surface gravity $\kappa = 1/4M$, a horizon quantity: on the singular side the connection rate diverges as $\sqrt{M/2r^{3}}$ (Proposition \claimref{singularity.connection-bivector-computed}(3)) and offers no finite period to be identified with $2\pi$. (R) (Premise \claimref{singularity.r-regularity-fixed-locus}) applies across the horizon locus in the chart: the Euclidean section is regular at its tip, which fixes the period $2\pi/\kappa$; for a state that is KMS for the Killing flow, this is also the period at which it is regular across the horizon locus in the Painlev\'e-Gullstrand chart. The horizon locus is met in a cross-section $\Sigma_{t_0} = \{t = t_0,\ r = 2M\}$ of the horizon locus in the Painlev\'e-Gullstrand chart, of area $16\pi M^{2}$, on which the Killing field $K = \hb^{-1}(e_t)$ is null and normal to the horizon, with $(K \cdot D)K = \kappa K$, $\kappa = 1/4M$; the boost flow is the flow of $K$, which carries cross-sections to cross-sections. There, by Propositions \claimref{singularity.unipotent-ray} and \claimref{singularity.solution-where-divergence-lies}(3), the gauge field is invertible and unimodular and division does not fail. Hence the transport principle, being a theory of the loci where division fails, makes no statement at the locus where the temperature is calibrated, and no strengthening of the framework's statements at the singular boundary can supply (R).

The bifurcation surface itself, where the boost flow has its fixed points, lies beyond one flat chart (it is the meeting of the four regions of the maximal extension); the chart contains the future horizon, on whose cross-sections the area, the surface gravity and the boost flow are those stated.

## technical
The only finite rate the Schwarzschild gravitational field supplies to the boost flow is the surface gravity $\kappa = 1/4M$, a horizon quantity: on the singular side the connection rate diverges as $\sqrt{M/2r^3}$ and gives no finite period to identify with $2\pi$. Premise (R) applies across the horizon locus $r = 2M$ of the Painlev\'e-Gullstrand chart, where the Euclidean section is regular at its tip, fixing the period $2\pi/\kappa$ (for a state that is KMS for the Killing flow, this is also the period at which it is regular across the horizon locus in the Painlev\'e-Gullstrand chart); on each cross-section of that locus the Killing field $K = \hb^{-1}(e_t)$ is null with $(K \cdot D)K = \kappa K$, the gauge field is invertible and unimodular, and division does not fail.

Since the transport principle is a theory of the loci where division fails, it makes no statement at the locus where the temperature is calibrated, and no strengthening of the framework's statements at the singular boundary can supply (R). The bifurcation surface itself lies beyond one flat chart; the chart's horizon cross-sections carry the same area, surface gravity and boost flow.

## lay
The framework's machinery acts only where division in its algebra breaks down, which for a black hole is at the singularity. The temperature, though, is set at the horizon, where nothing breaks down and the only finite rate on offer is the surface gravity. So the condition that fixes the temperature cannot come from the framework itself and has to be brought in from outside.

## one-liner
The temperature is calibrated by (R) across the horizon locus $r = 2M$ of the Painlev\'e-Gullstrand chart, where the gauge field is invertible and division does not fail, so the transport principle says nothing there and no strengthening of its statements at the singular boundary can supply (R).
