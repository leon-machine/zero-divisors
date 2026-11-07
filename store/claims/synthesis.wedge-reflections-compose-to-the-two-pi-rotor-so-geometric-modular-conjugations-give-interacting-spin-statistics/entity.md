---
id: synthesis.wedge-reflections-compose-to-the-two-pi-rotor-so-geometric-modular-conjugations-give-interacting-spin-statistics
kind: claim
version: 4
title: 'Wedge reflections compose to the $2\pi$ rotor; spin-statistics if geometric'
status: proved
region: synthesis
subject: quantum-fields
tags: [modular-theory, car-algebra, superselection, recovers-known-physics]
proposed_by:
  kind: ai
  session: 2026-11-02-qft-full
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: notation pass, imaginary units resolved by the unit principle
  version: 4
  source: maintainer pass 2026-11-07 (resolve units)
review: draft
imported_from:
- citation: 'B. Kuckert, A new approach to spin and statistics, Lett. Math. Phys. 35 (1995), 319--331; arXiv:hep-th/9412130.'
  key: Kuckert1995
  locator: 'Sec. 2, Assumptions I, II (modular P1CT symmetry), III, Definition 2.3; Sec. 3, Corollary 3.2, Theorem 3.4, Corollary 3.5'
  doi: 10.1007/BF00750839
- citation: 'H.-J. Borchers, The CPT-theorem in two-dimensional theories of local observables, Commun. Math. Phys. 143 (1992), 315--332.'
  key: Borchers1992
- citation: 'S. Doplicher and J. E. Roberts, Why there is a field algebra with a compact gauge group describing the superselection structure in particle physics, Commun. Math. Phys. 131 (1990), 51--107.'
  key: DoplicherRoberts1990
- citation: 'J. J. Bisognano and E. H. Wichmann, On the duality condition for quantum fields, J. Math. Phys. 17 (1976), 303--321.'
  key: BW1976
derivations:
- name: main
  uses:
  - synthesis.modular-period-on-values-is-the-dual-plane-turn@3
  - angle.imported-theorems-deliver-their-hypotheses@2
  - synthesis.imported-free-field-spin-statistics-and-guido-longo-theorem@1
  - synthesis.locality-of-the-attached-free-fields-fixes-their-statistics@3
  - synthesis.imported-kuckert-modular-pct-spin-statistics-and-borchers-theorem@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_wedge_reflection_is_conjugation_by_the_boost_bivector
- kind: check
  ref: check.py::check_reflection_reverses_the_edge_translations_and_the_boost_dilates_them
- kind: check
  ref: check.py::check_reflections_of_turned_wedges_compose_to_the_spin_rotor_of_twice_the_turn
- kind: check
  ref: check.py::check_the_klein_twist_with_unit_i4_squares_to_the_grading
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - field-theory.imported-standard-field-theory
  - synthesis.n-plus-null-ground-state
  - synthesis.modular-period-on-values-is-the-dual-plane-turn
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 3 -> 4. Borchers'' relation in the proof of (ii), Delta^{it} U(a) Delta^{-it} = U(e^{-2 pi t} a), is written Delta^{I_4 t}, I_4 the default scalar unit of the abstract Hilbert space (U1) and the unit the entity already uses in (iv), as the restated Kuckert-Borchers Fact has it. Declaration removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (complex-analysis): the proof uses Borchers'' relation Delta^{it}U(a)Delta^{-it} = U(e^{-2 pi t}a), quoted from the imported Fact, for the modular objects of an interacting net on a general Hilbert space.'
  maintainer_pass:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 1 -> 2, by Leon''s list of routine imports of 2 November 2026: a uses edge to the new imported Fact synthesis.imported-kuckert-modular-pct-spin-statistics-and-borchers-theorem@1 (Kuckert 1995, read in the arXiv text; Borchers'' theorem, its relations checked against a review), cited by claimref in the formal level and the proof; Borchers'' conjugation relation, earlier cited from memory, now cites that Fact. The bibliography entries are kept for the locators. Statement, proof steps and check unchanged.'
  open_problem: op.qft-structural-inputs
  note: >-
    The attack line "spin and statistics for interacting fields: replace the Jost-point import by a premise the
    series already holds, or record modular covariance of the wedge algebras as one", nonperturbative side. The
    weakest modular premise known to give the spin-statistics connection is Kuckert's (1995, read in the arXiv
    text): the modular conjugation of the wedge algebra acts on the local algebras as the wedge's P1T
    reflection; full modular covariance (Guido-Longo) implies it. What is written here is the spacetime-algebra form
    of the geometric half of Kuckert's argument: the reflection is conjugation by the wedge's own boost bivector,
    whose factorisation as PT after the dual-plane turn is the stored modular-period result (ii); the reflections
    of the wedge and its quarter-turned copy compose to a rotor of square -1 whatever the signs of the versors
    (along the turned wedges the lift by continuity reaches -1 at the causal complement); and the standard Klein
    twist, written with i = I4, squares to the grading. The positivity the theorem needs is the spectrum
    condition of the interacting net, part of its hypotheses; (N+) is posed for quasi-free states of a CAR mode
    algebra and does not supply it. Under the spectrum condition Borchers' theorem gives the action of the
    modular objects on translations; nothing in the store gives their action on the local algebras, which
    remains the premise; (HS) and (HD) do not bear on it. Kill condition registered before computing: the product of the reflections of W' and W
    not equal to the lift -1 of the 2 pi rotation, or the twist with I4 not squaring to the grading; neither
    fired. Transport-absent: the theorem is standard, and the dual-plane reading and the unit I4 in the twist
    re-express it, as the stored modular-period result classifies its own I4 reading.
  flags:
  - 'Kuckert 1995 read in the arXiv text (ar5iv): assumptions in dimension 1 + s, s >= 2; the conclusion R(2 pi) = k for covariant normal fields (Corollary 3.5) uses twisted duality from Doplicher and Roberts (1990, Theorem 5.4, cited from memory) and a compact internal symmetry group; journal volume and pages from memory'
  - 'Borchers 1992: the modular-group relation is in the stored Fact; the relation J U(a) J = U(-a) for the half-sided translations is cited from memory'
  - 'the field net of the theorem describes charges localisable in double cones or spacelike cones; electric charge, constrained by the Gauss law, is not of this kind, so for charged fields of QED the nonperturbative conclusion needs more than this premise (argued)'
---

## formal
Units and signature of the store; $\Cl(1,3)$, $I_{4} = \gamma_{0}\gamma_{1}\gamma_{2}\gamma_{3}$; $W = \{x : x^{1} > |x^{0}|\}$, its boost bivector $B = \gamma_{0}\gamma_{1}$, edge null directions $n_{\pm} = \pm\gamma_{0} + \gamma_{1}$ and dual plane $D = I_{4}B = \gamma_{2}\gamma_{3}$; $\mathrm{Ad}(V)x = VxV^{-1}$.
\begin{enumerate}
\item[(i)] \emph{(The wedge reflection; proved.)} $B^{2} = 1$, $B\tilde B = -1$, and $\mathrm{Ad}(B)$ is the reflection $j_{W}$: $(x^{0}, x^{1}) \mapsto (-x^{0}, -x^{1})$, $x^{2}$, $x^{3}$ fixed. Since $I_{4}D = -B$, $\mathrm{Ad}(B) = \mathrm{Ad}(I_{4}) \circ \mathrm{Ad}(D)$: the PT inversion after the turn by $\pi$ in the dual plane, which is the half modular period on values by \claimref{synthesis.modular-period-on-values-is-the-dual-plane-turn}(ii). This is the geometric part of the Bisognano-Wichmann conjugation, CPT composed with the turn by $\pi$ about the boost axis (Fact \claimref{angle.imported-theorems-deliver-their-hypotheses}).
\item[(ii)] \emph{(Edge translations; geometric part proved, modular action imported.)} $j_{W}$ reverses $n_{\pm}$ and fixes $\gamma_{2}$, $\gamma_{3}$; the wedge's boosts map $W$ into itself and dilate $n_{\pm}$ by reciprocal factors ($(5 + 4B)/3$: $n_{+} \mapsto n_{+}/9$, $n_{-} \mapsto 9n_{-}$). Under the spectrum condition, Borchers' theorem (Fact \claimref{synthesis.imported-kuckert-modular-pct-spin-statistics-and-borchers-theorem}(ii)) gives that the modular group of every wedge algebra (with the vacuum cyclic and separating) acts on the translations as the wedge's boosts at rapidity $-2\pi t$ and its modular conjugation as $j_{W}$, for interacting nets as well.
\item[(iii)] \emph{(Turned wedges; proved.)} Independently of signs: for $B_{\pi/2} = \gamma_{0}\gamma_{2}$, the reflection versor of the quarter-turned wedge, $(\pm B_{\pi/2}\cdot\pm B)^{2} = -1$, so the two reflections compose to a rotor representing the half turn whose square is the rotation by $2\pi$ in the spin group. For the wedge $W_{\theta}$ turned by $\theta$ in the plane $\gamma_{1}\gamma_{2}$, $B_{\theta} = \gamma_{0}(\cos\theta\,\gamma_{1} + \sin\theta\,\gamma_{2})$ and $B_{\theta}B = \cos\theta + \sin\theta\,\gamma_{1}\gamma_{2}$, the spin rotor of the turn by $2\theta$; $\theta \mapsto B_{\theta}B$ runs from $1$ to $-1$ on $[0, \pi]$, $W_{\pi} = W'$ and $B_{\pi} = -B$. As maps $\mathrm{Ad}(B_{\pi}) = \mathrm{Ad}(B)$; the sign $B_{\pi} = -B$ is the lift by continuity along $\theta$, and along that lift the product of the reflection versors of $W'$ and $W$ is the rotation by $2\pi$ of the spin group, $-1$ on spinor values and $(-1)^{2s}$ on spin-$s$ values.
\item[(iv)] \emph{(The twist with $i = I_{4}$; proved, the standard Klein-twist identity with $i$ written as $I_{4}$.)} For an even involution $k$ commuting with $I_{4}$, $V = (1 + I_{4}k)(1 + I_{4})^{-1}$ satisfies $VV^{*} = 1$, $Vk = kV$, $V^{2} = k$, and a conjugate-linear $J$ reversing $I_{4}$ and fixing $k$ has $JV^{*}J = V$, so $VJV^{*}J = k$.
\item[(v)] \emph{(Spin-statistics; imported, conditional.)} If the spectrum condition holds and the modular conjugation of the wedge algebra of the observables acts on the local algebras as $j_{W}$ (modular P1CT symmetry), with covering-group covariance, the spectrum condition, a unique vacuum, dimension at least $1 + 2$ and a compact group of internal symmetries, then for every covariant normal field the rotation by $2\pi$ equals the Bose-Fermi grading, $R(2\pi) = J_{W'}J_{W} = VJV^{*}J = k$ (Fact \claimref{synthesis.imported-kuckert-modular-pct-spin-statistics-and-borchers-theorem}(i), \cite{Kuckert1995}, Corollaries 3.2 and 3.5; there twisted duality is derived, from \cite{DoplicherRoberts1990}, not assumed); (iii) is the geometric step and (iv) the algebraic step in the spacetime algebra. Modular covariance (Fact \claimref{synthesis.imported-free-field-spin-statistics-and-guido-longo-theorem}(iii)) implies the premise.
\item[(vi)] \emph{(What remains; argued.)} The spectrum condition, a hypothesis of the theorem, gives by (ii) the action of the modular objects on translations; (N$_{+}$) is posed for quasi-free states of a CAR mode algebra (\claimref{synthesis.positive-null-energy-gives-r-premises}) and does not supply the spectrum condition of an interacting net. Nothing in the store gives the action of the modular conjugations on the local algebras, which is the remaining premise for interacting fields; (HS) and (HD) do not bear on it. Electric charge is not localisable in spacelike cones, so for the charged fields of QED the conclusion needs more than this premise.
\end{enumerate}

## technical
The geometric side of the modular route to spin and statistics has a short form in the spacetime algebra. The reflection of a wedge, which reverses time and the wedge's spatial direction, is conjugation by the wedge's own boost bivector $B$; by the stored dual-plane result it is the PT inversion after the half modular period on values. The reflections of a wedge and of its quarter-turned copy compose, whatever signs the versors carry, to a rotor whose square is $-1$, the rotation by $2\pi$ in the spin group; along the turned wedges the product is $\cos\theta + \sin\theta\,\gamma_{1}\gamma_{2}$, whose lift by continuity reaches $-1$ at the causal complement. With $i = I_{4}$ the Klein twist $V = (1 + I_{4}k)/(1 + I_{4})$ squares to the grading $k$. These are the two steps of Kuckert's theorem (standard): if each wedge's modular conjugation acts on the local algebras as the wedge's reflection, a premise weaker than modular covariance, then the rotation by $2\pi$ is the grading for interacting fields.

The spectrum condition, a hypothesis of that theorem, gives through Borchers' theorem the action of the modular objects on translations; the reflection reverses the edge's null translations and the boosts dilate them. Nothing in the store gives their action on the local algebras, which is what remains; the null ground-state premise of the horizons is posed for free (quasi-free) states and does not supply the spectrum condition of an interacting net. It does not reach electric charge, which the Gauss law keeps out of spacelike cones.

## lay
One way to explain why matter particles obey the exclusion rule and force particles do not uses a natural flow of the vacuum restricted to a wedge-shaped region of spacetime. In the series' algebra, the mirror image of such a wedge is a single algebraic element, the wedge's own boost plane, and mirroring twice in wedges turned by half a turn gives a full turn, which for a spin-one-half value is a sign change. If the vacuum's natural mirror operation matches the geometric mirror on every region, the spin rule follows for interacting particles. Positive energy gives that match for shifts along light rays, not for every region, and nothing in the series gives it for regions, so that match remains an assumption.

## one-liner
The wedge reflection is $\mathrm{Ad}(B)$, PT after the half modular period; the reflections of a wedge and its quarter-turned copy compose, for either signs of the versors, to a rotor of square $-1$ (the $2\pi$ rotation in the spin group); the $I_{4}$ twist squares to the grading; so under the spectrum condition, geometric wedge modular conjugations (weaker than modular covariance) give interacting spin-statistics by Kuckert's theorem, and nothing in the store supplies their action on the local algebras.
