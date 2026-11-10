---
id: synthesis.frozen-point-action-is-bf-transport-broken-by-the-blade-i-wedge-x
kind: claim
version: 1
title: 'The frozen-point action as BF transport broken on $I \wedge X$'
status: proved
region: synthesis
subject: einstein
tags: [tractors, frozen-point, curvature-and-field-equations, symmetry-breaking, the-number-n]
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
  - dark-energy.frozen-point-makes-stelle-west-vector@7
  - dark-energy.stelle-west-vector-frozen-point@6
  - dark-energy.imported-macdowell-mansouri-theorem-stelle-west@4
  - synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part@5
  - synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection@1
  - standard-model.imported-frozen-point-dictionary@9
  - synthesis.de-sitter-entropy-pi-n-squared@6
  - synthesis.imported-einstein-cartan-matter-coupling@1
  - dark-energy.imported-henneaux-teitelboim-promotion@6
  - synthesis.promoted-norm-weyl-clock-flat-weight@7
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_breaking_term_lives_on_the_blade
- kind: check
  ref: check.py::check_eliminating_b_gives_the_frozen_point_integrand
- kind: check
  ref: check.py::check_coupling_is_sixteen_pi_over_n_squared
- kind: check
  ref: check.py::check_bf_sector_is_pure_transport_and_torsion
- kind: check
  ref: check.py::check_translational_term_restores_unconstrained_torsion
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part
  - dark-energy.frozen-point-makes-stelle-west-vector
  - synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection
  - programme.n-parameter-of-the-laws
extraction:
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review (second round): synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part repinned 3 -> 4 after reviewing its restatement (formal setting restated (A(a) = Omega(a) - (Lambda/3) hb^-1(a) ^ V, l^2 = 3/|Lambda| dropped)); clauses (i) to (iv), the store sign and the frame equation, cited here, are unchanged, and the use here holds as cited.'
  open_problem: op.derive-gravitational-action
  note: >-
    Tests the Freidel-Starodubtsev reading (hep-th/0501191, cited from memory: MacDowell-Mansouri gravity as BF
    theory of the de Sitter group plus a symmetry-breaking term with dimensionless coupling quoted as
    G Lambda/3) on the series' objects. Results: the frozen point is the reduction datum and its norm sets the
    coupling, but it is not the breaking datum: the breaking term eps(I, V, B, B) = -<B iota B>_0, odd under the
    internal reflection, needs the second vector and sees the pair only through the blade
    I ^ V = I ^ X = ninf ^ n0, which is independent of Lambda (the classification showing that I alone admits no
    such invariant is a separate result and is not repeated here). With the breaking supported on the Lorentz
    block, eliminating B gives the frozen-point integrand exactly, plus a Pontryagin term from any part even under
    the internal reflection, with the translational components of B as multipliers imposing zero torsion; in
    vacuum that constraint is already the functional's own connection equation (rank 24), so the two agree in
    vacuum. With spinning matter the Lorentz-block BF form keeps the torsion zero (torsion-free coupling with the
    Hilbert source), unlike the stored functional's Einstein-Cartan coupling; the invariant translational term
    c <B_V ^ B_V>_0 replaces the constraint by a torsion-squared term (1/c) <F_V ^ F_V>_0 and returns the
    stored functional as c -> infinity, so the BF form does not decide the matter coupling. The pre-registered
    kill condition on alpha against N fired: alpha N^2 is 16 pi in the Clifford scalar-part normalisation with
    BF coefficient one, changes under B -> lambda B, and is 1 in the normalisation quoted by Freidel and
    Starodubtsev, so no relation to N beyond its definition is claimed. The action principle (import a) is not
    removed; the MacDowell-Mansouri form (import b) is rewritten, not reduced, since choosing eps(I, V, B, B) is
    the same choice as eps(I, V, F, F) (elimination inverts the quadratic form), and the field space, connections
    preserving I, is the same; the Einstein-Cartan coupling (import c) is not supplied. Transport-convenient. The
    Euler term is produced together with the rest, so the BF form does not remove it.

---

## formal
Let $\Lambda \neq 0$ and work on the Einstein region of a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), with the frozen point $I$, $Q(I) = \Lambda/3$, the canonical tractor $X$ and the Stelle-West vector $V = X - (3/\Lambda)I$ of Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector} and Lemma \claimref{dark-energy.stelle-west-vector-frozen-point}; in the flat chart $I = \ninf + (\Lambda/6)\nO$, $X = \nO$. The chart is that of the stored frozen-point check: generators $e_{0}$ ($+1$), $e_{1}, e_{2}, e_{3}$ ($-1$), $e_{+}$ ($+1$), $e_{-}$ ($-1$), $\nO = (e_{+} + e_{-})/2$, $\ninf = e_{+} - e_{-}$, pseudoscalar $I_{6} = e_{0}e_{1}e_{2}e_{3}e_{+}e_{-}$, and a four-form is read by its coefficient as the sum over the six coordinate planes, $B \wedge C = \sum_{P,Q}\omega(P,Q)B_{P}C_{Q}\,d^{4}x$; in this orientation $\epsilon(I, V, e\wedge e, e\wedge e) = +6\det(\hb^{-1})$, and the opposite orientation of the pair $(\ninf, \nO)$ reverses $I \wedge V$ and every sign of $\epsilon(I, V, \cdot, \cdot)$. Let $\iota := (I \wedge V)\,I_{6}$, the unit pseudoscalar of $\{I, V\}^{\perp}$ (in the flat chart $\iota = e_{0}e_{1}e_{2}e_{3}$), so $\iota^{2} = -1$. The field space is that of Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector}(iii): connections $A$ of the ambient bundle preserving $I$, with field strength $F$, a bivector-valued two-form with values in $\Lambda^{2}I^{\perp}$, whose Lorentz block $F_{L}$ (values in $\Lambda^{2}\{I, V\}^{\perp}$) is $R + \tfrac{\Lambda}{3}\,e\wedge e$ in the store's sign and whose translational block (values in $V \wedge \{I, V\}^{\perp}$) carries the torsion $De$. For a bivector-valued two-form $B$ with values in $\Lambda^{2}I^{\perp}$ (the de Sitter or anti-de Sitter algebra) and real $a, b$ with $a^{2} + b^{2} \neq 0$ and $c \neq 0$ set
\[
S_{a,b}[A, B] = \int \langle B \wedge F\rangle_{0} - \tfrac14 \int \langle B \wedge (a\iota + b) B_{L}\rangle_{0}, \qquad S_{a,b,c} = S_{a,b} - \tfrac{c}{4}\int\langle B_{V}\wedge B_{V}\rangle_{0},
\]
$B_{L}$ and $B_{V}$ the Lorentz and translational blocks of $B$ and the wedge that of two-forms ($S_{a,b}$ has its breaking supported on the Lorentz block). At $a = b = 0$ it is the BF functional of the reduced connection.
\begin{enumerate}
\item[(i)] \emph{(The breaking term lives on the blade $I \wedge X$; proved.)} For every $\Lambda \neq 0$, $I \wedge V = I \wedge X = \ninf \wedge \nO$, with $(I \wedge V)^{2} = 1$ and $\iota = (I\wedge V)I_{6}$; on bivectors $\epsilon(I, V, B, B') = -\langle B\,\iota\,B'\rangle_{0}$, a symmetric form invariant under the stabiliser of $(I, V)$ and odd under the internal reflection in a vector of $\{I, V\}^{\perp}$ (as spacetime densities after elimination, the $\epsilon$ terms are even under ordinary parity and the Pontryagin term odd). The breaking term $\epsilon(I, V, B, B)$ therefore needs the second vector (the slot count of Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector}(iii)) and depends on the pair only through a unit blade independent of $\Lambda$, so $\Lambda$ enters $S_{a,b}$ only through the connection and the coefficient $a$.
\item[(ii)] \emph{(Eliminating $B$; proved.)} At each point $S_{a,b}$ has a stationary point in $B$ exactly when the translational block of $F$ vanishes, that is when the torsion vanishes; there $B_{L} = 2(b - a\iota)F_{L}/(a^{2} + b^{2})$ is unique, the other blocks of $B$ are free multipliers, and the value is
\[
S_{a,b} = \frac{1}{a^{2} + b^{2}}\Big(a\int\epsilon(I, V, F, F) + b\int\langle F \wedge F\rangle_{0}\Big).
\]
At $b = 0$, $a = \alpha$ this is $\alpha^{-1}\int\epsilon(I, V, F, F)$, the frozen-point integrand of Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector}(iii) with $1/\alpha$ in place of its prefactor. On torsion-free fields $\langle F \wedge F\rangle_{0} = \langle R \wedge R\rangle_{0}$: the cross term $\langle R \wedge e \wedge e\rangle_{0}$ vanishes by the first Bianchi identity and $\langle e\wedge e \wedge e \wedge e\rangle_{0}$ vanishes identically, so $b$ adds only the Pontryagin density, and at $a = 0$ the reduced theory is topological.
\item[(iii)] \emph{(Same vacuum solutions; proved.)} The vacuum connection equation of $\int\epsilon(I, V, F, F)$, the map $T \mapsto \epsilon(I, V, \cdot, T \wedge e)$ on the $24$ torsion components, has rank $24$, so it is equivalent to zero torsion. Hence in vacuum the multiplier constraint of (ii) is already a field equation of the frozen-point functional, the same rank forces the translational multiplier to vanish, and the stationary points of $S_{\alpha, 0}$ are exactly those of the frozen-point functional with $B_{L} = -(2/\alpha)\,\iota F_{L}$. With a matter source coupled to the connection the same rank-$24$ map solves $B_{V}$ for the spin density while the torsion stays zero, so off vacuum $S_{\alpha, 0}$ and the stored functional with the Einstein-Cartan coupling of Fact \claimref{synthesis.imported-einstein-cartan-matter-coupling} differ.
\item[(iii$'$)] \emph{(The translational term; proved.)} The symmetric form $\langle B_{V}\, B'_{V}\rangle_{0}$ is invariant under the stabiliser of $(I, V)$. For $S_{a,b,c}$ the stationary point in $B$ exists for every $F$: $B_{L}$ as in (ii) and $B_{V} = 2F_{V}/c$, with value $S_{a,b} + \tfrac1c\int\langle F_{V}\wedge F_{V}\rangle_{0}$, a torsion-squared term in place of the zero-torsion constraint, which tends to zero as $c \to \infty$ and leaves the frozen-point functional, whose connection equation with spinning matter is that of the Einstein-Cartan coupling. The zero-torsion coupling of (iii) is therefore a property of the Lorentz-block restriction, not of the BF form.
\item[(iv)] \emph{(The BF sector is pure transport; proved.)} At $a = b = 0$ the field equations are $F = 0$ and $DB = 0$; for the store's tractor gauge field on the Einstein region $F = 0$ exactly where the Weyl part $W$ vanishes (its algebraic field strength is $-W$, Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}), that is on the locally de Sitter ($\Lambda > 0$) or anti-de Sitter ($\Lambda < 0$) fields, where transport is path-independent. With $a = \alpha$, $b = 0$, on a vacuum Einstein field $B_{L} = (2/\alpha)\,\iota W$: $B$ vanishes exactly on the pure-transport fields, annihilates $I$ and $V$, and measures the Weyl part.
\item[(v)] \emph{(The coupling; proved, given the stored normalisation.)} For torsion-free fields, in the orientation stated, $\frac{1}{Q(I)}\epsilon(I, V, F, F) = -(\mathcal{R} - 2\Lambda)\det(\hb^{-1})\,d^{4}x + \frac{3}{\Lambda}\epsilon(I, V, R, R)$, with $\mathcal{R}$ the store-sign scalar curvature ($\mathcal{R} = 4\Lambda$ on de Sitter). With the functional normalised as in Theorem \claimref{synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part}(iv) (frame equation $\mathcal{G}(a) + \Lambda a + 8\pi G\,T(a) = 0$, so the coefficient of $\int\epsilon(I, V, F, F)$ has magnitude $1/(16\pi G\,|Q(I)|)$) and $N^{2} = 1/(G\,Q(I))$ for $\Lambda > 0$ (Fact \claimref{standard-model.imported-frozen-point-dictionary}, Theorem \claimref{synthesis.de-sitter-entropy-pi-n-squared}), matching (ii) gives $|a|/(a^{2} + b^{2}) = N^{2}/(16\pi)$, so
\[
|a|\,N^{2} = 16\pi\,\frac{a^{2}}{a^{2} + b^{2}}, \qquad |\alpha| = 16\pi G\,Q(I) = \frac{16\pi}{N^{2}} \ \text{ at } b = 0,\ a = \alpha .
\]
With coefficient $\lambda$ on $\langle B \wedge F\rangle_{0}$ the effective value is $\lambda^{2}$ times that at coefficient $1$, the same as coefficient $1$ with breaking $(a, b)/\lambda^{2}$; so $\alpha N^{2}$ is fixed by the normalisation of the BF term (and by $b$), not by the series: it is the definition of $N$ re-expressed, not a relation.
\end{enumerate}

## technical
Freidel and Starodubtsev (cited from memory) read MacDowell-Mansouri gravity as topological BF theory of the de Sitter group broken by a quadratic term in $B$ with a tiny dimensionless coupling. This result tests that reading on the series' objects. The frozen point plays two parts: it reduces the ambient group to its stabiliser, the de Sitter or anti-de Sitter group, and its norm sets the coupling. It is not the breaking datum: the breaking term $\epsilon(I, V, B, B)$, odd under the internal reflection, needs a second vector, and it depends only on the blade $I \wedge X$ spanned by the frozen point and the canonical tractor, a unit blade the same for every $\Lambda$. A breaking even under that reflection leaves the reduced theory topological.

With the breaking on the Lorentz block, eliminating $B$ returns exactly the frozen-point integrand $\epsilon(I, V, F, F)$, with $1/\alpha$ as prefactor, plus a Pontryagin term for any even part of the breaking; the translational components of $B$ are multipliers that set the torsion to zero. In vacuum that constraint costs nothing, because the functional's own connection equation already forces zero torsion (a rank-$24$ map), so the BF form and the stored functional agree in vacuum. With spinning matter they differ: the BF form keeps the torsion zero and puts the spin into the multiplier, giving the torsion-free coupling with the Hilbert source, while the stored functional carries the Einstein-Cartan coupling. Adding the invariant translational term $c\langle B_{V}\wedge B_{V}\rangle_{0}$ trades the constraint for a torsion-squared term that vanishes as $c \to \infty$, returning the Einstein-Cartan case, so the matter coupling is decided by where the breaking is supported, not by the BF form (the even term of Freidel and Starodubtsev may include this translational piece; from memory). With no breaking the field equations say the reduced connection is flat: for the tractor gauge field this is the vanishing of the Weyl part, the locally de Sitter field, on which transport is path-independent. With breaking, on a vacuum field the multiplier $B$ is $2/\alpha$ times the dual Weyl curvature, so it vanishes exactly on pure transport.

The coupling in the store's normalisation is $16\pi G\,Q(I) = 16\pi/N^{2}$, about $10^{-120}$. The pre-registered test was whether this ties $\alpha$ to $N$ without a free factor. It does not: rescaling $B$ changes $\alpha$ at fixed physics, and the factor is $16\pi$ in the Clifford scalar-part normalisation and $1$ in the normalisation Freidel and Starodubtsev quote, so $\alpha N^{2}$ is a convention and the coupling is $N$ re-expressed.

For the three imports of the open problem: the action principle is not removed (the BF form with its breaking is still an action); the MacDowell-Mansouri form is rewritten, not reduced, as the choice of a quadratic breaking on the blade of the pair (frozen point, canonical tractor), which is the same choice as $\epsilon(I, V, F, F)$ because elimination inverts the quadratic form, on the same field space of connections preserving the frozen point; the Einstein-Cartan coupling is not supplied, since the breaking's support decides it. The Euler term comes out together with the Einstein-Hilbert and cosmological terms, so the BF form does not remove it. Transport-convenient: the topological sector is pure transport and gravity is its breaking, but the dynamics is still imported. All algebra is checked exactly in $\Cl(2,4)$, at $\Lambda = 3/4, -3/2, 12$, on de Sitter, Bianchi I and Kasner samples.

## lay
One way physicists have rewritten Einstein's gravity treats it as a broken version of a much simpler theory, one with no local dynamics at all, in which only the global shape of things matters. The breaking is controlled by a single tiny number. This result checks that rewriting against the series' own objects. The simple, unbroken theory turns out to be exactly the series' idea of pure transport: moving things around with no dependence on the path taken, which the series has in a universe of pure cosmological constant. Gravity is the breaking of it. But the series' frozen point cannot do the breaking alone: it needs a second object, the canonical tractor, and only the plane the two span matters. The tiny controlling number comes out as $16\pi$ divided by the square of the series' large number $N$, about $10^{-120}$, but the $16\pi$ is a choice of bookkeeping, so this is not a new prediction. Without spinning matter the rewriting and the series' action agree; with it they can differ, depending on a choice the rewriting leaves open. The rewriting still assumes an action, and it does not explain how spinning matter couples to gravity.

## one-liner
In BF form with breaking on the Lorentz block, $\int\langle B \wedge F\rangle_{0} - \tfrac{a}{4}\int\langle B \wedge \iota B_{L}\rangle_{0}$ with $\iota = (I\wedge V)I_{6}$, the frozen-point functional is flat transport broken on the blade $I \wedge X = \ninf\wedge\nO$ ($\Lambda$-free; $\epsilon(I, V, B, B') = -\langle B\iota B'\rangle_{0}$, store-chart orientation): eliminating $B$ gives $a^{-1}\int\epsilon(I, V, F, F)$ plus multipliers for zero torsion, so the two agree in vacuum (rank $24$), while with spinning matter the BF form keeps zero torsion and differs from the stored Einstein-Cartan coupling (an invariant translational term $c\langle B_{V}\wedge B_{V}\rangle_{0}$ returns it as $c \to \infty$); the unbroken sector is $W = 0$, pure transport, with $B_{L} = (2/a)\iota W$ on shell; and $|\alpha| = 16\pi G\,Q(I) = 16\pi/N^{2}$ is a normalisation convention, not a relation. Transport-convenient; the action, its Euler term and the matter coupling stay imported.
