---
id: synthesis.infinite-strings-tail-classes-and-no-reading-law-inside-the-algebra
kind: claim
version: 1
title: 'Strings on the infinite tower: tail classes, and no reading law inside the algebra'
status: proved
region: synthesis
subject: tower
tags: [measurement-and-records, superselection, car-algebra, finite-models]
proposed_by:
  kind: ai
  session: 2026-11-12-rung-state
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: idea and direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: session 2026-11-12-rung-state
- name: Claude Opus 5.5
  role: the tail classes and the read-until-decided rule, as candidates raised in review of the earlier results
  source: session 2026-11-12-rung-state
review: draft
about:
- obj.singularity.multi-mode-descent
derivations:
- name: main
  uses:
  - tower.fock-module-one-qubit-per-rung@6
  - tower.ladder-pairs-satisfy-car-vectors@4
  - tower.algebraic-limit-even-charge@3
  - tower.answers-iteration-question@5
  - synthesis.imported-powers-stormer-takesaki-disjointness@3
  - synthesis.state-of-a-new-rung-unique-symmetric-extension-is-the-half-weight@1
  - synthesis.selector-candidates-on-the-tower-integer-states-parity-deterministic-laws@1
  - singularity.p-reduced-metric-level-reading-many@7
  assumes:
  - synthesis.premise-positivity-of-values@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_strings_under_finite_changes_and_under_all_sign_changes
- kind: check
  ref: check.py::check_no_element_connects_strings_that_differ_beyond_its_support
- kind: check
  ref: check.py::check_even_atoms_other_than_strings_also_average_to_the_symmetric_state
- kind: check
  ref: check.py::check_weight_after_a_coupling_is_a_quadratic_form_and_is_not_two_valued
- kind: check
  ref: check.py::check_reading_until_decided_gives_the_prescribed_weight
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - one-relation.record-chain-votes-measurement-without-collapse
  - synthesis.records-of-unbounded-length-on-the-tower-interference-factor-and-limit
extraction:
  note: >-
    Steps 2 and 3 of three approved by Leon on 12 November 2026: are the values of rungs data on the infinite
    tower, and if so what would a law reading them be. Pre-registered before computing
    (colony/runs/2026-11-12-rung-state/PREREGISTRATION-3.md), with the groups named in advance and reported side
    by side, since the earlier finite result had been killed or kept by an unstated choice of group. The answer to
    "datum or label" is therefore given per group in clause (i) and is not one verdict; which group is the right
    notion of symmetry is the maintainer's decision. One item of the pre-registration was mislabelled: 2c was
    marked a test with an open outcome, but the uniform average of any complete family of orthogonal atoms is the
    symmetric state, so its outcome was fixed; the only content of clause (iii) is that even atoms other than
    strings exist, and what the store says about preferring the occupation context. Clauses (i), (ii), (iv), (v)
    are proofs with sanity checks on finite floors; nothing about the infinite tower is computed. Clause (iv) is a
    standard linearity argument (the weight of a test is a quadratic form in the state), written so as not to use
    continuity, which is not available over the rationals. Clause (v) is the classical comparison of a string of
    unbiased values with the binary digits of the target weight (from memory: von Neumann; Knuth and Yao). The
    Reading lists what a selector would need and adopts none of it. Transport-absent. Not done: any dynamics on
    the tower; the question whether automorphisms that change infinitely many rungs are implemented in a given
    representation (they are not, by the Shale and Stinespring criterion, cited from memory and not used).
---

## formal
Let $A$ be the algebraic limit of the tower, the Clifford algebra over $\Q$ of the orthogonal sum of hyperbolic planes $H_{1} \perp H_{2} \perp \cdots$, in which every element involves finitely many generators (Theorem \claimref{tower.algebraic-limit-even-charge}); $v_{j}$, $w_{j}$, $\mathrm{on}_{j}$, $\mathrm{off}_{j}$ as in Proposition \claimref{tower.ladder-pairs-satisfy-car-vectors}, states under Premise (P) (Premise \claimref{synthesis.premise-positivity-of-values}). For an infinite string $s \in \{0,1\}^{\mathbb{N}}$ the \emph{string state} $\omega_{s}$ is the state with $\omega_{s}(x) = \langle s_{\le n}, x\,s_{\le n}\rangle$ in the Fock module of the first $n$ rungs (Theorem \claimref{tower.fock-module-one-qubit-per-rung}) for any $n$ beyond the rungs $x$ involves. Three groups of automorphisms of $A$ commuting with $\dagger$: $G_{1}$, the sign changes of finitely many generators; $G_{2}$, the conjugations by even or odd unitaries of a finite floor; $G_{3}$, the sign changes of an arbitrary set of generators, finite or infinite.
\begin{enumerate}
\item[(i)] \emph{(Classes of strings, per group.)} Under $G_{1}$ and under $G_{2}$, $\omega_{t}$ is in the orbit of $\omega_{s}$ if and only if $s$ and $t$ differ at finitely many rungs: the classes are the tail classes, of which there are uncountably many. Under $G_{3}$ all string states are one orbit. $G_{3}$ is the product over all rungs of the symmetries of the step of Theorem \claimref{synthesis.state-of-a-new-rung-unique-symmetric-extension-is-the-half-weight}, and $G_{1}$ is the subgroup acting on finitely many rungs.
\item[(ii)] \emph{(No element connects two tail classes.)} If $s$ and $t$ differ at a rung that $x \in A$ does not involve, then $\langle t_{\le n}, x\,s_{\le n}\rangle = 0$ for every $n$ at or beyond that rung. So if $s$ and $t$ differ at infinitely many rungs, no element of $A$ has a nonzero value between them. In the completed algebra $\omega_{s}$ and $\omega_{t}$ are then disjoint (clauses (a) and (d) of Fact \claimref{synthesis.imported-powers-stormer-takesaki-disjointness}; argued from the import).
\item[(iii)] \emph{(The symmetric state does not single out the strings.)} On each finite floor the symmetric state (the iterated invariant extension of Theorem \claimref{synthesis.state-of-a-new-rung-unique-symmetric-extension-is-the-half-weight}(ii)) is the uniform average of the string states, and equally of any complete family of pairwise orthogonal atoms; on two rungs the four elements $\tfrac12 yy^{\dagger}$, $y = (1 \pm v_{1}v_{2})P_{0}$ and $y = (v_{1} \pm v_{2})P_{0}$, are even atoms, pairwise orthogonal with sum $1$, none a string. The multi-mode descent (Definition \claimref{obj.singularity.multi-mode-descent}) sends each of them to an equal mixture of two strings. The store takes the occupation-diagonal algebra as the level of records only on a stated choice between two assemblies, not decided there (Proposition \claimref{singularity.p-reduced-metric-level-reading-many}).
\item[(iv)] \emph{(No reading law inside the algebra.)} Let the system have two alternatives $\phi_{0}$, $\phi_{1}$, let the remaining rungs be in a fixed string state, or a fixed vector state of a finite floor (the data), and for $\psi = a\phi_{0} + b\phi_{1}$, $a, b \in \Q$, $a^{2} + b^{2} = 1$, let $\omega_{\psi}$ be the joint state. For every $y \in A$ the value $q(a, b) = \omega_{\psi}(y)$ is a quadratic form in $(a, b)$. If $q(a, b) \in \{0, 1\}$ for all such $(a, b)$, then $q$ is constant. Hence: a rule that reads fixed data and declares the outcome by the value of an element of the algebra (in particular the weight of any test after any unitary of a finite floor, or after any automorphism of $A$, or a pointwise limit of such) cannot give a definite outcome whose odds depend on the state of the system. A selector with the weights of (P) is not such a rule.
\item[(v)] \emph{(What a rule outside the algebra can do with unbiased values.)} Let $d_{1}d_{2}\cdots$ be the binary digits of a rational $p \in (0, 1)$, and let $b_{1}, b_{2}, \ldots$ be independent unbiased values. Stopping at the first $k$ with $b_{k} \ne d_{k}$ and declaring the first outcome when $b_{k} < d_{k}$ gives the first outcome with probability exactly $p$; the number of values read exceeds $k$ with probability $2^{-k}$ and has mean $2$. For $p = \tfrac{9}{25}$ the digits have period $20$, and no rule reading a bounded number of values gives $\tfrac{9}{25}$.
\end{enumerate}
\emph{Reading (argued, not proved).} On the infinite tower the tail class of a string is a label that nothing acting on finitely many rungs can change and no element of the algebra can connect to another: in that sense, and for the groups $G_{1}$, $G_{2}$, it is a datum, an infinite one. Under $G_{3}$ it is a label exchanged by symmetries, as the single values were on a finite tower. A tail class fixes no individual value, since values at finitely many rungs can be changed within it. A selector of outcomes on the tower would need: (1) that the occupation context is the level of facts and that one string is actual, for which (iii) gives the store's conditional support and nothing forcing it; (2) a rule that is not the value of any element, by (iv), so a law of a different kind from the framework's own, which (v) shows can be fed by unbiased values; (3) an order in which rungs are read, where the stored account has no clock on the tower and places the rungs beyond the first away from the physical region (Proposition \claimref{tower.answers-iteration-question}). None of the three is adopted here, and the list of candidates of Theorem \claimref{synthesis.selector-candidates-on-the-tower-integer-states-parity-deterministic-laws} is extended, not closed.

## technical
On the infinite tower a string of on and off values for all the rungs defines a state. Whether two strings are "the same up to relabelling" depends on which symmetries are allowed, and the three natural choices are reported side by side. If only changes on finitely many rungs count, two strings are equivalent exactly when they differ in finitely many places, and there are uncountably many classes; no element of the algebra connects two classes, and in the completed algebra their states are disjoint. If sign changes on infinitely many rungs at once also count, which is what one gets by applying the single step's symmetry at every step, all strings are equivalent. The symmetric state is an even mixture of all strings, but also of other complete families of sharp even states, so it does not single out strings; the store's preference for the occupation records is conditional on a stated choice.

A rule that reads fixed data and gives a definite outcome with odds depending on the system's state cannot be expressed by the value of any element of the algebra after any dynamics of the algebra: such a value is a quadratic form in the state, and a quadratic form taking only the values 0 and 1 on all rational unit vectors is constant. A rule outside the algebra can do it: comparing a string of unbiased values with the binary digits of the target weight gives that weight exactly, reading two values on average. So a selector needs an actual string, a rule of a different kind from the framework's dynamics, and an order of reading; the stored account of the tower supplies none of the three.

## lay
Imagine the framework's switches going on for ever, each one on or off. If you are only allowed to change finitely many switches, two patterns that differ in infinitely many places can never be turned into one another, and nothing the framework can measure connects them: in that sense the pattern, taken as a whole, is a real piece of information. If you are also allowed to flip infinitely many switches at once, any pattern can be turned into any other, and it is only a label. Which of these is the right notion of "the same" is a choice, and this result reports both. Even granting that the pattern is real, it cannot decide the results of measurements through anything the framework's own mathematics can express: every such quantity changes smoothly with the system being measured, whereas a definite result has to jump. A rule from outside could do it, by reading fresh switches one by one until the result is decided, and it would give the right odds exactly. But that needs three things the framework does not have: a reason one pattern is the real one, a rule of a new kind, and an order in which switches are read.

## one-liner
On the algebraic infinite tower, string states fall into tail classes under changes on finitely many rungs (uncountably many, connected by no element) and into one orbit under sign changes of arbitrary sets of generators; the symmetric state does not single out strings; the value of any element is a quadratic form in the system's state, so no rule inside the algebra reading fixed data selects with state-dependent odds; a rule outside it reading unbiased values until decided gives $\tfrac{9}{25}$ exactly.
