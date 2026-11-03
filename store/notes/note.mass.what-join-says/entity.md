---
id: note.mass.what-join-says
kind: note
version: 3
title: What the join says
status: remark
subject: mass
proposed_by:
  kind: extraction
  session: notes-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T11, deposited version
comments_on:
- mass.weight-composite
- mass.mass-weight-dictionary
- obj.mass.grip-mass-composite
- mass.exact-join
locators:
  paper: T11
  number: Rem 5.10
  label: rem:join
  line: 818
extraction:
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  correction:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Three readings of one number became two (the grip and the difference of Casimirs): by mass.casimir-form-join v4 the field-side de Sitter mass -H^2 C_2(I_Lambda^perp) differs from the grip by H^2 C_2(Lambda^2 CS), so it is not a third reading of the same number. Version 1 -> 2.'
---

## formal
Two readings of one number, the first of them a definition, and beside them a field-side number that differs from it. On the composite side, the momentum is the grip on the frozen point, $P = M(I_{\Lambda})$, and mass is its length (Definition \claimref{obj.mass.grip-mass-composite}, a definition; Theorem \claimref{mass.exact-join} is the closed form of that length). On the representation side, that squared length is $Q(I)$ times the difference between the conformal Casimir and the de Sitter Casimir (Proposition \claimref{mass.casimir-form-join}): the part of the composite's conformal charge that the frozen point breaks. On the field side, mass is a weight read against the frozen point (Theorem \claimref{mass.mass-weight-dictionary}), and the composite's squared de Sitter mass is $-H^{2}C_{2}(I_{\Lambda}^{\perp})$, with $H^{2} = Q(I_{\Lambda}) = \Lambda/3$; it differs from the squared grip $Q(P)$ by $H^{2}C_{2}(\Lambda^{2}\CS)$, and the two agree only where the conformal Casimir vanishes. The flat-space formula is the leading term of \eqref{eq:grip}, and the correction is one term, $\tfrac{\Lambda}{3}C$, with $C$ the internal $\mathfrak{su}(2)$ Casimir of the pair: it depends on the constituents only through the imbalance of their helicities and their Hermitian overlap, and it vanishes exactly when the Gram matrix is scalar. The massless composites, for $\Lambda > 0$, are exactly those with $B_{\Lambda} = 0$ and scalar Gram matrix, a locus that is neither empty nor the doubled locus (Theorem \claimref{mass.exact-join}(5)), so compositeness by itself sets no lower bound on mass; the families paper has since settled the question this remark left open, fixing the bracket by the join and identifying the condensation seed as the source term, the $\Lambda$-linear tilt of the mass functional, rather than as a point of the massless locus \cite[Props.~4.1-4.2]{ButlerT13}. The point-supported evaluation, $B_{\Lambda} = \sigma(x)\br{\pi^{1}\pi^{2}}$, is the point of contact with the classical picture: for a composite localised at $x$ the deformed bracket is the flat one rescaled by the de Sitter conformal factor, which is what a conformally invariant pairing must do. Finally, the join fixes the units of Remark \claimref{note.mass.what-dictionary-does-does-not-yield}: the imaginary weight of a composite with $|B_{\Lambda}| \gg H\sqrt{C}$ is $\sqrt{2}|B_{\Lambda}|/H$ at leading order, the symplectic area of the misalignment in Hubble units.

## technical
pending

## lay
pending

## one-liner
pending
