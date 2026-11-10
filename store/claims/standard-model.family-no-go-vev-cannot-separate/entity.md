---
id: standard-model.family-no-go-vev-cannot-separate
kind: claim
version: 6
title: 'Family no-go: a vev in the $10$ cannot separate the charged leptons from the down quarks'
status: proved
region: standard-model
subject: generations
tags: [no-go, flavour-and-mixing]
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
  - standard-model.yukawa-pattern-two-rung-module@6
  - standard-model.hyp-s-slot-statistics@10
  proof: proof-main.tex
- name: standard-route
  uses:
  - standard-model.imported-spinor-bilinears@1
  - standard-model.imported-clebsch-structure-seesaw@1
  proof: proof-standard-route.tex
checked_by:
- kind: check
  ref: check.py::check_one_family_clebsches_equal
- kind: check
  ref: check.py::check_family_factor_keeps_spectra
- kind: proof
  derivation: main
locators:
  paper: T12
  number: Thm 9.31
  label: thm:familynogo
  line: 1806
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: every rung vector gives |y_e| = |y_d| and |y_nu| = |y_u|; y_e F and y_d F have equal spectra in magnitude for a generic F, the 126 entries do not. Version 3 -> 4. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 4 -> 5. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 5 -> 6.'
  env: theorem
  typing:
    by: ai-typing-pass
    added:
    - standard-model.imported-spinor-bilinears
    - standard-model.imported-clebsch-structure-seesaw
    - standard-model.hyp-s-slot-statistics
    note: 'Added a standard-route through the imported spinor bilinears and Clebsch structure, since the
      paper says the single-10 tree relations are standard; the doubt is that the quoted sentence names
      the relations of Corollary cor:vev rather than this theorem directly. Hypothesis pass: assumes standard-model.hyp-s-slot-statistics
      added because its statement holds under Hypothesis (S). Levels pass: the lay level now states Hypothesis
      (S), which it had dropped.'
  source_title: 'Family no-go: a vev in the $10$ cannot separate the charged leptons from the down quarks'
  source_formal: |-
    Under Hypothesis (S), let the electroweak vev be a vector $x$ of the ten (a rung vector, $Y = \mp\tfrac12$), and let the three families be carried by a tensor factor $\C^{3}$ on which the family structure acts by an arbitrary matrix $F$, so that the mass matrices are $M_{e} = y_{e}\,F$ and $M_{d} = y_{d}\,F$ with $y_{e} = Y_{x}(L, e^{c})$, $y_{d} = Y_{x}(Q, d^{c})$ the one-family Clebsches. Then $|y_{e}| = |y_{d}|$, so $M_{e}$ and $M_{d}$ have identical characteristic polynomials up to sign, hence identical spectra in magnitude, for every $F$: no operation in family space, the breaking $S_{3} \to S_{2} \to 1$ included, produces $m_{\mu} \neq m_{s}$ or $m_{e} \neq m_{d}$ at tree level. The same holds for $M_{\nu}^{D}$ against $M_{u}$.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Only the lay level named twistor slots, now spinor slots; the formal level and both proofs had no twistor language, and the family factor C^3 is a multiplicity space, kept as written.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.hyp-s-slot-statistics
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
Under Hypothesis (S), let the electroweak vev be a vector $x$ of the ten (a rung vector, $Y = \mp\tfrac12$), and let the three families be carried by a tensor factor $\C^{3}$ on which the family structure acts by an arbitrary matrix $F$, so that the mass matrices are $M_{e} = y_{e}\,F$ and $M_{d} = y_{d}\,F$ with $y_{e} = Y_{x}(L, e^{c})$, $y_{d} = Y_{x}(Q, d^{c})$ the one-family Clebsches. Then $|y_{e}| = |y_{d}|$, so $M_{e}$ and $M_{d}$ have identical characteristic polynomials up to sign, hence identical spectra in magnitude, for every $F$: no operation in family space, the breaking $S_{3} \to S_{2} \to 1$ included, produces $m_{\mu} \neq m_{s}$ or $m_{e} \neq m_{d}$ at tree level. The same holds for $M_{\nu}^{D}$ against $M_{u}$.

## technical
Under Hypothesis (S), let the electroweak vev be a rung vector $x$ of the ten and let the families sit in a tensor factor $\C^{3}$ acted on by an arbitrary matrix $F$, so that $M_{e} = y_{e}F$ and $M_{d} = y_{d}F$ with $y_{e}$, $y_{d}$ the one-family Clebsches of $x$. The Yukawa pattern gives $|y_{e}| = |y_{d}|$, so $M_{e}$ and $M_{d}$ differ by a scalar of modulus one and have the same spectra in magnitude for every $F$.

Hence no structure in family space, the breaking $S_{3} \to S_{2} \to 1$ included, can give $m_{\mu} \neq m_{s}$ or $m_{e} \neq m_{d}$ at tree level; in the same way the Dirac neutrino matrix cannot be separated from $M_{u}$.

## lay
In the simplest unified picture, one Higgs field gives electrons and down quarks the same mass, and neutrinos and up quarks the same mass. Assuming the spinor slots behave like the pairs (Hypothesis (S)), this theorem shows that, if the Higgs is a single vector of the framework's ten-dimensional space, no arrangement of the three families can undo that equality at the simplest level of the calculation. Since real muons and strange quarks differ in mass, something beyond a single such vector is needed.

## one-liner
Under Hypothesis (S), a vev in the $10$ gives the charged leptons and down quarks, and the Dirac neutrinos and up quarks, identical mass spectra in magnitude at tree level, whatever the family structure.
