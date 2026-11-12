---
id: synthesis.records-of-unbounded-length-on-the-tower-interference-factor-and-limit
kind: claim
version: 1
title: 'Records of unbounded length on the tower: the interference factor and the limit state'
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
  role: the candidate (records of unbounded length) and its first computation, in review of the earlier results
  source: session 2026-11-12-rung-state
review: draft
derivations:
- name: main
  uses:
  - tower.fock-module-one-qubit-per-rung@6
  - tower.ladder-pairs-satisfy-car-vectors@4
  - tower.algebraic-limit-even-charge@3
  - synthesis.imported-powers-stormer-takesaki-disjointness@3
  assumes:
  - synthesis.premise-positivity-of-values@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_fock_module_is_the_clifford_algebra_of_the_ladder_pairs
- kind: check
  ref: check.py::check_interference_factor_on_a_full_basis_for_three_pairs
- kind: check
  ref: check.py::check_interference_is_full_for_an_element_touching_every_pair
- kind: check
  ref: check.py::check_record_modes_differ_by_a_fixed_hilbert_schmidt_amount_per_pair
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - one-relation.recorded-sectors-superselected-premise
  - one-relation.record-chain-votes-measurement-without-collapse
  - synthesis.selector-candidates-on-the-tower-integer-states-parity-deterministic-laws
extraction:
  note: >-
    Step 1 of three approved by Leon on 12 November 2026. The candidate came from the independent review of the
    earlier results (records of unbounded length; computed there for up to three pairs). Pre-registered before
    computing (colony/runs/2026-11-12-rung-state/PREREGISTRATION-3.md): item 1a was marked a test, with the open
    point the signs for odd elements and for record pairs interleaved with uncoupled ones; 1b and 1c were marked
    proofs with sanity checks. Outcome: 1a holds, on a full linear basis of the algebra for three pairs (so for
    all elements there, by linearity). Item 1a was mislabelled a test: the surprise it named, a failure on odd
    elements, was impossible from the start, since both branches hold the same number of quanta and an odd element
    has value zero between them; it was in effect a proof. Reviewed by an independent referee (Claude Opus 5.5,
    12 November 2026): sound with fixes, applied here. One was a mathematical error: the first draft said that for
    c = 0 the state equals the mixture as soon as N exceeds the largest pair an element involves, which is off by
    one (for N = 1 the element O_1 has value 24/25 against 0). The corrected sentence was then found, in a third pass, to be still wrong (it omitted that every pair the
    element involves must be among the coupled ones, since the starting vector fills only the first N pairs); it is
    stated here with both conditions and both counterexamples. The others narrowed wording: 'equals the mixture on
    every element' in place of 'no element has interference in the limit state', and the premise is said to hold
    for this model, not to be derived. What this is: a model coupling, chosen by
    hand, in which a record is written on more and more rungs; the stored premise that recorded sectors are
    superselected holds for it in the limit of unbounded records, as a statement about every element of the
    algebraic tower. What it is not: a derivation of that premise for laboratory recording (no stored dynamics
    writes such records, and the premise speaks of the modular period, which does not enter here); a statement at
    any finite stage (clause (ii)); a selector (both outcomes keep their weights). It is the model of Coleman and
    Hepp (Hepp, 1972), with Bell's objection (1975) as clause (ii); both cited from memory. Transport-absent:
    standard, restated on the tower. The reading at the level of the completed algebra (clause (iv)) rests on the
    imported Powers and Stormer criterion and is argued from it, not proved here.
---

## formal
Work in the Fock module of the ladder pairs (Theorem \claimref{tower.fock-module-one-qubit-per-rung}, Proposition \claimref{tower.ladder-pairs-satisfy-car-vectors}): $v_{j}$ acts by the wedge, $w_{j} = v_{j}^{\dagger}$ by the contraction, $\mathrm{on}_{j} = v_{j}w_{j}$, and states are those of unit vectors, $\omega_{\Psi}(x) = \langle\Psi, x\Psi\rangle$, which satisfy Premise (P) (Premise \claimref{synthesis.premise-positivity-of-values}). Rungs $0, 1$ are the system; for $j \ge 0$ the rungs $a_{j} = 2 + 2j$, $b_{j} = 3 + 2j$ are record pair $j$. Let $c, s \in \Q$ with $c^{2} + s^{2} = 1$, $|c| < 1$, and
\[
R_{j} = (1 - \Pi_{j}) + c\,\Pi_{j} + s\,(v_{a_{j}}w_{b_{j}} - v_{b_{j}}w_{a_{j}}), \qquad U_{j} = \mathrm{off}_{0} + \mathrm{on}_{0}R_{j},
\]
with $\Pi_{j}$ the test ``pair $j$ holds one quantum''; $R_{j}$ is an even rotor and $U_{j}$ an even unitary. Let $\Psi_{0} = (\tfrac35 v_{0} + \tfrac45 v_{1})\prod_{j < N}v_{a_{j}}\,|0\rangle$ and $\Psi_{N} = U_{N-1}\cdots U_{0}\Psi_{0} = \tfrac35 A_{N} + \tfrac45 B$, with branch vectors $A_{N}$ (system quantum on rung $0$, every pair rotated) and $B$ (system quantum on rung $1$, pairs untouched). For a set $K$ of pairs let $A_{K}$ be the branch vector with only the pairs of $K$ rotated, and for an element $x$ put
\[
I_{K}(x) = \tfrac{12}{25}\bigl(\langle A_{K}, xB\rangle + \langle B, xA_{K}\rangle\bigr),
\]
the interference of $x$: the value of $x$ in $\tfrac35 A_{K} + \tfrac45 B$ minus $\tfrac{9}{25}$ times its value in $A_{K}$ and $\tfrac{16}{25}$ times its value in $B$.
\begin{enumerate}
\item[(i)] \emph{(The factor.)} If $x$ involves no generator of the pairs outside $K$, with $K$ a set of $k$ of the $N$ pairs, then $I_{N}(x) = c^{\,N - k}\,I_{K}(x)$. For $c = 0$ (a record written in full on each pair) the interference of $x$ is zero unless $x$ involves every one of the $N$ pairs. The statement holds for every element, even or odd; for odd $x$ both sides are zero.
\item[(ii)] \emph{(Every finite stage keeps the interference.)} For every $N$ the element $O_{N} = UO_{0}U^{\dagger}$, $U = U_{N-1}\cdots U_{0}$, $O_{0} = v_{0}w_{1} + v_{1}w_{0}$, is even and self-adjoint with $O_{N}^{2}$ idempotent, has value $0$ in each branch and value $\tfrac{24}{25}$ in $\Psi_{N}$: $I_{N}(O_{N}) = \tfrac{24}{25}$, the interference $O_{0}$ had before any record. So the decay in (i) is not uniform over elements.
\item[(iii)] \emph{(The limit on the algebraic tower.)} On the algebraic limit of the tower (Theorem \claimref{tower.algebraic-limit-even-charge}), in which every element involves finitely many generators, $\omega_{\infty}(x) = \lim_{N}\omega_{\Psi_{N}}(x)$ exists for every $x$, is a state under (P), and
\[
\omega_{\infty} = \tfrac{9}{25}\,\omega_{A} + \tfrac{16}{25}\,\omega_{B},
\]
the mixture of the two branch states, $\omega_{A}(x) = \langle A_{K}, xA_{K}\rangle$ for any $K$ containing the pairs $x$ involves: $\omega_{\infty}$ equals the mixture on every element of the algebraic tower. The convergence is pointwise in $x$ and not uniform over elements of norm at most $1$, that is not in norm: by (ii), $\omega_{\Psi_{N}}(O_{N}) - \omega_{\infty}(O_{N}) = \tfrac{24}{25}$ for every $N$, and $O_{N}^{2}$ is an idempotent, so $O_{N}$ has norm at most $1$. For $c = 0$, $\omega_{\Psi_{N}}(x)$ equals the mixture's value as soon as every pair $x$ involves is among the $N$ coupled pairs and at least one of these $N$ pairs is not involved by $x$; in particular for $N > p + 1$, where $p \ge 0$ is the largest index of a pair $x$ involves. For $N = 1$ both conditions are needed: $O_{1}$ has value $\tfrac{24}{25}$ against $0$, and $\mathrm{on}_{a_{1}}$, which involves the pair $1$ that $\Psi_{1}$ leaves empty, has value $0$ against $\tfrac{16}{25}$.
\item[(iv)] \emph{(Reading at the level of the completed algebra; argued from an import.)} In each pair the one-quantum modes of the two branches have overlap $c$, and the projections onto them differ by $2s^{2}$ in squared Hilbert-Schmidt norm; over infinitely many pairs the difference of the two branches' one-particle projections is not Hilbert-Schmidt. By clauses (a) and (d) of Fact \claimref{synthesis.imported-powers-stormer-takesaki-disjointness}, the two branch states, which are pure gauge-invariant quasi-free states of the CAR algebra, are then not quasi-equivalent and so disjoint.
\end{enumerate}
\emph{Reading (argued, not proved).} For this model coupling the statement of Premise ``recorded sectors are superselected'' holds in the limit of records of unbounded length: the limiting state is the mixture on every element of the tower's algebra. At every finite stage an element reaching every record pair still has the full interference, by (ii). The coupling is written by hand; the premise itself, which speaks of laboratory records and the modular period, is not derived. Both outcomes keep their weights $\tfrac{9}{25}$, $\tfrac{16}{25}$ throughout: nothing is selected. In the limit the state is a mixture of two disjoint states (iv), so reading it as ``one of the two outcomes obtains, with probability its weight'' agrees with the value of every element; that reading is one further premise, it is not a mechanism, and it is available only in the limit, never at a finite stage.

## technical
A system with two alternatives is coupled, one after another, to pairs of rungs, each of which keeps or partly keeps a record of which alternative holds. The interference between the alternatives that an element of the algebra can detect falls by one factor $c$, the overlap of the two record states of a pair, for each record pair the element does not involve; with complete records ($c = 0$) it is zero unless the element involves every pair. At any finite number of pairs there is still an element that sees the interference in full, one that undoes all the records. In the limit of infinitely many pairs, every element of the algebraic tower involves finitely many rungs, so none sees any interference: the limiting state is exactly the mixture of the two branches. In the completed algebra the two branch states are disjoint; this is argued from the imported Powers and Stormer criterion, not proved here.

For this model the statement of the stored premise that recorded outcomes cannot interfere holds in the limit of unbounded records; at every finite stage an element reaching all the records still sees the interference in full. The premise itself is not derived. It is a model coupling written by hand, not a stored dynamics; it is conditional on (P); and it selects nothing.

## lay
The framework assumes that once a measurement result is recorded, the different possible results can no longer interfere. This result looks at a simple model inside the framework in which the record is copied onto more and more of the switches added by its basic construction. Each extra copy weakens the interference that any given instrument can detect, and an instrument that leaves even one perfect copy untouched detects none. With any finite number of copies an instrument that reaches all of them could still, in principle, detect the interference in full. With infinitely many copies no instrument can, because every instrument the framework allows reaches only finitely many switches. So in this model, which is set up by hand, what the assumption says can be shown, but only in the limit of an unending record. Both possible results remain present with their usual odds; nothing here says why one of them happens.

## one-liner
Under (P), for a system coupled by the controlled pair rotors $U_{j}$ to $N$ record pairs with overlap $c$ per pair, an element involving $k$ of the pairs has interference $c^{N-k}$ times that with only those $k$ coupled; an element reaching all pairs keeps the full $\tfrac{24}{25}$ at every $N$; on the algebraic tower the limit state is exactly the mixture $\tfrac{9}{25}$, $\tfrac{16}{25}$, and the branch states are disjoint (argued from the imported Powers and Stormer criterion); nothing is selected.
