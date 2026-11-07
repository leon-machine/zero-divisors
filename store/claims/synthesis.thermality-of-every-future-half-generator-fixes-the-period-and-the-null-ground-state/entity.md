---
id: synthesis.thermality-of-every-future-half-generator-fixes-the-period-and-the-null-ground-state
kind: claim
version: 3
title: 'Thermal future halves fix the period and the null ground state'
status: proved
region: synthesis
subject: thermality
tags: [thermal-premises, horizons, modular-theory, car-algebra, forcing-and-uniqueness, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-02-qft-full
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
review: draft
about:
- obj.hawking.continuum-mode-space
imported_from:
- citation: 'H.-J. Borchers and D. Buchholz, Global properties of vacuum states in de Sitter space, Ann. Inst. H. Poincare Phys. Theor. 70 (1999), 23--40; arXiv:gr-qc/9803036.'
  key: BorchersBuchholz1999
  locator: 'the geometric modular action of the de Sitter wedges in de Sitter-invariant vacua; cited from memory, theorem numbers and bibliographic data not checked'
derivations:
- name: main
  uses:
  - hawking.i-state-continuum@5
  - hawking.imported-ideal-fermi-gas-uniqueness@2
  - synthesis.positive-null-energy-gives-r-premises@4
  - synthesis.stationary-horizon-state-is-its-own-edge-scaling-limit@2
  - synthesis.de-sitter-horizon-translation-is-conformal-null-rotation@4
  - angle.imported-theorems-deliver-their-hypotheses@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_two_dilation_groups_generate_translations
- kind: check
  ref: check.py::check_null_vacuum_kernel_is_dilation_invariant_about_every_point
- kind: check
  ref: check.py::check_only_period_two_pi_is_translation_invariant
- kind: check
  ref: check.py::check_fermi_transform_residue_series
- kind: check
  ref: check.py::check_points_bounded_below_do_not_suffice
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.n-plus-null-ground-state
  - synthesis.hadamard-deposit-premise
  - synthesis.modular-period-on-values-is-the-dual-plane-turn
  - synthesis.microlocal-condition-on-a-generator-gives-the-local-null-ground-state
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'P = I_4 d/du, the Mellin modes and every two-point kernel are written with I_4; by Leon''s ruling R4 (one unit per entity) the Fourier integral and residue sum of Step 1, (X/Y)^{I_4 w} with poles at w = I_4 pi(2n + 1)/beta, are written with I_4 too and the bridging remark that they were written with i for I_4 is removed, exact since span{1, I_4} is the complex numbers; no bare i remains, so the declaration is removed.'
  maintainer_pass:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 1 -> 2: the text citations of synthesis.wedge-reflections-compose-to-the-two-pi-rotor-so-geometric-modular-conjugations-give-interacting-spin-statistics, both now in the store, become a claimref in the technical level and the proof and a plain id in the extraction note; no edge added (a cross-reference, not a premise). By Leon''s decisions of 2 November 2026 this result is recorded on synthesis.n-plus-null-ground-state as an equivalent form of the ground-state clause. Statement, proof steps and check unchanged.'
  open_problem: op.deposit-state-is-hadamard
  note: >-
    Bears on the ground-state clause of (N+), which the Hadamard results do not give: every Hadamard state has
    the local form of (N+), and within the stationary class (N+) is stationarity plus that local form at the
    edge. Here the clause is characterised without stationarity: on one generator, (N+) holds exactly when the
    state is thermal, at some temperature, for the boost about every point of a set unbounded below, on the
    future half beyond that point (the generator form of geometric modular action). The period 2 pi is derived,
    not assumed: thermality about two points of one generator already forces it, since dilations about two
    points generate translations and the I-state kernel is translation invariant only at period 2 pi. One
    point, or points bounded below, do not suffice. The same modular premise that gives interacting
    spin-statistics through the Guido-Longo theorem (modular covariance of wedge algebras; see also
    synthesis.wedge-reflections-compose-to-the-two-pi-rotor-so-geometric-modular-conjugations-give-interacting-spin-statistics) would therefore give
    the ground-state clause wherever every point of a generator is the edge of a wedge with geometric modular
    action: Minkowski and de Sitter horizons (argued for de Sitter, massive fields included), not the eternal
    hole. Transport-absent.
---

## formal
Units $\hbar = c = 1$. On one generator of a horizon, affine parameter $u \in \R$, let $\CAR(L^{2}(\R, du)\otimes K)$ be the continuum mode space (Definition \claimref{obj.hawking.continuum-mode-space}), $\mathfrak{A}_{a}$ its subalgebra over $L^{2}((a, \infty))\otimes K$, $\beta^{(a)}_{t}(\psi(u)) = e^{t/2}\psi(a + e^{t}(u - a))$ the boost about $a$, and $\omega_{0}$ the null vacuum, the gauge-invariant quasi-free state with symbol $\chi_{(-\infty,0)}(P)\otimes\id_{K}$, $P = I_{4}\,d/du$ (the unit of the mode space is $I_{4}$; numbers are read in $\mathrm{span}\{1, I_{4}\}$), the state of Premise \claimref{synthesis.n-plus-null-ground-state} (Theorem \claimref{synthesis.positive-null-energy-gives-r-premises}(i)).
\begin{enumerate}
\item[(i)] \emph{(Two points fix the period.)} If, for two points $a < b$, the restriction of a state $\omega$ to $\mathfrak{A}_{a}$ is KMS at some $\beta_{a} > 0$ for $\beta^{(a)}$ and its restriction to $\mathfrak{A}_{b}$ is KMS at some $\beta_{b} > 0$ for $\beta^{(b)}$, then $\beta_{a} = \beta_{b} = 2\pi$ and $\omega = \omega_{0}$ on $\mathfrak{A}_{a}$.
\item[(ii)] \emph{(The ground-state clause.)} If $A \subset \R$ is unbounded below and, for every $a \in A$, the restriction of $\omega$ to $\mathfrak{A}_{a}$ is KMS at some period for $\beta^{(a)}$, then $\omega = \omega_{0}$: $\omega$ is gauge-invariant, quasi-free, invariant under the null translations with positive generator. Conversely $\omega_{0}$ is KMS at $2\pi$ about every point. No stationarity, quasi-freeness, gauge invariance or temperature is assumed. The mirror statement holds for past halves and sets unbounded above.
\item[(iii)] \emph{(Sharpness.)} One point does not suffice (the half-thermal products of Theorem \claimref{synthesis.stationary-horizon-state-is-its-own-edge-scaling-limit}), nor does a set bounded below (states equal to $\omega_{0}$ beyond its infimum and arbitrary before it).
\item[(iv)] \emph{(The kernel.)} Off the diagonal, with $X = u - a$, $Y = v - a$, $s = \ln(X/Y)$, $d = u - v$: the unique KMS state at $\beta$ about $a$ has $\omega(\psi^{*}(v)\psi(u)) = \frac{I_{4}}{2\beta}(XY)^{-1/2}/\sinh(\pi s/\beta) = \frac{I_{4}}{\beta d}\sinh(s/2)/\sinh(\pi s/\beta)$, which at fixed $d$ does not depend on the position exactly when $\beta = 2\pi$, where it is $\frac{I_{4}}{2\pi d}$.
\item[(v)] \emph{(De Sitter, argued.)} If the state of a free field on de Sitter space has geometric modular action for the de Sitter wedges (each wedge algebra's modular group is its Killing boost at rapidity period $2\pi$; \cite{BorchersBuchholz1999}, cited from memory, for the de Sitter-invariant vacua) and each wedge algebra is generated by the modes on the future half of its horizon, then, every point of a horizon generator being the edge of such a wedge, (ii) gives (N$_{+}$) on the cosmological horizon for that field, massive fields included (Theorem \claimref{synthesis.de-sitter-horizon-translation-is-conformal-null-rotation} reaches only conformally invariant fields). Here the period $2\pi$ is already part of the hypothesis (geometric modular action is essentially the Bisognano-Wichmann property), so the derived period does no work; the gain over the stored conformal route is the massive case only, and it rests on the assumption, not proved here, that the horizon modes generate the wedge algebras (for massive fields the restriction to the horizon is not automatic). The eternal hole is not reached: only its bifurcation surface carries a Killing boost.
\end{enumerate}
Status: (i) to (iv) proved, with exact checks of the affine algebra, the kernel identities, the residue series and the finite counter-model; (v) argued, given two hypotheses not proved here. Standard: the I-state kernel and the forward direction. Transport-absent.

## technical
(N$_{+}$) asks that the modes on a horizon's light rays be in their ground state for sliding along the rays; the Hadamard results now give its short-distance form at every point, and within stationary states it is that short-distance form at the edge. What has been missing is a form of the global clause that does not presuppose stationarity. This result gives one, in the language of modular theory: on one light ray, the state is the (N$_{+}$) vacuum exactly when, beyond each point of a set of points reaching arbitrarily far into the past, it is thermal for the boost about that point. No temperature is specified: the period $2\pi$ is forced, because dilations about two different points compose to translations, and the thermal kernel about a point is translation invariant only at period $2\pi$. Nothing about the state is assumed in advance; it need not be quasi-free or gauge-invariant, since a thermal state for a boost is unique.

The condition cannot be weakened to one point (the stored half-thermal states are thermal about the edge only) or to points bounded below (the state below them is then free). It is the generator form of what modular theory calls geometric modular action, the property that the Bisognano-Wichmann theorem gives the vacuum of a relativistic field. So a single premise of modular covariance, which through the Guido-Longo theorem, or through the geometric action of the wedge reflections (\claimref{synthesis.wedge-reflections-compose-to-the-two-pi-rotor-so-geometric-modular-conjugations-give-interacting-spin-statistics}), would also give spin-statistics for interacting fields, gives the ground-state clause of (N$_{+}$) wherever every point of a generator is the edge of a wedge with geometric modular action. On de Sitter space this is so (argued, given that the wedge algebras are generated by their horizon modes and that the state has geometric modular action, which de Sitter-invariant vacua have); there the period is already in that hypothesis, so what is gained is only the massive case, which the stored conformal-energy argument does not reach and which rests on the horizon modes generating the wedge algebras; on the eternal black hole it is not, since only one point of each generator is the edge of a Killing wedge.

## lay
The series assumes that the quantum modes running along a horizon's light rays are in their lowest-energy state. For particles of the electron's kind (fermions), this result gives an equivalent condition that sounds quite different: from every point along a light ray, looking forward along the ray, the modes appear warm, as the modes beyond an accelerated observer's horizon do. Surprisingly, the temperature does not need to be specified: asking for warmth about two different points of the same ray already fixes it at the standard value, and asking for it about points reaching arbitrarily far back fixes the whole state as the lowest-energy one. This links the assumption to a well-studied property of the vacuum in relativistic quantum theory, and it shows how it could hold on the horizon of an expanding universe for massive particles too, given an assumption about how the horizon's modes relate to the region behind it, though not, by this route, on a black hole that has always existed.

## one-liner
For the fermionic (CAR) modes of a horizon generator, a state whose restriction beyond each point of a set unbounded below is KMS, at any period, for the boost about that point is the (N$_{+}$) null vacuum, with every period forced to $2\pi$ (two points suffice for the period, since dilations about two points generate translations and the thermal kernel $\sinh(s/2)/\sinh(\pi s/\beta)$ is translation invariant only at $\beta = 2\pi$); one point or a set bounded below does not suffice; it applies on generators each of whose points is the edge of a Killing wedge: Minkowski null planes, and de Sitter horizons (argued; there the period is in the geometric-modular-action hypothesis and the gain is the massive case, given that horizon modes generate the wedge algebras), not the eternal hole.
