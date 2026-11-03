---
id: standard-model.imported-cauchy-decomposition-exterior-power
kind: claim
version: 1
title: 'Imported: the Cauchy decomposition of an exterior power'
status: imported
region: standard-model
subject: standard-model
tags: [classical-theorem, representation-theory]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T12, deposited version
review: typed
imported_from:
- citation: I. G. Macdonald, Symmetric Functions and Hall Polynomials, second edition, Oxford University
    Press (1995).
  key: Macdonald1995
  locator: I, \S 4, (4.3$'$)
- citation: 'W. Fulton and J. Harris, Representation Theory: A First Course, Graduate Texts in Mathematics
    129, Springer (1991).'
  key: FultonHarris1991
  locator: Ex.~6.11
- citation: 'W. Fulton and J. Harris, Representation Theory: A First Course, Graduate Texts in Mathematics
    129, Springer (1991).'
  key: FultonHarris1991
  locator: \S 6.1, \S 15.3
- citation: 'W. Fulton and J. Harris, Representation Theory: A First Course, Graduate Texts in Mathematics
    129, Springer (1991).'
  key: FultonHarris1991
  locator: App.~B.2
locators:
  paper: T12
  number: Fact 2.6
  label: fact:cauchy
  line: 895
extraction:
  env: fact
  typing:
    by: ai-typing-pass
    note: 'Imported fact; levels only, no edges to review. Levels pass: conditions already kept.'
---

## formal
For finite-dimensional complex vector spaces $A$ and $B$ and every $k$,
\[
\Lambda^{k}(A \otimes B) \;\cong\; \bigoplus_{|\lambda| = k} S_{\lambda}A \otimes S_{\lambda'}B
\]
as $GL(A) \times GL(B)$-modules, the sum over partitions $\lambda$ of $k$ with $\lambda'$ the conjugate partition and $S_{\lambda}$ the Schur functor; $S_{\lambda}A = 0$ when $\lambda$ has more parts than $\dim A$. For $\dim A = 2$: $S_{(1,1)}A = \Lambda^{2}A = \det$, $S_{(2,1)}A \cong A \otimes \det$, $S_{(3)}A = S^{3}A$ of dimension four. For $\dim B = 3$: $\Lambda^{2}B \cong B^{*} \otimes \det$, $S_{(2,1)}B \cong \mathfrak{sl}(B) \otimes \det$, the eight-dimensional adjoint, $S_{(2,2)}B \cong S^{2}B^{*} \otimes \det^{2}$; and in general $\Lambda^{k}B \cong (\Lambda^{n-k}B)^{*} \otimes \det$ for $n = \dim B$, equivalently $(\Lambda^{k}B)^{*} \cong \Lambda^{n-k}B \otimes \det^{-1}$. Under $SU(A) \times SU(B)$ the determinant characters are trivial. For a direct sum, $\Lambda^{n}(A \oplus B) \cong \bigoplus_{j+k=n}\Lambda^{j}A \otimes \Lambda^{k}B$ as $GL(A) \times GL(B)$-modules. \emph{Provenance:} the Cauchy formula is \cite[I, \S 4, (4.3$'$)]{Macdonald1995} and \cite[Ex.~6.11]{FultonHarris1991}; the small identifications are the standard dimension-two and dimension-three cases of \cite[\S 6.1, \S 15.3]{FultonHarris1991}; the direct-sum formula is \cite[App.~B.2]{FultonHarris1991}.

## technical
For finite-dimensional complex spaces $A$ and $B$ the Cauchy formula gives $\Lambda^{k}(A \otimes B) \cong \bigoplus_{|\lambda| = k} S_{\lambda}A \otimes S_{\lambda'}B$ as $GL(A) \times GL(B)$-modules, summed over partitions $\lambda$ of $k$ with conjugate partition $\lambda'$, where $S_{\lambda}A = 0$ if $\lambda$ has more parts than $\dim A$.

The small cases used are explicit: for $\dim A = 2$, $\Lambda^{2}A = \det$, $S_{(2,1)}A \cong A \otimes \det$ and $S^{3}A$ is four-dimensional; for $\dim B = 3$, $\Lambda^{2}B \cong B^{*} \otimes \det$, $S_{(2,1)}B$ is the eight-dimensional adjoint twisted by $\det$, and $S_{(2,2)}B \cong S^{2}B^{*} \otimes \det^{2}$. The determinant characters are trivial under $SU(A) \times SU(B)$, and for direct sums $\Lambda^{n}(A \oplus B) \cong \bigoplus_{j+k=n}\Lambda^{j}A \otimes \Lambda^{k}B$. All of this is imported from standard representation theory.

## lay
This is a standard tool from the theory of symmetry. It says how the fully antisymmetric combinations built from a product of two spaces break up into simpler pieces, each piece pairing a pattern on one space with the mirrored pattern on the other. It comes with a short list of small cases in two and three dimensions that the paper uses repeatedly, and a companion rule for sums of spaces. All of it is taken from the textbook literature.

## one-liner
The exterior powers of $A \otimes B$ decompose as $\bigoplus_{|\lambda| = k} S_{\lambda}A \otimes S_{\lambda'}B$, with explicit cases for dimensions two and three and a direct-sum rule.
