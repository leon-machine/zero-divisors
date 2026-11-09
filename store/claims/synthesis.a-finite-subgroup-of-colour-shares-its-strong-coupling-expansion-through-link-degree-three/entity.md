---
id: synthesis.a-finite-subgroup-of-colour-shares-its-strong-coupling-expansion-through-link-degree-three
kind: claim
version: 1
title: 'A finite subgroup of colour shares the strong-coupling expansion to link degree three'
status: proved
region: synthesis
subject: quantum-fields
tags: [gauge-fields, rotors-and-stabilisers, finite-models, no-go, recovers-known-physics]
proposed_by:
  kind: ai
  session: 2026-11-08-colour-lattice
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: run 2026-11-08-colour-lattice
review: draft
about:
- obj.field-theory.single-algebra-field
derivations:
- name: main
  uses:
  - standard-model.gauge-algebra-minimal-massive-composite@4
  - synthesis.imported-wilson-lattice-gauge-theory-and-strong-coupling-confinement@1
  - synthesis.weak-factor-rotor-lattice-strong-coupling-area-law@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_colour_block_su3_and_the_finite_group_inside_it
- kind: check
  ref: check.py::check_finite_group_averages_equal_haar_through_degree_three
- kind: check
  ref: check.py::check_degree_four_separates_them_by_a_centre_violating_moment
- kind: check
  ref: check.py::check_gluing_rule_and_own_plaquette_loop_terms_agree
- kind: check
  ref: check.py::check_plaquette_series_agrees_through_beta_squared_and_differs_at_beta_cubed
- kind: check
  ref: check.py::check_finite_plaquette_weight_has_a_gap_and_colour_has_none
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.weak-factor-rotor-lattice-strong-coupling-area-law
  - synthesis.non-abelian-gauge-fixing-has-gribov-copies-and-the-weak-rotor-lattice-with-doublets-has-a-perimeter-law
  - synthesis.one-loop-running-coefficients-from-spacetime-algebra-spin-traces
  - synthesis.field-level-brst-differential-of-the-derived-gauge-fields-is-nilpotent
extraction:
  open_problem: op.qft-non-abelian-gauge-fields
  note: >-
    Bears on the attack item on colour (a colour rotor lattice and its continuum limit; pure-colour confinement is
    the Yang-Mills mass-gap problem and is not addressed): it states exactly how far the strong-coupling
    expansion of a colour lattice sees the group SU(3) through link degree three. Established exactly: the colour
    group realised in the e3..e8 block of Cl(9,0) as the rotations commuting with J = e34 + e56 + e78 and fixing
    the real part of the J-complex volume trivector (its Lie algebra, the eight su(3) bivectors, computed); a
    finite subgroup of order 96, the J-commuting signed permutations of e3..e8 fixing that trivector, each the
    action of a rational even versor, irreducible on the J-complex three-space (commutant span{1, j}) and so with
    trivial centre by Schur's lemma (the group known as Delta(96) in the flavour-symmetry literature); its averages
    equal the Haar averages of SU(3) on every link polynomial of degree at most three, derived by showing that its
    invariant tensors in degrees one to three are exactly the su(3)-annihilated ones (no Haar moment imported),
    and differ in degree four (20 invariants against 12, including a moment the centre of SU(3) forbids, the
    fourth power of the complex trace, average 1 against 0). Consequences: the gluing rule (1/3) for J-linear
    insertions, the term (beta/18)^A that a rectangle's own plaquettes contribute to its fundamental loop
    (beta = 6/g^2; the leading term for SU(3), by its centre; for the finite group, which has no centre, not shown
    to be leading), the tube terms of plaquette correlators, and the plaquette expectation beta/18 + beta^2/216
    are the same for the finite group and for SU(3); the plaquette differs first at beta^3 (0 against 1/972).
    Reading (argued): strong-coupling terms of this kind do not distinguish SU(3) from a finite group without
    centre whose weight is gapped at the identity (no continuum limit; a perimeter-law phase at weak coupling by
    the standard low-temperature argument for finite gauge groups, cited from memory, not imported); with the
    stored compact U(1) comparison (same form, massless at weak coupling, imported) they are no evidence of
    confinement or of a continuum mass gap. Store survey (a statement about the store's contents when this entity
    was written, not about the finite group, and not tracked by its derivation): no stored premise gives the gauge
    field a lattice spacing on flat spacetime (the completion premise F4 makes the coefficients real; P2's
    finiteness declaration concerns the descent's deposited mode set; the cells of C2 lie on the stretched
    singularity as a Schwarzschild calibration; R2's unit is a tower radius; a finite floor of the tower keeps no
    boost; the induced Newton coupling needs a cut-off the store does not fix), and no stored gap (the tower
    pairing gap, the two-species doublet pair mode, the window Sugawara density waves, which are gapless, the free
    gluons at null momenta) is a spectral gap of the four-dimensional gauge field. The SU(3) leading-order statements ((beta/18)^A with no lower term by the centre, the Polyakov lines, the tube) are in synthesis.colour-centre-flux-bounds-polyakov-lines-and-the-leading-glueball-tube, which derives the same degree-three lemma; string breaking with colour triplets is in synthesis.colour-triplets-give-the-fundamental-colour-loop-a-perimeter-law-at-strong-coupling. Prior art: Wilson 1974; Drouffe and
    Zuber's review of strong-coupling expansions (character expansion, closed surfaces); Creutz and Muenster on
    SU(N) strong coupling; finite subgroups of SU(3) as approximations of the gauge group (Bhanot and Rebbi,
    Phys. Rev. D 24 (1981) 3319), and of SU(2) (Petcher and Weingarten, Phys. Rev. D 22 (1980) 2465); otherwise
    cited from memory. Transport-absent.
---

## formal
Let $V$ be the span of $e_{3}, \dots, e_{8}$ in $\Cl(9,0)$, $J = e_{34} + e_{56} + e_{78}$, and $j(v) = v\cdot J$ the complex structure ($e_{3} \mapsto e_{4}$, $e_{4} \mapsto -e_{3}$, and so on), with $\mathrm{Re}\,\Omega = e_{357} - e_{368} - e_{458} - e_{467}$ and $\mathrm{Im}\,\Omega = e_{457} + e_{367} + e_{358} - e_{468}$, the real and imaginary parts of the $J$-complex volume form on the frame $e_{3}, e_{5}, e_{7}$. Let $SU(3)$ be the group of rotations of $V$ that commute with $j$ and fix $\mathrm{Re}\,\Omega$ (for a $j$-linear rotation, fixing $\mathrm{Re}\,\Omega$ is unit $J$-determinant), with Haar measure $dU$, and let $G$ be its subset of signed permutations of $e_{3}, \dots, e_{8}$. For a link $U$ write $\mathrm{tr}\,U = \sum_{a}e_{a}\cdot U(e_{a})$ (twice the real part of the $J$-complex trace) and $\chi(U) = \tfrac16\mathrm{tr}\,U$; the lattice weight is $\prod_{p}\exp(\beta\chi(U_{p}))$, $\beta = 6/g^{2}$, as in Fact \claimref{synthesis.imported-wilson-lattice-gauge-theory-and-strong-coupling-confinement}(i).
\begin{enumerate}
\item[(i)] \emph{(The colour group and a finite subgroup; computed.)} The bivectors of $V$ commuting with $J$ and with $\mathrm{Re}\,\Omega$ form an eight-dimensional Lie algebra orthogonal to $J$, the $\mathfrak{su}(3)$ summand of Theorem \claimref{standard-model.gauge-algebra-minimal-massive-composite}. $G$ is a group of order $96$; each element is $v \mapsto RvR^{-1}$ for a rational even versor $R$ with $RJR^{-1} = J$ and $R\,\mathrm{Re}\,\Omega\,R^{-1} = \mathrm{Re}\,\Omega$. The linear maps of $V$ commuting with $G$ are the span of $1$ and $j$, so $G$ is irreducible on the $J$-complex three-space and its central elements have the form $a + bj$; the only such element of $G$ is $1$, so its centre is trivial. The centre of $SU(3)$ is $\{1, \omega, \omega^{2}\}$, $\omega = -\tfrac12 + \tfrac{\sqrt3}{2}j$.
\item[(ii)] \emph{(Equal averages through degree three; proved.)} For $k = 1, 2, 3$ the $G$-invariant subspace of $V^{\otimes k}$ is the $SU(3)$-invariant one: $0$; the span of the metric and the form of $J$; the span of $\mathrm{Re}\,\Omega$ and $\mathrm{Im}\,\Omega$. Hence $\int f(U)\,dU = \tfrac{1}{96}\sum_{g \in G}f(g)$ for every polynomial $f$ of degree at most three in the components of $U$, and, for finitely many independent links, for every polynomial of degree at most three in each link.
\item[(iii)] \emph{(Degree four separates them; computed.)} In $V^{\otimes 4}$ the invariants have dimension $12$ for $SU(3)$ and $20$ for $G$. The derivation of $J$ vanishes on the $SU(3)$-invariants and has eigenvalues $\pm 4$ times the unit of $J$ on a two-dimensional part of the $G$-invariants, on which $\omega$ would act by $\omega^{\pm 4} \neq 1$: for the $J$-complex trace $t$, $\tfrac{1}{96}\sum_{G}t^{4} = 1$ while $\int t^{4}\,dU = 0$; and $\tfrac{1}{96}\sum_{G}(\mathrm{tr}\,U)^{4} = 20$ against $\int(\mathrm{tr}\,U)^{4}dU = 12$.
\item[(iv)] \emph{(Shared strong-coupling data; proved, sampled for the loops.)} For $j$-linear $X$, $Y$, $\int\mathrm{tr}(XU)\,dU = 0$ and $\int\mathrm{tr}(XU)\,\mathrm{tr}(U^{-1}Y)\,dU = \tfrac13\mathrm{tr}(XY)$, and the same over $G$. So every term of the strong-coupling expansion (the expansion of $\prod_{p}\exp(\beta\chi(U_{p}))$ in powers of $\beta$) whose integrand has degree at most three in each link has the same value for $G$ and for $SU(3)$. In particular, for every $R \times T$ rectangular fundamental loop $C$ the term of order $\beta^{RT}$ in $\langle\chi(U_{C})\rangle$ from the $RT$ plaquettes of the rectangle is $(\beta/18)^{RT}$ for both (summed over $G$ for $1 \times 1$ and $2 \times 1$); for $SU(3)$ it is the leading term, by its centre, while for $G$, which has no centre, it is not shown to be leading; and the term of a connected plaquette correlator from a tube of plaquettes joining the two, each to first order, has degree two on every link and agrees.
\item[(v)] \emph{(The plaquette; proved.)} With $z(\beta) = \int\exp(\beta\chi(U))\,dU$ (for $G$, the average over $G$), $(\ln z)'(\beta) = \kappa_{2}\beta + \tfrac12\kappa_{3}\beta^{2} + \tfrac16\kappa_{4}\beta^{3} + O(\beta^{4})$, $\kappa_{n}$ the cumulants of $\chi$: $\tfrac{\beta}{18} + \tfrac{\beta^{2}}{216} + 0\cdot\beta^{3}$ for $SU(3)$ and $\tfrac{\beta}{18} + \tfrac{\beta^{2}}{216} + \tfrac{\beta^{3}}{972}$ for $G$. On the hypercubic lattice of dimension at least three $\langle\chi(U_{p})\rangle = (\ln z)'(\beta) + O(\beta^{5})$ for both, the first closed surface being the boundary of an elementary cube (standard).
\item[(vi)] \emph{(A gapped finite weight; computed.)} $\chi(g) \le \tfrac13$ for every $g \neq 1$ in $G$, while on $SU(3)$ the rational elements $\mathrm{diag}(z, \bar z, 1)$, $z = ((n^{2} - 1) + 2nj)/(n^{2} + 1)$, have $1 - \chi = 4/(3(n^{2} + 1))$.
\end{enumerate}
\emph{Reading (argued).} No term of the colour lattice's strong-coupling expansion that uses link moments of degree at most three (the term of every rectangle from its own plaquettes, the plaquette through $\beta^{2}$, and the tube terms of plaquette correlators from which the leading strong-coupling glueball decay rate is read) distinguishes $SU(3)$ from $G$, a finite group without centre whose weight is gapped at the identity, so that its plaquettes freeze at weak coupling and it has no continuum limit. For $G$ a fundamental line can end on sheets through the degree-four invariant of (iii), so its large loops need not follow the rectangle's own term. With the stored comparison with compact $U(1)$ (same form, \claimref{synthesis.weak-factor-rotor-lattice-strong-coupling-area-law}(vi); deconfined and massless at weak coupling, Fact \claimref{synthesis.imported-wilson-lattice-gauge-theory-and-strong-coupling-confinement}(iv)), strong-coupling terms of this kind are not evidence of confinement or of a mass gap in the continuum, which needs $\beta \to \infty$ and asymptotic freedom (the sign of the stored one-loop colour coefficient). The Yang-Mills mass-gap problem is not addressed.

## technical
The strong-coupling expansion of a lattice gauge theory computes its coefficients from averages of products of link variables over the gauge group. In the colour block of the series' algebra, the six vectors $e_{3}, \dots, e_{8}$ with the complex structure $J = e_{34} + e_{56} + e_{78}$, the colour group is the set of rotations commuting with $J$ that fix the real part of the $J$-complex volume trivector; its Lie algebra is the eight $\mathfrak{su}(3)$ bivectors. Inside it the $J$-commuting signed permutations of the six vectors that fix that trivector form a finite group of order 96, each element the action of a rational versor; it is irreducible on the complex three-space, so by Schur's lemma its centre consists of complex scalars, and it has none but $1$. Its averages agree exactly with the colour group's Haar averages for every polynomial of degree at most three in a link, which is shown without importing any Haar integral: in degrees one to three its invariant tensors are exactly those the $\mathfrak{su}(3)$ bivectors annihilate (the metric and the form of $J$; the real and imaginary volume trivectors). So every strong-coupling term with each link to degree at most three is the same for both groups: the gluing factor $\tfrac13$, the term $(\beta/18)^{A}$ that a rectangle's own plaquettes contribute to its fundamental Wilson loop with $\beta = 6/g^{2}$ (the leading term for the colour group, by its centre; for the finite group, which has no centre, not shown to be leading), the tube terms of plaquette correlators, and the plaquette average $\beta/18 + \beta^{2}/216$. They first differ in degree four, where the finite group has twenty invariants against twelve, including the fourth power of the complex trace, which the colour group's centre forbids; the plaquette average then differs at $\beta^{3}$. The finite group's weight is gapped at the identity. As a reading (argued): the finite group freezes at weak coupling and has no continuum limit, so, with compact $U(1)$, already stored as sharing the form of the area law and known to be massless at weak coupling, strong-coupling terms of this kind decide neither confinement nor a mass gap in the continuum. Transport-absent.

## lay
A standard way to study the strong nuclear force is to put it on a grid and expand in powers of a small number valid when the force is very strong. This result shows, exactly, that many of the first terms of that expansion are the same for the true symmetry of the strong force and for a finite group of 96 discrete rotations that sits inside it. The finite version behaves very differently when the force is weak: it freezes and has no smooth limit. So these terms cannot tell whether the real force confines quarks or produces a mass gap, which is a famous unsolved problem that this result does not touch.

## one-liner
In the colour block of $\Cl(9,0)$ the $J$-commuting signed permutations of $e_{3}, \dots, e_{8}$ fixing the $J$-volume trivector form a finite subgroup of $SU(3)$ of order 96 with trivial centre (Schur) whose averages equal the Haar averages on every link polynomial of degree at most three (derived from invariant tensors) and differ in degree four (a centre-forbidden moment); so every strong-coupling term of link degree at most three is the same for both: the gluing factor $\tfrac13$, the term $(\beta/18)^{A}$ from a rectangle's own plaquettes ($\beta = 6/g^{2}$; leading for $SU(3)$ by its centre, not shown leading for the finite group), the tube terms of plaquette correlators and the plaquette $\beta/18 + \beta^{2}/216$, while the plaquette differs first at $\beta^{3}$ ($0$ against $\tfrac1{972}$); the finite weight is gapped at the identity; as a reading, such terms do not distinguish $SU(3)$ from a group without centre that freezes at weak coupling; the mass-gap problem is not addressed; transport-absent.
