---
id: standard-model.what-direction-made
kind: claim
version: 6
title: What the $126$ direction is made of
status: proved
region: standard-model
subject: generations
tags: [flavour-and-mixing, representation-theory]
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
  - standard-model.under-s-composites-state-space-spinor@6
  - families.doublet-direction-module-georgi-jarlskog-clebsch@6
  - standard-model.hyp-s-slot-statistics@10
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_pair_number_table
- kind: check
  ref: check.py::check_four_operators_forms
- kind: proof
  derivation: main
locators:
  paper: T12
  number: Cor 9.36
  label: cor:onetwentysix
  line: 1855
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: N_W table on the species; the forms of w4, w4 N_W, w4 chi, w4 N_W chi and T_GJ = w4 chi - 2/3 w4 N_W chi. Version 4 -> 5. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 5 -> 6.'
  env: corollary
  typing:
    by: ai-typing-pass
    added:
    - families.doublet-direction-module-georgi-jarlskog-clebsch
    - standard-model.hyp-s-slot-statistics
    note: 'Added the families Proposition for the closed form of T_GJ used in the statement; the closing
      clause that the pair number lies outside the mass mechanism leans on the two no-go theorems, which
      the proof does not cite, so they were not added. Hypothesis pass: assumes standard-model.hyp-s-slot-statistics
      added because its statement holds under Hypothesis (S). Levels pass: the lay stated the 126 direction
      as a plain fact, dropping Hypothesis (S) (review item 2); it now names (S).'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.hyp-s-slot-statistics
    stated_role:
    - families.doublet-direction-module-georgi-jarlskog-clebsch
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
Under Hypothesis (S), on the sixteen, the pair number $N_{W}$ takes the values $1$ and $3$ on the two rung-odd species $Q$ and $L$ and the values $0$ and $2$ on the rung-even ones, so $B - L$ takes four values where the rung algebra distinguishes only two parities. Among the operators $w_{4}$, $w_{4}N_{W}$, $w_{4}\chi$ and $w_{4}N_{W}\chi$, the first two have the $10$ form ($w_{4}N_{W}$'s symmetric form is $\tfrac32$ times $w_{4}$'s), the third has vanishing symmetric form, and only the fourth has the $126$ form, $|y_{e}| = \tfrac32$, $|y_{d}| = \tfrac12$, with $f(T_{\mathrm{GJ}}) = -\tfrac23 f(w_{4}N_{W}\chi)$ exactly, since $T_{\mathrm{GJ}} = w_{4}\chi - \tfrac23 w_{4}N_{W}\chi$ and the first term's form vanishes. The $126$ direction is the pair number read through the rung parity; neither factor alone reaches it, and the pair number is outside every object of the mass mechanism derived in the series.

## technical
Under Hypothesis (S), the pair number $N_{W}$ takes the values $1$ and $3$ on the rung-odd species $Q$ and $L$ and $0$ and $2$ on the rung-even ones, so $B - L$ takes four values where the rung algebra sees only two parities. Of $w_{4}$, $w_{4}N_{W}$, $w_{4}\chi$ and $w_{4}N_{W}\chi$, the first two give the $10$ form, the third has vanishing symmetric form, and only the fourth gives the $126$ form, with $|y_{e}| = \tfrac32$ and $|y_{d}| = \tfrac12$.

Since $T_{\mathrm{GJ}} = w_{4}\chi - \tfrac23 w_{4}N_{W}\chi$ and the first term's form vanishes, $f(T_{\mathrm{GJ}}) = -\tfrac23 f(w_{4}N_{W}\chi)$ exactly: the $126$ direction is the pair number read through the rung parity, neither factor alone reaches it, and the pair number lies outside every object of the mass mechanism derived in the series.

## lay
Assuming the slots behave like the pairs (Hypothesis (S)), the special direction that produces the factor of three between lepton and quark masses is taken apart here. It turns out to be the count of pairs inside a particle, read through a simple even-or-odd label on the particle's rung. Neither the count nor the label alone does the job, and nothing in the mass mechanism built so far contains the pair count.

## one-liner
Under Hypothesis (S), the $126$ doublet direction is $w_{4}N_{W}\chi$ up to a term with vanishing form: the pair number read through the rung parity, which neither factor reaches alone.
