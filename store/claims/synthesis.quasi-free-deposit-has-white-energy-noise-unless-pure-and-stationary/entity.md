---
id: synthesis.quasi-free-deposit-has-white-energy-noise-unless-pure-and-stationary
kind: claim
version: 1
title: 'Homogeneous gauge-invariant quasi-free deposit: white energy noise unless pure, stationary'
status: proved
region: synthesis
subject: dark-energy
tags: [car-algebra, no-go, confronted-with-data, needs-continuum]
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
derivations:
- name: main
  uses:
  - synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise@5
  - synthesis.descent-slice-constraints-and-the-three-readings-of-a-white-deposit@1
  - hawking.imported-quasi-free-states-car-algebra@2
  - synthesis.imported-string-gas-thermal-spectrum-and-conversion@1
  - synthesis.imported-large-scale-potential-and-sachs-wolfe-relations@2
  - synthesis.imported-planck-2018-lcdm-parameters@3
  - synthesis.quadratic-flows-cannot-thermalise-descent@3
  - synthesis.finite-range-descent-deposit-cannot-seed-cmb@6
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_zero_momentum_noise_of_a_weyl_state_in_cl30
- kind: check
  ref: check.py::check_fermi_ball_overlaps_and_structure_factors
- kind: check
  ref: check.py::check_index_amplitude_and_thermal_crossover_under_the_conversion
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise
  - synthesis.holographic-thermal-fluctuations-fall-short-in-the-descent-window
  - synthesis.quadratic-flows-cannot-thermalise-descent
extraction:
  maintainer_pass_2026_11_16:
    by: maintainer-2026-11-16
    date: '2026-11-16'
    note: 'Edges, version kept: uses edge added to synthesis.descent-slice-constraints-and-the-three-readings-of-a-white-deposit at version 1, which supplies the coefficient 3/2 of Hypothesis (UE) (cited by claimref in clause (iv) and in the proof; listed in coverage.yaml as a premise the check takes as stated); the pin to synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise moved 4 -> 5 (clauses (i) and (iv) there are unchanged). The name (UE_Phi) of the 9/4 variant is kept. No number or clause changed.'
  open_problem: op.descent-state-and-spectrum
  note: >-
    What this adds to the stored shot-noise bound. The bound says a quasi-free deposit exceeds the vacuum by at
    most its shot noise; this result says when the shot noise of the energy is absent at long wavelengths and what
    replaces it. Within homogeneous gauge-invariant quasi-free states the white term vanishes exactly for pure
    stationary states (filled energy bands up to a Fermi surface); every state with entropy, and every pure state
    of pairs, keeps it. For the filled ball the excess over the vacuum is linear in $k$ with exact corrections.
    Read on a descent slice of uniform expansion (Hypothesis (UE) of the statement, a hypothesis and not a premise:
    by Leon's decision of 16 November 2026 the descent slice is left free and no reading is adopted; the stored
    thermal reading uses the variant (UE$_{\Phi}$) through the imported string-gas conversion) a white term gives
    index $-1$ and the filled ball gives $n_{s} = 1$: a miss, between $8.3$ and $8.4$ standard deviations from the
    measured index, with an amplitude fixed by the Hubble rate alone and short by more than $10^{17}$ on the
    window. Kill conditions written before computing:
    (a) the energy structure factor of the filled ball does not vanish linearly at $k = 0$ (not met: it is
    $\tfrac{k_{F}^{4}k}{8\pi^{2}}(1 - \ell^{3}/30 + \ell^{4}/96)$); (b) the amplitude at a Fermi momentum of the
    window is within $10^{3}$ of the measured one (not met); (c) the stored deposit cannot be pure (met: clause
    (vi), so the scale-invariant row is a statement about a deposit the stored state rules exclude, and the stored
    deposit's row under (UE) is index $-1$, argued). Nothing is fitted. Two one-parameter families reach the
    measured index and are recorded as fits, not candidates: a thermal sea at $k/aT$ between $19.1$ and $19.3$ (running
    $+0.069$) and an occupied region whose boundary has box dimension $2.0351$ (argued). A Planck value of the
    running is not a stored Fact and is not used at any statement level (from memory, flagged:
    $-0.0045 \pm 0.0067$, Planck 2018). Literature from memory, none used in a proof step: the static structure
    factor $3k/4k_{F} - k^{3}/16k_{F}^{3}$ of the free Fermi gas is textbook; a structure factor vanishing linearly
    is Torquato's class II of hyperuniform systems, to which Gabrielli, Joyce and Sylos Labini (2002) assign the
    Harrison-Zel'dovich spectrum; the number variance of a Fermi sea in a sharp ball grows as $R^{2}\ln R$ (Gioev
    and Klich 2006). Hypothesis (UE) is the uniform-expansion reading of the result on the descent slice's constraints
    (synthesis.descent-slice-constraints-and-the-three-readings-of-a-white-deposit), where the coefficient
    $\tfrac32$ is derived; that result is a declared premise of this one (uses edge added on 16 November 2026).
    The letter $\ell = k/k_{F}$ is used for the wavenumber in units of the Fermi momentum, $X = a_{d}H_{d}/k$ for
    the Hubble ratio; $\kappa$ is not used here (it is the slice's expansion perturbation in that result).
    Transport-absent: free-fermion statistics and one constraint of the field equations; the Clifford algebra
    enters as the language of the one-particle space of a Weyl field.
---

## formal
Let $\CAR$ be the CAR algebra of the fermion modes on a slice, as in Theorem \claimref{synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise}, and $\omega$ a homogeneous gauge-invariant quasi-free state (Fact \claimref{hawking.imported-quasi-free-states-car-algebra}): its one-particle density is $E = \bigoplus_{p}E_{p}$, $0 \le E_{p} \le 1$, on the band space at momentum $p$, on which the one-particle Hamiltonian is $H_{p}$. For the cosine and sine moments $C$, $S$ of the energy density over a box of volume $V$ at wave vector $k$, with one-body form $\tfrac12(cH + Hc)$ as in clause (iv) of that theorem, put $S_{E}(k) = \lim_{V}(\mathrm{Var}\,C + \mathrm{Var}\,S)/V$, so that the contrast of the energy has spectrum $P_{\delta}(k) = S_{E}(k)/\bar\rho^{2}$. By clause (i) of that theorem,
\[
S_{E}(k) = \int\tr\bigl[\varepsilon_{k}(p)\,E_{p}\,\varepsilon_{k}(p)^{\dagger}\,(1 - E_{p + k})\bigr]\frac{d^{3}p}{(2\pi)^{3}}, \qquad \varepsilon_{k}(p) = \tfrac12(H_{p + k} + H_{p}),
\]
(averaged over $\pm k$ when the state is not symmetric under $k \mapsto -k$).
\begin{enumerate}
\item[(i)] \emph{(The white term.)} $S_{E}(0) = \int\tr[H_{p}E_{p}H_{p}(1 - E_{p})]\,d^{3}p/(2\pi)^{3} \ge 0$, and the integrand vanishes exactly when $H_{p}$ maps the range of $E_{p}$ into the eigenspace $E_{p} = 1$; where $H_{p}$ has no kernel, exactly when $E_{p}$ is a projection commuting with $H_{p}$. So $S_{E}(0) = 0$ if and only if the state is pure and stationary (up to zero modes of $H$); here stationary means $E_{p}H_{p} = H_{p}E_{p}$ for almost every $p$, invariance under the slice's one-particle dynamics generated by $H$, not under the cosmological evolution. The white term of the spectrum is $\lim_{k \to 0}S_{E}(k)$; it equals $S_{E}(0)$ when $E_{p}$ is continuous off a null set and the integrand is dominated, as for the filled ball of (iii), where the limit is zero linearly. The corresponding term of a momentum component is $\int p_{1}^{2}\tr[E_{p}(1 - E_{p})]\,d^{3}p/(2\pi)^{3}$, which vanishes exactly for pure states, stationary or not.
\item[(ii)] \emph{(One Weyl field, in $\Cl(3,0)$.)} Let the band space at $p$ be a minimal left ideal of $\Cl(3,0)$, with $H_{p}$ left multiplication by the vector $p$ (eigenvalues $\pm|p|$, spectral idempotents $P_{\pm}(p) = \tfrac12(1 \pm p/|p|)$), and $E_{p} = \tfrac12(\nu_{p} + \mu_{p})$ with a scalar $\nu_{p}$ and a vector $\mu_{p}$, $|\mu_{p}| \le \min(\nu_{p}, 2 - \nu_{p})$. Then
\[
\tr[H_{p}E_{p}H_{p}(1 - E_{p})] = \tfrac12\,p^{2}\bigl(\nu_{p}(2 - \nu_{p}) - \mu_{p}^{2}\bigr) + |p\wedge\mu_{p}|^{2}, \qquad \tr[E_{p}(1 - E_{p})] = \tfrac12\bigl(\nu_{p}(2 - \nu_{p}) - \mu_{p}^{2}\bigr),
\]
with $|p\wedge\mu|^{2} = p^{2}\mu^{2} - (p\cdot\mu)^{2}$. The first term is $p^{2}$ times $\sum n(1 - n)$ over the two eigen-occupations of $E_{p}$ and vanishes for pure states; the second is the squared bivector $p\wedge\mu_{p}$ and vanishes when $E_{p}$ commutes with $H_{p}$. Three classes: a stationary mixed state ($\mu \parallel p$, occupations $n$, $1 - n$ in $(0,1)$) has $2p^{2}n(1 - n)$ and momentum noise; a pure state of pairs ($\nu = 1$, $\mu = m$ a unit vector not parallel to $p$) has $|p\wedge m|^{2} = 4p^{2}n(1 - n)$, $n = \tfrac12(1 - m\cdot p/|p|)$, and no momentum noise; a pure stationary state ($E_{p} = P_{\pm}(p)$, $0$ or $1$) has neither.
\item[(iii)] \emph{(The filled ball.)} For the Weyl field with the negative band filled and the positive band filled for $|p| \le k_{F}$, the excess of $S_{E}$ over the vacuum's (negative band filled; the difference of the two integrands is integrable) is, for $\ell = k/k_{F} \le 1$ ($k$ and $k_{F}$ in the same units), exactly
\[
S_{E}(k) - S_{E}^{\mathrm{vac}}(k) = \frac{k_{F}^{4}\,k}{8\pi^{2}}\Bigl(1 - \frac{\ell^{3}}{30} + \frac{\ell^{4}}{96}\Bigr),
\]
the sum of a particle-hole part $\tfrac{k_{F}^{5}}{4\pi^{2}}(\tfrac{\ell}{2} - \tfrac{\ell^{5}}{320})$ and minus the Pauli-blocked part $\tfrac{k_{F}^{5}}{4\pi^{2}}(\tfrac{\ell^{4}}{60} - \tfrac{\ell^{5}}{120})$ of the vacuum's pair term. With $\bar\rho = k_{F}^{4}/8\pi^{2}$ per field and $g$ independent fields filled alike, $\Delta^{2}_{\delta}(k) = k^{3}P_{\delta}/2\pi^{2} = \tfrac{4}{g}\ell^{4}(1 - \ell^{3}/30 + \ell^{4}/96)$. (For comparison, the number structure factor of one band with trivial overlap is $\tfrac34\ell - \tfrac1{16}\ell^{3}$ for $\ell \le 2$, and with the Weyl overlap its particle-hole part is $\tfrac34\ell - \tfrac{5}{32}\ell^{3}$ for $\ell \le 1$.)
\item[(iv)] \emph{(Index and amplitude on a slice of uniform expansion.)} Hypothesis (UE), a hypothesis of this clause and of (v) and (vi) and not a premise (the descent slice's expansion datum is left free): the descent slice expands uniformly, so that outside the descent's Hubble length the primordial curvature perturbation is $\zeta_{\infty} = \tfrac32X^{2}\delta$, $X = a_{d}H_{d}/k \gg 1$. This is the Poisson relation $(k/a)^{2}\psi = -4\pi G\rho\,\delta$ with the potential the curvature perturbation of the slice (reading (UE) of Proposition \claimref{synthesis.descent-slice-constraints-and-the-three-readings-of-a-white-deposit}, where the coefficient $\tfrac32$ is derived; only spectra enter below, so the sign convention of $\zeta$ plays no part). Named variant (UE$_{\Phi}$): the same potential read instead as the Bardeen potential of the growing solution, as in Fact \claimref{synthesis.imported-string-gas-thermal-spectrum-and-conversion} with $\Phi = \tfrac23\mathcal{R}$ (Fact \claimref{synthesis.imported-large-scale-potential-and-sachs-wolfe-relations}); it gives $\zeta_{\infty} = \tfrac94X^{2}\delta$, every amplitude below multiplied by $\tfrac94$, and the same indices. Under (UE), $\Delta^{2}_{\zeta} = \tfrac94X^{4}\Delta^{2}_{\delta}$ and a contrast with $P_{\delta} \propto k^{s}$ gives $n_{s} - 1 = s - 1$: a state with white term gives $-1$, and the filled ball gives $\Delta^{2}_{\zeta} = \tfrac{9}{g}(H_{d}/k_{F})^{4}(1 - \ell^{3}/30 + \ell^{4}/96)$, so $n_{s} - 1 = -\tfrac{1}{10}\ell^{3} + O(\ell^{4})$ with $\ell = k/(a_{d}k_{F})$: $n_{s} = 1$ on observed scales, between $8.3$ and $8.4$ standard deviations from the measured $n_{s} - 1 = -0.0351 \pm 0.0042$ (Fact \claimref{synthesis.imported-planck-2018-lcdm-parameters}). If the filled fields carry the density, $3H_{d}^{2}\bar M_{P}^{2} = g k_{F}^{4}/8\pi^{2}$, the amplitude does not depend on $g$ or $k_{F}$:
\[
\Delta^{2}_{\zeta} = \frac{3H_{d}^{2}}{8\pi^{2}\bar M_{P}^{2}} = \frac{\rho}{8\pi^{2}\bar M_{P}^{4}} \qquad \bigl(\text{variant (UE}_{\Phi}\text{)}: \ \frac{27H_{d}^{2}}{32\pi^{2}\bar M_{P}^{2}}\bigr).
\]
Under (UE) it is between $3.5 \times 10^{-39}$ and $3.7 \times 10^{-39}$ at the energy density of a thermal bath at $7.3 \times 10^{8}$ GeV (the ceiling of the stored window; $g = 106.75$ there) and between $1.2 \times 10^{-26}$ and $1.3 \times 10^{-26}$ at that of $10^{12}$ GeV, more than $10^{17}$ below $A_{s}$; it equals $A_{s}$ at $\rho^{1/4}$ between $4.9 \times 10^{16}$ and $5.0 \times 10^{16}$ GeV ($H_{d}$ between $5.6 \times 10^{14}$ and $5.8 \times 10^{14}$ GeV), above the ceiling's energy scale by more than $2.7 \times 10^{7}$.
\item[(v)] \emph{(Thermal smearing; computed in the proof.)} For the sea at temperature $T \ll k_{F}$ and $k \ll k_{F}$, $S_{E}(k) = S_{E}^{T = 0}(k)\,F(k/T)$ with $F(y) = 2\int_{0}^{1}\mu\operatorname{coth}(\tfrac12 y\mu)\,d\mu$: $F = 4/y + y/9 + \dots$ for $y \ll 1$ (white, $S_{E}(0) = 4\bar\rho T$) and $F = 1 + 2\pi^{2}/3y^{2}$ up to exponentially small terms for $y \gg 1$. Under (UE) the index is $-1$ for $k/a_{d} \ll 4T_{d}$ and $-2e/(1 + e)$, $e = 2\pi^{2}T_{d}^{2}a_{d}^{2}/3k^{2}$, above; the measured index is reached where $k/(a_{d}T_{d})$ is between $19.1$ and $19.3$, with running $dn_{s}/d\ln k = t(2 - t) = +0.06896799$ at $t = 0.0351$ (a white term added to a linear one, $S = S(0) + ck$, would give $t(1 - t) = +0.03386799$). So scale invariance on the observed band needs $a_{d}T_{d}$ well below the smallest observed wavenumber.
\item[(vi)] \emph{(The stored deposit; argued.)} Under the dynamics (L$_{E}$) permits, occupations are conserved (Theorem \claimref{synthesis.quadratic-flows-cannot-thermalise-descent}), so the entropy of a quasi-free deposit is the record's, and with entropy conserved from the descent (as in Proposition \claimref{synthesis.finite-range-descent-deposit-cannot-seed-cmb}(iii)) the stored thermal deposit has $k_{*}/(a_{d}T_{d}) < 2 \times 10^{-26}$ (the proof of clause (iv) of Theorem \claimref{synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise}): it is in the white regime of (v), $k_{*}/(4a_{d}T_{d}) < 5 \times 10^{-27}$, and a pure stationary deposit is excluded. A purification by partner modes on the slice removes the white term only if the joint state is pure and stationary, by (i): the partners degenerate with their modes in momentum and energy and each pair a superposition of one quantum in the mode or in the partner. Then the partners hold at least $1 - n_{p}$ quanta at every momentum the modes occupy, an energy density of at least $\int\omega_{p}(1 - n_{p})\,d^{3}p/(2\pi)^{3}$, which diverges for Fermi-Dirac occupations. The stored pair states, $c\ket{00} + s\ket{11}$ of a mode and a partner, are not stationary when both carry positive energy on the slice and keep a white term, $4\omega^{2}n(1 - n)$ per pair in the form of (ii). So for the stored deposit Hypothesis (UE) gives index $-1$, and the scale-invariant row of (iv) is a statement about a deposit that the stored state rules do not produce.
\end{enumerate}

## technical
The stored bound caps the long-range fluctuations of any quasi-free fermion deposit by its shot noise. Shot noise of the energy is white: its spectrum tends to a constant at long wavelengths. This result asks when that constant vanishes. The variance of the total energy in a large region is $\Tr(HEH(1 - E))$ per unit volume, and it has two sources that the Clifford form of a Weyl field separates: a term proportional to $n(1 - n)$, the mixedness of the occupations, and the squared bivector $p\wedge\mu$, which measures how far the state's polarisation $\mu$ is from the momentum, that is, how far the state is from stationary. Thermal deposits have the first; pure states of pairs, such as pair creation produces, have the second (and no momentum noise); only filled bands have neither.

For a filled ball the energy fluctuations at wave vector $k$ come from the shell of states that a shift by $k$ carries across the Fermi surface, a volume linear in $k$, and the bipolar integrals are polynomials: the excess over the vacuum is $\tfrac{k_{F}^{4}k}{8\pi^{2}}$ up to relative corrections $\ell^{3}/30$ from the Pauli blocking of vacuum pairs. A structure factor linear in $k$ is the hyperuniform class to which the scale-invariant spectrum belongs (literature, from memory): read on a slice of uniform expansion, Hypothesis (UE), it gives equal power per logarithmic interval, with no parameter. That is $n_{s} = 1$, the same value as the stored thermal reading with an area-law heat capacity, here from the algebra's own statistics; it misses the measured index by between $8.3$ and $8.4$ standard deviations. The amplitude is also parameter-free once the sea carries the density, $3H_{d}^{2}/8\pi^{2}\bar M_{P}^{2}$, and reaches the measured value only at an energy scale between $4.9 \times 10^{16}$ and $5.0 \times 10^{16}$ GeV, more than $2.7 \times 10^{7}$ above the energy scale of the stored window's ceiling. (UE) is one of the readings the series leaves open, not a premise; on a flat slice the same sea is blue.

The scale-invariant row needs the deposit to be pure on the observed scales themselves. At temperature $T$ the spectrum is white below $k \approx 4aT$; the measured tilt is crossed at $k/aT$ between $19.1$ and $19.3$ with a running of $t(2 - t) = 0.06896799$, a fit of one number with a large positive running. The stored deposit is thermal with the record's entropy, more than twenty-six orders inside the white regime, so under (UE) its index is $-1$ (argued, clause (vi)). The variance of the number in a sharp ball of radius $R$ grows as $R^{2}\ln R$; the logarithm belongs to the sharp boundary and not to the spectrum, which has no logarithm (argued). An occupied region whose boundary is not rectifiable would give a structure factor $\propto k^{3 - D}$, $D$ the box dimension of the boundary, and an index $2 - D$: the measured index for $D = 2.0351$, a fit of one number (argued).

## lay
Earlier work showed that the particles laid down at the universe's first event can only produce ripples as large as their own random counting noise. This result looks at the long-wavelength part of that noise. It shows that the noise in the energy has two independent causes, heat and the creation of particle pairs, and that it disappears at long wavelengths only for a perfectly cold, perfectly still sea of particles filling every state up to a maximum momentum. Such a sea has a particular property: read through one assumed link between matter and gravitational potential (one of the readings the series leaves open), it gives ripples of equal strength on every scale, with no adjustable number. That is close to what is observed, but not it: the observed ripples are slightly stronger on large scales, and the difference is more than eight times the measurement's uncertainty. The sea would also have to be far denser than the theory's first event allows, and it would have to be free of heat on the scale of the whole visible universe, whereas the event the theory describes is hot. For a hot deposit the same assumed link gives ripples that grow in proportion to the scale, which is not observed either.

## one-liner
For a homogeneous gauge-invariant quasi-free state the energy's white term is $\int\tr[HEH(1 - E)]$, for a Weyl field $\tfrac12p^{2}(\nu(2 - \nu) - \mu^{2}) + |p\wedge\mu|^{2}$ per momentum, zero only for pure stationary states; the filled ball has excess $\tfrac{k_{F}^{4}k}{8\pi^{2}}(1 - \ell^{3}/30 + \ell^{4}/96)$, which on a descent slice of uniform expansion, Hypothesis (UE), gives $n_{s} = 1$ (between $8.3$ and $8.4$ standard deviations off) with $\Delta^{2}_{\zeta} = 3H_{d}^{2}/8\pi^{2}\bar M_{P}^{2}$, short by more than $10^{17}$ on the window, while under (UE) any deposit with entropy gives index $-1$ (for the stored deposit, argued).
