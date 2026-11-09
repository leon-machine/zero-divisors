---
id: synthesis.colour-triplets-give-the-fundamental-colour-loop-a-perimeter-law-at-strong-coupling
kind: claim
version: 1
title: 'Colour triplets give the fundamental colour loop a perimeter law at infinite coupling'
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
  - synthesis.non-abelian-gauge-fixing-has-gribov-copies-and-the-weak-rotor-lattice-with-doublets-has-a-perimeter-law@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_colour_moments_of_a_matrix_entry_from_invariants
- kind: check
  ref: check.py::check_frozen_triplet_mean_link_is_rank_one_and_its_coefficient
- kind: check
  ref: check.py::check_wilson_quark_corner_factor_is_independent_of_the_rectangle
- kind: check
  ref: check.py::check_quark_loop_gives_the_rectangle_a_perimeter_term_at_beta_zero
- kind: check
  ref: check.py::check_spinor_ideal_and_its_complex_unit
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.non-abelian-gauge-fixing-has-gribov-copies-and-the-weak-rotor-lattice-with-doublets-has-a-perimeter-law
  - synthesis.one-loop-running-coefficients-from-spacetime-algebra-spin-traces
  - synthesis.imported-singer-gauge-slice-neuberger-lattice-brst-and-fradkin-shenker-complementarity
extraction:
  open_problem: op.qft-non-abelian-gauge-fields
  note: >-
    Bears on the attack item on colour: what separates a colour lattice with the series' matter from the
    pure Yang-Mills mass-gap problem. The series' colour sector carries colour triplets (the quarks of n_g
    generations, n_g = 3 in the stored running coefficients), and the mass-gap problem concerns pure Yang-Mills.
    Established exactly, at infinite gauge coupling (beta = 0), in the colour block of Cl(9,0) (SU(3) = rotations
    of e3..e8 commuting with J = e34 + e56 + e78 and fixing the real J-volume trivector): (1) with a frozen colour
    triplet, a unit vector at each site with hopping kappa, every closed path of P distinct links has
    <chi(U_C)> = c(kappa)^P / 3 exactly; the mean link is c(kappa) times the projector onto the J-complex line of
    the triplet's direction, rank one, not a scalar as for the weak doublet, because the triplet's stabiliser is an
    SU(2) that leaves two colour directions unbroken; c = kappa/6 - kappa^3/288 + O(kappa^5), from Haar moments
    derived as invariant tensors (the fourth moment 1/16 is derived on the su(3)-annihilated invariants, which the
    order-96 subgroup does not reproduce); (2) with n_f flavours of Wilson quarks (r = 1) the leading term of
    every rectangular fundamental loop in the hopping expansion is (n_f/6)(2 kappa)^P, P the perimeter: the spin
    trace of the quark loop is -2^(P-1) for every rectangle and both orientations, computed as four times the
    scalar part in Cl(4,0) with hop factors 1 - d_mu and 1 + d_mu. So at beta = 0 with colour triplets the
    fundamental loop has a perimeter law (exactly for frozen triplets, at leading hopping order for quarks) and is
    no confinement criterion, as the stored perimeter law with the
    weak doublets; this is the colour analogue of that result, and complementarity for fundamental Higgs fields
    (Fradkin-Shenker, imported in the store's Fact on Singer, Neuberger and Fradkin-Shenker, cited here in prose) is
    the general statement for scalars; for quarks it is argued. The same finite group of order 96 and its degree-four invariants are stored in synthesis.a-finite-subgroup-of-colour-shares-its-strong-coupling-expansion-through-link-degree-three (iii); the pure-colour strong-coupling statements (centre bound, Polyakov lines, tube) are in synthesis.colour-centre-flux-bounds-polyakov-lines-and-the-leading-glueball-tube. The quark fields
    are Grassmann variables integrated to the determinant of the hopping operator, whose logarithm is expanded
    in closed loops (standard); this step is the one outside geometric algebra. Prior art: Wilson fermions with r = 1
    and the hopping expansion, attributed to Wilson's 1975 Erice lectures (cited from memory, not verified at
    source), the string-breaking and hopping-parameter literature (for example Montvay and Muenster's
    textbook), cited from memory. Transport-absent.
outside_ga:
  kind: other
  why: 'The quark fields of clause (ii) are Grassmann variables; their integral is the determinant of the hopping operator on spinor-colour space, expanded in closed loops as in the standard hopping expansion. The spin factors themselves are products of vectors of Cl(4,0) with the spinor trace written as four times the scalar part, and the colour factors are traces of rotations of the colour block. The complex unit of the spinor module is named as a geometric-algebra element: the spinors are the minimal left ideal Cl(4,0)f, f = (1 + d1d2d3d4)/2, with complex structure right multiplication by d1d2 (it commutes with the left action and squares to -1), and spinor-colour space is the tensor product over span{1, j} with this unit identified with j on colour; the spin traces used are real (the trace of left multiplication by a product of hop factors through d1d2 vanishes, checked), so the complex trace is half the real trace on the ideal, four times the scalar part.'
---

## formal
Let $V$, $J$, $j$, $\mathrm{Re}\,\Omega$, $SU(3)$ (the rotations of $V$ commuting with $j$ and fixing $\mathrm{Re}\,\Omega$, the $\mathfrak{su}(3)$ factor of Theorem \claimref{standard-model.gauge-algebra-minimal-massive-composite}), $\mathrm{tr}\,U = \sum_{a}e_{a}\cdot U(e_{a})$ and $\chi = \tfrac16\mathrm{tr}$ be as in the colour block of $\Cl(9,0)$ ($V = \mathrm{span}(e_{3}, \dots, e_{8})$, $J = e_{34} + e_{56} + e_{78}$), with Haar measure on each link, at infinite gauge coupling ($\beta = 0$ in the weight of Fact \claimref{synthesis.imported-wilson-lattice-gauge-theory-and-strong-coupling-confinement}(i)). Write $x = e_{3}\cdot U(e_{3})$ and $\Pi$ for the orthogonal projector onto $\mathrm{span}(e_{3}, e_{4})$.
\begin{enumerate}
\item[(i)] \emph{(Haar moments of an entry; computed.)} $\int x^{2}\,dU = \tfrac16$, $\int x^{4}\,dU = \tfrac1{16}$, $\int U\,x\,dU = \tfrac16\Pi$ and $\int U\,x^{3}\,dU = \tfrac1{16}\Pi$, obtained from the invariant tensors of degrees two and four (the fourth moment is not reproduced by the order-$96$ subgroup of $J$-commuting signed permutations, which gives $\tfrac16$).
\item[(ii)] \emph{(A frozen triplet; proved.)} Give each site a unit vector $\varphi_{x} \in V$ (Haar measure on the unit sphere) and the weight $\prod_{\ell}\exp(\kappa\,\varphi_{x}\cdot U_{\ell}(\varphi_{y}))$. For every closed path $C$ that uses $P$ distinct links once each, $\langle\chi(U_{C})\rangle = \tfrac13c(\kappa)^{P}$ exactly, with $c(\kappa) = \int x\,e^{\kappa x}dU/\int e^{\kappa x}dU = \tfrac{\kappa}{6} - \tfrac{\kappa^{3}}{288} + O(\kappa^{5})$, positive for $\kappa > 0$; the mean link in the unitary gauge $\varphi = e_{3}$ is $c(\kappa)\Pi$, of rank one over the $J$-complex numbers. At $\kappa = 0$ every such loop vanishes.
\item[(iii)] \emph{(Wilson quarks; proved.)} Let $n_{f}$ flavours of colour-triplet quarks carry the hopping operator $H$ with factor $(1 - d_{\mu})U_{\ell}$ for a hop along $+\mu$ and $(1 + d_{\mu})U_{\ell}^{-1}$ along $-\mu$, $d_{1}, \dots, d_{4}$ the vectors of $\Cl(4,0)$, the spinor trace being four times the scalar part, and the weight $\det(1 - \kappa H)^{n_{f}}$. For every closed rectangle with sides along $d_{\mu}$, $d_{\nu}$ and perimeter $P$, the spin trace of the product of hop factors round it is $-2^{P - 1}$ in either orientation, and the leading term of $\langle\chi(U_{C})\rangle$ in $\kappa$ for every $R \times T$ rectangular fundamental loop is $\tfrac{n_{f}}{6}(2\kappa)^{P}$, $P = 2(R + T)$.
\end{enumerate}
So at $\beta = 0$ a frozen colour triplet gives every simple loop exactly a perimeter law, and Wilson quarks give every rectangle a leading hopping term of perimeter form. (Argued:) at small $\beta > 0$ the perimeter term exceeds the area-law term $(\beta/18)^{RT}$ for large loops; this compares leading terms only and is not a bound on the full expectation.
\emph{Reading (argued).} With colour triplets the fundamental Wilson loop is no criterion of confinement for colour, as \claimref{synthesis.non-abelian-gauge-fixing-has-gribov-copies-and-the-weak-rotor-lattice-with-doublets-has-a-perimeter-law}(iv) found for the weak factor with doublets. The series' colour sector carries quark triplets ($n_{g}$ generations, an input of the stored one-loop running coefficients, $3$ at the imported values), so its physical colour question is the one with quarks, while the Yang-Mills mass-gap problem concerns the pure gauge field; nothing here addresses it.

## technical
At infinite gauge coupling a lattice gauge theory without matter has every Wilson loop zero, and the leading strong-coupling term of the fundamental loop is an area law. In the colour block of the series' algebra, with the colour group the rotations of $e_{3}, \dots, e_{8}$ that commute with $J = e_{34} + e_{56} + e_{78}$ and fix the real $J$-volume trivector, two kinds of colour-triplet matter change this exactly. A frozen triplet, a unit vector at each site with hopping strength $\kappa$, gives every closed path of $P$ distinct links at infinite coupling the expectation $c(\kappa)^{P}/3$, exactly a perimeter law, with $c = \kappa/6 - \kappa^{3}/288 + \dots$; unlike the weak doublet, whose mean link is a multiple of the identity, the triplet's mean link is a multiple of the projector onto one complex colour direction, because a triplet leaves an $SU(2)$ of colour unbroken. The colour averages are derived as invariant tensors of the colour block, the fourth moment included. Dynamical quarks, as Wilson fermions with hop factors $1 \mp d_{\mu}$ in the spacetime algebra of four Euclidean directions, give every rectangular fundamental loop at infinite coupling the leading term $(n_{f}/6)(2\kappa)^{P}$ in the hopping parameter, of perimeter form at leading hopping order: along each side the hop factors are idempotent up to a factor two, and the four corners give the same spin trace for every rectangle. So with colour triplets the fundamental loop is no confinement criterion at infinite coupling, as with the doublets in the weak factor. As a reading (argued): since the series has quarks, its physical colour question is the one with quarks, not the pure Yang-Mills mass-gap problem, which is not addressed. Transport-absent.

## lay
On a lattice, the usual sign of quark confinement is that a loop of colour field lines costs energy in proportion to the area it encloses. This result shows, exactly and in the series' own algebra, that once particles carrying colour are present, the cost at infinite coupling grows only with the loop's length: exactly for colour charges fixed in place, and at the leading order of the expansion in the quarks' hopping for moving quarks; the field line can break by creating a quark pair. Since the series contains quarks, this test of confinement, on this reading, does not apply to it directly. The famous open problem about a mass gap concerns the force field without quarks and is not touched here.

## one-liner
At infinite colour coupling, with links the rotations of $e_{3}, \dots, e_{8}$ commuting with $J$ and fixing the $J$-volume trivector: a frozen colour triplet gives every closed path of $P$ distinct links $\langle\chi(U_{C})\rangle = c(\kappa)^{P}/3$ exactly, $c = \kappa/6 - \kappa^{3}/288 + \dots$, with a rank-one mean link (an unbroken $SU(2)$, unlike the weak doublet), and $n_{f}$ flavours of Wilson quarks give every rectangle the leading hopping term $(n_{f}/6)(2\kappa)^{P}$ (spin trace $-2^{P-1}$ in $\Cl(4,0)$); so at infinite coupling the fundamental loop has a perimeter law with colour triplets (exactly when frozen, at leading hopping order for quarks) and is no confinement criterion; the pure Yang-Mills mass gap is not addressed; transport-absent.
