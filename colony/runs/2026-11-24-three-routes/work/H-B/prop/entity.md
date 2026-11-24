---
id: synthesis.trace-anomaly-leaves-no-exact-radiation-field-at-a-tame-wall
kind: claim
version: 1
title: The trace anomaly leaves no exact radiation field at a tame wall
status: proved
region: synthesis
subject: quantum-fields
tags: [curvature-and-field-equations, no-go, tameness, undetermined-input]
proposed_by:
  kind: ai
  session: 2026-11-24-three-routes
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-24-three-routes
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.radical-normal-tame-wall-is-a-regular-initial-surface-whose-smoothness-selects-no-state@3
  - synthesis.imported-heat-kernel-coefficients-and-background-field-gauge@2
  - synthesis.imported-sakharov-induced-gravity-coefficients@2
  - synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations@4
  - synthesis.krein-quartet-drops-from-the-induced-einstein-hilbert-coefficient-only-under-a-regulator-that-treats-it-alike@3
  - synthesis.imported-renormalised-stress-tensor-of-hadamard-dirac-states@1
  - synthesis.imported-einstein-cartan-matter-coupling@1
  - dark-matter.ceiling-valued-inherited-success@5
  proof: proof-main.tex
quantities:
- quantity.reduced-planck-mass@1
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_euler_density_of_the_robertson_walker_gauge_field
- kind: check
  ref: check.py::check_anomaly_weights_from_the_stored_heat_kernel_coefficient
- kind: check
  ref: check.py::check_anomalous_stress_map_its_trace_and_conservation
- kind: check
  ref: check.py::check_no_power_law_origin_is_tame_unless_the_anomaly_vanishes
- kind: check
  ref: check.py::check_branch_bound_and_the_numbers_for_the_stored_content
lineage:
  motivated_by:
  - synthesis.hadamard-deposit-premise
  - synthesis.deposit-over-the-conformal-vacuum-is-hadamard-exactly-when-every-occupation-moment-is-finite
  - synthesis.weyl-flat-variations-carry-only-the-stress-trace-and-the-whole-stress-clause-is-the-trace-free-channel
extraction:
  open_problem: op.deposit-state-is-hadamard
  note: >-
    Filed against the chain of the problem at its second step (the radiation-type descent). Hypotheses (A) and
    (E) are hypotheses of this result and not stored premises. The sign and normalisation of the anomalous trace in
    (A), rho - 3P = +alpha E with alpha the sum of the Euler weights over 360 (4 pi)^2, were checked in review on
    the arXiv text of E. Mottola and R. Vaulin, arXiv:gr-qc/0604051, Eqs. (3.4), (3.6b) and (4.12) (signature
    (-,+,+,+) there; de Sitter value T_ab = 6 b' H^4 g_ab); the proposer did not read it and had the sign from
    one remembered case. The reference is not in store/references.yaml and is to be added. Cited from memory
    and not imported, so to be
    imported as Facts or kept as named hypotheses at the maintainer's choice: (1) that the trace anomaly of a
    free conformally covariant field is, with the statistics weight, the local density of its heat-kernel
    coefficient a_4, the same for every Hadamard state (Christensen and Duff 1978 to 1979; Birrell and Davies,
    Quantum Fields in Curved Space, chapter 6; for the Dirac field Dappiaggi, Hack and Pinamonti 2009, whose
    stored Fact records only that the anomaly is computed there); (2) the Laplace-type operator of a gauge
    vector on a gravitational field, minus the vector Laplacian plus the Ricci map on the vector index, with two
    ghost scalars, which the stored attachment result quotes for the term linear in curvature; (3) the
    anomalous stress map of Weyl-flat fields in closed form (Brown and Cassidy 1977; Bunch and Davies 1977), used
    here only on the Robertson-Walker field, where its trace and conservation are proved in the proof; (4) that
    the constant C vanishes for the conformal vacuum (same sources), used only in the last sentence of clause
    (v) and in the Reading; (5) the published forms of the bounded branch and of the de Sitter solution
    (Starobinsky 1980; Fischetti, Hartle and Hu 1979; Anderson 1983; Wald 1978), prior art for clause (v), which
    the clause now credits, not used in its proof; (6) Boyle and Turok's weights (-28, -8) of the dimension-zero scalar, which the check
    recovers from the stored Fact (c) and the weights of clause (ii). The value H^2 = 360 pi/(G N) of the de
    Sitter solution for N scalar units was recalled as a cross-check of the sign and size of alpha, not looked
    up. Nothing was read on the web by the proposer. The stored channel weights 1, 3, 12 quoted in clause (ii) are
    cited in text only, with no uses edge: they test the Weyl-square weights, which no clause uses. The result
    filed alongside that the Reading names is cited in text by its id, to become a reference on acceptance. The
    ceiling 6 x 10^14 GeV is transcribed from the prose of the cited result (the check holds it as a literal).
    Not done: the solutions with a nonzero free coefficient b
    beyond their power-law origins; massive fields and interacting content, whose state-dependent trace is not
    treated; the Weyl-curved (Kasner) branch.
---

## formal
Units $\hbar = c = 1$, $\bar{M}_{P}^{-2} = 8\pi G$. Let $(\hb, \Omega)$ be the spatially flat Robertson-Walker gauge field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), $\hb^{-1}(\gamma_{0}) = \gamma_{0}$, $\hb^{-1}(\gamma_{i}) = a(t)\gamma_{i}$, with $H = \dot a/a$, field strength $\mathcal{R}(B)$ in the store's sign, Ricci map $\mathcal{R}(a) = \partial_{b}\cdot\mathcal{R}(b \wedge a)$, scalar $\mathcal{R}$, Ricci square $\Ric^{2} = \mathcal{R}(\partial_{a})\cdot\mathcal{R}(a)$ and Euler density $\mathcal{E} = K - 4\Ric^{2} + \mathcal{R}^{2}$, where $K = 4\Tr(\mathcal{R}^{2})$ is the square of the field strength, four times the trace over bivectors of $B \mapsto \mathcal{R}(\mathcal{R}(B))$ (in components $\mathrm{Riem}^{2}$). Two named hypotheses, neither a stored premise:
\begin{itemize}
\item[(A)] \emph{(The anomaly; standard, not imported; weights from the stored coefficient in (ii), sign and normalisation of the trace as in Mottola and Vaulin, arXiv:gr-qc/0604051, Eqs. (3.6b) and (4.12).)} The matter is free and conformally covariant: $n_{1/2}$ massless Weyl fields, $n_{1}$ gauge vectors with their ghosts at gauge parameter one, $n_{0}$ conformally coupled real scalars. Its state is Hadamard, homogeneous and isotropic, so its expected stress map (conserved: Fact \claimref{synthesis.imported-renormalised-stress-tensor-of-hadamard-dirac-states} for the Dirac field) is $T(\gamma_{0}) = \rho\,\gamma_{0}$, $T(\gamma_{i}) = -P\,\gamma_{i}$, and on Weyl-flat fields its trace is $\partial_{a}\cdot T(a) = \rho - 3P = \alpha\,\mathcal{E} + b\,\Box\mathcal{R}$, with $\alpha = \bigl(n_{0} + \tfrac{11}{2}n_{1/2} + 62\,n_{1}\bigr)/\bigl(360\,(4\pi)^{2}\bigr)$ the same for every Hadamard state and $b$ the one coefficient the renormalisation leaves free on Weyl-flat fields (Fact \claimref{synthesis.imported-sakharov-induced-gravity-coefficients}(d); its two tensors are proportional where the Weyl part vanishes, cited from memory).
\item[(E)] \emph{(The whole expected stress is the source.)} The field equation $\mathcal{G}(a) = -8\pi G\,T(a)$ (Fact \claimref{synthesis.imported-einstein-cartan-matter-coupling}(a) in the store's sign, the cosmological constant neglected) holds with the whole expected stress of the state as its source, the state-independent part $T_{A}$ of (iii) included. Nothing is assumed on whether the equation is the expectation of an equation between operators (the equation has no other source: the cosmological constant is neglected and the content is that of (A)).
\end{itemize}
\begin{enumerate}
\item[(i)] \emph{(The Euler density; proved.)} $\mathcal{R}(\gamma_{0} \wedge \gamma_{i}) = (\ddot a/a)\,\gamma_{0}\gamma_{i}$ and $\mathcal{R}(\gamma_{i} \wedge \gamma_{j}) = H^{2}\,\gamma_{i}\gamma_{j}$; the Weyl part is zero, $\mathcal{R} = 6(\ddot a/a + H^{2})$, and $\mathcal{E} = 24H^{2}\ddot a/a$. On every gravitational field $\mathcal{E} = -4\,\Tr\bigl((I_{4}\mathcal{R})^{2}\bigr)$, the trace over bivectors of $B \mapsto I_{4}\mathcal{R}(I_{4}\mathcal{R}(B))$. On the radiation field $a = t^{1/2}$ of Theorem \claimref{synthesis.radical-normal-tame-wall-is-a-regular-initial-surface-whose-smoothness-selects-no-state}(iv), $\mathcal{R} = 0$ and $\mathcal{E} = -\tfrac32 t^{-4} = -2\Ric^{2}$, minus twice the Ricci square stored there.
\item[(ii)] \emph{(The weights; computed from the stored coefficient.)} With the squared Dirac operator ($E = -\mathcal{R}/4$, connection curvature $\tfrac12\mathcal{R}(a \wedge b)$ acting by left multiplication), the vector operator ($E$ minus the Ricci map, less two ghost scalars) and the scalar operator ($E = -\xi\mathcal{R}$), the stored coefficient $a_{4}$ and statistics weights (Fact \claimref{synthesis.imported-heat-kernel-coefficients-and-background-field-gauge}(i), (iii)) give, in units of $1/(360\,(4\pi)^{2})$ and without total derivatives, $3W^{2} - \mathcal{E}$ for a conformally coupled real scalar, $9W^{2} - \tfrac{11}{2}\mathcal{E}$ for a Weyl field and $36W^{2} - 62\,\mathcal{E}$ for a gauge vector, $W^{2}$ the square of the Weyl part, with no $\mathcal{R}^{2}$ remainder (a minimally coupled scalar has the remainder $5\mathcal{R}^{2}$). The Weyl-square weights $3, 9, 36$ are three times the stored channel weights $c = 1, 3, 12$ of \claimref{synthesis.gravitational-pair-production-from-the-operator-source-at-first-order}(iv), computed there from pair sources with no heat-kernel input: a check of the stored coefficient and of the three operators of (ii) in their Weyl-square combination, which (A) does not use, not for the Euler weights, which have no stored counterpart. The Weyl-square weights are not used below, since the Weyl part vanishes on every field of this result. The Euler weights $1, \tfrac{11}{2}, 62$ are positive, so $\alpha > 0$ for every content of these three kinds. For the series' content (twelve vectors, forty-eight Weyl fields, the eight real components of two doublets; \claimref{synthesis.krein-quartet-drops-from-the-induced-einstein-hilbert-coefficient-only-under-a-regulator-that-treats-it-alike}(iv)) the weight is $1008 = 28 \times 36$ from the fermions and vectors and $1016$ with the scalars, taken conformally coupled as (A) requires: $\alpha = 127/(720\pi^{2})$. At the stored tree-level coupling $\xi = 0$ the doublets fall outside (A) (their trace has a state-dependent part); leaving them out gives $1008$, $\alpha = 7/(40\pi^{2})$, and changes the numbers of (vi) by under one percent.
\item[(iii)] \emph{(The stress; proved given (A).)} $\rho = C/a^{4} + 6\alpha H^{4} + b\bigl(H\dot{\mathcal{R}} - \tfrac{1}{12}\mathcal{R}^{2} + H^{2}\mathcal{R}\bigr)$ with $C$ a constant of the state, and $P = \tfrac13(\rho - \alpha\mathcal{E} - b\,\Box\mathcal{R})$. The term in $\alpha$ is the map $T_{A}(a) = 2\alpha\bigl[\mathcal{R}(\mathcal{R}(a)) - \tfrac23\mathcal{R}\,\mathcal{R}(a) - \tfrac12\Ric^{2}\,a + \tfrac14\mathcal{R}^{2}\,a\bigr]$, whose trace is $\alpha\mathcal{E}$ on every Weyl-flat field: $T_{A}(\gamma_{0}) = 6\alpha H^{4}\gamma_{0}$, $T_{A}(\gamma_{i}) = -\alpha(2H^{4} - 8H^{2}\ddot a/a)\gamma_{i}$. On the radiation field $\rho_{A} = \tfrac38\alpha t^{-4}$, $P_{A} = \tfrac58\alpha t^{-4}$, and the term in $b$ vanishes identically.
\item[(iv)] \emph{(No tame origin; proved given (A) and (E).)} If $\alpha \neq 0$ the radiation field $a = t^{1/2}$ solves the field equation for no $C$ and no $b$: the trace of the equation is $\mathcal{R} = 8\pi G(\alpha\mathcal{E} + b\,\Box\mathcal{R})$, whose left side is $0$ and whose right side is $-12\pi G\alpha\,t^{-4}$. For a power law $a = t^{p}$, $p \neq 0, 1$, the terms of order $t^{-4}$ of the equation cancel exactly when $2\alpha p^{2} = 3b(2p - 1)$; so $p = \tfrac12$ exactly when $\alpha = 0$. For $\alpha > 0$ the order $t^{-4}$ balances for a power law with $0 < p < 1$ exactly when $b < 0$ (then $0 < p < \tfrac12$) or $b > \tfrac23\alpha$ (then $\tfrac12 < p < 1$), at one exponent for each such $b$. Whether a solution with that leading behaviour exists is not shown. The bracket of such a power law is not tame in cosmic time (Theorem \claimref{synthesis.radical-normal-tame-wall-is-a-regular-initial-surface-whose-smoothness-selects-no-state}(iv)).
\item[(v)] \emph{(The branch joined to late radiation; proved given (A), (E) and $b = 0$.)} With $x = 2\alpha H^{2}/\bar{M}_{P}^{2}$ the equation is $3\bar{M}_{P}^{2}H^{2}(1 - x) = C/a^{4}$. On the branch that tends to the radiation field at late times ($x < \tfrac12$): $H^{2} < \bar{M}_{P}^{2}/(4\alpha)$, $C/a^{4} \le 3\bar{M}_{P}^{4}/(8\alpha)$, and $a^{4} \ge 8\alpha C/(3\bar{M}_{P}^{4}) > 0$; at that scale factor $H$ is finite and $\dot H = -2C/\bigl(3\bar{M}_{P}^{2}a^{4}(1 - 2x)\bigr)$ is unbounded, so the field ends at a positive scale factor where $\mathcal{R}$ is unbounded, not at a wall. With $C = 0$ the solutions are $H = 0$ and $H^{2} = \bar{M}_{P}^{2}/(2\alpha)$. This clause is standard and is stated here for the series' content, not as new: the bounded branch is that of Fischetti, Hartle and Hu and of Anderson, and the de Sitter root is Starobinsky's (all cited from memory).
\item[(vi)] \emph{(The series' content; computed.)} Here $C/a^{4}$ is identified with the thermal density of the content, $C/a^{4} = \tfrac{\pi^{2}}{30}gT^{4}$, which defines the temperature $T$ (a thermal deposit; for another state $T$ is a measure of its density only). With $\alpha = 127/(720\pi^{2})$ and $g = 116$ relativistic degrees of freedom, the largest radiation temperature on that branch has $T_{\max}^{4} = \tfrac{2025}{3683}\bar{M}_{P}^{4}$, $T_{\max} \approx 0.861\,\bar{M}_{P} \approx 2.1 \times 10^{18}$ GeV. On the radiation field the anomalous trace equals the density at $t_{\mathrm{eq}} = \sqrt{2\alpha}/\bar{M}_{P}$, between $0.94$ and $0.95$ Planck times. The stored ceiling $6 \times 10^{14}$ GeV is the upper end of the range of the rung scale (\claimref{dark-matter.ceiling-valued-inherited-success}): a mass, conditional on that result's Hypothesis (U), which the stored mirror and seeding results use as the ceiling of the descent temperature and which is used here as a temperature. At $T = 6 \times 10^{14}$ GeV, $C/a^{4}$ is $6.7 \times 10^{-15}$ of its largest value and the anomalous term is below $1.7 \times 10^{-15}$ of the density.
\end{enumerate}
\emph{Reading (argued).} The radiation-type descent is a stated hypothesis of the deposit results: under it the descended field is, in cosmic time, $t$ times the radical-normal tame wall. Together with a Hadamard state of the content and (E), that hypothesis cannot hold exactly: the conformal factor $t$ does not drop out of the stress, and the remainder is the anomalous map of (iii). The word whole is the content of (E) relative to the store. The stored Clausius theorem takes its stress as a given conserved map, classical or a renormalised expectation value (\claimref{synthesis.einstein-equations-from-c-loc-and-clausius}, (H3)), and the stored inverse-problem result makes the coupled system variational only if the heat tensor is the Hilbert stress up to a matter-independent term $\Theta[g]$ (\claimref{synthesis.inverse-problem-for-the-clausius-route}, clause (v)); $T_{A}$ is such a term, independent of the state, built from the field strength and conserved by itself on the Robertson-Walker field, and whether the system with it is variational is not settled there; the store does not require a local action. With the state-dependent part $C/a^{4}$ alone as the source the exact radiation field is a solution; with the whole expected stress it is not. So the store's routes to the field equation do not decide (E), and (E) is neither implied by nor in conflict with an operator source: it speaks only of the expectation. On a collar at or below the stored ceiling the departure is below two parts in $10^{15}$, and the deposit results use there only a smooth scale factor and the vanishing of the Weyl part, which stand. What does not stand is the extrapolation to the wall: followed back with $b = 0$ the field ends at $T_{\max}$ before any wall, and with $b \neq 0$ any power-law origin, if one exists, has $p \neq \tfrac12$, so that $M = ma$, which goes as the power $p/(1 - p)$ of the conformal time, is not linear in it through the origin (it is smooth there only at the isolated values $p = n/(n + 1)$, $n \ge 2$, reached at $b = 2\alpha n^{2}/(3(n^{2} - 1))$). Statements that use the wall itself, a mass term linear in conformal time through it or a continuation across it, are therefore outside what (A) and (E) allow (a result filed alongside, synthesis.wall-conjugation-invariance-on-a-radiation-type-descent-floors-the-dirac-deposit-and-selects-none, assumes both, as its hypotheses of an exactly linear scale factor on the two sides of the wall, for a Dirac field on a prescribed field; it is therefore not available jointly with (A) and (E)), unless the Euler weight of the content vanishes (the cancellation of Fact \claimref{synthesis.imported-sakharov-induced-gravity-coefficients}(c) needs thirty-six dimension-zero scalars, which the content does not have), or the field equation is not imposed between the wall and the collar. A state without quanta has $C = 0$ (cited from memory for the conformal vacuum) and by (v) does not source a radiation field at all. Interactions and masses give the content a further, state-dependent trace, not treated here. Transport-absent.

## technical
The deposit chain places the descent at the origin of a radiation-dominated Robertson-Walker field, because in cosmic time that field is exactly $t$ times the series' tame wall with the radical normal, and for conformally covariant fields the factor $t$ drops out. It drops out of the field equations of the matter, but not of its renormalised stress: every Hadamard state carries the trace anomaly, a multiple $\alpha$ of the Euler density, which on the radiation field is $-\tfrac32 t^{-4}$ although the scalar curvature vanishes there. The multiple is fixed by the content through the heat-kernel coefficient the store already imports: $1$, $\tfrac{11}{2}$ and $62$ per real scalar, Weyl field and gauge vector, all of one sign, so $1016$ for the series' content. With the whole expected stress as the source of the field equation, the anomalous part included, the exact radiation law is then not a solution, for any state and any value of the one coefficient the renormalisation leaves free. With that coefficient zero, the solution that becomes the radiation field at late times cannot be followed back past a temperature of about $0.86$ reduced Planck masses, where its scalar curvature is unbounded at a positive scale factor (the known bounded branch of the anomaly-corrected equation, here with the series' numbers); with it nonzero, a power-law origin, if the corrected equation has one, has an exponent other than one half (the leading terms can balance only at such an exponent; that a solution with it exists is not shown). On the window the store uses for the descent the correction is below two parts in $10^{15}$, so the collar of the deposit results is unaffected; the wall is what the anomaly removes. Transport-absent.

## lay
The series puts the birth of the hot universe at a special surface, a "tame wall", and relies on the fact that a universe filled with pure radiation expands in exactly the way that makes this surface regular. Quantum fields spoil the exactness. Any physically reasonable state of massless fields carries a small extra pressure and energy that depends only on how the universe is expanding, the trace anomaly. Its size is fixed by counting the fields, and for the particle content of the series it cannot vanish. Close to the wall it grows faster than the energy of the radiation and overtakes it at about the Planck time, so the radiation-filled universe cannot be traced back to the tame wall with these equations. With the one free coefficient of the theory set to zero it ends earlier, at a temperature just under the Planck scale; with it nonzero, any beginning of the simple power-law kind would be of a different sort, not the tame wall, and whether such a beginning exists is not shown. All of this assumes that the averaged energy and pressure of the quantum fields, this extra part included, are what shapes the gravitational field. Later on, at every temperature the series considers for the birth of the hot phase, the effect is smaller than one part in a million billion and changes nothing.

## one-liner
Given the trace anomaly (A) of a Hadamard state of free conformal content and the whole expected stress as the source (E), the radiation field $a = t^{1/2}$, whose Euler density is $-\tfrac32 t^{-4} = -4\Tr((I_{4}\mathcal{R})^{2})$, solves the field equation for no state and no value of the free coefficient unless the Euler weight vanishes, and it is $1016$ real-scalar units for the series' content ($\alpha = 127/(720\pi^{2})$); with the free coefficient zero the (standard) branch joined to late radiation ends at $T_{\max} \approx 0.86\,\bar{M}_{P}$ before any wall, and with it nonzero the order $t^{-4}$ balances for a power law only at $p \neq \tfrac12$ (existence of such a solution not shown), while at $6 \times 10^{14}$ GeV, the stored ceiling read as a temperature, the anomalous density is below $1.7 \times 10^{-15}$ of the total.
