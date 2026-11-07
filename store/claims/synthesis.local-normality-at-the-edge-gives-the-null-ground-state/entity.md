---
id: synthesis.local-normality-at-the-edge-gives-the-null-ground-state
kind: claim
version: 4
title: 'Local normality at the edge gives the null ground state'
status: proved
region: synthesis
subject: thermality
tags: [thermal-premises, horizons, car-algebra, modular-theory, superselection, forcing-and-uniqueness, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-10-31-all-open
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: premises repointed to the premise-free results split out of the null-energy and collapse results
  version: 3
  source: maintainer pass 2026-11-07
- name: Claude Opus 5.5
  role: unit conventions per Leon's rulings of 7 November 2026 (R2)
  version: 3
  source: maintainer pass 2026-11-07 (unit rulings)
- name: Claude Opus 5.5
  role: premise repointed to the carrier content split out of the stationary-horizon result
  version: 3
  source: maintainer pass 2026-11-07 (third cut)
- name: Claude Opus 5.5
  role: 'consistency pass, the flat-chart sentence for the edge (flagged, sentence missing) and the difference quotient Q(u, v) renamed q(u, v) against the house symbol Q(v)'
  version: 4
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'maintainer pass on Leon''s decisions, the shell value of clause (v) stated for the normalised kernel |2 pi R/I_4|^2 (restatement)'
  version: 4
  source: maintainer pass 2026-11-07 (decisions)
review: draft
about:
- obj.hawking.continuum-mode-space
derivations:
- name: main
  uses:
  - synthesis.stationary-generator-states-and-the-edge-scaling@1
  - synthesis.null-vacuum-singularity-under-reparametrisation-and-dilation@1
  - synthesis.imported-powers-stormer-takesaki-disjointness@3
  - synthesis.null-vacuum-on-a-horizon-generator@1
  - synthesis.imported-haag-local-normality@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_weight_half_preserves_the_local_hilbert_schmidt_norm
- kind: check
  ref: check.py::check_quasi_equivalence_gives_a_hilbert_schmidt_difference
- kind: check
  ref: check.py::check_homogeneous_remainder_is_not_square_integrable_at_the_edge
- kind: check
  ref: check.py::check_regular_reparametrisation_changes_the_vacuum_by_a_bounded_kernel
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.n-plus-null-ground-state
  - synthesis.stationary-horizon-state-is-its-own-edge-scaling-limit
  - synthesis.attachment-conformal-energy-is-generated-by-z
  - synthesis.tower-charge-sector-label-temperature-not
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Formal correction (DECISIONS A7, restatement): (v) gave the shell value ln(9/8) for the cross-edge block R = (I_4/2 pi)(u - v)^{-1} itself; the integral of |R|^2 over [s, 2s]^2 is (2 pi)^{-2} ln(9/8). Evidence (reconciler, exact): int_s^{2s} int_s^{2s} (u + w)^{-2} dw du = ln(3/2) - ln(4/3) = ln(9/8), the argument (a + d)(b + c)/((a + c)(b + d)) = 9/8 at a = c = s, b = d = 2s, as the check verifies. The formal now says the integral of |2 pi R/I_4|^2 over every square [s, 2s]^2 is ln(9/8). The conclusion (divergence over shells) is unchanged.'
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 3 -> 4: The flat-chart sentence for the edge (flagged, sentence missing) and the difference quotient Q(u, v) renamed q(u, v) against the house symbol Q(v); mathematics, links, pins, status and checks unchanged.'
  maintainer_pass_clause_split_3:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Third cut, at Leon''s decision of 7 November 2026, folded into version 3 of this pass: this result cited synthesis.stationary-horizon-state-is-its-own-edge-scaling-limit only for its carrier content (the weight-1/2 boost as the scaling about the edge, scaling limits and the local form, a stationary state as its own edge scaling limit, the half-thermal products), now the separate result synthesis.stationary-generator-states-and-the-edge-scaling (i) to (iii); the uses edge, the claimrefs and the checks'' premise calls are repointed to it, so this result no longer inherits (N+) through that one. No assumes edge added or removed; statement unchanged.'
  maintainer_pass_unit_rulings:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Leon''s rulings R1-R4 of 7 November 2026, folded into version 3 of this pass: R2: the null-vacuum kernel W_0 = (I_4/2 pi)(u - v + I_4 0)^{-1}, the cross-edge and thermal kernels written with I_4; no bare i remains, declaration removed'
  maintainer_pass_clause_split:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 2 -> 3, at Leon''s decision of 7 November 2026: it cited synthesis.positive-null-energy-gives-r-premises only for its (i) (the null vacuum, its kernel W_0, and that it satisfies the condition of (N+)) and synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet only for its lemmas (iii) and (iv); these are now synthesis.null-vacuum-on-a-horizon-generator (ii) and synthesis.null-vacuum-singularity-under-reparametrisation-and-dilation (i), (ii), and the two uses edges, the claimrefs and the checks'' premise calls are repointed to them, so this result no longer inherits Premise (N+) through them. Statement, proof argument and checks otherwise unchanged; no assumes edge added or removed; notation as the sweep left it. Pins moved to current versions (statements unchanged): synthesis.stationary-horizon-state-is-its-own-edge-scaling-limit 2 -> 3.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: the i of the generator kernels and of the thermal kernel (i/2 pi) pi T/sinh(pi T(u - v + i0)) is complex analysis of scalar kernels, kept whole. Declared complex-analysis; the wholesale alternative is listed for Leon.'
  open_problem: op.r-premises-external
  note: >-
    Names the principle that the stationary-class reformulation of the problem asks for, in its standard
    operator-algebraic form: local normality of the state to the null vacuum at the bifurcation surface, the
    analogue for the CAR algebra of an interval of one generator of the local normality requirement of algebraic
    quantum field theory (Haag, cited from memory), which is stated for the algebras of spacetime regions. The mechanism is
    one scaling identity: the weight-1/2 dilation, which is the boost on a generator, preserves the
    Hilbert-Schmidt norm of a kernel shrunk onto a point. With the Powers-Stormer criterion already in the store
    (imported for the tower-charge sector result of the dark-matter cluster), quasi-equivalence on the algebra of
    an interval gives a square-integrable difference; that suffices for the scaling limit at a point to be the
    null vacuum (the local form of (N+) at any point of a local Rindler horizon, field-strength free, replacing
    the null-surface Hadamard condition cited from memory in op.derive-loc-and-r-loc), and with stationarity at
    the edge for the state to be the null vacuum, which gives the positivity of the affine null translations on
    the eternal hole (op.null-positivity-curved-horizons, item (ii), within the stationary class). It
    strengthens the stored bounded-remainder clause to a square-integrable one, and shows that the half-thermal
    products are in a different local sector at the edge, Hawking period included. The principle is imported,
    not derived; (N+) remains the premise, and within stationary states the result makes local normality at
    the edge its equivalent form. Transport-absent. The scaling-limit route to the horizon temperature has a
    literature antecedent in Haag, Narnhofer and Stein 1984, who obtain the Hawking temperature from a
    scaling-limit condition at the horizon; the Hilbert-Schmidt form and the generator-algebra setting are what
    is added here. Literature from memory: Haag, Local Quantum Physics; Haag, Narnhofer and Stein 1984;
    Fredenhagen and Haag 1990.
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Uses edge added to the new imported Fact synthesis.imported-haag-local-normality (Haag; Haag, Narnhofer and Stein 1984), which the Reading and proof now cite in place of the citation from memory; content unchanged. Version 1 -> 2.'
  flags:
  - 'beyond one flat chart: on the eternal hole and de Sitter space the edge, where (iv) is posed, is not on the Painleve-Gullstrand or static chart; the condition is stated on the algebra of an interval of the generator through the edge point, with any regular parameter there'
---

## formal
Units $\hbar = c = 1$. On a generator of a horizon, with a regular parameter $u$ and the continuum mode space $\CAR(L^{2}(\R, du)\otimes K)$ of Definition \claimref{obj.hawking.continuum-mode-space}, let $\omega$ be a gauge-invariant quasi-free state with two-point kernel $W_{\omega}(u, v) = \omega(\psi^{*}(v)\psi(u))$, $\omega_{0}$ the null vacuum with $W_{0}(u, v) = \tfrac{I_{4}}{2\pi}(u - v + I_{4}0)^{-1}\otimes\id_{K}$ (the state that (N$_{+}$) selects, Theorem \claimref{synthesis.null-vacuum-on-a-horizon-generator}(ii)), and $R = W_{\omega} - W_{0}$. For an interval $J$ say that $\omega$ is \emph{locally normal to $\omega_{0}$ on $J$} if the restrictions of $\omega$ and $\omega_{0}$ to $\CAR(L^{2}(J)\otimes K)$ are quasi-equivalent, and that $\omega$ satisfies the \emph{local Hilbert-Schmidt condition on $J$} if $R$ restricted to $J \times J$ is a square-integrable kernel (in each $K$-component). Scaling limits and the local form of (N$_{+}$) are as in Theorem \claimref{synthesis.stationary-generator-states-and-the-edge-scaling}.
\begin{enumerate}
\item[(i)] \emph{(The scaling preserves local Hilbert-Schmidt norms; proved.)} For the scaling about $u_{0}$ with weight $p$ per leg, $(S_{\lambda}R)(x, y) = \lambda^{2p}R(u_{0} + \lambda x, u_{0} + \lambda y)$, and any interval $I$, $\|S_{\lambda}R\|^{2}_{L^{2}(I \times I)} = \lambda^{4p - 2}\|R\|^{2}_{L^{2}((u_{0} + \lambda I)^{2})}$. The norm is carried over unchanged exactly for $p = \tfrac12$, the weight of the boost and of the anticommutator.
\item[(ii)] \emph{(Local normality gives the local form; proved, given Powers-Stormer.)} Local normality to $\omega_{0}$ on $J$ implies the local Hilbert-Schmidt condition on $J$. If the condition holds on an interval $J$ containing $u_{0}$, then the scaled kernels $\lambda W_{\omega}(u_{0} + \lambda x, u_{0} + \lambda y)$ converge to $W_{0}$ in Hilbert-Schmidt norm on every bounded interval, so every $n$-point function converges: the scaling limit of $\omega$ at $u_{0}$ exists and is $\omega_{0}$, that is, $\omega$ is locally the null vacuum at $u_{0}$. No bound on $R$ near the point and no reference to the field strength enters.
\item[(iii)] \emph{(Parametrisation independence; proved.)} For a regular reparametrisation $f$ ($C^{3}$, $f' > 0$) the vacuum of the parameter $f$ differs from $\omega_{0}$ by a kernel continuous across the diagonal (Theorem \claimref{synthesis.null-vacuum-singularity-under-reparametrisation-and-dilation}(i)), hence square integrable on bounded intervals; so the local Hilbert-Schmidt condition relative to the vacuum of any regular parameter is one condition, and (ii) holds in the affine parameter of a generator whatever the field strength. Example (exact): $f(u) = u + \tfrac23 u^{3} + \tfrac15 u^{5}$, $f' = (1 + u^{2})^{2}$, gives the difference $(u - v)\big(\tfrac13 - \tfrac15(u^{2} + 3uv + v^{2})\big)/q(u, v)$ with $q = (f(u) - f(v))/(u - v) > 0$ (a difference quotient, not a square), leading term $S_{f}(0)(u - v)/12$.
\item[(iv)] \emph{(Stationarity plus local normality at the edge is (N$_{+}$); proved.)} Let the horizon be in the scope of (N$_{+}$), $u$ the affine parameter with the edge at $u = 0$, and $\omega$ stationary for the boost, which acts as the weight-$\tfrac12$ dilation about the edge (Theorem \claimref{synthesis.stationary-generator-states-and-the-edge-scaling}(i)). If $\omega$ satisfies the local Hilbert-Schmidt condition on an interval containing the edge, in particular if it is locally normal to $\omega_{0}$ there, then $\omega = \omega_{0}$: it satisfies (N$_{+}$), and its affine null translations are positive. This strengthens (ii) of that theorem, where $R$ is assumed bounded near $(0, 0)$.
\item[(v)] \emph{(Local disjointness of the thermal products; proved.)} A kernel homogeneous of degree $-1$ and nonzero on a set of positive measure is not square integrable on any neighbourhood of $(0, 0)$: its integral over each dyadic shell is the same positive number. Hence every stationary gauge-invariant quasi-free state other than $\omega_{0}$, in particular each product $\omega_{c}^{\times}$ of half-generator KMS states at rapidity period $2\pi c$, $c \in (0, \infty]$, including $c = 1$ where both halves are the I-state at $2\pi$, fails the local Hilbert-Schmidt condition on every interval containing the edge, and by Powers-Stormer it is disjoint from $\omega_{0}$ on the algebra of every such interval. For the cross-edge block $R$, common to all $c$, the integral of $|2\pi R/I_{4}|^{2}$ over every square $[s, 2s]^{2}$ is $\ln\tfrac98$ (that of $|R|^{2}$ is $(2\pi)^{-2}\ln\tfrac98$).
\end{enumerate}
\emph{Reading.} Within the stationary class, (N$_{+}$) is equivalent to local normality to the null vacuum at the bifurcation surface, an operator-algebraic condition with no temperature in it and no chart beyond a regular parameter of the generator through its edge point (by (iii) the vacuum of any regular parameter gives the same local Hilbert-Schmidt condition). On the eternal hole this gives item (ii) of the positivity problem, the positivity of the affine null translations, from stationarity plus local normality at the bifurcation surface, where the half-generators of the Painlev\'e-Gullstrand chart do not reach. At any point of a local Rindler horizon in a gravitational field of nonvanishing field strength, (ii) and (iii) give the local form of (N$_{+}$) from local normality at that point, in place of the null-surface form of a Hadamard condition. The condition is the analogue, for the CAR algebra of an interval of one generator relative to $\omega_{0}$, of the local normality principle of algebraic quantum field theory, which asks physical states to lie locally in the vacuum folium of the algebras of spacetime regions (Fact \claimref{synthesis.imported-haag-local-normality}(a)); it is not a theorem of the series, and (N$_{+}$) remains the premise, with this condition its equivalent form within stationary gauge-invariant quasi-free states. The scaling-limit route to the horizon temperature goes back to Haag, Narnhofer and Stein (1984; Fact \claimref{synthesis.imported-haag-local-normality}(b)). Without stationarity the local condition does not give (N$_{+}$) (argued): a state KMS for the affine translations at any temperature has a remainder bounded on bounded sets, so it satisfies the local Hilbert-Schmidt condition and, by (ii), has the null vacuum as scaling limit at every point, and it is not a ground state (that such a state is also locally normal is known for free fields, cited from memory, and not derived here). Transport-absent.

\emph{Beyond one flat chart.} On the eternal hole and on de Sitter space the edge, where (iv) is posed, is the bifurcation surface, which is global and is not carried by a single gravitational field $(\hb, \Omega)$ on flat spacetime (it lies off the Painlev\'e-Gullstrand and static charts); there the condition is stated on the algebra of an interval of the generator through the edge point, in any regular parameter, and the statements that hold on generator pieces of the invertible region are in GTG.

## technical
On a horizon generator the boost is the dilation about the edge with weight one half, and that weight is exactly the one for which rescaling a two-point kernel onto a shrinking neighbourhood preserves its Hilbert-Schmidt norm. Two consequences follow, for gauge-invariant quasi-free states. A state whose kernel differs from the null vacuum's by a square-integrable kernel near a point has the null vacuum as its scaling limit there, since the scaled difference has the norm of the original on a shrinking set, which tends to zero. And a stationary state, being its own scaling limit at the edge, with a square-integrable difference near the edge has difference zero, so it is the null vacuum of (N$_{+}$).

By the Powers-Stormer criterion, quasi-equivalence of quasi-free fermion states on the algebra of an interval implies the square-integrable difference. So the condition is local normality on the algebra of an interval of the generator, the analogue of the locality requirement of algebraic quantum field theory, stated without temperature and without reference to a chart beyond a regular parameter: a regular reparametrisation moves the vacuum by a bounded kernel, as an exact non-Moebius example shows, so the square-integrability condition does not depend on the parameter. Conversely, a nonzero kernel homogeneous of degree $-1$, which is what every stationary state other than the vacuum differs by, contributes the same positive amount on every dyadic shell around the edge and is not square integrable; so the stationary products of half-generator thermal states are locally disjoint from the vacuum at the edge, at every temperature, the right one included. The checks are exact: polynomial kernels integrated over rational rectangles, the finite-dimensional Powers-Stormer inequality, the rational arguments of the shell logarithms, and the reparametrisation identity on a rational grid. On the eternal hole and de Sitter space the edge is the bifurcation surface, which is global: no single gravitational field on flat spacetime carries it, so that part is read on the manifold assembled from several charts.

## lay
A black hole's horizon is made of light rays, and the series' premise says that the quantum field on those rays is in its lowest-energy state for sliding along them. This result shows that, for a field that does not change in time, that premise is the same as a standard locality requirement of quantum field theory: close to the point where the horizon's light rays begin, the state must look like the vacuum in the strong sense that the two cannot be told apart by measurements in a small enough region. The reason is a scaling property: zooming in by the horizon's own time evolution keeps a measure of the difference from the vacuum exactly unchanged, so a time-independent state that differs from the vacuum at all differs equally at every scale and is distinguishable at the starting point. States that are thermal on each half of the light ray fail at that point, even at the Hawking temperature. The locality requirement is borrowed from the literature, not derived in the series.

## one-liner
On a horizon generator the weight-$\tfrac12$ scaling preserves the Hilbert-Schmidt norm of a kernel shrunk onto a point, so for gauge-invariant quasi-free states local normality to the null vacuum at a point (via Powers-Stormer, a square-integrable difference) gives the local form of (N$_{+}$) there in any regular parameter, and a stationary such state locally normal to it at the edge is the null vacuum of (N$_{+}$), positivity included; every other stationary gauge-invariant quasi-free state differs by a degree $-1$ kernel that is not square integrable at the edge, so the half-thermal products, $c = 1$ included, are locally disjoint from the vacuum there.
