---
id: dark-matter.mode-counts-two-modules-which-one
kind: claim
version: 6
title: 'Mode counts: two modules, and which one the series'' matter lies in'
status: proved
region: dark-matter
subject: dark-matter
tags: [mode-counting, spinor-modules, dark-matter-ratio]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14, deposited version
review: typed
derivations:
- name: main
  uses:
  - dark-matter.mirror-tower-copy-one@8
  - dark-matter.type-residue-what-each-tower-can@5
  - tower.commuting-copies@5
  - tower.fock-module-one-qubit-per-rung@6
  - tower.witt-index-quantum-capacity@5
  assumes:
  - dark-matter.p1-single-frozen-point@1
  - dark-matter.p2-indifference@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T14.py
  tags:
  - label:thm:modes
- kind: check
  ref: check.py::check_rung_factor_is_residue_independent
- kind: check
  ref: check.py::check_ground_module_dimensions
- kind: check
  ref: check.py::check_weightings_depend_on_the_convention
- kind: check
  ref: check.py::check_odd_tower_pair_counts
locators:
  paper: T14
  number: Thm 4.4
  label: thm:modes
  line: 354
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: Witt index 1 + k and Fock factor 2^k; ground-module dimensions from the exported type computation; weightings 9/2, 13/4, 10, 15/2; complex pair counts 2 and 3. Version 5 -> 6.'
  env: theorem
  context_refs:
  - dark-matter.towers-are-residues-single-clock-filter
  - dark-matter.which-towers-can-carry-arrow
  - tower.witt-index-quantum-capacity
  outside_pilot_cites:
  - ButlerT9
  typing:
    by: ai-typing-pass
    added:
    - tower.witt-index-quantum-capacity
    - dark-matter.p1-single-frozen-point
    note: 'Added the tower paper''s capacity theorem, cited for the rung factor in clause (i), and P1,
      which the statement invokes for the common rung height; the residue proposition and the which-towers
      corollary are cited only for the labelling convention and a comparison, so they stay unedged. Levels
      pass: all three plain levels now name P1 (common rung height) and P2 (both modules counted); the
      lay level had dropped both.'
  source_title: 'Mode counts: two modules, and which one the series'' matter lies in'
  source_formal: |-
    Let the towers be populated at a common rung height $k$ (one descent, P1). The tower paper's Fock module of tower $r$ at that height is $S_{r} \otimes \mathcal{F}_{k}$, the ground spinor module tensored with the Fock space of the $k$ ladder pairs, with $\tfrac{1}{2}\dim_{\R} S_{r} \cdot 2^{k}$ fermionic modes; the Standard-Model paper's derived matter is a different object, the state space $\Lambda^{\bullet}(\C^{2} \oplus \C^{3})$ of five twistor modes, built from the conformal spin group alone (Theorem \claimref{dark-matter.mirror-tower-copy-one}(ii)). Then:
    \begin{enumerate}
    \item[(i)] the rung factor does not depend on the residue: every populated P3 representative has Witt index $\min(p,q) = 1$, so the capacity at height $k$ is $1 + k$ in every tower \cite[Thm.~4.3]{ButlerT3} and the Fock factor $\mathcal{F}_{k}$ has dimension $2^{k}$ in every tower;
    \item[(ii)] the ground factor is not: with both irreducible modules counted where the centre splits (Premise \claimref{dark-matter.p2-indifference}: selecting one of two inequivalent modules by the sign of the volume element would be an uncaused choice), $\dim_{\R} S_{r}$ is $8$ at $r = 6$, $4$ at $r = 2$, $4$ at $r = 1$, $4$ at $r = 7$, $8$ at $r = 3$ and $16$ at $r = 5$; with one module each, $2$ at $r = 1$ and $8$ at $r = 5$;
    \item[(iii)] hence the ground-module weighting of the five dark towers' Fock modes relative to this one's, in the labelling convention of Proposition \claimref{dark-matter.towers-are-residues-single-clock-filter}, is
    \[
    \sum_{r \neq 6} \frac{n_{r}}{n_{6}} \;=\; \frac{1}{2} + \frac{1}{2} + \frac{1}{2} + 1 + 2 \;=\; \frac{9}{2} \qquad\text{(both modules)},\qquad\text{or}\qquad \frac{13}{4}\ \text{(one module each)},
    \]
    and in the opposite convention, where this world is the $4$-dimensional real module and the mirror the $8$-dimensional quaternionic one, $40/4 = 10$ and $30/4 = 15/2$: the weighting depends on the convention because it divides by a named member's module, and it counts modes, not anything that enters an asymmetric sum (Corollary \claimref{dark-matter.which-towers-can-carry-arrow});
    \item[(iv)] but the series' matter is the derived state space, not the full Fock module, and the mirror's is identical to this tower's (Theorem \claimref{dark-matter.mirror-tower-copy-one}), so $n_{2} = n_{6}$ and the mirror's weight is $1$, not $\tfrac{1}{2}$; for the odd towers the state space needs the twistor correspondence in dimensions three and five, which the series establishes only in four \cite{ButlerT9}, so $n_{1,7,3,5}$ are not determined here beyond the pair counts $2$ (three dimensions) and $3$ (five), and they do not enter the asymmetric count, the odd towers carrying no asymmetry.
    \end{enumerate}
    The $9/2$ (or $10$) of (iii) is the value of a computation in a convention, not the count, by (iv).
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: 'Converted the twistor modes to conformal spinor modes and the twistor correspondence to the correspondence between points and lines of conformal spinors (formal, technical, proof). Kept $V_{\C}$ in the pair-count step: a maximal isotropic subspace of the complexified vector space is not an $I_6$-renaming.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - tower.witt-index-quantum-capacity
    - dark-matter.p1-single-frozen-point
    - dark-matter.p2-indifference
---

## formal
Let the towers be populated at a common rung height $k$ (one descent, P1). The tower paper's Fock module of tower $r$ at that height is $S_{r} \otimes \mathcal{F}_{k}$, the ground spinor module tensored with the Fock space of the $k$ ladder pairs, with $\tfrac{1}{2}\dim_{\R} S_{r} \cdot 2^{k}$ fermionic modes; the Standard-Model paper's derived matter is a different object, the state space $\Lambda^{\bullet}(\C^{2} \oplus \C^{3})$ of five conformal spinor modes (twistor modes), built from the conformal spin group alone (Theorem \claimref{dark-matter.mirror-tower-copy-one}(ii)). Then:
\begin{enumerate}
\item[(i)] the rung factor does not depend on the residue: every populated P3 representative has Witt index $\min(p,q) = 1$, so the capacity at height $k$ is $1 + k$ in every tower \cite[Thm.~4.3]{ButlerT3} and the Fock factor $\mathcal{F}_{k}$ has dimension $2^{k}$ in every tower;
\item[(ii)] the ground factor is not: with both irreducible modules counted where the centre splits (Premise \claimref{dark-matter.p2-indifference}: selecting one of two inequivalent modules by the sign of the volume element would be an uncaused choice), $\dim_{\R} S_{r}$ is $8$ at $r = 6$, $4$ at $r = 2$, $4$ at $r = 1$, $4$ at $r = 7$, $8$ at $r = 3$ and $16$ at $r = 5$; with one module each, $2$ at $r = 1$ and $8$ at $r = 5$;
\item[(iii)] hence the ground-module weighting of the five dark towers' Fock modes relative to this one's, in the labelling convention of Proposition \claimref{dark-matter.towers-are-residues-single-clock-filter}, is
\[
\sum_{r \neq 6} \frac{n_{r}}{n_{6}} \;=\; \frac{1}{2} + \frac{1}{2} + \frac{1}{2} + 1 + 2 \;=\; \frac{9}{2} \qquad\text{(both modules)},\qquad\text{or}\qquad \frac{13}{4}\ \text{(one module each)},
\]
and in the opposite convention, where this world is the $4$-dimensional real module and the mirror the $8$-dimensional quaternionic one, $40/4 = 10$ and $30/4 = 15/2$: the weighting depends on the convention because it divides by a named member's module, and it counts modes, not anything that enters an asymmetric sum (Corollary \claimref{dark-matter.which-towers-can-carry-arrow});
\item[(iv)] but the series' matter is the derived state space, not the full Fock module, and the mirror's is identical to this tower's (Theorem \claimref{dark-matter.mirror-tower-copy-one}), so $n_{2} = n_{6}$ and the mirror's weight is $1$, not $\tfrac{1}{2}$; for the odd towers the state space needs the correspondence between points and lines of conformal spinors (the twistor correspondence) in dimensions three and five, which the series establishes only in four \cite{ButlerT9}, so $n_{1,7,3,5}$ are not determined here beyond the pair counts $2$ (three dimensions) and $3$ (five), and they do not enter the asymmetric count, the odd towers carrying no asymmetry.
\end{enumerate}
The $9/2$ (or $10$) of (iii) is the value of a computation in a convention, not the count, by (iv).

## technical
With the towers populated at a common rung height $k$ (one descent, Premise P1), tower $r$'s Fock module is $S_{r} \otimes \mathcal{F}_{k}$, with $\tfrac{1}{2}\dim_{\R} S_{r} \cdot 2^{k}$ fermionic modes. The rung factor does not depend on the residue: every populated representative has Witt index $\min(p,q) = 1$, so $\dim \mathcal{F}_{k} = 2^{k}$ in every tower. The ground factor does: counting both irreducible modules where the centre splits, as Premise P2 (indifference) requires, $\dim_{\R} S_{r}$ is $8, 4, 4, 4, 8, 16$ at $r = 6, 2, 1, 7, 3, 5$, so the five dark towers' weighting relative to this one is $\sum_{r \neq 6} n_{r}/n_{6} = 9/2$, or $13/4$ with one module each, and $10$ or $15/2$ in the opposite labelling convention.

That weighting depends on the convention and is not the count. The series' matter is the derived state space $\Lambda^{\bullet}(\C^{2} \oplus \C^{3})$ of five conformal spinor modes, not the full Fock module, and the mirror's is identical to ours, so $n_{2} = n_{6}$. For the odd towers the state space would need the correspondence between points and conformal spinors in three and five dimensions, which is established only in four, so $n_{1,7,3,5}$ are fixed only up to the pair counts $2$ and $3$, and they do not enter the asymmetric count.

## lay
Assume, as the paper's premises do, that all the hidden worlds came from one descent and so sit at a common height on the ladder (Premise P1), and that where there are two mirror-image versions of the basic module both are counted (the indifference premise P2). One can then count how many particle states each hidden world has from the raw algebra, but the answer depends on bookkeeping choices, such as which world's count is used as the yardstick. The matter the framework actually derives lives in a smaller, specific space of states, and for the mirror world that space is exactly the same as ours. For the odd-dimensional worlds the corresponding count is not yet available beyond a count of their pairs.

## one-liner
Under P1 and P2, raw Fock-module counts give a convention-dependent dark weighting of $9/2$ (or $10$), but the series' matter is the derived state space, identical for the mirror ($n_{2} = n_{6}$) and undetermined for the odd towers beyond their pair counts.
