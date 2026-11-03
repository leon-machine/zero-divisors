---
id: field-theory.twistor-attachment
kind: claim
version: 6
title: The attachment through conformal spinors
status: proved
region: field-theory
subject: quantum-fields
tags: [conformal-spinors, car-algebra]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of FT, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - field-theory.imported-standard-field-theory@4
  - field-theory.imported-statistics-no-go-palatial-algebra@2
  - field-theory.imported-tower-limit@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_QFT.py
  tags:
  - id:A5.1
  - id:A5.2
  - id:A5.3
  - id:A5.4
  - id:A5.5
  - id:B2.1
  - id:A4.4
  - id:A4.5
  - id:A4.6
- kind: check
  ref: check.py::check_oscillator_module_spectrum_and_twistor_form
- kind: check
  ref: check.py::check_u22_preserves_positive_energy_helicity_modules
- kind: check
  ref: check.py::check_kernels_exchange_parity_is_spin_statistics
lineage:
  motivated_by:
  - field-theory.ground-does-not-attach-modes
locators:
  paper: FT
  number: Prop 3.2
  label: prop:attach
  line: 99
extraction:
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 5 -> 6, by Leon''s decision of 2026-11-01 on spin and statistics: a marked note at the end of the formal and technical levels that for the attached free fields the clause "a CAR lift is local exactly when 2s is odd" follows from locality with positive norm (synthesis.locality-of-the-attached-free-fields-fixes-their-statistics), the Jost-point import being kept for interacting fields; that with an indefinite (Krein) form a CAR scalar is local (the ghost case); and that KMS at period 2 pi ((N+), (R_loc)) does not fix statistics (synthesis.modular-period-on-values-is-the-dual-plane-turn), with no modular-covariance premise. Statement, proof and checks unchanged; no edge added; the pin of field-theory.imported-standard-field-theory moves to @3 (its marked note, imports unchanged).'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the oscillator module''s relations, twistor form, helicity and energy spectrum with multiplicities, u(2,2) preserving the positive-energy helicity modules, and the kernels'' exchange parity (-1)^{2s}. Version 4 -> 5.'
  env: proposition
  source_formal: 'The attachment available to the series is the twistor one: the palatial storey supplies
    a positive-energy one-particle space with a conformal-group action, the Penrose transform supplies
    the mode functions, and the tower''s CAR is the second quantisation over that space. In the oscillator
    model the helicity-$s$ module has energies $|s| + 1 + n$ with multiplicity $(n+1)(n + 2|s| + 1)$;
    the conformal energy is the palatial quadratic of the twistor form; the sixteen generators of $\mathfrak{u}(2,2)$
    preserve each positive-energy, fixed-helicity module. On this attachment the tower''s floors are energy
    cut-offs, not regions of spacetime. Spin-statistics constrains it: a CAR lift is local exactly when
    $2s$ is odd, and the series'' fermion assignments pass.'
  source_title: The twistor attachment
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: 'Converted ''the twistor one'' and ''the twistor form'' to the attachment through the conformal
      spinor space and the reversion form h on it, with the twistor names once in parentheses; the palatial
      storey and the Penrose transform keep their names (Penrose''s programme and transform). The proof''s
      ''Jost framing and Penrose isomorphism imported'' was kept: it names imports, not twistor machinery.'
  typing:
    by: ai-typing-pass
    added:
    - field-theory.imported-statistics-no-go-palatial-algebra
    - field-theory.imported-tower-limit
    note: 'Kept the standard field-theory fact (the Jost framing and the Penrose isomorphism the proof
      imports); added the palatial-algebra fact, whose oscillator realisation the model uses (check A5.1),
      and the tower-limit fact, whose CAR the attachment second-quantises over. Levels pass: levels written
      from scratch, keeping every condition and level qualifier of the formal statement.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    stated_role:
    - field-theory.imported-tower-limit
    - field-theory.imported-statistics-no-go-palatial-algebra
---

## formal
The attachment available to the series is the one through the conformal spinor space $\CS$ (the twistor attachment): the palatial storey supplies a positive-energy one-particle space with a conformal-group action, the Penrose transform supplies the mode functions, and the tower's CAR is the second quantisation over that space. In the oscillator model the helicity-$s$ module has energies $|s| + 1 + n$ with multiplicity $(n+1)(n + 2|s| + 1)$; the conformal energy is the palatial quadratic of the reversion form $h$ on $\CS$ (the twistor form); the sixteen generators of $\mathfrak{u}(2,2)$, the algebra preserving $h$, preserve each positive-energy, fixed-helicity module. On this attachment the tower's floors are energy cut-offs, not regions of spacetime. Spin-statistics constrains it: a CAR lift is local exactly when $2s$ is odd, and the series' fermion assignments pass.

\emph{Note (spin and statistics, 2026-11-01).} For the attached free fields (scalar, spinor, photon) the clause on CAR lifts follows from locality with a positive norm, given the massless two-point function (\claimref{synthesis.locality-of-the-attached-free-fields-fixes-their-statistics}); the Jost-point form of Fact \claimref{field-theory.imported-standard-field-theory} is kept for interacting fields. The positive norm is needed: with an indefinite (Krein) form a CAR scalar is local, the case of the Faddeev-Popov ghosts. The KMS condition at rapidity period $2\pi$ of the thermal premises (\claimref{synthesis.n-plus-null-ground-state}, and (R$_{\mathrm{loc}}$) of \claimref{synthesis.c-loc-local-horizon-premise}) holds for CAR and CCR modes alike and does not fix statistics (\claimref{synthesis.modular-period-on-values-is-the-dual-plane-turn}); modular covariance, which would fix them through an imported theorem, is not a premise of the store.

## technical
The series' modes attach to spacetime through the conformal spinor space: the palatial storey gives a positive-energy one-particle space with a conformal-group action, the Penrose transform gives the mode functions, and the tower's CAR second-quantises over that space. In the oscillator model the helicity-$s$ module has energies $|s| + 1 + n$ with multiplicity $(n+1)(n + 2|s| + 1)$, the conformal energy is the palatial quadratic of the reversion form $h$, and the sixteen generators of $\mathfrak{u}(2,2)$ preserve each positive-energy, fixed-helicity module.

The tower's floors are then energy cut-offs, not regions of spacetime, and spin-statistics constrains the attachment: a CAR lift is local exactly when $2s$ is odd, which the series' fermion assignments satisfy. (Note, 2026-11-01: for the attached free fields this follows from locality with a positive norm, \claimref{synthesis.locality-of-the-attached-free-fields-fixes-their-statistics}; the Jost-point import is kept for interacting fields, and the thermal period alone does not fix statistics, \claimref{synthesis.modular-period-on-values-is-the-dual-plane-turn}.)

## lay
Since spacetime symmetries do not act on the tower's modes directly, the link must come from elsewhere. It comes from the series' conformal spinor storey, which provides positive-energy particle states with the right symmetry, while the Penrose transform turns them into waves in spacetime. On this reading the tower's levels are energy cut-offs rather than places, and the usual link between spin and statistics holds for the series' fermions.

## one-liner
The modes attach to spacetime through the conformal spinor space, the palatial storey giving a positive-energy one-particle space and the Penrose transform the mode functions, with floors as energy cut-offs and local CAR lifts exactly for odd $2s$.
