---
id: standard-model.matching-traces
kind: claim
version: 4
title: The matching, from traces
status: proved
region: standard-model
subject: standard-model
tags: [running-and-unification]
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
  - standard-model.imported-one-loop-running-trace-ratio@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_traces_on_sixteen
- kind: check
  ref: check.py::check_matching_relations
locators:
  paper: T12
  number: Lem 10.5
  label: lem:matching
  line: 1923
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the four traces on the sixteen and the matching weights 3/5 and 2/5. Version 1 -> 2. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 2 -> 3. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 3 -> 4.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: The one-loop running fact supplies the normalisation and is kept; the paper gives no standard-route
      sentence for this textbook-like matching, so none was added.
---

## formal
On the sixteen,
\[
\tr T_{3L}^{2} \;=\; \tr T_{3R}^{2} \;=\; 2, \qquad \tr\,(B - L)^{2} \;=\; \tfrac{16}{3}, \qquad \tr Y^{2} \;=\; \tfrac{10}{3}.
\]
Consequently, at a scale where $\su(2)_{R} \oplus \su(4)$ breaks to $\su(3) \oplus \uu(1)_{Y}$, the inverse couplings in the normalisation of Fact \claimref{standard-model.imported-one-loop-running-trace-ratio}(a) match as
\[
a_{1} \;=\; \tfrac35\, a_{2R} + \tfrac25\, a_{4}, \qquad a_{2} \;=\; a_{2L}, \qquad a_{3} \;=\; a_{4}.
\]

## technical
On the sixteen, $\tr T_{3L}^{2} = \tr T_{3R}^{2} = 2$, $\tr (B - L)^{2} = \tfrac{16}{3}$ and $\tr Y^{2} = \tfrac{10}{3}$. In the trace normalisation of the one-loop running fact, the $\su(4)$ generator along $B - L$ is $T_{BL} = \sqrt{3/8}\,(B - L)$ and $Y = T_{3R} + \sqrt{2/3}\,T_{BL}$.

Hence, where $\su(2)_{R} \oplus \su(4)$ breaks to $\su(3) \oplus \uu(1)_{Y}$, the inverse couplings match as $a_{1} = \tfrac35 a_{2R} + \tfrac25 a_{4}$, $a_{2} = a_{2L}$ and $a_{3} = a_{4}$; the weights are the trace ratios $\tr T_{3R}^{2}/\tr Y^{2} = \tfrac35$ and $\tfrac14\tr(B - L)^{2}/\tr Y^{2} = \tfrac25$.

## lay
When the larger Pati-Salam symmetry breaks to the Standard Model at some energy, the strengths of the forces on either side must be joined up correctly. The paper reads the joining rule off simple traces of the charges over one generation. The hypercharge force takes three fifths of its inverse strength from the right-handed weak force and two fifths from the four-colour force, while the left-handed weak force and colour carry straight through.

## one-liner
Traces over the sixteen give the Pati-Salam matching $a_{1} = \tfrac35 a_{2R} + \tfrac25 a_{4}$, $a_{2} = a_{2L}$, $a_{3} = a_{4}$.
