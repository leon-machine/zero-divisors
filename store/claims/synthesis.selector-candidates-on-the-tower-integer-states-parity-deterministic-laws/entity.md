---
id: synthesis.selector-candidates-on-the-tower-integer-states-parity-deterministic-laws
kind: claim
version: 1
title: 'Candidates for a selector of outcomes on the tower: four examined, none selects'
status: proved
region: synthesis
subject: tower
tags: [measurement-and-records, superselection, grading-and-parity, finite-models]
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
review: draft
derivations:
- name: main
  uses:
  - tower.ladder-pairs-satisfy-car-vectors@4
  - synthesis.set-and-clear-of-a-bit-generate-the-hyperbolic-plane@1
  - synthesis.integer-clifford-algebras-contain-no-switch@1
  - synthesis.records-keep-even-states-even-only-for-parity-homogeneous-observables@1
  - synthesis.state-of-a-new-rung-unique-symmetric-extension-is-the-half-weight@1
  assumes:
  - synthesis.premise-positivity-of-values@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_integer_states_of_one_rung_in_the_two_integer_forms
- kind: check
  ref: check.py::check_parity_gives_two_sectors_and_no_record_superselection
- kind: check
  ref: check.py::check_no_deterministic_law_on_strings
- kind: check
  ref: check.py::check_unread_rungs_carry_the_uniform_weight
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - one-relation.record-chain-votes-measurement-without-collapse
  - one-relation.recorded-sectors-superselected-premise
  - one-relation.imported-indifference-instrument
  - descent-lift.imported-descent-modes-univalence-supplied-class
extraction:
  note: >-
    Asked for by Leon on 12 November 2026 after the rung-state result: look for other ideas, from the graph or not,
    that could give a mechanism for the collapse of the wave function, and say so if there is none. A mechanism has
    to end interference between outcomes and select one. Four candidates were pre-registered with kill conditions
    before computing (colony/runs/2026-11-12-rung-state/PREREGISTRATION-2.md): integer states, parity sectors as
    record sectors, a deterministic law on an actual string, and unread rungs as a supply of bits. Predicted before
    computing: the first three killed, the fourth available only as new premises. Outcome: as predicted. This is a
    survey with exact computations, not a no-go theorem: it covers the four candidates named and finite towers, and
    a candidate not listed is not excluded. Clause (iv) describes what a selector would cost; whether to adopt such
    premises is the maintainer's decision, and nothing here recommends it. Literature named in the Reading (Bell's
    beables for fermion number, 1984; Ghirardi, Rimini and Weber, 1986; Diosi and Penrose; Vink, 1993) is cited
    from memory and is not a premise of any clause. Transport-absent: the algebra is standard. Not done: the
    infinite tower, where disjoint representations could give more sectors than the two of clause (ii); laboratory
    recording; any statement about weights other than those computed.
---

## formal
Notation as in Theorem \claimref{synthesis.state-of-a-new-rung-unique-symmetric-extension-is-the-half-weight}: $\Cl_{\Q}(\ell,\ell)$ with generators $e_{j}$, $f_{j}$, ladder pairs $v_{j}$, $w_{j}$ (Proposition \claimref{tower.ladder-pairs-satisfy-car-vectors}), tests $\mathrm{on}_{j} = v_{j}w_{j}$, $\mathrm{off}_{j} = w_{j}v_{j}$ (Theorem \claimref{synthesis.set-and-clear-of-a-bit-generate-the-hyperbolic-plane}), strings $P_{s}$, states under Premise (P) (Premise \claimref{synthesis.premise-positivity-of-values}). An element is \emph{even} if it is a sum of blades of even grade; a state is even if it vanishes on odd elements. A \emph{selector} would have to (a) end interference between the outcomes of a measurement and (b) single out one of them. Four candidates:
\begin{enumerate}
\item[(i)] \emph{(Integer states give definiteness only by removing superposition.)} On one rung, the states under (P) with integer values on the blades $1, e, f, fe$ (the ladder's integer form, Theorem \claimref{synthesis.integer-clifford-algebras-contain-no-switch}) are exactly five: on, off, the state of weight $\tfrac12$ vanishing on $e$, $f$, $fe$, and the two states with $\omega(e) = \pm 1$; their weights on the on test are $0$, $1$, $\tfrac12$, $\tfrac12$, $\tfrac12$. The states with integer values on $1, v, w, vw$ (the switch's integer form) are exactly two: on and off. On $m$ rungs, a state with integer values on all products of the $v_{j}$, $w_{j}$ is the state of one string. So in the switch form every state is definite and none has a weight strictly between $0$ and $1$ on any test $P_{s}$ or on any $e_{j}$: definiteness holds, interference is absent altogether, and nothing is selected.
\item[(ii)] \emph{(Parity gives two sectors and does not separate records.)} The centre of the even subalgebra of $\Cl_{\Q}(2,2)$ is spanned by $1$ and the volume element $\Gamma$: two sectors. For the even state on four rungs given by $y = (\tfrac35 v_{1} + \tfrac45 v_{2})\,v_{3}\,P_{0}$ ($P_{0}$ the all-off string) and the even unitary $U = \mathrm{off}_{1} + \mathrm{on}_{1}X$, with $X$ the even self-adjoint element exchanging a quantum between rungs $3$ and $4$, the two records (quantum on rung $4$, quantum on rung $3$) have weights $\tfrac{9}{25}$ and $\tfrac{16}{25}$ and are perfectly correlated with the system's rung; both lie in the same sector of $\Gamma$ and of the total number; and the even self-adjoint element $O = v_{1}w_{2}v_{4}w_{3} + \text{adjoint}$ has value $\tfrac{24}{25}$ in the state after $U$ and $0$ in the state with the interference between the records removed. A coupling that writes the record on a single rung, $U' = \mathrm{off}_{1} + \mathrm{on}_{1}e_{3}$, is unitary, is neither even nor odd, and sends an even state to a state that is not even (compare Theorem \claimref{synthesis.records-keep-even-states-even-only-for-parity-homogeneous-observables}).
\item[(iii)] \emph{(No deterministic law on strings.)} On two rungs there is an even rotor $R$ ($R\tilde{R} = RR^{\dagger} = 1$) that takes the state of the string $(1,0)$ to a state with weights $\tfrac{9}{25}$ on $(1,0)$ and $\tfrac{16}{25}$ on $(0,1)$. A map from strings to strings takes a string of weight $1$ to a string of weight $1$. So no rule that assigns to each string one later string reproduces the weights of (P) under even rotors: a law for an actual string on a fixed finite set of rungs is stochastic, or draws on data outside those rungs.
\item[(iv)] \emph{(Unread rungs carry the uniform weight.)} In the one symmetric extension of Theorem \claimref{synthesis.state-of-a-new-rung-unique-symmetric-extension-is-the-half-weight}(ii), applied twice, each of the four strings of the two new rungs has weight $\tfrac14$, and in general $2^{-k}$ on $k$ new rungs. By clause (iii) of that theorem the strings are labels: no stored premise makes one of them actual.
\end{enumerate}
\emph{Reading (argued, not proved).} None of the four is a selector. (i) gives (b) for free only where (a) is trivial. (ii) shows the one exact superselection rule of a finite tower cannot do (a) for an allowed record; it does not bear on (b). (iii) and (iv) together say what a selector on the tower would be: a premise that one string is actual, and a law reading unread rungs, for which (iv) supplies an unbiased prior and nothing else. Those two premises are a theory of the kind of Bell's beables for fermion number; they would make each rung's value a datum, an unbounded list against the short count of free data in Proposition \claimref{one-relation.record-chain-votes-measurement-without-collapse}, and they would depend on the split of (P), which is not preserved by boosts. They are not adopted here. Stochastic collapse and gravitational collapse are further premises of other kinds, not examined beyond naming them.

## technical
A mechanism for collapse has two jobs: stop the outcomes interfering, and pick one. Four ideas were tried on finite towers, each with a kill condition written first. Requiring whole-number values makes every state a definite string when the integer form is the switch's, but only because nothing else is left: there is no superposition to collapse, and the ladder's integer form keeps three weights, 0, 1/2 and 1. Parity is the one exact superselection rule of a finite tower, with two sectors; a record written by an allowed (even) coupling leaves both outcomes in the same sector and an even observable still sees their interference in full, while a coupling that would put the outcomes in different sectors is not allowed. A deterministic rule for an actual string cannot reproduce the weights, since a rotor spreads one string over two. And the unread rungs of the earlier result give every string the same weight, an unbiased prior with no actual value behind it.

So the stored content holds no selector. One could be added as two premises (a string is actual; a law reads fresh rungs), and the cost is stated: an unbounded list of data and dependence on a split that boosts change. The result is a survey of named candidates on finite towers, conditional on (P); it is not a proof that no mechanism can exist.

## lay
For a quantum measurement to give one result, something has to stop the possible results from interfering and something has to choose one of them. This result tries four ideas for where the framework might already contain such a chooser, assuming its rule that averages are never negative. If only whole-number values are allowed, every state is definite, but only because all the in-between states have been thrown away, which also throws away interference that experiments see. The framework's one exact barrier between kinds of states, parity, has just two sides, and a measurement of the allowed kind leaves both results on the same side, still able to interfere. A fixed rule that moves one definite pattern of switches to another cannot give the right odds. And the fresh switches added by the framework's construction arrive as fair coins with no face showing. So the framework as it stands contains no chooser. One could be added by assuming that one pattern of switches is real and that fresh switches are read as they arrive, but that is a new assumption with a stated cost, and this result does not make it.

## one-liner
Under (P), on finite towers, four candidates for a selector of outcomes fail: integer states are definite only where superposition is absent (two states per rung in the switch form, five in the ladder form); parity has two sectors and an even record coupling leaves interference $\tfrac{24}{25}$ visible; an even rotor spreads one string to weights $\tfrac{9}{25}$, $\tfrac{16}{25}$, so no deterministic law on strings; unread rungs carry the uniform weight with no actual value; a selector would be two new premises.
