---
id: standard-model.bidoublet-complex
kind: claim
version: 11
title: A second doublet coupling is needed; the complex bidoublet supplies it
status: proved
region: standard-model
subject: standard-model
tags: [symmetry-breaking, flavour-and-mixing, confronted-with-data]
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
- name: Claude Opus 5.5
  role: strengthened check
  version: 11
  source: maintainer pass of 7 November 2026
review: typed
derivations:
- name: main
  uses:
  - standard-model.one-vev-vector-relations-breaking-pattern@7
  - standard-model.hyp-s-slot-statistics@10
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_real_rung_vector_has_conjugate_coefficients
- kind: check
  ref: check.py::check_mass_form_magnitudes
- kind: check
  ref: check.py::check_one_rung_vector_gives_equal_up_and_down_masses
- kind: check
  ref: check.py::check_two_couplings_separate_up_and_down
locators:
  paper: T12
  number: Cor 10.9
  label: cor:complexrung
  line: 1972
extraction:
  maintainer_pass_warnings:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 11: check_one_rung_vector_gives_equal_up_and_down_masses now also asserts the common mass squared |b|^2 of each sample by hand-stated value, so the mutation test has literals to perturb.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: x gamma_6 + y gamma_7 = a v_4 + conj(a) w_4 over Q(i), and the mass-form magnitudes |a|, |b| on the sixteen. Version 6 -> 7. Restated weaker (Leon 2026-10-23), version kept at 7, status proved: title now A second doublet coupling is needed; the complex bidoublet supplies it; under the c* reading of the one-vev Corollary one rung vector gives m_u = m_d at tree level whether real or complex, so m_t != m_b needs a second independent doublet coupling, which a complex bidoublet supplies (b = conj(a) for a real vector kept as the first sentence; all levels; a first proof sentence records the change); the check now also tests equal up-type and down-type magnitudes for one real or complex vector through c*, and unequal ones for two couplings. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 7 -> 8. Sample inputs moved to module level; no change to what is tested (rung vector built with the module''s rung(a, b), setdefault removed). Version 8 -> 9. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 9 -> 10.'
  maintainer_pass_2026_10_23_b:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Under the reading adopted on 2026-10-23 (up-type masses through the conjugate rung vector c*, Corollary standard-model.one-vev-vector-relations-breaking-pattern version 4), one coupling gives equal up-type and down-type entries, so the argument here that a complex bidoublet resolves m_t != m_b by the c reading no longer applies; the hierarchy needs a second coupling or another source. Version 5 -> 6.'
  i4_conversion:
    by: ai-i4-pass
    date: 2026-10-21
    converted:
    - 'proof and technical level: the rung-plane Majorana gamma_7 = I4(v4 - w4) and the coefficients (x + yI4), (x - yI4) on the Witt pair v4, w4 of a tower plane, conjugation read in span{1, I4}'
    kept:
    - 'formal level: no explicit i; b = conj(a) now means conjugation in span{1, I4}'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Formal level and proof have no twistor language; only the lay level was reworded. The i in a = x + iy is the Fock module''s; TWGA E4.1 would read it as I4 on a tower plane, but that changes the computation''s algebra, so it is kept.'
  source_title: |-
    The bidoublet is complex
  source_formal: |-
    Under Hypothesis (S), a real vector of a rung plane, $x\,\gamma_{6} + y\,\gamma_{7}$ with $x$ and $y$ real, equals $a\,v_{4} + b\,w_{4}$ with $b = \bar{a}$, so $|a| = |b|$, and by Corollary \claimref{standard-model.one-vev-vector-relations-breaking-pattern} $m_{u} = m_{d}$ at tree level. Since $m_{t} \ne m_{b}$, the rung field is complex: two electroweak doublets, a complex bidoublet.
  env: corollary
  context_refs:
  - standard-model.one-vev-vector-relations-breaking-pattern
  typing:
    by: ai-typing-pass
    added:
    - standard-model.one-vev-vector-relations-breaking-pattern
    - standard-model.hyp-s-slot-statistics
    note: 'Added the one-vev corollary, which the statement invokes ("by Corollary") for m_u = m_d. Hypothesis
      pass: assumes standard-model.hyp-s-slot-statistics added because its statement holds under Hypothesis
      (S). Levels pass: lay now keeps Hypothesis (S), which it had dropped.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.one-vev-vector-relations-breaking-pattern
    stated_role:
    - standard-model.hyp-s-slot-statistics
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
Under Hypothesis (S), a real vector of a rung plane, $x\,\gamma_{6} + y\,\gamma_{7}$ with $x$ and $y$ real, equals $a\,v_{4} + b\,w_{4}$ with $b = \bar{a}$, so $|a| = |b|$. By Corollary \claimref{standard-model.one-vev-vector-relations-breaking-pattern}, with the up-type masses read through the conjugate $c^{*}$, one rung vector $c = a\,v_{4} + b\,w_{4}$, real or complex, gives $m_{u} = m_{d}$ at tree level. So $m_{t} \ne m_{b}$ needs a second independent doublet coupling, and a complex bidoublet, carrying two electroweak doublets, supplies one.

## technical
Under (S), a real vector of a rung plane, $x\,\gamma_{6} + y\,\gamma_{7}$ with $x, y$ real, equals $(x + yI_{4})\,v_{4} + (x - yI_{4})\,w_{4}$, with the imaginary unit $I_{4}$, which commutes with the rung modes, so its coefficients $a, b$ on $v_{4}, w_{4}$ satisfy $b = \bar{a}$ and $|a| = |b|$. Under the one-vev relations, with the up-type masses read through the conjugate vector $c^{*}$ as the Standard Model uses the conjugate doublet, a single rung vector gives $m_{u} = m_{d}$ at tree level whether it is real or complex.

Since $m_{t} \neq m_{b}$, a second, independent doublet coupling is needed; a complex bidoublet carries two electroweak doublets and so supplies one.

## lay
Assuming the slots of the composite's basic spinor states behave like the pairs (Hypothesis (S)), the field that gives quarks their masses in this construction points along the rung directions. Read as the Standard Model reads it, with the up-type quarks taking their masses from the mirror image of the field, a single such field gives the up-type and down-type quarks equal masses at the simplest level, whether the field is real or complex. The top and bottom quarks have very different masses, so a second, independent coupling is needed; a complex field of this kind, which carries two Higgs-like doublets rather than one, can supply it.

## one-liner
Under (S), one rung vector, real or complex, gives $m_{u} = m_{d}$ at tree level once the up-type masses are read through its conjugate, so $m_{t} \neq m_{b}$ needs a second doublet coupling, which a complex bidoublet, carrying two electroweak doublets, supplies.
