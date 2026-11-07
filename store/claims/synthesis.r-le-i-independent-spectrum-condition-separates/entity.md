---
id: synthesis.r-le-i-independent-spectrum-condition-separates
kind: claim
version: 3
title: '(R), (L$_E$) and (I) are independent; a ground-state condition separates two'
status: proved
region: synthesis
subject: thermality
tags:
- thermal-premises
- entropy-premises
- finite-models
- no-go
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
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: unit pass, every imaginary unit resolved to the geometric-algebra unit it stands for
  version: 3
  source: maintainer pass 2026-11-07 (resolve units)
review: draft
derivations:
- name: main
  uses:
  - angle.within-supplied-class-spectrum-condition-selects@4
  - angle.hop-sea-filled-pairing@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_four_models_independence
- kind: check
  ref: check.py::check_pairing_ground_state_is_thermal_at_every_q
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - singularity.l-boundary-mode-locality
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Folded into version 3 of this pass. The window is boundary modes (U2): its numbers are read in span{1, J}, J = e_2 e_3 the complex unit of the radial atom (synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom, cited in the formal level), the source unit i read as J; the Killing flows Ad(e^{J t omega_k K_k}) and the continuation to imaginary time Jp (alpha^k_{Jp}(a_k) = q_k^{-1} a_k, the signs of that result) are written with J; the Jordan-Wigner space C^2 (x) C^2 has this field as scalars. No i remains; declaration removed. Mathematics, links and checks unchanged.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (complex-analysis): the Killing flows Ad(e^{it omega_k K_k}) and the imaginary-time continuation act on window modes realised by Jordan-Wigner on C^2 (x) C^2, a complex space the store does not tie to I_4.'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 1 -> 2.'
  open_problem: pr.locality-and-interface
  note: The three premises are postulates and are discussed, not assumed, so they are cited in the text and not listed as uses. Independence result for the premise target. It shows that none of (R), (L_E), (I) follows from the other two on finite windows, and that a premise selecting the window state as the unique ground state of the window dynamics cannot deliver (R) and (L_E) together (uniqueness is needed, since a degenerate ground space can hold both); so any single premise replacing (R) and (L_E) must select the state by other means. Transport-absent (finite fermionic models). The pairing family gives, for every Boltzmann factor, a generator with a unique thermal ground state; at one Boltzmann factor it agrees with the stored pairing form on the even sector only. It does not derive either premise.
---

## formal
Model a window by $\nu$ fermionic modes $a_{k}$ with their Killing flows $\alpha^{k}_{t} = \operatorname{Ad}(e^{Jt\omega_{k}K_{k}})$, $K_{k} = N_{k} - \tfrac12$, $\omega_{k} > 0$ (the window's numbers are read in $\mathrm{span}\{1, J\}$, $J = e_{2}e_{3}$ the complex unit of the boundary modes' radial atom, Theorem \claimref{synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom}, which commutes with the radial plane and with every vector orthogonal to spacetime, hence with every mode), a state $\omega$, a dynamics generator $H = H^{*}$ in the window algebra, and an exterior channel map $a^{\mathrm{out}}_{k} = \sum_{j}T_{kj}a_{j} + (\text{vacuum-fed terms})$, with $T$ a contraction on the channel space. Read the premises as: (R) each single-mode marginal of $\omega$ is $(\alpha^{k}, p)$-KMS at $p = 2\pi/\kappa$, as in Premise \claimref{singularity.r-regularity-fixed-locus}, equivalently its Boltzmann factor is $q_{k} = e^{-p\omega_{k}}$; (L$_E$) $H$ commutes with every $N_{k}$, as in Premise \claimref{singularity.l-boundary-mode-locality}; (I) $T$ is diagonal, so there is no cross-channel mixing: each channel feeds its own asymptotic channel, possibly attenuated by a vacuum-fed (greybody) loss, as in Premise \claimref{hawking.premise-i-interface-identification}; and the unique-ground-state condition (S) $\omega$ is the unique ground state of $H$.
\begin{enumerate}
\item[(i)] \emph{(Independence.)} On two modes: (M1) $H = \omega_{0}N_{0} + \omega_{1}N_{1}$, the product Gibbs state and $T = 1$ satisfy (R), (L$_E$), (I), with $\omega$ stationary for $H$; (M2) the same $H$ with the vacuum $\ket{00}$ and $T = 1$ satisfies (L$_E$), (I) and (S) but not (R), at any Boltzmann factor; (M3) the pairing generator below with its ground state and $T = 1$ satisfies (R), (I) and (S) but not (L$_E$); (M4) the state and generator of (M1) with a beam splitter $T$ of nonzero mixing angle and $q_{0} \ne q_{1}$ satisfy (R) and (L$_E$) but not (I). So none of (R), (L$_E$), (I) follows from the other two.
\item[(ii)] \emph{(Pairing realises (R) with (S) at every Boltzmann factor.)} For $0 < t < 1$ and $g > 0$ let $H_{t} = g\bigl[\tfrac{1 - t^{2}}{2t}(N_{0} + N_{1}) + a_{0}^{*}a_{1}^{*} + a_{1}a_{0}\bigr]$. Its unique ground state is $\ket{00} - t\ket{11}$ (with $\ket{11} = a_{0}^{*}a_{1}^{*}\ket{00}$), of energy $-gt$, separated from the rest of the spectrum, and both single-mode marginals are Gibbs with Boltzmann factor $t^{2}$; so for equal frequencies (R) holds with $t = e^{-p\omega/2}$, while $H_{t}$ does not commute with $N_{0}$.
\item[(iii)] \emph{(The unique-ground-state condition separates.)} Under (S), (L$_E$) excludes (R) (Proposition \claimref{angle.within-supplied-class-spectrum-condition-selects}(i): the unique ground state of a number-diagonal generator is a number basis state, with pure marginals), and by (ii) (R) is realised under (S) only outside (L$_E$). Hence no premise that selects the window state as the unique ground state of the window dynamics can yield (R) and (L$_E$) together. Uniqueness is needed: without it the exclusion fails, since the number-diagonal $H = (N_{0} - N_{1})^{2}$ has a degenerate ground space containing a state with thermal marginals (Proposition \claimref{angle.within-supplied-class-spectrum-condition-selects}(ii)).
\end{enumerate}

## technical
The three thermal-chain premises constrain different things: (R) the single-mode marginals of the state, (L$_E$) the generator of the window dynamics, (I) the exterior channel map. Four two-mode models, each checked in exact arithmetic, realise every pattern in which exactly one premise fails, so none is a consequence of the other two. They are linked only through a selection rule for the state. Under the unique-ground-state condition the link is exclusive: a number-diagonal generator has a number basis ground state, which is not thermal, while a two-mode pairing generator has, for every Boltzmann factor, a unique gapped ground state whose marginals are thermal. A single premise that replaces (R) and (L$_E$) therefore cannot be a unique-ground-state selection on the window; with a degenerate ground space the exclusion fails.

## lay
Three of the series' assumptions about black-hole thermality concern different things: the temperature of each mode, which kinds of internal dynamics are allowed, and how modes reach distant observers. Small explicit models show that none of the three can be deduced from the other two. They also show that picking the state as the single lowest-energy state of the internal dynamics would force a choice between the first two assumptions, so any single principle replacing both must pick the state some other way.

## one-liner
Explicit two-mode models make (R), (L$_E$), (I) mutually independent on finite windows; under a unique-ground-state condition (R) and (L$_E$) exclude each other, (R) being realised by a unique pairing ground state at every Boltzmann factor.
