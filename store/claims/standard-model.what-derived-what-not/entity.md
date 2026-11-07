---
id: standard-model.what-derived-what-not
kind: claim
version: 5
title: What is derived and what is not
status: proved
region: standard-model
subject: standard-model
tags: [ledger-audit, symmetry-breaking, undetermined-input]
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
derivations:
- name: main
  uses:
  - standard-model.transported-frozen-point@6
  - standard-model.ten-transported-ambient-space-doublets-are@2
  - standard-model.yukawa-pattern-two-rung-module@6
  - standard-model.frozen-point-first-rung-component@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_rung_component_norm_and_normalisation
- kind: check
  ref: check.py::check_rung_directions_are_doublet_directions
locators:
  paper: T12
  number: Prop 9.29
  label: prop:status
  line: 1790
extraction:
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 5: a marked note fixes the Hubble unit of v/H (H^2 = Lambda/3, that is H_0 sqrt(Omega_Lambda), against H_0; a factor of order one, about 0.2 in ln(v/H)); the conversion of 246 GeV in the check uses H = H_0 = 1.4 x 10^-42 GeV, and both readings give v/H between 10^44 and 10^45. Nothing else is changed.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the rung component -w_4 + (Lambda/3) v_4 of norm -Lambda/3 with coefficient one (GA), its doublet hypercharges, and the order of v/H. Version 3 -> 4.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  env: proposition
  context_refs:
  - standard-model.frozen-point-first-rung-component
  - standard-model.one-number-explain
  - standard-model.ten-transported-ambient-space-doublets-are
  - standard-model.yukawa-pattern-two-rung-module
  typing:
    by: ai-typing-pass
    added:
    - standard-model.ten-transported-ambient-space-doublets-are
    - standard-model.yukawa-pattern-two-rung-module
    - standard-model.frozen-point-first-rung-component
    note: 'Added the three results clause (1) collects (the ten, the Yukawa pattern, the first-rung frozen
      point); the one-number observation is only compared with, so it was not added. Levels pass: conditions
      already kept.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.frozen-point-first-rung-component
    - standard-model.ten-transported-ambient-space-doublets-are
    - standard-model.yukawa-pattern-two-rung-module
---

## formal
Three statements, at three levels. (1) \emph{Derived:} the representation of the Higgs doublet is the rung directions of the transported ambient space (Proposition \claimref{standard-model.ten-transported-ambient-space-doublets-are}); the Yukawa pattern of a vector in those directions is the Standard Model's (Theorem \claimref{standard-model.yukawa-pattern-two-rung-module}); the frozen point is a first-rung component and its transport by the founding construction produces second-rung components in the doublet directions, $H_{d}$-type for the point and $H_{u}$-type for its reciprocal, the direction being the lift's and the $O(\Lambda)$ admixture the frozen point's (Propositions \claimref{standard-model.frozen-point-first-rung-component}, \claimref{standard-model.transported-frozen-point}). (2) \emph{Not derived, and identified as the open number:} the scale of the rung component. Its coefficient one is the lift's normalisation, in the rung unit where $vw + wv = 1$, while the ground component has norm $\Lambda/3$ in the tractor metric; the total is null, $Q(c) = -\Lambda/3$, so in tractor units the rung component is as small as the cosmological scale, and a weak scale of $246$ GeV is the statement that the rung unit is $v/H \approx 10^{44}$ Hubble units. The series does not fix that number; Observation \claimref{standard-model.one-number-explain} compresses every scale into one number $N$, and this is either a second one or an instance of the first. (3) \emph{Not derived:} that a rung component of a parallel section is a dynamical field with a potential and a quantum, the physical Higgs boson, and that the weak gauge bosons acquire mass from it through the rung plane's own connection; the transport principle supplies the direction and the pattern of a constant background, not a Lagrangian.

\emph{Note (the Hubble unit).} The conversion here uses $H = H_{0} \approx 1.4 \times 10^{-42}$ GeV, giving $v/H_{0} \approx 1.7 \times 10^{44}$; the $H$ of the rung component's norm $-\Lambda/3$ and of $N = M_{P}/H$ is $H_{0}\sqrt{\Omega_{\Lambda}}$ ($H^{2} = \Lambda/3$), which gives $v/H \approx 2.1 \times 10^{44}$. The two differ by the factor $\sqrt{\Omega_{\Lambda}}$, of order one ($\ln(v/H)$ changes by about $0.2$), and both lie between $10^{44}$ and $10^{45}$.

## technical
(1) Derived: the Higgs doublet's representation is the rung directions of the transported ambient space, a vector in those directions has the Standard Model's Yukawa pattern, and transporting the frozen point, a first-rung component, produces second-rung components in the doublet directions, $H_{d}$-type for the point and $H_{u}$-type for its reciprocal. (2) Not derived: the scale of the rung component. Its coefficient one is the lift's normalisation in the rung unit, while the ground component has norm $\Lambda/3$ and the total is null, $Q(c) = -\Lambda/3$; a weak scale of $246$ GeV says the rung unit is $v/H \approx 10^{44}$ Hubble units, a number the series does not fix.

(3) Not derived: that a rung component of a parallel section is a dynamical field with a potential and a quantum, the physical Higgs boson, and that the weak gauge bosons get their mass from it through the rung plane's connection. The transport principle supplies the direction and pattern of a constant background, not a Lagrangian.

## lay
This is a ledger of what the framework does and does not explain about the Higgs. It derives where the Higgs doublet lives, among the directions transport adds, and the pattern of how it couples to quarks and leptons. It does not derive the size of the weak scale, about 246 GeV, which appears as a large unexplained number, and it does not derive that the Higgs is a field with its own particle and potential.

## one-liner
The Higgs doublet's representation, its Yukawa pattern and the transported frozen point's landing in the doublet directions are derived; the scale of the rung component and the Higgs as a dynamical field are not.
