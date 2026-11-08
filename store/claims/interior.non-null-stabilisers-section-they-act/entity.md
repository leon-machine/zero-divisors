---
id: interior.non-null-stabilisers-section-they-act
kind: claim
version: 5
title: Non-null stabilisers, and the section they act on
status: proved
region: interior
subject: einstein
tags: [rotors-and-stabilisers, conformal-model]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T06, deposited version
- name: Claude Opus 5.5
  role: 'maintainer pass, citation of the retired imported Fact repointed to its derivation in geometric algebra'
  version: 5
  source: run 2026-11-07-bit-root
review: typed
derivations:
- name: main
  uses:
  - std-algebra.bivector-lie-algebra@1
  - synthesis.completion-recovers-the-real-clifford-algebras@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T06.py
  tags:
  - num:4.4
- kind: check
  ref: check.py::check_stabiliser_is_so_of_the_complement
- kind: check
  ref: check.py::check_section_is_the_pseudosphere_with_transitive_isometries
- kind: check
  ref: check.py::check_polar_infinity_spacelike_or_timelike
locators:
  paper: T06
  number: Prop 4.4
  label: prop:flatstabnn
  line: 495
extraction:
  maintainer_pass_2026_11_08:
    by: ai-maintainer-pass
    note: >-
      Version 4 -> 5. Leon's decision of 7 November 2026: the imported Fact std-algebra.sylvester-inertia is retired, replaced by synthesis.completion-recovers-the-real-clifford-algebras, whose clause (iii) derives Sylvester's law of inertia in geometric algebra over any Euclidean field, the reals included; the citation and edge now point there.
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.bivector-lie-algebra, synthesis.completion-recovers-the-real-clifford-algebras where the proof uses them. Version 3 -> 4.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: stabiliser of non-null I in Cl(2,4) computed: dimension 10, equal to Lambda^2(I-perp), I-perp (1,4) or (2,3), nondegenerate form; M_I to the pseudosphere Q(Y) = -1/Q(I) with Lorentzian tangent spaces, transitive with 6-dimensional isotropy; polar infinity Riemannian or Lorentzian. Version 2 -> 3.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  typing:
    by: ai-typing-pass
    note: 'Self-contained flat-model computation; no edges needed. Levels pass: conditions already kept.'
  env: proposition
---

## formal
Let $I \in V$ with $Q(I) \neq 0$. Then:
\begin{enumerate}
\item the stabiliser subalgebra of $I$ is $\Lambda^2(I^\perp) \cong \mathfrak{so}(I^\perp)$, reductive, of dimension $10$, with trivial nilradical: $\mathfrak{so}(1,4)$ if $Q(I) > 0$ and $\mathfrak{so}(2,3)$ if $Q(I) < 0$;
\item the hyperplane section $M_I := \{X \in V : Q(X) = 0,\ \ip{X}{I} = 1\}$ is, under $Y := X - I/Q(I)$, the pseudosphere $\{Y \in I^\perp : Q(Y) = -1/Q(I)\}$, a complete constant-curvature Lorentzian $4$-manifold on which the stabiliser acts as the isometry group: de Sitter space for $Q(I) > 0$, anti-de Sitter space for $Q(I) < 0$;
\item the polar hypersurface $\{\ip{X}{I} = 0\}$ meets the quadric in the projectivised null cone of $I^\perp$: for $Q(I) > 0$ a spacelike conformal infinity ($S^3$ with its standard conformal structure), for $Q(I) < 0$ a timelike one.
\end{enumerate}

## technical
Let $I \in V$ with $Q(I) \neq 0$, so $V = \R I \oplus I^\perp$. Writing a bivector as $B = I\wedge u + C$ with $u \in I^\perp$ and $C \in \Lambda^2(I^\perp)$ gives $B(I) = -Q(I)\,u$, so the stabiliser is $\Lambda^2(I^\perp) \cong \mathfrak{so}(I^\perp)$: ten-dimensional and reductive, $\mathfrak{so}(1,4)$ for $Q(I) > 0$ and $\mathfrak{so}(2,3)$ for $Q(I) < 0$.

The section $M_I = \{X : Q(X) = 0,\ \ip{X}{I} = 1\}$ becomes, under $Y = X - I/Q(I)$, the pseudosphere $Q(Y) = -1/Q(I)$ in $I^\perp$: de Sitter space for $Q(I) > 0$ and anti-de Sitter space for $Q(I) < 0$, with the stabiliser acting as its isometry group. The polar hypersurface $\ip{X}{I} = 0$ meets the quadric in the projectivised null cone of $I^\perp$, a spacelike conformal infinity $S^3$ in the first case and a timelike one in the second.

## lay
In the series' six-dimensional ambient space, pick a direction whose squared length is not zero. The symmetries that leave it fixed are those of de Sitter space if the squared length is positive, or of anti-de Sitter space if it is negative. A natural slice of the space of points is then exactly that de Sitter or anti-de Sitter spacetime, and its boundary at infinity is spacelike or timelike accordingly.

## one-liner
A non-null vector $I$ has the reductive ten-dimensional stabiliser $\mathfrak{so}(I^\perp)$, and its hyperplane section of the null quadric is de Sitter or anti-de Sitter space according to the sign of $Q(I)$.
