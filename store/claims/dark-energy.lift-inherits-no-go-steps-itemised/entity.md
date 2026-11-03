---
id: dark-energy.lift-inherits-no-go-steps-itemised
kind: claim
version: 2
title: The lift inherits the no-go, with its steps itemised
status: proved
region: dark-energy
subject: dark-energy
tags: [no-go, quantum-gravity, ledger-audit]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T10, deposited version
review: typed
derivations:
- name: main
  uses:
  - dark-energy.acoustic-no-go-one-way-grip@3
  - dark-energy.imported-walls-sphere-theorem@6
  - dark-energy.point-infinity-has-no-physical-fluctuation@4
  - interior.imported-equivalence-einstein-equations@2
  - scrambling.principality-indifference-sphere@4
  assumes:
  - scrambling.indifference-structural-premise-series@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_partial_waves_diagonal
- kind: check
  ref: check.py::check_spin_separates_from_singlet
- kind: proof
  derivation: main
locators:
  paper: T10
  number: Asm 5.5
  label: asm:lift
  line: 999
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the finite cores of steps 1 and 4: harmonics of different degree orthogonal on the sphere, and spin-l operators of zero overlap with singlets in su(2)-invariant states. Version 1 -> 2.'
  typing:
    by: ai-typing-pass
    added:
    - dark-energy.acoustic-no-go-one-way-grip
    - dark-energy.imported-walls-sphere-theorem
    - dark-energy.point-infinity-has-no-physical-fluctuation
    - interior.imported-equivalence-einstein-equations
    - scrambling.indifference-structural-premise-series
    - scrambling.principality-indifference-sphere
    note: 'The Indifference principle is stored with status proved, not postulate, so it is carried in
      uses rather than assumes; the near-horizon reduction step has no store entity and remains at assembly
      level in the text only. Hypothesis pass: moved scrambling.indifference-structural-premise-series
      from uses to assumes, now that it is a postulate. Levels pass: the lay level now names the Indifference
      premise, the rotationally symmetric state and the assembly-level step; the one-liner adds the $\mathfrak{su}(2)$-invariant
      state.'
  env: assembly
  context_refs:
  - dark-energy.acoustic-no-go-one-way-grip
  - dark-energy.imported-walls-sphere-theorem
  - dark-energy.point-infinity-has-no-physical-fluctuation
  - interior.imported-equivalence-einstein-equations
  - scrambling.indifference-structural-premise-series
  - scrambling.principality-indifference-sphere
  flags:
  - no proof environment found
---

## formal
The remaining open item, that the four-dimensional lift might introduce a coupling invisible to the s-wave sector, is addressed by covering the spacetime in two pieces, with one step upgraded. The steps, each with its provenance:
\begin{enumerate}
\item \emph{Partial waves (exact, kinematic).} Near the horizon the four-dimensional two-point function between the graviton mode and any probe decomposes over partial waves, and the angular integration is diagonal in $\ell$ by spherical-harmonic orthogonality.
\item \emph{Near-horizon reduction (assembly, at the level it carries in T5).} Each fixed-$\ell$ sector reduces, at the horizon where the potential barrier vanishes, to a two-dimensional copy of the setting of the current algebra, in which the $\ell$-th component of the graviton mode is the $\ell$-th $\mathfrak{su}(2)$-harmonic of the current bilinears. Which operator is the stress tensor in the $\ell$-th copy is fixed by step (4), not assumed.
\item \emph{Exterior exactness (imported theorem).} On any region where the gauge-theoretic metric is invertible, the horizon included, the description coincides exactly with classical general relativity, by the geometry paper's import of gauge-theory gravity from Lasenby, Doran and Gull \cite[Fact~2.1]{ButlerT6}, whose couplings to the metric are stress-energy alone. The two pieces overlap and cover the spacetime.
\item \emph{The sphere step (conditional on the entropy paper's Indifference premise; then proved by covariance).} By the sphere theorem (Fact \claimref{dark-energy.imported-walls-sphere-theorem}, \cite[Thm.~5.5]{ButlerT8}, conditional on \cite[Principle~5.4]{ButlerT8}) every angular operator of the lift is a boundary-mode bilinear of definite spin under the adjoint $\mathfrak{su}(2)$, of spin $\ell \geq 1$ for every non-trivial harmonic, while the s-wave stress tensor $T$ is an $\mathfrak{su}(2)$ singlet. In an $\mathfrak{su}(2)$-invariant state the symmetry orthogonality of Proposition \claimref{dark-energy.acoustic-no-go-one-way-grip} applies verbatim: nonzero spin, zero overlap. Orthogonality by dimension would \emph{not} do here, the bilinears having dimension two like $T$; it is the spin that separates them. The lift inherits the no-go because the sphere is built from the same correlations to which the no-go applies, and those correlations carry spin.
\end{enumerate}
With Propositions \claimref{dark-energy.acoustic-no-go-one-way-grip} and \claimref{dark-energy.point-infinity-has-no-physical-fluctuation} and these steps, the acoustic programme is closed at the mixed level of its inputs: the metric-forming correlations admit exactly one coupling sector, its weakness is dimensional, its leading nonlinearity is Gertsenshtein's, and its Goldstones are eaten. Step (2), the near-horizon reduction, is at assembly level, its promotion shared with T5 and T7; step (4) is conditional on the entropy paper's Indifference premise, and the closure of the acoustic programme inherits that condition.

## technical
The open item is whether the four-dimensional lift could introduce a coupling invisible to the s-wave sector, and it is addressed by covering spacetime in two overlapping pieces. Near the horizon, the two-point function of the graviton mode with any probe decomposes over partial waves, diagonal in $\ell$; each fixed-$\ell$ sector reduces, at assembly level, to a copy of the current-algebra setting; and by the sphere theorem, conditional on the Indifference premise, every angular operator is a boundary-mode bilinear of spin $\ell\geq 1$ under the adjoint $\mathfrak{su}(2)$ while the s-wave $T$ is a singlet, so the symmetry orthogonality of the no-go gives zero overlap in an $\mathfrak{su}(2)$-invariant state. Wherever the gauge-theoretic metric is invertible, the horizon included, the description is classical general relativity, whose couplings to the metric are stress-energy alone.

It is spin, not scaling dimension, that separates the angular bilinears from $T$, since both have dimension two. With the no-go and the pure-gauge $(I,V)$-sector this closes the acoustic programme at the mixed level of its inputs: one coupling sector. The near-horizon reduction is at assembly level, and the closure inherits the Indifference condition.

## lay
The no-coupling result was first proved in a simplified, spherically averaged version of the theory. This result extends it to the full four-dimensional spacetime by splitting spacetime into a region near the horizon, where, in a rotationally symmetric state, the angular pieces carry spin and so cannot overlap with the spinless graviton mode, and a region where the ordinary equations of general relativity hold. The extension rests on one step done at a lower level of rigour, the near-horizon reduction, and is conditional on the series' Indifference premise.

## one-liner
At assembly level and conditional on the Indifference premise, the four-dimensional lift inherits the acoustic no-go: near the horizon the angular modes carry nonzero spin and decouple from $T$ in an $\mathfrak{su}(2)$-invariant state, and elsewhere classical general relativity couples to stress-energy alone.
