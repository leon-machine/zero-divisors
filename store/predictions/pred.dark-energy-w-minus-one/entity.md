---
id: pred.dark-energy-w-minus-one
kind: prediction
version: 3
title: 'Dark energy cannot evolve: w = -1'
status: live
subject: dark-energy
tags: [live-prediction, cosmological-constant]
region: programme
proposed_by:
  kind: extraction
  session: full-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T10, deposited version
review: typed
kill_condition:
  threshold: A confirmed detection of $w \neq -1$ at any epoch, with no parameter available to absorb
    it
  data_source: DESI DR2 with CMB and supernovae
  registered: 2026-08 (T17 stance table, row 2)
observations:
- date: 2026-10
  dataset: DESI DR2 BAO + CMB + supernovae (Unite)
  result: 'The combined Pantheon+ and DES-SN5YR sample (Unite, 2,884 type Ia supernovae) with CMB and
    DESI DR2 BAO gives w0 = -0.861 +0.044/-0.042, wa = -0.60 +0.17/-0.19: a 3.1 to 3.3 sigma frequentist
    preference for evolving dark energy, but only weak Bayesian evidence, and a Jeffreys-prior reanalysis
    favours LCDM. DESI''s DR2 Lyman-alpha full-shape analysis gives 2.7 sigma with the CMB. No DESI DR3
    yet.'
  verdict: contested
  source: Camilleri et al., arXiv:2609.05053 (2026); DESI, arXiv:2607.27410 (2026); Layton, Hall and Robertson,
    arXiv:2610.26493 (2026)
- date: 2026-08
  dataset: DESI DR2 with CMB and supernovae
  result: 'DESI DR2 with CMB and supernovae: a three-to-four sigma preference for evolving w is reported
    and contested (derivative-concentrated, prior-sensitive, internally tensioned).'
  verdict: contested
  source: T17 stance table, row 2
locators:
  paper: T10
  number: T17 stance 2
  label: tab:stances
extraction:
  maintainer_pass_2026_11_01:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2 -> 3, at Leon''s decision of 2026-11-01 (link and deflate): the registered condition is worded as in clause (iii) of the registration result version 8 (the gravitational connection, the one preserving the frozen point, keeps it parallel in the physical scale: the field-space premise), the basis is repinned to that version, and a marked deflation note records that on the reduced field space Lambda is a constant parameter and w = -1 is the LambdaCDM equation of state, so a confirmed w = -1 supports LambdaCDM with a frozen point but is not independent evidence for the premise, while w != -1 refutes it and LambdaCDM. The kill condition is unchanged.'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'The Henneaux-Teitelboim promotion was adopted on 2026-10-23; w = -1 is unchanged (Lambda constant on every solution of either branch), and N is now initial data under the promoted action. Version 1 -> 2.'
  env: table row
  source: T17 tab:stances
  typing:
    by: ai-typing-pass
    note: 'Kept the single basis use (the dark-energy paper''s registration proposition, which states
      the prediction and its condition); kill condition left as filled. Levels pass: conditions already
      kept.'
derivations:
- name: basis
  uses:
  - dark-energy.vacuum-region-registration-condition@8
---

## formal
Dark energy cannot evolve: $w = -1$ exactly, at every epoch; registered with its one condition, that on matter-filled regions the gravitational connection, the $\Cl(2,4)$ connection that preserves the frozen point $I$, keeps it parallel in the physical scale, $\ip{X}{I} = 1$ (Theorem \claimref{dark-energy.vacuum-region-registration-condition}(iii)); in that form the condition is the field-space premise (FS) of the gravitational action (Premise \claimref{synthesis.field-space-premise-parallel-frozen-point}), which the store adopts.

\emph{Note (deflation).} On the reduced field space of (FS) the norm $Q(I) = \Lambda/3$ is constant, so $\Lambda$ is a constant parameter and $w = -1$ is the $\Lambda$CDM equation of state. A confirmed $w = -1$ therefore supports $\Lambda$CDM with a frozen point but is not evidence for (FS) independent of $\Lambda$CDM; a confirmed $w \neq -1$ would refute (FS), and $\Lambda$CDM with it (Theorem \claimref{synthesis.parallel-frozen-point-on-matter-regions-is-the-field-space-premise}, Reading).

## technical
The stance reads dark energy as the norm of the frozen point, $Q(I) = \Lambda/3$. On the Einstein region the frozen point is parallel, so the norm cannot vary and enters the Einstein equations as stress-energy with $p = -\rho$, that is $w = -1$. The prediction extends this to every epoch: $w = -1$ exactly, with no evolution, under its one registered condition, that on matter-filled regions the gravitational connection, the one preserving the frozen point, keeps it parallel in the physical scale. That condition is the field-space premise (FS) of the gravitational action, which the store adopts.

On that field space $\Lambda$ is a constant parameter and $w = -1$ is the $\Lambda$CDM equation of state, so a confirmed $w = -1$ supports $\Lambda$CDM with a frozen point and is not independent evidence for (FS). A confirmed detection of $w \neq -1$ at any epoch would refute it, with no parameter available to absorb the result.

## lay
The framework says dark energy is not a substance that can change over time but a fixed geometric quantity. That means its equation of state, the ratio of its pressure to its energy density, must be exactly minus one at all times. This rests on one stated assumption about how the underlying geometry extends into regions filled with matter, an assumption the series now adopts for its law of gravity. Under that assumption dark energy behaves exactly as in the standard cosmological model, so a measurement that it never changes would agree with the series without being separate evidence for the assumption. Any confirmed measurement of a different value at any point in cosmic history would rule the idea out.

## one-liner
Under its one registered condition, the field-space premise (FS) (the gravitational connection keeps the frozen point parallel in the physical scale), the framework predicts that dark energy has $w = -1$ exactly at every epoch, with no evolution; on that field space this is the $\Lambda$CDM equation of state, not independent evidence for (FS).
