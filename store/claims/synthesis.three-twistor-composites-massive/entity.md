---
id: synthesis.three-twistor-composites-massive
kind: claim
version: 2
title: Three independent conformal spinors are massive when the cosmological constant is positive
status: proved
region: synthesis
subject: mass
tags: [frozen-point, conformal-spinors]
proposed_by:
  kind: ai
  session: 2026-10-22-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.mass.grip-mass-composite
derivations:
- name: main
  uses:
  - synthesis.many-twistor-join@2
  - mass.exact-join@7
  - mass.de-sitter-scale-frozen-point@6
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_three_twistor_composites_massive
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.many-twistor-join
extraction:
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  open_problem: op.many-twistor-grip
  note: A corollary of the N-twistor join on the rank of a massless composite. Transport-absent (flat chart and frozen point only). It bears on the sentence of the successor-problems note that three twistors span a plane of their own, read at the level of the frozen point only; it neither derives nor refutes Hypothesis (S). Standard linear algebra used without citation (isotropic subspaces of a nondegenerate antisymmetric form, the five-term Grassmann-Plucker relation).
---

## formal
Let $I_{\Lambda} = n_{\infty} + \lambda n_{0}$, $\lambda = \Lambda/6$, be the frozen point of Lemma \claimref{mass.de-sitter-scale-frozen-point}, and let $Z^{1}, \dots, Z^{N} \in \CS$ be a composite with brackets $B^{il}_{\Lambda} = \br{\pi^{i}\pi^{l}} + \lambda\,[\omega^{i}\omega^{l}] = (Z^{i})^{\mathsf T}\Omega_{\lambda}Z^{l}$, $\Omega_{\lambda} = \operatorname{diag}(\lambda\varepsilon, \varepsilon)$, as in Theorem \claimref{synthesis.many-twistor-join}. Let $W$ be the span of the $Z^{i}$ and $r = \dim W$.
\begin{enumerate}
\item \emph{(Faces.)} $\det\Omega_{\lambda} = \lambda^{2}$. If $\Lambda \ne 0$ (either sign) and $r \ge 3$, then $B^{il}_{\Lambda} \ne 0$ for some $i < l$.
\item \emph{(Mass.)} If $\Lambda > 0$ and $r \ge 3$ then $m^{2} \ge 2\sum_{i<l}|B^{il}_{\Lambda}|^{2} > 0$. Massless composites at $\Lambda > 0$ have $r \le 2$, and $r = 2$ occurs (the $r = 2$ massless spans are classified in the result filed alongside, synthesis.massless-composites-de-sitter-conformal-boundary(4)).
\item \emph{(Three constituents.)} If $r = 3$ for $Z^{1}, Z^{2}, Z^{3}$, let $\zeta(x) = \varepsilon(Z^{1}\wedge Z^{2}\wedge Z^{3}\wedge x)$ be their dual twistor and $I^{ab}$ the components of $I_{\Lambda} = e_{1}\wedge e_{2} + \lambda\,e_{3}\wedge e_{4}$ in $\Lambda^{2}\CS$. Then
\[
\zeta_{a}I^{ab} = -\bigl(B^{23}_{\Lambda}Z^{1} + B^{31}_{\Lambda}Z^{2} + B^{12}_{\Lambda}Z^{3}\bigr)^{b},
\]
this vector spans the radical of $\Omega_{\lambda}$ restricted to $W$ when it is nonzero, and the matrix $I^{ab}$ has determinant $\lambda^{2}$.
\item \emph{(The flat case.)} At $\Lambda = 0$ a composite with $r = 3$ has every $B^{il}_{0} = 0$, and then $m^{2} = 0$, if and only if $W = \Som \oplus \C\pi_{0}$ for some $\pi_{0} \ne 0$, that is all $\pi^{i}$ are proportional; no composite with $r = 4$ has every $B^{il}_{\Lambda} = 0$ for any $\Lambda$.
\end{enumerate}

## technical
The frozen point's pairing on conformal spinors is the antisymmetric form $\Omega_{\lambda}$, and its determinant is $\lambda^{2}$. For $\Lambda \ne 0$ it is a symplectic form on the four-dimensional space $\CS$, whose isotropic subspaces have dimension at most two, so three linearly independent constituents always have a nonzero bracket. With the join's nonnegative remainder this makes every composite of three or more independent constituents massive when $\Lambda > 0$; the massless spans found for two constituents are the largest possible. For three constituents the face brackets are the components of one vector, the frozen point applied to the composite's dual twistor, which vanishes only if the frozen point is degenerate. At $\Lambda = 0$ the pairing has rank two and massless three-constituent composites exist exactly when all $\pi^{i}$ are proportional. In the ambient reading the three bivectors $Z^{i}\wedge Z^{l}$ span a totally null three-plane, and the frozen point can lie in it only when it is null, which is $\Lambda = 0$.

## lay
A particle built from three or more independent twistors always has mass once the cosmological constant is positive. The built-in cosmological scale pairs twistors in a way that leaves room for at most two mutually unpaired ones, so with three, at least one pair is always gripped. With zero cosmological constant three twistors can still form a massless composite, but only in a special aligned configuration.

## one-liner
For $\Lambda \ne 0$ the frozen point's pairing $\Omega_{\lambda}$ has determinant $\lambda^{2}$, so three independent conformal spinors always have a nonzero bracket and, for $\Lambda > 0$, $m^{2} > 0$; at $\Lambda = 0$ massless three-constituent composites exist exactly when all $\pi^{i}$ are proportional.
