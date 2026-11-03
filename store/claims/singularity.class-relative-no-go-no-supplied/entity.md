---
id: singularity.class-relative-no-go-no-supplied
kind: claim
version: 3
title: 'The class-relative no-go: no supplied generator hops'
status: proved
region: singularity
subject: entropy
tags: [no-go, thermal-premises, boundary-modes]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
review: typed
derivations:
- name: main
  uses:
  - sheaf.function-linearity-tame-constructions@2
  - singularity.bundle-maps-quantise-without-hopping@3
  - singularity.function-linear-endomorphisms-are-bundle-maps@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_supplied_generators_commute_with_every_occupation
- kind: check
  ref: check.py::check_pairing_generators_lie_outside_the_class
locators:
  paper: T05
  number: Thm C.8
  label: thm:hopclass
  line: 2706
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: in the three-point Fock model, the computed function-linear maps and the parity products quantise to diagonal generators commuting with every N_x, while pairing generators commute with Gamma, move N_x and N_tot by 2 and are not of the form dGamma(a). Version 2 -> 3.'
  env: theorem
  typing:
    by: ai-typing-pass
    removed:
    - singularity.l-boundary-mode-locality
    note: 'Removed the assumes edge to (L_E): the theorem proves the no-hopping half of that premise within
      the supplied class rather than assuming it, and its proof never invokes it. Levels pass: the lay
      level now states the assumed function-linearity fact, which it had dropped.'
---

## formal
Assume Fact \claimref{sheaf.function-linearity-tame-constructions}. Let the \emph{supplied class} consist of the second quantisations $d\Gamma(a)$ of the $C^\infty(E)$-linear endomorphisms $a$ of the mode line bundle (the line bundle over $E$ whose fibre at $x$ is the one-particle line of the mode there), together with the products of the parity sections $\sigma(x)$. Then no generator in the supplied class moves occupation from the ladder at one point of $E$ to the ladder at another: every one of them commutes with every $N_x$. Indeed the supplied class is \emph{ultralocal}: each of its generators is a sum of single-point terms, a multiplication operator in the joint number basis, and propagates nothing between points, so the theorem excludes hopping by generators that could not move anything in any case. Within the supplied class, the no-hopping half of Premise \claimref{singularity.l-boundary-mode-locality} is a theorem. The class does not contain, and the theorem does not exclude, pairing generators of the form $v^{*}_x v^{*}_y + v_y v_x$: these are $C^\infty$-linear in their coefficient functions, commute with the total parity $\Gamma$, are not joint-diagonal, and do not commute with $N_x$; their exclusion remains part of Premise \claimref{singularity.l-boundary-mode-locality}.

## technical
Assume function-linearity of the tame constructions, and let the supplied class consist of the second quantisations $d\Gamma(a)$ of the $C^\infty(E)$-linear endomorphisms $a$ of the mode line bundle, together with products of the parity sections $\sigma(x)$. Every generator in this class commutes with every $N_x$, so none moves occupation between points of $E$: the class is ultralocal, each generator a sum of single-point multiplication operators in the joint number basis.

Within this class the no-hopping half of the boundary-mode locality premise is therefore a theorem. Pairing generators $v^{*}_x v^{*}_y + v_y v_x$ lie outside the class: they commute with the total parity $\Gamma$ but not with $N_x$, and their exclusion remains part of the premise.

## lay
The framework supplies only certain kinds of operators to drive the quantum modes at the singularity. Given that the series' tame constructions are function-linear (an imported fact), this result shows that none of those supplied operators can move a particle from one point to another, because each acts point by point. It does not rule out operators that create or destroy particles in pairs, so excluding those still has to be assumed.

## one-liner
Given function-linearity of the tame constructions, no generator in the supplied class moves occupation between points of $E$, while pairing generators lie outside the class and are not excluded.
