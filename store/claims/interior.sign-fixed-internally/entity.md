---
id: interior.sign-fixed-internally
kind: claim
version: 5
title: The sign is fixed internally
status: proved
region: interior
subject: einstein
tags: [tractors, cosmological-constant, forcing-and-uniqueness]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T06, deposited version
- name: Claude Opus 5.5
  role: 'consistency pass, stale paper references replaced by the series conventions'
  version: 5
  source: maintainer pass 2026-11-07 (consistency)
review: typed
derivations:
- name: main
  uses:
  - interior.non-null-stabilisers-section-they-act@5
  - interior.scale-tractor-leaves-cone@8
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_displayed_sign_attaches_de_sitter
- kind: check
  ref: check.py::check_opposite_sign_attaches_anti_de_sitter
locators:
  paper: T06
  number: Lem 4.8
  label: lem:signpin
  line: 544
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The formal pointed twice to the paper''s Section sec:setting; the conventions are the series'' and the store sign of the definition it already cites.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: with the displayed Schouten sign Lambda > 0 gives Q(I) = Lambda/3 > 0, I^perp (1,4), stabiliser so(1,4) and the de Sitter section; the opposite sign gives Q(I) < 0, (2,3), so(2,3) and anti-de Sitter. Version 3 -> 4.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the convention Ric = Lambda g for de Sitter is the store curvature sign of the GTG field strength (R(B) = (Lambda/3) B), and the connection is the tractor gauge field on flat spacetime. Proof prefixed.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  typing:
    by: ai-typing-pass
    note: 'Both uses are the two results the proof combines; kept.'
  env: lemma
  eqrefs: 1
---

## formal
The relative sign of the Schouten slots in \eqref{eq:tractorconn}, the $\nO \wedge \Sch(\hb^{-1}(a))$ term of the tractor gauge field of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}, is determined, within the series' conventions, by the requirement that the flat-model section attached to a $\Lambda > 0$ Einstein representative be de Sitter space: with the signs as displayed, $\Lambda > 0$ gives $Q(I_g) = \Lambda/3 > 0$, whose flat-model section is the de Sitter pseudosphere by Proposition \claimref{interior.non-null-stabilisers-section-they-act}(2); the opposite sign choice would attach the anti-de Sitter section to $\Lambda > 0$, contradicting the naming convention $\Ric_{ab} = \Lambda g_{ab}$, $R = 4\Lambda$ for de Sitter space, which is the store's curvature sign of the field strength, $\mathcal{R}(B) = \tfrac{\Lambda}{3}B$ on de Sitter space (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}).

## technical
The relative sign of the Schouten slots in the tractor connection, on flat spacetime the special-conformal part $\nO \wedge \Sch(\hb^{-1}(a))$ of the tractor gauge field, is not a free convention once the series' other conventions are fixed. With the displayed signs, a $\Lambda > 0$ Einstein representative has $Q(I_g) = \Lambda/3 > 0$, whose flat-model section is the de Sitter pseudosphere.

The opposite sign would give $Q(I_g) = -\Lambda/3$ and attach the anti-de Sitter section to $\Lambda > 0$, contradicting the naming convention $\Ric_{ab} = \Lambda g_{ab}$, $R = 4\Lambda$ for de Sitter space, the store's sign of the gravitational field strength. Since the section metric is the Einstein representative in the flat model, the assignment is forced.

## lay
Formulas in this area of geometry come with sign choices that differ between textbooks. This result shows that, given the series' other conventions, including its sign for the strength of the gravitational field, one sign is forced: only that choice makes a positive cosmological constant correspond to de Sitter space, as the naming requires.

## one-liner
Within the series' conventions, the sign of the Schouten term of the tractor gauge field is forced by requiring that $\Lambda > 0$ give the de Sitter section.
