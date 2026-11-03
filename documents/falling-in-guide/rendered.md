# Falling In (guide length)

**Abstract.** At the centre of a non-rotating black hole a curvature measure that no change of description alters grows without bound, so the breakdown is real. Both radial light directions swing inward and merge into one at the centre. The obstruction is a direction with no partner, so the repair enlarges the algebra to supply one. Each step up the resulting tower adds exactly one fermionic mode built from vectors. Inside the hole, Einstein's equations for empty space amount exactly to a marker on the metric staying constant. Coming back down is the same as averaging each observable with its parity-flipped version. For a mode whose mixed state gives both outcomes some probability, the partner making the doubled state pure is the mirror copy of its own algebra. Whatever the starting state, each descended mode of nonzero weight reads as thermal at exactly one temperature. The entropy gained in coming down measures how distinguishable the state is from its descended version, and is never negative. Two premises, on allowed states and on smoothness at the horizon, put every mode at the same Hawking temperature. The algebra alone cannot choose that value: its symmetries only flip the sign of an inverse temperature. At that temperature the Fermi-Dirac filling is the only simple Gaussian state thermal for the boost clock. Given the s-wave modelling convention, its collective boson modes have exactly the Bose-Einstein occupancy, up to an exponentially small correction on a finite window.

This guide follows a black hole from its centre, where the usual mathematics breaks down, to the radiation it gives off. It starts at the singularity, because everything later depends on knowing exactly what has gone wrong there and what kind of repair it calls for. Two short sections then describe the enlarged algebra that makes the repair, called the completion: how much room it has for quantum modes, and what Einstein's equations look like inside it. With the completion in place, the guide follows the return journey back down to the observables of a single mode, and asks what that step keeps and what it throws away. The next section puts a price on the return journey, measured as a gain in entropy. The last section shows how the same ingredients produce a temperature, why the algebra alone cannot set its value, and how the resulting state describes the radiation. Results that the argument uses without proving are gathered at the end and cited rather than shown.

## What we assume

**Postulate 1 ((P): univalence).** The premise (P) requires every physical state $\omega$ of the boundary modes to be even under the grading automorphism $\alpha$, that is $\omega \circ \alpha = \omega$. Equivalently, $\omega$ vanishes on the odd sector $\Aod$, so odd elements of the boundary-mode algebra have zero expectation value.

It is a premise, not a derived result: it restricts which states count as physical, and enters as an input wherever it is invoked.

**Postulate 2 ((R): regularity at the fixed locus).** Premise (R) imposes the KMS condition on each single-mode marginal at a fixed period. For mode $k$, with Killing flow $\alpha_t = \operatorname{Ad}(e^{it\omega_k K_k})$ and $a, b \in \{v_k, v_k^{*}\}$, the entire correlation function $F_{a,b}(t) = \omega(a\,\alpha_t(b))$ is required to continue in imaginary Killing time to a single-valued function on the regular Euclidean section of the Schwarzschild field, its two orderings being the two sides of the cut, which meet after one period: $F_{a,b}(t + ip) = \omega(\alpha_t(b)\,a)$ with $p = 2\pi/\kappa$.

The period is the one that smoothness of the Euclidean section at its tip dictates, a local condition. The condition is imposed on the single-mode marginals only.

On the continuum of the horizon's light rays, for the eternal hole, this content follows from the null ground-state premise (N$_{+}$), which has no temperature in it; the ladder wording here is its discretisation. (R) keeps its status as a premise.

## The singularity: where division fails

This section looks at the centre of the black hole, shows that the breakdown there is real, and identifies what kind of breakdown it is.

We begin with a quantity that no change of description can alter.

**Theorem 3 (Non-removability: the invariant argument).** The curvature scalar of the solution is $K := R_{abcd}R^{abcd} = 48M^2/r^6$, assembled from the curvature eigenvalue spectrum (each frame plane contributes four times its eigenvalue squared), and it diverges as $r \to 0$. Under the rotation-gauge law the curvature transforms by conjugation, $\mathcal{R}(B) \mapsto R\,\mathcal{R}(B)\tilde R$, which preserves every scalar contraction, and under position-gauge displacements it transforms by pullback, which relocates the function but cannot remove its unbounded range near the singular locus.

Hence $K$ is invariant under every gauge transformation of the theory, $r$-dependent transformations of arbitrary size included, and no gauge choice removes the degeneration at $r = 0$: the division-by-zero locus is a property of the solution, not of its presentation.

*Rests on:* singularity.solution-where-divergence-lies

With the breakdown shown to be genuine, we watch what happens to the paths of light on the way in.

**Theorem 4 (The cones fold).** In the Painlev\'e-Gullstrand gauge the metric is $g(a,a) = Q(\hb^{-1}(a))$ with $\hb^{-1} = 1 + \beta P$. For $a = \et + \lambda\,\er$ in the $(t,r)$ plane this gives $\hb^{-1}(a) = \et + (\lambda + \beta)\er$ and $g(a,a) = 1 - (\lambda + \beta)^2$, so the two null directions are $\lambda = -\beta \pm 1$, the radial null curves $dr/dt = -\beta \pm 1$. At the horizon, $\beta = 1$, they are the hovering ray $\lambda = 0$ and an ingoing ray $\lambda = -2$.

As $r \to 0$, $\beta \to \infty$ and both branches, normalised by their $\er$-coefficient, converge to $\er$, tipping inward on the way, while $g(\et,\et) = 1 - \beta^2 \to -\infty$, so no rescaling of the classical field stays finite and nondegenerate. The degeneration is through a null kernel direction in the exact sense of the rescaled-limit result, and it is not removable by gauge choice.

*Rests on:* singularity.degeneration-exactly, singularity.non-removability-invariant-argument, std-algebra.orthogonal-anticommute

Knowing which direction collapses, we can now name the kind of obstruction it is.

**Theorem 5 (Type N, and only type N).** The obstruction at $r = 0$ is of type N: the degenerating direction $\er$ is null for the limit form and lies in its radical, so it is an isotropic direction without a metric partner, in the degenerate sense that the root taxonomy hands to the sheaf framework, whose localisation theorem supplies the partner by completion on the exceptional set. Type C cannot occur: $\Cl(1,3)$ has $p - q = -2 \equiv 6 \pmod 8$, so it is central simple, $\Cl(1,3) \cong \Mat_2(\HH)$, with no central idempotents for ideal fusion to fuse.

Type P is present, as in every algebra of this size, but demands no transport: its rule is the identity assignment, so it neither licenses nor obstructs the ascent. The operative transport rule is the Witt completion, and no floor of the resulting tower ever develops a type-C obstruction.

*Rests on:* sheaf.localised-transport, sheaf.one-sided-completion, sheaf.one-sided-completion-singularity, sheaf.schwarzschild-degeneration-boundary-tame, singularity.degeneration-exactly, tower.rigidity-clock-frozen, transport.existence-classification-type-c, transport.existence-locus-type-n, transport.type-p-self-repairing, primer.classification-real-clifford-algebras, std-algebra.sta-matrix

## Quantum capacity of the completion

This short section asks how much room for quantum modes the completion provides as it is built up.

Since the repair works by enlarging the algebra, the natural next question is how much the enlargement can hold.

**Theorem 6 (Witt index is quantum capacity).** Let $(V, Q)$ be a nondegenerate real quadratic space of signature $(p,q)$, and call a family of vectors $(a_i, b_i)_{i \leq m}$ of $\Cl(V,Q)$ a mode family if it satisfies $a_i a_j + a_j a_i = 0$, $b_i b_j + b_j b_i = 0$ and $a_i b_j + b_j a_i = \delta_{ij}$. The largest possible $m$ is exactly the Witt index $\min(p,q)$. For the upper bound, the relations force the $a_i$ to span a totally isotropic subspace, and pairing against the $b_j$ shows the $a_i$ are linearly independent; a totally isotropic subspace of a nondegenerate form of signature $(p,q)$ has dimension at most $\min(p,q)$. The bound is attained by the normalised null pairs of $\min(p,q)$ orthogonal hyperbolic planes split off by a Witt decomposition.

Along the tower, $T_k$ has signature $(p{+}k, q{+}k)$ and hence Witt index $\min(p,q) + k$, so each rung raises the number of vector-realised modes by exactly one and by no more.

*Rests on:* tower.ladder-pairs-satisfy-car-vectors, std-algebra.vector-squares, std-algebra.witt-decomposition

## Einstein's equations in the completion

Here the question is what form Einstein's equations for empty space take once the completion is in place.

From the algebra of the completion we turn to its geometry.

**Theorem 7 (Covariant form of the vacuum equations).** Let $g$ be the derived metric of a gravitational field on flat spacetime, on its invertible region $\Mo$, and $I_g = (1,0,0) = \nInf$ its pure-scale tractor. The tractor connection, which on flat spacetime is the $\Cl(2,4)$ gauge field $\Omega_{T}$ built from $\Omega$, the frame $\hb^{-1}$ and the Schouten map, gives $\nabla_a I_g = (0,\, -\Sch_{ab},\, 0)$, so $I_g$ is parallel exactly when $\Sch = 0$, which holds exactly when $g$ is Ricci-flat, which is equivalent to the GTG vacuum field equations. The section is null, $Q(I_g) = 0$.

So the vacuum field equations on $\Mo$ are equivalent to parallelism of the scale tractor attached to $g$. The existence of some parallel null tractor is strictly weaker: it says only that $[g]$ is almost Ricci-flat, and a non-constant rescaling $e^{2\omega}g$ keeps a parallel section while losing the field equations. The statement is covariant under the gauge transformations of $\mathcal{T}$, whose structure algebra $\mathfrak{so}(2,4)$ acts through the bivectors of $\Cl(2,4)$.

*Rests on:* interior.imported-equivalence-einstein-equations, interior.imported-tractor-connection, interior.metric-parallelism-trace-schouten-condition

## Descent, parity and states

Having gone up into the completion, we need a way back down to what a single mode can show us, and this section studies that return step.

With the geometry settled, we look first at the map that comes back down from the completion.

**Theorem 8 (The descent is the parity average).** On the single-mode algebra $\Aa$ the descent equals the parity average: $E(x) = \tfrac12\bigl(x + \alpha(x)\bigr) = \tfrac12(x + \sigma x \sigma)$. Hence $E$ is the group average over $\{\id, \alpha\}$ and the unique conditional expectation of $\Aa$ onto its fixed-point algebra $\Aev$.

Its range is $\Aev$, its kernel is exactly the adjoined ladder sector $\Aod$, and it preserves every state with $\omega \circ \alpha = \omega$.

*Rests on:* singularity.descent-what-it-erases

Because coming down discards information, it is natural to ask where the partner that keeps the larger state pure comes from.

**Theorem 9 (Purity is an output: the partner is the commutant).** Let $\omega$ be a faithful state on the mode factor with $\varrho = \operatorname{diag}(\lambda_0^2, \lambda_1^2)$, $\lambda_i > 0$. Its GNS representation lives on $\C^2 \otimes \C^2$ with cyclic vector $\Omega = \sum_i \lambda_i |ii\rangle$, cyclic and separating for $\pi(\Aa) = \Aa \otimes 1$; the commutant $\pi(\Aa)' = 1 \otimes \Aa = J\pi(\Aa)J$ is the partner copy, and any two purifications of $\omega$ differ by a unitary on the purifying factor alone.

When $\omega$ is the Gibbs state at inverse temperature $\beta$, $\Omega$ is the thermofield double with $\tan\theta = \lambda_1/\lambda_0 = e^{-\omega_k/2T}$, the same vector the Schmidt-forcing argument produces. So purity of the doubled state, the existence of the partner and the thermofield form are consequences of the one-sided state rather than independent choices.

*Rests on:* singularity.modular-theory-matrix-factor-proved-outright

Turning from the doubled state back to a single mode, we ask what shape its descended state can take.

**Theorem 10 (The descended form is state independent).** For any state on the boundary mode space and any mode $k$, the descended marginal $E_k(\varrho_k)$ is diagonal in the number basis, because the range of $E_k$ is the even subalgebra. A diagonal density matrix $\operatorname{diag}(p_k, 1 - p_k)$ is then the Gibbs state $e^{-\beta_k\omega_k N_k}/Z_k$ for a unique $\beta_k \in [-\infty, +\infty]$, fixed by $\beta_k\omega_k = \log\bigl(p_k/(1-p_k)\bigr)$, provided $\omega_k \neq 0$.

At a zero-weight mode the right side is $\tfrac12\,\id$ for every $\beta_k$, so uniqueness fails there and existence requires $p_k = \tfrac12$. No hypothesis on the ascended state is used.

*Rests on:* singularity.descent-parity-average

## Entropy and information

Coming down is not free, and this section measures exactly what it costs.

Knowing what the descent leaves behind, we now put an exact figure on what it removes.

**Theorem 11 (The deficit theorem: the cost of descent, exactly).** Let $E$ be the pinching by a complete family of orthogonal projectors, the multi-mode descent $\EN$ included. Then $E$ is idempotent, trace-preserving and self-adjoint for the Hilbert-Schmidt pairing, and for every density matrix $\rho$ the entropy increase under $E$ is exactly a relative entropy: $S(E(\rho)) - S(\rho) = \rel{\rho}{E(\rho)} \geq 0$, with equality if and only if $\rho = E(\rho)$.

The level discrepancy of the chain is this quantity, so the cost of descent is an exact relative entropy rather than a qualitative statement.

## Temperature and Hawking radiation

The last section turns the descended states into a temperature, and that temperature into radiation.

With the cost understood, we use the two premises to fix which temperature the descended modes actually have.

**Theorem 12 (The rate, and the discharge of hypothesis (iii)).** Assume (P) and (R). At each mode the marginal is diagonal in the number basis, $\operatorname{diag}(1 - n, n)$ with $n = \omega(v^*v)$, and the gluing condition of (R) on the ladder pair reduces to $e^{p\omega}n = 1 - n$, so $n = (e^{p\omega} + 1)^{-1}$ with period $p = 2\pi/\kappa$. The marginal is therefore the Gibbs state of $K_k$ at $\beta_k = \beta = 2\pi/\kappa = 8\pi M$, that is $T = \kappa/2\pi = 1/8\pi M = \TH$, with occupancy $\omega(v_k^*v_k) = (e^{\beta\omega_k} + 1)^{-1} \in (0,1)$.

Since the occupancy lies strictly between $0$ and $1$, every marginal is faithful, hence cyclic and separating for its mode factor: the cyclic-and-separating hypothesis of the modular descent theorem is a consequence of (R), not an assumption. The temperature is the same at every mode without any condition on the joint state, because each mode sees the same $\kappa$, which is constant over the bifurcation sphere.

*Rests on:* singularity.ascended-marginals-are-diagonal, singularity.computed, singularity.descended-form-state-independent, singularity.modular-structure-completed-pair, singularity.plane-rate, singularity.p-univalence, singularity.r-regularity-fixed-locus

Having found the Hawking value, we ask how much of it the algebra itself determines.

**Theorem 13 (Rate rigidity: the temperature is not algebra intrinsic).** Let $\alpha_t = \operatorname{Ad}(e^{itK})$ be the boost's phase flow on the single-mode algebra $\Aa$, the rotor flow $\exp(\lambda\sigma/2)$ continued to imaginary rapidity, with $\beta$-KMS states $\omega_\beta$; every automorphism of this matrix factor is inner, $\theta = \operatorname{Ad}(U)$. An automorphism commuting with the flow fixes every $\omega_\beta$; one reversing the flow sends $\omega_\beta$ to $\omega_{-\beta}$; and a constant reparametrisation $\alpha_t \mapsto \alpha_{ct}$ with $c > 0$ leaves $\omega_\beta$ unchanged while rescaling its inverse temperature to $\beta/c$.

Hence automorphisms intertwining the flow act on the line of KMS states with orbits $\{\beta, -\beta\}$: $|\beta|$ is an invariant of the pair (state, parametrised flow), and the line carries no automorphism-theoretic structure beyond the orientation flip. A condition singling out one point of the line must either stipulate the state or refer to data outside $(\Aa, \alpha)$, and the value of $|\beta|$ is meaningful only relative to a parametrisation of the flow, which the algebra does not supply.

*Rests on:* singularity.kms-uniqueness-factor

With that caution in mind, we assemble the thermal state across all the boundary modes together.

**Theorem 14 (The I-state).** Take the boundary-mode algebra $\mathfrak{A}$ with its boost dynamics $\tau$ at $\beta = 1/\TH = 2\pi/\kappa$. The quasi-free state $\omega_I$ with Fermi-Dirac symbol $A_I = (1+e^{\beta h})^{-1}$, that is occupancies $n_j = 1/(e^{\omega_j/\TH}+1)$, restricts on every window $F$ to the Gibbs state of $H_F = \sum_{j\in F}\omega_j N_j$ and is KMS there exactly; it is the unique quasi-free extension of these window states, and it is $\tau$-KMS at $\beta$ on the whole algebra.

Within the quasi-free class the converse holds. Applying the KMS identity to two creation operators shows that the pairing vanishes, so a quasi-free $\tau$-KMS state at $\beta$ is automatically gauge-invariant. Applying it to a creation and an annihilation operator, with the CAR, gives $A(1+e^{-\beta h}) = e^{-\beta h}$, hence $A = A_I$: the two-point data are forced, and $\omega_I$ is the unique quasi-free state whose modular clock is the geometry's clock.

*Rests on:* hawking.gibbs-states-are-kms-conversely-finite, hawking.imported-kms-passes-inductive-limits, hawking.imported-quasi-free-states-car-algebra

It remains to see what this fermionic state looks like when its levels are repackaged as bosons.

**Theorem 15 (Bose-Einstein occupancy, with quantified window corrections).** On the bilateral ladder with level spacing $\epsilon$ and the sea at level $0$, carrying the linear s-wave weight assignment as a modelling input, the I-state occupancies are $n_k = (x^{-k}+1)^{-1}$ with Boltzmann factor $x = e^{-\beta\epsilon} \in (0,1)$. They obey the exact detailed-balance identity $n_k - n_{k+m} = (x^{-m}-1)\,n_{k+m}(1-n_k)$ for every $k$ and every $m \ge 1$.

Summing over $k \in \Z$, the left side telescopes to $1$ in each of the $m$ residue classes modulo $m$, so $\sum_{k} n_{k+m}(1-n_k) = m/(e^{\beta\epsilon m}-1)$. This sum is the current two-point function $\langle a_m^\dagger a_m\rangle_I$, so the unit-normalised boson $\hat a_m = a_m/\sqrt{m}$ has exactly the Bose-Einstein occupancy $1/(e^{\beta\epsilon m}-1)$ at $\TH$. On the window $[-K, K]$ with the sea at the centre, the bilateral sum exceeds the window sum by a positive amount at most $2m\,x^{K-m}/(1-x)$.

*Rests on:* hawking.i-state, hawking.imported-s-wave-bosonic-sector

## Results cited, not shown

**Fact (imported) 16 (Gibbs states are KMS, and conversely, in finite dimensions).** Let $\mathfrak{B} = \End(\C^m)$ carry the dynamics $\alpha_t = \mathrm{Ad}(e^{itH})$ for a diagonal $H$ with eigenvalues $\lambda_a$, repeated or not, and fix $\beta \in \R$. The Gibbs state $\omega_G(x) = \tr(e^{-\beta H}x)/\tr(e^{-\beta H})$ satisfies the KMS identity $\omega_G(xy) = \omega_G(y\,\alpha_{i\beta}(x))$ with $\alpha_{i\beta}(x) = e^{-\beta H}x\,e^{\beta H}$, by cyclicity of the trace.

Conversely, writing a KMS state as $\omega(x) = \tr(\rho x)$ and testing the identity on matrix units forces Gibbs ratios $\rho_{aa} = e^{-\beta(\lambda_a-\lambda_b)}\rho_{bb}$ between the diagonal entries and makes every off-diagonal entry vanish, even where eigenvalues coincide. Hence $\rho = e^{-\beta H}/Z$: the Gibbs state is the unique $\alpha$-KMS state at $\beta$.

*Provenance:* Transport Lab claim hawking.gibbs-states-are-kms-conversely-finite, version 2 (T07 Lem 3.1).

**Fact (imported) 17 (Imported: KMS passes to inductive limits).** Suppose a C*-algebra is the closure of an increasing union of subalgebras, each globally invariant under a one-parameter dynamics, and a state is KMS at inverse temperature $\beta$ on each subalgebra for the restricted dynamics. Then the state is KMS at $\beta$ on the whole algebra: the analytic-element requirement is checked on the dense union and passes to the closure. This is a standard result of operator-algebraic statistical mechanics, imported from the literature.

*Provenance:* O. Bratteli and D. W. Robinson, Operator Algebras and Quantum Statistical Mechanics 2, 2nd ed., Springer, Berlin (1997)., Prop.~5.3.25.

**Fact (imported) 18 (Imported: quasi-free states of the CAR algebra).** For every operator $A$ on $\ell^2(J)$ with $0 \le A \le 1$ there is a unique gauge-invariant state $\omega_A$ on the CAR algebra $\mathfrak{A}$ with two-point function $\omega_A(a^\dagger(f)\,a(g)) = \ip{g}{Af}$ and all higher truncated functions zero, so that the higher correlators are Wick determinants. More generally, a quasi-free state is determined by its symbol together with its pairing $P(f,g) = \omega(a^\dagger(f)\,a^\dagger(g))$, and gauge invariance is exactly $P = 0$.

On a finite window with diagonal symbol the state is the explicit product $\bigotimes_j \rho_j$ with $\rho_j = \mathrm{diag}(1-n_j,\, n_j)$ in the occupation basis. This is standard material, imported from the literature.

*Provenance:* H. Araki, On quasifree states of CAR and Bogoliubov automorphisms, Publ. RIMS Kyoto Univ. 6 (1971), 385--442.; O. Bratteli and D. W. Robinson, Operator Algebras and Quantum Statistical Mechanics 2, 2nd ed., Springer, Berlin (1997)., \S 5.2.

**Fact (imported) 19 (Imported: the s-wave bosonic sector).** Unconditionally, on a window of the boundary mode space the number-conserving bilinears (currents) satisfy the free-boson commutation relations exactly in the completed limit, the finite-window deviation being an exact difference of edge operators, and the bilinear subalgebra is globally invariant under the modular boost.

Conditionally on Premise (Q), joint quasi-freeness with linear s-wave weights, the restriction of the Fermi-Dirac KMS state to the bilinear subalgebra is KMS at the same temperature, which gives Bose-Einstein occupancy at $\TH$ for the s-wave sector. The boson-fermion correspondence behind this is classical.

*Provenance:* Transport Lab claim hawking.imported-s-wave-bosonic-sector, version 6 (T07 Fact 2.4).

**Fact (imported) 20 (Imported: equivalence with the Einstein equations).** On any region where the gauge field $\hb$ is invertible, the field equations of gauge theory gravity (GTG) for $(\hb, \Omega)$ are equivalent to the Einstein field equations for the metric $g(a,b) = \hb^{-1}(a)\cdot\hb^{-1}(b)$. In vacuum they are equivalent to Ricci-flatness of $g$. This is imported from the gauge-theory-gravity literature.

*Provenance:* A. Lasenby, C. Doran and S. Gull, Gravity, gauge theories and geometric algebra, Phil. Trans. R. Soc. Lond. A 356 (1998), 487--582., \S 4 (\S 4.3, covariant forms of the field equations), App.~C; C. Doran and A. Lasenby, Geometric Algebra for Physicists, Cambridge University Press (2003)., Ch.~13-14.

**Fact (imported) 21 (Imported: the tractor connection).** For a gravitational field on flat spacetime with derived metric $g$, the tractor bundle $\mathcal{T}$ of the conformal class $[g]$ is, on the invertible region, the vectors $\sigma\nInf + \mu + \rho\nO$ of $\Cl(2,4)$. It carries a canonical connection that depends only on $[g]$ and preserves the tractor metric. In the scale $g$ it reads $\nabla_a(\sigma,\mu_b,\rho) = \bigl(\nabla_a\sigma - \mu_a,\ \nabla_a\mu_b + g_{ab}\rho - \Sch_{ab}\sigma,\ \nabla_a\rho + \Sch_a{}^{b}\mu_b\bigr)$, with $\nabla$ on $\mu$ the gravitational covariant derivative, where in four dimensions the Schouten tensor is $\Sch_{ab} = \tfrac12\bigl(\Ric_{ab} - \tfrac{R}{6}g_{ab}\bigr)$, read from the field strength.

The connection is imported from the tractor-calculus literature. The relative sign of the Schouten slots against those references depends on curvature conventions, and it is fixed internally rather than by translating between conventions.

*Provenance:* T. N. Bailey, M. G. Eastwood and A. R. Gover, Thomas's structure bundle for conformal, projective and related structures, Rocky Mountain J. Math. 24 (1994), 1191--1217.; S. N. Curry and A. R. Gover, An introduction to conformal geometry and tractor calculus, with a view towards analysis on manifolds, in Asymptotic Analysis in General Relativity, London Mathematical Society Lecture Note Series 443, Cambridge University Press (2018), 86--170., \S 5.

**Fact (imported) 22 (Metric parallelism, and the trace of the Schouten condition).** (i) The tractor connection preserves the tractor metric. On flat spacetime the connection is a $\Cl(2,4)$ bivector-valued gauge field acting by the commutator product, an infinitesimal rotation, so it preserves $Q$; in index form, differentiating $Q(T)$ along any direction and substituting the connection, the genuine derivative terms reassemble the derivative of $Q(T)$, and the remaining terms cancel in pairs; the two Schouten terms are one contraction written with the index raised on either side, so no symmetry of $\Sch$ is needed.

(ii) For a gravitational field with derived metric $g$, if $\Sch_{ab} = c\,g_{ab}$ for a function $c$, tracing gives $c = R/24$, and substituting back gives $\Ric_{ab} = \tfrac{R}{4}g_{ab}$. In particular $\Sch_{ab} = 0$ if and only if $\Ric_{ab} = 0$.

*Provenance:* Transport Lab claim interior.metric-parallelism-trace-schouten-condition, version 6 (T06 Lem 4.2).

**Fact (imported) 23 (Classification of the real Clifford algebras).** The real Clifford algebra $\Cl(p,q)$ is, as a real associative algebra, a full matrix algebra over $\R$, $\C$ or $\HH$, or a direct sum of two copies of one, and which case occurs depends only on $d \equiv p - q \pmod 8$: $\Mat_k(\R)$ for $d = 0, 2$; $\Mat_k(\R) \oplus \Mat_k(\R)$ for $d = 1$; $\Mat_k(\C)$ for $d = 3, 7$; $\Mat_k(\HH)$ for $d = 4, 6$; and $\Mat_k(\HH) \oplus \Mat_k(\HH)$ for $d = 5$. The size $k$ is fixed by $\dim_\R \Cl(p,q) = 2^n$.

In particular $\Cl(p,q)$ is simple except when $p - q \equiv 1 \pmod 4$, where it is the direct sum of two isomorphic simple algebras.

*Provenance:* Transport Lab claim primer.classification-real-clifford-algebras, version 3 (T00 Thm 9.3).

**Fact (imported) 24 (Localised transport).** The subalgebra of the ambient sheaf $\shC = \Cl(T, h)$ generated by $T^*M$ is canonically isomorphic to $\shA$ globally, the wall included, because $h$ restricts to $G$ on $T^*M$ identically. Over $\Mo \cap \Mp$ the inclusion $\shA \subset \shC$ is fibrewise the conformal embedding $\Cl(p,q) \subset \Cl(p{+}1, q{+}1)$. Over $\Sig$ a radical covector $k$ has $Q(k) = 0$ in both algebras, yet the two-sided ideal it generates is square-zero in $A(x)$ and is the whole of $C(x)$, where $k^* = \nO/(2\nu)$ satisfies $Q(k^*) = 0$ and $k k^* + k^* k = 1$.

So the completion does not modify the degenerate algebra; it re-embeds it where its infinitesimals cease to be infinitesimal. The ladder pair $(k, k^*)$ exists exactly over $\Sig$, so the canonical anticommutation structure of the series' operator-algebraic reading is supported on the singular locus.

*Provenance:* Transport Lab claim sheaf.localised-transport, version 5 (T04 Cor 4.5).

**Fact (imported) 25 (One-sided completion).** Assume tameness (T1)-(T3), signature $(p,q)$ with $p \geq 1$ on the physical side $\Mp$, and a trivial radical line bundle, $w_1(\shL) = 0$, so that collar data exist. Then there is a smooth symmetric form $h$ on $T = T^*M \oplus \underline{\R}^2$, equal to $G \perp H$ outside a collar of $\Sig$, that is nondegenerate of constant signature $(p{+}1, q{+}1)$ at every point of $\Mp$, the wall included.

The proof takes coupling constants with $\mu\nu > 0$: on $\Sig$ the wall Gram gives the signature directly; in the collar on the physical side, after shrinking the collar, $s > 0$ and so $1 + 2\mu\nu\beta^2 s \geq 1$ in the determinant identity; outside the collar $h = G \perp H$. Consequently $\shC = \Cl(T, h)$ restricted to $\Mp$ is locally free of rank $2^{n+2}$ with every fibre isomorphic to $\Cl(p{+}1, q{+}1)$, which is $\Mat_4(\HH)$ in the physical case.

*Provenance:* Transport Lab claim sheaf.one-sided-completion, version 4 (T04 Thm 4.4).

**Fact (imported) 26 (One-sided completion at the singularity).** Adjoin the hyperbolic plane $(\nO, \nInf)$ to the weighted module $\shW$ and couple it to the dying direction by the collar construction, with normalised transversal $u = \partial_t/m$ (so that $k(u) = 1$), coupling constants with $\mu\nu < 0$, and bump supported inside the horizon. Here the dying eigenvalue is negative on the physical side and $s < 0$ inside the horizon, so the determinant factor satisfies $1 + 2\mu\nu\beta_b^2 s \geq 1$ wherever the bump is supported; hence the ambient form $h$ is nondegenerate of constant signature $(2,4)$ at every point of $\Mt$, the boundary $E$ included, and no shadow wall forms anywhere.

The subalgebra generated by $\shW$ is canonically the degeneration sheaf, and the ladder pair $k^* = \nO/(2\nu)$, with $k k^* + k^* k = 1$ and $Q(k) = Q(k^*) = 0$, exists exactly over $E$. This performs the ascent $\Cl(1,3) \to \Cl(2,4)$, that is $\Mat_2(\HH) \to \Mat_4(\HH)$, at the Schwarzschild singularity, localised on $E \cong \R \times S^2$.

*Provenance:* Transport Lab claim sheaf.one-sided-completion-singularity, version 4 (T04 Thm 8.12).

**Fact (imported) 27 (The Schwarzschild degeneration is boundary-tame in $\shW$).** In the frame $(\rho, \dtPG, \mu_1, \mu_2)$ of the weighted module $\shW$, the derived cometric of the Painlev\'e-Gullstrand gauge field $\hb = 1 - \beta P$ on flat spacetime has Gram matrix with $(\rho, \dtPG)$ block $\begin{pmatrix} m^2 - r & -m \\ -m & 1 \end{pmatrix}$ and angular block $\mathrm{diag}(-1, -1)$, with entries polynomial in $r$ and so extending smoothly to the boundary $E$. Then $\det G = -r$, giving signature $(1,3)$ at every $r > 0$, horizon included; at $E$ the rank is exactly three, with radical spanned by $k = \rho + m\,\dtPG$ and nondegenerate complement $\langle \rho, \mu_1, \mu_2 \rangle$ carrying $\mathrm{diag}(m^2, -1, -1)$, of signature $(1,2)$; and $Q(k) = G(k,k) = -r$ exactly, so the degeneration is first order with transversality datum $\delta(k \otimes k) = -\,dr|_E$.

The same module and radical arise from the Schwarzschild coordinate frame through the smooth invertible change of frame $\dtS = \dtPG + \tfrac{m}{m^2 - r}\rho$, and on $E$ the radical is spanned by $\dtS$. Finally $k = d\Phi$ with $\Phi = m t + \tfrac23 r^{3/2}$, and $k$ annihilates the infalling free-fall congruence along $\partial_t - \beta\,\partial_r$ at every radius.

*Provenance:* Transport Lab claim sheaf.schwarzschild-degeneration-boundary-tame, version 6 (T04 Thm 8.7).

**Fact (imported) 28 (Ascended marginals are diagonal).** For a state $\omega$ satisfying univalence, $\omega \circ \alpha = \omega$, the odd ladder elements of each mode have vanishing expectation: $\omega(v_k) = \omega(\alpha(v_k)) = -\omega(v_k)$, so $\omega(v_k) = \omega(v_k^{*}) = 0$. These are exactly the off-diagonal entries of the single-mode marginal $\varrho_k$ in the number basis, so $\varrho_k$ is diagonal and equals $E_k(\varrho_k)$. By the state independence of the descended form it is then the Gibbs state of $K_k$ at a unique $\beta_k$ when $\omega_k \neq 0$; at a zero-weight mode diagonality still holds, but the Gibbs form requires $p_k = \tfrac12$.

Consequently partial trace and pinching coincide on every single-mode marginal of such a state, without the extra hypothesis that was needed before. The parity protection lemma of the finite-mode model is the special case of the model's states, which are even because every configuration in their support has even total occupation.

*Provenance:* Transport Lab claim singularity.ascended-marginals-are-diagonal, version 5 (T05 Thm 7.10).

**Fact (imported) 29 ($\kappa = 1/4M$, computed).** For the static black-hole field on flat spacetime, a static observer has velocity $v = K/\sqrt f$, with $K = \hb^{-1}(e_t)$ the static Killing field and $Q(K) = f$. Its acceleration $(v \cdot D)v$ has the single radial coordinate component $A^r = f'/2$, its proper magnitude is $f'/(2\sqrt f)$, and multiplying by the redshift factor $\sqrt f$ gives the redshifted acceleration $f'(r)/2$ at every $r > 2M$.

Surface gravity is the horizon limit of this redshifted acceleration, so $\kappa = \lim_{r \to 2M} f'(r)/2 = \tfrac12 \cdot 2M/(2M)^2 = 1/4M$.

*Provenance:* Transport Lab claim singularity.computed, version 4 (T05 Prop A.2).

**Fact (imported) 30 (The degeneration, exactly).** As $r \to 0$ the gauge map and metric have exact rescaled limits, with every identity holding at finite $\beta$. The map satisfies $\beta^{-1}\hb = \beta^{-1}\id - P \to -P$, a rank-one map with image $\R\,\er$ and kernel $\et^{\perp} = \operatorname{span}(\er, e_\vartheta, e_\varphi)$. The metric satisfies $\beta^{-2} g \to \hat g$ with $\hat g(a,b) = -(a\cdot\et)(b\cdot\et)$, a form of rank one and signature $(0,1,3)$ whose radical is $\et^{\perp}$, the kernel of the limit map.

The folded direction $\er$ lies in this radical and is $\hat g$-null, whereas $g(\er,\er) = -1$ at every finite radius. The nullity of the degenerate direction is therefore a property of the limit form, not of the flat background, which is the exact content of degeneration through a null kernel direction.

*Provenance:* Transport Lab claim singularity.degeneration-exactly, version 2 (T05 Prop 2.6).

**Fact (imported) 31 (The descent, and what it erases).** With $P := v^* v$, the anticommutation relation and $v^2 = (v^*)^2 = 0$ give $P^2 = P$ and $1 - P = v v^*$. In the defining $2 \times 2$ representation, $v = E_{12}$ and $v^* = E_{21}$, so $P = \operatorname{diag}(0,1)$.

The descent $E(x) := PxP + (1-P)\,x\,(1-P)$ sends the matrix with entries $a, b, c, d$ to $\operatorname{diag}(a, d)$: it retains the occupation data and erases the coherences $b, c$.

*Provenance:* Transport Lab claim singularity.descent-what-it-erases, version 5 (T05 Prop 5.5).

**Fact (imported) 32 (KMS uniqueness at a factor).** On a matrix factor $\Aa$ with the inner flow $\alpha_t = \operatorname{Ad}(e^{itK})$ and any $\beta \neq 0$, a state $\omega = \tr(\varrho\,\cdot\,)$ satisfies the $(\alpha,\beta)$-KMS condition exactly when $\varrho = e^{-\beta K}/\tr e^{-\beta K}$. Writing the KMS identity $\omega(ab) = \omega(b\,e^{-\beta K}a\,e^{\beta K})$ as traces and using cyclicity shows that $\varrho\,e^{\beta K}$ commutes with every element, so it is central and therefore scalar because the algebra is a factor; normalisation fixes the constant, and the converse is the same computation read backwards.

So for each nonzero $\beta$ there is exactly one KMS state, and, for $K$ not a multiple of $1$, the KMS states of the flow form a single line parametrised by $\beta$.

*Provenance:* Transport Lab claim singularity.kms-uniqueness-factor, version 4 (T05 Thm 7.13).

**Fact (imported) 33 (Modular structure of the completed pair).** For a pair $(v, v^*)$ obeying the canonical anticommutation relations, set $\sigma := v^*v - vv^*$. Then $\sigma^2 = 1$, and in the hyperbolic atom $v = \tfrac12(e_0 + e_1)$, $v^* = \tfrac12(e_0 - e_1)$ inside $\Cl(1,1)$ one has $\sigma = e_0e_1$, the unit boost bivector of the plane. The rotor flow $R_\lambda = \exp(\lambda\sigma/2)$ acts by $v \mapsto e^{-\lambda}v$ and $v^* \mapsto e^{\lambda}v^*$, so the pair diagonalises the boost with opposite weights, the structure of outgoing and ingoing horizon modes.

The spectral projectors $\tfrac12(1 \pm \sigma)$ of the boost are exactly the occupation projectors $v^*v$ and $vv^*$, which are the descent projectors, and in the fermionic representation $\sigma = 2N - 1$, so $K := \sigma/2 = N - \tfrac12$. Since $\mathrm{Spin}^+(1,1)$ is one-dimensional, the boost flow is the only one-parameter flow implemented by real rotors of the atom; this uniqueness holds within real rotor flows of $\Cl(1,1)$, not among all one-parameter unitary groups of $\Mat_2(\C)$.

*Provenance:* Transport Lab claim singularity.modular-structure-completed-pair, version 4 (T05 Thm 6.3).

**Fact (imported) 34 (Modular theory of a matrix factor, proved outright).** Take $H = \C^n \otimes \C^n$, $M = \Mat_n(\C) \otimes 1$ and a cyclic separating vector in Schmidt form $\Omega = \sum_i \lambda_i |ii\rangle$ with all $\lambda_i > 0$ and $\sum_i \lambda_i^2 = 1$. The Tomita operator $S : a\Omega \mapsto a^*\Omega$ acts on basis vectors as $|ij\rangle \mapsto (\lambda_i/\lambda_j)|ji\rangle$, and its polar decomposition $S = J\Delta^{1/2}$ is explicit: $\Delta = \rho \otimes \bar\rho^{\,-1}$ with $\rho = \sum_i \lambda_i^2 |i\rangle\langle i|$, and $J$ the antilinear swap $|ij\rangle \mapsto |ji\rangle$.

Consequently the modular flow on $M$ is $\sigma_t(a) = \rho^{it} a \rho^{-it}$, and the vector state $\omega = \langle\Omega, \cdot\,\Omega\rangle$ satisfies the KMS identity $\omega(ab) = \omega(b\,\rho a \rho^{-1})$ for all $a, b \in M$. Because everything is finite-dimensional, all of this follows by direct computation.

*Provenance:* Transport Lab claim singularity.modular-theory-matrix-factor-proved-outright, version 4 (T05 Lem 7.1).

**Fact (imported) 35 (The plane and the rate).** The doubled curvature eigenvalue singles out the pair of planes $\{\sigma_r, I\sigma_r\}$ invariantly at every radius, and its two members are separated invariantly by their squares, $\sigma_r^2 = +1$ and $(I\sigma_r)^2 = -1$ (up to the orientation sign). So the plane of the completed pair is not chosen. At the horizon the boost member $\sigma_r$ is the boost plane of the Killing flow, whose surface gravity, computed as the redshifted proper acceleration of static observers, is $\kappa = \tfrac12 f'(r_h) = 1/4M$.

This fixes the geometric normalisation: an interval of $2\pi$ in rapidity corresponds to $2\pi/\kappa = 8\pi M$ of Schwarzschild time, and this single conversion factor is where the numerical value of the temperature enters the chain.

*Provenance:* Transport Lab claim singularity.plane-rate, version 4 (T05 Prop 6.2).

**Fact (imported) 36 (The solution, and where the divergence lies).** The pair $(\hb, \Omega)$ solves the vacuum field equations at every $r > 0$. On the radial plane both connection values are multiples of $\sigma_r$, so the commutator term of the field strength vanishes and $\mathcal{R}(\partial_t \wedge \partial_r) = -\partial_r(M/r^2)\,\sigma_r = (2M/r^3)\,\sigma_r$: an eigenplane with eigenvalue of magnitude $2M/r^3$, obtained within the gauge formalism. The full curvature operator is diagonal on the six frame planes with eigenvalue magnitudes $(2M/r^3, M/r^3, M/r^3, M/r^3, M/r^3, 2M/r^3)$ and vanishing Ricci contraction, the remaining planes being computed in the static chart and carried over by the imported equivalence with the Einstein equations on the invertible region.

Meanwhile $\det \hb = 1$ at every radius, horizon included, because $1 - \beta P$ is unipotent for the rank-one nilpotent $P$, and the $(t,r)$ block of the metric has determinant $-1$. So at finite radius the classical field is a volume-preserving shear, and the divergence of the description is carried by the connection, the curvature and the metric components, not by $\hb$.

*Provenance:* Transport Lab claim singularity.solution-where-divergence-lies, version 3 (T05 Prop 2.4).

**Fact (imported) 37 (Orthogonal vectors anticommute).** Two vectors anticommute exactly when they are orthogonal. In an orthogonal basis this gives the multiplication table of basis blades: the product $e_I e_J$ is the blade on the symmetric difference $I \triangle J$, times the squares of the shared generators, times a sign that counts how many transpositions are needed to sort the indices.

*Provenance:* Transport Lab claim std-algebra.orthogonal-anticommute, version 1.

**Fact (imported) 38 (The spacetime algebra as a matrix algebra, and the spacetime split).** In the store's signature the spacetime algebra is the algebra of $2 \times 2$ quaternion matrices, as the classification predicts for $p - q \equiv 6$. The familiar Dirac matrices are complex, so they represent the complexified algebra, $4 \times 4$ complex matrices; the real spacetime algebra sits inside as a real form. The spacetime split identifies the even part of the spacetime algebra with the algebra of the observer's three-dimensional space, and the two pseudoscalars coincide.

*Provenance:* Transport Lab claim std-algebra.sta-matrix, version 1.

**Fact (imported) 39 (The product of two vectors).** A vector squares to its quadratic form, and the symmetrised product of two vectors is twice their polar form: $uv + vu = 2B(u, v)$. So the product of two vectors splits into the scalar $B(u, v)$ and the antisymmetric part $\tfrac12(uv - vu)$.

*Provenance:* Transport Lab claim std-algebra.vector-squares, version 1.

**Fact (imported) 40 (Hyperbolic pairs and the Witt decomposition).** In a nondegenerate plane, a null vector $u$ has exactly one partner $w$ with $uw + wu = 1$, so the plane is hyperbolic. Globally, a real quadratic space splits orthogonally into $\min(p, q)$ hyperbolic planes, a definite remainder and the radical. Taking one null vector from each hyperbolic plane, together with the radical, gives a totally null subspace of the largest possible dimension, $\min(p, q) + r$.

*Provenance:* Transport Lab claim std-algebra.witt-decomposition, version 1.

**Fact (imported) 41 (The ladder pairs satisfy the CAR, as vectors).** In the $k$-th algebra of the tower, $T_k = \Cl(p{+}k, q{+}k)$, each adjoined hyperbolic plane carries a normalised null pair $(v_i, w_i)$. These vectors satisfy $v_i v_j + v_j v_i = 0$, $w_i w_j + w_j w_i = 0$ and $v_i w_j + w_j v_i = \delta_{ij}$ for all $1 \leq i, j \leq k$, which are the canonical anticommutation relations of $k$ fermionic modes. The relations hold exactly, among vectors of the algebra, with no normal ordering, no completion and no choice of representation.

Each relation is an instance of the Clifford relation $ab + ba = 2\langle a, b\rangle$ for vectors: the null vectors have $Q(v_i) = Q(w_i) = 0$, distinct planes are orthogonal, and the hyperbolic normalisation gives $\langle v_i, w_i\rangle = \tfrac12$. The vectors of a new rung are orthogonal to all earlier generators, so adding a rung adds one mode and leaves the existing relations untouched.

*Provenance:* Transport Lab claim tower.ladder-pairs-satisfy-car-vectors, version 4 (T03 Prop 4.1).

**Fact (imported) 42 (Rigidity; the clock is frozen).** Along the tower the transport charge $d = p - q \bmod 8$ is constant, since $(p{+}k) - (q{+}k) = p - q$. Each floor is a matrix algebra over the ground floor, so its division-ring type, simplicity class and centre equal those of the ground floor, and it is Morita equivalent to the ground floor. The obstruction taxonomy is therefore floor-independent; in particular a type-C obstruction, a central idempotent, never arises by transport from a simple ground algebra, at any height.

For the physical tower, $\Cl(1{+}k, 3{+}k) \cong \Mat_{2^{k+1}}(\HH)$ sits at clock position $6$ for every $k$: Bott periodicity shows up as immediate freeze, not eventual return.

*Provenance:* Transport Lab claim tower.rigidity-clock-frozen, version 5 (T03 Thm 3.6).

**Fact (imported) 43 (Existence and classification of type C).** A type C obstruction is a nontrivial central idempotent, so it must lie in the centre, which is $\R$ for even $n$ and $\R[\omega]$ for odd $n$. When $\omega^2 = -1$ that centre is a copy of $\C$, whose only idempotents are $0$ and $1$; when $\omega^2 = +1$ it is $\R \oplus \R$, with exactly two nontrivial idempotents $\varepsilon_\pm = \tfrac12(1 \pm \omega)$. Combining the parity of $n$ with the sign of $\omega^2$ shows that $\Cl(p,q)$, $n \geq 1$, has a nontrivial central idempotent if and only if $p - q \equiv 1 \pmod 4$.

In that case $\varepsilon_+ \varepsilon_- = 0$ and $\varepsilon_+ + \varepsilon_- = 1$, and $\Cl(p,q) = \varepsilon_+ A \oplus \varepsilon_- A$ is the splitting into two simple ideals. The grade involution sends $\omega \mapsto -\omega$ and so exchanges $\varepsilon_+$ and $\varepsilon_-$; it is an outer automorphism, because an inner automorphism fixes every central element and therefore cannot exchange them.

*Provenance:* Transport Lab claim transport.existence-classification-type-c, version 4 (T01 Thm 3.6).

**Fact (imported) 44 (Existence locus of type N).** A null vector is a nonzero $v$ with $Q(v) = 0$. In $\Cl(p,q)$ such vectors exist exactly when the signature is mixed, $pq \neq 0$: a definite form is anisotropic, while for $p, q \geq 1$ the sum of a positive and a negative unit basis vector is null. When they exist, the null vectors form a cone of dimension $n - 1$, the zero set of the quadratic form with the origin removed.

Every null vector satisfies $v^2 = 0$ and so is a two-sided zero divisor, and it has neither a left nor a right inverse in any unital algebra containing $\Cl(p,q)$: from $vw = 1$ one would get $v = v^2 w = 0$.

*Provenance:* Transport Lab claim transport.existence-locus-type-n, version 5 (T01 Prop 3.3).

**Fact (imported) 45 (Type P is self-repairing).** Let $A$ be any unital ring, $\mathcal{E}(A)$ its idempotents and $A' \supseteq A$ any unital extension. Taking each idempotent as its own partner, $\sigma(e) = e$, both von Neumann identities $e\,\sigma(e)\,e = e$ and $\sigma(e)\,e\,\sigma(e) = \sigma(e)$ hold because $e^3 = e$. The assignment commutes with every automorphism $\theta$ of $A'$ preserving $A$, since $\theta(e)$ is again an idempotent of $A$ and $\sigma$ is the identity.

In the obstruction taxonomy this says that the transport rule for type P, the non-central idempotents, is the identity at signature increment $(0,0)$: the repair is already present in the base algebra.

*Provenance:* Transport Lab claim transport.type-p-self-repairing, version 2 (T01 Prop 6.1).

**Prediction 46 (The no-echo prediction, registered).** Under Postulate (C1), the framework places its quantum structure at the stretched singularity $r_c = (2M)^{1/3}$, at Planck curvature deep inside the hole, while the horizon remains the smooth vacuum horizon of general relativity because the exterior dictionary is exact. The registered prediction is that post-merger ringdown is the unmodified Kerr quasinormal spectrum.

In particular there is no echo train at the Planck-structure delay $\tau_{\mathrm{echo}} \approx 8M\ln(M/m_P)$, about 35 ms at $10\,\Msun$ and 0.1 to 0.25 s for remnants of 30 to $70\,\Msun$, within the band of existing detectors. One statistically confirmed echo train would refute the framework's localisation of quantum structure.

The breakdown at the centre of a non-rotating black hole is a feature of the solution itself, not of how it is written down. It is the kind of obstruction caused by a direction with no partner, so the repair is to enlarge the algebra and supply one. Coming back down from the enlargement costs exactly an entropy gain, which is never negative and is zero only when there was nothing to discard. Under the two premises every mode comes out at the same Hawking temperature, with no assumption about correlations between modes. The Fermi-Dirac state at that temperature is the only simple Gaussian state that is thermal for the boost clock of the geometry. Given the s-wave modelling convention, its collective boson modes on the infinite ladder have exactly the Bose-Einstein thermal occupancy. What we assume comes down to a short list. The first premise, univalence, says that physical states of the boundary modes give zero average to every quantity that changes fermion number by an odd amount. The second, regularity, asks each boundary mode on its own to look thermal for the black hole's time flow, at the temperature for which the imaginary-time version of the spacetime is smooth. The s-wave convention behind the boson reading is a modelling input rather than a derived result. The value of the temperature also has meaning only once the clock's parameter is converted into physical time, and the algebra does not supply that conversion. One consequence faces observation directly: merging black holes should ring exactly as general relativity says, with no echoes, and a single confirmed echo would refute the framework.
