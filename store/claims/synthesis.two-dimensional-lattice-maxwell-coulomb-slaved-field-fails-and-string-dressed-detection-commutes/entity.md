---
id: synthesis.two-dimensional-lattice-maxwell-coulomb-slaved-field-fails-and-string-dressed-detection-commutes
kind: claim
version: 1
title: 'Lattice Maxwell in two dimensions: Coulomb slaved field fails, string dressing commutes'
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
  ref: check.py::check_string_shaped_slaved_field_keeps_the_constraint_and_is_not_static
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
    clause); it is not a model of spin two. Restated after review. The first filing said that the constraint and
    the dressing of observables do not restore commutation for a field with no variable of its own; that was
    stronger than what is shown, in two ways. (a) A field with no variable of its own is not fixed by the
    constraint: its transverse part may be any matter element, and the string-shaped field g chi P1 satisfies the
    constraint and commutes with the detection off the string (clause (5); a counterexample raised in
    review, checked). What fails at equal time is the static slaved field, the Coulomb one; what fails in (7) is the retarded slaved field, fixed by the move at step 0; a slaved field
    obeying the field equation that is string-shaped at the detection step commutes with that detection at all
    spacelike events and fails for a detection at another step (computed for steps 5 and 7). (b) With transverse variables
    the dressings treated are those by one Weyl operator W(g f): the detection then commutes with the field
    exactly off the support of f, so the string succeeds and the Coulomb dressing fails; dressings by sums of
    such operators are not treated. The kill conditions registered before the computation were: the
    string-dressed detection fails to commute with the field off the string (not met); with no transverse
    variable the field commutes with the detection away from the two sites in two space dimensions (not met for
    the Coulomb field, which fails on 76 of 82 links; met by the string-shaped slaved field, which is the
    restatement above); in one space dimension the constrained fields of the two paths differ outside the
    interval (not met). The model is exactly solvable (the dressings are Weyl operators), so its statements hold
    to every order in the coupling. The lattice Hamiltonian formulation of a gauge field, the dressing of a
    charge by its constrained field and the fact that such a dressing is not local are standard (Kogut and
    Susskind 1975; Dirac 1955; cited from memory); the mechanism of clause (7), a retarded field that depends on
    the source operator at an earlier event, which does not commute with the source's later detection, is the
    one named after Yang and Feldman and Peierls in the stored model's note. The transfer to the gravitational
    gauge field in the Reading is argued; the statements there about the multipoles left free by the
    conservation of energy and momentum and about compactly supported solutions of the linearised constraints
    are standard, cited from memory, and are not used in a proof step. The split of the first-order
    gravitational field equation into four constraint equations and two components with a pole on the cone is
    the subject of the result filed alongside this one. Decision for the maintainer, unchanged by this result:
    whether the series requires its gravitational field to commute with matter observables at spacelike
    separation. What this result contributes to it is argued, not proved, for gravity, and depends on the point
    (a): the gravitational constraints likewise leave the transverse trace-free data of the field undetermined,
    so a slaved gravitational field is fixed only by the constraints together with the field equation and a rule
    at null momentum.
---

## formal
\emph{The model.} A box of sites of the square lattice with its links and plaquettes; $\mathrm{div}$, $\mathrm{grad}$ and $\mathrm{curl}$ are the lattice differences, $\mathrm{div}\,\mathrm{grad}$ the graph Laplacian. The field has a pair $(A_{l}, E_{l})$ on each link $l$, entering through the Weyl operators $W(f) = \exp(I_{4}\sum_{l}f_{l}A_{l})$, $f$ a real function on the links, with $W(f)W(f') = W(f + f')$ and $[E_{l}, W(f)] = f_{l}\,W(f)$ (the unit written as in the field theory). Matter is one quantum on two sites $a$, $b$, in the algebra of a completed pair as in Theorem \claimref{synthesis.field-slaved-to-an-operator-source-does-not-commute-at-spacelike-separation}: $\Cl(1,1)$, $v = \tfrac12(e_{1} + e_{2})$, $w = \tfrac12(e_{1} - e_{2})$, $Q(v) = Q(w) = 0$, $P_{1} = vw$ (the quantum at $a$), $P_{2} = wv$ (at $b$), $v = P_{1}vP_{2}$ the move from $b$ to $a$ (\claimref{synthesis.set-and-clear-of-a-bit-generate-the-hyperbolic-plane}). The charge is $\rho_{a} = P_{1}$, $\rho_{b} = P_{2}$, with numbers at other sites that make the total zero and drop out of every commutator; it is built from the commuting numbers of the paths, as the source of the stored static coupling is (Proposition \claimref{field-theory.operator-newtonian-coupling}). The constraint is
\[
G_{s} = (\mathrm{div}\,E)_{s} - g\,\rho_{s} \quad\text{at every site } s,
\]
and an \emph{observable} is an element that commutes with every $G_{s}$. Let $\chi$ be the unit string on the links of a lattice path from $a$ to $b$, $\mathrm{div}\,\chi = \delta_{a} - \delta_{b}$, and $\kappa = \mathrm{grad}\,(\mathrm{div}\,\mathrm{grad})^{-1}\mathrm{div}\,\chi$ its gradient part: $\kappa = K(a) - K(b)$, where $g\,K(s)$ is the solution of the constraint with no curl (the Coulomb field) for the quantum at $s$. For a function $f$ on the links with $\mathrm{div}\,f = \delta_{a} - \delta_{b}$ put $X_{f} = v\,W(gf) - w\,W(-gf)$, the recombiner $U_{f} = p + q\,X_{f}$ ($p^{2} + q^{2} = 1$) and the detection $O_{f} = U_{f}^{-1}P_{1}U_{f}$; the bare ones are $U = p + q\,e_{2}$, $O = U^{-1}P_{1}U$. A \emph{slaved field} is a field with no variable of its own: an assignment to each link of an element of the matter algebra, satisfying the constraint.
\begin{enumerate}
\item[(1)] \emph{(Dressing; proved.)} $[G_{s}, U] = -g\,q\,(\delta_{sa} - \delta_{sb})\,e_{1}$: the bare recombiner is not an observable when the field has its own variables. $X_{f}^{2} = -1$, $U_{f}^{-1} = p - q\,X_{f}$, and $U_{f}$ and $O_{f} = p^{2}P_{1} + q^{2}P_{2} + pq\,(v\,W(gf) + w\,W(-gf))$ commute with every $G_{s}$, for every $f$ with $\mathrm{div}\,f = \delta_{a} - \delta_{b}$.
\item[(2)] \emph{(The field with its own variables: a dressing commutes off its support; proved.)} $[E_{l}, O_{f}] = g\,pq\,f_{l}\,X_{f}$. So the string-dressed detection $O_{\chi}$ commutes with the field on every link off the string and fails to on the string, and the detection $O_{\kappa}$ dressed by the Coulomb field fails on every link where $\kappa_{l} \neq 0$. The dressings treated are those by one Weyl operator; sums of such operators are not treated.
\item[(3)] \emph{(The two parts; proved.)} Let $E^{L} = \mathrm{grad}\,(\mathrm{div}\,\mathrm{grad})^{-1}\mathrm{div}\,E$ and $E^{T} = E - E^{L}$. On states annihilated by the constraint $E^{L}_{l} = g\sum_{s}K_{l}(s)\,\rho_{s}$, an element of the matter algebra. Then $[E^{L}_{l}, O_{\chi}] = g\,pq\,\kappa_{l}\,X_{\chi}$ and $[E^{T}_{l}, O_{\chi}] = g\,pq\,(\chi_{l} - \kappa_{l})\,X_{\chi}$. In the box of $7 \times 7$ sites with $a$, $b$ two links apart on its middle row, $\kappa_{l} \neq 0$ on $76$ of the $82$ links off the string (the other six lie on the bisector of $a$ and $b$): the constrained part alone and the transverse part alone each fail to commute with the string-dressed detection there, by opposite amounts.
\item[(4)] \emph{(The Coulomb slaved field; proved.)} The slaved field with no transverse part, $E_{l} = g\sum_{s}K_{l}(s)\rho_{s} = g\,\kappa_{l}\,P_{1}$ plus a number, is the static solution of the constraint and the field equation. For every element $m$ of the matter algebra, $[E_{l}, m] = g\,\kappa_{l}\,[P_{1}, m]$: it fails to commute, on the $76$ links, with every matter element that does not commute with the charge; for the bare detection $[E_{l}, O] = g\,\kappa_{l}\,pq\,e_{2}$. This is clause (2) of the stored model with the function of the event equal to the difference of the Coulomb fields of the two paths.
\item[(5)] \emph{(The constraint alone does not fix a slaved field; proved.)} The constraint fixes the divergence of a slaved field and leaves its transverse part free. $E_{l} = g\,\chi_{l}\,P_{1}$ plus a number is a slaved field, and $[E_{l}, O] = g\,\chi_{l}\,pq\,e_{2}$ vanishes on every link off the string. So at equal time the failure of (4) belongs to the Coulomb field, not to every slaved field. The string-shaped field is not a static solution of the field equation (after two steps of (7) it has changed on $10$ links of the small box, while the Coulomb field is unchanged), and under the field equation the gradient part of what it becomes is $g\kappa P_{1}$ at every step.
\item[(6)] \emph{(One space dimension; proved.)} On a chain every function on the links is a gradient, so $\kappa = \chi$ and there is no transverse part: the slaved field is unique, it differs between the two paths only between $a$ and $b$, and it commutes with every matter element on every link outside that interval.
\item[(7)] \emph{(Dynamics; computed.)} Let the field evolve by the lattice Maxwell equations in the temporal gauge with step $h = \tfrac12$, $E(n+1) = E(n) + h\,\mathrm{curl}^{T}\mathrm{curl}\,A(n)$, $A(n+1) = A(n) - h\,E(n+1)$, a canonical map that preserves the constraint and has an exact cone (a step reaches only links that share a plaquette), the quantum at rest. With the field's own variables, $[E_{l}(n), O_{\chi}(n_{d})] = pq\,S_{l}(n)\,X_{\chi}$ with $S(n)$ the solution with data $E = g\chi$, $A = 0$ at step $n_{d}$. In the box of $13 \times 13$ sites, $a$ and $b$ two links apart, $n_{d} = 5$, $0 \le n \le 10$: $S_{l}(n) = 0$ at all $2750$ events whose link is further from the string, in steps of the cone, than $|n - n_{d}|$ (events spacelike to the detection). The retarded slaved field, $E^{\mathrm{sl}}(n) = P_{1}E^{(a)}(n) + P_{2}E^{(b)}(n)$ with $E^{(a)}$, $E^{(b)}$ the solutions for the quantum moved at step $0$ from the site between them to $a$ or to $b$ (each satisfies the constraint at every step; it is the retarded field of the operator charge, and at step $0$ it is the string-shaped field of (5)), has $[E^{\mathrm{sl}}_{l}(n), O] = (E^{(a)} - E^{(b)})_{l}(n)\,pq\,e_{2}$, nonzero at $878$ of those $2750$ events, all at steps $n \ge 4$. Every one of the $878$ lies in the forward cone of the source event (the string at step $0$) and outside the cone of the detection. The failure is carried by the charge $P_{1}$ at the source event, which does not commute with the detection of the same quantum five steps later, a timelike pair; the field at a later event in the source's forward cone is a function of that charge. None of the $878$ events is spacelike to the source.
\end{enumerate}
\emph{Remark (a slaved field fitted to one detection; computed).} Obeying the field equation does not by itself make a slaved field fail. The slaved field $N(n) + S(n)\,P_{1}$, with $S$ the solution of (7) that is $g\chi$ at the detection step $n_{d} = 5$ and $N$ a number solution completing the constraint, satisfies the constraint and the field equation at every step, and its commutator with the detection at step $5$ is $S_{l}(n)\,pq\,e_{2}$, zero at all $2750$ spacelike events. It is fitted to that detection's time: against a detection at step $7$ it fails at $86$ of the $2562$ events spacelike to that one. What (7) shows to fail is the retarded slaved field, the one fixed by the move at step $0$.
\emph{Reading (argued).} The stored model had no constraint, and its text says that for a gauge field the instantaneous part is fixed by a constraint and the observables that commute are dressed ones. This model has both, in two space dimensions. What it shows is narrower than a general statement about constraints and dressings. For a field with no variable of its own: the constraint does not fix the field ((5)); the static slaved field, the Coulomb one, fails to commute with the detection at a distance ((4)); a slaved field can be chosen that commutes off the string at one time, and the retarded one that obeys the field equation fails at spacelike events at later times ((7)); a slaved field obeying the field equation commutes with a given detection only if it is fitted to that detection's time, by the same mechanism as in the stored model, the field in the source's forward cone being a function of the source operator at the earlier event. In one space dimension, where a gauge field has no transverse part, there is no failure outside the interval ((6)). For a field with transverse variables and canonical commutators: a detection dressed by one Weyl operator commutes with the field off the support of the dressing, so the string dressing gives commutation at every spacelike event and the Coulomb dressing does not ((2), (7)); the constrained part and the transverse part fail separately and cancel ((3)), the counterpart here of the cancellation between response and commutator function in the stored model. The string dressing is an operator that shifts the transverse field, so it does not exist without those variables, and such a pair is canonical, which no floor of the tower holds (\claimref{field-theory.no-canonical-commutation-relations-tower}). For the gravitational gauge field the following is argued and not shown by this model, which has a scalar charge and no spin two. The charge is the energy and momentum, the constraint equations are the four first-order equations without second time derivative, and they leave the transverse trace-free data of the field undetermined, as the constraint here leaves the transverse part. A rearrangement of an isolated source keeps its total energy and momentum, so the constrained fields of two paths agree in their monopole and dipole parts and differ from the quadrupole on (standard, cited from memory). A dressing of compact support for such a rearrangement differs from the constrained field by a transverse trace-free configuration. If the series requires its gravitational field to commute with matter observables at spacelike separation, the model suggests that a retarded slaved field would not meet the requirement and that canonical variables for the two free components, with a dressing of compact support, would; this is a suggestion by analogy and settles nothing.

## technical
A lattice Maxwell field in two space dimensions with a Gauss constraint, coupled to one quantum on two sites whose charge is built from the commuting path numbers. Observables commute with the constraint.

With the field's own variables: the bare recombiner of the stored model is not an observable; dressed by one Weyl operator $W(gf)$, $\mathrm{div}\,f = \delta_{a} - \delta_{b}$, it is, and the dressed detection commutes with the electric field exactly off the support of $f$. The string dressing commutes on all $82$ links off the string of a $7 \times 7$ box; the Coulomb dressing fails on $76$ of them. Split into its constrained (gradient) part and its transverse part, the field fails in each part alone on those $76$ links for the string-dressed detection, and the two cancel.

With no variable of its own: the constraint fixes only the divergence of the field. The static choice, the Coulomb field, fails to commute on the $76$ links with every matter element that does not commute with the charge. A string-shaped slaved field satisfies the constraint and commutes off the string, but is not a solution of the field equation at rest.

With an exact cone ($13 \times 13$ box, detection at step $5$): the string-dressed detection commutes with the field at all $2750$ spacelike events; the retarded slaved field obeying the field equation fails at $878$ of them. All $878$ lie in the forward cone of the source event: the failure is that of the source operator with its own later detection, carried outward by the retarded field; none is spacelike to the source.

On a chain there is no transverse part and the slaved field commutes outside the interval between the two sites.

Ledger: transport-absent. Standard lattice gauge theory and the standard facts about dressed charges, in an exact finite model; the series contributes the question.

## lay
An earlier result in the series built a small exact model in which a field that only repeats what its source did fails a basic test of locality, and noted that the model lacked a feature of gravity and of electromagnetism: part of such a field is tied to its source at every instant by a constraint, and the things one can measure are matter together with its attached field.

This result adds that feature, using a lattice version of the electromagnetic field on a flat two-dimensional grid, where the constraint is the law that ties the electric field to the charge.

The outcome has three parts. First, a field with no freedom of its own is not pinned down by the constraint alone; the natural choice, the ordinary static field of the charge, fails the test at a distance. Second, one can choose such a field so that it passes the test at one moment, but if it is made to obey the field's law of motion starting from the particle's earlier move, it fails later, at places that light from the particle's earlier position has reached and light from the later measurement has not. Third, if the wave-making part of the field is a quantum variable in its own right, there is a way of attaching field to matter, a thin line of field between the two positions, for which the test is passed everywhere; attaching the ordinary static field does not pass it. On a one-dimensional line none of the failures occur.

The model is electromagnetic, not gravitational, and the step to gravity is an argument by analogy. The series has not said whether it requires gravity to pass this test.

## one-liner
In an exact two-dimensional lattice Maxwell model with a Gauss constraint and one quantum on two sites: with no variable of its own, the Coulomb slaved field fails to commute, on $76$ of $82$ links, with every matter element that does not commute with the charge, and the retarded slaved field obeying the field equation fails at $878$ of $2750$ spacelike events, all in the source's forward cone (a string-shaped slaved field satisfies the constraint and commutes at one time; on a chain nothing fails outside the interval); with canonical transverse variables the string-dressed detection commutes at all $2750$ and the Coulomb-dressed one does not: the constraint and the Coulomb dressing do not restore commutation in two dimensions, canonical transverse variables with a string dressing do.
