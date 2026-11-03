---
id: synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise
kind: claim
version: 3
title: A quasi-free deposit on the fermionic boundary-mode algebra is its vacuum plus shot noise, whatever its correlation range or partner placement; for the I-state, or any quasi-free deposit with at least one thermal species' number of quanta at thermal energies, the shot term at the pivot is below $10^{-77}$
status: proved
region: synthesis
subject: dark-energy
tags: [no-go, confronted-with-data, car-algebra, modular-theory]
proposed_by:
  kind: ai
  session: 2026-10-31-all-open
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
derivations:
- name: main
  uses:
  - hawking.imported-quasi-free-states-car-algebra@2
  - hawking.i-state@3
  - synthesis.quadratic-flows-cannot-thermalise-descent@1
  - singularity.descent-parity-average@4
  - singularity.imported-descent-one-way-conditional-expectation@7
  - synthesis.finite-range-descent-deposit-cannot-seed-cmb@4
  - synthesis.frozen-point-geometry-reads-descent-as-vacuum@1
  - synthesis.imported-planck-2018-lcdm-parameters@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_wick_variance_on_fock_space
- kind: check
  ref: check.py::check_shot_noise_bound_and_its_proof_steps
- kind: check
  ref: check.py::check_bound_with_pairing_and_the_pure_pair_states
- kind: check
  ref: check.py::check_descent_parity_average
- kind: check
  ref: check.py::check_shot_term_at_the_pivot
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.finite-range-descent-deposit-cannot-seed-cmb
  - synthesis.frozen-point-geometry-reads-descent-as-vacuum
  - synthesis.quadratic-flows-cannot-thermalise-descent
  - standard-model.dating-descent
extraction:
  open_problem: op.descent-state-and-spectrum
  note: >-
    Answer to the open problem's first two lines of attack (an occupation law n_k proportional to
    k^(n_s - 3) compatible with the descent's one-way conditional expectation; a deposit of pure
    pairs restricting to the I-state with partner placement set before the metric). Both are
    deposits that are quasi-free states of the boundary-mode CAR algebra: the I-state is
    quasi-free and gauge-invariant (Theorem hawking.i-state), the pure pair states of the
    quadratic-flows result are pure quasi-free states of mode and partner, and quasi-freeness is
    kept by restriction and by quadratic flows. For every such state the fluctuation of every
    bilinear observable is that of a pure reference state (the vacuum) plus at most the square
    root of the number of quanta the observable sees, weighted by the observable: fermion
    statistics caps long-range order at the shot-noise level, so the correlation range and the
    partner placement drop out of the amplitude. The size of the shot term depends on the
    occupation profile only through the density of quanta nbar and their energy spread c_k: it is
    (3 c_k k^3/(2 pi^2 nbar))^(1/2) in amplitude. For the I-state, or any quasi-free deposit with at
    least one thermal Weyl species' number of quanta (comoving number fixed by entropy conservation
    to today) and c_k <= 1.31, about 10^80 quanta sit in a pivot volume and the shot term is below
    1e-77 against A_s = 2.1e-9, for every reheating temperature. A sparse deposit (of order one
    quantum per pivot volume) or an energetically broad one is bounded only by the formula, which
    then allows order-one contrast; such a deposit would have to reach today's radiation without
    conserving entropy, so the record does not fix its number. The descent's one-way conditional
    expectation, the parity average over one ladder mode, adds only a region-independent constant.
    Also outside the bound: deposits that are not quasi-free (a classical mixture over a field
    that modulates the deposit's local energy, whose variance of local means is not bounded here,
    or an entangled non-Gaussian state; a two-component cat mixture breaks the bound in the
    check), and quanta of a bosonic field outside the CAR algebra with occupations far above one.
    Every state rule the series states for boundary modes ((N+), the I-state, the
    maximum-entropy clause of (Q)) is quasi-free (argued); a non-Gaussian frozen vacuum of bosonic
    face modes in the families sector would lie outside the class and, if it were deposited at the
    descent, would carry super-shot variance; nothing stored decides whether it is deposited there.
    The bound concerns the fermion modes' energy; relative to the total energy density their
    contribution to the contrast is smaller still, and other components are not bounded here.
    Transport-convenient: the CAR algebra is the Clifford algebra of the Majorana generators, its
    bilinears are the bivectors and a pure quasi-free state is a complex structure; the inequality
    is a triangle inequality for the commutator with that complex structure. The Fermi-Dirac
    moments, entropy conservation from the descent to today and the vacuum's energy-density
    scaling are standard (from memory).
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2: a marked pointer note after the formal statement sends the classical-modulation escape to synthesis.adiabatic-deposit-modulation-is-a-time-shift and synthesis.local-conversion-cannot-redden-a-gaussian-spectator (closed for Gaussian modulators), as claimrefs, not edges, since both results use this one. The pins to the Planck parameters and to synthesis.finite-range-descent-deposit-cannot-seed-cmb moved to their versions 2 and 4 (the added densities and the added pointer note are not used here). No clause changed.'
  maintainer_pass_deposit_state:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2 -> 3, at Leon''s decisions of 2026-11-01 (deposit state, as restated in the final round): a marked note after the pointer note records that the vacuum of (ii) and (iv), any pure quasi-free state here, must be one over which the deposit is Hadamard if the deposit is to be Hadamard; for a massive Dirac field the instantaneous vacuum where ma'' is nonzero, and every deposit diagonal over it, are not Hadamard, and the shot-noise count does not decide the Hadamard property (claimrefs to the massive-Dirac and occupation-moment results, which use this one). No clause changed.'
---
## formal
Let $\CAR$ be the CAR algebra of $n$ fermionic modes $a_{1}, \dots, a_{n}$, equivalently the complexified Clifford algebra of the $2n$ Majorana generators $a_{j} + a_{j}^{\dagger}$, $i(a_{j}^{\dagger} - a_{j})$, whose quadratic elements are its bivectors. Write $\alpha = (a_{1}, \dots, a_{n}, a_{1}^{\dagger}, \dots, a_{n}^{\dagger})$ and, for a state $\omega$, $\Gamma_{IJ} = \omega(\alpha_{J}^{\dagger}\alpha_{I})$, so $0 \le \Gamma \le 1$; $\omega$ is quasi-free when its truncated functions beyond second order vanish (Fact \claimref{hawking.imported-quasi-free-states-car-algebra}), and a quasi-free state is pure exactly when $\Gamma^{2} = \Gamma$. A quadratic Hermitian element is $O = \tfrac12\alpha^{\dagger}F\alpha$ with $F$ Hermitian of the particle-hole form; for a gauge-invariant state and a number-conserving $O = N_{f} = \sum_{ij}f_{ij}a_{i}^{\dagger}a_{j}$ these reduce to the one-particle density $E_{ij} = \omega(a_{j}^{\dagger}a_{i})$ and $f$. Write $\mathrm{sd}_{\omega}(O) = \mathrm{Var}_{\omega}(O)^{1/2}$.
\begin{enumerate}
\item[(i)] \emph{(Variance.)} For every quasi-free $\omega$, $\mathrm{Var}_{\omega}(O) = \tfrac12\Tr\bigl(F\Gamma F(1 - \Gamma)\bigr)$, and $\mathrm{Var}_{\omega}(O) = \tfrac14\|[F, \Gamma]\|_{2}^{2}$ when $\omega$ is pure; for gauge-invariant $\omega$, $\mathrm{Var}_{\omega}(N_{f}) = \Tr\bigl(fEf(1 - E)\bigr)$.
\item[(ii)] \emph{(Vacuum plus shot noise.)} Let $\omega_{0}$ be any pure quasi-free state (the vacuum), $\Gamma_{0}^{2} = \Gamma_{0}$, and $N_{0}$ the number operator of its quasi-particles, $N_{0} = \tfrac12\alpha^{\dagger}(1 - 2\Gamma_{0})\alpha + \tfrac n2$. Then for every quasi-free $\omega$ and every $O$,
\[
\mathrm{sd}_{\omega}(O) \;\le\; \mathrm{sd}_{\omega_{0}}(O) + \Tr\bigl(F^{2}X\bigr)^{1/2}, \qquad X = (\Gamma - \Gamma_{0})^{2} + \Gamma(1 - \Gamma) \ge 0, \qquad \Tr X = 2\,\omega(N_{0}).
\]
$X$ is the system block of $(\widetilde\Gamma - \widetilde\Gamma_{0})^{2}$ for every quasi-free purification $\widetilde\Gamma$ of $\Gamma$, so $\Tr(F^{2}X)$ is the $F^{2}$-weighted count of the quanta of $\omega$ above $\omega_{0}$. In the gauge-invariant case $\mathrm{sd}_{\omega}(N_{f}) \le \mathrm{sd}_{\omega_{0}}(N_{f}) + \bigl(2\Tr(f^{2}X_{E})\bigr)^{1/2}$ with $X_{E} = (E - E_{0})^{2} + E(1 - E)$ and $\Tr X_{E} = \Tr(E(1 - E_{0})) + \Tr((1 - E)E_{0})$, the number of particles plus holes. The bound uses quasi-freeness: the mixture of the empty and the filled state of five modes, which is not quasi-free, violates it.
\item[(iii)] \emph{(The descent's conditional expectation.)} Let $E_{\mathrm{d}}(x) = \tfrac12(x + \sigma x\sigma)$ be the parity average over one ladder mode $a_{0}$ (Theorem \claimref{singularity.descent-parity-average}, the one-way conditional expectation of Fact \claimref{singularity.imported-descent-one-way-conditional-expectation}), $\sigma = 1 - 2a_{0}^{\dagger}a_{0}$. For every state $\omega$, $\sigma O\sigma = \tfrac12\alpha^{\dagger}SFS\alpha$ with $S$ the sign flip of $a_{0}$, and
\[
\mathrm{Var}_{\omega\circ E_{\mathrm{d}}}(O) = \tfrac12\mathrm{Var}_{\omega}(O) + \tfrac12\mathrm{Var}_{\omega}(\sigma O\sigma) + \tfrac14 D^{2}, \qquad D = \omega(O) - \omega(\sigma O\sigma), \qquad D^{2} \le 8\sum_{I \in K,\, J \notin K}|F_{IJ}|^{2},
\]
$K$ the two Nambu indices of $a_{0}$. Since $\omega \circ \mathrm{Ad}\,\sigma$ is quasi-free whenever $\omega$ is, (ii) bounds both variances, and the descent adds at most a constant fixed by the couplings of $O$ to the one ladder mode, independent of the region $O$ samples.
\item[(iv)] \emph{(On observed scales.)} Let the deposit on the descent slice be a homogeneous, gauge-invariant quasi-free state of the fermion modes, with density of quanta $\bar n$ (particles plus antiparticles, comoving) above the descended vacuum, and let $\delta$ be the contrast of the energy those modes carry, with $\Delta_{\delta}^{2}(k)$ and $\Delta_{\delta, \mathrm{vac}}^{2}(k)$ its dimensionless spectra in the deposit and in the vacuum. Then for every $k$
\[
\Delta_{\delta}^{2}(k)^{1/2} \;\le\; \Delta_{\delta, \mathrm{vac}}^{2}(k)^{1/2} + \Bigl(\frac{3c_{k}k^{3}}{2\pi^{2}\bar n}\Bigr)^{1/2}, \qquad c_{k} = \frac{\langle(\omega_{p} + k)^{2}\rangle}{\langle\omega_{p}\rangle^{2}},
\]
the means taken over the quanta. For the I-state at $T_{d}$ (Fermi-Dirac quanta, Theorem \claimref{hawking.i-state}) $c_{k} < 1.31$ on observed scales; with $\bar n$ at least that of one Weyl species, $\tfrac{3\zeta(3)}{2\pi^{2}}(a_{d}T_{d})^{3}$, and entropy conserved from the descent to today with $g_{s} \le 10^{4}$ at the descent, the shot term at the pivot $k_{*} = 0.05\ \mathrm{Mpc}^{-1}$ (Fact \claimref{synthesis.imported-planck-2018-lcdm-parameters}) is below $10^{-77}$ for every $T_{d}$, more than $10^{68}$ below $A_{s}$. The same bound holds for these modes' contribution to the contrast of the total energy density, which exceeds theirs. For a sparse or energetically broad deposit the bound is only the displayed formula: with of order one quantum per pivot volume it allows a contrast of order one.
\end{enumerate}
Consequently no quasi-free state of the boundary-mode algebra deposited at the descent differs from the descended vacuum by more than its shot noise, whatever its correlation range or the placement of the partners of its pairs (anywhere on the slice, before or after the metric): the range and the placement drop out, and the shot term is fixed by the density of quanta and their energy spread alone. For the I-state, and for any occupation profile with at least one thermal species' number of quanta and energy spread $c_{k} \le 1.31$, the deposit's spectrum differs from the vacuum's by less than $10^{-38}$ in amplitude at the pivot, and the descent's parity average does not change this; a sparse or energetically broad deposit is bounded only by $(3c_{k}k^{3}/2\pi^{2}\bar n)^{1/2}$. Beyond the bound lie states that are not quasi-free (a mixture over a field modulating the deposit's local energy, or an entangled non-Gaussian state) and quanta of a bosonic field outside the CAR algebra with occupations far above one.

\emph{Note (pointer).} The first escape, a classical modulation of the deposit by a field, is narrowed by two later results: such a modulation is adiabatic only along a local time shift of the one descent (Proposition \claimref{synthesis.adiabatic-deposit-modulation-is-a-time-shift}), and a local conversion of a Gaussian modulating field cannot lower its index, so under hypothesis (F) a Gaussian modulator read through the frozen point's invariant state gives index $2$ up to corrections of order $(k|x_{d}|)^{-2}$ (Proposition \claimref{synthesis.local-conversion-cannot-redden-a-gaussian-spectator}). The classical-modulation escape is closed for Gaussian modulators and stays open only for a red or non-Gaussian one.

\emph{Note (the vacuum and the Hadamard condition; added 1 November).} The bound holds for any pure quasi-free vacuum $\omega_{0}$, but a deposit meant to be a physical state of the descended fields must be Hadamard, and the choice of $\omega_{0}$ then matters: the deposit must be Hadamard as a whole, which its count of quanta above $\omega_{0}$ does not decide. For a massive Dirac field on a Robertson-Walker field, at an instant where $ma' \neq 0$ the instantaneous vacuum is not Hadamard, and neither is any deposit diagonal over it, whatever its occupations, although it has finitely many quanta above an adiabatic state of infinite order (Theorem \claimref{synthesis.massive-dirac-instantaneous-vacuum-and-non-smooth-descents-are-not-hadamard}, given Hollands' theorem that such adiabatic states are Hadamard). For the massless Dirac field over the conformal vacuum, on a Robertson-Walker field with smooth scale factor, a diagonal deposit is Hadamard exactly when every moment of its occupation profile is finite, while the number and energy spread of the quanta, the data of (iv), do not decide it (Theorem \claimref{synthesis.deposit-over-the-conformal-vacuum-is-hadamard-exactly-when-every-occupation-moment-is-finite}). The shot-noise bound itself is unaffected.

## technical
The question left by the stored results was whether the descent's deposited occupation numbers $n_{k}$, or pure pairs whose partners are placed before the metric, could carry the measured spectrum: the finite-range bound (Proposition \claimref{synthesis.finite-range-descent-deposit-cannot-seed-cmb}) excludes short-range deposits, and the frozen point's geometry (Proposition \claimref{synthesis.frozen-point-geometry-reads-descent-as-vacuum}) supplies range but reads every invariant state as the vacuum. Both leave the occupation numbers free. They are not free in amplitude. The I-state lives on a CAR algebra, and for a quasi-free state of a CAR algebra the variance of a bilinear observable is $\tfrac12\Tr(F\Gamma F(1 - \Gamma))$, a quantity that the Pauli bound $0 \le \Gamma \le 1$ keeps of the order of the number of quanta the observable sees. Made precise: purify the state (a quasi-free state is the restriction of a pure one on a doubled algebra; in the gauge-invariant case the purification $\bigl(\begin{smallmatrix}E & \sqrt{E(1 - E)} \\ \sqrt{E(1 - E)} & 1 - E\end{smallmatrix}\bigr)$ is explicit), use $\mathrm{Var} = \tfrac14\|[F, \widetilde\Gamma]\|_{2}^{2}$ for pure states and the triangle inequality against the vacuum's projector; the difference of the two projectors, squared, has system block $X = (\Gamma - \Gamma_{0})^{2} + \Gamma(1 - \Gamma)$ whatever the purification, and its trace counts the quanta. The Clifford reading is direct: the Majorana generators span a Euclidean space, quadratic observables are bivectors, a pure quasi-free state is a complex structure, and the variance of a bivector is the norm of its commutator with that complex structure.

For a homogeneous deposit the observable is the cosine (or sine) moment of the energy density over a comoving box; $\Tr(F^{2}X)$ is then at most $\tfrac34 V\int(\omega_{p} + k)^{2}x_{p}\,d^{3}p/(2\pi)^{3}$ with $x_{p}$ the density of quanta at momentum $p$, and the relative contrast's spectrum is bounded by the vacuum's plus $3c_{k}/(2\bar n)$ in $P(k)$: white noise at the level of the number of quanta, index $3$, the finite-range class whatever the range of the correlations. The number of quanta per pivot volume is fixed by the record: entropy conservation makes $a_{d}T_{d}$ a fixed multiple of $a_{0}T_{0}$, and $k_{*}/a_{0}T_{0} = 1.36 \times 10^{-27}$, so the shot term is independent of the reheating temperature and below $10^{-77}$. The descent's conditional expectation is a mixture of the state and its image under the flip of one ladder mode; the mixture adds the square of half the difference of the two means, which involves only the observable's couplings to that mode. The bound is not a statement about all states: it fails for a cat mixture of the empty and filled states (variance $25/4$ against a bound of $5$ on five modes), and it does not hold for bosonic quasi-free states, whose variance $\Tr(fEf(1 + E))$ grows with the occupations. So the result removes correlation range and partner placement as carriers of the amplitude for every quasi-free fermionic deposit, removes the thermal-density deposits (the I-state among them) outright, and names what is left: a sparse or energetically broad quasi-free deposit whose number of quanta the record does not fix (it would not conserve entropy on the way to today's radiation), a classical modulation of the deposit (a mixture whose local means vary on observed scales), a non-Gaussian entangled deposit, or a bosonic field with occupations far above one. The bound is on the fermion modes' energy; their share of the total contrast is smaller still.

## lay
The remaining hope for explaining the cosmic ripples from the descent was that it might have left the newborn universe's particles in some special pattern of occupation, correlated over vast distances. This result shows that, for the fermionic particles the theory starts from and for the whole family of states the theory uses (the thermal I-state, and pure pairs of particles and partners placed however one likes), the reach of the correlations does not help: only the number of particles matters, and for the thermal deposit the hope fails by an enormous margin. The reason is the exclusion principle: no mode can hold more than one fermion, so the number of particles in a region can fluctuate only by about the square root of the number present, however the particles are correlated. For the hot, thermal deposit the theory states (and for any deposit as dense as that), a region the size of the observed ripples holds about $10^{80}$ particles, so the fluctuations are about $10^{-40}$, against the measured $5 \times 10^{-5}$. A deposit with very few particles would fluctuate more; it would have to turn into today's radiation in a way that creates entropy, and the record does not say how many particles it had. The ripples, if the descent made them, must come from something of another kind: a field that varies the deposit itself from place to place, or a bosonic field in a highly excited state.

## one-liner
For every quasi-free state of a CAR algebra and every bilinear observable, $\mathrm{sd}_{\omega}(O) \le \mathrm{sd}_{\omega_{0}}(O) + \Tr(F^{2}X)^{1/2}$ with $X = (\Gamma - \Gamma_{0})^{2} + \Gamma(1 - \Gamma)$, $\Tr X = 2\omega(N_{0})$: if a deposit is quasi-free it is the vacuum plus shot noise whatever its correlation range or partner placement, and the descent's parity average adds a region-independent constant; for the I-state, or any occupation profile with at least one thermal species' number of quanta and energy spread $c_{k} \le 1.31$, the shot term at the pivot is below $10^{-77}$ for every reheating temperature, far below $A_{s} = 2.1 \times 10^{-9}$, while a sparse or energetically broad deposit is bounded only by $(3c_{k}k^{3}/2\pi^{2}\bar n)^{1/2}$.
