---
id: synthesis.light-ray-gauge-currents-of-a-generation-do-not-see-its-anomaly-cancellation
kind: claim
version: 1
title: 'Light-ray gauge currents of a generation see the linear anomaly condition, not cubic ones'
status: proved
region: synthesis
subject: quantum-fields
tags: [gauge-fields, hypercharge-and-anomalies, pairing-and-bogoliubov, chirality]
proposed_by:
  kind: ai
  session: 2026-11-08-current-algebra
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: run 2026-11-08-current-algebra
review: draft
about:
- obj.tower.tower
derivations:
- name: main
  uses:
  - std-algebra.witt-basis-car@1
  - synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins@1
  - synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves@1
  - synthesis.spin10-clause-content-is-the-neutral-singlet-choice@2
  - synthesis.slot-module-light-ray-arrays-are-weyl-components@3
  - synthesis.cpt-closure-forces-slot-module-and-chirality@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_partner_blocks_are_minus_transposes
- kind: check
  ref: check.py::check_particle_hole_reversal_intertwines_window_currents
- kind: check
  ref: check.py::check_trace_form_is_halving_independent_and_anomalies_are_not
- kind: check
  ref: check.py::check_abelian_level_depends_on_the_scale_of_y
- kind: check
  ref: check.py::check_hypercharge_constant_is_the_linear_anomaly_coefficient
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators
  - synthesis.triangle-anomaly-in-the-spacetime-algebra-is-the-pseudoscalar-part-of-the-field-square-and-cancels-per-generation
  - synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays
extraction:
  open_problem: op.qft-non-abelian-gauge-fields
  note: >-
    Adversarial attack on the item "the current algebra along generators" of op.qft-non-abelian-gauge-fields: test the
    statement that the Standard Model gauge algebra acts inside exact u(16) level-one channel currents per light ray and
    generation, and find what fails. Findings. The statement holds in the following exact sense: the channels are
    complex (Witt pairs with the unit J), every gauge generator is block diagonal on the isotypic components of the
    slot module and anti-Hermitian over span{1, J}, so the gauge currents are pair currents and the algebra sits in
    u(16), not merely in so(32); no gauge generator connects the two chirality arrays of a light ray, since the gauge
    algebra acts on the internal index and the chirality and the rotation about the generator act on the spinor
    values. What fails is narrower and is stated here: (a) the abelian level is a number only after a normalisation
    of Y is chosen (10/3, 4 or 120 by three natural choices), while the ratios 3 : 5 : 8 of the traces of T3^2, Y^2,
    Q^2 are fixed; (b) the gauge currents along a generator with energy and sea, up to the hypercharge constant,
    are the same for all 32 gauge-commuting CPT halvings (32 sign patterns, any neutral line), by an explicit inner
    particle-hole reversal. The hypercharge constant is the change of the sea's hypercharge, (L/2) tr Y over V_+, and
    tr Y is also the mixed central term of the hypercharge current with the number current in u(16): it is the
    mixed gravitational (linear) anomaly coefficient, nonzero for 24 of the 32 patterns. On the 8 patterns with
    tr Y = 0 the currents, energy and sea are isomorphic and 2 of them are anomaly-free. So there is no relation
    between the levels of g and the cubic anomaly conditions; the linear condition is the Y-N mixed level and the
    sea's hypercharge; the cubic ones are visible only with the rotation weights of the channels, as weighted cubic
    traces. Stored and cited:
    the window matrix form of the pair currents (synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins
    (i)), the Witt pairs (std-algebra.witt-basis-car), the window energy with half-integer weights and the sea
    (synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves (i), (iii)), the five-mode
    module and its 32 gauge-commuting halvings (synthesis.spin10-clause-content-is-the-neutral-singlet-choice (ii)),
    the sixteen channels per generation and light ray (synthesis.slot-module-light-ray-arrays-are-weyl-components (ii)),
    the anomaly-free halvings and the four conditions of Fact standard-model.imported-anomaly-coefficients
    (synthesis.cpt-closure-forces-slot-module-and-chirality (4)). Cited as mentions: the pair currents of the
    generators (synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators (iv)), the chirality arrays
    and weights (synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays (iii), (iv)), the triangle
    anomaly's symmetric tensor d (synthesis.triangle-anomaly-in-the-spacetime-algebra-is-the-pseudoscalar-part-of-the-field-square-and-cancels-per-generation
    (v), (vi)). The levels per factor and the Sugawara split are not the subject here; they enter only through the trace
    form 4 tr_5, which clause (iii) computes. Prior art, orientation only, cited from memory: a
    representation and its conjugate have equal quadratic (Dynkin) indices and opposite anomaly coefficients
    (classical); affine current algebras and the level as the Dynkin index of an embedding (Kac; Goddard and Olive), charge
    conjugation of chiral fermions in two dimensions, the cubic anomaly conditions (Bouchiat, Iliopoulos and Meyer;
    Gross and Jackiw), anomaly inflow on chiral edges (Callan and Harvey), sin^2 theta = 3/8 at the unification scale
    (Georgi, Quinn and Weinberg). Ledger: transport-absent (finite CAR on tower planes and finite linear algebra on the
    Stored with this one (maintainer pass): the embedding of the gauge algebra in the channel currents and its trace form are in synthesis.standard-model-currents-of-the-sixteen-channels-levels-and-window-sugawara-split; the matching of the slot module's unit with the channels' unit is recorded once in store/conventions.md.
    slot module; no transport completion used).
---

## formal
Let $V$ be the five-mode module of Theorem \claimref{synthesis.spin10-clause-content-is-the-neutral-singlet-choice}, with occupation states $a^{\dagger}_{S}\Omega$, $S \subseteq \{1, \dots, 5\}$ (modes $1, 2$ the slots, $3, 4, 5$ the pairs), isotypic components $V_{n,k}$ ($n$ slots, $k$ pairs), the gauge algebra $\mathfrak{g} = \mathfrak{s}(\uu(2) \oplus \uu(3))$ acting by $\hat t = \sum_{i,j}t_{ij}a^{\dagger}_{i}a_{j}$ ($t$ traceless and anti-Hermitian on the five modes) and $Y = (3n - 2k)/6$. Its numbers are read in $\mathrm{span}\{1, I_{4}\}$ (Theorem \claimref{synthesis.slot-module-light-ray-arrays-are-weyl-components}); on the channels below they are read in $\mathrm{span}\{1, J\}$, $J$ the kernel bivector, through $I_{4} \mapsto J$ (the other sign is the case of (ii) in which every component is reversed). A halving $V_{+}$ is a gauge-commuting CPT halving: one of $32$ sign patterns, one member of each conjugate pair $V_{n,k}$, $V_{2-n,3-k}$, with any line of the neutral block (\claimref{synthesis.spin10-clause-content-is-the-neutral-singlet-choice}(ii)). On one null generator take a window of levels $k = 0, \dots, L - 1$ ($L$ even) and one channel $x$ per occupation state of $V_{+}$, sixteen channels (\claimref{synthesis.slot-module-light-ray-arrays-are-weyl-components}(ii)); each mode $(x, k)$ is a tower plane $(e_{x,k}, f_{x,k})$, $Q(e_{x,k}) = 1$, $Q(f_{x,k}) = -1$, with $a^{*}_{x,k} = \tfrac12(e_{x,k} + f_{x,k})$, $a_{x,k} = \tfrac12(e_{x,k} - f_{x,k})$ (Theorem \claimref{std-algebra.witt-basis-car}). For a channel matrix $M$ let $\rho_{q}(M) = \sum_{k, k+q}\sum_{x,y}M_{xy}a^{*}_{x,k}a_{y,k+q}$ (\claimref{synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins}(i)); the gauge currents are $\rho_{q}(\rho_{+}(T))$, $\rho_{+}(T)$ the matrix of $\hat t$ on $V_{+}$; $H = \sum_{x,k}(k - \tfrac{L - 1}{2})n_{x,k}$ is the window energy with half-integer weights and the sea fills $k < L/2$ in every channel (\claimref{synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves}(i), (iii)).
\begin{enumerate}
\item[(i)] \emph{(Pair currents and partner blocks.)} Every $\rho_{+}(T)$ preserves each component and is anti-Hermitian over $\mathrm{span}\{1, J\}$, so every gauge current is a pair current of the channels, with no pair-creation bilinear $a_{x}a_{y}$ or $a^{*}_{x}a^{*}_{y}$: $\mathfrak{g}$ acts in the $\uu(16)$ of the channel currents, not merely in $\so(32)$. On a conjugate pair, in the bases $a^{\dagger}_{S}\Omega$ of $V_{n,k}$ and $\epsilon(S)a^{\dagger}_{S^{c}}\Omega$ of $V_{2-n,3-k}$, where $a^{\dagger}_{S}a^{\dagger}_{S^{c}}\Omega = \epsilon(S)a^{\dagger}_{1}\cdots a^{\dagger}_{5}\Omega$, the matrices of $\hat t$ are $M$ and $-M^{T}$. The trace of $\rho_{+}(T)$ on a component is $0$ for $T \in \su(2) \oplus \su(3)$ and $\dim V_{n,k}\,Y_{n,k}J$ for the hypercharge generator $JY$.
\item[(ii)] \emph{(Particle-hole reversal.)} Let $C$ be the channels of a set of whole components of $V_{+}$, and $V_{+}^{C}$ the halving that replaces each of them by its partner, read in the partner bases of (i). The map $\varphi_{C}$ with $e_{x,k} \mapsto e_{x,L-1-k}$, $f_{x,k} \mapsto -f_{x,L-1-k}$ for $x \in C$, fixing every other generator, is the inner automorphism $\operatorname{Ad}(\prod_{x \in C}u_{x})$, $u_{x} = f_{x,0}\cdots f_{x,L-1}\prod_{k < L/2}(e_{x,k} - e_{x,L-1-k})(f_{x,k} - f_{x,L-1-k})$, and commutes with the adjoint. It sends $a^{*}_{x,k}$ to $a_{x,L-1-k}$ and $n_{x,k}$ to $1 - n_{x,L-1-k}$ on $C$, fixes $H$, the sea and the set of vectors edge-clean at each depth, and for every $T \in \mathfrak{g}$ and every $q \ge 0$, exactly,
\[
\varphi_{C}\bigl(\rho_{q}(\rho_{+}(T))\bigr) = \rho_{q}(\rho_{+}^{C}(T)) + \delta_{q0}\,L\operatorname{tr}_{C}\rho_{+}(T),
\]
the constant being zero on $\su(2) \oplus \su(3)$. It reverses the rotation weights of $C$: for the mode rotation $\exp(\theta J\sum_{x,k}w_{x}n_{x,k})$ about the generator, $\varphi_{C}$ gives the rotation with $w_{x}$ replaced by $-w_{x}$ on $C$, times the phase $\exp(\theta JL\sum_{x \in C}w_{x})$.
\item[(iii)] \emph{(Levels and anomalies.)} So the exact window commutators of the gauge currents, their edge terms, their values on edge-clean vectors, the energy and the sea are, up to $\varphi_{C}$ and the hypercharge constant $L\operatorname{tr}_{C}\rho_{+}(JY)$, the same for all $32$ sign patterns and any neutral line; in particular $\operatorname{tr}_{V_{+}}(\rho_{+}(T)\rho_{+}(T')) = 4\operatorname{tr}_{5}(tt')$ for all $T, T'$ and every halving, so the traces of $T_{3}^{2}$, of a colour Cartan generator squared, and of $Y^{2}$ over $V_{+}$ are $2$, $2$, $\tfrac{10}{3}$ for all $32$. The hypercharge constant is not a normalisation: the sea of $V_{+}$ has hypercharge $\tfrac{L}{2}\operatorname{tr}_{V_{+}}Y\,J$ (that is, $\rho_{0}(\rho_{+}(JY))$ acts on it by this number), and $\varphi_{C}$, which maps sea to sea, changes it by $L\operatorname{tr}_{C}Y\,J$; on edge-clean vectors the mixed central term of $\rho_{q}(\rho_{+}(JY))$ with the number current $\rho_{q}(1)$ in $\uu(16)$ is $q\operatorname{tr}_{V_{+}}Y\,J$. Both are the mixed gravitational (linear) anomaly coefficient $\operatorname{tr}_{V_{+}}Y$, which takes the values $0, \pm 2, \pm 4, \pm 6$ and vanishes for exactly $8$ of the $32$ sign patterns. The four anomaly conditions of Fact \claimref{standard-model.imported-anomaly-coefficients}, with the colour cubic, hold for exactly two of the $32$ sign patterns, both among those $8$: the complementary pair $\pm(-1)^{n+k}$ of Theorem \claimref{synthesis.cpt-closure-forces-slot-module-and-chirality}(4). On the $8$ patterns with $\operatorname{tr}_{V_{+}}Y = 0$ the constant vanishes and $\varphi_{C}$ is an exact isomorphism of the gauge currents, the energy and the sea, so six anomalous patterns are not distinguished from the two anomaly-free ones. Hence the linear anomaly condition is visible along one generator (the sea's hypercharge, the $Y$-$N$ mixed level) and the cubic conditions are not; no trace quadratic in $\mathfrak{g}$ sees either. With the rotation weights the cubic ones are visible too: if the sixteen channels of $V_{+}$ carry one weight $w_{0}$, each anomaly coefficient is a weighted trace, linear for the mixed gravitational condition and cubic for the others, such as $\sum_{x}(w_{x}/w_{0})Y_{x}$ and $\sum_{x}(w_{x}/w_{0})Y_{x}^{3}$, which $\varphi_{C}$ preserves, while every trace quadratic in $\mathfrak{g}$ (every level) is blind to the weights.
\item[(iv)] \emph{(The abelian normalisation.)} With the stored $Y$, $\operatorname{tr}_{V_{+}}T_{3}^{2} = 2$, $\operatorname{tr}_{V_{+}}Y^{2} = \tfrac{10}{3}$, $\operatorname{tr}_{V_{+}}Q^{2} = \tfrac{16}{3}$ for $Q = T_{3} + Y$; relative to the trace form of the five modes the level of every factor, the abelian one included, is $4$; for the integral charges $6Y$ (greatest common divisor $1$) the abelian trace is $120$, and for $3Q$ it is $48$. A rescaling $Y \mapsto \lambda Y$ multiplies the abelian level by $\lambda^{2}$: it is a number only after a normalisation is chosen, while the ratios $\operatorname{tr}T_{3}^{2} : \operatorname{tr}Y^{2} : \operatorname{tr}Q^{2} = 3 : 5 : 8$, so $\operatorname{tr}T_{3}^{2}/\operatorname{tr}Q^{2} = \tfrac38$, are fixed.
\end{enumerate}
All clauses are proved. \emph{Reading (argued).} The statement that the Standard Model gauge algebra acts inside exact $\uu(16)$ level-one channel currents per light ray and generation holds as far as it goes: the channels are complex with the unit $J$, the gauge currents are pair currents, and no gauge generator connects the two chirality arrays of a light ray, because $\mathfrak{g}$ acts on the internal index while the chirality and the rotation about the generator act on the spinor values (\claimref{synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays}(iii), (iv)); reading the conjugate components in the other array is $\varphi_{C}$. Its exactness is that of the stored window identity: exact as an operator identity with edge terms, the central term exact on edge-clean vectors. What it carries of the anomaly content is only the linear part: four-dimensional anomaly cancellation has one linear condition, seen along a generator as the sea's hypercharge and the $Y$-$N$ central term, and cubic conditions that need the channel weights; on the eight sign patterns with $\operatorname{tr}Y = 0$ the gauge currents with energy and sea are the same for anomalous and anomaly-free halvings. The abelian level is a convention, and the trace form is positive on $\mathfrak{g}$, so along one generator the central term of no gauge current vanishes.

## technical
The sixteen Weyl components of a generation give sixteen complex channels on a light ray, and the stored window identity makes their pair currents a level-one $\uu(16)$ current algebra, exact up to edge terms. The gauge algebra $\mathfrak{s}(\uu(2) \oplus \uu(3))$ of the slot module acts on a halving $V_{+}$ by matrices that are anti-Hermitian over $\mathrm{span}\{1, J\}$ and preserve each isotypic component, so its currents are pair currents in $\uu(16)$, never pair-creation terms of $\so(32)$; and since it acts on the internal index while chirality acts on the spinor values, no gauge generator mixes the two chirality arrays. On a conjugate pair of components the matrices are $M$ and $-M^{T}$ in dual bases. The particle-hole reversal of the channels of some components, $a^{*}_{x,k} \mapsto a_{x,L-1-k}$, is an inner automorphism of the window algebra (a product of vectors); it fixes the energy with half-integer weights, the sea and the edge-clean vectors, maps the gauge currents of one halving exactly to those of the halving with those components conjugated, up to a constant in the hypercharge zero mode, and reverses the channels' rotation weights. So all $32$ gauge-commuting CPT halvings have the same trace form $4\operatorname{tr}_{5}$ (traces $2$, $2$, $\tfrac{10}{3}$ of $T_{3}^{2}$, a colour Cartan generator squared, $Y^{2}$), and the same gauge currents, energy and sea up to the hypercharge constant. That constant is not harmless: it is the change of the sea's hypercharge, $\tfrac{L}{2}\operatorname{tr}Y$, and $\operatorname{tr}Y$ is also the mixed central term of the hypercharge and number currents in $\uu(16)$, the mixed gravitational anomaly coefficient, nonzero for $24$ of the $32$ patterns. Among the $8$ with $\operatorname{tr}Y = 0$ the structures are isomorphic, and only $2$ are anomaly-free. So the linear anomaly condition is seen along a generator and the cubic ones are not; no level of $\mathfrak{g}$ sees either, and the cubic coefficients are cubic traces weighted by the rotation weights. The abelian level depends on the normalisation of $Y$ ($\tfrac{10}{3}$ with the stored $Y$, $4$ relative to the five modes, $120$ for integral charges $6Y$); the ratios $3 : 5 : 8$ of the traces of $T_{3}^{2}$, $Y^{2}$, $Q^{2}$ are fixed.

## lay
Along a single light ray on a horizon, the sixteen kinds of particle in one generation of matter behave like sixteen independent lanes of traffic, and the forces of the Standard Model rotate the lanes into one another. One can ask whether this one-dimensional picture knows the most delicate consistency condition of the Standard Model, that the quantum anomalies cancel within each generation. It knows only the simplest part of it. Swapping particles and holes on some of the lanes, an exact symmetry of the one-dimensional picture apart from a shift in the total hypercharge of the filled lanes, turns a consistent generation into one of thirty-two arrangements of which thirty are inconsistent. The picture sees that shift, which is the simplest of the consistency conditions, but it cannot tell apart the eight arrangements whose total hypercharge is zero, six of them inconsistent. The remaining conditions become visible only when one also keeps track of how each lane turns about the light ray. The strength of the abelian force in this picture is also not a fixed number: it depends on a choice of units, and only ratios between forces are fixed.

## one-liner
The gauge currents of a generation along a light ray are complex pair currents in u(16) with no chirality mixing; a particle-hole reversal makes them, with energy and sea, the same for all 32 gauge-commuting halvings up to a hypercharge constant equal to tr Y, which sees the mixed gravitational condition (8 of 32 pass), while no quadratic datum sees the cubic conditions (2 of those 8 are anomaly-free); the abelian level is a normalisation.
