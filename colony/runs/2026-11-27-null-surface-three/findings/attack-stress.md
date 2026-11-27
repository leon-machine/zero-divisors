# attack-stress: the second-order stress of the first-order gravitational field

Run 2026-11-27-null-surface-three, attacker `stress`. Target: a new stored result filed against
`op.einstein-from-the-field-theory`, extending R1
(`synthesis.null-plane-data-of-the-first-order-gravitational-field-are-the-shear-of-the-generators`) and R2
(`synthesis.field-equation-linear-in-the-curvature-with-a-conserved-source-is-einsteins`).

## Pre-registration (written before any computation)

Setting: hb = id + eps H1 + eps^2 H2 + ..., Omega fixed by the torsion equation, Einstein map of the stored
definition expanded as G = eps G1[H1] + eps^2 (G1[H2] + G2[H1,H1]) + ... on the constant physical frame.

Kill conditions:

- (K1) The flat divergence of G2[H1,H1] fails to vanish on an exact first-order solution (G1[H1] = 0) in exact
  arithmetic. If it fires, a stored entry is wrong (R2 clause (iii), or the first-order map): stop, locate the
  discrepancy, report, do not file.
- (K2) The change of G2[H1,H1] under a first-order displacement, or under a first-order rotation gauge change,
  on solutions, is NOT of the form G1[X] with X an explicit quadratic field. If it fires, file the true gauge
  behaviour instead.
- (K3, added by me) The null-null component n.G2(n) in the gauge h(n) = 0 does not equal
  <sigma, sigma> + (terms that are total derivatives along the generator or vanish on solutions). If it fires,
  the Reading of R1 ("the two components gravitate through their null energy as matter does") is wrong as
  stated and that is what gets reported.

Predictions written down before computing (from the structure, to be confirmed or refuted by exact arithmetic):

1. Sign and constant. The stored equation is G(a) = -8 pi G T(a) (R2 (vii), Lambda = 0). At second order
   G1[H2] = -8 pi G (T2 + t) with t = + G2[H1,H1]/(8 pi G). The orchestrator's sign (minus) is predicted wrong
   for the store's convention.
2. Off solutions: div_flat G2 (C) = -[ grad-dot . H1(G1-dot(C)) + G1(C) . w + C . (Omega1(d_a) . G1(a)) ],
   w = d_a . Omega1(a), from div G = 0 at order eps^2.
3. G2[H1,H1] is symmetric identically (not only on solutions), because the Ricci map of every torsion-free
   field is symmetric (R2 (ii)). No antisymmetric part, in any rotation gauge.
4. Displacement x -> x + eps xi: H1 -> H1 - xi_ (xi_(a) = a.grad xi) and
   G2[H1 - xi_] = G2[H1] + (xi.grad) G1[H1] - G1[(xi.grad)H1 - xi_ H1 + xi_ xi_]; on solutions the change is
   G1[X], X = -(xi.grad)H1 + xi_ H1 - xi_ xi_. Rotation U = exp(eps B/2): H1 -> H1 + beta (beta(a) = a.B),
   G2[H1 + beta] = G2[H1] - G1[H1 beta + beta beta/2] + [G1[H1], beta]; on solutions the change is G1[X_rot].
   The same holds for a change of second-order parametrisation. So t is NOT locally invariant.
5. In the gauge H1 symmetric, H1(n) = 0 (h = -2 H1, h(n) = 0):
   n.G2(n) = <sigma, sigma> + theta^2/2 + (1/8) d_n^2 <h, h> in the parametrisation hb = id + eps H1 + ...,
   and <sigma, sigma> + theta^2/2 - (1/8) d_n^2 <h, h> in the parametrisation hb^{-1} = id + eps s1 + ...;
   pointwise equal to <sigma, sigma> + theta^2/2 only in the exponential parametrisation hb^{-1} = exp(u).
   So agreement with R1's density is NOT pointwise in general; it holds after integration along a generator.

## Routes considered

- Route A (chosen): structural. Expand the stored identities (R2 (ii), (iii); Definition clause (e)) to second
  order; every clause is then a consequence of a stored statement, and G2 never has to be written out. Exact
  checks compute G2 from the gauge fields with eps carried as a truncated polynomial.
- Route B: write G2[H1,H1] out in GA by hand (Omega to second order from the torsion equation) and verify each
  property term by term. Delivers a closed formula; long, error-prone, and adds nothing to the proofs. Used
  only for the hand cross-check of one component (the null-null one, via the stored focusing equation).
- Route C: Noether route (canonical stress of the quadratic functional of R1 (vi), then Belinfante-type
  improvement). Would give a t that differs from G2/(8 pi G) by superpotential terms; needs the functional,
  hypothesis (V); not needed. Not pursued.

## Store search (done before proving)

Searched `search_claims` for: gravitational stress pseudotensor; second order gravitational field
self-coupling; Noether current of the gravitational field; energy of gravitational waves; superpotential.
Grepped store/claims ids for stress, pseudo, second-order, self-coupl, gravitat, noether, einstein, bianchi.
No stored result treats the quadratic part of the Einstein map, a gravitational stress, a pseudotensor, a
superpotential or the self-coupling. Nearest entries, none a duplicate:

- R1 clause (vi) and its Reading: the null energy (1/8 pi G) int <sigma, sigma> as the generator of null
  translations of the first-order symplectic form, and the remark (argued) that it stands beside the
  matter's null energy in the focusing equation. The present result turns that remark into a statement
  about the second-order field equation and says in which sense it is and is not pointwise.
- R2 clauses (ii), (iii), (vii): symmetric Ricci map, div G = 0, the equation G = -8 pi G T. Used as premises.
- `synthesis.vacuum-field-stress-tensor-is-einstein-tensor-or-trace` (v3): a first-order vacuum-field tensor
  built affinely from the Schouten classes is -G/(8 pi G) + c g or pure trace. Different object (affine in
  the curvature at a point); not used; mentioned in the extraction note as the neighbouring statement.
- `synthesis.imported-einstein-cartan-matter-coupling` (v1): imported frame equation; not used (R2 replaces it).
- `synthesis.weyl-flat-variations-...-trace-free-channel` (v1): stored first-order curvature R_p[h] and the
  response of matter; pinned for the stored first-order curvature formula.
- `op.einstein-from-the-field-theory`: the whole-stress clause is "a clause of the routes"; nothing in the
  store addresses the field's own stress.

## Outcomes (exact arithmetic, scripts in work/stress/)

Engine (`engine.py`): eps carried as a truncated polynomial (class Eps, modulo eps^3) in the coefficients of
gtg jets; Omega solved explicitly from the torsion equation in the frame (needs only a matrix inverse that is
a unit modulo eps); `gtg.Field`, `curvature_jet`, `ricci` do the rest. `torsion_free()` holds on every field.

- K1 did NOT fire. On two generic first-order vacuum solutions (three superposed null polynomial waves with
  transverse trace-free polarisations, plus a generic polynomial displacement, plus a generic polynomial
  rotation gauge; H1 not symmetric) G1[H1] = 0 as a jet and the flat divergence of G2[H1,H1] is exactly zero in
  all four components, with all 16 entries of G2 nonzero (`sol.py`).
- Prediction 2 (divergence off solutions) holds exactly on generic non-solutions (`t2.py`).
- Prediction 3 holds: G2 is symmetric identically, on and off solutions, H1 not symmetric (`t1.py`, `sol.py`).
- K2 did NOT fire. Both laws of prediction 4 hold exactly, off and on solutions, with the change nonzero in
  all 16 entries (`t3.py`): t is not locally gauge invariant; its change on solutions is G1[X].
- K3 did NOT fire. Prediction 5 holds exactly on generic light-cone-gauge solutions (four null waves with
  n.p != 0 and a residual displacement giving theta != 0), in the three parametrisations (`t4.py`). In the
  second sample the null-null component is NEGATIVE in the hb and hb^{-1} parametrisations: the density is
  not even of one sign pointwise except in the exponential parametrisation.
- Plane wave (`t5.py`): for h = f+(nbar.x) eps+ + fx(nbar.x) epsx the whole G2 is
  1/4 (<h',h'> + c <h,h>'') (a.k) k, k = nbar, c = +1/2 (hb = id + eps H1), -1/2 (hb^{-1} = id + eps s),
  0 (exponential). With c = 0 this is Isaacson's effective stress (1/32 pi G) <h',h'> k k without averaging.
- Dust (`t6.py`, `t7.py`): dust at rest with density rho0 = Laplacian(phi)/kappa in its own first-order field,
  moved by the geodesic equation at first order (d_t v1 = -Omega1(e0).e0 = -1/2 grad phi, Newton's law) and
  the continuity equation at second order. flat div T2 is nonzero (the force), flat div (T2 + G2/kappa) = 0
  exactly; also after a generic displacement and rotation gauge change (H1 not symmetric, all four components
  of flat div T2 nonzero).

Sign and constant (prediction 1): t = + G2[H1,H1]/(8 pi G) in the store's convention G = -8 pi G T. The
orchestrator's minus sign is the convention G = +8 pi G T of the literature; the store's is the opposite.

## Filed

`store/claims/synthesis.second-order-stress-of-the-first-order-gravitational-field/` (entity.md, proof-main.tex,
check.py), version 1, subject einstein, filed against `op.einstein-from-the-field-theory`.
Premises pinned: R1@1, R2@1, `synthesis.weyl-flat-variations-...-trace-free-channel`@1 (for the stored
first-order curvature the checks build the stored Einstein map from). `about:` the stored definition.

Setting: hb_eps = id + eps H1 + eps^2 H2, H1 and H2 not assumed symmetric, Omega from the torsion equation;
G_eps = eps G1[H1] + eps^2 (G1[H2] + G2[H1]) + O(eps^3); t = G2[H1]/(8 pi G) (store sign: G = -8 pi G T).
The field equation of clause (f) of the definition is not used; it enters clause (viii) as hypothesis (M1).

What is established, clause by clause:

- (i) proved. G1[H1] = E[h], h = -(H1 + H1^T); Omega1(a) = grad ^ S(a) - (a.grad) A (S symmetric part, A the
  bivector of the antisymmetric part). G1 does not see A. Check: against the stored G_p[h0] built from the
  stored curvature, with and without an antisymmetric part.
- (ii) proved. G2[H1] is a symmetric map for every H1, on and off solutions, in every rotation gauge (second
  order of: the Ricci map of a field obeying the torsion equation is symmetric, R2 (ii)). So there is NO
  antisymmetric part to report.
- (iii) proved. grad.(G2(c)) = -[grad-dot.H1(v-dot) + v.w + c.(Omega1(d_a).G1(a))], v = G1[H1](c),
  w = d_a.Omega1(a) (second order of div G = 0, R2 (iii)). Zero on first-order solutions. Checked off
  solutions (identity, 12 nonzero terms) and on two solutions that are neither symmetric nor plane waves.
- (iv) proved. Displacement: G2[H1 - xi_] = G2[H1] + (xi.grad)G1[H1] - G1[(xi.grad)H1 - xi_ H1 + xi_ xi_].
  Rotation (rotor exp(eps B/2)): G2[H1 + beta] = G2[H1] - G1[H1 beta + beta beta/2] + G1 beta - beta G1.
  Parametrisation: hb -> hb + eps^2 q adds G1[q]. On solutions each change is G1[X], X explicit. NOT locally
  invariant (computed nonzero in all 16 entries). The proof includes a short derivation that the transformed
  pair of clause (e) of the definition obeys the torsion equation (the definition asserts the laws; the
  torsion statement is derived).
- (v) proved. E[x](a) = grad.W_a[x], W_a[x] = 1/2 (grad ^ x(a) - a ^ d + a ^ grad tau); n.E[x](n) is a
  derivative along the generator plus a transverse divergence (explicit). So the four fluxes
  P_c = int_N n.t(c) are unchanged by gauge changes of compact support on N; P_n under weaker conditions.
- (vi) proved from R1 (iii)(c), (iv). In the gauge H1 symmetric, H1(n) = 0, identically (solution or not):
  n.G2_r(n) = <sigma, sigma> + theta^2/2 + (1/8 - r/4) d_n^2 <h, h>, G2_r = G2 + r G1[H1 H1]
  (r = 0: hb = id + eps H1; r = 1: hb^{-1} = id - eps H1; r = 1/2: exponential). Pointwise equality with R1's
  density only for r = 1/2 and theta = 0. With fall-off (F) on each generator, the integral along each
  generator equals the integral of <sigma, sigma>/(8 pi G) for every r, and P_n is R1's null energy P.
  No transverse divergence in this gauge; out of the gauge the difference is a generator derivative plus a
  transverse divergence, by (v).
- (vii) proved by an exact finite computation (two quadratic forms on six variables compared on 21
  arguments). One plane wave along nbar: G2_r(a) = 1/4 (<h', h'> + (1/2 - r) <h, h>'') (a.k) k. For r = 1/2
  this is Isaacson's effective stress at each point, with no average.
- (viii) proved given (M1) [G1[H1] = -8 pi G T1] and (M2) [div T = O(eps^3) in the field]:
  grad.(T2(c)) = -F(c) (force), grad.((T2 + t)(c)) = 0; converse; and a second-order equation
  G1[H2] = -8 pi G (T2 + mu t) is solvable only if (mu - 1) F = 0. Second order only; NOT a derivation of
  condition (C) of R2 ((M2) is that condition for the matter). Check: dust falling in its own field.

Weaker than hoped / to say plainly:

- No local invariance of t, and no canonical t: three independent ambiguities (displacement, rotation gauge,
  second-order parametrisation), all of the form G1[X]. The pointwise identification with <sigma, sigma>
  is true in one parametrisation and one gauge only; in two of the six sample cases the density is negative.
- (viii) fixes only the flat divergence of the self-source, and assumes the matter's conservation law.
- Not done: independence of P_c of the plane; evaluation of P_c for c other than n in terms of the data;
  positivity beyond P_n; the average over wavelengths; anything beyond second order; the plane-wave formula
  for a general null momentum is by rotor covariance (argued, not checked).

Gates (final run): lint 0 errors 0 warnings; checkone all 10 pass; mutants: every function ok, with --every
no literal survives.

## Unexpected links

- The exponential parametrisation hb = exp(.) is the one in which the second-order null-null equation is the
  stored focusing equation term by term (theta = d_n tr u exactly for hb^{-1} = exp(u)). This may matter to
  attacker `shear` (null data at any field strength): in that parametrisation the trace of u is the logarithm
  of the area element of the generators' cross-section.
- The off-solution divergence identity (iii) is the same expression as the matter's force density (viii):
  one operator (the second-order part of the covariant divergence) applied to G1 and to T1.
- The memory effect shows up in (v)/(vi): the displacement that reaches the gauge h(n) = 0 for data of compact
  support generally does not vanish at the far end of the generators; P_n is still unchanged because only
  d_n of the quadratic field has to vanish there.

## Decisions for Leon

1. Whether the Reading of R1 (the paragraph on the shear) cites clause (vi) here in place of its argued remark.
2. Whether `op.einstein-from-the-field-theory` takes clause (viii) under its work in store, with attack items
   (a) the same argument at every order (Deser's route), (b) deriving (M2) from the stored response of matter.
3. Whether (M1), (M2) stay local hypotheses (kept local; no assumes edge declared).
4. Reference parametrisation at second order: hb = id + eps H1 + eps^2 H2 (used in the statement) or the
   exponential one (in which (vi) and (vii) hold at each point).
5. Whether the truncated-polynomial ring `Eps` and the explicit torsion solve in check.py move into lib/gtg.py.
6. Sign: t = +G2/(8 pi G) follows the store's G = -8 pi G T; the brief's minus sign is the literature's.

## Literature

Appended to store/references.yaml (keys checked absent first): `Isaacson1968`, `Deser1970`.
Confirmed on 27 November 2026: Isaacson, Phys. Rev. 166 (1968) 1272, journal, volume, first page, year and that
the abstract speaks of a gauge-invariant averaged stress tensor from the second-order terms (APS page; title
from a search result). Deser, "Self-interaction and gauge invariance", author, title, abstract, DOI
10.1007/BF00759198 (arXiv:gr-qc/0411023 page).
From memory, not confirmed: the last page 1280 of Isaacson's paper; "Gen. Rel. Grav. 1 (1970), 9--18" for
Deser's; S. N. Gupta 1954 (Phys. Rev. 96, 1683, as given in the brief; not found by the search); Feynman's
lectures on gravitation (1962 to 1963); the Einstein and Landau-Lifshitz pseudotensors; P. Freud 1939 for the
superpotential. Chandrasekaran2026: only the abstract page, through a summarising fetch; nothing of it is used.
Doran and Lasenby 2003 is not cited: the entity relies on the stored definition, not on the book.

## Fix round (after the blind referee's SOUND WITH FIXES)

Referee report: findings/referee-stress.md. All nine required fixes applied as worded there (LaTeX notation
adapted, nothing else changed):

1. formal (iv), last sentence: the proving option. "At every point of every first-order solution some
   displacement changes it", by the scaling xi -> s xi and G1[xi_ xi_] != 0 (computed; the displaced flat
   field H1 = -xi_ has G2 = -G1[xi_ xi_] != 0, now in the displacement check, nonzero in all 16 components
   for the check's xi). Technical level and one-liner brought to the same limited wording; the proof of (iv)
   has the argument.
2. formal (viii): quadratic source renamed chi; the overreaching sentence replaced; "where F != 0".
3. Reading: the second-order field equation named as a hypothesis before the null-null equation; "a source
   with the flat divergence of t is forced".
4. technical ("Finally" paragraph). 5. lay (a), (b) with the optional parenthesis, (c). 6. one-liner (a), (b).
7. formal (vi): "when the integrals converge"; last sentence restricted to solutions, X named.
8. Source of the idea and extraction note: the description of the paper limited to what its abstract says,
   with R1 named as the reader of its text; Isaacson's form is clause (vii) at r = 1/2 only.
9. premise(R1_ID) and premise(WEYL_FLAT_ID) in the displacement and rotation checks.

Optional suggestions applied: 1 (new check on a non-solution in the gauge (LC)); 2 (the (v) check is now a
finite proof: ten unit symmetric maps times ten polarising momenta, and the proof says the identity is also
proved analytically); 3 (the `dropped` counters removed; pinned instead: 12 failing directions, 48 and 32
changed components); 5 (explicit boundary terms in the P_n condition); 6 (the hypotheses (L), (D), (V), (N)
attach to calling the right side the null energy, not to the equality of integrals); 7 (displaced flat field
in the displacement check); 8 ("is reflected in the pseudotensors"). Optional 4 (Deser DOI): left to the
coordinator; store/references.yaml not touched.

Nothing declined.

Kerr-Schild addition (from attacker `shear`): CONFIRMED, by my own proof and computation (work/stress/t9.py,
then the new check). For hb(a) = a + 1/2 eps W (a.l) l, l = 1/2 nbar, W = -y.w_lam(y): Omega(a) =
eps (a.l) l ^ w(y) solves the torsion equation exactly, R(a^b) = eps l ^ w((a^b).l), and the Einstein map is
eps (tr w)(a.l) l with no higher order, so G2[H1] = 0 at every point, for every w, in every parametrisation r
(H1 H1 = 0). The same wave in the transverse trace-free gauge is h = F with F'' = 2w, with the nonzero G2 of
clause (vii). Relation: H1KS = H1TT - xi_ + beta, xi = -1/2 F(y) + 1/4 (y.F'(y)) l, beta the antisymmetric
part of xi_ (so a displacement AND a rotation gauge change, both growing across the plane; the coordinator's
message named only the displacement), and G2_KS - G2_TT = G1[X] with X = X_xi[H1TT] + X_B[H1TT - xi_]
exactly. Stated in the Reading as an instance of (iv) that does not contradict (v) because xi grows
quadratically across the plane; fluxes zero against R1's null energy under (F); "the fall-off condition of
(v) cannot be dropped". The last sentence there (where the focusing is carried in the Kerr-Schild gauge) is
labelled argued. The other result is named in the extraction note as the source of the observation and is
not a premise.
