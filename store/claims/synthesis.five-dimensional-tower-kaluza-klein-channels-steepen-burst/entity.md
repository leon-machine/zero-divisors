---
id: synthesis.five-dimensional-tower-kaluza-klein-channels-steepen-burst
kind: claim
version: 2
title: 'Kaluza-Klein channels of a five-dimensional tower steepen the burst'
status: proved
region: synthesis
subject: dark-matter
tags: [radiation-spectrum, boundary-modes]
proposed_by:
  kind: ai
  session: 2026-10-31-all-open
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
  - hawking.greybody-inheritance-under-interface-premise@6
  - dark-matter.parallel-boundary-mode-spaces-one-wall@5
  - dark-tower-matter.five-dimensional-towers@6
  - dark-matter.sourcing-rule-forced-not-chosen@4
  - synthesis.dimmed-burst-time-rescaled-copy@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_level_sum
- kind: check
  ref: check.py::check_mass_time_law
- kind: check
  ref: check.py::check_tail_steepening
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - pred.dimmed-evaporation-bursts
  - dark-matter.thickness-not-gravitational-quantity
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The two Kaluza-Klein phases along e_5 in the proof, e^{i mu y} and e^{2 pi i k y/L_f}, are written with the field theory''s unit I_4 acting on the right (exact for fields of any grade); no bare i remains.'
  open_problem: op.odd-towers
  note: >-
    Supplies the five-dimensional towers' part of the emission coefficient o that op.odd-towers asks
    for, and finds that it is not a constant: the store counts a five-dimensional tower's
    Kaluza-Klein levels as light degrees of freedom in the bath (five-dimensional-towers (i), (iii)),
    and the infall result returns a hole's energy to every tower in proportion to its light degrees
    of freedom once the temperature exceeds their gaps, so the number of radiating levels grows as
    L_f T_H. An earlier estimate that set this aside imported a hole localised in the fifth
    direction, which needs a metric fifth direction, excluded by
    dark-matter.thickness-not-gravitational-quantity. Standard Kaluza-Klein and evaporation
    kinematics on the store's clauses (transport-absent). It restricts
    synthesis.dimmed-burst-time-rescaled-copy, for a populated five-dimensional tower, to holes
    above the crossover mass, and makes the extent of the fifth direction an evaporation observable
    although it is not a gravitational one.
---

## formal
Let the two five-dimensional towers be populated, with their fields on the one metric's exterior times a fifth direction of extent $L_{f}$ that the metric does not see (Proposition \claimref{dark-matter.sourcing-rule-forced-not-chosen}: a quantum with momentum $p_{5}$ along it appears as a four-dimensional quantum of mass $|p_{5}|$), and with the natural condition at the ends that keeps a zero mode (Proposition \claimref{dark-tower-matter.five-dimensional-towers}(v)), or with the fifth direction closed; $L_{f}$ is at least the counted thickness of R3, and equal to it when the matter fills the fifth direction. Let a black hole of the one metric, of mass $M$ and temperature $\TH = 1/(8\pi M)$, evaporate under the interface premise of Theorem \claimref{hawking.greybody-inheritance-under-interface-premise}.
\begin{enumerate}
\item[(i)] \emph{(Level sum.)} The Kaluza-Klein levels have masses $\mu_{k} = k\pi/L_{f}$, $k \ge 0$ (or $2\pi|k|/L_{f}$, $k \in \mathbb{Z}$, closed), and the number of levels of mass at most $\mu$ differs from $L_{f}\mu/\pi$ by at most one. Each level of each species $s$ is a channel of the exterior whose power is $M^{-2}\psi_{s}(M\mu)$, with $\psi_{s}$ of bounded variation. The tower's coefficient in the mass-loss law is therefore
\[
\Psi_{5}(M) \;=\; \frac{L_{f}}{\pi M}\sum_{s} I_{s} + R(M), \qquad I_{s} = \int_{0}^{\infty}\psi_{s}(y)\,dy > 0, \qquad |R(M)| \le \sum_{s}\mathrm{TV}(\psi_{s}),
\]
so that $-M^{2}\,dM/dt = A(M) + B/M$ with $B = \sum_{\text{5D towers}}(L_{f}/\pi)\sum_{s}I_{s} > 0$ and $A(M)$ bounded: this tower, the mirror, the gravitational sector, the three-dimensional towers (taken bounded) and the remainders $R$.
\item[(ii)] \emph{(Mass-time law.)} With $A_{+}$ an upper bound of $A$ and $V = \sum\mathrm{TV}(\psi_{s})$ over both towers, the remaining lifetime obeys $M^{4}/(4(B + A_{+}M)) \le \tau \le M^{4}/(4(B - VM))$ for $M < B/V$, so $M(\tau)^{4} = 4B\tau\,(1 + O(M/M_{\times}))$ below the crossover mass $M_{\times} = B/A$, against $M(\tau)^{3} = 3\Psi\tau$ for constant coefficients. The constant-coefficient regime of Proposition \claimref{synthesis.dimmed-burst-time-rescaled-copy} holds for a populated five-dimensional tower only for $M \gg M_{\times}$; below it no constant $D$ makes the burst a time-rescaled copy of the standard one.
\item[(iii)] \emph{(Tail.)} For primary visible emission $\phi_{\mathrm{vis}}(ME)$ with $x^{3}\phi_{\mathrm{vis}}(x)$ integrable, the visible quanta per unit energy emitted in the last $\tau$ obey $E^{4}N(E;\tau) \to C_{3}/B$ as $E \to \infty$, for every $\tau > 0$, with $C_{k} = \int_{0}^{\infty}\phi_{\mathrm{vis}}(x)x^{k}\,dx$, against $E^{3}N(E;\tau) \to C_{2}/\Psi$ for constant coefficients. For constant $A$ and a hole far above $M_{\times}$ at the start, $N(E) = E^{-3}\int_{0}^{\infty}\phi_{\mathrm{vis}}(x)\,x^{3}\,dx/(Ax + BE)$: the time-integrated tail falls as $E^{-3}$ below and as $E^{-4}$ above a break at $E_{b} = (A/B)(C_{3}/C_{2})$.
\item[(iv)] \emph{(What the break measures.)} $E_{b}$ and the crossover temperature $T_{\times} = 1/(8\pi M_{\times}) = A/(8\pi B)$ are inversely proportional to $L_{f}$, with a coefficient fixed by the towers' contents and the exterior's transmission coefficients. The extent of the fifth direction, which gravity cannot measure (Corollary \claimref{dark-matter.thickness-not-gravitational-quantity}), sets the evaporation spectrum.
\end{enumerate}

## technical
A five-dimensional tower's fields live on the shared exterior times a fifth direction the metric does not see, so each field is a ladder of four-dimensional fields of masses spaced by $\pi/L_{f}$, the Kaluza-Klein levels the store already counts in the cosmological bath. Under the interface premise each level is an emission channel of the shared exterior, and its power depends on the hole's mass only through $M\mu$ and the scaling $M^{-2}$. Summing the levels, whose number below a given mass grows linearly with $L_{f}$, gives a coefficient $(L_{f}/\pi M)\sum I_{s}$ plus a bounded remainder: the mass-loss law gains a term $B/M^{3}$. Below the crossover mass $M_{\times} = B/A$ that term dominates, the remaining lifetime is $M^{4}/(4B)$ instead of $M^{3}/(3\Psi)$, and the time-rescaling law of the dimmed burst no longer applies. The primary high-energy tail integrated over the burst steepens from $E^{-3}$ to $E^{-4}$ above a break energy inversely proportional to $L_{f}$, so the burst spectrum measures the extent of the fifth direction, which gravity cannot.

## lay
On the standard assumption that a black hole's radiation is fed by its horizon in every channel, a hidden world with an extra space direction can absorb the radiation of a small black hole in many more ways than ours can, because each kind of particle in it comes in a whole ladder of versions, one for each way of vibrating across the extra direction. The hotter the hole, the more rungs of the ladder it can reach, so as the hole shrinks and heats up it pours more and more of its energy into that world. Its final stage then runs differently from the standard picture: it loses mass on a faster schedule, and the very energetic light it sends us falls off more steeply with energy above a certain break. Where the break sits depends on the size of the extra direction, which gravity alone could never reveal.

## one-liner
Under the interface premise, a populated five-dimensional tower's Kaluza-Klein levels are emission channels of the shared exterior, so a hole's mass-loss law gains a term $B/M^{3}$ with $B$ proportional to the fifth direction's extent: below the crossover mass $M^{4} = 4B\tau$, the dimmed burst is no longer a time-rescaled copy, and its primary high-energy tail steepens from $E^{-3}$ to $E^{-4}$ above a break that measures that extent.
