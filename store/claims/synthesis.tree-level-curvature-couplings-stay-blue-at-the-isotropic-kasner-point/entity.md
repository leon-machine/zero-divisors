---
id: synthesis.tree-level-curvature-couplings-stay-blue-at-the-isotropic-kasner-point
kind: claim
version: 4
title: 'Tree-level curvature couplings stay blue at the isotropic Kasner point'
status: proved
region: synthesis
subject: dark-energy
tags: [kasner, no-go, confronted-with-data, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-01-xi-ledger
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
- name: Claude Opus 5.5
  role: GA rewrite (Kasner field strength in the store sign)
  version: 4
  source: maintainer pass 2026-11-07 (consistency)
review: draft
derivations:
- name: main
  uses:
  - mass.imported-thomas-operator@3
  - mass.mass-weight-dictionary@4
  - mass.weight-polynomial-two-series@6
  - mass.imported-unitary-representations-de-sitter-group@5
  - synthesis.parallel-frozen-point-on-matter-regions-is-the-field-space-premise@3
  - interior.kasner-form-interior@6
  - synthesis.bkl-bounce-invariant-holonomy-and-bound@2
  - synthesis.scalar-kasner-wall-is-reduced-five-dimensional-vacuum-wall@2
  - synthesis.kasner-hidden-scale-coupled-scalars-stay-blue@4
  - synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling@3
  - synthesis.imported-planck-2018-lcdm-parameters@3
  - synthesis.imported-einstein-cartan-matter-coupling@1
  - synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus@5
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_dictionary_extensions_off_the_einstein_region
- kind: check
  ref: check.py::check_curvature_coupling_acts_only_at_the_isotropic_disk_point
- kind: check
  ref: check.py::check_listed_couplings_are_blue_at_the_isotropic_point
- kind: check
  ref: check.py::check_hidden_scale_weight_bound
- kind: check
  ref: check.py::check_window_needs_weight_outside_unitary_range
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling
  - standard-model.dating-descent
extraction:
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: mass.imported-thomas-operator repinned 2 -> 3 after reviewing its correction of the consistency remark (at w = 1 on the constant density the display returns (n, 0, J), so (1/n) D sigma = (1, 0, J/4) = (1, 0, Lambda/6) in dimension four); the operator is unchanged; the use here holds as cited. Pin review: mass.imported-unitary-representations-de-sitter-group repinned 4 -> 5 after reviewing its B6 restatement (the sentence giving the Casimir the same normalisation with no shift moved out to the stated, unproved hypothesis of synthesis.operator-join-casimir-shifts (iii); the classification, the two series and the mass formula are unchanged); the use here holds as cited.'
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Line element to GA in the proof of (iii): the Kasner approach is the synchronous field hb^{-1}(e_i) = T^{P_i} e_i with its derived metric as reading, and the field strength is stated as the store-sign curvature operator, calR(e_0 e_i) = P_i(P_i - 1) T^-2 e_0 e_i and calR(e_i e_j) = P_i P_j T^-2 e_i e_j, replacing the hedge up to the store overall sign: these are exactly the store-sign eigenvalues (checked with lib/GA.py for dark-energy.frozen-point-datum-kasner-wall, plane by plane, so in any number of directions), and the scalar 2 sum P(P - 1) + sum_{i != j} P_i P_j follows from them. Statement unchanged.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The de Sitter weight -3/2 +- i nu, a physical number, is written -3/2 +- I_4 nu, and the coupling it gives, 1/4 -+ i nu/6, as 1/4 -+ I_4 nu/6, numbers read in span{1, I_4} (formal and proof); no bare i remains.'
  open_problem: op.descent-state-and-spectrum
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 1 -> 2: a marked note at the end of the formal level cites the premise registered by Leon''s decision of 2026-11-01 for hypothesis (P1), synthesis.pre-descent-contracting-kasner-stage-premise, and its companion (P2), synthesis.pre-descent-state-carried-into-descended-phase-premise, by claimref only; by the same decision this result has no uses or assumes edge to them, and its statement is unchanged.'
  note: >-
    Answers, at tree level, the coupling part of the recorded premise question whether the series fixes a
    curvature coupling. The whole result concerns a metric Kasner approach before the descent, the stage that
    hypothesis (P1) (a contracting metric stage before the descent) supplies; whether such a stage exists, and
    why modes leave the Hubble length only on it, is treated in the result (synthesis.kasner-exit-needs-a-contracting-metric-stage-and-a-wall-matching). Comparison list: the couplings a
    stored action or a reading of the dictionary fixes for a scalar, each with its selecting rule, and the
    Kasner points the stored wall results fix, written down before the values were compared with the window.
    One value was seen before the list was written: during orientation the second reading's principal-series
    family xi = m^2/(12 H^2) was noted to reach the window near nu = 4 (m about 4.3 H); that family was then
    entered as fixed by a field's mass, not as a candidate, and no stored scalar has such a mass. The list
    evaluated is the union of two independent lists of the same rules: 0, 1/8, 3/20, 1/6, 3/16, 1/5, 1/4,
    1/3, 3/8, 1/2, -1/6, -1/3 (twelve values; 1/8, 3/20, 3/8 and 3/16 are five-dimensional readings, 1/5 the
    six-dimensional Yamabe value, -1/6 and -1/3 the frozen point's own weight w = 1, which is not a propagating
    spectator), largest 1/2. The Lichnerowicz coefficient 1/4 of the squared Dirac operator is not a scalar
    coupling (massless spinors are conformally invariant, and fermions fall under the shot-noise bound). The
    dictionary is stored on Einstein regions only, and which connection builds the Thomas operator off them is
    not recorded; the result is stated for each reading. The first and third readings keep the frozen point in
    its stored form, as the field-space premise synthesis.field-space-premise-parallel-frozen-point requires
    on matter regions (synthesis.parallel-frozen-point-on-matter-regions-is-the-field-space-premise); the
    second pairs with a tractor that is not the frozen point off the Einstein region, so it needs that premise
    dropped. Every massive scalar of the series (the rung field's modes, the measured Higgs boson) has
    m much larger than H, so it lies on the principal series: the first reading gives it no real coupling and
    the second a coupling of order m^2/H^2; for these fields the exclusion rests on the stored actions and the
    third reading. Tree level: a coupling of an interacting scalar runs, and the stored zero is not stable
    under renormalisation. For the Wilson-line component A_y the stored action has no curvature term; a local
    A_y^2 R is not gauge invariant, but a periodic R V(W) of the holonomy W is, and the store does not fix it;
    with A_y's weight lambda = -1, and the curvature term taking the same power of the hidden scale as the
    kinetic term, the window would need such a coupling in [0.8559, 0.8815] (computed after the comparison;
    recorded, not a candidate). Not treated: fields the store does not hold, loop-level couplings, the
    five-dimensional stiff segment's interior and the anisotropic disk points (whose exponents no stored result
    fixes), and the conversion into the curvature perturbation. Transport-convenient: the readings are
    statements about the Cl(2,4) tractor pairing; the tilt computation is standard and transport-absent.
---

## formal
Assume hypothesis (P1): before the descent a gravitational field on flat spacetime approaches a wall with the synchronous diagonal derived metric $dT^{2} - \sum_{a}T^{2P_{a}}(dx^{a})^{2}$, $\sum_{a}P_{a} = 1$, as in Theorem \claimref{synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling}. Write a scalar's tree-level field equation as $(\Box + \xi R + \mu)\sigma = 0$ in the sign of the dictionary (de Sitter has $R = 4\Lambda > 0$; $\xi = \tfrac16$ is conformal). Let $D$ be the Thomas operator of Fact \claimref{mass.imported-thomas-operator} on a density of weight $w$ in dimension $n$, $J = R/(2(n - 1))$, and $I = \nInf + \rho\,\nO$ a tractor in the physical scale with $\rho$ independent of $J$.
\begin{enumerate}
\item[(i)] \emph{(The dictionary off the Einstein region.)} $I \cdot D\sigma = 0$ reads $(\Box + m^{2})\sigma = 0$ with $m^{2} = -wJ - \rho w(n + 2w - 2)$. Hence, in $n = 4$: with the frozen point in its stored form, $\rho = \Lambda/6$ (Theorem \claimref{synthesis.parallel-frozen-point-on-matter-regions-is-the-field-space-premise}), $\xi = -w/6$ and $\mu = -w(w + 1)\Lambda/3$ (first reading); with the derived metric's own scale tractor, $\rho = J/4$, $\xi = -w(w + 3)/12$ and $\mu = 0$ (second reading, not the frozen point off the Einstein region); with the Thomas operator of the connection whose special-conformal slot is $\rho\,\mathrm{id}$, $J \to 4\rho$, $\xi = 0$ and $\mu = -w(w + 3)\Lambda/3$ (third reading). On Einstein regions ($R = 4\Lambda$) the three agree with Theorem \claimref{mass.mass-weight-dictionary}; off them they differ. In every dimension the conformal weight $w = 1 - n/2$ gives the Yamabe value $\xi = (n - 2)/(4(n - 1))$ in the first two, with $\mu = 0$ in the first.
\item[(ii)] \emph{(Values.)} On the real weights of the unitary range $w \in [-3, 0]$ (Corollary \claimref{mass.weight-polynomial-two-series}) the first reading gives $\xi \in [0, \tfrac12]$, the second $\xi \in [0, \tfrac{3}{16}]$, the third $0$. On the principal series $w = -\tfrac32 \pm I_4\nu$ (numbers are read in $\mathrm{span}\{1, I_4\}$) the first gives $\xi = \tfrac14 \mp I_4\nu/6$, not real for $\nu \neq 0$, while the dictionary stays real on Einstein regions. The stored actions give $\xi = 0$ at tree level: the minimal coupling of Fact \claimref{synthesis.imported-einstein-cartan-matter-coupling}, the rung field's D-term action of Theorem \claimref{synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus}, the wall's massless scalar of Theorem \claimref{synthesis.scalar-kasner-wall-is-reduced-five-dimensional-vacuum-wall}, and the Wilson-line component $A_{y}$ of Theorem \claimref{synthesis.kasner-hidden-scale-coupled-scalars-stay-blue}, whose stored action has no curvature term (a local $A_{y}^{2}R$ is not gauge invariant; a periodic $R\,V(W)$ of the holonomy $W$ is gauge invariant and not fixed by the store).
\item[(iii)] \emph{(Where a coupling acts.)} $R = 0$ on the four-dimensional vacuum circle (the Schwarzschild interior of Lemma \claimref{interior.kasner-form-interior} and the points of Theorem \claimref{synthesis.bkl-bounce-invariant-holonomy-and-bound}), $R_{5} = 0$ at the five-dimensional vacuum ends $(0, 0, 0, 1)$ and $(\tfrac12, \tfrac12, \tfrac12, -\tfrac12)$, and the induced four-dimensional metrics there have $R = 0$. At the isotropic disk point $(\tfrac13, \tfrac13, \tfrac13)$, the Einstein-frame reduction of both ends, $RT^{2} = -\tfrac23$, of the sign opposite to de Sitter. So among the Kasner points the store fixes, a curvature coupling acts only there (every disk point with $c^{2} \neq 0$ has $R \neq 0$, but no stored result fixes the anisotropic ones).
\item[(iv)] \emph{(Confrontation.)} At the isotropic point a scalar with no hidden-scale weight in the Einstein frame has Bessel order $\nu^{2} = \tfrac32\xi$ and index $3 - 2\nu$. A scalar whose four-dimensional action carries $b^{\lambda}$ has Einstein-frame weight $b^{\lambda - 1}$, and with the curvature term carrying the same power of $b$, $\nu^{2} = \tfrac14(\lambda - 1)^{2} + \tfrac32\xi$. Every real tree-level coupling in (ii) is at most $\tfrac12$, so the index is at least $3 - \sqrt{3}$ for $\lambda = 1$ and at least $3 - \sqrt{7}$, which is positive, for the stored weights $|\lambda - 1| \le 2$. The measured $n_{s} - 1 = -0.0351 \pm 0.0042$ (Fact \claimref{synthesis.imported-planck-2018-lcdm-parameters}) needs, within three standard deviations and with $\lambda = 1$, $\xi \in [1.522584375, 1.548079215]$, which contains no listed value.
\item[(v)] \emph{(The window read back.)} In the first reading the window needs a real weight $w = -6\xi \in [-9.28847529, -9.13550625]$, where $-w(w + 3) < 0$: outside both series of Fact \claimref{mass.imported-unitary-representations-de-sitter-group}. The third cannot reach it. The second reaches it only on the principal series with $m^{2}/H^{2} = 12\xi$ between $18.27$ and $18.58$, a scalar mass that no stored field has.
\end{enumerate}
So, at tree level and on a metric Kasner approach before the descent, no scalar whose coupling a stored action or a reading of the dictionary with the frozen point in its stored form fixes reaches the measured tilt at the Kasner points the store fixes; a coupling in the window would be a new premise (a loop-level or unfixed coupling, a field outside these, or the own-scale reading with the field-space premise dropped and a scalar of that mass). Not covered: loop-level couplings, fields the store does not hold, the five-dimensional stiff segment's interior, the anisotropic disk points, and the conversion into the curvature perturbation.

\emph{Note (premises, 2026-11-01).} Hypothesis (P1) is now registered as Premise \claimref{synthesis.pre-descent-contracting-kasner-stage-premise}, with its companion (P2), the rule carrying the stage's state into the descended phase, as Premise \claimref{synthesis.pre-descent-state-carried-into-descended-phase-premise}. This result states (P1) as its hypothesis and has no assumes edge to it; granting both premises, the conclusion above stands, so they do not supply the tilt.

## technical
A stored result found that on a Kasner approach a scalar coupled to curvature matches the measured tilt only for a coupling near $1.53$ fitted to it, and left open whether the series fixes that coupling. Such an approach would have to precede the descent, a stage the series now takes as hypothesis (P1). The series' rule for how a scalar feels the geometry is its mass-weight dictionary, a pairing of the field's Thomas tractor with the frozen point, proved on vacuum Einstein regions. Away from them the pairing splits into a curvature coupling and a constant mass, and the split depends on the connection that builds the Thomas operator, which the store does not record. With the transport's operator and the frozen point in its stored form the coupling is $-w/6$; with the field-space connection it is zero; pairing with the metric's own scale tractor instead, which is not the frozen point there, gives $-w(w+3)/12$. For the real weights of the unitary range these lie between $0$ and $\tfrac12$; the heavy fields of the series, the rung field's modes among them, sit on the principal series, where the first reading is complex and the second enormous, so for them the exclusion rests on the stored actions, which have no curvature term at tree level, and on the field-space reading. At the Kasner points the store fixes, the curvature vanishes on the vacuum circle, at the five-dimensional vacuum ends and in their induced four-metrics, so a coupling acts only at the isotropic point reached by a massless scalar. There these couplings give an index of at least $3 - \sqrt{3}$, or $3 - \sqrt{7}$ once the stored hidden-scale weights are included: blue in both cases. Read back, the fitted coupling needs a weight below $-9$, a tachyon in the de Sitter stage, outside the unitary fields the dictionary uses; only the reading that drops the field-space premise reaches it, and then with a scalar heavier than four times the Hubble rate of $\Lambda$ and lighter than five, which no stored field is. Loop corrections are not treated.

## lay
In standard cosmology the slight tilt of the early universe's ripples comes from a stage of rapid expansion, which this framework lacks. If the framework allowed a squeezing stage before its origin, an earlier result found that a field feeling the curvature of space strongly enough could give the right tilt there, but only if the strength of that coupling were set by hand. This result asks whether the framework itself sets that strength, in its basic equations before quantum corrections. It collects the couplings the framework's own rules give its fields, reading its rule for masses in each way it allows. All are much weaker than needed, so the ripples come out tilted the wrong way. The value that would match corresponds to a field that would be unstable in today's accelerating universe, or to a field of a particular tiny mass that the framework does not contain. So the framework does not supply the needed coupling; adding one would be a new assumption.

## one-liner
At tree level and on a metric Kasner approach before the descent (hypothesis (P1)), the stored actions give scalars $\xi = 0$ and the mass-weight dictionary off the Einstein region gives $-w/6$ (the transport's Thomas operator with the frozen point in its stored form) or $0$ (the field-space connection), real values in $[0, \tfrac12]$ on the unitary real weights; among the stored Kasner points a coupling acts only at the isotropic disk point, where these give index at least $3 - \sqrt{3}$ with no hidden-scale weight and at least $3 - \sqrt{7}$ with the stored weights; the window $\xi \in [1.522584375, 1.548079215]$ needs a real weight below $-9$, outside both unitary series, and the own-scale reading $-w(w + 3)/12$, which drops the field-space premise, reaches it only for a principal-series scalar with $m^{2}/H^{2}$ between $18.27$ and $18.58$, which no stored field has.
