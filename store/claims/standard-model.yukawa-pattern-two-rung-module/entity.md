---
id: standard-model.yukawa-pattern-two-rung-module
kind: claim
version: 6
title: The Yukawa pattern of the two-rung module
status: proved
region: standard-model
subject: standard-model
tags: [flavour-and-mixing, recovers-known-physics, representation-theory]
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
- name: Claude Opus 5.5
  role: 'consistency pass, citation moved out of a formula'
  version: 6
  source: maintainer pass 2026-11-07 (consistency)
review: typed
derivations:
- name: main
  uses:
  - standard-model.invariant-pairing-five-modes@5
  - standard-model.hyp-s-slot-statistics@10
  proof: proof-main.tex
- name: standard-route
  uses:
  - standard-model.imported-spinor-bilinears@1
  proof: proof-standard-route.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_rung_vectors_carry_dirac_yukawas
- kind: check
  ref: check.py::check_pair_vectors_carry_triplet_couplings
- kind: check
  ref: check.py::check_symmetric_hypercharge_conserving_and_no_bare_mass
locators:
  paper: T12
  number: Thm 9.24
  label: thm:yukawa
  line: 1730
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'A citation of Hypothesis (S) had been inserted inside the formula 6(Y(S) + Y(T)) + 6Y(x) = 0 (as an argument of Y); it is moved after the formula. No mathematics changed.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: every nonzero Y_x on the 16 x 16 basis pairs for all ten vectors with species counts, symmetry, hypercharge conservation and no bare mass term. Version 4 -> 5.'
  env: theorem
  context_refs:
  - standard-model.invariant-pairing-five-modes
  typing:
    by: ai-typing-pass
    removed:
    - standard-model.imported-spinor-bilinears
    added:
    - standard-model.invariant-pairing-five-modes
    - standard-model.imported-spinor-bilinears
    - standard-model.hyp-s-slot-statistics
    note: 'Moved the spinor-bilinear Fact from main to a standard-route, since the source says the theorem
      computes rather than imports it and that the Fact''s 10-coupling is the standard pattern; added
      the invariant pairing lemma; doubt whether the Fact alone reaches the triplet clause (ii). Hypothesis
      pass: assumes standard-model.hyp-s-slot-statistics added because its statement holds under Hypothesis
      (S) (the clauses are unconditional about sectors; the species reading is under (S)). Levels pass:
      lay and one-liner now say the species reading is under Hypothesis (S).'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.invariant-pairing-five-modes
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
For a vector $x$ of the ten, let $Y_{x}(\psi, \varphi) = B(\psi, x\varphi)$ on the sixteen; the species names below are those of the sectors under Hypothesis (S), and the clauses as statements about sectors are unconditional. Then:
\begin{enumerate}
\item[(i)] For $x$ a rung creation vector ($Y = +\tfrac12$), $Y_{x}$ is nonzero exactly on the species pairs $(L, \nu^{c})$ and $(Q, u^{c})$; for $x$ a rung annihilation vector ($Y = -\tfrac12$), exactly on $(L, e^{c})$ and $(Q, d^{c})$.
\item[(ii)] For $x$ a pair creation vector (colour triplet, $Y = -\tfrac13$), $Y_{x}$ is nonzero exactly on $(Q, Q)$, $(d^{c}, \nu^{c})$ and $(e^{c}, u^{c})$; for $x$ a pair annihilation vector (antitriplet, $Y = +\tfrac13$), exactly on $(Q, L)$ and $(u^{c}, d^{c})$.
\item[(iii)] Every $Y_{x}$ is symmetric in its two arguments and conserves hypercharge, $Y(\psi) + Y(\varphi) + Y(x) = 0$ on every nonzero entry; and no mass term exists without a vector (Lemma \claimref{standard-model.invariant-pairing-five-modes}).
\end{enumerate}
So the rung directions carry precisely the Dirac Yukawa couplings of the Standard Model, up-type and neutrino through the hypercharge-$+\tfrac12$ doublet and down-type and charged-lepton through the hypercharge-$-\tfrac12$ doublet, and the ground directions carry precisely the colour-triplet couplings that mediate baryon-number violation.

## technical
For a vector $x$ of the ten, let $Y_{x}(\psi, \varphi) = B(\psi, x\varphi)$ on the sixteen, with $B$ the invariant pairing. A rung creation vector ($Y = +\tfrac12$) couples exactly $(L, \nu^{c})$ and $(Q, u^{c})$, and a rung annihilation vector ($Y = -\tfrac12$) exactly $(L, e^{c})$ and $(Q, d^{c})$; a pair creation vector (colour triplet) couples exactly $(Q, Q)$, $(d^{c}, \nu^{c})$ and $(e^{c}, u^{c})$, and a pair annihilation vector $(Q, L)$ and $(u^{c}, d^{c})$. Every $Y_{x}$ is symmetric and conserves hypercharge, and no mass term exists without a vector.

So the rung directions carry precisely the Standard Model's Dirac Yukawa couplings, up-type and neutrino through the $+\tfrac12$ doublet and down-type and charged-lepton through the $-\tfrac12$ doublet, and the ground directions carry the colour-triplet couplings that mediate baryon-number violation. The species names are those of Hypothesis (S); as statements about sectors the clauses are unconditional.

## lay
A mass for a quark or lepton comes from pairing two particle states through a Higgs-like direction. This theorem works out, for each of the ten directions of the transported space, which pairs of particle states it joins. Reading the sectors as particle species, which uses Hypothesis (S), the two added pairs of directions join exactly the pairs that the Standard Model's Higgs couplings join, while the original directions join the pairs that would let protons decay.

## one-liner
Through the invariant pairing, the rung vectors of the ten couple exactly the Standard Model's Dirac Yukawa pairs and the pair vectors exactly the colour-triplet, baryon-violating pairs, with the species named under Hypothesis (S).
