---
id: one-relation.overlap-table-sorted
kind: claim
version: 5
title: The overlap table, sorted
status: proved
region: one-relation
subject: one-relation
tags: [two-readings, ledger-audit]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T16, deposited version
review: typed
derivations:
- name: main
  uses:
  - one-relation.third-constant-conversion-constant-between-charts@6
  - one-relation.two-presentations@5
  - one-relation.two-capacities-three-consequences@6
  - one-relation.imported-completion-ladder@6
  - standard-model.pair-count-dimension@4
  - one-relation.imported-single-mode-thermality-modular-period@6
  - correspondence.clifford-side-ordering-shift@3
  - dark-energy.acoustic-no-go-one-way-grip@5
  - dark-energy.lift-inherits-no-go-steps-itemised@2
  - std-algebra.periodicity@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T16.py
  tags:
  - label:prop:overlap
- kind: check
  ref: check.py::check_ladder_pair_doubles_the_algebra
- kind: check
  ref: check.py::check_pair_count_is_the_complex_capacity
locators:
  paper: T16
  number: Prop 4.2
  label: prop:overlap
  line: 697
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.periodicity where the proof uses them. Version 4 -> 5.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the ladder pair of Cl(p+1,q+1) gives matrix units with E11 commuting with the base, injective corner of dimension 2^n and blocks spanning 4 * 2^n, for all ten bases with n <= 3; three orthogonal null vectors of C^(2,4) span a self-perpendicular isotropic U of dimension 3. Version 3 -> 4.'
  env: proposition
  context_refs:
  - correspondence.clifford-side-ordering-shift
  - dark-energy.acoustic-no-go-one-way-grip
  - dark-energy.lift-inherits-no-go-steps-itemised
  - one-relation.imported-completion-ladder
  - one-relation.imported-single-mode-thermality-modular-period
  - one-relation.two-capacities-three-consequences
  - sheaf.one-sided-completion-singularity
  - standard-model.pair-count-dimension
  typing:
    by: ai-typing-pass
    added:
    - one-relation.two-capacities-three-consequences
    - one-relation.imported-completion-ladder
    - standard-model.pair-count-dimension
    - one-relation.imported-single-mode-thermality-modular-period
    - correspondence.clifford-side-ordering-shift
    - dark-energy.acoustic-no-go-one-way-grip
    - dark-energy.lift-inherits-no-go-steps-itemised
    note: 'Added the results each clause sorts or rests on (capacities, ladder, pair count, thermality,
      and the hbar and G sources); left out the T04 completion theorem, cited only for the scope of the
      thermality reading; the hbar and G edges are the least certain since the clause is an identification.
      Levels pass: the lay and one-liner now say the placement of the constants is at observation level
      and that the placement of $G$ is conditional on its sources'' premises; the lay names premise (Q)
      and the indifference premise.'
  source_title: 'The overlap table, sorted'
  source_formal: |-
    Three numerical agreements in this series are read as consequences of the one relation having two charts. They are not of one kind, and the proposition sorts them; none is an agreement of independent computations. \emph{(i) One count in two vocabularies.} The tower's one-qubit-per-rung ladder is read off the periodicity isomorphism $\Cl(p+1,q+1) \cong \Mat(2, \Cl(p,q))$, one matrix doubling per rung; the capacity increment of Proposition \claimref{one-relation.two-capacities-three-consequences}(2) is index arithmetic. The isomorphism is the tower paper's structure theorem (Fact \claimref{one-relation.imported-completion-ladder}); its dimension shadow $2^{p+q+2} = 4 \cdot 2^{p+q}$ and the increment are identities that cannot fail, and the step that reads a matrix doubling as one mode is exactly the identification of Proposition \claimref{one-relation.two-presentations}; the content is that the metric reading's doubling and the Witt reading's mode are one count. \emph{(ii) An identification.} The pair count $(n+2)/2 = 3$ at spacetime dimension $n = 4$, under which the Standard-Model paper selects the strong force and four dimensions on its two declared conditionalities, is proved there to be the maximal isotropic dimension of the complexified ascended space, by the same argument this paper gives for the complex capacity \cite[Lem.~2.12]{ButlerT12}; its equality with $r_{\C}(2,4)$ of Proposition \claimref{one-relation.two-capacities-three-consequences}(3) is therefore an identification and not an agreement: the twistor's pairs are the fermionic modes of the complex reading, so the Standard-Model paper's count is a quantum capacity, and what is new here is only the extension to arbitrary signature with the attainment construction. \emph{(iii) A reading.} The thermality theorem (Fact \claimref{one-relation.imported-single-mode-thermality-modular-period}) is single-mode, its mode being the ladder pair of the ascent, a mode adjoined by the rung and not the boost pair of $(1,3)$; Proposition \claimref{one-relation.two-capacities-three-consequences}(2) says a rung adjoins exactly one mode in either count. That the theorem is single-mode \emph{because} one rung was ascended is the structural explanation this paper offers, and it is a reading of the two results together, not a computation; the theorem installs one mode per point of the singular boundary (Fact \claimref{one-relation.imported-single-mode-thermality-modular-period}, \cite[Thm.~8.12]{ButlerT4}), so the reading concerns each marginal and not a capacity ceiling. At observation level, each presentation also carries a constant, and the three constants are at three levels: $\hbar$ as the ordering shift of the Witt presentation, the half-per-mode shift proved in the twistor paper T9 \cite[Prop.~5.6]{ButlerT9}; $G$ as the compositeness scale of the metric presentation, the dimension-two irrelevance the dark-energy paper T10 reads at structural level from its acoustic no-go, the no-go itself conditional on the singularity paper's premise (Q), within an acoustic programme that paper closes at the mixed level of its inputs, the sphere step conditional on the indifference premise \cite[Prop.~5.2, Rem.~5.3, Assembly~5.5]{ButlerT10}; and $c$ as the datum of the transition between the two charts, invisible in the Witt chart, which contains rapidity and no other quantity, and fixed in the metric chart, which contains time and length separately (Lemma \claimref{one-relation.third-constant-conversion-constant-between-charts}, proved). The third is placed by a different mechanism from the first two, and it is a conformal invariant, surviving every conformal step the first two do not. This is an identification of \emph{where} the constants enter, not a derivation of their values, and it remains the synthesis's weakest point, flagged as such; what can be said in its favour is this: $c$ has no value to derive, its number being a unit convention, and in the Planck system all three are, so a placement can be nothing more than this.
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: 'Converted the twistor''s pairs to the pairs of a conformal spinor and the twistor paper to the correspondence paper. Kept the complexified ascended space and $r_{\C}$: the pair count is the maximal isotropic dimension of the complexified vector space, not an $I_6$-renaming.'
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    cited:
    - correspondence.clifford-side-ordering-shift
    - dark-energy.acoustic-no-go-one-way-grip
    - dark-energy.lift-inherits-no-go-steps-itemised
    - one-relation.imported-completion-ladder
    - one-relation.imported-single-mode-thermality-modular-period
    - one-relation.two-capacities-three-consequences
    - standard-model.pair-count-dimension
---

## formal
Three numerical agreements in this series are read as consequences of the one relation having two charts. They are not of one kind, and the proposition sorts them; none is an agreement of independent computations. \emph{(i) One count in two vocabularies.} The tower's one-qubit-per-rung ladder is read off the periodicity isomorphism $\Cl(p+1,q+1) \cong \Mat(2, \Cl(p,q))$, one matrix doubling per rung; the capacity increment of Proposition \claimref{one-relation.two-capacities-three-consequences}(2) is index arithmetic. The isomorphism is the tower paper's structure theorem (Fact \claimref{one-relation.imported-completion-ladder}); its dimension shadow $2^{p+q+2} = 4 \cdot 2^{p+q}$ and the increment are identities that cannot fail, and the step that reads a matrix doubling as one mode is exactly the identification of Proposition \claimref{one-relation.two-presentations}; the content is that the metric reading's doubling and the Witt reading's mode are one count. \emph{(ii) An identification.} The pair count $(n+2)/2 = 3$ at spacetime dimension $n = 4$, under which the Standard-Model paper selects the strong force and four dimensions on its two declared conditionalities, is proved there to be the maximal isotropic dimension of the complexified ascended space, by the same argument this paper gives for the complex capacity \cite[Lem.~2.12]{ButlerT12}; its equality with $r_{\C}(2,4)$ of Proposition \claimref{one-relation.two-capacities-three-consequences}(3) is therefore an identification and not an agreement: the pairs of a conformal spinor (the twistor's pairs) are the fermionic modes of the complex reading, so the Standard-Model paper's count is a quantum capacity, and what is new here is only the extension to arbitrary signature with the attainment construction. \emph{(iii) A reading.} The thermality theorem (Fact \claimref{one-relation.imported-single-mode-thermality-modular-period}) is single-mode, its mode being the ladder pair of the ascent, a mode adjoined by the rung and not the boost pair of $(1,3)$; Proposition \claimref{one-relation.two-capacities-three-consequences}(2) says a rung adjoins exactly one mode in either count. That the theorem is single-mode \emph{because} one rung was ascended is the structural explanation this paper offers, and it is a reading of the two results together, not a computation; the theorem installs one mode per point of the singular boundary (Fact \claimref{one-relation.imported-single-mode-thermality-modular-period}, \cite[Thm.~8.12]{ButlerT4}), so the reading concerns each marginal and not a capacity ceiling. At observation level, each presentation also carries a constant, and the three constants are at three levels: $\hbar$ as the ordering shift of the Witt presentation, the half-per-mode shift proved in the correspondence paper T9 \cite[Prop.~5.6]{ButlerT9}; $G$ as the compositeness scale of the metric presentation, the dimension-two irrelevance the dark-energy paper T10 reads at structural level from its acoustic no-go, the no-go itself conditional on the singularity paper's premise (Q), within an acoustic programme that paper closes at the mixed level of its inputs, the sphere step conditional on the indifference premise \cite[Prop.~5.2, Rem.~5.3, Assembly~5.5]{ButlerT10}; and $c$ as the datum of the transition between the two charts, invisible in the Witt chart, which contains rapidity and no other quantity, and fixed in the metric chart, which contains time and length separately (Lemma \claimref{one-relation.third-constant-conversion-constant-between-charts}, proved). The third is placed by a different mechanism from the first two, and it is a conformal invariant, surviving every conformal step the first two do not. This is an identification of \emph{where} the constants enter, not a derivation of their values, and it remains the synthesis's weakest point, flagged as such; what can be said in its favour is this: $c$ has no value to derive, its number being a unit convention, and in the Planck system all three are, so a placement can be nothing more than this.

## technical
Three numerical agreements in the series are sorted, and none is an agreement of independent computations. (i) One count in two vocabularies: the tower's one qubit per rung, read from $\Cl(p+1,q+1) \cong \Mat(2, \Cl(p,q))$, and the capacity increment per rung are one count, via the identification of the metric and Witt presentations. (ii) An identification: the Standard-Model pair count $(n+2)/2 = 3$ at $n = 4$ is the complex capacity $r_{\C}(2,4)$, so that count is a quantum capacity. (iii) A reading, not a computation: the thermality theorem is single-mode because one rung adjoins exactly one mode.

The three constants are placed at three levels: $\hbar$ as the ordering shift of the Witt presentation, $G$ as the compositeness scale of the metric presentation (at the conditional level of its sources), and $c$ as the datum of the transition between the two charts, which is proved. This locates where the constants enter and derives no values; it is flagged as the synthesis's weakest point.

## lay
Several numbers in this series of papers match up, and it would be tempting to count each match as independent confirmation. This result sorts them: one is the same count written two ways, one is a direct identification, and one is an interpretation. It also says, at observation level, where Planck's constant, Newton's constant and the speed of light enter the picture, without claiming to compute their values; the placement of Newton's constant rests on earlier premises (the singularity paper's premise (Q) and the indifference premise), and the paper flags this placement as the synthesis's weakest point.

## one-liner
The series' three numerical agreements are one count in two vocabularies, an identification and a reading, and, at observation level, $\hbar$, $G$ (conditionally on its sources' premises) and $c$ enter at the Witt, metric and chart-transition levels.
