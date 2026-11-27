# attack-corner: the corner area as generator of the relative boost of a null-plane pair

Run 2026-11-27-null-surface-three. Attacker `corner`. Files: scratch scripts in
`colony/runs/2026-11-27-null-surface-three/work/corner/`.

## Target
At the corner where the null planes n.x = 0 and nbar.x = 0 meet (the spacelike 2-plane spanned by
e_1, e_2), show from the stored symplectic current of R1 (clause (i), constant 1/(16 pi G) of
clause (vi)) that the on-shell generator of the boost of the n ^ nbar plane is a pure corner term
equal to delta A / (8 pi G), with the rotor normalised as exp(-chi B / 2), B^2 = +1. In place of the
imported Fact `synthesis.imported-wald-noether-charge-entropy`, which must NOT be a premise.

## Pre-registered kill conditions (written before any computation, 27 November 2026)
- (K1) The on-shell boost generator obtained by contracting the stored symplectic current
  omega/(16 pi G) with the boost variation of the field (transport of the argument plus the rotor on
  the frame) and integrating over a surface through the corner is NOT a pure corner term (a bulk
  remainder survives on solutions of the first-order vacuum equation, in a generic gauge).
- (K2) The corner term is NOT proportional to the first-order variation of the corner area (it
  contains components of h other than the transverse trace, or derivatives that do not assemble into
  the area variation, in a way no admissible corner-fixing displacement removes).
- (K3) The coefficient is not 1/(8 pi G): with omega/(16 pi G), the stored signs, and the rotor
  exp(-chi B / 2), delta H_chi != delta A / (8 pi G).
- Secondary, for clause (c): (K4) the second route (first-order focusing equation of R1 (ii)/(iii)
  integrated with the boost weight) disagrees with the first route in sign or coefficient.
- Secondary, for clause (d): (K5) the real-GA continuation of the boost rotor does not close at the
  angle that makes exp(-A/(4 G hbar)) come out; then (d) is filed as argued or left out.

Any of these firing is reported as the result, with the true statement filed.

## Routes considered (before computing)
1. (Chosen) Symbol/polynomial route in R1's toolkit: omega(h, L_xi h) with xi the boost field
   xi(x) = B . x (or x . B, sign to be fixed by the rotor convention), show omega(h, L_xi h) =
   divergence of an antisymmetric (bivector-valued) potential on shell, plus a term proportional to
   E[h]; integrate over the half null plane n.x = 0, nbar.x > 0 (or a spacelike wedge slice) and get
   the corner term. Exact check on polynomial vacuum solutions by Fractions.
2. First-law route through R1 (ii)/(iii): d_n theta = n.E[h](n) = -8 pi G n.T(n) at first order;
   multiply by the boost weight (affine parameter lambda along the generator from the corner) and
   integrate by parts: int lambda d_n theta = [lambda theta] - int theta = -(delta a at corner) + ...
   Gives boost energy = delta A/(8 pi G). Independent of the symplectic current: the cross-check.
3. Noether route from the quadratic functional S = -(1/32 pi G) int <h, E h>: the canonical
   Noether current of the boost, improved. Equivalent to 1 but with the extra burden of the
   non-covariance of the quadratic Lagrangian; kept as a fallback.

Choice: 1 with 2 as independent cross-check (the agreement of the two is the evidence asked for).

## Near-duplicates in the store (searched before proving)
- `synthesis.imported-wald-noether-charge-entropy` (imported; the Fact this result is to stand in
  place of, at first order on a flat null-plane pair). Not a premise.
- `synthesis.clausius-is-window-first-law-plus-boost-charge-conservation` (clause 6, 7: the boost
  charge on a generator int chi^v T_vv; matter side). Complementary: gives the matter boost charge,
  not the gravitational corner term.
- `synthesis.imported-null-plane-modular-hamiltonian-first-law` (imported; K(u0) = int (u-u0) T_uu).
- `synthesis.einstein-equations-from-c-loc-and-clausius` (uses delta A from Raychaudhuri with (Loc)).
- `synthesis.modular-period-on-values-is-the-dual-plane-turn` (the continued boost rotor on values is
  the dual-plane rotor exp(-theta I_4 B / 2); R(2 pi) = -1). Directly relevant to (d).
- `singularity.euclidean-rotor-where-it-lies` (on vectors the continued rotor needs I_5; not a real
  rotor of Cl(1,3)).
No stored result derives the corner term from the symplectic current.

## Log
(see below; kept current)

### Log entry 1 (27 November, after first computations; scripts explore1-5.py, dev_*.py, poly.py)

Structural finding BEFORE the kill conditions could be read off (labelled):

- (argued, then proved below) The stored current omega(h1, h2) is bilinear in two FIRST-order fields. The
  variation of the whole field under the flow of a vector field xi is D_xi + L_xi h: the displacement of the
  flat field, a -> a.grad xi + grad(xi.a), of order zero in h, plus the Lie variation of h, of order one.
  For the exact boost xi_B = x.B the first part vanishes (the boost with its rotor is a symmetry of the flat
  field). So "omega(delta h, boost variation)" has two different readings:
  (A) xi = the boost NEAR THE CORNER only (any xi with xi = 0 and grad xi = w grad(x.B) on the corner):
      omega(h, D_xi) = 2 E[h](xi) + div K_xi[h], with an explicit bivector potential K (found by exact
      linear algebra, explore1.py; rank 6 of 6, unique). On solutions the flux is a pure boundary term and
      the corner part is -2 w tr_perp(h)/2 ... see K2, K3. This is the first-order corner charge.
  (B) xi = the exact boost: omega(h, L_xi h) is the differential of a QUADRATIC generator, a bulk term
      (the boost energy of the field's own waves), not a corner term. It cannot be exact with a local
      potential (the flux form is nondegenerate on the two transverse trace-free components).

Kill conditions, outcome:

- (K1) FIRES in its literal form for the exact boost acting on first-order fields (reading B): the
  generator from the stored current is bulk and quadratic. It does NOT fire for reading A, which is the
  statement that is true at the order the stored current reaches: computed exactly (dev_c.py): for a
  polynomial vacuum field in a generic gauge (three null plane waves plus a displacement) and
  xi = f g x.B, flux through the window of N+ of omega(h, D_xi) = -613356/875 = -(int g tr_perp h over the
  corner), no bulk remainder; off shell the remainder is exactly 2 int n.E[h](xi). True statement filed.
  The two readings are tied together by the focusing equation (clause (vi) of the entity): the bulk
  quadratic generator equals the second-order area deficit of the corner over 8 pi G.
- (K2) does not fire: at the corner B.K_xi[h] = -w tr_perp h exactly, in every gauge, pointwise
  (dev_b.py; symbolic: K at the corner = grad^h(xi)[on xi] - 1/2 tau grad^xi, and B.(that) = tr_par h - tau).
  tr_perp h = tr h - n.h(nbar) is twice the first-order change of the area density (derived from hb:
  a = |hb^{-1}(e1) ^ hb^{-1}(e2)| = 1 + 1/2 tr_perp h; dev_f.py).
- (K3) does not fire: (1/16 pi G) x (2 delta a) = delta a/(8 pi G). The magnitude 1/(8 pi G) is forced. The
  SIGN depends on orientation and is forced once that is fixed: with the stored orientation (positive null
  energy, generator H of a flow X defined by dH = (1/16 pi G) flux of omega(delta h, X)), the flow along
  xi = w x.B near the corner on the FUTURE half N+ has corner term -(1/8 pi G) int w delta a; on Nbar+ it is
  +(1/8 pi G) int w delta a; a smooth xi through the pair has none; the relative boost (rates w_N, w_Nbar)
  has (1/8 pi G) int (w_Nbar - w_N) delta a.
- (K4) does not fire: the two routes agree exactly. In the gauge h(n) = 0, -B.K = tau - lam d_n tau on N
  (polynomial identity), and the integrated first-order focusing equation gives the same number
  (dev_d.py: both 192 on the sample window). Second order: n.omega(h, L h) on N =
  4 lam (<sigma,sigma> - theta^2/2) - 1/2 d_lam(lam(<h,d_n h> - tau d_n tau)), and the SAME combination
  <sigma,sigma> - theta^2/2 is the source of the focusing equation in area form
  a'' = a(theta^2/2 - <sigma,sigma> + n.R(n)) (checked exactly on a field that is not weak, dev_f.py).
  The opposite sign of the trace in the stored flux (R1 (ii)) is exactly the theta^2/2 of focusing.
- (K5) see clause (vii): the real-GA continuation is the stored one (on values, the rotor of the dual
  plane); I_4 B = e_1 e_2 is the corner plane itself. A first attempt at "the half turn is the identity on
  every symmetric map" was FALSE (dev_g.py): it is the identity on the transverse trace-free components,
  the trace and the n, nbar block, and -1 on the components mixing the corner with n, nbar. The weight
  exp(-+ delta A/(4 G hbar)) is filed as ARGUED only; what is proved is the conditional entropy statement
  (given the imported null-plane modular Hamiltonian Fact and a semiclassical source hypothesis).

Orientation from the prompting paper (arXiv:2611.34924, read on 27 November through WebFetch summaries
only, two partial fetches of the PDF text; not read in full): its boost charge is A/(8 pi G) per corner,
conjugate to the relative boost angle (its eqs. 3.41, 3.43, 3.66 as reported by the summary), trace weight
exp(-A/(4 G hbar)), boost acting on an area eigenstate by exp(i Gamma s/2 pi), s = A/(4 G hbar) (its D.13).
Its bibliography (as reported) has [51] Carlip and Teitelboim, The off-shell black hole, CQG 12 (1995) 1699,
[12] Donnelly and Freidel, JHEP 09 (2016) 102, [25] Chandrasekaran and Flanagan, arXiv:2309.03871. None of
its formulas is used.

### Log entry 2 (27 November, entity filed)

Filed: `store/claims/synthesis.corner-area-variation-of-a-null-plane-pair-is-the-charge-of-the-relative-boost/`
(entity.md, proof-main.tex, check.py; seven check functions). Subject einstein (the subject of the
Clausius entries and of the open problem; the imported Wald Fact sits in subject entropy). Filed against
`op.derive-loc-and-r-loc`.

What is established, clause by clause (labels as in the entity):

- (i) PROVED. omega(h, Delta_xi) = 2 E[h](xi) + div Psi_xi[h] for every first-order field h and every vector
  field xi, Psi = xi^(d - grad tau) - grad^h(xi)[on h] + grad^h(xi)[on xi] - 1/2 tau grad^xi. Hand proof in
  symbols; the check verifies it completely (the difference is linear in h, linear in xi and homogeneous
  quadratic in the two momenta: 10 x 4 x 36 = 1440 evaluations) and shows the coefficients are the only ones
  among the six bivectors with one derivative (rank six).
- (ii) PROVED. At the corner B.Psi = -w tr_perp h for a flow that is w x.B there; any gauge, pointwise.
  tr_perp Delta_zeta = 2 div_perp zeta_perp: unchanged by displacements whose part along the corner vanishes
  on it, changed by a divergence along the corner otherwise. Unchanged by omega -> omega + div Y(h1, h2), Y
  without derivatives.
- (iii) PROVED. Area density a = |hb^{-1}(e1) ^ hb^{-1}(e2)| = 1 + 1/2 tr_perp h + ...; derived from the
  Definition's clause (a), not assumed.
- (iv) PROVED. On solutions, in any gauge, (1/16 pi G) flux through N+ of omega(h, Delta_xi) =
  -(1/8 pi G) int w delta a for xi cut off away from the corner; +(1/8 pi G) int w delta a on Nbar+;
  pair: (1/8 pi G) int (w_Nbar - w_N) delta a. Exact check on a polynomial vacuum field in a generic gauge,
  both half-planes.
- (v) PROVED (given the first-order equation with source of R1 (vi), under its (L), (D), (V), (N)). Exact
  boost: div Psi = -2 E[h](xi_B); on each generator in the gauge h(n) = 0:
  int_0^Lam lam n.T(n) = (1/8 pi G)((da - lam da')(Lam) - da(0)). Two routes (symplectic current; integrated
  first-order focusing equation of R1) agree identically.
- (vi) (a), (b) PROVED; (c) PROVED GIVEN (F) (the null-null component of the field equation, a hypothesis;
  R2 (vii) is named as its source and is not a premise). (a) n.omega(h, L_B h) on N in the gauge =
  4 lam (<sigma,sigma> - theta^2/2) - 1/2 d_lam(...): the quadratic generator of the exact boost is a bulk
  term. (b) theta = d ln a / d lam and a'' = a (theta^2/2 - <sigma,sigma> + n.R(n)) at any field strength in
  the gauge s(n) = 0. (c) exact integrated form and its second order: the second-order area deficit of the
  corner over 8 pi G is the boost-weighted null energy of the two components (trace term included) plus
  matter's. NO check of its own for (c) beyond (a) and (b).
- (vii) (a) PROVED (pinned to synthesis.modular-period-on-values-is-the-dual-plane-turn@5): I_4 B = e_1 e_2,
  the dual of the boost plane is the corner plane; the continued boost is on values the rotor of the corner
  plane. (b) PROVED GIVEN the imported Fact synthesis.imported-null-plane-modular-hamiltonian-first-law@2
  (named as imported) and hypothesis (S) (semiclassical source): Delta S = Delta A/(4G) - S(rho || omega_0).
- The weight exp(-+ delta A/(4 G hbar)): ARGUED only (Reading). Missing step named: that a quantum state
  is thermal at period 2 pi for the whole generator, corner term included. Angle: 2 pi for the density
  operator (the period of the imported Fact), pi for the amplitude (square root). Sign by the sense of the
  boost. First order gives delta A, not A.

What failed or was weaker than hoped:
- K1 fired in its literal form (see log entry 1): the exact boost of first-order fields has a bulk quadratic
  generator from the stored current; the pure corner term belongs to the displacement that is the boost at
  the corner. Both statements filed.
- Only delta A (first order) and the second-order deficit through focusing; nothing on a background of
  nonvanishing field strength; (vi)(c) has no independent exact check (an exact second-order vacuum solution
  in the gauge was not constructed).
- The thermal weight is not derived.
- A false intermediate claim was caught by the check and corrected: the half turn of the dual plane is not the
  identity on every symmetric map (it reverses the components mixing the corner with n, nbar).

Gates (final run, see the report): lint 0 errors 0 warnings; checkone 7 of 7 pass; mutants: every literal of
every function killed (0 survivors).

References appended to store/references.yaml (keys checked absent first): CarlipTeitelboim1995,
DonnellyFreidel2016, AbbottDeser1982.

Cited from memory (flag for the maintainer):
- Carlip and Teitelboim 1995: title, journal, volume, year, first page confirmed from the prompting paper's
  bibliography as extracted by the fetch tool and by a web search listing arXiv gr-qc/9312002; the last page
  (1704) and the DOI (10.1088/0264-9381/12/7/011) are from memory.
- Donnelly and Freidel 2016: JHEP 09 (2016) 102 confirmed from the same bibliography; arXiv:1601.04744 from
  memory; DOI is the journal's pattern.
- Abbott and Deser 1982: title confirmed by web search; Nucl. Phys. B 195, pages 76-96 and the DOI from
  memory. That its superpotential is the potential of clause (i) for a Killing field is stated from memory.
- Wald 1993, Iyer and Wald 1994, Bisognano and Wichmann 1976, Unruh 1976 (keys already in the store),
  Wald 1994 (book), Gao and Wald 2001, Jacobson 1995: from memory, not read for this entity.
- The prompting paper: abstract and two partial text extractions only.

Unexpected links:
- The opposite sign of the trace in the stored null-plane flux (R1 (ii), where it "never enters") is exactly
  the theta^2/2 of the focusing equation in area form: the quadratic boost generator density
  <sigma,sigma> - theta^2/2 is the source of a''/a. A structural agreement between R1 (ii) and R1 (iii) at
  second order that R1 does not state.
- I_4 B = e_1 e_2: the dual of the boost plane is the corner plane, so the stored "dual-plane turn" of the
  modular period is the rotation of the corner in itself.
- Overlap with `shear` (area density rho^2, its linear equation) and with `stress` (n.G2(n) in the gauge):
  clause (vi)(b) should be re-pinned to the any-strength entry when it lands; (vi)(c) is the integrated,
  boost-weighted companion of `stress` prediction 5 (agreement after integration along a generator).

Decisions for Leon:
1. Whether users of clause (b) of the imported Wald Fact for the Einstein functional at first order cite
   clause (iv) here.
2. Whether op.derive-loc-and-r-loc takes an attack item: the corner charge on a background of nonvanishing
   field strength (needs the second-order symplectic current), the form of the curvature clause this route
   could reach.
3. Hypothesis (S) (semiclassical source) and the argued weight: register, keep local, or drop the Reading.
4. Sign convention of clause (iv) (relative boost named so that its generator is +delta A/8 pi G).
5. Re-pin (vi)(b) to the any-strength null-surface entry once stored.
6. DOIs and last pages of the three appended references to be verified (appended entries cannot be
   rewritten under the run's rules).

### Log entry 3 (27 November, final gates)

- `python -m tp.lint <id> --store store`: 0 error(s), 0 warning(s), 7 info (the pass times), exit 0.
- `python -m tp.checkone <id> --store store`: all 7 checks passed.
- `python -m tp.mutants <id> --store store`: every function "0 of 8 sampled perturbations survive ... ok",
  exit 0; with `--every`: 0 survivors of 17, 11, 17, 26, 30, 36, 37 literals. ("killed by an exception, not
  an assert" is the tool's label for a GA.check failure; spot-checked: the kills are GA.check failures, with
  two IndexErrors per function from perturbed slices.)
- Added after log entry 2: the flux through Nbar+ for the same vacuum field (exactly +2 int g delta a; the
  pair sums to zero for one smooth flow), the invariance of the flux form under the boost variation, and the
  number of clause (vii)(b) on a window (2 pi K = Delta A/4G with a polynomial source). The field-equation
  theorem R2 was removed from `uses`: hypothesis (F) is stated as a hypothesis, R2 named as its source only.
- Status: complete. Next step for the run: referee; for the problem: decision 2 above (corner charge on a
  background of nonvanishing field strength).

## Fix round (27 November, after the blind referee's SOUND WITH FIXES; report in findings/referee-corner.md)

All thirteen required fixes applied in entity.md (and proof-main.tex where the proof said the same thing).

1. Preamble: the referee's sentence on clause (f), (F) and R1 (vi) with (L), (D), (V), (N), verbatim; placed
   after the sentence that names the first-order theorem, so that the name is defined before it is used.
2. Label of (v) as specified; the magnitude sentence of (iv) as specified.
3. "Fluxes and generators": the pair's generator is DEFINED as the sum over its two halves (light-front
   setting, not proved). (iv): "the part of the generator linear in h is H = ..."; the two added sentences
   (relative boost near C and identity away from it; for the exact boost of both halves the linear part
   vanishes identically and the corner term enters only through the balance of (v)). The proof of (iv) says
   the same, and that the terms of first order in h give the quadratic part of (vi)(a).
4. One-liner: both replacements as specified. Also corrected there "is -tr_perp h, twice the change" to
   "minus twice" (my own slip, not in the report).
5. Reading: replaced as specified, with one change for consistency with fix 6: "the boost energy of matter at
   first order and, given (F), the quadratic boost generator of the field at second order".
6. (vi) heading; the added sentence in (a) (not positive definite unless theta = 0; theta constant along
   generators on vacuum fields in the gauge); (vi)(c) last sentence, the technical level, the lay sentence
   (as specified) and the extraction note no longer say "boost energy of the field's own two components".
   The check function was renamed (...is_the_quadratic_boost_generator) and now exhibits a gauge field for
   which the form is negative while the part of the two components is positive.
7. Extraction note and Reading: "independent of the gauge up to a divergence along the corner under
   displacements along it (clause (ii))".
8. Extraction note: "pin no imported Fact" for clauses (i) to (vi) (the one pinned imported Fact, the modular
   first law, is named in the sentence before as pinned by (vii)(b)); the past-cone paragraph as specified.
   I walked the cone myself (268 entities, 46 with status imported): the Wald Fact is not in it; the
   field-equation Facts are, through the two-free-directions result, the first-order theorem AND the
   dual-plane theorem (added to the referee's two paths), so the rotor identities of the dual-plane theorem
   are added to the list of clauses used, with the remark that they and the kernel at null momentum are
   recomputed in the check.
9. (vii)(b): "half a period gives 1/8G" moved to the Reading's paragraph on the weight; the entropy sentence
   restated as specified; (S) stated in full as specified (with K written out).
10. Source paragraph: "by exp(-A/4G hbar)".
11. Abbott and Deser: "plays ... the role of ... (not compared term by term here)".
12. Lay level: "the area at the far end, as it would be if continued back along the light rays to the corner,
    less the area at the corner". The first lay outcome now says the sliding is done near the corner and fades
    out away from it (same qualifier as fix 3).
13. Technical level: "the second-order area combination of (v) (the far cut continued back, less the corner)
    over 8 pi G, given the null-null field equation at second order"; the paragraph on the corner term now
    carries the qualifiers of fix 3; the entropy sentence matches fix 9.

Optional suggestions applied.
- Title: "First-order corner charge of the boost on a null-plane pair: area variation over $8\pi G$" (89
  characters). Id and folder unchanged.
- (i): the six bivectors span the rotor-covariant, reflection-even bivectors bilinear in h and xi with one
  derivative. Made a computed statement, not a remark: new check function counts the forms annihilated by the
  six unit bivectors (960 coefficients, nullity six modulo a prime), exhibits six independent ones (the three
  built with the product and their duals) and shows the three are the ones carried along by a reflection.
  Proof paragraph added.
- (vi)(c): h = 2 s_1, sigma and theta the coefficients of epsilon.
- Vacuous comparisons removed: `coef == COEF` replaced by solving the rank-six system for the six
  coefficients and asserting the solution 1, -1, -1, 1, -1/2, 0; `(gb - g) == 0` removed (one weight
  function is used by both cut-offs).
- check (vii): the (b) part and `premise(MODULAR)` taken out of the function for (a). (b) has its own
  function, which forms the Fact's modular Hamiltonian 2 pi K(u_0), K(u_0) = int (u - u_0) n.T(n) beyond the
  cut, for a polynomial source about TWO cuts (u_0 = 0 and 1/2) and compares with the area combination about
  the cut over 4 G; the redundant second comparison is gone; the label and the proof say that only the first
  law about a cut and the factor 2 pi/(8 pi G) are computed and nothing thermal. To make that true of the
  statement, (v) now says the first law holds about any cut of N (one line, with its proof). The imported
  Fact stays pinned in `uses`: (vii)(b) rests on it.
- Carlip and Teitelboim: "the Euclidean opening angle at the horizon".
- Units: a sentence in the Reading says hbar is restored there and in the source paragraph.
- Check (iv): a second function with a vacuum solution found by exact elimination (generic homogeneous
  quadratic field less a combination with the same image under E; not a displacement, not in the gauge):
  flux = -2 int g delta a exactly (area = -117/350); the off-shell remainder moved there.

Declined.
- An exact check of (vi)(c): not cheap (needs an exact second-order solution in the gauge, or jets in the
  expansion parameter as a fifth label, which lib/gtg.py's Field does not take). The clause and the proof now
  say that (c) has no separate check and follows from (a) and (b).
- The `shear` entity is not pinned (not stored); it is named in the extraction note as the general form of
  (vi)(b), with the same signs (a = rho^2).

Not touched: store/references.yaml; no git commands.

Gates after the fix round: lint 0 error(s), 0 warning(s), 10 info (pass times, all under 1.2 s); checkone
all 10 checks passed; mutants 0 of 8 sampled survive in each of the 10 functions (exit 0); with --every, no
literal survives in any function (19, 8, 11, 17, 17, 13, 30, 36, 22, 11 literals).
