---
id: correspondence.chiral-planes-summand-spaces
kind: claim
version: 5
title: "The chiral planes, and the summand spaces"
status: proved
region: correspondence
subject: conformal-spacetime
tags: [conformal-spinors, chirality, representation-theory]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T09, deposited version
review: typed
derivations:
- name: main
  uses:
  - correspondence.skew-lines-splittings-hyperbolic-planes-one@4
  - correspondence.chirality-split-ordering-insensitivity-asd-sector@6
  - std-algebra.bivector-lie-algebra@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T09.py
  tags:
  - label:lem:homone
- kind: check
  ref: check.py::check_planes_are_chiral_doublets
- kind: check
  ref: check.py::check_summand_hom_spaces_one_dimensional
locators:
  paper: T09
  number: Lem 4.4
  label: lem:homone
  line: 479
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.bivector-lie-algebra where the proof uses them. Version 4 -> 5.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the planes S_omega, S_pi are the two chiral doublets of l = g+ + g- (faithful on one, zero on the other), the l-isomorphism S_omega (x) S_pi -> W_C, and both Hom_l spaces computed as one-dimensional kernels. Version 3 -> 4.'
  env: lemma
  context_refs:
  - correspondence.chirality-split-ordering-insensitivity-asd-sector
  typing:
    by: ai-typing-pass
    added:
    - correspondence.chirality-split-ordering-insensitivity-asd-sector
    note: Added the chirality split because the statement takes its commuting decomposition as a hypothesis
      and the proof's ideal argument rests on it; the skew-lines edge is a real premise (mixed slot equals
      the image of W_C).
  source_title: "The chiral planes, and the summand spaces"
  source_formal: |-
    Let $\mathfrak{l} := \Lambda^2 (W_{1,3})_\C \subset \mathfrak{so}(V_\C)$ be the complexified Lorentz algebra of the splitting, acting on $W_\C := (W_{1,3})_\C$ by the bivector action and on $\Som$, $\Spi$ through $\rho$, and let $\mathfrak{l} = \mathfrak{g}^+ \oplus \mathfrak{g}^-$ be its decomposition into two commuting subalgebras each isomorphic to $\mathfrak{sl}(2,\C)$ (Proposition \claimref{correspondence.chirality-split-ordering-insensitivity-asd-sector}(1): a statement about $\Lambda^2 W_{1,3}$ alone, whose proof uses nothing from this section). Then:
    \begin{enumerate}
    \item the map $\Som \otimes \Spi \to W_\C$, $\omega\otimes\pi \mapsto \Psi^{-1}(\omega\wedge\pi)$, is an isomorphism of $\mathfrak{l}$-modules, and one of $\mathfrak{g}^\pm$ acts faithfully on $\Som$ and trivially on $\Spi$ while the other acts faithfully on $\Spi$ and trivially on $\Som$: the two planes are the two chiral doublets;
    \item $\operatorname{Hom}_{\mathfrak{l}}(W_\C \otimes \Spi,\ \Som)$ and $\operatorname{Hom}_{\mathfrak{l}}(W_\C \otimes \Som,\ \Spi)$ are one-dimensional.
    \end{enumerate}
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: "Converted the wording of the technical, lay and one-liner levels (the planes $\\Som$, $\\Spi$ of the conformal spinor space in place of the twistor planes); the formal level has no twistor wording and is unchanged, and the proof only renames $\\Lambda^2$ of twistor space to $\\Lambda^2\\CS$. The complexified Lorentz algebra and $W_\\C$ are kept: their complexification doubles the dimension and is not the complex unit $I_4$ of spacetime."
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    cited:
    - correspondence.chirality-split-ordering-insensitivity-asd-sector
---

## formal
Let $\mathfrak{l} := \Lambda^2 (W_{1,3})_\C \subset \mathfrak{so}(V_\C)$ be the complexified Lorentz algebra of the splitting, acting on $W_\C := (W_{1,3})_\C$ by the bivector action and on $\Som$, $\Spi$ through $\rho$, and let $\mathfrak{l} = \mathfrak{g}^+ \oplus \mathfrak{g}^-$ be its decomposition into two commuting subalgebras each isomorphic to $\mathfrak{sl}(2,\C)$ (Proposition \claimref{correspondence.chirality-split-ordering-insensitivity-asd-sector}(1): a statement about $\Lambda^2 W_{1,3}$ alone, whose proof uses nothing from this section). Then:
\begin{enumerate}
\item the map $\Som \otimes \Spi \to W_\C$, $\omega\otimes\pi \mapsto \Psi^{-1}(\omega\wedge\pi)$, is an isomorphism of $\mathfrak{l}$-modules, and one of $\mathfrak{g}^\pm$ acts faithfully on $\Som$ and trivially on $\Spi$ while the other acts faithfully on $\Spi$ and trivially on $\Som$: the two planes are the two chiral doublets;
\item $\operatorname{Hom}_{\mathfrak{l}}(W_\C \otimes \Spi,\ \Som)$ and $\operatorname{Hom}_{\mathfrak{l}}(W_\C \otimes \Som,\ \Spi)$ are one-dimensional.
\end{enumerate}

## technical
Let $\mathfrak{l} = \Lambda^2(W_{1,3})_\C$ be the complexified Lorentz algebra of the splitting, written as the sum $\mathfrak{g}^+\oplus\mathfrak{g}^-$ of two commuting copies of $\mathfrak{sl}(2,\C)$ supplied by the chirality split, acting on $W_\C = (W_{1,3})_\C$ and on the planes $\Som$, $\Spi$ of the conformal spinor space. Then $\omega\otimes\pi \mapsto \Psi^{-1}(\omega\wedge\pi)$ is an isomorphism of $\mathfrak{l}$-modules $\Som\otimes\Spi \cong W_\C$, and one of $\mathfrak{g}^\pm$ acts faithfully on $\Som$ and trivially on $\Spi$ while the other does the reverse: the two planes are the two chiral doublets.

Moreover the spaces $\operatorname{Hom}_{\mathfrak{l}}(W_\C\otimes\Spi, \Som)$ and $\operatorname{Hom}_{\mathfrak{l}}(W_\C\otimes\Som, \Spi)$ are each one-dimensional, so a Lorentz-equivariant map of either type is unique up to a scalar.

## lay
The Lorentz symmetry of spacetime, once complex numbers are allowed, splits into two independent halves. This result shows that the two planes into which the spinor space of the conformal algebra splits are exactly the basic two-component objects of these halves, one plane for each, and that together they rebuild the spacetime directions. It also shows that there is essentially only one symmetric way to combine a spacetime direction with one plane so as to land in the other.

## one-liner
The two planes $\Som$, $\Spi$ of the conformal spinor space are the chiral doublets of the complexified Lorentz algebra, their tensor product is complexified Minkowski space, and each equivariant map from a direction and one plane to the other is unique up to scale.
