---
id: synthesis.records-keep-even-states-even-only-for-parity-homogeneous-observables
kind: claim
version: 1
title: 'Sector average (x + axa)/2 keeps even states of (P) even iff a is parity-homogeneous'
status: proved
region: synthesis
subject: clifford-structure
tags: [entanglement, measurement-and-records, finite-models]
proposed_by:
  kind: ai
  session: 2026-11-10-phase2
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-10-phase2
review: draft
derivations:
- name: main
  uses:
  - synthesis.signed-directions-and-the-integer-clifford-algebra@2
  - tower.commuting-copies@5
  - synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate@1
  - singularity.descent-parity-average@5
  - synthesis.positivity-of-values-is-additivity-of-non-negative-weights-on-effects@1
  assumes:
  - synthesis.premise-positivity-of-values@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_record_map_commutes_with_parity_exactly_for_homogeneous_observables
- kind: check
  ref: check.py::check_one_mode_per_party_at_homogeneous_settings_even_states_give_at_most_two
- kind: check
  ref: check.py::check_two_modes_per_party_odd_homogeneous_observables_exceed_two_on_an_even_state
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - singularity.p-univalence
  - one-relation.recorded-sectors-superselected-premise
  - synthesis.chsh-with-parity-even-observables-needs-two-modes-per-party-and-no-klein-twist
  - synthesis.univalence-from-even-stationary-dynamics
  - synthesis.splits-adapted-to-the-null-pairs-and-the-states-common-to-all-of-them
extraction:
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: >-
      Version kept at 1 (an assumes edge, lineage and notes only). The assumes edge to synthesis.premise-
      positivity-of-values, which the review asked for and only a maintainer may add, is added at the
      premise's current version 2: clauses (i), (ii)(1), (iii), (iv) and (v) are statements about states of
      (P); the premise leaves lineage, the proof names it in a first line, and the coverage record lists it as
      untouched (an assumption about values, not computable). The third sufficient condition for the value at
      most 2 with one mode per party, states common to all splits adapted to the isotropic subspaces, is the
      stored result synthesis.splits-adapted-to-the-null-pairs-and-the-states-common-to-all-of-them, clause
      (iv), recorded in lineage as a comparison. The statement and the checks are unchanged.
  open_problem: op.positivity-of-values
  note: >-
    Bears on the attack item of op.positivity-of-values that asks whether elements odd under the total parity
    are observables, and on what the univalence premise (singularity.p-univalence, a premise about states) says
    about observables. Kill conditions registered before computing: an observable of mixed parity whose record
    map keeps every even state even, or a homogeneous one that does not; an even state above $2$ at one mode per
    party with homogeneous settings. Neither fired. What is proved is algebra: the record map of an observable
    keeps all even states even exactly when the observable is even or odd; in one mode per party the
    homogeneous observables are the blades, and every even functional satisfying (P) then gives at most $2$;
    with two modes per party odd observables exceed $2$ on an even state. What is argued and is a reading, not
    a theorem: that the record map $E_{a}$ is the formal content of the stored premise that recorded sectors
    are superselected (one-relation.recorded-sectors-superselected-premise), and that univalence is to hold
    after a record as well as before. Under that reading the one-mode Klein-twisted violation of the stored
    CHSH result, clause (vii), is not available at all: its settings above $2$ contain an observable of mixed
    parity. The stored statement that the parity average of the directions gives at most $2$ averages the
    observables; this result keeps the observables and constrains them through the records. The condition is
    the classical one that a superselection rule restricts measurements to those compatible with the charge
    (Wick, Wightman and Wigner 1952; from memory). Premise assumed: synthesis.premise-positivity-of-values (assumes edge added by the maintainer pass of
    10 November 2026). Clauses (i), (ii)(1), (iii), (iv) and (v) are statements about states of (P). The stored theorem
    synthesis.univalence-from-even-stationary-dynamics (version 5) is cited in a remark as another route to a
    restriction on recorded observables, with a different reading and a stronger conclusion (even only). The
    example of clause (iv) is that of the stored result on weights on effects, clause (v), which is cited for the
    average of the CHSH element and the value; only the record computation is kept here. The stationary theorem
    is a comparison only and is a lineage entry, not a premise. A third sufficient condition for the value at
    most $2$ with one mode per party, states common to all splits adapted to the isotropic subspaces, is
    the stored result synthesis.splits-adapted-to-the-null-pairs-and-the-states-common-to-all-of-them, clause (iv), a comparison recorded in lineage.
---

## formal
Let $k$ be $\Q$ or any ordered field and $\Cl_{k}(\ell,\ell)$ the algebra of $\ell$ modes: generators $e_{j}$, $f_{j}$ with $Q(e_{j}) = 1$, $Q(f_{j}) = -1$, mode parities $p_{j} = f_{j}e_{j}$, adjoint $\dagger$ the linear extension of the inverse on blades (Theorem \claimref{synthesis.signed-directions-and-the-integer-clifford-algebra}), scalar part $\langle x\rangle_{0}$. Let $\Gamma = p_{1}\cdots p_{\ell}$ be the total parity, $\alpha(x) = \Gamma x\Gamma$ (the grade involution: it fixes even blades and negates odd ones) and $E = \tfrac12(\mathrm{id} + \alpha)$ the total-parity average (Theorem \claimref{singularity.descent-parity-average} in its total-parity form). A functional $\omega$ is \emph{even} if $\omega \circ \alpha = \omega$. An \emph{observable} is an $a$ with $a^{\dagger} = a$, $a^{2} = 1$; it is \emph{homogeneous} if $\alpha(a) = a$ or $\alpha(a) = -a$. \emph{(P)} is Premise \claimref{synthesis.premise-positivity-of-values}; a \emph{state} is a functional satisfying it. The \emph{sector average} of an observable $a$, called its \emph{record map} below (that it describes a record is a reading, stated after the clauses and not part of the theorem), is
\[
E_{a}(x) = \tfrac12(x + axa) = P_{+}xP_{+} + P_{-}xP_{-}, \qquad P_{\pm} = \tfrac12(1 \pm a) .
\]
\begin{enumerate}
\item[(i)] \emph{(The sector average, under (P) for its statements about states; proved.)} $E_{a}$ is linear and idempotent, $E_{a}(1) = 1$, $E_{a}(x^{\dagger}) = E_{a}(x)^{\dagger}$, $E_{a}(xx^{\dagger}) = (P_{+}x)(P_{+}x)^{\dagger} + (P_{-}x)(P_{-}x)^{\dagger}$, and $E_{a}(P_{+}xP_{-}) = 0$. So if $\omega$ satisfies (P) then so does $\omega \circ E_{a}$, and $\omega \circ E_{a}$ vanishes on the elements $P_{+}xP_{-}$ and $P_{-}xP_{+}$ that connect the two sectors of $a$.
\item[(ii)] \emph{(Sector averages and parity; proved.)} For an observable $a$ the following are equivalent: (1) under (P), $\omega \circ E_{a}$ is even for every even state $\omega$; (2) $E_{a}\alpha = \alpha E_{a}$; (3) $a$ is homogeneous.
\item[(iii)] \emph{(One mode per party, under (P); proved.)} In $\Cl_{k}(2,2)$ with the parties of clause (vii) of Theorem \claimref{synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate} (mode $1$, and mode $2$ twisted by $p_{1}$ as in Theorem \claimref{tower.commuting-copies}), the homogeneous observables other than $\pm 1$ are $\pm X_{1}$, $\pm Z_{1}$ for party $1$ and $\pm X_{2}$, $\pm Z_{2}$ for party $2$, where $X_{1} = e_{1}$, $X_{2} = e_{2}p_{1}$ (odd) and $Z_{1} = p_{1}$, $Z_{2} = p_{2}$ (even). For every choice $A_{1}, A_{2}$ among the first four and $B_{1}, B_{2}$ among the second four, with $C = A_{1}(B_{1} + B_{2}) + A_{2}(B_{1} - B_{2})$, $U = X_{1}X_{2}$ and $V = Z_{1}Z_{2}$: $E(C) = \mu U + \nu V$ with $|\mu| + |\nu| \le 2$, and every even state has $|\omega(C)| = |\omega(E(C))| \le 2$.
\item[(iv)] \emph{(The settings above $2$ are of mixed parity, under (P); proved by an example.)} At $A_{1} = X_{1}$, $A_{2} = Z_{1}$, $B_{1} = \tfrac35X_{2} + \tfrac45Z_{2}$, $B_{2} = \tfrac45X_{2} - \tfrac35Z_{2}$, clause (v) of Theorem \claimref{synthesis.positivity-of-values-is-additivity-of-non-negative-weights-on-effects} gives an even state $\omega$, that of the atom $\tfrac14(1 + U)(1 + V)$, with $\omega(C) = \tfrac{14}{5} > 2$ (there $u = U$ and $\Gamma = V$), and notes that the value above $2$ uses directions of mixed parity; clause (viii) of the stored CHSH theorem notes the same possibility. What is added here is the record: $B_{1}$ is not homogeneous, and $\omega \circ E_{B_{1}}$ is not even, its value on the odd element $X_{1}Z_{2}$ being $\tfrac{12}{25}$.
\item[(v)] \emph{(Odd observables with two modes per party, under (P); proved.)} In $\Cl_{k}(4,4)$ let $A_{1} = e_{1}$, $A_{2} = e_{2}$, $B_{1} = e_{3}p_{1}p_{2}$, $B_{2} = e_{4}p_{1}p_{2}$. All four are odd observables, blades up to sign; $A_{i}$ commutes with $B_{j}$; $C$ and $K = -A_{1}A_{2}B_{1}B_{2}$ are even, and the functional $\omega(x) = \langle(1 + K)(1 + \tfrac13C)x\rangle_{0}$ is an even state with $\omega(C) = \tfrac83 > 2$. The record maps of the four observables commute with $\alpha$.
\end{enumerate}
\emph{Reading (argued, not part of the theorem).} Premise \claimref{one-relation.recorded-sectors-superselected-premise} says that after a record the recorded sectors do not interfere; for a two-valued observable $a$ and values given by a functional $\omega$, the functional with no interference between the sectors of $a$ and the same values on what commutes with $a$ is $\omega \circ E_{a}$. Premise \claimref{singularity.p-univalence} says that physical states are even. If both hold, before and after a record, then by (ii) an observable that can be recorded is even or odd, never a sum of the two. Odd observables are then allowed, one mode per party gives at most $2$ in both settings, and a value above $2$ needs two modes per party whether the observables are even (Theorem \claimref{synthesis.chsh-with-parity-even-observables-needs-two-modes-per-party-and-no-klein-twist}) or odd (clause (v)). Sufficient conditions for the value at most $2$ with one mode per party that are recorded and consistent: homogeneous settings and even states (clause (iii)); averaged directions (clause (vii) of the stored CHSH theorem); and, as a formula, $|X| + |Z| \le 2$ in clause (v) of Theorem \claimref{synthesis.positivity-of-values-is-additivity-of-non-negative-weights-on-effects} when every direction is even or odd, of which clause (iii) is the statement for all signed choices with its certificate.

\emph{Remark (another route, argued).} Theorem \claimref{synthesis.univalence-from-even-stationary-dynamics}, clause 3, says that every density stationary under the flow of an even generator is even exactly when no odd signed sum of weights vanishes. If ``recorded'' is read as ``never unwritten, hence stationary'', that theorem gives that a recorded observable is even, without the map $E_{a}$ and without asking that univalence hold after a record. The comparison: that route also needs a reading (recorded implies stationary); it is stored for the complex Fock realisation, not for $\Cl_{k}(\ell,\ell)$ under (P); and its conclusion, even, is stronger than even or odd and would exclude the odd observables of clause (v). It does not replace clause (ii), which is about an arbitrary observable and the map $E_{a}$. Which reading of a record is meant is not decided here.

## technical
The univalence premise restricts states to those that vanish on parity-odd elements; it says nothing directly about observables. This result supplies the link through records, under (P), positivity of values, for the statements about states. The theorem is about the sector average $E_{a}(x) = \tfrac12(x + axa)$ of a two-valued observable $a$, which removes the interference between the two sectors of $a$ and sends states to states; that it describes a record of $a$ is a reading. The theorem: $E_{a}$ sends every even state to an even state exactly when $a$ is even or odd under the total parity. An observable that is a sum of an even and an odd part, such as the direction $\tfrac35e_{1} + \tfrac45p_{1}$ of one mode, turns an even state into one that is not even. In the realisation of the CHSH bound with one mode per party and a Klein twist, the only homogeneous observables are $\pm e_{1}$, $\pm p_{1}$ and their twisted partners, and at these settings every even state gives the CHSH combination a value of at most $2$; the settings that reach $14/5$ on an even state use a direction of mixed parity. Parity-odd observables as such are not excluded: with two modes per party, four odd blades give $8/3$ on an even state. So, under the reading that records act by $E_{a}$ and that states stay even after a record, the two settings recorded side by side (even observables, or odd ones with a twist) both need two modes per party, and the one-mode violation is not available. The reading is argued; the algebra is proved. A different reading (recorded means stationary) with the stored theorem on even stationary dynamics would give that recorded observables are even, excluding the odd ones; the two readings are not decided between here.

## lay
The series has a rule that physical states must look the same when every fermion-like mode changes sign ("even" states), but it had no rule about which quantities can be measured. This result connects the two, assuming (P), the series' assumption that averages are never negative on a quantity times its mirror image. When a two-valued quantity is measured and the result recorded, the state changes in a definite way. The theorem says that this change keeps every even state even exactly when the measured quantity is itself purely even or purely odd; a quantity that mixes the two kinds spoils the rule. For two experimenters with one mode each, the only quantities that pass this test are too few to beat the classical limit of 2 on the standard combination of correlations. Quantities of the odd kind are still allowed, but each experimenter needs two modes to exceed 2. This holds if recording works as described and the rule on states holds after a recording too; those two points are a reading of the series' premises, not something proved here.

## one-liner
In $\Cl_{k}(\ell,\ell)$ under (P), the sector average $E_{a}(x) = \tfrac12(x + axa)$ of an observable (a record of $a$, on a reading that is argued) sends every even state to an even state exactly when $a$ is even or odd; with one twisted mode per party the homogeneous settings give every even state $|\omega(C)| \le 2$, a mixed setting gives $\tfrac{14}{5}$ and its record breaks evenness, and two modes per party with odd observables give $\tfrac83$.
