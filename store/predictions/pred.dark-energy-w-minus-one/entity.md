---
id: pred.dark-energy-w-minus-one
kind: prediction
version: 5
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
- name: Claude Opus 5.5
  role: 'consistency pass, label of the cited result corrected'
  version: 4
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Fable 5.2
  role: 'kill condition registered as a region with its significance rule; no-fallback note; observation row'
  version: 5
  source: maintainer pass of 2026-11-10
review: typed
kill_condition:
  threshold: 'Two independent surveys each exclude the point $(w_0, w_a) = (-1, 0)$ of the two-parameter
    form $w(a) = w_0 + w_a(1 - a)$ at five standard deviations or more, each survey allowed the shared
    CMB prior, by the collaboration''s published frequentist distance of that point (Bayesian evidence
    recorded beside it); or, in the model-independent reading, a detection of $w \neq -1$ at any epoch
    confirmed by the same rule; with no parameter available to absorb it. The rule is conservative.'
  data_source: Stage IV dark-energy surveys with their own late-time distance or growth data (at present
    DESI and the Dark Energy Survey), each alone or with the CMB
  registered: '2026-11-10 (significance, number of surveys and statistic fixed by Leon Butler; replaces
    the wording of 2026-08, T17 stance table, row 2: "A confirmed detection of w different from -1 at
    any epoch, with no parameter available to absorb it")'
observations:
- date: 2026-11
  dataset: Dark Energy Survey, full survey (3x2pt, supernovae, BAO), alone and with DESI DR2 BAO and CMB;
    DESI DR2 BAO with CMB
  result: 'Against the rule registered on 2026-11-10 (two independent surveys, each at five sigma): not
    met. DES alone: w0 = -0.84 +/- 0.10, wa = -0.44 +0.60/-0.55, 2.2 sigma from (w0, wa) = (-1, 0). DES
    with DESI DR2 BAO: w0 = -0.84 +0.06/-0.07, wa = -0.53 +0.33/-0.28, 2.3 sigma. Adding the primary
    CMB: w0 = -0.82 +/- 0.05, wa = -0.63 +0.21/-0.18, 3.0 sigma; 2.3 to 3.2 sigma as one probe at a
    time is left out. DESI DR2 BAO with CMB: 3.1 sigma, and 2.8 to 4.2 sigma with a supernova sample
    added, depending on the sample. Every fit lies in the quadrant w0 > -1, wa < 0.'
  verdict: contested
  source: DES Collaboration, arXiv:2605.27221 (2026); DESI Collaboration, arXiv:2503.14738 (2025)
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
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version 4 -> 5, at Leon''s decisions of 2026-11-10: the kill condition, which named neither a significance, a number of surveys nor a parametrisation, is registered as the point (w0, wa) = (-1, 0) excluded at five standard deviations by each of two independent surveys (shared CMB prior allowed, published frequentist distance, Bayesian evidence recorded), with the earlier wording at any epoch kept as the model-independent reading and the rule stated to be conservative; a note labelled argued records that the series has no fallback and why the stored w = -1/4 branch is not one; observation row of 2026-11 added (abstracts of both sources read on the web on 2026-11-10). The prediction itself is unchanged.'
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The registration result was cited as a Theorem; it is a Proposition (T10 Prop. 4.2), as the notes and the result itself name it; wording only.'
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
Dark energy cannot evolve: $w = -1$ exactly, at every epoch; registered with its one condition, that on matter-filled regions the gravitational connection, the $\Cl(2,4)$ connection that preserves the frozen point $I$, keeps it parallel in the physical scale, $\ip{X}{I} = 1$ (Proposition \claimref{dark-energy.vacuum-region-registration-condition}(iii)); in that form the condition is the field-space premise (FS) of the gravitational action (Premise \claimref{synthesis.field-space-premise-parallel-frozen-point}), which the store adopts.

\emph{Note (deflation).} On the reduced field space of (FS) the norm $Q(I) = \Lambda/3$ is constant, so $\Lambda$ is a constant parameter and $w = -1$ is the $\Lambda$CDM equation of state. A confirmed $w = -1$ therefore supports $\Lambda$CDM with a frozen point but is not evidence for (FS) independent of $\Lambda$CDM; a confirmed $w \neq -1$ would refute (FS), and $\Lambda$CDM with it (Theorem \claimref{synthesis.parallel-frozen-point-on-matter-regions-is-the-field-space-premise}, Reading).

\emph{Note (the registered region).} In the two-parameter form $w(a) = w_{0} + w_{a}(1 - a)$ the prediction is the single point $(w_{0}, w_{a}) = (-1, 0)$. The series counts it refuted when two independent surveys each exclude that point at five standard deviations or more. Two surveys are independent when their late-time data (galaxy, supernova and lensing samples) are disjoint; each may use the shared CMB prior. The significance is the collaboration's published frequentist distance of the point (the two-parameter $\Delta\chi^{2}$ converted to standard deviations); the Bayesian evidence is recorded beside it and does not decide. The wording ``at any epoch'' stays as the model-independent reading: an exclusion of constant dark-energy density at some epoch, at the same significance and by two independent surveys, in an analysis not tied to the two-parameter form, counts the same. The rule is conservative: under it the series counts $w = -1$ as standing through releases in which a combined analysis reports a preference for evolution at three or four standard deviations, and it says so here.

\emph{Note (no fallback; argued).} A search of the store, not a proof, finds no adopted structure that permits a dark-energy equation of state different from $-1$ on an accelerating solution, so the series has no fallback for $w \neq -1$. Of the two stored ways of making the norm a variable, the promoted norm keeps $w = -1$ on every solution, and the norm released locally gives, under hypothesis (Mat), for the bare functional on isotropic fields with flat slices, a cosmological term that tracks one fluid with deceleration, no solution with radiation and no prediction in vacuum (Theorem \claimref{synthesis.norm-released-locally-on-isotropic-fields-tracks-dust-and-never-accelerates}(iv)-(vii), within its scope). The same search finds one stored structure with a late-time equation of state different from $-1$: the branch of Theorem \claimref{synthesis.unit-ball-clauses-hold-at-one-epoch-unless-hidden-direction-co-expands}(ii) with R3 standing and a static hidden direction, in which a fraction between $0.316$ and $0.317$ of the dark matter dilutes with effective $w = -\tfrac14$. It is not a fallback: the branch is not adopted; it is a dark-matter component and not a variable norm, with no pressure derived; read with the constant as one dark energy it has $w > -1$ at every epoch and approaches $-1$ from above, so $w_{a} > 0$ and no crossing of $-1$, against the quadrant $w_{0} > -1$, $w_{a} < 0$ of the survey fits in the observations below; and its share grows by the factor between $189$ and $190$ from $1 + z = 1090$ stated there, so the dark-matter densities inferred at that epoch and today would disagree (not confronted with data here). The exponent of the hidden direction in that branch is therefore not a parameter available to absorb a detection, and adopting it after one would be a fit. A detection by the registered rule would refute (FS) and the reading of dark energy as the frozen point's norm, and the series would need a new premise.

## technical
The stance reads dark energy as the norm of the frozen point, $Q(I) = \Lambda/3$. On the Einstein region the frozen point is parallel, so the norm cannot vary and enters the Einstein equations as stress-energy with $p = -\rho$, that is $w = -1$. The prediction extends this to every epoch: $w = -1$ exactly, with no evolution, under its one registered condition, that on matter-filled regions the gravitational connection, the one preserving the frozen point, keeps it parallel in the physical scale. That condition is the field-space premise (FS) of the gravitational action, which the store adopts.

On that field space $\Lambda$ is a constant parameter and $w = -1$ is the $\Lambda$CDM equation of state, so a confirmed $w = -1$ supports $\Lambda$CDM with a frozen point and is not independent evidence for (FS). A confirmed detection of $w \neq -1$ at any epoch would refute it, with no parameter available to absorb the result.

What counts as confirmed is registered. In the two-parameter form $w(a) = w_{0} + w_{a}(1 - a)$ the prediction is the point $(w_{0}, w_{a}) = (-1, 0)$, and it is refuted when two independent surveys (disjoint late-time data, the CMB prior allowed in each) each exclude that point at five standard deviations by the collaboration's published frequentist distance, with the Bayesian evidence recorded beside it; a model-independent exclusion of constant dark-energy density at some epoch counts by the same rule. The rule is conservative: combined analyses at three or four standard deviations do not meet it. The series has no fallback (argued, from a search of the store and not a proof): the promoted norm keeps $w = -1$, the locally released norm tracks one fluid and decelerates within the scope of the stored result, and the one stored structure with a late-time equation of state different from $-1$, an unadopted dark-matter branch with effective $w = -\tfrac14$, has $w_{a} > 0$ and never crosses $-1$, the opposite of the survey fits, and would make the dark-matter densities inferred early and late disagree.

## lay
The framework says dark energy is not a substance that can change over time but a fixed geometric quantity. That means its equation of state, the ratio of its pressure to its energy density, must be exactly minus one at all times. This rests on one stated assumption about how the underlying geometry extends into regions filled with matter, an assumption the series now adopts for its law of gravity. Under that assumption dark energy behaves exactly as in the standard cosmological model, so a measurement that it never changes would agree with the series without being separate evidence for the assumption. Any confirmed measurement of a different value at any point in cosmic history would rule the idea out. What counts as confirmed is fixed in advance: two independent surveys must each exclude an unchanging dark energy at five standard deviations, the usual threshold for a discovery, by the survey team's own published measure. This is a cautious rule, and it means the series will keep the prediction standing through results that fall short of it, including combined analyses at three or four standard deviations. As far as a search of the collection shows, the series has nothing to fall back on if the rule is met: it would need a new assumption.

## one-liner
Under its one registered condition, the field-space premise (FS) (the gravitational connection keeps the frozen point parallel in the physical scale), the framework predicts that dark energy has $w = -1$ exactly at every epoch, with no evolution; on that field space this is the $\Lambda$CDM equation of state, not independent evidence for (FS); refuted when two independent surveys each exclude $(w_{0}, w_{a}) = (-1, 0)$ at five standard deviations (published frequentist distance, shared CMB prior allowed; a conservative rule), with no stored fallback (argued).
