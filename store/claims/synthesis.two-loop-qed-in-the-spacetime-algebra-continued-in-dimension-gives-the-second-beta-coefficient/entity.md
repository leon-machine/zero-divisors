---
id: synthesis.two-loop-qed-in-the-spacetime-algebra-continued-in-dimension-gives-the-second-beta-coefficient
kind: claim
version: 2
title: 'Two-loop QED in the spacetime algebra gives the second beta coefficient'
status: proved
region: synthesis
subject: quantum-fields
tags: [recovers-known-physics, scattering-amplitudes, running-and-unification, gauge-fields]
proposed_by:
  kind: ai
  session: 2026-11-02-qft-full
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
imported_from:
- citation: 'K. G. Chetyrkin and F. V. Tkachov, Integration by parts: the algorithm to calculate beta-functions in 4 loops, Nucl. Phys. B 192 (1981), 159--204.'
  key: ChetyrkinTkachov1981
  locator: 'the integration-by-parts identities (the triangle rule), the massless one-loop bubble G(a, b) as a ratio of Gamma functions, and the two-loop self-energy integral with five unit lines equal to 6 zeta(3)/q^2 in four dimensions; imported in Fact synthesis.imported-dimensional-regularisation-and-the-bmhv-gamma5 (iv)'
  doi: 10.1016/0550-3213(81)90199-1
- citation: 'M. Steinhauser, Results and techniques of multi-loop calculations, Phys. Rept. 364 (2002), 247--357; arXiv:hep-ph/0201075.'
  key: Steinhauser2002
  locator: 'eq. (2.33): Z3 = 1 - (alpha/pi)(1/(3 eps) + (alpha_s/pi) C_F/(8 eps)), with the statement that the sum of the bare two-loop diagrams has only a simple pole and does not depend on the gauge parameter; read 2026-11-02'
  doi: 10.1016/S0370-1573(02)00142-6
- citation: 'S. Fanchiotti, B. A. Kniehl and A. Sirlin, Incorporation of QCD effects in basic corrections of the electroweak theory, Phys. Rev. D 48 (1993), 307--331; arXiv:hep-ph/9212285.'
  key: FanchiottiKniehlSirlin1993
  locator: 'eq. (7c) and the text after eq. (7a): the massless limit of the order alpha alpha_s light-quark vacuum polarisation constant, f2 = 55/12 - 4 zeta(3), with f1 = 5/3 at one loop; read 2026-11-02 (journal data from memory)'
- citation: 'R. Jost and J. M. Luttinger, Vacuumpolarisation und e^4-Ladungsrenormalisation fur Elektronen, Helv. Phys. Acta 23 (1950), 201--214.'
  key: JostLuttinger1950
  locator: 'the order e^4 charge renormalisation of electrodynamics (the second coefficient of the beta function); imported in Fact synthesis.imported-lsz-reduction-ward-identity-and-the-second-qed-beta-coefficient (iii)'
- citation: 'J. C. Ward, An identity in quantum electrodynamics, Phys. Rev. 78 (1950), 182.'
  key: Ward1950
  locator: 'Z1 = Z2 to all orders from the derivative of the self-energy; imported in Fact synthesis.imported-lsz-reduction-ward-identity-and-the-second-qed-beta-coefficient (ii)'
  doi: 10.1103/PhysRev.78.182
- citation: 'M. Abramowitz and I. A. Stegun, Handbook of Mathematical Functions, National Bureau of Standards (1964).'
  key: AbramowitzStegun1964
  locator: '6.1.33: ln Gamma(1 + z) = -gamma z + sum_{n >= 2} (-1)^n zeta(n) z^n / n; cited from memory'
derivations:
- name: main
  uses:
  - synthesis.one-loop-qed-in-the-spacetime-algebra@2
  - field-theory.coupled-system-tree-level@3
  - synthesis.imported-dimensional-regularisation-and-the-bmhv-gamma5@2
  - synthesis.imported-one-loop-integrals-and-pauli-villars-regulators@1
  - synthesis.imported-lsz-reduction-ward-identity-and-the-second-qed-beta-coefficient@1
  assumes:
  - synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_contraction_rule_in_integer_dimensions
- kind: check
  ref: check.py::check_diagram_traces_against_clifford_scalar_parts
- kind: check
  ref: check.py::check_reduction_benchmarks
- kind: check
  ref: check.py::check_one_loop_beta0_and_finite_part
- kind: check
  ref: check.py::check_two_loop_simple_pole_beta1_and_finite_part
- kind: check
  ref: check.py::check_gauge_independence_and_transversality
- kind: check
  ref: check.py::check_subdivergences_cancel_between_vertex_and_self_energy
- kind: check
  ref: check.py::check_ward_identity_at_two_loops_integrand_by_integrand
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.one-loop-qed-in-the-spacetime-algebra
extraction:
  maintainer_pass:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 1 -> 2, by Leon''s decisions of 2026-11-02: an assumes edge to the Krein-form premise synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields@2, which the result states as its hypothesis (the covariant photon on internal lines); the dimensional-regularisation Fact repinned at @2, whose new clause (iv) holds the d-dimensional integral rules, the bubble and the 6 zeta3 benchmark that were cited from memory; a uses edge to the new Fact synthesis.imported-lsz-reduction-ward-identity-and-the-second-qed-beta-coefficient@1 (Ward 1950, Jost and Luttinger 1950); the Clifford-conjugation result accepted with it is cited by claimref and its reading corrected to its reviewed strength (it restates the one-particle Gupta-Bleuler form, it does not fix it). Statement and check unchanged.'
  open_problem: op.qft-loops-and-renormalisation
  note: >-
    The problem's second attack line (renormalisation beyond one loop, Z1 = Z2 at two loops). Standard results:
    the second coefficient of the QED beta function (Jost and Luttinger 1950), Z1 = Z2 (Ward 1950), the two-loop
    massless vacuum polarisation and its constant (checked against Steinhauser 2002, eq. (2.33), and Fanchiotti,
    Kniehl and Sirlin 1993, eq. (7c)), recomputed here, not copied. What is new is only that the series'
    formalism reproduces them beyond one loop: the Dirac algebra is the spacetime algebra's product continued in
    dimension by one Clifford contraction rule, checked against the Clifford algebras of every integer dimension
    from four to eight; traces are four times the scalar part; the unit of the Feynman rules stands outside the
    product (no $I_{4}$ enters a vector-like loop, so the obstruction of the unit result does not arise); every
    coefficient is an exact rational function of $d$. Regulator: dimensional regularisation, imported (Fact
    synthesis.imported-dimensional-regularisation-and-the-bmhv-gamma5), not native; the integration-by-parts
    reduction, the bubble formula and the benchmark are its clause (iv) (Chetyrkin and Tkachov 1981).
    From Fact synthesis.imported-one-loop-integrals-and-pauli-villars-regulators only the Wick rotation (ii) and the
    covariant photon with its gauge parameter (iv) are used, not the Pauli-Villars clause (iii). The coefficient
    beta1 is the same in every mass-independent scheme for a single coupling, so it does not depend on the choice of
    dimensional regularisation; the constant 16 zeta3 - 55/3 is the MS-bar value. The result states the
    Krein-form premise as its hypothesis and has an assumes edge to it (2 November 2026). Transport-absent: no
    transport structure enters.
---

## formal
Under the Krein-form premise \claimref{synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields} (the covariant photon $(\delta_{\alpha\beta} - (1 - \xi)r_{\alpha}r_{\beta}/Q(r))/Q(r)$ on internal lines, Fact \claimref{synthesis.imported-one-loop-integrals-and-pauli-villars-regulators}(iv)), with the vertex of \claimref{field-theory.coupled-system-tree-level}, the conventions of \claimref{synthesis.one-loop-qed-in-the-spacetime-algebra} (trace equal to four times the scalar part; the unit of the Feynman rules a coefficient outside the Clifford product), after the Wick rotation (Fact \claimref{synthesis.imported-one-loop-integrals-and-pauli-villars-regulators}(ii)) and in dimensional regularisation, $d = 4 - 2\epsilon$ (Fact \claimref{synthesis.imported-dimensional-regularisation-and-the-bmhv-gamma5}(i)). Write $a = \alpha/(4\pi)$, $\Pi_{\mu\nu}(q) = (Q(q)\delta_{\mu\nu} - q_{\mu}q_{\nu})\Pi(Q(q))$ for one massless Dirac fermion, and $G(a_{1}, a_{2})$ for the massless one-loop bubble. The $d$-dimensional integral rules used (the radial integral, symmetric integration in $d$ dimensions, translation invariance, the vanishing of scale-free integrals and of total derivatives, hence integration by parts), the bubble formula and the five-line benchmark are those of Fact \claimref{synthesis.imported-dimensional-regularisation-and-the-bmhv-gamma5}(iv) \cite{ChetyrkinTkachov1981}. Then:
\begin{enumerate}
\item (The algebra in $d$ dimensions; computed.) The rule $\gamma_{\alpha}\gamma_{\alpha} = d$, $\gamma_{\alpha}Xb\gamma_{\alpha} = -(\gamma_{\alpha}X\gamma_{\alpha})b + 2bX$ ($b$ a vector, $X$ a product of vectors) reproduces $\sum_{\alpha}\gamma_{\alpha}X\gamma^{\alpha}$ in $\Cl(D, 0)$ for $D = 4, \ldots, 8$ and in $\Cl(1, D-1)$ for $D = 4, 5, 6$, and the resulting traces of every word below equal four times the scalar part of the explicit Clifford products in $\Cl(D, 0)$, $D = 4, 5, 6$.
\item (Reduction; computed.) With the denominators $Q(k)$, $Q(k - q)$, $Q(l)$, $Q(l - q)$, $Q(k - l)$, every two-loop integral that occurs is an exact rational function of $d$ times $M_{1} = G(1,1)^{2}$ plus a rational function of $d$ times $M_{2} = G(1,1)G(1, 3 - d/2)$ (integration by parts \cite{ChetyrkinTkachov1981}); on the benchmark with five unit lines this gives $6\zeta_{3} + O(\epsilon)$.
\item (One loop; computed.) $\Pi^{(1)} = -\tfrac{2(d-2)}{d-1}\,a\,(4\pi)^{\epsilon}G(1,1)\,Q(q)^{-\epsilon} = -\tfrac43\tfrac{a}{\epsilon} + \dots$, so $\beta_{0} = \tfrac43$ in $\mu^{2}da/d\mu^{2} = \beta_{0}a^{2} + \beta_{1}a^{3}$; the $\overline{\mathrm{MS}}$ constant is $-\tfrac{20}{9}a$.
\item (Two loops; computed.) Summed over the two self-energy insertions and the vertex correction: the coefficient of $1 - \xi$ vanishes identically in $d$, so the result does not depend on $\xi$ and holds in particular in the Feynman gauge $\xi = 1$, the gauge whose Fock space realises the one-particle Gupta-Bleuler form $-u\cdot w$ of (K1), which the store restates as the trace form of Clifford conjugation (\claimref{synthesis.clifford-conjugation-is-the-twistor-adjoint-and-its-trace-form-is-the-one-particle-gupta-bleuler-form}; a restatement, not a derivation of the premise), and $q_{\mu}q_{\nu}\Pi^{(2)}_{\mu\nu} = 0$ identically in $d$; in the Feynman gauge the self-energy insertions carry $+\tfrac43 a^{2}/\epsilon^{2}$ and the vertex correction $-\tfrac43 a^{2}/\epsilon^{2}$; the sum is $\Pi^{(2)} = a^{2}\bigl(-\tfrac{2}{\epsilon} + 16\zeta_{3} - \tfrac{55}{3} + 4\ln(Q(q)/\mu^{2}) + O(\epsilon)\bigr)$ in $\overline{\mathrm{MS}}$ normalisation. Hence $Z_{3} = 1 - \tfrac43\tfrac{a}{\epsilon} - 2\tfrac{a^{2}}{\epsilon}$, $\beta_{1} = 4$, and with $n_{f}$ fermions $\mu\,d\alpha/d\mu = \tfrac{2n_{f}}{3\pi}\alpha^{2} + \tfrac{n_{f}}{2\pi^{2}}\alpha^{3}$ \cite{JostLuttinger1950, Steinhauser2002, FanchiottiKniehlSirlin1993} (Fact \claimref{synthesis.imported-lsz-reduction-ward-identity-and-the-second-qed-beta-coefficient}(iii)).
\item (Ward identity at two loops; proved for the integrands, argued for the integrals.) In $\Cl(1,3)$ with massive lines and the unit outside the product, $S(k + h) - S(k) = -S(k + h)hS(k)$ makes the sum of the insertions of $h$ into the open fermion line of the rainbow, crossed and polarisation-insertion self-energies equal to minus the difference of the line at $p + h$ and at $p$, and the insertions into a closed loop telescope to the difference of one integrand at loop momenta $l + h$ and $l$; with the shift invariance of dimensional regularisation, $\Lambda^{(2)}(p, p) = -\partial\Sigma^{(2)}/\partial p$ and $Z_{1} = Z_{2}$ at two loops \cite{Ward1950} (as in Fact \claimref{synthesis.imported-lsz-reduction-ward-identity-and-the-second-qed-beta-coefficient}(ii)).
\end{enumerate}

## technical
Under the Krein-form premise, with the series' vertex and the conventions of one-loop electrodynamics in the spacetime algebra (traces four times the scalar part, the unit outside the product), after the Wick rotation and in dimensional regularisation, the two-loop vacuum polarisation of a massless Dirac fermion is computed exactly in the dimension $d$. The Dirac algebra is continued by one Clifford rule, $\gamma_{\alpha}\gamma_{\alpha} = d$ and $\gamma_{\alpha}Xb\gamma_{\alpha} = -(\gamma_{\alpha}X\gamma_{\alpha})b + 2bX$, which agrees with the explicit Clifford algebras of every integer dimension from four to eight; no $I_{4}$ enters the vector-like loop, so the obstruction recorded for the unit does not arise.

Scalar products are rewritten through the five denominators and every integral is reduced by integration by parts and the Gamma-function bubble (standard rules of dimensional regularisation, imported) to two masters with exact rational coefficients in $d$; the reduction reproduces the known value $6\zeta_{3}$ of the two-loop integral with five unit lines. At one loop the code gives $\beta_{0} = 4/3$ (with $a = \alpha/(4\pi)$). At two loops the dependence on the gauge parameter cancels identically in $d$ (so the Feynman gauge, whose Fock space realises the one-particle Gupta-Bleuler form, gives the same result as every covariant gauge), the polarisation is transverse identically in $d$, and the double pole of the self-energy insertions ($+4/3$) cancels that of the vertex correction ($-4/3$), which is the cancellation of the one-loop counterterms by $Z_{1} = Z_{2}$. What is left is a simple pole, $-2a^{2}/\epsilon$, so $\beta_{1} = 4$ per fermion, the standard value of Jost and Luttinger, $\mu\,d\alpha/d\mu = 2\alpha^{2}/(3\pi) + \alpha^{3}/(2\pi^{2})$, and the $\overline{\mathrm{MS}}$ constant $16\zeta_{3} - 55/3$ agrees with the literature. For a single coupling $\beta_{1}$ is the same in every mass-independent scheme, so it does not depend on the choice of dimensional regularisation; of the one-loop Fact only the Wick rotation and the covariant photon are used, not its Pauli-Villars clause.

At the level of integrands the Ward-Takahashi identity holds at two loops in $\Cl(1,3)$ with massive lines: the resolvent identity telescopes the insertions on each open line and on the closed loop, so with the shift invariance of dimensional regularisation $Z_{1} = Z_{2}$ at two loops.

## lay
Electrodynamics in the series' algebra of spacetime now goes one step beyond the first quantum corrections. The screening of charge by virtual electron pairs is computed to second order, with the dimension of spacetime treated as a variable so that the infinities appear in a controlled way; the algebra continues to any dimension through one rule, checked in every whole dimension from four to eight. The result has the textbook structure: it does not depend on the arbitrary choice of how the photon is described, it conserves charge, and the nested infinities of its pieces cancel among themselves because of the identity that keeps the electron's charge and its normalisation in step. The strength of the electric force grows with energy at the standard rate, including the standard second-order term. All of this holds under the series' premise that the photon's states carry the standard indefinite measure; the method of taming the infinities is borrowed, not the series' own, but the second-order rate does not depend on which standard method is used.

## one-liner
Under the Krein-form premise and in dimensional regularisation, two-loop electrodynamics in the spacetime algebra continued in dimension gives a transverse, gauge-parameter independent vacuum polarisation with a simple pole only (the subdivergences cancel by $Z_{1} = Z_{2}$), the standard $\beta_{1} = 4$ per fermion (Jost and Luttinger 1950; $\mu\,d\alpha/d\mu = 2\alpha^{2}/(3\pi) + \alpha^{3}/(2\pi^{2})$) and the $\overline{\mathrm{MS}}$ constant $16\zeta_{3} - 55/3$; $Z_{1} = Z_{2}$ at two loops integrand by integrand (argued for the integrals); the integration-by-parts rules imported.
