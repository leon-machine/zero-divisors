---
id: descent-lift.classical-shared-bit-reduced-view-pure
kind: claim
version: 4
title: The classical shared bit is the reduced view of a pure four-mode state
status: proved
region: descent-lift
subject: descent
tags: [descent-map, entanglement, measurement-and-records]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-descent-lift, the series'' standard disclaimer'
review: typed
about:
- obj.descent-lift.lift
derivations:
- name: main
  uses:
  - descent-lift.lift-costs-one-rung-per-mode@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_joint_state_and_marginals
- kind: check
  ref: check.py::check_schmidt_coefficients_move_to_pair_record_cut
locators:
  paper: T05-descent-lift
  number: Cor 5.1
  label: cor:stored
  line: 235
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the lifted (4/5, 3/5) state entry by entry, its pair, single-mode and record marginals (16/25, 9/25), and equal Schmidt data across the mode-mode and pair-record cuts. Version 2 -> 3. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 3 -> 4.'
  env: corollary
  typing:
    by: ai-typing-pass
    added:
    - descent-lift.lift-costs-one-rung-per-mode
    note: 'added the lift theorem: ''its lift'' is the explicit two-rung lift of that theorem, which the
      proof applies; the thermal-marginal comparison with the singularity paper''s sample point is an
      identification, not a premise. Levels pass: lay now says the result is for the sample state (4/5,
      3/5) under the two-rung lift, not for every pair.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - descent-lift.lift-costs-one-rung-per-mode
---

## formal
Let the pair be in the thermofield state $c\ket{00} + s\ket{11}$, $(c, s) = (\tfrac45, \tfrac35)$. Its lift is the pure, even four-mode state
\[
c\,\ket{00} \otimes (\ket{00} + \ket{11}) + s\,\ket{11} \otimes (\ket{00} - \ket{11}),
\]
up to normalisation. The pair's marginal is $\operatorname{diag}(\tfrac{16}{25}, \tfrac{9}{25})$ on $\{\ket{00}, \ket{11}\}$, exactly the descent of the pair, the classical shared bit; each single mode of the pair keeps the thermal marginal $\operatorname{diag}(\tfrac{16}{25}, \tfrac{9}{25})$ of the singularity paper's sample point; and the record's marginal has the same spectrum $(\tfrac{16}{25}, \tfrac{9}{25})$. The entanglement of the pair, with Schmidt coefficients $(c, s)$ across the mode-mode cut, has become entanglement with the same Schmidt coefficients across the pair-record cut.

## technical
Take the pair in the thermofield state $c\ket{00} + s\ket{11}$ at $(c, s) = (\tfrac45, \tfrac35)$. Applying the two-rung lift gives, up to normalisation, the pure even four-mode state $c\,\ket{00}\otimes(\ket{00} + \ket{11}) + s\,\ket{11}\otimes(\ket{00} - \ket{11})$.

Its marginal on the pair is $\operatorname{diag}(\tfrac{16}{25}, \tfrac{9}{25})$ on $\{\ket{00}, \ket{11}\}$, exactly the descent of the pair, the classical shared bit; each single mode keeps the thermal marginal $\operatorname{diag}(\tfrac{16}{25}, \tfrac{9}{25})$ of the singularity paper's sample point; and the record's marginal has the same spectrum. The pair's entanglement, with Schmidt coefficients $(c, s)$ across the mode-mode cut, reappears with the same Schmidt coefficients across the pair-record cut.

## lay
Take the series' sample entangled pair of modes, with amplitudes four fifths and three fifths. When the descent turns it into a classical shared bit, the lost coherence can be kept, using the two-rung lift, by a record made of two extra modes. The pair and record together are then in a single pure state, and the classical bit is simply what the pair looks like when the record is ignored. The entanglement that was between the two modes is now between the pair and the record, with the same strengths.

## one-liner
Under the two-rung lift the classical shared bit $\operatorname{diag}(\tfrac{16}{25}, \tfrac{9}{25})$ is the pair's marginal of a pure even four-mode state, the pair's entanglement having moved to the pair-record cut with the same Schmidt coefficients.
