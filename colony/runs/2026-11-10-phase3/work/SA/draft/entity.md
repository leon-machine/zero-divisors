---
id: synthesis.red-tilt-criterion-on-power-law-stages-and-the-index-ledger-of-the-stored-sources
kind: claim
version: 1
title: 'Red-tilt criterion on power-law stages and the index ledger of the stored sources'
status: proved
region: synthesis
subject: dark-energy
tags: [kasner, frozen-point, no-go, confronted-with-data, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-10-phase3
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-10-phase3
review: draft
derivations:
- name: main
  uses:
  - synthesis.imported-bessel-reduction-and-small-argument-hankel-forms@2
  - synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling@3
  - synthesis.kasner-approach-gives-horizon-exit-and-index-three@4
  - synthesis.kasner-hidden-scale-coupled-scalars-stay-blue@4
  - synthesis.tree-level-curvature-couplings-stay-blue-at-the-isotropic-kasner-point@4
  - synthesis.imported-wands-duality-of-perturbation-spectra@1
  - synthesis.frozen-phase-spectrum-not-red@4
  - synthesis.frozen-point-geometry-reads-descent-as-vacuum@3
  - synthesis.finite-range-descent-deposit-cannot-seed-cmb@5
  - mass.weight-polynomial-two-series@6
  - synthesis.imported-planck-2018-lcdm-parameters@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_order_of_the_mode_equation_by_exact_frobenius_series
- kind: check
  ref: check.py::check_power_law_threshold_two_thirds_and_the_kasner_trace
- kind: check
  ref: check.py::check_ledger_of_kasner_rows_from_residue_weights
- kind: check
  ref: check.py::check_de_sitter_row_in_the_same_equation
- kind: check
  ref: check.py::check_dust_with_cosmological_constant_scaling_and_running
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling
  - synthesis.frozen-phase-spectrum-not-red
  - synthesis.imported-wands-duality-of-perturbation-spectra
extraction:
  open_problem: op.descent-state-and-spectrum
  note: >-
    A consolidation with three additions. Stored already, and cited, not re-proved: the order formula and the index
    $3 - 2\nu$ on a Kasner approach, the rows for the minimally coupled scalar, the cross modes, the hidden-scale
    weights, the Kaluza-Klein vector, the tree-level couplings and the fitted window of the curvature coupling, the
    weights of the frozen phase, and the absence of exit after the descent. Added here: (a) the single inequality
    $f^{2} + 4\kappa > 9(1 - P)^{2}$ that decides redness for every stored mode equation, the de Sitter case in
    conformal time included; (b) the threshold $p > \tfrac23$ for isotropic power laws, its incompatibility with the
    Kasner trace, and the closed margins of the rows; (c) the scaling statement for dust with a cosmological constant.
    Kill condition written before the rows were computed: no stored structure gives a red index on three observed
    axes alike without a number chosen for that purpose. It was met: the result is negative. What "the stored mode
    equations" covers, so that the label is exact: a pattern search of the formal level of all claims for
    fluctuation, two-point, power spectrum, primordial, Goldstone, zero mode, massless scalar, dilaton, radion,
    moduli, Hubble length, horizon exit, spectral index, tilt, squeezing, Bogoliubov and pair creation (241
    entities, titles read, about forty read at one-liner or formal level), and the stored record of the open
    problem. The search is by pattern and reading, not a formal audit of every derivation: the clause "no other
    stored structure" is argued on that basis. Structures with no stored mode equation on a slice (the tower's pair
    channel, the density-wave bosons of a null generator, the horizon arrays, the frozen point's norm and point at
    infinity, the deposit's band data) are outside this result; they are listed in the run's findings. Prior art for
    clause (vi): Cai and Wilson-Ewing, A LambdaCDM bounce scenario, JCAP 2015 (arXiv 1412.2914; abstract checked on
    the web: a slight red tilt from a positive cosmological constant in a contracting dust stage, and a positive
    running); the exponent six and the relation between running and index are derived here by scaling and are not
    quoted from that paper. Wands 1999 is the stored Fact. Transport-absent: the statements are about mode equations
    on the stored fields; the residue weights of the Clifford algebra enter only as the bookkeeping of the exponents.
---

## formal
Let $T > 0$ be a time variable, $k > 0$ a comoving momentum, and let a mode $\chi(T)$ obey
\[
\ddot\chi + \frac{1 + f}{T}\,\dot\chi + \Bigl(k^{2}T^{-2P} - \frac{\kappa}{T^{2}}\Bigr)\chi = 0 \qquad (\mathrm{E})
\]
with real constants $f$ (the friction excess), $\kappa$ (the curvature or mass term) and $P \ne 1$ (the exponent of the momentum's axis). Write $q = 1 - P$, $D = f^{2} + 4\kappa$ and assume $D \ge 0$. Every mode equation of the stored results on the primordial spectrum has this form: on a Kasner approach $T$ is proper time (Theorems \claimref{synthesis.kasner-approach-gives-horizon-exit-and-index-three} and \claimref{synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling}), and on the frozen point's de Sitter field $T$ is minus the conformal time (clause (v)). Write $n - 1$ for the index of the dimensionless spectrum, $\Delta^{2}(k) \propto k^{n - 1}$, and $N_{\mathrm{obs}} = -0.0351 \pm 0.0042$ for the measured value (Fact \claimref{synthesis.imported-planck-2018-lcdm-parameters}).
\begin{enumerate}
\item[(i)] \emph{(Order and criterion.)} With $s = kT^{q}/|q|$ the solutions of (E) are $T^{-f/2}$ times Bessel functions of $s$ of order
\[
\nu = \frac{\sqrt{D}}{2|q|}
\]
(Fact \claimref{synthesis.imported-bessel-reduction-and-small-argument-hankel-forms}). Given the stored index $n - 1 = 3 - 2\nu$ of a mode with $\nu > 0$ that is in its adiabatic vacuum before it leaves the Hubble length (Theorem \claimref{synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling}(iii), stated there for $P < 1$), the exited spectrum is red exactly when $D > 9q^{2}$, scale invariant exactly when $D = 9q^{2}$, and within three standard deviations of $N_{\mathrm{obs}}$ exactly when $3.0225^{2}\,q^{2} \le D \le 3.0477^{2}\,q^{2}$.
\item[(ii)] \emph{(Isotropic power laws.)} For a massless minimally coupled field on a stage whose $d$ observed directions all have scale factor $T^{p}$, $p \ne 1$, with no other direction, $f = dp - 1$, $\kappa = 0$, $P = p$, and
\[
D - 9q^{2} = \bigl((d + 3)p - 4\bigr)\bigl((d - 3)p + 2\bigr) .
\]
For $d = 3$ this is $12p - 8$: the order is $|3p - 1|/(2|1 - p|)$, the form $\tfrac32 + 1/(p - 1)$ of Fact \claimref{synthesis.imported-wands-duality-of-perturbation-spectra}, and the spectrum is red exactly when $p > \tfrac23$. The ratio of the Hubble rate to the physical momentum is $pT^{p - 1}/k$, so modes leave the Hubble length toward $T = 0$ for $p < 1$ (a contraction) and toward large $T$ for $p > 1$ (an accelerated expansion). The window of (i) is $p \in [0.66791, 0.66930]$ on the contracting branch, centre $\tfrac{40351}{60351}$, where $n - 1 = (4 - 6p)/(1 - p)$, and $p \in [42.9, 89.9]$ on the expanding branch, centre $\tfrac{20351}{351}$, where $n - 1 = -2/(p - 1)$. Read as a fluid of constant pressure ratio $w_{\mathrm{f}}$, $p = 2/(3(1 + w_{\mathrm{f}}))$, the contracting branch has $n - 1 = 12w_{\mathrm{f}}/(1 + 3w_{\mathrm{f}})$ and the centre is $w_{\mathrm{f}} = -0.0029$.
\item[(iii)] \emph{(The Kasner trace excludes the red set.)} On a stage whose exponents sum to one over all directions, hidden ones included, a massless minimally coupled field has $f = 0$ whatever the exponents (Theorem \claimref{synthesis.kasner-approach-gives-horizon-exit-and-index-three}(ii)), so $D = 0$ and the order is $0$. If the $d$ directions have equal exponents the trace gives $p = 1/d < \tfrac23$ for $d \ge 2$. So on every stage with unit trace, which is every stored wall, a red index needs $D > 9q^{2}$ to come from the field's own weight in $f$ or from $\kappa$.
\item[(iv)] \emph{(Ledger of the Kasner rows.)} On the equal-exponent segment $(p, p, p, 1 - 3p)$, $0 \le p \le \tfrac12$, of Theorem \claimref{synthesis.kasner-hidden-scale-coupled-scalars-stay-blue}, with hidden exponent $P_{h} = 1 - 3p$ and $q = 1 - p$: the cross modes of observed pairs have $f = 0$; a scalar whose action carries the hidden scale to the power $\lambda \in \{-1, 0, 1\}$ (the gauge field's hidden component, a confined field, a bulk zero mode) has $f = (\lambda - 1)P_{h}$ and
\[
9q^{2} - f^{2} \ge 9q^{2} - 4P_{h}^{2} = (1 + 3p)(5 - 9p) > 0 ,
\]
so none is red at any point of the segment. The Kaluza-Klein vector's potential has $f = 2(P_{h} - p)$ and $f^{2} - 9q^{2} = (1 + 5p)(11p - 5)$: red exactly for $p > \tfrac{5}{11}$, points that only five-dimensional stiff matter reaches (none is stored) and the vacuum end $p = \tfrac12$, while $f^{2} \le 16q^{2}$ on the whole segment, so its field strength has index $5 - 2\nu \ge 1$. At the isotropic point in the Einstein frame a scalar with curvature coupling $\xi$ ($\tfrac16$ conformal) has $4\nu^{2} = (\lambda - 1)^{2} + 6\xi$ (Theorem \claimref{synthesis.tree-level-curvature-couplings-stay-blue-at-the-isotropic-kasner-point}(iv)); over the twelve tree-level values stored there and $\lambda \in \{-1, 0, 1\}$ the largest is $7 < 9$. The window of (i) at $\lambda = 1$ is $\xi \in [1.522584375, 1.548079215]$, the stored fitted window, which contains no stored value.
\item[(v)] \emph{(The de Sitter row.)} On the frozen point's field in its flat slicing, with $T$ minus the conformal time, a scalar of mass $m$ obeys (E) with $f = -3$, $P = 0$, $\kappa = -m^{2}/H^{2}$. With the dictionary $m^{2} = -w(w + 3)H^{2}$ (Corollary \claimref{mass.weight-polynomial-two-series}), $D = (2w + 3)^{2}$ and $\nu = |w + \tfrac32|$: for $w \in [-\tfrac32, 0]$ the index is $-2w$, the stored value (Proposition \claimref{synthesis.frozen-phase-spectrum-not-red}(iii)); $D \le 9$ on the real weights $w \in [-3, 0]$ with equality only at $w = 0$ and $w = -3$; a red index needs $\kappa > 0$, that is $m^{2} < 0$, and $N_{\mathrm{obs}}$ needs $w = \tfrac{351}{20000}$, $m^{2}/H^{2} = -\tfrac{21183201}{400000000}$. The index is that of modes that have left the frozen point's Hubble length; the observed modes have not (Theorem \claimref{synthesis.frozen-point-geometry-reads-descent-as-vacuum}(ii)).
\item[(vi)] \emph{(Dust with the cosmological constant: the one stored content in the red set.)} Of the stored stages of the descended phase, radiation ($p = \tfrac12$, order $\tfrac12$) is blue, dust ($p = \tfrac23$, order $\tfrac32$) sits exactly on the threshold, and neither has exit while it expands (Proposition \claimref{synthesis.finite-range-descent-deposit-cannot-seed-cmb}(ii)). Consider, as a hypothesis that the store does not hold, the same content contracting: $\dot a^{2}/a^{2} = Aa^{-3} + \Lambda/3$ with $A > 0$ and $\Lambda > 0$ the frozen point's constant. The equation of a massless field, $\ddot\chi + 3(\dot a/a)\dot\chi + (k/a)^{2}\chi = 0$, is unchanged by $(a, k, A) \to (ca, ck, c^{3}A)$, and the monomials in $A$, $\Lambda$, $k$ that are invariant under this map and carry no dimension of time are the powers of
\[
x = \frac{\Lambda A^{2}}{k^{6}} ,
\]
which is three times the ratio of the constant's density to the dust's when the mode leaves the Hubble length of the dust stage ($a = A/k^{2}$). Hence, for any rule fixing the state that respects the scaling and uses no further dimensional constant, $\Delta^{2}(k) = \Delta^{2}_{\mathrm{dust}}\,G(x)$ with $\Delta^{2}_{\mathrm{dust}}$ free of $k$. If $G$ is twice differentiable at $x = 0$ with $G(0) = 1$, the index $N = n - 1$ and the running $\alpha = dN/d\ln k$ satisfy
\[
N = -6x\,\frac{G'}{G} , \qquad \alpha + 6N = -36x^{2}\,\frac{G'^{2} - G''G}{G^{2}} ,
\]
so $\alpha = -6N$ up to terms of relative order $x$: a red tilt comes with a positive running six times as large, $\alpha = 0.2106$ at $N = -0.0351$, and the value of $x$ at the pivot, about $N/(-6G'(0))$, is a number chosen to match the index.
\end{enumerate}
So among the stored mode equations none gives a red index on three observed axes alike without a number chosen for that purpose. The numbers that would do it are the curvature coupling of (iv), stored as free and not adopted; the point $p > \tfrac{5}{11}$ of the segment for the Kaluza-Klein potential, whose field strength stays blue; and the exit epoch $x$ of (vi) on a stage the store does not hold, which fixes a running that the store does not confront with data. That no further stored structure has a mode equation is argued from a search (see the note), not proved. Not covered: the conversion of any of these modes into the curvature perturbation, the state of (vi) (on the contracting stage the modes are outside the Hubble length in the far past, where the constant dominates, so an adiabatic vacuum is defined only to finite order in $x$), loop-level couplings, and structures without a stored mode equation on a slice.

## technical
The stored results on the primordial spectrum treat one source at a time: a scalar near a Kasner wall, fields coupled to a hidden direction, the gravitational field's own modes, curvature couplings, the frozen point's de Sitter field. Each ends in a Bessel order. This result puts them under one equation with three constants, the friction excess, the curvature or mass term and the exponent of the momentum's axis, and reads redness off one inequality, given the stored relation between the order and the index: the square of the friction excess plus four times the curvature term must exceed nine times the square of one minus the exponent. Three consequences follow. First, for a field that feels only the geometry on an isotropic power-law stage, the inequality is the single condition that the exponent exceed two thirds; the stored walls all have exponents summing to one, which gives no friction excess at all and, when isotropic, the exponent one third, so under that trace condition the geometry alone never reddens a spectrum. Second, the stored rows are recomputed with closed margins: fields weighted by the hidden scale stay blue along the whole equal-exponent segment, the Kaluza-Klein potential is red only beyond the point five elevenths, where no stored source reaches and where its field strength is still blue, the twelve tree-level curvature couplings stay below the threshold, and the de Sitter field is red only for a negative mass term. Third, the one stored matter content that lies in the red set is dust with the frozen point's cosmological constant, taken as a contracting stage, which the store does not hold: there a scaling argument shows that the spectrum depends on the momentum only through its inverse sixth power, so, assuming the dependence is smooth, a red tilt comes with a positive running six times as large, about 0.21 at the measured tilt, and the tilt itself is set by choosing when the observed modes leave the Hubble length. The result is negative: under the stored content no mode equation gives the measured tilt without a chosen number. It is a consolidation with exact margins, and the completeness of the list of sources is argued from a search.

## lay
The early universe's ripples are slightly stronger on large scales than on small ones. This framework has no accepted account of that slight tilt, and earlier results tested its possible sources one by one. This result gathers them under one formula, assuming the earlier results' link between a ripple's equation and its tilt. The formula says when a source gives more ripple on large scales: the universe's stage must stretch or squeeze space fast enough, faster than a fixed threshold, or the field must carry an extra coupling strong enough to make up the difference. Every stage the framework actually contains falls short of the threshold, and every coupling it fixes is too weak, so under the framework's present content each source is tilted the wrong way or not at all. One combination comes close: ordinary matter together with the dark energy the framework already has, if the universe had once been contracting. Given that assumption, which the framework does not make, the tilt could be matched by choosing a moment, but the tilt would then change rapidly with scale. The conclusion is that the measured tilt needs a new assumption, not a new calculation.

## one-liner
Given the stored index $3 - 2\nu$, a mode obeying $\ddot\chi + (1 + f)\dot\chi/T + (k^{2}T^{-2P} - \kappa T^{-2})\chi = 0$ is red exactly when $f^{2} + 4\kappa > 9(1 - P)^{2}$; for a minimally coupled field on an isotropic power law this is $p > \tfrac23$, which the unit trace of every stored wall excludes; the stored hidden-scale, Kaluza-Klein, tree-level curvature and de Sitter rows all fail it or pass it only through a chosen number; and under the hypothesis of a contracting dust stage with the frozen point's constant the spectrum depends on $k$ through $\Lambda A^{2}/k^{6}$ only, so a red tilt carries a running of $-6$ times the index.
