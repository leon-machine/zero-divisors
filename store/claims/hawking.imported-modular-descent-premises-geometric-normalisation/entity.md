---
id: hawking.imported-modular-descent-premises-geometric-normalisation
kind: claim
version: 7
title: 'Imported: modular descent, its premises, and the geometric normalisation'
status: proved
region: hawking
subject: descent
tags: [modular-theory, descent-map, hawking-temperature, undetermined-input]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T07, deposited version
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 7
  source: maintainer pass 2026-11-07 (GA units)
review: typed
derivations:
- name: main
  uses:
  - hawking.imported-modular-descent-premises-geometric-normalisation-external@1
  - hawking.modular-structure-completed-pair@3
  - singularity.computed@4
  - singularity.descended-form-state-independent@4
  - singularity.euclidean-section-period@5
  - singularity.matching-steps-4b-4c-join-equation@6
  - singularity.modular-descent@6
  - singularity.rate-discharge-hypothesis-iii@5
  - singularity.rate-rigidity-temperature-not-algebra-intrinsic@5
  assumes:
  - singularity.p-univalence@2
  - singularity.r-regularity-fixed-locus@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_kms_states_are_gibbs_lines
- kind: check
  ref: check.py::check_descended_state_kms_at_free_beta
- kind: check
  ref: check.py::check_geometric_normalisation
locators:
  paper: T07
  number: Fact 2.2
  label: fact:descent
  line: 408
outside_ga:
  kind: complex-analysis
  why: 'the phase flow Ad(e^{it sigma/2}) of the completed pair is the scalar phase of the complexified atom, whose modes anticommute with I_4 (conventions, known limit 1); with I_4 in its place exp(I_4 t sigma/2) would be a real rotor of the dual plane and the flow a different one'
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (complex-analysis): the phase flow Ad(e^{it sigma/2}) of the completed pair is the scalar phase of the complexified atom, whose modes anticommute with I_4 (conventions, known limit 1); with I_4 in its place exp(I_4 t sigma/2) would be a real rotor of the dual plane and the flow a different one.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the one-mode KMS solution line diag(1, q), the descended thermofield marginals KMS at q = 9/16 and 16/9 (beta free in sign), and kappa = 1/4M, period 8 pi M, T_H = 1/(8 pi M) as exact rational identities. Version 5 -> 6.'
  env: fact
  context_refs:
  - hawking.modular-structure-completed-pair
  - singularity.descended-form-state-independent
  - singularity.euclidean-section-period
  - singularity.matching-steps-4b-4c-join-equation
  - singularity.modular-descent
  - singularity.rate-discharge-hypothesis-iii
  - singularity.rate-rigidity-temperature-not-algebra-intrinsic
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    added:
    - hawking.modular-structure-completed-pair
    - singularity.computed
    note: 'added the completed-pair proposition, whose boost flow the hypotheses are stated for, and the
      singularity paper''s computation of the surface gravity from the gauge field, cited in the provenance
      but missed by extraction; repinned the singularity targets to their current versions; no standard
      route added, since the Bisognano-Wichmann-Sewell and Israel results are cited as the mechanism and
      already enter main through the external-ingredients entry. Levels pass: the lay level now states
      the state hypotheses (pure, boost-invariant, entangling), which it had partly dropped.'
  source_formal: 'Let the ascended algebra of a horizon pair carry a state that is pure, invariant under
    the boost flow of Proposition \claimref{hawking.modular-structure-completed-pair}, and entangling across
    the pair (cyclic and separating for the one-sided subalgebra). Then the descended state is KMS for the
    boost flow at \emph{some} inverse temperature $\beta \in \R$ of rapidity, and the hypotheses leave $\beta$
    free, its sign included; the Gibbs \emph{form} of the descended state is state-independent. Positivity
    and the value are supplied by T5''s named premises: under (P) univalence and (R) the KMS condition at
    the geometric period (one modular period equal to one rapidity period $2\pi$, i.e.\ Schwarzschild time
    $2\pi/\kappa$, the Euclidean period $8\pi M$), the descended state is Fermi-Dirac at $\beta = 2\pi$
    of rapidity, which is the physical temperature $\TH = \kappa/2\pi = 1/8\pi M$; the boost plane is the
    one the shape operator scales by $-2$, and $\kappa = 1/4M$ is proved from the gauge field. Per mode
    of Schwarzschild frequency $\omega$ the reduced density matrix is the Fermi-Dirac matrix $\mathrm{diag}(1,
    e^{-\omega/\TH})/Z$. \emph{Provenance:} T5 \cite[Thms.~7.3 and 7.6, Prems.~7.8 and 7.19, Prop.~7.18,
    Thm.~7.20, Cor.~6.4]{ButlerT5}, with $\kappa = 1/4M$ from the gauge field in \cite[App.~A]{ButlerT5};
    premise (R) is proved irreducible there, the temperature being no algebra-intrinsic quantity \cite[Thm.~7.16]{ButlerT5}.
    The wedge-modular mechanism is Bisognano-Wichmann-Sewell \cite{BisognanoWichmann1976, Sewell1982}, and
    the thermofield reading is Israel''s \cite{Israel1976}.'
  flow_note: 'both: invariance is under the rotor flow exp(lambda sigma/2) (T05 Thm 6.3, T08 Lem 4.2) of
    T07 Prop 2.1 (equivalently its phase flow); the descended state is KMS for the phase flow e^{-i omega
    t} on the modes (T05 Thm 7.16, T07 Def 2.7), the Euclidean rotation of T05 Prop 7.21, generated by the
    same K = sigma/2.'
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 4
    note: 'The two boost flows: flow_note recorded; formal, proof main, technical now name the flow (original
      formal in source_formal, proof in orig-proof-*.tex where changed; version bumped).'
---

## formal
Let the ascended algebra of a horizon pair carry a state that is pure, invariant under the boost flow of Proposition \claimref{hawking.modular-structure-completed-pair}, and entangling across the pair (cyclic and separating for the one-sided subalgebra). Then the descended state is KMS for the phase flow $\operatorname{Ad}(e^{it\sigma/2})$ of the same generator at \emph{some} inverse temperature $\beta \in \R$ of rapidity, and the hypotheses leave $\beta$ free, its sign included; the Gibbs \emph{form} of the descended state is state-independent. Positivity and the value are supplied by T5's named premises: under (P) univalence and (R) the KMS condition at the geometric period (one modular period equal to one rapidity period $2\pi$, i.e.\ Schwarzschild time $2\pi/\kappa$, the Euclidean period $8\pi M$), the descended state is Fermi-Dirac at $\beta = 2\pi$ of rapidity, which is the physical temperature $\TH = \kappa/2\pi = 1/8\pi M$; the boost plane is the one the shape operator scales by $-2$, and $\kappa = 1/4M$ is proved from the gauge field. Per mode of Schwarzschild frequency $\omega$ the reduced density matrix is the Fermi-Dirac matrix $\mathrm{diag}(1, e^{-\omega/\TH})/Z$. \emph{Provenance:} T5 \cite[Thms.~7.3 and 7.6, Prems.~7.8 and 7.19, Prop.~7.18, Thm.~7.20, Cor.~6.4]{ButlerT5}, with $\kappa = 1/4M$ from the gauge field in \cite[App.~A]{ButlerT5}; premise (R) is proved irreducible there, the temperature being no algebra-intrinsic quantity \cite[Thm.~7.16]{ButlerT5}. The wedge-modular mechanism is Bisognano-Wichmann-Sewell \cite{BisognanoWichmann1976, Sewell1982}, and the thermofield reading is Israel's \cite{Israel1976}.

## technical
Suppose the ascended algebra of a horizon pair carries a state that is pure, invariant under the boost flow of the completed pair, and entangling across the pair (cyclic and separating for the one-sided subalgebra). Then the descended state is KMS for the phase flow $\operatorname{Ad}(e^{it\sigma/2})$ of the same generator at some inverse temperature $\beta\in\R$ of rapidity, with $\beta$ left free, sign included; the Gibbs form of the descended state is state independent.

Under the premises (P) univalence and (R) the KMS condition at the geometric period, the descended state is Fermi-Dirac at $\beta = 2\pi$ of rapidity, the physical temperature $\TH = \kappa/2\pi = 1/8\pi M$, with $\kappa = 1/4M$ proved from the gauge field; per mode of Schwarzschild frequency $\omega$ the reduced density matrix is $\operatorname{diag}(1, e^{-\omega/\TH})/Z$. Premise (R) is irreducible, the temperature being no algebra-intrinsic quantity.

## lay
When a pure state that is entangled across a black-hole horizon and unchanged by the horizon's boost is viewed from one side only, it looks thermal, but the algebra alone does not fix the temperature, not even its sign. Two named premises from the singularity work, one about fermion parity and one about regularity of the geometry, fix it at the Hawking temperature. Each mode then has the Fermi-Dirac occupation expected of fermions at that temperature.

## one-liner
A pure, boost-invariant, entangling state of a horizon pair descends to a KMS state at an undetermined temperature, which the premises (P) and (R) fix as Fermi-Dirac at the Hawking temperature $\TH = 1/8\pi M$.
