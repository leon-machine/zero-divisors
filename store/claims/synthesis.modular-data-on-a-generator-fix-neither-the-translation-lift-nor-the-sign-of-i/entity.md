---
id: synthesis.modular-data-on-a-generator-fix-neither-the-translation-lift-nor-the-sign-of-i
kind: claim
version: 5
title: 'Net-level modular data on a generator fix neither the translation lift nor the unit''s sign'
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
- name: Claude Opus 5.5
  role: premises repointed to the premise-free results split out of the null-energy and collapse results
  version: 3
  source: maintainer pass 2026-11-07
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 4
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: 'consistency pass, the bare i of the title replaced by the unit''s sign, and a sentence saying that the unindexed J of (iv) is the transverse bivector, not a modular conjugation J_a, and which sign of the boost bivector B is used'
  version: 5
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'maintainer pass, premise repointed to the premise-free transverse-bivector result at Leon''s decisions'
  version: 5
  source: maintainer pass 2026-11-07 (decisions)
review: draft
about:
- obj.hawking.continuum-mode-space
imported_from:
- citation: 'D. Buchholz, M. Florig and S. J. Summers, An algebraic characterization of vacuum states in Minkowski space. II. Continuity aspects, Lett. Math. Phys. 49 (1999), 337--350; arXiv:math-ph/9909003.'
  key: BuchholzFlorigSummers1999
  locator: 'Sec. 2, the Condition of Geometric Modular Action (a)-(d), a condition on the wedge algebras as sets; Prop. 3.5 (CGMA gives continuous translations); Prop. 3.6 (CGMA and Modular Stability give sp U in the closed forward cone or in its negative); the remark that CGMA alone does not give a ground state. Statements checked against the arXiv text, journal data against Crossref; now Fact synthesis.imported-buchholz-florig-summers-geometric-modular-action-and-modular-stability.'
- citation: 'D. Buchholz and S. J. Summers, An algebraic characterization of vacuum states in Minkowski space, Commun. Math. Phys. 155 (1993), 449--458.'
  key: BuchholzSummers1993
  locator: 'origin of the Condition of Geometric Modular Action (last section), as cited in BuchholzFlorigSummers1999; not read directly'
derivations:
- name: main
  uses:
  - synthesis.null-vacuum-on-a-horizon-generator@1
  - angle.imported-theorems-deliver-their-hypotheses@3
  - synthesis.imported-powers-stormer-takesaki-disjointness@3
  - singularity.modular-theory-matrix-factor-proved-outright@6
  - synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom@1
  - synthesis.microlocal-condition-on-a-generator-gives-the-local-null-ground-state@6
  - synthesis.normality-on-the-closed-generator-gives-the-vacuum-folium-not-the-ground-state@4
  - synthesis.geometric-modular-conjugations-on-a-generator-give-the-null-ground-state@5
  - synthesis.imported-modular-conjugation-of-the-chiral-fermi-field-is-the-twisted-reflection@2
  - synthesis.imported-buchholz-florig-summers-geometric-modular-action-and-modular-stability@4
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
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version kept at 5 (already raised in this run). Decision item D4 (routine): synthesis.wedge-reflections-compose-to-the-two-pi-rotor-... was cited only for the identity I_4 B = J (B = e_0 e_3, J = e_1 e_2); it is repointed to the premise-free synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom@1 (J = e_2 e_3 = I_4 sigma, sigma = e_0 e_1), carried to this plane by the cyclic spatial rotation e_1 -> e_3 -> e_2 -> e_1, which fixes I_4 (by hand: I_4 e_0 e_3 = e_1 e_2 and I_4 e_0 e_1 = e_2 e_3; the check asserts I_4 B = J exactly); uses edge, formal citation and the check''s premise call repointed, so the wedge result''s premises (C1, C2, L, P, R, N+) no longer reach this result through it.'
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 4 -> 5: The bare i of the title replaced by the unit''s sign, and a sentence saying that the unindexed J of (iv) is the transverse bivector, not a modular conjugation J_a, and which sign of the boost bivector B is used; mathematics, links, pins, status and checks unchanged.'
  maintainer_pass_clause_split:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 2 -> 3, at Leon''s decision of 7 November 2026: it cited synthesis.positive-null-energy-gives-r-premises only for its (i) (the null vacuum as the unique gauge-invariant quasi-free ground state), which is now synthesis.null-vacuum-on-a-horizon-generator (ii); the uses edge, the claimrefs and the checks'' premise calls are repointed to it, so this result no longer inherits Premise (N+) through them. Statement, proof argument and checks otherwise unchanged; no assumes edge added or removed; notation as the sweep left it. Pins moved to current versions (statements unchanged): synthesis.microlocal-condition-on-a-generator-gives-the-local-null-ground-state 4 -> 5; synthesis.normality-on-the-closed-generator-gives-the-vacuum-folium-not-the-ground-state 1 -> 3; synthesis.geometric-modular-conjugations-on-a-generator-give-the-null-ground-state 2 -> 3.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'By Leon''s ruling R2 (7 November 2026) the complex unit of the generator''s mode space is the field theory''s unit I_4, written throughout: P = I_4 d/du, the null-vacuum kernel (I_4/2 pi)(u - v + I_4 0)^{-1}, the Klein twist and the phases c = I_4 eta = -I_4, the gauge transforms e^{I_4 u kappa}, e^{I_4 vartheta}, the modular group Delta^{I_4 s}, the cross-cut kernels, the Majorana decomposition and the finite Slater checks; the reading ''if the field''s i is read as J'' is restated as a reading through J = I_4 B, the bivector that the unit I_4 forms with the boost bivector B, with the claim unchanged. Nothing stays; the earlier declaration is removed.'
  open_problem: op.r-premises-external
  note: >-
    Adversarial arm on the ground-state clause of (N+) without stationarity, testing the condition of geometric
    modular action (modular conjugations of the half-line algebras act as reflections about the cuts). Result:
    a bound on net-level principles, not a derivation. Every condition on the net of local algebras and the
    vector (CGMA in the Buchholz-Summers form, geometric modular groups on the net, modular stability, twisted
    duality, a positive-energy implementer of the net translations) is shared by the null vacuum and all its
    local gauge transforms, among them the translation-invariant Fermi seas chi(P < kappa), which are
    generator-Hadamard, locally normal and not ground states for the field translations; for scalar kappa they
    are ground states on the gauge-invariant subalgebra, so the ground-state clause must stay posed on the field
    algebra. Complex conjugation of the real (Majorana) algebra carries the vacuum to the filled positive-energy
    sea. So no principle invariant under the local gauge group G1 or the real-linear group G2 implies the
    ground-state clause; the two data they cannot see are the lift of the affine translations to the fields (a
    flat connection along the generator; the lift by parallel transport, zero connection, excludes the Fermi
    seas) and the orientation of the imaginary unit relative to time, which the series does not fix and (N+)
    assumes. The elementwise form with a constant phase fixes the lift (products of the reflections are the field
    translations) and carries the orientation of i as its phase: that is the companion field-level result,
    synthesis.geometric-modular-conjugations-on-a-generator-give-the-null-ground-state, whose Step 4
    (natural-cone positivity) gives the vacuum's phase, c = i eta = -i, under the named assumption eta = -1.
    Transport-absent.
  maintainer_pass:
    by: maintainer-2026-11-06
    date: '2026-11-06'
    note: 'Version 1 -> 2: the derivation now pins the companion field-level result (for the vacuum''s phase), the Fact on the field-level modular conjugation of the chiral Fermi field (the vacuum''s half-line conjugations act as twisted reflections), the Buchholz-Florig-Summers Fact and the Powers-Stormer Fact at version 3, cited with claimref; and the lay level no longer says that the field-level mirror data fix the orientation of i, which they carry as a sign that is assumed (Leon''s decision of 6 November). Statement, proof and check otherwise unchanged.'
---

## formal
Units $\hbar = c = 1$. On one horizon generator with affine parameter $u \in \R$, let $\mathfrak{h} = L^{2}(\R, du)\otimes K$, $\CAR(\mathfrak{h})$ the continuum mode space (Definition \claimref{obj.hawking.continuum-mode-space}; its complex unit is the field theory's unit $I_{4}$, and numbers are read in $\mathrm{span}\{1, I_{4}\}$), $\mathfrak{A}(O)$ its subalgebra over $L^{2}(O)\otimes K$ for an interval or half-line $O$, $\tau_{t}(a(f)) = a(f(\cdot - t))$ the field translations, $P = I_{4}\,d/du$, and $\omega_{0}$ the null vacuum, the gauge-invariant quasi-free state with symbol $\chi_{(-\infty,0)}(P)\otimes\id_{K}$ (convention $\omega(a^{*}(f)a(g)) = \ip{g}{Ef}$), the unique gauge-invariant quasi-free state of (N$_{+}$) (Theorem \claimref{synthesis.null-vacuum-on-a-horizon-generator}(ii)). For a measurable $m : \R \to U(K)$ let $\alpha_{m}(a(f)) = a(mf)$, and let $r_{a}(u) = 2a - u$. $\Theta$ is the grading unitary, normalised by $\Theta\Omega = \Omega$; the vacuum's half-line conjugations act on the fields as $J_{a}\,a(f)\,J_{a} = \Theta\,a^{*}(c\,f\circ r_{a})$, $f$ supported in $(a, \infty)$, with a constant phase $c$ (Fact \claimref{synthesis.imported-modular-conjugation-of-the-chiral-fermi-field-is-the-twisted-reflection}(c); $c = I_{4}\eta$ in the notation $J_{a}\psi(f)J_{a} = \eta Z\psi^{*}(\rho_{a}f)Z^{*}$ with the Klein twist $Z$; $c = -I_{4}$).
\begin{enumerate}
\item[(i)] \emph{(Net-level identity.)} For every $m$, the state $\omega_{0}\circ\alpha_{m}$ has the GNS triple $(\mathcal{H}_{0}, \pi_{0}\circ\alpha_{m}, \Omega_{0})$ and the same von Neumann algebra $\pi_{0}(\mathfrak{A}(O))''$ for every interval and half-line $O$ as $\omega_{0}$. Its modular operators and conjugations for every such algebra are the vacuum's, so every condition on the net $O \mapsto \pi(\mathfrak{A}(O))''$ and the vector holds for it exactly when it holds for $\omega_{0}$: the generator form of the Condition of Geometric Modular Action ($J_{a}$ maps the algebra of each $O \subset (a, \infty)$ onto the twisted algebra of $r_{a}O$, every cut $a$), geometric modular groups on the net, modular stability, twisted Haag duality, and the existence of a unitary group with positive generator implementing the net translations and fixing the vector.
\item[(ii)] \emph{(Fermi seas.)} For $m(u) = e^{I_{4}u\kappa}$, $\kappa$ a constant Hermitian operator on $K$, $\omega_{\kappa} = \omega_{0}\circ\alpha_{m}$ is the gauge-invariant quasi-free state with symbol $\chi_{(-\infty,0)}(P - \kappa)$: pure, $\tau$-invariant, locally normal to $\omega_{0}$ on every bounded interval (the symbols differ there by $\pm$ a positive trace-class operator), and its two-point kernel differs from the vacuum's by a smooth kernel, so it satisfies the generator microlocal condition of \claimref{synthesis.microlocal-condition-on-a-generator-gives-the-local-null-ground-state} at every point. For $\kappa \neq 0$ it is not a ground state for $\tau$: the excitations at momenta between $0$ and an eigenvalue of $\kappa$ (holes for a positive eigenvalue, particles for a negative one) have negative energy, and the generator is unbounded below. Its charge density is $\tr\kappa/2\pi$ and its energy density $\tr\kappa^{2}/4\pi$. It is the ground state of the other lift $\alpha_{m}^{-1}\tau_{t}\alpha_{m}$, $a(f) \mapsto a(e^{-I_{4}t\kappa}f(\cdot - t))$, $\tau_{t}$ followed by the internal rotation $e^{-I_{4}t\kappa}$, with one-particle generator $P - \kappa$. For $\kappa = k\,\id_{K}$, on the gauge-invariant subalgebra it is a ground state for $\tau$ (there $\alpha_{m}$ commutes with $\tau$ and the vacuum's positive implementer serves), distinct from $\omega_{0}$ by its charge density; with $K$ two-dimensional and $\kappa$ of eigenvalues $\pm k$ the charge density vanishes. Elementwise, its modular conjugations act as $J_{a}\,a(f)\,J_{a} = \Theta\,a^{*}(c\,e^{2I_{4}\kappa(a - u)}f\circ r_{a})$: a reflection with a position-dependent phase, constant only for $\kappa = 0$; so the elementwise action does see the lift.
\item[(iii)] \emph{(The sign.)} The filled positive-energy sea $\bar\omega_{0}$, symbol $\chi_{(0,\infty)}(P)$, equals $\omega_{0}\circ\alpha_{R}$ for the reflection $R : u \mapsto -u$, and equals $x \mapsto \overline{\omega_{0}(\theta(x))}$ for the antilinear automorphism $\theta$ fixing every Majorana field $a(f) + a^{*}(f)$; $\theta$ commutes with $\tau$, the grading and the gauge group and maps each real local subalgebra onto itself. Its half-line modular conjugations act as the reflections about the cuts with the conjugate phase $\bar c = +I_{4}$, with the same half-line inclusions (the conjugation of the twisted complement algebra is $\Theta J$). The vacuum's $c = -I_{4}$ is fixed by natural-cone positivity in the companion field-level result \claimref{synthesis.geometric-modular-conjugations-on-a-generator-give-the-null-ground-state} (its Step 4, $\eta = -1$); the reflected cross-cut kernels $\mp I_{4}/(2\pi t)$ of the two states agree with it (argued, through the continuum form of (vi)). So net-level data do not see the sign, and the elementwise phase records it.
\item[(iv)] \emph{(Independence.)} Let $G_{1}$ be the automorphisms of $\CAR(\mathfrak{h})$ mapping each $\mathfrak{A}(O)$ onto itself and commuting with the gauge group and grading, and $G_{2}$ the linear or antilinear automorphisms commuting with $\tau$, the gauge group and the grading and mapping each real local subalgebra onto itself. A property of states invariant under $G_{1}$ (under $G_{2}$) that $\omega_{0}$ has is shared by every $\omega_{\kappa}$ (by $\bar\omega_{0}$), and none of these is a ground state for $\tau$. So no principle invariant under $G_{1}$ or $G_{2}$ implies the ground-state clause of (N$_{+}$); $\omega_{\kappa}$ is the ground state of the lift $\alpha_{m}^{-1}\tau_{t}\alpha_{m}$. The two data these groups cannot see are: the lift of the affine translations to the fields (which of the automorphisms $\alpha_{m}\tau_{t}\alpha_{m}^{-1}$, all mapping $\mathfrak{A}(O)$ onto $\mathfrak{A}(O + t)$, is the translation; for $m(u) = e^{I_{4}u\kappa}$ the lift $\alpha_{m}^{-1}\tau_{t}\alpha_{m}$ is $\tau_{t}$ followed by $e^{-I_{4}t\kappa}$, transport along the generator with a flat connection; parallel transport, the zero connection, gives $\tau$), and the orientation of the unit $I_{4}$ relative to the time orientation, which the series does not fix and (N$_{+}$) assumes. In $\Cl(1,3)$, with $n = \gamma_{0} + \gamma_{3}$, $B = \gamma_{0}\gamma_{3}$ (the boost bivector in the sign $B_{k} = \gamma_{0}n$ of the conventions, $n$ there the spatial direction $\gamma_{3}$) and $J = \gamma_{1}\gamma_{2}$ (here $J$ without an index is this transverse bivector, not a modular conjugation $J_{a}$), exactly: $I_{4}B = J$, $J^{2} = -1$, the transverse rotor $\exp(\varphi J/2)$ fixes $n$ and $B$, and the transverse reflection fixes $n$ and $B$ and reverses $J$ and $I_{4}$. Reading (argued, not proved): read through $J = I_{4}B$, the transverse bivector that the field's unit $I_{4}$ forms with the generator's boost bivector $B$, the lift datum is a transverse rotation rate invisible to the generator's null direction and boost, and the sign datum is the orientation $I_{4}$ relative to $B$.
\item[(v)] \emph{(One cut; affine structure.)} For $m(u) = e^{I_{4}\vartheta(|u|)}$, any measurable $\vartheta$, $J_{0}$ acts elementwise as the vacuum's reflection about $0$ with the constant phase $c$, while the modular group of $\mathfrak{A}((0,\infty))$ acts elementwise as the boost about $0$ followed by the local phase $e^{I_{4}(\vartheta(e^{s}|u|) - \vartheta(|u|))}$, which is geometric only if $e^{I_{4}\vartheta(x)} = e^{I_{4}\mu}x^{I_{4}\lambda_{0}}$ for constants $\lambda_{0}$, $\mu$. The slope-jump vacuum of \claimref{synthesis.normality-on-the-closed-generator-gives-the-vacuum-folium-not-the-ground-state}(vi) has modular conjugations acting by the reflections of its own regular parameter $\lambda$, $u \mapsto \lambda^{-1}(2\lambda(a) - \lambda(u))$, and by no affine reflection, at every cut.
\item[(vi)] \emph{(The modular conjugation from the one-particle operator; two finite cases.)} For the Slater states on $1 + 1$ and $2 + 2$ modes of Step 6 (basis projection $E$ of rank $r$, $\Omega$ cyclic and separating for the CAR algebra $M$ of the first block of modes), $J\,a(f)\,J = \Gamma_{\Omega}\,a^{*}(Wf)$, with $\Gamma_{\Omega} = (-1)^{r}\Gamma$ the parity normalised to fix $\Omega$ and $W$ the polar part of the block of $E$ crossing from $M$'s modes to the others; so elementwise geometric action of $J$ at a cut is a statement about the polar part of the cross-cut block. (The general finite case, by factorising the Slater state over Schmidt pairs, is argued.)
\end{enumerate}
Status: (i) to (v) proved (the vacuum's modular data imported, Facts \claimref{angle.imported-theorems-deliver-their-hypotheses} and \claimref{synthesis.imported-modular-conjugation-of-the-chiral-fermi-field-is-the-twisted-reflection}; the vacuum's phase $c = -I_{4}$ from \claimref{synthesis.geometric-modular-conjugations-on-a-generator-give-the-null-ground-state}; the Hankel-kernel route to it argued); the $\Cl(1,3)$ identities in (iv) proved, their reading argued; (vi) proved for the two finite cases by exact computation, with uniqueness of the polar decomposition. Comparison (literature, verified): for wedges in Minkowski space the Condition of Geometric Modular Action gives translations, and with Modular Stability positivity only up to sign (Fact \claimref{synthesis.imported-buchholz-florig-summers-geometric-modular-action-and-modular-stability}(c), (d) \cite{BuchholzFlorigSummers1999}); (i) and (iii) are the generator forms of those two gaps. Transport-absent.

## technical
The open problem asks whether the ground-state clause of (N$_{+}$), that the generator modes are in their lowest-energy state for sliding along the light ray, follows from a principle of the series with no thermal input. A natural candidate is geometric modular action of the modular conjugations alone: no modular group and no temperature enter it. This result bounds what such a principle can do when it is stated at the level of the net. Every condition stated in terms of the algebras of regions and the state vector (the condition in the form Buchholz and Summers use, modular stability, Haag duality, and positive energy for some implementation of the net translations) is satisfied identically by the null vacuum and by every local gauge transform of it, because a local gauge transformation maps each region's algebra onto itself. Among these are the translation-invariant Fermi seas, filled up to a nonzero null momentum: they satisfy the generator microlocal condition and are locally normal everywhere, yet the field translations have negative-energy excitations in them; they are ground states of a different lift of the translations, and on the gauge-invariant observables, for a scalar shift, ground states of the translations themselves with a constant charge density. Complex conjugation of the real Majorana algebra carries the vacuum to the filled positive-energy sea. So no principle invariant under these groups implies the ground-state clause; the two data they cannot see are (1) which automorphism lifts the affine translations to the fields, equivalently a flat connection along the generator (parallel transport gives the zero connection), and (2) the orientation of the unit $I_{4}$ relative to time, which the series does not fix. The action of the same modular conjugations on the fields themselves sees both: it fixes the lift and records the orientation as its phase, which is what the companion field-level result uses (\claimref{synthesis.geometric-modular-conjugations-on-a-generator-give-the-null-ground-state}). Read in $\Cl(1,3)$ through $J = I_{4}B$, the transverse bivector that the field's unit $I_{4}$ forms with the boost bivector $B$ (\claimref{synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom}, rotated by the cyclic spatial rotation $e_{1} \mapsto e_{3} \mapsto e_{2} \mapsto e_{1}$, which fixes $I_{4}$ and carries its $\sigma = e_{0}e_{1}$, $J = e_{2}e_{3}$ to $B = e_{0}e_{3}$, $J = e_{1}e_{2}$), the first datum would be a transverse rotation rate that the boost does not see and the second the orientation of $I_{4}$ relative to $B$; this reading is argued, not proved. At a single cut even the field-level conjugation says nothing about the modular group.
## lay
The series assumes that the quantum modes along a horizon's light rays sit in their lowest-energy state. One hoped-for justification uses a mirror symmetry that quantum theory attaches to each half of a ray. This result shows what that justification cannot reach when it looks only at which observables belong to which stretch of the ray. The same mirror data are shared by states filled with particles up to some momentum, which have the same local algebras and mirror data region by region and are locally indistinguishable from the empty state in the sense of local normality, and by the state in which every positive-energy level is filled, which differs in the orientation of the square root of minus one relative to the direction of time. So two pieces of information must be supplied separately: how a slide along the ray is carried over to the field, and that orientation. The mirror data acting on the fields themselves fix the first, and record the second as a sign that is not fixed by anything else in the series and must be assumed.
## one-liner
On a horizon generator every local gauge transform of the null vacuum, the translation-invariant Fermi seas $\chi(P < \kappa)$ included (generator-Hadamard, locally normal, not ground states for the field translations but for the lift with generator $P - \kappa$, and for scalar $\kappa$ ground states on the gauge-invariant observables), has the vacuum's local algebras and modular objects, so net-level principles (geometric modular action in the Buchholz-Summers form, modular stability, positive net translations) cannot give the ground-state clause of (N$_{+}$); complex conjugation of the Majorana algebra gives the filled sea with conjugate modular phase; the net misses two data, the lift of the translations to the fields and the orientation of the unit $I_{4}$, which the elementwise action of the conjugations does see.
