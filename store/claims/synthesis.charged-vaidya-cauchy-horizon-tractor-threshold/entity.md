---
id: synthesis.charged-vaidya-cauchy-horizon-tractor-threshold
kind: claim
version: 1
title: 'Tractor transport to the charged Vaidya Cauchy horizon: a flux threshold'
status: proved
region: synthesis
subject: interior
tags: [tractors, horizons, limits, null-directions]
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
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.tractor-transport-weak-null-crossing@4
  - synthesis.crossing-transport-tipler-threshold-sharp@4
  - interior.imported-tractor-connection@2
  - synthesis.imported-gtg-dictionary@1
  - synthesis.plane-wave-weak-null-crossing-null-shell-ambiguity@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_store_sign
- kind: check
  ref: check.py::check_vaidya_schouten
- kind: check
  ref: check.py::check_crossing_ray
- kind: check
  ref: check.py::check_inner_horizon
- kind: check
  ref: check.py::check_threshold_bookkeeping
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - interior.filtration-cauchy-horizon-read-literature
  - synthesis.plane-wave-weak-null-crossing-null-shell-ambiguity
extraction:
  open_problem: op.cauchy-horizon-transport
  flags:
  - 'beyond one flat chart: the Cauchy horizon is the boundary v -> infinity of the region-II chart of background labels (v, r, x, y); clauses (1)-(4) are statements on the approach side, and a crossing needs a continuation of the gravitational field beyond that boundary, which is not constructed here'
  note: >-
    First black-hole Cauchy horizon in the store on which the hypotheses of
    synthesis.tractor-transport-weak-null-crossing are verified rather than read from the literature. The model is the
    charged Vaidya(-de Sitter) field, Einstein-Maxwell with an ingoing null dust and Lambda (Hiscock's model of a
    charged hole fed by infalling radiation, Phys. Lett. A 83 (1981) 110, cited from memory, for Lambda = 0): it has no
    outgoing flux and so no mass inflation, so it tests the blue-shift half of the Cauchy-horizon instability, not the
    Poisson-Israel half. Exact content: the Schouten tensor is (Lambda/6) g - (m'/r^2) dv dv + Maxwell, the dust part
    rank-one null along dv with the focusing sign; along every outgoing radial null free-fall worldline in region II the
    parallel conormal is dv/w with w the blue-shift factor, growing like exp(kappa_- v); the Tipler-type integral is
    comparable to the accreted mass; the L^1 test is the blue-shifted flux. Reading, argued: F is (up to 4 pi and
    bounded factors) the energy the crossing observer absorbs, int T(gamma', gamma') ds, so uniqueness of tractor
    transport is finiteness of the blue-shifted dose, and its failure is the infinite blue shift of Penrose and Simpson
    read in the bottom slot. For exponential tails the threshold beta > 1/2 coincides with the H^1 threshold of
    Cardoso, Costa, Destounis, Hintz and Jansen (2018) for Reissner-Nordstrom-de Sitter, where a field decaying like
    exp(-alpha v) has flux exp(-2 alpha v) (literature, cited from memory, not part of the proof); here it is proved for
    null dust, not for a scalar field. Price-law tails (flux decaying like an inverse power p > 2 of v; the value of the
    exponent, cited from memory, does not matter here) are case (b) of the sharp threshold. Not covered: the outgoing flux and
    mass inflation of the perturbed Reissner-Nordstrom interior, the scalar-field horizons of Dafermos and Luk-Oh, and
    Kerr. The continuation across the horizon with continuous Levi-Civita transport, needed for the crossing clauses (1)
    and (2) of the stored theorem, is not proved here. Literature, cited from memory, not checked, and not part of the proof: weak null singularities of this spherical kind admit a C^0 extension with
    Christoffel symbols in L^1_loc (Dafermos) and none with Christoffel symbols in L^s_loc for s > 1 (Cameron and
    Sbierski, arXiv:2609.05167, which names Reissner-Nordstrom-Vaidya); L^1 is the regularity a linear transport
    equation needs, so the remaining hypothesis sits at the sharp borderline of extendibility (argued).
---
## formal
Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) whose derived metric, in background labels $(v, r, x, y)$ with $r > 0$ (a reading, Fact \claimref{synthesis.imported-gtg-dictionary}), is
\[
g = f\,dv^{2} - 2\,dv\,dr - r^{2}q\,(dx^{2} + dy^{2}), \qquad f(v, r) = 1 - \frac{2m(v)}{r} + \frac{e^{2}}{r^{2}} - \frac{\Lambda r^{2}}{3}, \qquad q = \frac{4}{(1 + x^{2} + y^{2})^{2}}
\]
(signature $(1,3)$; the charged Vaidya field with ingoing null dust, Maxwell charge $e$ and cosmological constant $\Lambda$). Suppose $m \in C^{2}[v_{0}, \infty)$, $m' \ge 0$, $m(v) \to m_{\infty}$ with $\int^{\infty}(m_{\infty} - m)\,dv < \infty$, and that $f_{\infty} := f|_{m = m_{\infty}}$ has a simple root $r_{-} > 0$ with $f_{\infty} < 0$ on $(r_{-}, r_{+})$, $r_{+}$ its next root; put $\kappa_{-} := -\tfrac12 f_{\infty}'(r_{-}) > 0$. Suppose further that for every $v \ge v_{0}$ the function $f(v, \cdot)$ has simple roots $r_{-}(v) < r_{+}(v)$ with $f(v, \cdot) < 0$ between them and $r_{\pm}(v) \to r_{\pm}$ (automatic for $\Lambda = 0$ and $m(v_{0}) > |e|$, not in general for $\Lambda \neq 0$); region II is $\{r_{-}(v) < r < r_{+}(v)\}$. Let $\gamma$ be an outgoing radial null free-fall worldline (a radial null geodesic of $g$ with $dr/dv = f/2$) starting in region II, with affine parameter $s$. Then:
\begin{enumerate}
\item \emph{(Field strength.)} In the store's convention ($\Ric = \Lambda g$ for de Sitter) the Schouten map is
\[
\Sch = \frac{\Lambda}{6}\,g - \frac{m'}{r^{2}}\,dv \otimes dv + \frac{e^{2}}{2r^{4}}\,(-h_{2} + h_{S}),\qquad R = 4\Lambda,
\]
with $h_{2}$ and $h_{S}$ the $(v, r)$ and sphere blocks of $g$; the dust part is rank-one null along $dv$, with the focusing sign $-m'/r^{2} \le 0$.
\item \emph{(The crossing hypotheses on the approach side.)} Along $\gamma$, $r(v)$ decreases to $r_{-}$ and $\int^{\infty}(r - r_{-})\,dv < \infty$; $\gamma' = w\,(\partial_{v} + \tfrac12 f\,\partial_{r})$ with $(\log w)' = -\tfrac12\partial_{r}f$ along $\gamma$, so $w = C e^{\kappa_{-}v}(1 + o(1))$ for a constant $C > 0$, and $\gamma$ reaches $v = \infty$, the Cauchy horizon, at a finite affine parameter $s_{c}$, with $s_{c} - s = e^{-\kappa_{-}v}(1 + o(1))/(\kappa_{-}C)$. The covector $n := dv/w$ is $D$-parallel and null along $\gamma$ with $\nu = n(\gamma') = 1$, and
\[
\Sch(\gamma', \cdot) = S\,\nu\,n + R, \qquad S = -\frac{m'}{r^{2}}\,w^{2} \le 0, \qquad R = \Bigl(\frac{\Lambda}{6} - \frac{e^{2}}{2r^{4}}\Bigr)\gamma'^{\flat},
\]
where $\gamma'^{\flat} = g(\gamma', \cdot)$ is $D$-parallel, so $R$ has bounded components in a $D$-parallel frame. The Tipler-type integral is finite: $\int_{s_{0}}^{s_{c}}(s_{c} - s)|S|\,ds$ is bounded above and below by positive multiples of the accreted mass $m_{\infty} - m(v_{0})$.
\item \emph{(The threshold.)} $\int_{s_{0}}^{s_{c}}|S|\,ds < \infty$ if and only if the blue-shifted flux $F := \int_{v_{0}}^{\infty} m'(v)\,e^{\kappa_{-}v}\,dv$ is finite. Hence, by Proposition \claimref{synthesis.tractor-transport-weak-null-crossing}: if $F < \infty$ the tractor transport coefficient $A = E_{\gamma'} + N_{\Sch(\gamma', \cdot)}$ is integrable up to $s_{c}$ and every parallel tractor has a limit at the Cauchy horizon; if $F = \infty$, in the splitting of $g$ a parallel tractor has bounded components up to $s_{c}$ only if $\sigma(s_{c}) = 0$ and $\ip{n}{\mu(s_{c})} = 0$, the divergence sitting in the $\mathfrak g_{1}$ slot along $n$. Case (c) of Proposition \claimref{synthesis.crossing-transport-tipler-threshold-sharp} (Tipler-strong) never occurs in this class. If the field is continued across the Cauchy horizon with continuous derived metric, $D$-transport continuous across and no surface layer, transport across is unique when $F < \infty$ and defined exactly modulo $\exp(\R N_{n})$ when $F = \infty$.
\item \emph{(Tails.)} If $m' = \mu e^{-2\alpha v}(1 + o(1))$ with $\mu, \alpha > 0$, then $F < \infty$ exactly when $\beta := \alpha/\kappa_{-} > \tfrac12$, and $|S|$ is bounded above and below by multiples of $(s_{c} - s)^{2\beta - 2}$, the power profile of Proposition \claimref{synthesis.crossing-transport-tipler-threshold-sharp}(4) with the same $\beta$. If $m' = \mu v^{-p}(1 + o(1))$ with $p > 2$, then $F = \infty$ and $|S|$ is comparable to $(s_{c} - s)^{-2}(\log\frac{1}{s_{c} - s})^{-p}$, the logarithmic profile with $q = p > 1$: case (b), transport defined modulo one nilpotent direction, divergence in the bottom slot.
\end{enumerate}

## technical
The open problem asks whether the tractor transport of the completion survives the crossing of a perturbed Cauchy horizon, and the store's crossing theorem answers it for a curvature class whose realisation at a black-hole Cauchy horizon was only argued from the literature. This result verifies the hypotheses on an exact black-hole interior: the charged Vaidya gravitational field (Einstein-Maxwell with an ingoing null dust, with or without a cosmological constant), whose mass function $m(v)$ increases to a limit as radiation falls in. The Schouten tensor is computed exactly: its dust part is $-(m'/r^{2})\,dv\otimes dv$, rank-one null with the focusing sign, and the Maxwell and $\Lambda$ parts act on an outgoing radial null tangent as a bounded multiple of the tangent's own parallel covector. Along every outgoing radial null free-fall worldline in region II the radius decreases to the inner root $r_{-}$, and the blue-shift factor $w = dv/ds$ grows like $e^{\kappa_{-}v}$, $\kappa_{-}$ the inner surface gravity, so the worldline reaches the Cauchy horizon at finite affine parameter; the parallel null conormal is $dv/w$. The two integrals of the crossing theorem then become physical: the Tipler-type integral is comparable to the total accreted mass, always finite, and the $L^{1}$ norm of the singular coefficient is comparable to the blue-shifted flux $\int m'\,e^{\kappa_{-}v}\,dv$. So the transport reaches the horizon with a unique limit exactly when the crossing observer absorbs a finite blue-shifted dose; otherwise it diverges in the nilpotent slot along the conormal, and is defined modulo $\exp(\R N_{n})$ once the field is continued across. Inverse-power (Price-type) tails are always in the divergent case; exponential tails, as in the de Sitter case, give uniqueness exactly for $\beta = \alpha/\kappa_{-} > \tfrac12$, the same threshold the literature finds for the $H^{1}$ form of strong cosmic censorship. The model has no outgoing flux, so it tests the blue-shift instability and not mass inflation, and the continuation across the horizon is not constructed. The exact checks compute the curvature from second-order jets at rational points, the geodesic and parallel-transport identities along the outgoing ray, the inner surface gravity on two rational examples, and the exponent bookkeeping of the exponential tails.

## lay
Inside a charged black hole there is an inner horizon. Radiation falling into the hole piles up there, because an observer crossing it sees all the late radiation squeezed into an instant and strongly blue-shifted. This result takes the standard exact model of that situation, a charged hole fed by a stream of infalling radiation, and checks one by one the conditions under which the series' theorem on carrying structure across such a horizon applies. All the conditions on the approach hold. The theorem's two key quantities turn out to be governed by simple physical totals: one by the total mass that falls in, which is finite here, and the other is the total blue-shifted energy the crossing observer receives. When that energy is finite the series' transport goes through cleanly; when it is infinite, as it is for the slowly fading radiation expected around real holes, the transport still survives but loses one number, in exactly the place the theory predicted. The model leaves out the outgoing radiation that makes real inner horizons more violent, so it is a first realistic test rather than the final answer.

## one-liner
On the charged Vaidya gravitational field with an ingoing null-dust tail the weak null crossing hypotheses hold on the approach to the Cauchy horizon, the Tipler-type integral is comparable to the accreted mass, and tractor transport has a unique limit exactly when the blue-shifted flux $\int m'\,e^{\kappa_{-}v}\,dv$ is finite: inverse-power tails diverge in the nilpotent slot, exponential tails are unique exactly for $\beta > \tfrac12$.
