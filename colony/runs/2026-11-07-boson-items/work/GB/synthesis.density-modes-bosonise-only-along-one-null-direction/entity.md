---
id: synthesis.density-modes-bosonise-only-along-one-null-direction
kind: claim
version: 1
title: 'Density modes bosonise only along one null direction'
status: proved
region: synthesis
subject: quantum-fields
tags: [bosonisation, car-algebra, no-go, limits]
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
  - tower.ladder-pairs-satisfy-car-vectors@4
  - hawking.current-commutator-exactly-edge-split@4
  - std-algebra.orthogonal-anticommute@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_window_identity_any_dimension
- kind: check
  ref: check.py::check_uniform_occupation_gives_zero_form
- kind: check
  ref: check.py::check_half_space_sea_value
- kind: check
  ref: check.py::check_density_current_term
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum
  - synthesis.imported-schwinger-term-and-mattis-lieb-density-algebra
  - synthesis.floor-regulator-keeps-the-charge-and-the-central-term-below-the-cut-off
extraction:
  open_problem: bos.dimension
  note: >-
    Attack on the run target bos.dimension (exact bosonisation is special to one dimension: what survives in
    higher dimension, and what the series needs). Answer: on finite windows of momenta in any dimension the
    density form is the occupation of an entry strip minus that of an equal exit strip; it vanishes for every
    sea with uniform total occupation on the strips (the relativistic sea, one filled state per momentum, in any
    dimension, and the 1+1 Dirac sea of both chiralities) and for every bounded sea away from the window's
    edges, and it is nonzero only through a sea that is a half-space in one direction, where it is that
    direction's one-dimensional value times the transverse overlap and zero for transverse q. In d = 3 the
    central term of the relativistic sea sits in the density-current commutator, at the window's edge, of size
    between 4qN(N - q) and 8qN^2 (cut-off squared), against 2q in d = 1. New here: (i) the strip identity in
    any dimension and with channel arrays; (ii) the exact zero for uniform and bounded seas on every window;
    (iii) the half-space value; (iv) the density-current term with its exact bounds. Stored and cited, not
    refiled: the one-dimensional, one-channel edge identity (hawking.current-commutator-exactly-edge-split) and
    the floor value min(p, 2N - p) (floor-regulator (ii), (iii)); the statement that a finite band has no
    central term, and the existence of the relativistic Schwinger term, are imported literature
    (synthesis.imported-schwinger-term-and-mattis-lieb-density-algebra (ii), (iii)), here derived on windows
    and sized, not used as premises. Reading (argued): the modes of a horizon generator have one null
    direction and no transverse dispersion, so they are case (iii), exact chiral density bosons for each
    transverse mode (fluctuation-forms (vi) on the band); bulk 3+1 matter is case (ii) and (iv): its densities
    are not bosons, and its only central term is the cut-off Schwinger term. So exact bosonisation in the
    series is per generator, a one-dimensional statement stacked over the transverse section, and does not
    give propagating 3+1 bosons. Prior art, orientation only, cited from memory:
    Schwinger's 1959 theorem on the equal-time commutator, the vanishing of the 3+1 density-density
    commutator in a relativistic theory, and higher-dimensional bosonisation by Fermi-surface patches
    (Haldane; Houghton and Marston; Castro Neto and Fradkin), whose corrections at patch edges this result
    does not compute. Ledger: transport-absent (finite CAR on tower planes; transport not used).
---

## formal
Let the modes $a_{k,\alpha}$ carry a momentum $k$ in a finite window $W \subset \mathbb{Z}^{d}$ and a channel $\alpha$ in a finite set of $c$ channels; each mode is a tower plane, $a^{*} = v$, $a = w$ (Theorem \claimref{tower.ladder-pairs-satisfy-car-vectors}), $v^{*} = w$, numbers in $\mathrm{span}\{1, J\}$ with $J$ the kernel bivector. For a channel array $M$ let $\rho_{q}(M) = \sum_{k, k+q \in W}a_{k}^{*}Ma_{k+q}$, with $a_{k}^{*}Ma_{l} = \sum_{\alpha,\beta}M_{\alpha\beta}a_{k,\alpha}^{*}a_{l,\beta}$, $\rho_{q} = \rho_{q}(\id)$, $n(S) = \sum_{k\in S}a_{k}^{*}a_{k}$, and let $E_{-}(q) = (W \cap (W - q)) \setminus (W + q)$ and $E_{+}(q) = (W \cap (W + q)) \setminus (W - q)$ be the entry and exit strips.
\begin{enumerate}
\item[(i)] \emph{(Strip identity.)} $[\rho_{q}(M), \rho_{q}(M')^{*}] = \sum_{k \in W\cap(W-q)}a_{k}^{*}MM'^{*}a_{k} - \sum_{k \in W\cap(W+q)}a_{k}^{*}M'^{*}Ma_{k}$ exactly; in particular $[\rho_{q}, \rho_{q}^{*}] = n(E_{-}(q)) - n(E_{+}(q))$, with $|E_{-}(q)| = |E_{+}(q)|$.
\item[(ii)] \emph{(Zero form.)} If a state has the same total occupation $\omega(a_{k}^{*}a_{k})$ at every momentum of $E_{-}(q) \cup E_{+}(q)$, then $\omega([\rho_{q}, \rho_{q}^{*}]) = 0$. This holds at every $q$ and on every window for the sea that fills one channel state per momentum (the lower band of a two-channel $h(k)$, in particular the relativistic sea in any dimension and the $1 + 1$ Dirac sea of both chiralities, where each chirality alone gives $\pm\min(q, 2N - q)$) and for a sea contained in $W \cap (W - q) \cap (W + q)$ (a bounded Fermi sea away from the window's edges): their total density modes carry no canonical pair.
\item[(iii)] \emph{(One null direction.)} For $W = \{-N, \dots, N - 1\}^{d}$ and the sea $F = \{k : k_{1} < 0\}$ in every channel, $\omega_{F}([\rho_{q}, \rho_{q}^{*}]) = c\,\min(q_{1}, 2N - q_{1})\prod_{j \ge 2}(2N - |q_{j}|)$ for $q_{1} \ge 0$ (and its negative for $q_{1} < 0$), and the commutator acts as this number on every vector that agrees with $F$ on the strips; it vanishes for $q_{1} = 0$.
\item[(iv)] \emph{(The density-current term.)} For two channels, the sea of the lower band of $h(k) = \sum_{i}k_{i}\sigma_{i}$ ($\sigma_{i}$ the channel arrays representing the generators of the Pauli algebra $\Cl(3,0)$, the band projector $\tfrac12(1 - k/|k|)$), the cube $W = \{-N, \dots, N - 1\}^{d}$ and $q = (0, \dots, 0, q)$, $1 \le q < N$: $\omega([\rho_{q}, \rho_{q}(\sigma_{3})^{*}]) = \sum_{k\in E_{-}\cup E_{+}}|k_{d}|/|k|$, a sum over $2q(2N)^{d-1}$ strip points. It equals $2q$ for $d = 1$ ($h = k\sigma_{3}$), and lies in $(4qN(N - q), 8qN^{2}]$ for $d = 3$, while $\omega([\rho_{q}, \rho_{q}^{*}]) = 0$ by (ii).
\end{enumerate}
Clauses (i) to (iv) are proved. \emph{Reading (argued).} Exact density bosons need a sea that is a half-space in one direction, as on a null generator, whose modes have no transverse dispersion: there, by (iii), each transverse mode carries the one-dimensional chiral boson (Theorem \claimref{synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum}(vi) on the band), and densities with purely transverse momentum carry none. Bulk matter in $3 + 1$ dimensions is cases (ii) and (iv): its density modes carry no canonical pair, and its central term is the density-current Schwinger term, located at the cut-off and growing as its square. So the series' exact bosons are one-dimensional, per generator, and not propagating $3 + 1$ bosons.

## technical
Put fermion modes on a finite window of momenta in $d$ dimensions, each a tower plane, with finitely many channels per momentum, and form the densities $\rho_{q}(M) = \sum_{k}a_{k}^{*}Ma_{k+q}$. (i) Exactly, $[\rho_{q}(M), \rho_{q}(M')^{*}]$ is the sum of $a_{k}^{*}MM'^{*}a_{k}$ over the momenta $k$ with $k + q$ in the window minus the sum of $a_{k}^{*}M'^{*}Ma_{k}$ over those with $k - q$ in the window; for the plain density this is the number in an entry strip minus the number in an exit strip of the same size. (ii) So the density form vanishes in any state with the same total occupation all over the strips: the relativistic sea, which fills one state per momentum in any dimension (also the $1 + 1$ Dirac sea of both chiralities, whose two chiralities give $\pm\min(q, 2N - q)$ separately), and any bounded Fermi sea away from the window's edges; their density modes have no canonical pair on any window. (iii) A sea filling the half-space $k_{1} < 0$ gives the one-dimensional value $\min(q_{1}, 2N - q_{1})$ times the transverse overlap and the channel number, and nothing for transverse $q$. (iv) For the two-component relativistic sea the central term sits instead in the density-current commutator, $\sum|k_{d}|/|k|$ over the strips: $2q$ in one dimension, between $4qN(N - q)$ and $8qN^{2}$ in three, growing with the square of the cut-off. Reading (argued): exact bosonisation needs one null direction without transverse dispersion, which the series has on each horizon generator (one chiral boson per transverse mode); bulk $3 + 1$ densities are not bosons.

## lay
In one dimension, ripples in a sea of fermions behave exactly like bosons, and the graph uses this on the light rays that make up a horizon. This result checks what happens in more dimensions. The boson behaviour comes from the edge of the sea: it needs a sea filled on one side of a single direction. A sea of the kind that fills ordinary three-dimensional space gives density ripples with no boson behaviour at all, on any finite piece of it, and its only trace of the effect sits at the cut-off and grows with it. Light rays on a horizon have exactly one direction of motion, so there the boson behaviour holds for each ray separately, but it does not produce bosons that move through three-dimensional space.

## one-liner
On any finite window of momenta the density form is an entry-strip minus an exit-strip occupation, so relativistic and bounded seas give density modes no canonical pair in any dimension; only a half-space sea along one null direction does.
