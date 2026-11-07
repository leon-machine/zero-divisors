# Bridge survey, 7 November 2026: three open problems

Read-only survey of the Transport Lab (phys-graph at 8eef5a4). Nothing filed or edited. Labels: proved (in store), computed (exact, Fractions + GA.py, scratch scripts), argued, speculative. Per-problem reports: op.hypothesis-s.md, op.r-premises-external.md, op.deposit-state-is-hadamard.md (same folder).

## Selection
Ranked by future cone of the premise discharged and by links to other problems:
1. op.hypothesis-s: standard-model.slot-module-hypothesis, future cone 225.
2. op.r-premises-external: (N+) carries every temperature, S = A/4, 8 pi M, de Sitter.
3. op.deposit-state-is-hadamard: (HD); references shared with 7 other problems.
Caveat (found below): cone sizes are inflated where a result cites one algebraic clause of an entity whose other clauses hold given postulates. Cone-based ranking should be read with that in mind.

## Cross-problem findings

### X1. The Hadamard chain's dependence on (N+) is bookkeeping, not logic (checked by lookup)
Path found: synthesis.hadamard-scaling-limit-premise -> synthesis.hadamard-dirac-states-scale-to-the-flat-massless-vacuum-at-every-point-of-a-gravitational-field -> synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes -> synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays -> synthesis.positive-null-energy-gives-r-premises -> (N+). The bulk-Hadamard proof cites the light-ray result only for clause (i), the projector Lambda(m) = mk/4 (pure algebra); the light-ray result uses positive-null-energy only in a later clause (the carrier boost's weight 1/2). It also cites synthesis.slot-module-light-ray-arrays-are-weyl-components(i), which brings in (S). So the scaling theorem lists 18 postulates in holds_given, including (N+), (S), R1-R3, P2, P3, H1, apparently none of them used. A clause-level split (maintainer) would clear them.

### X2. With X1, (HD) supplies the sign eta of (N+) wherever it reaches (STRONG, argued)
synthesis.geometric-modular-conjugations-on-a-generator-give-the-null-ground-state: field-level geometric modular action (CGMA) at dense cuts gives the null vacuum for eta = -1 and only the filled sea for eta = +1. The filled sea differs from the null vacuum by the kernel of sign(P), not Hilbert-Schmidt on any interval, so it is locally disjoint from the vacuum everywhere. Hence CGMA of either sign plus the local form at one point gives (N+). The local form is a theorem for Hadamard states, and (HD) is an oriented wavefront condition. So on every field (HD) and the propagation Facts reach, eta is not a separate datum: it is the orientation inside (HD). Remains: CGMA at dense cuts; the eternal hole and eternal de Sitter (no descent, so (HD) does not reach). Ledger: absent.

### X3. One sign the kinematics cannot fix appears in all three problems, but it is at least two bits (computed)
- (N+): eta, vacuum versus filled sea (store: a datum (N+) assumes).
- (HD): indifference and real states select occupation 1/2 (synthesis.incidence-vacua-thermofield-real-capacity); lifting off 1/2 needs an orientation.
- (S): the neutral-singlet bit (Omega or Omega^T) and the flag sign epsilon; notes note.field-theory.what-does-t12 and note.standard-model.setting-two-flags-resolved-2 say one parity identification fixes both.
Common structure: each bit is invisible to every structure the swap commutes with (the Z2 form of dark-matter.orientation-arrow-seventeenth-refutation). Computed (work/flag_energy.py, all pass): for the eight Witt flags of Cl(2,4) adapted to (e0, nu), (e1, e2), (e3, e-) with signs (s0, s1, s2), Z psi = -i s0 psi (Z = e0 nu) while the stored family bit (I6 eigenvalue) is s0 s1 s2. So the matter-asymmetry flag (dark-matter.premise-flag-as-datum) and eta are independent unless J's orientation on the four-space orthogonal to Z is fixed. The store does not link them; T16's "particle-antiparticle orientation is the sign separating positive from negative frequency" holds only given that second orientation.

### X4. A possible geometric home for the orientation: the branch at the wall (PLAUSIBLE)
Computed (hd/screen.py, exact to order 12): across the radical-normal tame wall (synthesis.radical-normal-tame-wall-is-a-regular-initial-surface-whose-smoothness-selects-no-state; tau = 2 sqrt t, far side Riemannian), a massless mode analytic in t continues with cos k tau -> cosh k tau_E and sin k tau -> +-i sinh k tau_E, the sign the branch of sqrt t. The far-side decaying mode continues to e^{-+ik tau}: requiring boundedness on the far side selects the conformal vacuum for one branch and the filled sea for the other. If this survives for Dirac fields, the chain is: wall branch -> (HD) reference vacuum -> (X2) local (N+) with its sign. Kill condition: the bounded far-side Euclidean Dirac solutions (weight t^{-3/4}, phase e^{-+3 pi i/4}) continued through t are not exactly a Hardy (positive-energy) subspace for either branch. Gives the vacuum, not a temperature; a hot deposit needs a finite far-side width (only candidate: the shadow wall, sheaf.conservation-degeneracy-located, probably collar-dependent). Ledger: essential if it survives.

## Per-problem leads (best first)

op.deposit-state-is-hadamard
- L2 STRONG (conditional): a finite deposit over the attachment's flag vacuum is a finite-rank smooth kernel, hence Hadamard (field-theory.twistor-attachment floors are conformal-energy cut-offs; dark-matter.p2-indifference declares the deposited mode set finite; synthesis.hadamard-condition-leaves-the-deposit-spectrum-free-on-bounded-bands). Needs a decision: does P2's finiteness apply per window to field modes? That window bound is the k_UV of op.descent-state-and-spectrum. Ledger: convenient.
- L1 = X4.
- L3 PLAUSIBLE: maximum-entropy or KMS deposit for the collar's conformal-time flow (synthesis.q-splits-maximum-entropy-affine-weights); needs a new collar (G) premise.
- Obstructions: indifference gives the trace; modular descent at the wall pair deposits a trace (the pair boost is gauge); every finite-moment bound (entropy counts, area law, C2, shot noise, local quasi-equivalence) excludes the trace but not power tails; stabiliser invariance selects only the vacuum; for massless fields (HD) reduces to the inherited state (op.pre-descent-theory).

op.r-premises-external
- A = X2. B = X3. C PLAUSIBLE: a module-level image of CGMA in the twistor storey (synthesis.wick-rotated-boost-selects-observer-tube-point; boost at rapidity i pi is the wedge reflection), which could replace the imported Bisognano-Wichmann converse; sign-blind; Minkowski and de Sitter only.
- Obstruction O1 (argued, conditional on dark-matter.premise-cpt-covariance): C = Ad(I6) o kappa fixes every real bivector of Cl(2,4) and is antilinear, so it reverses every self-adjoint generator, null translations included, and maps the null vacuum to the filled sea. No principle built from kinematics and actions can then fix eta. Flag: an antiunitary that fixes the translations reverses the energy, so C is not the CPT operator of quantum field theory (which keeps energy positive); the premise text's "that this conjugation realises that operator is argued" looks false.
- Eternal hole: nothing found supplies reflections about non-bifurcation cuts; negative evidence that a premise is needed there.

op.hypothesis-s
- What synthesis.cpt-closure-forces-slot-module-and-chirality leaves open: the neutral-singlet bit, clause (G) (unique vacuum, b = 1), clause (f), clauses (a) and (b).
- A STRONG (reduction; computed b = 1..4, argued all b): if the slot module is a Fock module of either statistics over its one-slot space bC^2, CPT closure forces b = 1 and Lambda C^2 (b >= 2 gives weak spin one at slot number two; CCR modules are infinite). Statistics, vacuum count and doublet count become outputs; the Fock clause is still a premise, automatic if slot quanta are tower modes ("each twistor a rung", the missing theorem). Ledger: convenient.
- B PLAUSIBLE: Pati-Salam su(4) and so(2,4) are real forms of one complex algebra, so the Pati-Salam clause is the chirality's conformal invariance on the pair factor. Computed: gauge plus the even pair algebra leaves exactly +-(-1)^N among anomaly-free CPT halvings and excludes the vacuum-swapped one; su(4) alone suffices. Remains: identify the label copy's parity with the twistor's, which by the store's notes also fixes epsilon. Kill: no map carries the twistor chirality to the label copy's k-parity. Ledger: essential.
- C STRONG: clause (f) is a Klein convention on V (twist unique up to sign; the 21 Pati-Salam bivectors and the grading unchanged). Ledger: absent.
- No bridge to the thermal side beyond the shared pattern of X3.

## Decisions for Leon
1. Clause-level split of synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays and synthesis.slot-module-light-ray-arrays-are-weyl-components (maintainer edit), clearing the Hadamard chain's inherited postulates (X1).
2. Whether P2's finiteness declaration covers field modes per window (L2).
3. The CPT premise wording: C as defined reverses energy (O1).
4. Whether to run the attacker-referee method on the deciding computations: X4 far-side Dirac continuation; X3 on tube-point flags (synthesis.positive-structure-is-twistor-form-at-imaginary-time; kill: both energy signs within one family); Lead A of (S) for all b.

Subjects walked (union): standard-model, tower, quantum-fields, conformal-spacetime, descent, thermality, entropy, clifford-structure, completion, one-relation, walls, generations, dark-matter, dark-energy, standard-algebra, lepton, singularity, programme, zero-divisors. Cost about 690k subagent tokens.
