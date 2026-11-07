---
id: synthesis.sudden-descent-feature-not-tilt
kind: claim
version: 4
title: 'A sudden descent leaves a feature, not a red tilt'
status: proved
region: synthesis
subject: dark-energy
tags: [frozen-point, cosmological-constant, no-go, confronted-with-data, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-10-22-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 4
  source: maintainer pass 2026-11-07 (GA units)
review: draft
derivations:
- name: main
  uses:
  - synthesis.frozen-phase-spectrum-not-red@2
  - mass.de-sitter-scale-frozen-point@6
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_mode_function_and_wronskian
- kind: check
  ref: check.py::check_bogoliubov_normalisation
- kind: check
  ref: check.py::check_closed_form
- kind: check
  ref: check.py::check_small_x_blue
- kind: check
  ref: check.py::check_large_x_windows_not_red
- kind: check
  ref: check.py::check_every_window_not_red
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - standard-model.dating-descent
  - dark-energy.imported-henneaux-teitelboim-promotion
  - mass.imported-unitary-representations-de-sitter-group
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'By Leon''s ruling R4 (one unit per entity, and the same mode functions as synthesis.frozen-point-geometry-reads-descent-as-vacuum, which writes them with I_4): the instantaneous-vacuum data chi'' = -I_4 k (2k)^{-1/2}, the Bunch-Davies solution u(z) = e^{-I_4 z}(1 - I_4/z), its Wronskian 2 I_4, the matching chi_z = -I_4 and the Bogoliubov coefficients alpha = e^{-I_4 x}A, A = 1 - I_4/x - 1/(2x^2), beta = -e^{I_4 x}B are written with I_4, numbers read in span{1, I_4}, exact since that span is the complex numbers; no bare i remains, so the declaration is removed.'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Check strengthened: required factor 1.204365805 and floor(e^7) = 1096 pinned by hand (1096 now derived, not typed); Taylor coefficient bound tested on the computed range; every enclosure tested for soundness against independent closed-form enclosures of F; inputs and precision parameters moved to module level. Version 1 -> 2.'
  maintainer_pass_deposit_state:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2 -> 3, at Leon''s decisions of 2026-11-01 (deposit state): a marked note after the formal statement records that the model''s instantaneous-vacuum start is not a Hadamard state (clause (iv) of synthesis.massive-dirac-instantaneous-vacuum-and-non-smooth-descents-are-not-hadamard), so the model describes a state the adopted Hadamard deposit premise excludes; the spectrum computation and every clause are unchanged.'
  open_problem: op.descent-state-and-spectrum
  note: 'Sharpens the first escape of the frozen-phase no-go (the descent state must break the slicing dilatation): if the descent is a single event into the frozen phase and the field starts there in the instantaneous vacuum, the spectrum is flat at small scales, suppressed at large scales and ringing in between, and no 7-e-fold window carries the measured red index (exact rational enclosures for every window). Read as a pointer, not a theorem: dilatation breaking that produces the measured tilt would have to persist while the whole observed window is set. The mode computation is standard de Sitter field theory and transport-absent; the series supplies the setting (frozen phase in flat slicing, the massless point of its weight dictionary, the descent as the origin). The de Sitter scale during the descent is not addressed.'
---

## formal
Work in the frozen phase in its flat slicing, the setting of Proposition \claimref{synthesis.frozen-phase-spectrum-not-red} (de Sitter space $\eta/(Hx_0)^2$ of Lemma \claimref{mass.de-sitter-scale-frozen-point}, conformal time $\eta = x_0 < 0$, scale factor $a = -1/(H\eta)$), and model the descent as an event at conformal time $\eta_d < 0$: before it the field has no propagating modes, and at it a massless scalar $\phi$ (the massless point of the series' weight dictionary, weight $0$) is set, mode by mode, to the instantaneous vacuum of $\chi = a\phi$, namely $\chi = (2k)^{-1/2}$, $\chi' = -I_{4}k(2k)^{-1/2}$ (numbers are read in $\mathrm{span}\{1, I_{4}\}$). Write $x = k|\eta_d|$ and let $\Delta^{2}(k)$ be the late-time ($\eta \to 0$) dimensionless spectrum of $\phi$.
\begin{enumerate}
\item[(i)] \emph{(Exact spectrum.)} $\Delta^{2}(k) = (H/2\pi)^{2}F(x)$ with
\[
F(x) \;=\; 1 + \frac{1}{2x^{4}} + \frac{1}{x^{2}}\Bigl[\Bigl(1 - \frac{1}{2x^{2}}\Bigr)\cos 2x - \frac{1}{x}\sin 2x\Bigr],
\]
the Bogoliubov coefficients relative to the Bunch-Davies modes being $\alpha = e^{-I_{4} x}A$, $\beta = -e^{I_{4} x}B$ with $A = 1 - I_{4}/x - 1/(2x^{2})$, $B = 1/(2x^{2})$, and $|\alpha|^{2} - |\beta|^{2} = 1$.
\item[(ii)] \emph{(Modes outside at the descent.)} $F(x) = \tfrac49 x^{2} - \tfrac1{15}x^{4} + \tfrac{8}{1575}x^{6} + O(x^{8})$, so for $k|\eta_d| \ll 1$ the local index is $n_s - 1 \to +2$: large scales are suppressed, a blue cutoff.
\item[(iii)] \emph{(Modes inside at the descent.)} $(|A| - B)^{2} \le F(x) \le (|A| + B)^{2}$ with $|A|^{2} = 1 + 1/(4x^{4})$, so $F \to 1$ with oscillations of envelope $x^{-2}$.
\item[(iv)] \emph{(Every window.)} For every $x_1 > 0$, $\ln F(x_1) - \ln F(e^{7}x_1) < 7 \times 0.0267$, the smallest red drop the measured $n_s = 0.9649 \pm 0.0042$ \cite{Planck2018} allows at two standard deviations over seven e-folds of $k$ (the measured range $\ell \approx 2$ to $2500$ spans about $7.1$ e-folds). So no window of that width has a mean index inside the measured band.
\end{enumerate}
Consequently, under this model, a sudden descent imprints a feature at $k \sim 1/|\eta_d|$ (suppression of modes outside at the descent, a decaying ringing, flatness for modes well inside) and no window of the measured width carries the measured red index: the first escape named in Proposition \claimref{synthesis.frozen-phase-spectrum-not-red}, dilatation breaking by the descent's state, is not supplied by a single descent event with an instantaneous-vacuum start. Other initial states at the descent are not covered.

\emph{Note (the start state is not Hadamard; added 1 November).} The model's instantaneous-vacuum start is not a Hadamard state: at the descent it falls below the Bunch-Davies state by $1/(2k^{3}\eta_{d}^{2})$ per mode in $\langle\chi^{2}\rangle$, with $|\beta_{k}|^{2} = 1/(4k^{4}\eta_{d}^{4})$, and the mode sums diverge logarithmically, so its two-point function does not differ by a smooth kernel from that of an infrared-regularised Bunch-Davies comparison state, which is Hadamard (taken as given there, with the smooth-difference property of scalar Hadamard states) (Theorem \claimref{synthesis.massive-dirac-instantaneous-vacuum-and-non-smooth-descents-are-not-hadamard}(iv)). The model therefore describes a state that the Hadamard deposit premise, Premise \claimref{synthesis.hadamard-deposit-premise}, excludes. The late-time spectrum computed above, and the conclusion that this start supplies a feature and not a tilt, are unaffected.

## technical
Model the descent as an instant $\eta_d$ in the frozen phase's flat slicing at which a massless scalar starts in the instantaneous vacuum. Matching to the Bunch-Davies modes gives Bogoliubov coefficients with $|\alpha|^{2} - |\beta|^{2} = 1$ and the late-time spectrum $(H/2\pi)^{2}F(k|\eta_d|)$, with $F$ in closed form. Modes already outside the horizon at the descent are suppressed, $F \approx \tfrac49 x^{2}$, a blue cutoff with local index $+2$; modes well inside approach the flat spectrum with oscillations of relative size $x^{-2}$, bounded between $(|A| - B)^{2}$ and $(|A| + B)^{2}$.

The measured index, $n_s = 0.9649 \pm 0.0042$, needs $\ln\Delta^{2}$ to fall by at least $7 \times 0.0267$ across the seven e-folds of the measured window. Exact rational enclosures of $F$ (a Taylor bound below $x = 1$, a gridded bound with Taylor-enclosed $\cos$ and $\sin$ on $[1, 3]$, the envelope bounds above $3$) show that no window of seven e-folds has that drop. A single descent event with an instantaneous-vacuum start thus leaves a feature, not a tilt. Read as a pointer, not proved here: if the descent's state is to break the dilatation and produce the measured red tilt, the breaking would have to last while the whole observed window is set, about seven e-folds of the frozen phase if horizon exit sets the modes; other initial states are not computed. The computation is standard de Sitter field theory; the series supplies the frozen-phase setting and the claim that the descent sources the earliest correlations.

## lay
An earlier result showed that if the universe's descent into its present phase respected that phase's stretching symmetry, it could not produce the slight tilt measured in the early universe's ripples: the symmetry has to be broken. The simplest way to break it is for the descent to happen at one moment, which sets a scale. This result computes what such a sudden start does to a simple field: ripples much larger than the scale set by the moment are suppressed, ripples much smaller come out with the flat, untilted pattern, and in between the pattern rings and then settles. Nowhere does it produce the gentle, steady tilt seen across the observed range of sizes. So a sudden start of this simple kind is ruled out as the source of the tilt; the natural reading, not proved here, is that a descent producing the tilt would have to be a drawn-out process, lasting while all the observed sizes were being imprinted.

## one-liner
If the descent is a single event at $\eta_d$ into the frozen phase and a massless field starts there in the instantaneous vacuum, its spectrum is $(H/2\pi)^{2}F(k|\eta_d|)$ with $F \approx \tfrac49 x^{2}$ outside and $F \to 1$ with $x^{-2}$ ringing inside, and no seven-e-fold window carries the measured red index (exact for every window); such a sudden start does not supply the tilt.
