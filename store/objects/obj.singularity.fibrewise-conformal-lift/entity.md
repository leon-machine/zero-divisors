---
id: obj.singularity.fibrewise-conformal-lift
kind: object
version: 2
title: The fibrewise conformal lift
status: defined
region: singularity
subject: completion
tags: [conformal-model, hyperbolic-plane]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
review: typed
about:
- obj.transport.null-lift-completion
locators:
  paper: T05
  number: Def 5.1
  label: def:lift
  line: 1526
extraction:
  env: definition
  context_refs:
  - singularity.transport-schwarzschild-fibre
  - transport.descent-read-out-map
  - transport.swap-rescale-normal-form
  - transport.totality
  typing:
    by: ai-typing-pass
    note: "Definition; levels follow the formal text, with the coordinate formulas imported from the root paper stated as part of the definition."
  connect_pass:
    by: ai-connect-pass
    date: 2026-10-21
    added_premises: []
    added_dependants: []
    added_about: [obj.transport.null-lift-completion]
    verdict: connected
    note: 'Its one user, the Schwarzschild fibre proposition, already had the about link; the lift is the root paper null-lift construction on each tangent space, so about was added to that definition.'
---

## formal
Let $p$ lie in the invertible region, so that the tangent space $(T_pM, g_p)$ is nondegenerate of signature $(1,3)$, and write $Q_p(x) := g_p(x,x)$.
Adjoin to $T_pM$ the hyperbolic plane $H = \operatorname{span}(\nO, \nInf)$ of Rule 1, with $\nO^2 = \nInf^2 = 0$ and $\nO \cdot \nInf = -1$ (the normalisation of T1 \cite{ButlerT1}, under which the lift below is null: $X_p(x)^{2} = Q_p(x)\,(1 + \nO\cdot\nInf) = 0$), giving the completion $\Cl(2,4)$ of Section \ref{sec:ascent}. The \emph{lift} of $x \in T_pM$ is the null ray
\begin{equation}
X_p(x) \;:=\; \bigl[\, \nO + x + \tfrac12 Q_p(x)\, \nInf \,\bigr] \;\in\; \mathcal{Q}_p ,
\end{equation}
and in the coordinates $N = s\,\nO + x + t\,\nInf$, written $(s,x,t)$, the quadric is cut out by the incidence condition $Q_p(x) = 2st$, the transported reciprocal is the linear involution $\iota(s,x,t) = (2t,\, x,\, \tfrac12 s)$, and the read-out is $\dsc(s,x,t) = x/s$, undefined where $s$ vanishes \cite[Thm.~4.10, Prop.~4.21, Lem.~4.23]{ButlerT1}. For a covector $\xi$ at an invertible point, the lift is that of its metric dual, $X_p(\xi) := X_p(\xi^{\sharp})$, computed directly from the dual norm since $Q_p(\xi^{\sharp}) = Q^{*}_p(\xi)$; clause (4) of Proposition \claimref{singularity.transport-schwarzschild-fibre} applies it in this form.

## technical
At a point $p$ of the invertible region the tangent space $(T_pM, g_p)$ is nondegenerate of signature $(1,3)$; write $Q_p(x) = g_p(x,x)$. Adjoin the hyperbolic plane spanned by null vectors $\nO, \nInf$ with $\nO\cdot\nInf = -1$, giving the completion $\Cl(2,4)$. The lift of $x \in T_pM$ is the null ray $X_p(x) = [\nO + x + \tfrac12 Q_p(x)\,\nInf]$ on the fibre quadric $\mathcal{Q}_p$.

In coordinates $N = s\,\nO + x + t\,\nInf$ the quadric is $Q_p(x) = 2st$, the transported reciprocal is the linear involution $\iota(s,x,t) = (2t, x, \tfrac12 s)$, and the read-out is $\dsc(s,x,t) = x/s$, undefined where $s = 0$. A covector $\xi$ is lifted through its metric dual, $X_p(\xi) = X_p(\xi^\sharp)$, computed from $Q_p(\xi^\sharp) = Q^*_p(\xi)$.

## lay
At each ordinary point of spacetime the directions at that point are given two extra dimensions, so that every direction becomes a light-like ray in a six-dimensional space. On these rays the reciprocal becomes a simple linear swap of two coordinates. Reading a direction back off its ray means dividing by one coordinate, which fails exactly where that coordinate is zero.

## one-liner
At an invertible point $p$ the fibrewise conformal lift sends a tangent vector $x$ to the null ray $[\nO + x + \tfrac12 Q_p(x)\,\nInf]$ in the $\Cl(2,4)$ completion of $T_pM$, where the reciprocal is the linear involution $(s,x,t) \mapsto (2t,x,\tfrac12 s)$ and the read-out is $x/s$.
