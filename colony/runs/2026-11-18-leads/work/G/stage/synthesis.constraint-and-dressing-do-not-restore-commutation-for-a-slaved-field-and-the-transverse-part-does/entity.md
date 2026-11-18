---
id: synthesis.constraint-and-dressing-do-not-restore-commutation-for-a-slaved-field-and-the-transverse-part-does
kind: claim
version: 1
title: 'Lattice model with a constraint: slaved field, dressed detection, transverse part'
status: proved
region: synthesis
subject: quantum-fields
tags: [quantum-gravity, gauge-fields, finite-models, no-go]
proposed_by:
  kind: ai
  session: 2026-11-18-leads
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-18-leads
review: draft
outside_ga:
  kind: other
  why: the link variables of the lattice field obey canonical commutation relations (they enter through Weyl operators), which no finite Clifford algebra holds (the stored statistics result); the lattice is not the spacetime algebra; only the matter factor of the model is an element of the algebra
derivations:
- name: main
  uses:
  - synthesis.field-slaved-to-an-operator-source-does-not-commute-at-spacelike-separation@1
  - synthesis.set-and-clear-of-a-bit-generate-the-hyperbolic-plane@1
  - field-theory.operator-newtonian-coupling@4
  - field-theory.no-canonical-commutation-relations-tower@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_bare_recombiner_breaks_the_constraint_and_the_string_dressed_one_keeps_it
- kind: check
  ref: check.py::check_string_dressed_detection_commutes_with_the_field_off_the_string
- kind: check
  ref: check.py::check_constrained_part_alone_fails_and_the_transverse_part_cancels_it
- kind: check
  ref: check.py::check_in_one_space_dimension_the_constrained_part_is_the_string
- kind: check
  ref: check.py::check_dynamics_string_dressed_detection_commutes_at_spacelike_events_and_the_slaved_field_does_not
lineage:
  motivated_by:
  - pred.gravity-entangles-standard-phase
  - synthesis.field-slaved-to-an-operator-source-does-not-commute-at-spacelike-separation
extraction:
  open_problem: op.gravitational-field-at-null-momentum
  note: >-
    Filed against the third attack item of the problem: repeat the lattice model with the constraint structure of
    a gauge field, the instantaneous part fixed by a constraint and the observables dressed. The model is a
    lattice Maxwell field with a Gauss constraint and a scalar charge, in two space dimensions (and one, as a
    clause); it is not a model of spin two. The kill conditions registered before the computation were: the
    string-dressed detection fails to commute with the field off the string (not met); with no transverse
    variable the field commutes with the detection away from the two sites in two space dimensions (not met: it
    fails on 76 of 82 links); in one space dimension the constrained fields of the two paths differ outside the
    interval (not met). The model is exactly solvable (the dressings are Weyl operators), so its statements hold
    to every order in the coupling and in particular at first order. The lattice Hamiltonian formulation of a
    gauge field, the dressing of a charge by its constrained field and the fact that such a dressing is not
    local are standard (Kogut and Susskind 1975; Dirac 1955; cited from memory). The transfer to the
    gravitational gauge field in the Reading is argued; the statements there about the multipoles left free by
    the conservation of energy and momentum and about compactly supported solutions of the linearised
    constraints are standard, cited from memory (for the second, the gluing results of Corvino and Schoen and
    their use by Donnelly and Giddings for dressed observables), and are not used in a proof step. The split of
    the first-order gravitational field equation into four constraint equations and two components with a pole
    on the cone is the subject of the result filed alongside this one on the field at null momentum. Decision
    for the maintainer, unchanged by this result and sharpened by it: whether the series requires its
    gravitational field to commute with matter observables at spacelike separation; if it does, the constraint
    and the dressing of observables do not supply that, and the two free components need variables of their
    own.
---

## formal
\emph{The model.} A box of sites of the square lattice with its links and plaquettes; $\mathrm{div}$, $\mathrm{grad}$ and $\mathrm{curl}$ are the lattice differences, $\mathrm{div}\,\mathrm{grad}$ the graph Laplacian. The field has a pair $(A_{l}, E_{l})$ on each link $l$, entering through the Weyl operators $W(f) = \exp(I_{4}\sum_{l}f_{l}A_{l})$, $f$ a real function on the links, with $W(f)W(f') = W(f + f')$ and $[E_{l}, W(f)] = f_{l}\,W(f)$ (the unit written as in the field theory). Matter is one quantum on two sites $a$, $b$, in the algebra of a completed pair as in Theorem \claimref{synthesis.field-slaved-to-an-operator-source-does-not-commute-at-spacelike-separation}: $\Cl(1,1)$, $v = \tfrac12(e_{1} + e_{2})$, $w = \tfrac12(e_{1} - e_{2})$, $Q(v) = Q(w) = 0$, $P_{1} = vw$ (the quantum at $a$), $P_{2} = wv$ (at $b$), $v = P_{1}vP_{2}$ the move from $b$ to $a$ (\claimref{synthesis.set-and-clear-of-a-bit-generate-the-hyperbolic-plane}). The charge is $\rho_{a} = P_{1}$, $\rho_{b} = P_{2}$, with numbers at other sites that make the total zero and drop out of every commutator; it is built from the commuting numbers of the paths, as the source of the stored static coupling is (Proposition \claimref{field-theory.operator-newtonian-coupling}). The constraint is
\[
G_{s} = (\mathrm{div}\,E)_{s} - g\,\rho_{s} \quad\text{at every site } s,
\]
and an \emph{observable} is an element that commutes with every $G_{s}$. Let $\chi$ be the unit string on the links of a lattice path from $a$ to $b$, $\mathrm{div}\,\chi = \delta_{a} - \delta_{b}$, and $\kappa = \mathrm{grad}\,(\mathrm{div}\,\mathrm{grad})^{-1}\mathrm{div}\,\chi$ its gradient part: $\kappa = K(a) - K(b)$, where $g\,K(s)$ is the solution of the constraint with no curl for the quantum at $s$. For a function $f$ on the links with $\mathrm{div}\,f = \delta_{a} - \delta_{b}$ put $X_{f} = v\,W(gf) - w\,W(-gf)$, the recombiner $U_{f} = p + q\,X_{f}$ ($p^{2} + q^{2} = 1$) and the detection $O_{f} = U_{f}^{-1}P_{1}U_{f}$; the bare ones are $U = p + q\,e_{2}$, $O = U^{-1}P_{1}U$.
\begin{enumerate}
\item[(1)] \emph{(Dressing; proved.)} $[G_{s}, U] = -g\,q\,(\delta_{sa} - \delta_{sb})\,e_{1}$: the bare recombiner is not an observable. $X_{f}^{2} = -1$, $U_{f}^{-1} = p - q\,X_{f}$, and $U_{f}$ and $O_{f} = p^{2}P_{1} + q^{2}P_{2} + pq\,(v\,W(gf) + w\,W(-gf))$ commute with every $G_{s}$, for $f = \chi$ and for $f = \kappa$.
\item[(2)] \emph{(The field with its own variables, string dressing; proved.)} $[E_{l}, O_{\chi}] = g\,pq\,\chi_{l}\,X_{\chi}$: the string-dressed detection commutes with the field on every link off the string, and fails to on the string.
\item[(3)] \emph{(The two parts; proved.)} Let $E^{L} = \mathrm{grad}\,(\mathrm{div}\,\mathrm{grad})^{-1}\mathrm{div}\,E$ and $E^{T} = E - E^{L}$. On states annihilated by the constraint $E^{L}_{l} = g\sum_{s}K_{l}(s)\,\rho_{s}$, an element of the matter algebra. Then $[E^{L}_{l}, O_{\chi}] = g\,pq\,\kappa_{l}\,X_{\chi}$ and $[E^{T}_{l}, O_{\chi}] = g\,pq\,(\chi_{l} - \kappa_{l})\,X_{\chi}$. In the box of $7 \times 7$ sites with $a$, $b$ two links apart on its middle row, $\kappa_{l} \neq 0$ on $76$ of the $82$ links off the string (the other six lie on the bisector of $a$ and $b$): the constrained part alone and the transverse part alone each fail to commute with the detection there, by opposite amounts.
\item[(4)] \emph{(The field with no variable of its own; proved.)} If the field has no transverse variable, the algebra of the model is the matter algebra, every element of it is an observable, the field is $E_{l} = g\,\kappa_{l}\,P_{1}$ plus a number, and $[E_{l}, O] = g\,\kappa_{l}\,pq\,e_{2}$: nonzero on the same $76$ links. This is clause (2) of the stored model with the function of the event fixed by the constraint: it is the difference of the constrained fields of the two paths.
\item[(5)] \emph{(Which dressing; proved.)} With the field's own variables, the detection dressed by the constrained field satisfies $[E_{l}, O_{\kappa}] = g\,pq\,\kappa_{l}\,X_{\kappa}$ and fails on the same $76$ links. Commutation off its support holds for the string-dressed detection, whose support is the string; the support of $O_{\kappa}$ is every link where $\kappa \neq 0$.
\item[(6)] \emph{(One space dimension; proved.)} On a chain every function on the links is a gradient, so $\kappa = \chi$: the constrained fields of the two paths differ only between $a$ and $b$, and the field with no variable of its own commutes with the detection on every link outside that interval.
\item[(7)] \emph{(Dynamics; computed.)} Let the field evolve by the lattice Maxwell equations in the temporal gauge with step $h = \tfrac12$, $E(n+1) = E(n) + h\,\mathrm{curl}^{T}\mathrm{curl}\,A(n)$, $A(n+1) = A(n) - h\,E(n+1)$, a canonical map that preserves the constraint and has an exact cone (a step reaches only links that share a plaquette), the quantum at rest. Then $[E_{l}(n), O_{\chi}(n_{d})] = pq\,S_{l}(n)\,X_{\chi}$ with $S(n)$ the solution with data $E = g\chi$, $A = 0$ at step $n_{d}$. In the box of $13 \times 13$ sites, $a$ and $b$ two links apart, $n_{d} = 5$, $0 \le n \le 10$: $S_{l}(n) = 0$ at all $2750$ events whose link is further from the string, in steps of the cone, than $|n - n_{d}|$. The slaved field of the constrained model, $E^{\mathrm{sl}}(n) = P_{1}E^{(a)}(n) + P_{2}E^{(b)}(n)$ with $E^{(a)}$, $E^{(b)}$ the solutions for the quantum moved at step $0$ from the site between them to $a$ or to $b$ (each satisfies the constraint at every step, and it is the retarded field of the operator charge), has $[E^{\mathrm{sl}}_{l}(n), O] = (E^{(a)} - E^{(b)})_{l}(n)\,pq\,e_{2}$, nonzero at $878$ of those $2750$ events, all at steps $n \ge 4$.
\end{enumerate}
\emph{Reading (argued).} The stored model had no constraint, and its text says that for a gauge field the instantaneous part is fixed by a constraint and the observables that commute are dressed ones. This model has both. What it shows: a constraint and the dressing of observables do not by themselves give commutation of the field with matter observables at spacelike separation. If the field has no variable of its own, it is the constraint's solution, an element of the matter algebra, and its commutator with the detection is the difference of the two paths' constrained fields times the stored matter factor ((4), and (7) for the retarded field); that difference vanishes outside the source only in one space dimension ((6)), where a gauge field has no transverse part. If the field has transverse variables with canonical commutators, there is a dressing with compact support, the string, and the detection dressed by it commutes with the field at every spacelike event ((2), (7)); the constrained part and the transverse part fail separately and cancel ((3)), the counterpart here of the cancellation between response and commutator function in the stored model. The string dressing is an operator that shifts the transverse field, so it does not exist without those variables, and such a pair is canonical, which no floor of the tower holds (\claimref{field-theory.no-canonical-commutation-relations-tower}). For the gravitational gauge field the charge is the energy and momentum, the constraint equations are the four first-order equations without second time derivative, and a rearrangement of an isolated source keeps its total energy and momentum, so the constrained fields of two paths agree in their monopole and dipole parts and differ from the quadrupole on (standard, cited from memory): the difference falls off faster than in this model but is not zero outside the source. A dressing of compact support for such a rearrangement differs from the constrained field by a transverse trace-free configuration, that is by a state of the two components that the source does not fix (argued; the model has a scalar charge and no spin two). So the model sharpens the open question without settling it: if the series requires its gravitational field to commute with matter observables at spacelike separation, the constraint structure of the gauge field and dressed observables do not meet the requirement for a field with no variable of its own; they meet it when the two free components have canonical variables.

## technical
A lattice Maxwell field in two space dimensions with a Gauss constraint, coupled to one quantum on two sites whose charge is built from the commuting path numbers. Observables commute with the constraint.

The bare recombiner of the stored model is not an observable. Dressed by a string of flux between the two sites it is, and with the field's own variables the string-dressed detection commutes with the electric field on every link off the string ($82$ of $84$ in a $7 \times 7$ box), exactly.

Split the field into its constrained (gradient) part, which on the constraint surface is an element of the matter algebra, and its transverse part. Each alone fails to commute with the detection on $76$ of the $82$ links; the two cancel.

If the field has no variable of its own it is the constrained part, and it fails on those $76$ links: the constraint fixes which function of the event multiplies the stored matter factor, the difference of the two paths' constrained fields, and does not remove it. In one space dimension that difference vanishes outside the two sites.

A detection dressed by the constrained field, instead of the string, fails on the same links even when the field has its own variables.

With an exact cone ($13 \times 13$ box, detection at step $5$): the string-dressed detection commutes with the field at all $2750$ spacelike events; the slaved retarded field of the constrained model fails at $878$ of them while satisfying the constraint at every step.

Ledger: transport-absent. Standard lattice gauge theory and the standard facts about dressed charges, in an exact finite model; the series contributes the question.

## lay
An earlier result in the series built a small exact model in which a field that only repeats what its source did fails a basic test of locality, and noted that the model lacked a feature of gravity and of electromagnetism: part of such a field is tied to its source at every instant by a constraint, and the things one can measure are matter together with its attached field.

This result adds that feature. It uses a lattice version of the electromagnetic field, where the constraint is the law that ties the electric field to the charge.

The outcome is that the feature does not rescue a field with no freedom of its own. Such a field, at a distance, still carries the information of which path the particle took, at once, and still fails the test, in all but a one-dimensional world. What rescues it is the part of the field that is free of the constraint, the part that makes waves, provided it is a quantum variable in its own right: then there is a way of attaching field to matter that stays local, and the test is passed everywhere.

The model is electromagnetic, not gravitational, and the step to gravity is an argument, not a computation. The series has not said whether it requires gravity to pass this test; this result says what passing it would take.

## one-liner
In an exact lattice Maxwell model with a Gauss constraint and one quantum on two sites, the string-dressed detection commutes with the electric field off the string ($82$ of $84$ links; all $2750$ spacelike events with an exact cone) when the field has its own variables, the constrained and transverse parts failing separately on $76$ links and cancelling; a field with no variable of its own is the constrained part and fails on those $76$ links (and its retarded form at $878$ spacelike events), except in one space dimension: the constraint and dressed observables do not restore commutation, the transverse variables do.
