---
id: standard-model.one-vev-vector-relations-breaking-pattern
kind: claim
version: 7
title: 'One vev vector under (S): tree relations, breaking pattern and splitting'
status: proved
region: standard-model
subject: standard-model
tags: [symmetry-breaking, flavour-and-mixing]
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
  - standard-model.ten-transported-ambient-space-doublets-are@2
  - standard-model.yukawa-pattern-two-rung-module@6
  - standard-model.hyp-s-slot-statistics@9
  - standard-model.imported-tower-commuting-copies-fock-module@6
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_mass_form_magnitudes
- kind: check
  ref: check.py::check_conjugate_reading_gives_four_equal_masses
- kind: check
  ref: check.py::check_rung_terms_select_isospin_components
- kind: check
  ref: check.py::check_breaking_to_one_u1
locators:
  paper: T12
  number: Cor 9.25
  label: cor:vev
  line: 1744
extraction:
  maintainer_pass_weak_scale:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 7 (Leon''s decision of 2026-11-01 on the Yukawa form): a marked note says that the c* reading stands for the su(2)_R-covariant completion (Y on c and Ytilde on c* as wholes; synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix) and that the per-sector reading stated here is its leading mass reading, not su(2)_R covariant. What the corollary asserts is unchanged.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: M_c entries |a| and |b| on the four species pairs at complex samples, the conjugate reading with four equal masses, the T_3 selection, and the one-dimensional stabiliser T_3 - Y. Version 4 -> 5. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 5 -> 6.'
  env: corollary
  context_refs:
  - neutrino.imported-ceiling-under-hypothesis-u-arrow
  - standard-model.imported-spinor-bilinears
  typing:
    by: ai-typing-pass
    note: 'Context references to the spinor-bilinears fact and the neutrino ceiling are comparisons, not
      premises, and were not added; the standard Spin(10) 10_H route covers only the tree mass relations,
      not the breaking pattern or the splitting reading, so no standard-route derivation was added. Hypothesis
      pass: assumes standard-model.hyp-s-slot-statistics added because its statement holds under Hypothesis
      (S). Levels pass: the lay now names Hypothesis (S) and keeps the tree-level qualifier on the mass
      relations.'
    added:
    - standard-model.hyp-s-slot-statistics
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.hyp-s-slot-statistics
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Version 4 (Leon''s decision 10 of 2026-10-23): the up-type masses, and with them the neutrino Dirac mass, are read through the conjugate c* = conj(b) v_4 + conj(a) w_4 of the tower''s conjugation, as the Standard Model uses the conjugate doublet, because the reading through c gives on the null-lift locus the product law m_u m_d = Lambda/3, which the top and bottom masses rule out (synthesis.rung-field-on-the-lift-locus (5)); m_u = |a| is restated as the coupling to c*, m_u = |a(c*)| = |b|, so one coupling gives all four tree Dirac masses equal and the up/down hierarchy needs a second coupling or another source. The mass-form computation itself is unchanged; the imported tower Fact is added to uses for the conjugation (v_j* = w_j). Version 3 note follows. Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
Under Hypothesis (S), let $c = a\,v_{4} + b\,w_{4}$ be a fixed vector of the rung plane and $M_{c}(\psi, \varphi) = B(\psi, c\varphi)$ the resulting mass form on the sixteen. Then the nonzero entries of $M_{c}$ have magnitude $|a|$ on $(L, \nu^{c})$ and $(Q, u^{c})$ and $|b|$ on $(L, e^{c})$ and $(Q, d^{c})$. The up-type masses, and with them the neutrino's Dirac mass, are read through the conjugate $c^{*} = \bar{b}\,v_{4} + \bar{a}\,w_{4}$ of the tower's conjugation ($v_{j}^{*} = w_{j}$, Fact \claimref{standard-model.imported-tower-commuting-copies-fock-module}), as the Standard Model gives up-type masses through the conjugate doublet: they are the entries of $M_{c^{*}}$ on $(Q, u^{c})$ and $(L, \nu^{c})$, the coupling to $c^{*}$, of magnitude $|a(c^{*})| = |b|$ with $a(c^{*})$ the $v_{4}$ coefficient of $c^{*}$, while the down-type and charged-lepton masses are the entries of $M_{c}$. So at tree level $m_{\nu} = m_{u} = |b|$ and $m_{e} = m_{d} = |b|$: one coupling gives all four Dirac masses equal, the relations of a single real $10$ of $\mathrm{Spin}(10)$ (Fact \claimref{standard-model.imported-spinor-bilinears}), and the neutrino's Dirac mass is the up-type mass, as the neutrino paper's top-like valuation takes it (Fact \claimref{neutrino.imported-ceiling-under-hypothesis-u-arrow}). Read through $c$ itself the up-type entry would be $|a|$, with $m_{u}/m_{d} = |a|/|b|$ set by the direction of $c$; on the null-lift locus that reading gives the product law $m_{u}m_{d} = \Lambda/3$, which the observed top and bottom masses rule out (Theorem \claimref{synthesis.rung-field-on-the-lift-locus}(5)), and it is not the series' reading. Under the reading through $c^{*}$ the direction of $c$ no longer separates up-type from down-type masses: the observed up-down hierarchy needs a second coupling or another source. The $v_{4}$ term couples only the $T_{3} = -\tfrac12$ components of $L$ and $Q$ and the $w_{4}$ term only the $T_{3} = +\tfrac12$ components: a vector along one rung breaks the slot $SU(2) \times U(1)_{Y}$ to the $U(1)$ that fixes it, the electroweak pattern. And doublet-triplet splitting, the requirement that the triplet partner of the doublet not acquire a vev and not stay light, is the requirement that the vector lie in the rung directions and not in the ground ones: the split is between what transport adjoined and what the ground completion already had.

\emph{Note (the covariant completion, 2026-11-01).} The reading through $c^{*}$ stands for the $\su(2)_{R}$-covariant completion of the coupling: one family matrix $Y$ on $c$ and one $\tilde{Y}$ on $c^{*}$, each on the whole vector, so that $M_{d} = bY + \bar{a}\tilde{Y}$ and $M_{u} = aY + \bar{b}\tilde{Y}$ (\claimref{synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix}, with the second family matrix $\tilde{Y}$ independent of $Y$). The per-sector reading stated above (down-type entries from $c$, up-type entries from $c^{*}$, one coupling) is its leading mass reading, equal to it up to relative corrections $e^{-2\eta}$ on the lift family; it is not $\su(2)_{R}$ covariant, since it vanishes on the $a$ half of $c$, which the right-handed $\su(2)$ carries into the $b$ half. The tree relations stated above are those of the leading reading with $\tilde{Y} = Y$.

## technical
Under Hypothesis (S), a fixed rung-plane vector $c = a\,v_{4} + b\,w_{4}$ gives the mass form $M_{c}(\psi, \varphi) = B(\psi, c\varphi)$ on the sixteen, with entries of magnitude $|a|$ on $(L, \nu^{c})$ and $(Q, u^{c})$ and $|b|$ on $(L, e^{c})$ and $(Q, d^{c})$. The series reads the up-type masses, and the neutrino's Dirac mass with them, through the conjugate vector $c^{*} = \bar{b}\,v_{4} + \bar{a}\,w_{4}$, as the Standard Model uses the conjugate Higgs doublet for up-type quarks. Then the up-type entry is $|b|$, like the down-type one, and at tree level one coupling gives $m_{\nu} = m_{u} = m_{e} = m_{d} = |b|$, the relations of a single real $10$ of $\mathrm{Spin}(10)$. Read through $c$ itself, the up-type entry would be $|a|$; on the null-lift locus that reading makes the up-type and down-type masses multiply to the cosmological scale, which the top and bottom masses rule out. So the up-down hierarchy needs a second coupling or another source.

The $v_{4}$ term couples only the $T_{3} = -\tfrac12$ components of $L$ and $Q$ and the $w_{4}$ term only the $T_{3} = +\tfrac12$ components, so a vector along one rung breaks the slot $SU(2) \times U(1)_{Y}$ to the $U(1)$ fixing it, the electroweak pattern. Doublet-triplet splitting becomes the requirement that the vector lie in the rung directions rather than the ground ones.

## lay
Assuming the slots behave like the pairs (Hypothesis (S)), a single fixed direction in the space added by the transport construction plays the role of the Higgs field's background value. As in the Standard Model, the up-type quarks get their masses from the mirror image of that field. Read that way, at the simplest level a single coupling gives the up quark, the down quark, the electron and the neutrino one common mass, the pattern of the simplest Higgs field of the $\mathrm{Spin}(10)$ grand unified theory, so the large difference between up-type and down-type masses must come from a further coupling or another source. The field breaks the electroweak symmetry in the observed way. And the requirement that the Higgs field's coloured partner neither acquire a background value nor stay light becomes the requirement that the direction lie among the added directions rather than the original ones.

## one-liner
Under Hypothesis (S), one rung-plane vector $c$, with up-type masses read through its conjugate $c^{*}$, gives the tree relations $m_{\nu} = m_{u} = m_{e} = m_{d}$ of a single real $10$ (so the up-down hierarchy needs a second coupling), the electroweak breaking pattern, and doublet-triplet splitting as rung versus ground directions.
