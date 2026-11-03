**STATUS: READY for restaters (2026-10-23).** Sections 0-15 and "Bifurcation surfaces: restatement on a cross-section" are final; Leon's decisions are recorded under "Leon's decisions". Section 16 (d dimensions) is final; tractor entities and d-dimensional entities are owned by the lead.

# GTG dictionary: curved-spacetime language to Gauge Theory Gravity on flat spacetime

The shared translation table for run 2026-10-23-gtg. Restaters use it as written. If you need
an entry it lacks, add it under "Proposed additions" at the end (your name, the entry) and use
it consistently.

Store entities that carry this table:

- `obj.synthesis.gtg-flat-spacetime-gauge-fields` (definition): flat spacetime, \hb, Omega, D,
  R(B), the covariant field strength, the derived metric, the gauge freedoms, the invertible
  region. Cite it with `about:` or `\claimref{}` when a restated statement names these objects.
- `synthesis.imported-gtg-dictionary` (imported Fact): the translation statements (physical
  vectors, curvature dictionary, Weyl and Schouten, geodesics as D-parallel transport, Killing
  vectors and surface gravity). Cite it in a proof's opening sentence when the proof is written
  in metric language. It does not duplicate the equivalence of the field equations, which stays
  in `singularity.imported-equivalence-einstein-equations` (T05 Fact 2.1, with the curvature
  clause) and `interior.imported-equivalence-einstein-equations` (T06 Fact 2.1).
- Exact checks of the algebraic entries (Weyl, Schouten, Euler density, de Sitter, surface
  gravity from the stored connection, the PG metric): `verify/dictionary_identities.py`
  (27 checks, all pass).

Sources (abbreviations used below):

- **LDG** = A. Lasenby, C. Doran and S. Gull, Gravity, gauge theories and geometric algebra,
  Phil. Trans. R. Soc. Lond. A 356 (1998) 487-582 (arXiv:gr-qc/0405033). Checked on 2026-10-23
  against the arXiv text: the table of contents, eqs. (3.9), (3.18), (3.26)-(3.27), (3.31),
  (3.33), (3.35)-(3.36), (3.53), (3.72)-(3.74), (4.1)-(4.4), (4.9), (4.11)-(4.13), (4.21),
  (4.36)-(4.40), and the introduction's remark that GTG and GR differ on horizons and topology.
  The text available to me stops in Sec. 4.5; Secs. 4.3 (covariant forms), 4.4 (trajectories),
  5.1-5.3 (Weyl, duality, Petrov), 6.4 (black holes), 6.6 and 9 (cosmology) and App. C (the
  translation of tensor calculus) were located by title only.
- **DL** = C. Doran and A. Lasenby, Geometric Algebra for Physicists, CUP (2003). Chapter and
  section titles checked against the CUP table of contents: 13.4 Gauge principles for
  gravitation, 13.5 The gravitational field equations, 13.6 The structure of the Riemann tensor,
  14.1 Solving the field equations, 14.2 Spherically-symmetric systems, 14.3 Schwarzschild black
  holes, 14.5 Cosmology, 14.7 Axially-symmetric systems. No equation inside was checked.
- **L19** = A. N. Lasenby, Geometric algebra, gravity and gravitational waves, Adv. Appl.
  Clifford Algebras (2019), doi:10.1007/s00006-019-0991-y (arXiv:1912.05960). Checked: Sec. 4
  (D_a, the covariant D = \bar h(\partial_a) D_a in its notation, R(a^b), the covariant Riemann
  as R h(B), the metric g = \bar h^{-1} h^{-1}, vacuum equations), Sec. 5 (Newtonian gauge
  \bar h(a) = a - sqrt(2M/r)(a.e_r)e_t and its Riemann), eq. (8.5) (Weyl), (8.43)-(8.44).

---

## 0. Conventions fixed here (read first)

**C1. Background.** Flat spacetime: the vectors of Cl(1,3) at every point, with the fixed product
a.b and Q(a) = a^2, signature (+,-,-,-). Points are labelled by the position vector x; background
frame {e_mu}, reciprocal {e^mu}, flat vector derivative \nabla = e^mu d_mu. "Coordinates"
x^mu = e^mu . x are labels in the flat background only. The background carries no gravitational
meaning (LDG Sec. 3.1: a rule relating position vectors within a single vector space; Sec. 3.2:
the inner product "is not related to a curved space metric").

**C2. \hb is the series' gauge field, and it is LDG's underbar h.** The series writes
\hb(a) for the position-gauge field acting on background vectors and reads the metric as
g(a,b) = \hb^{-1}(a).\hb^{-1}(b) with frame g_mu = \hb^{-1}(e_mu). In LDG's notation that map is
\underline{h} (LDG (3.35)-(3.36): g_mu = \underline h^{-1}(e_mu), g_mu nu = g_mu . g_nu; L19
Sec. 4: g = \bar h^{-1} \underline h^{-1}). Confirmation from the stored Schwarzschild field:
the series' \hb(a) = a - beta (a.e_t) e_r (`sheaf.gauge-field-cometric`) is the adjoint of LDG's
Newtonian gauge \bar h(a) = a - beta (a.e_r) e_t (L19 Sec. 5); with the series' \hb the formula
g = \hb^{-1}.\hb^{-1} returns the PG line element (checked). Write \hb^T for the adjoint,
a.\hb^T(b) = \hb(a).b; LDG's \bar h is the series' \hb^T. For the Kerr-Schild field
\hb(a) = a + H (a.k) k the map is symmetric and the distinction disappears. \hb extends to
multivectors as an outermorphism.

**C3. Rotation gauge field.** Omega(a): a bivector-valued linear function of the background
vector a (LDG (3.26)-(3.27)). On physical vectors, omega(A) := Omega(\hb(A)) (LDG (3.72)).

**C4. Covariant derivative.** D_a M = a.\nabla M + Omega(a) x M, with A x B = (AB - BA)/2
(LDG (3.26)); on spinors D_a psi = a.\nabla psi + Omega(a) psi / 2 (LDG (3.53)). Along a
physical vector A: A.D = D_{\hb(A)} (LDG (3.73)-(3.74) in the series' notation). The covariant
vector derivative is D = \hb^T(\partial_a) D_a (L19 Sec. 4), so the physical gradient of a scalar
phi is \hb^T(\nabla phi).

**C5. Field strength and covariant curvature (store sign).** The background field strength is
R(a ^ b) = a.\nabla Omega(b) - b.\nabla Omega(a) + Omega(a) x Omega(b), [D_a, D_b] M = R(a ^ b) x M
(LDG (4.1)-(4.4)). LDG's covariant curvature is R(\hb(B)) (LDG (4.9), "our gauge theory analogue of
the Riemann tensor"). **The store's curvature operator is its negative,**

  \mathcal{R}(B) := -R(\hb(B)),

a linear map on physical bivectors, so that the store's existing curvature convention holds
unchanged (C6). Ricci: \mathcal{R}(b) = \partial_a . \mathcal{R}(a ^ b) (the contraction of LDG
(4.11)); scalar: \mathcal{R} = \partial_a . \mathcal{R}(a) (LDG (4.12)); \mathcal{G}(a) =
\mathcal{R}(a) - a \mathcal{R}/2. The contractions are over physical arguments with the flat product.
**The setting note `note.singularity.setting-gauge-theory-exactly` writes the script letter for
the background field strength with LDG's sign and contracts it directly; read its display as
R(a ^ b), and its contractions as applying to -\mathcal{R}(B) = R(\hb(B)) (LDG's sign).** On the
stored PG radial plane, which is \hb-invariant, R and R(\hb(.)) agree.

**C6. Sign of the curvature: the store's convention.** The store has one curvature convention,
stated in `synthesis.einstein-condition-is-infinity-vacuum-incidence`(7): in signature (+,-,-,-)
de Sitter space has Ric = Lambda g, so the store's Ric is minus Ric^o, the Ricci tensor of the
convention in which the round sphere has positive Ricci curvature, and Einstein's equation reads
Ric + 8 pi G T = (Lambda + 4 pi G tr T) g. The T05 and T06 curvature spectra follow it
(`singularity.curvature-gauge-field-exact-shape-decoupling`: \mathcal{R}(sigma_r) = +2M/r^3 sigma_r;
`interior.imported-kerr-curvature`). LDG, L19 and DL use the opposite sign. With C5:

- de Sitter: \mathcal{R}(B) = (Lambda/3) B, \mathcal{R}(a) = Lambda a, \mathcal{R} = 4 Lambda.
- Schwarzschild: \mathcal{R}(B) = (M/2r^3)(B + 3 sigma_r B sigma_r) = -(M/r^3) S(B) as stored
  (L19 Sec. 5 gives the negative, in LDG's sign). Checked against the stored connection
  (`singularity.connection-bivector-computed`, Omega(e_t) = (M/r^2) sigma_r with sigma_r = e_r e_t,
  the orientation for which (K.D)K = K/(4M) at r = 2M): R(e_t ^ e_r) = (2M/r^3) sigma_r, so LDG's
  radial eigenvalue is -2M/r^3 and the store's +2M/r^3.
- For a physical null k: Ric^o(k,k) = -k.\mathcal{R}(k).
- Field equation: \mathcal{G}(a) + Lambda a = -8 pi T(a) (equivalently \mathcal{R}(a) + 8 pi T(a) =
  (Lambda + 4 pi tr T) a); LDG's form \mathcal{G}_LDG(a) - Lambda a = 8 pi T(a) (LDG (4.21), (4.36)) is
  the same equation.
- Quadratic invariants (Kretschmann, Euler density), eigenvalue ratios, traces and eigenplanes do
  not depend on the sign.

Rule for restaters: write GTG forms in the store sign; when a source formula is in LDG's or the
round-sphere-positive sign, convert (\mathcal{R} = -\mathcal{R}_LDG, Ric = -Ric^o) or name the sign
in the statement, as the stored Raychaudhuri Fact does with Ric^o. (Needs Leon: the store sign is
the opposite of the GTG literature's.)

**C7. Other signatures.** Statements written in (-,+,+,+): under g -> -g, Christoffels,
R^a_{bcd}, R_ab, G_ab and T_ab are unchanged; R_abcd (all down), the scalar R and Lambda g_ab
change sign. Restate in (+,-,-,-) or keep the statement's own declared signature; do not mix.

**C8. Invertible region.** U is the domain where \hb is defined and invertible. Every translation in
this table holds on U only. In the PG and Kerr-Schild gauges \hb is unimodular (det \hb = 1, \hb(I) = I)
wherever it is defined: r = 0 in PG and the Kerr ring are where \hb is undefined (beta, respectively H,
diverges), not where it is non-invertible. They are loci of the flat background, not boundaries of a
manifold.

**C9. Units and constants.** G = c = 1 unless the stored statement says otherwise.

**C10. Connection sign: the store displays Omega in the GTG sign throughout (Leon, 2026-10-23).**
The definition's convention is D_a M = a.\nabla M + Omega(a) x M (left action), and every displayed
connection bivector is in that sign. Values computed from Cartan one-forms are converted when they are
assembled into bivectors: omega^i_0 = H_i theta^i gives omega(gamma_i) = -H_i gamma_0 ^ gamma_i for the
synchronous derived metric d tau^2 - sum a_i^2 dx_i^2 (checked); so `interior.interior-connection-exactly`
reads Omega(e_i) = -sigma_i B_i (B_i = e_0 ^ e_i; the sphere term +(cot theta/r) R_23 keeps its sign), and
the Hubble-normalised Kasner model is -sum_i p_i B_i (x) theta^i, which is the admissibility condition of
`obj.interior.weighted-blow-up-hubble-normalisation-admissible`; the weight bivector B_w = sum_i p_i B_i is
kept as defined and the limiting value is -B_w. Cartan one-forms omega^{ab} may still be shown as forms.
The curvature sign is unchanged: with Omega_C = -omega (the right-action values D_a v = a.\nabla v +
v . Omega_C(a)), a.\nabla Omega_C(b) - b.\nabla Omega_C(a) - Omega_C(a) x Omega_C(b) = -R(a ^ b) is the
store's curvature sign (C6), the Cartan one. The PG
connection of `singularity.connection-bivector-computed` with sigma_r = e_r e_t is in the definition's
sign (it gives kappa = +1/4M through (K.D)K = kappa K, checked).

**C11. Sign identifications (G1, checked on all frame planes of Schwarzschild and de Sitter).** In
(+,-,-,-), with Riem^o the round-sphere-positive Riemann tensor and the store's \mathcal{R}:
Riem^o(u,v,w,z) = (w ^ z) . \mathcal{R}(u ^ v); the Riemann endomorphism R(u,v)w is
-\mathcal{R}(u ^ v) . w, i.e. R(e_c, e_d) = -\mathcal{R}(e_c ^ e_d) as a bivector; hence
C(k,a,k,b) = (k ^ b) . \mathcal{W}(k ^ a); and the store-sign Weyl eigenvalue on sigma_r of
Schwarzschild-de Sitter is w_h = 2M/r^3 (at r_b: 2M/r_b^3). Coordinate Ricci (G2):
Ric^o_{mu nu} = -g_mu . \mathcal{R}(g_nu).

---

## 1. Metric and line element

| Curved spacetime | GTG on flat spacetime | Source |
|---|---|---|
| "a spacetime (M, g)" | "a gravitational field (\hb, Omega) on flat spacetime, defined on the invertible region U, whose derived metric is g" | LDG Sec. 3; setting note |
| metric g_mu nu | g_mu nu = g_mu . g_nu, g_mu = \hb^{-1}(e_mu); g(a,b) = \hb^{-1}(a).\hb^{-1}(b) for background vectors a, b | LDG (3.35)-(3.36); L19 Sec. 4 |
| inverse metric g^mu nu | g^mu . g^nu, g^mu = \hb^T(e^mu); g_mu . g^nu = delta | LDG (3.35) |
| line element ds^2 = g_mu nu dx^mu dx^nu | ds^2 = Q(\hb^{-1}(dx)) for the background displacement dx | LDG (3.36) |
| tetrad / vierbein e^a_mu, orthonormal frame | an orthonormal set {gamma_a} of Cl(1,3) (physical vectors use the flat product); coordinate components gamma^a . g_mu; background directions \hb(gamma_a) | LDG Sec. 3.5 |
| soldering form (coframe) e^a, frame map | e^a(v) = gamma^a . \hb^{-1}(v); frame map E_a = \hb(gamma_a). A corank-one soldering form is a locus where \hb^{-1} drops rank; at the sheaf paper's wall \hb^{-1} has a half-power pole and \hb drops rank (G2) | C2 |
| volume element sqrt(-g) d^4x | det(\hb)^{-1} d^4x | L19 Sec. 4 (L = det h^{-1} \mathcal{R}) |
| coordinate transformation / diffeomorphism | position-gauge displacement x -> f(x), acting by pullback: \hb'(a; x) = \hb(\bar f^{-1}(a); x') in LDG's adjoint notation (series: transform \hb^T by that rule) | LDG (3.9), (3.33) |
| local Lorentz (frame) rotation | rotation gauge: \hb(a) -> \hb(R~ a R) (so \hb^T(a) -> R \hb^T(a) R~ and physical vectors \hb^{-1}(a) -> R \hb^{-1}(a) R~), Omega(a) -> R Omega(a) R~ - 2 (a.\nabla R) R~, \mathcal{R}(B) -> R \mathcal{R}(R~ B R) R~. The setting note writes \hb(a) -> R \hb(a) R~, which is LDG's law for its \bar h = the series' \hb^T (C2) | LDG (3.18), (3.31) |

The metric is a derived reading, never a structure of the background. Write "the derived metric g"
or "the metric induced by \hb", not "the metric of spacetime".

## 2. Physical and background vectors

| Curved spacetime | GTG | Source |
|---|---|---|
| tangent vector at a point | a physical vector A = \hb^{-1}(a), a the background vector (displacement) it sits over | LDG (3.35) |
| A is null / timelike / spacelike | the background vector a is physically null iff Q(\hb^{-1}(a)) = 0, timelike iff > 0, spacelike iff < 0 | definition of g |
| light cone at x | the cone {a : Q(\hb^{-1}(a)) = 0} of background vectors; it is the image under \hb of the flat null cone | C2 |
| 4-velocity u, g(u,u) = 1 | v = \hb^{-1}(x'), Q(v) = 1, x(tau) the background worldline | LDG Sec. 4.4 (title checked) |
| covector / gradient d_mu phi | physical gradient \hb^T(\nabla phi) | C4 |
| frame g_mu, coframe g^mu | g_mu = \hb^{-1}(e_mu), g^mu = \hb^T(e^mu) | LDG (3.35) |
| index raising/lowering | not needed: physical vectors use the flat product | LDG Sec. 3.2 |

## 3. Covariant derivative and parallel transport

| Curved spacetime | GTG | Source |
|---|---|---|
| Levi-Civita derivative nabla_mu of a tensor | D_mu = D_{e_mu} acting on the physical multivector field; A.D = D_{\hb(A)} | C4 |
| Christoffel symbols Gamma^rho_{mu nu} | g^rho . (D_mu g_nu) (component reading only) | LDG App. C (title only; not checked) |
| torsion-free, metric-compatible | torsion: D ^ \hb^T(a) = \hb^T(\nabla ^ a) (LDG (4.40) in its notation \bar h); metric compatibility is automatic, since D acts by commutator with a bivector | LDG (4.37)-(4.40) |
| parallel transport of M along x(lambda) | D_{x'} M = 0, i.e. dM/dlambda = -Omega(x') x M; solution M(lambda) = U M(0) U~ with dU/dlambda = -Omega(x') U / 2, U(0) = 1: a rotor, so the flat product of transported physical vectors is preserved | from C4 (one-line derivation) |
| synchronous diagonal field d tau^2 - sum a_i^2 (dx^i)^2, H_i = d_tau log a_i | omega(gamma_0) = 0, omega(gamma_i) = -H_i gamma_0 ^ gamma_i in the definition's convention, the value the store displays (Omega(e_i) = -sigma_i B_i; as one-forms omega^{i0} = H_i e^i) (C10; G2's entry, sign corrected, checked) | C10 |
| holonomy around a loop | the rotor U of the closed loop; for an infinitesimal loop spanned by background a, b it is 1 - R(a ^ b)/2 (per unit area) | LDG (4.1) |

**Torsion equation, notation.** The setting note writes D ^ \hb(a) = \hb(\nabla ^ a), copying LDG's
symbol; in the series' convention (C2) it reads D ^ \hb^T(a) = \hb^T(\nabla ^ a). (Needs Leon.)

## 4. Geodesics

| Curved spacetime | GTG | Source |
|---|---|---|
| timelike geodesic, u^nu nabla_nu u^mu = 0 | D_{x'} v = 0 with v = \hb^{-1}(x'), Q(v) = 1: dv/dtau = -Omega(x') . v = v . omega(v) | LDG Sec. 4.4 (title); from C3-C4 |
| affinely parametrised null geodesic | k = \hb^{-1}(x'), Q(k) = 0, D_{x'} k = 0 | same |
| geodesic deviation | (v.D)(v.D) xi, linear in xi through \mathcal{R}(xi ^ v) . v; state the overall sign used (C6) | DL 13.6 (title) |

## 5. Curvature

| Curved spacetime | GTG | Source |
|---|---|---|
| Riemann tensor R_{mu nu}{}^{rho sigma} | \mathcal{R}(B) on physical bivectors; \mathcal{R}(g_mu ^ g_nu) = R(e_mu ^ e_nu) reproduces it on the frame planes | LDG (4.4), (4.9); `singularity.imported-equivalence-einstein-equations` |
| curvature operator on bivectors, its spectrum, eigenplanes | the linear map B -> \mathcal{R}(B) on the six-dimensional bivector space; same objects | same Fact (second clause) |
| Ricci tensor R_mu nu | \mathcal{R}(b) = \partial_a . \mathcal{R}(a ^ b); R_mu nu = g_mu . \mathcal{R}(g_nu) | LDG (4.11) |
| Ricci scalar R | \mathcal{R} = \partial_a . \mathcal{R}(a) | LDG (4.12) |
| Kretschmann R_abcd R^abcd | 2 <\mathcal{R}(a ^ b) \mathcal{R}(\partial_b ^ \partial_a)> (checked: 48 M^2/r^6 on Schwarzschild) | this table; verify script |
| Schouten tensor P_ab | P(a) = (\mathcal{R}(a) - a \mathcal{R}/6)/2 (four dimensions); macro \Sch | standard; checked |
| Weyl tensor C_abcd (trace-free part of Riemann) | \mathcal{W}(a ^ b) = \mathcal{R}(a ^ b) - P(a) ^ b - a ^ P(b) = \mathcal{R}(a ^ b) - (\mathcal{R}(a) ^ b + a ^ \mathcal{R}(b))/2 + \mathcal{R} a ^ b / 6; trace-free: \partial_a . \mathcal{W}(a ^ b) = 0 | L19 (8.5); LDG 5.1 (title); checked |
| Weyl self-duality, Petrov type | \mathcal{W}(IB) = I \mathcal{W}(B): \mathcal{W} is linear over {1, I}; Petrov type from its eigenvalues on the three-dimensional {1,I}-module of bivectors | LDG 5.2-5.3 (titles) |
| Weyl scalars Psi_0..Psi_4 | components of \mathcal{W} on a null tetrad's bivectors (k ^ m etc.) | store: `pairing.imported-weyl-scalars-petrov-type-schwarzschild` |
| Bianchi identities | \partial_a ^ \mathcal{R}(a ^ b) = 0 (first), \dot D ^ \dot{\mathcal{R}}(B) = 0 with D acting covariantly (second) | LDG 5.4 (title) |
| conformally flat | \mathcal{W} = 0 | standard |

## 6. Einstein tensor and field equations

| Curved spacetime | GTG | Source |
|---|---|---|
| Einstein tensor G_mu nu | \mathcal{G}(a) = \mathcal{R}(a) - a \mathcal{R}/2 | LDG (4.13) |
| Einstein's equation with Lambda | \mathcal{G}(a) + Lambda a = -8 pi T(a), i.e. \mathcal{R}(a) + 8 pi T(a) = (Lambda + 4 pi tr T) a (store sign, C6) | LDG (4.21), (4.36), sign converted |
| vacuum, Ricci-flat | \mathcal{R}(a) = 0 (with Lambda: \mathcal{R}(a) = Lambda a) | L19 Sec. 4 |
| Einstein metric Ric = Lambda g (store convention) | \mathcal{R}(a) = Lambda a | C6 |
| coordinate Ricci, round-sphere-positive sign (standard Christoffel formula R_{mu nu} = d_rho Gamma^rho_{mu nu} - ...) | Ric^o_{mu nu} = -g_mu . \mathcal{R}(g_nu) (G2) | C6, C11 |
| equivalence of the two theories | on U the GTG equations are Einstein's equations for the derived metric | `singularity.imported-equivalence-einstein-equations`, `interior.imported-equivalence-einstein-equations` |

## 7. Stress-energy

| Curved spacetime | GTG | Source |
|---|---|---|
| T_mu nu | T(a), a symmetric linear map on physical vectors; T_mu nu = g_mu . T(g_nu) | LDG Sec. 4 |
| energy density seen by observer u | v . T(v), Q(v) = 1 | standard |
| null energy condition | k . T(k) >= 0 for every physical null k | standard |
| Ric^o(k,k) = 8 pi T(k,k) on null k | -k . \mathcal{R}(k) = 8 pi k . T(k) | C6 |
| heat flux through a horizon element | the flux of T(chi) across the patch, chi the approximate boost vector field (Section 9) | Jacobson 1995 via `synthesis.imported-jacobson-clausius-1995` |

## 8. Killing vectors and surface gravity

| Curved spacetime | GTG | Source |
|---|---|---|
| Killing vector field xi, nabla_(mu xi_nu) = 0 | a physical vector field K for which A -> A.D K is antisymmetric in the flat product: B.(A.D K) + A.(B.D K) = 0; then A.D K = A . F_K with the bivector F_K = (D ^ K)/2 | standard, read through C4 |
| coordinate form xi = xi^mu d_mu | background generator \hb(K) = K^mu e_mu; in a stationary gauge K = \hb^{-1}(e_t) | C2 |
| static Killing field of Schwarzschild | K = \hb^{-1}(e_t) = e_t + beta e_r in the stored PG gauge; Q(K) = 1 - beta^2 | `sheaf.gauge-field-cometric` |
| Killing horizon | the locus where Q(K) = 0 and K is normal to it | standard |
| surface gravity kappa: xi^b nabla_b xi^a = kappa xi^a on the horizon | (K.D) K = kappa K on the locus; with the stored connection, D_{e_t} K = Omega(e_t) . K = K/(4M) at r = 2M (checked) | Wald 1984 Sec. 12.5; `singularity.imported-surface-gravity-redshifted-acceleration` |
| Killing spinor, Killing-Yano tensor | D-constancy conditions on the corresponding multivector fields; read each stored statement with D_a | DL 14.7 (title) |

## 9. Null congruences, expansion, shear, Raychaudhuri; local Rindler horizons

| Curved spacetime | GTG | Source |
|---|---|---|
| null geodesic congruence k^a | a physical null vector field k, Q(k) = 0, (k.D) k = 0 | Section 4 |
| screen space | physical vectors orthogonal to k and to an auxiliary null n with k.n = 1 | standard |
| B_ab = nabla_b k_a | the linear map A -> A.D k restricted to the screen space | C4 |
| expansion theta, shear sigma_ab, twist omega_ab | trace, symmetric trace-free part and antisymmetric part of that map; theta = D.k for a geodesic congruence | standard |
| Raychaudhuri / Sachs equations | (k.D) theta = -theta^2/2 - |sigma|^2 + |omega|^2 + k.\mathcal{R}(k) (store sign: -Ric^o(k,k) = k.\mathcal{R}(k)); shear sourced by \mathcal{W} contracted twice with k, projected trace-free to the screen | `synthesis.imported-raychaudhuri-null-congruence` read through C6 and Section 5 |
| local Rindler horizon at p, generated by l | at the point x0 use both gauge freedoms to set \hb(x0) = 1 and Omega(x0) = 0 (the GTG reading of Riemann normal coordinates with a parallel frame; then \hb = 1 + O(|x - x0|^2) with the quadratic term linear in \mathcal{R}(x0)); the patch is the flat null hyperplane piece {x : l.(x - x0) = 0} near x0, l a null vector of Cl(1,3) (physically null at x0 since \hb(x0) = 1), with the frame D-transported from x0 along straight background rays | standard construction read through C2-C5; Jacobson 1995 |
| local boost / approximate Killing field | the boost generated by the bivector of the plane l ^ n at x0: chi(x) = (x - x0) . (l ^ n), Killing to the order O(\mathcal{R}(x0) |x - x0|^2) | same |
| local boost patch, causal diamond | the corresponding piece of flat background with the transported frame; everything at leading order in |x - x0| against the curvature scale of \mathcal{R}(x0) | `synthesis.local-boost-temperature-is-local-regularity` |

Local Rindler and local boost patches are local: one chart, native GTG.

## 10. Horizons as loci

| Curved spacetime | GTG | Source |
|---|---|---|
| Killing horizon | the locus {Q(K) = 0} of the flat background (Section 8) | standard |
| apparent horizon / marginally trapped surface | a closed two-surface in the background on which the outgoing expansion theta_+ = D.k_+ vanishes | standard |
| event horizon | on a chart that contains the exterior and its causal future (the stored PG and Kerr-Schild charts do), the boundary of the causal past of the asymptotic region, read with the cones of Section 2; for the stored stationary gauges it is the Killing horizon locus | LDG Sec. 6.4 (title) |
| the horizon is a regular place | \hb is invertible on the horizon locus (PG: at every r > 0) | `sheaf.gauge-field-cometric` |
| black hole versus white hole | the sign of beta in PG fixes the sector: the stored gauge is the black-hole (ingoing) sector; GTG's black holes are time-asymmetric gauge sectors, and the eternal two-sided extension is not on one chart | LDG Sec. 1 (checked) |

## 11. Solutions as stored or standard

All on the invertible region U; "chart" means the flat background region the fields live on.

- **Schwarzschild (PG gauge, as stored).** \hb = 1 - beta P, beta = sqrt(2M/r), P(a) = (a.e_t) e_r,
  P^2 = 0; \hb^{-1} = 1 + beta P; ds^2 = dt^2 - (dr + beta dt)^2 - r^2 dOmega^2; U = {r > 0}.
  Connection: `singularity.connection-bivector-computed`. Curvature: C6. Covers the exterior and
  the black-hole interior; not the white hole or the second exterior (Section 14).
  Sources: `sheaf.gauge-field-cometric`; LDG 6.4; DL 14.3; L19 Sec. 5.
- **Kerr (Kerr-Schild gauge, as stored).** \hb(a) = a + H (a.k) k, Q(k) = 0, \hb^{-1}(a) =
  a - H (a.k) k; derived metric g = eta - 2H k k (in the reading of C2). U is the background minus
  the ring; H and k are smooth off the ring but the r > 0 sheet's fields, continued through the
  disc bounded by the ring, land on the r < 0 sheet (Section 14). Sources:
  `interior.imported-kerr-schild-form-kerr-gauge`; DL 14.7; L19 Sec. 5.1 (Kerr curvature
  -(M/2)(r + I L cos theta)^{-3}(B + 3 sigma_r B sigma_r) in LDG's sign; the store's
  `interior.imported-kerr-curvature` carries it in the store sign, C6). A PG-type Kerr gauge
  exists (Doran's form, L19 ref. [8]; C. Doran, Phys. Rev. D 61 (2000) 067503, cited from
  memory).
- **de Sitter.** Flat slicing on t in R: \hb^{-1}(e_t) = e_t, \hb^{-1}(e_i) = e^{Ht} e_i,
  H^2 = Lambda/3; static/PG form: \hb = 1 - beta P with **beta = -rH** (the expanding chart: free fall dr/dt = Hr;
  it contains the static observer's future horizon; beta = +rH is the contracting chart, which
  contains the past horizon; checked) (Schwarzschild-de Sitter: beta^2 = 2M/r + Lambda r^2/3, sign
  chosen per region and stated). \mathcal{R}(B) = (Lambda/3) B (store sign; checked in LDG's), Weyl
  zero. Either chart covers the expanding (Poincare) half; global de Sitter does not fit (Section 14).
- **FLRW.** k = 0: \hb^{-1}(e_t) = e_t, \hb^{-1}(e_i) = a(t) e_i (comoving gauge) on the whole
  chart; LDG 6.6 and 9 use a Newtonian-type gauge as well. k < 0: on the whole chart. k > 0: only
  on a chart that omits one point of each closed slice (stereographic), so the closed universe as a
  whole is beyond one chart (Section 14). Sources: LDG 6.6, 9.2 (titles); DL 14.5 (title).
- **Kasner.** On t > 0: \hb^{-1}(e_t) = e_t, \hb^{-1}(e_i) = t^{p_i} e_i, so
  \hb(e_i) = t^{-p_i} e_i; ds^2 = dt^2 - sum t^{2p_i} dx_i^2; \hb fails at t = 0. Vacuum iff
  sum p_i = sum p_i^2 = 1. Local Kasner collars (the stored interior collars) are native.
  Compact (toroidal) Kasner is beyond one chart.

## 12. Tractors and the scale tractor in the conformal model Cl(2,4)

**What is standard.** The tractor bundle of a conformal four-manifold has rank six and fibre
signature (2,4); the normal tractor connection is the normal conformal Cartan connection, an
so(2,4)-valued connection depending only on the conformal class (Bailey, Eastwood and Gover 1994,
`BEG1994`; Curry and Gover 2018, stored in `interior.imported-tractor-connection`). Gauge-theoretic
readings exist on a manifold: Kaku, Townsend and van Nieuwenhuizen (gauging SO(2,4), 1977, from
memory); J. Attard and J. Francois, Tractors and twistors from conformal Cartan geometry: a gauge
theoretic approach I (arXiv:1609.07307, checked: tractor connections are induced by the normal
Cartan connection; the construction is on a curved conformal manifold, flat Klein model only as
reference); Y. Herfray and C. Scarinci, Einstein gravity as a gauge theory for the conformal
group, Class. Quantum Grav. (2022), doi:10.1088/1361-6382/ac3e53 (arXiv:2011.00945, checked:
first-order formulation of conformal tractor geometry, variational tractor Einstein equation).
On a flat background in GA, Lasenby and Hobson (J. Math. Phys. 57 (2016) 092505,
doi:10.1063/1.4963143, arXiv:1510.06699, checked at abstract level) gauge the Weyl group
(Poincare plus dilations) as gauge fields in Minkowski spacetime, and Hobson and Lasenby, "Fresh
perspective on gauging the conformal group" (2021, abstract checked; journal not checked), gauge
the conformal group through their extended Weyl gauge theory, not as a Cartan connection valued in
Cl(2,4) bivectors. A. Lasenby, Recent applications of conformal geometric algebra (IWMM 2004,
LNCS 3519, Springer 2005; abstract checked) and the Lasenby-Lasenby-Wareham report treat
conformal GA for geometry, not gravity; I found no gauge-theory-of-gravity content in either.

**Finding.** No source found carries the normal tractor connection as a gauge field on flat
spacetime valued in the bivectors of the conformal model Cl(2,4).

**Decided (Leon, 2026-10-23): carried as the store's own transcription, with an exact check.** The
proved claim `synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection` (5 exact checks, layer 4
clean) fixes the form: Omega_T(a) = Omega(a) - n_inf ^ \hb^{-1}(a) + n_0 ^ P(\hb^{-1}(a)) on tractors
sigma n_inf + mu + rho n_0 (so u_p = n_inf, X_p = n_0, e_a = \hb^{-1}(a) in the stored splitting
nabla_a = nabla^g_a - u_p ^ e_a + X_p ^ P(e_a)); (i) it is the stored connection slot by slot and preserves Q;
(ii) n_inf + rho n_0 is parallel iff Einstein with Lambda = 6 rho, Q = Lambda/3; (iii) the flat de Sitter
scale tractor is parallel and equals I_Lambda at the origin; (iv) its algebraic field strength is
-W, no dilation block; (v) on I-perp it is the MacDowell-Mansouri connection Omega(a) - \hb^{-1}(a) ^ V/l^2,
D_a V = \hb^{-1}(a). Restate tractor statements as "the tractor connection, which on flat spacetime is
the Cl(2,4) gauge field Omega_T of [that theorem]". The text below is the earlier proposal, kept for
the record.

**What the store would be asserting (earlier proposal).** On the invertible region U,
tractors at x are vectors of Cl(2,4) = Cl(1,3) + the plane {e_+, e_-} (null vectors n_0, n_inf of
the store's conventions), and the tractor connection is the Cl(2,4)-bivector-valued rotation-gauge
field
  Omega_T(a) = Omega(a) + c_1 n ^ \hb^{-1}(a) + c_2 n' ^ P(\hb^{-1}(a)),
D^T_a V = a.\nabla V + Omega_T(a) x V, where n, n' are the two null directions of the added plane
singled out by the scale (the stored X_p and u_p of `standard-model.imported-tractor-bundle-spinor-bundle-their`
read the same way), the soldering term is the frame \hb^{-1}(a), P is the Schouten map, and the
constants c_1, c_2 (signs and normalisation) are those fixed internally by
`interior.sign-fixed-internally`. Its gauge freedoms are the Cl(2,4) rotors of the parabolic
subgroup (Lorentz, dilation exp(phi E/2), special conformal), acting by LDG's law (3.31):
Omega_T -> R Omega_T R~ - 2 (a.\nabla R) R~. The vacuum statement of
`correspondence.imported-vacuum-equations-scale-tractor` reads D^T_a I = 0 for the scale tractor I.
This is no stronger than BEG1994 restricted to U (the tractor bundle is trivial over a contractible
region, so a global frame exists and the connection is a matrix of one-forms, here a bivector-valued
function of a), but the identification "the tractor connection is a Cl(2,4) gauge field on flat
spacetime" is the store's transcription, not a literature result, and it wants an exact check
(on the stored de Sitter and Schwarzschild fields: the soldering and dilation blocks of the field
strength of Omega_T vanish and its Lorentz block is \mathcal{W}).

## 13. Euler density, Gauss-Bonnet and MacDowell-Mansouri

| Curved spacetime | GTG | Source |
|---|---|---|
| Euler density R_abcd R^abcd - 4 R_ab R^ab + R^2 | E = 2<\mathcal{R}(a ^ b)\mathcal{R}(\partial_b ^ \partial_a)> - 4 \mathcal{R}(\partial_a).\mathcal{R}(a) + \mathcal{R}^2 = -2 <\mathcal{R}(a ^ b) I \mathcal{R}(I \partial_b ^ \partial_a)> (both checked exactly on five curvature operators; sign-independent) | verify script |
| integral of E over a region | int E det(\hb)^{-1} d^4x over the background region | Section 1 |
| Euler term is a total derivative | locally E det(\hb)^{-1} is a divergence; on one flat chart its integral is a boundary term at the edge of U | Chern 1944 via `synthesis.imported-chern-gauss-bonnet` |
| 2D Gauss-Bonnet on a closed two-surface (horizon cross-section) | native: the surface is a compact subset of the background; integrate the induced curvature of the surface | `synthesis.imported-chern-gauss-bonnet` (a) |
| 4D Chern-Gauss-Bonnet, int E = 32 pi^2 chi(M) | needs a closed four-manifold: beyond one chart (Section 14) | same (b) |
| MacDowell-Mansouri: SO(1,4) connection A = omega + e | adjoin one vector V, Q(V) = -l^2, l^2 = 3/Lambda (Cl(1,4)); A(a) = Omega(a) + \hb^{-1}(a) ^ W, W = V/Q(V) = -V/l^2, i.e. Omega(a) - \hb^{-1}(a) ^ V / l^2: then D_a V = \hb^{-1}(a), the soldering form, as the stored Fact requires (checked; the sign +\hb^{-1}(a) ^ V/l^2 gives D_a V = -\hb^{-1}(a)). It is the tractor gauge field with P = (Lambda/6) id restricted to I-perp (`synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection`(v)) | `dark-energy.imported-macdowell-mansouri-theorem-stelle-west`; Wise2010 |
| its curvature F^ab = R^ab + l^{-2} e^a ^ e^b | covariant Lorentz block -\mathcal{R}(B) + l^{-2} B = -(\mathcal{R}(B) - l^{-2} B) in the store sign, from Theta(A) x Theta(B) = (A ^ B)/l^2 (checked); write \mathcal{F}(B) := -(\mathcal{R}(B) - l^{-2}B), as the stored Fact does: the 2-form F^ab = R^ab + l^{-2} e^a ^ e^b is exactly this operator (C11: R(u,v) = -\mathcal{R}(u ^ v) as a bivector, and (e^a ^ e^b)(u,v) acts as (u ^ v).w; GR2); it vanishes exactly on de Sitter; the V-block is the torsion | verify script |
| S_MM ~ l^2 int eps F ^ F | l^2 int det(\hb)^{-1} (-2) <\mathcal{F}(a ^ b) I \mathcal{F}(I \partial_b ^ \partial_a)> up to the stored normalisation: Euler term + Einstein-Hilbert term + cosmological term | same Fact read through the row above |

## 14. Beyond one flat chart

GTG puts every gravitational field on the one flat background with fields (\hb, Omega) single-valued
and \hb invertible on U. LDG state that GTG and GR differ "on matters such as the role of horizons
and topology" (LDG Sec. 1, checked) and require position-gauge maps to be one-to-one and to cover
all of spacetime (LDG Sec. 3.1, checked). The following cannot be carried by a single globally
defined (\hb, Omega) on R^{1,3}:

1. **Non-trivial spacetime topology.** Closed FLRW (closed spatial slices), global de Sitter
   (R x S^3), global anti-de Sitter, compact Kasner and any spatially compact model, every
   Euclidean closed instanton (S^4, S^2 x S^2, CP^2). Their local content (field equations,
   curvature, horizons, temperatures from local regularity) is native on a patch.
2. **Topological integrals.** 4D Chern-Gauss-Bonnet (int E = 32 pi^2 chi(M) for closed M), and any
   result that evaluates chi, a signature or an instanton number. On one chart such integrals are
   boundary terms. 2D Gauss-Bonnet on a closed horizon cross-section is native (item above).
3. **Maximal analytic extensions and second sheets.** The Kruskal extension (white hole, second
   exterior), Kerr's r < 0 sheet reached through the disc bounded by the ring, the Kerr and
   Reissner-Nordstrom inner horizons continued into further universes, double covers and blow-ups
   of the ring (multivalued or doubled fields). One chart carries one time-asymmetric sector and
   one sheet. **This includes the Lorentzian bifurcation surface** of a Killing horizon (the fixed
   locus of the boost flow, r = 2M at the meeting of the four Kruskal regions): the ingoing PG
   chart contains the future horizon but not the bifurcation two-sphere, and there K = e_t + beta e_r
   has no zero. A statement that uses the Lorentzian bifurcation surface itself is flagged; one that
   uses only the regularity of the Euclidean section at its tip is local (item 5).
4. **Conformal compactification.** Points at infinity, scri, the conformal boundary of de Sitter:
   they are null rays of R^{2,4} in the conformal model, not points of the flat GTG chart.
   Statements about them are native to the conformal model Cl(2,4), not to one GTG chart.
5. **Euclidean sections as global objects.** Regularity of the Euclidean section at a bifurcation
   point is local (a polar chart about the tip) and native on the Wick-rotated flat background; a
   statement about the whole closed Euclidean manifold is item 1.

**Open question (G3, not researched).** The Kruskal manifold is topologically R^2 x S^2, i.e. R^4 minus a
line; whether the whole extension, bifurcation surface included, can be carried by a single field
(\hb, Omega) on R^{1,3} that fails only on a removed line is open. Until settled, item 3 stands.

Not beyond one chart (do not flag): horizons as loci; the PG and Kerr-Schild charts with their
singular loci; non-contractible loops in U (holonomy around the Kerr ring, which is single-valued
on U); local Rindler patches and diamonds; collars of the singularity; temperatures from local
regularity.

**Flag sentence (add to the formal level, at its end, and in one plain sentence to technical):**

> \emph{Beyond one flat chart.} The [global ingredient: e.g. Euler characteristic of the closed
> four-manifold / the $r < 0$ sheet of Kerr / the closed spatial slices] is global and is not
> carried by a single gravitational field $(\hb, \Omega)$ on flat spacetime; the statements above
> that hold on the invertible region are in GTG, and [the global ingredient] is read on the
> manifold assembled from the derived metric's charts.

Technical-level sentence: "Its [global ingredient] is global: no single gravitational field on flat
spacetime carries it, so that part is read on the curved manifold."

**Flags field: yes.** `extraction.flags` holds extraction diagnostics as short strings whose prefix
before the colon is a category (counted by tp/extract.py, carried into the site's node data by
tp/build.py and tp/site.py); the validator does not read it. Record each flagged entity with one
entry of the form
  `'beyond one flat chart: <global ingredient>'`
so the flagged set can be listed mechanically. The text sentence is the statement; the flag only
indexes it.

## 15. Phrase list (quick substitutions)

- "curved spacetime with metric g" -> "a gravitational field (\hb, \Omega) on flat spacetime whose
  derived metric is g"
- "the curvature of spacetime" -> "the field strength \mathcal{R}(B) of the gravitational field"
- "spacetime is curved / flat" -> "the field strength is nonzero / vanishes" (flatness of the
  background is not a physical statement)
- "geodesic" -> "worldline whose velocity \hb^{-1}(x') is D-parallel"
- "null direction at p" -> "physically null direction at x: a with Q(\hb^{-1}(a)) = 0"
- "Riemann normal coordinates at p" -> "a gauge with \hb(x0) = 1 and Omega(x0) = 0"
- "coordinate singularity" -> "a failure of the gauge choice, removable by a gauge transformation"
- "curvature singularity" -> "a locus where \hb is undefined or fails to be invertible (in the PG and
  Kerr-Schild gauges: undefined, its potential diverging; \hb is unimodular where defined) and the field
  strength diverges"
- "the manifold" (local statements) -> "the invertible region U"
- keep "horizon", "Killing", "geodesic", "de Sitter", "Kasner": they are names of GTG objects too.

---

## 16. GTG in d dimensions (Leon's decision, 2026-10-23)

**Construction.** Background: the vectors of Cl(p,q), d = p + q, with the fixed product; the
store's Lorentzian case is (1, d-1) in (+,-,...,-). Gravity is (\hb, Omega): \hb a position-dependent
invertible linear map of vectors (outermorphism), Omega(a) bivector-valued. Everything in C2-C5 is
written in geometric calculus that does not use the dimension: D_a M = a.\nabla M + Omega(a) x M,
R(a ^ b) = a.\nabla Omega(b) - b.\nabla Omega(a) + Omega(a) x Omega(b), \mathcal{R}(B) = -R(\hb(B)) (store
sign), \mathcal{R}(b) = \partial_a . \mathcal{R}(a ^ b), \mathcal{R} = \partial_a . \mathcal{R}(a),
\mathcal{G}(a) = \mathcal{R}(a) - a\mathcal{R}/2, g(a,b) = \hb^{-1}(a) . \hb^{-1}(b), gauge laws as in the
definition (rotors of Spin(p,q)).

**What LDG's construction needs, and what changes with d.** (Checked against the construction, not
against a d-dimensional source; LDG and DL work in Cl(1,3).)
- Needed and dimension-free: linear functions and their adjoints and outermorphisms, rotors and the
  rotation gauge law (DL ch. 4, 11: Spin(p,q) for any p, q), the commutator field strength, the
  contractions with \partial_a, and the torsion equation D ^ \hb^T(a) = \hb^T(\nabla ^ a), which fixes
  Omega uniquely from \hb in every dimension (the Levi-Civita uniqueness in frame form: d^2(d-1)/2
  torsion components against d^2(d-1)/2 connection components). So the equivalence with Einstein's
  equations for the derived metric (the frame formalism) holds in every d >= 2 on the invertible
  region.
- Dimension-specific: the Schouten map P(a) = (\mathcal{R}(a) - a\mathcal{R}/(2(d-1)))/(d-2) (d >= 3) and
  the Weyl curvature \mathcal{W}(a ^ b) = \mathcal{R}(a ^ b) - P(a) ^ b - a ^ P(b) (trace-free; zero in
  d = 3); de Sitter_d: \mathcal{R}(B) = 2Lambda B/((d-1)(d-2)), \mathcal{R}(a) = 2Lambda a/(d-2);
  field equation \mathcal{G}(a) + Lambda a = -8 pi G_d T(a) (store sign); the duality W(IB) = I W(B)
  and the Petrov classification are four-dimensional; the Euler density is topological only in d = 4
  (Lovelock term in d = 5, 6); Dirac/spinor parts (LDG Sec. 3.3-3.4) are not used.
- Exact identities: `verify/d_dimensional_identities.py` (27 checks, all pass: d = 3, 5, 6 and
  signature (2,3); the d-dimensional Schouten coefficients make W vanish on Kulkarni-Nomizu
  operators and trace-free in general; de Sitter_d solves the store-sign field equation).
- Store anchor: the definition object's clause "(d dimensions)" (version 2) states this.

**Rows.**

| Curved spacetime, d dimensions | GTG on flat R^{p,q} | Source |
|---|---|---|
| d-dimensional spacetime (M, g) | a gravitational field (\hb, Omega) on flat R^{p,q}, derived metric g | definition, d-dim clause |
| bulk with a hypersurface (brane) | a hypersurface of the flat background with unit physical normal n = \hb^{-1}(N)/norm; induced metric from \hb^{-1} restricted to it; extrinsic curvature K(a) = projected D_a n | dictionary rows read in d dims |
| warped product g = g_4 + l^2 d theta^2 (or a(theta)^2 g_4 + ...) | \hb^{-1} block-diagonal: \hb^{-1}(a_4) = w(theta) \hb_4^{-1}(a_4), \hb^{-1}(e_theta) = l e_theta | definition, d-dim clause |
| Einstein-Hilbert action int sqrt(-g) R d^dx | int det(\hb)^{-1} \mathcal{R} d^dx (sign as the stored statement) | L19 Sec. 4 (4D form), d-dim clause |
| d-dimensional geodesic ball, Riemann normal coordinates | the normal gauge \hb(x0) = 1, Omega(x0) = 0 at a point of R^{p,q} (Section 9 in d dims) | Section 9 |
| Wald / Noether charge in n dimensions | the Lagrangian as a scalar of \mathcal{R} and its D-derivatives; binormal of the bifurcation surface -> the unit bivector of the horizon's boost plane on a cross-section (Bifurcation surfaces section) | dictionary rows read in n dims |
| locally conformally flat (d >= 4) | a gauge with \hb^{-1}(a) = e^{omega} a exists locally, iff \mathcal{W} = 0 (G1's reading) | Weyl's theorem, d >= 4 |

## Bifurcation surfaces: restatement on a cross-section (Leon's decision, 2026-10-23)

The ingoing PG chart (and the static/PG de Sitter chart) contains the future horizon but not the
bifurcation surface. Restate on a cross-section of the horizon locus inside the chart: the area,
the surface gravity and the boost (Killing) flow are the same there. Use the wording below
verbatim (adapt only the symbols already in the statement).

**Schwarzschild.** Replace "the bifurcation surface (at $r = 2M$)" / "the bifurcation sphere" by

> a cross-section $\Sigma_{t_0} = \{t = t_0,\ r = 2M\}$ of the horizon locus in the
> Painlev\'e-Gullstrand chart, of area $16\pi M^{2}$, on which the Killing field
> $K = \hb^{-1}(e_t)$ is null and normal to the horizon, with $(K \cdot D)K = \kappa K$,
> $\kappa = 1/4M$; the boost flow is the flow of $K$, which carries cross-sections to
> cross-sections

**de Sitter (static observer).** Replace "the bifurcation sphere $S_\Lambda$ of areal radius $1/H$" by

> a cross-section of the cosmological horizon locus $r = 1/H$ in the static
> Painlev\'e-Gullstrand chart of de Sitter space ($\hb = 1 - \beta P$, $\beta = -rH$, the expanding chart, whose free-fall observers have $dr/dt = Hr$ and which contains the static observer's future horizon), of area
> $4\pi/H^{2}$, on which the static Killing field is null and normal with surface gravity $H$

**Schwarzschild-de Sitter, Kerr:** the same pattern, with the stored $r_{b}$, $r_{c}$, $r_{+}$ and
their $\kappa$ (Kerr: the Kerr-Schild chart, $K = \hb^{-1}(\partial_t + \Omega_H \partial_\phi)$).

**"The fixed locus of the boost flow" and premise (R)-type regularity.** Replace "at the fixed
locus of the boost flow, the bifurcation surface" by

> across the horizon locus in the chart: the Euclidean section is regular at its tip, which fixes the
> period 2 pi/kappa; for a state that is KMS for the Killing flow, this is also the period at which it
> is regular across the horizon locus in the PG chart

**Note sentence (add once, at the end of the formal level, after the restated text):**

> The bifurcation surface itself, where the boost flow has its fixed points, lies beyond one flat
> chart (it is the meeting of the four regions of the maximal extension); the chart contains the
> future horizon, on whose cross-sections the area, the surface gravity and the boost flow are
> those stated.

Do not add `beyond one flat chart` to `extraction.flags` for these: the content is carried in the
chart. **Exception (flag, do not restate):** a statement whose content uses the past half of the
horizon generators or the edge itself (for example "$u \in \R$, the whole generator, with $u = 0$
on the bifurcation surface" in premise (N$_+$) case (a) and the theorem built on it). There, keep
the text, add the flag sentence of Section 14 naming "the whole generator of the eternal
horizon, through its bifurcation surface", and add the flags entry; list it under "Needs Leon" in
your report.

## Leon's decisions (2026-10-23)

1. Curvature sign: keep the store's sign (C6); the object and conventions state the one sign flip
   against Doran-Lasenby ch. 14.
2. The T05 setting note and the equivalence Facts' locator are corrected by the lead.
3. Tractors: carried as the store's own flat-space Cl(2,4) transcription with an exact check (lead).
4. Bifurcation surfaces: as in the section above.
5. GTG is extended to d dimensions (section to follow; the lead restates the 5D and d-dimensional
   entities).

## Needs Leon (answered: see "Leon's decisions")

1. **Curvature sign.** The store's curvature convention (de Sitter Ric = Lambda g in (+,-,-,-),
   `synthesis.einstein-condition-is-infinity-vacuum-incidence`(7); the T05/T06 spectra) is the
   negative of the GTG literature's. The definition object adopts the store's sign,
   \mathcal{R}(B) = -R(\hb(B)), so no stored statement changes sign; the alternative is to adopt
   LDG's sign and re-sign every stored curvature formula. Decide which.
2. **The T05 setting note** (`note.singularity.setting-gauge-theory-exactly`) copies LDG's symbols:
   it writes the background field strength with the script letter and contracts it directly, and
   writes the torsion equation and the rotation law of \hb with \hb where the series' convention
   needs the adjoint \hb^T (C2, C5, Section 1). Correct the note, or let the definition object
   supersede it.
3. **Locator of the equivalence Facts.** `singularity.imported-equivalence-einstein-equations` and
   `interior.imported-equivalence-einstein-equations` cite LDG "\S 7"; LDG's Section 7 is
   "Electromagnetism in a gravitational background". The equivalence lives in Section 4 (4.3,
   covariant forms of the field equations) and Appendix C (the translation of tensor calculus).
4. **Tractors**: decided; see Section 12 (carried by a proved claim with exact checks).
5. **Bifurcation surfaces** (Section 14 item 3): premises (R), (N+) and the de Sitter and Wald
   entropy statements name the Lorentzian bifurcation surface, which no single GTG chart contains.
   Decide whether to restate them on a horizon cross-section in the chart (same area, same
   surface gravity) or to flag them.
6. **Five-dimensional and d-dimensional statements** (the dark-matter warped reductions, the
   induced-equations Fact, Jacobson 2016 in d dimensions): GTG on a flat R^{1,4} background is
   possible but outside this 4D dictionary; keep them in metric language for now?

## Still for Leon (from the lead's restatement pass)

1. **Connection sign (C10).** Stored connection values from Cartan forms (T06 interior, pairing) are
   the right-action values Omega_C = -omega; the T05 PG connection is in the definition's sign. The
   store is coherent (curvature in the Cartan sign everywhere), but a reader setting a stored Omega
   beside a GTG formula must know which. Decide whether to re-sign the Cartan-valued entities or keep
   the rule of C10. **Decided (Leon, 2026-10-23): re-sign; the store displays Omega in the GTG sign
   throughout (C10 as now written; fixer F1 applied it).**
2. **MacDowell-Mansouri 2-form vs operator.** The stored F^{ab} = R^{ab} + l^{-2} e^a ^ e^b and the
   operator form -(\mathcal{R}(B) - l^{-2}B) of the tractor theorem (v) agree in vanishing on de Sitter;
   the relative sign of the l^{-2} term between the 2-form and the bivector operator is the index-lowering
   convention, not checked symbol by symbol. **Closed (referee GR2, 2026-10-23): with C11's
   R(u,v) = -\mathcal{R}(u ^ v) and (e^a ^ e^b)(u,v) acting as (u ^ v).w, F^ab = R^ab + l^{-2} e^a ^ e^b is
   exactly -(\mathcal{R}(B) - l^{-2}B), and in (+,-,-,-) de Sitter has R^ab = -l^{-2} e^a ^ e^b, so F^ab = 0
   there; row 13 and the Fact now use \mathcal{F}(B) = -(\mathcal{R}(B) - l^{-2}B).**

## Proposed additions

(G2's three entries below are accepted into the main tables: Section 1 soldering row, Section 6
coordinate Ricci row, Section 3 synchronous row with the sign corrected per C10.)

(Restaters: add entries here with your name; use them consistently.)

**G2 (restater, 2026-10-23).** Used consistently in the G2 restatements; each follows from rows above.

- *Soldering form and frame map.* An orthonormal coframe (soldering form) is the physical-vector map
  in components, e^a(v) = gamma^a . \hb^{-1}(v); the dual frame map R^{1,3} -> TM is \hb
  (E_a = \hb(gamma_a)). So a corank-one soldering form (`dark-energy.walls-free-sector`) is a locus where
  \hb^{-1} drops rank, while at the sheaf paper's wall (`dark-energy.sheaf-papers-wall-soldering-variables`)
  \hb^{-1} has a half-power pole and \hb drops rank. (Section 1, tetrad row; C2.)
- *Coordinate Ricci components, round-sphere-positive sign.* Ric^o_{mu nu} = -g_mu . \mathcal{R}(g_nu),
  the polarisation of the C6 entry Ric^o(k,k) = -k . \mathcal{R}(k). This is the sign of the standard
  Christoffel formula R_{mu nu} = d_rho Gamma^rho_{mu nu} - ... (used in
  `synthesis.diagonal-kasner-momentum-constraint` and its check).
- *Synchronous diagonal field.* For derived metric d tau^2 - sum a_i^2 (dx^i)^2 with H_i = d_tau log a_i,
  the rotation-gauge field on the orthonormal physical frame is Omega(gamma_i) = -H_i gamma_0 ^ gamma_i,
  Omega(gamma_0) = 0, in the definition's convention (C10; `interior.interior-connection-exactly`,
  Omega(e_i) = -sigma_i B_i, B_i = e_0 ^ e_i); as one-forms omega^{i0} = H_i e^i. (Sign corrected
  2026-10-23 per Leon's C10 decision.)
