---
id: scrambling.clock-inventory-boundary-modes
kind: claim
version: 6
title: The clock inventory of the boundary modes
status: proved
region: scrambling
subject: entropy
tags: [boundary-modes, modular-theory, hawking-temperature]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T08, deposited version
- name: Claude Opus 5.5
  role: notation pass, imaginary units resolved by the unit principle (U1 to U6)
  version: 6
  source: maintainer pass 2026-11-07 (resolve units)
review: typed
derivations:
- name: main
  uses:
  - hawking.modular-structure-completed-pair@3
  - scrambling.boundary-mode-space-matrix@4
  - scrambling.imported-modes-modular-inventory@5
  - singularity.euclidean-rotor-where-it-lies@5
  - tower.witt-index-quantum-capacity@4
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T08.py
  tags:
  - label:lem:inventory
- kind: check
  ref: check.py::check_intrinsic_flows_are_bivector_flows
- kind: check
  ref: check.py::check_single_pair_is_the_boost
- kind: check
  ref: check.py::check_inventory_by_clock_criterion
- kind: check
  ref: check.py::check_pairing_trichotomy
- kind: check
  ref: check.py::check_rotated_modes_atom_boosts_and_so_nn
- kind: check
  ref: check.py::check_witt_eigenspaces_isotropic_and_dual
locators:
  paper: T08
  number: Lem 4.2
  label: lem:inventory
  line: 677
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'By the unit principle (U2) numbers on the boundary modes are read in span{1, J}, J = e_2 e_3 the complex unit of the radial atom, which commutes with the mode operators (synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom, cited in the proof): the phase circle e^{J theta n} and its generator J times a bivector, the adjoint eigenvalues +-J and +-J sqrt|cd| and the continued action e^{-+J theta} at rapidity lambda = J theta are written with J; the outside_ga declaration is removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: the proof''s point is that e^{i theta n} lies outside the real boundary-mode algebra, and the eigenvalues +-i and e^{+-i theta} are on the singularity atom of the plane e0e1, where I_4 anticommutes with the modes (conventions, known limit 1); declared (version and levels unchanged). Declaration kind set to complex-analysis by Leon''s ruling R1 (atom, boundary-mode and window flows keep i).'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: bivector flows only (Cl(3,3)); single-pair boost; clock criterion A^3 = tA on 3-mode Fock ad matrices for the inventory and the pairing trichotomy by sign of cd; rotated modes, so(n,n) dimension count, isotropic dual eigenspaces. Version 3 -> 4. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 4 -> 5.'
  env: lemma
  context_refs:
  - tower.witt-index-quantum-capacity
  outside_pilot_cites:
  - ButlerT5
  typing:
    by: ai-typing-pass
    added:
    - tower.witt-index-quantum-capacity
    note: 'Kept all four uses (repinned the Euclidean rotor to its current version 2) and added the capacity
      Fact from context_refs, whose hyperbolic pairs make the quadratic space split for the Witt-extension
      step; the E111 on \renewcommand and \roman sits in the immutable formal text and needs a notation.yaml
      entry outside this folder. Levels pass: conditions already kept.'
  i4_conversion:
    by: ai-i4-pass
    date: '2026-10-21'
    converted: []
    kept:
    - '$e^{i\theta\hat n}$ and "$i$ times a bivector": the proof''s point is that this generator lies outside
      the real boundary-mode algebra, so $I_4$ must not be substituted'
    - adjoint eigenvalues $\pm i$, $\pm i\sqrt{|cd|}$ (complex numbers as numbers)
    - $e^{\pm i\theta}$ at imaginary rapidity (analytic continuation)
    - indices $i, j$ (index)
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - tower.witt-index-quantum-capacity
  flow_note: rotor flow exp(lambda sigma/2) (T05 Thm 6.3, T08 Lem 4.2). Its clocks are intrinsic flows of
    the real Clifford boundary-mode algebra with real adjoint eigenvalues, so hyperbolic rotor flows; the
    period beta it assigns them is the Euclidean period of their continuation, the phase flow's KMS period,
    converted at kappa.
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 4
    note: 'The two boost flows: flow_note recorded.'
---

## formal
Every clock of the boundary modes runs at the modular rate $\kappa$, with period $\beta = 2\pi/\kappa = 8\pi M$. Precisely:
\begin{enumerate}
\renewcommand{\labelenumi}{(\roman{enumi})}
\item Call a flow \emph{intrinsic} when it is a one-parameter group of inner automorphisms of the boundary-mode algebra, with even generator, preserving the vector grade. The intrinsic flows of a Clifford boundary-mode algebra are rotor (bivector-generated) flows, quadratic in the pair operators.
\item Call an intrinsic flow a \emph{clock} when it is hyperbolic (its adjoint action on the mode operators semisimple with real eigenvalues) with a common rapidity across the modes it moves, the rapidity being the parameter the geometric normalisation converts to Schwarzschild time. The algebra fixes only the orbits, not the speed (Fact \claimref{scrambling.imported-modes-modular-inventory}'s reparametrisation clause), so a clock's parameter is normalised to the rapidity itself, not a multiple of it. For a single completed pair the bivector space is one-dimensional, its flow is the boost, and the conversion runs at the surface gravity $\kappa = 1/4M$.
\item A nonzero bivector generates a clock exactly when its adjoint action on the mode operators is semisimple with real eigenvalues, all nonzero ones of equal magnitude, which the normalisation to rapidity sets to one; if $\operatorname{ad}_X$ is semisimple with spectrum $\{+c, 0, -c\}$ then the $\pm c$ eigenspaces are isotropic and mutually dual for the neutral form of the boundary modes, so by Witt extension $X$ is $O(n,n)$-conjugate to $c$ times a sum of standard atom boosts; the geometric normalisation, being a property of the quadratic space rather than of a choice of modes, is invariant under that conjugation and converts every such flow at the one $\kappa$. Writing $E_{ij} = \psi_i^\dagger\psi_j$ for the gauge-invariant bilinears of the $n$-mode boundary space's mode operators $\psi_i$ (Proposition \claimref{scrambling.boundary-mode-space-matrix}, proved independently of this lemma), the cases below are illustrative rather than a partition. The diagonal $E_{ii}$ are the atoms' boosts (Fact \claimref{scrambling.imported-modes-modular-inventory}) and the equal-coefficient sum $\sum_i E_{ii}$ their simultaneous boost, all with adjoint eigenvalues $\pm 1$; the symmetric combinations $E_{ij} + E_{ji}$ are opposed pairs of boosts of the rotated modes $(\psi_i \pm \psi_j)/\sqrt{2}$, again $\pm 1$. The antisymmetric $E_{ij} - E_{ji}$ are compact and the strictly off-diagonal $E_{ij}$ nilpotent, neither carrying a rapidity; a mixed diagonal $\sum_i c_i E_{ii}$ with unequal $|c_i|$ has no common rapidity. And the pairing sector $c\,\psi_i^\dagger\psi_j^\dagger + d\,\psi_j\psi_i$, outside $\mathfrak{gl}(n)$ and completing the bivector algebra of the completed boundary mode space, of dimension $n(2n-1)$ against $\mathfrak{gl}(n)$'s $n^2$ (the $n$ hyperbolic pairs of Fact \claimref{tower.witt-index-quantum-capacity} make the quadratic space split, so that algebra is $\mathfrak{so}(n,n)$), is classified by the sign of one product, its adjoint eigenvalues being $\pm\sqrt{cd}$: hyperbolic for $cd > 0$ (a clock, at unit rapidity outright when $cd = 1$), compact for $cd < 0$, nilpotent for $cd = 0$.
\end{enumerate}
The boundary mode space therefore has many intrinsic flows and one clock rate: whichever clock is read, single-atom, rotated-pair, common, or paired, its period is $\beta$.

## technical
An intrinsic flow of the boundary-mode algebra is a one-parameter group of inner automorphisms with even generator preserving the vector grade; such flows are generated by bivectors, quadratic in the pair operators. A clock is an intrinsic flow whose adjoint action on the mode operators is semisimple with real eigenvalues, the nonzero ones of one common magnitude normalised to unit rapidity. For a single completed pair the only clock is the boost, converted to Schwarzschild time at the surface gravity $\kappa = 1/4M$.

For $n$ modes, a bivector with adjoint spectrum $\{+c, 0, -c\}$ is $O(n,n)$-conjugate, by Witt extension, to $c$ times a sum of standard atom boosts, and the geometric normalisation converts every such flow at the same $\kappa$. Examples are the single-atom boosts $E_{ii}$, the rotated-pair boosts $E_{ij} + E_{ji}$ and the pairing terms $c\,\psi_i^\dagger\psi_j^\dagger + d\,\psi_j\psi_i$ with $cd > 0$; antisymmetric, nilpotent and unequal-weight combinations are not clocks. Every clock therefore has period $\beta = 2\pi/\kappa = 8\pi M$.

## lay
The black hole's boundary modes can evolve internally in many ways, but only some of these behave like clocks ticking at a steady rate. Every such clock, however it is built from the modes, runs at one and the same rate, set by the surface gravity of the horizon. So all of them share a single period, the black hole's natural thermal cycle.

## one-liner
Every clock of the boundary modes runs at the modular rate $\kappa$, so every one has period $\beta = 2\pi/\kappa = 8\pi M$.
