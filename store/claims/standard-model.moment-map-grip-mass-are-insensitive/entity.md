---
id: standard-model.moment-map-grip-mass-are-insensitive
kind: claim
version: 4
title: The moment map, the grip and the mass are insensitive to the slots
status: proved
region: standard-model
subject: mass
tags: [spinor-modules, frozen-point, mass-generation]
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
about:
- obj.mass.grip-mass-composite
- obj.standard-model.two-rung-module-sectors-slot-components
derivations:
- name: main
  uses:
  - standard-model.module-factorises-even-ground-elements-act@5
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_sector_additivity_and_rung_mixing_invariance
- kind: check
  ref: check.py::check_sum_over_slot_components
- kind: check
  ref: check.py::check_grip_depends_on_the_multiset
- kind: proof
  derivation: main
locators:
  paper: T12
  number: Thm 9.10
  label: thm:blind
  line: 1582
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: moment and grip additive over rung sectors and slot components, invariant under unitary rung mixing, and dependent only on the multiset of components, in the Fock form of the five-mode module. Version 1 -> 2. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 2 -> 3. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 3 -> 4.'
  env: theorem
  context_refs:
  - standard-model.imported-grip-area-casimir-form
  typing:
    by: ai-typing-pass
    added:
    - obj.mass.grip-mass-composite
    - obj.standard-model.two-rung-module-sectors-slot-components
    note: 'Kept the module-factorisation edge; the grip Fact in context_refs is used only for the grip''s
      definition, so it went in as the about edge to the grip object (with the module definition) rather
      than as a uses edge carrying the Casimir premises. Levels pass: lay now keeps the product-form hypothesis.'
---

## formal
Let $I \in V$ be any ambient vector of the ground completion, in particular the frozen point at any $\Lambda$, and let the module carry a product form. Then for every state $\Psi$ of the two-rung module:
\begin{enumerate}
\item[(i)] the moment $M_{U \wedge I}(\Psi)$, the grip $P(\Psi)$ and $m^{2}(\Psi)$ are invariant under the rung mixing $U(2)$ and are computed sector by sector: writing $\Psi = \Psi_{0} + \Psi_{1} + \Psi_{2}$ by rung number, $M_{U \wedge I}(\Psi) = \sum_{j} M_{U \wedge I}(\Psi_{j})$ and $P(\Psi) = \sum_{j} P(\Psi_{j})$, with no cross-sector terms;
\item[(ii)] within a sector, the moment is the sum over slot components: for $\Psi_{j} = \sum_{a} e_{a} \otimes \psi_{a}$, $M_{U \wedge I}(\Psi_{j}) = \sum_{a} \ip{\psi_{a}}{A_{W}(U \wedge I)\psi_{a}}_{W}$ and $P(\Psi_{j}) = \sum_{a} P_{W}(\psi_{a})$, where $A_{W}$ and $P_{W}$ are the generator and the grip of Fact \claimref{standard-model.imported-grip-area-casimir-form} on $\Lambda^{\bullet}W$;
\item[(iii)] the grip of a state depends on its slot components only through the multiset $\{\psi_{a}\}$: the same components placed at any slot states, or in any slot sector of the same size, give the same grip and the same mass.
\end{enumerate}

## technical
Let $I \in V$ be any ambient vector of the ground completion, such as the frozen point at any $\Lambda$, and give the two-rung module a product form. Every generator $A(U \wedge I)$ acts on the pair factor only, so the moment, the grip and the mass of a state are invariant under the rung mixing $U(2)$ and split by rung number with no cross-sector terms: $P(\Psi) = \sum_{j} P(\Psi_{j})$.

Within a sector, $\Psi_{j} = \sum_{a} e_{a} \otimes \psi_{a}$ gives $M_{U \wedge I}(\Psi_{j}) = \sum_{a} \ip{\psi_{a}}{A_{W}(U \wedge I)\psi_{a}}_{W}$ and $P(\Psi_{j}) = \sum_{a} P_{W}(\psi_{a})$. The grip therefore depends on the slot components only through the multiset $\{\psi_{a}\}$: the same components at other slot states, or in another slot sector of the same size, give the same grip and the same mass.

## lay
The state space here has two kinds of internal label, slots and pairs. This result shows that, once the module is given a product form, the series' mass mechanism, measured against any ground reference vector, cannot tell the slots apart. It simply adds up the contributions of the pieces of a state, whatever slot each sits in, so only the pieces themselves and how many there are matter.

## one-liner
For any ground ambient vector $I$ and any product form, the moment, grip and mass on the two-rung module are $U(2)$-invariant and are sums over rung sectors and slot components.
