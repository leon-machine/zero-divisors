---
id: note.primer.setting-rotors-how-algebra-moves-things
kind: note
version: 1
title: 'Rotors: how the algebra moves things'
status: setting
subject: clifford-structure
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T00, deposited version
comments_on:
- primer.twisted-adjoint-action
locators:
  paper: T00
  number: Setting
  section: 'Rotors: how the algebra moves things'
  line: 368
---

## formal
Geometric algebra does not act on vectors through matrices; it acts through its own elements, by a sandwich product. The basic case is the reflection. For an invertible vector $u$, the map
\[
x \;\longmapsto\; -\,u\,x\,u^{-1}
\]
is the reflection of the vector $x$ in the hyperplane orthogonal to $u$: it fixes everything orthogonal to $u$ (which anticommutes past $u$, absorbing the minus sign) and negates $u$ itself. Every isometry of a nondegenerate quadratic space is a product of reflections (the Cartan--Dieudonn\'e theorem \cite{Lam2005}), so products of invertible vectors, called \emph{versors}, reach every element of the orthogonal group $O(p,q)$.

The group formed by versors whose factors are normalised to $Q(u) = \pm 1$ is called $\Pin(p,q)$; its even part, products of an even number of unit vectors, is $\Spin(p,q)$, and covers the rotations. An even versor $R$ with $R\tilde{R} = 1$ is a \emph{rotor}, and it acts by plain conjugation, $x \mapsto R\,x\,R^{-1}$, two reflections making one rotation. One more name the series uses: $\Spin^0(p,q)$ is the \emph{identity component} of $\Spin(p,q)$, the elements joined to $1$ by a continuous path inside the group; in a definite signature of dimension at least two it is all of $\Spin$, while in mixed signature it is a proper subgroup. The precise action of a general versor, including the odd ones, needs a small twist by the grade involution; it is set out and proved in the toolkit (Lemma \claimref{primer.twisted-adjoint-action}).

## technical
pending

## lay
pending

## one-liner
pending
