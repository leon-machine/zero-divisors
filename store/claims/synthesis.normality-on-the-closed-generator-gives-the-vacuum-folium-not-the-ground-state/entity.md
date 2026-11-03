---
id: synthesis.normality-on-the-closed-generator-gives-the-vacuum-folium-not-the-ground-state
kind: claim
version: 1
title: 'On a horizon generator closed by its Moebius covariance, the Hilbert-Schmidt form of local normality to the null vacuum on every interval, the arcs through the point at infinity included, is a globally square-integrable two-point difference; for pure gauge-invariant quasi-free states this is global quasi-equivalence with the null vacuum, the folium form of (N$_{+}$) with the affine translations positive in the state''s representation, and it gives (N$_{+}$) itself only with translation or boost stationarity; it excludes the affine-KMS states on one far end, while normality at every finite point, the vacuum on each far end separately and implementability of the affine group do not fix the folium'
status: proved
region: synthesis
subject: thermality
tags: [thermal-premises, horizons, car-algebra, superselection, forcing-and-uniqueness]
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
  - synthesis.imported-powers-stormer-takesaki-disjointness@2
  - synthesis.stationary-horizon-state-is-its-own-edge-scaling-limit@2
  - synthesis.positive-null-energy-gives-r-premises@4
  - synthesis.attachment-conformal-energy-is-generated-by-z@1
  - synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet@1
  - synthesis.imported-haag-local-normality@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_the_attachment_closes_each_null_line_into_a_circle
- kind: check
  ref: check.py::check_three_arcs_cover_every_pair_of_points
- kind: check
  ref: check.py::check_affine_kms_states_fail_on_a_single_far_end
- kind: check
  ref: check.py::check_the_slope_jump_vacuum_is_the_null_vacuum_on_each_far_end
- kind: check
  ref: check.py::check_the_slope_jump_vacuum_is_globally_disjoint_from_the_null_vacuum
- kind: check
  ref: check.py::check_the_affine_group_is_implementable_on_the_slope_jump_vacuum
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.n-plus-null-ground-state
  - synthesis.local-normality-at-the-edge-gives-the-null-ground-state
  - synthesis.attachment-conformal-energy-is-generated-by-z
extraction:
  open_problem: op.r-premises-external
  note: >-
    Answers the problem's second attack line (a stationarity-free form of (N+): local normality at every point
    together with the attachment's vacuum far from the hole, tested against the affine-KMS states) and tests its
    first (an implementability condition for the boost on the generators' algebra). The output is the folium form
    of (N+), not (N+): for pure states the condition is global quasi-equivalence with the null vacuum restated, and
    positivity of the translations in the vacuum folium is standard; the ground-state clause still needs
    stationarity. What is new is the three-arc lemma (the Hilbert-Schmidt condition on every arc of the closed
    generator is global), that the affine-KMS states fail already on one far end, and the slope-jump vacuum: a
    regular reparametrisation, linear outside a compact set with different slopes at the two ends, whose vacuum is
    the null vacuum exactly on each far end, satisfies the local Hilbert-Schmidt condition on every bounded interval,
    has every affine map implementable, and is disjoint from the null vacuum. In the coordinate -1/u it is a kink at
    the point at infinity, the degree -1 obstruction of the stored half-thermal products moved from the edge to
    infinity. The property used to close the generator is the standard SL(2, R) covariance of the chiral null
    vacuum; the twistor attachment realises it geometrically on null lines of Minkowski space. Complementary to the
    microlocal condition on a generator (synthesis.microlocal-condition-on-a-generator-gives-the-local-null-ground-state):
    neither condition implies the other, and even together they do not give (N+) without stationarity.
    Transport-absent. The principle remains imported (local normality, Fact synthesis.imported-haag-local-normality),
    posed on the closed generator. Literature from memory, not used in the proof: Segal's implementability of
    smooth circle diffeomorphisms for the free chiral fermion (which would upgrade the bounded-interval clauses
    from the Hilbert-Schmidt form to local normality proper).
  flags:
  - 'beyond one flat chart: the closing at infinity is the abstract Moebius covariance of the one-generator algebra and its vacuum; on null lines of Minkowski space (and on de Sitter horizons) the attachment realises it by conformal rotors, while on the eternal hole the point at infinity of a Kruskal generator is not a spacetime point joined by the attachment and only the abstract covariance is available'
---

## formal
Units $\hbar = c = 1$. On a generator with affine parameter $u$ and the continuum mode space $\CAR(L^{2}(\R, du)\otimes K)$ of Definition \claimref{obj.hawking.continuum-mode-space}, let $\omega$ be a gauge-invariant quasi-free state with two-point kernel $W_{\omega}$, $\omega_{0}$ the null vacuum, $W_{0}(u, v) = \tfrac{i}{2\pi}(u - v + i0)^{-1}\otimes\id_{K}$ (Theorem \claimref{synthesis.positive-null-energy-gives-r-premises}(i)), $R = W_{\omega} - W_{0}$, and the local Hilbert-Schmidt condition on a set $A$ as in Theorem \claimref{synthesis.local-normality-at-the-edge-gives-the-null-ground-state} ($R$ square integrable on $A \times A$). The \emph{closed generator} is $\R \cup \{\infty\}$; its intervals are the bounded intervals and the complements of bounded intervals (the arcs through $\infty$).
\begin{enumerate}
\item[(i)] \emph{(The attachment closes the generator; proved.)} In $\Cl(2,4)$ with $\nInf = \nu + e_{-}$, $\nO = \tfrac12(\nu - e_{-})$ and the points $X(s) = \nO + s n$ of the null line of $n = e_{0} + e_{1}$ ($Q(X(s)) = 0$), the rotors $1 + \tfrac{t}{2}n\nInf$, $1 + \tfrac{c}{2}m\nO$ ($m = e_{0} - e_{1}$) and $\cosh\theta + \sinh\theta\,\nu e_{-}$ act on the line by $s \mapsto s + t$, $s \mapsto s/(1 - 2cs)$ and $s \mapsto e^{-2\theta}s$; the composite $J$ of a translation by $-1$, a special conformal map with $c = -\tfrac12$ and a translation by $-1$ acts by $s \mapsto -1/s$ and sends $\nO$ to a multiple of $n$, the point at infinity of the line. The null vacuum kernel with the spinor weight is invariant under every $g(s) = (as + b)/(cs + d)$, $ad - bc = 1$: $(cu + d)^{-1}(cv + d)^{-1}\,(g(u) - g(v))^{-1} = (u - v)^{-1}$. So $\infty$ is a regular point of the closed generator for $\omega_{0}$, and the local Hilbert-Schmidt condition on an arc through it is posed as on any other interval. The property used is the $SL(2, \R)$ covariance of the chiral vacuum, which holds on every generator; the conformal rotors are its realisation on null lines of Minkowski space, and on the eternal hole only the abstract covariance is available.
\item[(ii)] \emph{(Local on the closed generator is global; proved.)} If $\omega$ satisfies the local Hilbert-Schmidt condition on every interval of the closed generator, in particular if it is locally normal to $\omega_{0}$ on each (Powers-Stormer, as in the theorem cited above), then $R$ is square integrable on $\R \times \R$: with $E_{1} = \{|u| > L\}$ and two disjoint bounded intervals $E_{2}, E_{3} \subset [-L, L]$, every pair of points avoids some $E_{k}$, and the complements $A_{k}$ are intervals of the closed generator. For a pure state ($W_{\omega}$ a projection) this is equivalent to quasi-equivalence, hence unitary equivalence, with $\omega_{0}$ on the whole generator algebra (Fact \claimref{synthesis.imported-powers-stormer-takesaki-disjointness}(a)): on the closed generator the condition is global normality restated. For mixed states it gives the square-integrable difference only, not quasi-equivalence.
\item[(iii)] \emph{(Stationary states; proved, the boost case a corollary of the stored theorem.)} If $R$ is square integrable on a far end and $\omega$ is stationary for the affine translations, then $\omega = \omega_{0}$; if instead $\omega$ is stationary for the boost about a point, $\omega = \omega_{0}$ already by Theorem \claimref{synthesis.local-normality-at-the-edge-gives-the-null-ground-state}(iv), of which this is a corollary. So the condition gives (N$_{+}$) itself only together with one of the two stationarities.
\item[(iv)] \emph{(The folium form of (N$_{+}$); proved for pure states, standard once (ii) holds.)} A pure $\omega$ with the condition of (ii) is a vector state of the null vacuum's representation, in which the affine translations are implemented with nonnegative generator $P$; so the positivity clause of (N$_{+}$) holds in the representation of $\omega$, and the averaged null energy along the complete generator relative to $\omega_{0}$, $\omega(P)$, is nonnegative wherever defined. The ground-state clause, $\omega = \omega_{0}$, is not implied: no condition depending only on the folium can single out $\omega_{0}$, since its normal excitations share it (the state with projection $P_{0} + |g\rangle\langle g|$).
\item[(v)] \emph{(Affine-KMS states; proved.)} A state KMS for the affine translations at temperature $T > 0$ differs from $\omega_{0}$ by the nonzero translation-invariant kernel $\tfrac{i}{2\pi}\big(\pi T/\sinh(\pi T s) - 1/s\big)$, $s = u - v$, with expansion $-\tfrac{i}{2\pi}\big(\tfrac{(\pi T)^{2}s}{6} - \tfrac{7(\pi T)^{4}s^{3}}{360} + \dots\big)$; a nonzero translation-invariant kernel is not square integrable on $(L, \infty)^{2}$ for any $L$. So these states, which satisfy the local Hilbert-Schmidt condition at every finite point, fail it on a single far end.
\item[(vi)] \emph{(The far ends must be joined; proved, given Powers-Stormer.)} Let $f$ be the regular reparametrisation with $f(u) = u$ for $u \le -1$, $f(u) = u/4$ for $u \ge 1$ and $f' = 1 - \tfrac34 S(\tfrac{u + 1}{2})$ on $[-1, 1]$, $S(t) = 6t^{5} - 15t^{4} + 10t^{3}$ ($C^{3}$, $f' \in [\tfrac14, 1]$), and $\omega_{f}$ the vacuum of the parameter $f$, $W_{f}(u, v) = \sqrt{f'(u)f'(v)}\,W_{0}(f(u), f(v))$, a pure state. Then: $W_{f} = W_{0}$ on $(-\infty, -1)^{2}$ and on $(1, \infty)^{2}$, so $\omega_{f}$ is the null vacuum on each far end; $\omega_{f}$ satisfies the local Hilbert-Schmidt condition on every bounded interval (Theorem \claimref{synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet}(iii)), so it is locally the null vacuum at every finite point; for every affine map $\alpha$ (translations, and boosts about every point) $\omega_{f}\circ\alpha$ is quasi-equivalent to $\omega_{f}$; and on $(1, \infty)\times(-\infty, -1)$, $W_{f} - W_{0} = \tfrac{i}{2\pi}(u + 2v)/((u - 4v)(u - v))$, homogeneous of degree $-1$ and not square integrable, so $\omega_{f}$ is disjoint from $\omega_{0}$ and fails the condition of (ii) on the arcs through $\infty$. With slope $1/\mu$ at $+\infty$ in place of $\tfrac14$ the cross-block difference is $\tfrac{i}{2\pi}\big(\sqrt{\mu}/(u - \mu v) - 1/(u - v)\big)$, and the states are mutually disjoint for different $\mu$ (slopes $\tfrac14$ and $\tfrac19$, $\mu = 4, 9$, differ by $-\tfrac{i}{2\pi}(u + 6v)/((u - 4v)(u - 9v))$ on the cross block). In the coordinate $w = -1/u$ the reparametrisation has slope $1$ for $w > 0$ and $4$ for $w < 0$: $\omega_{f}$ is a kink at the point at infinity, the degree $-1$ obstruction of the stored half-thermal products at the edge (Theorem \claimref{synthesis.local-normality-at-the-edge-gives-the-null-ground-state}(v)) moved to infinity.
\end{enumerate}
\emph{Reading.} The stationarity-free output is the folium form of (N$_{+}$), not (N$_{+}$): local normality to the null vacuum on every interval of the Moebius-closed generator, the point at infinity included, which for pure states is global quasi-equivalence with $\omega_{0}$ restated, and in which positivity of the affine translations is standard. It holds for $\omega_{0}$ and its normal excitations, gives (N$_{+}$) only with translation or boost stationarity, and excludes the affine-KMS states and the half-thermal products. The new content is the three-arc lemma, the failure of the affine-KMS states on one far end, and the slope-jump vacua: the far-away clause has to be posed on the arcs through $\infty$, which join the two ends, since the vacuum on each end separately, local normality at every finite point and implementability of the boosts about every point are all satisfied by the disjoint states $\omega_{f}$ (with a $C^{\infty}$ transition in place of the quintic, $\omega_{f}$ also has a smooth remainder on bounded intervals; argued). The condition is complementary to the microlocal condition on a generator (\claimref{synthesis.microlocal-condition-on-a-generator-gives-the-local-null-ground-state}): that one is a short-distance condition at finite points, this one a condition at the point at infinity, and neither implies the other (the affine-KMS states and a smooth slope-jump vacuum pass the first and fail the second; $P_{0} + |g\rangle\langle g|$ with $g$ not smooth passes the second and fails the first). Even together they do not give (N$_{+}$) without stationarity: with $g$ a Schwartz function that state passes both and is not a ground state. The principle is the generator-algebra analogue of local normality (Fact \claimref{synthesis.imported-haag-local-normality}), imported, not derived. Transport-absent; the closing of the generator is the standard Moebius covariance of the chiral vacuum, which the twistor attachment realises on null lines of Minkowski space.

## technical
On a horizon generator the earlier local-normality result needs stationarity to turn a local condition into the premise (N$_{+}$). Without stationarity, local conditions at points cannot do it: states thermal for the affine translations look like the vacuum near every point. The remedy examined here is to impose the condition also far away, and the result shows exactly what that gives. On a single far end the thermal states already fail, since a translation-invariant difference accumulates without bound along the end. The vacuum on each end separately is not enough: the vacuum of a parameter whose slope at one end differs from the slope at the other is the vacuum on each end and near every finite point, admits every translation and boost as a symmetry of its folium, and is still disjoint from the vacuum, through a scale-invariant correlation between the two ends; seen from the point at infinity it is a kink, the same obstruction that the half-thermal products present at the edge. The chiral vacuum is covariant under Moebius maps of the generator, which the twistor attachment realises on null lines of Minkowski space, so the two ends meet at a regular point of a circle. Imposing local normality on every arc of that circle makes the difference square integrable globally, by a covering with three arcs. For pure states this is just global equivalence with the vacuum representation, in which the null energy is positive: the folium form of (N$_{+}$). Being the vacuum itself, the ground-state clause, still needs invariance under the boost or the translations; no condition on the folium can do more, because excitations of the vacuum share its folium. Checks: the conformal rotors in $\Cl(2,4)$ acting on the points of a null line, the Moebius invariance of the vacuum kernel, the arc cover, the series of $x/\sinh x$, and the slope-jump kernel identities with exact lower bounds on dilated rectangles.

## lay
The series assumes that the quantum field on the light rays of a horizon is in its lowest-energy state. Earlier work showed that for a field that does not change in time this is the same as a standard locality requirement at the point where the horizon's light rays begin. Here the time-independence is dropped. Looking like the vacuum near every point of a light ray is not enough, since a warm state does so too; asking for the vacuum far along the ray rules out the warm state, but a subtler state still passes if the two far ends are tested separately. Joining the two ends of a light ray at one point, as the symmetries of the vacuum allow, and requiring the vacuum's local behaviour there as well puts the state in the vacuum's family, where energy along the ray is never negative; being the vacuum itself still needs time-independence.

## one-liner
On a horizon generator closed by the Moebius covariance of the chiral vacuum (realised on Minkowski null lines by the attachment's conformal rotors), local normality to the null vacuum on every interval including the arcs through infinity is a globally square-integrable kernel difference, which for pure states is global quasi-equivalence with the null vacuum: the folium form of (N$_{+}$), with positive affine translations in the state's representation, giving (N$_{+}$) itself only with translation or boost stationarity; affine-KMS states fail on one far end, and a slope-jump vacuum (a kink at infinity) shows that normality at finite points, the vacuum on each far end separately and implementability of the affine group do not fix the folium.
