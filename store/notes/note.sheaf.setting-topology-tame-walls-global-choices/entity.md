---
id: note.sheaf.setting-topology-tame-walls-global-choices
kind: note
version: 1
title: Topology of tame walls, and the global choices
status: setting
subject: walls
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T04, deposited version
comments_on:
- sheaf.tame-walls-are-two-sided
- sheaf.imported-real-line-bundles
- sheaf.one-sided-completion
- obj.sheaf.collar-data-coupling
locators:
  paper: T04
  number: Setting
  section: Dictionary, choices, and scope
  line: 818
  subsection: Topology of tame walls, and the global choices
---

## formal
The construction's global inputs, and what obstructs them, are then exactly these:

\begin{enumerate}
\item \textbf{The side.} Always available, by Corollary \claimref{sheaf.tame-walls-are-two-sided}; the residual choice is a global sign, a torsor over $H^0(\Sig; \mathbb{Z}_2)$, fixed in the gravitational application by physics (the Lorentzian side).
\item \textbf{Orientation of the radical line.} The spanning section $k$ exists globally iff $\shL$ is trivial, iff $w_1(\shL) = 0 \in H^1(\Sig; \mathbb{Z}_2)$ (Fact \claimref{sheaf.imported-real-line-bundles}). The constructions divide over this class. The ideal sheaf and the residue are quadratic or scale-covariant in $k$, so they descend to the line bundle and need nothing. The \emph{coupling} does not descend: it is of weight $-1$ in $k$ (the transversal $u$ with $k(u) = 1$ is itself a trivialisation of $\shL^*$), so collar data, and with them the completion of Theorem \claimref{sheaf.one-sided-completion} in the untwisted plane $\underline{\R}^2$, exist exactly when $w_1(\shL) = 0$, which is why Definition \claimref{obj.sheaf.collar-data-coupling} carries that standing hypothesis. For $w_1(\shL) \neq 0$, which is possible and marks walls whose dying direction is globally non-orientable, the residue theorem's conclusion that the partner line is canonically $\shL^*$ dictates the repair: the adjoined plane must be the $\shL$-twisted plane $\shL \oplus \shL^*$ rather than $\underline{\R}^2$. That twisted variant is not developed here and is recorded among the successor problems. The class $w_1(\shL)$ is a genuine invariant of the degeneration, constrained by the residue theorem to satisfy $2 w_1(\shL) = w_1(N^*\Sig) = 0$, which is no constraint mod 2.
\item \textbf{The transversal field and the collar.} Given the global $k$ of item 2, the space of pairs $(u, \beta)$ with $k(u) = 1$ is convex, hence contractible: no further obstruction, and any two choices are homotopic through admissible choices.
\item \textbf{The coupling constants.} Only the product $\mu\nu$ enters (Remark \claimref{note.sheaf.only-product-coupling-constants-matters}); the good-coupling condition of Lemma \claimref{sheaf.tame-wall-induction} is an open condition $0 < |\mu\nu| < 1/(2S)$, contractible at each fixed sign of $\mu\nu$ (as a condition on the product; the set of pairs $(\mu,\nu)$ has one contractible component per sign choice of each factor). The discrete datum is the sign of $\mu\nu$, i.e.\ which side's ascent is performed: combined with item 1 this is the only genuinely binary global choice, and the two options are exchanged by relabelling the sides.
\end{enumerate}

## technical
pending

## lay
pending

## one-liner
pending
