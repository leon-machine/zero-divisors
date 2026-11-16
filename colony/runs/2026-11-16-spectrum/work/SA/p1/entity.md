---
id: synthesis.descent-slice-constraints-and-the-three-readings-of-a-white-deposit
kind: claim
version: 1
title: 'Constraints on the descent slice and the three readings of a white deposit'
status: proved
region: synthesis
subject: dark-energy
tags: [curvature-and-field-equations, two-readings, confronted-with-data, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-16-spectrum
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-16-spectrum
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.imported-gtg-dictionary@2
  - synthesis.imported-superhorizon-zeta-conservation@3
  - synthesis.imported-large-scale-potential-and-sachs-wolfe-relations@2
  - synthesis.finite-range-descent-deposit-cannot-seed-cmb@5
  - synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise@4
  - synthesis.imported-planck-2018-lcdm-parameters@3
  - synthesis.imported-bbn-reheating-temperature-floor@1
  - hawking.i-state@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_constraints_of_the_perturbed_field_from_the_field_equation
- kind: check
  ref: check.py::check_slice_independent_combinations_and_the_poisson_relation
- kind: check
  ref: check.py::check_radiation_equation_and_the_growing_mode_projection
- kind: check
  ref: check.py::check_three_readings_and_the_index_ledger
- kind: check
  ref: check.py::check_thermal_deposit_under_uniform_expansion
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise
  - synthesis.finite-range-descent-deposit-cannot-seed-cmb
  - synthesis.holographic-thermal-fluctuations-fall-short-in-the-descent-window
  - synthesis.adiabatic-deposit-modulation-is-a-time-shift
extraction:
  open_problem: op.descent-state-and-spectrum
  note: >-
    What this adds. The stored results read a deposit's density contrast as the curvature perturbation at order
    one (the quasi-free result's clause (iv) and its "index 3"; the time-shift result's flat slice), while the
    stored thermal reading with a heat capacity converts the same kind of energy noise by the Poisson relation and
    records index -1 for an extensive capacity. Both are solutions of the constraint part of the field equations on
    the descent slice; they differ in one first-order datum of the slice that no stored premise fixes, the
    perturbation of its expansion, equivalently its first-order local density parameter. The result states the
    exact map from slice data to the growing mode in the radiation field, the three readings and their indices,
    and the numbers for the thermal deposit. Kill conditions written before computing: (a) a stored premise or
    proved result forces one reading; (b) a coefficient of the constraint differs when derived from the stored
    field equation; (c) the uniform-expansion datum is a decaying mode. None was met: (b) and (c) by exact
    computation, (a) by a search of the store that is a pattern search with reading and not an audit of every
    derivation (patterns: separate universe, uniform time, simultaneous, descent slice, spatially flat, flatness,
    junction, Weyl-flat, constraint, Poisson). Hypotheses (UE) and (LC) below are stated hypotheses of clauses, not
    postulates of the store; adopting either, or neither, is a premise decision. The result supplies no mechanism:
    index -1 and index +1 are both far from the measured index, and nothing is fitted. Literature cited from
    memory, to be checked before any import: the classification of large-scale density spectra by what a local
    rearrangement conserves (mass alone, white; mass with free momentum, $k^{2}$; mass and momentum, $k^{4}$) is
    Zel'dovich's and Peebles'; thermal fluctuations frozen outside the Hubble length giving a white spectrum is in
    Magueijo and Pogosian (2003); that the free data at an isotropic (conformally regular) initial singularity of a
    perfect fluid are the conformal 3-geometry alone, the matter being slaved, is Tod's and Anguige and Tod's
    (1999); the conformally flat constant-mean-curvature construction of initial data from a freely given density
    is York's. None is used in a proof step. Transport-absent: linearised constraints of the stored field equation
    and thermodynamic fluctuation formulas; the series supplies the setting (a deposit on a descent slice with no
    earlier metric stage to fix the slice's data). Three stored results are discussed and cited without being
    premises of any step: the time-shift result, the thermal reading with a heat capacity, and the window ceiling
    $7.3 \times 10^{8}$ GeV of the untuned fit (quoted as a temperature at which the formula of (vi) is evaluated);
    the first rests on Hypothesis (U) and the other two on Premise (EW), which exclude each other, so none is
    declared as a premise and this result rests on neither.
---

## formal
Units $\hbar = c = 1$, with Newton's constant $G$ written out (the Definition has $G = 1$). Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) with $\Lambda = 0$, a first-order scalar perturbation of the spatially flat Robertson-Walker field in conformal time $\eta$, of wavenumber $k \neq 0$ along $e_{1}$:
\[
\hb^{-1}(e_{0}) = a\,(1 + \phi\cos kx^{1})\,e_{0}, \qquad \hb^{-1}(e_{1}) = a\,(1 - \psi\cos kx^{1})\,e_{1} + a\,b\,\sin kx^{1}\,e_{0}, \qquad \hb^{-1}(e_{j}) = a\,(1 - \psi\cos kx^{1})\,e_{j}\quad(j = 2, 3),
\]
with $a$, $\phi$, $\psi$, $b$ functions of $\eta$, $\mathcal{H} = a'/a$, $H = \mathcal{H}/a$ (labelled reading: derived metric $a^{2}[(1 + 2\phi\cos kx^{1})d\eta^{2} + 2b\sin kx^{1}\,d\eta\,dx^{1} - (1 - 2\psi\cos kx^{1})\sum_{j}(dx^{j})^{2}]$). Up to the gauge freedoms of the Definition that keep the slices $\Sigma_{\eta} = \{\eta = \mathrm{const}\}$ (a rotor field, a relabelling of points within the slices) every first-order scalar perturbation with its slicing has this form. Let $n = e_{0} + b\sin kx^{1}e_{1}$ be the unit normal of the slices and $m_{1} = e_{1} + b\sin kx^{1}e_{0}$. The \emph{slice data} are: $\psi$; the expansion $\theta = D\cdot n = 3H + \kappa\cos kx^{1}$, with $\delta_{H} = \kappa/3H$; and, for matter with stress-energy $T$, the density seen by $n$, $n\cdot T(n) = \rho\,(1 + \delta\cos kx^{1})$, and its flux, $m_{1}\cdot T(n) = -(\rho + p)\,v\sin kx^{1}$ ($v$ is the matter's velocity along $e_{1}$ relative to $n$), with $u = (aH/k)\,v$ and $1 + w = (\rho + p)/\rho$.
\begin{enumerate}
\item[(i)] \emph{(Constraints.)} The first-order expansion of the normal is $a\kappa = -3(\psi' + \mathcal{H}\phi) + kb$, and the field equation $\mathcal{G}(a) = -8\pi G\,T(a)$ contracted with $n$ gives, to first order,
\[
\Bigl(\frac{k}{a}\Bigr)^{2}\psi = H\kappa - \tfrac32 H^{2}\delta, \qquad v = \frac{2k(\psi' + \mathcal{H}\phi)}{3(1 + w)\mathcal{H}^{2}} .
\]
The scalar curvature of the slice's induced field (round sphere positive) is $-4(k/a)^{2}\psi\cos kx^{1}$, so the first relation says that it equals $6H^{2}(\delta - 2\delta_{H})\cos kx^{1}$: the slice's curvature is its first-order local density parameter, $\Omega_{\Sigma} - 1 = \delta - 2\delta_{H}$ with $\Omega_{\Sigma} = 8\pi G\,n\cdot T(n)/(\theta^{2}/3)$. The slice data $(\psi, \delta, u)$ can be given freely; $\kappa$ and $b$ then follow.
\item[(ii)] \emph{(Slice-independent combinations.)} Under a first-order change of the time label, $(\phi, \psi, b) \mapsto (\phi + \xi' + \mathcal{H}\xi,\ \psi - \mathcal{H}\xi,\ b - k\xi)$, one has $u \mapsto u + \mathcal{H}\xi$ and $\delta \mapsto \delta - 3(1 + w)\mathcal{H}\xi$, so $\mathcal{R} = \psi + u$, $\zeta = -\psi + \delta/(3(1 + w))$ (the variable of Fact \claimref{synthesis.imported-superhorizon-zeta-conservation}), $\delta_{c} = \delta + 3(1 + w)u$ and $\Psi = \psi - \mathcal{H}b/k$ do not depend on the slicing; $\zeta = -\mathcal{R} + \delta_{c}/(3(1 + w))$, and on every slice $k^{2}\Psi = -\tfrac32\mathcal{H}^{2}\delta_{c}$. Here $u\cos kx^{1}$ is, up to sign, $H$ times the proper-time offset between the slice and the slice orthogonal to the matter flow, $\mathcal{R}$ is the curvature perturbation of that slice and $\delta_{c}$ its density contrast.
\item[(iii)] \emph{(The growing mode in the radiation field.)} Let the matter be a perfect fluid with $p = \rho/3$ to first order, so $a \propto \eta$. Then $\phi = \psi$ in the slicing $b = 0$, $\Psi'' + 4\Psi'/\eta + \tfrac13 k^{2}\Psi = 0$, and with $x = k\eta/\sqrt3 = k/(\sqrt3\,aH)$ the solutions are $\Psi = A_{0}\,g(x) + D\,d(x)$, $g = 3(\sin x - x\cos x)/x^{3}$, $d = (\cos x + x\sin x)/x^{3}$. The solution $d$ has $\mathcal{R} = \cos x/(2x)$ and carries no constant curvature perturbation; the solution $g$ has $\zeta = -\mathcal{R} = -\tfrac32 A_{0}$ at $x \to 0$, the constant of Fact \claimref{synthesis.imported-large-scale-potential-and-sachs-wolfe-relations} ($\Phi = \tfrac23\mathcal{R}$). Call $\zeta_{\infty} = -\tfrac32 A_{0}$ the \emph{primordial curvature perturbation} of the solution. For data on a slice $\Sigma$ at $x = x_{d}$, exactly,
\[
\zeta_{\infty} = -\bigl[\mathcal{R}_{\Sigma}\,(\cos x_{d} + x_{d}\sin x_{d}) + \tfrac14\,\delta_{c,\Sigma}\cos x_{d}\bigr]
= -\psi_{\Sigma}(\cos x_{d} + x_{d}\sin x_{d}) - \tfrac14\delta_{\Sigma}\cos x_{d} - u_{\Sigma}(2\cos x_{d} + x_{d}\sin x_{d}),
\]
and by (i), outside the Hubble length ($x_{d} \ll 1$),
\[
\zeta_{\infty} = \tfrac32\Bigl(\frac{a_{d}H_{d}}{k}\Bigr)^{2}(\Omega_{\Sigma} - 1) - \tfrac14\,\delta_{\Sigma} - 2\,\frac{a_{d}H_{d}}{k}\,v_{\Sigma} + \text{(relative corrections of order } x_{d}^{2}\text{)} .
\]
\item[(iv)] \emph{(Three readings.)} Hypothesis (UE), \emph{uniform expansion}: $\delta_{H} = 0$ on the descent slice. Then $\zeta_{\infty} = \bigl[(\cos x_{d} + x_{d}\sin x_{d})/(2x_{d}^{2}) - \tfrac14\cos x_{d}\bigr]\delta_{\Sigma} - (2\cos x_{d} + x_{d}\sin x_{d})u_{\Sigma}$, with bracket $\tfrac{1}{2x_{d}^{2}} + \tfrac{x_{d}^{2}}{16} - \dots$, so $\zeta_{\infty} = \tfrac32(a_{d}H_{d}/k)^{2}\delta_{\Sigma}$ up to relative corrections of order $x_{d}^{4}$ and the velocity term. Hypothesis (LC), \emph{local criticality}: $\Omega_{\Sigma} = 1$, that is $\delta_{H} = \tfrac12\delta$, the slice intrinsically flat. Then $\zeta_{\infty} = -\tfrac14\delta_{\Sigma}\cos x_{d} - (2\cos x_{d} + x_{d}\sin x_{d})u_{\Sigma}$. With (LC) and matter at rest on the slice ($v_{\Sigma} = 0$), $\zeta_{\infty} = -\tfrac14\delta_{\Sigma}\cos x_{d}$, and on the slice itself $\zeta = \tfrac14\delta_{\Sigma}$, $\mathcal{R} = 0$: the order-one reading of the stored results. A slice between the two, $\delta_{H} = \tfrac12(1 - \lambda)\delta$, has leading term $\tfrac32\lambda(a_{d}H_{d}/k)^{2}\delta_{\Sigma}$: with order-one term $\tfrac14(\lambda - 1)\delta_{\Sigma}$, so every $\lambda \neq 0$ is of the first kind for $k$ below about $a_{d}H_{d}\sqrt{6|\lambda|}$.
\item[(v)] \emph{(Index ledger.)} Let the deposit's contrast and longitudinal velocity on the slice be uncorrelated with spectra $P_{\delta} \propto k^{s}$, $P_{v} \propto k^{s'}$ as $k \to 0$, and $\Delta^{2} = k^{3}P/2\pi^{2}$. For $k \ll a_{d}H_{d}$: under (UE), $\Delta^{2}_{\zeta} = \tfrac94(a_{d}H_{d}/k)^{4}\Delta^{2}_{\delta} + 4(a_{d}H_{d}/k)^{2}\Delta^{2}_{v}$, index $n_{s} - 1 = s - 1$ when $s \le s' + 2$; under (LC), $\Delta^{2}_{\zeta} = \tfrac1{16}\Delta^{2}_{\delta} + 4(a_{d}H_{d}/k)^{2}\Delta^{2}_{v}$, index $s' + 1$ when $s' \le s + 2$, and $s + 3$ only when the velocity term is absent. For a white deposit ($s = s' = 0$) the three readings give $-1$, $+1$ and $+3$. Under (UE) a white contrast is a perturbation only on a band with an infrared end, since $\int\Delta^{2}_{\zeta}\,dk/k$ diverges at small $k$.
\item[(vi)] \emph{(The thermal deposit.)} For a thermal state of massless quanta at temperature $T_{d}$ with $\rho = \tfrac{\pi^{2}}{30}g\,T_{d}^{4}$ (for the fermion modes the Fermi-Dirac occupations of the I-state, Theorem \claimref{hawking.i-state}, as read on the descent slice in Theorem \claimref{synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise}(iv)), at rest on the slice, $P_{\delta} = 4T_{d}/\rho$ and $P_{v} = T_{d}/(\rho + p) = \tfrac{3}{16}P_{\delta}$ for $k \ll a_{d}T_{d}$ (physical volume). Under (UE), with $H_{d} = \pi\sqrt{g/90}\,T_{d}^{2}/\bar M_{P}$,
\[
\Delta^{2}_{\zeta}(k) = \frac{135}{\pi^{4}g}\Bigl(\frac{H_{d}}{T_{d}}\Bigr)^{3}\frac{a_{d}H_{d}}{k}, \qquad \Delta^{2}_{\zeta}(k_{*}) = \frac{g^{2/3}g_{s0}^{1/3}}{60}\Bigl(\frac{T_{d}}{\bar M_{P}}\Bigr)^{4}\frac{a_{0}T_{0}}{k_{*}},
\]
the second with entropy conserved from the descent ($g_{s0} = 43/11$) and the record values of Fact \claimref{synthesis.imported-planck-2018-lcdm-parameters}: between $2 \times 10^{-60}$ and $3 \times 10^{-60}$ at $T_{d} = 1$ MeV ($g = 10.75$); between $3.4 \times 10^{-12}$ and $3.6 \times 10^{-12}$ at the ceiling $7.3 \times 10^{8}$ GeV of the window under Premise (R) (Proposition \claimref{synthesis.untuned-fit-caps-lightest-heavy-neutrino}; $g = 106.75$), below $A_{s}$ at the pivot by a factor between $580$ and $620$ but, the index being $-1$, between $0.36$ and $0.39$ of $A_{s}$ at $k = a_{0}H_{0}$; equal to $A_{s}$ for $T_{d}$ between $3.6 \times 10^{9}$ and $3.7 \times 10^{9}$ GeV; between $12$ and $13$ at $10^{12}$ GeV, where the reading is not a perturbation. At the ceiling the infrared end of (v) lies beyond $1.2 \times 10^{9}$ present Hubble radii. Under (LC) the same deposit gives $\Delta^{2}_{\zeta} = \tfrac1{16}\bigl(1 + 12(a_{d}H_{d}/k)^{2}\bigr)\Delta^{2}_{\delta}$, index $+1$, with $\Delta^{2}_{\delta}(k_{*})$ between $3.9 \times 10^{-82}$ and $4.1 \times 10^{-82}$ for the whole bath, so below $4 \times 10^{-41}$ at the pivot for every $T_{d} \le 10^{12}$ GeV.
\item[(vii)] \emph{(Where the stored results stand; argued.)} The bound of Proposition \claimref{synthesis.finite-range-descent-deposit-cannot-seed-cmb}(i) is a statement about a covariance of $\zeta$ and is not affected. A deposit of matter of finite range does not have $\zeta$ of finite range unless (LC) holds and its longitudinal momentum is compensated: under (UE) its $\zeta$ is the potential of its excess, of infinite range. Clause (iv) of Theorem \claimref{synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise} bounds $\Delta^{2}_{\delta}$; its reading as the primordial spectrum ("index $3$", "below $10^{-77}$ at the pivot") is the reading (LC) with matter at rest. The flat slice in the proof of Proposition \claimref{synthesis.adiabatic-deposit-modulation-is-a-time-shift} is (LC) for classical modulations: with the patch's own curvature as a fourth local datum the term $\tfrac32(a_{d}H_{d}/k)^{2}(\Omega_{\Sigma} - 1)$ is added. The thermal reading of Proposition \claimref{synthesis.holographic-thermal-fluctuations-fall-short-in-the-descent-window} uses the Poisson conversion, the reading (UE), and its "extensive capacity gives $-1$" is the index of the first formula of (vi). No stored premise was found that fixes $\delta_{H}$ on the descent slice.
\end{enumerate}

## technical
The gravitational gauge fields on a slice are not free data once the matter on it is given: the part of the field equation contracted with the slice's normal is a constraint. To first order around the flat Robertson-Walker field it says that the intrinsic curvature of the slice is $6H^{2}$ times the slice's local density parameter minus one, $\delta - 2\delta_{H}$: a patch that is denser than average is curved unless it also expands faster by half the excess. So the matter's contrast on the descent slice does not determine the slice's curvature perturbation; the perturbation of the slice's expansion is a second, independent datum, and a deposit laid down in one event with no earlier metric stage has nothing that fixes it.

In the radiation field the conversion to the constant curvature perturbation outside the Hubble length is exact and linear in three slice data: the local density parameter, enhanced by $(a_{d}H_{d}/k)^{2}$; the matter's longitudinal velocity, enhanced by $a_{d}H_{d}/k$; and the contrast itself at order one, with coefficient $-\tfrac14$. The decaying solution is projected out by a closed formula, since its comoving curvature perturbation is $\cos x/(2x)$. Two pure hypotheses bracket the readings. If the slice expands uniformly, a white matter deposit has a curvature perturbation of infinite range, the potential of its mass excess, with index $-1$ and amplitude larger than the contrast's by $\tfrac94(a_{d}H_{d}/k)^{4}$, at the pivot a factor between $5 \times 10^{21}$ and $7 \times 10^{21}$ for a descent at $1$ MeV and between $2.5 \times 10^{82}$ and $3.2 \times 10^{82}$ at $10^{12}$ GeV. If every patch is critical, the slice is flat and the stored order-one reading holds, but only when the deposit's momentum noise is also absent; a thermal deposit has white momentum noise, and then the index is $+1$, not $3$. The three indices $-1$, $+1$, $+3$ are the classical ladder for density spectra according to whether mass, momentum, or neither is left uncompensated.

For the thermal deposit under uniform expansion the amplitude at the pivot has a closed form in which $\pi$ cancels. It is of order $10^{-60}$ at the nucleosynthesis floor, $3.5 \times 10^{-12}$ at the window's ceiling under Premise (R), equal to the measured amplitude near $3.6 \times 10^{9}$ GeV and above one at $10^{12}$ GeV. Its index is $-1$, so it is not a candidate for the measured spectrum at any temperature; what the reading would give is an upper limit on the descent's temperature from the largest observed scales, not derived here. The store already uses both conversions, in different results, without a premise that chooses: the quasi-free and time-shift results read the contrast at order one, and the thermal reading with a heat capacity uses the Poisson relation. The finite-range bound itself is about $\zeta$ and stands. The dynamic clause is stated for a perfect radiation fluid; for free quanta the anisotropic stress noise changes the order-one coefficient by a term of the same order and leaves the two enhanced terms unchanged (argued).

## lay
The theory starts the universe with one event that lays down hot matter. Earlier results asked whether the random unevenness of that matter could be the seed of the ripples seen in the cosmic background, and answered no, by a huge margin, after reading the unevenness of the matter directly as the ripple. This result shows that the reading was a choice. Gravity ties the matter in a region to the shape of space there by a rule that involves a third quantity: how fast that region is expanding. If every region started expanding at the same rate, the denser regions are curved, and on very large scales the ripple is enormously larger than the matter's unevenness and strongest on the largest scales. If instead every region started with exactly the expansion rate that matches its own density, space is flat everywhere and the earlier reading holds, provided the matter also has no random drift. Nothing in the theory says which start is the right one. Neither gives the observed ripples: one is far too tilted towards large scales, the other far too weak and tilted the other way. The gain is that a hidden assumption in several earlier results now has a name, and that under the first reading the theory's own hot start would be visible on the largest scales unless it was cooler than a few billion GeV.

## one-liner
On a slice of a perturbed flat Robertson-Walker field the constraint is $\,^{3}R = 6H^{2}(\delta - 2\delta_{H})$, and in the radiation field $\zeta_{\infty} = \tfrac32(a_{d}H_{d}/k)^{2}(\delta - 2\delta_{H}) - \tfrac14\delta - 2(a_{d}H_{d}/k)v$ outside the Hubble length (exactly $-[\mathcal{R}(\cos x + x\sin x) + \tfrac14\delta_{c}\cos x]$): a white deposit reads as index $-1$ under uniform expansion, $+1$ on a flat slice with momentum noise, $+3$ only on a flat slice at rest, and no stored premise chooses; the thermal deposit under uniform expansion has $\Delta^{2}_{\zeta}(k_{*}) = \tfrac{1}{60}g^{2/3}g_{s0}^{1/3}(T_{d}/\bar M_{P})^{4}a_{0}T_{0}/k_{*}$, equal to $A_{s}$ near $3.6 \times 10^{9}$ GeV.
