---
id: synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum
kind: claim
version: 1
title: Fluctuation forms of the tower and density-wave bosons of the null vacuum
status: proved
region: synthesis
subject: quantum-fields
tags: [bosonisation, car-algebra, ladder-pairs, limits, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-07-bosons
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: run 2026-11-07-bosons
review: draft
about:
- obj.tower.tower
derivations:
- name: main
  uses:
  - field-theory.imported-tower-limit@3
  - field-theory.how-close-tower-comes-ccr@4
  - field-theory.no-canonical-commutation-relations-tower@3
  - hawking.current-commutator-exactly-edge-split@4
  - synthesis.floor-regulator-keeps-the-charge-and-the-central-term-below-the-cut-off@3
  - synthesis.null-vacuum-on-a-horizon-generator@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_single_fermions_collect_into_one_fermion
- kind: check
  ref: check.py::check_hopping_ladder_is_the_particle_hole_image_of_the_pairing_ladder
- kind: check
  ref: check.py::check_block_commutators_and_their_values_in_product_states
- kind: check
  ref: check.py::check_block_form_rank_and_its_tracial_kernel
- kind: check
  ref: check.py::check_density_form_edge_operator_converse_and_product_values
- kind: check
  ref: check.py::check_null_vacuum_window_has_nondegenerate_density_and_block_forms
- kind: check
  ref: check.py::check_fluctuation_commutator_tends_to_the_form
- kind: check
  ref: check.py::check_finite_excitations_of_a_deep_sea_see_the_canonical_relation
- kind: check
  ref: check.py::check_product_state_is_the_quasi_free_state_of_its_symbol
- kind: proof
  derivation: main
extraction:
  note: >-
    From Leon's working document "From the Bit to the Numbers" (7 November 2026), Step 6 and objection 4 (bosons as
    collective modes of the tower), re-proved and re-checked here; not an attack on an open problem. Every step is
    derived in the algebra of the tower planes; no imported Fact is a premise. Stored already and cited: the pairing
    quasi-spin [b, b*] = 1 - 2k/n (field-theory.how-close-tower-comes-ccr; the hopping ladder of (ii) is derived here
    directly and is its image under particle-hole conjugation of one mode per block); the edge-operator form of the
    density commutator and its value min(p, 2N - p) on the filled sea (hawking.current-commutator-exactly-edge-split,
    synthesis.floor-regulator-keeps-the-charge-and-the-central-term-below-the-cut-off, and the bosonisation bridge of
    the s-wave sector); the null vacuum as the state of (N+) (synthesis.null-vacuum-on-a-horizon-generator). New here:
    (i) the collective sum of single-fermion modes is one fermion mode exactly; (iii) and (iv) the block's fluctuation
    form, its values in product and Gibbs states and its rank 2[p1 != p2] + 2[p1 + p2 != 1], zero exactly on the
    tracial states of the block's even algebra; (v) the converse of the edge-clean statement and the product-state
    value of the density commutator, which vanishes for every state with balanced edges and not only for the trace
    state; (vi) the restriction of the null vacuum (and of any gauge-invariant quasi-free state with symbol
    phi(P) tensor id_K) to momentum-band modes is a product state, for the null vacuum the bands' filled sea, so on
    each generator of a horizon that Premise (N+) covers the band density modes have a non-degenerate form on every
    window; with the explicit invariant domain D of finite excitations, this places the canonical relations of the
    infinite filled sea on those band modes; (vii) the exact fluctuation commutator and its law of large numbers.
    Stored, not new: the canonical relations on the infinite filled-sea array are Theorem
    singularity.bosonisation-bridge-s-wave-sector (1) (there for the s-wave boundary modes, the normal-ordering
    constants dropping out), and they follow from hawking.current-commutator-exactly-edge-split; (vi) re-derives them
    on D from that edge identity. Prior art, not premises: the same relation is the stored Fact
    synthesis.imported-schwinger-term-and-mattis-lieb-density-algebra (Tomonaga; Mattis and Lieb, J. Math. Phys. 6
    (1965) 304-312); (vii) is the algebraic core of the
    quantum central limit theorem, whose full statement (the fluctuation states converge to a quasi-free state of the
    algebra of canonical commutation relations with symplectic form phi([Q, R])) is in C. D. Cushen and R. L. Hudson,
    A quantum-mechanical central limit theorem, J. Appl. Probab. 8 (1971) 454-469, doi:10.2307/3212170, D. Goderis,
    A. Verbeure and P. Vets, Non-commutative central limits, Probab. Th. Rel. Fields 82 (1989) 527-544, and D.
    Goderis and P. Vets, Central limit theorem for mixing quantum systems and the CCR-algebra of fluctuations,
    Commun. Math. Phys. 122 (1988) 249-265 (Cushen and Hudson's bibliographic data verified, and the form of the
    symplectic form checked against the sources, on 7 November 2026; the volume and pages of the other two not
    independently verified); that convergence of states is not claimed. The name of (ii) is T. Holstein and
    H. Primakoff, Phys. Rev. 58 (1940) 1098 (bibliographic data verified on 7 November 2026; the identity is proved here). Ledger: (i) to (v) and
    (vii) are transport-absent (finite CAR algebra of tower planes, standard many-body structure); (vi) is
    transport-convenient (the generator's continuum mode space and the state (N+) selects). The dependence on (N+) is
    only through which state each generator of a horizon that Premise (N+) covers is in: clause (vi) is a statement
    about the null vacuum, which needs no premise.
---

## formal
Let the tower planes carry the null pairs $v_{j}, w_{j}$ with $\{v_{j}, w_{k}\} = \delta_{jk}$, $v_{j}^{2} = w_{j}^{2} = 0$ (Fact \claimref{field-theory.imported-tower-limit}), $v_{j} = \tfrac12(e_{j} + f_{j})$, $w_{j} = \tfrac12(e_{j} - f_{j})$ with $Q(e_{j}) = 1$, $Q(f_{j}) = -1$, read as $a_{j}^{*} = v_{j}$, $a_{j} = w_{j}$, with $*$ the adjoint of T03 ($v_{j}^{*} = w_{j}$) and $n_{j} = v_{j}w_{j}$. On $m$ planes the scalar part is the normalised trace, so a state with density element $\rho$ is $\omega(X) = 2^{m}\langle\rho X\rangle_{0}$; the gauge-invariant product state with occupations $p_{j}$ has $\rho = \prod_{j}(p_{j}n_{j} + (1 - p_{j})(1 - n_{j}))$, and the trace state is $p_{j} = \tfrac12$ for all $j$. A \emph{block} is two planes, a lower mode $1$ and an upper mode $2$, with hopping element $b = v_{1}w_{2}$, pairing element $c = w_{1}w_{2}$ and even algebra $\mathcal{A}_{e} = \Cl^{+}(2,2)$ of its two planes (real, eight-dimensional), the sum of two copies of $\Mat_{2}(\R)$ on the eigenspaces of number parity (the pseudoscalar of the block). For a state $\omega$ let $\sigma_{\omega}(X, Y) = \omega([X, Y])$, a real antisymmetric bilinear form on $\mathcal{A}_{e}$, the \emph{fluctuation form}.
\begin{enumerate}
\item[(i)] \emph{(Single fermions collect into one fermion.)} Annihilators of distinct modes anticommute, and for every $N$, $S = N^{-1/2}\sum_{i=1}^{N} w_{i}$ satisfies $S^{2} = 0$ and $\{S, S^{*}\} = 1$: the normalised collective sum of single-fermion modes is one fermion mode, never a boson. Even elements of distinct blocks commute; in particular hopping and pairing elements of distinct blocks and their adjoints commute.
\item[(ii)] \emph{(The hopping ladder.)} For $N$ blocks with $b_{i} = v_{1i}w_{2i}$ and $B = N^{-1/2}\sum_{i}b_{i}$, $[B, B^{*}] = N^{-1}\sum_{i}(n_{1i} - n_{2i})$ exactly, and with $K_{3} = \tfrac12\sum_{i}(n_{2i} - n_{1i})$ the triple $(\sqrt{N}B^{*}, \sqrt{N}B, K_{3})$ closes as $\mathfrak{su}(2)$. On the states $(B^{*})^{k}\Omega_{\mathrm{pol}}$, $\Omega_{\mathrm{pol}}$ the polarised state (every lower mode filled, every upper mode empty), $[B, B^{*}] = 1 - 2k/N$ for $k = 0, \dots, N$, these states are nonzero and $(B^{*})^{N+1}\Omega_{\mathrm{pol}} = 0$; the canonical relation $[B, B^{*}] = 1$ is reached only as $N \to \infty$ on states of bounded $k$. The reflection $f_{1i} \mapsto -f_{1i}$ of every lower plane, which exchanges $v_{1i}$ and $w_{1i}$ (particle-hole conjugation of the lower mode), maps $\sqrt{N}B$ to the pairing sum $\sum_{i}w_{1i}w_{2i}$ of Proposition \claimref{field-theory.how-close-tower-comes-ccr} and $N[B, B^{*}]$ to its commutator $N - \sum_{j}n_{j}$: the two ladders are one.
\item[(iii)] \emph{(Block commutators and their values.)} $[b, b^{*}] = n_{1} - n_{2}$ and $[c, c^{*}] = 1 - n_{1} - n_{2}$. In the product state with occupations $p_{1}, p_{2}$, $\omega([b, b^{*}]) = p_{1} - p_{2}$ and $\omega([c, c^{*}]) = 1 - p_{1} - p_{2}$: in the polarised state ($p_{1} = 1$, $p_{2} = 0$) these are $1$ and $0$; in the Gibbs state of $\varepsilon(n_{2} - n_{1})$ at temperature $T$ (Fermi-Dirac occupations of two levels at $\mp\varepsilon$ about the chemical potential), $p_{1} = y/(1 + y)$ and $p_{2} = 1/(1 + y)$ with $y = e^{\varepsilon/T}$, they are $\tanh(\varepsilon/2T) = (y - 1)/(y + 1)$, exactly $\tfrac12$ at $e^{\varepsilon/T} = 3$, and $0$; in the trace state both are $0$.
\item[(iv)] \emph{(The rank of the block's form.)} For a state $\omega$ of a block, $\sigma_{\omega}$ vanishes identically on $\mathcal{A}_{e}$ if and only if $\omega$ is tracial on $\mathcal{A}_{e}$, that is $\omega|_{\mathcal{A}_{e}} = \lambda\tau_{+} + (1 - \lambda)\tau_{-}$ with $\tau_{\pm}$ the normalised traces of the even- and odd-number sectors and $0 \le \lambda \le 1$; this never holds for a pure state. For the product state with occupations $p_{1}, p_{2}$,
\[
\operatorname{rank}\sigma_{\omega} = 2\,[p_{1} \ne p_{2}] + 2\,[p_{1} + p_{2} \ne 1],
\]
the first term from the hopping (odd-sector) mode, the second from the pairing (even-sector) mode; it is $0$ exactly for the trace state, and $2$ for every pure product state.
\item[(v)] \emph{(Density modes on a window.)} On $M$ modes $j = 0, \dots, M - 1$ (lower $j$, lower momentum) let $\rho_{q} = \sum_{k}v_{k}w_{k+q}$, $1 \le q \le M - 1$. Then $[\rho_{q}, \rho_{q}^{*}] = \sum_{k < q}n_{k} - \sum_{k \ge M - q}n_{k}$ (as stored in Theorem \claimref{hawking.current-commutator-exactly-edge-split} and Theorem \claimref{synthesis.floor-regulator-keeps-the-charge-and-the-central-term-below-the-cut-off}(ii); re-derived here); for $2q \le M$ it acts on a vector $\psi$ as the scalar $q$ if and only if $\psi$ lies in the edge-clean subspace (the lowest $q$ modes filled, the highest $q$ empty). In the product state with occupations $p_{k}$, $\omega([\rho_{q}, \rho_{q}^{*}]) = \sum_{k < q}p_{k} - \sum_{k \ge M - q}p_{k}$: $\min(q, M - q)$ on the filled sea ($M$ even, the lowest $M/2$ modes filled), strictly between $0$ and $q$ for a Fermi-Dirac profile, and $0$ in the trace state and in every product state whose two edge sums agree (constant occupation, for instance), though such a state is not tracial on the blocks when the constant is not $\tfrac12$. On density modes alone the form therefore degenerates for more states than the trace state; on a block's even algebra, by (iv), among product states only the trace state degenerates.
\item[(vi)] \emph{(Density waves of the null vacuum.)} On one horizon generator let $\mathfrak{h} = L^{2}(\R, du)\otimes K$, $P = I_{4}\,d/du$ (the unit of $\mathfrak{h}$ is $I_{4}$), and $\omega_{0}$ the null vacuum, the gauge-invariant quasi-free state with symbol $\chi_{(-\infty,0)}(P)\otimes\id_{K}$, which is the state Premise (N$_{+}$) assigns to the generator, by the uniqueness in Theorem \claimref{synthesis.null-vacuum-on-a-horizon-generator}(ii). Fix $\Delta > 0$ and a unit vector $\eta \in K$, and for $k \in \mathbb{Z}$ let $g_{k} = h_{k}\otimes\eta$ with $h_{k}$ the unit vector whose $P$-spectral wave function is $\Delta^{-1/2}$ times the indicator of $[k\Delta, (k + 1)\Delta)$. The restriction of $\omega_{0}$ to the CAR algebra of $\{g_{k}\}$ is the product state with $n_{k} = 1$ for $k < 0$ and $0$ for $k \ge 0$; more generally a gauge-invariant quasi-free state with symbol $\phi(P)\otimes\id_{K}$ restricts to the product state with $p_{k} = \Delta^{-1}\int_{k\Delta}^{(k+1)\Delta}\phi$. Hence on every window $k = -N, \dots, N - 1$ the null vacuum is the window's filled sea, edge-clean at every depth $q \le N$: its density form is non-degenerate, $\omega_{0}([\rho_{q}, \rho_{q'}^{*}]) = \min(q, 2N - q)\,\delta_{qq'}$ and $\omega_{0}([\rho_{q}, \rho_{q'}]) = 0$, and every block of two window modes has a form of rank $2$; with the symbol $\tfrac12$ (the trace state) both forms vanish. On the whole band $k \in \mathbb{Z}$, let $\mathcal{D}$ be the span of the finite excitations of the filled sea $\Omega$ (vectors $x\Omega$, $x$ a polynomial in finitely many $v_{k}, w_{k}$) in the representation of $\omega_{0}$; there $\rho_{q} = \sum_{k \in \mathbb{Z}}v_{k}w_{k+q}$ ($q \ge 1$) is a finite sum on each vector, $\rho_{q}\Omega = 0$, and on $\mathcal{D}$
\[
[\rho_{q}, \rho_{q'}^{*}] = q\,\delta_{qq'}, \qquad [\rho_{q}, \rho_{q'}] = 0 ,
\]
so $\rho_{q}/\sqrt{q}$ are canonical boson modes with vacuum $\Omega$: the relations of Theorem \claimref{singularity.bosonisation-bridge-s-wave-sector}(1) on the infinite filled-sea array, here on the band modes of the null vacuum with the explicit domain $\mathcal{D}$. On no finite window is the central term a scalar (Proposition \claimref{field-theory.no-canonical-commutation-relations-tower}, and (v)).
\item[(vii)] \emph{(The fluctuation commutator and its law of large numbers.)} For a state $\omega$ of the block's even algebra $\mathcal{A}_{e}$ (for instance the product state of (iv)), with $\omega^{\otimes N}$ the product state on the even algebras of $N$ blocks, for $X \in \mathcal{A}_{e}$ let $X_{k}$ be its copy on block $k$ and $F_{N}(X) = N^{-1/2}\sum_{k}(X_{k} - \omega(X))$. For $Q, R \in \mathcal{A}_{e}$ and $C = [Q, R]$,
\[
[F_{N}(Q), F_{N}(R)] = \frac1N\sum_{k}C_{k} = \sigma_{\omega}(Q, R) + D_{N}, \qquad \omega^{\otimes N}(D_{N}) = 0, \qquad \omega^{\otimes N}(D_{N}^{*}D_{N}) - \omega^{\otimes N}(D_{N}^{*})\,\omega^{\otimes N}(D_{N}) = \frac{\omega(C^{*}C) - \omega(C^{*})\,\omega(C)}{N},
\]
exactly. So the commutator of fluctuations tends to the scalar $\sigma_{\omega}(Q, R)$ in mean square: in this sense the fluctuations obey, as $N \to \infty$, the canonical relations $[F(Q), F(R)] = \sigma_{\omega}(Q, R)$ (the convergence of the fluctuation states themselves is not claimed), with $\tfrac12\operatorname{rank}\sigma_{\omega} \in \{0, 1, 2\}$ independent canonical pairs per block by (iv), none exactly when $\omega$ is tracial on the block. For a real state $\sigma_{\omega}$ vanishes on every pair of self-adjoint even elements, so the canonical pairs are $(a, a^{*})$ with $a$ not self-adjoint and $[a, a^{*}]$ a scalar, and no unit is needed; a Weyl form with self-adjoint fields would need a central unit, which the block's even algebra lacks (its pseudoscalar squares to $+1$). For a gauge-invariant product state, where $\omega(b) = 0$, the hopping mode is $F_{N}(b) = B$ of (ii), with $\omega^{\otimes N}([B, B^{*}]) = p_{1} - p_{2}$ at every $N$.
\end{enumerate}
All clauses are proved. \emph{Reading.} Bosons are not elementary in the tower (no floor carries the canonical relation, and single fermions collect into a fermion); they arise here as collective fluctuation modes of even block elements, and they need both the infinite tower and a state that is not tracial. Under (N$_{+}$) the state on each generator of a horizon that Premise (N$_{+}$) covers is the filled sea, and by (vi) its band density modes are bosons on the finite excitations of the infinite band: density waves of the filled sea. This is not a construction of the photon or other gauge bosons.

## technical
In the tower a boson can only be collective. A single fermion operator summed over many modes and normalised is again exactly one fermion mode, and no finite floor carries the canonical commutation relation (the stored no-go). Even elements of distinct blocks commute, so they can build bosons. For a block of two modes the hopping element $b = a_{1}^{*}a_{2}$ has $[b, b^{*}] = n_{1} - n_{2}$ and the pairing element $c = a_{1}a_{2}$ has $[c, c^{*}] = 1 - n_{1} - n_{2}$; the normalised sum of hopping elements over $N$ blocks is a quasi-spin with $[B, B^{*}] = 1 - 2k/N$ on its ladder (the Holstein-Primakoff form), the stored pairing quasi-spin after particle-hole conjugation of the lower modes.

The fluctuation form $\sigma_{\omega}(X, Y) = \omega([X, Y])$ on a block's even algebra counts the boson modes a state's fluctuations carry. For $N$ blocks in a product state the commutator of the normalised fluctuations is exactly the average of the single-block commutators, which by the law of large numbers tends to the number $\sigma_{\omega}(Q, R)$, with variance falling as $1/N$: the commutator of the fluctuations tends to this form in mean square; in that sense the fluctuations obey canonical commutation relations with it (convergence of the fluctuation states is not claimed). For a real state the form vanishes on pairs of self-adjoint elements, so the canonical pairs are an element and its adjoint, and no imaginary unit enters. In a product state with occupations $p_{1}, p_{2}$ its rank is $2[p_{1} \ne p_{2}] + 2[p_{1} + p_{2} \ne 1]$: the hopping boson needs unequal occupations and the pairing boson needs $p_{1} + p_{2} \ne 1$. The values are $1$ for the hopping mode in the polarised state, $\tanh(\varepsilon/2T)$ in a Fermi-Dirac state at levels $\mp\varepsilon$ (where the pairing mode drops out), and $0$ for both in the trace state. The form vanishes on a block exactly for the states tracial on its even algebra; among product states, only the trace state.

The density modes $\rho_{q}$ on a window of $M$ modes have the stored edge-operator commutator, which acts as the scalar $q$ exactly on edge-clean vectors; in a product state its value is the occupation of the lowest $q$ modes minus that of the highest $q$, so it vanishes for the trace state and for any product state with balanced edges. On a horizon generator, the null vacuum restricted to modes supported in momentum bands is the filled sea of those bands, so the band density modes have a non-degenerate form on every window, and on the finite excitations of the infinite band they satisfy the canonical relations exactly, as already stored for the s-wave boundary modes (the bosonisation bridge) and known as the Tomonaga and Mattis-Lieb density algebra, here derived from the edge identity on an explicit domain. This reads: on the generators (N$_{+}$) covers, the filled sea carries bosons, its chiral density waves, one band at a time; this is not a construction of the photon or other gauge bosons. Premise (N$_{+}$) is what puts the filled sea on each generator of a horizon it covers.

## lay
The tower is built from fermions, particles that cannot share a state. Bosons, the particles that can, are not among its building blocks: adding up many single fermion operations just gives another fermion, and no finite part of the tower holds an exact boson. Bosons appear instead as collective ripples. Pairs of fermion operations from different parts of the tower behave independently, and their averaged ripple behaves like a boson when the underlying state is lopsided, for example with low levels filled and high levels empty. In the completely random state, where every level is half filled, the ripples carry no boson at all. The series' premise about horizons says the horizon lines it covers are in their lowest-energy state, a filled sea of fermions, and in that state the density ripples are exact bosons once the band of levels along the line is taken to be infinite. These ripples are not the photon or the other force carriers.

## one-liner
Single-fermion sums in the tower are fermions; fluctuations of even two-mode block elements commute to the form $\omega([Q, R])$ (exactly, up to a term of variance $O(1/N)$), of rank $2[p_{1} \ne p_{2}] + 2[p_{1} + p_{2} \ne 1]$ in a product state ($[b, b^{*}] = n_{1} - n_{2}$: $1$ polarised, $\tanh(\varepsilon/2T)$ thermal, $0$ trace), zero exactly for tracial states; density forms vanish in product states with balanced edges; the null vacuum, the state under (N$_{+}$), is the filled sea on momentum bands, so its density waves are canonical bosons on the finite excitations of the infinite band.
