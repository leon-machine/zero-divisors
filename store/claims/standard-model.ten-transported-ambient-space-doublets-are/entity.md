---
id: standard-model.ten-transported-ambient-space-doublets-are
kind: claim
version: 2
title: The ten is the transported ambient space, and its doublets are the rungs
status: proved
region: standard-model
subject: standard-model
tags: [representation-theory, symmetry-breaking, ladder-pairs]
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
  - standard-model.imported-fock-model-twistor-space@5
  - standard-model.imported-tower-commuting-copies-fock-module@6
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_weights_by_commutators
- kind: check
  ref: check.py::check_four_multiplets
- kind: check
  ref: check.py::check_one_mode_states_form_the_five
- kind: check
  ref: check.py::check_ten_is_the_complexified_ambient_space
locators:
  paper: T12
  number: Prop 9.22
  label: prop:ten
  line: 1706
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: hypercharge, 2T_3 and su(3) weights by commutators on the module, the four invariant multiplets, the one-mode states, and the ten as the complexified ambient space in GA. Version 1 -> 2.'
  env: proposition
  context_refs:
  - standard-model.imported-spinor-bilinears
  typing:
    by: ai-typing-pass
    note: 'Both edges kept as the source of the identification with the ambient space; the spinor-bilinear
      Fact is a comparison only, and no standard-route was added because the standard decomposition of
      the 10 does not give the identification with the transported ambient space. Levels pass: conditions
      already kept.'
---

## formal
Under $S(U(2) \times U(3))$ acting on the module, the ten decomposes as
\[
R_{2} \oplus \overline{R}_{2} \oplus W \oplus \overline{W} \;=\; (2,1)_{1/2} \oplus (2,1)_{-1/2} \oplus (1,3)_{-1/3} \oplus (1,\bar{3})_{1/3}:
\]
the rung creation vectors $v_{4}, v_{5}$ are a weak doublet of hypercharge $+\tfrac12$ with $2T_{3} = +1, -1$, the rung annihilation vectors $w_{4}, w_{5}$ the conjugate doublet of hypercharge $-\tfrac12$, and the pair vectors are colour triplets and antitriplets of hypercharge $\mp\tfrac13$, weak singlets. This is the $10$ of $\mathrm{Spin}(10)$ restricted as in Fact \claimref{standard-model.imported-spinor-bilinears}, realised as the transported ambient space itself: the Higgs doublet's representation is carried by the directions transport adjoined, and the colour-triplet partner's by the null directions the ground completion already had.

## technical
Under $S(U(2) \times U(3))$ acting on the module, the ten vectors of the transported ambient space decompose as $R_{2} \oplus \overline{R}_{2} \oplus W \oplus \overline{W} = (2,1)_{1/2} \oplus (2,1)_{-1/2} \oplus (1,3)_{-1/3} \oplus (1,\bar{3})_{1/3}$. The rung creation vectors $v_{4}, v_{5}$ are a weak doublet of hypercharge $+\tfrac12$, the rung annihilation vectors $w_{4}, w_{5}$ the conjugate doublet, and the pair vectors colour triplets and antitriplets of hypercharge $\mp\tfrac13$, weak singlets.

This is the $10$ of $\mathrm{Spin}(10)$, realised as the transported ambient space itself: the Higgs doublet's representation is carried by the two hyperbolic planes that transport adjoined, and the colour-triplet partner's by the null directions the ground completion already had.

## lay
Transport adds new directions to the space the framework works in. This result shows that, under the weak, colour and hypercharge symmetries, the two added pairs of directions have exactly the quantum numbers of the Higgs doublet, while the original directions carry those of a coloured partner. So the Higgs doublet's quantum numbers are those of directions the framework already builds, rather than being put in by hand.

## one-liner
The ten vectors of the transported ambient space decompose as $(2,1)_{1/2} \oplus (2,1)_{-1/2} \oplus (1,3)_{-1/3} \oplus (1,\bar{3})_{1/3}$, the rung directions carrying the Higgs doublet's representation.
