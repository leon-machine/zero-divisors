---
id: one-relation.third-constant-conversion-constant-between-charts
kind: claim
version: 6
title: The third constant is the conversion constant between the charts
status: proved
region: one-relation
subject: one-relation
tags: [two-readings, null-directions, witt-index]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T16, deposited version
review: typed
derivations:
- name: main
  uses:
  - one-relation.imported-null-cone-determines-form-zeemans@3
  - one-relation.imported-witts-extension-theorem@2
  - std-algebra.bivector-exponential@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_finite_ratio_iff_nondegenerate_and_mixed
- kind: check
  ref: check.py::check_one_number_by_witt
- kind: check
  ref: check.py::check_witt_rescaling_is_the_boost
- kind: check
  ref: check.py::check_time_orientation_iff_min_p_q_is_one
- kind: check
  ref: check.py::check_cone_determines_the_form
- kind: check
  ref: check.py::check_three_constants_fix_three_units
locators:
  paper: T16
  number: Lem 4.4
  label: lem:speed
  line: 710
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.bivector-exponential where the proof uses them. Version 5 -> 6.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the Galilean degeneration and null vectors iff mixed, conjugate hyperbolic planes of (1,3), the Witt rescaling as the boost rotor at three rapidities, component counts of {Q > 0} by certified union-find, the cone fixing Q up to scale, and the (c, hbar, G) determinant -2. Version 2 -> 3. Check strengthened: expected component count derived from the S^(p-1) rule; sign-purity asserted iff two components and both time signs asserted on every nonempty {Q > 0}; samples moved to module level. Version 3 -> 4. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 4 -> 5.'
  env: lemma
  context_refs:
  - dark-matter.towers-are-residues-single-clock-filter
  - scrambling.imported-modes-modular-inventory
  - transport.no-go-level-elements
  typing:
    by: ai-typing-pass
    removed: [one-relation.two-capacities-three-consequences]
    note: 'Removed the capacities proposition to break the E301 cycle: clause (ii) rests on Witt''s extension theorem and only identifies it with the capacities proposition''s Witt fact; context_refs (T01, T08, T14 results) are comparisons and were not added.'
  source_title: 'The third constant is the conversion constant between the charts'
  source_formal: |-
    Let $(V, Q)$ be a real quadratic space of signature $(p, q)$, $n = p + q \geq 2$, with events carrying a time coordinate and space coordinates measured in independently chosen units, so that a quadratic form on events is dimensionally homogeneous only after a conversion constant $c$ is chosen, $Q = c^{2}t^{2} - |\mathbf{x}|^{2}$ in the Lorentzian case. Then:
    \begin{enumerate}
    \item[(i)] \emph{(Existence and finiteness.)} A finite invariant ratio of length to time exists if and only if $Q$ is nondegenerate and mixed, $pq \neq 0$: the null cone is that invariant ratio, preserved by every isometry, and it is nonempty exactly when the signature is mixed; dividing $Q$ by $c^{2}$ and letting $c \to \infty$ degenerates $Q$ to the rank-one form $t^{2}$, whose zero set is the simultaneity hyperplane, the Galilean case the root paper sets aside. The word \emph{speed} is reserved for the case of clause (iv). Two of the three standing hypotheses of the root paper's no-go theorem \cite[Thm.~4.2]{ButlerT1}, nondegenerate and mixed, are jointly the existence of a finite invariant ratio; the third, $n \geq 3$, is not needed here and enters only through Zeeman's theorem below.
    \item[(ii)] \emph{(One number.)} The invariant ratio is a property of a hyperbolic plane, and the isometry group is transitive on the hyperbolic planes of $(V, Q)$ (Witt's extension theorem, Fact \claimref{one-relation.imported-witts-extension-theorem}), so every hyperbolic plane carries the same $c$. This is the Witt fact of Proposition \claimref{one-relation.two-capacities-three-consequences}(1): the uniqueness of the boost qubit and the uniqueness of the invariant ratio are one statement.
    \item[(iii)] \emph{(Invisible in the Witt chart, fixed in the metric chart.)} On a hyperbolic plane with orthonormal pair $e_{0}, e_{1}$, $e_{0}^{2} = 1$, $e_{1}^{2} = -1$, the Witt chart $f_{\pm} = \tfrac12(e_{0} \pm e_{1})$, $f_{+} \cdot f_{-} = \tfrac12$, has a one-parameter freedom the metric chart does not show, $f_{+} \to \lambda f_{+}$, $f_{-} \to f_{-}/\lambda$, $\lambda > 0$; that rescaling is exactly the boost rotor of rapidity $\eta = \log\lambda$ acting on the orthonormal frame, $R = \cosh(\eta/2) - \sinh(\eta/2)\,e_{0}e_{1}$, with $R e_{0}\tilde{R} = \cosh\eta\, e_{0} + \sinh\eta\, e_{1}$ and $R f_{+}\tilde{R} = e^{\eta}f_{+}$, and the coordinate velocity of the boosted time axis is $c\tanh\eta$. The Witt chart contains rapidity, a dimensionless number, and no other quantity; the metric chart contains time and length separately; the transition from one to the other is what requires the conversion constant $c$. That the algebra fixes orbits and not speeds, as the entropy paper states \cite[Fact~2.2]{ButlerT8}, is this clause: the Witt chart is scale-free, and the geometric normalisation that converts rapidity to time is the chart transition.
    \item[(iv)] \emph{(A speed with an arrow.)} The set $\{Q > 0\}$ retracts onto the unit sphere of the positive part and has the components of $S^{p-1}$: two when $p = 1$, one when $p \geq 2$, none when $p = 0$; symmetrically $\{Q < 0\}$ splits exactly when $q = 1$. Hence a nondegenerate form admits a future/past split, a $\mathbb{Z}_{2}$ of time orientation, if and only if $\min(p, q) = 1$. The dark-matter paper's causal criterion \cite[Prop.~3.1]{ButlerT14}, stated there as a definition, is thereby a theorem about the cone: a signature has a single time if and only if its timelike set is disconnected. $c$ is a speed, a length over one time, precisely in the causal signatures; in $(2,2)$ the null cone exists and determines the form, so an invariant ratio exists, but there is no single time to divide by and no arrow, and the invariant is not a speed.
    \end{enumerate}
    With Fact \claimref{one-relation.imported-null-cone-determines-form-zeemans}, the cone determines $Q$ up to scale, so $c$ is a conformal invariant and survives every conformal step of the series, the projective-to-conformal completion, the twistor correspondence and the tractor bundle, which is why those papers can set $c = 1$ with no effect on their results; $G$ does not survive the conformal step, needing the scale the conformal class forgets, and $\hbar$ does not survive the classical chart, needing the ordering. The three constants therefore sit at three levels: $c$ at the conformal level (the cone), $G$ at the metric level (the scale), $\hbar$ at the Witt level (the ordering); and the exponent matrix of $(c, \hbar, G)$ over (length, time, mass) has determinant $-2$, so the three together fix the three base units and every remaining constant is dimensionless over (length, time, mass), while $\hbar$ and $G$ alone fix no base unit. Zeeman's theorem (Fact \claimref{one-relation.imported-null-cone-determines-form-zeemans}) connects (iv) back to the conformal level: in a causal signature with $n \geq 3$ the causal automorphisms are the conformal ones up to dilation.
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: 'One phrase in the formal level converted: the twistor correspondence is now the correspondence between points and lines of conformal spinors, with the twistor name in parentheses. The rest is already geometric algebra; the proof is unchanged.'
---

## formal
Let $(V, Q)$ be a real quadratic space of signature $(p, q)$, $n = p + q \geq 2$, with events carrying a time coordinate and space coordinates measured in independently chosen units, so that a quadratic form on events is dimensionally homogeneous only after a conversion constant $c$ is chosen, $Q = c^{2}t^{2} - |\mathbf{x}|^{2}$ in the Lorentzian case. Then:
\begin{enumerate}
\item[(i)] \emph{(Existence and finiteness.)} A finite invariant ratio of length to time exists if and only if $Q$ is nondegenerate and mixed, $pq \neq 0$: the null cone is that invariant ratio, preserved by every isometry, and it is nonempty exactly when the signature is mixed; dividing $Q$ by $c^{2}$ and letting $c \to \infty$ degenerates $Q$ to the rank-one form $t^{2}$, whose zero set is the simultaneity hyperplane, the Galilean case the root paper sets aside. The word \emph{speed} is reserved for the case of clause (iv). Two of the three standing hypotheses of the root paper's no-go theorem \cite[Thm.~4.2]{ButlerT1}, nondegenerate and mixed, are jointly the existence of a finite invariant ratio; the third, $n \geq 3$, is not needed here and enters only through Zeeman's theorem below.
\item[(ii)] \emph{(One number.)} The invariant ratio is a property of a hyperbolic plane, and the isometry group is transitive on the hyperbolic planes of $(V, Q)$ (Witt's extension theorem, Fact \claimref{one-relation.imported-witts-extension-theorem}), so every hyperbolic plane carries the same $c$. This is the Witt fact of Proposition \claimref{one-relation.two-capacities-three-consequences}(1): the uniqueness of the boost qubit and the uniqueness of the invariant ratio are one statement.
\item[(iii)] \emph{(Invisible in the Witt chart, fixed in the metric chart.)} On a hyperbolic plane with orthonormal pair $e_{0}, e_{1}$, $e_{0}^{2} = 1$, $e_{1}^{2} = -1$, the Witt chart $f_{\pm} = \tfrac12(e_{0} \pm e_{1})$, $f_{+} \cdot f_{-} = \tfrac12$, has a one-parameter freedom the metric chart does not show, $f_{+} \to \lambda f_{+}$, $f_{-} \to f_{-}/\lambda$, $\lambda > 0$; that rescaling is exactly the boost rotor of rapidity $\eta = \log\lambda$ acting on the orthonormal frame, $R = \cosh(\eta/2) - \sinh(\eta/2)\,e_{0}e_{1}$, with $R e_{0}\tilde{R} = \cosh\eta\, e_{0} + \sinh\eta\, e_{1}$ and $R f_{+}\tilde{R} = e^{\eta}f_{+}$, and the coordinate velocity of the boosted time axis is $c\tanh\eta$. The Witt chart contains rapidity, a dimensionless number, and no other quantity; the metric chart contains time and length separately; the transition from one to the other is what requires the conversion constant $c$. That the algebra fixes orbits and not speeds, as the entropy paper states \cite[Fact~2.2]{ButlerT8}, is this clause: the Witt chart is scale-free, and the geometric normalisation that converts rapidity to time is the chart transition.
\item[(iv)] \emph{(A speed with an arrow.)} The set $\{Q > 0\}$ retracts onto the unit sphere of the positive part and has the components of $S^{p-1}$: two when $p = 1$, one when $p \geq 2$, none when $p = 0$; symmetrically $\{Q < 0\}$ splits exactly when $q = 1$. Hence a nondegenerate form admits a future/past split, a $\mathbb{Z}_{2}$ of time orientation, if and only if $\min(p, q) = 1$. The dark-matter paper's causal criterion \cite[Prop.~3.1]{ButlerT14}, stated there as a definition, is thereby a theorem about the cone: a signature has a single time if and only if its timelike set is disconnected. $c$ is a speed, a length over one time, precisely in the causal signatures; in $(2,2)$ the null cone exists and determines the form, so an invariant ratio exists, but there is no single time to divide by and no arrow, and the invariant is not a speed.
\end{enumerate}
With Fact \claimref{one-relation.imported-null-cone-determines-form-zeemans}, the cone determines $Q$ up to scale, so $c$ is a conformal invariant and survives every conformal step of the series, the projective-to-conformal completion, the correspondence between points and lines of conformal spinors (the twistor correspondence) and the tractor bundle, which is why those papers can set $c = 1$ with no effect on their results; $G$ does not survive the conformal step, needing the scale the conformal class forgets, and $\hbar$ does not survive the classical chart, needing the ordering. The three constants therefore sit at three levels: $c$ at the conformal level (the cone), $G$ at the metric level (the scale), $\hbar$ at the Witt level (the ordering); and the exponent matrix of $(c, \hbar, G)$ over (length, time, mass) has determinant $-2$, so the three together fix the three base units and every remaining constant is dimensionless over (length, time, mass), while $\hbar$ and $G$ alone fix no base unit. Zeeman's theorem (Fact \claimref{one-relation.imported-null-cone-determines-form-zeemans}) connects (iv) back to the conformal level: in a causal signature with $n \geq 3$ the causal automorphisms are the conformal ones up to dilation.

## technical
On a real quadratic space of signature $(p,q)$ with $n = p + q \geq 2$, where time and space are measured in independent units, a finite invariant ratio of length to time exists if and only if $Q$ is nondegenerate and mixed, $pq \neq 0$: it is the null cone. Witt's extension theorem makes the isometry group transitive on hyperbolic planes, so the ratio is a single number $c$. In the Witt chart $f_{\pm} = \tfrac12(e_{0} \pm e_{1})$ the rescaling $f_{+} \to \lambda f_{+}$, $f_{-} \to f_{-}/\lambda$ is the boost of rapidity $\eta = \log\lambda$; that chart holds only rapidity, so the transition to the metric chart's separate time and length is what needs $c$.

A future/past split exists exactly when $\min(p,q) = 1$, so $c$ is a speed with an arrow only in causal signatures. Since the cone fixes $Q$ up to scale, $c$ is a conformal invariant, while $G$ needs the metric scale and $\hbar$ the Witt ordering; together $(c, \hbar, G)$ fix the three base units. No value of $c$ is derived.

## lay
The speed of light can be seen as a conversion factor between units of time and units of length. This result shows such a factor exists only when spacetime mixes time-like and space-like directions, that there is only one such number, and that it is invisible in the quantum description and appears only on passing to the geometric one. It also places the three fundamental constants at three different levels of structure, without deriving any of their values.

## one-liner
The constant $c$ is the unique invariant ratio carried by the null cone of a nondegenerate mixed form, the conversion between the scale-free Witt chart and the metric chart, and a speed with an arrow exactly when $\min(p,q) = 1$.
