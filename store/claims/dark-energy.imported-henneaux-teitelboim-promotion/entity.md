---
id: dark-energy.imported-henneaux-teitelboim-promotion
kind: claim
version: 5
title: 'Imported: the Henneaux-Teitelboim promotion'
status: imported
region: dark-energy
subject: dark-energy
tags:
- classical-theorem
- cosmological-constant
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T10, deposited version
review: typed
imported_from:
- citation: M. Henneaux and C. Teitelboim, The cosmological constant and general covariance, Phys. Lett.
    B 222 (1989), 195--199.
  key: HenneauxTeitelboim1989
locators:
  paper: T10
  number: Fact 5.11
  label: fact:ht
  line: 1059
extraction:
  maintainer_pass_2026_10_31:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Version 4 -> 5, at Leon''s decision of 2026-10-31: a marked note records that releasing the Stelle-West norm locally, with no three-form, is not this promotion and excludes Schwarzschild-de Sitter, citing the result that the norm is no local output. The imported statement is unchanged.'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'The store adopted the promotion on 2026-10-23 (programme.n-parameter-of-the-laws version 3); the imported statement is unchanged. Version 3 -> 4.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  typing:
    by: ai-typing-pass
    note: Imported literature fact; the transcription to the Stelle-West norm is described as an open
      decision, as the statement says.
  env: fact
  unresolved_refs:
  - rem:promotion
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants:
    - standard-model.trichotomy-what-kind-number
    added_about:
    - obj.dark-energy.four-ways-number-enters-theory-shape
    verdict: connected
    note: Import, so about only (the four-ways classification, since the promotion moves Lambda from a
      parameter of the laws to initial data); the trichotomy's clause (4) states the promotion's content
      and now uses and cites it.
about:
- obj.dark-energy.four-ways-number-enters-theory-shape
---

## formal
In the unimodular formulation of general relativity the cosmological constant is not a parameter of the action but the value of a Lagrange-multiplier field, conjugate to a cosmic-time variable, whose constancy $d\Lambda = 0$ is an equation of motion; $\Lambda$ is then a constant of integration, a label of the solution rather than of the theory, and the formulation is generally covariant. \emph{Provenance:} \cite{HenneauxTeitelboim1989}; the transcription to the Stelle-West norm, promoting the value $\Lambda/3$ of the constraint $Q(I) = \Lambda/3$ to that field, is Remark \ref{rem:promotion}'s; the series keeps $\Lambda$ fixed by the frozen point (the registered input) and records this promotion as the variational form of the Clausius route.

\emph{Note (a local release is not this promotion).} The promotion is global: $\Lambda$ is constant by its own equation of motion, with a conjugate three-form (a cosmic time) carrying the variational freedom. Releasing the norm of the Stelle-West vector locally instead, with no three-form, so that its value varies pointwise, gives for the frozen-point functional the pointwise equation $\epsilon(I, V, F, F) = 0$, which fails at every point of the Schwarzschild-de Sitter field with nonzero mass, and in the constant-coupling family with the MacDowell-Mansouri term a solution of constant norm needs the Weyl square constant, which that field also violates; such a release excludes Schwarzschild-de Sitter (Theorem \claimref{synthesis.stelle-west-norm-is-no-local-output}(iv)).

## technical
In the unimodular formulation of general relativity the cosmological constant is not a parameter of the action but the value of a Lagrange-multiplier field, conjugate to a cosmic-time variable, whose constancy $d\Lambda = 0$ is an equation of motion. $\Lambda$ is then a constant of integration, a label of the solution rather than of the theory, and the formulation is generally covariant. Transcribing this to the Stelle-West norm, by promoting the value $\Lambda/3$ of the constraint $Q(I) = \Lambda/3$ to such a field, is a separate decision that is left open. Released locally instead, without the three-form, the norm obeys a pointwise equation that every Schwarzschild-de Sitter black hole violates, so a local release excludes those fields.

## lay
In a well-known reformulation of general relativity, the cosmological constant stops being a fixed setting of the theory and becomes a quantity that the equations hold constant, much like a conserved charge. Different solutions can then carry different values. Whether to make the same move for the frozen point's length is recorded as an open choice.

## one-liner
In the Henneaux-Teitelboim unimodular formulation of general relativity, $\Lambda$ is a constant of integration fixed by an equation of motion rather than a parameter of the action.
