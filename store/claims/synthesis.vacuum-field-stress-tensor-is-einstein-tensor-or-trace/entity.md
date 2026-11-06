---
id: synthesis.vacuum-field-stress-tensor-is-einstein-tensor-or-trace
kind: claim
version: 3
title: 'A vacuum-read stress tensor is the Einstein tensor or pure trace'
status: proved
region: synthesis
subject: einstein
tags: [curvature-and-field-equations, null-directions, no-go, car-algebra]
proposed_by:
  kind: ai
  session: 2026-10-23-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
derivations:
- name: main
  uses:
  - synthesis.einstein-condition-is-infinity-vacuum-incidence@3
  - interior.imported-tractor-connection@2
  - interior.metric-parallelism-trace-schouten-condition@6
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_first_order_data
- kind: check
  ref: check.py::check_schur
- kind: check
  ref: check.py::check_dichotomy
- kind: check
  ref: check.py::check_conservation
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.einstein-condition-is-infinity-vacuum-incidence
  - synthesis.einstein-equations-from-c-loc-and-clausius
extraction:
  maintainer_pass_2:
    by: maintainer-2026-10-24
    date: '2026-10-24'
    note: 'Referee fixes to the GTG wording pass (2026-10-24): ''a gravitational field of nonvanishing field strength'' (gauge-independent) in place of ''a nonvanishing gravitational field''; global content read on several charts of flat spacetime, each with its own gravitational field, glued by displacement and rotation gauge transformations (complexified charts for the half-flat manifold, the conformal compactification for a conformal boundary); ''not carried by the store''s one-chart fields'' in place of ''no single gravitational field carries''; equivalence statements weakened where the old text was weaker; remaining curved-spacetime phrases in lay text restated. Wording only. Version 2 -> 3.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: g is the derived metric of a gravitational field on flat spacetime and the tractor connection its Cl(2,4) gauge field; the dichotomy unchanged. Checks untouched.'
  open_problem: ein.infinity-vacuum-incidence
  note: >-
    The matter case of the infinity-vacuum incidence, and the question left by an earlier argued remark
    that a stress tensor defined linearly on the CAR side needs a second algebra, made a theorem. The
    first-order data of the vacuum field that do not depend on how the field is extended are the
    classes of the canonical tractors, -P(v,w) for the infinity vacua and g(v,w) for the point vacua
    (the incidence theorem, clause (2)). A symmetric tensor read off them linearly and covariantly
    (equivariant under their common stabiliser, the Lorentz group of the tangent space) is
    a P + b J g + c g, by an exact commutant computation that is Schur's lemma for the Lorentz group on
    symmetric two-tensors. The own-ray matter clause with such a tensor holds for every metric exactly
    when a = -1/(4 pi G), and then, if it is also required to be conserved in every metric, the tensor
    is minus the store-convention Einstein tensor over 8 pi G plus a cosmological term, so the clause
    defines the source; otherwise the clause holds only at Einstein points, where the tensor is pure
    trace and carries no null energy. Hence a source that can vary independently of the curvature, the
    only kind for which the clause is a law, is not a function of the vacuum field's first-order classes:
    it needs a further datum (a state on some algebra, for the series the field theory's tower algebra,
    or a second algebra) and a hypothesis tying it to the classes, which on the Clausius route is the
    hypothesis (H1). Dependence on the classes of non-canonical vacuum sections is excluded by hypothesis:
    those classes depend on the extension of the vacuum field, a choice, not on the metric (argued in the
    proof). Higher-order data are discussed in a remark only (argued, Schur and parity). Imported: none
    beyond the store's Facts; the contracted Bianchi identity is standard and checked exactly at a point.
    The result is limited to first-order classes: a source that is not a function of them, for example
    an independent T(k,k) given as the density of the generator of null translations of a field theory
    on the patch, is not excluded, and is exactly the kind of further datum the conclusion asks for.
    Transport-convenient: the classes are the series' objects; the content is Schur's lemma and the
    contracted Bianchi identity, and the conservation step is the linear case of Lovelock's theorem (a
    conserved symmetric tensor linear in the curvature in four dimensions is a G_ab + c g_ab; Lovelock
    1971-72, cited from memory).
---

## formal
Let $g$ be the derived metric, of signature $(1,3)$, of a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), $x$ a point of its invertible region, and use the tractor connection of Fact \claimref{interior.imported-tractor-connection} (on flat spacetime the $\Cl(2,4)$ gauge field $\Omega_{T}$ of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}) in the splitting of $g$. By Theorem \claimref{synthesis.einstein-condition-is-infinity-vacuum-incidence}(2) the pairing classes of the canonical tractors along a physical vector $v \in T_xM$ are
\[
\omega_v(I_g, w) = -\Sch(v, w), \qquad \omega_v(X, w) = g(v, w),
\]
for $w$ in the $\mu$ slot, independent of how the vacua are extended off $x$. Call a symmetric tensor $\Theta$ at $x$ a \emph{first-order vacuum-field tensor} if $\Theta = L(\Sch) + c\,g$ with $L$ linear and $c$ a number (that is, $\Theta$ is an affine function of these classes) and $L$ is equivariant under the stabiliser of $(I_g, X)$ in the tractor orthogonal group, which acts on the $\mu$ slot as $O(1,3)$. Write $\kappa := 4\pi G$ for a constant $G > 0$ and $J = g^{ab}\Sch_{ab}$. Then:
\begin{enumerate}
\item \emph{(Form.)} $\Theta = a\,\Sch + b\,J g + c\,g$ for numbers $a, b, c$.
\item \emph{(Dichotomy.)} The matter clause of Theorem \claimref{synthesis.einstein-condition-is-infinity-vacuum-incidence}(7) with source $\Theta$, $\omega_{\ell}(I_g, \ell) = \kappa\,\Theta(\ell, \ell)$ for every real null $\ell$ at $x$, is $(1 + \kappa a)\,\Sch(\ell, \ell) = 0$ for every real null $\ell$. Hence either (a) $a = -1/\kappa$, and the clause holds for every $\Sch$; or (b) $a \neq -1/\kappa$, the clause holds only where $\Sch = \tfrac{J}{4}g$ ($x$ an Einstein point), and there $\Theta = (\tfrac{a}{4} + b)J\,g + c\,g$ is pure trace, with $\Theta(\ell,\ell) = 0$ for every null $\ell$.
\item \emph{(Conservation.)} If $\Theta$ is built this way at every point of a region, then $\nabla^a\Theta_{ab} = (a + b)\nabla_b J$, by the contracted Bianchi identity $\nabla^a\Sch_{ab} = \nabla_b J$. In case (a), $\Theta$ is conserved for every metric if and only if $b = 1/\kappa$, and then
\[
\Theta = -\frac{1}{8\pi G}\Bigl(\Ric - \tfrac12 R\,g\Bigr) + c\,g, \qquad \Ric + 8\pi G\,\Theta = \Bigl(\tfrac12 R + 8\pi G\,c\Bigr)g
\]
identically in the store's convention: the Einstein equation of clause (7) holds for every metric with $T := \Theta$, which is a definition of the source.
\item \emph{(Consequence.)} If the source $T$ in clause (7) can take, at a point with given $\Sch$, values with different $T(\ell,\ell)$ (so that the clause is a relation between independent data and can fail), or can have $T(\ell,\ell) \neq 0$ for some null $\ell$, then $T$ is not a first-order vacuum-field tensor. A matter law in the form of clause (7) needs a symmetric tensor that is not a covariant affine function of the canonical classes, together with a hypothesis tying it to them. The statement concerns first-order classes only: a source that is not a function of them, such as an independent $T(k,k)$ given as the density of the generator of null translations of a field theory on the patch, is not excluded by it.
\end{enumerate}

## technical
The incidence theorem reads Einstein's equations as a condition on the vacua annihilated by the pure-scale tractor: along its own light ray each such vacuum is excited by an amount that should equal $4\pi G$ times the matter's null energy. An earlier remark argued that a stress tensor defined on the CAR side, linearly, would need a second algebra; this result makes that precise. The first-order data of the vacuum field that do not depend on how the field is extended off a point are the classes of the two canonical tractors: $-\Sch(v,w)$ for the infinity vacua and $g(v,w)$ for the point vacua. A symmetric tensor built from them linearly and covariantly, that is equivariantly for their common stabiliser, which acts on the tangent space as the Lorentz group, must be $a\Sch + bJg + cg$: an exact computation shows that the linear maps of symmetric two-tensors commuting with a rational boost, two rational rotations and two reflections form a two-dimensional space, spanned by the identity and the trace map, which is Schur's lemma for the Lorentz group here. Since a null vector has $g(\ell,\ell) = 0$, the matter clause with such a source is $(1 + 4\pi G a)\Sch(\ell,\ell) = 0$ on the null cone. Either $a = -1/4\pi G$ and the clause holds in every metric, or it forces $\Sch$ to be pure trace at the point, where the source is pure trace too and no null energy flows. In the first branch, asking the source to be conserved in every metric fixes $b$ by the contracted Bianchi identity $\nabla^a\Sch_{ab} = \nabla_b J$, and the source is the Einstein tensor over $8\pi G$ (in the sphere-positive convention, minus the store-convention one) plus a cosmological term: Einstein's equation then holds identically because it is how the source was defined. In neither branch is the matter clause a law relating matter to geometry. (The conservation step is the linear case of Lovelock's theorem; the form is Schur's lemma.) So a source that can vary independently of the curvature at a point, the kind a matter law needs, is not a function of the vacuum field's first-order classes: it needs a further datum, a state on some algebra (for the series, the field theory's tower algebra, which is a different object from the tractor Clifford bundle that carries the vacua) or a second algebra, and a hypothesis tying it to the classes, which on the Clausius route is the hypothesis (H1) of the Einstein derivation. The classes of non-canonical vacuum sections are excluded because they depend on how the vacuum field is extended, a choice, not on the metric. The result is limited to sources read off the first-order classes; an independent null energy density, such as the density of the generator of null translations of a field theory on the patch, is not excluded and is an instance of the further datum. The checks verify the class formulas, the commutant dimension, the dichotomy on eleven null directions for three sample triples $(a,b,c)$ and for $a = -1/\kappa$, the contracted Bianchi identity at a point of a metric with generic second and third derivatives, and the Einstein-tensor identity of the conserved branch.

## lay
In the series, Einstein's equations can be read as a statement about certain quantum vacuum states: along its own light ray each of them is disturbed by exactly the energy that matter carries along that ray. A natural hope is to find the matter's energy on the same quantum side, built from how those vacua are disturbed. This result shows that this cannot work if the matter's energy is built linearly, and without singling out a direction, from those disturbances. Any such recipe gives one of two things. Either the "matter" is just the curvature itself relabelled, so Einstein's equations hold automatically because they define the matter, or the recipe allows no matter flowing along light rays at all, only a cosmological-constant-like term. In neither case do the equations say anything about how real matter sources the gravitational field. A real matter law needs something the vacuum disturbances do not carry: a separate quantum state of matter, or a second quantum system, and a rule linking it to the geometry.

## one-liner
A symmetric tensor read linearly and Lorentz-covariantly off the canonical first-order classes $-\Sch(v,w)$ and $g(v,w)$ of the infinity and point vacua is $a\Sch + bJg + cg$ (Schur, exact commutant), so the own-ray matter clause with it either holds in every metric, as a relabelling of the curvature ($a = -1/4\pi G$; conserved only as the Einstein tensor over $8\pi G$ in the sphere-positive convention plus a cosmological term, a definition of the source) or only at Einstein points with a pure-trace source: a matter law needs a datum outside the vacuum field's first-order classes (an independent null energy density is not excluded) and a hypothesis tying it to them.
