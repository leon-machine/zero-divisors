---
id: synthesis.inverse-frame-free-tractor-gauge-field-preserves-a-frozen-point
kind: claim
version: 2
title: 'An equivalent reading of the field-space premise in the gauge group of gauge theory gravity: a $\Cl(2,4)$ gauge field assembled from $(\hb, \Omega)$ and no further field (T), covariant under that group, soldered, and either polynomial with no inverse frame (P) or built without derivatives (O), is $\Omega - \nInf \wedge e + \rho\,\nO \wedge e$ with $\rho$ constant, which preserves the constant tractor $I_{\rho} = \nInf + \rho\,\nO$, $\ip{X}{I_{\rho}} = 1$, for every gravitational field; neither (P) nor (O) suffices without (T), the series'' tractor transport violates both and meets the family exactly on Einstein fields, and under the parabolic group the reduction is a gauge choice, so this is a premise exchange, not a derivation'
status: proved
region: synthesis
subject: einstein
tags: [tractors, gauge-fields, forcing-and-uniqueness]
proposed_by:
  kind: ai
  session: 2026-11-01-field-space
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.imported-gtg-dictionary@1
  - synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection@1
  - dark-energy.frozen-point-makes-stelle-west-vector@5
  - dark-energy.walls-free-sector@5
  - dark-energy.frozen-point-datum-kasner-wall@7
  - synthesis.frozen-point-field-space-is-the-gtg-pair-and-its-omega-equation-is-the-torsion-equation@2
  - synthesis.imported-holonomy-reductions-of-cartan-geometries@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_displacement_weight_bounds_the_slot_only_without_inverse_frame
- kind: check
  ref: check.py::check_lorentz_equivariant_maps_between_the_slots
- kind: check
  ref: check.py::check_the_admissible_field_determines_the_frozen_point
- kind: check
  ref: check.py::check_normal_tractor_connection_meets_the_family_only_on_einstein_fields
- kind: check
  ref: check.py::check_wall_regularity_separates_the_family_from_the_normal_connection
- kind: check
  ref: check.py::check_an_independent_slot_field_leaves_no_parallel_tractor
- kind: check
  ref: check.py::check_a_parallel_tractor_of_unit_pairing_is_gauged_to_the_constant_frozen_point
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.curvature-only-tractor-actions-are-macdowell-mansouri
  - synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared
extraction:
  open_problem: op.derive-gravitational-action
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 1 -> 2: the "filed alongside" citations are now claimrefs; the GTG-pair bijection, cited in (ii) and used in the converse of (vi), is a uses edge (it does not depend on this result), with the clause numbers corrected to the final numbering of that result (bijection (ii), Omega-equation (i)) in the note and the proof; the slot lattice and the infinite-stiffness result stay text only (the lattice depends on this result; the stiffness result is a parenthetical reading). The Reading (vi) names the field-space premise synthesis.field-space-premise-parallel-frozen-point (text only, no assumes edge: this result is a reading of it) and cites the imported Cap-Gover-Hammerl Fact for the holonomy-reduction form (uses edge). Coverage records both new premises as untouched. Statement unchanged.'
  note: >-
    A premise exchange, not a derivation: an equivalent reading, in the gauge group of gauge theory gravity,
    of the field-space premise "the varied gravitational connection admits a parallel tractor I with
    <X, I> = 1". Turns the slot step of clause (vi) of the curvature-only classification (there argued by
    degree counting) into a proof, with the no-inverse-frame hypothesis (P) and the order-zero hypothesis (O)
    as alternatives under the two-field premise (T), and states exactly what it assumes. Related results: \claimref{synthesis.frozen-point-field-space-is-the-gtg-pair-and-its-omega-equation-is-the-torsion-equation} (clause (ii), the bijection of gauge-theory-gravity pairs with the I-preserving connections, used in (ii) and (vi); clause (i), the Omega-equation is the torsion equation, so the independence of hb and Omega decides only the torsion equation), \claimref{synthesis.frozen-point-integrand-gives-einstein-only-with-the-symmetric-slot-frozen} (the freely varied slot returns the Schouten slot) and \claimref{synthesis.frozen-point-reduces-the-connection-only-when-infinitely-stiff} (a dynamical frozen point reduces the connection only in the infinitely stiff limit). The premise itself is recorded as \claimref{synthesis.field-space-premise-parallel-frozen-point}. The hypotheses
    mention neither the frozen point nor its norm nor any field equation; the frozen point comes out up to
    the one constant rho, which the registered input N fixes (Lambda = 6 rho). Neither (P) nor (O) is
    supplied by transport: the series' tractor transport satisfies (T), (G), (S) and violates both, in the
    special-conformal slot only. (T) is the stored definition of a gravitational field as the pair
    (hb, Omega); without it (P) admits an independent slot field and the unreduced field space. (G) uses the
    gauge group of gauge theory gravity, not the parabolic group the store assigns to the tractor field;
    under the latter the reduction is a gauge choice. Transport-convenient: the tractor frame and the
    comparison with the normal tractor connection are the series'; the forcing is displacement-weight
    counting or frame transitivity with Lorentz representation theory.
---

## formal
Work in $\Cl(2,4)$ with $\nO = \tfrac12(e_{4} + e_{5})$, $\nInf = e_{4} - e_{5}$ ($\nO \cdot \nInf = 1$), $W = \{\nO, \nInf\}^{\perp}$ the spacetime vectors, and canonical tractor $X = \nO$, as in Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}. Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}, clauses (a) to (e); its field equations (f) are not used) with soldering form $e(a) = \hb^{-1}(a)$. Every bivector-valued one-form on flat spacetime is uniquely
\[
A(a) \;=\; L(a) + b(a)\,\nO \wedge \nInf - \nInf \wedge \tau(a) + \nO \wedge S(a), \qquad L(a) \in \Lambda^{2}W,\ b(a) \in \R,\ \tau(a), S(a) \in W
\]
(the Lorentz, dilation, translation and special-conformal slots). Consider the hypotheses:
\begin{enumerate}
\item[(T)] \emph{(Two gauge fields.)} Each slot at $x$ is given by a rational expression in the components at $x$ of $\hb$, $\Omega$ and finitely many of their partial derivatives (as is every construction from the frame, its inverse, contractions and the Hodge dual), with coefficients that may depend on $x$, and involves no further field.
\item[(G)] \emph{(Gauge covariance under the group of gauge theory gravity.)} Under the rotation gauge (rotor fields $U$ of the Lorentz group of $W$, which fix $\nO$ and $\nInf$) and the affine displacements $x \mapsto Mx + c$, with the laws of Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}(e), $A$ transforms as $\Omega$ does: $A \mapsto UA\tilde U - 2(a \cdot \nabla U)\tilde U$ and $A(a; x) \mapsto A(Ma; Mx + c)$. The dilation and special-conformal rotors, which the store also uses to gauge the tractor field (Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}, closing paragraph), are not imposed.
\item[(S)] \emph{(Soldering.)} $A(a) \times X = e(a)$.
\item[(P)] \emph{(No inverse frame.)} The expression in (T) is a polynomial in the components of $e$, $\Omega$ and their derivatives; $\hb$, the inverse of the soldering form, does not occur.
\item[(O)] \emph{(Order zero.)} The expression in (T) involves no derivatives of $\hb$ or $\Omega$ ($\hb$ itself may occur).
\end{enumerate}
Write $I_{\rho} = \nInf + \rho\,\nO$, so that $Q(I_{\rho}) = 2\rho$, and $A_{\rho}(a) = \Omega(a) - \nInf \wedge e(a) + \rho\,\nO \wedge e(a)$.
\begin{enumerate}
\item[(i)] \emph{(Forcing; proved.)} Under (T), (G), (S) and either (P) or (O), $A = A_{\rho}$ for a real constant $\rho$: the dilation slot vanishes, the Lorentz slot is $\Omega$ with coefficient one, and the special-conformal slot is $\rho\,e$. Both routes end in the same Lorentz-commutant lemma: the Lorentz-equivariant linear maps $W \to W$ are the multiples of the identity, and those $W \to \R$, $W \to \Lambda^{2}W$, $\Lambda^{2}W \to W$, $\Lambda^{2}W \to \R$ vanish. Under (P) the slots are reduced to linear ones by displacement weight; under (O) by transitivity of the linear displacements on frames.
\item[(ii)] \emph{(The field space fixes the point; proved.)} For every gravitational field and every $\rho$, $A_{\rho}(a) \times I_{\rho} = 0$, so the constant tractor $I_{\rho}$ is parallel, and the vectors annihilated by every $A_{\rho}(a)$ form exactly the line of $I_{\rho}$, for every invertible frame. For $\rho \neq 0$, with $\Lambda := 6\rho$, $I_{\rho}$ is the frozen point $\nInf + \tfrac{\Lambda}{6}\nO$ of Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector}; no field equation is imposed. That the $A_{\rho}$ are exactly the connections preserving $I_{\rho}$ (a bijection with the pairs $(\hb^{-1}, \Omega)$) is clause (ii) of Theorem \claimref{synthesis.frozen-point-field-space-is-the-gtg-pair-and-its-omega-equation-is-the-torsion-equation}.
\item[(iii)] \emph{(The series' transport; proved.)} The tractor gauge field $\Omega_{T}$ of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection} satisfies (T), (G), (S) and neither (P) nor (O): its special-conformal slot $\Sch(e(a))$ involves derivatives of $\Omega$, and with the field strength of $\Omega$ fixed it is homogeneous of degree $-1$ under $e \mapsto c\,e$; at a frame of corank one it generically has a pole. In the splitting of $\hb$, $\Omega_{T} = A_{\rho}$ exactly when $\Omega$ is torsion-free and $\Sch = \rho\,\mathrm{id}$, that is on Einstein fields with $\Lambda = 6\rho$ (Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}(ii)). A gauge transformation by a rotor field $g$ of $\Cl(2,4)$ carries parallel tractors to parallel tractors, so a normal tractor connection with no parallel tractor is gauge equivalent to no $A_{\rho}$. So the field space presupposes no Einstein condition: for $\Omega_{T}$ the parallelism of $I_{\rho}$ is the Einstein condition, for $A_{\rho}$ it is an identity.
\item[(iv)] \emph{(Which hypotheses do the work; proved.)} Without (P) and (O), $\Omega_{T}$ is admissible. Without (T), a special-conformal slot that is a field of its own satisfies (P), (G) and (S), no constant tractor is annihilated by every $A(a)$, and for generic first jets of $(e, \Omega, S)$ the field strength annihilates no vector, so no tractor is parallel (the unreduced field space; read as a Higgs field on that space, the frozen point reduces the connection only in an infinitely stiff limit, as shown in Theorem \claimref{synthesis.frozen-point-reduces-the-connection-only-when-infinitely-stiff}; varied freely in the frozen-point integrand, that slot returns the Schouten slot of the normal tractor connection, as shown in Theorem \claimref{synthesis.frozen-point-integrand-gives-einstein-only-with-the-symmetric-slot-frozen}(ii)). Without the restriction of (G) to the group of gauge theory gravity: a special-conformal rotor $U$ (which fixes $X$) carries $A_{\rho}$ to a connection preserving the non-constant tractor $U I_{\rho}\tilde U$, with $\ip{X}{U I_{\rho}\tilde U} = 1$, so the family is not invariant under the parabolic group the store assigns to the tractor field, and under that group the reduction is a gauge choice: the invariant content is that the connection admits a parallel tractor with nonzero pairing with $X$, and (T), (G) select the gauge in which it is constant. What (T) and (G) add is that the dilation and special-conformal directions carry neither a field nor a gauge freedom of their own, so that $A_{\rho}$ depends on $\hb$ and not only on its conformal class. Under (T), (G) and (P) or (O), $\Omega$ is moreover a field independent of $\hb$: a Lorentz slot that is a function of the frame alone would by step 1 of (i) be linear in the undifferentiated frame and so carry no inhomogeneous rotation term. That this independence decides only the torsion equation, not the frozen point, is clause (i) of Theorem \claimref{synthesis.frozen-point-field-space-is-the-gtg-pair-and-its-omega-equation-is-the-torsion-equation}.
\item[(v)] \emph{(A series reading of (P); argued.)} Transport does not supply (P) or (O), by (iii). The series meets frames of corank one at the walls of Theorem \claimref{dark-energy.walls-free-sector}, where $\hb$ fails and the equations are used because they are polynomial in $e$. A rational expression of (T) has denominators powers of $\det e$; since $\det$ is irreducible and its zero set has smooth real points of corank one, an expression bounded at such points is a polynomial. So (W), \emph{the tractor gauge field is defined at frames of corank one, with $\Omega$ regular there}, with (T), (G) and (S) implies (P), and with it (i) and (ii). (W) is the series' stance only at these corank-one walls: at the Kasner wall the stored frozen-point datum has a simple pole in the Levi-Civita block with divergent curvature invariants, so not a gauge artefact (Proposition \claimref{dark-energy.frozen-point-datum-kasner-wall}), and there the series lets the equations reach the wall as conditions on the residue rather than asking the gauge field to be regular (Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector}, consequence 1). The stored polynomiality is that of the action in the connection, $I$ and $V$, which the unreduced field space shares, so it motivates (P) for the assembly only once (T) is granted.
\item[(vi)] \emph{(Reading; proved from (ii) and the bijection of Theorem \claimref{synthesis.frozen-point-field-space-is-the-gtg-pair-and-its-omega-equation-is-the-torsion-equation}(ii).)} The premise ``the varied gravitational connection admits a parallel tractor $I$ with $\ip{X}{I} = 1$'' (Premise \claimref{synthesis.field-space-premise-parallel-frozen-point}; by Fact \claimref{synthesis.imported-holonomy-reductions-of-cartan-geometries}(a) a holonomy reduction of the connection to the stabiliser of $I$) and the hypotheses (T), (G), (S) with (P) or (O) describe the same field space: $A_{\rho}$ has the parallel tractor $I_{\rho}$ with $\ip{X}{I_{\rho}} = 1$; conversely, for a connection with nondegenerate soldering and a parallel $I$ with $\ip{X}{I} = 1$, $Q(I) = 2\rho$ is constant, a special-conformal gauge transformation (which fixes $X$) makes it the constant $I_{\rho}$, and then the connection is valued in the stabiliser of $I_{\rho}$, hence of the form $A_{\rho}$ for a unique pair by clause (ii) of Theorem \claimref{synthesis.frozen-point-field-space-is-the-gtg-pair-and-its-omega-equation-is-the-torsion-equation}, which satisfies all the hypotheses. So the result exchanges one statement of the premise for another; it does not derive it from transport.
\end{enumerate}

## technical
The open problem asks why the gravitational action should be varied over $\Cl(2,4)$ connections that preserve the frozen point $I$, given that on the series' own transport, the normal tractor connection, preserving $I$ is the Einstein condition. This result restates that field space by hypotheses that mention neither $I$ nor any field equation; it is a premise exchange, an equivalent reading of the premise that the varied connection admits a parallel tractor $I$ with $\ip{X}{I} = 1$, not a derivation from transport. Build a $\Cl(2,4)$ gauge field from the two gauge fields of gauge theory gravity and nothing else, the position-gauge field $\hb$ (through its soldering form $e = \hb^{-1}$) and the rotation-gauge field $\Omega$; require it to transform as a gauge field under the rotations and displacements of gauge theory gravity; solder the canonical tractor to the frame; and either forbid the inverse frame $\hb$ or forbid derivatives. Either restriction makes every slot linear in $e$ and $\Omega$ (by displacement weight, or by moving any frame to any other with a linear displacement), and Lorentz covariance then leaves exactly $A_{\rho} = \Omega - \nInf \wedge e + \rho\,\nO \wedge e$ with $\rho$ constant. This field annihilates the constant tractor $\nInf + \rho\,\nO$ for every gravitational field, and nothing else, with $\Lambda = 6\rho$ left to the registered input. Conversely every connection with a parallel tractor of unit pairing with $X$ takes this form in a suitable gauge, so the two statements of the premise are equivalent.

The series' transport has the Schouten map in the last slot, which needs both derivatives and the inverse frame: it scales as $1/c$ when the frame is scaled by $c$ and has a pole where the frame drops rank. It coincides with $A_{\rho}$ exactly on Einstein fields, so the restriction that would assume the answer is never made. The limits are stated: without the two-field premise an independent special-conformal field is also polynomial and preserves no tractor, and a frozen point treated as a Higgs field reduces the connection only when infinitely stiff; and the covariance asked for is that of gauge theory gravity, not the larger parabolic group with which the store gauges the tractor field, under which the reduction is only a choice of gauge for a connection that admits a parallel tractor. Transport supplies neither restriction; the one series reading of the first is that the gauge field be defined on the corank-one walls where the frame degenerates, which the series asks for there but not at the Kasner wall.

## lay
Earlier work found that the series' formula for gravity gives Einstein's equations only if one assumes in advance which shapes of the gravitational field are allowed: those that keep a special fixed direction, the frozen point, unchanged. This result asks what could justify that assumption without assuming Einstein's equations. It builds the six-dimensional field from the two ingredients of gauge theory gravity and nothing else, and adds one rule: never divide by the frame that measures lengths, or alternatively never use rates of change. Either rule forces the field into a single form, and every field of that form keeps one fixed direction unchanged, which is the frozen point. So these rules are another way of stating the assumption, not a reason for it. The series' own way of carrying directions from point to point breaks both rules, and agrees with the forced form only where Einstein's equations already hold. The rules are not derived from the series, and they work only together with the premise that there are just two ingredients.

## one-liner
Premise exchange (an equivalent reading of the field-space premise, a parallel tractor $I$ with $\ip{X}{I} = 1$, in the gauge group of gauge theory gravity): a $\Cl(2,4)$ gauge field built from $(\hb, \Omega)$ and no further field (T), covariant under the gauge group of gauge theory gravity, with $A \times X = \hb^{-1}$, and either polynomial with no inverse frame (P) or free of derivatives (O), is $\Omega - \nInf \wedge e + \rho\,\nO \wedge e$ with $\rho$ constant (linearity by displacement weight or by frame transitivity; Lorentz commutants fix the slots), which annihilates exactly the line of $I_{\rho} = \nInf + \rho\,\nO$ for every field, so the connections preserving the frozen point ($\Lambda = 6\rho$) follow without the Einstein condition; the series' tractor transport violates (P) and (O) (Schouten slot of frame degree $-1$, a pole at corank-one frames) and equals the family only on Einstein fields; (T) is needed, and under the parabolic group with which the store gauges the tractor field the reduction is a gauge choice; (P) is not supplied by transport, its series reading being regularity at the corank-one walls only.
