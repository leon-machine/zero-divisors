---
id: dark-tower-matter.three-dimensional-phases
kind: claim
version: 4
title: The phases of the three-dimensional towers
status: proved
region: dark-tower-matter
subject: dark-matter
tags: [gauge-fields, mass-generation]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T14c, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - dark-tower-matter.anomalies@4
  - dark-tower-matter.three-dimensional-content@4
  - dark-tower-matter.residue-seven-unit@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_T14c.py
  tags:
  - id:K4
- kind: check
  ref: check.py::check_phase_split_from_minimal_level
- kind: check
  ref: check.py::check_contact_suppression
- kind: check
  ref: check.py::check_r7_central_unit
lineage:
  supersedes:
  - dark-matter.radiation-audit-what-theorem-closes-what
locators:
  paper: T14c
  number: Obs 9.1
  label: prop:phases
  line: 773
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: phase split of the effective level from bare level +-1/2 (two C, two T), flux-attachment spin shift, contact suppression bound, central unit of Cl(2,3). Version 2 -> 3. Check strengthened: threshold ratio 1/sqrt(2e-16) (integer part 70710678) and the probability 2.0408e-16 at 7e7 pinned by hand; inputs moved to module level. Version 3 -> 4.'
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 1
    note: 'Lineage supersedes added (decision 1, CONTRADICTIONS_STRUCTURE H3): T14 Prop 6.2(2) said every compact
      U(1) in three dimensions confines by monopoles; with the half-integral level of Prop 6.5(i) that holds
      in phase (C) only. The audit''s clause (2) and conclusion are narrowed and cite this result and the
      anomaly proposition. Lineage is unpinned in the store schema.'
  env: proposition
  context_refs:
  - dark-matter.radiation-audit-what-theorem-closes-what
  - dark-tower-matter.anomalies
  - dark-tower-matter.residue-seven-unit
  flags:
  - no proof environment found
  typing:
    by: ai-typing-pass
    added:
    - dark-tower-matter.anomalies
    - dark-tower-matter.residue-seven-unit
    - dark-tower-matter.three-dimensional-content
    note: 'E107 fix: the assembly-level proposition has no proof environment; it applies imported three-dimensional
      gauge dynamics (Polyakov; Deser, Jackiw and Templeton; Affleck et al.; Wilczek; none in the store)
      to the forced level of the anomaly proposition, so that proposition, the content and (for r = 7)
      the residue-seven unit were made its edges with a cites-only proof file. The dark-matter paper''s
      radiation audit is corrected here, not used. Levels pass: levels written from scratch, keeping every
      condition and level qualifier of the formal statement.'
---

## formal
Imported: Polyakov confinement of a compact $U(1)$ with Maxwell dynamics \cite{Polyakov1977}; topological mass $e^{2}k/2\pi$ and the absence of confinement at nonzero Chern-Simons level \cite{DJT1982, AHPS1989}; flux attachment, with spin shifted by $q^{2}/2k$ \cite{Wilczek1982}. With the minimal bare level $|k| = \tfrac{1}{2}$ of Proposition \claimref{dark-tower-matter.anomalies}(i), each factor is in one of two phases, set by whether the cell's mass sign is aligned with its bare level:
\begin{enumerate}
\item[(C)] effective level $0$: Polyakov-confining; the cells bind into neutral onia that annihilate at full strength into a lighter channel;
\item[(T)] effective level $\pm 1$: topologically massive, the photon gapped at $e^{2}/2\pi$; the unit-charge lines are transparent and the cells become effectively neutral and, on the standard signs, spin $0$ (interpretive).
\end{enumerate}
In phase (T) with $e^{2} \gg m$ the cells are stable by their gauge charges (at $r = 7$ also by the algebra's central unit, Proposition \claimref{dark-tower-matter.residue-seven-unit}), and contact processes scale as $(m/e^{2})^{2}$. Assembly level. T14's Proposition 6.2 states that every compact $U(1)$ in three dimensions confines \cite[Prop.~6.2]{ButlerT14}; with the forced half-integral level that holds in phase (C) only. Both phases close T14's radiation channel: nothing light remains in phase (T), and even two massless $2+1$ dimensional photons at the photon temperature would give $\Delta\Neff$ of about $4 \times 10^{-3}$ on sheets (supplementary \file{CHECK\_COS}).

## technical
At assembly level, with imported Polyakov confinement, topological mass and flux attachment. With the minimal bare Chern-Simons level $|k| = \tfrac12$ forced by the parity anomaly, each abelian factor is in one of two phases, set by whether the cell's mass sign is aligned with its bare level: (C) effective level $0$, Polyakov-confining, the cells binding into neutral onia that annihilate at full strength into a lighter channel; or (T) effective level $\pm 1$, topologically massive with the photon gapped at $e^2/2\pi$, the unit-charge lines transparent and the cells effectively neutral and, interpretively, of spin $0$. In phase (T) with $e^2 \gg m$ the cells are stable by their gauge charges (at $r = 7$ also by the central unit), and contact processes scale as $(m/e^2)^2$.

The dark-matter paper's statement that every compact $U(1)$ in three dimensions confines holds in phase (C) only. Both phases close its radiation channel: even two massless $2+1$ dimensional photons at the photon temperature would give $\Delta\Neff$ of about $4 \times 10^{-3}$ on sheets.

## lay
At assembly level, and relying on established results about forces in two space dimensions, each three-dimensional tower's force can sit in one of two phases. In one it confines, binding particles into neutral pairs that annihilate; in the other the force carrier gains a mass, and with strong coupling the particles become effectively neutral and stable. Either way the towers add almost no radiation to the early universe.

## one-liner
At assembly level, with the forced half-integral Chern-Simons level, each three-dimensional factor either confines (phase C) or is topologically massive (phase T), and both phases close the radiation channel.
