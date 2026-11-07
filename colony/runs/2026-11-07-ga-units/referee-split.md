# Blind referee: the four clause-split entities (2026-11-07)

Scope: synthesis.canonical-part-of-a-spinor-on-a-null-plane (E1), synthesis.null-vacuum-on-a-horizon-generator (E2),
synthesis.null-vacuum-singularity-under-reparametrisation-and-dilation (E3), synthesis.stationary-generator-states-and-the-edge-scaling (E4).
Read: BRIEF.md (referee role), conventions.md (GA language, imaginary units incl. the 7 November rule), RULINGS.md R2/R4 (unit rulings only).
Not read: split.md, work/, survey/, findings/.

## Method

- Every proof step read and re-derived by hand (below, "checked").
- Premises fetched at their pinned versions (field-theory.second-quantisation@5, hawking.i-state-continuum@5,
  hawking.imported-quasi-free-kms-reduces-two@2, hawking.imported-ideal-fermi-gas-uniqueness@2, synthesis.null-vacuum-on-a-horizon-generator@1); all pins are the current versions.
- Past cones (Lab.cone): E1 33 entities, E2 7, E3 8, E4 8. No postulate in any cone; holds_given = [] for all four.
  E2 to E4 rest only on the hawking I-state chain and three imported literature Facts; E1 only on the algebra chain
  (std-algebra, tower, transport, field-theory.imported-tower-limit). (N+) (synthesis.n-plus-null-ground-state) appears only in prose,
  as "a separate matter" or as a name for a reading (E4's "local form of (N+)"); no step uses it. No other postulate under another name.
- Origin comparison against 8eef5a4 (entity.md and proof-main.tex of the four source results), by sentence-level diff after normalising i to I_4.
- All four checks run (runcheck): every function PASS, exit 0. Each broken by targeted perturbations (table below).
- Own exact recomputations: E1 flux by hand; E2 ground-state sign by an exact finite CAR model; E3 Schwarzian for xi = U + U^3; E4 g_2 coefficient by hand.

## E1 synthesis.canonical-part-of-a-spinor-on-a-null-plane

Steps checked. (i) k gamma_0 = 1 + B, km = 2 + 2B, mk = 2 - 2B; idempotence and orthogonality from B^2 = 1; Dirac self-adjointness
(reverse of (1 - B)/2 is (1 + B)/2, gamma_0 B gamma_0 = -B); ker L_m equals the (-1)-eigenspace both ways. (ii) kvk = 2(k.v)k gives J.k = 0 on
the image of Lambda(k). (iii) (I_4 sigma_3)^2 = -1; I_4 commutes with bivectors; right and left multiplications commute. (iv) splitting
a = m(k.a)/2 + k(m.a)/2 + a_perp (checked at a = k, m); k nabla = 2 Lambda(k)(k.nabla) + k nabla_perp; k nabla_perp Lambda(k) psi = 0 by
anticommutation; covariant maps: f(psi) = psi f(1); rotors span Cl+ (cos/cosh + X sin/sinh give 1 and the six bivectors,
e^{a gamma_01} e^{b gamma_23} gives I_4); the constraint equation is correct.

Premise: field-theory.second-quantisation@5 (1) says Lambda(k) = k gamma_0/(2k_0) is the orthogonal projector onto ker k: exactly what (i) and the
plane-wave remark of (ii) need.

Own route: psi = 1 + 2 gamma_12 + 3 gamma_03 gives J = psi gamma_0 psi~ = 14 gamma_0 - 6 gamma_3 by hand, so J.k = 20 and J.m = 8;
Lambda(m) psi = 2 + 2 gamma_03 + gamma_12 + I_4 (norm^2 10) and Lambda(k) psi = -1 + gamma_03 + gamma_12 - I_4 (norm^2 4): 20 = 2*10, 8 = 2*4.

Origin: (i)-(ii) match light-ray (i); (iii) is weaker than light-ray (iii) (two complex channels, no chirality split), correctly so; (iv) matches
slot-module (i), with the right-multiplier step now proved where the source argued it. Self-adjointness and complementarity are new and proved.
Nothing else changed apart from numbering and I_4.

Defect (inherited verbatim from slot-module (i)): the proof says the constraint fixes Lambda(k) psi along each generator "up to its value at
one end of the generator", but formal (iv), technical and one-liner state flatly that "the free data on N_k are Lambda(m) psi". That omits the
integration constant (the light-front zero mode).

Minor: "with linear maps on any internal index" should say the covariant map is a matrix of right multipliers psi_a -> sum_b psi_b X_ba
(the proof's argument gives exactly this for real-linear maps, Majorana conjugation included); the check covers only the case with no internal index.

Literature: Kogut-Soper 1970, flagged from memory as orientation, not used. The GA form psi -> psi sigma_1 of charge conjugation is stated without
a source (standard; not needed, since the lemma covers it).

Verdict: SOUND WITH FIXES.
1. Formal (iv), after "fixes Lambda(k) psi along each generator from Lambda(m) psi": add "(up to its value at one end of each generator)", and
   change the conclusion to "the free data on N_k are Lambda(m) psi, together with that one boundary value of Lambda(k) psi per generator, for every
   mass matrix". Make the same change in technical and one-liner ("whatever the masses" and "the free data on the plane").
2. Formal (iv): replace "(with linear maps on any internal index)" with "(with an internal index, a matrix of right multiplications)".

## E2 synthesis.null-vacuum-on-a-horizon-generator

Steps checked. Conventions: a(f) antilinear; A(u,v) = omega(psi*(v) psi(u)); nu_a(a(f)) = a(f(. - a)) = a(e^{I_4 a P} f) with P = I_4 d/du.
(i) the weight condition e^{2 lambda Re w_0} e^{-lambda} = 1; beta_t nu_a beta_{-t}(psi(u)) = psi(u + e^{lambda} a) by direct composition.
(ii) necessity: delta(a(g)) = a(I_4 P g) = -I_4 a(Pg) (antilinearity), which gives -<Pg, Ag> >= 0; delta(a*(f)) = I_4 a*(Pf) and
omega(a(f)a*(g)) = <f,(1-A)g> give <f,(1-A)Pf> >= 0. So A(k) = 0 for k > 0 and 1 for k < 0. P e^{I_4 k u} = -k e^{I_4 k u}, so chi(P < 0) keeps k > 0,
with kernel (1/2pi) int_0^inf e^{I_4 k x} dk = (I_4/2pi)(x + I_4 0)^{-1}.
(ii) converse (checked with particular care): a projection symbol gives a pure Fock state whose GNS representation is the Fock space of
chi_[0,inf)(P)h (particles) and the conjugate of chi_(-inf,0)(P)h (holes). Gamma(e^{I_4 a P}) implements nu, with generator dGamma(P) >= 0 on
particles and dGamma(-P) >= 0 on holes (the conjugation reverses the sign), and it annihilates the vacuum. Correct.
Own route: an exact finite CAR model in Gaussian rationals (2 modes, Jordan-Wigner; one-particle generators (1, -1) and (3/2, -2/5); the dynamics
convention delta(a(f)) = a(i h f) verified). Symbol chi(h < 0) gives -i omega(x* delta x) = 37/4, 109/225, 9191/900, 37 on four test elements and
GNS spectrum {0, 1, 1, 2}. Symbol chi(h > 0) gives all four values negative and spectrum {-2, -1, -1, 0}. So the sign of (ii) and of the converse
is right for the convention tau_t(a(f)) = a(e^{I_4 t h} f).
(iii) Mellin: v = ux substitution; the pole at 1 + I_4 0; downward rotation x = r e^{-I_4 pi} (decay O(|x|^{-3/2}), O(|x|^{-1/2}) at 0);
Euler; e^{-I_4 pi s} = -I_4 e^{pi w}, sin(pi s) = cosh(pi w), so m(w) = (1 + e^{-2 pi w})^{-1}. h phi_w = -kappa w phi_w, so beta = 2pi/kappa.
Past half: the reflected kernel is the conjugate, giving m(-w), and gamma_t = beta_{-t} has generator +kappa w: beta = 2pi/kappa again.
Strip: F(lambda + I_4 theta) analytic on 0 < theta < 2pi for u, v > 0, the boundary values give the two orderings (weight factor e^{I_4 pi} = -1),
and the KMS convention omega(A tau_{t + i beta}B) = omega(tau_t(B) A) is matched. (a) to (d) are correct.

Premises at pinned versions: i-state-continuum@5 uses tau_t(a(f)) = a(e^{I_4 t h} f) and the symbol (1 + e^{beta h})^{-1} (obj.hawking.continuum-mode-space@2);
kms-reduces-two@2 lifts the two-point identity; ideal-fermi-gas-uniqueness@2 gives uniqueness among all states. Each says what is used.

Sign conventions against the store: chi(P < 0), P = I_4 d/du, W_0 = (I_4/2pi)(u - v + I_4 0)^{-1} agree with (N+) v11 ("filled sea chi_(-inf,0)(P)",
the time reverse chi_(0,inf)(P) a ground state only for the reversed translations), and with the field-level modular result
(T_0 = chi_(-inf,0)(P), eta = -1, modular group the boost at rapidity -2pi t, which is KMS at +2pi for beta_t: consistent with (iii)).
The orientation of I_4 relative to time enters only through "nonnegative generator of e^{I_4 a H}", exactly as (N+) datum (2) says.

Origin: setup, (ii) and (iii) match source (i) and (ii) sentence by sentence after i -> I_4. The source's horizon geometry ((iii)), the (iv)
obstruction and the (v) spectrum condition are left behind, as stated. New: the converse in (ii), the explicit second ordering, and clause (i)
gathered from the setup and (iv). "the restriction of omega there is pure" became "omega_0 there is pure", which is the same statement.
No other content change.

Gaps:
- Necessity: "A commutes with e^{I_4 a P}, so A is a function of P" holds only for K one-dimensional. In general A is decomposable,
  A = int (+) A(k) dk with 0 <= A(k) <= 1 on K. The two inequalities then force A(k) = 0 (k > 0) and id_K (k < 0) fibrewise, so the conclusion
  stands. Inherited.
- The converse's "standard for quasi-free states with projection symbol, cited from memory" is the stored Fact
  synthesis.imported-powers-stormer-takesaki-disjointness@3 (d) (Araki 1970: a gauge-invariant quasi-free state is pure if and only if its symbol is a projection,
  and it is then a Fock state). That Fact is imported and postulate-free, so pinning it leaves the cone free of postulates.

Literature from memory: Bratteli-Robinson Vol. 2 "§5.3.19". As I recall (also from memory), the characterisation is Definition 5.3.18 with
Proposition 5.3.19, so the cited content is right but "§" is the wrong label. Euler's integral and Mellin-Plancherel are correct.
Bisognano-Wichmann, Hislop-Longo and Sewell are named as orientation and not flagged as from memory.

Checks: the strip, past-half and Mellin functions compute with Gaussian rationals QI and write "i" in their comments, while the kernel
function works in span{1, I_4} of Cl(1,3). This is not a soundness issue: R4 governs entity text. The converse has no check (proof only).

Verdict: SOUND WITH FIXES.
1. Proof, (ii) converse: replace "(standard for quasi-free states with projection symbol, cited from memory)" with
   "(Fact \claimref{synthesis.imported-powers-stormer-takesaki-disjointness}(d))", and add synthesis.imported-powers-stormer-takesaki-disjointness@3 to uses
   (a maintainer decision; imported, no postulate). Also add a premise() call in a check, or drop the item from the extraction note's from-memory list.
2. Proof, (ii) necessity: replace "so $A$ is a function of $P$" with "so $A$ commutes with $P\otimes\id_K$ and is decomposable over the spectrum of $P$,
   $A = \int^{\oplus} A(k)\,dk$, $0 \le A(k) \le 1$ on $K$", and read the two inequalities fibrewise.
3. Proof: "Bratteli and Robinson, Vol.~2, \S 5.3.19" -> "Bratteli and Robinson, Vol.~2, Definition 5.3.18 and Proposition 5.3.19"; extraction note: add
   "Bisognano-Wichmann, Hislop-Longo, Sewell (orientation, from memory)".

## E3 synthesis.null-vacuum-singularity-under-reparametrisation-and-dilation

Steps checked. (i) Expansion: N/D = 1 + (ac - b^2)x^2/a^2 + O(x^3) and (ac - b^2)/a^2 = S/6. The ratio is 1 + S x^2/12, so the difference is S x/12.
The I_4 0 delta parts cancel (delta(Delta xi) = delta(x)/a, times a). Weight 0 and 1 controls; weight h gives (h/6) S x^{2-2h}. The xi = U^3 case.
Own route: xi = U + U^3 at 0 has S = 6 and squared ratio (1 + 3x^2)/(1 + x^2)^2 = 1 + x^2 + ..., which is S/6 = 1.
(ii) delta_eps(psi(g)) = psi(eps^{-1/2} g(./eps)); the substitution gives W_0 invariant and eps R(eps x, eps x'); the bound eps C ||f||_1 ||g||_1;
extension from compact support by uniform L^2 bounds; homogeneous degree -1 remainder survives.
Premise: (ii) uses null-vacuum@1 (i) for the automorphism and (ii) for W_0; both are stated there.

Origin: (i) and (ii) are source (iii) and (iv) verbatim after i -> I_4, with beta_tau -> delta_eps and "U, r and the affine parameter" ->
"every regular parameter" (the general statement the proof gives). The Boulware sentence is left behind. No content change.

Defects (both inherited):
- Proof (ii), sharpness remark: "such states lie outside the class of (i) when the $a_k$ are discontinuous at $0$" is wrong as stated. A bounded
  discontinuous a_k gives a bounded remainder, which is inside the class ("remainder bounded near a point"). The formal claim "states outside
  the class can have the same limit" is still true with an unbounded a_k. Example: a(u) = (u + I_4 0)^{-1/4}(u + I_4)^{-1} is in the range of
  chi(P < 0) (an upper-half-plane boundary value), in L^2 and unbounded at 0, and T_0 - c|a><a|/||a||^2, 0 < c <= 1, is a valid symbol whose
  remainder is unbounded near (0,0) and whose dilation limit is omega_0.
- "a gauge-invariant quasi-free state is determined by its two-point function (Fact kms-reduces-two, the quasi-free structure)": that Fact is
  about the KMS condition. The determination is hawking.imported-quasi-free-states-car-algebra@2 (unique state with that symbol, Wick determinants).

Verdict: SOUND WITH FIXES.
1. Proof (ii): "when the $a_{k}$ are discontinuous at $0$" -> "when some $a_{k}$ is unbounded near $0$ (for example
   $a(u) = (u + I_{4}0)^{-1/4}(u + I_{4})^{-1}$, in the range of $T_{0}$, with $T_{0} - c|a\rangle\langle a|/\|a\|^{2}$, $0 < c \le 1$)"; delete "which also holds when $R$
   is bounded but discontinuous at the origin" or keep it, since it is true but inside the class.
2. Cite hawking.imported-quasi-free-states-car-algebra@2 for "determined by its two-point function" (formal (ii) and proof), in place of or beside
   kms-reduces-two (imported, no postulate; a maintainer decision).

## E4 synthesis.stationary-generator-states-and-the-edge-scaling

Steps checked. (i) <sigma f, sigma g> = lambda^{2p-1}<f,g>; (e_1e_0)^2 = 1, e_1e_0 l = l, e_1e_0 n = -n, B l B~ = B^2 l = e^lambda l.
(ii) stationarity gives lambda W(lambda x, lambda y) = W, so the scaling family is constant; the iff uses both directions of null-vacuum (ii), which is why
the converse was added. The bounded-difference argument is correct.
(iii) The log map gives W_0 -> (I_4/2pi)(2 sinh((x - x')/2))^{-1}; W_c = c^{-1} F((x - x')/c); the Fourier symbol is m_1(cw); h = -kappa w gives
beta = 2pi c/kappa. g_c = y^{-1}(S(y/2c)^{-1} - S(y/2)^{-1}) with first coefficient -(c^{-2} - 1)/24 and y^3 coefficient 7(c^{-4} - 1)/5760.
The analyticity strip, the off-edge scaling limit, the cross-edge block 0 versus (I_4/2pi)(u - v)^{-1}, and non-identity with omega_0 via uniqueness of the I-state.
Own route: c = 2 gives 1/(4 sinh(y/4)) - 1/(2 sinh(y/2)) = y^{-1}[(1 - y^2/96) - (1 - y^2/24)] = y/32 = -(1/4 - 1)/24.

Origin: (i)-(iii) are source (i)-(iii) after i -> I_4, with "satisfies (N+)" -> "is the gauge-invariant quasi-free ground state of the null
translations" (the same content, since (N+) assumes quasi-free) and the horizon identification removed; "omega_0 is its own scaling limit at every
point" is promoted from the proof to the statement. (iv) null energy and (v) are left behind. No content change.

Defect (inherited): proof (iii), "For $c = \infty$ the symbol is $\chi_{(-\infty, 0)}(w)$" has the wrong sign. m_c(w) = (1 + e^{-2pi c w})^{-1} -> 1 for w > 0,
and the stated kernel (uv)^{-1/2}/(y + I_4 0) has Fourier symbol chi_(0,inf)(w). The boost ground state occupies h = -kappa w < 0, i.e. w > 0.
The formal statement ("c = infinity: the ground state of that boost") is right.

Checks: check_cross_edge_block asserts the product state's zero cross block (D = 0 - X) rather than computing it. It is definitional, so not vacuous.

Verdict: SOUND WITH FIXES.
1. Proof (iii): "the symbol is $\chi_{(-\infty, 0)}(w)$" -> "the symbol is $\chi_{(0, \infty)}(w)$, that is $\chi_{(-\infty,0)}(h)$". Fix the same slip in
   synthesis.stationary-horizon-state-is-its-own-edge-scaling-limit, which still carries it.

## Perturbations (all on copies in scratch; store untouched)

| entity | perturbation | result |
|---|---|---|
| E1 | B = gamma_0 gamma_3 (sign flip) | projectors, flux, mass checks FAIL |
| E1 | psi coefficient 3 -> 4 with flux == 20 kept | flux FAIL |
| E1 | m = gamma_0 - 2 gamma_3 (not null) | projectors, flux, mass FAIL |
| E1 | covariance equations on 2 of 6 bivectors | covariant-maps FAIL |
| E1 | Hestenes unit -> gamma_1 gamma_3 gamma_0; I_4 -> gamma_1 gamma_3 | two-channels FAIL (both) |
| E2 | ground-state inequalities reversed | filled-sea FAIL |
| E2 | conjugation order of boost and translation reversed | dilation FAIL |
| E2 | Mellin target e^{2 pi h} -> e^{-2 pi h} | Mellin FAIL |
| E2 | sign of the second ordering dropped | kernel/anticommutator FAIL |
| E2 | weight test rho^{k-2} -> rho^{k-3} | strip FAIL |
| E3 | weight 1/2 -> 1 in the squared ratio | reparametrisation FAIL |
| E3 | extra eps factor | dilation FAIL |
| E3 | xi coefficient 1/7 -> 1/6 | tabulated S/6 FAIL |
| E4 | drop the 1/c in W_c | kernels FAIL |
| E4 | 4^j -> 2^j in S(z)^{-1} | off-edge FAIL |
| E4 | rotor bivector e_1e_0 -> e_0e_1 | boost/scaling FAIL |

Two perturbations of E1 passed: Hestenes' unit replaced by -(I_4 sigma_3) = gamma_1 gamma_2, which is not a real change, and B's sign flip
left the two-channel and covariant-maps checks passing. This is expected: those facts do not depend on B's sign or on which right unit is used.

## Summary

All four hold with no postulate. Nothing in their past cones carries (N+) or any other postulate. The split changed no content beyond
numbering, the unit I_4, the stated additions (E1's self-adjointness and the computed right-multiplier lemma; E2's converse) and the
removal of the horizon-specific clauses. The converse in E2 is correct and its sign agrees with (N+), the field-level modular result and an
exact finite model. Every fix is wording or citation, and all but E2's converse citation are inherited from the source results.
