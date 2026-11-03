---
id: standard-model.grip-mass-two-rung-module
kind: claim
version: 7
title: The grip mass in the two-rung module at $\Lambda = 0$
status: proved
region: standard-model
subject: mass
tags:
- spinor-modules
- frozen-point
- mass-generation
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
- obj.standard-model.two-rung-module-sectors-slot-components
- obj.mass.grip-mass-composite
derivations:
- name: main
  uses:
  - standard-model.imported-fock-model-twistor-space@5
  - standard-model.imported-grip-area-casimir-form@5
  - standard-model.module-factorises-even-ground-elements-act@5
  - standard-model.moment-map-grip-mass-are-insensitive@4
  - standard-model.under-s-composites-state-space-spinor@6
  - standard-model.hyp-s-slot-statistics@9
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_components_per_rung_sector_and_chirality
- kind: check
  ref: check.py::check_grip_mass_of_each_sector
- kind: check
  ref: check.py::check_sector_labels_under_s
locators:
  paper: T12
  number: Thm 9.11
  label: thm:mass
  line: 1595
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: binom(n,j) components and one pair parity per sector, sector masses 0, 2|<pi1 pi2>|^2 and 2 sum |<pi_a pi_b>|^2, and the singlet and doublet hypercharges. Version 5 -> 6. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 6 -> 7.'
  correction:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'W503: the one-liner now names Hypothesis (S), which the formal statement and the assumes edge carry for the species reading. Version 4 -> 5.'
  env: theorem
  typing:
    by: ai-typing-pass
    added:
    - obj.standard-model.two-rung-module-sectors-slot-components
    - standard-model.hyp-s-slot-statistics
    note: 'Kept all five edges, each cited in the proof as a premise; added the two-rung module definition
      as an about edge, since the sectors and slot components are defined there. Hypothesis pass: assumes
      standard-model.hyp-s-slot-statistics added because its statement holds under Hypothesis (S) (for
      the species reading). Levels pass: lay no longer says the doublets are the only species that can
      be massive, only that they are the only ones with nonzero grip mass.'
  source_title: The grip mass in the two-rung module at $\Lambda = 0$
  source_formal: 'At $\Lambda = 0$, with $I = n_{\infty}$, let $\Psi$ be a state of one chirality half
    of the two-rung module, so that every slot component $\psi_{a}$ lies in $\T$ or in $\T''$. Then:

    \begin{enumerate}

    \item[(i)] $P(\Psi) = \sum_{a} p_{a}$, a sum of $\sum_{j}\binom{2}{j}$ null, future-directed momenta,
    one per slot component, each the momentum of a single twistor or single dual twistor;

    \item[(ii)] a state in a slot-singlet sector, $j = 0$ or $j = 2$, has exactly one slot component and
    $m^{2}(\Psi) = 0$: the grip mass vanishes identically on the sectors $(0,0), (0,2), (2,0), (2,2)$,
    which under Hypothesis (S) are the species $\nu^{c}, u^{c}, e^{c}, d^{c}$ of the generation, and on
    their conjugates;

    \item[(iii)] a state in the slot-doublet sector has two slot components with spinor parts $\pi^{1},
    \pi^{2}$ and $m^{2}(\Psi) = 2|\br{\pi^{1}\pi^{2}}|^{2}$, the two-twistor area formula, vanishing exactly
    when the components'' spinor parts are proportional; these are the sectors $(1,1), (1,3)$, under Hypothesis
    (S) the species $Q$ and $L$ of the generation;

    \item[(iv)] for the $n$-rung module the same holds with $\binom{n}{j}$ components, and $m^{2} = 2\sum_{a
    < b}|\br{\pi^{a}\pi^{b}}|^{2}$ over the components of a state in rung sector $j$; in particular the
    slot-singlet sectors $j = 0$ and $j = n$ are massless at every $n$.

    \end{enumerate}'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: Twistor space and its dual \T, \T' are now the conformal spinor space and its dual \CS, \CSm{}
      in all levels and the proof, and single twistors are single conformal spinors; the sector counting
      is unchanged.
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
At $\Lambda = 0$, with $I = n_{\infty}$, let $\Psi$ be a state of one chirality half of the two-rung module, so that every slot component $\psi_{a}$ lies in $\CS$ or in $\CSm{}$, the conformal spinor space or its dual (twistor space or its dual). Then:
\begin{enumerate}
\item[(i)] $P(\Psi) = \sum_{a} p_{a}$, a sum of $\sum_{j}\binom{2}{j}$ null, future-directed momenta, one per slot component, each the momentum of a single conformal spinor or single dual conformal spinor;
\item[(ii)] a state in a slot-singlet sector, $j = 0$ or $j = 2$, has exactly one slot component and $m^{2}(\Psi) = 0$: the grip mass vanishes identically on the sectors $(0,0), (0,2), (2,0), (2,2)$, which under Hypothesis (S) are the species $\nu^{c}, u^{c}, e^{c}, d^{c}$ of the generation, and on their conjugates;
\item[(iii)] a state in the slot-doublet sector has two slot components with spinor parts $\pi^{1}, \pi^{2}$ and $m^{2}(\Psi) = 2|\br{\pi^{1}\pi^{2}}|^{2}$, the two-spinor area formula, vanishing exactly when the components' spinor parts are proportional; these are the sectors $(1,1), (1,3)$, under Hypothesis (S) the species $Q$ and $L$ of the generation;
\item[(iv)] for the $n$-rung module the same holds with $\binom{n}{j}$ components, and $m^{2} = 2\sum_{a < b}|\br{\pi^{a}\pi^{b}}|^{2}$ over the components of a state in rung sector $j$; in particular the slot-singlet sectors $j = 0$ and $j = n$ are massless at every $n$.
\end{enumerate}

## technical
At $\Lambda = 0$ the frozen point is $I = n_{\infty}$, and the grip of a state $\Psi$ of one chirality half of the two-rung module is its total momentum, $P(\Psi) = \sum_{a} p_{a}$: a sum of null, future-directed momenta, one for each slot component, each that of a single conformal spinor or single dual conformal spinor. A rung sector $j$ has $\binom{2}{j}$ slot components.

So the slot-singlet sectors $j = 0, 2$ have one component and are exactly massless, while the slot-doublet sector $j = 1$ has two components with spinor parts $\pi^{1}, \pi^{2}$ and $m^{2} = 2|\br{\pi^{1}\pi^{2}}|^{2}$, vanishing exactly when the spinor parts are proportional. Under Hypothesis (S) the massless sectors are $\nu^{c}, u^{c}, e^{c}, d^{c}$ and their conjugates, and the doublet sectors are $Q$ and $L$. With $n$ rungs, $m^{2} = 2\sum_{a<b}|\br{\pi^{a}\pi^{b}}|^{2}$, and the sectors $j = 0$ and $j = n$ are massless for every $n$.

## lay
In this framework a particle's mass comes from how its parts grip a fixed reference point. Here that grip is computed on a model state space built from two rungs, with no cosmological constant. States with a single part are always massless, while states with two parts get a mass measured by how misaligned the two parts are. Read as one generation of matter under Hypothesis (S), this makes the quark and lepton doublets the only species with a nonzero grip mass.

## one-liner
At $\Lambda = 0$ the grip mass vanishes identically on the slot-singlet sectors of the two-rung module and is the two-spinor area $2|\br{\pi^{1}\pi^{2}}|^{2}$ on the slot-doublet sector; under Hypothesis (S) the singlet sectors are $\nu^{c}, u^{c}, e^{c}, d^{c}$ and the doublet sectors $Q$ and $L$.
