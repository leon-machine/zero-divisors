---
id: synthesis.s-wave-array-is-a-boundary-mode-set
kind: claim
version: 4
title: 'The s-wave array is a boundary-mode set'
status: proved
region: synthesis
subject: thermality
tags: [boundary-modes, car-algebra, modular-theory, needs-continuum]
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
  version: 4
  source: maintainer pass 2026-11-07 (GA units)
review: draft
about:
- obj.hawking.boundary-mode-algebra-windows-boost-dynamics
derivations:
- name: main
  uses:
  - singularity.bosonisation-bridge-s-wave-sector@7
  - tower.ladder-pairs-satisfy-car-vectors@4
  - hawking.imported-algebra-boundary-modes-car-algebra@5
  - tower.answers-iteration-question@5
  - hawking.gibbs-states-are-kms-conversely-finite@2
  - hawking.i-state@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_tower_pairs_give_windows
- kind: check
  ref: check.py::check_particle_hole_turns_array_into_positive_modes
- kind: check
  ref: check.py::check_zero_mode_kms_is_trace
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - note.hawking.setting-mode-continuum
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The boost phases on the boundary-mode array are written in the field unit I_4 (the unit of the boundary-mode algebra); nothing stays (v_i, w_j, delta_{ij} are indices).'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'check_tower_pairs_give_windows asserts the dimension 4^n of the generated algebra (rank of ordered words, n = 1..4); docstring (3) sign slip e^{beta omega} -> e^{-beta omega} fixed. Version 1 -> 2. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 2 -> 3.'
  open_problem: op.boundary-mode-provenance
  note: 'Gives the boundary modes one provenance: the ladder pairs of the blown-up singular boundary aggregated into the s-wave array (the singularity paper''s flagged identification), with the tower of iterated completions as the model of their algebra only. The array becomes a mode set of the thermality paper''s definition after particle-hole conjugation below the level, each positive frequency then occurring twice, and the one zero-frequency mode, excluded by the definition, is forced into the trace by the KMS relation, so the singularity paper''s state on the array is the I-state on that mode set tensored with the trace. Transport-convenient: the tower model is the series'' own; the rest is standard fermion bookkeeping.'
---

## formal
Let $\{\psi_k, \psi_k^{\dagger}\}_{k \in \mathbb{Z}}$ be the s-wave array of boundary modes of Theorem \claimref{singularity.bosonisation-bridge-s-wave-sector}, with boost weights $\omega_k = \kappa k$ and the sea filled below the level, and let $\beta = 2\pi/\kappa$.
\begin{enumerate}
\item[(i)] \emph{(The tower is the model, not the count.)} The adjoined null pairs of the tower satisfy the CAR exactly at the level of vectors (Fact \claimref{tower.ladder-pairs-satisfy-car-vectors}), so $n$ rungs realise a window algebra of $n$ modes and the tower limit is the CAR algebra over a countable set (Fact \claimref{hawking.imported-algebra-boundary-modes-car-algebra}). On the physical closure one ascent completes the description, further rungs lying on shadow walls outside the physical region (Corollary \claimref{tower.answers-iteration-question}(1)); so the physical boundary modes are not counted by rungs, and the tower supplies the form of their algebra only.
\item[(ii)] \emph{(Particle-hole conjugation makes the array a mode set.)} Put $b_k := \psi_k^{\dagger}$ for $k < 0$ and $b_k := \psi_k$ for $k \geq 0$. The $b_k$ satisfy the CAR, the boost dynamics acts as $b_k \mapsto e^{-I_{4}\kappa|k|t}b_k$ (the unit of the mode space is $I_{4}$), and on every finite window $\sum_k \kappa k\,N_k = \sum_k \kappa|k|\,N'_k + \sum_{k<0}\kappa k$ with $N'_k = b_k^{\dagger}b_k$, so the Gibbs state of the one is the Gibbs state of the other. Each frequency $\kappa m$, $m \geq 1$, occurs exactly twice (a particle at $k = m$, a hole at $k = -m$), and the frequency $0$ once, at $k = 0$. The Fermi-Dirac marginals $n_k = (e^{\beta\kappa k} + 1)^{-1}$ of the bosonisation theorem become $\langle N'_k\rangle = (e^{\beta\kappa|k|} + 1)^{-1}$ for $k \neq 0$.
\item[(iii)] \emph{(The zero mode is in its trace state.)} On one mode of frequency $\omega \geq 0$ the KMS relation at $\beta$ is $n = e^{-\beta\omega}(1 - n)$, whose unique solution is the Fermi-Dirac value; at $\omega = 0$ it is $n = \tfrac12$, the trace.
\end{enumerate}
Consequently the definition of the boundary-mode algebra (Definition \claimref{obj.hawking.boundary-mode-algebra-windows-boost-dynamics}) applies with $J = \mathbb{Z}\setminus\{0\}$ and $\omega_j = \kappa|j|$, with one provenance, the ladder pairs of the blown-up singular boundary aggregated over s-wave channels, and the tower as model. Under (Q), the state of the array with these marginals, quasi-free on $J$, is the I-state of Theorem \claimref{hawking.i-state} on that mode set, and the excluded zero mode carries the trace, so the extension to the full array has no free parameter.

## technical
The boundary modes have two descriptions in the series: as rungs of the tower of iterated completions, whose limit is a CAR algebra over a countable set, and as the ladder pairs of the blown-up singular boundary, one per point, aggregated over s-wave channels into an array $\psi_k$, $k \in \mathbb{Z}$, with weights $\kappa k$ and a filled sea. The tower's null pairs satisfy the CAR exactly, so they model the algebra; but the physical closure has one ascent, further rungs sitting on shadow walls, so they do not count the modes.

The array becomes a mode set of the thermality paper's definition by particle-hole conjugation below the level: $b_k = \psi_k^{\dagger}$ for $k < 0$. The Hamiltonian changes by a constant, every frequency becomes $\kappa|k| \geq 0$, each positive frequency appears twice (particle and hole), and the Fermi-Dirac marginals stay Fermi-Dirac at $\kappa|k|$. One mode has frequency zero; the thermality paper's definition requires positive frequencies and so excludes it, but the KMS relation forces its occupation to $1/2$, the trace. So, under (Q), the singularity paper's quasi-free state on the array is the I-state on $J = \mathbb{Z}\setminus\{0\}$ with $\omega_j = \kappa|j|$, tensored with the trace on the zero mode.

## lay
The series describes the quantum modes at a black hole's singularity in two ways: as the steps of an infinite tower of algebraic completions, and as one pair of modes at each point of the singularity's boundary, gathered into a list by keeping the spherically symmetric part. The first description is only a mathematical model: physically the tower stops after one step. This result makes the second description fit the thermal theory exactly. Modes below the filled level are relabelled as holes, which makes every frequency positive; each frequency then appears twice, once for a particle and once for a hole; and the single mode of zero frequency, which the thermal theory's definition leaves out, is forced to be exactly half occupied. Given the singularity paper's assumption that the joint state is of the simplest (quasi-free) kind, its thermal state is then the series' unique thermal state, with nothing left to choose.

## one-liner
The boundary modes have one provenance, the s-wave array of ladder pairs, with the tower as model only; conjugating below the level makes it a mode set with frequencies $\kappa|k|$ (each positive one twice), and the excluded zero mode is forced into the trace, so under (Q) the array's quasi-free state is the I-state with nothing free.
