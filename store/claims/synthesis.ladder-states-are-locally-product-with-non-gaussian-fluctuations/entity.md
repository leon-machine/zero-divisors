---
id: synthesis.ladder-states-are-locally-product-with-non-gaussian-fluctuations
kind: claim
version: 1
title: 'Ladder states are locally the product state but fluctuate as boson number states'
status: proved
region: synthesis
subject: quantum-fields
tags: [bosonisation, car-algebra, ladder-pairs, limits]
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
  - synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_ladder_moments_are_boson_number_moments
- kind: check
  ref: check.py::check_ladder_marginals_tend_to_the_polarised_product_state
- kind: check
  ref: check.py::check_limit_moments_are_not_quasi_free
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum
extraction:
  open_problem: bos.qclt-states
  note: >-
    Attack on the run target bos.qclt-states (convergence of the fluctuation states, not only of the commutator,
    to a quasi-free boson state). This is the bound on that target, not its positive form: the hypothesis of
    product states cannot be weakened to convergence of the local (finite-block) state. New to the store: on N blocks the
    Holstein-Primakoff ladder vectors psi_k = (K*)^k P_pol give states omega_k whose every finite marginal tends to
    the polarised product state as N grows (explicit bound km/(N - k + 1) on the weight off the polarised
    projector of m blocks), with pair correlations k(N - k)/(N(N - 1)) for every pair alike (the state is
    permutation symmetric),
    while the fluctuation of the hopping element has the exact moments
    omega_k(B*^m B^m) = (k)_m (N - k + 1)(N - k + 2)...(N - k + m)/N^m, which tend to the factorial moments of the
    k-boson number state; for k >= 1 this is not quasi-free (k(k - 1) against 2k^2 at m = 2). The vectors psi_k are
    the Dicke states of the collective hopping, and their limit is the Holstein-Primakoff (Fock number state)
    limit; the ladder coefficient K psi_k = k(N - k + 1) psi_(k-1) is the quasi-spin ladder of
    field-theory.how-close-tower-comes-ccr (with its Inonu-Wigner contraction) read after particle-hole
    conjugation of the lower modes, as in fluctuation-forms (ii); this entity holds the coefficient for the
    fluctuation moments, and synthesis.central-limit-of-tower-fluctuation-states-with-the-kernel-unit
    (iii) treats the case k = 0. What is new to the store is the moment formula of the ladder states, their
    marginal bound and pair correlations, and the comparison with quasi-free states. Stored and cited,
    not refiled: the hopping ladder and [B, B*] = 1 - 2k/N, and the fluctuation map F_N with its commutator law
    (synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum (ii), (vii)). The
    statement that fluctuations of product states tend to quasi-free states is the quantum central limit
    theorem, prior art cited in that entity (Cushen and Hudson 1971; Goderis, Verbeure and Vets 1989), not used
    here; its hypotheses (product states, or a fixed state with summable clustering) are what the counter-model
    shows cannot be replaced by local convergence of a sequence of states. Prior art, orientation only, cited
    from memory: Dicke states and their Holstein-Primakoff (Fock) limit are standard in many-body physics; the
    exchangeable-state and de Finetti setting of quantum fluctuations is in the same literature. No imported
    Fact is a premise and no imaginary unit is used (the states and the hopping mode are real). Ledger:
    transport-absent (finite CAR algebra of tower planes).
---

## formal
Use the notation of Theorem \claimref{synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum}(ii): $N$ blocks of two tower planes, plane $j$ with $Q(e_{j}) = 1$, $Q(f_{j}) = -1$, $v_{j} = \tfrac12(e_{j} + f_{j}) = a_{j}^{*}$, $w_{j} = \tfrac12(e_{j} - f_{j}) = a_{j}$ (the anticommutation relations of Theorem \claimref{tower.ladder-pairs-satisfy-car-vectors}), $n_{j} = v_{j}w_{j}$; block $i$ has a lower mode $l_{i}$ and an upper mode $u_{i}$, hopping element $b_{i} = v_{l_{i}}w_{u_{i}}$, $K = \sum_{i}b_{i}$, $B = N^{-1/2}K$, and polarised element $P = \prod_{i}n_{l_{i}}(1 - n_{u_{i}})$. Vectors are elements $x$ of the algebra in its left regular representation, with $\langle x, y\rangle = \langle x^{*}y\rangle_{0}$ (scalar part); the basis blades are orthonormal for it. For $k = 0, \dots, N$ let $\psi_{k} = (K^{*})^{k}P$ and $\omega_{k}(X) = \langle\psi_{k}, X\psi_{k}\rangle/\langle\psi_{k}, \psi_{k}\rangle$; $\omega_{0}$ is the polarised product state, and $\omega_{k}(b_{i}) = 0$, so the fluctuation $F_{N}(b)$ of clause (vii) of the cited theorem, centred at $\omega_{k}$, is $B$. For integers write $(k)_{m} = k(k - 1)\cdots(k - m + 1)$ and $(x)^{(m)} = x(x + 1)\cdots(x + m - 1)$.
\begin{enumerate}
\item[(i)] \emph{(Exact moments.)} $KP = 0$, $K\psi_{k} = k(N - k + 1)\psi_{k-1}$ and $\langle\psi_{k}, \psi_{k}\rangle = k(N - k + 1)\langle\psi_{k-1}, \psi_{k-1}\rangle$, so $\psi_{k} \ne 0$ for $k \le N$. For all $m \ge 0$,
\[
\omega_{k}\bigl((B^{*})^{m}B^{m}\bigr) = \frac{(k)_{m}\,(N - k + 1)^{(m)}}{N^{m}},
\]
which is $0$ for $m > k$, and $\omega_{k}((B^{*})^{a}B^{c}) = 0$ for $a \ne c$.
\item[(ii)] \emph{(Local convergence to the polarised product state.)} For $m \le N$ and $P_{m} = \prod_{i<m}n_{l_{i}}(1 - n_{u_{i}})$, $\omega_{k}(P_{m}) = \binom{N - m}{k}\big/\binom{N}{k} \ge 1 - \varepsilon_{m}$ with $\varepsilon_{m} = km/(N - k + 1)$; $P_{m}$ is a minimal projection of the algebra of the first $m$ blocks, $P_{m}XP_{m} = \omega_{0}(X)P_{m}$ there, and for every $X$ in that algebra $|\omega_{k}(X) - \omega_{0}(X)| \le (2\sqrt{\varepsilon_{m}} + \varepsilon_{m})\|X\|$. So at fixed $k$ every finite marginal of $\omega_{k}$ tends in norm to that of the polarised product state as $N \to \infty$. The one-block occupation is $\omega_{k}(n_{u_{i}}) = k/N$, and for $i \ne j$, $\omega_{k}(b_{i}^{*}b_{j}) = k(N - k)/(N(N - 1))$ and $\omega_{k}(n_{u_{i}}n_{u_{j}}) = k(k - 1)/(N(N - 1))$: every pair of blocks is correlated at order $1/N$, every pair alike (the state is permutation symmetric), and $\sum_{j \ne i}\omega_{k}(b_{i}^{*}b_{j}) = k(N - k)/N \to k$.
\item[(iii)] \emph{(The fluctuation state is a number state.)} As $N \to \infty$ at fixed $k$, $\omega_{k}((B^{*})^{a}B^{c}) \to \delta_{ac}(k)_{a}$, the moments of the $k$-boson number state of a canonical mode (the canonical relation $[B, B^{*}] \to 1$ on these vectors is clause (ii) of the cited theorem). A quasi-free state of one canonical mode $a$ with $\langle a\rangle = \langle a^{2}\rangle = 0$ and $\langle a^{*}a\rangle = x$ has, by the pairing rule that defines it, $\langle(a^{*})^{m}a^{m}\rangle = m!\,x^{m}$. For $k \ge 1$ the limit is not of that form: at $m = 2$, $k(k - 1) \ne 2k^{2}$, and at $m = k + 1$ the limit is $0$ while $(k + 1)!\,k^{k+1} > 0$. For $k = 0$ (the product state) the limit is the vacuum, which is quasi-free.
\item[(iv)] \emph{(The local state does not fix the fluctuation state.)} The states $\omega_{0}, \omega_{1}, \omega_{2}, \dots$ have the same local limit, the polarised product state, and pairwise different limits of their fluctuation states. Hence convergence of fluctuation states to a quasi-free state cannot be derived from the convergence of finite marginals alone; the known sufficient hypotheses (product structure, or a uniform clustering bound, at every $N$) are not implied by it. Their necessity is not claimed.
\end{enumerate}
Clauses (i) to (iv) are proved. \emph{Reading.} The quantum central limit theorem turns product states into quasi-free (Gaussian) boson states; the non-Gaussian boson states of a collective mode, its number states, are realised on the tower by the ladder vectors $(K^{*})^{k}P$, which are not product states though they look like the product state on every finite set of blocks. The correlation that carries the boson is spread over all pairs of blocks alike, at order $1/N$.

## technical
On $N$ blocks of two modes the polarised element has every lower mode filled and every upper mode empty; the collective hopping $K^{*}$ flips one block at a time, and $K$ unflips. The ladder vectors $\psi_{k} = (K^{*})^{k}P$ satisfy $K\psi_{k} = k(N - k + 1)\psi_{k-1}$, from the stored commutator $[K, K^{*}] = \sum_{i}(n_{l_{i}} - n_{u_{i}})$, which is $N - 2j$ on $\psi_{j}$. Hence the moments of the normalised mode $B = K/\sqrt{N}$ in the state of $\psi_{k}$ are $(k)_{m}(N - k + 1)\cdots(N - k + m)/N^{m}$ exactly, which tend to $k(k - 1)\cdots(k - m + 1)$: the moments of a state with exactly $k$ bosons. A Gaussian (quasi-free) state with the same mean occupation $k$ would have $m!\,k^{m}$, so at $m = 2$ it would give $2k^{2}$ instead of $k(k - 1)$. Yet each $\psi_{k}$ is, block by block, almost the polarised state: the chance that $m$ given blocks are all polarised is $\binom{N - m}{k}/\binom{N}{k}$, at least $1 - km/(N - k + 1)$, and since the polarised projector of $m$ blocks is minimal, every expectation on those blocks is within $2\sqrt{\varepsilon} + \varepsilon$ of the product value. The correlations are $k(N - k)/(N(N - 1))$ for every pair of blocks: tiny for each pair, but summing to about $k$. So the local state does not determine the limit of the fluctuation states, and the central limit theorem for states cannot replace its hypothesis at each size by local convergence in the limit.

## lay
When many small two-level units are put together, the collective wobble of the whole system usually behaves like a smooth bell-curve quantity, a Gaussian, and in the quantum case like a boson in a thermal or vacuum state. That is the quantum central limit theorem, and it needs the units to be independent. This entry shows that the independence cannot be replaced by something weaker that sounds almost the same. Take the state in which exactly k of N units have been flipped, spread evenly over all of them. Look at any fixed handful of units and, for large N, they are almost certainly unflipped, exactly as in the independent state where none is flipped. But the collective wobble is not Gaussian at all: it is a state holding exactly k bosons. The difference is carried by very weak correlations shared evenly by every pair of units. This is also where the tower keeps its states with a definite number of bosons.

## one-liner
On $N$ blocks the ladder vectors $(K^{*})^{k}P_{\mathrm{pol}}$ have every finite marginal within $O(\sqrt{km/N})$ of the polarised product state, yet the hopping fluctuation $B = K/\sqrt{N}$ has exact moments $(k)_{m}(N - k + 1)^{(m)}/N^{m} \to (k)_{m}$, the $k$-boson number state, which is not quasi-free for $k \ge 1$.
