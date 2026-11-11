---
id: synthesis.frozen-point-unique-for-the-field-space-connection
kind: claim
version: 1
title: 'One frozen point up to scale for the field-space connection'
status: proved
region: synthesis
subject: dark-matter
tags: [tractors, frozen-point, premises-p1-p5]
proposed_by:
  kind: ai
  session: 2026-11-11-contradictions
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-11-contradictions
- name: Claude Opus 5.5
  role: 'independent derivation and checks (field strengths from fields, the derivative step, the torsion counter-model, the reversed-signature reading), and the corrections they forced'
  source: run 2026-11-11-contradictions, referee report
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.frozen-point-field-space-is-the-gtg-pair-and-its-omega-equation-is-the-torsion-equation@3
  - synthesis.frozen-point-unique-where-weyl-has-no-kernel@7
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_pointwise_action_of_the_field_space_connection
- kind: check
  ref: check.py::check_field_strength_and_kernels_on_de_sitter_fluid_and_schwarzschild_fields
- kind: check
  ref: check.py::check_torsion_counter_model
- kind: check
  ref: check.py::check_reversed_signature_reading
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.field-space-premise-parallel-frozen-point
  - dark-matter.p1-single-frozen-point
  - synthesis.two-frozen-points-conformally-flat
extraction:
  note: >-
    Written to close a gap of omission found in a read of the premises on 11 November 2026: the metric clause
    of Premise P1 cites the uniqueness of the frozen point for the normal tractor connection, while under the
    field-space premise (FS) the frozen point is parallel in the physical scale for the connection A_rho, not
    for the normal tractor connection on matter regions. This is the same uniqueness statement for A_rho. An
    earlier draft claimed more (that the unit pairing of (FS) forces the constant to one, so that the
    normalisation and the common N of P1 follow); an independent review showed that step circular, since
    requiring unit pairing with the one X for every tower's frozen point is the metric clause itself, and it
    is not claimed. Kill condition registered before the independent computation: a field on which the field
    strength of A_rho computed from the field differs from the Lorentz block of clause (i), or a kernel table
    different from clause (iv) (did not fire). Transport-convenient: the chart, X and the frozen point are the
    series' objects; the argument is the standard one for parallel sections of a connection (a parallel
    section is annihilated by the field strength).
---

## formal
Work in $\Cl(2,4)$ in the chart of Premise \claimref{synthesis.field-space-premise-parallel-frozen-point}: $\ip{\nO}{\nInf} = 1$, $X = \nO$. Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), twice continuously differentiable, $U$ a connected open subset of its invertible region, $\rho$ any real number and $\Lambda := 6\rho$. Let
\[
A_{\rho}(a) \;=\; \Omega(a) - u \wedge \hb^{-1}(a), \qquad u = \nInf - \rho\,\nO, \qquad I_{\rho} = \nInf + \rho\,\nO,
\]
the gauge field of Theorem \claimref{synthesis.frozen-point-field-space-is-the-gtg-pair-and-its-omega-equation-is-the-torsion-equation}(ii), with $D_{a}V = a\cdot\nabla V + A_{\rho}(a)\times V$ and $D_{a}I_{\rho} = 0$. Write a tractor as $V = \sigma\,\nInf + \mu + \tau\,\nO$, $\mu$ a spacetime vector. For a torsion-free field put $L(B) := -(\mathcal{R}(B) - \tfrac{\Lambda}{3}B)$, in the store's sign of $\mathcal{R}$; a \emph{kernel vector} of $L$ at a point is a spacetime vector $\mu \neq 0$ with $L(B)\cdot\mu = 0$ for every bivector $B$.
\begin{enumerate}
\item[(i)] \emph{(The action and the field strength; proved.)} $A_{\rho}(a)\times(\sigma\nInf + \tau\nO) = (\tau - \rho\sigma)\,\hb^{-1}(a)$ and $A_{\rho}(a)\times\mu = \Omega(a)\times\mu - (\hb^{-1}(a)\cdot\mu)\,u$. For a torsion-free field the field strength of $A_{\rho}$ is the Lorentz block alone, $F(\hb(B)) = L(B)$ (the stored formula of the Theorem above, clause (ii)), so $F\times V = L\cdot\mu$.
\item[(ii)] \emph{(Uniqueness; proved.)} Let the field be torsion-free. If at one point of $U$ the operator $L$ has no kernel vector, then every tractor field parallel for $A_{\rho}$ on $U$ is $c\,I_{\rho}$ with $c$ constant. No condition on $\rho$ is needed; at $\rho = 0$ the parallel tractors are the multiples of $\nInf$.
\item[(iii)] \emph{(Einstein fields; proved.)} If the field is Einstein with the same constant, $\mathcal{R}(a) = \Lambda a$ in the store's sign, then $L = -\mathcal{W}$, the Weyl part, and the condition of (ii) is the condition of Theorem \claimref{synthesis.frozen-point-unique-where-weyl-has-no-kernel}. On the de Sitter field at that $\Lambda$, $F = 0$ and uniqueness fails: locally the parallel tractors form a six-dimensional space.
\item[(iv)] \emph{(Isotropic fields with matter; proved, given the Friedmann equations.)} On a homogeneous isotropic field with flat slices, scale factor $a(t)$, with $H^{2} = \tfrac13(\kappa\rho_{m} + \Lambda)$ and $\ddot a/a = -\tfrac16\kappa\rho_{m}(1 + 3w) + \tfrac13\Lambda$ ($\kappa = 8\pi G$, a fluid of density $\rho_{m}$ and pressure $w\rho_{m}$; the two equations are hypotheses here), $L$ is a multiple of the identity on the time-space bivectors and on the space-space bivectors, with factors proportional to $\rho_{m}(1 + 3w)$ and to $\rho_{m}$. So for $\rho_{m} \neq 0$ there is no kernel vector unless $w = -\tfrac13$, where the kernel is the time direction; at $\rho_{m} = 0$ the field is de Sitter at the same $\Lambda$ and $F = 0$.
\item[(v)] \emph{(Torsion; the counter-model computed, the condition argued.)} With torsion $T$ the field strength is $F = L - u\wedge T$, and $F\times V = L\cdot\mu - (T\cdot\mu)\,u + (\tau - \rho\sigma)\,T$. The condition of (ii) is then not sufficient pointwise: on a dust instant where $L$ has no kernel vector, the choice $T(B) = -(L(B)\cdot\mu_{0})/c$ puts $V_{0} = \mu_{0} + \sigma\nInf + \tau\nO$, $\tau - \rho\sigma = c \neq 0$, $\mu_{0} \neq 0$, in the kernel of every $F(B)$. A sufficient condition (argued): at some point the map $(\mu, c) \mapsto \bigl(B \mapsto L(B)\cdot\mu - c\,T(B),\ B \mapsto T(B)\cdot\mu\bigr)$ is injective; $I_{\rho}$ is parallel with or without torsion.
\end{enumerate}
\emph{Applied to towers.} If the frozen points $I_{r}$ of all towers are parallel for the one connection $A_{\rho}$ on $U$, a hypothesis and the content of ``one connection'' in the metric clause of Premise \claimref{dark-matter.p1-single-frozen-point}, and $U$ contains one point of the kind in (ii), for example any point with matter of (iv), then $I_{r} = c_{r}I_{\rho}$ with constants $c_{r}$: the scales are $\ip{X}{I_{r}} = c_{r}$, the metrics agree up to the constant factors $c_{r}^{-2}$, and $Q(I_{r}) = c_{r}^{2}\Lambda/3$. The metric clause holds exactly when $c_{r} = \pm 1$, and the common $N$ of that premise is the same condition (given one $G$). Neither is derived here: Premise (FS) normalises one tractor, $\ip{X}{I} = 1$, and asking the same of every tower's frozen point is the metric clause itself. What changes against the normal tractor connection is the set where uniqueness fails: for $A_{\rho}$ the independent choice of Theorem \claimref{synthesis.two-frozen-points-conformally-flat} exists only where $L$ vanishes, that is on a component that is de Sitter at that $\Lambda$, and not on every conformally flat region; a single point with matter of (iv) in $U$ excludes it on all of $U$. $U$ is a component of the invertible region: the statement does not cross a wall where $\hb$ fails to invert.

\emph{Remark (the tower of reversed signature; computed pointwise, the reading argued).} With the quadratic form reversed, a bivector acts on vectors with the opposite sign. Keeping $X = \nO$ and reversing $\nInf$, the field-space form of the reversed tower with $\rho' = -\rho$ and $\Omega' = -\Omega$ is $-A_{\rho}$ as an element and the same covariant derivative, and its frozen point is $I' = -I_{\rho}$, with unit pairing with $X$ and $Q'(I') = -2\rho$. Keeping $\nInf$ and reversing $\nO$ instead, $u$ and $I_{\rho}$ are unchanged as vectors and the reversed form is $A_{\rho}$ with the frame reversed, $\operatorname{Ad}(I_{4})A_{\rho}$; $I_{4}$ acts as $-1$ on spacetime vectors, fixes the added plane and reverses both the time and the space orientation. So the two towers of a reversal pair can share one covariant derivative, up to the sign of the frozen point or that discrete element; in the reversed tower's own labels $\Lambda' = -\Lambda$, so its $N$ is read with $\Lambda = 3\varepsilon H^{2}$. That they do share it is the hypothesis ``one connection'', not a consequence.

## technical
For the connection $A_{\rho} = \Omega - u\wedge\hb^{-1}$ of the field-space premise, which keeps the frozen point $I_{\rho} = \nInf + \rho\nO$ parallel on every field, a parallel tractor must be annihilated by the field strength. On torsion-free fields the field strength is the Lorentz block $L = -(\mathcal{R} - \tfrac{\Lambda}{3}\mathrm{id})$, $\Lambda = 6\rho$, which acts only on the spacetime part $\mu$ of a tractor. Where $L$ has no kernel vector, $\mu = 0$ near the point, the remaining two components are constant with $\tau = \rho\sigma$, and the tractor is a constant multiple of $I_{\rho}$ there, hence on the whole connected region.

On Einstein fields at the same $\Lambda$ the operator is minus the Weyl part, so the condition is the stored one for the normal tractor connection. With matter it holds much more widely: for an isotropic field with a perfect fluid it fails only at $w = -\tfrac13$ and at vanishing density, where the field is de Sitter and the connection is flat. With torsion the condition is not sufficient and a stronger one is given.

Applied to towers whose frozen points are all parallel for the one connection, this gives $I_{r} = c_{r}I_{\rho}$. The constants are not fixed: $c_{r} = \pm 1$ is the metric clause of P1 and its common $N$, and stays a premise. For the tower of reversed signature the connection can be shared up to the sign of the frozen point or the discrete element $\operatorname{Ad}(I_{4})$.

## lay
The series fixes the cosmological constant through one special direction, the frozen point, which the gravitational field must carry along unchanged. This result shows that when there is any ordinary matter anywhere in a connected region, that direction is the only one the field carries unchanged, up to an overall factor. The overall factor is not fixed by the argument and remains an assumption of the series.

## one-liner
For the field-space connection $A_{\rho} = \Omega - (\nInf - \rho\nO)\wedge\hb^{-1}$ on a torsion-free field, every parallel tractor on a connected part of the invertible region is a constant multiple of $I_{\rho}$ once $-(\mathcal{R} - \tfrac{\Lambda}{3}\mathrm{id})$, $\Lambda = 6\rho$, has no kernel vector at one point: the Weyl condition on Einstein fields, and any isotropic matter except $w = -\tfrac13$; the constants $c_{r}$ of several towers stay free, and torsion needs a stronger condition.
