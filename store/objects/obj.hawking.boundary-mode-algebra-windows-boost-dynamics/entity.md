---
id: obj.hawking.boundary-mode-algebra-windows-boost-dynamics
kind: object
version: 2
title: The boundary-mode algebra, windows, and the boost dynamics
status: defined
region: hawking
subject: thermality
tags: [boundary-modes, car-algebra]
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
review: draft
outside_ga:
  kind: complex-analysis
  why: 'the algebra is defined as the CAR algebra over the complex space l^2(J) with windows End(Lambda C^F), and the boost dynamics tau_t(a_j) = e^{-i omega_j t}a_j is the scalar phase of that complex algebra; its modes descend from the atom of the spacetime radial plane, which anticommutes with I_4 (conventions, known limits 1 and 2), so I_4 is not shown to be its unit'
locators:
  paper: T07
  number: Def 2.7
  label: def:ledger
  line: 430
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: the phase e^{-i omega_j t} of the boost dynamics is the scalar of the complex CAR algebra over l^2(J) as defined (T07 Def 2.7), and the store records that the modes of T05''s atom anticommute with I_4 and that this algebra is complex here and real in the scrambling results (conventions, known limits 1 and 2); declared complex-analysis, left for Leon to rule.'
  env: definition
  open_problem: op.boundary-mode-provenance
  correction:
    by: 2026-10-22-toe
    version: 2
    note: >-
      Version 1 left the provenance of the countable mode set to the cited tower-limit Fact, and the
      paper's running text says the modes are countable because the tower adjoins them one rung at a
      time. The singularity paper (s-wave aggregation of the ladder pairs of E, one per point) and the
      tower paper's corollary (one ascent on the physical closure; further rungs on shadow walls) say
      otherwise. The definition now states one provenance: J indexes the s-wave aggregate of the ladder
      pairs, the tower limit being the algebra's model. The defined objects (algebra, windows, flow,
      normalisation) are unchanged. The particle-hole and zero-mode clause is this definition's
      convention, not a statement of either paper.
  context_refs:
  - hawking.imported-algebra-boundary-modes-car-algebra
  - hawking.imported-modular-descent-premises-geometric-normalisation
  - singularity.bosonisation-bridge-s-wave-sector
  - tower.answers-iteration-question
  typing:
    by: ai-typing-pass
    note: Definition; no derivation edges.
  i4_conversion:
    by: ai-i4-pass
    date: '2026-10-21'
    converted: []
    kept:
    - '$\tau_t(a_j) = e^{-i\omega_j t}a_j$: kept as the scalar of the complex CAR algebra over $\ell^2(J)$
      with windows $\End(\Lambda^\bullet \C^F)$ (matrix algebras over $\C$); converting would need the definition
      itself recast over $\mathrm{span}\{1, I_4\}$, and the related scrambling statements say the phase
      generator lies outside the real boundary-mode algebra. Doubtful, left for the maintainer'
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants:
    - hawking.imported-quasi-free-states-car-algebra
    added_about: []
    verdict: connected
    note: A definition cannot carry uses or assumes; the added links are about edges from the claims whose
      statements use the defined notion.
  flow_note: phase flow e^{-i omega t} on the modes (T05 Thm 7.16, T07 Def 2.7), the Euclidean rotation
    of T05 Prop 7.21. The definition's boost dynamics is tau_t(a_j) = e^{-i omega_j t} a_j in Schwarzschild
    time, a phase rotation of each mode; its rapidity form lambda = kappa t is the same phase flow, not
    the real rotor flow of T08.
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 4
    note: 'The two boost flows: flow_note recorded.'
---

## formal
Fix a countable mode set $J$ with Schwarzschild frequencies $\omega_j > 0$ ($j \in J$), the frequencies the geometry assigns to the boundary modes (Fact \claimref{hawking.imported-modular-descent-premises-geometric-normalisation}). \emph{Provenance of $J$:} the boundary modes are the ladder pairs of the blown-up singular boundary, one per point, aggregated over the s-wave channels into the countable array of Theorem \claimref{singularity.bosonisation-bridge-s-wave-sector}, an identification the singularity paper makes and flags. By convention here (it is in neither the singularity paper nor the thermality paper, and reconciles the array's weights $\kappa k$, $k \in \mathbb{Z}$, with $\omega_j > 0$), the modes below the level enter $J$ through their particle-hole conjugates, so that every frequency is positive, and the one zero-frequency mode of the array lies outside $J$; the bookkeeping is filed alongside (synthesis.s-wave-array-is-a-boundary-mode-set). The tower of iterated completions is the algebra's model, not the source of its countability: its limit is the CAR algebra with the adjoined null pairs as modes (Fact \claimref{hawking.imported-algebra-boundary-modes-car-algebra}), while on the physical closure one ascent completes the description and further rungs lie on shadow walls outside the physical region (Corollary \claimref{tower.answers-iteration-question}). The \emph{boundary-mode algebra} $\mathfrak{A}$ is the CAR algebra over $\ell^2(J)$ (Fact \claimref{hawking.imported-algebra-boundary-modes-car-algebra}), the C*-inductive limit of the \emph{window algebras} $\mathfrak{A}_F$, $F \subset J$ finite, each $\mathfrak{A}_F \cong \End(\Lambda^\bullet \C^F)$ of dimension $4^{|F|}$. The \emph{boost dynamics} is the one-parameter group $\tau_t$ acting on generators by $\tau_t(a_j) = e^{-i\omega_j t}\,a_j$, with $t$ Schwarzschild time: the quasi-free flow whose one-particle Hamiltonian is $h = \mathrm{diag}(\omega_j)$; it preserves every window. In rapidity $\lambda = \kappa t$ the same flow has boost weights $\omega_j/\kappa$ and modular temperature $2\pi$ (Fact \claimref{hawking.imported-modular-descent-premises-geometric-normalisation}); in Schwarzschild time the inverse temperature is $\beta = 1/\TH = 2\pi/\kappa$, and this normalisation is used throughout.

## technical
Fix a countable mode set $J$ with Schwarzschild frequencies $\omega_{j} > 0$. The set $J$ indexes the s-wave aggregate of the ladder pairs of the blown-up singular boundary, one pair per point, as the singularity paper identifies them, with, by this definition's own convention, the modes below the level entering through their particle-hole conjugates and the single zero-frequency mode left outside; the tower of iterated completions supplies the algebra's form, not the count, since the physical closure needs one ascent only. The boundary-mode algebra $\mathfrak{A}$ is the CAR algebra over $\ell^{2}(J)$, the C*-inductive limit of the window algebras $\mathfrak{A}_{F} \cong \End(\Lambda^{\bullet}\C^{F})$ for finite $F \subset J$, each of dimension $4^{|F|}$. The boost dynamics is the quasi-free flow $\tau_{t}(a_{j}) = e^{-i\omega_{j}t}a_{j}$ in Schwarzschild time $t$, with one-particle Hamiltonian $h = \mathrm{diag}(\omega_{j})$; it preserves every window.

In rapidity $\lambda = \kappa t$ the same flow has boost weights $\omega_{j}/\kappa$ and modular temperature $2\pi$; in Schwarzschild time the inverse temperature is $\beta = 1/\TH = 2\pi/\kappa$, the normalisation used throughout.

## lay
This definition sets up the algebra describing a black hole's horizon modes: a collection of fermion modes, each with a frequency fixed by the geometry, built up from finite groups of modes. The modes come from the singularity's boundary, one pair per point, gathered into a countable list by keeping the spherically symmetric part; the tower of repeated completions is used only as a mathematical model of the algebra they form, not as the reason there are countably many. It also fixes how the modes evolve in time, each rotating at its own frequency, and the temperature scale that goes with that evolution.

## one-liner
The boundary-mode algebra is the CAR algebra over a countable mode set, built from finite windows, with boost dynamics $\tau_{t}(a_{j}) = e^{-i\omega_{j}t}a_{j}$ at inverse temperature $\beta = 2\pi/\kappa$.
