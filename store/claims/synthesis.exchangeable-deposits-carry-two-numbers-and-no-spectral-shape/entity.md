---
id: synthesis.exchangeable-deposits-carry-two-numbers-and-no-spectral-shape
kind: claim
version: 1
title: 'An exchangeable deposit supplies two second moments; any shape is the placement''s'
status: proved
region: synthesis
subject: dark-energy
tags: [no-go, car-algebra, representation-theory, finite-models]
proposed_by:
  kind: ai
  session: 2026-11-16-spectrum
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-16-spectrum
review: draft
derivations:
- name: main
  uses:
  - synthesis.finite-range-descent-deposit-cannot-seed-cmb@6
  - synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise@5
  - synthesis.ladder-states-are-locally-product-with-non-gaussian-fluctuations@1
  - tower.ladder-pairs-satisfy-car-vectors@4
  - synthesis.frozen-phase-spectrum-not-red@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_doubly_transitive_relabelling_leaves_two_numbers
- kind: check
  ref: check.py::check_embedding_supplies_the_only_shape
- kind: check
  ref: check.py::check_exchangeable_fermion_states
- kind: check
  ref: check.py::check_similarities_are_doubly_transitive_and_leave_one_exponent
- kind: check
  ref: check.py::check_placements_tiling_lattice_and_off_lattice
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.finite-range-descent-deposit-cannot-seed-cmb
  - synthesis.ladder-states-are-locally-product-with-non-gaussian-fluctuations
  - standard-model.dating-descent
extraction:
  maintainer_pass_2026_11_16:
    by: maintainer-2026-11-16
    date: '2026-11-16'
    note: 'Pin review, version kept: the pin to synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise moved 4 -> 5 (the variance formula of its clause (i), the only part used here, is unchanged). The id is kept by Leon''s decision of 16 November 2026. No number or clause changed.'
  open_problem: op.descent-state-and-spectrum
  note: >-
    The stored finite-range bound leaves one escape for a passive deposit: correlations set before or outside the
    descended metric, "initial data of the pre-metric sector". This result says what such data must carry. A
    deposit laid down with no geometric information is invariant under relabelling of its units, and then its
    second moments are two numbers; every dependence of a slice spectrum on the wavenumber is that of the map of
    the units into the slice, which is not part of the state. For cells that tile the slice, and for point cells
    on a periodic lattice, the spectrum is white, the stored finite-range class; for point cells that are not on
    a lattice the second number multiplies the placement's own structure factor, so the placement can carry a
    shape, and that case is in the statement as its boundary. The exact criterion for two numbers is transitivity
    of the invariance group on unordered pairs of units. So (argued) the escape needs a state whose invariance
    group separates pairs, that is, a deposit that already carries the separations of its units, or a placement
    of the units in the slice that carries the shape; a conformal structure alone leaves one exponent, the
    weight, which is the stored reading of the frozen phase. Kill condition written before the proof: an
    exchangeable state whose slice two-point function is not white plus a zero mode refutes the claim. For cells
    tiling the slice or on a lattice none exists (the constants and the vectors of zero sum are the only
    invariant subspaces that a covariance of this symmetry distinguishes); for point cells off a lattice two
    cells a quarter circle apart are such a state, so the claim is stated with that restriction. Transport-absent
    in its core (a symmetry argument valid for any algebra of observables); transport-convenient in clause (iv),
    where the fermion modes are null vectors of tower planes and the stored ladder states are the worked example.
    A white spectrum of the matter contrast is not a white spectrum of the curvature perturbation: the conversion
    depends on the descent slice, which the series leaves free, and it is not part of this result. The triple
    transitivity of the Lorentz group on null directions, mentioned in the technical text, is standard and is
    not used in the proof.
---
## formal
Let a deposit consist of $N \ge 2$ units labelled $1, \dots, N$ (cells of the descent slice, light rays, tower blocks), with Hermitian elements $O_{1}, \dots, O_{N}$ of its algebra of observables, and let a group $G$ of relabellings act on that algebra by automorphisms $\alpha_{g}$ with $\alpha_{g}(O_{i}) = O_{g i}$. For a state $\omega$ put
\[
C_{ij} = \tfrac12\,\omega(O_{i}O_{j} + O_{j}O_{i}) - \omega(O_{i})\,\omega(O_{j}), \qquad v = C_{11},
\]
and write $U$ for the $N \times N$ matrix with every entry $1$. The state is \emph{exchangeable} when $\omega \circ \alpha_{g} = \omega$ for every $g$ in the symmetric group of the labels.
\begin{enumerate}
\item[(i)] \emph{(Two numbers.)} If $\omega \circ \alpha_{g} = \omega$ for all $g \in G$ and $G$ is transitive on the labels and on unordered pairs of distinct labels (every doubly transitive group is, the symmetric group among them; for $N \ge 3$ the second condition implies the first), then $C = (v - c)\,1 + c\,U$ for one number $c$: $C$ has the eigenvalue $v - c$ on every vector of zero sum and $v + (N - 1)c$ on the constants, and positivity is $-v/(N - 1) \le c \le v$.
\item[(ii)] \emph{(No shape.)} Let each unit sit in a slice with a real profile $g_{i}$, so that the slice field is $\phi(x) = \sum_{i}g_{i}(x)\bigl(O_{i} - \omega(O_{i})\bigr)$, and for a real test function $f$ let $f_{i} = \int f g_{i}$. Under the hypothesis of (i),
\[
\mathrm{Var}_{\omega}\bigl(\phi(f)\bigr) = (v - c)\sum_{i}f_{i}^{2} + c\Bigl(\sum_{i}f_{i}\Bigr)^{2}.
\]
The state enters through $v - c$ and $c$ alone; the dependence on $f$, and so on the wavenumber, is that of two quadratic forms fixed by the embedding. Two cases are white. (a) \emph{Cells that tile the slice}, $\sum_{i}g_{i} = 1$: then $\sum_{i}f_{i} = \int f = 0$ for every mode of nonzero wave vector, the variance is $(v - c)\sum_{i}f_{i}^{2}$, constant in $k$ below the inverse size of a cell and multiplied above it by the squared transform of the cells. (b) \emph{Point cells on a periodic lattice}, $g_{i} = V_{c}\,\delta(x - x_{i})$ at the points $x_{i}$ of a lattice of cell volume $V_{c}$: every cosine or sine mode of nonzero wave vector of the dual lattice has $\sum_{i}f_{i} = 0$, and $P(k) = (v - c)V_{c}$ for every such $k$. In both cases $\Delta^{2}(k) = k^{3}P/2\pi^{2} \propto k^{3}$ on those scales, the finite-range class of Theorem \claimref{synthesis.finite-range-descent-deposit-cannot-seed-cmb}, together with a term supported at $k = 0$. \emph{Boundary of the statement.} For point cells that are not on a lattice the second term does not vanish at nonzero wave vector: the sum of the cosine and sine variances is $V_{c}^{2}\bigl[(v - c)N + c\,N S_{\mathrm{pl}}(k)\bigr]$ with $S_{\mathrm{pl}}(k) = N^{-1}\bigl[(\sum_{i}\cos k\cdot x_{i})^{2} + (\sum_{i}\sin k\cdot x_{i})^{2}\bigr]$ the structure factor of the placement, and $c$ may be as large as $v$; so the spectrum then has the placement's shape, weighted by the state's second number. The smallest case: two cells at $x = 0$ and $x = L/4$ on a circle of length $L$; the modes $\cos(2\pi x/L)$ and $\cos(4\pi x/L)$ have $f = (1, 0)$ and $f = (1, -1)$ and variances $v$ and $2(v - c)$, whose ratio depends on $c$.
\item[(iii)] \emph{(The criterion.)} If $G$ is transitive on the labels but not on unordered pairs of distinct labels, let $A$ be the adjacency matrix of one orbit of $G$ on such pairs, of valency $d$. For $0 < |\varepsilon| < 1/d$ the matrix $1 + \varepsilon A$ is $G$-invariant, positive definite and not of the form in (i), and it is the covariance of a $G$-invariant state (the centred Gaussian measure with that covariance, the $O_{i}$ being the coordinates). So, for $G$ transitive on the labels, the two-number form holds for every $G$-invariant state exactly when $G$ is transitive on unordered pairs of distinct labels, and in general the number of free second moments is one more than the number of orbits of $G$ on such pairs.
\item[(iv)] \emph{(Fermion modes.)} Let the units be $N$ fermion modes, $a_{i}^{*} = v_{i}$ and $a_{i} = w_{i}$ the null vectors of $N$ tower planes (Theorem \claimref{tower.ladder-pairs-satisfy-car-vectors}), with the symmetric group permuting the planes, and let $\omega$ be exchangeable. Then the one-particle matrix is $E_{ij} = \omega(a_{j}^{*}a_{i}) = (n - e)\delta_{ij} + e$ with $n$ and $e$ real, the pairing vanishes, $\omega(a_{i}a_{j}) = 0$ for all $i, j$, and in particular $-n/(N - 1) \le e \le (1 - n)/(N - 1)$, so $|e| \le 1/(N - 1)$ (the other eigenvalue of $E$ adds $n - 1 \le e \le n$). If $\omega$ is also quasi-free then, by the variance formula of Proposition \claimref{synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise}(i), for every real symmetric one-body matrix $f$ and $N_{f} = \sum_{ij}f_{ij}a_{i}^{*}a_{j}$,
\[
\mathrm{Var}_{\omega}(N_{f}) = \alpha(1 - \alpha)\Tr f^{2} + e(1 - 2\alpha)\,\mathbf{1}^{T}f^{2}\mathbf{1} - e^{2}\bigl(\mathbf{1}^{T}f\mathbf{1}\bigr)^{2}, \qquad \alpha = n - e,
\]
$\mathbf{1}$ the vector with every entry $1$; for diagonal $f$ this is $(n(1 - n) + e^{2})\sum_{i}f_{i}^{2} - e^{2}(\sum_{i}f_{i})^{2}$, the form of (ii) with $v - c = n(1 - n) + e^{2}$ and $c = -e^{2}$, $|c| \le (N - 1)^{-2}$. The stored ladder states $\omega_{k}$ of $N$ blocks (Theorem \claimref{synthesis.ladder-states-are-locally-product-with-non-gaussian-fluctuations}(ii)), which are exchangeable and not quasi-free, have for the upper occupations $v = \tfrac kN(1 - \tfrac kN)$ and $c = \tfrac{k(k - 1)}{N(N - 1)} - \tfrac{k^{2}}{N^{2}}$, so $v + (N - 1)c = 0$ (the total is sharp) and $v - c = \tfrac{k(N - k)}{N(N - 1)}$.
\item[(v)] \emph{(A conformal structure leaves one exponent.)} The similarities $x \mapsto \lambda R(x) + b$ of a Euclidean slice ($\lambda > 0$, $R$ a product of reflections $x \mapsto -uxu^{-1}$ in $\Cl(3,0)$) are transitive on ordered pairs of distinct points. Hence a kernel $K(x, y)$ on distinct points that is invariant under them is constant, and a kernel of weight $\Delta$, $K(gx, gy) = \lambda_{g}^{-2\Delta}K(x, y)$, is a constant multiple of $Q(x - y)^{-\Delta}$.
\end{enumerate}
Consequently a deposit that carries no geometric information, in the sense that its state is invariant under a group of relabellings of its units transitive on pairs, supplies two second moments: on a slice into which its units are placed as cells tiling the slice, or as point cells on a periodic lattice, it is white noise plus a term at $k = 0$, and in general the dependence on the wavenumber is that of the placement (the cells' form factor and, through $c$, the placement's structure factor), the same for every such state. \emph{Reading (argued).} A deposit set before the metric can therefore carry a spectrum other than the white one only if its invariance group separates pairs of units, that is, if the state already carries the separations of its units, or if the map of its units into the slice carries the shape; a conformal structure alone leaves one exponent, the weight. This result concerns the second moments of the deposit's matter observables; how a white energy spectrum converts into a spectrum of the curvature perturbation depends on the descent slice and is not decided here.

## technical
The stored finite-range bound closes passive deposits with correlations of finite range and leaves the pre-metric sector as the place where long-range correlations could be set. The question taken up here is what a pre-metric state must contain for that. If the deposit is laid down before any metric and with no geometric information, nothing distinguishes one pair of its units from another, and its state is invariant under relabelling. The covariance matrix of the units' observables then commutes with the permutation representation, which is the sum of the trivial representation and one irreducible representation, so it has two eigenvalues: one for the constant mode and one for everything else. Placing the units in a slice as cells that tile it, or as point cells on a lattice, gives white noise on every mode of nonzero wave vector, with the constant mode carrying the second number, and above the inverse cell size the squared transform of the cells. That is the whole of what the state contributes. The placement can contribute more: for point cells that are not on a lattice the second number multiplies the structure factor of the set of points, so a clustered or otherwise correlated placement shows its own shape in the spectrum; two cells a quarter of a circle apart already show it. The dependence on the wavenumber is in every case a property of the placement, the same for all such states. The criterion is exact: the two-number form holds for every invariant state precisely when the group is transitive on unordered pairs, and otherwise each further orbit on pairs is a further free second moment, as the nearest-neighbour covariance on a ring shows. For fermion modes exchangeability forces the pairing to vanish and bounds the coherence between two modes by $1/(N - 1)$; the quasi-free case is explicit, and the stored ladder states of the tower are the worked non-Gaussian example, with a sharp total and white fluctuations beneath it. Two groups of the series are of the transitive kind. The similarities of a slice, which the frozen point's stabiliser induces on its late-time boundary, are transitive on pairs of points, so an invariant kernel of weight zero is constant and a kernel of weight $\Delta$ is the single power $Q(x - y)^{-\Delta}$, index $2\Delta$: the stored reading in which the index is twice a weight and never negative on the unitary series (Proposition \claimref{synthesis.frozen-phase-spectrum-not-red}). The Lorentz group on the sphere of null directions is triply transitive (standard), so a state of light rays invariant under it is of the same kind. The Euclidean group of a slice is not transitive on pairs: its orbits are the separations, and an invariant covariance is a free function of the separation, which is the setting of the stored finite-range bound. So the pre-metric escape is not closed by this result, but it is narrowed (argued) to deposits that carry the separations of their units before the metric does, or whose units are laid into the slice by a map that itself carries the shape. Whiteness here is a statement about the matter observables; what it means for the curvature perturbation depends on the descent slice, which the series leaves free.

## lay
Suppose the event that began the universe scattered its energy into a great many cells before there was any notion of distance, so that no pair of cells was special. Then the pattern of fluctuations has only two numbers in it: how much one cell fluctuates, and how much any two cells fluctuate together. If the cells fill space, the result is featureless noise in the matter, the same at every scale, plus a uniform offset. The measured ripples of the early universe are not featureless: they have nearly equal strength on every scale, which is a very particular long-range pattern. So a deposit made before distance existed cannot hold that pattern unless it already knew which cells would be near which, or the way the cells were laid out in space supplied it; and featureless noise in the matter does not give the measured pattern under any of the ways of reading it off that have been examined (argued). Knowing only angles and shapes (a conformal structure) is not enough: it allows one exponent and nothing more.

## one-liner
A state invariant under a group of relabellings transitive on pairs of its units (exchangeable states among them) has covariance $(v - c)\,1 + c\,U$: on a slice tiled by its cells, or for point cells on a lattice, it is white noise plus a term at $k = 0$, all other dependence on the wavenumber being the placement's (for point cells off a lattice, the placement's structure factor through $c$); the criterion is exact, an exchangeable fermion state has no pairing and coherence at most $1/(N - 1)$, and similarity-invariant kernels are single powers, so a pre-metric deposit carries a spectrum only if it, or its placement, carries the separations of its units (argued).
