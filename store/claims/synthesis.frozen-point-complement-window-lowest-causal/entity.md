---
id: synthesis.frozen-point-complement-window-lowest-causal
kind: claim
version: 1
title: 'The frozen point''s complement as window: lowest causal representatives'
status: proved
region: synthesis
subject: dark-matter
tags: [towers-by-residue, dark-tower-premises, premises-p1-p5]
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
  - dark-energy.frozen-point-makes-stelle-west-vector@7
  - std-algebra.sylvester-inertia@1
  - synthesis.residues-zero-four-real-chirality-anomaly@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_complement_signature
- kind: check
  ref: check.py::check_inertia_bound
- kind: check
  ref: check.py::check_window_census
- kind: check
  ref: check.py::check_residue_zero_member
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - dark-matter.p3-nearest-dimension-representatives
  - dark-matter.towers-are-residues-single-clock-filter
  - dark-matter.nesting
extraction:
  open_problem: op.window-p3
  note: >-
    A sharp reformulation of P3, not a derivation from the series' present premises. P1's one frozen
    point I reduces the tractor space R^{2,4} to its complement, of signature (1,4) for a positive
    cosmological constant, which is the residue-5 tower's own signature. The window hypothesis (W),
    that every tower's spacetime is up to overall sign a nondegenerate subspace of that complement
    (the sign freedom is what P2's reversal orbit requires), leaves no choice of representative:
    exactly the lowest causal member of each residue other than 4, and nothing of residue 4, which
    is the window the unit-ball fit needs. (W) was looked for knowing that the window of dimensions
    up to five gives the fit (towers-are-residues-single-clock-filter (iii) lists it), so it is a
    costed alternative to P3, recorded and not adopted as a premise, not a result that makes the ratio a
    prediction. The emptiness of residue 4 also uses the single-clock filter (towers hold matter only at
    causal signatures): (W) alone admits the definite (0,4) and (4,0). The frozen point is not needed for
    the census (iii), since the whole tractor space admits the same causal set; it enters only in (iv). It
    would replace both of P3's clauses and the residue-4 half of the costed single-ideal clause; the
    single-ideal choice at residue 0 remains. Transport-convenient: it uses the frozen point of the
    tractor reduction, not transport itself.
---

## formal
Let $I$ be the frozen point of Premise \claimref{dark-matter.p1-single-frozen-point}, a vector of the tractor space $\R^{2,4}$ with $Q(I) = \Lambda/3$, and $I^{\perp}$ its orthogonal complement (Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector}(i)). Call a tower's spacetime, a quadratic space of signature $(p,q)$, \emph{admitted} if it or its negative is isometric to a nondegenerate subspace of $I^{\perp}$; write (W) for the hypothesis that every populated tower's spacetime is admitted, and (W$_{T}$) for the same with the whole tractor space in place of $I^{\perp}$. A signature is causal if $\min(p,q) = 1$, and (C) is the single-clock filter of Proposition \claimref{dark-matter.towers-are-residues-single-clock-filter}: towers hold matter only at causal signatures. (W) is a candidate premise that restates the window of P3; it was found knowing the window the unit-ball fit needs and is a costed alternative to Premise \claimref{dark-matter.p3-nearest-dimension-representatives}, not a derivation of it.
\begin{enumerate}
\item[(i)] \emph{(The complement; computed, exact.)} $I^{\perp}$ has signature $(1,4)$ if $\Lambda > 0$, $(2,3)$ if $\Lambda < 0$, and is $(1,3)$ plus the radical spanned by $I$ if $\Lambda = 0$. For $\Lambda > 0$ it has residue $1 - 4 \equiv 5 \pmod 8$: the frozen point's complement has the signature of the residue-$5$ tower.
\item[(ii)] \emph{(Admission; proved.)} A nondegenerate $(a,b)$ is isometric to a subspace of a space whose nondegenerate part is $(P,Q)$ if and only if $a \le P$ and $b \le Q$ (Sylvester inertia, Fact \claimref{std-algebra.sylvester-inertia}); it is admitted if and only if this holds for $(a,b)$ or for $(b,a)$. The sign freedom is what Premise \claimref{dark-matter.p2-indifference} requires: it equates residues $r$ and $-r$, and $(p,q) \mapsto (q,p)$ maps the admitted set onto itself.
\item[(iii)] \emph{(The window; proved, exact census.)} For $\Lambda > 0$ the admitted causal signatures are exactly
\[
(1,1),\ (2,1),\ (1,2),\ (3,1),\ (1,3),\ (4,1),\ (1,4),
\]
of residues $0, 1, 7, 2, 6, 3, 5$: one for each residue other than $4$, and that one is the residue's lowest causal member, of dimension $\min(r, 8-r) + 2$. No causal member of residue $4$ is admitted: its lowest, $(1,5)$ and $(5,1)$, has five directions of one sign. Under (W$_{T}$) the admitted causal set is the same for every sign of $\Lambda$. Under (W) and (C) no choice of representative remains, and the lowest-causal clause and the emptiness of residue $4$ both follow, the latter without the pairing reading of mass and without (G6). (W) alone admits the definite $(0,4)$ and $(4,0)$ of residue $4$ (and $(0,2)$, $(2,0)$ and other definite signatures), sterile by (C). Since (W$_{T}$) admits the same causal set, this clause does not need the frozen point.
\item[(iv)] \emph{(A cosmological constant that is not positive.)} For $\Lambda < 0$ and for $\Lambda = 0$ the admitted causal signatures under (W) are $(1,1)$, $(2,1)$, $(1,2)$, $(3,1)$, $(1,3)$: residues $3$ and $5$, the five-dimensional towers, are not admitted. Under (W) the five-dimensional towers exist because $\Lambda > 0$.
\item[(v)] \emph{(Residue $0$.)} The admitted representative of residue $0$ is the causal $(1,1)$, where Premise \claimref{dark-matter.p3-nearest-dimension-representatives} has the two-time $(2,2)$. Given the imported anomaly theorems of Theorem \claimref{synthesis.residues-zero-four-real-chirality-anomaly}(iii), single-ideal matter there has no conserved stress in the one metric's field and cannot source it; with one spinor ideal residue $0$ is therefore empty under (W) as well. What (W) leaves of the costed clause is the choice of a single chiral ideal at $(1,1)$.
\end{enumerate}

## technical
The frozen point of the descent reduces the six-dimensional tractor space of the one metric to its five-dimensional complement, which for a positive cosmological constant has one time and four space directions, the signature of a five-dimensional tower. Suppose every tower's spacetime fits inside that complement as a nondegenerate subspace, up to an overall sign of the metric, which is the freedom the indifference premise needs to treat a tower and its mirror alike. By the inertia theorem a space fits exactly when it has at most one direction of one sign and at most four of the other. Among signatures with a single time this leaves seven: one for each residue except 4, always the residue's lowest causal member, and none of residue 4, whose lowest member needs five directions of one sign. The whole tractor space gives the same seven, so this census does not need the frozen point; it enters only in the statement for a cosmological constant that is not positive. Definite signatures such as $(0,4)$ also fit, and they are excluded by the single-clock filter, which the result uses alongside the hypothesis. So the window premise P3 and the emptiness of residue 4 would follow from one geometric hypothesis with the single-clock filter; the hypothesis restates the window of dimensions up to five, found knowing that the fit needs it, and is a costed alternative to P3, not a derivation; residue 0 is represented by the plane $(1,1)$, where the store's anomaly result already rules out single-ideal matter. With a negative or zero cosmological constant the complement is smaller and the five-dimensional towers would not exist.

## lay
The series sorts its hidden worlds into eight families and has to say how many dimensions each one has; so far it simply picked, for each family, the option closest to our four. This result offers a single geometric reason instead. The moment that froze the universe's structure singles out a five-dimensional space, the same shape as one of the hidden worlds. If every hidden world must fit inside that space, then each family has exactly one possible shape with a single time, the smallest one, except one family, which cannot fit at all, and that is the family the dark-matter count needs to be empty. The reason is new and has to be adopted as an assumption; it was found while knowing which answer the count needs, so it explains the choice rather than predicting the number.

## one-liner
If every tower's spacetime is, up to sign, a nondegenerate subspace of the frozen point's complement in the tractor space, of signature $(1,4)$ for $\Lambda > 0$, then each residue other than $4$ has exactly one causal representative, its lowest, and residue $4$ has no causal one, replacing P3 and the residue-$4$ half of the costed clause by one hypothesis with the single-clock filter; for $\Lambda \le 0$ the five-dimensional towers drop out. (W) restates the window of dimensions up to five, found knowing the fit; it is not a derivation.
