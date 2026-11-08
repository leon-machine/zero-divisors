---
id: synthesis.standard-model-currents-of-the-sixteen-channels-levels-and-window-sugawara-split
kind: claim
version: 1
title: Standard Model currents of the sixteen channels of a light ray, levels and Sugawara split
status: proved
region: synthesis
subject: quantum-fields
tags: [gauge-fields, bosonisation, car-algebra, representation-theory, recovers-known-physics]
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
  - field-theory.imported-tower-limit@3
  - synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators@1
  - synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves@1
  - synthesis.slot-module-light-ray-arrays-are-weyl-components@3
  - synthesis.cpt-closure-forces-slot-module-and-chirality@1
  - standard-model.gauge-algebra-minimal-massive-composite@4
  - synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays@5
  - synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum@1
  - synthesis.null-vacuum-on-a-horizon-generator@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_gauge_algebra_acts_on_the_sixteen_channels_by_channel_unitary_matrices
- kind: check
  ref: check.py::check_levels_trace_form_is_four_times_the_slot_form
- kind: check
  ref: check.py::check_adjoint_casimirs_and_central_charges
- kind: check
  ref: check.py::check_split_commutes_on_localised_window_vectors
- kind: check
  ref: check.py::check_central_charges_from_level_two_vacuum_norms
- kind: proof
  derivation: main
extraction:
  open_problem: op.qft-non-abelian-gauge-fields
  note: >-
    Attack on the item "the current algebra along generators" of op.qft-non-abelian-gauge-fields: the embedding of the
    gauge algebra in the u(16) channel currents of a light ray and generation, the levels, and the Sugawara split of the
    energy along a generator. Stored and used: the pair currents of the channels and their exact window commutator with
    the level-one central term on edge-clean vectors
    (synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators (iv), (v)), the domain D of finite
    excitations of the band of the null vacuum and the localisation argument of
    synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves (iii), the sixteen Weyl
    components per light ray and generation (synthesis.slot-module-light-ray-arrays-are-weyl-components (ii)), the slot
    module with its gauge action and the anomaly-free halving (synthesis.cpt-closure-forces-slot-module-and-chirality),
    the chirality weights about the generator (synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays (iv)),
    the gauge algebra of the minimal massive composite (standard-model.gauge-algebra-minimal-massive-composite).
    Complex or real: each channel is one tower mode per level, a complex fermion with the kernel unit J of the tower
    level as the scalar of operators (unit principle U2, as in the stored pair currents); the gauge generators are
    number-conserving on V_+, so they lie in the u(16) of pair currents and need none of the pairing bilinears that
    enlarge it to so(32). Prior art, not premises: affine Lie algebras and their levels (V. G. Kac, 1968; R. V. Moody,
    1968; cited from memory), the Sugawara construction (H. Sugawara, Phys. Rev. 170 (1968) 1659, cited from memory),
    the coset construction (P. Goddard, A. Kent and D. Olive, Phys. Lett. B 152 (1985) 88, cited from memory),
    free-fermion current algebras (I. B. Frenkel and V. G. Kac, 1980; P. Goddard and D. Olive, Int. J. Mod. Phys. A 1
    (1986) 303; cited from memory); None of these is used: every statement
    is derived here from the stored window algebra, and the levels, adjoint Casimirs and central values are computed
    exactly. New to the store: the embedding and the trace identity tr_16 = 4 tr_5 + 4 tr tr on gl(5) (clauses (i),
    (ii)); the split, with the window condition under which it holds (iii); the level-two values (iv). Ledger: (ii) to
    (iv) are transport-absent as algebra (free-fermion current algebra on the CAR algebra of tower planes); (i) is
    transport-convenient (the channels are the series' slot module on the light rays of a horizon). What is not
    claimed: the Virasoro relations of the factor parts, the transverse dynamics, the four-dimensional gauge field,
    Yang-Mills, confinement, or a relation between the levels and the cubic anomaly conditions (the levels are
    quadratic traces; only the trace condition tr rho(Y) = 0 enters, as the vanishing of the hypercharge-number
    central term).
---

## formal
Let $V = \Lambda^{\bullet}\C^{5}$ be the slot module (modes $1, 2$ the slots, $3, 4, 5$ the pairs; Theorem \claimref{synthesis.cpt-closure-forces-slot-module-and-chirality}), with the gauge algebra $\mathfrak{g} = \mathfrak{s}(\uu(2) \oplus \uu(3)) \cong \su(3) \oplus \su(2) \oplus \uu(1)$ of the minimal massive composite (Theorem \claimref{standard-model.gauge-algebra-minimal-massive-composite}) acting through the bilinears $\sum_{a,b}X_{ab}a^{*}_{a}a_{b}$, $X \in \mathfrak{g}$, and hypercharge $Y = \mathrm{diag}(\tfrac12, \tfrac12, -\tfrac13, -\tfrac13, -\tfrac13)$, so $Y = (3n - 2k)/6$ on states with $n$ slots and $k$ pairs. Let $V_{+}$ be the half of even mode number (the anomaly-free halving $(-1)^{n + k}$ with the empty state as neutral singlet), and for $X \in \gl(5)$ let $\rho(X)$ be the $16 \times 16$ matrix of $\sum X_{ab}a^{*}_{a}a_{b}$ on $V_{+}$ in the occupation basis. Read the sixteen basis states as the sixteen channels of a light ray of one generation (Theorem \claimref{synthesis.slot-module-light-ray-arrays-are-weyl-components}(ii)): on a window of $L$ levels channel $x$ carries tower modes $c_{x,k}$, $k = 0, \dots, L - 1$ (Fact \claimref{field-theory.imported-tower-limit}), $j^{xy}_{m} = \sum_{k}c^{*}_{x,k}c_{y,k+m}$, and for a $16 \times 16$ matrix $M$ with entries in $\mathrm{span}\{1, J\}$ ($J$ the kernel unit of the tower level, $J^{2} = -1$, central among the modes) $J(M)_{m} = \sum_{x,y}M_{xy}j^{xy}_{m}$, $N_{m} = J(1)_{m}$. Let $H = \sum_{x,k}(k + \tfrac12)n_{x,k}$, and let $\Omega_{s}$ fill levels $0, \dots, s - 1$ of every channel. For a subalgebra $\mathfrak{f}$ of $\gl(16)$ on which $\operatorname{tr}_{16}$ is nondegenerate, with a basis $M_{A}$, the trace-dual basis $M^{A}$ and $\lambda_{\mathfrak{f}}$ defined by $\sum_{A}[M^{A}, [M_{A}, X]] = \lambda_{\mathfrak{f}}X$ on $\mathfrak{f}$, put
\[
H_{\mathfrak{f}} = \frac{1}{2 + \lambda_{\mathfrak{f}}}\Bigl(2\sum_{q \ge 1}J(M^{A})_{-q}J(M_{A})_{q} + J(M^{A})_{0}J(M_{A})_{0}\Bigr), \qquad L^{\mathfrak{f}}_{-2}\Omega_{s} = \frac{1}{2 + \lambda_{\mathfrak{f}}}J(M^{A})_{-1}J(M_{A})_{-1}\Omega_{s}
\]
(summed over $A$). Then:
\begin{enumerate}
\item[(i)] \emph{(The embedding.)} $\rho$ maps $\mathfrak{g}$ into $\gl(V_{+})$ (no gauge generator maps $V_{+}$ into $V_{-}$), is a Lie homomorphism, satisfies $\rho(X^{*}) = \rho(X)^{*}$ and $\operatorname{tr}\rho(X) = 8\operatorname{tr}X$, hence is traceless on $\mathfrak{g}$. The compact generators ($X^{*} = -X$, entries in $\mathrm{span}\{1, J\}$) go to anti-Hermitian channel matrices, so the gauge rotations act on the sixteen channels by unitary matrices over $\mathrm{span}\{1, J\}$ and the gauge currents $J(\rho X)_{m}$ are pair currents: they lie in $\uu(16)$ and need no pairing bilinears $c_{x}c_{y}$, $c^{*}_{x}c^{*}_{y}$. All sixteen channels are left-handed Weyl components and carry one weight under the rotation about the generator (Theorem \claimref{synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays}(iv)), so every $\uu(16)$ current, in particular every gauge current, has helicity $0$. The hypercharges of the channels are $0$, $1$ (once each), $\tfrac16$ (six), $-\tfrac23$, $\tfrac13$ (three each), $-\tfrac12$ (two).
\item[(ii)] \emph{(Levels.)} For all $X, X' \in \gl(5)$, $\operatorname{tr}_{16}(\rho(X)\rho(X')) = 4\operatorname{tr}_{5}(XX') + 4\operatorname{tr}X\operatorname{tr}X'$; on $\mathfrak{g}$ the trace form of the channels is four times that of $\C^{5}$. So on window vectors edge-clean at depth $\max(|m|, |l|)$,
\[
[J(\rho X)_{m}, J(\rho X')_{l}] = J(\rho[X, X'])_{m+l} + 4m\operatorname{tr}_{5}(XX')\,\delta_{m+l,0} \qquad (X, X' \in \mathfrak{g}),
\]
and on every window vector the exact window commutator of the pair currents holds. The levels of $\su(3)$ and $\su(2)$, measured by the trace form of their fundamental (the $\C^{5}$ form on each block), are both $4$; for the abelian factor $\operatorname{tr}_{16}\rho(Y)^{2} = \tfrac{10}{3} = 4\operatorname{tr}_{5}Y^{2}$ in the normalisation $Y = (3n - 2k)/6$ (an abelian level depends on the normalisation of its generator; the normalisation-free statement is the factor $4$ between the two trace forms). The three factors are trace-orthogonal and traceless, so their currents commute with each other and with $N_{m}$ on those vectors.
\item[(iii)] \emph{(The split.)} $\lambda_{\su(3)} = \tfrac32$, $\lambda_{\su(2)} = 1$, $\lambda = 0$ for $\rho(Y)$ and $N$ (so the coefficients $2/(2 + \lambda)$ are $\tfrac47$, $\tfrac23$, $1$). Define $H_{c}$ by $H = H_{\su(3)} + H_{\su(2)} + H_{Y} + H_{N} + H_{c}$. On the domain $\mathcal{D}$ of finite excitations of the band of the null vacuum in every channel, where $H$ means the sea-normal-ordered $H_{\infty}$ of Theorem \claimref{synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves}(iii) summed over the channels and the zero modes $J(M)_{0}$ are counted from the sea, and, with the window $H$ and window zero modes, on window vectors equal to $\Omega_{s}$ outside levels $s - K, \dots, s + K - 1$ when $\min(s, L - s) \ge 3(K + |m|)$, for $X$ in a factor $\mathfrak{f}$ and $X'$ in another factor or $X' = 1$:
\[
[H_{\mathfrak{f}}, J(\rho X)_{m}] = -m\,J(\rho X)_{m}, \qquad [H_{\mathfrak{f}}, J(\rho X')_{m}] = 0, \qquad [H_{c}, J(\rho X)_{m}] = [H_{c}, N_{m}] = 0 .
\]
These relations do not hold on every window vector (they fail on a vector with a particle at the top level of a four-level window): the split into factor parts that generate the factors' own shifts holds on localised vectors only.
\item[(iv)] \emph{(Central values.)} For $s \ge 2$, $L - s \ge 2$, $\|L^{\mathfrak{f}}_{-2}\Omega_{s}\|^{2} = \dim\mathfrak{f}/(2 + \lambda_{\mathfrak{f}}) = c_{\mathfrak{f}}/2$ with $c_{\mathfrak{f}} = 2\dim\mathfrak{f}/(2 + \lambda_{\mathfrak{f}})$: $c_{\su(3)} = \tfrac{32}{7}$, $c_{\su(2)} = 2$, $c_{Y} = c_{N} = 1$, and for the whole $\uu(16)$, $L_{-2}\Omega_{s} = \tfrac{1}{34}\bigl(\sum_{x,y}j^{yx}_{-1}j^{xy}_{-1} + N_{-1}N_{-1}\bigr)\Omega_{s}$ with $\|L_{-2}\Omega_{s}\|^{2} = 8$, $c = 16$. The four vectors are mutually orthogonal, each has inner product $\|L^{\mathfrak{f}}_{-2}\Omega_{s}\|^{2}$ with $L_{-2}\Omega_{s}$, and the remainder has $\|L_{-2}\Omega_{s} - \sum_{\mathfrak{f}}L^{\mathfrak{f}}_{-2}\Omega_{s}\|^{2} = \tfrac{26}{7}$: the coset carries $c_{c} = 16 - \tfrac{32}{7} - 2 - 1 - 1 = \tfrac{52}{7}$. The Virasoro relations of the $L^{\mathfrak{f}}$ are not derived; $c_{\mathfrak{f}}$ is defined as $2\dim\mathfrak{f}/(2 + \lambda_{\mathfrak{f}})$, equal to twice the level-two norm, and would be the central charge if they hold.
\end{enumerate}
\emph{Reading.} Along each generator, one generation's sixteen channels carry the Standard Model gauge algebra as exact level-four currents (level $\tfrac{10}{3}$ for hypercharge in its own normalisation), of helicity $0$, inside the level-one $\uu(16)$ current algebra, and on localised vectors the energy splits into the factors' Sugawara parts with central values $\tfrac{32}{7}$, $2$, $1$, the number current's $1$ and a remainder $\tfrac{52}{7}$. This is a current algebra along each light ray, kinematics with a $1 + 1$ dimensional energy; it is not the four-dimensional gauge field.

## technical
The sixteen channels of a light ray of one generation are the even-degree states of the five-mode slot module $\Lambda^{\bullet}\C^{5}$. The gauge algebra acts on them through number-conserving bilinears, so it embeds in the $\uu(16)$ pair currents of the channels by anti-Hermitian matrices over $\mathrm{span}\{1, J\}$; it never mixes the channels with their conjugates, and since all sixteen channels are left-handed every current has helicity $0$. The trace form of the channels is $\operatorname{tr}_{16}(\rho X\rho X') = 4\operatorname{tr}_{5}(XX') + 4\operatorname{tr}X\operatorname{tr}X'$, so on the gauge algebra the central term of the window current algebra is four times the $\C^{5}$ trace: $\su(3)$ and $\su(2)$ at level $4$, hypercharge with $\operatorname{tr}\rho(Y)^{2} = \tfrac{10}{3}$ in the normalisation $Y = (3n - 2k)/6$.

Splitting the quadratic Casimir of $\gl(16)$ along $\su(3)$, $\su(2)$, hypercharge and the number current, each factor's Sugawara part, normalised by $2 + \lambda$ with the adjoint Casimir $\lambda = \tfrac32, 1, 0, 0$ in the trace-dual basis, generates the shifts of its own currents and commutes with the others' currents on localised window vectors (and on the band of the null vacuum); the remainder commutes with all gauge currents there, but not on every window vector. The level-two norms of the sea give the central values $\tfrac{32}{7}$, $2$, $1$, $1$ and $\tfrac{52}{7}$ for the remainder, out of $16$.

## lay
On each light ray at a horizon, one generation of matter supplies sixteen fermion channels, one for each left-handed particle of the generation. Pairs of these fermions form currents, and the forces of the Standard Model act on the channels as rotations of these currents. The strength of the currents' quantum term, the level, comes out as four for both the strong and the weak force, and four for hypercharge when it is measured in the same units as the internal modes. The energy of the channels along the light ray divides into parts built from the currents of each force plus a remainder, whose sizes (central values, the central charges if the factor energies obey the Virasoro algebra, which is not shown here) are computed exactly. This is a theory of currents along each light ray, not the gauge field that fills space.

## one-liner
The gauge algebra acts on the sixteen Weyl channels of a light ray by unitary pair-current matrices of helicity $0$ with $\operatorname{tr}_{16} = 4\operatorname{tr}_{5}$ (levels $4$; hypercharge $\operatorname{tr}\rho(Y)^{2} = \tfrac{10}{3}$); on localised window vectors the energy splits into factor Sugawara parts with $\lambda = \tfrac32, 1, 0$ and central values $\tfrac{32}{7}, 2, 1$, number $1$, coset $\tfrac{52}{7}$, out of $16$.
