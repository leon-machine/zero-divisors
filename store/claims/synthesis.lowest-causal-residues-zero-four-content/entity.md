---
id: synthesis.lowest-causal-residues-zero-four-content
kind: claim
version: 1
title: 'Mass content of the lowest causal signatures at residues 0 and 4'
status: proved
region: synthesis
subject: dark-matter
tags: [towers-by-residue, dark-tower-premises]
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
  - dark-tower-matter.where-mass-begins@2
  - dark-tower-matter.constituents-field@2
  - dark-matter.imported-eight-towers-mod-8-clock@4
  - dark-matter.towers-are-residues-single-clock-filter@5
  - dark-matter.unit-ball-rule@5
  assumes:
  - dark-tower-matter.h1-momentum@1
  proof: proof-main.tex
about:
- obj.dark-tower-matter.ideals-fields-momentum
checked_by:
- kind: check
  ref: check.py::check_lowest_causal_residues_zero_four_content
- kind: proof
  derivation: main
extraction:
  open_problem: op.window-p3
  note: >-
    Content test of the window question. P3 agrees with the lowest causal signature at the six
    residues other than 0 and 4, where it picks the non-causal (2,2) and (4,0) or (0,4) against the
    causal (1,1) and (1,5) or (5,1). This applies T14c's own constituent definitions at those two
    causal signatures. Part (i) uses the (1,1) ascent (transport-essential for the floor count);
    parts (ii) and (iii) are Clifford-algebra content (transport-absent). The use of H1 in
    dimensions two and six extends that premise beyond the dimensions three to five it is stated
    for; this is declared, not derived.
---

## formal
Use the constituent definitions of Definition \claimref{obj.dark-tower-matter.ideals-fields-momentum}, with the momentum of Premise \claimref{dark-tower-matter.h1-momentum} read in dimensions two and six as it is read in dimensions three and five, and in dimension six take $f = \tfrac{1}{4}(1 + e_{t}e_{a})(1 \pm I)$, $I$ the pseudoscalar of $V$, a primitive idempotent of $\Cl^{0}(V)$ for either sign.
\begin{enumerate}
\item[(i)] \emph{(Floors; proved.)} Along a tower of $(1,1)$ ascents over a definite ground $(m,0)$ or $(0,m)$, $\min(p,q)$ rises by one per floor, so the tower has exactly one causal floor, $(m+1,1)$ or $(1,m+1)$, while residue and Morita class are constant along it (Fact \claimref{dark-matter.imported-eight-towers-mod-8-clock}). The causal signatures of residue $r$ are therefore one per tower, of dimension $m + 2$ with $m \equiv r$ or $m \equiv -r \pmod 8$, and the lowest has dimension $\min(r, 8-r) + 2$. A rule reading only data constant along towers cannot choose among them; the causal filter chooses the floor, and the remaining choice is the tower.
\item[(ii)] \emph{(Residue 0; computed, exact.)} At $(1,1)$, the lowest causal signature of residue $0$, $\Cl^{0}(V) \cong \R \oplus \R$, the spinor ideal $S$ is one-dimensional with field $\R$, and $j(\lambda f) = \lambda^{2} j(f)$ with $j(f)$ null. Every total momentum of constituents from $S$ is null: no number of constituents is massive. The single ideal is one of two chiralities: $\Cl^{0}(V)$ has two non-isomorphic simple modules, and $f = \tfrac12(1 + e_{t}e_{a})$ picks one by the orientation of $e_{a}$, a choice that is not canonical in dimension two (in dimensions three to five all such ideals are isomorphic). The complementary ideal $\Cl^{0}(V)(1-f)$ carries the opposite null ray, and one constituent from each ideal has $m^{2} = 1$: with both chiralities admitted, mass begins at two constituents at $(1,1)$ as well. The emptiness of residue $0$ is therefore a consequence of the single-ideal definition, not of the algebra alone.
\item[(iii)] \emph{(Residue 4; computed, exact.)} At $(1,5)$ and at $(5,1)$, for either sign of the chiral factor, $S$ has real dimension $8$ and field $\HH$, $Q(j(\psi)) = 0$ identically on $S$, and two constituents are massive ($m^{2} = \tfrac{1}{4}$ on two basis elements): mass begins at two constituents, as in dimensions three and four (Theorem \claimref{dark-tower-matter.where-mass-begins}(i)).
\item[(iv)] \emph{(The window; computed.)} Under the lowest-causal choice and the single-ideal definition, the absence of massive matter in residue $0$ follows from (ii); in residue $4$ it does not follow from content. Under R1 to R3 (Proposition \claimref{dark-matter.unit-ball-rule}) a populated tower of space dimension five adds $V_{3}/V_{5} = 5/(2\pi)$, giving $\tfrac{11}{3} + \tfrac{47}{6\pi}$, between $6.160$ and $6.161$, about $12$ standard errors above the observed $5.364 \pm 0.065$. The unit-ball value is a fit (Proposition \claimref{dark-matter.status-rule}: the relation was found by solving for the observed value, and its clauses were chosen with it known), and the emptiness of residue $4$ is one of the clauses that fit needs. Premise \claimref{dark-matter.p3-nearest-dimension-representatives} secures this by representing residue $4$ by the definite $(4,0)$ or $(0,4)$, a non-causal signature; no content result secures it at the causal $(1,5)$ or $(5,1)$.
\end{enumerate}

## technical
Apply T14c's own definitions of constituents, spinor ideal and momentum, under Premise H1 extended to dimensions two and six, at the lowest causal signatures of the two residues where Premise P3 departs from the lowest causal choice. Along a tower of $(1,1)$ ascents exactly one floor is causal, so within a residue the causal signatures are one per tower and the open choice is which tower. At $(1,1)$ (residue $0$) the even algebra splits as $\R \oplus \R$, the spinor ideal is one-dimensional and every momentum lies on one null ray, so constituents of one ideal never combine to a massive composite; the ideal is one of two chiralities, fixed by the orientation of a space direction, and one constituent of each chirality is massive. At $(1,5)$ and $(5,1)$ (residue $4$) the ideal is eight-dimensional over $\HH$, single momenta are null and pairs are massive: mass begins at two, as in this world. So under the lowest-causal choice residue $0$'s emptiness follows from the single-chirality definition and residue $4$'s does not follow from content. If R1 to R3 hold and residue $4$ were populated at dimension six, the unit-ball ratio would be between $6.160$ and $6.161$, about $12$ standard errors above the observed $5.364 \pm 0.065$; the unit-ball value is a fit, and it needs residue $4$ empty, which P3 supplies by choosing the non-causal $(4,0)$.

## lay
The dark-matter paper assigns each of eight families of possible worlds one representative signature, and its premise P3 makes two of those choices differently from the simplest rule (take the smallest signature with exactly one time direction). This result tests the two disputed families with the series' own description of matter, under the series' assumption about how a constituent's momentum is defined. In the two-dimensional world of one family, the paper's definition admits constituents of one handedness only; these can only move at light speed in one direction, so they never bind into anything with mass. Constituents of both handednesses together would bind, so this family is empty of massive matter because of that one-handedness choice, not by the algebra alone. In the six-dimensional world of the other family, constituents bind into massive pairs just as in ours. So content does not empty that second family; if it held matter in the proportions the paper uses, the predicted dark-to-visible ratio would be about 6.16 instead of the observed 5.36. The paper's match therefore depends on a premise that keeps the second family empty.

## one-liner
Under T14c's constituent definitions with H1 extended to dimensions two and six, the lowest causal member $(1,1)$ of residue 0 holds no massive composite of one spinor ideal (a chirality choice; both ideals together are massive), while $(1,5)$ and $(5,1)$ of residue 4 have mass from two constituents, so under R1 to R3 the unit-ball fit ($5.364$, against about $6.16$ with residue 4 populated) needs residue 4 empty by premise.
