---
id: synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator-and-ward-preserving-extensions-differ-only-by-the-renormalisation-constants
kind: claim
version: 2
title: 'Regulator-free one-loop vacuum polarisation and Ward-preserving extensions'
status: proved
region: synthesis
subject: quantum-fields
tags: [recovers-known-physics, scattering-amplitudes, running-and-unification, needs-continuum]
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
- obj.tower.tower
imported_from:
- citation: 'H. Epstein and V. Glaser, The role of locality in perturbation theory, Ann. Inst. H. Poincare A 19 (1973), 211--295.'
  key: EpsteinGlaser1973
  locator: 'Sec. 5'
- citation: 'R. Brunetti and K. Fredenhagen, Microlocal analysis and interacting quantum field theories: renormalization on physical backgrounds, Commun. Math. Phys. 208 (2000), 623--661; arXiv:math-ph/9903028.'
  key: BrunettiFredenhagen2000
  locator: 'Thm. 5.2; Thm. 5.3'
  doi: 10.1007/s002200050004
- citation: 'D. Z. Freedman, K. Johnson and J. I. Latorre, Differential regularization and renormalization: a new method of calculation in quantum field theory, Nucl. Phys. B 371 (1992), 353--414.'
  key: FreedmanJohnsonLatorre1992
- citation: 'G. Scharf, Finite Quantum Electrodynamics: The Causal Approach, 2nd ed., Springer, Berlin (1995).'
  key: Scharf1995
  locator: 'the existence of gauge-invariant (Ward-preserving) time-ordered products in the causal approach; imported in Fact synthesis.imported-epstein-glaser-extension-theorem-and-ward-preserving-time-ordered-products (iii)'
- citation: 'S. Hollands and R. M. Wald, Local Wick polynomials and time ordered products of quantum fields in curved spacetime, Commun. Math. Phys. 223 (2001), 289--326; arXiv:gr-qc/0103074.'
  key: HollandsWald2001
derivations:
- name: main
  uses:
  - field-theory.second-quantisation@5
  - field-theory.coupled-system-tree-level@3
  - field-theory.twistor-attachment@6
  - synthesis.floor-regulator-keeps-the-charge-and-the-central-term-below-the-cut-off@3
  - synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport@2
  - synthesis.hadamard-dirac-states-scale-to-the-flat-massless-vacuum-at-every-point-of-a-gravitational-field@3
  - synthesis.imported-epstein-glaser-extension-theorem-and-ward-preserving-time-ordered-products@1
  assumes:
  - synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_spin_traces_and_homogeneity_in_the_spacetime_algebra
- kind: check
  ref: check.py::check_vacuum_polarisation_extension_is_transverse_and_gives_the_log_coefficient
- kind: check
  ref: check.py::check_covariant_ambiguities_are_the_renormalisation_constants
- kind: check
  ref: check.py::check_scalar_bubble_extension_gives_the_quartic_coefficient
- kind: check
  ref: check.py::check_scaling_degrees_and_degrees_of_divergence
- kind: check
  ref: check.py::check_no_weighting_of_the_conformal_energy_keeps_a_boost
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.one-loop-qed-in-the-spacetime-algebra
  - synthesis.floor-regulator-keeps-the-charge-and-the-central-term-below-the-cut-off
  - synthesis.hadamard-scaling-limit-premise
extraction:
  maintainer_pass:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 1 -> 2, by Leon''s decisions of 2026-11-02: an assumes edge to the Krein-form premise synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields@2, because clause (iii) states it as the hypothesis of its self-energy and vertex parts (the edge covers only those parts; clauses (ii), (vi) and the vacuum polarisation use neither the premise nor a regulator); a uses edge to the new imported Fact synthesis.imported-epstein-glaser-extension-theorem-and-ward-preserving-time-ordered-products@1 (the extension theorem and the existence of Ward-preserving time-ordered products), which replaces the citations from memory; the pin of the floor-regulator result moves to @3, into which clause (vii) is merged as its clause (v); the triangle result accepted with it is now cited by claimref (no uses edge: it is a consequence drawn, not a premise); the lay level states the conditions. Statement unchanged.'
  open_problem: op.qft-loops-and-renormalisation
  note: >-
    Answers the problem's first attack line (a native Lorentz-covariant regulator) by the extension of
    distributions across the coincident points, ordered by the scaling degree, the calculus of the stored Hadamard
    scaling results. Standard throughout: the extension theorem (Epstein and Glaser 1973, Sec. 5; Brunetti and
    Fredenhagen 2000, Thms. 5.2 and 5.3; imported, synthesis.imported-epstein-glaser-extension-theorem-and-ward-preserving-time-ordered-products, where the theorem numbers and statements are
    checked against the arXiv text); differential renormalisation and this vacuum polarisation
    (Freedman, Johnson and Latorre 1992; the identity Q^-2 = -(1/4) box(ln(M^2 Q)/Q) off the origin checked against
    eq. (1) of arXiv:hep-ph/9203207, the journal reference cited from memory); the existence of Ward-preserving
    time-ordered products in electrodynamics (Scharf; imported, synthesis.imported-epstein-glaser-extension-theorem-and-ward-preserving-time-ordered-products (iii)); the one-loop values
    (e^2/(12 pi^2), 3/(16 pi^2), Z1 = Z2) are textbook. What the store gains: the first loop result with no
    regulator; the vacuum polarisation coefficient, and with it the fermion weight of the running, without
    Pauli-Villars fields of negative weight and without the Krein-form premise (the stored one-loop result needs
    both); the covariant difference spaces of the one-loop extensions as exact ranks of polynomial maps in Cl(1,3)
    with the unit I4 (the parity-odd differences I4 and q I4 are left multiplications, distinct from the field
    theory's unit, which stands outside the product); the uniqueness of a vector-conserving three-current
    extension, which makes the axial divergence computed with Pauli-Villars fields in the triangle result
    (synthesis.triangle-anomaly-in-the-spacetime-algebra-is-the-pseudoscalar-part-of-the-field-square-and-cancels-per-generation)
    the same in every covariant vector-conserving scheme; and, as a separate step on the stored seven-dimensional
    commutant of the floor result, the closure and Schur argument that no smooth weighting of the floors keeps a
    boost. What is not proved here: that an extension obeying the Ward-Takahashi identity, transversality of the
    four-photon kernel, or conservation of the two vector currents exists; this is imported (Scharf; the Fact
    above, clause (iii)). The self-energy and vertex kernels contain the photon propagator in a covariant gauge, so
    the parts of clause (iii) about them are read under the Krein-form premise
    synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields, to which the result has an assumes edge
    (2 November 2026) covering those parts only; clauses (ii) and (vi) do not use it. Transport-absent for clauses (i) to (iv) and (vi); clause (v) is
    transport-convenient (it runs through the store's Hadamard scaling theorem) and argued; clause (vii) uses the
    conformal model and is transport-convenient. The Euclidean section and its continuation to the Feynman
    distributions are the standard Wick rotation; the unit there is the bare i of complex analysis, as the
    conventions allow. Clause (vii) is merged (2 November 2026) into version 3 of the floor-regulator result
    (synthesis.floor-regulator-keeps-the-charge-and-the-central-term-below-the-cut-off), as its clause (v).
  flags:
  - 'the differential-renormalisation identity was checked against a later paper of the same school, not the 1992 original'
  - 'the existence of Ward-preserving extensions beyond the vacuum polarisation (self-energy and vertex, four-photon, three-current) is imported (Scharf; Fact synthesis.imported-epstein-glaser-extension-theorem-and-ward-preserving-time-ordered-products (iii)), not proved'
  - 'the self-energy and vertex kernels rest on the Krein-form premise (covariant photon propagator); the assumes edge added on 2 November 2026 covers those parts only'
  - 'clause (v) is argued: products of Hadamard Feynman parametrices obey the scaling-degree bound by the wave front set condition (Brunetti and Fredenhagen), and the curved-field ambiguities are those of Hollands and Wald, both cited from memory'
  - 'Schur''s lemma for irreducible unitary representations and the irreducibility of the attachment''s one-particle helicity modules under the conformal algebra are cited from memory'
---

## formal
Units $\hbar = c = 1$. Work on the Euclidean section of the flat field (the Feynman distributions follow by the standard Wick rotation), with $s = Q(x)$ for the square of the vector $x$, $\partial^{2} = \nabla^{2}$ and $L_{\mu} = \ln(\mu^{2}s)$. Symmetric two-tensor kernels are written as linear functions of a vector $a$; the transverse operator is $T(f)(a) = (a\cdot\nabla)\nabla f - a\,\nabla^{2}f$ (in index reading $(\partial_{\mu}\partial_{\nu} - g_{\mu\nu}\partial^{2})f$). Take the Dirac field of Proposition \claimref{field-theory.second-quantisation}, the vertex and coupling of Proposition \claimref{field-theory.coupled-system-tree-level}, the vectors of $\Cl(4,0)$ (Euclidean section) or $\Cl(1,3)$ with their Clifford product (the Dirac matrices in the matrix reading), and the massless propagator $S_{0}(x) = x/(2\pi^{2}s^{2})$ as a vector-valued kernel. Assume the extension theorem (Epstein and Glaser \cite{EpsteinGlaser1973}; Brunetti and Fredenhagen \cite{BrunettiFredenhagen2000}, Thms. 5.2, 5.3; Fact \claimref{synthesis.imported-epstein-glaser-extension-theorem-and-ward-preserving-time-ordered-products}(i), (ii)): a distribution on $\R^{n}\setminus\{0\}$ of scaling degree $\mathrm{sd} < n$ has a unique extension of the same degree; for $\mathrm{sd} \ge n$ extensions exist and two differ by $\sum_{|a| \le \omega}c_{a}\partial^{a}\delta$, $\omega = \mathrm{sd} - n$. The method and every value below are standard; the statement records them in the series' algebra.
\begin{enumerate}
\item[(i)] \emph{(Traces and degrees; computed.)} $\langle\gamma_{\mu}x\gamma_{\nu}x\rangle_{0} = 2x_{\mu}x_{\nu} - g_{\mu\nu}Q(x)$, $\langle\gamma_{\mu}x\gamma_{\nu}\rangle_{0} = 0$, $\gamma^{\mu}x\gamma_{\mu} = -2x$, and the matrix trace on the Dirac module is $4\langle X\rangle_{0}$. $S_{0}$ is homogeneous of degree $-3$. The one-loop kernels have scaling degree $6$ (vacuum polarisation), $5$ (self-energy), $4$ (scalar bubble), so $\omega = 2, 1, 0$; by additivity the vertex, three- and four-photon kernels have $\omega = 0, 1, 0$.
\item[(ii)] \emph{(Vacuum polarisation; proved given the imported theorem.)} With the massive propagator $S = (\frac{1}{2\pi^{2}s^{2}} - \frac{m^{2}}{8\pi^{2}s})x + \frac{m}{4\pi^{2}s} + R$, where the $m^{2}$ coefficient follows from the Klein-Gordon recursion and $R$ is of scaling degree at most $0$ (the Hadamard form, Fact \claimref{synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport}, on the flat field), the kernel $\Pi(a) = -e^{2}\sum_{\mu\nu}a^{\mu}\,4\langle\gamma_{\mu}S(x)\gamma_{\nu}S(-x)\rangle_{0}\,\gamma^{\nu}$ on $x \neq 0$ is
\[
\Pi = \frac{e^{2}}{12\pi^{4}}\,T\Big(\frac{1}{s^{2}}\Big) - \frac{e^{2}m^{2}}{8\pi^{4}}\,T\Big(\frac{1}{s}\Big) + \Pi^{(\le 2)},
\]
each part divergence-free, $\Pi^{(\le 2)}$ of scaling degree at most $2$. Since $s^{-2} = -\frac14\nabla^{2}(L_{\mu}/s)$ off the origin and $L_{\mu}/s$ and $1/s$ are locally integrable, $\bar\Pi = -\frac{e^{2}}{48\pi^{4}}T(\nabla^{2}(L_{\mu}/s)) - \frac{e^{2}m^{2}}{8\pi^{4}}T(1/s) + \overline{\Pi^{(\le 2)}}$ (distributional derivatives) is an extension that is Lorentz covariant and transverse: the Ward identity holds for it. With $\nabla^{2}(1/s) = -4\pi^{2}\delta$, $\mu\,\partial_{\mu}\bar\Pi = \frac{e^{2}}{6\pi^{2}}T(\delta)$, so in $\bar\Pi(q)(a) = (Q(q)a - (a\cdot q)q)\Pi(q^{2})$ the logarithm $\ln(\mu^{2}/Q(q))$ has coefficient of magnitude $e^{2}/(12\pi^{2})$ per Dirac fermion (its sign fixed by the convention relating $\Pi$ to the effective charge): the stored coefficient. Every covariant transverse extension differs from $\bar\Pi$ by $c\,T(\delta)$ (clause (iii)); the $m^{2}$ part has a unique transverse extension (no photon mass and no scale). No regulator field and no internal photon line enter, so neither Pauli-Villars fields nor the Krein form is used.
\item[(iii)] \emph{(How Ward-preserving extensions can differ; computed.)} Among local polynomial maps in the momenta valued in $\Cl(1,3)$ (exact ranks under the six Lorentz bivector generators): the photon two-point differences of degree at most $2$ form a space of dimension $3$ ($a$, $Q(q)a$, $(a\cdot q)q$), the transverse ones dimension $1$ ($Z_{3}$); the self-energy differences of degree at most $1$ dimension $4$ ($1$, $I_{4}$, $q$, $qI_{4}$, as left multiplications), $2$ under the reflection $v \mapsto \gamma_{0}v\gamma_{0}$ ($\delta m$, $Z_{2}$); the vertex differences of degree $0$ dimension $2$ ($a$, $aI_{4}$), $1$ under the reflection; with the Ward-Takahashi identity $q_{\mu}\Lambda^{\mu} = \Sigma(p) - \Sigma(p + q)$ the joint self-energy and vertex space has dimension $2$ under the reflection ($4$ without) and forces $c_{V} = -c_{2}$, that is $Z_{1} = Z_{2}$; the three-current differences of degree at most $1$ form a space of dimension $8$, of which none is transverse on any two legs; the four-photon differences a space of dimension $4$, none transverse on one leg. So if Lorentz-covariant extensions obeying the Ward identities and the reflection exist (imported, Scharf \cite{Scharf1995}, Fact \claimref{synthesis.imported-epstein-glaser-extension-theorem-and-ward-preserving-time-ordered-products}(iii); proved here only for the vacuum polarisation, clause (ii)), any two differ exactly by $Z_{3}$, $\delta m$ and $Z_{2} = Z_{1}$. The self-energy and vertex kernels contain the photon propagator in a covariant gauge, so these parts are read under the Krein-form premise \claimref{synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields}. In particular at most one covariant three-current extension (one axial, two vector legs) conserves both vector currents, so every such extension has the same axial divergence.
\item[(iv)] \emph{(Status of the units.)} The parity-odd differences $I_{4}$ and $qI_{4}$ of (iii) are left multiplications; the field theory's unit stands outside the product (the conventions' right unit), so they are pseudoscalar terms removed by the reflection, not complex rescalings of $\delta m$ and $Z_{2}$, which reality of the coefficients removes.
\item[(v)] \emph{(On a gravitational field; argued.)} By Theorem \claimref{synthesis.hadamard-dirac-states-scale-to-the-flat-massless-vacuum-at-every-point-of-a-gravitational-field} every gauge-invariant quasi-free Hadamard state of the Dirac field has, at every point, scaling degree $3$ with the flat massless kernel as limit; with the scaling-degree bound for products of Hadamard parametrices (Brunetti and Fredenhagen) the one-loop kernels on a gravitational field have the flat degrees of divergence and the flat leading scale coefficients, the further ambiguities being local terms in the field strength of matching dimension (Hollands and Wald \cite{HollandsWald2001}).
\item[(vi)] \emph{(Separately, the scalar field: the quartic bubble; computed.)} For a free scalar field, $\Delta_{0}^{2} = 1/(16\pi^{4}s^{2})$ extends to $-\frac{1}{64\pi^{4}}\nabla^{2}(L_{\mu}/s)$ with $\mu\,\partial_{\mu}$ of it equal to $\delta/(8\pi^{2})$; for $\lambda\phi^{4}/4!$ the three channels with symmetry factor $\frac12$ give $\mu\,d\lambda/d\mu = 3\lambda^{2}/(16\pi^{2})$ at one loop (standard).
\item[(vii)] \emph{(Separately, the floors: no smooth weighting keeps a boost; proved.)} The commutant $\mathfrak{k}$ of the conformal Hamiltonian $H = \gamma_{0}e_{+}$ among the fifteen bivectors of $\Cl(2,4)$ is seven-dimensional and contains no boost (stored, Theorem \claimref{synthesis.floor-regulator-keeps-the-charge-and-the-central-term-below-the-cut-off}(iv)). New here: $\mathfrak{k}$ together with any one boost, translation, special conformal generator or the dilation generates all fifteen (computed for seven sample generators; for an arbitrary element outside $\mathfrak{k}$ argued from the irreducibility of the complement), so on an irreducible module (the attachment's one-particle helicity modules, Proposition \claimref{field-theory.twistor-attachment}) a bounded weighting $f(H)$ of the modes by conformal energy that commutes with one boost commutes with the whole conformal algebra and is constant (Schur): no weighting of the floors, smooth or sharp, keeps a boost. (Merged on 2 November 2026 into the floor-regulator result as its clause (v).)
\end{enumerate}

## technical
The stored one-loop electrodynamics uses Pauli-Villars fields, some of negative weight, so its regulator rests on the same indefinite form as the covariant gauge; the floors of the tower keep the Ward identity but no boost. A standard alternative (Epstein and Glaser; in this computational form, Freedman, Johnson and Latorre) needs no regulator: the one-loop kernels are well defined away from coincident points, and extending them across is the only step that needs a choice, governed by the scaling degree, the calculus of the stored Hadamard scaling results. Carried out in the spacetime algebra on the Euclidean section, the vacuum polarisation away from the origin, including the order-$m^{2}$ term from the Klein-Gordon recursion, is $(e^{2}/(12\pi^{4}))T(s^{-2})$ minus $(e^{2}m^{2}/(8\pi^{4}))T(s^{-1})$ plus a part of low scaling degree, $T$ the transverse operator $a \mapsto (a\cdot\nabla)\nabla - a\nabla^{2}$. Writing $s^{-2}$ as a Laplacian of the locally integrable $\ln(\mu^{2}s)/s$ gives an extension that is transverse and covariant by construction; its dependence on the scale $\mu$ is a multiple of $T(\delta)$, whose coefficient $e^{2}/(6\pi^{2})$ is twice the magnitude $e^{2}/(12\pi^{2})$ of the stored log coefficient. No regulator field and no photon line, so no Krein form, enters. For the other one-loop kernels the result is narrower: exact rank computations in $\Cl(1,3)$ show how covariant extensions obeying the Ward identities and the reflection can differ (exactly by $Z_{3}$, $\delta m$ and $Z_{2} = Z_{1}$, not at all for the three- and four-photon kernels, and at most one vector-conserving three-current extension, so one axial divergence), while their existence is the imported part (Scharf's Ward-preserving time-ordered products); the self-energy and vertex kernels carry the covariant photon propagator and so hold under the Krein-form premise. On a gravitational field the Hadamard scaling theorem gives every Dirac two-point function the flat scaling degree, so the same counting carries over with terms in the field strength added (argued). Two separate statements are recorded with it: the scalar bubble gives the standard quartic coefficient $3/(16\pi^{2})$, and, beyond the stored commutant of the conformal Hamiltonian, that commutant plus one boost generates the whole conformal algebra, so by Schur's lemma no smooth weighting of the floors keeps a boost.

## lay
Calculations with quantum loops produce infinities that are usually tamed by a regulator, an artificial modification at very high energies removed at the end. The series had used borrowed regulators, one of which needs fictitious particles with negative probabilities, and its own natural cut-off, the floors of its tower, singles out one observer and so breaks relativity. A known method, extending the loop quantities across the points where they are singular, is here carried out in the series' algebra. For the screening of electric charge by the vacuum it needs no regulator and no fictitious particles, stays relativistic, keeps charge conservation, and gives the standard strength of screening. For the other one-loop quantities the calculation shows that the only freedom left by relativity and charge conservation is the three constants physicists already adjust (the electron's mass, the normalisation of its field and the strength of the charge); that a version keeping charge conservation exists there is taken from the literature, and for the electron's own corrections the photon's states are assumed to carry the standard indefinite measure of the series' premise. The whole calculation assumes the standard theorem on extending such quantities, also taken from the literature. Separately, no smoothing of the tower's floors can restore relativity.

## one-liner
Standard (Epstein and Glaser 1973; Freedman, Johnson and Latorre 1992), now in the store: under the imported extension theorem the one-loop vacuum polarisation in the spacetime algebra extends with no regulator to a covariant transverse kernel with log coefficient of magnitude $e^{2}/(12\pi^{2})$ per Dirac fermion, using no Pauli-Villars field and no Krein form; Ward-preserving covariant extensions of the other one-loop kernels, if they exist (imported, not proved; self-energy and vertex under the Krein-form premise), differ only by $Z_{3}$, $\delta m$, $Z_{2} = Z_{1}$, and the vector-conserving three-current extension is unique, so its axial divergence is scheme independent; separately, the scalar bubble gives $3/(16\pi^{2})$ and no smooth weighting of the floors keeps a boost; transport-absent except clauses (v) and (vii), transport-convenient.
