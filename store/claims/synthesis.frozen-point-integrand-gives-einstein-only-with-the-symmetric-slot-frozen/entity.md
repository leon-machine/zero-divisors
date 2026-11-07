---
id: synthesis.frozen-point-integrand-gives-einstein-only-with-the-symmetric-slot-frozen
kind: claim
version: 2
title: 'The frozen-point integrand gives Einstein only with the symmetric slot frozen'
status: proved
region: synthesis
subject: einstein
tags: [tractors, gauge-fields, curvature-and-field-equations, forcing-and-uniqueness]
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
  - dark-energy.frozen-point-makes-stelle-west-vector@7
  - synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection@1
  - synthesis.imported-gtg-dictionary@2
  - synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared@4
  - synthesis.curvature-only-tractor-actions-are-macdowell-mansouri@3
  - synthesis.imported-lovelock-and-anderson-duchamp-natural-lagrangians@1
  - synthesis.imported-conformal-gravity-bach-equations-and-conformal-gauge-form@1
  - synthesis.inverse-frame-free-tractor-gauge-field-preserves-a-frozen-point@2
  - synthesis.imported-holonomy-reductions-of-cartan-geometries@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_integrand_sees_only_the_lorentz_block_and_the_blade
- kind: check
  ref: check.py::check_free_slot_returns_the_schouten_slot_and_the_weyl_square
- kind: check
  ref: check.py::check_slot_lattice
- kind: check
  ref: check.py::check_quadratic_remainders_are_not_variationally_trivial
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.curvature-only-tractor-actions-are-macdowell-mansouri
  - synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared
  - synthesis.stelle-west-norm-is-no-local-output
extraction:
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: synthesis.imported-gtg-dictionary repinned 1 -> 2 after reviewing its correction of the component reading in clause (iv) to R(g_mu ^ g_nu) = -R(e_mu ^ e_nu), agreeing with the store''s sign R(B) = -R(hb(B)) the clause already stated, with GA wording in (ii) and (iv); the translation rules are unchanged; the use here holds as cited.'
  open_problem: op.derive-gravitational-action
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 1 -> 2: the citations of the inverse-frame-free forcing (clause (v), the forcing under (T)) and of the GTG-pair bijection are now claimrefs; the forcing is a uses edge (it does not depend on this result), the bijection stays text only (it is recomputed here). The invariant form of the premise in (v) now names the field-space premise synthesis.field-space-premise-parallel-frozen-point (text only, no assumes edge: this result is a reading of it) and cites the imported Cap-Gover-Hammerl Fact for the holonomy-reduction reading (uses edge). Coverage records both as untouched. The curvature-only classification is repinned to version 3 (clause (vi) reworded under (T), as (v) here says). Statement unchanged.'
  note: >-
    Adversarial result on the open problem's first attack (derive the field space). It compares the field
    spaces of Cl(2,4) connections on which the frozen-point integrand can be varied: the special-conformal slot
    S of the connection (the n0 block, the Schouten map on the normal tractor connection) splits into a trace,
    an antisymmetric and a trace-free symmetric part, and each part is either frozen at its Lorentz-invariant
    value (rho times the identity, zero, zero) or varied; the dilation block is zero or varied. The varied
    parts enter algebraically and are eliminated through their own equations. The I-preserving field space
    is the row with everything frozen and the dilation zero; the unreduced field space (torsion-free conformal Cartan connections) is the
    row with everything varied, and its on-shell connection is the normal tractor connection, which proves in
    the series the elimination step of the Kaku-Townsend-van Nieuwenhuizen construction (imported Fact (b)).
    The answer to "Einstein iff the field space is reduced by a tractor" is: yes for the symmetric part of the
    slot (frozen at rho id with rho constant and nonzero), no as a statement about the connection, since the
    dilation and, on torsion-free fields, the antisymmetric part are invisible to the integrand, so field spaces
    that preserve no tractor off shell give the same equations. Bearing on the no-inverse-frame hypothesis (P):
    every row satisfies (P) (the density is a polynomial in Omega, the coframe and the slot one-form, with no
    inverse frame); in the all-varied row the inverse frame appears only on shell, through the solution S equal
    to the Schouten map. So (P) excludes the normal tractor connection as an off-shell expression in (hb,
    Omega), not as the outcome of a variational principle; clause (vi) of the curvature-only result holds for
    slots that are functions of (hb, Omega), and the field space then rests on the premise that the symmetric
    part of the slot is not a field (the premise (T) of \claimref{synthesis.inverse-frame-free-tractor-gauge-field-preserves-a-frozen-point}: gauge content hb and Omega, ten components per direction, the de Sitter or anti-de Sitter count, not the
    conformal fifteen). In invariant form that premise is that the varied connection admits a parallel tractor I with <X, I> = 1 (\claimref{synthesis.field-space-premise-parallel-frozen-point}); the frozen slot rho id with zero dilation is its reading in the gauge where I
    is constant. The statement that A preserves ninf + rho n0 exactly when the slot is rho id and the dilation
    vanishes is the bijection of \claimref{synthesis.frozen-point-field-space-is-the-gtg-pair-and-its-omega-equation-is-the-torsion-equation}(ii), recomputed here in (i). None of this presupposes the Einstein condition: the
    frozen value rho id is an input independent of the curvature, and the frozen row meets the normal row
    (S equal to the Schouten map) exactly on Einstein fields with Lambda = 6 rho (Theorem
    \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}(ii)). Transport-convenient:
    the computation is finite linear algebra on the conformal and Lorentz algebras; the one transport-specific
    reading is that the series' own transport is what the unconstrained variation selects.
---

## formal
Work in $\Cl(2,4)$ with $\nO$, $\nInf$ as in Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection} ($\nO \cdot \nInf = 1$), canonical tractor $X = \nO$, frozen point $I = \nInf + \tfrac{\Lambda}{6}\nO$ and $V = X - \tfrac{3}{\Lambda}I$ (Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector}), and $\epsilon$ with the orientation of Theorem \claimref{synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared}. A $\Cl(2,4)$ gauge field on flat spacetime whose $\nInf$ block is nondegenerate is, in the splitting of that theorem,
\[
A(a) \;=\; \Omega(a) \;-\; \nInf \wedge \hb^{-1}(a) \;+\; \nO \wedge S\bigl(\hb^{-1}(a)\bigr) \;+\; \beta(a)\,\nInf \wedge \nO ,
\]
with $\Omega$ the rotation gauge field, $\hb^{-1}(a)$ the coframe, $S$ a field of linear maps of spacetime vectors (the special-conformal slot; the normal tractor connection has $S = \Sch$) and $\beta$ a scalar one-form (the dilation). Split $S$, with respect to the derived metric, into its trace part $\sigma\,\id$, its antisymmetric part and its trace-free symmetric part. A \emph{slot field space} varies $\hb$ and $\Omega$ and, for each of the three parts, either freezes it at its Lorentz-invariant value ($\sigma = \rho$, a constant; the other two zero) or varies it as an independent field; $\beta$ is zero or varied. Fields are torsion-free (the curvature of $\Omega$ obeys the first Bianchi identity). $E_{4}$, $|W|^{2}$, $|\Ric_{0}|^{2}$ and $R^{2}$ denote the Euler density, the Weyl square, the square of the trace-free Ricci map and of the Ricci scalar (index readings, store's curvature sign), $\mathcal{L}$ the density $\epsilon(I, V, F, F) = \epsilon(I, X, F, F)$ as a multiple of the volume form.
\begin{enumerate}
\item[(i)] \emph{(What the integrand sees; proved.)} $\mathcal{L}$ depends on $A$ only through the Lorentz block of $F$, $F_{W}(B) = -\mathcal{R}(B) + T_{S}(B)$ with $T_{S}(a \wedge b) = a \wedge S(b) + S(a) \wedge b$ (on frame vectors), and on the frozen point only through the blade $I \wedge X = \nInf \wedge \nO$, so not on $\Lambda$; it does not depend on $\beta$. The connection preserves $\nInf + \rho\,\nO$ if and only if $S = \rho\,\id$ and $\beta = 0$.
\item[(ii)] \emph{(The free slot is the normal tractor connection; proved.)} $\mathcal{L}$ is quadratic in $S$ with a nondegenerate quadratic part on all sixteen components. With the whole slot varied, its equation has the unique solution $S = \Sch$, the Schouten map, at which $F_{W} = -\mathcal{W}$ and $\mathcal{L} = \tfrac14 |W|^{2}$. So on the torsion-free conformal Cartan connections (values in all bivectors, nondegenerate soldering, curvature of $\Omega$ obeying the first Bianchi identity, gauged by the parabolic group of the line of $X$), with the whole slot varied, the on-shell connection is the normal tractor connection, and the reduced functional is the Weyl-squared functional of Theorem \claimref{synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared}, with the Bach equations (Fact \claimref{synthesis.imported-conformal-gravity-bach-equations-and-conformal-gauge-form}(a)). The equation for $\Omega$ on this field space with torsion is not treated here. This proves in the series the elimination step of Fact \claimref{synthesis.imported-conformal-gravity-bach-equations-and-conformal-gauge-form}(b).
\item[(iii)] \emph{(The lattice; proved.)} After eliminating the varied parts, with $\Lambda = 6\rho$:
  \begin{itemize}
  \item symmetric part frozen (antisymmetric part frozen or varied, $\beta$ zero or varied): $\tfrac14 E_{4} - 2\rho\,(R - 2\Lambda)$, Euler, Einstein-Hilbert and volume terms with the frozen point's $\Lambda$;
  \item trace varied, trace-free part frozen: $\tfrac14 E_{4} - \tfrac{1}{24}R^{2}$, with no Einstein-Hilbert or volume term;
  \item trace frozen, trace-free part varied: $\tfrac14 E_{4} + \tfrac12 |\Ric_{0}|^{2} - 2\rho\,(R - 2\Lambda)$;
  \item both varied: $\tfrac14 E_{4} + \tfrac12 |\Ric_{0}|^{2} - \tfrac{1}{24}R^{2} = \tfrac14 |W|^{2}$, as in (ii).
  \end{itemize}
  At $\rho = 0$ (the connection preserves the null tractor $\nInf$) the first row is $\tfrac14 E_{4}$ alone. On torsion-free fields the antisymmetric part's equation sets it to zero, so it is inert; with torsion it is not.
\item[(iv)] \emph{(Einstein exactly on the frozen rows; proved, given the imported Facts.)} The reduced functional has Euler-Lagrange equations of second order, which are then Einstein's equations with $\Lambda = 6\rho$, if and only if the symmetric part of the slot is frozen at $\rho\,\id$ with $\rho \neq 0$: in the other rows the remainder over $\tfrac14 E_{4}$ and the Einstein-Hilbert part, namely $-\tfrac{1}{24}R^{2}$, $\tfrac12|\Ric_{0}|^{2}$ or their sum, is not variationally trivial. So the integrand gives Einstein's equations if and only if the field space, with the inert directions set to zero, is the one preserving $I$; the field space need not preserve any tractor off shell (rows with $\beta$ or the antisymmetric part varied preserve none for generic values of those fields).
\item[(v)] \emph{(The no-inverse-frame hypothesis does not separate the rows; proved.)} In every row $\mathcal{L}$ is a polynomial in $\Omega$, the coframe and the slot one-form $S(\hb^{-1}(a))$, with no inverse frame, and invariant under the Lorentz and dilation gauge transformations that fix the blade. In the all-varied row the inverse frame enters only on shell, through $S = \Sch$. So the hypothesis (P) of Theorem \claimref{synthesis.curvature-only-tractor-actions-are-macdowell-mansouri} excludes the normal tractor connection as an off-shell function of $(\hb, \Omega)$, and the forcing of $S = \rho\,\id$ (its clause (vi), proved as clause (i) of Theorem \claimref{synthesis.inverse-frame-free-tractor-gauge-field-preserves-a-frozen-point}) holds only for slots that are functions of $(\hb, \Omega)$, the premise (T) there; the $I$-preserving field space rests on (T), that the symmetric part of the slot is not a field, which (P) does not supply. In invariant form (T) with (P) reads: the varied connection admits a parallel tractor $I$ with $\ip{X}{I} = 1$ (Premise \claimref{synthesis.field-space-premise-parallel-frozen-point}, a holonomy reduction to the stabiliser of $I$ in the sense of Fact \claimref{synthesis.imported-holonomy-reductions-of-cartan-geometries}(a)), and $S = \rho\,\id$, $\beta = 0$ is that statement in the gauge where $I$ is constant.
\end{enumerate}

## technical
The open problem asks why the gravitational action should be varied over $\Cl(2,4)$ connections that preserve the frozen point, since on the series' own transport, the normal tractor connection, the same integrand is the Weyl square. This result compares the natural field spaces directly. Write a $\Cl(2,4)$ connection with nondegenerate soldering as rotation gauge field, coframe, special-conformal slot $S$ and dilation. The frozen-point integrand sees only the Lorentz block of the field strength, curvature plus $a \wedge S(b) + S(a) \wedge b$, and does not see the dilation or $\Lambda$. Split $S$ into trace, antisymmetric and trace-free symmetric parts and freeze or vary each. Varied parts appear algebraically and are eliminated by their equations.

On torsion-free fields, varying the whole slot returns $S$ equal to the Schouten map, so the unconstrained field space lands on the normal tractor connection and the Weyl square (conformal gravity, the Bach equations). Freezing the trace and the trace-free part at $\rho$ times the identity, with $\rho$ a nonzero constant, gives the Euler density plus Einstein-Hilbert with $\Lambda = 6\rho$. Varying only the trace removes the Einstein-Hilbert term and leaves the Euler density with an $R^{2}$ term; varying only the trace-free part adds a Ricci-squared term. Those remainders are not variationally trivial, so only the frozen rows give Einstein's equations. The antisymmetric part and the dilation make no difference without torsion, so preserving a tractor is necessary only up to those inert directions.

Every row satisfies the no-inverse-frame hypothesis, because the slot is itself a field; in the all-varied row the inverse frame comes back through the solution of the slot equation. So no-inverse-frame excludes the normal tractor connection only when the slot is required to be built from the frame and rotation gauge field. The field space therefore rests on a premise the hypothesis does not supply: the symmetric part of the slot is not an independent field, so the gauge content is the ten components of the de Sitter or anti-de Sitter algebra rather than the fifteen of the conformal algebra. In gauge-invariant form this is the statement that the varied connection admits a parallel tractor; freezing the slot is that statement in the gauge where the tractor is constant. None of this presupposes Einstein's equations.

## lay
The series borrows a rule, the action, from which the equations of gravity follow. The same formula gives Einstein's equations or a different theory, conformal gravity, depending on which shapes of the six-dimensional connection one is allowed to vary. This result tries every natural choice. If the extra part of the connection is left free, the rule hands back the series' own transport and conformal gravity. Einstein's equations come out only when that extra part is fixed to be a nonzero constant multiple of the basic frame, with the constant giving the cosmological constant. The rule that forbids dividing by the frame does not make that choice, because a free extra part obeys the rule too. So the choice is a separate assumption.

## one-liner
Writing a $\Cl(2,4)$ connection as rotation field, coframe, special-conformal slot $S$ and dilation, on torsion-free fields the frozen-point integrand sees only the Lorentz block $-\mathcal{R} + a \wedge S(b) + S(a) \wedge b$; varying the whole slot gives $S = \Sch$ (the normal tractor connection) and $\tfrac14|W|^{2}$, and after eliminating varied parts the integrand gives Einstein's equations with $\Lambda = 6\rho$ exactly when the symmetric part of $S$ is frozen at $\rho\,\id$, $\rho \neq 0$ (freeing the trace gives $\tfrac14 E_{4} - R^{2}/24$, freeing the trace-free part adds $\tfrac12|\Ric_{0}|^{2}$), the dilation and the antisymmetric part being inert; every row satisfies the no-inverse-frame hypothesis, so the frozen slot (in invariant form, a parallel tractor $I$ with $\ip{X}{I} = 1$) is a premise that hypothesis does not supply.
