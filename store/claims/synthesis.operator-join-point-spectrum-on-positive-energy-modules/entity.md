---
id: synthesis.operator-join-point-spectrum-on-positive-energy-modules
kind: claim
version: 1
title: On the positive-energy modules of two constituents ($\Lambda > 0$) the bracket and its conjugate span a unitary $\mathfrak{su}(1,1)$ with $K_{0} = \tr\hat h/2\hbar$, the operator join is $\tfrac{\Lambda}{3}\hbar^{2}(K_{0}^{2} - C_{\mathfrak{su}(1,1)} + j(j+1) - 2)$, and modulo the decomposition of $D^{+} \otimes D^{-}$ for $SL(2,\R)$ (cited from memory) its point spectrum lies in $[\tfrac{\Lambda}{3}\hbar^{2}, \infty)$ with the bound attained; so the join has no normalisable zero mode in any helicity sector, and the seed cannot be carried by normalisable massless states of the join
status: proved
region: synthesis
subject: mass
tags: [frozen-point, conformal-spinors, no-go, symmetry-breaking]
proposed_by:
  kind: ai
  session: 2026-10-24-all-open
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
derivations:
- name: main
  uses:
  - synthesis.operator-join-ordering-constants@2
  - synthesis.operator-join-seed-has-no-diagonal-matrix-elements@1
  - synthesis.operator-join-casimir-shifts@2
  - mass.exact-join@7
  - field-theory.twistor-attachment@6
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_positive_energy_module_is_the_stored_oscillator_model
- kind: check
  ref: check.py::check_bracket_is_pair_form
- kind: check
  ref: check.py::check_join_is_casimir_form
- kind: check
  ref: check.py::check_lowest_weights_and_gap
- kind: check
  ref: check.py::check_discrete_series_in_the_product
- kind: check
  ref: check.py::check_no_zero_mode_and_gap
- kind: check
  ref: check.py::check_anti_de_sitter_scale_control
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.operator-join-seed-has-no-diagonal-matrix-elements
  - synthesis.operator-join-ordering-constants
extraction:
  open_problem: op.operator-join
  note: >-
    Answers the reformulated question in the negative on the positive-energy modules, the problem's
    success clause "a proof that none exist on the positive-energy modules, settling that the seed must
    come from outside the join". Route: in the oscillator model of the stored attachment the store's
    conjugation is the Hilbert adjoint, and at the Fock scale matched to the frozen point (lam s^4 = 1,
    unitarily equivalent to any other scale by a dilation) the deformed bracket is the pure pair form
    hbar sqrt(lam)(det a + det c^dag). The stored commutator [B, Bdag] = hbar lam tr h then makes B, Bdag
    and tr h a unitary su(1,1) whose Casimir, with the internal spin, fixes the join. The module is
    the sum over the oscillator spins (j_a, j_c) of D+(j_a + 1) tensor D-(j_c + 1); its discrete-series
    parts are D+(j_a - j_c - n), D-(j_c - j_a - n) with kappa > 1/2 (proved by the lowest-weight
    recurrence and Gauss's test), every such kappa is at most the internal spin j, and the zero-mode
    equation K0^2 - kappa(kappa - 1) + j(j+1) = 2 has no solution with j >= kappa >= 1; the minimum of
    the left side is 3, attained at kappa = 1, K0 = 1, j = 1, an infinite-sum normalisable eigenvector
    with m^2 = Lambda hbar^2/3 (checked on its low components). Cited from memory (to be imported as a
    Fact): the tensor product of a holomorphic and an antiholomorphic discrete series of SL(2,R)
    decomposes as finitely many discrete series plus a direct integral of principal series with
    absolutely continuous measure (Pukanszky 1961, Trans. AMS 100; Repka 1978, Amer. J. Math. 100), so
    the Casimir has no point spectrum below -1/4; numerical support in the proof. Filed alongside,
    synthesis.operator-join-positive-energy-no-finite-energy-zero-modes, a distinct result: it proves
    the adjoint, the per-isotype form 2 Bdag B + (Lambda/3) hbar^2 (s1 + s2 + j(j+1) - 2)
    with its lower bound, and that the join has no eigenvector of finite energy content for any
    eigenvalue for Lambda >= 0 (including Lambda = 0), so the polynomial realisation's constant zero mode
    has no counterpart; it leaves normalisable eigenvectors of infinite energy content undecided. This
    result decides exactly those (Lambda > 0): the point spectrum, all of it carried by infinite-sum
    vectors, starts at Lambda hbar^2/3; with it, the join has no normalisable zero mode of either kind
    for Lambda > 0. The adjointness and the multiplicities of clause (1) are also proved in the result
    filed alongside, synthesis.attachment-conformal-energy-is-generated-by-z (the identification of
    this oscillator realisation with the attachment's module); on acceptance it becomes a use of
    clause (1). For Lambda < 0 the matched scale is lam s^4 = -1: the pure terms of B vanish, B
    preserves the oscillator number, and the join has discrete spectrum with zero modes of finite
    energy content (three at oscillator number 2, all with j = 1 and s1 + s2 = 0; checked), so the
    statement is for Lambda > 0 only. The adapted scale lam s^4 = 1 is the Fock structure of the
    tube point i rho e0 with rho^2 = 2 s^4 = 12/Lambda (det A = -Q(m)/2 in the incidence chart), the tube
    point whose compact plane contains the frozen point. Also
    computed: zero lies in the continuous spectrum of the join only in the sectors
    (K0, j) = (0, 0), (+-1, 0), (+-1/2, 1/2), and the join's spectrum reaches -(7/12) Lambda hbar^2 in the
    (0, 0) sector (the central ordering constant outweighs the positive part there); and the result is
    sharp in the constant: with -Lambda hbar^2 in place of -(2 Lambda/3) hbar^2 a zero mode would exist.
    The flat limit is separate (the adapted scale degenerates); at Lambda = 0 the join is multiplication
    by 2|<pi1 pi2>|^2 in the momentum reading, nonzero off a null set, so again no zero mode (argued,
    standard). Transport-absent in its analytic core (representation theory of su(1,1)); the join, its
    ordering constant and the attachment are the series'.
---

## formal
Let $\Lambda > 0$, $\lambda = \Lambda/6$, and let $\mathcal{H}$ be the positive-energy module of two constituents, the oscillator model of the twistor attachment (Proposition \claimref{field-theory.twistor-attachment}): for each constituent $i$ and spinor index $A$ bosonic modes $a_{iA}$, $c_{iA}$ with Fock vacuum, and, for a scale $s > 0$, $\omega^{A}_{i} = \tfrac{s}{\sqrt2}\sqrt{\hbar}(a_{iA} + c_{iA}^{\dagger})$, $\pi_{iA'} = \tfrac{1}{\sqrt2 s}\sqrt{\hbar}(a_{iA} - c_{iA}^{\dagger})$, with $\bar\pi_{iA} = \pi_{iA'}^{\dagger}$, $\bar\omega_{i}^{A'} = (\omega_{i}^{A})^{\dagger}$. Let $\hat B$, $\hat B^{\dagger}$, $\hat h_{il}$, $\hat C$ and $\hat m^{2} = \hat B^{\dagger}\hat B + \hat B\hat B^{\dagger} + \tfrac{\Lambda}{3}\hat C - \tfrac{2\Lambda}{3}\hbar^{2}$ be as in Proposition \claimref{synthesis.operator-join-ordering-constants}(3).
\begin{enumerate}
\item \emph{(The module.)} These operators satisfy $[Z^{\alpha}_{i}, \bar Z_{l\beta}] = \hbar\delta_{il}\delta^{\alpha}_{\beta}$, the store's conjugate $\hat B^{\dagger}$ is the Hilbert adjoint of $\hat B$ and $\hat h_{il}^{\dagger} = \hat h_{li}$; each constituent's helicity modules have energies $|s| + 1 + n$ with multiplicity $(n+1)(n + 2|s| + 1)$; and different $s$ give unitarily equivalent modules, related by a dilation.
\item \emph{(Pair form.)} At $\lambda s^{4} = 1$, $\hat B = \hbar\sqrt{\lambda}\,(A + C^{\dagger})$ with $A = a_{00}a_{11} - a_{01}a_{10}$ and $C = c_{00}c_{11} - c_{01}c_{10}$ (index order $iA$), and $\tr\hat h = \hbar(N_{a} - N_{c})$. Hence $K_{-} = \hat B/\hbar\sqrt{\lambda}$, $K_{+} = K_{-}^{\dagger}$, $K_{0} = \tr\hat h/2\hbar$ satisfy $[K_{-}, K_{+}] = 2K_{0}$, $[K_{0}, K_{\pm}] = \pm K_{\pm}$: a unitary $\mathfrak{su}(1,1)$ commuting with the internal $SU(2)$.
\item \emph{(The join as Casimirs.)} With $C_{\mathfrak{su}(1,1)} = K_{0}^{2} - K_{0} - K_{+}K_{-}$ and $\hat C = \hbar^{2}j(j+1)$ on internal spin $j$,
\[
\hat m^{2} = \tfrac{\Lambda}{3}\hbar^{2}\bigl(K_{0}^{2} - C_{\mathfrak{su}(1,1)} + j(j+1) - 2\bigr).
\]
\item \emph{(Content.)} $\mathcal{H} = \bigoplus_{j_{a}, j_{c}} \bigl(V_{j_{a}} \otimes V_{j_{c}}\bigr)_{\text{spinor}} \otimes \bigl(V_{j_{a}} \otimes V_{j_{c}}\bigr)_{\text{internal}} \otimes D^{+}(j_{a} + 1) \otimes D^{-}(j_{c} + 1)$, and a lowest (highest) weight vector of $D^{\pm}(\kappa)$ with $\kappa > \tfrac12$ exists in $D^{+}(\kappa_{1}) \otimes D^{-}(\kappa_{2})$ exactly for $\kappa = \pm(\kappa_{1} - \kappa_{2}) - n$, $n = 0, 1, \dots$; in particular $\kappa \le |j_{a} - j_{c}| \le j$, and $K_{0} \equiv j \pmod 1$.
\item \emph{(Point spectrum.)} The point spectrum of $\hat m^{2}$ on $\mathcal{H}$ is contained in $[\tfrac{\Lambda}{3}\hbar^{2}, \infty)$, and $\tfrac{\Lambda}{3}\hbar^{2}$ is an eigenvalue (the lowest weight of $D^{+}(1)$ in $(j_{a}, j_{c}) = (1, 0)$, $j = 1$, $K_{0} = 1$). So $\hat m^{2}$ has no normalisable zero mode in any joint eigenspace of $(\hat h_{11}, \hat h_{22})$, a fortiori none in two neighbouring ones, and by Proposition \claimref{synthesis.operator-join-seed-has-no-diagonal-matrix-elements}(3) no normalisable massless state of the join carries a nonzero seed: the seed must come from outside the join.
\end{enumerate}
Clause (5) uses a cited fact: the Casimir of $\mathfrak{su}(1,1)$ on $D^{+}(\kappa_{1}) \otimes D^{-}(\kappa_{2})$ has point spectrum only on the discrete-series components (cited from memory, see the proof).

## technical
The positive-energy modules are the stored oscillator model, and there the store's conjugate of the deformed bracket is the Hilbert adjoint. Choosing the Fock scale matched to the frozen point (any scale is unitarily equivalent by a dilation) makes the bracket a pure pair operator, $\hat B = \hbar\sqrt{\lambda}(A + C^{\dagger})$, and the stored commutator $[\hat B, \hat B^{\dagger}] = \hbar\lambda\tr\hat h$ says that $\hat B$, $\hat B^{\dagger}$ and $\tr\hat h$ span a unitary $\mathfrak{su}(1,1)$ with compact generator $K_{0} = \tr\hat h/2\hbar$. The palatial join is then $\tfrac{\Lambda}{3}\hbar^{2}(K_{0}^{2} - C + j(j+1) - 2)$, with $C$ the $\mathfrak{su}(1,1)$ Casimir and $j$ the internal spin. The module is a sum of products $D^{+}(j_{a} + 1) \otimes D^{-}(j_{c} + 1)$; normalisable eigenvectors live only on their discrete-series parts $D^{\pm}(\kappa)$, $\kappa \le |j_{a} - j_{c}| \le j$, where the join is at least $\tfrac{\Lambda}{3}\hbar^{2}$, a value it attains. So the join has no normalisable zero mode in any sector, and its massless states can carry no seed. Zero is in the continuous spectrum only in the sectors $(K_{0}, j) = (0, 0)$, $(\pm1, 0)$, $(\pm\tfrac12, \tfrac12)$.

## lay
The series gives a composite of two twistors a mass through an expression called the join, and asks whether a small seed term could tip massless composites into a condensate. That needs massless states in two neighbouring helicity sectors. Here the join is written, on the physical state space, in terms of a hidden symmetry of the pair (an $SU(1,1)$ built from the mass bracket itself), and its exact form shows, for positive $\Lambda$ and modulo a standard decomposition theorem cited from memory, that every genuine, normalisable state has mass squared at least $\Lambda\hbar^{2}/3$, a tiny but nonzero amount set by the cosmological constant. There are no massless normalisable composites at all, so the seed has to come from somewhere other than the join.

## one-liner
On the positive-energy modules the join is $\tfrac{\Lambda}{3}\hbar^{2}(K_{0}^{2} - C_{\mathfrak{su}(1,1)} + j(j+1) - 2)$ with $\hat B \propto K_{-}$, modulo the cited decomposition of $D^{+} \otimes D^{-}$ its point spectrum starts at $\tfrac{\Lambda}{3}\hbar^{2}$ ($\Lambda > 0$), and so it has no normalisable zero modes: the seed must come from outside the join.
