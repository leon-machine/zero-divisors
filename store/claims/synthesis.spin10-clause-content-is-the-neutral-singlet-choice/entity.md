---
id: synthesis.spin10-clause-content-is-the-neutral-singlet-choice
kind: claim
version: 2
title: 'The Spin(10) clause''s content is the choice of neutral singlet'
status: proved
region: synthesis
subject: standard-model
tags: [hypotheses-s-r-c, spinor-modules, hypercharge-and-anomalies, car-algebra]
proposed_by:
  kind: ai
  session: 2026-10-24-all-open
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
  - standard-model.hyp-s-slot-statistics@9
  - synthesis.cpt-closure-forces-slot-module-and-chirality@1
  - standard-model.imported-fock-representation-clifford-algebra-bogoliubov@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_commutants_of_the_three_symmetries
- kind: check
  ref: check.py::check_halvings_fixed_by_each_symmetry
- kind: check
  ref: check.py::check_controls
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.cpt-closure-forces-slot-module-and-chirality
  - standard-model.slot-module-hypothesis
extraction:
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Version 2, wording only: the clause analysed here is the Spin(10) form (version 2 of the slot-module premise) and its grading form (version 3); version 4 restates it as commuting with the Pati-Salam algebra of the chain, equivalent for an anomaly-free halving by synthesis.neutral-singlet-bit-decided-by-gauge-algebra-leaving-u5 (iii). The formal statement now refers to the Spin(10) and grading forms as the earlier versions of the clause. Mathematics unchanged.'
  open_problem: op.hypothesis-s
  note: >-
    The problem's first line of attack (the chirality as the volume element of the five-mode Clifford
    algebra, commuting with Spin(10)) and its closing instruction (record which clauses remain
    premises). The stored check of Hypothesis (S) already shows that the Spin(10) commutant is the two
    parities and that the volume element is the parity; what is added is the ladder below it, computed
    exactly: the gauge algebra alone leaves 32 sign patterns and a continuous choice of lines in the
    neutral block; the number-conserving bilinears u(5) of the joint Clifford system (the total mode
    number alone does the same for the final count) make the block diagonal, so the neutral line is
    the empty or the full state, 8 halvings; the stored anomaly result
    cuts the charged signs to the overall label, 4 halvings; Spin(10), through the creation brackets
    a_i* a_j*, which connect the vacuum to degree two, cuts to 2. So the whole content of the Spin(10)
    clause of the slot-module premise, beyond the gauge symmetry, the joint Clifford system's number
    conservation and anomaly freedom, is one binary choice: whether the sterile singlet of the particle
    half is the empty five-mode state or the full one. It is equivalent to requiring the ten Majorana
    generators of the joint Clifford system to be odd for the chirality (the chirality is the grading of
    the Clifford system), which is the form in which the clause reads as structure rather than as a
    group requirement; neither form is derivable from the others (the vacuum-swapped halving is an
    exact counter-model to every clause but this one, and it is unitarily equivalent to the
    chosen one by a gauge-commuting swap, so no gauge quantum number decides). The ladder
    counts are computed from the operators (components, weights, u(5) and so(10) orbits), not
    enumerated by hand. Recorded as a remaining premise, in its sharpest
    form. Transport-absent in content (finite Clifford algebra); the module is the series'. No
    literature needed beyond the stored Facts.
---

## formal
Let $V = \Lambda^{\bullet}(\C^{2} \oplus W) = \Lambda^{\bullet}\C^{5}$ be the five-mode module of Theorem \claimref{standard-model.hyp-s-slot-statistics}(ii), modes $1, 2$ the slots and $3, 4, 5$ the pairs, $N$ the total mode number, with the gauge algebra $\mathfrak{s}(\uu(2) \oplus \uu(3))$ acting by the bilinears of each block and $Y = (3n - 2k)/6$; let $\uu(5)$ be the span of all number-conserving bilinears $a^{\dagger}_{i}a_{j}$ and $\so(10)$ that of all bilinears, including $a_{i}a_{j}$ and $a^{\dagger}_{i}a^{\dagger}_{j}$, generating the $\Spin(10)$ of clause (v) there (Fact \claimref{standard-model.imported-fock-representation-clifford-algebra-bogoliubov}); let $\gamma_{1}, \dots, \gamma_{10}$ be the Majorana generators. A CPT halving is as in Theorem \claimref{synthesis.cpt-closure-forces-slot-module-and-chirality}: an involution $\Gamma$ commuting with the gauge algebra whose $-1$ eigenspace is isomorphic to the conjugate of its $+1$ eigenspace. The neutral block is the span of the empty state $\Omega$ and the full state $\Omega^{\top} = a^{\dagger}_{1}\cdots a^{\dagger}_{5}\Omega$, the two copies of $(1,1)_{0}$.
\begin{enumerate}
\item[(i)] \emph{(Commutants.)} The commutant of the gauge algebra on $V$ has dimension $14$ ($10$ multiplicity-one components and the full $2 \times 2$ algebra of the neutral block; the charged weight spaces are one-dimensional), that of $\uu(5)$ dimension $6$ (one projector per degree), that of $\so(10)$ dimension $2$ (the two parity projectors), and that of the $\gamma_{p}$ dimension $1$; $\gamma_{1}\cdots\gamma_{10} = -(-1)^{N}$.
\item[(ii)] \emph{(The ladder of halvings.)} The CPT halvings commuting with the gauge algebra are: a sign on each of the five conjugate pairs of charged components ($32$ patterns), together with any pair of complementary lines in the neutral block, one in each half. Those commuting also with $\uu(5)$ have the signs constant on each degree and the neutral lines equal to $\C\Omega$ and $\C\Omega^{\top}$ in either order: $8$ halvings (commuting with the total mode number $N$ alone already forces the neutral lines to be $\C\Omega$ and $\C\Omega^{\top}$, and after anomaly freedom gives the same four below; only the intermediate count $8$ needs $\uu(5)$). With the chirality of Theorem \claimref{synthesis.cpt-closure-forces-slot-module-and-chirality}(4) on the charged components (anomaly freedom), $4$ remain: the overall label, and whether $\Omega$ or $\Omega^{\top}$ lies in the particle half. The two choices are unitarily equivalent: the swap $S$ of $\Omega$ and $\Omega^{\top}$, the identity elsewhere, is an involution commuting with the gauge algebra, and the vacuum-swapped halving is $S(-1)^{N}S$; so no gauge quantum number sees the difference, and only the $\so(10)$ pair operators, which $S$ does not commute with, do. Those commuting with $\so(10)$ are exactly $\pm(-1)^{N}$: the vacuum-swapped halving (even charged components with $\Omega^{\top}$ against odd ones with $\Omega$) commutes with $\uu(5)$, is anomaly-free, and fails on the creation bracket $a^{\dagger}_{1}a^{\dagger}_{2}$.
\item[(iii)] \emph{(The clause as a grading.)} $\Gamma = \pm(-1)^{N}$ are exactly the involutions of $V$ for which every $\gamma_{p}$ is odd, $\Gamma\gamma_{p}\Gamma = -\gamma_{p}$, that is, the gradings of the joint Clifford system; for the vacuum-swapped halving some $\gamma_{p}$ is not odd. Hence the $\Spin(10)$ form of the chirality clause of the slot-module premise (its version 2) is equivalent to the grading form (its version 3): the chirality is the grading of the joint Clifford system of clause (f); and the clause's content beyond the gauge symmetry, number conservation and anomaly freedom is the single choice of $\Omega$ rather than $\Omega^{\top}$ as the particle half's neutral singlet. It is not derivable from those: the vacuum-swapped halving satisfies all of them. (The current version of the premise states the clause as commuting with the Pati-Salam algebra of the chain, which for an anomaly-free halving admits the same two halvings $\pm(-1)^{N}$.)
\end{enumerate}

## technical
The composite's state space under Hypothesis (S) is the sixteen-plus-sixteen states of five fermionic modes. Which states count as particles and which as antiparticles is a choice of involution that the premise fixes by asking it to commute with Spin(10). This result measures exactly how much that request does. The stored CPT theorem already gives the chirality on every charged state and leaves a free line in the two-dimensional neutral block; what is added is the cut of that line to two points and its resolution. Gauge symmetry alone allows thirty-two sign choices on the charged states and any split of the two neutral singlet states. Conserving the total mode number forces the split to be the empty state against the full one. The stored anomaly result then fixes all the charged signs. What remains is one bit: does the particle half contain the empty state or the full one. The two answers are carried into each other by swapping the two neutral states, a unitary that commutes with every gauge generator, so nothing with a gauge quantum number can decide it. Spin(10), through its operators that create two modes at once, makes it the empty state, and that is the same as saying that every creation and annihilation operator flips chirality. So the Spin(10) clause is one bit of premise, equivalent to the natural grading of the Clifford system, and cannot be derived from the other clauses.

## lay
In this model each matter particle of one family is a pattern of five occupied or empty slots, and the rule that sorts patterns into particles and antiparticles is assumed, not derived. The result counts what the assumptions actually decide: symmetry and consistency fix everything except one yes-or-no question, whether the completely empty pattern belongs with the particles or with the antiparticles. The remaining assumption decides that one question, and it amounts to saying that filling or emptying a slot always switches a particle to an antiparticle.

## one-liner
On $\Lambda^{\bullet}\C^{5}$ the gauge algebra, $\uu(5)$ and $\so(10)$ have commutants of dimensions $14$, $6$ and $2$; gauge-commuting CPT halvings are $32$ sign patterns times a free pair of neutral lines, $\uu(5)$ (or the total mode number) and anomaly freedom leave four, differing only in whether $\Omega$ or $\Omega^{\top}$ is the particle half's singlet, two choices conjugate under the gauge-commuting swap of the two, and $\Spin(10)$ leaves $\pm(-1)^{N}$, the involutions for which the ten Majoranas are odd: the $\Spin(10)$ clause is that one bit, equivalent to the Clifford grading, and not derivable from the rest.
