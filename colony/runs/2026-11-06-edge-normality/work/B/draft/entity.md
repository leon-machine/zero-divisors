---
id: synthesis.modular-data-on-a-generator-fix-neither-the-translation-lift-nor-the-sign-of-i
kind: claim
version: 1
title: 'Modular data on a generator fix neither the translation lift nor the sign of i'
status: proved
region: synthesis
subject: thermality
tags: [thermal-premises, horizons, modular-theory, car-algebra, forcing-and-uniqueness, no-go, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-06-edge-normality
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: run 2026-11-06-edge-normality
review: draft
about:
- obj.hawking.continuum-mode-space
imported_from:
- citation: 'D. Buchholz, M. Florig and S. J. Summers, An algebraic characterization of vacuum states in Minkowski space. II. Continuity aspects, Lett. Math. Phys. 49 (1999), 337--350; arXiv:math-ph/9909003.'
  key: BuchholzFlorigSummers1999
  locator: 'Sec. 2, the Condition of Geometric Modular Action (a)-(d), a condition on the wedge algebras as sets; Prop. 3.5 (CGMA gives continuous translations); Prop. 3.6 (CGMA and Modular Stability give sp U in the closed forward cone or in its negative); the remark that CGMA alone does not give a ground state. Statements checked against the arXiv text; journal pages not checked.'
- citation: 'D. Buchholz and S. J. Summers, An algebraic characterization of vacuum states in Minkowski space, Commun. Math. Phys. 155 (1993), 449--458.'
  key: BuchholzSummers1993
  locator: 'origin of the Condition of Geometric Modular Action (last section), as cited in BuchholzFlorigSummers1999; not read directly'
derivations:
- name: main
  uses:
  - synthesis.positive-null-energy-gives-r-premises@4
  - angle.imported-theorems-deliver-their-hypotheses@1
  - synthesis.imported-powers-stormer-takesaki-disjointness@2
  - singularity.modular-theory-matrix-factor-proved-outright@4
  - synthesis.wedge-reflections-compose-to-the-two-pi-rotor-so-geometric-modular-conjugations-give-interacting-spin-statistics@2
  - synthesis.microlocal-condition-on-a-generator-gives-the-local-null-ground-state@4
  - synthesis.normality-on-the-closed-generator-gives-the-vacuum-folium-not-the-ground-state@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_polar_part_gives_the_modular_conjugation
- kind: check
  ref: check.py::check_fermi_sea_is_a_local_gauge_transform_of_the_vacuum
- kind: check
  ref: check.py::check_hankel_phases_of_the_vacuum_and_the_filled_sea
- kind: check
  ref: check.py::check_lift_and_sign_data_in_geometric_algebra
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.n-plus-null-ground-state
  - synthesis.thermality-of-every-future-half-generator-fixes-the-period-and-the-null-ground-state
  - synthesis.local-normality-at-the-edge-gives-the-null-ground-state
outside_ga:
  kind: complex-analysis
  why: 'Tomita-Takesaki modular theory on the Fock space of the generator modes (Hilbert-space structure); the two residual data are then located in Cl(1,3), where the imaginary unit is the transverse bivector I_4 B.'
extraction:
  open_problem: op.r-premises-external
  note: >-
    Adversarial arm on the ground-state clause of (N+) without stationarity, testing the condition of geometric
    modular action (modular conjugations of the half-line algebras act as reflections about the cuts). Result:
    a bound, not a derivation. Every condition on the net of local algebras and the vector (CGMA in the
    Buchholz-Summers form, geometric modular groups, modular stability, a positive-energy implementer of the
    net translations) is shared by the null vacuum and all its local gauge transforms, among them the
    translation-invariant Fermi seas chi(P < k), which are Hadamard, locally normal and not ground states for
    the field translations; on the gauge-invariant subalgebra they are ground states. Complex conjugation of the
    real (Majorana) algebra carries the vacuum to the filled positive-energy sea and fixes every real structure.
    So the ground-state clause is independent of all principles invariant under these two groups, and becomes
    expressible exactly when two data are fixed: the lift of the affine translations to the fields (a flat
    connection along the generator) and the orientation of the imaginary unit relative to the time orientation
    (in Cl(1,3), the sign of J = I_4 B). With both fixed, the elementwise form of CGMA (constant phase) is the
    natural candidate principle; at one cut it carries no information on the modular group. Transport-absent.
---

## formal
Units $\hbar = c = 1$. On one horizon generator with affine parameter $u \in \R$, let $\mathfrak{h} = L^{2}(\R, du)\otimes K$, $\CAR(\mathfrak{h})$ the continuum mode space (Definition \claimref{obj.hawking.continuum-mode-space}), $\mathfrak{A}(O)$ its subalgebra over $L^{2}(O)\otimes K$ for an interval or half-line $O$, $\tau_{t}(a(f)) = a(f(\cdot - t))$ the field translations, $P = i\,d/du$, and $\omega_{0}$ the null vacuum, the gauge-invariant quasi-free state with symbol $\chi_{(-\infty,0)}(P)\otimes\id_{K}$ (convention $\omega(a^{*}(f)a(g)) = \ip{g}{Ef}$), the unique gauge-invariant quasi-free state of (N$_{+}$) (Theorem \claimref{synthesis.positive-null-energy-gives-r-premises}(i)). For a measurable $m : \R \to U(K)$ let $\alpha_{m}(a(f)) = a(mf)$, and let $r_{a}(u) = 2a - u$.
\begin{enumerate}
\item[(i)] \emph{(Net-level identity.)} For every $m$, the state $\omega_{0}\circ\alpha_{m}$ has the GNS triple $(\mathcal{H}_{0}, \pi_{0}\circ\alpha_{m}, \Omega_{0})$ and the same von Neumann algebra $\pi_{0}(\mathfrak{A}(O))''$ for every interval and half-line $O$ as $\omega_{0}$. Its modular operators and conjugations for every such algebra are the vacuum's, so every condition on the net $O \mapsto \pi(\mathfrak{A}(O))''$ and the vector holds for it exactly when it holds for $\omega_{0}$: the generator form of the Condition of Geometric Modular Action ($J_{a}$ maps the algebra of each $O \subset (a, \infty)$ onto the twisted algebra of $r_{a}O$, every cut $a$), geometric modular groups on the net, modular stability, twisted Haag duality, and the existence of a unitary group with positive generator implementing the net translations and fixing the vector.
\item[(ii)] \emph{(Fermi seas.)} For $m(u) = e^{iu\kappa}$, $\kappa$ a constant Hermitian operator on $K$, $\omega_{\kappa} = \omega_{0}\circ\alpha_{m}$ is the gauge-invariant quasi-free state with symbol $\chi_{(-\infty,0)}(P - \kappa)$: pure, $\tau$-invariant, locally normal to $\omega_{0}$ on every bounded interval (the symbols differ there by $\pm$ a positive trace-class operator), and its two-point kernel differs from the vacuum's by a smooth kernel, so it satisfies the generator microlocal condition of \claimref{synthesis.microlocal-condition-on-a-generator-gives-the-local-null-ground-state} at every point. For $\kappa \neq 0$ it is not a ground state for $\tau$: the excitations at momenta between $0$ and an eigenvalue of $\kappa$ (holes for a positive eigenvalue, particles for a negative one) have negative energy, and the generator is unbounded below. Its charge density is $\tr\kappa/2\pi$ and its energy density $\tr\kappa^{2}/4\pi$. For $\kappa = k\,\id_{K}$, on the gauge-invariant subalgebra it is a ground state for $\tau$ (there $\alpha_{m}$ commutes with $\tau$ and the vacuum's positive implementer serves), distinct from $\omega_{0}$ by its charge density; with $K$ two-dimensional and $\kappa$ of eigenvalues $\pm k$ the charge density vanishes, and the state is the ground state for $\tau$ followed by the internal rotation $e^{it\kappa}$. Elementwise, its modular conjugations act as $J_{a}\,a(f)\,J_{a} = \Theta\,a^{*}(c\,e^{2i\kappa(a - u)}f\circ r_{a})$, $\Theta$ the Klein twist and $c$ the vacuum's constant phase: a reflection with a position-dependent phase, constant only for $\kappa = 0$.
\item[(iii)] \emph{(The sign.)} The filled positive-energy sea $\bar\omega_{0}$, symbol $\chi_{(0,\infty)}(P)$, equals $\omega_{0}\circ\alpha_{R}$ for the reflection $R : u \mapsto -u$, and equals $x \mapsto \overline{\omega_{0}(\theta(x))}$ for the antilinear automorphism $\theta$ fixing every Majorana field $a(f) + a^{*}(f)$; $\theta$ commutes with $\tau$, the grading and the gauge group and maps each real local subalgebra onto itself. Its half-line modular conjugations act as the reflections about the cuts with the conjugate phase $\bar c$, with the same half-line inclusions; in the polar-part computation the reflected off-diagonal kernels are $\mp i/(2\pi t)$ and $c = -i$ for $\omega_{0}$, $\bar c = +i$ for $\bar\omega_{0}$.
\item[(iv)] \emph{(Independence.)} Let $G_{1}$ be the automorphisms of $\CAR(\mathfrak{h})$ mapping each $\mathfrak{A}(O)$ onto itself and commuting with the gauge group and grading, and $G_{2}$ the linear or antilinear automorphisms commuting with $\tau$, the gauge group and the grading and mapping each real local subalgebra onto itself. A property of states invariant under $G_{1}$ (under $G_{2}$) that $\omega_{0}$ has is shared by every $\omega_{\kappa}$ (by $\bar\omega_{0}$), and none of these is a ground state for $\tau$. So no principle invariant under $G_{1}$ or $G_{2}$ implies the ground-state clause of (N$_{+}$). Two data separate it: the lift of the affine translations to the fields (which of the automorphisms $\alpha_{m}\tau_{t}\alpha_{m}^{-1}$, all mapping $\mathfrak{A}(O)$ onto $\mathfrak{A}(O + t)$, is the translation; for $m(u) = e^{iu\kappa}$ this is $\tau_{t}$ followed by the internal rotation $e^{it\kappa}$, transport along the generator with the flat connection $\kappa\,du$), and the orientation of the imaginary unit relative to the time orientation. In $\Cl(1,3)$, with $n = \gamma_{0} + \gamma_{3}$, $B = \gamma_{0}\gamma_{3}$ and $J = \gamma_{1}\gamma_{2}$: $I_{4}B = J$, $J^{2} = -1$; the transverse rotor $\exp(\varphi J/2)$ fixes $n$ and $B$, so the lift datum is invisible to the generator's null direction and boost; the transverse reflection fixes $n$ and $B$ and reverses $J$ and $I_{4}$, so the sign datum is the orientation $I_{4}$.
\item[(v)] \emph{(One cut; affine structure.)} For $m(u) = e^{i\vartheta(|u|)}$, any measurable $\vartheta$, $J_{0}$ acts elementwise as the vacuum's reflection about $0$ with the constant phase $c$, while the modular group of $\mathfrak{A}((0,\infty))$ acts elementwise as the boost about $0$ followed by the local phase $e^{i(\vartheta(e^{s}|u|) - \vartheta(|u|))}$, which is geometric only if $e^{i\vartheta(x)} = e^{i\mu}x^{i\lambda_{0}}$ for constants $\lambda_{0}$, $\mu$. The slope-jump vacuum of \claimref{synthesis.normality-on-the-closed-generator-gives-the-vacuum-folium-not-the-ground-state}(vi) has modular conjugations acting by the reflections of its own regular parameter $\lambda$, $u \mapsto \lambda^{-1}(2\lambda(a) - \lambda(u))$, and by no affine reflection, at every cut.
\item[(vi)] \emph{(The modular conjugation from the one-particle operator; finite modes.)} For a Slater state on $n_{0} + n_{1}$ modes with basis projection $E$ and $\Omega$ cyclic and separating for the CAR algebra $M$ of the first $n_{0}$ modes, $J\,a(f)\,J = (-1)^{n_{0}}\Gamma\,a^{*}(Wf)$, with $\Gamma$ the parity and $W$ the polar part of the off-diagonal block of $E$; so elementwise geometric action of $J$ at a cut is a statement about the polar part of the cross-cut block.
\end{enumerate}
Status: (i) to (v) proved (the vacuum's modular data imported; (iii)'s explicit phases computed from (vi) in its continuum form, argued); (vi) proved for the stated finite cases by exact computation, with uniqueness of the polar decomposition. Comparison (literature, verified): for wedges in Minkowski space the Condition of Geometric Modular Action gives translations, and with Modular Stability positivity only up to sign \cite{BuchholzFlorigSummers1999}; (i) and (iii) are the generator forms of those two gaps. Transport-absent.

## technical
The open problem asks whether the ground-state clause of (N$_{+}$), that the generator modes are in their lowest-energy state for sliding along the light ray, follows from a principle of the series with no thermal input. A natural candidate is geometric modular action of the modular conjugations alone: no modular group and no temperature enter it. This result bounds what any such principle can do. Every condition stated in terms of the algebras of regions and the state vector (including that candidate in the form Buchholz and Summers use, modular stability, Haag duality, and positive energy for some implementation of the translations) is satisfied identically by the null vacuum and by every local gauge transform of it, because a local gauge transformation maps each region's algebra onto itself. Among these are the translation-invariant Fermi seas, filled up to a nonzero null momentum: they are Hadamard and locally normal everywhere, yet the field translations have negative-energy excitations in them; on the gauge-invariant observables they are ground states with a constant charge density. Complex conjugation of the real Majorana algebra carries the vacuum to the filled positive-energy sea and preserves every real structure. So the ground-state clause is not implied by any principle blind to (1) which automorphism lifts the affine translations to the fields, equivalently a flat connection along the generator, and (2) the orientation of the imaginary unit relative to time; in $\Cl(1,3)$ the second is the orientation $I_{4}$ through $I_{4}B = J$ (\claimref{synthesis.wedge-reflections-compose-to-the-two-pi-rotor-so-geometric-modular-conjugations-give-interacting-spin-statistics}), and the first is a transverse rotation rate that the boost does not see. Only the elementwise form of the condition, with a constant phase, sees both, and at a single cut it says nothing about the modular group.

## lay
The series assumes that the quantum modes along a horizon's light rays sit in their lowest-energy state. One hoped-for justification uses a mirror symmetry that quantum theory attaches to each half of a ray. This result shows what that kind of justification cannot reach. The same mirror data are shared by states that are filled with particles up to some momentum, which look exactly like the empty state region by region, and by the state in which every positive-energy level is filled, which differs only in the sign convention for the square root of minus one. So two pieces of information must be supplied separately: how a slide along the ray is carried over to the field, and which orientation the imaginary unit has relative to the direction of time.

## one-liner
On a horizon generator every local gauge transform of the null vacuum, the translation-invariant Fermi seas $\chi(P < \kappa)$ included (Hadamard, locally normal, not ground states for the field translations, but ground states on the gauge-invariant observables), has the vacuum's local algebras and modular objects, so geometric modular action in the Buchholz-Summers form, modular stability and positive net translations cannot give the ground-state clause of (N$_{+}$); complex conjugation of the Majorana algebra gives the filled sea with conjugate modular phase; the clause needs two data, the lift of the translations to the fields and the orientation of $i$ ($I_{4}B = J$ in $\Cl(1,3)$).
