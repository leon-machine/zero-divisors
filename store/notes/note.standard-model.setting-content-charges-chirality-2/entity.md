---
id: note.standard-model.setting-content-charges-chirality-2
kind: note
version: 3
title: Content, charges, chirality
status: setting
subject: standard-model
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T12, deposited version
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 2
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: 'maintainer pass on Leon''s decisions, a dated bracket: Hypothesis (S) is now derived from the slot-module premise, and the thirteenth generator against the twisted action'
  version: 3
  source: maintainer pass 2026-11-07 (decisions)
comments_on:
- standard-model.hyp-s-slot-statistics
- standard-model.global-form-quotient-determined
- standard-model.quarks-leptons-two-level-fermion-content
- standard-model.hypercharge-global-form-pair-counting-consistency
locators:
  paper: T12
  number: Setting
  section: Content, charges, chirality
  line: 1081
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Dated bracket added to the paper text, which is kept (DECISIONS G3, R04 items 1 and 8): Hypothesis (S) is now a proved claim (standard-model.hyp-s-slot-statistics@9) derived from the postulate standard-model.slot-module-hypothesis. The thirteenth-generator sentence gets a bracket citing standard-model.under-s-composites-state-space-spinor@6 (3)(b): in the twisted action every abelian generator in the span is anomaly-free.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'By Leon''s ruling R3: the hypercharge generator is (3 I_4 1_2, -2 I_4 1_3), its phase lambda = e^{I_4 theta}, its action I_4 q; the slot and pair spaces C^2, W are read over span{1, I_4} on the tower''s floors (stated once; notational, nothing about Hypothesis (S) follows); no bare i remains, so the earlier declaration is removed.'
---

## formal
The comparison of Remark \claimref{note.standard-model.eighth-refutation-split-conclusion-decisive-test} set the Standard Model's elementary fermions against the state space's entire Fock space. The corrected comparison needs one definition and one declared hypothesis, stated here so that the propositions below are about defined objects and so that the reader can see exactly which results rest on which.

\emph{The hypercharge generator.} The Lie algebra of Theorem \claimref{standard-model.global-form-quotient-determined}'s group is $\mathfrak{s}(\uu(2) \oplus \uu(3)) = \{(X, X') : \tr X + \tr X' = 0\}$, and its centre is one-dimensional, spanned by
\[
\mathsf{y} := (3I_{4}\,\mathbf{1}_{2},\; -2I_{4}\,\mathbf{1}_{3}),
\]
the unique trace-free combination of the two scalar generators up to scale (numbers and the module's complex structure are read in $\mathrm{span}\{1, I_{4}\}$, the module read on the tower's floors, where $I_{4}$ commutes with the tower vectors; $\mathbf{1}_{n}$ is the identity). The one-parameter subgroup $\exp(\theta\mathsf{y}) = (\lambda^{3}\mathbf{1}_{2}, \lambda^{-2}\mathbf{1}_{3})$, $\lambda = e^{I_{4}\theta}$, is the image of the $U(1)$ factor of Theorem \claimref{standard-model.global-form-quotient-determined}'s second isomorphism, so $\mathsf{y}$ acts on an irreducible constituent by $I_{4}q$ where $q$ is the abelian weight of Theorem \claimref{standard-model.global-form-quotient-determined}(ii). \emph{Hypercharge} is $Y := q/6$: the normalisation in which the lattice condition reads $t/3 + \delta/2 + Y \in \mathbb{Z}$, and in which, as computed below, a single pair has weight one unit. The sign of $\mathsf{y}$ is not fixed by the algebra: $(a, b, \lambda) \mapsto (\lambda^{-3}a, \lambda^{2}b)$ is an equally good second isomorphism with the same $\mathbb{Z}_{6}$ kernel, and it reverses every weight. The sign chosen here is the one in which the pair-level generators of Proposition \claimref{standard-model.quarks-leptons-two-level-fermion-content}(1) have weight $+1$; the opposite sign gives the conjugate listing throughout, and the choice is part of the particle-antiparticle orientation of Theorem \claimref{standard-model.hypercharge-global-form-pair-counting-consistency}(1). This is a definition of the symbol $Y$; that the symbol so defined is the hypercharge of the Standard Model is the observation-level identification of Theorem \claimref{standard-model.gauge-algebra-minimal-massive-composite}'s reading, and is not claimed by the definition.

\emph{The tensor state space, and what it does not contain.} The state space of the minimal massive hierarchy is $\Lambda^{\bullet}(\C^{2} \otimes \C^{3})$, generated from its vacuum by the six creation operators of the cells of Figure \ref{fig:hierarchy}; a cell is one pair of one twistor, and an automorphism acts on the cells as $A \otimes B$. On this state space the $U(1)$ factor $(\lambda^{3}, \lambda^{-2})$ acts on a cell by $\lambda^{3}\lambda^{-2} = \lambda$, so a state with $k$ cells occupied has weight $k$, and Proposition \claimref{standard-model.raw-representation-content-state-space} lists every representation that occurs: $(2,3)$ at one cell, and in every degree only the representations of \eqref{eq:fock}. In particular no $(2,1)$ occurs anywhere in the tensor state space, and the states that fill a whole row of the figure, $(v \otimes f_{1}) \wedge (v \otimes f_{2}) \wedge (v \otimes f_{3})$ for $v \in \C^{2}$, are cubic in $v$ and span $S^{3}\C^{2} \otimes \Lambda^{3}\C^{3} = (4, 1)$, the quadruplet of Proposition \claimref{standard-model.raw-representation-content-state-space}'s degree three, of weight $+3$. A lepton doublet, $(2,1)$ of weight $-3$, is therefore not an object of the tensor state space, and no reading of its generators produces one. The same computation shows more: every cell has weight $+1$, so the state space contains no state of negative weight at all, and \eqref{eq:fock} contains no $(1, \bar{3})$ in any degree; so the single-twistor sector of Proposition \claimref{standard-model.quarks-leptons-two-level-fermion-content}(3), with its negative weights $-2k$ and its $\bar{3}$ at grade two, is not a subspace of the tensor state space either. What is unconditional is the state space's own content, the quark doublet as its cells and the negative theorem; the single-twistor sector is a computation on the Fock space $\Lambda^{\bullet}W$ of one twistor's pairs, which under the hypothesis below is the slot-free row of one object holding both. The lepton needs a hypothesis, stated here.

\begin{quote}
\emph{Hypothesis (S), slot statistics.} The twistor slots of the composite are fermionic modes on the same footing as its pairs: the composite's state space is the Fock space $\Lambda^{\bullet}(\C^{2} \oplus W)$ of five modes, two slot modes and three pair modes, a state being a set of occupied slots and occupied pairs, on which $(A, B) \in U(2) \times U(3)$ acts as $\Lambda^{\bullet}(A \oplus B)$; and, as in Fact \claimref{standard-model.imported-pair-systems-two-chirality-halves} for the three-mode Fock space $\Lambda^{\bullet}W$, the chirality of a state is the parity of its total mode number (Fact \claimref{standard-model.imported-fock-representation-clifford-algebra-bogoliubov} supplies the structure: $\Lambda^{\bullet}\C^{5}$ is the spinor module of $\Cl(10)$ and its parity grading is that module's chirality).
\end{quote}

Hypothesis (S) is a structural premise, not a theorem of the series, and the paper carries it as one: every result below that needs it says so, and successor problem (6) records what deciding it would settle and what it would cost. (Status now, 7 November 2026: the store derives (S) from a weaker postulate, Premise \claimref{standard-model.slot-module-hypothesis}, in Proposition \claimref{standard-model.hyp-s-slot-statistics}; the results that need (S) rest on that premise.) Two remarks on its content. Under (S) a cell of the tensor state space, one slot with one pair, is the state with one slot mode and one pair mode occupied, of weight $3 - 2 = 1$, so the pair-level content of the tensor state space is recovered; but (S) does not record which pairs belong to which slot, so it is not a refinement of the two-level hierarchy but a different state space with the same one-cell sector. And under (S) the automorphisms preserving the slot-pair split act faithfully: the kernel $K$ of Theorem \claimref{standard-model.global-form-quotient-determined} acts on the $(j, k)$ component by $\lambda^{j - k}$, so the automorphism group of the five-mode state space that preserves the slot-pair split and the mode number is $U(2) \times U(3)$ itself, thirteen-dimensional, and the framework's rule that the gauge group is the automorphism group then yields one abelian generator more than Theorem \claimref{standard-model.gauge-algebra-minimal-massive-composite}'s twelve. The extra generator, the total mode number $j + k$ (or equivalently $j - k$), cannot be gauged: Proposition \claimref{standard-model.under-s-composites-state-space-spinor}(3) proves that over the derived generation every abelian generator in the span of the two mode numbers except hypercharge fails three of the four anomaly conditions, so the automorphism rule read with anomaly cancellation returns the twelve. (Status now, 7 November 2026: that holds for the action $\Lambda^{\bullet}(A \oplus B)$; in the action the state space carries, through $\Lambda^{\bullet} \otimes \det^{-1/2}$, every abelian generator in that span is anomaly-free, Proposition \claimref{standard-model.under-s-composites-state-space-spinor}(3)(b), and the rule read with anomaly cancellation returns thirteen.) What (S) still costs is the second item: a state space that is not a refinement of the two-level hierarchy.

## technical
pending

## lay
pending

## one-liner
pending
