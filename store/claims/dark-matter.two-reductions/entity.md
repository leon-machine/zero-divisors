---
id: dark-matter.two-reductions
kind: claim
version: 7
title: The two reductions
status: proved
region: dark-matter
subject: dark-matter
tags: [counting-rules, cosmological-constant]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14, deposited version
review: typed
derivations:
- name: main
  uses:
  - dark-matter.imported-induced-equations-hypersurface@3
  assumes:
  - dark-matter.d-democracy-total-mass@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_wallis_factors_and_zero_mode_thickness
- kind: check
  ref: check.py::check_warped_field_volume_and_curvature_weights
- kind: check
  ref: check.py::check_local_projection_thickness
- kind: check
  ref: check.py::check_sheet_spacing_and_totals_under_democracy
locators:
  paper: T14
  number: Prop 7.22
  label: prop:reduction
  line: 1070
extraction:
  maintainer_pass_2:
    by: maintainer-2026-10-24
    date: '2026-10-24'
    note: 'Gauge Theory Gravity wording pass at Leon''s request (2026-10-24): curved-spacetime and conformally-flat wording restated in terms of the gravitational field on flat spacetime (a nonvanishing gravitational field; the Weyl part of the field strength vanishes, the conformally flat derived metric kept as a reading; global content read on an atlas of flat charts patched by gauge transformations). Wording only; statements, proofs'' arguments and checks unchanged. Version 6 -> 7. Referee fixes to the GTG wording pass (2026-10-24): ''a gravitational field of nonvanishing field strength'' (gauge-independent) in place of ''a nonvanishing gravitational field''; global content read on several charts of flat spacetime, each with its own gravitational field, glued by displacement and rotation gauge transformations (complexified charts for the half-flat manifold, the conformal compactification for a conformal boundary); ''not carried by the store''s one-chart fields'' in place of ''no single gravitational field carries''; equivalence statements weakened where the old text was weaker; remaining curved-spacetime phrases in lay text restated. Wording only.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: Wallis factors in Q(pi) by two routes, the warped GTG field volume and curvature weights, the local projection rho/2 and thickness (pi/4) l, the sheet spacing (4/3) l and the totals 5, 13/3, 17/3, 5 under D. Version 4 -> 5. Check maintenance: comparisons over zip now also compare lengths, so a length mismatch cannot pass on a shorter prefix; no change to what is claimed. Version 5 -> 6.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: five-dimensional GTG (d-dimensional clause): the warped de Sitter_5 is the derived metric of the field hb^{-1}(e_theta) = l e_theta, hb^{-1}(a_4) = cos theta hb_4^{-1}(a_4) on flat R^{1,4}, the Einstein-Hilbert action int det(hb)^{-1} R; clause (iii) uses the closed four-sphere of radius l, flagged beyond one flat chart. Content unchanged. Fix (referee GR2, 2026-10-23): the background is flat R^{4,1} in the signature (-,+,+,+,+) of eq:warp (in the store sign the derived metric is its negative), at formal, technical and proof prefix.'
  flags:
  - 'beyond one flat chart: the closed four-sphere of radius l carrying the sheet family'
  small_findings_pass:
    by: ai-small-findings-pass
    date: 2026-10-22
    finding: VALUES L7
    open_problem: op.small-findings
    note: 'The levels now say that both reductions need a metric fifth direction, a setting that dark-matter.thickness-not-gravitational-quantity shows short-range tests of Newton''s law exclude; the computation stands as a computation in that setting, kept for comparison with the unit-ball rule.'
  env: proposition
  eqrefs: 3
  typing:
    by: ai-typing-pass
    added:
    - dark-matter.d-democracy-total-mass
    note: 'Added premise D to assumes since the totals are stated under D; the totals also use the mirror
      share one through the section equation for the ratio, which is not a store entity, so no edge was
      added for it. Levels pass: conditions already kept.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-matter.d-democracy-total-mass
    note: The one-liner now names premise D, which the check (W503) found missing.
---

## formal
In the setting of \eqref{eq:warp}, read in five-dimensional Gauge Theory Gravity (the $d$-dimensional clause of Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}): the warped product $\ell^{2}d\theta^{2} + \cos^{2}\theta\,ds_{4}^{2}$ is the derived metric of the gravitational field on flat $\R^{4,1}$, in the signature $(-,+,+,+,+)$ of \eqref{eq:warp} (in the store's sign the derived metric is its negative), with $\hb^{-1}(e_\theta) = \ell\,e_\theta$ and $\hb^{-1}(a) = \cos\theta\,\hb_{4}^{-1}(a)$ on the four-dimensional directions, and the five-dimensional Einstein-Hilbert action is $\int \det(\hb)^{-1}\,\mathcal{R}\,d^{5}x$ (sign as in \eqref{eq:warp}):
\begin{enumerate}
\item[(i)] (Zero mode.) Integrating the five-dimensional Einstein-Hilbert and matter actions over $\theta$, the gravitational term, the bulk dust and the equatorial sheet acquire the factors
\[
\ell\int_{-\pi/2}^{\pi/2}\cos^{2}\theta\,d\theta = \frac{\pi\ell}{2}, \qquad
\ell\int_{-\pi/2}^{\pi/2}\cos^{4}\theta\,d\theta = \frac{3\pi\ell}{8}, \qquad 1,
\]
so $G_{4} = \frac{2G_{5}}{\pi\ell}$. Newton's constant cancels in the ratio, and the five-dimensional tower's effective thickness is
\[
L_{\mathrm{eff}} \;=\; \frac{3\pi}{8}\,\ell \;=\; \frac{V_{4}}{V_{3}}\,\ell .
\]
\item[(ii)] (Local projection.) For dust comoving with the slice, $T_{ab}n^{a}n^{b} = 0$ and $T = -\rho_{5}$, so the bulk term of Fact \claimref{dark-matter.imported-induced-equations-hypersurface} contributes on the slice the energy density
\[
\frac{2\kappa_{5}^{2}}{3}\left(\rho_{5} - \frac{\rho_{5}}{4}\right) \;=\; \frac{\kappa_{5}^{2}\,\rho_{5}}{2} .
\]
With the $G_{4}$ of (i) this is an effective thickness $L_{\mathrm{eff}} = \frac{\pi}{4}\,\ell$.
\item[(iii)] (The sheets.) A comoving family of three-dimensional sheets carrying total mass $M_{\mathrm{tot}}$ over our $\Sph^{4}$ of radius $\ell$, each at the three-dimensional tower's own density $\frac{M_{\mathrm{tot}}}{|\Sph^{3}|\,\ell^{3}}$, has spacing
\[
s \;=\; \frac{|\Sph^{4}|}{|\Sph^{3}|}\,\ell \;=\; \frac{4}{3}\,\ell
\]
along the polar arc.
\end{enumerate}
Consequently, under D: (i) with (iii) gives every share $1$ and the total $5.000$; (ii) with (iii) gives $4.333$; (i) with sheets one radius apart gives $5.667$; (ii) with sheets one radius apart gives $5.000$ again (Table \ref{tab:reductions}). The rule's $L_{\mathrm{eff}} = \ell$ is produced by neither reduction. \emph{Beyond one flat chart.} The closed four-sphere of radius $\ell$ over which the sheet family of (iii) is counted is global and is not carried by a single gravitational field $(\hb, \Omega)$ on flat spacetime; the statements above that hold on the invertible region are in Gauge Theory Gravity, and that four-sphere is read on the manifold assembled from the derived metric's charts.

## technical
The fifth direction of a five-dimensional tower is promoted to a metric direction, writing $\dS_{5}$ of radius $\ell$ as the warped product $ds_{5}^{2} = \ell^{2}d\theta^{2} + \cos^{2}\theta\,ds_{4}^{2}$ with our world at the equator, in five-dimensional Gauge Theory Gravity the derived metric of a gravitational field on flat $\R^{4,1}$, in the signature $(-,+,+,+,+)$ of the warped product, and a four-dimensional Friedmann equation is extracted in two ways. Zero-mode integration over $\theta$ gives the gravitational, bulk and equatorial factors $\pi\ell/2$, $3\pi\ell/8$ and $1$, so $G_{4} = 2G_{5}/(\pi\ell)$ and the effective thickness is $L_{\mathrm{eff}} = \tfrac{3\pi}{8}\ell = \tfrac{V_{4}}{V_{3}}\ell$. Local projection with the imported induced-equation term gives the energy density $\kappa_{5}^{2}\rho_{5}/2$ for comoving dust, an effective thickness $\tfrac{\pi}{4}\ell$. A comoving family of three-dimensional sheets, each at that tower's own density, has spacing $s = \tfrac{4}{3}\ell$ along the polar arc. The integrals are Wallis's. The four-sphere over which the sheets are counted is closed, so that count is read beyond one flat chart, on several charts of flat spacetime glued by gauge transformations.

Under premise D (every populated tower carries the same total mass) the combinations give totals $5.000$ (zero mode with those sheets), $4.333$ (projection with those sheets), $5.667$ (zero mode, sheets one radius apart) and $5.000$ (projection, sheets one radius apart). Neither reduction produces the unit-ball rule's $L_{\mathrm{eff}} = \ell$. Both reductions need the fifth direction to carry the metric, a setting that short-range tests of Newton's law exclude (Proposition \claimref{dark-matter.thickness-not-gravitational-quantity}); the numbers are computations in that excluded setting, kept for comparison.

## lay
If the hidden fifth direction of a five-dimensional dark tower is treated as a real direction of space, there are two textbook ways to work out how its matter would look from our four-dimensional world. This result computes both, together with the spacing of the sheets of a three-dimensional tower. Assuming each tower carries the same total mass, the resulting dark-to-ordinary ratios lie between about 4.3 and 5.7, and neither method gives the thickness that the paper's unit-ball rule uses. Both methods need gravity to reach into the fifth direction, which laboratory tests rule out, so these are comparisons, not physical predictions.

## one-liner
Zero-mode and local-projection reductions of a five-dimensional de Sitter tower give effective thicknesses $3\pi\ell/8$ and $\pi\ell/4$, sheets of the three-dimensional tower sit $4\ell/3$ apart, and, under the democracy of the total mass (D), neither reduction yields the unit-ball rule's thickness $\ell$; both need a metric fifth direction, a setting short-range gravity tests exclude.
