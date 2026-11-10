---
id: dark-matter.superselected-hence-dark-exactly-stable
kind: claim
version: 5
title: Superselected, hence dark and exactly stable
status: proved
region: dark-matter
subject: dark-matter
tags: [superselection]
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
about:
- obj.dark-matter.frozen-phase-operators
derivations:
- name: main
  uses:
  - dark-matter.imported-eight-towers-mod-8-clock@4
  - dark-matter.imported-gravity-only-coupling@4
  - dark-matter.residue-soldered-invariant-not-algebraic-one@5
  - sheaf.infinite-wall-sequence@4
  assumes:
  - dark-matter.p1-single-frozen-point@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_ascent_preserves_residue
- kind: check
  ref: check.py::check_completion_is_matrix_amplification
- kind: check
  ref: check.py::check_no_soldered_map_between_residues
locators:
  paper: T14
  number: Prop 4.1
  label: prop:stable
  line: 306
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: residue invariance of the (1,1) ascent and Cl(p+1,q+1) = Mat_2(Cl(p,q)), and the soldering obstruction between the six populated residues. Version 4 -> 5.'
  small_findings_pass:
    by: ai-small-findings-pass
    date: 2026-10-22
    finding: VALUES M6
    open_problem: op.small-findings
    note: 'VALUES M6: the darkness clause rests on the imported acoustic no-go (dark-matter.imported-gravity-only-coupling), which holds within the s-wave current algebra, at its mixed level, with the sphere step conditional on the Indifference premise and the thermal state on premise (Q). The levels name those conditions and the first-order qualifier for readability; once the gravity-only Fact is stored as a restatement of the series'' acoustic no-go (its correction filed alongside), they also reach holds_given through the graph. Exact stability (steps 1-3) does not use the import and is unchanged.'
  typing:
    by: ai-typing-pass
    added:
    - dark-matter.imported-gravity-only-coupling
    - sheaf.infinite-wall-sequence
    note: 'Added the gravity-only coupling Fact (the darkness clause is stated as following from it with
      P1) and the sheaf paper''s wall-sequence corollary, which step (2) uses under the same hypotheses
      (compact base, good couplings); the infall proposition is cited only for the black-hole remark and
      already uses this claim, so it was not added. Levels pass: the lay level now states P1, the sector
      decomposition and the wall-sequence hypotheses, which it had dropped, and the one-liner adds the
      wall-sequence hypotheses.'
  env: proposition
  context_refs:
  - dark-matter.imported-gravity-only-coupling
  - dark-matter.parallel-boundary-mode-spaces-one-wall
  outside_pilot_cites:
  - ButlerT4
  - ButlerT5
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-matter.imported-gravity-only-coupling
    - sheaf.infinite-wall-sequence
---

## formal
By Premise \claimref{dark-matter.p1-single-frozen-point} and the acoustic programme (Fact \claimref{dark-matter.imported-gravity-only-coupling}, the series' acoustic no-go, at its mixed level: within the s-wave current algebra, with the sphere step conditional on the Indifference premise and the thermal state on premise (Q)), matter in a neighbouring tower gravitates on this metric and does nothing else observable at first order: dark by structural necessity, at that level. Stability is then not suppressed but exact, in three steps, the first of which is proved given the sector decomposition of Definition \claimref{obj.dark-matter.frozen-phase-operators}.
\begin{enumerate}
\item The tower charge $r$ is superselected in the frozen phase: frozen-phase operators are built from the one soldering and preserve its signature (Theorem \claimref{dark-matter.residue-soldered-invariant-not-algebraic-one}), so portal matrix elements between residues vanish identically away from walls.
\item The walls are unreachable: singular loci ascend within-tower, since the completion adjoins exactly $(1,1)$ and preserves the residue (Fact \claimref{dark-matter.imported-eight-towers-mod-8-clock}), while the mod-8 shadow walls that separate residues are displaced successively away from the physical region, by the wall-sequence theorem of the sheaf paper \cite[\S5]{ButlerT4}, under that theorem's hypotheses (a compact base and good couplings at every stage), carried here.
\item Therefore the only inter-tower event in the universe's history is the descent itself: the towers communicated once, at the origin, and have been in absolute mutual darkness but for weight ever since. The singular locus of a black hole is an inter-tower event for energy, as it already was for weight, and never for the residue of any quantum: energy crosses at the wall, the residue does not (Proposition \claimref{dark-matter.parallel-boundary-mode-spaces-one-wall}).
\end{enumerate}
One residue is flagged at observation level: dark-tower matter crossing this tower's horizons carries superselected charge the four-dimensional boundary mode space cannot hold, which routes it into the tower-wise run of the singularity paper's ascend-then-descend structure \cite{ButlerT5}; the computation of that routing, with the mass range of its Gauss-law clause, is Proposition \claimref{dark-matter.parallel-boundary-mode-spaces-one-wall}.

## technical
By P1 and the gravity-only coupling (the series' acoustic no-go, at its mixed level), which holds within the s-wave current algebra and is conditional on the Indifference premise and premise (Q), matter in a neighbouring tower gravitates on this metric and does nothing else observable at first order, at that level. Stability is then exact, in three steps: (1) given the sector decomposition, frozen-phase operators are built from one soldering and preserve its signature, so portal matrix elements between residues vanish away from walls and the tower charge $r$ is superselected; (2) the walls are unreachable, since singular loci ascend within a tower preserving the residue and the mod-$8$ shadow walls are displaced successively away from the physical region, under the wall-sequence theorem's hypotheses of a compact base and good couplings; (3) hence the only inter-tower event is the descent itself.

A black hole's singular locus is inter-tower for energy, as it already was for weight, but never for the residue of any quantum. Dark-tower matter crossing our horizons carries superselected charge that the four-dimensional boundary mode space cannot hold, a residue flagged at observation level.

## lay
Assuming all the sectors share one spacetime metric set by a single frozen point (Premise P1), matter in the hidden sectors can affect us only through its weight, which is why it is dark; this part is carried over from earlier work, holds in the framework's spherically averaged description of the modes near horizons, and inherits two of that work's assumptions (the Indifference premise and premise (Q)). Given how the sectors are split, and provided the sheaf paper's conditions for its walls hold (a compact base and well-behaved couplings), this result argues that no process can change a particle's tower, so dark matter of this kind never decays; energy can still pass between the towers through gravity. The sectors met only once, at the universe's birth; a black hole can pass energy between them, but never a particle's sector label.

## one-liner
Under P1, the sector decomposition and the wall-sequence theorem's hypotheses (compact base, good couplings), the tower charge is exactly superselected, so dark-tower matter is exactly stable; that it only gravitates, at first order, is the series' acoustic no-go's, within the s-wave current algebra and conditional on the Indifference premise and premise (Q).
