---
id: synthesis.slot-covariance-forces-gram-square
kind: claim
version: 2
title: For face forms sesquilinear in the face vector, slot-mixing covariance and the face-wise diagonal force the Gram square, which the permutations alone do not
status: proved
region: synthesis
subject: generations
tags: [flavour-and-mixing, mass-generation]
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
derivations:
- name: main
  uses:
  - synthesis.many-twistor-join@2
  - standard-model.internal-symmetry-ladder@3
  - families.chart-computation-sign-twist-bracket-form@5
  assumes:
  - families.slot-covariance-of-mass-law@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_face_vector_cofactor
- kind: check
  ref: check.py::check_invariant_forms
- kind: check
  ref: check.py::check_gram_square_on_configurations
- kind: check
  ref: check.py::check_lambda_obstruction
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - families.alignment-computed-thirteenth-refutation-democracy-one
  - families.skeleton-rank-one-plus-ordering-shift
extraction:
  open_problem: op.gram-square-and-face-space
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: Version 2 adds an assumes edge to the new postulate families.slot-covariance-of-mass-law (Leon's decision to adopt slot-U(3) covariance of the family mass law as a premise), the hypothesis that does the work here, and names it at every level; the mathematics is unchanged.
  note: 'Successor problem (2) of the families paper asks to derive that the full three-family form is the square of a face-space map. This result derives it from stated structure: the face vector of the three-spinor join transforms under the slot mixing U(3) of the internal-symmetry ladder by the cofactor law, Schur''s lemma leaves two covariant sesquilinear forms, and the face-wise diagonal (each face''s own two-spinor bracket term) selects the Gram square. The hypothesis that does the work is covariance of the mass law under the full slot U(3), equivalently under the internal U(2) of every pair of slots (the three pairwise U(2) generate U(3)); the permutations alone leave a nine-dimensional freedom, including the face-wise diagonal form, which is positive and gives three degenerate families at the democratic point. Whether the slot U(3) constrains the mass law is a premise to decide, not settled here. The derivation is exact at Lambda = 0 and for the bracket part at any Lambda; for Lambda not zero the faces'' Casimir terms are not the diagonal of any covariant form built from the join''s ingredients, by the non-invariant excess (Lambda/12) sum_i h_ii^2. The face identification (families.hyp-face-identification) is not used: the result is about forms on face space, and reading the form as the family Yukawa form is that hypothesis''s reading. Not addressed: the order-one-angle argument the successor problem mentions, the real structure (see synthesis.coherent-face-vector-real-slices) and the strong dressing. The uniqueness is standard representation theory (transport-absent); the inputs, the frozen point''s pairing with the face bivectors and the slot group of the ladder, are the series'' objects.'
---

## formal
Let $Z^{1}, Z^{2}, Z^{3} \in \CS$ be a three-spinor composite with the conventions of Theorem \claimref{synthesis.many-twistor-join}: $B^{il}_{\Lambda} = \ip{I_{\Lambda}}{Z^{i} \wedge Z^{l}}$ and the Gram matrix $h$. Call $\beta_{k} := B^{ij}_{\Lambda}$, $(i, j)$ the cyclic successors of $k$, the face vector, and let the slot mixing $Z^{i} \mapsto \sum_{j} Z^{j}U_{ji}$, $U \in U(3)$, be the internal group of the three-spinor system (Proposition \claimref{standard-model.internal-symmetry-ladder}). A face form is a Hermitian matrix $M(Z)$ on face space; it is covariant if $M(Z \cdot U) = \overline{R_{U}}\,M(Z)\,R_{U}^{\mathsf T}$ for all $U$, with $R_{U}$ as in (i).
\begin{enumerate}
\item[(i)] \emph{(The cofactor law.)} $\beta \mapsto R_{U}\beta$ with $R_{U} = \det(U)\,U^{-1}$, and $h \mapsto U^{\dagger}hU$; $U \mapsto R_{U}$ maps $U(3)$ onto $U(3)$, and on permutations it is the sign-twisted action $\Omega \mapsto \pm P\Omega$ of Proposition \claimref{families.chart-computation-sign-twist-bracket-form}(1).
\item[(ii)] \emph{(The Gram square, forced.)} The covariant face forms $M_{kl} = \sum_{m,n} A_{kl}^{mn}\,\bar\beta_{m}\beta_{n}$ with constant coefficients are exactly $a\,\bar\beta\beta^{\mathsf T} + b\,|\beta|^{2}\,\mathbb{1}$. Exactly one of them has the face-wise diagonal $M_{kk} = 2|\beta_{k}|^{2}$, each face's own two-spinor bracket term:
\[
M \;=\; 2\,\bar\beta\,\beta^{\mathsf T},
\]
the Gram square of the face map $Z \mapsto \beta(Z)$. Its trace is the bracket part of the three-spinor join, $\tr M = 2\sum_{i<l}|B^{il}_{\Lambda}|^{2} = m^{2} - \tfrac{\Lambda}{3}C_{3}$, and in every configuration it is positive semidefinite of rank at most one, with spectrum $(2|\beta|^{2}, 0, 0)$ and eigenvector $\bar\beta$.
\item[(iii)] \emph{(The permutations alone do not force it.)} The permutation-covariant face forms with constant coefficients and face-wise diagonal $M_{kk} = 2|\beta_{k}|^{2}$, covariant under the sign-twisted permutations only, form a nine-dimensional complex affine space (the Gram square plus the nine-dimensional space of covariant zero-diagonal tensors). It contains the face-wise form $2\operatorname{diag}(|\beta_{k}|^{2})$, positive semidefinite, of rank three for generic $\beta$ and with three degenerate families at the democratic direction, and the forms $2\bar\beta\beta^{\mathsf T} + c\,(\J - \mathbb{1})|\beta|^{2}$, indefinite for every real $c \neq 0$.
\item[(iv)] \emph{(The cosmological term.)} The faces' full two-spinor joins sum to the composite's,
\[
\sum_{k}\Bigl(2|\beta_{k}|^{2} + \tfrac{\Lambda}{3}\,C(h_{k})\Bigr) \;=\; m^{2} + \tfrac{\Lambda}{12}\sum_{i} h_{ii}^{2},
\]
with $h_{k}$ the $2 \times 2$ block of face $k$, and for $\Lambda \neq 0$ no covariant face form in the span of $\bar\beta\beta^{\mathsf T}$, $|\beta|^{2}\mathbb{1}$, $\bar h^{2}$, $(\tr h)\bar h$, $\tr(h^{2})\mathbb{1}$, $(\tr h)^{2}\mathbb{1}$ has these joins as its diagonal.
\end{enumerate}
So, for a family form sesquilinear in the face vector with constant coefficients and with the face-wise diagonal, covariance of the mass law under the slot $U(3)$, which is Premise \claimref{families.slot-covariance-of-mass-law}, makes it the Gram square of the face vector, exactly at $\Lambda = 0$ and for the bracket part at any $\Lambda$, and classically one family is massive in every configuration.

## technical
In a three-spinor composite, the frozen point's pairing with the three two-spinor faces gives a face vector $\beta$ whose components are the faces' mass brackets. Under the slot mixing $U(3)$ of the internal-symmetry ladder, $\beta$ transforms by the cofactor law $\beta \mapsto \det(U)U^{-1}\beta$, which on permutations is the families paper's sign-twisted action. By Schur's lemma the covariant Hermitian forms on face space that are sesquilinear in $\beta$ form a two-parameter family, $a\,\bar\beta\beta^{\mathsf T} + b\,|\beta|^{2}\mathbb{1}$, and requiring each diagonal entry to be that face's own two-spinor mass term $2|\beta_{k}|^{2}$ fixes $a = 2$, $b = 0$: the family form is the Gram square $2\bar\beta\beta^{\mathsf T}$, whose trace is the bracket part of the three-spinor join and which has rank one in every configuration.

The content of the Gram-square property comes from the sesquilinear-in-$\beta$ ansatz: every positive semidefinite form is a Gram matrix of some map, and what is derived here is that it is the rank-one square of the face map itself (the point raised in the light-cone result filed alongside, synthesis.light-cone-koide-is-quarter-turn). The permutations alone do not force this: the permutation-covariant forms with the face-wise diagonal form a nine-dimensional affine space, including the purely face-wise form $2\operatorname{diag}(|\beta_{k}|^{2})$, positive and with three equal families at the democratic point, so it is the continuous slot symmetry, equivalently the internal $U(2)$ of every pair of slots, that selects the Gram square. That symmetry of the mass law is assumed, as the premise of slot covariance (a flavour symmetry of the law broken by the state), and the Gram square holds under it. At $\Lambda \neq 0$ the faces' Casimir terms add up to the composite's plus $(\Lambda/12)\sum_{i}h_{ii}^{2}$, which is not $U(3)$ invariant, and no covariant form built from the join's ingredients has the faces' full joins on its diagonal.

## lay
The families paper explains why one generation of matter is much heavier than the other two by assuming that the table of family masses has a special "square" form, which automatically leaves room for only one heavy family. This result derives that form instead of assuming it. In a three-part composite, each pair of parts carries a mass, and the parts can be mixed among themselves by a continuous symmetry. If the rule that assigns masses is built directly from the pairs' masses and respects that symmetry, which is assumed here as a premise, there are only two candidate mass tables, and requiring each pair's own mass to appear on the diagonal leaves exactly the square form. Swapping the parts around, without continuous mixing, would not be enough: it also allows a table in which the three families are equally heavy. A small correction from the cosmological constant does not fit the symmetric rule.

## one-liner
For a family form sesquilinear in the face vector $\beta$ with constant coefficients and face-wise diagonal $2|\beta_{k}|^{2}$, covariance under the three-spinor slot mixing $U(3)$ (under which $\beta$ transforms by the cofactor law), assumed as the premise of slot covariance, forces the Gram square $2\bar\beta\beta^{\mathsf T}$ (exact at $\Lambda = 0$, rank one), while the permutations alone leave a nine-dimensional affine freedom including a face-wise form with three equal families.
