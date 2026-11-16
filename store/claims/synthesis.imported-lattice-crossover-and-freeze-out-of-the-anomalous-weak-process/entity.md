---
id: synthesis.imported-lattice-crossover-and-freeze-out-of-the-anomalous-weak-process
kind: claim
version: 1
title: 'Imported: lattice crossover and freeze-out temperatures of the anomalous weak process'
status: imported
region: synthesis
subject: dark-matter
tags: [matter-asymmetry, symmetry-breaking]
proposed_by:
  kind: ai
  session: maintainer-2026-11-16
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction and decision
- name: Claude Fable 5.2
  role: drafting
  source: maintainer pass 2026-11-16 (anomaly)
review: draft
imported_from:
- citation: 'M. D''Onofrio, K. Rummukainen and A. Tranberg, The sphaleron rate in the minimal Standard Model, Phys. Rev. Lett. 113 (2014), 141602; arXiv:1404.3565.'
  key: DOnofrioRummukainenTranberg2014
  doi: 10.1103/PhysRevLett.113.141602
  locator: 'abstract; equations (2), (7), (8), (9)'
extraction:
  note: >-
    Imported by Leon's decision D3 of 16 November 2026, so that
    synthesis.conditional-inheritance-of-b-minus-l-and-the-conversion-coefficient-as-a-gram-ratio (clause (vii))
    and the registered asymmetry premise can pin the freeze-out temperature of the anomalous weak process and its
    position below the crossover. Read at source on 16 November 2026, the arXiv record and text of 1404.3565
    (version 1, 14 April 2014): the abstract (no true phase transition, a sharply defined crossover at
    T_c = (159 +- 1) GeV; the rate in the symmetric phase (18 +- 3) alpha_W^5 T^4; a log-linear parametrisation
    in the broken phase between 130 GeV and T_c; the freeze-out temperature T_* = (131.7 +- 2.3) GeV; the values
    are properties of the Standard Model and relevant for low-scale leptogenesis); equation (2); the fit (7) and
    its stated range; the rate (8); the criterion (9) with alpha = 0.1015 taken from its reference [11] (Burnier,
    Laine and Shaposhnikov) and the Hubble rate with g_* = 106.75. The text writes "log" in (7) without a base;
    the natural logarithm is the reading under which (7) meets (8) near T_c, and the formal level says so. The
    simulated theory is the minimal Standard Model at its physical parameters; the text does not print the Higgs
    mass used beyond referring to the discovered particle at 125 to 126 GeV. The text gives no value of the
    Higgs expectation value over the temperature at T_* or T_c. The journal reference (volume 113, article
    141602) is read from the DOI on the arXiv record; the journal page was not opened.
  maintainer_pass_2026_11_16:
    by: maintainer-2026-11-16
    date: '2026-11-16'
    note: 'Created by the maintainer pass of 2026-11-16 at Leon''s decision D3 (the lattice crossover and freeze-out temperatures as a Fact, checked at source).'
---

## formal
For the minimal Standard Model at its physical parameters, from lattice simulations of its effective three-dimensional theory; nothing here is derived in the store.
\begin{enumerate}
\item[(a)] \emph{(Crossover.)} There is no true phase transition between the symmetric and the broken phase of the weak symmetry; the crossover is sharply defined, at the pseudocritical temperature $T_{c} = 159 \pm 1$ GeV.
\item[(b)] \emph{(The rate.)} The anomalous weak process changes baryon and lepton number together, $B(t) - B(0) = L(t) - L(0) = 3\,[N_{\mathrm{CS}}(t) - N_{\mathrm{CS}}(0)]$, $N_{\mathrm{CS}}$ the Chern-Simons number of the weak field. Its rate $\Gamma$ per unit volume is, in the symmetric phase ($T > T_{c}$), $\Gamma/T^{4} = (8.0 \pm 1.3) \times 10^{-7} \approx (18 \pm 3)\,\alpha_{W}^{5}$, and in the broken phase, for $130\ \mathrm{GeV} < T < T_{c}$,
\[
\log\bigl(\Gamma/T^{4}\bigr) = (0.83 \pm 0.01)\,T/\mathrm{GeV} - (147.7 \pm 1.9),
\]
the logarithm read as natural (the source does not name the base; with this reading the two forms meet near $T_{c}$).
\item[(c)] \emph{(Freeze-out.)} The process freezes out, in the sense $\Gamma(T_{*})/T_{*}^{3} = \alpha\,H(T_{*})$ with $\alpha = 0.1015$ and $H^{2} = \pi^{2}g_{*}T^{4}/(90M_{\mathrm{Planck}}^{2})$, $g_{*} = 106.75$, at
\[
T_{*} = 131.7 \pm 2.3\ \mathrm{GeV},
\]
which is below the crossover, in the range of the broken-phase form of (b).
\end{enumerate}
\emph{Provenance:} \cite{DOnofrioRummukainenTranberg2014}, abstract and equations (2), (7), (8), (9).

## technical
For the measured Higgs mass the electroweak transition is a smooth crossover, not a true phase transition. This lattice computation finds the crossover at $159 \pm 1$ GeV and measures the rate of the anomalous weak process through it. Above the crossover the rate per unit volume is a pure number times $T^{4}$; below it the rate falls exponentially with falling temperature as the Higgs expectation value grows. Comparing the rate with the expansion rate gives the temperature at which the process stops acting, $131.7 \pm 2.3$ GeV: the process is still active for some time after the weak symmetry is broken, and freezes out in the broken phase.

## lay
The weak-force process that trades baryons against leptons worked only in the hot early universe. A large computer simulation of the known particle physics finds two temperatures: about 159 GeV, where the Higgs field switches on, smoothly and not in a sudden jump, and about 132 GeV, where the process becomes too slow to matter and stops. So the trading went on for a while after the Higgs field had begun to switch on. The series takes these numbers from the literature.

## one-liner
Lattice, minimal Standard Model: the weak transition is a crossover at $T_{c} = 159 \pm 1$ GeV, the anomalous weak process has $\Gamma/T^{4} \approx (18 \pm 3)\alpha_{W}^{5}$ above it and freezes out at $T_{*} = 131.7 \pm 2.3$ GeV, below the crossover (D'Onofrio, Rummukainen and Tranberg 2014).
