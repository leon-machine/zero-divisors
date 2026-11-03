---
id: standard-model.no-tower-but-one-contributes-towers
kind: claim
version: 3
title: No tower but this one contributes to this tower's running
status: proved
region: standard-model
subject: standard-model
tags: [running-and-unification, towers-by-residue, superselection, mirror-sector]
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
  - standard-model.connection-forced@4
  - standard-model.gauge-algebra-minimal-massive-composite@4
  - standard-model.imported-coefficient-sum-indices@1
  - standard-model.imported-sectors-superselection-mirror-copy@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_other_tower_fields_have_zero_index
- kind: check
  ref: check.py::check_other_towers_leave_this_tower_running_unchanged
locators:
  paper: T12
  number: Prop 8.5
  label: prop:towers
  line: 1309
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: indices of another tower''s fields vanish (traces of squares of the Cartan generators acting only through the hierarchy fibre), so they add (0,0,0) and leave (41/10, -19/6, -7) unchanged. Version 2 -> 3.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Only the proof had twistor language (the two-twistor ladder), now the ladder of two conformal spinors.'
  source_title: |-
    No tower but this one contributes to this tower's running
  source_formal: |-
    Under the sector decomposition of Fact \claimref{standard-model.imported-sectors-superselection-mirror-copy}, let $\phi$ be any field of a tower other than this one, of either statistics and any multiplicity. Then $\phi$ has index zero under each of $SU(2)$, $SU(3)$ and $U(1)_{Y}$ of this tower, and contributes zero to each of $b_{1}, b_{2}, b_{3}$ at every scale. Consequently the mirror tower and the four odd-dimensional towers together contribute $\Dl = (0, 0, 0)$ to this tower's one-loop run, and the partner-like content Proposition \claimref{standard-model.spectrum-run} demands, if the framework supplies it, is supplied by this tower.
  env: proposition
  context_refs:
  - standard-model.spectrum-run
  typing:
    by: ai-typing-pass
    note: 'All four edges are premises of the proof and were kept; the spectrum-run context reference
      only names what the conclusion is about, so it was not added. Levels pass: the lay level now presents
      gravity-only interaction between towers as the sector decomposition the result is stated under.'
---

## formal
Under the sector decomposition of Fact \claimref{standard-model.imported-sectors-superselection-mirror-copy}, let $\phi$ be any field of a tower other than this one, of either statistics and any multiplicity. Then $\phi$ has index zero under each of $SU(2)$, $SU(3)$ and $U(1)_{Y}$ of this tower, and contributes zero to each of $b_{1}, b_{2}, b_{3}$ at every scale. Consequently the mirror tower and the four odd-dimensional towers together contribute $\Dl = (0, 0, 0)$ to this tower's one-loop run, and the partner-like content Proposition \claimref{standard-model.spectrum-run} demands, if the framework supplies it, is supplied by this tower.

## technical
Under the sector decomposition of the superselection fact, a field $\phi$ of any other tower carries no component of this tower's hierarchy bundle $\mathcal{H}$, since such a component would give a non-gravitational coupling between towers, which the decomposition excludes. As this tower's gauge fields are connections on $\mathcal{H}$, every generator acts as zero on $\phi$.

So $\phi$ has index zero under each of $SU(2)$, $SU(3)$ and $U(1)_{Y}$ and, by the index formula, adds nothing to $b_{1}, b_{2}, b_{3}$ at any scale, for either statistics and any multiplicity. The mirror tower and the four odd-dimensional towers therefore contribute $\Dl = (0, 0, 0)$ to this tower's one-loop run, and any partner-like content the running demands, if the framework supplies it, is supplied by this tower.

## lay
The framework contains several towers, separate copies of matter; under its sector decomposition they interact with one another only through gravity. A particle from another tower feels none of our tower's forces, so it cannot change how the strengths of our forces vary with energy. Any extra particles needed to make our forces' strengths meet must therefore come from our own tower, if the framework supplies them at all.

## one-liner
Under the sector decomposition, fields of other towers have zero index under this tower's gauge factors and add nothing to its running coefficients.
