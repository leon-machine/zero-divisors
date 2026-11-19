---
id: synthesis.invariant-forms-on-spinor-ideal-factor-through-reversion
kind: claim
version: 1
title: 'Invariant forms on a spinor ideal factor through reversion'
status: proved
region: synthesis
subject: dark-matter
tags: [towers-by-residue, dark-tower-premises, chirality, pseudoscalar-and-centre]
proposed_by:
  kind: ai
  session: 2026-10-31-all-open
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
  - synthesis.reversion-pairing-vanishes-residues-zero-four@1
  - synthesis.lowest-causal-residues-zero-four-content@2
  - dark-tower-matter.where-mass-begins@2
  proof: proof-main.tex
about:
- obj.dark-tower-matter.ideals-fields-momentum
checked_by:
- kind: check
  ref: check.py::check_invariant_forms_factor_through_reversion
- kind: check
  ref: check.py::check_general_proof_ingredients
- kind: check
  ref: check.py::check_symmetry_types_give_mass_thresholds
- kind: proof
  derivation: main
extraction:
  open_problem: op.window-p3
  note: >-
    Answers the second attack line of op.window-p3 (can the pairing reading of mass be derived
    from what a field mass term needs) in the following sense: a field mass term is a
    spin-invariant bilinear form in the field, and every such form on a spinor ideal is a linear
    functional of the reversion pairing, for every nondegenerate signature, so the pairing reading
    is the reading "mass needs an invariant pairing" with no choice of pairing left. The field
    theory fact that a single chirality has no mass term in dimensions 2 mod 4 is recovered with an
    own Clifford proof. Clifford structure, transport-absent. The reading of mass itself (pairing
    against momentum) remains the costed clause; this result removes only the freedom in which
    pairing, and shows the series' own thresholds (two, two, one at dimensions three, four, five)
    are read off the symmetry type of the invariant forms.
---

## formal
Let $V$ have nondegenerate signature $(p,q)$, $n = p + q$, and let $f$, $f'$ be idempotents of $\Cl^{0}(V)$ with left ideals $S = \Cl^{0}(V)f$ and $S' = \Cl^{0}(V)f'$, on which the spin Lie algebra acts by left multiplication by bivectors. Call a real bilinear form $B : S \times S' \to \R$ \emph{invariant} if $B(b\psi, \phi) + B(\psi, b\phi) = 0$ for every bivector $b$.
\begin{enumerate}
\item[(i)] \emph{(Every dimension and every nondegenerate signature $(p,q)$; proved.)} $B$ is invariant if and only if
\[
B(\psi, \phi) \;=\; B\bigl(f, \rev{\psi}\phi\bigr) \qquad \text{for all } \psi \in S,\ \phi \in S',
\]
that is, if and only if $B$ is a linear functional of the reversion pairing $\rev{\psi}\phi \in S'$; and every linear functional of the reversion pairing is invariant. So the invariant forms on $S \times S'$ vanish identically exactly when $\rev{\psi}\phi = 0$ for all $\psi \in S$, $\phi \in S'$.
\item[(ii)] \emph{(Every dimension; proved.)} At a causal signature of residue $0$ or $4$ ($n \equiv 2 \pmod 4$, $\omega^{2} = +1$), every invariant form on an ideal of one chirality vanishes identically, and so does every invariant form between any number of copies of that ideal; between the two chiralities invariant forms exist. At every other causal residue the spinor ideal of Definition \claimref{obj.dark-tower-matter.ideals-fields-momentum} carries a nonzero invariant form. Hence with one spinor ideal per tower no mass term exists at residues $0$ and $4$ in any dimension: no derivative-free spin-invariant bilinear in the field, of Dirac or Majorana type, real or complex.
\item[(iii)] \emph{(Computed, exact.)} At the nine causal signatures of dimensions two to six (both chiralities in dimensions two and six) the invariant forms on $S \times S$ have dimension $0$ at $(1,1)$, $(1,5)$, $(5,1)$, $1$ at $(1,2)$, $(2,1)$, $2$ at $(1,3)$, $(3,1)$ and $4$ at $(1,4)$, $(4,1)$, and in each case they are spanned by the blade components of $\rev{\psi}\phi$; on $S_{+} \times S_{-}$ the dimension is $1$ at $(1,1)$ and $4$ at $(1,5)$, $(5,1)$. At $n = 3, 4$ every invariant form is alternating; at $n = 5$ the space has a basis of one symmetric and three alternating forms.
\item[(iv)] \emph{(Computed, exact.)} The least number of constituents of one ideal carrying a nonzero invariant pairing is one when some invariant form is not alternating, two when all are alternating and some is nonzero, and none when there is no invariant form. By (iii) it is two, two and one at $n = 3, 4, 5$, the thresholds of Theorem \claimref{dark-tower-matter.where-mass-begins}, and none at $n = 2$ and $6$.
\end{enumerate}
Consequently the pairing reading of mass in dimensions $n \equiv 2 \pmod 4$ (the costed clause of Observation \claimref{dark-matter.status-rule}(vi), resting on Proposition \claimref{synthesis.reversion-pairing-vanishes-residues-zero-four}) is not a choice among pairings: it is the reading that mass is carried by an invariant pairing of constituents, as in T14c's mass laws and in a field mass term, and under it one ideal at residues $0$ and $4$ carries no mass in any dimension. The only alternative left is the momentum reading, which assigns an invariant mass to pairs of quanta that individually have no mass term. Which of the two readings of mass the series takes remains the clause; which pairing is no longer open.

## technical
A mass term for a field is a quadratic expression in the field, without derivatives, that every rotation and boost leaves unchanged: a spin-invariant bilinear form on the spinor ideal. Invariance under the bivectors propagates to the whole even subalgebra, since products of bivectors span it, in the form $B(a\psi, \phi) = B(\psi, \rev{a}\phi)$. Writing $\psi = af$ and using the idempotent twice gives $B(\psi, \phi) = B(f, \rev{\psi}\phi)$: every invariant form is read off the reversion pairing, and the reversion pairing is the only one there is. At residues $0$ and $4$ the reversion pairing vanishes on one chirality in every dimension, so no invariant form survives there, and a single chiral ideal, or any number of copies of it, has no mass term of any kind; the two chiralities together do pair. Exact computation at the nine lowest causal signatures confirms the factorisation and shows that the symmetry type of the invariant forms (alternating in dimensions three and four, with a symmetric member in five) reproduces the series' thresholds for where mass begins.

## lay
For a particle to have mass, the equations describing it need a term that pairs the particle's field with itself in a way that looks the same to every observer. This result shows that for the building blocks the dark-matter papers use, all such pairings are versions of a single one, the pairing the series already uses for mass. In the two families of hidden worlds that the dark-matter count needs to be empty, that pairing is identically zero in every dimension, so a world built from one kind of building block can have no mass term at all there. What remained a choice of pairing is now no choice; what remains open is only whether mass must come from a pairing at all.

## one-liner
Every spin-invariant bilinear form on a spinor ideal is $B(\psi, \phi) = B(f, \rev{\psi}\phi)$, a linear functional of the reversion pairing, for every nondegenerate signature $(p,q)$; so at residues $0$ and $4$ a single chiral ideal has no mass term of any kind, and the series' mass thresholds at dimensions three to five are read off the symmetry type of the invariant forms.
