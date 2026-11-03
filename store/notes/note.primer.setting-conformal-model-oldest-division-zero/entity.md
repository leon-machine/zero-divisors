---
id: note.primer.setting-conformal-model-oldest-division-zero
kind: note
version: 1
title: The conformal model, and the oldest division by zero
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
- primer.commutation-rule
locators:
  paper: T00
  number: Setting
  section: The conformal model, and the oldest division by zero
  line: 423
---

## formal
The final construction is the one the series turns into a principle. Take a quadratic space $(\mathbb{V}, Q)$ of signature $(p,q)$ and adjoin two extra directions $e_+, e_-$ with $e_+^{2} = +1$, $e_-^{2} = -1$: one hyperbolic plane, giving $\Cl(p{+}1, q{+}1)$. Out of the new plane build the null pair
\[
n_0 = \tfrac12(e_- - e_+), \qquad n_\infty = e_- + e_+ ,
\]
representing the origin and the point at infinity, and represent each point $x \in \mathbb{V}$ by the vector
\[
X(x) \;=\; n_0 + x + \tfrac12 Q(x)\, n_\infty .
\]
A short computation gives $X(x)^{2} = 0$: every point of the space is represented by a \emph{null} vector in the enlarged space, determined up to scale, so points become null rays on a quadric. The lift also remembers the geometry exactly, since $X(x) \cdot X(y) = -\tfrac12\,Q(x - y)$. This is the \emph{conformal model} of geometric algebra \cite{Hestenes2001, DFM2007, DoranLasenby2003}, and its power is that the conformal transformations of $\mathbb{V}$, inversions included, all become sandwich products in the enlarged algebra.

What this primer takes from the model is the oldest division by zero. Take the real line, $\mathbb{V} = \R$ with $Q(x) = x^{2}$. The reciprocal $x \mapsto 1/x$ fails at the origin. In the enlarged space, the quadric is a circle, the projective line $\R P^{1}$ in homogeneous coordinates $[\,x : s\,]$, and the reciprocal becomes the linear swap $[\,x : s\,] \mapsto [\,s : x\,]$, which is total: it never fails anywhere. At the origin it gives $[\,0 : 1\,] \mapsto [\,1 : 0\,]$, the point at infinity. Division by zero has an answer; the answer simply is not a real number, and it lies in the completion. Nothing here is new: this is the nineteenth-century projective resolution of $1/0$, the same construction that makes M\"obius maps $z \mapsto (az+b)/(cz+d)$ total on the Riemann sphere.

What the series adds, and this is the point at which the reader should turn to T1, is a uniqueness claim: for a general quadratic space this completion is not one convenient construction among many but the \emph{unique minimal} resolution of the null cone's division failure, the repair of the element itself being provably impossible. The construction becomes a theorem.

## technical
pending

## lay
pending

## one-liner
pending
