---
id: one-relation.measure-indifference-borns-rule-located
kind: claim
version: 3
title: 'The measure from indifference: Born''s rule located'
status: proved
region: one-relation
subject: one-relation
tags: [indifference, measurement-and-records, recovers-known-physics]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T16, deposited version
- name: Claude Opus 5.5
  role: 'maintainer pass, uses edge to the imported envariance Fact at Leon''s decisions'
  version: 3
  source: maintainer pass 2026-11-07 (decisions)
review: typed
derivations:
- name: main
  uses:
  - one-relation.dirac-current-conserved-density@3
  - one-relation.imported-indifference-instrument@4
  - one-relation.imported-envariance-born-rule@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T16.py
  tags:
  - label:prop:born
- kind: check
  ref: check.py::check_density_is_positive_and_frame_relative
- kind: check
  ref: check.py::check_indifference_forces_equality_on_transitive_orbits
- kind: check
  ref: check.py::check_fine_graining_returns_squared_norms
locators:
  paper: T16
  number: Prop 6.2
  label: prop:born
  line: 817
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 2 -> 3. Decision item B5 (routine): the fine-graining and continuity steps, Zurek''s envariance argument imported with its critique, now pin the new Fact one-relation.imported-envariance-born-rule (uses edge added, cited in the formal and the proof); statement unchanged.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: J = psi gamma_0 psi~ for even psi: J . gamma_0 is the sum of squares of psi, J^2 = a^2 + b^2, and a boosted frame gives a different positive density; invariant weight spaces equal the orbit counts (uniform on transitive orbits); fine-graining returns the squared norms. Version 1 -> 2.'
  env: proposition
  context_refs:
  - one-relation.schr-odinger-slow-shadow
  typing:
    by: ai-typing-pass
    note: 'Kept both edges; the slow-shadow proposition in context_refs is cited only for the unsourced
      frame and is not a premise; the envariance argument (Zurek) is the standard counterpart but is not
      in the store, so no standard-route derivation. Levels pass: the lay level now marks indifference
      as a premise rather than a theorem, keeps the frame-relativity of the density and says the result
      is conditional.'
---

## formal
The unique conserved density among constant sesquilinear ones is the Dirac density of Lemma \claimref{one-relation.dirac-current-conserved-density}, the $\gamma_{0}$ component of the geometric current $J = \psi\gamma_{0}\tilde{\psi}$: positivity, conservation and uniqueness in that class are proved. The current is fixed up to scale; the \emph{density} is its component along a timelike $\gamma_{0}$, which is the laboratory's rest frame, declared unsourced in Proposition \claimref{one-relation.schr-odinger-slow-shadow}(3): the located Born density is frame-relative, and the paper says so here rather than leaving it implicit in the lemma. What remains of Born's rule is the identification of this density with occupation weight, and the framework closes part of the remaining gap with its founding principle, the indifference premise (Fact \claimref{one-relation.imported-indifference-instrument}, a structural premise of the series and not a theorem): for a superposition of equal-norm, flag-degenerate components, any unequal weight assignment would instantiate a preference nothing caused, so indifference forces equality; rational weights follow by fine-graining into equal-norm constituents permuted by Witt rotations that are exact symmetries of the frozen vacuum; and continuity completes the squared-norm measure as the only assignment consistent with vacuum indifference. This is the envariance argument (Fact \claimref{one-relation.imported-envariance-born-rule}, \cite{Zurek2005}) transplanted into the framework's vocabulary, and it inherits that argument's standing critique: the fine-graining step presupposes that weights compose additively, which is a fragment of the probabilistic reading it derives. That presupposition is hereby isolated as the residual postulate, smaller than Born and not zero: \emph{that weights exist and add}. Structural-conditional level, with the refutation condition stated: exhibit a weight assignment respecting vacuum indifference that is not the squared norm, and the reduction fails.

## technical
The unique conserved density among constant sesquilinear ones is the Dirac density, the $\gamma_{0}$ component of the geometric current $J = \psi\gamma_{0}\tilde{\psi}$; it is positive, conserved and unique in that class, and frame-relative, since $\gamma_{0}$ is the laboratory's unsourced rest frame. Identifying it with occupation weight uses the indifference premise: equal-norm, flag-degenerate components related by exact vacuum symmetries must receive equal weight; fine-graining then gives rational weights and continuity the squared-norm measure.

This is the envariance argument in the framework's vocabulary and it inherits that argument's critique: fine-graining presupposes that weights exist and add, which is isolated as the residual postulate, smaller than Born's rule but not nothing. The level is structural and conditional; a weight assignment respecting vacuum indifference that is not the squared norm would refute the reduction.

## lay
Born's rule says the chance of a quantum outcome is the squared size of its part of the wave. Here the relevant density is fixed as the unique conserved, positive one, measured in the laboratory's rest frame. Then the series' indifference premise, a declared starting point and not a theorem, that nothing may prefer one of several equivalent outcomes, forces equal chances for equal parts and builds up to the squared-size rule. One assumption remains, that chances exist and add up, and the paper names it as what is still postulated, so the result is conditional on both.

## one-liner
Under the indifference premise, and granting that weights exist and add, the squared-norm measure on the unique conserved Dirac density is the only weight assignment consistent with vacuum indifference.
