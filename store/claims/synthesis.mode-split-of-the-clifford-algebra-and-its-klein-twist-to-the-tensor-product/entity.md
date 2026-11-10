---
id: synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product
kind: claim
version: 1
title: 'The mode split of the Clifford algebra and its Klein twist to the tensor product'
status: proved
region: synthesis
subject: entropy
tags: [entanglement, grading-and-parity, dictionaries, car-algebra]
proposed_by:
  kind: ai
  session: 2026-11-09-bridges
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-09-bridges
review: draft
derivations:
- name: main
  uses:
  - tower.commuting-copies@5
  - tower.ladder-pairs-satisfy-car-vectors@4
  - synthesis.blade-square-signs-f2-quadratic-form@3
  - synthesis.joint-clifford-clause-is-a-klein-convention-on-the-composite-space@1
  - singularity.descent-parity-average@5
  - singularity.eviction-window-thermal-product-radiation-entropy@7
  - synthesis.eviction-keeps-one-replica-saddle@4
  - synthesis.eviction-keeps-one-of-catalan-many-replica-saddles@4
  - synthesis.eviction-deficit-against-page-deficit@5
  - singularity.assembled-page-curve-up-typicality@3
  - synthesis.imported-haar-moments-of-random-pure-state@3
  - singularity.imported-page-average-entropy-subsystem@1
  - synthesis.finite-normaliser-averages-leave-the-haar-moments-at-order-four-and-on-a-parity-sector@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_parity_twist_gives_commuting_copies_and_the_projection_is_the_partial_trace
- kind: check
  ref: check.py::check_even_pure_states_have_equal_moments_on_both_sides_and_a_non_even_one_does_not
- kind: check
  ref: check.py::check_eviction_states_are_even_products_with_the_stored_purities
- kind: check
  ref: check.py::check_sector_renyi_moments_keep_the_catalan_limit_and_weight_genus_by_four
- kind: check
  ref: check.py::check_sector_mean_entropy_exceeds_the_imported_value_by_a_rational_amount
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.eviction-keeps-one-replica-saddle
  - tower.commuting-copies
  - singularity.descent-parity-average
extraction:
  open_problem: op.island-dictionary
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'The sector lemma of clause (vi) (the moments of a random state of a parity sector) is cut to a citation of clause (iv) of the finite-averages result, where it is proved, with a premise edge; the genus form, the Catalan limit, the coefficient of d^{-2} and the bounds stay here. Direction of the graph: this result cites the two eviction results (at version 3, which its fate table describes) and they do not cite it. The fate-table row for the deficit theorem is marked "at version 4": version 5 of that theorem carries the sector column itself. Version kept: the entity was accepted in the same pass.'
  note: >-
    The stored eviction comparisons split window from radiation by a tensor product of abstract spaces. This
    result states the split inside the Clifford algebra of the modes (sub-Clifford algebras, reduction by blade
    projection), proves its relation to the tensor product through the stored commuting-copies twist, and
    recomputes the comparisons for even states, which lie in one parity sector. Outcome: every eviction-side
    statement survives unchanged; the random-state columns keep their leading terms and change below them.
    Kill condition registered before computing: an eviction result whose leading term changes on this split
    (did not fire); auxiliary: the projection differs from the twisted partial trace on an even state (did not
    fire), an even pure state with unequal spectra on the two sides (did not fire; it does happen for pure
    states that are not even, clause (iv)), the stored eviction state is not even (did not fire). Cross-references:
    the lemma of clause (vi)
    (the sector form of the moments, with the sector mean purity) is clause (iv) of
    synthesis.finite-normaliser-averages-leave-the-haar-moments-at-order-four-and-on-a-parity-sector and is
    cited from there; the derived second moment is
    synthesis.quarter-turn-rotors-of-the-even-subalgebra-form-a-state-design-of-order-three, whose parity-sector
    corollary gives the index-two line of (vi) at powers of two without the imported Fact. New here: the twist relation (ii) to (iv) with the
    counterexample, the product rule (v), the proof that the Catalan limit is unchanged with the weight 4^g, the
    bounds, and, for the mean entropy, the rational difference Delta from the imported value with its bounds and
    the comparison with the stored deficit bounds (the closed form of the sector mean entropy itself is not new,
    see below). The result derives, in the algebra, the content of the
    imported Fact descent-lift.imported-fermionic-operations-are-even-reduced for mode algebras (the reduced
    state is the restriction to the subsystem's algebra, agrees with the partial trace for even states, products
    with an even factor exist) and sharpens it (the reduction to A is a partial trace for every state; the other
    reduction differs exactly on listed odd blades); whether its dependants drop the import is a maintainer
    decision. The stored theorem singularity.descent-parity-average is stated for one mode; the uses edge is for
    that one-mode case only, and the total-parity average used here is a definition. Prior art, cited
    from memory and not checked: the graded tensor product and the Jordan-Wigner or Klein transformation are
    classical; fermionic partial traces and the parity superselection rule for mode entanglement (Banuls, Cirac
    and Wolf 2007; Friis, Lee and Bruschi 2013; Bravyi and Kitaev 2002 and Araki and Moriya 2003, the sources of
    the imported Fact just named). Prior art checked on the web (first third of the paper read): Bianchi, Hackl,
    Kieburg, Rigol and Vidmar, Volume-law entanglement entropy of typical pure quantum states, arXiv:2112.06959,
    whose general direct-sum formula (equation (45) there) gives (vii) as its two-block case; rederived here
    from Page's Fact. Nothing is imported from these. Background used
    and not derived: the invariant probability measure on a unit sphere is unique and is the law of a
    normalised Gaussian vector; the first moment of p ln p for a Beta law. Transport-absent: algebra of the
    modes and counting; the results it re-reads are the series' eviction comparisons.
---

## formal
Let $\Cl(\ell,\ell)$ have generators $e_{k}$, $f_{k}$ ($1 \le k \le \ell$) with $Q(e_{k}) = 1$, $Q(f_{k}) = -1$, and null pairs $v_{k} = \tfrac12(e_{k} + f_{k})$, $w_{k} = \tfrac12(e_{k} - f_{k})$, the $\ell$ modes of Proposition \claimref{tower.ladder-pairs-satisfy-car-vectors}; put $p_{k} = 1 - 2w_{k}v_{k} = f_{k}e_{k}$ (the parity of mode $k$, $p_{k}^{2} = 1$), $\Gamma_{X} = \prod_{k \in X}p_{k}$ for a set $X$ of modes and $\Gamma = \Gamma_{\{1,\dots,\ell\}}$. Coefficients are real, or lie in $\mathrm{span}\{1, I_{4}\}$ with $I_{4}$ commuting with every generator; $x \mapsto x^{\dagger}$ is the anti-automorphism fixing each $e_{k}$, negating each $f_{k}$ (and $I_{4}$), which exchanges $v_{k}$ and $w_{k}$; $\operatorname{tr} = 2^{\ell}\langle\cdot\rangle_{0}$. A \emph{state} is a sum $\rho = \sum_{r}x_{r}x_{r}^{\dagger}$ with $\operatorname{tr}\rho = 1$; it is \emph{pure} if $\rho^{2} = \rho$ and \emph{even} if $\Gamma\rho = \rho\Gamma$, that is, if it is fixed by $x \mapsto \tfrac12(x + \Gamma x\Gamma)$, the average of Theorem \claimref{singularity.descent-parity-average} with the total parity $\Gamma$ in place of the single-mode $\sigma$; that theorem is stated for one mode and the $\ell$-mode form is a definition here. For a set $A$ of $a$ modes with complement $B$ of $b \ge 1$ modes ($a \ge 1$, $d_{A} = 2^{a}$, $d_{B} = 2^{b}$, $D = d_{A}d_{B}$) let $\Cl(A) \cong \Cl(a,a)$ be the subalgebra generated by the $e_{k}, f_{k}$ with $k \in A$, $E_{A}$ the linear projection onto its blades, $\rho_{A} = d_{B}E_{A}(\rho)$ and $\operatorname{tr}_{A} = d_{A}\langle\cdot\rangle_{0}$ on $\Cl(A)$.
\begin{enumerate}
\item[(i)] \emph{(The split; proved.)} Homogeneous $x \in \Cl(A)$, $y \in \Cl(B)$ satisfy $xy = (-1)^{|x||y|}yx$, and multiplication $\Cl(A) \otimes \Cl(B) \to \Cl(\ell,\ell)$ is a linear bijection that is multiplicative for the graded product only. $E_{A}$ is the one linear map onto $\Cl(A)$ with $\langle E_{A}(x)y\rangle_{0} = \langle xy\rangle_{0}$ for all $y \in \Cl(A)$; it satisfies $E_{A}(yxy') = yE_{A}(x)y'$ for $y, y' \in \Cl(A)$ and $E_{A}(x^{\dagger}) = E_{A}(x)^{\dagger}$, and $\rho_{A}$ is a state of $\Cl(A)$, with purity $\operatorname{tr}_{A}\rho_{A}^{2} = d_{A}d_{B}^{2}\langle E_{A}(\rho)^{2}\rangle_{0}$.
\item[(ii)] \emph{(The Klein twist; proved.)} $\Gamma_{A}^{2} = 1$; $\Gamma_{A}$ anticommutes with the generators of $\Cl(A)$ and commutes with $\Cl(B)$. The twisted generators $y\Gamma_{A}$, $y \in \{e_{k}, f_{k} : k \in B\}$, keep their squares, anticommute with each other and commute with $\Cl(A)$; the algebra $B'$ they generate is isomorphic to $\Cl(b,b)$, and multiplication $\Cl(A) \otimes B' \to \Cl(\ell,\ell)$ is an isomorphism of algebras for the ordinary tensor product (Theorem \claimref{tower.commuting-copies}, with ground algebra $\Cl(B)$ and the planes of $A$). The even part of $B'$ is the even part of $\Cl(B)$, and its odd part is $\Gamma_{A}$ times the odd part of $\Cl(B)$. If $K$ commutes with $\Cl(B)$ and every $yK$ commutes with $\Cl(A)$ and has the square of $y$, then $K = \pm\Gamma_{A}$ (compare Theorem \claimref{synthesis.joint-clifford-clause-is-a-klein-convention-on-the-composite-space}(iv)).
\item[(iii)] \emph{(Reductions; proved.)} For every $x$, the partial trace of the tensor split of (ii) over $B'$ is $d_{B}E_{A}(x)$: the reduction to $A$ is the same for the two splits, for every state. The partial trace over $\Cl(A)$ is $d_{A}E_{B'}(x)$, with $E_{B'}$ the projection onto the blades $e_{T}$ ($|T|$ even) and $\Gamma_{A}e_{T}$ ($|T|$ odd), $e_{T}$ the blades of $\Cl(B)$; so $E_{B'}(x) = E_{B}(x)$ exactly when $x$ has no component on $e_{T}$ or $\Gamma_{A}e_{T}$ with $|T|$ odd, in particular for every even $x$.
\item[(iv)] \emph{(Even states; proved.)} If $\rho$ is even, $\rho_{A}$ and $\rho_{B}$ are even, $\rho_{B}$ is the reduced state of the tensor split as well, and $\rho_{A}$ commutes with $\Gamma_{A}$. If moreover $\rho$ is pure, then $\operatorname{tr}_{A}\rho_{A}^{n} = \operatorname{tr}_{B}\rho_{B}^{n}$ for every $n \ge 1$ (equal nonzero spectra), and $\Gamma\rho = \pm\rho$: the state lies in a parity sector, of dimension $D/2$, which in the tensor split is $(\text{even} \otimes \text{even}) \oplus (\text{odd} \otimes \text{odd})$ or $(\text{even} \otimes \text{odd}) \oplus (\text{odd} \otimes \text{even})$ and not a tensor product. For a pure state that is not even the equality can fail: at $\ell = 2$, $\rho = \tfrac14(1 + e_{1} - f_{1}e_{2} + f_{1}e_{1}e_{2}) = \tfrac12(1 + e_{1})\,\tfrac12(1 + e_{2}p_{1})$ has $\rho_{A} = \tfrac12(1 + e_{1})$, of purity $1$, and $\rho_{B} = \tfrac12$, of purity $\tfrac12$.
\item[(v)] \emph{(Products of even states; proved.)} If $P_{1}, \dots, P_{r}$ are disjoint sets of modes with union all modes and $\rho_{j}$ is an even state of $\Cl(P_{j})$, the $\rho_{j}$ commute, $\rho = \prod_{j}\rho_{j}$ is an even state, pure if every $\rho_{j}$ is, $\rho_{A} = \prod_{j}(\rho_{j})_{A \cap P_{j}}$, and $\operatorname{tr}_{A}\rho_{A}^{n} = \prod_{j}\operatorname{tr}(\rho_{j})_{A \cap P_{j}}^{n}$: for even states the tensor product is the product in the algebra, with no twist. The pair state with amplitudes $c$ on $\ket{00}$ and $s$ on $\ket{11}$ ($c^{2} + s^{2} = 1$, $r = c^{2} - s^{2}$) of modes $k$, $k'$ is
\[
\rho_{kk'} = \tfrac14(1 + p_{k}p_{k'})(1 + rp_{k}) + cs\,(w_{k}w_{k'} + v_{k'}v_{k}) ,
\]
a pure even state with reduction $\tfrac12(1 + rp_{k})$ on mode $k$, of purity $\tfrac12(1 + r^{2}) = c^{4} + s^{4}$. Reading the pairs of Theorem \claimref{singularity.eviction-window-thermal-product-radiation-entropy} as these pair states, its state is a pure even state, its window is the product $\prod_{k \in W}\tfrac12(1 + r_{k}p_{k})$, and the radiation has the same nonzero spectrum.
\item[(vi)] \emph{(Renyi moments of a parity sector; proved, the two upper bounds computed.)} For a unit vector drawn from the unitarily invariant measure of a parity sector, $\langle\operatorname{tr}_{A}\rho_{A}^{n}\rangle = 2\sum_{\sigma \in S_{n}}(d_{A}/2)^{\#(\sigma^{-1}\eta)}(d_{B}/2)^{\#(\sigma)}/\prod_{l=0}^{n-1}(D/2 + l)$, with $\eta$, $\#$ as in Theorem \claimref{synthesis.eviction-keeps-one-of-catalan-many-replica-saddles} and the average that of Fact \claimref{synthesis.imported-haar-moments-of-random-pure-state} on the sector; this formula is clause (iv) of Theorem \claimref{synthesis.finite-normaliser-averages-leave-the-haar-moments-at-order-four-and-on-a-parity-sector}, cited and not reproved here. At $n = 2$ it is $(d_{A} + d_{B})/(D + 2)$, strictly between $\max(1/d_{A}, 1/d_{B})$ and the unrestricted $(d_{A} + d_{B})/(D + 1)$, and below $1/d_{A} + 1/d_{B}$ by $2(d_{A} + d_{B})/(D(D + 2))$. At $d_{A} = d_{B} = d$, with $N_{n,g}$ the number of $\sigma$ with $\#(\sigma) + \#(\sigma^{-1}\eta) = n + 1 - 2g$,
\[
d^{\,n-1}\langle\operatorname{tr}\rho^{n}\rangle_{\mathrm{sector}} = \frac{\sum_{g}N_{n,g}(4/d^{2})^{g}}{\prod_{l<n}(1 + 2l/d^{2})}
\qquad\text{against}\qquad
\frac{\sum_{g}N_{n,g}\,d^{-2g}}{\prod_{l<n}(1 + l/d^{2})}
\]
for the unrestricted average: both tend to $N_{n,0} = C_{n}$, and the coefficient of $d^{-2}$ is $-(C_{n}n(n-1) - 4N_{n,1})$ against $-(\tfrac12 C_{n}n(n-1) - N_{n,1})$. The sector value exceeds $d^{1-n}$ for all $n$, $d$ (proved); it is below the unrestricted one, itself below $C_{n}d^{1-n}$, for $2 \le n \le 6$ and $d = 2, \dots, 32$ (computed; $N_{n,1} = 0, 1, 10, 70, 420$).
\item[(vii)] \emph{(Mean entropy of a parity sector; proved from Fact \claimref{singularity.imported-page-average-entropy-subsystem} and the background named in the note.)} For $m = d_{A} \le n = d_{B}$ the same average of the entropy of $\rho_{A}$ is
\[
\langle S_{A}\rangle_{\mathrm{sector}} = \sum_{k = n/2 + 1}^{mn/2}\frac1k - \frac{m - 2}{2n} ,
\]
which exceeds the Fact's $\sum_{k=n+1}^{mn}\tfrac1k - \tfrac{m-1}{2n}$ by the rational number $\Delta(m,n) = \tfrac{1}{2n} - \sum_{k=mn/2+1}^{mn}\tfrac1k + \sum_{k=n/2+1}^{n}\tfrac1k$, with $\tfrac{1}{2mn} < \Delta(m,n) < \tfrac{1}{2(mn+1)} + \tfrac{1}{2n(n+1)}$ (sector value $\tfrac12$ against the Fact's $\tfrac13$ at $m = n = 2$, $\Delta = \tfrac16$; sector value $\tfrac{271}{280}$ at $m = n = 4$, $\Delta = \tfrac{6553}{144144}$). The deficit $\delta_{\mathrm{sec}} = \ln m - \langle S_{A}\rangle_{\mathrm{sector}}$ satisfies
\[
\frac{m-2}{2n} + \frac{2(m-1)}{2mn + m + 1} \;<\; \delta_{\mathrm{sec}}(m,n) \;<\; \frac{m}{2n} - \frac{1}{mn} ,
\]
so it is positive, below $\tfrac12$, in $(\tfrac25, \tfrac12)$ at the crossing $m = n \ge 4$, above $(m-1)/(2n)$ for $m \ge 4$ and below it for $m = 2$.
\end{enumerate}
Fate of the stored comparisons on this split, for the even states they use. Theorem \claimref{singularity.eviction-window-thermal-product-radiation-entropy}: all four clauses unchanged, its tensor product read as the product of (v) and $S_{R} = S_{L}$ by (iv). Theorem \claimref{synthesis.eviction-keeps-one-replica-saddle} at version 3: (i), (ii), (v) unchanged; in (iii), (iv) the random-state value on a sector is $(m + n)/(mn + 2)$, at the crossing $2m/(m^{2} + 2)$, below the eviction value in $S_{2}$ by $\ln 2 - \ln(1 + 2m^{-2}) \in (\ln 2 - 2m^{-2}, \ln 2)$: leading term $\ln 2$ unchanged, the term of order $m^{-2}$ doubled. Theorem \claimref{synthesis.eviction-keeps-one-of-catalan-many-replica-saddles} at version 3: (i), (ii) unchanged; (iii) with the sector formula of (vi), limit $C_{n}$ and gap $\ln C_{n}/(n-1)$ of (iv) unchanged. Theorem \claimref{synthesis.eviction-deficit-against-page-deficit} at version 4 (version 5 carries the sector column itself): (ii), (iii) unchanged; (i) with the bounds of (vii), half a nat at the crossing unchanged, the lower bound $(m-1)/(2n)$ lost at $m = 2$ only. Fact \claimref{singularity.assembled-page-curve-up-typicality}: unchanged at the order it states. None fails; each stored statement about an abstract tensor product remains true as stated.

## technical
The eviction comparisons of the series divide a set of fermionic modes into window and radiation and compare the reduced state with that of a random pure state. As stored they use a tensor product of two abstract spaces. In the Clifford algebra of the modes the natural split is different: each side is the sub-Clifford algebra generated by its own modes, and reduction is the projection onto its blades. The two sub-Clifford algebras do not commute (their odd elements anticommute), so together they are a graded tensor product. The stored commuting-copies twist repairs this: multiplying the generators of one side by the parity blade of the other gives a commuting copy, and the pair (untwisted side, twisted side) is an ordinary tensor product. The projection onto the untwisted side is exactly the partial trace of that tensor product, for every state; the projection onto the other side differs from the partial trace only on odd blades. So for even states, the states fixed by the total-parity average, both reductions coincide with the tensor-product ones, the two sides of a pure state have the same spectrum, and products of even states are plain products in the algebra. For a pure state that is not even the two sides can have different purities, so evenness is the exact hypothesis under which the stored arguments transfer.

What does change is the ensemble behind the word "typical". A pure even state lies in one parity sector, half the dimension, and a sector is a sum of two tensor products, not one. The random-state columns of the comparisons, recomputed on a sector, keep every leading term: the Renyi-2 gap $\ln 2$, the gap $\ln C_{n}/(n-1)$ at index $n$, half a nat of entropy at the crossing. Below leading order they move: the mean purity is $(m + n)/(mn + 2)$, a permutation of genus $g$ in the moment sum is weighted by $4^{g}$ relative to the unrestricted average, and the mean entropy is larger than Page's by a rational amount between $1/(2mn)$ and $1/(2mn) + 1/(2n^{2})$, about $3/(4m^{2})$ at the crossing. The eviction side does not move at all, since its state is an even product of pair states. The mean entropy uses Page's Fact on the two blocks of a sector and is the two-block case of a known formula for random states on a direct sum of tensor products; the moment formula uses the imported all-moment Fact on the sector. Both are conditional on those imports.

## lay
When physicists ask how much two parts of a system share, they usually treat the two parts as independent building blocks glued together in the simplest way. For particles like electrons that picture is slightly off, because operations on one part can pick up a sign from the other. This result does the bookkeeping directly in the algebra the series uses for such particles and shows precisely how it relates to the usual picture: a simple relabelling by a sign factor turns one into the other. For the states the series actually uses, in which the total number of particles is even or odd but never a mixture of both, the two pictures give the same answers for each part, and all of the series' statements about its own radiation mechanism stand as they were. What shifts slightly is the benchmark of a "random state": with the even-or-odd restriction a random state is a little more mixed than without it. The main terms of every comparison stay the same, and only small corrections change, by amounts given exactly, using two textbook averages the collection holds as imports. For states that mix even and odd the two pictures can disagree, and an example is given.

## one-liner
For modes of $\Cl(\ell,\ell)$ split into sub-Clifford algebras with reduction by blade projection, the twist by a parity blade gives the ordinary tensor product, the two splits reduce every even state alike (not every state), eviction's statements are unchanged, and the random-state columns on a parity sector keep their leading terms: mean purity $(m + n)/(mn + 2)$, limit $C_{n}$, mean entropy $\sum_{k=n/2+1}^{mn/2}1/k - (m-2)/(2n)$ (moments from the imported all-moment Fact applied to a sector, entropy from Page's imported average on two blocks).
