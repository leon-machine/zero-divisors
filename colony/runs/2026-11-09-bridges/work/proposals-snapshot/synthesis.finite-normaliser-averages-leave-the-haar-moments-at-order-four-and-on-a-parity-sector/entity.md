---
id: synthesis.finite-normaliser-averages-leave-the-haar-moments-at-order-four-and-on-a-parity-sector
kind: claim
version: 1
title: 'Stabiliser-family averages leave the Haar moments at order four, and on parity sectors'
status: proved
region: synthesis
subject: entropy
tags: [entanglement, grading-and-parity, counting-rules]
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
  - synthesis.signed-directions-and-the-integer-clifford-algebra@2
  - synthesis.imported-haar-average-purity@2
  - synthesis.imported-haar-moments-of-random-pure-state@2
  - singularity.imported-page-average-entropy-subsystem@1
  - synthesis.eviction-keeps-one-replica-saddle@3
  - synthesis.eviction-keeps-one-of-catalan-many-replica-saddles@3
  - synthesis.eviction-deficit-against-page-deficit@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_sixty_two_mode_states_give_four_fifths_seven_tenths_and_thirteen_twentieths
- kind: check
  ref: check.py::check_rank_count_and_moments_agree_with_haar_at_two_and_three_and_never_at_four
- kind: check
  ref: check.py::check_parity_sector_moments_are_the_sector_values_not_the_imported_ones
- kind: check
  ref: check.py::check_bivector_quarter_turns_alone_fail_first_at_eight_directions
- kind: check
  ref: check.py::check_mean_entropy_of_the_finite_average_is_not_the_page_value
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.signed-directions-and-the-integer-clifford-algebra
  - synthesis.eviction-keeps-one-of-catalan-many-replica-saddles
extraction:
  open_problem: op.island-dictionary
  note: >-
    Test of the suggestion that averages over the finite group of quarter turns of the signed directions could
    replace the three imported random-state results of the entropy subject (mean purity, all Renyi moments, mean
    entropy). Outcome, mixed: the second and third moments are reproduced (proved for every split), so the mean
    purity used by the Renyi-2 comparison can be derived from the stored group; the fourth and higher moments and
    the mean entropy are not, so the all-moment import and Page's average cannot be replaced. Clause (ii) is the
    blade-state case of the quarter-turn design statement proposed in the same run
    (synthesis.quarter-turn-rotors-of-the-even-subalgebra-form-a-state-design-of-order-three, intended citation once
    it is stored); that statement, not clause (ii), is what derives the Haar purity, at powers of two. The three
    eviction results and Page's Fact are comparison targets, not premises of a proof step. The stored descent is the
    parity average onto the even algebra, which is the reading under which the sector values of (iv) are the
    relevant ones (a choice of reading, put to the maintainer). Further, and with the finite
    average the Catalan count of the all-index comparison would read 2, 5, 16, 67, 374 at indices 2 to 6, the
    subspace counts of a binary space (proved for every index after review, by counting tuples through the subspace they span). On a
    parity sector the design property survives and the value changes: mean purity (dA + dB)/(dA dB + 2). The
    quarter turns of bivectors alone suffice at four and six directions and not from eight. Kill conditions
    registered before computing: the fourth moment agrees (did not fire); the sector value equals the imported
    one (did not fire); bivector turns suffice for every number of directions (did not fire). Prior art, cited
    from memory and not checked: the normaliser of an extraspecial 2-group is a unitary 3-design and not a
    4-design (Webb 2016; Zhu 2017; Kueng and Gross 2015), the count of stabiliser states by entanglement
    (Fattal, Cubitt, Yamamoto, Bravyi and Chuang 2004; Dahlsten and Plenio 2006), braiding quarter turns as the
    non-universal part of the fermionic normaliser (Bravyi and Kitaev 2002). Nothing here is imported from them:
    clauses (i), (ii), (iv) are proved by counting, the rest are exact evaluations. Transport-absent: finite
    group and counting arithmetic in the Clifford algebra of the signed directions; the results it is compared
    with are the series' eviction comparisons.
---

## formal
Let $e_{1}, \dots, e_{2m}$ be the signed directions of $\Cl(2m, 0)$, $Q(e_{r}) = 1$, with strings $S \subseteq \{1, \dots, 2m\}$, blades $e_{S}$, and the forms $b(S,T) = |S||T| + |S \cap T|$, $q(S) = \binom{|S|}{2} \pmod 2$ of Theorem \claimref{synthesis.signed-directions-and-the-integer-clifford-algebra}(ii) (commutation and square signs); adjoin a central unit $\omega$, $\omega^{2} = -1$ (the product of all generators of $\Cl(2m, 1)$ or $\Cl(2m + 1, 0)$, whichever has square $-1$), so that $h_{S} = e_{S}$ or $\omega e_{S}$ has square $+1$, and write $\mathrm{tr} = 2^{m}\langle\cdot\rangle_{0}$. A \emph{family} is a subspace $L \subseteq \mathbb{F}_{2}^{2m}$ of dimension $m$ on which $b$ vanishes, and its \emph{states} are the $2^{m}$ idempotents $\rho = 2^{-m}\prod_{r}(1 + s_{r}h_{S_{r}})$, $S_{r}$ a basis of $L$, $s_{r} = \pm 1$. For $1 \le a < m$, $b' = m - a$, let $A$ be the subalgebra generated by $e_{1}, \dots, e_{2a}$ and $\omega$, $d_{A} = 2^{a}$, $d_{B} = 2^{b'}$, $D = d_{A}d_{B}$; the trace-preserving conditional expectation onto $A$ is the projection onto the blades of $A$, $\rho_{A} = d_{B}$ times the projection of $\rho$, and $\mathrm{tr}\rho_{A}^{n} = (|L_{A}|/d_{A})^{n-1}$ with $L_{A}$ the strings of $L$ inside $\{1, \dots, 2a\}$. A quarter turn $(1 + u)/\sqrt2$, $u = e_{w}$ or $\omega e_{w}$ of square $-1$, permutes the states and acts on strings by $x \mapsto x + b(x, w)w$. The \emph{finite average} $\langle\cdot\rangle_{\mathrm{fin}}$ is the mean over all states of all families (no clause uses that these states form one orbit of the quarter turns; they do for $m \le 3$, computed, and in general that needs three classical inputs not derived here: Witt's extension theorem, generation of $Sp(2m, 2)$ by transvections, and the sign flips by conjugation with blades); the \emph{sector average} is the mean over the states with $v = \{1, \dots, 2m\} \in L$ and a fixed sign of $h_{v}$, the parity sector, of dimension $D/2$ (one orbit of the quarter turns about even strings for $m \le 4$, computed; not used). Haar values are those of Facts \claimref{synthesis.imported-haar-average-purity}, \claimref{synthesis.imported-haar-moments-of-random-pure-state} and \claimref{singularity.imported-page-average-entropy-subsystem}.
\begin{enumerate}
\item[(i)] \emph{(Count by rank; proved.)} The number of families with $|L_{A}| = 2^{a - e}$ (so $\rho_{A}$ flat of rank $2^{e}$) is $N(a, a - e)\,N(b', b' - e)\,|Sp(2e, 2)|$, with $N(c, k) = \binom{c}{k}_{2}\prod_{r=0}^{k-1}(2^{c-r} + 1)$ the number of $k$-dimensional subspaces of $\mathbb{F}_{2}^{2c}$ on which $b$ vanishes and $|Sp(2e, 2)| = 2^{e^{2}}\prod_{r=1}^{e}(4^{r} - 1)$; the total is $\prod_{r=1}^{m}(2^{r} + 1)$. At $a = b' = 1$: $9$ and $6$ families, $36$ and $24$ states.
\item[(ii)] \emph{(Moments two and three agree; proved for every $a$, $b'$ by counting; a special case.)} $\langle\mathrm{tr}\rho_{A}^{2}\rangle_{\mathrm{fin}} = (d_{A} + d_{B})/(D + 1)$ and $\langle\mathrm{tr}\rho_{A}^{3}\rangle_{\mathrm{fin}} = (d_{A}^{2} + d_{B}^{2} + 3D + 1)/((D + 1)(D + 2))$, the Haar values. This is the case of a blade state, with $W = V_{A}$, of the quarter-turn design statement (intended citation: synthesis.quarter-turn-rotors-of-the-even-subalgebra-form-a-state-design-of-order-three, a proposal of the same run, not yet citable), which gives the same moments for every state; it is kept here with its counting proof as a cross-check and is not the general design result.
\item[(iii)] \emph{(Moment four does not: values computed, the crossing limit proved.)} $\langle\mathrm{tr}\rho_{A}^{4}\rangle_{\mathrm{fin}}$ exceeds the Haar value for every $a + b' \le 8$: $\tfrac{13}{20}$ against $\tfrac{22}{35}$ at $a = b' = 1$, $\tfrac{3}{17}$ against $\tfrac{52}{323}$ at $a = b' = 2$. For every $a$, $b'$, $n$ (proved): $\langle|L_{A}|^{n-1}\rangle_{\mathrm{fin}} = \sum_{r \ge 0}N(a, r)\,\prod_{j=m-r+1}^{m}(2^{j} + 1)^{-1}\,\prod_{j=0}^{r-1}(2^{n-1} - 2^{j})$, the three factors being the number of $r$-dimensional subspaces of $V_{A}$ on which $b$ vanishes, the fraction of families containing one of them, and the number of $(n-1)$-tuples spanning it. At the crossing $a = b' = c$, $d = 2^{c}$, the $r$-th term of $d^{n-1}\langle\mathrm{tr}\rho_{A}^{n}\rangle_{\mathrm{fin}}$ tends to the Gaussian binomial $\binom{n-1}{r}_{2}$ as $c \to \infty$, so the coefficient tends to $G_{n-1} = \sum_{r}\binom{n-1}{r}_{2}$, the number of subspaces of $\mathbb{F}_{2}^{n-1}$, for every $n \ge 2$ (proved): $2, 5, 16, 67, 374$ for $n = 2, \dots, 6$, where the Haar coefficient tends to the Catalan numbers $2, 5, 14, 42, 132$ (Theorem \claimref{synthesis.eviction-keeps-one-of-catalan-many-replica-saddles}(iii)). Computed: the coefficient lies within $2^{-16}$ at $c = 16$ and $2^{-32}$ at $c = 24$ below these values. Equivalently the limit is $\phi\sum_{k \ge 0}2^{(n-1)k - k^{2}}\phi_{k}^{-2}$, $\phi_{k} = \prod_{j=1}^{k}(1 - 2^{-j})$, $\phi = \phi_{\infty}$ (the count (i) summed by rank).
\item[(iv)] \emph{(Parity sector; proved.)} For a unit vector drawn from the unitarily invariant measure of the parity sector, $\langle\mathrm{tr}\rho_{A}^{n}\rangle = 2\sum_{\sigma \in S_{n}}(d_{A}/2)^{\#(\sigma^{-1}\eta)}(d_{B}/2)^{\#(\sigma)}/\prod_{l=0}^{n-1}(D/2 + l)$ (the same Schur average as the Fact, on a space that is $(\text{even} \otimes \text{even}) \oplus (\text{odd} \otimes \text{odd})$ and not a tensor product), so the mean purity is
\[
\frac{d_{A} + d_{B}}{D + 2} \quad\text{in place of}\quad \frac{d_{A} + d_{B}}{D + 1} ,
\]
and the sector average of the purity equals it for every $a$, $b'$; so does the sector average of $\mathrm{tr}\rho_{A}^{3}$, with value $(d_{A}^{2} + d_{B}^{2} + 3D + 4)/((D + 2)(D + 4))$ (proved for every $m$ by the same double count; also a corollary of the design statement named in (ii), with $\omega$ as its unit). Computed for $m \le 4$: the sector average of $\mathrm{tr}\rho_{A}^{4}$ exceeds the sector's Haar value. At $m = 2$ the six states reached from $\tfrac14(1 + h_{12})(1 + h_{34})$ by the six bivector quarter turns have purities $1, 1, \tfrac12, \tfrac12, \tfrac12, \tfrac12$, mean $\tfrac23$, against $\tfrac45$ for two unrestricted modes.
\item[(v)] \emph{(Which quarter turns; proved, with the values at $m = 4$ computed.)} The quarter turns about bivectors permute the directions, and the orbit of the family spanned by $\{1,2\}, \{3,4\}, \dots$ is the $(2m - 1)!!$ perfect matchings, equal to the $\prod_{r=1}^{m-1}(2^{r} + 1)$ families containing $v$ exactly for $m \le 3$ ($3$, $15$) and fewer for every $m \ge 4$ ($105$ of $135$ at $m = 4$, where the classes of even strings modulo $v$ fall into orbits of $28$ and $35$ and the mean purity at $a = b' = 2$ is $\tfrac{17}{35}$, against $\tfrac49$ for the sector and $\tfrac{8}{17}$ for the Fact; one quartic quarter turn added restores $135$ and $\tfrac49$). The orbits of the bivector turns on the classes of even strings modulo $v$ are the $\lfloor m/2\rfloor$ size classes $\{2k, 2m - 2k\}$: $3$; $15$; $28 + 35$; $45 + 210$ at $m = 2, 3, 4, 5$; so bivector turns fail for odd $m \ge 5$ as well, although every class then has a real quarter turn of unit norm. Without the adjoined unit, a quarter turn of unit norm about $e_{w}$ exists in $\Cl(2m, 0)$ exactly when $q(w) = 1$; for $m$ odd every class of even strings modulo $v$ has such a member ($e_{v}^{2} = -1$, the even subalgebra has its own unit), and for $m$ even $q$ descends to the classes and is preserved, so for even $m \ge 4$ the classes with $q = 0$ and $q = 1$ are never exchanged ($28$ and $35$ at $m = 4$; $528$ and $495$ at $m = 6$, counted; that these are single orbits at $m = 6$ is not checked).
\item[(vi)] \emph{(Mean entropy; computed.)} The finite average of the entropy is $\ln 2$ times the mean of $e$: $\tfrac25\ln 2 < \tfrac{7}{25}$ at $a = b' = 1$ against Page's $\tfrac13$; at the crossing it lies below $\ln d$ by between $0.84\ln 2$ and $0.86\ln 2$ for $c = 8, 16, 24$, more than $0.56$, where Page's deficit is below $\tfrac12$.
\end{enumerate}
So the average over these states reproduces the imported mean purity and third moment and nothing further: the number of Fact \claimref{synthesis.imported-haar-average-purity}, as used in Theorem \claimref{synthesis.eviction-keeps-one-replica-saddle}(iii), (iv), is reproduced by (ii), but deriving the Haar value needs the state-independent average of the design statement named in (ii) together with invariance of the measure, and holds at powers of two only, while the stored clause is stated for all $m$, $n$; Fact \claimref{synthesis.imported-haar-moments-of-random-pure-state}, as used at every index in Theorem \claimref{synthesis.eviction-keeps-one-of-catalan-many-replica-saddles}(iii), (iv), and Page's average, as used in Theorem \claimref{synthesis.eviction-deficit-against-page-deficit}, could not: with the finite average the gap $\ln C_{n}/(n - 1)$ would read $\ln G_{n-1}/(n - 1)$, $\tfrac13\ln 16$ at $n = 4$, and the half nat at the crossing about $0.59$. On a parity sector the Renyi-2 comparison at the crossing $d_{A} = d_{B} = d$ reads $2d/(d^{2} + 2)$, below the capacity value in $S_{2}$ by $\ln 2 - \ln(1 + 2d^{-2})$ in place of $\ln 2 - \ln(1 + d^{-2})$; the leading terms and the Catalan limit are unchanged (argued from (iv): the planar permutations contribute $C_{n}d^{1-n}$ in both). None of the stored results is contradicted: they state the Haar values for an abstract tensor product and do not use a finite group or a sector.

## technical
The signed directions generate a finite group whose quarter turns shuffle a finite set of special states, those fixed by a largest commuting set of blades. Averaging over that finite set is exact arithmetic: a reduced state always has a flat spectrum of rank a power of two, and the number of states of each rank is a product of counts of isotropic subspaces. The average purity and the average third moment come out equal to the random-state (Haar) values for every split, by a two-line double count. The fourth moment does not, in every split of at most eight modes (computed): one against one mode it is 13/20 where the random-state value is 22/35. At the point where the two parts have equal size the finite average replaces the Catalan numbers 2, 5, 14, 42 of the random-state moments by 2, 5, 16, 67, the numbers of subspaces of a binary space (proved in the limit of large equal parts), and the mean entropy sits about 0.59 below the maximum instead of one half. If only states of one fermion parity are allowed, the group that preserves parity still reproduces the random-state values of that sector, but those are different numbers, because a parity sector is not a product of two parts: the mean purity has D + 2 in the denominator where the unrestricted formula has D + 1. Finally, the quarter turns in planes of two directions reach every allowed family only for four and six directions; from eight on they reach 105 of 135 families and give a different mean.

## lay
Some of the series' comparisons use the entanglement of a quantum state picked completely at random, a result taken from the literature. This entry asks whether the same numbers can be obtained from the series' own finite group of quarter turns, by averaging over a finite list of states instead of over all of them. The answer is yes for the two simplest measures and no beyond: the finite list gives exactly the random value for the average purity and for the next moment, then departs at the fourth moment in every case computed, up to eight modes (13/20 instead of 22/35 in the smallest), and it gives a different average entropy. It also shows that if only states with an even number of particles are allowed, the random value itself changes slightly, and that quarter turns in planes alone are enough only for the two smallest cases. Everything here is for the finite list of states named, with the splits and sizes stated in each clause.

## one-liner
Averages over the states of the quarter-turn group of $2m$ signed directions equal the Haar moments of a subsystem at orders two and three for every split and exceed them at order four for every split of at most eight modes (computed; $\tfrac{13}{20}$ against $\tfrac{22}{35}$), with crossing coefficients tending to the subspace counts $2, 5, 16, 67, 374, \dots$ against the Catalan numbers (proved); on a parity sector the mean purity is $(d_{A} + d_{B})/(d_{A}d_{B} + 2)$; bivector quarter turns alone suffice only for $m \le 3$.
