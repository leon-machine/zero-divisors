---
id: synthesis.gauge-algebra-by-tower
kind: claim
version: 1
title: One rule for the gauge algebra of every causal tower
status: proved
region: synthesis
subject: dark-matter
tags: [gauge-fields, towers-by-residue, mirror-sector, dark-tower-premises]
proposed_by:
  kind: ai
  session: gauge-table-2026-10-22
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
  - standard-model.gauge-algebra-minimal-massive-composite@4
  - standard-model.four-dimensions-forces-converse@4
  - standard-model.pair-count-dimension@3
  - standard-model.internal-symmetry-ladder@4
  - mass.mass-symplectic-area-two-twistor-formula@3
  - dark-tower-matter.gauge-algebras@5
  - dark-tower-matter.where-mass-begins@2
  - dark-tower-matter.constituents-field@2
  - dark-tower-matter.pairs@3
  - dark-tower-matter.ladder@2
  - dark-tower-matter.third-pairs-unit-five-dimensions@4
  - dark-tower-matter.mirror-algebra@4
  assumes:
  - dark-tower-matter.h2-identification@1
  - dark-tower-matter.u-transposition-rule@2
  - dark-tower-matter.h1-momentum@1
  proof: proof-main.tex
supports:
- dark-matter.mirror-tower-copy-one@8
checked_by:
- kind: check
  ref: check.py::test_gauge_algebra_by_tower
- kind: proof
  derivation: main
extraction:
  note: >-
    Synthesis found by a scan of the graph: T12 Thm 4.1 and T14c Thm 5.1 apply
    one construction (the automorphism algebra of the minimal massive hierarchy)
    and the store had no link between them. This result states the common rule
    with T14c's inputs, tabulates all six causal towers, shows that the
    four-dimensional row is T12's theorem and that the mirror row equals it (the
    copy theorem, recorded as a supports link rather than a premise, so that P1,
    P2, P3 and (S) do not enter its holds-given set). The field column F (T14c
    Thm 3.2) and the hierarchy's scalars K are kept apart: they differ in the
    five-dimensional towers. The mirror's agreement rests on U1; the full-module
    commutant (T14 Thm 3.4's ground type, a different object) would break it.
---

## formal
Assume H2 (Premise \claimref{dark-tower-matter.h2-identification}) and Premise U (\claimref{dark-tower-matter.u-transposition-rule}), and in dimensions three and five H1 (\claimref{dark-tower-matter.h1-momentum}). For a causal tower of residue $r = p - q \bmod 8$, signature $(p,q)$, dimension $n = p + q$ and conformal space $\hatV$ of signature $(p+1, q+1)$, let
\begin{itemize}
\item $F$ be the field of its constituents (Theorem \claimref{dark-tower-matter.constituents-field});
\item $a$ be the number of constituents at which mass begins (Theorem \claimref{dark-tower-matter.where-mass-begins}): $a = 2$ for $n = 3, 4$ and $a = 1$ for $n = 5$;
\item $b$ be the number of ladder pairs of a constituent, the complex Witt index $\lfloor (n+2)/2 \rfloor$ of $\hatV$ (Proposition \claimref{dark-tower-matter.pairs});
\item $K$ be the scalars of the pairs: $\R$ when the real Witt index of $\hatV$, which is $2$ in every causal tower, equals $b$; otherwise the centraliser in $F$ of the unit $u \in F$ that builds the last pair, which is $\mathrm{span}\{1, u\} \cong \C$ both for $F = \C$ and for $F = \HH$ (Theorem \claimref{dark-tower-matter.third-pairs-unit-five-dimensions}).
\end{itemize}
The hierarchy is $K^{a} \otimes_{K} K^{b}$. Its automorphisms are the maps $A \otimes B$ with $A$, $B$ in the isometry groups of the standard forms over $K$, $O$ over $\R$ and $U$ over $\C$ (Theorem \claimref{dark-tower-matter.ladder}, its $Sp(1)$ at $n = 5$ cut to the $K$-linear circle as in Theorem \claimref{dark-tower-matter.gauge-algebras}(ii), and U2), modulo the kernel $\{(\lambda, \lambda^{-1})\}$ of unit scalars of $K$; its automorphism algebra $\mathfrak{g}_{r}$ has dimension $\tfrac12 a(a-1) + \tfrac12 b(b-1)$ over $\R$ and $a^{2} + b^{2} - 1$ over $\C$. The six causal towers give:
\begin{center}\small
\begin{tabular}{@{}cccccccll@{}}
\toprule
$r$ & $(p,q)$ & $n$ & $F$ & $K$ & $a$ & $b$ & hierarchy & $\mathfrak{g}_{r}$, $\dim$ \\
\midrule
$6$ & $(1,3)$ & $4$ & $\C$ & $\C$ & $2$ & $3$ & $\C^{2} \otimes \C^{3}$ & $\su(2) \oplus \su(3) \oplus \uu(1)$, $12$ \\
$2$ & $(3,1)$ & $4$ & $\C$ & $\C$ & $2$ & $3$ & $\C^{2} \otimes \C^{3}$ & $\su(2) \oplus \su(3) \oplus \uu(1)$, $12$ \\
$1$ & $(2,1)$ & $3$ & $\R$ & $\R$ & $2$ & $2$ & $\R^{2} \otimes \R^{2}$ & $\so(2) \oplus \so(2)$, $2$ \\
$7$ & $(1,2)$ & $3$ & $\R$ & $\R$ & $2$ & $2$ & $\R^{2} \otimes \R^{2}$ & $\so(2) \oplus \so(2)$, $2$ \\
$3$ & $(4,1)$ & $5$ & $\HH$ & $\C$ & $1$ & $3$ & $\C^{1} \otimes \C^{3}$ & $\uu(3) = \su(3) \oplus \uu(1)$, $9$ \\
$5$ & $(1,4)$ & $5$ & $\HH$ & $\C$ & $1$ & $3$ & $\C^{1} \otimes \C^{3}$ & $\uu(3) = \su(3) \oplus \uu(1)$, $9$ \\
\bottomrule
\end{tabular}
\end{center}
\begin{enumerate}
\item[(i)] The row $r = 6$ is Theorem \claimref{standard-model.gauge-algebra-minimal-massive-composite}. In dimension four the rule's inputs are T12's: two constituents (Theorem \claimref{dark-tower-matter.where-mass-begins}(i), which is T11's two-constituent formula, Proposition \claimref{mass.mass-symplectic-area-two-twistor-formula}, in the even algebra), three pairs (Lemma \claimref{standard-model.pair-count-dimension}) over $\C$, and the slot group $U(2)$ (Proposition \claimref{standard-model.internal-symmetry-ladder}). The rule therefore returns $\C^{2} \otimes \C^{3}$ and the Standard Model algebra, of dimension $12$; at three constituents it returns T12's seventeen-dimensional $\su(3) \oplus \su(3) \oplus \uu(1)$; and no other row is the Standard Model algebra, by Proposition \claimref{standard-model.four-dimensions-forces-converse}(2) for the complex rows and by dimension for the real ones.
\item[(ii)] The row $r = 2$, the mirror, equals the row $r = 6$: in both signatures the centre of the even conformal algebra is $\mathrm{span}\{1, I_{6}\}$ with $I_{6}^{2} = -1$, the even algebras are isomorphic (Theorem \claimref{dark-tower-matter.mirror-algebra}), and $F$, $a$, $b$, $K$ coincide. This agrees with the mirror copy theorem's gauge algebra (Theorem \claimref{dark-matter.mirror-tower-copy-one}(i)). The agreement rests on U1: read with the commutant of the full Clifford module, $\HH$ for $(1,3)$ and $\R$ for $(3,1)$, the two rows would differ.
\item[(iii)] The rows $r = 1, 7, 3, 5$ are Theorem \claimref{dark-tower-matter.gauge-algebras}(i) and (ii).
\item[(iv)] The field $F$ is not the hierarchy's scalars: in the five-dimensional towers $F = \HH$ and $K = \C$, the slot algebra $\mathfrak{sp}(1)$ of the single constituent being cut, once U3 places $u$ in $F$, to the circle that commutes with the pair algebra.
\end{enumerate}
The column $\mathfrak{g}_{r}$ is exact linear algebra on the hierarchy; the hierarchy column rests on U (and on H1 in dimensions three and five); reading $\mathfrak{g}_{r}$ as the tower's gauge algebra is H2.

## technical
T12 and T14c compute a gauge algebra the same way: take the smallest composite that can have mass, write it as a two-level hierarchy $K^{a} \otimes K^{b}$ (constituent slots tensor pair slots), and take the Lie algebra of the maps $A \otimes B$ that preserve both levels and the positive norm, modulo the common scalars. Assuming, as T14c does, that this algebra is the gauge algebra (premise H2) and that the construction transposes by its rule U (with the momentum premise H1 in dimensions three and five), the three inputs are where mass begins ($a$), how many ladder pairs a constituent carries ($b$, the complex Witt index of the conformal space) and which scalars the pairs carry ($K$: the reals when the real ladder pairs already suffice, otherwise the circle that the pair unit generates inside the constituents' field). With T14c's inputs the rule gives, in the six causal towers: $\C^{2} \otimes \C^{3}$ and $\su(2) \oplus \su(3) \oplus \uu(1)$ (dimension $12$) in this tower and its mirror; $\R^{2} \otimes \R^{2}$ and $\so(2) \oplus \so(2)$ (dimension $2$) in the three-dimensional towers; $\C^{1} \otimes \C^{3}$ and $\uu(3)$ (dimension $9$) in the five-dimensional towers.

In four dimensions T14c's inputs coincide with T12's (two constituents from T11's mass formula, three complex pairs, the unitary ladder), so the rule reproduces T12's theorem, including its seventeen-dimensional control at three constituents. The mirror's row is the same, as the mirror copy theorem requires; this agreement depends on taking the constituents' field from the even conformal ideal (where it is $\C$ in both signatures), not from the full Clifford module (quaternionic for ours, real for the mirror's). In five dimensions the constituents' field is the quaternions but the hierarchy's scalars are complex: the rule's $K$ is not the field. The check recomputes the onset count, the field, the real pairs and every automorphism algebra in exact arithmetic, and confirms that a different onset count, pair count or field gives a different algebra.

## lay
The Standard-Model paper found our forces as the symmetries of the smallest composite that can have mass: two constituents, each with three internal slots, with complex numbers as scalars. The dark-matter note applied the same recipe to the other worlds of the series. This result writes the recipe down once and runs it in all six worlds that can hold matter, under the note's premises that the recipe gives the forces and that it carries over to other worlds in one stated way. In our world it gives back exactly the Standard Model's forces, as it must. In the mirror world it gives the same forces, as the series' mirror theorem says, but only because the recipe reads the scalars from the right part of the algebra. In the three-dimensional worlds it gives two independent forces like electromagnetism; in the five-dimensional worlds a colour force and one charge.

## one-liner
One rule (the automorphisms of the minimal massive hierarchy $K^{a} \otimes K^{b}$) gives $\su(2) \oplus \su(3) \oplus \uu(1)$ in this tower and the mirror, $\so(2) \oplus \so(2)$ in the three-dimensional towers and $\uu(3)$ in the five-dimensional ones; its four-dimensional row is T12's theorem and its mirror row the copy theorem's, under H2 and U (and H1 in dimensions three and five).
