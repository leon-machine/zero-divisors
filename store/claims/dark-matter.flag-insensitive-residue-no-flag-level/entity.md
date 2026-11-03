---
id: dark-matter.flag-insensitive-residue-no-flag-level
kind: claim
version: 3
title: 'The flag is insensitive to the residue: no flag-level strengthening'
status: proved
region: dark-matter
subject: dark-matter
tags: [witt-index, hyperbolic-plane, towers-by-residue, no-go]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14, deposited version
review: typed
derivations:
- name: main
  uses:
  - std-algebra.witt-extension@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T14.py
  tags:
  - label:prop:flaggable
- kind: check
  ref: check.py::check_witt_transitivity_on_hyperbolic_pairs
- kind: check
  ref: check.py::check_paper_witnesses_13_and_22
- kind: check
  ref: check.py::check_definite_residue_has_flag_but_no_plane
locators:
  paper: T14
  number: Prop 3.2
  label: prop:flaggable
  line: 164
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.witt-extension where the proof uses them. Version 2 -> 3.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: Witt transitivity by explicit reflections on 21 independently built hyperbolic pairs in all nondefinite P3 representatives; the (1,3) and (2,2) witnesses and Jacobian rank; definite r = 4 with a complex maximal isotropic subspace. Version 1 -> 2.'
  env: proposition
  context_refs:
  - dark-matter.flag-bit-exists-exactly-tower-dimension
  - dark-matter.which-towers-can-carry-arrow
  typing:
    by: ai-typing-pass
    note: The statement's clauses quoting the flag-bit theorem and the which-towers corollary are real
      dependencies, but neither edge was added because both would close a cycle through the two-families
      proposition, which uses this claim only for Witt's theorem (an edge for its owner to review).
---

## formal
The sterile towers are not the unflaggable ones, and no flag-level strengthening of the count exists: in every nondefinite representative the isometry group acts transitively on hyperbolic planes and on the null lines within them (Witt's theorem), so no representative offers a distinguished plane or half of one, and the descent's flag is as uncaused in $(1,3)$ as in $(2,2)$. The definite representatives of $r = 4$ contain no hyperbolic plane, so no \emph{rung-level} flag can be chosen in them, but the descent's flag, a maximal isotropic of the complexified ambient, exists there as for every even residue (Theorem \claimref{dark-matter.flag-bit-exists-exactly-tower-dimension}); the sterility of $r = 4$ is the single-clock filter restated. So the exclusion of $r = 0$ rests on the two-time instability import alone, and a stabilisation of two-time dynamics is an open fork: six causal towers, the $r = 0$ tower an \emph{oriented} one (Corollary \claimref{dark-matter.which-towers-can-carry-arrow}), a Kleinian copy of the Standard Model with an asymmetric share of one, costed in Section \ref{sec:premises}.

## technical
In every nondefinite representative the isometry group acts transitively on hyperbolic planes and on the null lines within them, by Witt's theorem, so no representative offers a distinguished plane or half of one: the descent's flag is as uncaused in $(1,3)$ as in $(2,2)$. The definite representatives of residue $4$ contain no hyperbolic plane, so no rung-level flag can be chosen in them, but the descent's flag, a maximal isotropic subspace of the complexified ambient, exists there as in every even residue; the sterility of residue $4$ is the single-clock filter restated.

Hence the sterile towers are not the unflaggable ones and no flag-level strengthening of the count exists. The exclusion of residue $0$ rests on the imported two-time instability alone, and a stabilisation of two-time dynamics is an open fork: six causal towers, with the residue-$0$ tower an oriented one, a Kleinian copy of the Standard Model with an asymmetric share of one.

## lay
One might hope to rule out some hidden worlds more firmly by showing they cannot support the orientation choice made at the descent. This result shows that hope fails: symmetry treats every candidate choice alike in every relevant world, ours included. So the hidden world with two time directions is excluded only because two-time physics is unstable, and if that instability were ever cured it would return as an oriented copy of the Standard Model.

## one-liner
Witt's theorem makes the descent's flag equally uncaused in every nondefinite representative, so no flag-level strengthening of the tower count exists and the exclusion of residue $0$ rests on the two-time instability import alone.
