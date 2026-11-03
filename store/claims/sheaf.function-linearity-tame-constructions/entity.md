---
id: sheaf.function-linearity-tame-constructions
kind: claim
version: 2
title: Function-linearity of the tame constructions
status: proved
region: sheaf
subject: walls
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T04, deposited version
review: typed
about:
- obj.sheaf.collar-data-coupling
- obj.sheaf.weighted-coframe-module
derivations:
- name: main
  uses:
  - sheaf.blade-basis-degenerate-forms-included@4
  - std-algebra.functoriality@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
locators:
  paper: T04
  number: Prop 9.17
  label: prop:functionlinear
  line: 1327
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.functoriality where the proof uses them. Version 1 -> 2.'
  env: proposition
  context_refs:
  - sheaf.degeneration-sheaf
  - sheaf.exceptional-algebra-deformation-normal-cone
  - sheaf.localised-transport
  - sheaf.one-sided-completion
  typing:
    by: ai-typing-pass
    note: 'Kept the blade-basis edge; the four context references name the constructions that are inspected
      rather than results the proof relies on, so they were not added. Levels pass: the lay said ''in
      this framework'', wider than the paper''s own constructions the formal quantifies over; it now says
      ''in this paper''.'
---

## formal
\leavevmode
\begin{enumerate}
\item Every construction of this paper, the degeneration sheaf and its ideal (Theorem \claimref{sheaf.degeneration-sheaf}), the coupling and the ambient form (Definition \claimref{obj.sheaf.collar-data-coupling}), the one-sided completion (Theorem \claimref{sheaf.one-sided-completion}), the ladder pair (Corollary \claimref{sheaf.localised-transport}), the exceptional rescaling (Proposition \claimref{sheaf.exceptional-algebra-deformation-normal-cone}) and the weighted module (Definition \claimref{obj.sheaf.weighted-coframe-module}), is $C^\infty$-linear over the base: it is obtained from the input data by operations that are linear over the function algebra, and it never differentiates a coefficient function.
\item The class of $C^\infty$-linear operations is closed under composition, under sums and multiplication by functions, under the tensor operations and Clifford multiplication, and under passage to the $C^\infty$-submodules and quotients the constructions form (the ideal, the quotient algebra, the even part, the weighted module). Every composite of the constructions therefore remains in the class; the class-membership of an assembled object never has to be re-argued.
\item Consequently every endomorphism \emph{supplied by} the constructions, of any bundle they build, is $C^\infty$-linear, hence tensorial: a bundle map, and on a line bundle multiplication by a function. The quantifier is over the supplied endomorphisms, not over all endomorphisms of the supplied bundles: an arbitrary endomorphism of a bundle the constructions build, a differential operator on its sections, say, need not be $C^\infty$-linear, and none such is supplied.
\end{enumerate}

## technical
Every construction of the sheaf framework (the degeneration sheaf and its ideal, the coupling and ambient form, the one-sided completion, the ladder pair, the exceptional rescaling and the weighted module) is obtained from the input data by operations that are linear over $C^\infty$ of the base, and none differentiates a coefficient function. This class of operations is closed under composition, sums and multiplication by functions, tensor operations and Clifford multiplication, and passage to the submodules and quotients the constructions form, so every composite of the constructions stays in the class.

Consequently every endomorphism supplied by the constructions is $C^\infty$-linear and hence tensorial: a bundle map, and on a line bundle multiplication by a function. The statement concerns only the endomorphisms the constructions supply; an arbitrary endomorphism of a bundle they build, such as a differential operator on its sections, need not be $C^\infty$-linear.

## lay
All the objects built in this paper are assembled point by point, without differentiating the input functions. This property survives every way the pieces are combined. As a result, any map these constructions produce acts point by point, which is what lets them be carried over unchanged to data that vary from place to place.

## one-liner
All the tame constructions are linear over smooth functions and stay so under composition and the standard operations, so every endomorphism they supply is tensorial.
