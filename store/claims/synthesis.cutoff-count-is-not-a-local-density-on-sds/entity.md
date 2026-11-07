---
id: synthesis.cutoff-count-is-not-a-local-density-on-sds
kind: claim
version: 3
title: 'On Schwarzschild-de Sitter the cutoff count is not a local density'
status: proved
region: synthesis
subject: einstein
tags: [counting-rules, horizons, mode-counting, entropy-premises, no-go, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-10-23-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.exceptional-boundary-measure-one-calibration@2
  - interior.schwarzschild-de-sitter-weighted-limit@7
  - singularity.stretched-singularity-count@8
  - scrambling.epoch-modular-period-two-unknowns-become@6
  - synthesis.sds-clausius-fixes-area-constant@5
  - synthesis.residue-from-mode-entropy@4
  - synthesis.boundary-mode-thermal-entropy@2
  - synthesis.q-splits-maximum-entropy-affine-weights@6
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_cutoff_volume_rates
- kind: check
  ref: check.py::check_count_over_hole_period
- kind: check
  ref: check.py::check_no_horizon_period_gives_area_law
- kind: check
  ref: check.py::check_mean_entropy_forced_down
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.c-loc-is-a-second-placement-of-the-count
  - synthesis.kerr-ring-count-misses-area-law
  - synthesis.c-loc-entropy-clause-curvature-independent-density
extraction:
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Version 2, label only: in (iv) kappa k is now attributed to version 2 of Premise (Q) and kappa(k + 1/2) to its version 3 (Leon''s decision 9), and zero weight to the one-mode-per-unit reading of the registered residue; the conclusion covers every fixed weight law and is unchanged. Version 1 -> 2.'
  open_problem: op.derive-loc-and-r-loc
  note: >-
    Test of the constructive route to clause (Loc): derive the curvature-independence of the horizon
    entropy density from what the counted modes are, namely the cutoff modes of (C1) and (C2) (at leading
    order the exceptional-set form (C2')), counted over the modular period under (IC) (stated in the store for Schwarzschild; read here with a
    horizon's modular period) and identified with
    the hole's horizon modes (one mode set, as version 2 of the local-horizon premise states). The route
    fails off the Schwarzschild family. On Schwarzschild-de Sitter, whose interior has the same Kasner wall,
    the cutoff's volume rate is 12 pi M on the exceptional set for every Lambda, while the hole's modular
    period grows with Lambda; with the density calibrated at Lambda = 0 the count over the hole's period is
    u/(3u-2) times A_b/4, a ratio that varies along the family (written through the curvature at the horizon,
    1/(1 - 2 Lambda/3 w_h), w_h the radial Weyl eigenvalue), divergent at
    the Nariai limit. The area law would need the epoch 2 pi r_b^2/M, the period of the Lambda-free part of
    the surface gravity, which is neither horizon's period (kappa_c < kappa_b < M/r_b^2). Consequences:
    under one mode set the literal count contradicts the hole's Clausius entropy A_b/4 for every Lambda > 0,
    as the literal Kerr count does for every spin, so it counts against the literal cutoff placement off
    Lambda = 0, not against (Loc); under the area-law hypothesis the counted modes' mean entropy must fall
    with Lambda/w_h, so their weights in units of the hole's surface gravity cannot follow a fixed law; every weight law the store states (zero weight, kappa k, kappa(k + 1/2), the clock values 0 or +-kappa) is fixed in those units, so under (Q) no assignment escapes; without clause (Q-w) an affine law omega_k = c k + d with c depending on Lambda/w_h (in the class of synthesis.q-splits-maximum-entropy-affine-weights (ii)) would escape, and no stored result adopts one (on modes shared by both sheets of an edge, where (R_loc) forces zero weight, synthesis.r-loc-needs-sheet-labelled-modes, filed alongside, that escape is closed too). On a one-parameter family every quantity is a function of u; the expression through Lambda/w_h is that function written in curvature at the horizon, not by itself evidence of a local density.
    Negative result for deriving (Loc) from the count: the count reading eta = 4 pi nu <s> is
    curvature-independent only on the Lambda = 0 Schwarzschild family. The regime for (C1) is Lambda -> 0,
    M -> infinity at fixed Lambda M^2 (Planck units); for (C2') the count is exact. Transport-absent.
  maintainer_pass_gtg:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the Schwarzschild-de Sitter metric function is read from the gravitational field on flat spacetime in the Painleve-Gullstrand gauge hb = 1 - beta P, beta^2 = 1 - f(r), with Killing field K = hb^{-1}(e_t); w_h is the eigenvalue of the Weyl map of the field strength on the radial plane (store sign), and curvature at the horizon is the field strength there. All formulas, clauses (i) to (v) and their strength unchanged; proof given a pointer to the dictionary Fact.'
---

## formal
Units $\hbar = c = G = 1$. For $\Lambda > 0$ and $0 < M < 1/(3\sqrt{\Lambda})$ let $f(r) = 1 - 2M/r - \Lambda r^{2}/3$ be the metric function of the Schwarzschild-de Sitter field on flat spacetime, in the Painlev\'e-Gullstrand gauge $\hb = 1 - \beta P$, $P(a) = (a \cdot e_{t})\,e_{r}$, $\beta^{2} = 2M/r + \Lambda r^{2}/3 = 1 - f(r)$ (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), with black-hole horizon $r_{b}$ and cosmological horizon $r_{c}$, $2M < r_{b} < 3M < r_{c}$, surface gravities $\kappa_{b} = f'(r_{b})/2 = (3M - r_{b})/r_{b}^{2}$ and $\kappa_{c} = -f'(r_{c})/2$ for the Killing field $\partial_{t}$, the physical vector field $K = \hb^{-1}(e_{t})$, $A_{b} = 4\pi r_{b}^{2}$, $u = 2M/r_{b} \in (\tfrac23, 1)$, and $w_{h} = 2M/r_{b}^{3}$ the radial eigenvalue of the electric part of the Weyl tensor at the horizon, the eigenvalue of the Weyl map $\mathcal{W}$ of the field strength on the radial plane $\sigma_{r}$ in the store's sign. The interior near $r = 0$ has the Kasner wall, exponents and boundary data of the Schwarzschild interior (Theorem \claimref{interior.schwarzschild-de-sitter-weighted-limit}), so the count rules read verbatim on it.
\begin{enumerate}
\item[(i)] \emph{(The cutoff does not see $\Lambda$.)} The measure of the exceptional set (Theorem \claimref{synthesis.exceptional-boundary-measure-one-calibration}(ii)) is $\mu_{E} = \lim_{\tau\to0}V(\tau)/\tau = 12\pi M$ per unit Killing time for every $\Lambda$; $\Lambda$ enters $V$ and $\tau$ only at relative order $\Lambda r^{3}/M$. On the slice $r_{c}^{3} = 2M$ of (C1) (Proposition \claimref{singularity.stretched-singularity-count}) the volume rate is $8\pi M\sqrt{1 - r_{c}/2M + \Lambda/3}$ exactly, so $8\pi M$ at leading order in $(2M)^{-2/3}$ and $\Lambda$ (Planck units; $\Lambda M^{2}$ may stay finite).
\item[(ii)] \emph{(The count over the hole's period.)} Let the counted epoch be the hole's modular period $2\pi/\kappa_{b}$: this reads (IC), which the store states for Schwarzschild, with a horizon's modular period, as it gives at $\Lambda = 0$ (Theorem \claimref{scrambling.epoch-modular-period-two-unknowns-become}), and the density be fixed by the area law at $\Lambda = 0$ ($\nu' = 1/24\pi$ in the 1-nat convention for (C2$'$), equivalently the registered density for (C1) and (C2)). Then the count $N$ and its entropy at mean mode entropy $\langle s\rangle_{0}$ satisfy, exactly for (C2$'$) and at leading order for (C1) and (C2),
\[
\frac{N\langle s\rangle_{0}}{A_{b}/4} \;=\; \frac{M}{\kappa_{b}r_{b}^{2}} \;=\; \frac{u}{3u - 2} \;=\; \frac{1}{1 - 2\Lambda/(3w_{h})} ,
\]
equal to $1$ at $\Lambda = 0$, strictly larger for $\Lambda > 0$, increasing in $\Lambda M^{2}$ and unbounded as $9\Lambda M^{2} \to 1$ (the Nariai limit, $\kappa_{b} \to 0$). Read as an entropy per unit horizon area, the count gives $\tfrac14/(1 - 2\Lambda/3w_{h})$. On this one-parameter family every quantity is a function of $u$; this is that function written through the Ricci curvature ($\Lambda$, the Ricci map $\mathcal{R}(a) = \Lambda a$) and the radial Weyl eigenvalue ($w_{h}$) of the field strength at the horizon, a relabelling which shows that the ratio is not one constant, not that the count is a local density.
\item[(iii)] \emph{(No horizon period gives the area law.)} $N\langle s\rangle_{0} = A_{b}/4$ holds exactly for the epoch $2\pi r_{b}^{2}/M$, the period of $M/r_{b}^{2}$, the part of the surface gravity without $\Lambda$. For $\Lambda > 0$, $\kappa_{c} < \kappa_{b} < M/r_{b}^{2}$, so either horizon's modular period gives a count above $A_{b}/4$.
\item[(iv)] \emph{(Consequences.)} Under the identification of the hole's horizon modes with its cutoff modes (one mode set, Premise \claimref{synthesis.c-loc-local-horizon-premise}), the literal count assigns the hole's horizon the entropy $(A_{b}/4)\,u/(3u - 2)$, while the Clausius relation along the family with the series' temperatures and zero entropy at zero mass gives $A_{b}/4$ (Theorem \claimref{synthesis.sds-clausius-fixes-area-constant}); the two disagree for every $\Lambda > 0$. Under the area-law hypothesis of Theorem \claimref{synthesis.residue-from-mode-entropy} (the counted modes carry $A_{b}/4$), the mean entropy per counted mode is $\langle s\rangle = \langle s\rangle_{0}(3u - 2)/u < \langle s\rangle_{0} \le \ln 2$, so the counted modes' Killing weights in units of $\kappa_{b}$ must grow with $\Lambda/w_{h}$ (Theorem \claimref{synthesis.boundary-mode-thermal-entropy}): no weight law fixed in units of the surface gravity, such as $\omega_{k} = \kappa k$, reconciles the count with the area law on this family, and at the registered zero-weight value for $\Lambda = 0$ every $\Lambda > 0$ needs nonzero weights. Every weight law the store states is of that kind (zero weight, the registered residue's case with one mode per counted unit; $\kappa k$ of version 2 of Premise (Q); $\kappa(k + \tfrac12)$, the offset of its version 3; $0$ or $\pm\kappa$ under the unadopted clock hypothesis (K)), so under one mode set the literal count contradicts $A_{b}/4$ for each of them. Under Premise (Q) no assignment escapes. Without its weight clause (Q-w), an affine law $\omega_{k} = ck + d$ with $c$ depending on $\Lambda/w_{h}$, in the class characterised by Theorem \claimref{synthesis.q-splits-maximum-entropy-affine-weights}(ii), would escape; no stored result adopts one, and on modes shared by the two sheets of an edge, where (R$_{\mathrm{loc}}$) forces zero weight (filed alongside, synthesis.r-loc-needs-sheet-labelled-modes), that escape is closed as well.
\item[(v)] \emph{(For clause (Loc).)} The cutoff count per unit horizon area per modular period is curvature-independent on the $\Lambda = 0$ family only. So clause (Loc) of the local-horizon premise is not a consequence of (C1), (C2) and (IC), read with a horizon's modular period, with one mode set: the count reading $\eta = 4\pi\nu\langle s\rangle$ fails to be a curvature-independent density on Schwarzschild-de Sitter, and a curvature-independent density can come only from a placement of the modes on the horizon with a density fixed by flat data, which restates (Loc). As with the literal Kerr count, the disagreement counts against the literal cutoff placement and (IC) away from $\Lambda = 0$, not against (Loc).
\end{enumerate}

## technical
Clause (Loc) of the local-horizon premise says the entropy per unit area of a small horizon does not depend on the curvature (the gravitational field strength) or the matter at the point. The constructive hope is that this follows from what the counted modes are: if the series' boundary modes, placed at the curvature cutoff inside a hole and counted over one modular period, always add up to a fixed multiple of the horizon area, the density they define would be universal. This result tests that hope on the one family beyond Schwarzschild where the store's count rules apply verbatim, Schwarzschild-de Sitter, whose singularity is the same Kasner wall. The cutoff's volume rate does not feel the cosmological constant at all ($12\pi M$ on the exceptional set), but the hole's modular period does: the surface gravity drops from $M/r_{b}^{2}$ to $(3M - r_{b})/r_{b}^{2}$. So with the density calibrated on Schwarzschild, the count over one period exceeds the area law by the factor $u/(3u - 2)$, which, written through the field strength at the horizon, is $1/(1 - 2\Lambda/3w_{h})$ ($w_{h}$ the radial Weyl eigenvalue): an entropy per unit area that is not one constant, and diverging as the hole approaches the Nariai limit. Neither horizon's period fixes it; only the period of the $\Lambda$-free part of the surface gravity would. Hence the count does not supply (Loc); under the identification of horizon and cutoff modes it contradicts the hole's Clausius entropy $A_{b}/4$ for every positive $\Lambda$, as the literal Kerr count does for every spin; and if the counted modes are to carry $A_{b}/4$, their mean entropy, and so their weights, must depend on the curvature ratio. For physical holes the discrepancy is tiny, of relative size $\tfrac83\Lambda M^{2}$, but it is exact and grows without bound towards Nariai.

## lay
The local-horizon assumption says that every small piece of horizon carries the same entropy per unit area, whatever the strength of the gravitational field there. One might hope to derive this from the series' own way of counting a black hole's quantum modes, which sit deep inside the hole near the singularity and are counted over one tick of the horizon's thermal clock. For an ordinary black hole this count gives exactly a quarter of the horizon area. In a universe with a cosmological constant, the black hole's thermal clock slows down while the region near the singularity is unchanged, so the same counting gives more than a quarter of the area, and much more for the largest holes a positive cosmological constant allows. Measured per unit of horizon area, the count's entropy changes from hole to hole as the cosmological constant's share of the gravitational field strength at the horizon changes. So the counting rule cannot be the reason the entropy per area is universal; that has to be assumed or come from modes placed on the horizon itself.

## one-liner
On a Schwarzschild-de Sitter hole the cutoff count over the hole's modular period is $u/(3u - 2)$ times $A_{b}/4$ ($u = 2M/r_{b}$), an entropy per unit horizon area $1/(4(1 - 2\Lambda/3w_{h}))$ ($w_{h} = 2M/r_{b}^{3}$, the radial eigenvalue of the Weyl part of the field strength) unbounded towards Nariai, and no horizon period restores the area law; so (Loc) does not follow from (C1), (C2) and (IC) read with a horizon's modular period under one mode set, and under (Q), with the area-law hypothesis, no weight assignment reconciles the count with $A_{b}/4$.
