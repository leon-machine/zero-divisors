---
id: synthesis.frozen-point-geometry-reads-descent-as-vacuum
kind: claim
version: 2
title: 'Under (F), the frozen point reads the descent deposit as vacuum'
status: proved
region: synthesis
subject: dark-energy
tags: [frozen-point, cosmological-constant, conformal-model, no-go, confronted-with-data, rotors-and-stabilisers, needs-continuum]
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
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 2
  source: maintainer pass 2026-11-07 (GA units)
review: draft
derivations:
- name: main
  uses:
  - mass.de-sitter-scale-frozen-point@6
  - dark-matter.imported-frozen-point-de-sitter-radius@6
  - standard-model.imported-frozen-point-dictionary@7
  - synthesis.frozen-phase-spectrum-not-red@2
  - synthesis.sudden-descent-feature-not-tilt@3
  - synthesis.finite-range-descent-deposit-cannot-seed-cmb@4
  - synthesis.quadratic-flows-cannot-thermalise-descent@1
  - synthesis.imported-planck-2018-lcdm-parameters@3
  - synthesis.imported-bbn-reheating-temperature-floor@1
  - mass.imported-unitary-representations-de-sitter-group@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_pair_invariant_of_the_stabiliser
- kind: check
  ref: check.py::check_descent_slice_and_the_range
- kind: check
  ref: check.py::check_index_of_the_invariant_class
- kind: check
  ref: check.py::check_two_scales_bracket_the_observed_modes
- kind: check
  ref: check.py::check_adiabatic_index_bound_at_the_descent
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - standard-model.dating-descent
  - dark-matter.p1-single-frozen-point
  - synthesis.finite-range-descent-deposit-cannot-seed-cmb
  - synthesis.frozen-phase-spectrum-not-red
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The two-point kernel D_c of the horizon-generator modes (the continuum mode space, whose unit is the field''s unit I_4) is written with I_4 (proof); by Leon''s ruling R4 (one unit per entity) the scalar mode analysis is written with I_4 too: the Bunch-Davies mode e^{-I_4 k eta}(1 - I_4/k eta)/sqrt(2k) (formal and proof), its reduced equation, the Fourier kernels e^{-I_4 k.r} and the phase e^{2 I_4 u + I_4 theta}, numbers read in span{1, I_4}, exact since that span is the complex numbers; no bare i remains, so no declaration.'
  open_problem: op.descent-state-and-spectrum
  flags:
  - 'beyond one flat chart: the descent slice is placed in the frozen point''s chart through the late-time matching of the descended universe to the frozen point''s de Sitter field (hypothesis (F) in the formal level); the conformal compactification is used only as the identification of the two flat charts'
  note: >-
    Answer to the open problem's first line of attack ("a structure of the pre-metric sector whose
    correlations are set by the frozen point's global geometry rather than by the descent's Hubble
    length"). Such a structure exists and is canonical: the pair invariant Z of the frozen point's
    stabiliser, which on the descent slice depends only on the separation measured in the slice's
    conformal distance |x_d| to future infinity. It supplies the range: the stored requirement of
    460 to 6.8e17 Hubble lengths of the descent is one comoving length, about 1e-5 of the present
    Hubble radius (42 kpc comoving), and |x_d| is 4.3 Hubble radii. What it does not supply is the
    index: at the descent every observed mode is inside the frozen point's horizon (k|x_d| from 2.7
    to about 1e4), so every Hadamard state invariant under the stabiliser, and the Bunch-Davies state
    of the massless point, reads there as the Minkowski vacuum, with index 2. The stored weight
    result (n_s >= 1 for unitary-series fields) is the k|x_0| -> 0 limit, which is the far future;
    at the descent, dilatation invariance alone constrains nothing. So the three symmetry classes a
    deposit can have at the descent give indices 3 (finite range), 2 (frozen-point-invariant) and
    unconstrained (dilatation-covariant only), and the measured 0.9649 is a slice correlator that
    grows with separation as r^0.035, further from the vacuum than scale invariance. The problem is
    thereby reduced to the descent's occupation numbers, which nothing in the series fixes.
    Hypothesis (F) is one of two readings of the join between the frozen phase and the descended
    phase: the late-time chart reading used here (the descent slice at x_0 = -eta_inf in the frozen
    point's chart) and the reading in which the frozen phase ends at the descent with the scale
    factor continuous, in which the observed modes sit inside the frozen horizon by more than 7e9; the
    conclusion holds in both, and the bound of (iii) for the whole unitary series is stated at this
    matching. Transport-absent apart from the Cl(2,4) form of the invariant and the placement of the
    slice: the conformally coupled scalar's invariant propagator, the uniqueness of the invariant
    Hadamard state for positive mass (the Euclidean state), the Hankel asymptotics of its modes and
    the Bunch-Davies mode of the massless scalar are standard (from memory; the check verifies the
    massless mode and the rational identities exactly, not that H^2/(8 pi^2 (Z-1)) is the invariant
    Hadamard state). The result's stabiliser correlations, to about 4.3 present Hubble radii, make
    available in principle the one escape of the deposit clause of the monopole bound filed
    alongside (synthesis.pati-salam-monopoles-bound-descent-history: an orientation aligned beyond
    the descent's Hubble length); the obstruction here concerns the zeta spectrum, not vacuum
    orientation.
---
## formal
Work in the conformal model of Lemma \claimref{mass.de-sitter-scale-frozen-point} ($\ip{\nO}{\nInf} = 1$, $X(x) = \nO + x - \tfrac12 Q(x)\,\nInf$, $Q$ of signature $(+,-,-,-)$) with the flat-slicing frozen point $I_{\mathrm{fs}} = He_{0}$ of Proposition \claimref{synthesis.frozen-phase-spectrum-not-red}, $\Lambda = 3H^{2}$, scale function $\ip{X(x)}{I_{\mathrm{fs}}} = Hx_{0}$, so that the frozen point's gravitational field is de Sitter in its flat slicing with conformal time $x_{0} < 0$ and $x_{0} \to 0^{-}$ its future infinity. Let the descended universe be the flat FLRW field of the stored finite-range result on the same flat background, $\hb^{-1}(a) = a(\eta)\,a$ in conformal coordinates $(\eta, \vec x)$, with $\dot a^{2}/H_{0}^{2} = \Omega_{r}a^{-2} + \Omega_{m}a^{-1} + \Omega_{\Lambda}a^{2}$ and the record values of Fact \claimref{synthesis.imported-planck-2018-lcdm-parameters}. Hypothesis (F): its late-time de Sitter stage is the frozen point's field, $a(\eta) \to 1/(H|x_{0}|)$ with $x_{0} = \eta - \eta_{\infty}$, $\eta_{\infty} = \int_{0}^{\infty}da/(a^{2}\dot a)$ the conformal time from the origin to future infinity (the reading of the dating and of P1: one frozen point, $w = -1$). Write $\eta_{d}$ for the conformal time of the descent and $x_{d} = \eta_{d} - \eta_{\infty}$ for the descent slice in the frozen point's chart.
\begin{enumerate}
\item[(i)] \emph{(The pair invariant.)} For points $X = X(x)$, $Y = X(y)$ of the null cone, $Z(X, Y) := 1 + \tfrac{\Lambda}{3}\,\ip{X}{Y}/(\ip{X}{I_{\mathrm{fs}}}\ip{Y}{I_{\mathrm{fs}}})$ is unchanged by rescaling either representative and by every rotor fixing $I_{\mathrm{fs}}$ (the stabiliser $SO(1,4)$ of Fact \claimref{dark-matter.imported-frozen-point-de-sitter-radius}: spatial rotations, spatial translations, special conformal maps, the dilatation), and it is changed by a time translation. On the chart $Z = 1 - Q(x - y)/(2x_{0}y_{0})$, so at equal time $Z - 1 = |\vec x - \vec y|^{2}/(2x_{0}^{2})$: a two-point function set by the frozen point's global geometry, $G = G(Z)$, depends on the descent slice only through $|\vec x - \vec y|/|x_{d}|$, and its correlations reach the length $|x_{d}|$.
\item[(ii)] \emph{(Where the descent slice sits, and the range it needs.)} With the record values, $a_{0}H_{0}\eta_{\infty} \in (4.32, 4.34)$ and $a_{0}H_{0}\eta_{0} \in (3.17, 3.19)$; for a descent at $T_{d} \ge 1$ MeV (Fact \claimref{synthesis.imported-bbn-reheating-temperature-floor}) $a_{0}H_{0}\eta_{d} < 10^{-7}$, so $a_{0}H_{0}|x_{d}| \in (4.32, 4.34)$. The range the stored amplitude bound requires (Proposition \claimref{synthesis.finite-range-descent-deposit-cannot-seed-cmb}(i), (iii), with $\sigma^{2} \le 1$) is one comoving length for every $T_{d}$, $a_{0}H_{0}R_{\mathrm{req}} = (3\pi A_{s}/2)^{1/3}\,a_{0}H_{0}/k_{*} \in (9.4 \times 10^{-6}, 9.8 \times 10^{-6})$ over $A_{s} \in (2.07, 2.13) \times 10^{-9}$ (the stored $460$ and $6.8 \times 10^{17}$ Hubble lengths of the descent are this one length), and $|x_{d}|/R_{\mathrm{req}} > 4.4 \times 10^{5}$. The pivot has $u_{*} := k_{*}|x_{d}| \in (960, 968)$ and the largest observed scales, $k = 2/\eta_{0}$, have $u \in (2.70, 2.74)$: every observed mode is inside the frozen point's Hubble length at the descent (exit is at $u = 1$, in the future, Proposition \claimref{synthesis.finite-range-descent-deposit-cannot-seed-cmb}(iv)). In the other reading of the join, the frozen phase ending at the descent with the scale factor continuous, the same modes sit inside the frozen phase's Hubble length by $k/(a_{d}H_{\Lambda}) > 7 \times 10^{9}$ at $1$ MeV; both readings place every observed mode inside, and nothing below depends on which is taken.
\item[(iii)] \emph{(The index of the invariant class.)} Let the deposit on the descent slice be the equal-time two-point function of a state of a scalar field of the series' weight dictionary (Fact \claimref{standard-model.imported-frozen-point-dictionary}, $m^{2} = -w(w+3)H^{2}$) on the frozen point's field. For the conformal weight $w = -1$ ($m^{2} = 2H^{2}$) the stabiliser-invariant Hadamard state has $G = H^{2}/(8\pi^{2}(Z - 1)) = 1/(4\pi^{2}a_{\mathrm{fp}}^{2}|\vec x - \vec y|^{2})$ with $a_{\mathrm{fp}} = 1/(H|x_{d}|)$, a correlator homogeneous of degree $-2$ on the slice, so $\Delta^{2}(k) = k^{2}/(4\pi^{2}a_{\mathrm{fp}}^{2})$ and $n_{s} - 1 = 2$ at every $k$. For the massless point $w = 0$ the dilatation-invariant Bunch-Davies state, whose mode $\chi_{k} = e^{-I_4k\eta}(1 - I_4/k\eta)/\sqrt{2k}$ (numbers are read in $\mathrm{span}\{1, I_4\}$) solves $\chi'' + (k^{2} - 2/\eta^{2})\chi = 0$, gives $\Delta^{2}(k) = (H/2\pi)^{2}(1 + u^{2})$, $u = k|x_{d}|$, with local index $2u^{2}/(1 + u^{2})$: above $1.99999$ at the pivot and in $(1.7, 1.8)$ at $k = 2/\eta_{0}$. For every other weight with $m^{2} > 0$ the stabiliser-invariant Hadamard state is unique, the Euclidean state, whose mode's Hankel asymptotics give $\Delta^{2} \propto u^{2}(1 + O(u^{-2}))$ at $u \gg |\nu|$; at leading adiabatic order the local index of every field of the unitary series (Fact \claimref{mass.imported-unitary-representations-de-sitter-group}), $3 - u^{2}/(u^{2} + \tfrac14 - \nu^{2})$, lies in $[2 - 2/(u^{2} - 2), 3)$, which at the pivot is above $2 - 3 \times 10^{-6}$ and more than $480$ standard deviations above the measured $n_{s} - 1 = -0.0351 \pm 0.0042$. At the pivot separation $Z - 1 = 1/(2u_{*}^{2}) < 6 \times 10^{-7}$. The $\alpha$-vacua are not Hadamard (an antipodal singularity) and their local index oscillates with amplitude of order $u|\beta_{\alpha}|$: they are excited states whose Bogoliubov coefficient is a datum, not a reading of the frozen point's geometry.
\item[(iv)] \emph{(The three classes at the descent.)} On the descent slice a correlator homogeneous of degree $-2\Delta$ gives $n_{s} - 1 = 2\Delta$: finite range (effective degree $-3$ and below) gives $3$ (the stored bound); the frozen point's invariant class gives $2$; a deposit covariant under the slicing's dilatation alone, $G(x_{0}; r) = x_{0}^{-2w}g(r/x_{0})$, has an unconstrained spectrum $\Delta^{2} = F(k|x_{d}|)$ on the slice, the weight fixing the index only as $k|x_{0}| \to 0$, which Proposition \claimref{synthesis.frozen-phase-spectrum-not-red} reads on the far-future boundary. The measured $n_{s} = 0.9649$ (Fact \claimref{synthesis.imported-planck-2018-lcdm-parameters}) is a slice correlator of degree $1 - n_{s} = 0.0351$, growing with separation.
\end{enumerate}
Consequently the frozen point's global geometry supplies the correlation range the measured amplitude needs, with a margin above $4 \times 10^{5}$ at every reheating temperature, and the obstruction to a descent-sourced spectrum is not range but horizon exit: at the descent the observed modes are outside the descent's Hubble length ($k_{*}/a_{d}H_{d} < 5 \times 10^{-6}$ at $1$ MeV) and inside the frozen point's ($k_{*}|x_{d}| > 960$), so a deposit set by the descent's scale is white ($n_{s} - 1 = 3$) and one set by the frozen point's is the vacuum's ($n_{s} - 1 = 2$); the measured index needs a deposited excitation above the vacuum whose occupation numbers nothing in the series fixes. Stationary excitations do not reopen the route: for the states thermal at rapidity period $2\pi c$ on each half of a horizon generator the two-point kernel differs from the vacuum's by $-(c^{-2} - 1)\epsilon^{2}/24 + O(\epsilon^{4})$ at relative separation $\epsilon$ along the generator (filed alongside, synthesis.stationary-horizon-state-is-its-own-edge-scaling-limit), so while $c^{-1}$ is small against $u$ such a state reads as the vacuum, and a member hot enough to resolve the observed modes is a thermal deposit of finite range, the stored bound's class (argued).

## technical
The question was whether the series' one global structure before the descent, the frozen point $I$ with its $SO(1,4)$ stabiliser, could correlate the descent's deposit over the lengths the stored finite-range bound demands. It can: the stabiliser's pair invariant $Z$ is a function of the chord $\ip{X}{Y}$ divided by the two scale functions, and on an equal-time slice of the frozen point's flat slicing it reduces to the separation over the slice's conformal distance to future infinity. Placing the descent slice needs one identification, hypothesis (F): the descended universe's late-time de Sitter stage is the frozen point's own field, so the FLRW conformal time runs from the origin to $\eta_{\infty}$ and the descent sits at $x_{0} = -\eta_{\infty}$ in the frozen point's chart. An exact bracket of $\int da/\sqrt{\Omega_{r} + \Omega_{m}a + \Omega_{\Lambda}a^{4}}$ (monotone Riemann sums with integer square roots, record parameters) gives $a_{0}H_{0}\eta_{\infty} \in (4.32, 4.34)$. The required range, once written in comoving units, is independent of the reheating temperature, $a_{0}H_{0}R_{\mathrm{req}} = (3\pi A_{s}/2)^{1/3}/222.4$, about $9.5 \times 10^{-6}$ (the two stored numbers, $460$ at $1$ MeV and $6.8 \times 10^{17}$ at $10^{12}$ GeV, divided by the stored Hubble ratios, both give it); $|x_{d}|$ is $4.4 \times 10^{5}$ times larger.

The index then follows from where the observed modes are relative to the frozen point's horizon: $k|x_{d}|$ runs from $2.7$ at the largest observed scales to about $10^{4}$ at $\ell \approx 2500$, all inside. A state invariant under the stabiliser and Hadamard reads at such separations as the Minkowski vacuum, correlator $1/(4\pi^{2}a^{2}r^{2})$, index $2$; the conformally coupled weight makes this exact at every scale, the massless point's Bunch-Davies spectrum $(H/2\pi)^{2}(1 + u^{2})$ makes the approach to $2$ explicit, and the leading adiabatic index $3 - u^{2}/(u^{2} + \tfrac14 - \nu^{2})$ bounds every unitary-series field between $2 - 2/(u^{2} - 2)$ and $3$ (the leading adiabatic bound, stated here at this matching). The $\alpha$-vacua, not being Hadamard, fall outside the class: their index oscillates and their Bogoliubov coefficient is a datum. This is the counterpart, at the descent, of the stored weight result: that result fixes the index by the dilatation weight only in the limit $k|x_{0}| \to 0$, which for the frozen point of the observed $\Lambda$ is the far future; at the descent dilatation invariance alone leaves the spectrum an arbitrary function of $k|x_{d}|$. The classification is therefore complete for the symmetry classes the series offers: white, vacuum, or unconstrained. The measured spectrum, a correlator growing as $r^{0.035}$, lies on the far side of scale invariance from the vacuum, so it is an excitation deposited mode by mode, in the sense of the quadratic-flows result, with occupation numbers the series does not supply. The join between the frozen phase and the descended phase can also be read with the frozen phase ending at the descent and the scale factor continuous; the observed modes are then inside the frozen horizon by more than $7 \times 10^{9}$ and the conclusion is the same. Transport-absent apart from the $\Cl(2,4)$ form; the de Sitter propagators and the Bunch-Davies mode are standard (the mode is verified exactly in the check; that $H^{2}/(8\pi^{2}(Z-1))$ is the invariant Hadamard state of the conformal weight, and the uniqueness of that state for positive mass, are cited from memory).

## lay
Before the descent there is one global structure in this theory: the frozen point, whose symmetry group is that of de Sitter space. Could that structure have correlated the newborn universe over the enormous distances the cosmic background requires? The arithmetic says yes with a huge margin: the distance it correlates is the present Hubble radius, and the distance the measured amplitude needs is about a hundred-thousandth of that. But the same arithmetic says what spectrum such a correlation would give. At the descent every scale we now observe was deep inside the frozen point's horizon, and a de Sitter-symmetric state looks there like empty flat space, whose ripples grow steeply with wavenumber (index $2$ above scale invariance) rather than falling gently (the measured $0.035$ below it). So the frozen point can supply the reach of the correlations but not their shape; the shape would have to be an excitation the descent deposits, and nothing in the theory yet says what it is.

## one-liner
Under hypothesis (F) (the late de Sitter stage is the frozen point's own field), a deposit correlated by the frozen point's stabiliser invariant $Z$ reaches $|x_{d}| = \eta_{\infty} - \eta_{d}$, $a_{0}H_{0}|x_{d}| \in (4.32, 4.34)$, which exceeds the required range ($a_{0}H_{0}R_{\mathrm{req}} \approx 9.5 \times 10^{-6}$, one length for every $T_{d}$) by over $4 \times 10^{5}$; but with $k_{*}|x_{d}| \in (960, 968)$ every observed mode is inside the frozen point's horizon at the descent, so the invariant (Euclidean) state of every unitary-series field, and the massless Bunch-Davies state, give the vacuum's $n_{s} - 1 = 2$ up to $O(u^{-2})$, more than $480$ standard deviations from the measured value: range is not the obstruction, horizon exit is.
