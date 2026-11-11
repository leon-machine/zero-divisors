---
id: synthesis.hawking-page-test-on-schwarzschild-anti-de-sitter
kind: claim
version: 1
title: 'Hawking-Page on Schwarzschild-anti-de Sitter: reproduced under (Z), lost under Wald'
status: proved
region: synthesis
subject: entropy
tags: [hawking-temperature, horizons, cosmological-constant, recovers-known-physics]
proposed_by:
  kind: ai
  session: 2026-11-11-hawking-page
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: session 2026-11-11-hawking-page
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.sds-clausius-fixes-area-constant@5
  - synthesis.quarter-from-temperature@1
  - synthesis.euler-term-horizon-entropy-shift@5
  - synthesis.imported-wald-noether-charge-entropy@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_chart_and_first_law
- kind: check
  ref: check.py::check_branches_and_free_energy
- kind: check
  ref: check.py::check_dimension_d
- kind: check
  ref: check.py::check_wald_constant_removes_the_transition
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.sds-clausius-fixes-area-constant
  - synthesis.euler-term-horizon-entropy-shift
extraction:
  note: >-
    A test asked for by Leon on 2026-11-11, after a comparison of the store with the preprint "The Hawking-Page
    transition at weak coupling" (hexagon:2611.00175), which quotes T_min = sqrt(2)/(pi R) and T_HP = 3/(2 pi R)
    for the five-dimensional case. The store had no result on a black hole with Lambda < 0. This result carries
    the hypotheses of synthesis.sds-clausius-fixes-area-constant, (T), (Cl) and (Z), to the Schwarzschild-anti-de
    Sitter field and adds Hawking and Page's free-energy criterion (FE) as a labelled hypothesis: it is not a
    stored premise, and the series' frozen point has Lambda > 0, so the whole result is a counterfactual test of
    the horizon thermodynamics, not a statement about the series' universe. What the test can and cannot show:
    any framework with temperature kappa/2 pi and a Clausius relation gets the quarter and the two branches, so
    reproducing them is not evidence for the series' count of boundary modes (the density of counted units is
    not tested, as with the Kerr count). What it does discriminate is the additive constant: the transition at
    r_h = ell needs the constant to be zero, the normalisation (Z) the store already uses, and it is absent
    under the Wald entropy of the MacDowell-Mansouri action as written, whose Euler term adds +pi ell^2 for
    Lambda < 0. For Lambda > 0 the stored argument against the Wald constant is nonnegativity; for Lambda < 0
    the constant is positive, nonnegativity is silent, and the free-energy comparison is the test. Not done
    here: (T) for Lambda < 0 from a regularity or null-energy premise (it is assumed, as (T) is in the
    Schwarzschild-de Sitter result); a gauge of the field real on the whole exterior (the Painleve-Gullstrand
    gauge as stored is real only out to r_*); the free energy of the horizonless field's own thermal content,
    set to zero in (FE); the identification of the MacDowell-Mansouri on-shell Euclidean action with the Weyl
    square, used only as an orientation remark in the proof.
---

## formal
Let $\Lambda = -3/\ell^{2} < 0$, in units $\hbar = c = G = 1$, and for $M > 0$ consider the Schwarzschild-anti-de Sitter gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) in the Painlev\'e-Gullstrand gauge $\hb = 1 - \beta P$, $\beta^{2} = 2M/r - r^{2}/\ell^{2}$, whose static Killing field $K = \hb^{-1}(e_t)$ has $Q(K) = f(r) = 1 - 2M/r + r^{2}/\ell^{2}$. Write $r_{h}$ for a positive zero of $f$ and $x = r_{h}/\ell$. Suppose
\begin{enumerate}
\item[(T)] the horizon is at the temperature $T = f'(r_{h})/4\pi$ of the flow of $K$, the value that (R) gives at $\Lambda = 0$ (Theorem \claimref{synthesis.quarter-from-temperature}); for $\Lambda < 0$ no stored premise supplies it and it is assumed, as (T) is in Theorem \claimref{synthesis.sds-clausius-fixes-area-constant};
\item[(Cl)] the horizon obeys the Clausius relation $dM = T\,dS$ along the family at fixed $\Lambda$;
\item[(FE)] (Hawking and Page's criterion, not a stored premise) at a given temperature the field with the smaller free energy $F = M - TS$ is the equilibrium one, the horizonless field ($M = 0$, no horizon locus) being taken with $F = 0$.
\end{enumerate}
Then:
\begin{enumerate}
\item[(o)] \emph{(The chart.)} $\beta^{2} \ge 0$ exactly on $0 < r \le r_{*}$, with $r_{*}^{3} = 2M\ell^{2}$, where $Q(K) = 1$; so the gauge as stored does not cover $r > r_{*}$. $f$ is increasing with exactly one positive zero, and $r_{h} < \min(2M, r_{*})$: the horizon locus lies inside the chart, and every clause below uses only the horizon locus.
\item[(i)] \emph{(The quarter.)} $M = \tfrac12 r_{h}(1 + x^{2})$ and $4\pi T = (1 + 3x^{2})/r_{h}$. Under (T) and (Cl), $S = \pi r_{h}^{2} + c$ with $c$ independent of $M$, and (Z), $S \to 0$ as $M \to 0$, holds if and only if $c = 0$.
\item[(ii)] \emph{(The branches.)} $T \ge T_{\min} = \sqrt{3}/(2\pi\ell)$, with equality only at $x^{2} = \tfrac13$. For $T < T_{\min}$ there is no black hole; for $T > T_{\min}$ there are exactly two, a small one ($x^{2} < \tfrac13$, $dM/dT < 0$) and a large one ($x^{2} > \tfrac13$, $dM/dT > 0$).
\item[(iii)] \emph{(The transition under (Z).)} With $c = 0$, $F = \tfrac14 r_{h}(1 - x^{2})$: positive on the whole small branch, and on the large branch negative exactly when $r_{h} > \ell$. Under (FE) the horizonless field is the equilibrium one for $T < T_{\mathrm{HP}}$ and the large black hole for $T > T_{\mathrm{HP}}$, with
\[
T_{\mathrm{HP}} = \frac{1}{\pi\ell}, \qquad \frac{T_{\mathrm{HP}}}{T_{\min}} = \frac{2}{\sqrt{3}},
\]
the mass jumping from $0$ to $\ell$ and the entropy from $0$ to $\pi\ell^{2}$ (so $\Delta M = T_{\mathrm{HP}}\,\Delta S$). This is Hawking and Page's transition.
\item[(iv)] \emph{(Dimension $d \ge 4$.)} For the field with $f = 1 - \mu/r^{d-3} + r^{2}/\ell^{2}$ on flat $\R^{1,d-1}$, assume (T), the entropy $S = \tfrac14\Omega_{d-2}r_{h}^{d-2}$ (a quarter of the area of the cross-section, $\Omega_{d-2}$ the area of the unit sphere) and let $M$ be the Clausius energy, $dM = T\,dS$ with $M = 0$ at $r_{h} = 0$. Then $4\pi T = \bigl((d-3) + (d-1)x^{2}\bigr)/r_{h}$, $16\pi M = (d-2)\Omega_{d-2}r_{h}^{d-3}(1 + x^{2})$ and
\[
F = \frac{\Omega_{d-2}\,r_{h}^{d-3}}{16\pi}\,(1 - x^{2}), \qquad T_{\min} = \frac{\sqrt{(d-1)(d-3)}}{2\pi\ell}, \qquad T_{\mathrm{HP}} = \frac{d-2}{2\pi\ell},
\]
the transition again at $r_{h} = \ell$. For $d = 5$: $T_{\min} = \sqrt{2}/(\pi\ell)$ and $T_{\mathrm{HP}} = 3/(2\pi\ell)$.
\item[(v)] \emph{(Under the Wald constant.)} Assume in place of (Z) the hypothesis (W) of Theorem \claimref{synthesis.euler-term-horizon-entropy-shift}(ii), the Wald entropy of the MacDowell-Mansouri action as written (Fact \claimref{synthesis.imported-wald-noether-charge-entropy}). Then $c = -3\pi\chi/2\Lambda = +\pi\ell^{2}$ ($\chi = 2$), $S \to \pi\ell^{2}$ as $M \to 0$, and
\[
F_{W} = F - \pi\ell^{2}\,T = -\,\frac{\ell\,(1 + x^{2})^{2}}{4x} < 0
\]
for every black hole of the family, on both branches. Under (FE) a black hole is then preferred to the horizonless field at every temperature at which one exists, $T \ge T_{\min}$, and nothing happens at $T = 1/(\pi\ell)$. Since $c > 0$, nonnegativity of the entropy does not exclude this constant for $\Lambda < 0$ (it does for $\Lambda > 0$, Theorem \claimref{synthesis.sds-clausius-fixes-area-constant}(v)); (Z) does. So for $\Lambda < 0$ Hawking and Page's transition is reproduced under (Z) and not under (W).
\end{enumerate}

## technical
The hypotheses of the stored Schwarzschild-de Sitter result, horizon temperature equal to surface gravity over $2\pi$ for the flow of the gauge's Killing field (T) and Hawking's Clausius relation along the family (Cl), are carried to $\Lambda < 0$, where the store had no black-hole result. The Painlev\'e-Gullstrand gauge with flat slices is real only out to the radius $r_{*}$ at which free fall from rest turns round, $r_{*}^{3} = 2M\ell^{2}$; the horizon locus is always inside it, which is all the result uses. (T) and (Cl) give a quarter of the area plus a constant, as for $\Lambda > 0$. The temperature has a minimum at $r_{h} = \ell/\sqrt{3}$, with a small branch of negative heat capacity and a large branch of positive heat capacity above it.

The additive constant is what the test discriminates. With the store's normalisation (Z), zero entropy at zero mass, the free energy $M - TS$ is $r_{h}(1 - r_{h}^{2}/\ell^{2})/4$, it changes sign at $r_{h} = \ell$, and with Hawking and Page's comparison of free energies (a hypothesis here, labelled (FE)) the transition sits at $T = 1/(\pi\ell)$; in five dimensions the same computation gives $3/(2\pi\ell)$ and $T_{\min} = \sqrt{2}/(\pi\ell)$, the standard values. With the Wald entropy of the series' action as written, the Euler term adds $+\pi\ell^{2}$, the free energy of every black hole is negative, and the transition at $r_{h} = \ell$ disappears. For $\Lambda > 0$ that constant was negative and excluded by nonnegativity; for $\Lambda < 0$ it is positive and only (Z), or the transition itself, speaks against it.

Scope: (T) is assumed, not derived, for $\Lambda < 0$; (FE) is not a stored premise; the series' frozen point has $\Lambda > 0$, so this is a test of the horizon thermodynamics on a field the series does not say is realised. The quarter follows from (T) and (Cl) alone, so the test does not reach the series' density of counted boundary modes.

## lay
In a universe with a negative cosmological constant, a famous calculation by Hawking and Page shows that hot radiation suddenly prefers to become a large black hole once the temperature passes a definite value. This result checks whether the framework's rules for horizon temperature and entropy, which were set up for our universe and for ordinary black holes, give the same answer when applied there. Assuming the usual temperature of a horizon, the ordinary law linking heat and entropy, and Hawking and Page's rule that the state of lower free energy wins, they do, in four dimensions and in five: black holes exist only above a minimum temperature, come in a small unstable kind and a large stable kind, and the large kind takes over at exactly the standard temperature. The check is not strong evidence for the framework, because any theory with the usual temperature and heat law passes it. What it does decide is a detail the framework had already had to settle: its own form of the gravitational action, read literally, adds a fixed amount of entropy to every black hole, and with that extra amount the transition would not occur where Hawking and Page found it. The framework's choice to leave that amount out is the one that gives the standard result.

## one-liner
For the Schwarzschild-anti-de Sitter field on flat spacetime, under (T) and Clausius $S = \pi r_{h}^{2} + c$; with (Z) the free energy is $r_{h}(1 - r_{h}^{2}/\ell^{2})/4$ and Hawking and Page's criterion gives $T_{\min} = \sqrt{3}/(2\pi\ell)$, $T_{\mathrm{HP}} = 1/(\pi\ell)$ ($3/(2\pi\ell)$ in five dimensions), while the Wald constant $+\pi\ell^{2}$ of the series' action makes every black hole's free energy negative and removes the transition.
