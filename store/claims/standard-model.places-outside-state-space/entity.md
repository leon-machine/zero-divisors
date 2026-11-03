---
id: standard-model.places-outside-state-space
kind: claim
version: 2
title: The places outside the state space
status: conjectured
region: standard-model
subject: standard-model
tags:
- running-and-unification
- open-problem
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
lineage:
  motivated_by:
  - standard-model.imported-coefficient-sum-indices
  - standard-model.mass-bracket-charged-singlet
  - standard-model.table-exact
  - standard-model.under-s-state-space-complete-multiplets
locators:
  paper: T12
  number: Obs 8.14
  label: obs:seats
  line: 1431
extraction:
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: Converted the two-twistor U(2) to the U(2) mixing two conformal spinors in the formal and technical
      levels.
  source_title: The places outside the state space
  source_formal: 'The state space is not the whole of what this paper derives, and the demanded content,
    being split content, is more naturally sought where the series already has splits. Three places, in
    order of how much structure the series has for them, none of them a derivation. (a) \emph{The automorphism
    algebra.} The gauge fields lie in the adjoint of $S(U(2) \times U(3))$, which is not a complete multiplet
    of any simple $G_{U}$ containing it (the $24$ of $SU(5)$ minus the $(2,3)_{-5/6}$ and its conjugate),
    and it is this incompleteness that gives the Standard Model''s own $-\tfrac{11}{3}C_{2}$ its three
    unequal values. Fermionic content in the adjoint, the gauginos, is the split content the series''
    structure most nearly suggests, and Proposition \claimref{standard-model.table-exact} says it is not
    enough alone: it needs the doublet content of the next place, and even then falls short at one loop.
    (b) \emph{The mass bracket.} Proposition \claimref{standard-model.mass-bracket-charged-singlet} shows
    the mass bracket to be a charged singlet under the two-twistor $U(2)$, the order parameter whose condensate
    is the mass of the mass paper T11 \cite{ButlerT11}; the Higgs doublet of Fact \claimref{standard-model.imported-coefficient-sum-indices}
    is imported, not derived, and a derivation of the scalar sector would say how many doublets there
    are, which is the row ``second doublet'''' of the table and the $\tfrac{1}{10}, \tfrac16$ of the higgsino
    row''s scalar partner. (c) \emph{The slot/pair split.} Proposition \claimref{standard-model.under-s-state-space-complete-multiplets}
    says the split must cut across the $SU(5)$ pieces and that the framework''s one derived cut is between
    slots and pairs. The $\bar{5}$ of the scalar sector, a doublet and a colour triplet, is cut exactly
    there: the doublet is the slot part, the triplet the pair part, and a mechanism that gave the two
    different masses would be the framework''s doublet-triplet splitting. No such mechanism is derived
    in the series. This is the structural form of the partner question after this subsection, and Section
    \ref{sec:mechanism} takes it up: not ``which tower'''' but ``what sets a slot-mode mass apart from
    a pair-mode mass''''. The same cut also enters as a gauge symmetry rather than as a mass difference:
    the automorphisms that preserve the split between slots and pairs are Pati-Salam (Section \ref{sec:split}).'
  env: observation
  context_refs:
  - standard-model.imported-coefficient-sum-indices
  - standard-model.mass-bracket-charged-singlet
  - standard-model.table-exact
  - standard-model.under-s-state-space-complete-multiplets
  outside_pilot_cites:
  - ButlerT11
  typing:
    by: ai-typing-pass
    note: 'An observation that explicitly offers no derivation, so it stays conjectured with its existing
      motivating claims; no edges. Levels pass: conditions already kept.'
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants: []
    added_about: []
    verdict: standalone
    note: Observation offering no derivation; spectrum-run cites its clause (b) only to say the doublet
      is imported.
---

## formal
The state space is not the whole of what this paper derives, and the demanded content, being split content, is more naturally sought where the series already has splits. Three places, in order of how much structure the series has for them, none of them a derivation. (a) \emph{The automorphism algebra.} The gauge fields lie in the adjoint of $S(U(2) \times U(3))$, which is not a complete multiplet of any simple $G_{U}$ containing it (the $24$ of $SU(5)$ minus the $(2,3)_{-5/6}$ and its conjugate), and it is this incompleteness that gives the Standard Model's own $-\tfrac{11}{3}C_{2}$ its three unequal values. Fermionic content in the adjoint, the gauginos, is the split content the series' structure most nearly suggests, and Proposition \claimref{standard-model.table-exact} says it is not enough alone: it needs the doublet content of the next place, and even then falls short at one loop. (b) \emph{The mass bracket.} Proposition \claimref{standard-model.mass-bracket-charged-singlet} shows the mass bracket to be a charged singlet under the $U(2)$ mixing two conformal spinors (the two-twistor $U(2)$), the order parameter whose condensate is the mass of the mass paper T11 \cite{ButlerT11}; the Higgs doublet of Fact \claimref{standard-model.imported-coefficient-sum-indices} is imported, not derived, and a derivation of the scalar sector would say how many doublets there are, which is the row ``second doublet'' of the table and the $\tfrac{1}{10}, \tfrac16$ of the higgsino row's scalar partner. (c) \emph{The slot/pair split.} Proposition \claimref{standard-model.under-s-state-space-complete-multiplets} says the split must cut across the $SU(5)$ pieces and that the framework's one derived cut is between slots and pairs. The $\bar{5}$ of the scalar sector, a doublet and a colour triplet, is cut exactly there: the doublet is the slot part, the triplet the pair part, and a mechanism that gave the two different masses would be the framework's doublet-triplet splitting. No such mechanism is derived in the series. This is the structural form of the partner question after this subsection, and Section \ref{sec:mechanism} takes it up: not ``which tower'' but ``what sets a slot-mode mass apart from a pair-mode mass''. The same cut also enters as a gauge symmetry rather than as a mass difference: the automorphisms that preserve the split between slots and pairs are Pati-Salam (Section \ref{sec:split}).

## technical
Since the state space alone cannot supply the split content the meeting condition demands, this observation lists three places where the series already has splits, none of them a derivation. (a) The gauge fields: the adjoint of $S(U(2) \times U(3))$ is not a complete multiplet of any simple group containing it, and gauginos are the split content the structure most nearly suggests, though alone they are not enough and even with doublet content they fall short at one loop. (b) The mass bracket is a charged singlet under the $U(2)$ mixing two conformal spinors, while the Higgs doublet is imported; a derived scalar sector would fix how many doublets there are.

(c) The slot/pair split: the scalar $\bar{5}$ is cut exactly there, the doublet being the slot part and the colour triplet the pair part, so a mechanism giving slot modes and pair modes different masses would be the framework's doublet-triplet splitting. No such mechanism is derived in the series.

## lay
The particles of one generation cannot by themselves make the three forces meet, so something with uneven masses is needed. This note lists three places in the framework where such unevenness might come from: partners of the force carriers, the scalar sector that gives mass, and the split between the two kinds of mode in a composite. It is a list of places to look, not a result, and the paper derives none of them.

## one-liner
The split content the meeting condition demands is most naturally sought in the gauge adjoint, the scalar sector behind the mass bracket, or the slot/pair split, though none of these is derived.
