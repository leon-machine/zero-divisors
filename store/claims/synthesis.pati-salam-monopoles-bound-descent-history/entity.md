---
id: synthesis.pati-salam-monopoles-bound-descent-history
kind: claim
version: 1
title: Given the monopole literature inputs, on the stored Pati-Salam chain with no inflation after the descent the Pati-Salam monopoles exceed the flux limit unless they form below 0.48 v_R = 2.0 x 10^10 GeV, so the seeding origin of the odd-tower remainder fails independently of Premise (R) and of perturbative couplings, unless the transition is cold, the symmetry is not restored at high temperature, or the monopoles are removed by a temporary breaking of electromagnetism
status: proved
region: synthesis
subject: dark-matter
tags: [no-go, confronted-with-data, symmetry-breaking, dark-matter-ratio, needs-continuum]
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
  - standard-model.what-angle-asks-neutrino-sector@4
  - standard-model.majorana-element@7
  - standard-model.imported-pati-salam-representation-theory-survival@1
  - synthesis.seeding-remainder-excludes-perturbative-pati-salam@2
  - synthesis.imported-planck-2018-lcdm-parameters@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_kibble_constant
- kind: check
  ref: check.py::check_hypercharge_is_a_circle_in_pati_salam
- kind: check
  ref: check.py::check_causal_minimum_exceeds_flux_limit
- kind: check
  ref: check.py::check_annihilation_cannot_lower_it
- kind: check
  ref: check.py::check_seeding_needs_cold_transition
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.seeding-remainder-excludes-perturbative-pati-salam
  - synthesis.untuned-fit-caps-lightest-heavy-neutrino
  - synthesis.finite-range-descent-deposit-cannot-seed-cmb
  - standard-model.dating-descent
extraction:
  open_problem: op.pre-descent-theory
  note: 'Cross-subject obstruction for the problem''s first attack (which of perturbative Pati-Salam couplings, Premise (R) and the seeding origin to give up). On the stored chain the (10,1,3) breaks Pati-Salam directly to the Standard Model at M_I, so the breaking leaves stable magnetic monopoles, and the series'' history has no inflation after the descent to dilute them. The causal (Kibble) minimum then exceeds the MACRO flux limit unless the transition is cold. The seeding origin needs a reheating temperature 32 times v_R, so the bath restores the symmetry and the transition happens afterwards: the seeding origin is excluded on the chain whether or not (R) and perturbativity hold, unless the transition temperature is below 0.48 v_R or the symmetry is not restored at high temperature (Weinberg 1974; Dvali, Melfo and Senjanovic 1995, from memory), or a temporary breaking of electromagnetism removes the monopoles (Langacker and Pi 1980, from memory). The literature inputs (the MACRO limit, the Kibble probability, Preskill''s annihilation floor, the Lazarides-Magg-Shafi monopole charge, the topology pi_2(G/H) = pi_1(H)) are cited from memory and should be imported as Facts. The deposit clause links the problem to op.descent-state-and-spectrum: both ask whether the pre-metric deposit is correlated beyond the descent''s Hubble length. Transport-absent.'
---

## formal
Work on the chain of Proposition \claimref{standard-model.what-angle-asks-neutrino-sector}: the $(10,1,3)$ vev breaks $G = SU(4) \times SU(2)_{L} \times SU(2)_{R}$ directly to the Standard Model group $H$ at $M_{I} = 1.95 \times 10^{10}$ GeV (Proposition \claimref{standard-model.majorana-element}), with $v_{R} = M_{I}/g_{R} = 4.15 \times 10^{10}$ GeV, and assume (D): no inflationary stage follows the descent and entropy is conserved after it (the history of Conjecture \claimref{standard-model.dating-descent}, taken here as a hypothesis). Assume (K): wherever the broken phase forms by a causal process (a thermal transition at $T_{c}$, or a deposit at $T_{d}$ whose vacuum orientation is uncorrelated beyond the Hubble length), at least one monopole forms per Hubble volume $H^{-3}$ with probability $p \ge \tfrac{1}{10}$, with $g_{*} \ge 106.75$ there; and take as premises the literature inputs (a) to (e) of the proof, which are not imported in the store and are cited from memory: (a) $\pi_{2}(G/H) \cong \pi_{1}(H)$ for simply connected $G$, with stable monopoles for each class; (b) the Kibble-Preskill causal estimate underlying (K); (c) Preskill's annihilation floor; (d) the MACRO flux limit $\mathcal{F} < 1.4 \times 10^{-16}$ cm$^{-2}$ s$^{-1}$ sr$^{-1}$, applied to galactic monopoles with speed $\beta \ge 7 \times 10^{-4}$; (e) high-temperature symmetry restoration, with its known exceptions. The statements below are proved given (a) to (e).
\begin{enumerate}
\item[(i)] \emph{(Monopoles exist.)} The hypercharge $Y = T_{3R} + \tfrac12(B - L)$ is traceless on the $4$ and on the $SU(2)_{R}$ doublet, so it generates a circle in the simply connected $G$ commuting with $SU(3) \times SU(2)_{L}$; it gives the Standard Model hypercharges on the $(4,2,1) \oplus (\bar 4,1,2)$ and closes first at period $6$. Hence $\pi_{2}(G/H) = \pi_{1}(H) \supseteq \mathbb{Z}$: the breaking leaves stable monopoles, of mass $M_{M} \approx 4\pi v_{R}/g_{R} > 10^{12}$ GeV.
\item[(ii)] \emph{(The causal minimum against the flux limit.)} The minimum of (K) at temperature $T$ is $n_{M}/s \ge p\,(\pi^{2}g_{*}/1440)^{1/2}(T/M_{P})^{3}$ ($M_{P}$ the reduced Planck mass), not diluted afterwards under (D); at $T = v_{R}$ it exceeds $3.6 \times 10^{-25}$, while the flux limit allows at most $3.7 \times 10^{-26}$ today, a factor above $12$. The minimum exceeds the limit for every $T \ge 0.48\,v_{R} = 2.0 \times 10^{10}$ GeV and every $\beta \ge 10^{-4}$, and not at $T = 0.3\,v_{R}$.
\item[(iii)] \emph{(Neither annihilation nor closure decides it.)} Preskill's annihilation floor, $n_{M}/s \sim 10^{-10}(M_{M}/10^{14}\,\mathrm{GeV}) > 10^{-12}$, lies far above the causal minimum, so annihilation cannot bring $n_{M}/s$ below it; closure ($\Omega h^{2} < 0.12$) allows up to $3.9 \times 10^{-22}$ and is not the binding constraint.
\item[(iv)] \emph{(The seeding origin.)} The seeding condition of Theorem \claimref{synthesis.seeding-remainder-excludes-perturbative-pati-salam}, $c\,T_{d}^{4} \ge A/2$ with $A^{1/4} = 1.217 \times 10^{12}$ GeV and $c = 0.312$, needs $T_{d} > 1.36 \times 10^{12}$ GeV $> 32\,v_{R}$, so unless the symmetry is not restored at high temperature the transition happens in the descended phase, and by (ii) the seeding origin is excluded on the chain unless $T_{c} < 0.48\,v_{R}$ or the monopoles are removed after they form by a temporary breaking of electromagnetism that confines them in flux tubes (the Langacker-Pi mechanism, from memory), which needs a stage of the descended phase the chain does not contain. This holds whether or not Premise (R) (\claimref{neutrino.r-descent-reheats-below-lower-heavy}) and perturbative couplings hold. Seeding with $T_{d}$ below $2.0 \times 10^{10}$ GeV needs $c > 6.8 \times 10^{6}$, about $3 \times 10^{9}$ vector species.
\item[(v)] \emph{(The deposit clause.)} A descent below $T_{c}$ that deposits the broken phase with an orientation uncorrelated beyond its Hubble length gives the same minimum at $T_{d}$, so it is excluded for $T_{d} \ge 2.0 \times 10^{10}$ GeV. A deposit aligned beyond its Hubble length escapes, and such correlations are available in principle: a deposit correlated by the frozen point's stabiliser reaches the length $|x_{d}|$ of the descent slice in the frozen point's chart, about four present Hubble radii (filed alongside, synthesis.frozen-point-geometry-reads-descent-as-vacuum, whose obstruction concerns the spectrum of $\zeta$, not the vacuum orientation).
\end{enumerate}
Consequently, on the chain the reheating temperature of the descent is below $2.0 \times 10^{10}$ GeV, or the transition is cold ($T_{c} < 0.48\,v_{R}$), or the symmetry is not restored at high temperature with a deposit aligned beyond the descent's Hubble length, or the monopoles are removed by a Langacker-Pi stage; of the three premises that the stored seeding result finds incompatible, the seeding origin is the one that also fails on its own.

## technical
On the stored chain, the Majorana element's vev breaks Pati-Salam straight to the Standard Model at about $2 \times 10^{10}$ GeV. Because the hypercharge is a circle inside the simply connected Pati-Salam group, the breaking leaves stable magnetic monopoles, of mass above $10^{12}$ GeV. In the series' history the descent is at the origin and nothing inflates afterwards, so monopoles formed after the descent are never diluted.

The literature inputs used here (the topology of the breaking, the causal estimate, the annihilation floor, the MACRO limit and high-temperature restoration) are premises cited from memory, not yet imported. Causality fixes a minimum: where the broken phase forms with an orientation that is uncorrelated beyond the Hubble length, at least about one monopole in ten Hubble volumes survives, which gives $n_{M}/s \ge p\sqrt{\pi^{2}g_{*}/1440}\,(T/M_{P})^{3}$. At $T = v_{R}$ this is above $3.6 \times 10^{-25}$; the MACRO flux limit allows at most $3.7 \times 10^{-26}$ for galactic monopoles. Annihilation cannot help, because it acts only above a floor near $10^{-12}$, and closure is not the binding constraint. The minimum stays above the limit for every formation temperature above $0.48\,v_{R}$, about $2 \times 10^{10}$ GeV.

The seeding origin of the odd-tower remainder needs a descent hotter than $1.36 \times 10^{12}$ GeV, thirty-two times $v_{R}$. The bath then restores Pati-Salam, and the breaking happens afterwards in the descended phase; its monopoles exceed the flux limit unless the transition is cold, below $0.48\,v_{R}$. That holds whatever one decides about Premise (R) and perturbative couplings, so among the three premises the stored seeding result cannot reconcile, the seeding origin is the one with an independent obstruction. The escapes are a cold transition, high-temperature non-restoration with a deposit aligned beyond the descent's Hubble length, a temporary breaking of electromagnetism that confines and annihilates the monopoles (the Langacker-Pi mechanism), or a chain other than the stored one. An aligned deposit is available in principle: a deposit correlated by the frozen point's stabiliser reaches about four present Hubble radii on the descent slice (filed alongside, synthesis.frozen-point-geometry-reads-descent-as-vacuum). A cooler descent that deposits the broken phase with an uncorrelated orientation meets the same bound at its own temperature.

## lay
The theory's particle physics breaks a larger symmetry down to the familiar one at about twenty billion times the proton mass in energy units. Symmetry breaking of this kind leaves behind magnetic monopoles, isolated magnetic charges, wherever separate regions of the early universe chose their broken state independently. Without a later period of rapid expansion to thin them out, causality guarantees a minimum number of them. Underground detectors have looked for passing monopoles and found none, which caps their number below that minimum unless the breaking happened in a cool universe. One proposed origin for part of the dark matter needs the universe to start far hotter than that, so it would produce too many monopoles, whatever else is assumed, unless the breaking happens in an unusual way or the monopoles are removed later.

## one-liner
Given the monopole literature inputs (cited from memory), on the stored Pati-Salam chain with no inflation after the descent (Hypothesis (D)) causally formed Pati-Salam monopoles exceed the MACRO flux limit (by a factor above $12$ at $T = v_{R}$) unless they form below $0.48\,v_{R} = 2.0 \times 10^{10}$ GeV, so the seeding origin of the odd-tower remainder, which needs $T_{d} > 1.36 \times 10^{12}$ GeV, fails independently of (R) and of perturbative couplings, unless the transition is cold, the symmetry is not restored at high temperature, or a temporary breaking of electromagnetism removes the monopoles.
