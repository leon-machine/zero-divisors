---
id: standard-model.what
kind: claim
version: 3
title: What $N$ is
status: conjectured
region: standard-model
subject: dark-energy
tags:
- the-number-n
- boundary-modes
- horizons
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
lineage:
  motivated_by:
  - dark-energy.vacuum-region-registration-condition
  - scrambling.mode-count
  - standard-model.trichotomy-what-kind-number
locators:
  paper: T12
  number: Obs 7.2
  label: obs:whatN
  line: 1243
extraction:
  env: observation
  context_refs:
  - dark-energy.vacuum-region-registration-condition
  - scrambling.mode-count
  - standard-model.trichotomy-what-kind-number
  - synthesis.de-sitter-entropy-pi-n-squared
  - synthesis.de-sitter-mode-count
  outside_pilot_cites:
  - ButlerT17
  typing:
    by: ai-typing-pass
    note: 'Observation kept as conjectured; its three motivating claims were already recorded and are
      the ones its clauses cite. Levels pass: the lay level and one-liner now say that the $w = -1$ prediction
      behind the epochal reading is registered and conditional (review item 9).'
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants: []
    added_about:
    - obj.dark-energy.four-ways-number-enters-theory-shape
    verdict: connected
    note: About the four-ways definition, whose clause (P) its clause (ii) uses.
  correction:
    by: ai-correction
    date: '2026-10-22'
    note: 'Clause (i) brought into line with the performed count (note.synthesis.what-n-is-counted; conventions.md
      known limit 5), as for standard-model.why-large and standard-model.largeness-number-universes-boundary-modes:
      the indication is now a computed entropy pi N^2 (exact, Einstein-Hilbert area law) and a mode count
      pi N^2/ln 2, about 4.77e122, under the black hole counting rule; N = 1.026e61 on H0 = 67.4 km/s/Mpc,
      Omega_Lambda = 0.685, M_P = 1.221e19 GeV (exact interval arithmetic). Clauses (ii) and (iii) unchanged.
      The counted theorems are recorded under context_refs, not motivated_by, since they are motivated
      by this observation.'
  open_problem: op.t12-n-after-the-count
about:
- obj.dark-energy.four-ways-number-enters-theory-shape
---

## formal
(i) The boundary-mode count of the entropy paper T8 \cite[\S 3, Thm.~3.4]{ButlerT8}, applied to the cosmological horizon rather than to the black-hole singularity, was offered here as a preliminary indication that the de Sitter horizon entropy is of order $N^{2}$, so that $N$ is the square root of the pair capacity of the universe's own boundary mode space. No paper of the series performs that application; it is now performed in the store. Under the Einstein-Hilbert area law the horizon entropy is exactly $S_{\Lambda} = \pi N^{2}$ (Theorem \claimref{synthesis.de-sitter-entropy-pi-n-squared}), and if the horizon's modes are counted by the black hole's rule they number $|J| = \pi N^{2}/\ln 2$, about $4.8 \times 10^{122}$, with capacity $C = |J|\ln 2 = S_{\Lambda}$, so that $N = \sqrt{C/\pi}$ (Theorem \claimref{synthesis.de-sitter-mode-count}). The indication therefore holds exactly for the entropy and up to the factor $\sqrt{\pi}$ for the capacity; $N$, about $1.0 \times 10^{61}$, is not itself the number of the universe's boundary modes but the square root of that number up to $\sqrt{\pi/\ln 2}$. (ii) This bears on the question as posed. The ascended action is polynomial with no dimensionless constants, and every scale enters through the frozen point. Under the action as written, with the frozen point's norm fixed before variation, $N$ is a parameter of the laws, an import recorded in Proposition \claimref{standard-model.trichotomy-what-kind-number}(4); under the promoted action, where the norm is the value of a Lagrange-multiplier field, the frozen point is a property of the selected descent, $N$ is a state-count and not a coupling, and to ask that it be derived from the laws is to ask a question that refutes itself as posed. Which reading holds is the decision Proposition \claimref{standard-model.trichotomy-what-kind-number}(4) records open, and the capstone \cite[Table~1]{ButlerT17} keeps the count. (iii) The Dirac coincidence ($N$ is also, at present, the age of the universe in Planck units) would suggest $N$ is a clock and $\Lambda$ decays as $1/t^{2}$; but the series' registered prediction $w = -1$ exactly \cite[Prop.~4.2(iii)]{ButlerT10}, itself registered and conditional there, forbids this: the frozen point is frozen. The framework predicts that the coincidence is epochal, and that prediction is tested by the dark-energy measurement of $w$ already registered in the series.

## technical
At observation level. The paper offered, as a preliminary indication, that the boundary-mode count of the entropy paper applied to the cosmological horizon gives an entropy of order $N^{2}$, making $N$ the square root of the pair capacity of the universe's own boundary mode space. That application is now performed: the horizon entropy is exactly $\pi N^{2}$ under the Einstein-Hilbert area law, and under the black hole's counting rule the horizon carries about $\pi N^{2}/\ln 2 \approx 4.8 \times 10^{122}$ modes, so $N \approx 1.0 \times 10^{61}$ is the square root of the capacity up to $\sqrt{\pi}$ and of the mode count up to $\sqrt{\pi/\ln 2}$, not the mode count itself. Under the action as written $N$ is a parameter of the laws; under the promoted action, where the norm is a Lagrange-multiplier field, $N$ is a state-count of the selected descent and not a coupling. Which reading holds is recorded open.

The Dirac coincidence would suggest that $N$ is a clock and $\Lambda$ decays as $1/t^{2}$, but the series' registered conditional prediction $w = -1$ forbids this. The framework therefore predicts that the coincidence is epochal, which the measurement of $w$ tests.

## lay
This observation ties the huge number $N$, about $10^{61}$, to something physical: the horizon of the observable universe carries about $10^{122}$ basic modes, roughly the square of $N$, a count now performed under the black hole's counting rule rather than only indicated. Depending on an open choice about the form of the theory, $N$ is either a fixed parameter of the laws or a property of how our universe came to be. The fact that $N$ also matches the present age of the universe in natural units is read as a feature of our era, because the framework's registered prediction, itself conditional, is that dark energy does not change over time; a measurement of how dark energy behaves will test this.

## one-liner
At observation level, $N$ (about $10^{61}$) is the square root of the universe's horizon mode count (about $\pi N^{2}/\ln 2 \approx 4.8 \times 10^{122}$ under the black hole's counting rule) up to $\sqrt{\pi/\ln 2}$, a parameter of the laws or a state-count according to an open choice, and, by the registered and conditional prediction $w = -1$, the Dirac coincidence is epochal.
