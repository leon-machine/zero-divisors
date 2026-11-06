# Filer S: results of the 6 November scalars session

Run 2026-11-06-edge-normality. Task: file R1 to R6 of scalars-context.md as proposals where new.
Work scripts: colony/runs/2026-11-06-edge-normality/work/S/.

Status: done. Three proposals filed (R1+R2, R3+R6, R5); R4 already in store; R7 already in store.

## Provenance field
`extraction.open_problem` is not required: validate_draft (tp/mcp_server.py) and tp/validate.py
never require it, and 141 stored synthesis claims carry none; their non-problem provenance is
`extraction.note` plus `lineage.motivated_by`. These proposals use the same: no open_problem,
an `extraction.note` naming the source (Leon's working document "Scalars and the Continuum: Review
and Extensions", 6 November 2026) and the ledger position.

## Duplicate decisions (filled as I go)

### R1 + R2: blade square signs as an F2 quadratic form (with the sign from symmetry)
- Duplicate check: read std-algebra.orthogonal-anticommute (e_I e_J = +/- prod Q e_{I xor J}, no
  form), transport.classification-real-clifford-algebras and primer.classification-real-clifford-algebras
  (the table by p - q mod 8), primer.sign / transport.sign (omega^2), std-algebra.periodicity,
  tower.rigidity-clock-frozen, tower.commuting-copies. grep -ril over store/claims, store/notes,
  store/objects for Arf, Salingaros, vee group, F_2, quadratic form over, extraspecial, Brauer,
  blade squares: no stored entity states the F2 quadratic form, its Arf invariant or the Gauss sum.
  search_claims returns only the blade basis. Decision: NEW. R2 is small and merged as clause (i).
- Re-checked with GA.py, exact: q from GA squares and polar form from GA anticommutation for every
  pair of blades in the 20 signatures with n <= 5; radical, Gauss sum (also as the scalar part of
  (1 - j)(1 + j)^p (1 - j)^q with j = e1e2 in Cl(2,0)) and type for all 44 signatures with
  1 <= n <= 8 (24 with n even, as in the session); the sign from symmetry in a normal-ordered
  quantum-plane model with c = 2, 1/3, -1, 1. Added (not in the session's text): the Gauss-sum
  closed form giving the whole table including odd n (R+R / H+H by the quotient Arf invariant),
  and clause (v), the (1,1) ascent as an isometry q_(p,q) + q_(1,1) -> q_(p+1,q+1) through the
  twisted generators (checked in Cl(p+1,q+1) for five ground signatures), Arf(q_(1,1)) = 0,
  Arf(q_(0,2)) = 1. That clause carries the part of R4 that was not already stored.
- Ledger: (i)-(iv) transport-absent (classical reformulation); (v) transport-convenient.
- Literature from memory (in extraction.note, not used in the proof): Salingaros vee groups;
  Lounesto; Arf 1941; extensions of elementary abelian 2-groups by quadratic forms (Quillen 1971);
  Frobenius-Schur indicator reading. The proof defines Arf by the Gauss-sum sign, so nothing is imported.
- Proposal: synthesis.blade-square-signs-f2-quadratic-form. validate_draft ok (info only: I213
  subject neighbours mostly standard-algebra); check4 exit 0, no findings.

### R3 + R6: integral orders of the (1,1) plane; the Witt partner as generalised inverse
- Duplicate check: read in full transport.regularity-localises-zero-divisors-idempotents (von
  Neumann regularity of nondegenerate Clifford algebras, generic x with axa = a),
  one-relation.two-presentations (both bases generate the same algebra over C; nothing over Z),
  descent-lift.pairing-creator-under-transport-algorithm (clause (ii): n^dag is the Moore-Penrose
  inverse of the pairing creator for the Fock adjoint). Also read std-algebra.cl11-matrix,
  std-algebra.witt-basis-car, transport.pseudo-inverse-torsor, std-algebra.zero-divisors-annihilated,
  std-algebra.radical-ideal-and-quotient, conformal.minimal-nondegenerate-completion and the T01 notes
  note.transport.setting-hyperbolic-atom-matrix-algebra-moore and
  note.transport.moore-penrose-boundary-idempotent-side. grep for M_2(Z), maximal order, integral
  order/idempotent, index 4, generalised inverse, Moore-Penrose, von Neumann regular, semisimplif.
  Findings: "the partner is the (Moore-Penrose) generalised inverse of a null vector" is ALREADY IN
  STORE in substance (T01 setting note on the hyperbolic atom; the pseudo-inverse torsor; the
  pairing-creator clause (ii)), but only as a note for the bare Witt pair, so it is kept as clause
  (iii) of the filed claim, flagged in extraction.note as a restatement. NEW: the integral orders
  (nothing in the store works over Z), the derivative through the partner, and rho x rho = 0 for a
  radical vector (non-regularity of degenerate algebras; the store has only the idempotent failure).
  Not an extension of a stored entity: one-relation.two-presentations is an extracted paper
  proposition, and a caveat over Z is better cited from a new claim than written into it.
- Re-checked with GA.py, exact: closure and integer structure constants of both Z-spans, the matrix
  isomorphism, change-of-basis determinant 4, 2 Lambda_W in Lambda_O, no idempotents other than 0, 1
  in Lambda_O (proof: x^2 = x forces scalar part 1/2; brute-force control over coordinates in
  {-3..3}), the ten nontrivial idempotents of Lambda_W with coordinates in {-1,0,1} all of scalar
  part 1/2; nmn = n, mnm = m in Cl(1,1), Cl(2,2), Cl(1,3); the adjoint exchanging a, a'; the
  derivative for 2x^3 + 5x at five points and (x^3 + 3x)/(x^2 + 1) at three, against hand-stated
  values; rho x rho = 0 on every blade in five degenerate signatures.
- Correction to the session text: the session said the two presentations "agree after inverting 2
  (quadratic versus bilinear form)". Made precise: Z a + Z a' with Q(xa + ya') = xy is the unimodular
  quadratic (hyperbolic) module; Z e+ + Z e- is an index-2 sublattice whose polar form has
  determinant -4 and whose bilinear form (half the polar form) is unimodular. The session's
  "(1 +/- e_+)/2 needs 1/2" holds, and those idempotents lie in neither order.
- Ledger: transport-convenient. Literature from memory (not used in the proof): Bass 1974 / Knus 1991
  on Clifford algebras of hyperbolic modules over rings; Reiner on maximal orders.
- Proposal: synthesis.hyperbolic-plane-integral-orders-and-partner-inverse. validate_draft ok (info
  I213 only); check4 exit 0 after strengthening the derivative check (first run gave W413, 7 of 8
  perturbations surviving; the check now compares with hand-stated values).

### R4: Morita ascent and the quaternionic kernel
- Duplicate check: std-algebra.periodicity (Cl(p+1,q+1) = M_2(Cl(p,q))), transport.rule-1-morita-trivial,
  tower.commuting-copies, tower.rigidity-clock-frozen (every floor shares the ground's division-ring type,
  centre, Morita class; the physical tower Cl(1+k,3+k) = M_{2^(k+1)}(H) frozen at clock position 6, which
  is the session's (p, p+2) chain for p >= 1), std-algebra.quaternions (Cl(0,2) = H, all three of e1, e2,
  e1e2 square to -1), std-algebra.even-subalgebra-isomorphism (Cl^+(p,p+2) = Cl(p,p+1), M(C) by the
  table), std-algebra.sta-matrix (even part of Cl(1,3) = Cl(3,0)), odd-extensions.twistor-algebra (even
  part of Cl(2,4) = M(4,C)), synthesis.plane-commutant-even-ground (ii) (centre of the even algebra is
  span{1, omega} in even dimension), and the conventions' section on I4 and I6 = I4 E (never identified).
  Decision: ALREADY IN STORE; not filed. The one piece not stored in this form, the anisotropic kernel
  (0,2) as the carrier of the quaternionic type against the (1,1) ascent, is clause (v) of the R1 proposal
  (Arf(q_(0,2)) = 1, Arf(q_(1,1)) = 0).
- Not reproduced: "the generator moves only under the naive inclusion". Computed in Cl(2,4) with GA.py:
  I4 is not central in the even part of Cl(2,4) (I6 is), and the twisted (tower) embedding x -> x omega
  sends I4 to I4 as well (product of four twisted generators, omega^4 = 1), so under both the naive
  inclusion and the tower embedding the central unit changes from I4 to I6 = I4 E; I6 is not +/- the image
  of I4 under either. The session's sentence may mean another identification; Leon to say which, if it
  matters.

### R5: limits as null steps
- Duplicate check: grep for dual number, Cl(0,0,1), derivative with nilpotent, elementary symmetric,
  nested square roots, half-angle, Archimedes, Taylor coefficient: transport.units-span and
  std-algebra.zero-divisors-annihilated mention dual numbers only as an algebra; note.primer.rotation-exactly
  has the half-angle rotor with rational (a, b); std-algebra.rotors-beyond-exponentials uses the
  (5/4 + 3/4 B) boost for another purpose; the boost scaling a null vector by e^(+/-lambda) appears in
  many synthesis results (for example synthesis.boost-evolution-on-generators-is-one-unitary-group).
  None states the four facts. Decision: NEW, filed as one claim.
- Re-checked with GA.py, exact: (a) on (x^3 + 3x)/(x^2 + 1) at four points against hand-stated values;
  (b) N = 2..6 in Cl(0,0,2N) and N = 3 with six orthogonal null vectors of Cl(6,6); (c) in Cl(1,1,2) with
  d = s rho1 rho2, s = 1, -3, 2/5, and R^2 = 5/4 + 3/4 B; (d) the field Q(r1, r2, ...), r_(k+1)^2 = 2 + r_k,
  implemented exactly as iterated quadratic extensions (class Tw in the check; coefficients of GA
  elements), R_(k+1)^2 = R_k and R_k R_k~ = 1 for k = 0..5, Archimedes' recursion for k = 1..5; (e) tan and
  arctan to degree 21 (largest denominator 194896477400625 = 3^9 5^4 7^3 11 13 17 19, odd), exp's 1/k!.
  The pi bounds and 4^k (U_k - L_k) -> pi^3/8 are in proof text only (numerical; float sanity run in
  scratch: L_6, U_6 = 3.14128, 3.14222; 4^6 gap = 3.876 against 3.8758).
- Correction to the session text: "products of two Witt null directions in Cl(N,N)" cannot give N
  commuting square-zero steps (a maximal isotropic set of Cl(N,N) has N vectors, giving floor(N/2)
  steps); it needs Cl(2N,2N), which is what the session's own example (N = 3 in Cl(6,6)) uses.
- Ledger: (a), (d), (e) transport-absent; (b), (c) transport-convenient. Tagged needs-continuum because
  clause (iv) states pi through the exponential chart (the finitist audit's criterion); the exact parts
  do not need it. Literature from memory: dual numbers (Clifford 1873), Archimedes, 2-adic valuation of
  the tangent numbers (for "every degree", not claimed).
- Proposal: synthesis.limits-as-null-steps. validate_draft ok (info only); check4 exit 0, no findings.

### R6
Merged into the R3 proposal (clauses (iii) to (v)); duplicate decision recorded there.

### Not filed (as instructed)
- R7 (I4 gamma0 gamma3 = gamma1 gamma2; Bisognano-Wichmann reflection as I4 times the transverse
  pi-rotation): ALREADY IN STORE, so not a candidate. synthesis.wedge-reflections-compose-to-the-two-pi-rotor-so-geometric-modular-conjugations-give-interacting-spin-statistics
  clause (i) states D = I4 B = gamma2 gamma3 for B = gamma0 gamma1 and Ad(B) = Ad(I4) o Ad(D), "the
  geometric part of the Bisognano-Wichmann conjugation, CPT composed with the turn by pi about the boost
  axis"; singularity.euclidean-rotor-where-it-lies (its 2026-11-01 note) and
  synthesis.modular-period-on-values-is-the-dual-plane-turn carry the imaginary-rapidity reading. The
  session's version uses the boost axis gamma3 instead of gamma1; same identity. No proposal from
  attackers A or B in proposals/ at the time of writing.
- R8: Wiesbrock 1993 is imported (scrambling.imported-time-plane-modular-data) only for "one half-sided
  modular inclusion recovers the two-dimensional conformal structure"; the store has no import of
  "half-sided modular inclusion with unique vacuum forces type III_1" (Longo; Wiesbrock), of the
  uniqueness of the hyperfinite III_1 factor (Connes 1976 for the injective III_lambda; Haagerup 1987 for
  III_1), or of Araki-Woods (R_(1/2) tensor R_(1/3) is III_1 since log 2 / log 3 is irrational). All from
  memory, statements not verified here.
- R9 (Hurwitz order of the kernel H = Cl(0,2)): lead only; nothing in the store on the Hurwitz order.

## Decisions for Leon
1. Accept or reject the three proposals; all are transport-absent or transport-convenient
   reformulations, not progress on an open problem. Most likely to be judged too elementary for the
   store: synthesis.limits-as-null-steps (clauses (i) to (iii) are classical identities); keep it only if
   the finitist thread wants the exact-versus-numerical boundary recorded as a claim.
2. Literature to import as Facts if the proposals are accepted (all cited from memory, none used as a
   premise): Salingaros's vee groups; the Arf invariant and its additivity; central extensions of
   elementary abelian 2-groups by quadratic forms (Quillen 1971); Clifford algebras of hyperbolic modules
   over rings (Bass 1974; Knus 1991); M_2(Z) a maximal order (Reiner); dual numbers; Archimedes. From R8:
   Longo / Wiesbrock (hsm inclusion with unique vacuum gives III_1), Connes-Haagerup uniqueness of the
   hyperfinite III_1 factor, Araki-Woods.
3. Whether one-relation.two-presentations should carry a wording note: its proof says "both bases
   generate the same algebra, since a Witt basis is a linear change of basis of an orthogonal one over C";
   true over any ring containing 1/2, false over Z (index-4 suborder). Left to the maintainer; the new
   claim cites it and states the integral difference.
4. R4's sentence "the generator moves only under the naive inclusion" was not reproduced (see R4 above).
5. Provenance format: no extraction.open_problem (not required by validate_draft or the validator; 141
   stored synthesis claims have none); provenance in extraction.note. If Leon wants a uniform marker for
   results brought in from working documents (for example extraction.source_doc), that is a schema
   decision.
