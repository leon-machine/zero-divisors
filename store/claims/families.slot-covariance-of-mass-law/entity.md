---
id: families.slot-covariance-of-mass-law
kind: claim
version: 1
title: 'Slot covariance of the family mass law: a flavour symmetry of the law, broken by the state'
status: postulate
region: families
subject: generations
tags: [flavour-and-mixing, mass-generation, face-identification]
proposed_by:
  kind: ai
  session: maintainer-2026-10-22
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
lineage:
  motivated_by:
  - synthesis.slot-covariance-forces-gram-square
  - families.hyp-face-identification
extraction:
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: New postulate, adopted by Leon's decision to take slot-U(3) covariance of the family mass law as a premise. It was the hypothesis that does the work in synthesis.slot-covariance-forces-gram-square, stated there inside the theorem; that result now assumes it.
---

## formal
\emph{Premise (slot covariance).} Let $Z = (Z^{1}, Z^{2}, Z^{3})$ be a three-spinor composite, $\beta(Z)$ its face vector and $M(Z)$ the family mass law, the Hermitian form on face space that the families paper reads as the family Yukawa form (Hypothesis \claimref{families.hyp-face-identification}). The law is covariant under the full slot mixing $U(3)$ of the three-spinor system (Proposition \claimref{standard-model.internal-symmetry-ladder}):
\[
M(Z \cdot U) \;=\; \overline{R_{U}}\,M(Z)\,R_{U}^{\mathsf T}, \qquad R_{U} = \det(U)\,U^{-1}, \qquad U \in U(3),
\]
equivalently under the internal $U(2)$ of every pair of slots. It is a flavour symmetry of the law and not of the state: a given composite's face vector is not invariant, and selects the family that carries the mass.

\emph{What it is for.} For a family form sesquilinear in $\beta$ with constant coefficients and the face-wise diagonal $2|\beta_{k}|^{2}$, the premise forces the Gram square $M = 2\bar\beta\beta^{\mathsf T}$, of rank one, exactly at $\Lambda = 0$ and for the bracket part at any $\Lambda$ (Theorem \claimref{synthesis.slot-covariance-forces-gram-square}); covariance under the permutations alone leaves a nine-dimensional affine freedom, including the face-wise form with three equal families at the democratic point.

\emph{Refutation condition.} The premise is false if the family mass law, derived from the composite's structure, is not covariant under the slot $U(3)$, for example if it carries slot-dependent coefficients as the permutation-covariant forms of that theorem's clause (iii) do; the Gram square, and so the premise within the sesquilinear class, is refuted if three nonzero family masses are shown to be needed by the law at $\Lambda = 0$.

## technical
The three conformal spinors of a three-spinor composite can be mixed among themselves by a $U(3)$, under which the face vector, the three pairwise mass brackets, transforms by the cofactor law. The premise is that the rule assigning the family mass table to a composite respects this mixing, as a symmetry of the law; a particular composite's face vector breaks it, and its direction picks out the massive family. Under the premise, a sesquilinear family form whose diagonal entries are the faces' own mass terms must be the rank-one Gram square of the face vector, so classically one family is massive. Without it, with only the permutations of the slots as symmetry, many forms remain, among them one with three equally heavy families. The premise would be refuted by a derivation of the mass law that depends on the slot frame, or by a need for three nonzero masses at tree level with $\Lambda = 0$.

## lay
In this framework's working identification, each family of matter particles corresponds to one pair among the three basic parts of a composite, and the three parts can be continuously mixed into one another. This assumption says that the rule which assigns masses to the families treats all such mixtures alike, even though any actual composite picks out a direction and so breaks that symmetry. With the assumption, the mass table is forced into a form in which only one family is heavy, which is the pattern seen in nature at first approximation. Without it, the rule would also allow three equally heavy families.

## one-liner
Premise: the family mass law is covariant under the slot mixing $U(3)$ of the three-spinor system, a flavour symmetry of the law broken by the state, which forces the rank-one Gram square.
