---
id: note.transport.setting-completion-conformal-model
kind: note
version: 1
title: 'The completion: the conformal model'
status: setting
subject: completion
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T01, deposited version
comments_on:
- transport.density
locators:
  paper: T01
  number: Setting
  section: 'Type N: the isotropic obstruction, and Rule 1'
  line: 833
  subsection: 'The completion: the conformal model'
---

## formal
This section is standard \cite{Hestenes2001, HLR2001, DFM2007, DoranLasenby2003}; we fix conventions and, for later use, the topology. Adjoin to $\mathbb{V}$ two orthogonal directions $e_+, e_-$ with $e_+^2 = 1$, $e_-^2 = -1$, both orthogonal to $\mathbb{V}$, giving $\Cl(p{+}1, q{+}1)$. Define the null pair
\[
\nO = \tfrac12(e_- - e_+), \qquad \nInf = e_- + e_+,
\]
so that $\nO^2 = \nInf^2 = 0$ and $\nO \cdot \nInf = -1$; the plane $H = \mathrm{span}\{\nO, \nInf\}$ they span is hyperbolic (Section \ref{subsec:null}). Represent each point $x \in \mathbb{V}$ by
\begin{equation}
X(x) \;=\; \nO + x + \tfrac12 Q(x)\, \nInf .
\end{equation}
Direct computation gives the two standard identities
\begin{equation}
X(x)^2 = 0, \qquad X(x)\cdot X(y) = -\tfrac12\, Q(x-y),
\end{equation}
so every point is represented by a null vector, and the representation is metrically faithful. Representatives are regarded projectively: a \emph{point} of the model is a null ray $[\,X\,] = \{\lambda X : \lambda \in \R^\times\}$ on the quadric
\[
\mathcal{Q} \;=\; \{[N] : N \in \mathbb{V} \oplus H,\ N \neq 0,\ N^2 = 0\}
\]
of the ambient space. Writing a general vector as $N = s\,\nO + x + t\,\nInf$ ($s, t \in \R$, $x \in \mathbb{V}$), one has $N \cdot \nInf = -s$; the rays with $s = 0$, an invariant condition since it reads $N \cdot \nInf = 0$, are not of the form $[X(x)]$ for any $x$, and we call them \emph{ideal points}. As is well known, the versor group of $\Cl(p{+}1,q{+}1)$ acting by \eqref{eq:tau} realises on $\mathcal{Q}$ the full conformal group of $(\mathbb{V}, Q)$, the group of its angle-preserving transformations, with inversions realised by reflections \cite{HLR2001, Angles2008}.

## technical
pending

## lay
pending

## one-liner
pending
