---
id: synthesis.floor-regulator-keeps-the-charge-and-the-central-term-below-the-cut-off
kind: claim
version: 3
title: 'A floor keeps the charge and, below the cut-off, the central term'
status: proved
region: synthesis
subject: quantum-fields
tags: [car-algebra, ladder-pairs, recovers-known-physics, no-go]
proposed_by:
  kind: ai
  session: 2026-11-01-qft
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.tower.tower
derivations:
- name: main
  uses:
  - field-theory.imported-tower-limit@3
  - field-theory.twistor-attachment@6
  - field-theory.no-canonical-commutation-relations-tower@3
  - field-theory.how-close-tower-comes-ccr@4
  - synthesis.imported-schwinger-term-and-mattis-lieb-density-algebra@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_floor_keeps_charge_and_continuity
- kind: check
  ref: check.py::check_central_term_is_an_edge_operator
- kind: check
  ref: check.py::check_sea_value_and_spectral_weight
- kind: check
  ref: check.py::check_conformal_energy_cut_keeps_no_boost
- kind: check
  ref: check.py::check_no_weighting_of_the_conformal_energy_keeps_a_boost
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - field-theory.how-close-tower-comes-ccr
  - field-theory.twistor-attachment
  derived_from:
  - synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator-and-ward-preserving-extensions-differ-only-by-the-renormalisation-constants
extraction:
  maintainer_pass_2026_11_02:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 2 -> 3, by Leon''s decision of 2026-11-02 to merge the floors no-go of the regulator-free vacuum polarisation (its clause (vii)) into this result: new clause (v), the closure of the seven-dimensional commutant of (iv) with any one boost, translation, special conformal generator or the dilation to all fifteen bivectors (computed for every anticommuting basis bivector and every boost, translation and special conformal generator of the standard basis, argued for an arbitrary element outside the commutant), and by Schur''s lemma no weighting of the floors by conformal energy, sharp or smooth, keeps a boost; with its proof step and a new check function (the closure computation of the regulator-free result). Clauses (i) to (iv) unchanged. The source is recorded under lineage (derived_from) and cited in the text; no uses edge, since the regulator-free result uses this one.'
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 1 -> 2, by Leon''s list of imports of 2026-11-01: a uses edge to the imported Fact synthesis.imported-schwinger-term-and-mattis-lieb-density-algebra@1 (Schwinger''s commutator term, the Tomonaga and Mattis-Lieb density algebra and its truncated-band origin), which replaces the citations from memory; the pin of field-theory.twistor-attachment moves to @6 (a marked spin-statistics note added there, content unchanged). Statement and check unchanged.'
  open_problem: op.qft-loops-and-renormalisation
  note: >-
    Tests the problem's third attack line, a regulator native to the series, on the tower's finite floors
    read as mode cut-offs (on the twistor attachment the floors are energy cut-offs). The free continuity
    equation and the charge survive exactly on every floor; the central (Schwinger commutator) term of the
    density algebra, which carries the vacuum polarisation of a one-chirality field and the chiral anomaly in
    two dimensions, cannot be a scalar on a floor (the trace argument of the no-CCR theorem) and is an edge
    operator there, equal to the continuum value on the filled sea for momenta up to the cut-off. The
    one-dimensional chiral field on a circle is the computed model; the four-dimensional statement is argued.
    The conformal-energy cut keeps the compact subalgebra and no boost, so the floors are not a
    Lorentz-invariant regulator. The density algebra, its central term and bosonisation are standard (imported,
    synthesis.imported-schwinger-term-and-mattis-lieb-density-algebra: Schwinger 1959 for the commutator term,
    Tomonaga and Mattis-Lieb for the density algebra);
    the new content is that the tower's floors reproduce them exactly below the cut-off and what they break.
    Transport-absent for clauses (i) to (iii) (CAR truncation); transport-convenient for (iv) (the conformal
    model). The bosonisation of the Schwinger model is cited from memory. Clause (v), merged on 2 November 2026 from
    the regulator-free vacuum polarisation (its clause (vii)), is transport-convenient (the conformal model); Schur's
    lemma for irreducible unitary representations and the irreducibility of the attachment's one-particle helicity
    modules under the conformal algebra are cited from memory.
---

## formal
Let a floor of the tower carry $2N$ planes, with mode operators $a_k^{*}, a_k$ ($k = -N, \dots, N - 1$) obeying the CAR of Fact \claimref{field-theory.imported-tower-limit}, read as the right-moving modes of one chirality on a circle of $2N$ momenta in units of the circle's $2\pi/L$, with $n_k = a_k^{*}a_k$, $H = \sum_k k\,n_k$, $\mathcal{N} = \sum_k n_k$ and $\rho(p) = \sum_{k,\,k+p} a_{k+p}^{*}a_k$ (both indices in the window).
\begin{enumerate}
\item[(i)] \emph{(Charge and continuity; proved.)} $[\mathcal{N}, H] = 0$, $[\mathcal{N}, \rho(p)] = 0$ and $[H, \rho(p)] = p\,\rho(p)$ exactly on every floor, for $1 \le |p| \le 2N - 1$; $\rho(\pm 2N) = 0$.
\item[(ii)] \emph{(The central term is an edge operator; proved.)} For $1 \le p \le 2N$,
\[
[\rho(p), \rho(-p)] = \sum_{k \ge N - p} n_k - \sum_{k < -N + p} n_k ,
\]
whose scalar part is zero; no floor carries a nonzero scalar central term.
\item[(iii)] \emph{(The continuum value below the cut-off; proved.)} On the filled sea $\Omega$ ($n_k = 1$ for $k < 0$, $0$ otherwise), $\rho(-p)\Omega = 0$, $[\rho(-p), \rho(p)]\Omega = \min(p, 2N - p)\,\Omega$, and $\rho(p)\Omega$ is an eigenvector of $H$ at energy $E_\Omega + p$ with $\rho(-p)\rho(p)\Omega = \min(p, 2N - p)\,\Omega$. So $b_p = \rho(-p)/\sqrt{p}$ satisfies $[b_p, b_p^{*}] = 1$ on $\Omega$ exactly for $p \le N$, the continuum central term $p$ and the continuum one-loop density response (all spectral weight at energy $p$, total weight $p$) are reproduced exactly up to the cut-off, and above it the weight is $2N - p$. The value depends on the state at the window's edges: with the top mode also occupied, $[\rho(-1), \rho(1)]$ acts as $0$.
\item[(iv)] \emph{(No boost survives the conformal-energy cut; proved.)} In $\Cl(2,4)$ the commutant of the conformal Hamiltonian $\gamma_0e_+$ (the compact combination of $P_0 = \gamma_0n_\infty$ and $K_0 = \gamma_0n_0$, up to normalisation) among the fifteen bivectors is seven-dimensional; it meets the Lorentz bivectors in the span of the three rotations and contains no nonzero translation and no nonzero special conformal generator. So, if the floors are the conformal-energy cut-offs of Proposition \claimref{field-theory.twistor-attachment}, every finite floor is invariant under the spatial rotations and not under any boost.
\item[(v)] \emph{(No weighting of the floors keeps a boost; merged from Theorem \claimref{synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator-and-ward-preserving-extensions-differ-only-by-the-renormalisation-constants}(vii), 2 November 2026.)} The commutant $\mathfrak{k}$ of (iv) is closed under the commutator, and $\mathfrak{k}$ together with any one of the eight basis bivectors that anticommute with $\gamma_0e_+$ (among them the dilation $e_+e_-$), or of the boosts $\gamma_0\gamma_j$, the translations $\gamma_\mu n_\infty$ and the special conformal generators $\gamma_\mu n_0$, generates all fifteen bivectors (computed); for an arbitrary element outside $\mathfrak{k}$ the same follows from the irreducibility of the eight-dimensional complement under $\mathfrak{k}$ (argued). Hence on an irreducible unitary module, such as the attachment's one-particle helicity modules of Proposition \claimref{field-theory.twistor-attachment} (irreducibility cited), a bounded weighting $f(\gamma_0e_+)$ of the modes by conformal energy that commutes with one boost commutes with the whole conformal algebra and is a multiple of the identity (Schur's lemma, cited): no weighting of the floors, sharp or smooth, keeps a boost.
\end{enumerate}
\emph{Reading.} As a regulator the floors keep the global Ward identity (charge conservation and the free continuity equation) exactly at every floor. The central term that makes the one-chirality density algebra a boson algebra, and that fixes the chiral fermion's vacuum polarisation and the two-dimensional chiral anomaly, is not a scalar on any floor (by the trace argument of Proposition \claimref{field-theory.no-canonical-commutation-relations-tower}); it is an edge operator that equals its continuum value on the filled sea for every momentum up to the cut-off, the density analogue of the quasi-spin $[b, b^{*}] = 1 - 2k/n$ of Proposition \claimref{field-theory.how-close-tower-comes-ccr}. The regulator breaks Lorentz invariance at every finite floor, keeping only the compact part of the conformal algebra, and by (v) no smoothing of the cut-off restores a boost. A sharp cut-off on conformal energy also leaves terms in the regulated zero-point energy that match no local invariant, which a cut-off vanishing with its slope at the edge removes (\claimref{synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations}); clauses (i) to (iii) concern the sharp cut-off only.

## technical
The tower's finite floors are the natural candidate for a regulator native to the series: on the twistor attachment they are energy cut-offs. Nothing specific to the tower enters clauses (i) to (iii): they hold for any finite truncation of a chiral band, and the truncated-band origin of the central term is standard (Mattis and Lieb). This result tests what such a sharp cut-off keeps, on the computed model of a one-chirality field on a circle with $2N$ momentum modes taken from $2N$ tower planes, $H = \sum_k k\,n_k$ and densities $\rho(p) = \sum_k a_{k+p}^{*}a_k$.

The global Ward identity survives exactly: the charge commutes with $H$ and with every density, and $[H, \rho(p)] = p\,\rho(p)$, the free continuity equation of a chiral current, holds on every floor. The central term of the density algebra does not survive as a scalar: $[\rho(p), \rho(-p)]$ is the number in the top $p$ modes minus the number in the bottom $p$ modes, an edge operator with zero scalar part, as the trace argument of the no-CCR theorem requires. On the filled sea it equals $\min(p, 2N - p)$, so the continuum value $p$ (the Schwinger commutator term, the boson normalisation of bosonisation, and the weight of the chiral fermion's one-loop density response, all at energy exactly $p$) is reproduced exactly for $p \le N$ and falls linearly above the cut-off. With an excitation at the window's edge the value changes, so the central term holds on states with vacuum-like edges, as the quasi-spin reaches the CCR only on states of bounded number.

Lorentz invariance is not kept: in $\Cl(2,4)$ the commutant of the conformal Hamiltonian $\gamma_0e_+$ is the seven-dimensional compact algebra, which contains the three spatial rotations and no boost, translation or special conformal generator. A conformal-energy cut therefore regulates in one conformal frame; the four-dimensional loop integrals of the standard theory with a Lorentz-invariant regulator are not what the floors give. Nor does smoothing help: the commutant together with any one boost generates the whole conformal algebra, so on an irreducible module a weighting of the modes by conformal energy that commutes with a boost commutes with everything and is a constant (Schur's lemma); no weighting of the floors, sharp or smooth, keeps a boost (merged on 2 November 2026 from the regulator-free vacuum polarisation, where it was first stated).

## lay
A calculation in quantum field theory with loops needs a regulator, a way of cutting off the infinitely many high-energy modes. The series has a natural candidate: its tower is built floor by floor, each floor holding finitely many fermion modes, and on the series' link to spacetime the floors are energy cut-offs. This result tests that candidate, and with it any sharp cut-off on the number of modes, on a simple model, one chirality of a fermion moving around a circle. The floor keeps electric charge exactly and keeps the charge flowing correctly. The subtle quantum term that gives the vacuum its polarisability, and that underlies the anomaly of chiral fermions, cannot exist exactly on any finite floor; instead it appears at the floor's edges, and it takes exactly the right value for every wavelength longer than the cut-off, provided the modes near the cut-off are in their vacuum state. The price is relativity: a floor is defined by one notion of energy and is unchanged by rotations but not by boosts. Smoothing the cut-off does not help: no gradual weighting of the floors by energy restores the boosts.

## one-liner
On a sharp cut-off of $2N$ one-chirality momentum modes (a floor of the tower, or any finite truncation of a chiral band) the charge and $[H, \rho(p)] = p\rho(p)$ are exact, $[\rho(p), \rho(-p)]$ is the edge operator (top $p$ numbers minus bottom $p$ numbers), equal to the continuum central term $p$ on the filled sea and on states with vacuum-like edges exactly for $p \le N$ and $\min(p, 2N - p)$ above, and not on states excited at the edges; the conformal-energy cut keeps the rotations but no boost, and no weighting of the floors by conformal energy, sharp or smooth, keeps one (the commutant with one boost generates the conformal algebra; Schur); transport-absent except (iv), (v).
