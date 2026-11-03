---
id: synthesis.one-loop-qed-in-the-spacetime-algebra
kind: claim
version: 2
title: 'One-loop electrodynamics in the spacetime algebra, in a covariant gauge with imported Pauli-Villars regulators: transverse vacuum polarisation with coefficient $e^{2}/(12\pi^{2})$, $F_{2}(0) = \alpha/(2\pi)$ through the real bivector $\gamma^{\mu} \wedge q$, $Z_{1} = Z_{2}$, and the unit outside the product on massive lines'
status: proved
region: synthesis
subject: quantum-fields
tags: [recovers-known-physics, scattering-amplitudes, pseudoscalar-and-centre, chirality]
proposed_by:
  kind: ai
  session: 2026-11-01-qft
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.field-theory.single-algebra-field
derivations:
- name: main
  uses:
  - field-theory.second-quantisation@5
  - field-theory.elementary-photon-ga@4
  - field-theory.coupled-system-tree-level@3
  - synthesis.imported-one-loop-integrals-and-pauli-villars-regulators@1
  assumes:
  - synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_chiral_traces_are_two_proj
- kind: check
  ref: check.py::check_vacuum_polarisation_transverse_with_log_coefficient_one_twelfth
- kind: check
  ref: check.py::check_contraction_identities_four_dimensional
- kind: check
  ref: check.py::check_vertex_magnetic_part_and_schwinger_coefficient
- kind: check
  ref: check.py::check_resolvent_and_ward_takahashi_integrand
- kind: check
  ref: check.py::check_unit_inside_massive_loop_breaks_transversality
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - field-theory.coupled-system-tree-level
extraction:
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 1 -> 2, by Leon''s decisions of 2026-11-01: an assumes edge to the Krein-form premise synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields@1, which this result states as its hypothesis (the indefinite-form premise for the gauge field, now cited by claimref at the formal and technical levels and in the proof), and a uses edge to the imported Fact synthesis.imported-one-loop-integrals-and-pauli-villars-regulators@1 (Feynman parametrisation, the Wick-rotated integrals, Pauli-Villars, the covariant photon propagator, on-shell states), which replaces the citation from memory. Statement and check unchanged.'
  open_problem: op.qft-loops-and-renormalisation
  note: >-
    The problem's first attack line: one-loop vacuum polarisation, the Schwinger term and the Ward identity
    with exact rational coefficients and a stated regulator. These are standard results (Schwinger 1948;
    Pauli and Villars 1949; Peskin and Schroeder chs. 6 and 7; the machinery imported in synthesis.imported-one-loop-integrals-and-pauli-villars-regulators); the content here is
    that the series' formalism reproduces them, with the Dirac algebra as the spacetime algebra's product and
    the trace as four times the scalar part, and where the unit $i = I_{4}$ may stand. The Feynman-parameter
    integrals are exact rationals ($\int_{0}^{1} x(1-x)\,dx = 1/6$; the magnetic integral is $1$);
    the logarithms and $\pi$ are kept symbolic. Imported (Fact synthesis.imported-one-loop-integrals-and-pauli-villars-regulators;
    the gauge-field form is Premise synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields): the covariant photon propagator $-g_{\mu\nu}/k^{2}$ on internal
    off-shell lines, which needs the indefinite-form quantisation of the gauge field (the Krein-form premise for
    covariant gauges; the gauge-fixing result synthesis.self-adjoint-brst-charge-needs-a-krein-form-and-the-tower-supplies-the-ghosts and the gauge
    independence of on-shell quantities, since the stored photon gives covariant exchange only at tree level
    on conserved currents; Feynman parametrisation; the Wick-rotated integrals of $(\ell^{2} - \Delta)^{-n}$;
    Pauli-Villars regulators (fields of negative weight); on-shell external states. The scheme: Pauli-Villars
    fermions on the fermion loop for clause (2), a Pauli-Villars photon on the photon line for clauses (3) and
    (4). Pauli-Villars regulators of a single Weyl fermion carry Dirac masses and break chirality, so the
    chiral statement in (2) is about the numerator only. Transport-absent: no transport structure enters; the
    spacetime algebra is convenient (the magnetic structure is a real bivector, chiral traces are $2\proj$).
    Clause (5) is the formalism-specific finding and is the loop-level consequence of the unit result filed
    alongside (synthesis.unit-i4-keeps-its-three-properties-only-in-dimension-zero-mod-four): the unit that
    stays covariant is the right unit, equivalently a coefficient outside the product.
---

## formal
Work in a covariant gauge, under the indefinite-form (Krein) premise for the gauge field, Premise \claimref{synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields} (imported, Fact \claimref{synthesis.imported-one-loop-integrals-and-pauli-villars-regulators}: the covariant propagator $-g_{\mu\nu}/k^{2}$ on internal lines; the photon of Proposition \claimref{field-theory.elementary-photon-ga}(4) gives the covariant form only at tree level on conserved currents). Take the Dirac matrices as the spacetime algebra's product (vectors $\gamma_{\mu}$ of $\Cl(1,3)$, reciprocal frame $\gamma^{\mu}$), the propagator numerator of momentum $k$ as the multivector $k + m$, the vertex as $\gamma^{\mu}$ with the coupling of Proposition \claimref{field-theory.coupled-system-tree-level}, and the units of the Feynman rules and of the Wick rotation as coefficients collected in front of the Clifford product. Regulate with imported Pauli-Villars fields of weights $c_{i}$ (negative weights included), $\sum_{i} c_{i} = \sum_{i} c_{i}M_{i}^{2} = 0$ ($c_{0} = 1$, $M_{0} = m$): fermions on the fermion loop in (2), a photon on the photon line in (3) and (4). Then:
\begin{enumerate}
\item (Traces.) The matrix trace of $X \in \Cl(1,3)$ is $4\langle X\rangle_{0}$, and the chiral traces are $2(\langle X\rangle_{0} \mp i\,x_{4})$, $x_{4}$ the coefficient of $I_{4}$ in $X$: twice $\proj(X)$ of Definition \claimref{obj.field-theory.single-algebra-field}, read with $I_{4} \mapsto \mp i$.
\item (Vacuum polarisation.) With $k = \ell - xq$, $k' = \ell + (1-x)q$ and four-dimensional symmetric integration, the numerator $4\langle\gamma^{\mu}(k+m)\gamma^{\nu}(k'+m)\rangle_{0}$, read as the map $a \mapsto \sum_{\mu\nu}a_{\mu}N^{\mu\nu}\gamma_{\nu}$, is $a \mapsto -2Q(\ell)a + 8x(1-x)(Q(q)a - (a\cdot q)q) + 4\Delta a$, $\Delta = m^{2} - x(1-x)Q(q)$. The part proportional to $a$ has Euclidean radial integral $L - \Delta + \Delta^{2}/(L + \Delta)$ at squared cut-off $L$, so under the regulators it vanishes as $L \to \infty$; the polarisation is transverse, $\Pi(a) = (Q(q)a - (a\cdot q)q)\Pi(q^{2})$, with $\Pi(q^{2}) = -\tfrac{e^{2}}{2\pi^{2}}\int_{0}^{1}x(1-x)\ln(M^{2}/\Delta)\,dx$ up to a constant, $M$ the regulator scale. The coefficient of the logarithm is $e^{2}/(12\pi^{2})$ per Dirac fermion, its rational part $\tfrac{1}{16}\int_{0}^{1}8x(1-x)\,dx = \tfrac{1}{12}$. For a massless chiral fermion the numerator (not the regulated loop, whose regulators carry Dirac masses) has $I_{4}$ part zero after the shift and symmetric integration, and scalar part half the Dirac one.
\item (Vertex.) In four dimensions $\gamma^{\nu}a\gamma_{\nu} = -2a$, $\gamma^{\nu}ab\gamma_{\nu} = 4a\cdot b$, $\gamma^{\nu}abc\gamma_{\nu} = -2cba$. With Feynman parameters $(x, y, z)$, $k = \ell - yq + zp$, $k' = \ell + (1-y)q + zp$, $p' = p + q$ on shell, the $\ell$-free part of $\gamma^{\nu}(k'+m)\gamma^{\mu}(k+m)\gamma_{\nu}$ between $(p'+m)$ and $(p+m)$ equals $a\gamma^{\mu} + b(p+p')^{\mu} + c\,q^{\mu}$ with $b = 2mz(1-z)$ and $c = -2m(z-2)(x-y)$, odd under $x \leftrightarrow y$; the $Q(\ell)$ part is $Q(\ell)\gamma^{\mu}$. Between the same projectors $(p+p')^{\mu} = 2m\gamma^{\mu} + \gamma^{\mu} \wedge q$ (the Gordon identity; $\gamma^{\mu} \wedge q$ is $-i\sigma^{\mu\nu}q_{\nu}$ in the matrix reading). The magnetic form factor is $F_{2}(0) = \tfrac{e^{2}}{8\pi^{2}}\,m\int b/\Delta = \tfrac{e^{2}}{8\pi^{2}} = \tfrac{\alpha}{2\pi}$, the parameter integral being exactly $1$.
\item (Ward identity.) $S(k) = (k - m)^{-1} = (k + m)/(Q(k) - m^{2})$ satisfies $S(k + h) - S(k) = -S(k+h)\,h\,S(k)$, so with the regulator on the photon line only the self-energy integrand obeys $\Sigma(p + h) - \Sigma(p) = -h_{\mu}\Lambda^{\mu}(p + h, p)$ integrand by integrand: the Ward-Takahashi identity, and at $h \to 0$, $\Sigma'(p) = -\Lambda(p, p)$, so $Z_{1} = Z_{2}$.
\item (Where the unit stands.) If the unit is instead placed as $I_{4}$ inside the product at each propagator, the polarisation numerator becomes $-N + 8m^{2}\,\mathrm{id}$ ($N$ the numerator of (2), $\mathrm{id}$ the identity map on vectors): it agrees for massless lines, and for a massive loop the extra term leaves a non-transverse remainder proportional to $\sum_{i} c_{i}M_{i}^{2}\ln\Delta_{i}$, not zero. So on a massive Dirac line the unit is a coefficient outside the Clifford product (equivalently the right unit).
\end{enumerate}

## technical
In a covariant gauge, under the indefinite-form (Krein) premise for the gauge field (\claimref{synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields}; the covariant photon propagator inside loops is imported, \claimref{synthesis.imported-one-loop-integrals-and-pauli-villars-regulators}), with the Dirac matrices as the spacetime algebra's product, propagator numerators $k + m$, the vertex $\gamma^{\mu}$, the units of the Feynman rules and the Wick rotation collected in front of the Clifford product, and imported Pauli-Villars regulators of positive and negative weight ($\sum c_{i} = \sum c_{i}M_{i}^{2} = 0$; fermions on the fermion loop, a photon on the photon line), one-loop electrodynamics reproduces the standard results with exact rational coefficients. The trace is four times the scalar part, and the chiral traces are $2\proj$ read with $I_{4} \mapsto \mp i$.

The vacuum-polarisation numerator after the shift is $a \mapsto -2Q(\ell)a + 8x(1-x)(Q(q)a - (a\cdot q)q) + 4\Delta a$; the part proportional to $a$ has radial integral $L - \Delta + \Delta^{2}/(L+\Delta)$ and cancels under the regulators, leaving a transverse polarisation whose logarithm has coefficient $e^{2}/(12\pi^{2})$ per Dirac fermion ($\int_{0}^{1}x(1-x)\,dx = 1/6$). For a massless chiral fermion the numerator's $I_{4}$ part vanishes after the shift and symmetric integration and its scalar part is half; this is a statement about the numerator, since the regulators carry Dirac masses.

In the vertex the four-dimensional contraction identities and the on-shell projectors leave a magnetic coefficient $b = 2mz(1-z)$, the Gordon identity carries the real bivector $\gamma^{\mu} \wedge q$, and the exact parameter integral gives $F_{2}(0) = \alpha/(2\pi)$. The resolvent identity $S(k+h) - S(k) = -S(k+h)hS(k)$ gives the Ward-Takahashi identity integrand by integrand, so $Z_{1} = Z_{2}$.

Placing the unit as $I_{4}$ inside the product at each propagator instead flips the mass term: harmless on massless chiral lines, but on a massive loop it leaves a non-transverse remainder proportional to $\sum c_{i}M_{i}^{2}\ln\Delta_{i}$, so on massive lines the unit stands outside the product.

## lay
The standard first quantum corrections of electrodynamics, the screening of charge by virtual pairs, the electron's extra magnetic moment and the identity that keeps charge the same at every order, come out of the series' algebra of spacetime with the usual numbers. Two standard ingredients are taken from the literature: the usual covariant description of the photon inside loops, and the usual way of taming the infinities with heavy auxiliary particles, some of which enter with negative weight; both rest on a premise the series adopts, that the photon's states carry the standard indefinite measure in which some unphysical states have negative length. The charge screening has the textbook strength, the magnetic correction is the fine-structure constant over two pi, and the magnetic structure is a plain plane element of spacetime with no imaginary number in it. One point is specific to the series: its imaginary unit, the spacetime volume element, may sit inside the algebraic products only on massless lines; on massive lines it must stay outside, or charge conservation fails.

## one-liner
Under the Krein-form premise, in a covariant gauge with imported Pauli-Villars regulators (some of negative weight), one-loop electrodynamics in the spacetime algebra gives a transverse vacuum polarisation with coefficient $e^{2}/(12\pi^{2})$, $F_{2}(0) = \alpha/(2\pi)$ through the real bivector $\gamma^{\mu} \wedge q$, and $Z_{1} = Z_{2}$, with the unit outside the product on massive lines.
