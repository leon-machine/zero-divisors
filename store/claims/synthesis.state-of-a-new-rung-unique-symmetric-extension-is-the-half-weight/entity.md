---
id: synthesis.state-of-a-new-rung-unique-symmetric-extension-is-the-half-weight
kind: claim
version: 1
title: 'State of a new rung: the one symmetric extension has weight one half'
status: proved
region: synthesis
subject: tower
tags: [measurement-and-records, car-algebra, hyperbolic-plane, finite-models]
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
  role: independent review
  source: session 2026-11-12-rung-state
review: draft
derivations:
- name: main
  uses:
  - tower.ladder-pairs-satisfy-car-vectors@4
  - rungs.imported-totality-minimality-completion@6
  - synthesis.set-and-clear-of-a-bit-generate-the-hyperbolic-plane@1
  - synthesis.exchange-of-set-and-clear-is-inner-and-fixed-by-no-integer-state@1
  - synthesis.no-two-valued-weights-on-the-atoms-of-two-modes-the-even-subalgebra-admits-them@1
  assumes:
  - synthesis.premise-positivity-of-values@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_both_values_extend_the_state_under_p
- kind: check
  ref: check.py::check_one_invariant_extension_with_weight_one_half
- kind: check
  ref: check.py::check_strings_form_one_orbit_and_two_rotor_classes
- kind: check
  ref: check.py::check_a_string_is_a_weight_on_one_context
- kind: check
  ref: check.py::check_dependence_of_uniqueness_on_the_group
- kind: check
  ref: check.py::check_either_sign_change_alone_admits_another_invariant_extension
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - one-relation.record-chain-votes-measurement-without-collapse
  - synthesis.boundary-mode-thermal-entropy
  - tower.fock-module-one-qubit-per-rung
extraction:
  open_problem: op.outcome-selector-premises
  note: >-
    A test asked for by Leon on 12 November 2026, after a review of the no-collapse result: the counting argument
    there says a collapse needs unboundedly many fresh bits and the framework has a short list of free data; his
    question was whether the bits could come from iterating the transport without end, one rung at a time. The
    question was put as: is the set or clear value of a new rung forced by the completion, or is it a datum?
    Pre-registered before computing (colony/runs/2026-11-12-rung-state/PREREGISTRATION.md, committed first), with
    three hypotheses and their kill conditions: forced (killed if both values extend the state under (P)); datum
    (killed if a symmetry of the step exchanges the values and the strings on several rungs form one orbit with two
    classes under rotors); coin (exactly one symmetric extension, of weight one half, not sharp, not integer
    valued). Predicted before computing: forced killed, datum killed, coin holds. Outcome: as predicted. What this
    does and does not show: iteration supplies unboundedly many two-state systems; the completion fixes no value on
    them and gives the values no meaning beyond a relabelling, apart from the one class bit of the whole string,
    a chirality bit of the same kind as the stored orientation bit (that it is that bit is not shown). So the iteration is not, by itself, a source of the bits
    a selection of outcomes needs. It is not a no-go for a selector: a further premise could declare each rung's
    value a datum and give a law that reads it, at the cost of an unbounded list of data and against clause (iv).
    The symmetries used are the sign changes of the new generators, the automorphisms that fix the old algebra and
    keep the adjoint of (P); a wider or narrower notion of symmetry of the step would change clause (ii), and that
    choice is a reading. The coincidence of the weight one half with the stored occupation of a boundary mode at
    zero weight (synthesis.boundary-mode-thermal-entropy, which is under premises of its own) is recorded as an
    observation, not as a derivation of either from the other. Transport-convenient: the algebra is standard
    (product states on a tensor factor, the two families of pure spinors); what is new is the question it is set
    against. Not done: correlated extensions are covered by clause (ii) only in the invariant case; no statement is made
    about laboratory recording. The infinite tower (the CAR limit) is not treated, and the answer there may differ:
    under symmetries that act on finitely many rungs, strings that differ on infinitely many rungs are not related
    (their states are disjoint, argued from the stored Powers and Stormer criterion), so whether rung values are data
    there turns on whether automorphisms acting on infinitely many rungs count as symmetries; that is argued, not
    computed. The completion Fact cited for the step is stated for dimension at least three over the reals; the
    clauses use only the adjunction of a hyperbolic plane to Cl_Q(l,l), which the ladder-pair Proposition supplies,
    so l = 0, 1 and the rationals do not rest on that Fact. Reviewed by an independent referee (Claude Opus 5.5,
    12 November 2026): sound with fixes, applied here: the dependence of clause (ii) on the group, the parity
    condition in clause (iv), the restriction to finite towers, and 'a chirality bit of the same kind' in place of
    an identification with the stored orientation bit. The referee judged two of the three pre-registered
    hypotheses weak tests: 'forced' was killable by elementary product states, and 'datum' was killed by the choice
    of group, so only 'coin' was a test whose outcome was open. A second review the same day found that the group-dependence
    sentence added after the first was itself wrong (it said the sign change of f does not exchange on with off,
    and that an exchange with a sign change moving e suffices; the sign change of e alone does both and uniqueness
    still fails for l = 1); corrected here, with the counterexample in the check.
---

## formal
Let $A_{\ell} = \Cl_{\Q}(\ell,\ell)$ with generators $e_{j}$, $f_{j}$, $Q(e_{j}) = 1$, $Q(f_{j}) = -1$, and ladder pairs $v_{j} = \tfrac12(e_{j} + f_{j})$, $w_{j} = \tfrac12(e_{j} - f_{j})$ (Proposition \claimref{tower.ladder-pairs-satisfy-car-vectors}). One step of the transport adjoins one hyperbolic plane, unique up to isometry (Fact \claimref{rungs.imported-totality-minimality-completion}): $A_{\ell} \subset A_{\ell+1}$, with new generators $e$, $f$ and new pair $v$, $w$. Write $\mathrm{on} = vw$ and $\mathrm{off} = wv$, the two tests of the new rung (Theorem \claimref{synthesis.set-and-clear-of-a-bit-generate-the-hyperbolic-plane}); $\mathrm{on} + \mathrm{off} = 1$. Assume Premise (P), positivity of values (Premise \claimref{synthesis.premise-positivity-of-values}), for the split $e_{j}, f_{j}$: a \emph{state} is a linear $\omega$ with $\omega(1) = 1$, $\omega(xx^{\dagger}) \ge 0$, $\omega(x^{\dagger}) = \omega(x)$. An \emph{extension} of a state $\omega$ on $A_{\ell}$ is a state $\Omega$ on $A_{\ell+1}$ with $\Omega = \omega$ on $A_{\ell}$. A \emph{symmetry of the step} is an automorphism of $A_{\ell+1}$ that fixes $A_{\ell}$ pointwise, maps the new plane to itself and commutes with $\dagger$: these are the sign changes $\sigma_{e}$ ($e \mapsto -e$), $\sigma_{f}$ ($f \mapsto -f$) and $\sigma_{e}\sigma_{f}$.
\begin{enumerate}
\item[(i)] \emph{(The completion does not fix the value.)} For every state $\omega$ on $A_{\ell}$ and every $t \in \Q$ with $0 \le t \le 1$ there is an extension $\Omega_{t}$ with $\Omega_{t}(a\,\mathrm{on}) = t\,\omega(a)$ and $\Omega_{t}(a\,\mathrm{off}) = (1 - t)\,\omega(a)$ for $a \in A_{\ell}$, vanishing on $A_{\ell}e$ and $A_{\ell}f$ (the sum $A_{\ell+1} = A_{\ell} \oplus A_{\ell}e \oplus A_{\ell}f \oplus A_{\ell}fe$ is direct, so $a \mapsto a\,\mathrm{on}$ is injective). In particular both the value on ($t = 1$) and the value off ($t = 0$) extend $\omega$. The restriction of $\Omega_{t}$ to the new rung is sharp, that is given by an idempotent, exactly for $t \in \{0, 1\}$.
\item[(ii)] \emph{(One symmetric extension.)} $\sigma_{f}$ exchanges $v$ with $w$ and on with off; $\sigma_{e}$ exchanges $v$ with $-w$ and on with off. Among all linear functionals on $A_{\ell+1}$ that restrict to $\omega$, exactly one is invariant under the symmetries of the step: $\Omega_{1/2}$. It is an extension, it gives on and off the weight $\tfrac12$ each, it is not sharp on the new rung, and it takes a value that is not an integer; no extension that is integer valued on the tests, and none that is sharp on the new rung, is invariant (compare Theorem \claimref{synthesis.exchange-of-set-and-clear-is-inner-and-fixed-by-no-integer-state}). \emph{Dependence on the group.} Among the symmetries that commute with $\dagger$ the uniqueness for every $\ell$ needs both $\sigma_{e}$ and $\sigma_{f}$. Under $\sigma_{f}$ alone it fails already for $\ell = 0$: the state with $\Omega(e) = 1$ is invariant, sharp and integer valued on the blades. Under $\sigma_{e}$ alone it holds for $\ell = 0$, where reality forces $\Omega(f) = 0$, and fails for $\ell = 1$: with $e_{1}$ the old generator of square $1$, the state of $\tfrac12(1 + e_{1}f)$ is invariant, restricts to the symmetric state of the old rung, gives on the weight $\tfrac12$ and gives $e_{1}f$ the value $1$. $\Omega_{1/2}$ is also invariant under the boosts $e \mapsto ce + sf$, $f \mapsto se + cf$, $c^{2} - s^{2} = 1$, which are isometries of the new plane but do not commute with $\dagger$ (the adjoint of (P) is relative to the split); under the group generated by the boosts and $\sigma_{e}\sigma_{f}$, which keeps set and clear in their roles, every $\Omega_{t}$ is invariant. Whether $\sigma_{e}$ and $\sigma_{f}$ count as symmetries of the step is a reading, not decided here.
\item[(iii)] \emph{(Strings of values are labels, up to one bit.)} On $m$ rungs the $2^{m}$ products of tests $P_{s} = \prod_{j}(\mathrm{on}_{j}$ or $\mathrm{off}_{j})$, $s \in \{0,1\}^{m}$, are pairwise orthogonal idempotents with sum $1$. The sign changes of the $f_{j}$ permute them simply transitively: all $2^{m}$ strings are one orbit of automorphisms that keep the generators up to sign and commute with $\dagger$. Changing two values at once, at rungs $i$ and $j$, is conjugation by the rotor $f_{i}f_{j}$. The volume element $\Gamma = \prod_{j}f_{j}e_{j}$ commutes with every rotor and $\Gamma P_{s} = \pm(-1)^{|s|}P_{s}$ with one overall sign, so under rotors the strings fall into exactly two classes, by the parity of $|s|$.
\item[(iv)] \emph{(A string is a weight on one context; whether it extends depends on which elements are tests.)} For two rungs the four $P_{s}$ are one context of atoms in the sense of Theorem \claimref{synthesis.no-two-valued-weights-on-the-atoms-of-two-modes-the-even-subalgebra-admits-them}, on which a string gives the weights $1, 0, 0, 0$; the state of a string gives an atom of another context the weight $\tfrac12$, and that atom is not even. If the atoms of mixed parity are tests, then by clause (i) of that theorem no assignment of the values $0$ and $1$ to all atoms sums to $1$ on every context, so a string cannot be extended to a pre-assignment of an outcome to every test. If only even elements are tests, clause (iii) of the same theorem gives a two-valued additive weight on all self-adjoint idempotents of the even subalgebra of two modes; it has the value $1$ on exactly one string, and composing it with sign changes of the $f_{j}$ moves that string to any given one, so there a string does extend and the obstruction is absent.
\end{enumerate}
\emph{Reading (argued, not proved).} The question was whether iterating the transport supplies, rung by rung, the fresh bits that a selection of measurement outcomes would need. By (i) the completion forces no value. By (ii) and (iii) it gives the values no meaning beyond a relabelling, except the one class bit of the whole string, a chirality bit of the same kind as the stored orientation bit (that it is that bit is not shown); the only extension it singles out is the unbiased one, which has no value and exists only once $\tfrac12$ does. By (iv) a string taken as data could not fix outcomes test by test if tests of mixed parity are allowed, and could for even tests on two modes. So on every finite tower, and with the exchange counted as a symmetry, iteration supplies two-state systems and no bits of data; the infinite tower is not treated here. A selector built on the tower would need a further premise: that each rung's value is a datum, with a law reading it. The weight $\tfrac12$ equals the stored occupation of a boundary mode at zero weight; that is recorded as an observation.

## technical
A transport step adds one hyperbolic plane, hence one two-state system, to the algebra. Under the premise (P) on values, a state on the old algebra extends to the enlarged one with any weight between 0 and 1 on the new rung's "on" test, so the completion does not decide whether the new rung is on or off. The step has symmetries, the sign changes of the two new generators, which leave the old algebra and the adjoint of (P) alone; one of them exchanges set with clear. Exactly one extension is symmetric under both sign changes: the one with weight one half on each value. Both are needed in general: under the sign change of $f$ alone, and for one or more old rungs under that of $e$ alone, other invariant extensions exist, and under the boosts with the joint sign change every weight is invariant. It is not sharp and not integer valued. For several rungs, the strings of on and off values are all carried into one another by such sign changes, and pairs of changes are rotations, so the only thing about a string that a rotation cannot change is the parity of the number of rungs that are on: one bit, a chirality bit of the same kind as the store's orientation bit (that it is that bit is not shown). Finally a string is a yes-or-no assignment on one set of mutually exclusive tests; the stored result on two-valued weights shows it cannot be continued to all tests if tests of mixed parity are allowed, and can be for even tests on two modes.

The result is conditional on (P) and on the reading of "symmetry of the step" as the sign changes of the new generators. It is algebra on finite towers; the infinite tower and laboratory records are not treated. It does not exclude a selector of outcomes; it shows that iteration alone is not one.

## lay
Each step of the framework's basic construction adds one new on-off switch. The question was whether these switches, added without end, could be the hidden source of the random-looking outcomes of quantum measurements: perhaps each new switch arrives already on or already off, and those settings decide what we see. Assuming the framework's rule that averages can never be negative, this result shows the construction does not decide the setting of a new switch: on and off are both allowed, and so is anything in between. If the two mirror symmetries of a new switch both count as symmetries of the construction, the only arrangement that respects them is the fifty-fifty one, which has no definite setting at all; if either does not count, this conclusion fails in general. For many switches, any pattern of settings can be turned into any other by relabelling, apart from one overall yes-or-no fact, of the same kind as one the framework already counts. And a pattern of settings could fix the answers to all measurements in advance only if measurements are restricted to a special kind (those that do not mix even and odd). So, for any finite number of switches, adding switches gives a supply of coins, not a supply of results of coin tosses. The case of infinitely many switches is not settled here. To make the switches decide outcomes one would have to add a new assumption saying so.

## one-liner
Under (P), a state on $\Cl_{\Q}(\ell,\ell)$ extends to the next rung with any weight $t \in [0,1]$ on its on test; exactly one extension is invariant under the sign changes of the new generators, the one with $t = \tfrac12$, neither sharp nor integer valued; strings of values on $m$ rungs form one orbit of sign changes and two classes under rotors; so on every finite tower the transport supplies two-state systems but, if the exchange of on with off counts as a symmetry of the step, no bits of data.
