---
id: scrambling.imported-modes-modular-inventory
kind: claim
version: 4
title: 'Imported: the mode''s modular inventory'
status: proved
region: scrambling
subject: descent
tags: [modular-theory, rotors-and-stabilisers]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T08, deposited version
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 4
  source: maintainer pass 2026-11-07 (GA units)
review: typed
derivations:
- name: main
  uses:
  - hawking.modular-structure-completed-pair@3
  - singularity.euclidean-rotor-where-it-lies@4
  - singularity.computed@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_boost_bivector_weights_and_spectral_projectors
- kind: check
  ref: check.py::check_unique_flow_up_to_reparametrisation
- kind: check
  ref: check.py::check_surface_gravity_normalisation
- kind: check
  ref: check.py::check_euclidean_continuation_period_and_reality
locators:
  paper: T08
  number: Fact 2.2
  label: fact:inventory
  line: 592
outside_ga:
  kind: complex-analysis
  why: 'the clause states that the continuation''s generator i sigma lies outside the real algebra Cl(1,3) (T5 Prop. 7.21(3)); with the atom''s unit J (U2) it is J sigma = I_4 and with I_4 it is e_2 e_3, both in Cl(1,3), so no pseudoscalar of the algebra can stand for this i without making the statement false'
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 4 kept (already raised in this pass). Not resolved (U6). The clause states that the continuation''s generator i sigma lies outside the real algebra (T5 Prop. 7.21(3), singularity.euclidean-rotor-where-it-lies (3): outside Cl(1,3)). With the atom''s unit J of U2 the generator is J sigma = I_4, and with I_4 it is I_4 sigma = e_2 e_3; both lie in Cl(1,3), so either replacement makes the statement false. The central I_5 of Cl(2,3) would keep it true but would give the complexified atom a unit other than the J that U2 assigns to it. The bare i stays and the declaration is kept with its reason narrowed. Text unchanged.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (complex-analysis): the continuation of the boost rotor to imaginary rapidity lives in the complexified atom, and the result states that its generator i sigma lies outside the real algebra, so no pseudoscalar of that algebra can stand for i.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: on the atom Cl(1,1), sigma = e+e- with weights -1/+1, sigma = P1 - P0, a one-dimensional bivector space, kappa = 1/4M from f = 1 - 2M/r, and the continuation''s 2 pi conjugation period with i sigma outside the real algebra. Version 2 -> 3.'
  env: fact
  context_refs:
  - hawking.modular-structure-completed-pair
  - singularity.euclidean-rotor-where-it-lies
  outside_pilot_cites:
  - ButlerT5
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    added:
    - singularity.computed
    note: added the computed surface gravity, since the fact cites the source's appendix for the geometric
      normalisation at kappa = 1/4M; the rapidity-to-time conversion itself (the plane-and-rate proposition)
      was not added because the fact cites the appendix, not that proposition
  i4_conversion:
    by: ai-i4-pass
    date: '2026-10-21'
    converted: []
    kept:
    - '$i\sigma$: generator of the continuation to imaginary rapidity in the complexified atom, stated to
      lie outside the real algebra (analytic continuation; imported from T5)'
  flow_note: rotor flow exp(lambda sigma/2) (T05 Thm 6.3, T08 Lem 4.2). The flow it imports is the rotor
    flow with weights -1, +1 on the pair; the 2 pi imaginary-rapidity cycle it also records is the phase
    flow's, which it places outside the real algebra as the clock's Euclidean continuation.
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 4
    note: 'The two boost flows: flow_note recorded.'
---

## formal
For a completed pair, the boost bivector $\sigma$ satisfies $\sigma^2 = 1$, generates the rotor flow with weights $\mp 1$ on the pair, has the occupation projectors as spectral projectors, acts in Fock representation through $\tfrac12\sigma = N - \tfrac12$, and is the unique one-parameter rotor flow of the atom \emph{up to reparametrisation of the flow parameter and orientation} (the bivector space is one-dimensional: the algebra fixes the orbits, not the speed, which is the normalisation the geometry supplies). The geometric normalisation converts rapidity to Schwarzschild time at the surface gravity $\kappa = 1/4M$. Continued to imaginary rapidity, the boost rotor becomes a unitary of the complexified atom whose conjugation action has period exactly $2\pi$; the continuation's generator $i\sigma$ lies outside the real algebra, so the cycle belongs to the clock's Euclidean continuation, not to any intrinsic flow of the boundary modes. \emph{Provenance:} \cite[Prop.~2.1]{ButlerT7} (proved self-contained there); the normalisation \cite[App.~A]{ButlerT5}; the continuation and its $2\pi$ conjugation period \cite[Prop.~7.21(1)]{ButlerT5}; the exclusion of $i\sigma$ from the real algebra \cite[Prop.~7.21(3)]{ButlerT5}.

## technical
For a completed pair, the boost bivector $\sigma = v^{*}v - vv^{*}$ satisfies $\sigma^{2} = 1$, generates the rotor flow under which the two ladder elements carry weights $\mp 1$, has the occupation projectors as its spectral projectors, and in the Fock representation satisfies $\tfrac12\sigma = N - \tfrac12$. It is the unique one-parameter rotor flow of the atom up to reparametrisation of the flow parameter and orientation: the bivector space is one-dimensional, so the algebra fixes the orbits but not the speed, and the geometric normalisation converts rapidity to Schwarzschild time at surface gravity $\kappa = 1/4M$.

Continued to imaginary rapidity, the boost rotor becomes a unitary of the complexified atom whose conjugation action has period exactly $2\pi$. Its generator $i\sigma$ lies outside the real algebra, so this cycle belongs to the clock's Euclidean continuation and not to any intrinsic flow of the boundary modes.

## lay
Each boundary mode carries a built-in clock: one element that generates boosts, counts whether the mode is occupied, and supplies the projections used to discard coherence. The algebra fixes the shape of this clock's motion but not its rate; the black hole's geometry sets the rate through its surface gravity. Continuing the clock to imaginary time gives a cycle of period $2\pi$, but that cycle lies outside the real algebra, so it is not a genuine motion of the modes.

## one-liner
Imported: the completed pair's boost bivector squares to one, generates the atom's unique rotor flow up to reparametrisation, equals $2N - 1$ in Fock representation, runs at $\kappa = 1/4M$ once normalised, and has a $2\pi$ imaginary-rapidity cycle generated outside the real algebra.
