# Consistency pass K1: rulings R1 and R2 across the store (2026-11-07)

Scope: Leon's rulings R1 (boundary-mode, atom and window flows keep i) and R2 (the horizon's continuum
mode space and the Hadamard chain carry I_4) on every entity outside the split-owned list. I also
re-checked group B's R1/R2 entities against the entities outside group B. The other agent did R3 and R4.
Before each edit I appended the id to claimed.txt. No conflicts arose. No commits, no check.py edits,
no status, link, pin or ledger changes.

Validation: `tp check --layers 1,2,3 --keep-going --author leon`, filtered to ids_K1.txt (22 ids). It gives
0 errors and 0 warnings. The only finding is the I213 on singularity.l-stabiliser-tangent, which is
already in baseline.log. The store-wide total is also 0 errors and 0 warnings. A detector re-scan shows
every remaining bare i in my entities is declared, or is an index (the epsilon^{i}, i >= 1 exponents in
restricted-dirac Step 5).

## Per entity

### R1: reverted to 8eef5a4 (formal and proofs identical to 8eef5a4, version restored, the sweep's credit entry dropped)
Each got `outside_ga: {kind: complex-analysis}`. The sweep's maintainer note was replaced by a
declaration-only note naming R1. This is the same pattern group B used for c-loc, local-boost and r-loc.
- synthesis.point-spectrum-boost-admits-no-half-sided-translations: 4 -> 3. R1. Restored e^{-i omega_j t}, Ad(e^{itK}), [K, P] = icP, Delta^{is}, e^{-2 pi ik}.
- synthesis.s-wave-array-is-a-boundary-mode-set: 4 -> 3. R1. Restored the boost phases on b_k and psi_k and the one-mode tau_t.
- synthesis.q-splits-maximum-entropy-affine-weights: 5 -> 4. R1. Restored e^{itK_geo}, the boost phases, and the window's C (the span{1, I_4} gloss removed).
- synthesis.quadratic-flows-cannot-thermalise-descent: 2 -> 1. R1. Restored Ad(e^{itX_k}), the coherence and pairing phases, e^{-itk}, the Cayley form and Q(i).
- synthesis.half-integer-weight-array-carries-half-ln2: 5 -> 4. R1. Restored the window flow e^{-i omega_k t} and e^{2 pi iK}. The declaration now also covers the theta-function i, which was already kept.
- synthesis.null-ordering-of-counted-units-is-zeta-symmetric: 3 -> 2. R1. Restored the window twist phase e^{2 pi i delta}. This reversion was not on the known list.

### R1: passage restored inside an entity that keeps its other conversions
- synthesis.boost-evolution-on-generators-is-one-unitary-group: 3 (unchanged). R1. Group A1 had replaced the quoted window formula a_j -> e^{-i omega_j t}a_j with words; that formula is restored exactly. The generator's continuum conversions to I_4 stay (R2). Now declared complex-analysis for that one quoted window flow, and the note is updated.

### R1: declaration kind made uniform (other -> complex-analysis; no text or version change; note amended)
- synthesis.number-diagonal-dynamics-spreads-nothing, synthesis.residue-common-weight-particle-hole, scrambling.clock-inventory-boundary-modes, singularity.l-stabiliser-tangent, synthesis.collar-isotropy-selects-t-boost: version unchanged. These are atom, completed-pair and frame-atom flows, which R1 declares complex-analysis.

### R2: converted to I_4
- obj.hawking.continuum-mode-space: 2 (kept). R2. The complex unit of h is I_4, and tau_t(a(f)) = a(e^{I_4 th}f) at the formal and technical levels. The countable-case sentence now says the boundary-mode algebra keeps its own complex unit, not identified with I_4. The declaration is removed. Group E had already bumped this entity to 2 for a declaration only, so I did not bump it again: the pass makes one version step from 8eef5a4. I updated E's credit and note.
- synthesis.modular-data-on-a-generator-fix-neither-the-translation-lift-nor-the-sign-of-i: 3 -> 4. R2. All 43 units are now I_4: P = I_4 d/du, W_0, the phases c = I_4 eta = -I_4, e^{I_4 u kappa}, e^{I_4 vartheta}, x^{I_4 lambda_0}, Delta^{I_4 s}, the cross-cut kernels, the Majorana decomposition and the finite Slater checks. "If the field's i is read as J" now reads "read through J = I_4 B, the transverse bivector that the field's unit I_4 forms with the boost bivector B" in (iv), the technical level and Step 4. "The orientation of the imaginary unit" now reads "the orientation of the unit I_4". The claim is unchanged and the declaration is removed. The title still says "the sign of i" (see below).
- synthesis.geometric-modular-conjugations-on-a-generator-give-the-null-ground-state: 3 -> 4. R2. Converted P, W_0, the Klein twist Z = (1 + I_4 Theta)/(1 + I_4), the twisted reflection positivity, Delta_a^{I_4 t}, the continuation to rapidity I_4 pi, the Fourier and Laplace kernels, the Pick-function continuation (Im is the I_4-coefficient) and (3 + 4 I_4)/5. The declaration is removed.
- synthesis.collapse-in-vacuum-regular-at-future-horizon-selects-hawking-temperature: 1 -> 2. R2. Converted the null and thermal kernels, the KMS continuation -I_4 beta, and I_4 f' = +-I_4 f for I_4 d/d lambda. The declaration is removed.
- synthesis.hadamard-scaling-limit-premise: 4 -> 5. R2. Converted W_0, its i0 on both sides of the leaf, and the bulk limit I_4 nabla D_+ e_0 (an even value). The i0 regularisation of the bulk kernel stays i (declared).
- synthesis.dirac-states-restrict-to-null-hypersurfaces-through-the-flux-contraction-and-are-thin-layer-limits-under-the-generator-car: 2 -> 3. R2. The null-side (u - u' + I_4 0)^{-1} is converted. The regulator i epsilon s and its i0 stay i, and so does the Kay-Wald form quoted from the literature (declared).
- synthesis.field-strength-cancels-from-the-leading-null-singularity-of-hadamard-dirac-states-on-null-hypersurfaces: 3 -> 4. R2. Converted W_0, (u - u' + I_4 0)^{-1}, log(-I_4 s) and log(-I_4(u - u')). The i0 of a time function and the regulator sigma + i epsilon s, with its integrand, stay i (declared).
- synthesis.dirac-causal-propagator-between-nearby-null-leaves-tends-to-the-generator-car-on-every-geodesic-null-hypersurface: 2 -> 3. R2. Converted W_0, the layer limit (from "tends to" onward), the jump -2 pi I_4 delta, (I_4/2 pi)Lambda, log(I_4 s), and "the unit I_4 acts on the right". The regulator and its i0 sgn v in the Morse-coordinate computation stay i (declared).
- synthesis.hadamard-dirac-states-scale-to-the-flat-massless-vacuum-at-every-point-of-a-gravitational-field: 3 -> 4. R2. The Dirac numerator and the squared operator now use the right unit R_{I_4} : x -> xI_4, the notation group B introduced in the imported parametrix: (R_{I_4}D_x + m_0)H_+ e_0 and (R_{I_4}D - m_0)(R_{I_4}D + m_0). The plane waves are e^{-+I_4 p.z} with p = +-R_{I_4} nabla (checked by hand: (nabla e^{-I_4 p.z})I_4 = p e^{-I_4 p.z}). The even limit kernels are (I_4/2 pi^2)(y - y')e_0/Q^2 = I_4 nabla D_+ e_0. The boundary values sigma_{+-}, the regulators, Q(y - y' - i0 e_0) and the imported D_+ stay i (declared).
- synthesis.restricted-dirac-hadamard-parametrix-on-a-null-hypersurface-is-the-null-vacuum-plus-a-bounded-kernel: 1 -> 2. R2. The numerator is now (R_{I_4}D_x + m_0) in G_par and in the log part. The outputs are written with I_4: W_0, log(-I_4 s), log(-I_4(u - u')), the I_4 0 term, (I_4/2 pi) d_u log phi_t and the nonlinear-time limit. The regulator sigma_epsilon and every epsilon-expression it generates stay i, and so does the imported i0 prescription (declared).

Bookkeeping on every R2 entity: a credit entry (Claude Opus 5.5, notation pass, new version) and an `extraction.maintainer_pass_ga_units` note.
Each R2 entity also says once where its unit stands and that numbers are read in span{1, I_4}.

### Group B, re-checked against entities outside group B (no edits)
- c-loc, local-boost and r-loc (R1 reverts, complex-analysis) match the reverts above and the E/D2 window entities.
- modular-period (keeps the Cl(1,1) completed-pair phase i) is consistent with R1.
- clausius-is-window: its conversions are all on the generator's continuum (T_vv, h, Mellin modes), so it is consistent with R2. Its window first law carries no unit.
- locality keeps Q(xi) - i0 xi_0. That is the same R2 exception I applied to the Hadamard chain.
- imported-hadamard-parametrix uses R_{I_4}, which is the notation I followed.

## What could not be done exactly, or needs Leon's eye
1. Where the regulator's i meets the I_4 of its output. R2 keeps i only in the i0 shift of the spacetime separation. In field-strength, dirac-causal, dirac-states and restricted-dirac, that shift is written in scalar form, sigma + i epsilon(t(x) - t(x')). The computation that follows produces the null-side boundary values that R2 writes with I_4. I kept i in the regulator and in every epsilon-expression, and wrote the evaluated outputs with I_4. Each of those entities now says once that the values of the regularised kernels are numbers read in span{1, I_4}. So a few equations have i on the left and I_4 on the right, for example the transverse integral in field-strength Step 2 and "partial_u t/(s_0 + i g epsilon) -> partial_u log(s_0 + I_4 0)" in restricted-dirac. This is the identification of C with span{1, I_4}. It is notation, not a change in the mathematics, but it is where the R2 split shows.
2. The Dirac numerator. R_{I_4} acts on the value of the whole product, e_0 included. Read that way, (R_{I_4}D_x + m_0)H_+ e_0 equals the old (iD_x + m_0)H_+ e_0. Applying R_{I_4} to D_x H_+ before the factor e_0 would flip the sign of the unit term. The entity texts say that the unit acts on the right and commutes with every left factor. They do not spell out this order.
3. The modular-data entity's title ("... nor the sign of i") and id are unchanged. Every level now says "the unit I_4". Leon may want the title retitled "... nor the sign of the unit".
4. obj.hawking.continuum-mode-space keeps version 2 (see above). Under a strict reading of SWEEP ("version + 1"), it would be 3.
5. Possible errors from the sweep reports that are still present (not fixed, since the mathematics is out of scope):
   - quadratic-flows, formal (ii): the sign of the coherence phase does not match the proof (sweep-D1). It is now back in its i form.
   - boost-evolution (iii): the Hamiltonian sign under antilinear a(f) (sweep-A1).
6. The Borchers relation in positive-null-energy (split-owned) is still quoted as Delta^{is}, in the imported Fact's form. modular-data and geometric-modular now write Delta^{I_4 s} on the same continuum space. That is allowed by the imported-Fact rule, but it is a small notational mismatch.

## Work for the split-owned entities (not touched)
A detector scan of all 11 split-owned ids finds no bare i. The two new null-vacuum entities write I_4 throughout. So none of them needs R1/R2 work beyond these optional points:
- synthesis.positive-null-energy-gives-r-premises: if the Borchers relation in its proof is applied on the generator's continuum space and not only quoted, R2 would write Delta^{I_4 s}. Its window commutator (k_j - k_l)P_jl = icP_jl correctly keeps i (R1), and its declaration (imported) names both.
- synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes: being edited now, uncommitted. Its plane waves e^{-p.(x - x')I_4} with the right unit match hadamard-dirac-states-scale. If it writes a bulk boundary value Q(... - i0 e_0) anywhere, that shift should keep i, declared complex-analysis (R2). It currently has no bare i and no declaration.
- synthesis.null-vacuum-on-a-horizon-generator and synthesis.null-vacuum-singularity-under-reparametrisation-and-dilation are new and untracked, created by the split agent. They are not in SPLIT_OWNED.txt, so I did not edit them. They already follow R2.

## Left to the R3/R4 agent (claimed there)
- synthesis.thermality-of-every-future-half-generator-fixes-the-period-and-the-null-ground-state: its kernels are already I_4. The remaining i is the Step 1 contour (R4).
- synthesis.frozen-point-geometry-reads-descent-as-vacuum: its generator kernel D_c is already I_4. The remaining i is in the Bunch-Davies and Fourier kernels (R4).
