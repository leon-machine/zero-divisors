---
id: transport.swap-rescale-normal-form
kind: claim
version: 4
title: Swap-and-rescale normal form
status: proved
region: transport
subject: completion
tags: [conformal-model]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T01, deposited version
review: typed
derivations:
- name: main
  uses:
  - transport.totality@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_incidence_and_ordinary_normal_form
- kind: check
  ref: check.py::check_iota_is_the_swap_rescale_involution
- kind: check
  ref: check.py::check_three_strata_of_ideal_points
locators:
  paper: T01
  number: Prop 4.21
  label: prop:swap
  line: 1007
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: about the core definitions it is stated in. Version 3 -> 4.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: incidence Q(x) = 2st, the normal form of ordinary points, iota as (s, x, t) -> (2t, x, s/2) with read-out, and the three strata of ideal points, in three signatures. Version 1 -> 2. check_three_strata_of_ideal_points strengthened: projective classes on a grid of null (0, x, t), strata disjointness, labelling by null vectors (i) and null rays (ii), single class (iii), hand-derived class counts. Version 2 -> 3.'
  env: proposition
  eqrefs: 3
  typing:
    by: ai-typing-pass
    note: 'Kept the single premise, totality, used for the identification of strata (i) and (iii) with values of iota.'
about:
- obj.std-algebra.conformal-algebra
---

## formal
In the setting of Theorem \claimref{transport.totality}, represent elements of the quadric by homogeneous triples $(s, x, t)$ with $s,t \in \R$ and $x \in \mathbb{V}$, standing for $N = s\,\nO + x + t\,\nInf$ and defined up to overall scale, subject to the incidence (nullity) condition
\begin{equation}
Q(x) = 2st .
\end{equation}
The ordinary points are the classes with $s \neq 0$, normal form $(1, x, \tfrac12 Q(x))$, i.e.\ \eqref{eq:lift}. The ideal points, the classes with $s = 0$, then satisfy $Q(x) = 0$ and fall into three disjoint strata:
\begin{enumerate}
\item[(i)] $t \neq 0$ and $x \neq 0$: unique representative $(0, x', \tfrac12)$ with $x' = x/(2t)$ null; these classes are labelled bijectively by the null \emph{vectors} of $\mathbb{V}$, and are exactly the values $\iota$ takes on lifted null points (Theorem \claimref{transport.totality}(3));
\item[(ii)] $t = 0$, $x \neq 0$: the class retains only the null \emph{ray} $[x]$; these classes are labelled by the null directions of $\mathbb{V}$;
\item[(iii)] $x = 0$, which given $s = 0$ forces $t \neq 0$: the single classical point at infinity $[\nInf]$, which is the value $\iota[X(0)]$ by Theorem \claimref{transport.totality}(3).
\end{enumerate}
In these coordinates the map $\iota$ of Theorem \claimref{transport.totality} is the linear involution
\[
\iota(s, x, t) = (2t,\, x,\, \tfrac12 s),
\]
which preserves the incidence condition, is total, and recovers the reciprocal upon normalising the first slot where possible; where normalisation is impossible (first slot zero) the output is an ideal point.

## technical
Represent points of the quadric by homogeneous triples $(s, x, t)$, standing for $N = s\,\nO + x + t\,\nInf$ up to scale and subject to the incidence condition $Q(x) = 2st$. Ordinary points have $s \neq 0$ and normal form $(1, x, \frac12 Q(x))$. Ideal points, with $s = 0$, force $Q(x) = 0$ and fall into three disjoint strata: (i) $t \neq 0$, $x \neq 0$, with unique representative $(0, x', \frac12)$, $x' = x/(2t)$ null, labelled by null vectors and exactly the values of $\iota$ on lifted null points; (ii) $t = 0$, $x \neq 0$, retaining only the null ray $[x]$; (iii) $x = 0$, the single point at infinity $[\nInf]$, which is $\iota[X(0)]$.

In these coordinates the transported reciprocal is the linear involution $\iota(s, x, t) = (2t, x, \frac12 s)$. It preserves the incidence condition, is total, and recovers the reciprocal on normalising the first slot where possible; where the first slot is zero the output is an ideal point.

## lay
Points of the enlarged space can be written as a triple: a number, an ordinary vector, and a second number. In these terms, taking the reciprocal just swaps the two numbers, with a factor of two, a simple operation that always works. Dividing out the first number gives back the usual answer; when that number is zero, the answer is one of three kinds of point at infinity.

## one-liner
In homogeneous coordinates $(s, x, t)$ with $Q(x) = 2st$, the transported reciprocal is the linear involution $(s, x, t) \mapsto (2t, x, \frac12 s)$, and the ideal points $s = 0$ fall into three strata.
