---
id: synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves
kind: claim
version: 1
title: Exact window Sugawara identity and Luttinger normal modes of tower density waves
status: proved
region: synthesis
subject: quantum-fields
tags: [bosonisation, car-algebra, limits]
proposed_by:
  kind: ai
  session: 2026-11-07-boson-items
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: run 2026-11-07-boson-items
review: draft
about:
- obj.tower.tower
derivations:
- name: main
  uses:
  - std-algebra.witt-basis-car@1
  - hawking.current-commutator-exactly-edge-split@4
  - synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum@1
  - synthesis.null-vacuum-on-a-horizon-generator@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_window_sugawara_identity_holds_as_an_algebra_identity
- kind: check
  ref: check.py::check_linear_dispersion_and_the_phase_flow_with_the_kernel_unit
- kind: check
  ref: check.py::check_band_compression_of_the_null_momentum_has_half_integer_weights
- kind: check
  ref: check.py::check_luttinger_normal_modes_on_edge_clean_vectors
- kind: proof
  derivation: main
extraction:
  open_problem: bos.dynamics
  note: >-
    Attack on the target bos.dynamics: the dynamics of the density-wave bosons of the tower (Sugawara form, linear
    dispersion, solvable density-density interaction), derived in the Clifford algebra of the tower planes. The store
    held the Sugawara construction only as an imported conformal-field-theory Fact
    (dark-energy.imported-conformal-orthogonality-sugawara-construction); it is not a premise here. Stored and used:
    the current algebra with its edge split (hawking.current-commutator-exactly-edge-split), the density modes of a
    window and the canonical relations on the domain D of finite excitations of the band of the null vacuum
    (synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum (v), (vi)), and the null
    vacuum itself (synthesis.null-vacuum-on-a-horizon-generator). New to the store: (i) the Sugawara (Kronig) identity holds on
    every finite window as an identity in the algebra, with no edge correction: sum_q rho_q* rho_q =
    sum_j j n_j - Nhat(Nhat - 1)/2, equivalently H = Q^2/2 + sum_q rho_q* rho_q for the half-integer weights about the
    sea; the edge operators that spoil the canonical commutator on a window cancel in this ordering; and an energy
    sum_j eps_j n_j is a multiple of sum_q rho_q* rho_q plus a function of the number exactly when eps is affine;
    (ii) linear dispersion and the phase flow of the density modes with the kernel unit J of a tower level; (iii) the
    compression of the null momentum P to the band modes has the half-integer weights Delta (k + 1/2), the null
    vacuum's window sea is the ground state of the compressed energy, and on D the infinite-band energy is
    Q^2/2 + sum_q rho_q* rho_q; (iv) a Luttinger-type density coupling between two families of modes of opposite
    orientation, with coupling constants on finitely many wave numbers, keeps the Heisenberg equations of the density
    modes linear on D, with real normal modes and frequencies q sqrt((1 + g4)^2 - g2^2), and on windows exactly on the
    edge-clean vectors. Prior art, not premises: the identity H = Q^2/2 + sum rho* rho on the infinite filled sea is
    the Kronig identity of bosonisation (R. de L. Kronig, Physica 2 (1935) 968-980, cited from memory) and the Sugawara
    construction (H. Sugawara, Phys. Rev. 170 (1968) 1659-1662, cited from memory); the solution of the
    density-coupled model is D. C. Mattis and E. H. Lieb, J. Math. Phys. 6 (1965) 304-312 (as cited in the stored
    Fact synthesis.imported-schwinger-term-and-mattis-lieb-density-algebra) and F. D. M. Haldane, J. Phys. C 14 (1981)
    2585-2609 (cited from memory). For finitely many fermions on levels bounded below the identity is in K. Schoenhammer and V. Meden,
    Fermion-boson transmutation and comparison of statistical ensembles in one dimension, Am. J. Phys. (1996),
    doi:10.1119/1.18339, eq. (38); the window form, with an upper cut-off as well, follows by the same antisymmetry
    and is new to the store, not to the literature. The half-integer offset of the weight clause of singularity.q-joint-quasi-freeness-s-wave
    (version 3), read in the store as a reading of the modes as spinors of boost weight 1/2, appears in (iii) as the
    band centre of the compression; this is recorded, not used to change that premise. Not claimed: the compression in
    (iii) is not invariant under the null translations (the band modes are not eigenvectors of P), so (iii) is a
    statement about the compressed energy and the null vacuum restricted to the band modes, not about the full
    dynamics of the generator; the families of (iv) are not identified with particular generators; no gauge boson is
    constructed. Ledger: (i), (ii) and (iv) are transport-absent (finite CAR algebra of tower planes); (iii) is
    transport-convenient (the generator's mode space and its null vacuum).
---

## formal
Let a window carry $L$ tower planes with null pairs $v_{j} = \tfrac12(e_{j} + f_{j})$, $w_{j} = \tfrac12(e_{j} - f_{j})$, $Q(e_{j}) = 1$, $Q(f_{j}) = -1$, $j = 0, \dots, L - 1$, the Witt pairs of Theorem \claimref{std-algebra.witt-basis-car} read with $v_{j}$ as creators, $n_{j} = v_{j}w_{j}$, $\hat N = \sum_{j}n_{j}$, $*$ the adjoint ($v_{j}^{*} = w_{j}$), and the density modes $\rho_{q} = \sum_{j = 0}^{L - 1 - q}v_{j}w_{j + q}$, $1 \le q \le L - 1$, of Theorem \claimref{hawking.current-commutator-exactly-edge-split} (each lowers the level index by $q$). Let $T = \sum_{q = 1}^{L - 1}\rho_{q}^{*}\rho_{q}$.
\begin{enumerate}
\item[(i)] \emph{(Window Sugawara identity.)} For every $L$, exactly,
\[
T = \sum_{j}j\,n_{j} - \tfrac12\hat N(\hat N - 1).
\]
For $L = 2M$, with $k = j - M$, the half-integer weights $k + \tfrac12$, the sea $k < 0$ filled, $H = \sum_{k}(k + \tfrac12)n_{k} + \tfrac12M^{2}$ and $\mathcal{Q} = \hat N - M$, this reads $H = \tfrac12\mathcal{Q}^{2} + T$: $H$ vanishes on the sea and is at least $\tfrac12\mathcal{Q}^{2}$. There is no edge correction, although $[\rho_{q}, \rho_{q}^{*}]$ is the edge operator of the stored result. An energy $\sum_{j}\varepsilon_{j}n_{j}$ equals $aT + g(\hat N)$ for a real $a$ and a function $g$ if and only if $\varepsilon_{j} = aj + b$.
\item[(ii)] \emph{(Linear dispersion and the phase flow.)} $[H, \rho_{q}^{*}] = q\rho_{q}^{*}$ and $[H, \rho_{q}] = -q\rho_{q}$ exactly. In a tower level $\Cl(L, L + 2)$ with kernel bivector $J = g_{1}g_{2}$ ($J^{2} = -1$, commuting with every plane generator), $e^{JtH} = e^{JtM^{2}/2}\prod_{k}\bigl(1 + (e^{Jt(k + 1/2)} - 1)n_{k}\bigr)$ is unitary for real $t$ and $e^{JtH}\rho_{q}^{*}e^{-JtH} = e^{Jqt}\rho_{q}^{*}$: every density wave of wave number $q$ turns at frequency $q$ with the unit $J$, whatever its position in the window.
\item[(iii)] \emph{(The band of the null vacuum.)} On a horizon generator, with $P = I_{4}\,d/du$, the null vacuum $\omega_{0}$ of Theorem \claimref{synthesis.null-vacuum-on-a-horizon-generator} and the band modes $g_{k} = h_{k}\otimes\eta$ of width $\Delta$ of Theorem \claimref{synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum}(vi), $\ip{g_{k}}{Pg_{l}} = \delta_{kl}\Delta(k + \tfrac12)$: the compression of $P$ to the span of the band modes has the half-integer weights $\Delta(k + \tfrac12)$, and on the window $k = -M, \dots, M - 1$ its second quantisation is $\Delta\sum_{k}(k + \tfrac12)n_{k} = \Delta(H - \tfrac12M^{2})$. The restriction of $\omega_{0}$ to the window is the sea, the ground state of $H$, with $\mathcal{Q} = 0$ and $\rho_{q}$ annihilating it. On the domain $\mathcal{D}$ of finite excitations of the infinite band, $H_{\infty} = \sum_{k \ge 0}(k + \tfrac12)n_{k} - \sum_{k < 0}(k + \tfrac12)(1 - n_{k})$ and $\mathcal{Q}_{\infty} = \sum_{k \ge 0}n_{k} - \sum_{k < 0}(1 - n_{k})$ are finite sums on each vector, and on $\mathcal{D}$
\[
H_{\infty} = \tfrac12\mathcal{Q}_{\infty}^{2} + \sum_{q \ge 1}\rho_{q}^{*}\rho_{q} = \tfrac12\mathcal{Q}_{\infty}^{2} + \sum_{q \ge 1}q\,b_{q}^{*}b_{q}, \qquad b_{q} = \rho_{q}/\sqrt q ,
\]
with $[b_{q}, b_{q'}^{*}] = \delta_{qq'}$ on $\mathcal{D}$: in each charge sector the energy is that of free bosons of frequency $q$.
\item[(iv)] \emph{(Luttinger coupling.)} Take two families of window modes, $R$ with weights $k + \tfrac12$ and sea $k < 0$, and $L$ with weights $-(k + \tfrac12)$ and sea $k \ge 0$, with density modes $\rho_{R, q} = \sum_{k}v_{R, k}w_{R, k + q}$ and $\rho_{L, q} = \sum_{k}v_{L, k + q}w_{L, k}$, both lowering the energy by $q$. For a finite set $S$ of wave numbers and real $g_{4, q}$, $g_{2, q}$ ($q \in S$) with $|g_{2, q}| < 1 + g_{4, q}$, let
\[
H = H_{R} + H_{L} + \sum_{q \in S}\Bigl[g_{4, q}\bigl(\rho_{R, q}^{*}\rho_{R, q} + \rho_{L, q}^{*}\rho_{L, q}\bigr) + g_{2, q}\bigl(\rho_{R, q}\rho_{L, q} + \rho_{L, q}^{*}\rho_{R, q}^{*}\bigr)\Bigr],
\]
$r_{q}$ the root of $g_{2, q}r^{2} - 2(1 + g_{4, q})r + g_{2, q} = 0$ with $|r_{q}| < 1$, $\beta_{q}^{*} = \rho_{R, q}^{*} + r_{q}\rho_{L, q}$, $\gamma_{q}^{*} = \rho_{L, q}^{*} + r_{q}\rho_{R, q}$ and $\omega_{q} = q\sqrt{(1 + g_{4, q})^{2} - g_{2, q}^{2}}$. On the domain $\mathcal{D}$ of finite excitations of both infinite seas, $H$ maps $\mathcal{D}$ into itself and
\[
[H, \beta_{q}^{*}] = \omega_{q}\beta_{q}^{*}, \qquad [H, \gamma_{q}^{*}] = \omega_{q}\gamma_{q}^{*} ;
\]
the Heisenberg equations of the density modes close linearly, with real coefficients. On finite windows the same relations hold exactly on every vector whose two families are edge-clean at depth $\max S$, and do not hold on every vector off that subspace (the check exhibits one where they fail; on others, such as the vector with both families empty, they still hold).
\end{enumerate}
All clauses are proved. \emph{Reading.} The kinetic energy of fermions with linear dispersion is already, on every finite window and with no edge correction, the quadratic form of the density waves plus the charge term $\tfrac12\mathcal{Q}^{2}$; the finite size shows only in the commutators of the density modes, not in this energy. Density-density couplings keep the dynamics quadratic in the density waves and so solvable.

## technical
On a window of tower planes, let $\rho_{q}$ move one fermion $q$ levels down. The sum $T = \sum_{q}\rho_{q}^{*}\rho_{q}$ equals $\sum_{j}j\,n_{j} - \tfrac12\hat N(\hat N - 1)$ exactly, as an identity in the algebra, on every window: the kinetic energy of fermions with equally spaced levels is the quadratic form of the density waves, and with the levels $k + \tfrac12$ about the sea it is $\tfrac12\mathcal{Q}^{2} + T$, the Sugawara (Kronig) form with the charge term. The finite window shows only in $[\rho_{q}, \rho_{q}^{*}]$, which is an edge operator; the energy identity itself has no edge term. The identity needs the linear dispersion: an energy is a multiple of $T$ plus a function of the number exactly when its levels are equally spaced.

Each density wave of wave number $q$ raises the energy by exactly $q$, wherever it sits, so with the kernel unit $J$ of a tower level the flow $e^{JtH}$ turns $\rho_{q}^{*}$ at frequency $q$. On a horizon generator, compressing the null momentum to the band modes of width $\Delta$ gives exactly the weights $\Delta(k + \tfrac12)$, the half-integer offset being the band centre; the null vacuum restricted to the bands is the sea, the ground state, and on the finite excitations of the infinite band the energy is $\tfrac12\mathcal{Q}^{2} + \sum_{q}q\,b_{q}^{*}b_{q}$ with canonical $b_{q}$.

Coupling two families of opposite orientation through their densities, with constants $g_{4}$ (within a family) and $g_{2}$ (between them) on finitely many wave numbers, keeps the Heisenberg equations of the densities linear; real normal modes $\rho_{R}^{*} + r\rho_{L}$ have frequencies $q\sqrt{(1 + g_{4})^{2} - g_{2}^{2}}$. On windows this holds exactly on the vectors that are edge-clean at the coupled depth.

## lay
Fermions on a line whose energy levels are equally spaced have a hidden description: their energy can be rewritten exactly as the energy of ripples in their density, plus a term that only counts how many fermions were added or removed. This is the core of how fermions in one dimension turn into bosons. The result shows that the rewriting holds exactly even for a finite stretch of levels, with nothing to correct at the ends, provided the spacing is even. Each ripple then carries an energy proportional to its wavelength number, which is what a sound wave does. When the ripples of two streams moving in opposite directions push on each other, the motion stays simple: new combined ripples form with a changed common speed (slower or faster, depending on the two couplings), and the problem can still be solved exactly. On a horizon line the lowest-energy state the series uses is the state with no ripples.

## one-liner
On every window of tower planes $\sum_{q}\rho_{q}^{*}\rho_{q} = \sum_{j}j\,n_{j} - \tfrac12\hat N(\hat N - 1)$ exactly, so $\sum_{k}(k + \tfrac12)n_{k} + \tfrac12M^{2} = \tfrac12\mathcal{Q}^{2} + \sum_{q}\rho_{q}^{*}\rho_{q}$ with no edge term; density waves have frequency $q$ (unit $J$), and a Luttinger density coupling gives real normal modes of frequency $q\sqrt{(1 + g_{4})^{2} - g_{2}^{2}}$.
