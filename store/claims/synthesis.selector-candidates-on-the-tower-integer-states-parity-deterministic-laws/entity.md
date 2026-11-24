---
id: synthesis.selector-candidates-on-the-tower-integer-states-parity-deterministic-laws
kind: claim
version: 1
title: 'Four candidates for a selector of outcomes on finite towers: none selects'
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
- name: Claude Opus 5.5
  role: independent review; the odd homogeneous coupling and the multi-mode descent in clause (ii)
  source: session 2026-11-12-rung-state
review: draft
about:
- obj.singularity.multi-mode-descent
derivations:
- name: main
  uses:
  - tower.ladder-pairs-satisfy-car-vectors@4
  - synthesis.set-and-clear-of-a-bit-generate-the-hyperbolic-plane@1
  - synthesis.integer-clifford-algebras-contain-no-switch@1
  - synthesis.records-keep-even-states-even-only-for-parity-homogeneous-observables@1
  - synthesis.state-of-a-new-rung-unique-symmetric-extension-is-the-half-weight@1
  - tower.answers-iteration-question@5
  assumes:
  - synthesis.premise-positivity-of-values@3
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
- kind: check
  ref: check.py::check_odd_coupling_and_the_stored_descent
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - one-relation.record-chain-votes-measurement-without-collapse
  - one-relation.recorded-sectors-superselected-premise
  - one-relation.imported-indifference-instrument
  - descent-lift.imported-descent-modes-univalence-supplied-class
extraction:
  open_problem: op.outcome-selector-premises
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
    infinite tower; laboratory recording; any statement about weights other than those computed. Reviewed by an
    independent referee (Claude Opus 5.5, 12 November 2026): sound with fixes, applied here (the wording of (i) on
    the e_j; the centre for general n; the odd homogeneous coupling, which is allowed and was wrongly excluded in
    the first draft; the multi-mode descent, which the first draft did not mention; the scope of the conclusion).
    The referee judged the pre-registered tests weak: C1 near-tautological, C2 a test of total parity only and not
    of the stored mode-wise descent, C3 a straw man unless taken with C4, and C4's kill condition a statement about
    the store. The referee's own search added candidates not stored here as results: records of unbounded length on
    the infinite tower (the branches become disjoint in the limit, argued from the stored Powers and Stormer
    criterion, with interference present at every finite stage for an observable touching every record rung), which
    would turn the recorded-sectors premise into a theorem in that limit and selects nothing; tail classes of the
    infinite tower; the descent's corner read-out, which picks a fixed branch and not one with its weight; a
    pseudo-random law seeded by stored data, excluded by the absence of a law and not by the count of data. These
    are in colony/runs/2026-11-12-rung-state/verify/R-opus.md and are not claimed here.
---

## formal
Notation as in Theorem \claimref{synthesis.state-of-a-new-rung-unique-symmetric-extension-is-the-half-weight}: $\Cl_{\Q}(\ell,\ell)$ with generators $e_{j}$, $f_{j}$, ladder pairs $v_{j}$, $w_{j}$ (Proposition \claimref{tower.ladder-pairs-satisfy-car-vectors}), tests $\mathrm{on}_{j} = v_{j}w_{j}$, $\mathrm{off}_{j} = w_{j}v_{j}$ (Theorem \claimref{synthesis.set-and-clear-of-a-bit-generate-the-hyperbolic-plane}), strings $P_{s}$, states under Premise (P) (Premise \claimref{synthesis.premise-positivity-of-values}). An element is \emph{even} if it is a sum of blades of even grade; a state is even if it vanishes on odd elements. A \emph{selector} would have to (a) end interference between the outcomes of a measurement and (b) single out one of them. Four candidates:
\begin{enumerate}
\item[(i)] \emph{(Integer states give definiteness only by removing superposition.)} On one rung, the states under (P) with integer values on the blades $1, e, f, fe$ (the ladder's integer form, Theorem \claimref{synthesis.integer-clifford-algebras-contain-no-switch}) are exactly five: on, off, the state of weight $\tfrac12$ vanishing on $e$, $f$, $fe$, and the two states with $\omega(e) = \pm 1$; their weights on the on test are $0$, $1$, $\tfrac12$, $\tfrac12$, $\tfrac12$. The states with integer values on $1, v, w, vw$ (the switch's integer form) are exactly two: on and off. On $m$ rungs, a state with integer values on all products of the $v_{j}$, $w_{j}$ is the state of one string. So in the switch form every state is definite and none has a value strictly between $0$ and $1$ on any test $P_{s}$, or a nonzero value on any $e_{j}$; the tests $\tfrac12(1 \pm e_{j})$ of the rational algebra, which are not in the switch's integer form, get the weight $\tfrac12$. Definiteness holds inside the integer form, interference is absent there altogether, and nothing is selected.
\item[(ii)] \emph{(Parity gives two sectors and does not separate records; the stored descent ends interference and does not select.)} The centre of the even subalgebra of $\Cl_{\Q}(n,n)$ is spanned by $1$ and the volume element $\Gamma$ (standard; computed here for $n = 2, 3$): two sectors. A unitary that is even or odd satisfies $\Gamma U = \pm U\Gamma$, so it maps each sector into one sector: the outcomes of a record written by such a coupling on a state in one sector lie in one sector. For the even state on four rungs given by $y = (\tfrac35 v_{1} + \tfrac45 v_{2})\,v_{3}\,P_{0}$ ($P_{0}$ the all-off string) and the even unitary $U = \mathrm{off}_{1} + \mathrm{on}_{1}X$, with $X$ the even self-adjoint element exchanging a quantum between rungs $3$ and $4$, the two records (quantum on rung $4$, quantum on rung $3$) have weights $\tfrac{9}{25}$ and $\tfrac{16}{25}$ and are perfectly correlated with the system's rung; both lie in the same sector of $\Gamma$ and of the total number; and the even self-adjoint element $O = v_{1}w_{2}v_{4}w_{3} + \text{adjoint}$ has value $\tfrac{24}{25}$ in the state after $U$ and $0$ in the state with the interference between the records removed. The same holds for the odd coupling $U'' = \mathrm{off}_{1}e_{4} + \mathrm{on}_{1}e_{3}$ on the state given by $(\tfrac35 v_{1} + \tfrac45 v_{2})P_{0}$: it is unitary, odd, keeps even states even, writes records on single rungs with weights $\tfrac{9}{25}$, $\tfrac{16}{25}$, and the even element $U''(v_{1}w_{2} + \text{adjoint})U''^{\dagger}$ has value $\tfrac{24}{25}$. A coupling that is neither even nor odd, $U' = \mathrm{off}_{1} + \mathrm{on}_{1}e_{3}$, sends an even state to a state that is not even (compare Theorem \claimref{synthesis.records-keep-even-states-even-only-for-parity-homogeneous-observables}). \emph{The stored descent.} The multi-mode descent $\mathcal{E}(x) = \sum_{s}P_{s}xP_{s}$ (Definition \claimref{obj.singularity.multi-mode-descent}) applied to the state after $U$ keeps the record weights $\tfrac{9}{25}$, $\tfrac{16}{25}$ and sends the value of $O$ to $0$: it ends the interference between the records. Applied to the state before any record it sends the value $\tfrac{24}{25}$ of the system's own interference element $v_{1}w_{2} + \text{adjoint}$ to $0$. So requirement (a) is met by a stored map if a premise places it at records and not elsewhere; it gives every record its weight and singles out none.
\item[(iii)] \emph{(No deterministic law on strings.)} On two rungs there is an even rotor $R$ ($R\tilde{R} = RR^{\dagger} = 1$) that takes the state of the string $(1,0)$ to a state with weights $\tfrac{9}{25}$ on $(1,0)$ and $\tfrac{16}{25}$ on $(0,1)$. A map from strings to strings takes a string of weight $1$ to a string of weight $1$. So no rule that assigns to each string one later string reproduces the weights of (P) under even rotors: a law for an actual string on a fixed finite set of rungs, with the string as the only hidden datum, is stochastic, or draws on data outside those rungs.
\item[(iv)] \emph{(Unread rungs carry the uniform weight.)} In the one symmetric extension of Theorem \claimref{synthesis.state-of-a-new-rung-unique-symmetric-extension-is-the-half-weight}(ii), applied twice, each of the four strings of the two new rungs has weight $\tfrac14$, and in general $2^{-k}$ on $k$ new rungs. By clause (iii) of that theorem the strings are labels on a finite tower, and a search of the store found no premise that makes one of them actual (a statement about the store, not a computation). The stored account of the tower counts against reading rungs as fresh events: the tower has no clock, and the rungs beyond the first sit on shadow walls away from the physical region (Proposition \claimref{tower.answers-iteration-question}).
\end{enumerate}
\emph{Reading (argued, not proved).} None of the four is a selector on finite towers; the statement is about these four and does not exclude a candidate not listed. (i) gives (b) for free only where (a) is trivial. (ii) shows the one exact superselection rule of a finite tower cannot do (a) for a record written by an even or odd coupling, while the stored descent does (a) wherever it is applied and never (b). (iii) and (iv) together say what a selector on the tower would be: a premise that one string is actual, and a law reading unread rungs, for which (iv) supplies an unbiased prior and nothing else (with a bounded number of rungs read per event such a law gives weights with denominator a power of two only; reading until decided gives any rational weight with a finite number of reads with probability one; argued, standard, not computed here). Premises of those two kinds make a theory of the kind of Bell's beables for fermion number; they would make each rung's value a datum, an unbounded list against the short count of free data in Proposition \claimref{one-relation.record-chain-votes-measurement-without-collapse}, and they would depend on the split of (P), which is not preserved by boosts. They are not adopted here. Stochastic collapse and gravitational collapse are further premises of other kinds, not examined beyond naming them.

## technical
A mechanism for collapse has two jobs: stop the outcomes interfering, and pick one. Four ideas were tried on finite towers, each with a kill condition written first. Requiring whole-number values makes every state a definite string when the integer form is the switch's, but only because nothing else is left: there is no superposition to collapse, and the ladder's integer form keeps three weights, 0, 1/2 and 1. Parity is the one exact superselection rule of a finite tower, with two sectors; a record written by an even or an odd coupling leaves both outcomes in the same sector and an even observable still sees their interference in full. A deterministic rule for an actual string cannot reproduce the weights, since a rotor spreads one string over two. And the unread rungs of the earlier result give every string the same weight, an unbiased prior with no actual value behind it.

So none of the four candidates is a selector on finite towers. The store does hold a map that ends interference, the multi-mode descent, which wipes out interference between occupation records and keeps their weights; applied everywhere it also wipes out the system's own interference before any record, so it would need a premise saying where it acts, and it picks nothing. A selector could be added by premises of two kinds (a string is actual; a law reads fresh rungs), and the cost is stated: an unbounded list of data and dependence on a split that boosts change. The result is a survey of named candidates on finite towers, conditional on (P); it is not a proof that no mechanism can exist.

## lay
For a quantum measurement to give one result, something has to stop the possible results from interfering and something has to choose one of them. This result tries four ideas for where the framework might already contain such a chooser, assuming its rule that averages are never negative. If only whole-number values are allowed (in one of the two whole-number versions of the algebra), every state is definite, but only because all the in-between states have been thrown away, which also throws away interference that experiments see. The framework's one exact barrier between kinds of states, parity, has just two sides, and a measurement of the allowed kind leaves both results on the same side, still able to interfere. A fixed rule that moves one definite pattern of switches to another cannot give the right odds. And the fresh switches added by the framework's construction arrive as fair coins with no face showing. So none of these four ideas gives a chooser. The framework does contain a step that stops results interfering, but it treats every result alike and would need a rule saying when it applies. One could be added by assuming that one pattern of switches is real and that fresh switches are read as they arrive, but that is a new assumption with a stated cost, and this result does not make it.

## one-liner
Under (P), on finite towers, four named candidates for a selector of outcomes fail: integer states are definite only where superposition is absent (two states per rung in the switch form, five in the ladder form); parity has two sectors and an even or odd record coupling leaves interference $\tfrac{24}{25}$ visible, while the stored multi-mode descent removes it and selects nothing; an even rotor spreads one string to weights $\tfrac{9}{25}$, $\tfrac{16}{25}$, so no deterministic law on strings; unread rungs carry the uniform weight with no actual value; a selector would need new premises of two kinds (that a string is actual; a law that reads it).
