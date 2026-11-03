---
id: standard-model.invariant-operators-module
kind: claim
version: 7
title: The invariant operators on the module
status: proved
region: standard-model
subject: standard-model
tags:
- spinor-modules
- representation-theory
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
  - standard-model.imported-tower-commuting-copies-fock-module@5
  - standard-model.under-s-composites-state-space-spinor@6
  - standard-model.hyp-s-slot-statistics@9
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_commutant_dimensions
- kind: check
  ref: check.py::check_sectors_and_the_chirality_changing_operator
- kind: check
  ref: check.py::check_one_mass_per_species
locators:
  paper: T12
  number: Prop 9.16
  label: prop:commutant
  line: 1643
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the commutant dimensions 14 and 6 by exact elimination, the sector characters, the chirality-changing invariant, and one free number per species. Version 4 -> 5. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 5 -> 6. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 6 -> 7.'
  env: proposition
  typing:
    by: ai-typing-pass
    removed:
    - standard-model.imported-grip-area-casimir-form
    note: 'Removed the grip-area Casimir fact: the proof cites it only as the end of a range of facts
      that impose no constraint, and the commutant computation does not use it; kept the Fock-module fact
      and the Spin(10) spinor proposition. Hypothesis pass: assumes standard-model.hyp-s-slot-statistics
      added because its statement holds under Hypothesis (S) (for the species reading). Levels pass: lay
      now names Hypothesis (S).'
    added:
    - standard-model.hyp-s-slot-statistics
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.hyp-s-slot-statistics
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
about:
- obj.standard-model.two-rung-module-sectors-slot-components
---

## formal
The commutant of $\mathfrak{s}(\uu(2) \oplus \uu(3))$ acting on the two-rung module is fourteen-dimensional: the twelve sectors $(j,k)$ are pairwise inequivalent as representations except the two singlets $(1,1)_{0}$ at $(0,0)$, the vacuum, and $(2,3)$, the filled state, so an invariant operator is one scalar on each of the ten other sectors and an arbitrary $2 \times 2$ block on the span of the vacuum and the filled state. Those two states lie in opposite chirality halves, so the one off-diagonal invariant operator is chirality-changing. Restricted to the sixteen-dimensional even half alone the commutant is six-dimensional; under Hypothesis (S) that half is the generation, and an invariant mass operator on it is exactly one number per species, $(m_{\nu^{c}}, m_{u^{c}}, m_{Q}, m_{L}, m_{e^{c}}, m_{d^{c}})$, and the framework imposes no relation among the six.

## technical
Under $\mathfrak{s}(\uu(2) \oplus \uu(3))$ acting on the two-rung module, the twelve sectors $(j,k)$ are pairwise inequivalent except the vacuum $(0,0)$ and the filled state $(2,3)$, both singlets $(1,1)_{0}$. The commutant is therefore fourteen-dimensional, $14 = 10 \cdot 1^{2} + 1 \cdot 2^{2}$: one scalar on each of the ten other sectors and a $2 \times 2$ block on the vacuum and the filled state, whose off-diagonal part changes chirality because the two lie in opposite chirality halves.

On the sixteen-dimensional even half the commutant is six-dimensional. Under Hypothesis (S) that half is the generation, and an invariant mass operator on it is exactly one free number per species, $(m_{\nu^{c}}, m_{u^{c}}, m_{Q}, m_{L}, m_{e^{c}}, m_{d^{c}})$, with no relation imposed among them.

## lay
The paper asks which operators on the composite's state space respect its full gauge symmetry. Almost every block of states is distinguishable from every other, so such an operator can only multiply each block by its own number, with one exception where two blocks look alike and can be mixed. Restricted to one generation of matter, under the paper's hypothesis about the state space (Hypothesis (S)), this leaves six independent numbers, one per species, and the framework places no relation among them.

## one-liner
The commutant of $\mathfrak{s}(\uu(2) \oplus \uu(3))$ on the two-rung module is fourteen-dimensional, and on the even half, the generation under Hypothesis (S), it is one free number per species.
