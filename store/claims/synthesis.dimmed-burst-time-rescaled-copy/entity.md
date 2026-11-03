---
id: synthesis.dimmed-burst-time-rescaled-copy
kind: claim
version: 2
title: The dimmed final burst is the standard burst rescaled in time; its primary high-energy tail is dimmed by the full ratio, its energy in a fixed final window only by the two-thirds power
status: proved
region: synthesis
subject: dark-matter
tags: [radiation-spectrum, boundary-modes]
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
review: draft
derivations:
- name: main
  uses:
  - dark-matter.parallel-boundary-mode-spaces-one-wall@5
  - hawking.greybody-inheritance-under-interface-premise@6
  - dark-matter.mirror-tower-copy-one@8
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_mass_loss_law
- kind: check
  ref: check.py::check_time_rescaling
- kind: check
  ref: check.py::check_mirror_floor
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - pred.dimmed-evaporation-bursts
extraction:
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Scope note added to the formal and technical levels: with a populated five-dimensional tower the time-rescaled copy holds only for masses well above the crossover M_x of synthesis.five-dimensional-tower-kaluza-klein-channels-steepen-burst (under the interface premise); the statement for constant coefficients is unchanged. Version 1 -> 2.'
  open_problem: op.odd-towers
  note: >-
    Promotes the late-evaporation counting of the infall result to a statement about the burst
    spectrum, as op.odd-towers asks, without needing the odd towers' emission weights: they enter
    only through one number, the ratio D of the total emission coefficient to that of this tower plus gravitons. The content is standard evaporation kinematics applied to the
    store's democratic-return clause (transport-absent). It sharpens pred.dimmed-evaporation-bursts:
    the dimming by the full ratio holds at fixed hole mass and for the high-energy tail, while a
    search keyed to the time before the end sees the final-window energy dimmed by D^(2/3).
---

## formal
Let a black hole of the one metric evaporate in the regime where every populated tower's light species are lighter than its temperature, so that the emission coefficients are constant. Write $\Psi_{\mathrm{vis}}$ for this tower's coefficient in the mass-loss law, $\Psi_{\mathrm{grav}}$ for the gravitational sector's, $\Psi_{\mathrm{odd}}$ for the odd towers', $\Psi_{\mathrm{tot}}$ for the total, $g = \Psi_{\mathrm{grav}}/\Psi_{\mathrm{vis}}$, $o = \Psi_{\mathrm{odd}}/\Psi_{\mathrm{vis}}$, and let the standard expectation be the hole with this tower and gravitons only, total coefficient $\Psi_{0} = \Psi_{\mathrm{vis}} + \Psi_{\mathrm{grav}}$. Put $D = \Psi_{\mathrm{tot}}/\Psi_{0}$. Let $\tau$ be the hole's remaining lifetime and $N(E;\tau)$ the number of visible quanta per unit energy emitted in its last $\tau$, $N_{0}$ its standard value.
\begin{enumerate}
\item[(i)] Every channel's flux per unit energy depends on $M$ and $E$ only through $ME$ (Theorem \claimref{hawking.greybody-inheritance-under-interface-premise}), so $dM/dt = -\Psi_{\mathrm{tot}}/M^{2}$ and $M(\tau)^{3} = 3\Psi_{\mathrm{tot}}\tau$; at fixed $M$ the visible power is the same as in the standard case (Proposition \claimref{dark-matter.parallel-boundary-mode-spaces-one-wall}(i)).
\item[(ii)] \emph{(Time rescaling.)} For any visible emission $h(E, M)$ per unit time, secondaries included, the same function in every tower configuration because the exterior metric does not record which tower the mass came from,
\[
N(E;\tau) \;=\; \frac{1}{D}\, N_{0}(E;D\tau):
\]
the visible burst of the last $\tau$ is the standard burst of the last $D\tau$, divided by $D$.
\item[(iii)] \emph{(Three dimming laws.)} Consequently, at fixed remaining lifetime: the visible energy emitted in the last $\tau$ is $D^{-2/3}$ times its standard value; the hole's temperature is $D^{-1/3}$ times its standard value; and for primary emission, whose flux depends on $E$ and $M$ only through $ME$, the high-energy tail $N(E;\tau) \to C\,E^{-3}/(\Psi_{0}D)$ for $E\,M(\tau)$ large, which does not depend on $\tau$, is $1/D$ times its standard value. Only this primary tail, and the visible fraction of the power at fixed mass, are dimmed by the full ratio.
\item[(iv)] \emph{(Floor.)} The mirror's light content copies ours (Theorem \claimref{dark-matter.mirror-tower-copy-one}), so $D = (2 + g + o)/(1 + g) = 2 + (o - g)/(1 + g)$: $D \ge 2$ if and only if $o \ge g$, and with $o = 0$, $D = 2 - g/(1 + g)$. The factors of (iii) are $D$, $D^{2/3}$ and $D^{1/3}$.
\end{enumerate}
The odd towers enter only through $o$; the burst prediction needs their emission coefficients and no other property of them.

\emph{Scope note.} A populated five-dimensional tower never meets the hypothesis of constant coefficients at every mass: under the interface premise its Kaluza-Klein levels are emission channels of the shared exterior, the mass-loss law gains a term $B/M^{3}$ with $B$ proportional to the fifth direction's extent, and the time-rescaled copy (ii), with the laws (iii) drawn from it, holds for such a tower only for masses well above the crossover mass $M_{\times} = B/A$ of \claimref{synthesis.five-dimensional-tower-kaluza-klein-channels-steepen-burst}(ii); below it $M^{4} = 4B\tau$ and the primary high-energy tail steepens from $E^{-3}$ to $E^{-4}$ above a break.

## technical
In the regime where every tower's light species are lighter than the hole's temperature, the greybody-inherited flux makes the mass-loss law $dM/dt = -\Psi_{\mathrm{tot}}/M^{2}$. Against the standard expectation, this tower plus gravitons, the total is larger by $D = (2 + g + o)/(1 + g)$, with $g$ and $o$ the gravitational and odd-tower coefficients relative to this tower's and the mirror counted as a copy. The visible emission at a given mass is the same function as in the standard case, so a hole with dark towers passes through the same masses, and emits the same visible spectrum at each, but $D$ times faster: the visible burst of its last $\tau$ is the standard burst of the last $D\tau$, divided by $D$.

Three laws follow at fixed time before the end: the visible energy is dimmed by $D^{2/3}$, the temperature lowered by $D^{1/3}$, and the high-energy tail of the primary spectrum, independent of $\tau$ and falling as $E^{-3}$, dimmed by the full $D$. $D$ is at least $2$ exactly when the odd towers emit at least as much as the gravitational sector, and is $2 - g/(1 + g)$ if they emit nothing.

Scope: if a five-dimensional tower is populated, its Kaluza-Klein levels (under the interface premise) add a term $B/M^{3}$ to the mass-loss law, so these laws hold only for masses well above the crossover mass $M_{\times}$ of \claimref{synthesis.five-dimensional-tower-kaluza-klein-channels-steepen-burst}; below it the remaining lifetime is $M^{4}/(4B)$ and the primary tail steepens to $E^{-4}$.

## lay
The series predicts that the last explosive moments of a small evaporating black hole should be fainter than usual, because the hole also radiates into hidden worlds. This result says exactly how. The hidden worlds make the hole lose mass faster, so it runs through the same sequence of temperatures in less time. As a result, a telescope watching the final seconds sees the light of a longer stretch of the ordinary burst, squeezed and divided. The very high energy light emitted directly by the hole is dimmed by the full factor (about two from the mirror world alone), but the total light in the final seconds is dimmed less, by that factor to the power two thirds, and the burst looks cooler at a given time before its end.

## one-liner
With $D = (2 + g + o)/(1 + g)$ the ratio of total emission to that of this tower plus gravitons, the visible burst of a hole's last $\tau$ is the standard burst of its last $D\tau$ divided by $D$: the primary high-energy tail dims by $D$, the final-window energy by $D^{2/3}$, and the temperature at fixed time to the end by $D^{1/3}$; $D \ge 2$ if and only if the odd towers emit at least as much as gravity.
