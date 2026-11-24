---
id: synthesis.infinite-strings-tail-classes-and-reading-rules-linear-and-not
kind: claim
version: 1
title: 'Strings on the infinite tower: tail classes, and reading rules linear and not'
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
  role: independent review; the tail classes, the rung permutations, the comparison rule of clause (v) and the read-until-decided rule
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
  - synthesis.records-of-unbounded-length-on-the-tower-interference-factor-and-limit@1
  - singularity.p-reduced-metric-level-reading-many@7
  assumes:
  - synthesis.premise-positivity-of-values@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_strings_under_finite_changes_and_under_all_sign_changes
- kind: check
  ref: check.py::check_rung_permutations_act_on_strings
- kind: check
  ref: check.py::check_no_element_connects_strings_that_differ_beyond_its_support
- kind: check
  ref: check.py::check_even_atoms_other_than_strings_also_average_to_the_symmetric_state
- kind: check
  ref: check.py::check_weight_after_a_coupling_is_a_quadratic_form_and_is_not_two_valued
- kind: check
  ref: check.py::check_comparison_rule_selects_within_two_to_the_minus_n
- kind: check
  ref: check.py::check_reading_until_decided_gives_the_prescribed_weight
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - one-relation.record-chain-votes-measurement-without-collapse
extraction:
  open_problem: op.outcome-selector-premises
  note: >-
    Steps 2 and 3 of three approved by Leon on 12 November 2026: are the values of rungs data on the infinite
    tower, and if so what would a law reading them be. Pre-registered before computing
    (colony/runs/2026-11-12-rung-state/PREREGISTRATION-3.md), with the groups named in advance and reported side
    by side. The answer to "datum or label" is given per group in clause (i) and is not one verdict; which group is
    the right notion of symmetry is the maintainer's decision. One item of the pre-registration was mislabelled:
    2c was marked a test with an open outcome, but the uniform average of any complete family of orthogonal atoms
    is the symmetric state, so its outcome was fixed. Reviewed by an independent referee (Claude Opus 5.5,
    12 November 2026): the formal clauses of the first draft were sound and its title, one-liner, lay level and
    Reading were OVERSTATED. The first draft said there is "no reading law inside the algebra". That is false:
    the lemma of clause (iv) excludes only rules given by the value of one element, that is rules linear in the
    state, and the referee exhibited a rule that selects with the weights of (P) to within 2^-n; it is clause (v) here,
    recomputed. A third pass corrected the description of that rule: it is the sign of the value of one element,
    not a comparison needing two, so the dividing line is between declaring the outcome to be a value (linear in
    the state) and declaring it by the sign of a value (not linear), not inside against outside the algebra, and
    not one element against two. Also added from the review: the rung permutations as a fourth
    group (three orbits with finite changes); that the symmetric state of the infinite tower is disjoint from every
    string state; a fuller list of what a selector would need. The check of clause (iv) cannot fail on its second
    half for any quadratic form, and the checks of (ii) and (iii) restate elementary facts; coverage says so.
    Clause (vi) is the comparison of unbiased values with the binary digits of a target (Knuth and Yao, 1976, from
    memory). Transport-absent. Not done: any dynamics on the tower; whether automorphisms that change infinitely
    many rungs are implemented in a given representation.
---

## formal
Let $A$ be the algebraic limit of the tower, the Clifford algebra over $\Q$ of the orthogonal sum of hyperbolic planes $H_{1} \perp H_{2} \perp \cdots$, in which every element involves finitely many generators (Theorem \claimref{tower.algebraic-limit-even-charge}); $v_{j}$, $w_{j}$, $\mathrm{on}_{j}$, $\mathrm{off}_{j}$ as in Proposition \claimref{tower.ladder-pairs-satisfy-car-vectors}, states under Premise (P) (Premise \claimref{synthesis.premise-positivity-of-values}). For an infinite string $s \in \{0,1\}^{\mathbb{N}}$ the \emph{string state} $\omega_{s}$ is the state with $\omega_{s}(x) = \langle s_{\le n}, x\,s_{\le n}\rangle$ in the Fock module of the first $n$ rungs (Theorem \claimref{tower.fock-module-one-qubit-per-rung}) for any $n$ beyond the rungs $x$ involves. Four groups of automorphisms of $A$ commuting with $\dagger$: $G_{1}$, the sign changes of finitely many generators; $G_{2}$, the conjugations by even or odd unitaries of a finite floor; $G_{3}$, the sign changes of an arbitrary set of generators, finite or infinite; $G_{4}$, the permutations of the rungs ($v_{j} \mapsto v_{\pi(j)}$, $w_{j} \mapsto w_{\pi(j)}$ for a bijection $\pi$ of the rungs).
\begin{enumerate}
\item[(i)] \emph{(Classes of strings, per group.)} Under $G_{1}$ and under $G_{2}$, $\omega_{t}$ is in the orbit of $\omega_{s}$ if and only if $s$ and $t$ differ at finitely many rungs: the classes are the tail classes, of which there are uncountably many. Under $G_{3}$ all string states are one orbit. Under the group generated by $G_{1}$ and $G_{4}$ there are exactly three orbits: strings with finitely many rungs on, with finitely many off, and with infinitely many of each. $G_{3}$ is the product over all rungs of the symmetries of the step of Theorem \claimref{synthesis.state-of-a-new-rung-unique-symmetric-extension-is-the-half-weight}, and $G_{1}$ its subgroup acting on finitely many generators. In every one of these cases each class contains strings with either value at any given rung: no single rung's value is constant on a class.
\item[(ii)] \emph{(No element connects two tail classes.)} If $s$ and $t$ differ at a rung that $x \in A$ does not involve, then $\langle t_{\le n}, x\,s_{\le n}\rangle = 0$ for every $n$ at or beyond that rung. In the completed algebra, argued from clauses (a) and (d) of Fact \claimref{synthesis.imported-powers-stormer-takesaki-disjointness}: $\omega_{s}$ and $\omega_{t}$ are disjoint when $s$ and $t$ differ at infinitely many rungs, and the symmetric state (weight $\tfrac12$ on every rung) is a factor state disjoint from every string state.
\item[(iii)] \emph{(The symmetric state does not single out the strings.)} On each finite floor the symmetric state (the iterated invariant extension of Theorem \claimref{synthesis.state-of-a-new-rung-unique-symmetric-extension-is-the-half-weight}(ii)) is the uniform average of the string states, and equally of any family of pairwise orthogonal atoms with sum $1$; on two rungs, with $P_{0} = \mathrm{off}_{1}\mathrm{off}_{2}$, the four elements $\tfrac12 yy^{\dagger}$, $y = (1 \pm v_{1}v_{2})P_{0}$ and $y = (v_{1} \pm v_{2})P_{0}$, are even atoms, pairwise orthogonal with sum $1$, none a string. The multi-mode descent (Definition \claimref{obj.singularity.multi-mode-descent}) sends each of them to an equal mixture of two strings. The store takes the occupation-diagonal algebra as the level of records only on a stated choice between two assemblies, not decided there (Proposition \claimref{singularity.p-reduced-metric-level-reading-many}).
\item[(iv)] \emph{(No reading rule that is linear in the state.)} Let the system have two alternatives $\phi_{0}$, $\phi_{1}$, let the remaining rungs be in a fixed string state, or a fixed vector state of a finite floor (the data), and for $\psi = a\phi_{0} + b\phi_{1}$, $a, b \in \Q$, $a^{2} + b^{2} = 1$, let $\omega_{\psi}$ be the joint state. For every $y \in A$ the value $q(a, b) = \omega_{\psi}(y)$ is a quadratic form in $(a, b)$. If $q(a, b) \in \{0, 1\}$ for all such $(a, b)$, then $q$ is constant. Hence a rule that reads data distributed independently of the system and declares the outcome by the value of \emph{one} element of the algebra in the joint state (in particular the weight of a test after a unitary of a finite floor, or after an automorphism of $A$, or a pointwise limit of such) cannot give a definite outcome whose odds depend on the state of the system. This excludes the rules whose outcome is the value of an element, which are linear in the state, and no others.
\item[(v)] \emph{(A rule that declares the outcome by the sign of a value selects.)} Let the system be the rungs $1, 2$ with alternatives $\phi_{0} = v_{1}|0\rangle$, $\phi_{1} = v_{2}|0\rangle$, let the data be a string $s$ on $n$ further rungs $d_{1}, \ldots, d_{n}$, and let $Y_{n} = \sum_{k \le n}2^{-k}\,\mathrm{on}_{d_{k}}$. In the joint state, $\omega_{\psi}(Y_{n}) = \sum_{k}2^{-k}s_{k}$ and $\omega_{\psi}(\mathrm{on}_{1}) = a^{2}$. The rule ``first outcome if and only if $\omega_{\psi}(Y_{n}) < \omega_{\psi}(\mathrm{on}_{1})$'' gives a definite outcome for every string, and over the $2^{n}$ strings with equal weight the first outcome has frequency $\lceil 2^{n}a^{2}\rceil/2^{n}$, within $2^{-n}$ of the weight $a^{2}$ of (P). The rule uses only the value of an element of the algebra in the joint state; it is not linear in the state: its outcome is the indicator that the value of the one element $Y_{n} - \mathrm{on}_{1}$ is negative, a step function of that value.
\item[(vi)] \emph{(Reading until decided.)} Let $d_{1}d_{2}\cdots$ be the binary digits of a rational $p \in (0, 1)$, and let $b_{1}, b_{2}, \ldots$ be independent unbiased values. Stopping at the first $k$ with $b_{k} \ne d_{k}$ and declaring the first outcome when $b_{k} < d_{k}$ gives the first outcome with probability exactly $p$; the number of values read exceeds $k$ with probability $2^{-k}$ and has mean $2$. For $p = \tfrac{9}{25}$ the digits have period $20$, and no rule reading a bounded number of values gives $\tfrac{9}{25}$. For $p = a^{2}$ not a dyadic fraction, on every string of $n$ values that this rule has decided it declares the same outcome as the rule of (v), and on the one string it leaves undecided (the first $n$ digits of $a^{2}$) the rule of (v) declares the first outcome.
\end{enumerate}
\emph{Reading (argued, not proved).} On the infinite tower the tail class of a string is a label that nothing acting on finitely many rungs can change and no element of the algebra can connect to another: for the groups $G_{1}$, $G_{2}$ it is a datum, an infinite one; with permutations of the rungs added only three classes remain; under $G_{3}$ it is a label exchanged by symmetries. No single rung's value is a datum in any of the four cases of (i) ($G_{1}$; $G_{2}$; $G_{3}$; $G_{1}$ with $G_{4}$). With complete records the two limiting branch states of Theorem \claimref{synthesis.records-of-unbounded-length-on-the-tower-interference-factor-and-limit} are string states that differ at infinitely many rungs, so the choice of group also decides whether those recorded outcomes are data or labels. By (v) and (vi) a deterministic rule that selects outcomes with the weights of (P) can be written in the framework's own terms, given premises of two kinds, none of them stored. Actuality: that the occupation context is the level of facts and one string is actual, for which (iii) gives the store's conditional support and nothing forcing it, and by (ii), as argued there, a string state is disjoint from the symmetric state of the infinite tower, so reading that state as ignorance of an actual string is a further step; that the string is typical for the uniform weight, that fresh rungs are used for each event, and that they are independent of the system. A law: the rule of (v), which declares the outcome by the sign of a value in which the system's own state enters, and so is a law in which the state guides the outcome, of the pilot-wave kind; and an order in which rungs are read, where the stored account has no clock on the tower and places the rungs beyond the first away from the physical region (Proposition \claimref{tower.answers-iteration-question}). None of this is stored or adopted here, and the candidates of Theorem \claimref{synthesis.selector-candidates-on-the-tower-integer-states-parity-deterministic-laws} are extended, not closed.

## technical
On the infinite tower a string of on and off values for all the rungs defines a state. Whether two strings are "the same up to relabelling" depends on which symmetries are allowed, and four natural choices are reported side by side. If only changes on finitely many rungs count, strings are equivalent exactly when they differ in finitely many places, and there are uncountably many classes; no element of the algebra connects two classes. If the rungs may also be permuted, three classes remain. If sign changes on infinitely many rungs at once count, which is what applying the single step's symmetry at every step gives, all strings are equivalent. In no case is the value of one particular rung fixed by the class. The symmetric state is an even mixture of all strings on each finite floor, but also of other families of sharp even states, and on the infinite tower it is disjoint from every string state (argued from an import).

A rule that reads fixed data and declares the outcome by the value of one element of the algebra cannot give odds that depend on the system's state: such a value is a quadratic form in the state, and a quadratic form taking only the values 0 and 1 on all rational unit vectors is constant. That excludes only rules whose outcome is the value of an element, which are linear in the state. A rule that declares the outcome by the sign of a value can select: reading the data rungs as the binary digits of a number and asking whether it is below the weight of the system's first alternative gives a definite outcome for each string and the right odds to within $2^{-n}$ for $n$ data rungs; read digit by digit, it stops after two rungs on average. Such a rule is not linear in the state: it declares the outcome by the sign of a value, not by the value. So a deterministic selector exists in the framework's terms given an actual, typical string of rung values independent of the system, this comparison law, and an order of reading. None of these is stored.

## lay
Imagine the framework's switches going on for ever, each one on or off. Whether two such patterns count as "really different" depends on what you are allowed to do. If you may change only finitely many switches, patterns that differ in infinitely many places can never be turned into one another, and nothing the framework can measure connects them: the pattern as a whole is then a real piece of information, though the setting of any one switch is not. If you may also shuffle the switches, or flip infinitely many at once, most or all patterns become equivalent. This result reports each case. It then asks whether such a pattern, if real, could decide the results of measurements. It cannot do so if the result is simply the value of one quantity of the framework in the combined state. But a rule that looks only at whether such a value is positive or negative can: treat the fresh switches as the binary digits of a number, and say the first result happens if that number is below the usual odds of the first result. For a typical pattern this gives the right odds, reading two switches on average. So a rule that picks results exists. What it needs is not in the framework: that one pattern is real and typical, that the rule above is a law of nature (a law in which the wave itself steers the result), and an order in which switches are read.

## one-liner
On the algebraic infinite tower, string states form tail classes under changes on finitely many rungs (uncountably many, connected by no element), three classes if rungs may be permuted, and one orbit under sign changes of arbitrary sets of generators; a rule declaring the outcome to be the value of an element (linear in the state) cannot select with state-dependent odds, while the rule declaring it by the sign of the value of $\sum 2^{-k}\mathrm{on}_{d_k} - \mathrm{on}_{1}$ selects with frequency within $2^{-n}$ of $a^{2}$ given an actual typical string; none of its premises is stored.
