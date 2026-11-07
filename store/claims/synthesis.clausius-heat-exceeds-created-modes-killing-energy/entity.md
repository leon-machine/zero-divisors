---
id: synthesis.clausius-heat-exceeds-created-modes-killing-energy
kind: claim
version: 3
title: 'Clausius heat exceeds the created modes'' Killing energy'
status: proved
region: synthesis
subject: einstein
tags: [boundary-modes, thermal-premises, horizons, no-go, mode-counting]
proposed_by:
  kind: ai
  session: 2026-10-23-toe
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
review: draft
derivations:
- name: main
  uses:
  - singularity.kms-uniqueness-factor@4
  - synthesis.boundary-mode-thermal-entropy@2
  - synthesis.boundary-mode-first-law-of-entanglement@6
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_kms_unique_on_window
- kind: check
  ref: check.py::check_exchange_leaves_kms
- kind: check
  ref: check.py::check_created_mode_ledger
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.einstein-equations-from-c-loc-and-clausius
  - synthesis.central-label-carries-mass-at-zero-weight
  - synthesis.hole-mass-is-ground-energy-label
outside_ga:
  kind: complex-analysis
  why: 'the boost dynamics Ad(e^{itH_F}) acts on the window algebra End(Lambda C^F) of the boundary-mode algebra, whose modes descend from the atom of the spacetime radial plane and anticommute with I_4 (conventions, known limits 1 and 2), as its defining object declares'
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (complex-analysis): the boost dynamics Ad(e^{itH_F}) acts on the window algebra End(Lambda C^F) of the boundary-mode algebra, whose modes descend from the atom of the spacetime radial plane and anticommute with I_4 (conventions, known limits 1 and 2), as its defining object declares.'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Version 2, label only: the zero-weight limit is now described as where the registered residue sits when each counted unit is one mode, since under (Q) version 3 (weights kappa(k + 1/2)) the registered value is also realised by two arrays at nonzero weight; statement, proof and checks unchanged. Version 1 -> 2.'
  open_problem: ein.clausius-hypothesis
  note: >-
    An adversarial test of the route that would derive the Clausius hypothesis (H1) of the Einstein
    derivation from the boundary-mode first law: matter hands boost energy to the patch's boundary modes,
    energy is conserved, and the first law turns it into entropy. The result separates two readings of
    the temperature clause (R_loc). Read at every instant (the hypothesis (R_inst) of the statement), KMS
    uniqueness on a finite window makes a fixed window's state, entropy and Killing energy constant, so
    the entropy change of a local horizon can only come from a change of the mode set, and Clausius then
    demands T s(x) of heat per created mode while the mode carries only omega n(x) of Killing energy: the
    gap T ln(1 + e^{-x}) per mode is carried neither by matter nor by any mode's Killing energy, so (H1),
    (R_inst) with fixed weights, and conservation of boost energy between matter and the modes' Killing
    energy cannot all hold when heat crosses. At zero weight, where the registered residue sits, the gap
    is the whole heat: this is the local counterpart of the c-number mass label of the stored microcanonical
    model. Read only for the state before the crossing, the first-law route is available, but the window
    then leaves the unique KMS state at first order in the heat (an exact resonant-exchange model shows
    it). So the one extra structure (H1) needs, beyond (C_loc), is an energy carrier outside the modes (the
    label) with a rule creating modes from matter's boost energy, or a dynamics of the weights, which the
    boundary-mode Definition does not provide (with weights that move with the heat the ledger can
    balance, as the proof shows), or a weakening of (R_loc) to the state before the crossing. The last is
    the reading Jacobson-type arguments use, and on it the first-law route is treated in the result filed
    alongside, synthesis.clausius-is-window-first-law-plus-boost-charge-conservation; this result prices
    the every-instant reading. The per-mode gap T ln(1 + e^{-x}) is minus the free energy of a mode created
    in its Gibbs state, a chemical potential for mode creation in T dS = dE - mu dN: standard
    thermodynamics; the content is that the series' premises supply no carrier for it. Imported: none
    beyond the store. Transport-absent: finite-dimensional thermal bookkeeping on the series' windows.
---

## formal
Let the boundary modes of a local horizon patch be organised in windows $F$, finite sets of fermionic modes with Killing weights $\omega_j \ge 0$ and boost dynamics $H_F = \sum_{j \in F}\omega_j N_j$, as in Definition \claimref{obj.hawking.boundary-mode-algebra-windows-boost-dynamics} (whose weights are positive; the value $\omega = 0$ is admitted here as the limit at which the registered residue sits when each counted unit is one mode; under the weight clause of version 3 of Premise (Q) the registered value is also realised by two arrays per unit at nonzero weight), with inverse temperature $\beta = 1/T$ in Killing time and $x_j = \beta\omega_j$, and write $n(x) = 1/(e^{x} + 1)$ and $s(x) = \ln(1 + e^{-x}) + x\,n(x)$ (Theorem \claimref{synthesis.boundary-mode-thermal-entropy}). Consider the hypotheses:
\begin{enumerate}
\item[(R$_{\mathrm{inst}}$)] at each instant considered, the state of the patch's boundary modes restricts to each window as a KMS state of its boost dynamics at $\beta$, the weights being fixed (the temperature clause (R$_{\mathrm{loc}}$) of Premise \claimref{synthesis.c-loc-local-horizon-premise} read at every instant);
\item[(Cl)] between two instants, the boundary-mode entropy changes by $\delta S = \delta Q/T$, where $\delta Q$ is the boost energy matter delivers (the Clausius hypothesis (H1) of Theorem \claimref{synthesis.einstein-equations-from-c-loc-and-clausius}, with the entropy carried by the boundary modes as in clause (Loc));
\item[(E)] the boost energy matter delivers equals the change $\delta E$ of the boundary modes' Killing energy $\langle H\rangle$.
\end{enumerate}
Then:
\begin{enumerate}
\item \emph{(No heat into a fixed window.)} Under (R$_{\mathrm{inst}}$) a window's state is $\varrho_{I} = e^{-\beta H_F}/Z_F$ (Theorem \claimref{singularity.kms-uniqueness-factor}), so between two instants at which (R$_{\mathrm{inst}}$) holds with the same window, its entropy and Killing energy are unchanged.
\item \emph{(Created modes.)} If between two instants obeying (R$_{\mathrm{inst}}$) the mode set grows by a set $C$ and loses a set $D$ (other modes unchanged), then $\delta S = \sum_{C}s(x_j) - \sum_{D}s(x_j)$ and $\delta E = T\bigl(\sum_{C}x_j n(x_j) - \sum_{D}x_j n(x_j)\bigr)$.
\item \emph{(The deficit.)} Under (R$_{\mathrm{inst}}$) and (Cl),
\[
\delta Q - \delta E \;=\; T\Bigl(\sum_{C}\ln\bigl(1 + e^{-x_j}\bigr) - \sum_{D}\ln\bigl(1 + e^{-x_j}\bigr)\Bigr).
\]
If all created and lost modes share one weight $x \ge 0$ (the common-weight setting of the registered residue), with net number $\delta m$, then $\delta Q = T s(x)\,\delta m$, $\delta E = T x\,n(x)\,\delta m$ and $\delta Q - \delta E = T\ln(1 + e^{-x})\,\delta m$, which is nonzero whenever $\delta Q \neq 0$; the fraction of the heat that is Killing energy is $x\,n(x)/s(x) < 1$, and it is $0$ at $x = 0$, where $\delta Q = T\ln 2\,\delta m$. The same holds if modes are only created ($D = \emptyset$), for any weights. Hence (R$_{\mathrm{inst}}$), (Cl) and (E) are inconsistent whenever heat crosses in either of these settings.
\item \emph{(The other reading.)} If (R$_{\mathrm{inst}}$) is required only at the earlier instant, a fixed window can receive Killing energy $\delta E$ with (E), and its first law then gives Clausius at first order (the route of the result filed alongside, synthesis.clausius-is-window-first-law-plus-boost-charge-conservation); by (1) the new state is not KMS for the window's boost at $\beta$ unless $\delta E = 0$. An exact example: a resonant number-conserving exchange between a window mode at $e^{-x} = 1/3$ (occupation $1/4$) and an occupied matter mode, rotating the one-particle sector by $\cos\theta = 3/5$, conserves total occupation and leaves the window mode at occupation $73/100$, not the KMS value.
\end{enumerate}
So on the store's premises (H1) needs one further structure: an energy carrier that is neither matter nor the boundary modes' Killing energy, taking $T\ln(1 + e^{-x})$ per created mode (all of the heat at zero weight), with a rule by which matter's boost energy creates modes; or a dynamics of the weights, which the boundary-mode Definition does not provide; or a weakening of (R$_{\mathrm{loc}}$) to the state before the crossing.

## technical
One route to the Clausius hypothesis of the Einstein derivation is to let matter hand its boost energy to the horizon's boundary modes, conserve energy, and use the first law of entanglement to turn the energy into entropy. This result tests that route against the temperature clause of the local-horizon premise, which says the boundary modes are in a KMS state for the local boost. A finite window has exactly one KMS state at a given temperature, so if the clause holds at every instant and the window and its weights are fixed, the window's entropy and energy cannot change at all. The horizon entropy can then grow only by adding modes, which is the area-count picture. A mode added in its thermal state brings entropy $s(x)$ but Killing energy only $\omega n(x)$, and the Clausius relation asks for heat $T s(x)$; the difference, $T\ln(1 + e^{-x})$ per mode, is positive for every weight. So the three statements, Clausius, the temperature clause at every instant with fixed weights, and conservation of boost energy between matter and the modes' Killing energy, cannot all hold when heat crosses: some third carrier must take that energy. At zero weight, where the registered calibration residue sits in its one-mode-per-unit reading, the modes carry no Killing energy and the third carrier takes all the heat: this is, locally, the same tension as the hole's mass sitting on a c-number label rather than in the counted modes, and the label's energy is fed at $T\ln 2$ per created mode. The gap is the created mode's free energy with opposite sign, $-F = T\ln Z$ per mode, a chemical potential $\mu = -T\ln(1 + e^{-x})$ for mode creation in $T\,dS = dE - \mu\,dN$; that much is standard thermodynamics, and the content here is that the series' premises supply no carrier for it. Weights that moved with the heat could balance the ledger instead, but the boundary-mode Definition fixes them as labels and provides no such dynamics. If instead the temperature clause is only required before the crossing, the reading Jacobson-type arguments use, energy can flow into a fixed window and the first law gives the right entropy at first order (the route filed alongside, synthesis.clausius-is-window-first-law-plus-boost-charge-conservation), but the window then leaves its KMS state; an exact resonant exchange shows the occupation moving from $1/4$ to $73/100$. This result prices the every-instant reading. The checks verify KMS uniqueness on a two-mode window (a one-dimensional solution space of the KMS equations), the exchange model, the factorisation of the Gibbs state when a mode is added, and the per-mode ledger at $e^{x} = 3$ and at zero weight with exact logarithms of rationals. The result does not decide which reading of the premise is right; it says what each reading costs.

## lay
One hope for deriving Einstein's equations in the series is this: when matter falls across a horizon, it hands its energy to the horizon's quantum modes, and the standard thermodynamic law then turns that energy into the entropy that the horizon's area measures. This result checks the hope against the series' own assumption that those horizon modes are always at the horizon's temperature. A fixed set of modes at a fixed temperature has only one possible state, so it cannot soak up energy and stay at that temperature. The horizon can then gain entropy only by gaining modes. But a new mode at the horizon's temperature carries less energy than the heat the thermodynamic law requires for the entropy it brings, and at the special value the series' calibration uses it carries none at all. So the energy has to go somewhere other than the matter or the modes' own energy: something like the extra mass label the series already needed for black holes. The alternative is to let the modes leave their temperature while heat flows in, which gives up the assumption the hope started from.

## one-liner
If the temperature clause of (C$_{\mathrm{loc}}$) holds at every instant with fixed weights, KMS uniqueness makes a fixed window absorb no heat, so Clausius entropy enters as created modes, and the heat $T s(x)$ per mode exceeds the mode's Killing energy $\omega n(x)$ by $T\ln(1 + e^{-x}) > 0$ (all of it at zero weight): (H1) needs a carrier beyond matter and the modes' Killing energy (the gap is minus the created mode's free energy), or a dynamics of the weights, or the clause must be weakened to the state before the crossing, where a fixed window does take heat but leaves its KMS state.
