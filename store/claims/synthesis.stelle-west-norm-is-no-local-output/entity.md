---
id: synthesis.stelle-west-norm-is-no-local-output
kind: claim
version: 2
title: 'The Stelle-West norm is no local output'
status: proved
region: synthesis
subject: einstein
tags: [tractors, curvature-and-field-equations, forcing-and-uniqueness, frozen-point]
proposed_by:
  kind: ai
  session: 2026-10-31-gravity-action
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
  - dark-energy.stelle-west-vector-frozen-point@6
  - dark-energy.imported-frozen-point-geometry@7
  - dark-energy.frozen-point-makes-stelle-west-vector@6
  - dark-energy.imported-macdowell-mansouri-theorem-stelle-west@3
  - singularity.non-removability-invariant-argument@3
  - synthesis.promoted-norm-weyl-clock-flat-weight@7
  - dark-energy.imported-henneaux-teitelboim-promotion@6
  - dark-energy.under-action-written-norm-parameter-laws@4
  - synthesis.rung-unit-transverse-to-norm@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_norm_of_the_stelle_west_vector_is_fixed_by_the_frozen_point
- kind: check
  ref: check.py::check_released_norm_equation_is_the_euler_identity
- kind: check
  ref: check.py::check_pointwise_values_on_torsion_free_einstein_blocks
- kind: check
  ref: check.py::check_schwarzschild_de_sitter_is_excluded_and_de_sitter_norm_is_free
- kind: check
  ref: check.py::check_coupling_ratio_and_the_weyl_obstruction
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part
  - synthesis.tube-point-clause-invariant-under-boost-commuting-symmetries
extraction:
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review (second round): dark-energy.imported-frozen-point-geometry repinned 6 -> 7 after reviewing its restatement (the sentence naming the tractor gauge-field theorem moved to a text-only remark); the parts cited here (parallel frozen point, Q(I) = Lambda/3, the stabilisers, the scale-g display and the Schouten tensor) are unchanged, and the use here holds as cited.'
  open_problem: op.derive-gravitational-action
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Version 1 -> 2: the mentions of the Weyl-square result and the five-dimensional Chern-Simons reduction filed alongside are now claimrefs (text only, no uses edges: the value here is computed on the Einstein blocks, and the radion equation is a parallel); pin moved to version 5 of the Henneaux-Teitelboim Fact, whose added note cites this result. Statement unchanged.'
  note: >-
    Route of a dynamical Stelle-West vector (the Westman-Zlosnik programme of Cartan gravity with dynamical
    symmetry breaking, cited from memory): can the norm Q(V) = -3/Lambda of the frozen-point functional be an
    output rather than an input? Negative within the constant-coupling family of three terms. On the series'
    objects the norm is not a second datum (the stored lemma's Q(I)Q(V) = -1). Released as a local field, the frozen-point MacDowell-Mansouri
    functional's equation along V is its own integrand, on torsion-free Einstein fields the Weyl density, so the
    Schwarzschild-de Sitter connection has no stationary Stelle-West vector while de Sitter is stationary for
    every norm. Adding the two other terms of this family, the Weyl part still enters only through the
    MacDowell-Mansouri term, and without that term the norm is tied to the curvature by a ratio of couplings.
    Couplings depending on Q(V) and further invariant terms are not treated. The Henneaux-Teitelboim
    promotion (recorded as the Clausius route's own variational form) is the global version, where the same
    density is the advance of the conjugate time rather than an equation. Transport-convenient for (i), transport-absent for (ii)-(iv).
---

## formal
Let $\Lambda \neq 0$ and work on the Einstein region of a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), in the scale of its frozen point $I = \nInf + \tfrac{\Lambda}{6}\nO$, $Q(I) = \Lambda/3$ (Fact \claimref{dark-energy.imported-frozen-point-geometry}), with canonical tractor $X = \nO$ and Stelle-West vector $V_{c} = X - \tfrac{3}{\Lambda}I$ (Lemma \claimref{dark-energy.stelle-west-vector-frozen-point}). Let $\nabla$ range over the connections of the ambient bundle preserving $I$, with field strength $F$ a bivector-valued two-form in $\Lambda^{2}I^{\perp}$, let $V$ be a field in $I^{\perp}$, $\nabla V$ its vector-valued one-form, and $\epsilon$ the fibre volume form, as in Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector}(iii). For constants $c_{1}, c_{3}, c_{5}$ put
\[
S_{c}[\nabla, V] = \int \bigl(c_{1}L_{1} + c_{3}L_{3} + c_{5}L_{5}\bigr),\qquad
L_{1} = \epsilon(I, V, F, F),\quad L_{3} = \epsilon(I, V, \nabla V, \nabla V, F),\quad L_{5} = \epsilon(I, V, \nabla V, \nabla V, \nabla V, \nabla V).
\]
The stored functional is $c_{1} = 1/Q(I)$, $c_{3} = c_{5} = 0$ with $Q(V) = -3/\Lambda$ imposed; \emph{releasing the norm} means varying $V$ over all of $I^{\perp}$. A field is \emph{torsion-free} if $F \in \Lambda^{2}\{I, V\}^{\perp}$ and $\nabla V$ takes values in $\{I, V\}^{\perp}$. \emph{Convention.} Densities are four-form coefficients in the stored chart, $\nO = \tfrac12(e_{+} + e_{-})$, $\nInf = e_{+} - e_{-}$, fibre pseudoscalar $e_{0}e_{1}e_{2}e_{3}e_{+}e_{-}$, each four-form coefficient being the sum over ordered complementary pairs of frame planes; in this convention $\lambda := \epsilon(I, V_{c}, e, e, e, e) = 6$. (The opposite orientation $\nO = \tfrac12(e_{+} - e_{-})$, $\nInf = e_{+} + e_{-}$ together with the sum over all $24$ orderings of the frame indices multiplies every density by $-4$; the ratios below do not change.)
\begin{enumerate}
\item[(i)] \emph{(The norm is not a second datum; the stored lemma.)} By Lemma \claimref{dark-energy.stelle-west-vector-frozen-point}(i), $\ip{V_{c}}{I} = 0$ and $Q(V_{c})\,Q(I) = -1$; the same holds for $V = X/\sigma - I/Q(I)$ with any null $X$, $\sigma = \ip{X}{I} \neq 0$, a rescaling of $X$. Since $\nabla I = 0$ makes $Q(I)$ constant, the one input is $Q(I)$, which fixes $\Lambda = 3Q(I)$.
\item[(ii)] \emph{(The equation along $V$; proved.)} The Euler-Lagrange equation $E_{V}$ of $S_{c}$ in $V$ satisfies, pointwise, $\ip{V}{E_{V}} = c_{1}L_{1} + 3c_{3}L_{3} + 5c_{5}L_{5}$. On torsion-free fields its components along $\{I, V\}^{\perp}$ vanish identically, so with the norm released the one new equation is $c_{1}L_{1} + 3c_{3}L_{3} + 5c_{5}L_{5} = 0$.
\item[(iii)] \emph{(Values on Einstein blocks; proved.)} On a torsion-free field with $V = tV_{c}$, $\nabla V = t\,e$ ($e$ the soldering form, $t \neq 0$ constant) and Lorentz block $F = \mathcal{W} + \kappa\,e \wedge e$, with $\mathcal{W}$ a Weyl curvature map and $\kappa$ constant,
\[
L_{1} = t\bigl(\kappa^{2} + \tfrac{1}{24}|W|^{2}\bigr)\lambda,\qquad L_{3} = \kappa\,t^{3}\lambda,\qquad L_{5} = t^{5}\lambda,
\]
with $|W|^{2} = W_{abcd}W^{abcd}$ (index reading). The Weyl part enters only through $c_{1}|W|^{2}$; the value $\epsilon(I, V, F, F) = \tfrac14|W|^{2}$ on the tractor field strength of every torsion-free field is the general identity of Theorem \claimref{synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared}(iii).
\item[(iv)] \emph{(Consequences; proved.)} (a) \emph{Bare release} ($c_{3} = c_{5} = 0$, $c_{1} \neq 0$): the equation of $V$ is the covector $U \mapsto \epsilon(I, U, F, F)$ on $I^{\perp}$, which does not involve $V$. For the Schwarzschild-de Sitter field with lapse $1 - 2M/r - \tfrac{\Lambda}{3}r^{2}$, either sign of $\Lambda$, it is a nonzero multiple of the dual of $V_{c}$, with $\epsilon(I, V_{c}, F, F) = 12M^{2}r^{-6}$, nonzero at every point when $M \neq 0$: the connection is stationary with $V_{c}$ for the stored functional, and with no $V \in I^{\perp}$ at all for the released one. The de Sitter field is stationary with $V = tV_{c}$ for every $t$: the norm is undetermined, and $Q(tV_{c}) = -3/\Lambda_{t}$ with $\Lambda_{t} = \Lambda/t^{2}$ the constant of the frame $t\,e$, a label of the solution. (b) If $c_{1} \neq 0$, every torsion-free Einstein configuration with constant $t$ and $\kappa$ solving the equation along $V$ has $|W|^{2}$ constant; the Schwarzschild-de Sitter field with $M \neq 0$ is excluded for every such $(t, \kappa)$. (c) If $c_{1} = 0 \neq c_{3}$, the equation along $V$ on such configurations is $\kappa = -\tfrac{5c_{5}}{3c_{3}}t^{2}$: the norm is tied to the curvature by the ratio of couplings $c_{5}/c_{3}$.
\end{enumerate}
\emph{Scope.} Couplings depending on $Q(V)$ (a potential) and further invariant terms are not treated: a $Q(V)$-dependent coefficient $c_{k}(Q(V))$ adds $2Q(V)\,c_{k}'L_{k}$ to the equation along $V$ and can fix the norm.

\emph{Reading (argued).} Within $S_{c}$ the norm of the frozen-point functional is an input as written (Proposition \claimref{dark-energy.under-action-written-norm-parameter-laws}), with $\Lambda$ fixed by the frozen point; a global label under the Henneaux-Teitelboim promotion (Fact \claimref{dark-energy.imported-henneaux-teitelboim-promotion}), recorded as the Clausius route's own variational form, whose conjugate time advances by the same Weyl density, $k|W|^{2}\mathrm{vol}$ on vacuum solutions (Theorem \claimref{synthesis.promoted-norm-weyl-clock-flat-weight}(iii)), there the integral of the density rather than a pointwise equation; and released locally it is either undetermined at the price of the black holes or a ratio of couplings. It is never a local output within this family. The same scalar equation, with the same conclusion, is the radion equation of the five-dimensional Chern-Simons reduction (Theorem \claimref{synthesis.macdowell-mansouri-is-the-frozen-point-reduction-of-five-dimensional-chern-simons}(iii)): in both the Lagrangian has degree one in the released scale. Clause (i) is transport-convenient (the frozen point and the canonical tractor); (ii) to (iv) are transport-absent. Nothing here selects the rung unit: every function of $V$ invariant under the ambient isometries is invariant under the rung boosts, which are isometries fixing the ground (Theorem \claimref{synthesis.rung-unit-transverse-to-norm}(1)).

## technical
The Stelle-West vector of the series' MacDowell-Mansouri functional is not an independent datum: by the stored lemma $Q(V)Q(I) = -1$, so its norm is $-3/\Lambda$ automatically. Asking for the norm as an output means releasing it: varying $V$ over all of $I^{\perp}$ in $\int(c_{1}\epsilon(I,V,F,F) + c_{3}\epsilon(I,V,\nabla V,\nabla V,F) + c_{5}\epsilon(I,V,(\nabla V)^{4}))$ with constant couplings, the polynomial family of Cartan gravity with a dynamical symmetry-breaking vector. Because every derivative term puts $V$ into two slots of $\epsilon$, the equation along $V$ is exactly $c_{1}L_{1} + 3c_{3}L_{3} + 5c_{5}L_{5}$, and the tangential components vanish on torsion-free fields. On a torsion-free Einstein block $\mathcal{W} + \kappa\,e\wedge e$ with $V = tV_{c}$ the three densities are $t(\kappa^{2} + |W|^{2}/24)$, $\kappa t^{3}$ and $t^{5}$ times one constant ($6$ in the stored chart): the Weyl part enters only through the MacDowell-Mansouri term. So with that term alone no Stelle-West vector is stationary on the Schwarzschild-de Sitter connection, where $|W|^{2} = 48M^{2}/r^{6}$, while de Sitter is stationary for every norm; with that term and the others, a constant-norm solution needs $|W|^{2}$ constant; without it, the norm is tied to the curvature by $c_{5}/c_{3}$. Couplings depending on the norm are not treated. The Henneaux-Teitelboim promotion is the global version, where the same density is the advance of the conjugate time. Within this family the norm is an input, a global label or a coupling ratio, never a local output.

## lay
In the series' version of a known gravitational action, a fixed vector of a given length (the Stelle-West vector) breaks the symmetry, and its length encodes the cosmological constant. One might hope that letting this vector move freely would make its length, and so the cosmological constant, come out of the equations rather than being put in. This result shows it does not, for the family of actions with fixed coefficients built in the same way. First, in the series the vector's length is not a separate number at all: it is fixed by the length of the frozen point. Second, if the length is allowed to vary from point to point, the new equation demands that a particular measure of tidal curvature vanish everywhere, which rules out black holes while allowing empty expanding space with any length. Adding the two other terms of this family either keeps that problem or ties the length to a ratio of new constants. Coefficients that themselves depend on the length are not covered. Treating the length as one constant for the whole universe is the version that keeps black holes.

## one-liner
Within the constant-coupling family $c_{1}L_{1} + c_{3}L_{3} + c_{5}L_{5}$ ($L_{1} = \epsilon(I,V,F,F)$, $L_{3} = \epsilon(I,V,\nabla V,\nabla V,F)$, $L_{5} = \epsilon(I,V,(\nabla V)^{4})$), the Stelle-West norm is no local output: the norm is $-1/Q(I)$ by the stored lemma; released, the equation along $V$ is $c_{1}L_{1} + 3c_{3}L_{3} + 5c_{5}L_{5}$, on torsion-free Einstein blocks $t(\kappa^{2} + |W|^{2}/24)\lambda$, $\kappa t^{3}\lambda$, $t^{5}\lambda$ ($\lambda = 6$ in the stored chart); with $c_{1}$ alone no $V$ is stationary on the Schwarzschild-de Sitter connection ($12M^{2}/r^{6}$) while de Sitter is stationary for every norm; with $c_{1} \neq 0$ a constant-norm solution needs $|W|^{2}$ constant, and with $c_{1} = 0$ the norm is the coupling ratio $\kappa = -\tfrac{5c_{5}}{3c_{3}}t^{2}$. Couplings depending on $Q(V)$ are not treated; transport-absent apart from (i).
