---
id: synthesis.sheet-relic-bounds-under-e-fix-the-coupling-not-the-cells-mass
kind: claim
version: 1
title: 'Sheet relics under E: survival and clusters bound the coupling, not the cell''s mass'
status: proved
region: synthesis
subject: dark-matter
tags: [halos-and-clusters, confronted-with-data, dark-matter-ratio]
proposed_by:
  kind: ai
  session: 2026-11-24-unit-ball-t14c
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'direction: the tension between the unit-ball rule and T14c'
- name: Claude Fable 5.2
  role: 'proposal, mathematics, check and drafting'
  source: run 2026-11-24-unit-ball-t14c
- name: Claude Opus 5.5
  role: 'blind referee: the logarithm''s dependence on the mass, the regime condition, the fixed-size reading at composite strength, the one-length clause'
  source: run 2026-11-24-unit-ball-t14c
review: draft
derivations:
- name: main
  uses:
  - dark-matter.projection-every-towers-content-dilutes-ones@3
  - dark-tower-matter.three-dimensional-phases@4
  - simulations.imported-low-energy-scattering-two-dimensions@1
  - simulations.imported-bullet-cluster@1
  assumes:
  - dark-matter.e-equal-mass-per-unit-ball@1
  - dark-matter.r3-one-cell-per-unshared-direction@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_sheet_density_is_fixed_by_e_alone
- kind: check
  ref: check.py::check_depletion_scales_as_x_and_the_mass_cancels_in_phase_t
- kind: check
  ref: check.py::check_phase_t_floor_on_the_coupling
- kind: check
  ref: check.py::check_cluster_bound_scales_as_x_and_loses_the_mass
- kind: check
  ref: check.py::check_full_strength_puts_the_bound_on_the_mass
- kind: check
  ref: check.py::check_one_length_and_the_five_dimensional_depth
lineage:
  motivated_by:
  - dark-matter.unit-ball-rule
  - dark-tower-matter.survival-sheets
  - dark-tower-matter.r1-has-no-mechanism-odd-towers
  - dark-tower-matter.towers-built
  - dark-tower-matter.five-dimensional-towers
  - simulations.cluster-bound-two-dimensions
  - synthesis.dark-to-baryon-total-uses-r1-r2-and-d-only-as-mass-per-unit-ball
extraction:
  open_problem: op.thickness-deposit-rule
  note: >-
    Written to resolve a tension between two stored statements. The unit-ball rule (version 7) rests on E and R3 and
    says the quanta do not enter; the T14c results on the three-dimensional towers are stated at the particle model
    (R1 and R2: the nucleon's mass, one quantum per unit ball), and two of their sentences, "the viable phase needs
    m/e^2 below 1.1 to 1.5e-8, which nothing in the content protects" and "strong coupling with an unprotected light
    mass", read as requirements on the towers. This result redoes the same estimates on E and R3 alone. Its formulas
    are the source's (verify_T14c.py, K3 and K4; T14b Proposition 3.1 and Computation 3.3); what is new is that the
    cell's mass and the common length are left free. The edges are drawn so that R1 and R2 are not in the past cone:
    the depletion law is re-derived in the proof and not taken from dark-tower-matter.survival-sheets, and the
    cluster bound is recomputed from the imported bound and not taken from simulations.cluster-bound-two-dimensions,
    both of which hold given R1 and R2. Clause (vi) uses the model of the source's K7 as a stated hypothesis and
    draws no edge to dark-tower-matter.five-dimensional-towers, for the same reason. Referee corrections applied
    (blind, one round): the mass enters through the logarithm; the scaling of phase (T) needs e^2 well above m, so
    what is removed is the 1e-8 requirement and not every condition on the ratio; the composite-strength statement
    is split by what a composite's size does; and the common length cannot be lowered freely, since it is the
    five-dimensional towers' depth. Assumes edges to E and R3 are drawn for the maintainer to confirm.
---

## formal
\emph{Setting.} Assume Premise E (\claimref{dark-matter.e-equal-mass-per-unit-ball}) and Premise R3 (\claimref{dark-matter.r3-one-cell-per-unshared-direction}), and nothing about a tower's quanta. A three-dimensional tower ($r = 1, 7$) holds cells of mass $m$ on sheets one length $d$ apart, comoving, in the sourcing rule of Lemma \claimref{dark-matter.projection-every-towers-content-dilutes-ones}; $d$ is E's common length, taken comoving and quoted at its present value. Write $\rho_{b}$ for this world's present baryon density, $m_{N} = 0.938$ GeV for the nucleon mass, $d_{b} = (3m_{N}/4\pi\rho_{b})^{1/3} \approx 0.98$ m for this world's baryon spacing, and
\[
X \;=\; \frac{d}{d_{b}}\Bigl(\frac{m_{N}}{m}\Bigr)^{2} .
\]
The particle model (R1 and R2, \claimref{dark-matter.r1-equal-mass-per-quantum}, \claimref{dark-matter.r2-one-quantum-per-unit-ball}) is the point $m = m_{N}$, $d = d_{b}$, where $X = 1$. All numbers are decimal estimates of the order-of-magnitude kind the source's are, at $g = 3.36$, $10.75$ and $106.75$ relativistic species and $\ln(a_{f}/a_{i}) = 25.8$.
\begin{enumerate}
\item[(i)] \emph{(The sheet density does not see the cells.)} The comoving mass per unit area of a sheet is
\[
\Sigma \;=\; \tfrac{4}{3}\,\rho_{b}\,d ,
\]
whatever the cells weigh and however many they are; the number per unit area is $\Sigma/m$. At $d = d_{b}$, $\Sigma$ is one nucleon mass per disc of radius $d_{b}$, the particle model's density.
\item[(ii)] \emph{(Survival.)} For a symmetric population annihilating in its sheet with $\sigma_{1}v = 2P/m$, $P$ the absorption probability per encounter, in radiation domination
\[
\frac{1}{N_{f}} \;=\; \frac{1}{N_{0}} + \frac{2P}{m}\,\frac{\ln(a_{f}/a_{i})}{a^{2}H}, \qquad N_{0} = \frac{\Sigma}{m},
\]
so the depletion term $N_{0}/N_{f} - 1 = 2P\,\Sigma\ln(a_{f}/a_{i})/(m^{2}a^{2}H)$ is $X$ times its value at the particle model. The relic keeps $99$ percent of its number exactly when $P\,X \le P_{\max}$, with $P_{\max}$ between $1.2 \times 10^{-16}$ and $2.2 \times 10^{-16}$ over the three values of $g$.
\item[(iii)] \emph{(Phase (T): the mass cancels.)} In the topologically massive phase of Observation \claimref{dark-tower-matter.three-dimensional-phases}, with its scaling of contact processes taken as the source's estimate takes it, $P = (m/e^{2})^{2}$ for $e^{2} \gg m$, the depletion term is
\[
\frac{2\,\Sigma\,\ln(a_{f}/a_{i})}{e^{4}\,a^{2}H},
\]
in which $m$ does not appear. Survival is the condition $e^{2} \ge c\,m_{N}\sqrt{d/d_{b}}$ with $c$ between $6.7 \times 10^{7}$ and $9.2 \times 10^{7}$: a coupling above $6.3$ to $8.7 \times 10^{7}$ GeV at $d = d_{b}$, for every cell mass. Read at $m = m_{N}$, $d = d_{b}$ it is $m/e^{2}$ below about $1.1$ to $1.5 \times 10^{-8}$, the requirement stated in Computation \claimref{dark-tower-matter.survival-sheets} and Observation \claimref{dark-tower-matter.r1-has-no-mechanism-odd-towers}. So on E and R3 alone that requirement is a floor on the coupling in units fixed by this world's baryon density and the common length, and not a small ratio of the cell's mass to the coupling.
\item[(iv)] \emph{(Clusters.)} With in-sheet cross-section $\lambda = (4/k)\sin^{2}\delta_{0}$, $k = mv/2$ (Fact \claimref{simulations.imported-low-energy-scattering-two-dimensions}), and sheets $s$ apart, $s$ proportional to $d$, the collision rate $n_{2}\lambda v$ is that of a gas with
\[
\frac{\sigma_{\mathrm{eff}}}{m} \;=\; \frac{\lambda s}{m} \;=\; \frac{8\sin^{2}\delta_{0}\,s}{m^{2}v},
\]
which at equal $\delta_{0}$, speed and compression is $X$ times its value at the particle model. At the bound $1\ \mathrm{cm^{2}\,g^{-1}}$ (Fact \claimref{simulations.imported-bullet-cluster}) in a core of overdensity $10^{4}$ at redshift $0.3$ and $3000$ km/s, $\sin^{2}\delta_{0}\,X \le S_{*}$ with $\sqrt{S_{*}}$ between $1.6$ and $1.8 \times 10^{-7}$ (at $X = 1$ the phase-shift bound of Computation \claimref{simulations.cluster-bound-two-dimensions}). With $\sin\delta_{0} = m/e^{2}$ the mass cancels again: $e^{2}$ above $5.2$ to $5.9 \times 10^{6}$ GeV $\times \sqrt{d/d_{b}}$, weaker than (iii).
\item[(v)] \emph{(Full strength.)} At $P = 1$ the bound of (ii) is on the mass: $m \ge c\,m_{N}\sqrt{d/d_{b}}$ with the same $c$, a lower bound for s-wave annihilation ($8.7 \times 10^{7}$ GeV passes and $6.3 \times 10^{7}$ GeV fails at $d = d_{b}$ for every $g$). At $m = m_{N}$, $d = d_{b}$ the depletion exceeds $4 \times 10^{13}$, the surviving fraction of order $10^{-14}$ that T14 and T14c state. For clusters the scaling at composite strength depends on what the size $a$ of a composite does: if $a$ goes as $1/m$, so that $ka$ is fixed, $\sigma_{\mathrm{eff}}/m$ goes as $X$; at fixed $a$ it goes as $d/m$ once $ka \gg 1$. In neither case is it independent of $m$ and $d$, so ``composite strength makes the matter a fluid in clusters, whatever the size of a composite'' (Corollary \claimref{simulations.confinement-scale-does-not-matter}) and ``the density the rule assigns excludes composite strength'' are statements at the particle model.
\item[(vi)] \emph{(One length.)} E's length is one length for every tower, so the $d$ of (i) to (v) is the depth of the five-dimensional towers' extra direction. Take the model of the source's estimate that nothing confines there (Computation \claimref{dark-tower-matter.five-dimensional-towers}(ii)) as a hypothesis, with the quark mass $m_{5}$ free: pure-glue coefficient $11$, the strong-coupling value $g_{5}^{2} = 8\pi^{3}/m_{5}$, and the depth $L = d$ comoving, evaluated at $T = m_{5}/20$. Its exponent is $m_{5}L/(11\pi) = \kappa\,d/d_{b}$ with $\kappa$ between $220$ and $228$ at $g_{s} = 106.75$ and between $475$ and $490$ at $g_{s} = 10.75$; $m_{5}$ enters only through $g_{s}$. The confinement length $(d/\pi)\,e^{\kappa d/d_{b}}$ of that model exceeds the Hubble radius for $d \ge 0.3$ m and is inside it for $d \le 0.1$ m at $g_{s} = 10.75$, $61.75$ and $106.75$. So lowering $d$ to ease the floor of (iii) is not free: below a few tenths of a metre the source's five-dimensional conclusions are no longer established, and with $d \ge 0.3$ m the floor of (iii) is above $3.4 \times 10^{7}$ GeV.
\end{enumerate}
\emph{Limits.} The cancellation of (iii) and (iv) is exact in the stated formulas and not beyond them. The logarithm depends on $m$ if the non-relativistic onset tracks it ($25.8 = \ln(m_{N}/25T_{0})$; the floor rises by about $1.3$ at $m = 7 \times 10^{7}$ GeV). The scaling $P = (m/e^{2})^{2}$ needs $e^{2}$ well above $m$, so $m/e^{2}$ is still at most of order a tenth: what goes is the requirement of a ratio near $10^{-8}$, not every condition on the ratio; a coefficient in $P$ moves the floor by its square root. And the result supplies nothing: E fixes neither $\Sigma$'s origin, nor $d$, nor $e^{2}$, and the series has no mechanism for any of them in the odd towers (Observation \claimref{dark-tower-matter.r1-has-no-mechanism-odd-towers}). The mirror's entries in Observation \claimref{dark-tower-matter.towers-built} do not involve the odd towers' quanta and are untouched, so that observation's conclusion, that no configuration of the towers as built passes every test at face value, stands; what changes is the third of its four choices, which on E and R3 alone is a three-dimensional coupling above about $10^{8}$ GeV at metre spacing and not an unprotected light mass.

## technical
Assume E and R3 only, with a sheet tower's cell mass $m$ and the common length $d$ free. E fixes the sheet's mass per unit area, $\Sigma = \tfrac43\rho_{b}d$, independently of the cells. In the source's own formulas the depletion of a symmetric sheet relic, $2P\Sigma\ln(a_{f}/a_{i})/(m^{2}a^{2}H)$, and the effective cross-section per mass in clusters, $8\sin^{2}\delta_{0}\,s/(m^{2}v)$, are both $X = (d/d_{b})(m_{N}/m)^{2}$ times their values at the particle model. In phase (T), where $P = (m/e^{2})^{2}$ and $\sin\delta_{0} = m/e^{2}$, the mass cancels exactly: survival needs $e^{2}$ above $6.3$ to $8.7 \times 10^{7}$ GeV $\times\sqrt{d/d_{b}}$ and the cluster bound $5.2$ to $5.9 \times 10^{6}$ GeV $\times\sqrt{d/d_{b}}$, for every cell mass well below $e^{2}$. T14c's requirement of $m/e^{2}$ below $1.1$ to $1.5 \times 10^{-8}$ is the first bound read at the nucleon mass and metre spacing. At full strength the bound falls on the mass instead, and the composite-strength statements of T14 and T14b hold at the particle model, not on E alone.

E's length is one length for all towers, so $d$ is also the five-dimensional towers' depth: in the model of the source's no-confinement estimate the exponent is proportional to $d$ ($220$ to $490$ times $d/d_{b}$ over the range of $g_{s}$) and the confinement length drops inside the Hubble radius between $0.1$ and $0.3$ m. With $d$ at least $0.3$ m the coupling's floor is above $3.4 \times 10^{7}$ GeV.

Limits: the logarithm depends weakly on $m$; the scaling needs $e^{2} \gg m$, so the result removes the $10^{-8}$ requirement and not every condition on $m/e^{2}$; nothing fixes $\Sigma$, $d$ or $e^{2}$; and the verdict that no configuration of the towers as built passes every test stands on the mirror's entries, which do not involve the quanta.

## lay
The rule for the amount of dark matter now says only how much mass each hidden sector holds, not what its particles weigh. A companion note tested the flat, sheet-like sectors assuming their particles weigh what a proton does, and concluded that they would need a particle mass a hundred million times smaller than their force scale, with nothing to keep it that small. This result redoes the same sums without that assumption. The particle's mass then drops out exactly. What is left is a lower limit on the strength scale of the sector's force, about a hundred million proton masses if the sheets are a metre apart, and the particles may weigh anything comfortably below that. So the note's objection changes character: the sector needs a large force scale that nothing in the series supplies, but not a finely tuned small mass. The spacing of the sheets cannot be shrunk freely to help, because the same length is the depth of the five-dimensional sectors. Nothing here rescues the overall picture: the series still has no reason for the sectors to hold the amounts the rule needs, and the mirror sector's problems are untouched.

## one-liner
On E and R3 alone, with the cell mass $m$ and the common length $d$ free, the source's survival and cluster conditions for the sheet towers in phase (T) do not contain $m$: they are floors on the coupling, $e^{2}$ above $6.3$ to $8.7 \times 10^{7}$ GeV $\times\sqrt{d/d_{b}}$, of which T14c's ``$m/e^{2}$ below $10^{-8}$'' is the reading at the nucleon mass and metre spacing.
