---
id: standard-model.equal-weight-module
kind: claim
version: 5
title: Equal weight on the module
status: proved
region: standard-model
subject: generations
tags: [flavour-and-mixing, seesaw-and-majorana, representation-theory]
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
  - standard-model.invariant-pairing-five-modes@5
  - standard-model.majorana-element@7
  - families.doublet-direction-module-georgi-jarlskog-clebsch@6
  - standard-model.hyp-s-slot-statistics@9
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_projector_onto_nu_c_pair
- kind: check
  ref: check.py::check_equal_weight_forms
- kind: check
  ref: check.py::check_commutes_iff_equal_weight
- kind: proof
  derivation: main
locators:
  paper: T12
  number: Prop 11.3
  label: prop:equalweight
  line: 2049
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: P projects onto nu^c and its conjugate; v4 kept off the condensate has the form of 3/4 (v4 + T^u); commutation with P on the sixteen iff a = a'' iff nu^c is annihilated; w4 and T_GJ commute. Version 4 -> 5.'
  env: proposition
  context_refs:
  - families.doublet-direction-module-georgi-jarlskog-clebsch
  - standard-model.majorana-element
  typing:
    by: ai-typing-pass
    added:
    - standard-model.majorana-element
    - families.doublet-direction-module-georgi-jarlskog-clebsch
    - standard-model.hyp-s-slot-statistics
    note: 'Added the Majorana element, which defines the projector P, and the families Proposition, which
      supplies the up-type direction compared against; both are hypotheses of the statement. Hypothesis
      pass: assumes standard-model.hyp-s-slot-statistics added because its statement holds under Hypothesis
      (S). Levels pass: conditions already kept.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.hyp-s-slot-statistics
    stated_role:
    - families.doublet-direction-module-georgi-jarlskog-clebsch
    - standard-model.majorana-element
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
Under Hypothesis (S), let $P = T^{\dagger}T + TT^{\dagger}$, with $T$ the Majorana element of Proposition \claimref{standard-model.majorana-element}, so that $P$ projects onto $\nu^{c}$ and its conjugate; and let $T^{u}_{\mathrm{GJ}} = v_{4}(B - L)\chi$, the up-type twin of $T_{\mathrm{GJ}}$ \cite[Prop.~8.1(iv)]{ButlerT13}. On the sixteen:
\begin{enumerate}
\item[(1)] the vector $v_{4}$ kept off the condensate, $v_{4} - (v_{4}P + Pv_{4})$, has the mass form of $\tfrac34(v_{4} + T^{u}_{\mathrm{GJ}})$, the $10$ and the $126$ doublet at equal weight; it couples $(Q, u^{c})$ exactly as $v_{4}$ does and has no $(L, \nu^{c})$ entry; and $w_{4} - (w_{4}P + Pw_{4})$ has the mass form of $w_{4}$;
\item[(2)] $a\,v_{4} + a'\,T^{u}_{\mathrm{GJ}}$ commutes with $P$ if and only if $a' = a$, which is exactly when it annihilates $\nu^{c}$; and every $b\,w_{4} + b'\,T_{\mathrm{GJ}}$ commutes with $P$.
\end{enumerate}

## technical
Under Hypothesis (S), let $P = T^{\dagger}T + TT^{\dagger}$, the projector onto $\nu^{c}$ and its conjugate built from the Majorana element $T$, and let $T^{u}_{\mathrm{GJ}} = v_{4}(B - L)\chi$ be the up-type $126$ direction. Keeping $v_{4}$ off the condensate, $v_{4} - (v_{4}P + Pv_{4})$, gives the mass form of $\tfrac34(v_{4} + T^{u}_{\mathrm{GJ}})$: the $10$ and the $126$ doublet at equal weight, coupling $(Q, u^{c})$ exactly as $v_{4}$ does and with no $(L, \nu^{c})$ entry; the same operation leaves the mass form of $w_{4}$ unchanged.

Moreover $a\,v_{4} + a'\,T^{u}_{\mathrm{GJ}}$ commutes with $P$ if and only if $a' = a$, which is exactly when it annihilates $\nu^{c}$, while every $b\,w_{4} + b'\,T_{\mathrm{GJ}}$ commutes with $P$.

## lay
Under the framework's working hypothesis about how particle slots behave, this computes what happens when the up-type Higgs direction is kept away from the right-handed neutrino condensate. The result is an equal mix of the two standard ingredients of unified mass models, which removes the neutrino's Dirac mass while leaving the up quark's untouched. It also shows that requiring compatibility with the condensate is the same as requiring that removal, so the one cannot be used to derive the other.

## one-liner
Under Hypothesis (S), keeping $v_{4}$ off the Majorana condensate gives the $10$ and $126$ up-type doublets at equal weight, and commuting with the condensate projector is equivalent to annihilating $\nu^{c}$.
