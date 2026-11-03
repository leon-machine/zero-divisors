---
id: tower.answers-iteration-question
kind: claim
version: 5
title: Answers to the iteration question
status: proved
region: tower
subject: tower
tags: [car-algebra, limits]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T03, deposited version
review: typed
about:
- obj.tower.tower
derivations:
- name: main
  uses:
  - tower.wall-package@5
  - tower.rigidity-clock-frozen@5
  - tower.algebraic-limit-even-charge@3
  - tower.car-limit-even-charge@5
  assumes:
  - sheaf.tameness@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_clock_never_ticks
- kind: check
  ref: check.py::check_one_qubit_per_rung
- kind: proof
  derivation: main
locators:
  paper: T03
  number: Cor 6.2
  label: cor:iteration
  line: 464
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the frozen clock on the physical tower (charge 6, centre R, Mat_{2^(k+1)}(H) from a quaternion corner) and one CAR mode per rung. Version 4 -> 5.'
  env: corollary
  context_refs:
  - tower.algebraic-limit-even-charge
  - tower.car-limit-even-charge
  - tower.rigidity-clock-frozen
  typing:
    by: ai-typing-pass
    added:
    - tower.rigidity-clock-frozen
    - tower.algebraic-limit-even-charge
    - tower.car-limit-even-charge
    note: 'Added the rigidity theorem and the two even-charge limit theorems, which clauses 2 and 3 cite
      as their content; kept the wall package and the tameness postulate. Version bumped to 2 for the
      edge change; existing @1 pins from other claims are left for the repin pass. Levels pass: lay and
      one-liner now keep the compact-wall and trivial-radical hypotheses, and technical names tameness
      as an assumption.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - tower.algebraic-limit-even-charge
    - tower.car-limit-even-charge
    - tower.rigidity-clock-frozen
    - sheaf.tameness
---

## formal
Let $(M, G)$ be a tame corank-one degeneration in the sense of \cite[Hyp.~2.1]{ButlerT4}, with trivial radical line bundle and compact wall as in Fact \claimref{tower.wall-package}, presenting the transport demand of the series' geometric setting.
\begin{enumerate}
\item \emph{Where ascent is forced.} On the physical closure, one ascent completes the description: by Fact \claimref{tower.wall-package} the one-sided completion is nondegenerate up to and including the wall and the transported reciprocal divides totally there; nothing on the physical side demands a second rung. Beyond the physical region, the demand repeats: by Fact \claimref{tower.wall-package} the degeneration relocates to a tame shadow wall, and the infinite wall sequence carries exactly one rung of this paper's tower per wall, displaced successively away from the physical region.
\item \emph{Why the clock never ticks.} Theorem \claimref{tower.rigidity-clock-frozen}: the tower is Morita-stationary from its first step, and the mod-8 structure classifies the eight parallel towers, not stages of one.
\item \emph{What the limit is.} Theorems \claimref{tower.algebraic-limit-even-charge} and \claimref{tower.car-limit-even-charge}: for even transport charge, the ground algebra tensored with the free fermionic field algebra, the modes being the transported null pairs themselves.
\end{enumerate}
The depth of the hierarchy, on this account: one forced conformal ascent, plus a fermionic ladder of capacity, one qubit per rung.

## technical
Assuming tameness, for a corank-one degeneration with trivial radical line bundle and compact wall, the iteration question has three answers. On the physical closure one ascent suffices: the one-sided completion is nondegenerate up to and including the wall and the transported reciprocal divides totally there. Beyond the physical region the degeneration relocates to tame shadow walls, and the infinite wall sequence carries one rung of the tower per wall, displaced successively away from the physical region.

The clock never ticks, because the tower is Morita-stationary from its first step and the mod-8 structure classifies eight parallel towers rather than stages of one. For even transport charge the limit is the ground algebra tensored with the free fermionic field algebra, the modes being the transported null pairs. The depth of the hierarchy is thus one forced conformal ascent plus a fermionic ladder of capacity, one qubit per rung.

## lay
The question was how many times the series' completion step has to be repeated. Under the tameness premise, and for a compact wall with a trivial radical line, on the physical side of a degeneration the answer is once; further steps are demanded only beyond it, one for each successive hidden wall. Repeating the step never changes the algebra's essential type, and in the infinite limit, for even charge, it simply adds the modes of a free fermion field, one qubit per step.

## one-liner
Under tameness, with a compact wall and trivial radical line bundle, one conformal ascent completes the physical region, further rungs arise one per shadow wall beyond it, the mod-8 clock is frozen, and for even charge the limit is the ground algebra tensored with a free fermionic field algebra.
