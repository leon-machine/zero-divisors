---
id: synthesis.density-modes-bosonise-only-along-one-null-direction
kind: claim
version: 1
title: 'Window density forms are strip differences; total densities of uniform seas carry none'
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
    higher dimension, and what the series needs). Restated after review. Answer: on finite windows of momenta in
    any dimension the commutator of two density modes with any shifts is an exact difference of two bilinear sums
    (the level-one u(n) current algebra on a window, any d), and for equal shifts the density form is the
    occupation of an entry strip minus that of an equal exit strip. So total density modes carry no canonical
    pair in any state with uniform total occupation on the strips (the one-band relativistic sea in any
    dimension, the 1+1 Dirac sea of both chiralities) and, for a given q, in any sea clear of the strips;
    channel-resolved densities can carry one (each chirality of the 1+1 sea; the spin-resolved density of the
    3+1 sea, mean value half the density-current sum). A half-space sea gives the sharp one-dimensional value
    times the transverse overlap, scalar on the sea; quadrant and tilted seas give other nonzero values, so a
    half-space is not necessary for a nonzero form, only for this sharp value. The density-current sum of the
    two-component relativistic sea is bounded in (4qN(N - q), 8qN^2] for d = 3; its growth (2N)^(d-1) is the
    transverse mode count, the value per transverse momentum being of order q, as in d = 1 (2q). Credits: (iii)
    is the finite-window form of the leading Fermi-surface patch commutator of higher-dimensional bosonisation
    (Haldane; Houghton and Marston; Castro Neto and Fradkin; cited from memory), whose patch-edge corrections are
    not computed here; (ii) for total densities is the finite-band statement of Mattis and Lieb (stored as
    imported, synthesis.imported-schwinger-term-and-mattis-lieb-density-algebra (ii)) sized on windows; (iv) is
    the classical quadratic divergence of the 3+1 Schwinger term (Schwinger 1959, stored clause (iii) of the same
    Fact), here bounded on a cube. These are prior art, not premises. New here: the window statements with
    channel arrays and unequal shifts in any dimension (which the proposals
    synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins (i) and
    synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators (iv) cite), the exact zero for
    uniform seas on every window, the per-q scope for bounded seas, and the exact cube bounds. Stored and cited,
    not refiled: the one-dimensional, one-channel edge identity (hawking.current-commutator-exactly-edge-split)
    and the floor value min(p, 2N - p) (floor-regulator (ii), (iii)); the per-generator stacking over transverse
    modes is fluctuation-forms (vi) for each unit vector of K. Reading (argued): the series' exact bosons are
    per generator, sharp on the half-space sea of each generator; whether propagating 3+1 bosons arise is not
    addressed. Ledger: transport-absent (finite CAR on tower planes; transport not used).
---

## formal
Let the modes $a_{k,\alpha}$ carry a momentum $k$ in a finite window $W \subset \mathbb{Z}^{d}$ and a channel $\alpha$ in a finite set of $c$ channels; each mode is a tower plane, $a^{*} = v$, $a = w$ (Theorem \claimref{tower.ladder-pairs-satisfy-car-vectors}), $v^{*} = w$, numbers in $\mathrm{span}\{1, J\}$ with $J$ the kernel bivector. For a channel array $M$ and a shift $m \in \mathbb{Z}^{d}$ let $\rho_{m}(M) = \sum_{k, k+m \in W}a_{k}^{*}Ma_{k+m}$, with $a_{k}^{*}Ma_{l} = \sum_{\alpha,\beta}M_{\alpha\beta}a_{k,\alpha}^{*}a_{l,\beta}$, so $\rho_{m}(M)^{*} = \rho_{-m}(M^{*})$; $\rho_{q} = \rho_{q}(\id)$, $n(S) = \sum_{k\in S}a_{k}^{*}a_{k}$, and $E_{-}(q) = (W \cap (W - q)) \setminus (W + q)$, $E_{+}(q) = (W \cap (W + q)) \setminus (W - q)$ the entry and exit strips.
\begin{enumerate}
\item[(i)] \emph{(Window identity.)} For all shifts $m, l$ and arrays $M, M'$, exactly,
\[
[\rho_{m}(M), \rho_{l}(M')] = \sum_{k, k+m, k+m+l \in W}a_{k}^{*}MM'a_{k+m+l} - \sum_{k, k+l, k+l+m \in W}a_{k}^{*}M'Ma_{k+l+m} .
\]
In particular $[\rho_{q}(M), \rho_{q}(M')^{*}] = \sum_{k \in W\cap(W-q)}a_{k}^{*}MM'^{*}a_{k} - \sum_{k \in W\cap(W+q)}a_{k}^{*}M'^{*}Ma_{k}$ and $[\rho_{q}, \rho_{q}^{*}] = n(E_{-}(q)) - n(E_{+}(q))$, with $|E_{-}(q)| = |E_{+}(q)|$.
\item[(ii)] \emph{(Uniform seas.)} If a state has the same total occupation $\omega(a_{k}^{*}a_{k})$ at every momentum of $E_{-}(q) \cup E_{+}(q)$, then $\omega([\rho_{q}, \rho_{q}^{*}]) = 0$. This holds at every $q$ and on every window for the sea that fills one channel state per momentum (the lower band of a two-channel $h(k)$, in particular the relativistic sea in any dimension and the $1 + 1$ Dirac sea of both chiralities), and, for a given $q$, for a sea contained in $W \cap (W - q) \cap (W + q)$ (for $d = 1$, $N = 3$, the sea $\{-2, -1, 0\}$ gives $0, 1, 1$ at $q = 1, 2, 3$). The forms $\omega([\rho_{q}, \rho_{q'}^{*}])$, $q \ne q'$, vanish in every state diagonal in momentum; so in a uniform sea the total density modes carry no canonical pair. Channel-resolved densities $\rho_{q}(M)$ need not: each chirality of the $1 + 1$ Dirac sea gives $\pm\min(q, 2N - q)$, and $\rho_{q}(\tfrac12(1 + \sigma_{3}))$ of the sea of (iv) gives half the sum in (iv).
\item[(iii)] \emph{(Half-space sea.)} For $W = \{-N, \dots, N - 1\}^{d}$ and the sea $F = \{k : k_{1} < 0\}$ in every channel, $\omega_{F}([\rho_{q}, \rho_{q}^{*}]) = c\,\min(q_{1}, 2N - q_{1})\prod_{j \ge 2}(2N - |q_{j}|)$ for $q_{1} \ge 0$ (and its negative for $q_{1} < 0$), and the commutator acts as this number on every vector that agrees with $F$ on the strips; it vanishes for $q_{1} = 0$. Other seas with unequally occupied strips give other values (for $d = 2$, $N = 3$, one channel: the quadrant $\{k_{1} < 0, k_{2} < 0\}$ gives $3$ at $q = (1, 0)$ and $5$ at $q = (1, 1)$, the tilted half-space $\{k_{1} + k_{2} < 0\}$ gives $5$ at $q = (1, 0)$).
\item[(iv)] \emph{(The density-current term.)} For two channels, the sea of the lower band of $h(k) = \sum_{i}k_{i}\sigma_{i}$ ($\sigma_{i}$ the channel arrays representing the generators of the Pauli algebra $\Cl(3,0)$, band projector $\tfrac12(1 - \hat k)$, $\hat k = k/|k|$), the cube $W = \{-N, \dots, N - 1\}^{d}$ and $q = (0, \dots, 0, q)$, $1 \le q < N$: $\omega([\rho_{q}, \rho_{q}(\sigma_{3})^{*}]) = S := \sum_{k\in E_{-}\cup E_{+}}|k_{d}|/|k|$, a sum over $2q(2N)^{d-1}$ strip points; $\omega([\rho_{q}(P_{+}), \rho_{q}(P_{+})^{*}]) = S/2$ for $P_{+} = \tfrac12(1 + \sigma_{3})$, while $\omega([\rho_{q}, \rho_{q}^{*}]) = 0$ by (ii). $S = 2q$ for $d = 1$ ($h = k\sigma_{3}$), and $S \in (4qN(N - q), 8qN^{2}]$ for $d = 3$.
\end{enumerate}
Clauses (i) to (iv) are proved. \emph{Reading (argued).} Density modes with a sharp central value on the sea arise for a sea that is a half-space in one direction, as on a null generator, whose modes have no transverse dispersion (there each transverse mode carries the one-dimensional chiral boson, Theorem \claimref{synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum}(vi) on the band), and, approximately, on each patch of a Fermi surface; other seas with unequal strip occupations (quadrants, tilted or edge-crossing seas) give nonzero but different values, and the spin-resolved densities of the $3 + 1$ relativistic sea have a nonzero mean form at the cut-off, $S/2$, with a relative mean-square defect that in floating-point evaluation decreases like $N^{-2}$ ($N = 2, \dots, 8$, not part of the proof). The total density modes of the $3 + 1$ relativistic sea carry no canonical pair; the growth $(2N)^{d-1}$ of $S$ is the transverse mode count, the value per transverse momentum being of order $q$, as in $d = 1$. So the series' exact bosons are per generator, sharp on each generator's half-space sea; whether propagating $3 + 1$ bosons arise is not addressed.

## technical
Put fermion modes on a finite window of momenta in $d$ dimensions, each a tower plane, with finitely many channels per momentum, and form the densities $\rho_{m}(M) = \sum_{k}a_{k}^{*}Ma_{k+m}$ for any shift $m$. (i) Exactly, $[\rho_{m}(M), \rho_{l}(M')]$ is the sum of $a_{k}^{*}MM'a_{k+m+l}$ over $k$ with $k + m$ and $k + m + l$ in the window minus the sum of $a_{k}^{*}M'Ma_{k+l+m}$ over $k$ with $k + l$ and $k + l + m$ in the window; for the plain density with equal shifts this is the number in an entry strip minus the number in an exit strip of the same size. (ii) So the form of the total density vanishes in any state with the same total occupation all over the strips: the relativistic sea, which fills one state per momentum in any dimension, and the $1 + 1$ Dirac sea of both chiralities at every $q$; and, for the $q$ at hand, a Fermi sea clear of the strips. Forms between unequal shifts vanish in momentum-diagonal states, so the total density modes of a uniform sea carry no canonical pair. Channel-resolved densities can: each chirality of the $1 + 1$ sea gives $\pm\min(q, 2N - q)$. (iii) A sea filling the half-space $k_{1} < 0$ gives the sharp one-dimensional value $\min(q_{1}, 2N - q_{1})$ times the transverse overlap and the channel number, and nothing for transverse $q$; quadrant and tilted seas give other nonzero values. (iv) For the two-component relativistic sea the density-current form is $S = \sum|k_{d}|/|k|$ over the strips, and the spin-resolved density has form $S/2$: $S = 2q$ in one dimension, between $4qN(N - q)$ and $8qN^{2}$ in three, the factor $(2N)^{2}$ being the transverse mode count. Reading (argued): densities with a sharp central value come from a half-space sea, as on each horizon generator (one chiral boson per transverse mode) and approximately on Fermi-surface patches; total densities of the $3 + 1$ relativistic sea carry no canonical pair; propagating $3 + 1$ bosons are not addressed.

## lay
In one dimension, ripples in a sea of fermions behave exactly like bosons, and the graph uses this on the light rays that make up a horizon. This result checks what happens in more dimensions on finite pieces of momentum space. The boson behaviour comes from the edge of the sea, and it is sharp for a sea filled on one side of a single direction. In a sea of the kind that fills ordinary three-dimensional space, the total density ripples have no boson behaviour on any finite piece of it; ripples of one spin component do, on average, through the edge of the momentum range, but not sharply. Light rays on a horizon have exactly one direction of motion, so there the boson behaviour holds sharply for each ray separately; whether bosons moving through three-dimensional space arise is not settled here.

## one-liner
On any finite window of momenta the density form is the occupation of an entry strip minus that of an exit strip, so total density modes carry no canonical pair in seas with uniform occupation on the strips (one-band relativistic seas in any dimension, bounded seas clear of the strips); a half-space sea gives the sharp one-dimensional value times the transverse overlap, and the two-component relativistic sea carries its form in the density-current pairing, in $(4qN(N - q), 8qN^{2}]$ for $d = 3$ and not sharp on the sea.
