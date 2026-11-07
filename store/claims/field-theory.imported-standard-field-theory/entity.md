---
id: field-theory.imported-standard-field-theory
kind: claim
version: 5
title: 'Imported: standard field theory'
status: imported
region: field-theory
subject: quantum-fields
tags: [classical-theorem, conformal-spinors, hypercharge-and-anomalies]
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
- name: Claude Opus 5.5
  role: 'maintainer pass, marked pointer to the anomaly Fact at Leon''s decisions'
  version: 5
  source: maintainer pass 2026-11-07 (decisions)
review: typed
imported_from:
- citation: R. F. Streater and A. S. Wightman, PCT, Spin and Statistics, and All That, ch. 4 (the Jost-point
    form of the spin-statistics theorem; named in the source)
- citation: The Penrose transform and its H^1 isomorphism (Penrose; named in the source)
- citation: S. Weinberg and E. Witten, the Weinberg-Witten theorem (named in the source)
- citation: The random-phase Goldstone pole of the Nambu-Jona-Lasinio model (named in the source)
- citation: The Coulomb-gauge Hamiltonian of quantum electrodynamics (Sakurai; Weinberg, The Quantum Theory
    of Fields, vol. I; named in the source)
- citation: The Adler-Bell-Jackiw anomaly (named in the source)
locators:
  paper: FT
  number: Fact 2.4
  label: fact:standard
  line: 86
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 4 -> 5. Decision item E3 (routine): a dated, marked pointer after the Adler-Bell-Jackiw anomaly names synthesis.imported-adler-bell-jackiw-axial-anomaly, which imports it with its citations and equation and is kept as its home; no link edge (a Fact listing), no retirement.'
  maintainer_pass_qft_full:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 3 -> 4, by Leon''s decision of 2 November 2026 on the Jost import: a marked note at the formal and technical levels that the Jost-point import is needed only beyond perturbation theory (synthesis.interacting-fields-of-causal-perturbation-theory-keep-the-spin-statistics-connection-at-even-ghost-number), and that Kuckert''s modular P1CT symmetry with the spectrum condition is a weaker alternative premise (Fact synthesis.imported-kuckert-modular-pct-spin-statistics-and-borchers-theorem; synthesis.wedge-reflections-compose-to-the-two-pi-rotor-so-geometric-modular-conjugations-give-interacting-spin-statistics), a note only, not adopted. The six imports and their provenance are unchanged; no edge added.'
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2 -> 3, by Leon''s decision of 2026-11-01 on spin and statistics: a marked note at the end of the formal and technical levels that for the attached free fields the statistics follow from locality with positive norm (synthesis.locality-of-the-attached-free-fields-fixes-their-statistics), the Jost-point import being kept for interacting fields; that KMS at period 2 pi ((N+), (R_loc)) does not fix statistics (synthesis.modular-period-on-values-is-the-dual-plane-turn); and that there is no modular-covariance premise. The six imports are unchanged; no edge added.'
  env: fact
  flags:
  - imported fact with no citation
  source_formal: The Jost-point form of the spin-statistics theorem (Streater and Wightman, ch.~4); the
    Penrose transform and its $H^1$ isomorphism; the Weinberg-Witten theorem (massless particles of spin
    greater than one half carry no charge under a conserved Lorentz-covariant current); the random-phase
    Goldstone pole of the Nambu-Jona-Lasinio model; the Coulomb-gauge Hamiltonian of quantum electrodynamics;
    the Adler-Bell-Jackiw anomaly.
  source_title: 'Imported: standard field theory'
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: 'Converted the two twistor-bearing imports: the Penrose transform now names its spacetime-algebra
      kernels and its cohomology on the projective spinor space, and the Jost-point form names the geometric-algebra
      reading of the complex Lorentz path (both from the twistor GA run, E2); the six imports themselves
      are unchanged. The added readings are the dictionary''s, not part of what is imported.'
  typing:
    by: ai-typing-pass
    note: 'The extractor found no citation; the source names its six imports in the statement (and Sakurai
      and Weinberg for Coulomb-gauge electrodynamics in its prior art), so those names are the provenance;
      the note has no bibliography to give fuller references. Levels pass: levels written from scratch,
      keeping every condition and level qualifier of the formal statement.'
---

## formal
The Jost-point form of the spin-statistics theorem (Streater and Wightman, ch.~4), whose complex Lorentz path reads in geometric algebra as the rotation of one chirality through $2\pi$, $(1-\Pi) + \Pi\exp(\theta\gamma_1\gamma_2)$ with $\Pi = (1 - E)/2$, ending at conjugation by $E$, the total inversion $x \mapsto -x$ on the conformal model; the Penrose transform, whose kernels the spacetime algebra writes as $x\psi_0\gamma_0/Q(x)^2$ (spin $\tfrac12$), $xBx/Q(x)^3$ (Maxwell) and $1/Q(x)$ (scalar), and its $H^1$ isomorphism with cohomology on regions of the projective spinor space $\PCS$ (projective twistor space); the Weinberg-Witten theorem (massless particles of spin greater than one half carry no charge under a conserved Lorentz-covariant current); the random-phase Goldstone pole of the Nambu-Jona-Lasinio model; the Coulomb-gauge Hamiltonian of quantum electrodynamics; the Adler-Bell-Jackiw anomaly.

\emph{Note (spin and statistics, 2026-11-01).} For the attached free fields (scalar, spinor, photon) the statistics follow from locality with a positive norm, given the massless two-point function (\claimref{synthesis.locality-of-the-attached-free-fields-fixes-their-statistics}); the Jost-point form imported here is kept for interacting fields. The KMS condition at rapidity period $2\pi$ of the thermal premises (\claimref{synthesis.n-plus-null-ground-state}, and (R$_{\mathrm{loc}}$) of \claimref{synthesis.c-loc-local-horizon-premise}) holds for CAR and CCR modes alike and does not fix statistics (\claimref{synthesis.modular-period-on-values-is-the-dual-plane-turn}); modular covariance of the wedge algebras, which would fix them through an imported theorem, is not a premise of the store.

\emph{Note (the Jost import, 2 November 2026).} The Jost-point form is needed only beyond perturbation theory: in causal perturbation theory the interacting fields keep the spin-statistics connection of the free fields to every order, on every field with an even number of ghost factors (\claimref{synthesis.interacting-fields-of-causal-perturbation-theory-keep-the-spin-statistics-connection-at-even-ghost-number}). Beyond perturbation theory a premise remains. Kuckert's modular P$_{1}$CT symmetry (the modular conjugation of each wedge algebra acts on the local algebras as the wedge's reflection), with covariance under the covering group, the spectrum condition and compact internal symmetries, is a weaker alternative premise from which the connection follows (Fact \claimref{synthesis.imported-kuckert-modular-pct-spin-statistics-and-borchers-theorem}; its spacetime-algebra form, \claimref{synthesis.wedge-reflections-compose-to-the-two-pi-rotor-so-geometric-modular-conjugations-give-interacting-spin-statistics}); it is recorded here as a note only, not adopted, and nothing in the store supplies it. The imports listed above are unchanged.
## technical
Six standard results that the field-theory note imports: the Jost-point form of the spin-statistics theorem; the Penrose transform and its $H^1$ isomorphism; the Weinberg-Witten theorem, that massless particles of spin greater than one half carry no charge under a conserved Lorentz-covariant current; the random-phase Goldstone pole of the Nambu-Jona-Lasinio model; the Coulomb-gauge Hamiltonian of quantum electrodynamics; and the Adler-Bell-Jackiw anomaly. (Note, 7 November 2026: the Adler-Bell-Jackiw anomaly is imported with its sources and its equation in Fact \claimref{synthesis.imported-adler-bell-jackiw-axial-anomaly}, which is its home in the store; it is named here as the note names it.) (Note, 2026-11-01: for the attached free fields the spin-statistics connection follows from locality with a positive norm, \claimref{synthesis.locality-of-the-attached-free-fields-fixes-their-statistics}; the Jost-point import is kept for interacting fields, and the thermal period alone does not fix statistics, \claimref{synthesis.modular-period-on-values-is-the-dual-plane-turn}.) (Note, 2 November 2026: the Jost-point import is needed only beyond perturbation theory, since causal perturbation theory carries the free fields' spin-statistics connection to interacting fields order by order, \claimref{synthesis.interacting-fields-of-causal-perturbation-theory-keep-the-spin-statistics-connection-at-even-ghost-number}; Kuckert's modular P$_{1}$CT symmetry with the spectrum condition would be a weaker premise there, noted and not adopted, \claimref{synthesis.wedge-reflections-compose-to-the-two-pi-rotor-so-geometric-modular-conjugations-give-interacting-spin-statistics}.)

In geometric algebra Jost's complex Lorentz path is the rotation of one chirality through $2\pi$, ending at conjugation by the ascent bivector $E$, and the Penrose transform's kernels are $x\psi_0\gamma_0/Q(x)^2$ for spin $\tfrac12$, $xBx/Q(x)^3$ for Maxwell and $1/Q(x)$ for the scalar, with the cohomology taken on regions of the projective spinor space $\PCS$.

## lay
The field-theory note relies on six textbook results that it does not reprove: the theorem linking spin to statistics, the transform that turns geometric data into massless fields, a theorem forbidding certain massless charged composite particles, the way a fermion condensate yields a massless scalar, the standard energy operator of quantum electrodynamics, and the axial anomaly.

## one-liner
Imported: Jost-point spin-statistics, the Penrose transform and its $H^1$ isomorphism, Weinberg-Witten, the Nambu-Jona-Lasinio Goldstone pole, the Coulomb-gauge Hamiltonian and the Adler-Bell-Jackiw anomaly.
