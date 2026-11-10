# attack-QB: cluster Q, items Q2 and Q3 (constructive), adversarial on QA's Q1

Labels: proved / computed / argued / conjectured. Work files: colony/runs/2026-11-10-phase3/work/QB/.

## Orientation (direct lookups)
- Stored curved-field result: synthesis.vacuum-polarisation-kernel-on-a-gravitational-field-has-the-flat-leading-part-and-no-weyl-term-of-degree-four (v1).
  Clauses (i), (ii) proved ((ii) given the protraction identity as a hypothesis); (iii), (iv) argued.
- The imported Fact: synthesis.imported-local-covariance-with-scaling-of-time-ordered-products (v1), clause (iii):
  the difference of two local, covariant, almost homogeneously scaling extensions of a kernel with omega = 2 has,
  at a derivative of delta of order j, a constant-coefficient polynomial in the curvature operator, its derivatives
  and the mass of dimension 2 - j. Not in the Fact: the Ward identity on the field; the value of any constant.
- Flat theorem: synthesis.one-loop-vacuum-polarisation-extends-...-renormalisation-constants (v4), clause (v) argued.
- Protraction identity d_a ^ calR(a ^ b) = 0. Assumed, never derived, in: the curved-field kernel result (clause
  (ii), stated hypothesis); the checks of correspondence.no-real-lorentzian-vacuum-half-flat,
  interior.filtration-cauchy-horizon-read-literature and
  synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared (imposed as a condition defining algebraic
  Weyl maps); pairing.loop-classes-are-weyl-components (pair symmetry cited "as a consequence of the first Bianchi
  identity" through the imported dictionary clause (iv)). docs/ALGEBRA_CORE.md does not contain it. The open problem
  op.qft-loops-and-renormalisation has an attack item asking for it. In the sense of "stored under another name":
  the imported dictionary Fact (synthesis.imported-gtg-dictionary, clause (iv)) reads calR as the Riemann tensor of
  the derived metric, so the identity is implied by an import plus a classical theorem; it is not derived in store.
- Tooling: lib/gtg.py has Field with solve_omega (torsion-free Omega from hb, exact jets), strength, curvature.

## Q3: the protraction identity from vanishing torsion
Routes.
1. (chosen) Coframe route in GA: torsion-free means D ^ g^mu = 0 for the coframe g^mu = hb^T(e^mu). Apply D ^ again,
   use [D_a, D_b] M = R(a ^ b) x M (definition clause (c)), then pure algebra. Delivers the identity in every
   dimension and signature; needs only clauses (b), (c), (f) of the definition.
2. Import route: read calR as the Riemann tensor of the derived metric through the dictionary Fact, clause (iv), and
   quote the classical first Bianchi identity. Delivers nothing new; this is how the store uses it today.
3. Frame route: D_mu g_nu = D_nu g_mu, cyclic sum of the commutator gives the cyclic vector identity, then pair
   symmetry, then protraction. Longer; its end point (the cyclic vector identity) is kept as a clause and checked.
Kill conditions (pre-registered before computing):
- K3a. A torsion-free sample field with d_a ^ calR(a ^ b) != 0. DID NOT FIRE (six fields, exact).
- K3b. A sample with torsion on which the identity still holds for generic data (then the derivation from torsion
  would be empty). DID NOT FIRE: with torsion the protraction is nonzero, and equals what clause (ii) predicts.
- K3c. The proof needs an input outside the definition (pair symmetry assumed, a metric reading). DID NOT FIRE: the
  proof uses the Leibniz rule, the commutator of clause (c) and a grade count; pair symmetry is an output.

Established (proposal synthesis.protraction-identity-of-the-curvature-operator-from-vanishing-torsion):
- (i) proved, every bivector map M, every dimension and signature: with P(c) = d_a ^ M(a ^ c) (protraction),
  C(c) = d_b ^ d_a ^ (M(a ^ b) . c) (cyclic trivector), E = d_c ^ P(c): C(c) = 2 P(c) - c . E, d_c ^ C(c) = -2 E,
  so P(c) = C(c)/2 - c . (d_e ^ C(e))/4. Complete check in four dimensions (two signatures), sample in five.
- (ii) proved, every field (torsion allowed): C_calR(g^mu)/2 = D ^ Theta^mu - Theta^nu ^ D_nu g^mu, Theta^mu the
  torsion bivectors. Exact on two polynomial fields with torsion.
- (iii) proved: torsion-free implies d_a ^ calR(a ^ b) = 0, the cyclic vector identity, and
  d_a calR(a ^ b) = calR(b). Exact on four polynomial coframes with Omega solved from the torsion equation
  (signatures (1,3), (1,2), (2,2)) and on the library's Schwarzschild and de Sitter fields.
- (iv) computed (d = 3, 4, 5): kernel of the protraction has dimension d^2 (d^2 - 1)/12 and lies in the symmetric
  maps; B -> I B is symmetric with protraction -3 I c. General d: classical, cited.
- Candour: this is the classical first Bianchi identity and the route is that of Lasenby, Doran and Gull 1998,
  Section 5, eqs. (5.1) to (5.6) (checked on the web against the arXiv text gr-qc/0405033 through a text tool).
  New only: the form with torsion (ii), the explicit inversion (i), the rank computations. Transport-absent.
- Gate: check4 exit 0, no findings; validate ok, no E or W.

## Q2: local covariance and the freedom of the curved-field extension
Routes.
1. (chosen) Classify exactly the terms the Fact's clause (iii) allows for the vacuum-polarisation kernel (two vector
   slots, omega = 2): invariant theory as exact linear algebra on the Lorentz algebra acting through GA, then
   transversality on the DIFFERENCE of two Ward-preserving extensions, with exact covariant calculus on a
   torsion-free sample field.
2. Import the curved-field Ward identity as well. Maintainer-only; listed as a decision.
3. Lift clause (iv) of the stored entity by a corrected version. Rejected: the clause also rests on the argued
   degree count; a new conditional result is cleaner and the entity update is a maintainer decision.
Kill conditions (pre-registered):
- K2a. The space of local covariant terms is not what the stored text expects, or the Weyl part can enter.
  DID NOT FIRE: 2 terms at order 2, 0 at order 1, 3 at order 0 (m^2, scalar curvature, Ricci map); Weyl: 0.
- K2b. The transverse subspace has dimension different from 1. DID NOT FIRE: exactly (1, -1, 0, 0, 1).
- K2c. Closing the clause needs an input the Fact does not supply. FIRED, as expected, for EXISTENCE: see below.

Which clause, exactly: the last sentence of clause (iv) of the stored curved-field result, "That the Ward identity on
the field then leaves the single constant Z_3 is argued and not derived here", and with it the last half-sentence
of clause (v) of the flat theorem ("the further ambiguities being local terms in the field strength of matching
dimension").
What the Fact supplies: (a) the coefficients are constants, not functions of the point; (b) each coefficient is a
polynomial in calR, its derivatives and m of dimension 2 - j. Nothing else.
What is derived from that (proposal
synthesis.curved-field-vacuum-polarisation-freedom-is-five-local-covariant-constants-of-which-one-is-transverse):
- (i) proved given the Fact's form and the protraction identity (hypothesis there, since a proposal cannot cite a
  proposal): the difference of two local covariant extensions is c1 Lap + c2 D(D.) + c3 m^2 + c4 calR_0 + c5 calR(.)
  on vector fields: FIVE constants in place of 15 functions per index pair. Counts by exact rank under the Lorentz
  algebra: invariants of 3 vector slots 0, of 4 vector slots 4 (2 symmetric in the derivative pair), bilinear forms
  linear in a bivector map 6 / 3 on symmetric maps / 2 under protraction / 0 on Weyl type. So no Weyl term and no
  parity-odd term can occur in the freedom.
- (ii) proved: D.(D ^ A) = Lap A - D(D.A) + calR(A) in the store's sign (exact on a sample field; the opposite
  sign fails); transversality K(D chi) = 0 on all torsion-free fields and masses holds exactly for
  c (1, -1, 0, 0, 1): K A = c D.(D ^ A). ONE constant, the flat Z_3; photon mass and the two curvature couplings
  excluded, the Ricci coefficient fixed.
- (iii) proved given the two imported Facts and omega = 2: two transverse local covariant extensions differ by
  that one constant, the same on all torsion-free fields.
- (iv) argued: existence of a transverse extension, under two suppositions not in the store (the divergence of a
  local covariant extension is itself of the Fact's local form at dimension 3; the kernel is symmetric): five
  candidate anomaly terms, four removable by the freedom, the fifth (D calR_0) chi excluded by symmetry.
What stays open in the stored clause (so it is NOT lifted to proved as a whole):
- omega = 2 on the field is argued on the imported scaling-degree rules (clause (vi) of the extension Fact);
- existence of a Ward-preserving local covariant extension (needs the literature's Ward identity on a
  gravitational field: Hollands 2008 for gauge theories, Zahn 2012 for the Dirac current);
- the Fact is from memory and sourced for a scalar field; the Dirac current is the less well sourced part;
- the stored kernel is the parametrix trace, not a state's current two-point function.
A correction to the stored entity's own note: the first Hadamard transport equation is NOT needed for the count of
the freedom (it enters only the coefficients at degree four, clause (iii)), so the reduction to Z_3 does not wait
for it.
Web checks (10 November 2026, arXiv abstract pages through a text tool): Hollands and Wald gr-qc/0103074 (title,
authors, DOI 10.1007/s002200100540; uniqueness up to finitely many parameters, the Minkowski ones plus curvature
couplings; "continuity under variations of the metric" in the abstract, the Fact says smooth or analytic
dependence); gr-qc/0111108 (existence; scaling expansion in polynomials of the curvature times Lorentz-invariant
distributions; DOI 10.1007/s00220-002-0719-y); both scalar field only. Volumes and pages were not shown on the pages
read, so the Fact's "223 (2001) 289-326" and "231 (2002) 309-345" remain unverified. J. Zahn, The renormalized
locally covariant Dirac field, arXiv:1210.4031 (DOI 10.1142/S0129055X13300124): Wick powers and time-ordered
products of the locally covariant Dirac field in gauge backgrounds, current conserved, remaining freedom
characterised: the natural source for the Dirac part of the Fact; not imported.
Gate: see "Proposals filed".

## Adversarial on Q1 (QA's proposal
synthesis.one-loop-self-energy-and-vertex-extend-with-the-ward-identity-holding-at-a-common-cut-off-length)
Read: the proposal's entity, proof, coverage (QA's findings file was behind its proposal).
1. Is the Ward identity checked or imposed? It is derived in the proof (Step 5: Fubini, then Steps 2 and 3), and
   NOT computed by the check: no eight-dimensional pairing is evaluated; the check covers the chain-rule
   bookkeeping, the scale derivatives and the zero-transfer form. The coverage file says so. Not imposed by a
   constant, but it is built in by the choice of subtraction region (the cylinder Q(u+v) < l^2 in place of a ball
   of R^8): relative to a generic extension that choice is one finite renormalisation. The proposal says this in
   clause (iii); the lay level's "with nothing adjusted" is fair only with that reading.
2. Independent recomputation (my own route, radial integrals by hand, no polynomial bumps):
   - Step 3, m = 0: the only rotation-covariant candidates of degree -2 linear in n are alpha (n.w) w/s^2 + beta n/s;
     applying the vector derivative gives alpha = 1/(2 pi^2), beta = 0. Agrees.
   - [1/s^2]_1 = -(1/4) Lap(ln s/s) + pi^2 delta: for radial phi, -(1/4) int (ln s/s) Lap phi = 2 pi^2 J - pi^2 phi(0),
     J = int_0^inf (phi - theta(1 - r) phi(0)) dr/r. Agrees.
   - [w/s^3]_1 = (1/16) grad Lap(ln s/s) - (3 pi^2/8) grad delta: on g = w_b phi(s) the right side is the left
     minus (3 pi^2/8) delta_ab phi(0). Agrees. Hence ln M^2 = 1 and 3/2 and the ratio 1/2 (ln(M_Sigma/M_V) = 1/4).
   - The photon kernel in the covariant gauge: Fourier transform of k_a k_b/k^4 is
     (1/(8 pi^2))(delta_ab/s - 2 w_a w_b/s^2), giving QA's D_w. Agrees; so -2 xi and 3 + xi stand.
3. Gauge parameter: the identity holds for every xi because only the dependence of the photon kernel on w = u + v
   is used; every constant is xi-dependent (leading self-energy proportional to xi, zero in Landau gauge at m = 0).
   No gauge-independence is claimed and none holds for these constants. No defect.
4. Infrared: no regulator is hidden. But the subtraction is over a region that is unbounded in the position of
   the photon vertex, and its convergence is the decay |t|^-6 of the Euclidean kernel. That is a Euclidean fact.
5. The one substantive scope point (for QA and the referees): everything is on the Euclidean section. For the
   two-point kernels of the stored result the passage to Feynman distributions is a statement about functions of
   one vector. For the vertex, the cut-off region Q(u+v) < l^2 is not bounded in Lorentzian signature and the
   construction does not transfer as written; the Ward identity for the time-ordered Lorentzian extensions
   follows only through the continuation of the Euclidean distributions, which the proposal lists as "not
   covered". So "for these two kernels at one loop the existence imported (Scharf) is proved here" should read
   "on the Euclidean section"; Scharf's statement is about causal (Lorentzian) time-ordered products and the
   import should stay for that. The one-liner has the scope; clause (vi), the technical and the lay level should
   carry it too.
6. Does the GA form add anything? No, and the proposal says so itself. Vectors of Cl(4,0), no matrix, no unit.
Verdict as sibling adversary: no error found; one scope restatement (item 5); the Ward identity is proof-only
evidence (item 1).
No overlap with my proposals (Q1 is flat, Euclidean, self-energy and vertex; mine are the curved-field freedom of
the vacuum polarisation and the Bianchi identity).

## Proposals filed (2 of 3 allowed)
1. synthesis.protraction-identity-of-the-curvature-operator-from-vanishing-torsion (Q3). check4 exit 0, no
   findings; validate ok, no E or W; registered (accepted_for_review true); coverage.yaml copied.
2. synthesis.curved-field-vacuum-polarisation-freedom-is-five-local-covariant-constants-of-which-one-is-transverse
   (Q2). check4 exit 0, two I405 infos (declared premises untouched, with reasons in coverage.yaml); validate ok,
   no E or W; registered; coverage.yaml copied. It states the protraction identity as a hypothesis (a proposal
   cannot cite a proposal); proposal 1 is the intended citation.
Not filed: nothing on Q1 (QA's). No corrected version of the stored curved-field entity (maintainer decision 1).

## Unexpected links
- Protraction identity and the renormalisation freedom (Q3 into Q2): the identity is what removes a third
  curvature term from the freedom. On symmetric bivector maps there are three invariant bilinear forms; the third
  is the pseudoscalar trace (the E of Q3's clause (i), dual to a scalar) times a.b, a parity-odd coupling. It
  vanishes exactly because the curvature operator of a torsion-free field has vanishing protraction. With torsion
  (Einstein-Cartan, which the definition's clause (f) allows for spinning matter) the count is larger: up to six
  curvature-linear terms, and D ^ D chi != 0, so transversality itself changes form. The Dirac field sources
  torsion in the stored definition; the stored curved-field kernel assumes it away. This is a real scope line for
  the QFT-on-a-gravitational-field results, not only a convenience.
- No Weyl term in the freedom (Q2) matches the stored clause (iii) "no Weyl term at degree four" from a different
  direction: there it is a property of the parametrix, here of the invariant theory. The two are independent
  statements that agree.
- For the bridge-hunter's list: the count "20 = dimension of algebraic curvature maps = kernel of the protraction"
  is the same linear algebra the dark-energy and frozen-point results use when they impose the first Bianchi
  identity on Weyl maps (11 against 10 dimensions in the note of
  synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared: the eleventh is B -> I B).

## Decisions for Leon
1. After acceptance, update the stored curved-field result
   (synthesis.vacuum-polarisation-kernel-on-a-gravitational-field-...-degree-four, clauses (ii) and (iv), and its
   note) and clause (v) of the flat theorem: (a) the protraction identity becomes a cited theorem, not a hypothesis;
   (b) the sentence "that the Ward identity then leaves the single constant Z_3 is argued and not derived" becomes
   "two transverse local covariant extensions differ by Z_3 (cited); existence of one is not proved"; (c) the note's
   list of what the reduction waits for drops the first Hadamard transport equation. Recommendation: yes to all
   three; clause (iv) stays argued as a whole because omega = 2 and existence are not proved.
2. Repoint the entities that impose or assume the first Bianchi identity to the new result (the three checks that
   define algebraic Weyl maps, and pairing.loop-classes-are-weyl-components for the pair symmetry; in four
   dimensions the pair symmetry is now computed in store, in general dimension still classical). Recommendation:
   yes, as citations only; no statement changes.
3. Existence of a Ward-preserving local covariant extension on a gravitational field: import it (a new clause of
   the local-covariance Fact or a new Fact: "the divergence of a local covariant time-ordered product of conserved
   currents is a local covariant term, removable by a finite renormalisation"; sources Hollands 2008, already cited
   by the extension Fact's clause (v), and Zahn 2012 arXiv:1210.4031 for the Dirac current), or leave it open.
   With that import clause (iv) of proposal 2 becomes a proof and the curved-field clause closes up to omega = 2.
   Recommendation: import, with the source checked against the paper, not from memory.
4. The local-covariance Fact's bibliography and wording: add Zahn (arXiv:1210.4031) as the source for the Dirac
   field, which the Fact calls its less well sourced part; replace "smooth, in a second form analytic, dependence"
   by what the 2001 abstract says ("continuity under variations of the metric") unless the paper is read; the
   volumes and pages remain unverified (the arXiv pages show only DOIs). Recommendation: yes.
5. Torsion scope: the definition lets the Dirac field source torsion, and with torsion both proposals' conclusions
   change (protraction nonzero by an exact formula; more curvature terms in the freedom; D ^ D chi != 0). Decide
   whether QFT-on-a-gravitational-field results in the store are stated on torsion-free fields by standing
   convention (then say so once, in the conventions), or whether the torsion case is an open item under
   op.qft-loops-and-renormalisation. Recommendation: record it as an open attack item; at one loop on a fixed
   background the torsion sourced by the loop's own field is higher order.
6. On QA's Q1 proposal: keep the Scharf import for the Lorentzian (causal) statement; QA's result removes the need
   for it only on the Euclidean section at one loop. Ask QA to carry "on the Euclidean section" into clause (vi),
   the technical and the lay level (my adversarial item 5).
7. Whether docs/ALGEBRA_CORE.md should gain a line for the protraction identity (the RUN item says "derived in
   the algebra core"): the result is filed as a claim about the definition object, with no premises; adding it to
   the core document is a maintainer edit. Recommendation: one line with the claim id.
