---
id: synthesis.gauge-factor-sugawara-parts-satisfy-virasoro-relations-on-the-band
kind: claim
version: 1
title: Virasoro relations of the gauge factors' Sugawara parts and of the remainder on the band
status: proved
region: synthesis
subject: quantum-fields
tags: [gauge-fields, bosonisation, car-algebra, representation-theory, recovers-known-physics]
proposed_by:
  kind: ai
  session: 2026-11-09-solvable
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: run 2026-11-09-solvable
review: draft
about:
- obj.tower.tower
derivations:
- name: main
  uses:
  - field-theory.imported-tower-limit@3
  - synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators@1
  - synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves@1
  - synthesis.standard-model-currents-of-the-sixteen-channels-levels-and-window-sugawara-split@1
  - synthesis.window-energy-of-one-generation-is-exactly-the-so10-sugawara-energy@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_band_operators_realise_the_tower_modes
- kind: check
  ref: check.py::check_band_energy_is_virasoro_at_sixteen_and_shifts_every_pair_current
- kind: check
  ref: check.py::check_factor_parts_shift_their_own_currents_at_every_mode
- kind: check
  ref: check.py::check_factor_parts_satisfy_virasoro_relations
- kind: check
  ref: check.py::check_remainder_is_a_virasoro_algebra_at_fifty_two_sevenths_commuting_with_the_factors
- kind: check
  ref: check.py::check_band_energy_is_so10_plus_number_at_every_mode
- kind: check
  ref: check.py::check_vacuum_norms_and_adjoints
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.standard-model-currents-of-the-sixteen-channels-levels-and-window-sugawara-split
extraction:
  open_problem: op.qft-non-abelian-gauge-fields
  note: >-
    Attack on the item "Derive the Virasoro relations of the gauge factors' Sugawara parts on the band domain, so that
    their central values (32/7, 2, 1, 1 and the remainder 52/7) are central charges in the full sense" of
    op.qft-non-abelian-gauge-fields. Stored and used: the embedding of the gauge algebra in the pair currents of the
    sixteen channels of a light ray, the levels, the adjoint Casimirs lambda and the band current algebra with its
    central term on the domain D (synthesis.standard-model-currents-of-the-sixteen-channels-levels-and-window-sugawara-split
    (i) to (iii)), which defined only the zero modes H_f and the vectors L^f_{-2} Omega; the domain D and the
    sea-normal-ordered energy (synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves
    (iii)); the window identity H = H_so10 + H_N
    (synthesis.window-energy-of-one-generation-is-exactly-the-so10-sugawara-energy (iii)). New: every mode L^f_n of
    each factor, the shift of the factor's currents by every L^f_n, the Virasoro relations of each factor with central
    charge 2 dim f/(2 + lambda), those of the band energy at 16 and of the remainder at 52/7, the mutual commutation
    of the five parts, and the so(10) form of the remainder at every mode (the stored identity was the zero mode only).
    The derivation is from the stored band commutator by an explicit cutoff computation on each vector of D, and the
    check realises D exactly (semi-infinite sea, fermion signs counted from the top level). Prior art, not premises,
    cited from memory: H. Sugawara, Phys. Rev. 170 (1968) 1659; V. G. Kac, Infinite-dimensional Lie algebras
    (Cambridge, 1990), chapter 12 (the Virasoro relations of the Sugawara operators, c = k dim g/(k + h)); P. Goddard,
    A. Kent and D. Olive, Phys. Lett. B 152 (1985) 88 and Commun. Math. Phys. 103 (1986) 105 (the coset construction
    and unitarity); conformal embeddings of the spinor type, among them so(10) at level 4 in su(16) at level 1
    (A. N. Schellekens and N. P. Warner, Phys. Rev. D 34 (1986) 3092; F. A. Bais and P. G. Bouwknegt, Nucl. Phys. B
    279 (1987) 561); the free-fermion Virasoro algebra. None is used as a premise. Related stored Fact, not a duplicate:
    dark-energy.imported-conformal-orthogonality-sugawara-construction@1 imports the Sugawara bilinear as the stress
    tensor and states no Virasoro relations. Ledger: transport-absent as algebra
    (free-fermion current algebra on the tower planes); the sixteen channels are the series' slot module on the light
    rays of a horizon, as in the stored split. The sum of the constants -c_f/24 over the five parts is -16/24, the -1/24 per component of the zeta-symmetric null
    ordering (synthesis.null-ordering-of-counted-units-is-zeta-symmetric) summed over sixteen channels; this is only
    the additivity of the central charges, and the shift by -c/24 is not a band quantity. What is not claimed: the
    relations on every window vector (the stored split already fails at a window edge), the transverse dynamics, the four-dimensional gauge field or Yang-Mills;
    the remainder is identified as the coset of so(10) at level 4 by the gauge algebra, whose further structure (its
    primary fields, its relation to the counted-mode sea) is not addressed.
---

## formal
In the setting of Theorem \claimref{synthesis.standard-model-currents-of-the-sixteen-channels-levels-and-window-sugawara-split}: the sixteen channels of a light ray of one generation are the even states of the slot module $\Lambda^{\bullet}\C^{5}$; channel $x$ carries tower modes $c_{x,k}$, $k \in \Z$ (Fact \claimref{field-theory.imported-tower-limit}); $\mathcal{D}$ is the domain of finite excitations of the band of the null vacuum in every channel, with the sea $\Omega$ (levels $k < 0$ filled) and zero modes counted from it; $J(M)_{m} = \sum_{x,y}M_{xy}\sum_{k}c^{*}_{x,k}c_{y,k+m}$ for a $16 \times 16$ matrix $M$ over $\mathrm{span}\{1, J\}$; the factors $\mathfrak{f} = \su(3), \su(2), Y, N$ act through $\rho$, with trace-dual bases $M_{A}$, $M^{A}$ for $\operatorname{tr}_{16}$ and adjoint Casimirs $\lambda_{\mathfrak{f}} = \tfrac32, 1, 0, 0$. For every $n \in \Z$ put
\[
L^{\mathfrak{f}}_{n} = \frac{1}{2 + \lambda_{\mathfrak{f}}}\sum_{A}\sum_{q \in \Z}{:}J(M^{A})_{n-q}J(M_{A})_{q}{:}, \qquad L_{n} = \sum_{x}\sum_{k \in \Z}\Bigl(k + \frac12 + \frac{n}{2}\Bigr){:}c^{*}_{x,k}c_{x,k+n}{:},
\]
the normal ordering putting the mode of larger index on the right and counting from the sea, so $L^{\mathfrak{f}}_{0} = H_{\mathfrak{f}}$ and $L_{0} = H$ of the stored split; let $L^{c}_{n} = L_{n} - \sum_{\mathfrak{f}}L^{\mathfrak{f}}_{n}$ and let $L^{\so(10)}_{n}$ be the same Sugawara sum for the $45$ bilinears $a^{*}_{a}a_{b} - \tfrac12\delta_{ab}$, $a^{*}_{a}a^{*}_{b}$, $a_{a}a_{b}$ of the five modes ($\lambda = 4$). On each vector of $\mathcal{D}$ all these sums are finite. On $\mathcal{D}$:
\begin{enumerate}
\item[(i)] \emph{(Shifts; proved.)} For $X$ in $\mathfrak{f}$ and all $m, n$, $[L^{\mathfrak{f}}_{n}, J(\rho X)_{m}] = -mJ(\rho X)_{m+n}$, and $[L^{\mathfrak{f}}_{n}, J(\rho X')_{m}] = 0$ for $X'$ in another factor or $X' = 1$; $[L_{n}, J(M)_{m}] = -mJ(M)_{m+n}$ for every $M$.
\item[(ii)] \emph{(Virasoro relations; proved.)} For each factor,
\[
[L^{\mathfrak{f}}_{m}, L^{\mathfrak{f}}_{n}] = (m - n)L^{\mathfrak{f}}_{m+n} + \frac{c_{\mathfrak{f}}}{12}(m^{3} - m)\,\delta_{m+n,0}, \qquad c_{\mathfrak{f}} = \frac{2\dim\mathfrak{f}}{2 + \lambda_{\mathfrak{f}}}: \quad c_{\su(3)} = \tfrac{32}{7},\ c_{\su(2)} = 2,\ c_{Y} = c_{N} = 1,
\]
and the band energy satisfies the same relations with $c = 16$. Moreover $(L^{\mathfrak{f}}_{n})^{*} = L^{\mathfrak{f}}_{-n}$ and $L^{\mathfrak{f}}_{n}\Omega = 0$ for $n \ge -1$, so each is a unitary representation of the Virasoro algebra on $\mathcal{D}$.
\item[(iii)] \emph{(The remainder; proved.)} $L^{c}_{n}$ commutes with every gauge current $J(\rho X)_{m}$, with $N_{m}$ and with every $L^{\mathfrak{f}}_{n}$; the parts of distinct factors commute; and $L^{c}$ satisfies the Virasoro relations with $c = 16 - \tfrac{32}{7} - 2 - 1 - 1 = \tfrac{52}{7}$, with $(L^{c}_{n})^{*} = L^{c}_{-n}$. So the band energy is the sum of five mutually commuting unitary Virasoro algebras of central charges $\tfrac{32}{7}$, $2$, $1$, $1$ and $\tfrac{52}{7}$, and the central values of the stored split are central charges.
\item[(iv)] \emph{(The $\so(10)$ form; proved.)} $L_{n} = L^{\so(10)}_{n} + L^{N}_{n}$ for every $n$ (central charges $15 + 1$), so $L^{c}_{n} = L^{\so(10)}_{n} - L^{\su(3)}_{n} - L^{\su(2)}_{n} - L^{Y}_{n}$: the remainder is the coset of $\so(10)$ at level $4$ by the gauge algebra.
\item[(v)] \emph{(Computed.)} Exactly on $\mathcal{D}$ (its fermion signs checked against the Clifford relations of the tower planes): (i) and (ii) for the four factors and the band energy on sample vectors (the sea, an $\su(2)$ excitation, a charged vector and, for the band energy and (iv), a two-level hop) and modes $|m|, |n| \le 2$ ($\le 3$ for the band energy), failing when $c_{\mathfrak{f}}$ or $\lambda_{\mathfrak{f}}$ is raised by $1$; (iii) on the same vectors; (iv) for $n = -2, \dots, 2$, failing for the $25$ number-conserving bilinears alone; $\|L^{\mathfrak{f}}_{-2}\Omega\|^{2} = \tfrac{16}{7}, 1, \tfrac12, \tfrac12$ and $\|L^{\mathfrak{f}}_{-3}\Omega\|^{2} = \tfrac{64}{7}, 4, 2, 2$, and for the remainder $\tfrac{26}{7}$ and $\tfrac{104}{7}$, that is $\tfrac{c}{12}(m^{3} - m)$.
\end{enumerate}
These are statements on $\mathcal{D}$, and the central charges are those of the band: on a finite window no operators satisfy the Virasoro relations with $c \ne 0$ (argued: on a finite-dimensional space the traces of $[L_{1}, L_{-1}] = 2L_{0}$ and $[L_{2}, L_{-2}] = 4L_{0} + \tfrac{c}{2}$ force $\operatorname{tr}L_{0} = 0$ and then $c = 0$), and the factor split already fails at the window edge (stored split (iii)). With the shift $L_{0} - \tfrac{c}{24}$ applied to each part (a convention: on $\mathcal{D}$ every part annihilates the sea, so the constants are not band quantities), the constants $-\tfrac{c_{\mathfrak{f}}}{24}$ of the five parts add to $-\tfrac{16}{24}$, sixteen times $-\tfrac{1}{24}$ per channel; this is the additivity $16 = \tfrac{32}{7} + 2 + 1 + 1 + \tfrac{52}{7}$ of (iii) and needs the remainder. Nothing here concerns the transverse dynamics or the four-dimensional gauge field.

## technical
Along a light ray, one generation's sixteen channels carry the Standard Model gauge algebra as level-four currents inside the level-one $\uu(16)$ current algebra, and the stored split defined each factor's Sugawara energy $H_{\mathfrak{f}}$ and the level-two vector $L^{\mathfrak{f}}_{-2}\Omega$ only. Here every mode $L^{\mathfrak{f}}_{n}$ is defined on the band of the null vacuum by the normal-ordered Sugawara sum, normalised by $2 + \lambda_{\mathfrak{f}}$ with the adjoint Casimir in the trace-dual basis. An explicit cutoff computation on each vector of the band, from the stored current commutator, shows that $L^{\mathfrak{f}}_{n}$ shifts the factor's currents and that the modes satisfy the Virasoro relations with $c_{\mathfrak{f}} = 2\dim\mathfrak{f}/(2 + \lambda_{\mathfrak{f}})$: $\tfrac{32}{7}$, $2$, $1$, $1$. The band energy, a fermion bilinear, satisfies them with $c = 16$; the remainder after the four parts commutes with all gauge currents and with the parts and is a Virasoro algebra at $c = \tfrac{52}{7}$, and all five are unitary. At every mode the band energy is the $\so(10)$ Sugawara energy plus the number current's, so the remainder is the coset of $\so(10)$ at level four by the gauge algebra. The check realises the semi-infinite band exactly and verifies the relations on sample vectors.

## lay
On each light ray at a horizon one generation of matter supplies sixteen fermion channels, and the forces of the Standard Model act on them through currents built from pairs of fermions. The energy carried along the light ray was known to split into a share for the strong force, one for the weak force, one for hypercharge, one for fermion number and a remainder, with numbers attached to each share. Here each share is shown to carry the conformal symmetry of motion along one light ray (one chiral half), the Virasoro algebra, with those numbers as its central charges: 32/7, 2, 1, 1 and 52/7 out of 16. The remainder is what the grand-unified symmetry SO(10) carries beyond the Standard Model forces. This is the standard Sugawara and coset construction of two-dimensional physics, derived here from the series' light-ray currents; it describes motion along one light ray, not the four-dimensional gauge field.

## one-liner
On the band of the null vacuum, each gauge factor's Sugawara modes $L^{\mathfrak{f}}_{n}$ (all $n$) shift its currents and satisfy the Virasoro relations with $c = 2\dim\mathfrak{f}/(2 + \lambda)$: $\tfrac{32}{7}$, $2$, $1$, $1$; the band energy has $c = 16$, the remainder commutes with the factors and is a Virasoro algebra at $c = \tfrac{52}{7}$, the coset of $\so(10)$ at level $4$ by the gauge algebra; all unitary.
