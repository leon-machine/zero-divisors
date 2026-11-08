---
id: synthesis.transverse-corank-two-walls-are-wild
kind: claim
version: 3
title: 'Transverse corank-two walls are wild: tameness is not generic'
status: proved
region: synthesis
subject: walls
tags: [tameness, degenerate-algebras, no-go]
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
- name: Claude Opus 5.5
  role: 'maintainer pass, citation of the retired imported Fact repointed to its derivation in geometric algebra'
  version: 3
  source: run 2026-11-07-bit-root
review: draft
derivations:
- name: main
  uses:
  - sheaf.invariant-form-t3@2
  - synthesis.completion-recovers-the-real-clifford-algebras@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_corank_one_differential_is_delta
- kind: check
  ref: check.py::check_transverse_corank_two_three_signatures
- kind: check
  ref: check.py::check_cone_is_not_a_hypersurface
- kind: check
  ref: check.py::check_corank_two_point_survives_perturbation
- kind: check
  ref: check.py::check_tame_wall_is_two_signature
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - sheaf.tameness
extraction:
  maintainer_pass_2026_11_08:
    by: ai-maintainer-pass
    note: >-
      Version 2 -> 3. Leon's decision of 7 November 2026: the imported Fact std-algebra.sylvester-inertia is retired, replaced by synthesis.completion-recovers-the-real-clifford-algebras, whose clause (iii) derives Sylvester's law of inertia in geometric algebra over any Euclidean field, the reals included; the citation and edge now point there.
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites synthesis.completion-recovers-the-real-clifford-algebras where the proof uses them. Version 1 -> 2.'
  open_problem: pr.tameness
  note: >-
    Answers the route "are generic degenerations automatically tame?" of pr.tameness on the
    necessity side: transverse corank-two points are stable, so the tame cometrics are not dense
    for n >= 3. The corank-one identity d(det G) = c delta(k (x) k) and the r + 1 signature count
    are proved in the proof file because the stability argument needs them in this form; they are
    also proved in synthesis.tameness-splits-regularity-and-order (filed alongside), whose
    regularity characterisation this result complements with stability and non-genericity. Imports only the elementary differential topology of the corank
    stratification of real symmetric matrices (the corank-r stratum is a submanifold of
    codimension r(r+1)/2) and the inverse function theorem; both are proved in the proof file
    in the form used. Transport-absent: the statement is about symmetric forms on a bundle.
    No clause assumes tameness: Hypotheses sheaf.tameness are the definition being tested, cited
    in the text and in lineage, so the result carries no assumes edge.
---

## formal
Let $M$ be a smooth manifold of dimension $n \geq 2$ with a smooth cometric $G$, and let $\Sig$ be the set where $G$ degenerates. In a local frame $G$ is a smooth map to the real symmetric $n \times n$ matrices; call $G$ \emph{transverse} at a point $x$ of corank $r$ if this map is transverse at $x$ to the submanifold of corank-$r$ matrices, which has codimension $r(r+1)/2$ (a frame-independent condition). Write $(p_0, q_0)$ for the signature of $G_x$ on a complement of its radical.
\begin{enumerate}
\item \emph{(Stable wild points.)} Let $n \geq 3$ and let $G$ be transverse at a point $x$ of corank two. Then $\det G$ vanishes to second order at $x$, near $x$ the set $\Sig$ is a quadric cone in three transverse coordinates times $\R^{n-3}$, and the radical at $x$ has rank two, so (T1) and (T2) of Hypotheses \claimref{sheaf.tameness} fail near $x$. Every cometric close to $G$ in $C^1$ near $x$ has a transverse corank-two point near $x$. Hence for every $n \geq 3$ the cometrics that are not tame contain a nonempty $C^1$-open set: tameness is not generic. The corank-two points of a transverse cometric form a submanifold of codimension three, worldlines when $n = 4$.
\item \emph{(Three signatures, one of them two-time.)} Every neighbourhood of such a point meets the three signatures $(p_0{+}2, q_0)$, $(p_0{+}1, q_0{+}1)$, $(p_0, q_0{+}2)$; if $(1,3)$ is one of them, $(2,2)$ is another.
\item \emph{(Surfaces.)} For $n = 2$, a cometric transverse at every point of $\Sig$ has no point of corank two and is tame.
\end{enumerate}

## technical
Tameness asks three things of a degenerating cometric: a smooth wall, a corank-one radical line along it, and first-order vanishing. This result shows that they are not what a generic degeneration does once the dimension is at least three. At a transverse point where the cometric loses two directions at once, the determinant vanishes to second order, the degeneracy locus is a quadric cone rather than a smooth wall, and the radical has rank two; such points survive every small perturbation, so the tame cometrics are not dense. Three signatures meet at each such point, and if this world's signature $(1,3)$ is one of them, a two-time signature $(2,2)$ is another. On surfaces the phenomenon cannot occur and transverse degenerations are tame. Transport-absent.

## lay
The series assumes that when the geometry of spacetime breaks down it does so along a smooth wall, losing one direction at a time and at a steady rate. This result shows that in three or more dimensions this is not what typically happens everywhere. At some places two directions can be lost at once, and no small change to the geometry removes such places: in four dimensions they form lines, the wall pinches into a cone there, and three kinds of geometry meet. Next to our kind of spacetime, one of the three always has two time directions.

## one-liner
For $n \geq 3$ tameness is not generic: transverse corank-two points are stable, make the wall a cone, and are met by three signatures, which next to $(1,3)$ include $(2,2)$; on surfaces transverse degenerations are tame.
