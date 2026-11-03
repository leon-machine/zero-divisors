---
id: dark-energy.frozen-point-makes-stelle-west-vector
kind: claim
version: 5
title: The frozen point makes the Stelle-West vector
status: proved
region: dark-energy
subject: dark-energy
tags: [frozen-point, tractors, curvature-and-field-equations, rotors-and-stabilisers]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T10, deposited version
review: typed
derivations:
- name: main
  uses:
  - dark-energy.imported-frozen-point-geometry@6
  - dark-energy.imported-macdowell-mansouri-theorem-stelle-west@3
  - dark-energy.imported-walls-sphere-theorem@6
  - dark-energy.stelle-west-vector-frozen-point@5
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T10.py
  tags:
  - label:thm:action
- kind: check
  ref: check.py::check_reduction_and_curvature_in_i_perp
- kind: check
  ref: check.py::check_stelle_west_datum_and_lorentz_block
- kind: check
  ref: check.py::check_action_prefactor_expansion_and_invariance
locators:
  paper: T10
  number: Thm 3.1
  label: thm:action
  line: 685
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the reduction to I-perp, the tractor field strength with derivatives (zero on de Sitter, Weyl on Kasner), the Stelle-West datum and Lorentz block, and the action prefactor, expansion and ambient invariance. Version 3 -> 4. Check strengthened: Q(I) = Lambda/3 pinned and Schouten preconditions (de Sitter Lambda/6, Kasner vacuum 0) asserted; samples moved to module level. Version 4 -> 5.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the Einstein region is that of a gravitational field on flat spacetime, the ambient connection its Cl(2,4) tractor gauge field, whose reduction to I-perp is the MacDowell-Mansouri connection Omega(a) - hb^{-1}(a) ^ V/l^2 (tractor theorem, clause v); the soldering form is the physical frame. Content unchanged.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  typing:
    by: ai-typing-pass
    note: 'Kept all four premises; the Kasner-wall proposition cited in consequence (1) was not added,
      because it uses this theorem and is cited only to illustrate the wall, so adding it would make a
      cycle. Levels pass: the lay level now states the Einstein region with nonzero cosmological constant,
      and no longer says the action makes sense where the metric degenerates (at the wall only the field
      equations reach, not the value).'
  env: theorem
  context_refs:
  - dark-energy.frozen-point-datum-kasner-wall
  - dark-energy.imported-weighted-limit-schwarzschild-singularity-matching
  eqrefs: 2
---

## formal
On the Einstein region with $\Lambda \neq 0$ of a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), whose tractor connection is the $\Cl(2,4)$ gauge field $\Omega_{T}$ of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}, in the notation of Lemma \claimref{dark-energy.stelle-west-vector-frozen-point}:
\begin{enumerate}
\item[(i)] \emph{(Reduction; proved.)} Parallelism of $I$ reduces the ambient $SO(2,4)$-structure to the stabiliser of $I$, the de Sitter group $SO(1,4)$ for $\Lambda > 0$ and the anti-de Sitter group $SO(2,3)$ for $\Lambda < 0$, and the tractor connection to a metric connection on the rank-five bundle $I^\perp$, of signature $(1,4)$ or $(2,3)$ respectively; the ambient curvature takes values in $\Lambda^2 I^\perp$. (The de Sitter names are used below; the anti-de Sitter branch reads identically with these substitutions, and every statement that follows uses only $\{I,V\}^\perp$, whose signature is $(1,3)$ on both branches.)
\item[(ii)] \emph{(The Stelle-West datum; proved.)} $V$ is a section of $I^\perp$ of fixed squared norm $-3/\Lambda = -\ell^2$, its stabiliser in $SO(1,4)$ (or $SO(2,3)$) is the Lorentz group of $\{I, V\}^\perp$, of signature $(1,3)$, its covariant derivative is the soldering form, the physical frame $\hb^{-1}(a)$, and the reduced connection is $D + e\wedge V/Q(V)$, on flat spacetime the gauge field $\Omega(a) - \hb^{-1}(a) \wedge V/\ell^{2}$, with Lorentz curvature block $R + \ell^{-2}\,e\wedge e$. The pair (reduced connection, $V$) is exactly the datum of Fact \claimref{dark-energy.imported-macdowell-mansouri-theorem-stelle-west}. The Stelle-West vector is therefore not the frozen point, which is parallel; it is made from the frozen point and the canonical tractor, $V = X - (3/\Lambda)\,I$.
\item[(iii)] \emph{(The action; proved, with the Stelle-West contraction of Fact \claimref{dark-energy.imported-macdowell-mansouri-theorem-stelle-west} as the imported input.)} The MacDowell-Mansouri functional of that datum is
\[
\begin{aligned}
S[\nabla, I, V] \;&\sim\; \frac{1}{Q(I)} \int \epsilon(I, V, F, F), \\
S[\nabla, I, X - \tfrac{3}{\Lambda}I] \;&\sim\; \frac{3}{\Lambda}\int \epsilon(I, X, F, F) \quad\text{(value at the canonical solution),}
\end{aligned}
\]
where $\epsilon(I, V, F, F)$ denotes the fibre volume form of $\mathcal{T}$ contracted with $I$, with $V$, and with the two bivector legs of $F\wedge F$, the first line being the functional and the second its value at the canonical Stelle-West vector of Lemma \claimref{dark-energy.stelle-west-vector-frozen-point}, written in the scale the frozen point determines (the canonical tractor $X$ carries a conformal weight): \emph{extremise the square of the curvature as seen from the point at infinity}, the frozen point supplying the reduction and the prefactor, the canonical tractor the Stelle-West slot. In the variational principle $\nabla$ ranges over the metric connections of the ambient bundle that preserve $I$, $\nabla I = 0$, equivalently those that reduce to $I^\perp$, which is the field space of Fact \claimref{dark-energy.imported-macdowell-mansouri-theorem-stelle-west} (the twenty further components per point of an unconstrained ambient connection are exactly $\nabla I$, which enter the integrand quadratically through $[I\wedge u, I\wedge v] = -Q(I)\,u\wedge v$ and would spoil the identification with the Einstein-Cartan equations); this space is carried to itself by the ambient gauge group acting on $\nabla$, $I$ and $V$ together, since $(g\nabla g^{-1})(gI) = g(\nabla I)$, and the tractor connection \eqref{eq:conn} is the point of it occupied by the canonical solution of Lemma \claimref{dark-energy.stelle-west-vector-frozen-point}, generic gauge transformations moving it within the space without preserving the tractor shape. $I$ is a field subject to $Q(I) = \Lambda/3$, and $V$ an independent field subject to $\ip{V}{I} = 0$, $Q(V) = -3/\Lambda$, of which Lemma \claimref{dark-energy.stelle-west-vector-frozen-point} exhibits the canonical solution; the identity $Q(I)\,Q(V) = -1$ holds for either sign of $\Lambda$.
\end{enumerate}
Two consequences, each at its level:
\begin{enumerate}
\item \emph{(Proved.)} $S$ is polynomial in the connection, $I$ and $V$, with no inverse metric anywhere: its integrand is defined wherever the ambient bundle and its connection are regular. At the Schwarzschild wall the connection is not regular (Proposition \claimref{dark-energy.frozen-point-datum-kasner-wall} on the Kasner model, transported by Fact \claimref{dark-energy.imported-weighted-limit-schwarzschild-singularity-matching}: a simple pole with the Kasner residue), and there the integrand's topological term diverges while its variational principle and field equations reach the wall as conditions on the residue; what the polynomial form yields at $\Sigma$ is the equations, not the number. Section \ref{sec:vacate} makes this precise.
\item \emph{(Proved; the limit at the level of Fact \claimref{dark-energy.imported-macdowell-mansouri-theorem-stelle-west}.)} The prefactor $1/Q(I) = 3/\Lambda$ has a simple pole at $\Lambda = 0$ and the integrand $\epsilon(I, X, F, F)$ is polynomial in $\Lambda$: the curvature-squared presentation exists precisely when $\Lambda \neq 0$, that is, precisely when the frozen point is off the null cone. This is a boundary of the presentation, not of the action principle. By the expansion of Fact \claimref{dark-energy.imported-macdowell-mansouri-theorem-stelle-west},
\[
S \;\sim\; \frac{3}{\Lambda}\int \epsilon_{abcd}R^{ab}\wedge R^{cd} \;+\; 2\int \epsilon_{abcd}\,e^a\wedge e^b\wedge R^{cd} \;+\; \frac{\Lambda}{3}\int \epsilon_{abcd}\,e^a\wedge e^b\wedge e^c\wedge e^d ,
\]
the first term is topological with vanishing interior variation (a boundary term only), and after its subtraction the limit $\Lambda \to 0$ is the Einstein-Cartan functional $2\int\epsilon_{abcd}\,e^a\wedge e^b\wedge R^{cd}$: polynomial, defined at degenerate $e$, and no longer of curvature-squared form.
\end{enumerate}

## technical
On the Einstein region with $\Lambda\neq 0$ of a gravitational field on flat spacetime, parallelism of the frozen point $I$ for the tractor gauge field, with $Q(I) = \Lambda/3$, reduces the ambient $SO(2,4)$-structure to $SO(1,4)$ for $\Lambda > 0$ or $SO(2,3)$ for $\Lambda < 0$, and the tractor connection to a metric connection on $I^\perp$. The vector $V = X - (3/\Lambda)I$, made from the frozen point and the canonical tractor, has $Q(V) = -3/\Lambda$, stabiliser the Lorentz group of $\{I,V\}^\perp$ and covariant derivative the soldering form, and the pair (reduced connection, $V$) is exactly the MacDowell-Mansouri datum. The action is $S[\nabla,I,V] \sim Q(I)^{-1}\int\epsilon(I,V,F,F)$, with $I$ and $V$ constrained fields.

This functional is polynomial in the connection, $I$ and $V$, with no inverse metric. Its prefactor $3/\Lambda$ has a simple pole at $\Lambda = 0$; by the imported expansion $S \sim (3/\Lambda)\int\epsilon_{abcd}R^{ab}\wedge R^{cd} + 2\int\epsilon_{abcd}e^a\wedge e^b\wedge R^{cd} + (\Lambda/3)\int\epsilon_{abcd}e^a\wedge e^b\wedge e^c\wedge e^d$, the first term is topological, and after its subtraction the limit $\Lambda\to 0$ is the Einstein-Cartan functional, defined at degenerate $e$.

## lay
The frozen point is a fixed direction in the larger conformal space whose length encodes the cosmological constant. On the region where Einstein's equations hold with a nonzero cosmological constant, this result shows that the frozen point, together with one canonical geometric object, produces exactly the extra vector that a known reformulation of gravity, due to MacDowell and Mansouri and to Stelle and West, requires. Gravity's action can then be written as the square of the curvature as seen from the point at infinity, with no inverse metric anywhere, so it is defined wherever the connection stays regular. At the black hole's wall, where the connection is singular, its value diverges but its field equations still reach the wall; and the curvature-squared form itself exists only while the cosmological constant is nonzero.

## one-liner
On the Einstein region with $\Lambda\neq 0$ the frozen point reduces the ambient structure to de Sitter or anti-de Sitter type and, with the canonical tractor, supplies the Stelle-West vector $V = X - (3/\Lambda)I$, so the MacDowell-Mansouri action is $Q(I)^{-1}\int\epsilon(I,V,F,F)$, polynomial and free of inverse metrics.
