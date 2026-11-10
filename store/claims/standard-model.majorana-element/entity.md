---
id: standard-model.majorana-element
kind: claim
version: 7
title: The Majorana element is the $(10,1,3)$
status: proved
region: standard-model
subject: standard-model
tags: [seesaw-and-majorana, representation-theory, symmetry-breaking]
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
  - standard-model.automorphisms-preserve-slot-pair-split-are@7
  - standard-model.invariant-pairing-five-modes@5
  - standard-model.under-s-composites-state-space-spinor@6
  - standard-model.hyp-s-slot-statistics@10
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_t_pairs_nu_c_with_itself
- kind: check
  ref: check.py::check_stabiliser_is_standard_model
- kind: check
  ref: check.py::check_orbit_is_10_1_3
- kind: check
  ref: check.py::check_thirteenth_generator_broken
locators:
  paper: T12
  number: Prop 10.7
  label: prop:breaking
  line: 1950
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: T maps nu^c to the full state, its stabiliser in the compact 21 is su(3) + su(2)_L + u(1)_Y, its orbit is the (10,1,3), and [X, T] = 5T. Version 4 -> 5. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 5 -> 6. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 6 -> 7.'
  env: proposition
  context_refs:
  - standard-model.invariant-pairing-five-modes
  - standard-model.under-s-composites-state-space-spinor
  typing:
    by: ai-typing-pass
    added:
    - standard-model.invariant-pairing-five-modes
    - standard-model.under-s-composites-state-space-spinor
    - standard-model.hyp-s-slot-statistics
    note: 'Added the five-mode pairing lemma (the mass form in (1) is that pairing) and the Spin(10) spinor
      proposition (source of the thirteenth generator and X = 2Y - 5/2(B-L)), both named in context_refs.
      Hypothesis pass: assumes standard-model.hyp-s-slot-statistics added because its statement holds
      under Hypothesis (S). Levels pass: the lay now names Hypothesis (S) and says the stabiliser statement
      is within the Pati-Salam algebra.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.invariant-pairing-five-modes
    - standard-model.under-s-composites-state-space-spinor
    - standard-model.hyp-s-slot-statistics
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
Under Hypothesis (S), let $T = v_{1}v_{2}v_{3}v_{4}v_{5}$, the product of the five creation operators, a grade-five element of the Clifford algebra of the ten. Then:
\begin{enumerate}
\item[(1)] $T$ maps $\nu^{c}$, the empty state, to the full state and annihilates every other state, so the form $B(\psi, T\varphi)$ of Lemma \claimref{standard-model.invariant-pairing-five-modes} on the sixteen is the $\nu^{c}\nu^{c}$ entry alone: the right-handed neutrino's Majorana mass;
\item[(2)] $T$ commutes with $\su(3)$, $\su(2)_{L}$ and $Y$, and $[B - L, T] = -2T$; in the compact Pati-Salam algebra, the real span of the $21$, the subalgebra fixing $T$ is twelve-dimensional, exactly $\su(3) \oplus \su(2)_{L} \oplus \uu(1)_{Y}$;
\item[(3)] the orbit of $T$ under the $21$ spans thirty dimensions, on which $\su(2)_{L}$ acts trivially, and $T$ is the highest weight of an $\su(2)_{R}$ triplet: the orbit is the $(10,1,3)$.
\end{enumerate}
So a vev along $T$ breaks Pati-Salam to the Standard Model algebra and gives $\nu^{c}$ its Majorana mass at the same scale. It also breaks the thirteenth generator of Proposition \claimref{standard-model.under-s-composites-state-space-spinor}(3), which lies in $\su(2)_{R} \oplus \su(4)$ as $X = 2T_{3R} - \tfrac32(B - L)$.

## technical
Under Hypothesis (S), $T = v_{1}v_{2}v_{3}v_{4}v_{5}$ sends the empty state $\nu^{c}$ to the full state and annihilates every other state, so the mass form $B(\psi, T\varphi)$ on the sixteen has only the $\nu^{c}\nu^{c}$ entry: a Majorana mass for the right-handed neutrino. $T$ commutes with $\su(3)$, $\su(2)_{L}$ and $Y$, with $[B - L, T] = -2T$; inside the real span of the $21$ Pati-Salam generators its stabiliser is exactly the twelve-dimensional $\su(3) \oplus \su(2)_{L} \oplus \uu(1)_{Y}$, and its orbit spans the thirty-dimensional $(10,1,3)$.

So a vev along $T$ breaks Pati-Salam to the Standard Model algebra and gives $\nu^{c}$ its Majorana mass at the same scale. It also breaks the thirteenth generator, which lies in $\su(2)_{R} \oplus \su(4)$ as $X = 2T_{3R} - \tfrac32(B - L)$.

## lay
Assuming the slots behave like the pairs (Hypothesis (S)), a particular element built from all five creation operators turns the empty state, the right-handed neutrino, into the completely filled state and does nothing else. Used as a mass term it gives only the right-handed neutrino a mass, of the kind a neutral particle can have on its own. Among the Pati-Salam symmetries, those that leave the element unchanged are exactly those of the Standard Model, so a background value along it breaks the larger Pati-Salam symmetry to the Standard Model and gives that neutrino its mass at the same energy.

## one-liner
Under Hypothesis (S), the product of the five creation operators spans the $(10,1,3)$ under Pati-Salam, gives only $\nu^{c}$ a Majorana mass, and is fixed by exactly the Standard Model algebra.
