---
id: neutrino.mixing-none-leading-order
kind: claim
version: 1
title: 'Mixing: none at leading order'
status: conjectured
region: neutrino
subject: neutrinos
tags:
- flavour-and-mixing
- confronted-with-data
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T15, deposited version
review: typed
lineage:
  motivated_by:
  - neutrino.rank-one-seesaw-ordering-sum-double
  - neutrino.imported-indifference-faces-democratic-alignment-rank
  - neutrino.breaking-relation
locators:
  paper: T15
  number: Obs 4.8
  label: obs:mixing
  line: 675
extraction:
  env: observation
  unresolved_refs:
  - rem:branch
  flags:
  - conjecture with no referenced motivation
  typing:
    by: ai-typing-pass
    note: 'kept as a conjecture: the observation is mostly unscripted estimates and an open question,
      with only the shared eigenvector checked by script; motivated by the rank-one seesaw, the democratic
      alignment that makes the charged-lepton matrix rank one, and the breaking lemma. Levels pass: the
      lay level and one-liner no longer say there is no mixing at all; at leading order the heavy-heavy
      mixing vanishes and the light-plane mixing is undetermined, as the formal states, and the lay level
      now says "at leading order".'
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants: []
    added_about: []
    verdict: standalone
    note: Terminal observation (unscripted estimates and an open requirement for successor problem 1);
      nothing relies on it and no definition bears on it.
---

## formal
The structure delivers no large mixing by itself. The charged-lepton matrix and the light neutrino matrix are both rank one along the same democratic direction $u'$ at leading order, so their heavy eigenvectors coincide, the heavy-heavy mixing vanishes, and the mixing in the degenerate light plane is undetermined. All three observed angles must therefore come from the breaking, and the requirement is stated as a number: the observed $|U_{\tau 3}|^{2} = c_{13}^{2}c_{23}^{2}$ lies in $(0.39, 0.55)$ at $\sin^{2}\theta_{23} \in (0.44, 0.60)$ \cite{NuFIT2024}, so the two heavy eigenvectors, the charged lepton's and the neutrino's, must be separated by between about $42$ and $51$ degrees, about $47$ at the centre of the bracket (the conversion to degrees is not scripted). What the breaking of Remark \ref{rem:branch} supplies at the $S_{3} \to S_{2}$ direction is a tilt of about $13$ degrees on the neutrino side and about $3$ on the charged side (unscripted estimates at that remark's instance); whether a breaking of the size that remark fixes can supply a near-maximal $\theta_{23}$ is open, and is the number successor problem (1) must meet. The PMNS numbers depend on the same breaking and are this paper's observation, not an import. The classic democratic-texture route to large angles (the quark-sector construction of \cite{HHW1978}, carried to the lepton sector by a later literature not cited here) needs a democratic charged-lepton matrix against a non-democratic neutrino one, which this structure does not supply at leading order. The script confirms that both leading forms have $u'$ as the eigenvector of their nonzero eigenvalue.

## technical
At leading order the charged-lepton matrix and the light neutrino matrix are both rank one along the democratic direction $u'$, so their heavy eigenvectors coincide, the heavy-heavy mixing vanishes, and the mixing in the degenerate light plane is undetermined. All three observed angles must then come from the breaking. The observed $|U_{\tau 3}|^{2} = c_{13}^{2}c_{23}^{2} \in (0.39, 0.55)$ requires the two heavy eigenvectors to be separated by about $42$ to $51$ degrees.

At the breaking instance used for the masses, unscripted estimates give a tilt of about $13$ degrees on the neutrino side and $3$ on the charged side; whether a breaking of that size can supply a near-maximal $\theta_{23}$ is open. The classic democratic-texture route to large angles needs a democratic charged-lepton matrix against a non-democratic neutrino one, which this structure does not supply at leading order.

## lay
Neutrinos change type as they travel, and the amount of this mixing is large. In this framework, at leading order (a first approximation), the heaviest charged lepton and the heaviest neutrino line up along the same direction, so there is no mixing between them, and the mixing among the two lighter ones is left undetermined. All the observed mixing must therefore come from the corrections that break that alignment, and whether they can be large enough is an open question.

## one-liner
At leading order the rank-one structure gives no heavy-heavy lepton mixing and leaves the light-plane mixing undetermined, so all three observed angles must come from the breaking.
