---
id: synthesis.microlocal-condition-on-a-generator-gives-the-local-null-ground-state
kind: claim
version: 4
title: 'On a horizon generator the generator analogue of the microlocal (Hadamard) condition, on both orderings of the two-point kernel, is equivalent to a smooth difference from the null vacuum, so with no stationarity and no temperature it gives the local form of (N$_{+}$) at every point (with the stored theorem and boost stationarity at the edge, (N$_{+}$)); the affine-KMS states satisfy it, so it does not select the ground state'
status: proved
region: synthesis
subject: thermality
tags: [thermal-premises, horizons, car-algebra, forcing-and-uniqueness]
proposed_by:
  kind: ai
  session: 2026-11-01-five-fronts
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.hawking.continuum-mode-space
derivations:
- name: main
  uses:
  - synthesis.local-normality-at-the-edge-gives-the-null-ground-state@2
  - synthesis.stationary-horizon-state-is-its-own-edge-scaling-limit@2
  - synthesis.positive-null-energy-gives-r-premises@4
  - synthesis.imported-microlocal-hadamard-condition@2
  - synthesis.imported-local-quasi-equivalence-of-hadamard-states@1
  - synthesis.imported-kay-wald-uniqueness-and-no-go@1
  - synthesis.imported-propagation-of-hadamard-form@1
  - synthesis.imported-powers-stormer-takesaki-disjointness@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_affine_kms_remainder_is_smooth_at_every_point
- kind: check
  ref: check.py::check_symbol_criterion_separates_thermal_mixture_and_jump_states
- kind: check
  ref: check.py::check_mixture_fails_the_local_hilbert_schmidt_condition_everywhere
- kind: check
  ref: check.py::check_half_thermal_products_fail_the_condition_at_the_edge_only
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.n-plus-null-ground-state
  - synthesis.local-normality-at-the-edge-gives-the-null-ground-state
  - synthesis.imported-haag-local-normality
  - synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet
extraction:
  open_problem: op.r-premises-external
  note: >-
    Poses on the continuum mode space of one horizon generator the analogue of the microlocal form of the
    Hadamard condition (Radzikowski 1996; for the Dirac field on both orderings, Hollands 2001), and proves on
    one generator the analogue of the statement that Hadamard states differ by smooth kernels: the condition
    holds on an interval exactly when the two-point kernel differs from the null vacuum's by a smooth kernel
    there. The condition is pointwise, stationarity-free and temperature-free; it implies the local
    Hilbert-Schmidt condition of the stored local-normality theorem, hence the local form of (N+) at every
    point; the stationary clause is that theorem's (iv), applied as a corollary, and is the mechanism of the
    Kay-Wald uniqueness theorem on the generator algebra. It answers the stationarity-free half of
    op.r-premises-external negatively for every pointwise condition of this kind: the affine-KMS states satisfy
    it at every point (the stored theorem's Reading states this as argued; here it is proved). It is strictly
    stronger than the local Hilbert-Schmidt condition and than boundedness of the remainder (a state whose
    remainder jumps across the diagonal) and excludes the translation-invariant vacuum and anti-vacuum mixtures
    at every point. It is complementary to the condition at the point at infinity of the closed generator
    (synthesis.normality-on-the-closed-generator-gives-the-vacuum-folium-not-the-ground-state): neither implies the other, and even together they
    do not give (N+) without stationarity. Bears on op.derive-loc-and-r-loc (second alternative): what is left
    there, that the series' states satisfy local normality at every point of the generators, would follow from
    this condition on the generators, which would follow from the bulk Hadamard condition given a restriction
    of bulk Hadamard states to the generator algebra (not in the store; for the Dirac field it needs the s-wave
    reduction J3) and the propagation of the bulk condition from one Cauchy surface (Fulling, Sweeny and Wald).
    Imposed at every point it would also close the vacuum gap of the period left by the Clausius relation on
    the action shell (synthesis.clausius-on-the-action-shell-ties-entropy-density-to-period),
    as a new premise, not a derivation. Transport-absent. Literature: M. Radzikowski, Commun. Math. Phys. 179
    (1996) 529; S. Hollands, the Hadamard condition for Dirac fields (arXiv gr-qc/9906076, checked against the
    source); R. Verch, Commun. Math. Phys. 160 (1994) 507 (scalar field); C. D'Antoni and S. Hollands,
    Commun. Math. Phys. 261 (2006) 133 (Dirac field; arXiv math-ph/0106028); B. Kay and R. Wald, Phys. Rep.
    207 (1991) 49, with a gap in the proofs corrected in B. Kay and L. Lupo, Class. Quantum Grav. 33 (2016)
    215001, App. B (content checked in Kay's review arXiv 2308.14517, Sec. 7); S. Fulling, M. Sweeny and
    R. Wald, Commun. Math. Phys. 63 (1978) 257; L. Hormander, The Analysis of Linear Partial Differential
    Operators I, Ch. 8. The bulk results are imported as Facts (synthesis.imported-microlocal-hadamard-condition,
    synthesis.imported-local-quasi-equivalence-of-hadamard-states, synthesis.imported-kay-wald-uniqueness-and-no-go,
    synthesis.imported-propagation-of-hadamard-form, and clause (c) of
    synthesis.imported-powers-stormer-takesaki-disjointness), each checked against its source as its note says;
    Hormander and the statement that Kay and Wald analyse restrictions to a horizon are cited from memory.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 1 -> 2, at Leon''s decision of 2026-11-01 importing the cited literature as Facts: uses edges added to the four new Facts (microlocal Hadamard condition; local quasi-equivalence of Hadamard states; Kay-Wald uniqueness and no-go; propagation of the Hadamard form) and to the Powers-Stormer Fact at version 2, whose clause (c) is the inequality, and the citations from memory in the proof''s Reading replaced by citations of them; statement, proof of (i) to (iv) and check unchanged.'
  maintainer_pass_2:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2 -> 3, at Leon''s decision of 2026-11-01 adopting the Hadamard scaling-limit premise (HS): a marked note in the formal and technical levels records that the restriction of bulk Hadamard states to the generator algebra, recorded here as missing, is computed on the flat field (synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes), and that where the field strength is nonzero the consequence (ii) follows for such states given (HS) (synthesis.hadamard-scaling-limit-premise), so the open premise reduces, for that use, to the series'' states being Hadamard plus (HS). Statement, proof and checks unchanged; no edge added.'
  flags:
  - 'beyond one flat chart: on the eternal hole and de Sitter space the edge, where the stationary corollary is posed, is not on the Painleve-Gullstrand or static chart; the condition is stated on the algebra of an interval of the generator, in any smooth regular parameter'
  - 'analogue, not restriction: no theorem restricting a four-dimensional Hadamard state to the algebra of one null generator of a general field is in the store; the condition is defined directly on the generator algebra (on the flat field the restriction to null planes is computed in synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes)'
  maintainer_pass_hs_bound:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 3 -> 4, at Leon''s decisions of 2 November 2026 (Hadamard scaling bound): (HS), synthesis.hadamard-scaling-limit-premise, is now a theorem (version 4); the marked notes (formal, technical) that called it an adopted premise now name it as a theorem. What this entity asserts is unchanged.'
---

## formal
Units $\hbar = c = 1$. On a generator of a horizon, with a regular parameter $u$ and the continuum mode space $\CAR(L^{2}(\R, du)\otimes K)$ of Definition \claimref{obj.hawking.continuum-mode-space}, let $\omega$ be a gauge-invariant quasi-free state with the two orderings of its two-point kernel $W_{\omega}(u, v) = \omega(\psi^{*}(v)\psi(u))$ and $\tilde W_{\omega}(u, v) = \omega(\psi(u)\psi^{*}(v)) = \delta(u - v)\otimes\id_{K} - W_{\omega}(u, v)$, let $\omega_{0}$ be the null vacuum, $W_{0}(u, v) = \tfrac{i}{2\pi}(u - v + i0)^{-1}\otimes\id_{K}$ (the state that (N$_{+}$) selects, Theorem \claimref{synthesis.positive-null-energy-gives-r-premises}(i)), and $R = W_{\omega} - W_{0}$. For a distribution $D$ on $J \times J$, $J$ an open interval, write $\mathrm{WF}(D)$ for its wave-front set, and let $\Gamma_{\pm} = \{(u, u; \xi, -\xi) : u \in J,\ \pm\xi > 0\}$, with the sign convention in which $\mathrm{WF}(W_{0}) = \Gamma_{+}$. Say that $\omega$ satisfies the \emph{microlocal spectrum condition on $J$} (the generator analogue of the microlocal form of the Hadamard condition) if $\mathrm{WF}(W_{\omega}) \subset \Gamma_{+}$ and $\mathrm{WF}(\tilde W_{\omega}) \subset \Gamma_{-}$ on $J \times J$, in each $K$-component. It names no temperature, no period and no symmetry of the state. The local Hilbert-Schmidt condition, scaling limits and the local form of (N$_{+}$) are as in Theorem \claimref{synthesis.local-normality-at-the-edge-gives-the-null-ground-state}.
\begin{enumerate}
\item[(i)] \emph{(Equivalence; proved.)} $\omega$ satisfies the microlocal spectrum condition on $J$ if and only if $R$ is smooth on $J \times J$. The condition is the same in every smooth regular parameter.
\item[(ii)] \emph{(Consequences; proved, a corollary of the stored theorem.)} If $\omega$ satisfies the condition on $J$, it satisfies the local Hilbert-Schmidt condition on every closed bounded subinterval of $J$, so by Theorem \claimref{synthesis.local-normality-at-the-edge-gives-the-null-ground-state}(ii) its scaling limit at every point of $J$ is $\omega_{0}$: the local form of (N$_{+}$) holds at every point of $J$, with no stationarity and no temperature assumed. With that theorem's (iv): if the horizon is in the scope of (N$_{+}$), $J$ contains the edge and $\omega$ is stationary for the boost, then $\omega = \omega_{0}$.
\item[(iii)] \emph{(Examples; computed exactly.)} (a) Every state KMS for the affine translations at inverse temperature $\beta$, $W_{\beta}(u, v) = \tfrac{i}{2\beta}\sinh\!\big(\pi(u - v + i0)/\beta\big)^{-1}$, satisfies the condition on every interval: $R$ is real-analytic on the whole plane, with leading term $-\tfrac{i\pi}{12\beta^{2}}(u - v)$. (b) For $0 \le t < 1$ the states with occupation symbol $t\,\theta(p) + (1 - t)\,\theta(-p)$, gauge-invariant, quasi-free and invariant under the affine translations, have $R = -(1 - t)\tfrac{i}{\pi}\,\mathrm{PV}(u - v)^{-1}$ and fail the condition and the local Hilbert-Schmidt condition at every point. (c) The stationary half-thermal products $\omega_{c}^{\times}$ of Theorem \claimref{synthesis.stationary-horizon-state-is-its-own-edge-scaling-limit} satisfy the condition on every interval not containing the edge and fail it on every interval that contains it. (d) The state with occupation symbol $\theta(p) - \mathrm{sign}(p)\,c/(1 + |p|)$, $0 < c \le \tfrac12$, has a bounded, square-integrable remainder with a jump across the diagonal, $R(u, v) \to -\tfrac{ic}{2}\,\mathrm{sign}(u - v)$ as $u - v \to 0$; it satisfies the local Hilbert-Schmidt condition and the bounded-remainder condition and fails the microlocal spectrum condition at every point. So the microlocal condition is strictly stronger than both.
\item[(iv)] \emph{(No selection; proved, from (iii)(a).)} The microlocal spectrum condition, and with it the local Hilbert-Schmidt condition, holds at every point for every affine-KMS state with $\beta < \infty$, which is not a ground state; neither selects the state of (N$_{+}$) without a global datum, such as boost stationarity at the edge in (ii).
\end{enumerate}
\emph{Note (the bulk link; added 1 November).} The restriction of bulk Hadamard states to the generator algebra, recorded in the technical level as not in the store, is now computed on the flat field for the Dirac field on every null plane, with the transverse labels as $K$ and no s-wave reduction: every gauge-invariant quasi-free Hadamard state restricts to a state satisfying the condition of (i) on every interval of every generator (Theorem \claimref{synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes}(iii)). Where the field strength is nonzero, the consequence (ii), the local form of (N$_{+}$) at each point, follows for such states by Theorem \claimref{synthesis.hadamard-scaling-limit-premise}, (HS) (formerly a premise); the condition of (i) on intervals is not derived there. So the open premise that the series' states satisfy this condition reduces, for the use the store makes of it, to their being Hadamard plus (HS). Statement and proof unchanged.

## technical
The Hadamard condition is the standard requirement on physical states of a quantum field in a gravitational background: at short distances every physical state looks like the vacuum. In its microlocal form it says that the singularities of the two-point function carry only positive frequency, a pointwise condition with no reference to any symmetry. This result poses the generator analogue of that condition on one generator of a horizon, for the two orderings of the continuum modes' two-point kernel, and proves the generator analogue of the statement that Hadamard states differ by smooth kernels: the condition holds exactly when the kernel differs from the null vacuum's by a smooth function. The proof is two lines: the difference inherits positive frequency from one ordering and negative frequency from the other, and a distribution singular in neither direction is smooth. So the condition gives the square-integrable remainder from which the store already derives the local form of (N$_{+}$) at every point; for a state stationary under the boost the stored theorem then gives (N$_{+}$), which is the Kay-Wald mechanism on the generator algebra. Thermal states for the affine translations meet the condition at every point, so it cannot select the ground state by itself (the stored theorem states this as argued; here it is proved): a global datum is still needed. Translation-invariant mixtures of the vacuum and the anti-vacuum fail it everywhere, the stored half-thermal products fail it at the edge only, and a state whose remainder jumps across the diagonal shows that it is stronger than both square integrability and boundedness of the remainder. It is complementary to normality at the point at infinity of the closed generator: neither condition implies the other, and together they still do not give (N$_{+}$) without stationarity. What op.derive-loc-and-r-loc still needs (the series' states satisfy local normality at every point of the generators) would follow from this condition, which in turn would follow from the bulk Hadamard condition given a restriction of bulk Hadamard states to the generator algebra, which is not in the store (for the Dirac field it needs the s-wave reduction J3), and the propagation of the bulk condition from one Cauchy surface. (Added 1 November: on the flat field that restriction is now computed, for the Dirac field on every null plane with no s-wave reduction, and where the field strength is nonzero the local form at each point follows for Hadamard states by the scaling-limit theorem (HS), formerly a premise; so for that use the open premise reduces to the series' states being Hadamard.)

## lay
Physicists usually require that any reasonable quantum state, looked at closely enough, resembles empty space. The precise version of this requirement says that the very fine-grained structure of the state carries only positive energy. This result writes a version of that requirement for the quantum modes running along a single light ray of a horizon and shows that it is the same as saying the state differs from the vacuum only by something smooth. From there the store's earlier results give the horizon temperature at every point, without assuming that anything is static. It does not single out the vacuum, though: a gas of modes at any temperature also passes, so to get the full premise one still needs the state to be static near the point where the two halves of the horizon meet. Whether the series' states obey the requirement is still an open assumption.

## one-liner
On a horizon generator the generator analogue of the microlocal (Hadamard) condition, on both orderings, holds exactly when the two-point kernel differs from the null vacuum's by a smooth kernel, so with no stationarity and no temperature it gives the local form of (N$_{+}$) at every point (and, with the stored theorem and boost stationarity at the edge, (N$_{+}$)); affine-KMS states pass it everywhere, translation-invariant vacuum and anti-vacuum mixtures fail it everywhere, the half-thermal products fail it at the edge only, and it is strictly stronger than the local Hilbert-Schmidt and bounded-remainder conditions.
