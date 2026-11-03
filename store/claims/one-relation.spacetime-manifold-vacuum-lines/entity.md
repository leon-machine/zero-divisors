---
id: one-relation.spacetime-manifold-vacuum-lines
kind: claim
version: 6
title: "Spacetime as the manifold of vacuum lines"
status: proved
region: one-relation
subject: conformal-spacetime
tags: [conformal-model, conformal-spinors, null-directions]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T16, deposited version
review: typed
derivations:
- name: main
  uses:
  - one-relation.imported-pure-spinors-incidence-chart@5
  - one-relation.imported-witts-extension-theorem@2
  - one-relation.two-presentations@4
  - sheaf.localised-transport@5
  - sheaf.one-sided-completion@4
  - sheaf.one-sided-completion-singularity@4
  - std-algebra.inverse-of-vector@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T16.py
  tags:
  - label:prop:vacuummanifold
- kind: check
  ref: check.py::check_every_point_is_null
- kind: check
  ref: check.py::check_points_are_lines_of_vacua
- kind: check
  ref: check.py::check_car_over_a_chosen_vacuum
locators:
  paper: T16
  number: Prop 4.1
  label: prop:vacuummanifold
  line: 626
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.inverse-of-vector where the proof uses them. Version 5 -> 6.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: every point X(x) a nonzero nilpotent with forced slot coefficient, its incidence line of pure vacua whose annihilators contain X(x), lines meeting exactly for null separation, and the CAR over a chosen vacuum. Version 4 -> 5.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  env: proposition
  context_refs:
  - one-relation.third-constant-conversion-constant-between-charts
  - one-relation.two-presentations
  - sheaf.localised-transport
  - sheaf.one-sided-completion
  - sheaf.one-sided-completion-singularity
  outside_pilot_cites:
  - ButlerT5
  typing:
    by: ai-typing-pass
    added:
    - one-relation.two-presentations
    - sheaf.one-sided-completion
    - sheaf.localised-transport
    - sheaf.one-sided-completion-singularity
    note: 'The proof says clauses (3) and (4) are readings of (1)-(2) together with the imported theorems
      named, so the two-presentations proposition and the three sheaf localisation results were added;
      the paper flags those clauses as readings, and the third-constant lemma is cited only as commentary,
      so it was not added. Levels pass: conditions already kept.'
  source_title: "Spacetime as the manifold of vacuum lines"
  source_formal: |-
    Four clauses.
    \begin{enumerate}
    \item \emph{(Every point is null.)} Under the embedding of Fact \claimref{one-relation.imported-pure-spinors-incidence-chart}, $\ip{X(x)}{X(x)} = 0$ identically: every point of spacetime is a non-invertible element of the algebra. Division by zero is not confined to special loci but is the condition of every point. The embedding needs $Q(x) = c^{2}t^{2} - |\mathbf{x}|^{2}$ dimensionally homogeneous, so the null embedding is where the third constant first enters the series (Lemma \claimref{one-relation.third-constant-conversion-constant-between-charts}).
    \item \emph{(Every point is a projective line of vacua.)} The point's null vector acts on the Fock module of Fact \claimref{one-relation.imported-pure-spinors-incidence-chart} as a nilpotent, $c(X(x))^{2} = \ip{X(x)}{X(x)} = 0$, whose kernel has dimension four on the eight-dimensional module and exactly two on the twistor half $\T$: that two-dimensional kernel is the point's incidence line $L_{x}$. Every twistor $u$ on $L_{x}$ is the Fock vacuum of its own three-pair system $W_{u}$, and $X(x) \in W_{u}$ for each of them: a point is not one vacuum but a projective line of distinct vacua, all of whose isotropic systems contain its null vector. Complexified compactified spacetime is the manifold of such lines, the Klein quadric of lines in $\mathbb{P}(\T)$, of which the real compactified spacetime is the real slice (double covered by the completion's fibre quadric, Fact \claimref{one-relation.imported-pure-spinors-incidence-chart}); it is not the pure-spinor variety $\mathbb{P}(\T)$, which has one dimension fewer. Two points are null-separated exactly when their incidence lines share a vacuum: $\ip{X(x)}{X(y)} = -\tfrac12 Q(x - y)$.
    \item \emph{(The location of each theory.)} The two theories then read: general relativity is the dynamics \emph{of} the vacua, how the vacuum family varies from point to point, carried by the connection; quantum mechanics is the dynamics \emph{above} a vacuum, excitations over a chosen vacuum obeying the CAR of Proposition \claimref{one-relation.two-presentations}. The choice of a vacuum on a point's incidence line is an extra datum, a null direction at the point, which the reading must supply and the point does not.
    \item \emph{(Ubiquity, and what a singularity is.)} Quantum mechanics holds everywhere because every point carries its incidence line of vacua; a singularity is where the vacuum family degenerates, where the choice of vacuum itself becomes operator-valued, which is the sheaf paper's localisation theorem, in the Schwarzschild form the singularity paper carries, read in this language \cite[Thm.~4.4, Cor.~4.5, Thm.~8.12]{ButlerT4}, \cite[App.~B]{ButlerT5}.
    \end{enumerate}
    The series' statement is thereby sharpened: division by zero does not only mark special loci, it constitutes every point.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: "Renamed twistor space and twistors to the conformal spinor space and conformal spinors (\\CS, \\PCS) in all levels and the proof; the incidence line is the kernel of the point's null vector, as in the dictionary."
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    cited:
    - one-relation.two-presentations
    - sheaf.localised-transport
    - sheaf.one-sided-completion
    - sheaf.one-sided-completion-singularity
---

## formal
Four clauses.
\begin{enumerate}
\item \emph{(Every point is null.)} Under the embedding of Fact \claimref{one-relation.imported-pure-spinors-incidence-chart}, $Q(X(x)) = 0$ identically: every point of spacetime is a non-invertible element of the algebra. Division by zero is not confined to special loci but is the condition of every point. The embedding needs $Q(x) = c^{2}t^{2} - |\mathbf{x}|^{2}$ dimensionally homogeneous, so the null embedding is where the third constant first enters the series (Lemma \claimref{one-relation.third-constant-conversion-constant-between-charts}).
\item \emph{(Every point is a projective line of vacua.)} The point's null vector acts on the Fock module of Fact \claimref{one-relation.imported-pure-spinors-incidence-chart} as a nilpotent, $c(X(x))^{2} = Q(X(x)) = 0$, whose kernel has dimension four on the eight-dimensional module and exactly two on the conformal spinor half $\CS$ (twistor space): that two-dimensional kernel is the point's incidence line $L_{x}$. Every conformal spinor $u$ on $L_{x}$ is the Fock vacuum of its own three-pair system $W_{u}$, and $X(x) \in W_{u}$ for each of them: a point is not one vacuum but a projective line of distinct vacua, all of whose isotropic systems contain its null vector. Complexified compactified spacetime is the manifold of such lines, the Klein quadric of lines in $\PCS = \mathbb{P}(\CS)$, of which the real compactified spacetime is the real slice (double covered by the completion's fibre quadric, Fact \claimref{one-relation.imported-pure-spinors-incidence-chart}); it is not the pure-spinor variety $\PCS$, which has one dimension fewer. Two points are null-separated exactly when their incidence lines share a vacuum: $\ip{X(x)}{X(y)} = -\tfrac12 Q(x - y)$.
\item \emph{(The location of each theory.)} The two theories then read: general relativity is the dynamics \emph{of} the vacua, how the vacuum family varies from point to point, carried by the connection; quantum mechanics is the dynamics \emph{above} a vacuum, excitations over a chosen vacuum obeying the CAR of Proposition \claimref{one-relation.two-presentations}. The choice of a vacuum on a point's incidence line is an extra datum, a null direction at the point, which the reading must supply and the point does not.
\item \emph{(Ubiquity, and what a singularity is.)} Quantum mechanics holds everywhere because every point carries its incidence line of vacua; a singularity is where the vacuum family degenerates, where the choice of vacuum itself becomes operator-valued, which is the sheaf paper's localisation theorem, in the Schwarzschild form the singularity paper carries, read in this language \cite[Thm.~4.4, Cor.~4.5, Thm.~8.12]{ButlerT4}, \cite[App.~B]{ButlerT5}.
\end{enumerate}
The series' statement is thereby sharpened: division by zero does not only mark special loci, it constitutes every point.

## technical
Under the point embedding, $Q(X(x)) = 0$ for every $x$, so every point of spacetime is a non-invertible element of the algebra. On the Fock module $c(X(x))$ is nilpotent, with kernel of dimension four, two on the conformal spinor half: that kernel is the incidence line $L_x$, and each conformal spinor $u$ on it is the Fock vacuum of a three-pair system $W_u$ containing $X(x)$. So a point is a projective line of vacua, complexified compactified spacetime is the Klein quadric of such lines, and since $\ip{X(x)}{X(y)} = -\tfrac12 Q(x - y)$, two points are null-separated exactly when their lines share a vacuum.

Two further clauses are readings, not new dynamics: general relativity is the dynamics of the vacua, carried by the connection, and quantum mechanics the dynamics above a chosen vacuum, its CAR excitations, the choice of vacuum on a line being an extra null-direction datum; and a singularity is where the vacuum family degenerates, read through the sheaf localisation theorems.

## lay
In this picture every point of spacetime is a light-like vector, so in the algebra each point behaves like a zero divisor. Each point also carries a whole line of possible vacuum states, and two points are light-like separated exactly when their lines share a vacuum. The result then reads gravity as how these vacua change from point to point and quantum mechanics as the excitations above a chosen vacuum, with singularities where the family of vacua breaks down.

## one-liner
Every spacetime point is a null vector and so a projective line of Fock vacua, and two points are null-separated exactly when their lines share a vacuum.
