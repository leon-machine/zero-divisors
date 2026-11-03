---
id: sheaf.tameness
kind: claim
version: 1
title: Tameness
status: postulate
region: sheaf
subject: walls
tags: [degenerate-algebras, tameness]
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
locators:
  paper: T04
  number: Hyp 2.1
  label: hyp:tame
  line: 372
extraction:
  env: hypothesis
  context_refs:
  - sheaf.invariant-form-t3
  typing:
    by: ai-typing-pass
    note: "postulate with no derivation, so the context reference to the invariant-form lemma defining delta cannot be recorded as an edge; (T3) does depend on that lemma's definition"
---

## formal
The pair $(M, G)$ is a \emph{tame corank-one degeneration} if:
\begin{enumerate}
\item[(T1)] $\Sig$ is a smooth closed hypersurface of $M$;
\item[(T2)] $G$ has corank exactly one at every point of $\Sig$, and the radical lines assemble into a smooth line subbundle $\shL \subset T^*M|_\Sig$, locally spanned by a covector field $k$;
\item[(T3)] (transversality) the degeneration is first-order: the canonical section $\delta$ of Lemma \claimref{sheaf.invariant-form-t3} below is nowhere vanishing on $\Sig$.
\end{enumerate}

## technical
A pair $(M, G)$ is a tame corank-one degeneration if: (T1) the wall $\Sig$ is a smooth closed hypersurface of $M$; (T2) $G$ has corank exactly one at every point of $\Sig$, and the radical lines form a smooth line subbundle $\shL \subset T^*M|_\Sig$, locally spanned by a covector field $k$; and (T3) the degeneration is first order, meaning that the canonical transversality section $\delta$ is nowhere vanishing on $\Sig$.

## lay
This is the standing assumption on how a geometry is allowed to degenerate. The places where it degenerates must form a smooth closed wall, exactly one direction must lose its length at each point of the wall, and these directions must vary smoothly along it. In addition, the length must vanish at a linear rate as the wall is reached, not to higher order.

## one-liner
A tame corank-one degeneration is one whose degeneracy locus is a smooth closed hypersurface carrying a smooth radical line bundle of corank exactly one, with first-order (transversal) degeneration.
