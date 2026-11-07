# attack-SA (constructive, cluster S)

Status: done. Two proposals filed (both check4 0 errors 0 findings, validate_draft ok). Labels: proved / computed / argued / conjectured.

## Orientation (direct lookups)
- Stored: synthesis.fluctuation-forms-...-null-vacuum (v1): (i) collective single-fermion sums are one fermion; (vii)
  fluctuation commutator tends to sigma_omega in mean square; real states give sigma = 0 on self-adjoint pairs, so a Weyl form
  needs a central unit (absent in the block's even algebra). Item 4 (filer U): the kernel J = g1 g2 of Cl(N, N+2) is that unit.
- Cl(N, N+2) at N = 1 is Cl(1,3): kernel plane = transverse plane e2 e3, J = the transverse bivector of
  synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom (phase flow v -> e^{-Jt} v there).
- Sugawara is only an imported Fact (dark-energy.imported-conformal-orthogonality-sugawara-construction); no Kac-Moody,
  Luttinger-model or dispersion entity. Current algebra with edge split: hawking.current-commutator-exactly-edge-split.
- (Q) version 3 weights omega_k = kappa (k + 1/2) (half-integer offset).

## bos.spin-statistics
Routes: R1 kernel rotor acting on modes by left multiplication (U_theta = exp(theta J Nhat/2)); R2 modular/Kuckert (store,
continuum); R3 Pauli locality (store, continuum); R4 Klein twist inside the level. Chose R1 + R4.
Kill condition (pre-registered): U(2 pi) != Gamma, or U not unitary/CAR-preserving, or a half-integer-weight element
commuting with a disjoint copy, or a collective pair mode of half-integer weight. NOT triggered.
Established (computed exactly, m = 1, 2, 3; proved in the dropped draft):
- U_theta = prod_j (1 + (e^{theta J/2} - 1) n_j) unitary group; Ad U_theta w_j = e^{-theta J/2} w_j (left action of the
  rotor that turns the kernel plane through theta: R g1 R~ = cos g1 - sin g2); U_{2 pi} = Gamma; U_pi^2 = Gamma; J Gamma = I
  (level pseudoscalar, sign +1 in the order g1 g2 e1 f1 ...); Klein twist V = (1 + I)(1 + J)^{-1} unitary, V^2 = Gamma.
- At m = 1, Ad U_theta = tau_{-theta/2}, the radial atom's phase flow.
- Weights: modes 1/2, hopping, density, phi, pi 0, pairing 1.
- Graded locality: odd copies anticommute, even commute; collective bracket of matching kind = block sum; LLN for the
  anticommutator of odd fluctuations (mean p2, variance p2(1 - p2)/N for x = w_1 n_2); trace over span{1, J} forbids a
  canonical commutator at finite N (not a canonical anticommutator).
Sibling SB filed synthesis.ladder-bosons-inherit-spin-statistics-from-the-single-modes, which contains U_s(theta) =
exp(theta J L_s) for arbitrary spin data (mine is s_j = 1/2 for all j), U(2 pi) = Gamma iff all s_j half-integer, graded
locality, and a counter-model. So I DROPPED my kernel-turn/weights clauses (work/SA/dropped/) and kept only the collective
brackets + trace asymmetry, merged into proposal 1 as clause (i). Not filed: the Klein twist from I and the m = 1 phase-flow
identification (small; listed below for Leon).

## bos.qclt-states
Routes: R1 exact factorisation of Weyl characteristic functions over commuting blocks + ordered cumulants + l1 bound;
R2 Cushen-Hudson moments; R3 Holstein-Primakoff polarised state. Chose R1 (R3 as cross-check, included as clause (iii)).
Kill condition (pre-registered): factorisation fails for non-commuting x within a block; J-extension not positive; limit
fails the Weyl relation; third cumulant not exactly N^{-1/2}. NOT triggered.
Established:
- proved + computed: omega_N(prod W_N(x_j)) = [omega(prod e^{J y_j/sqrt N})]^N; ordered cumulants kappa_N = N^{1-k/2} kappa
  (computed exactly for k = 2, 3, 4, six ordered lists incl. non-commuting phi, pi, chi, on N = 1, 2, 3 blocks);
  kappa_2(phi, pi) = J(p1 - p2), kappa_3(n) = p(1 - p)(1 - 2p) != 0 (rate attained).
- proved: |omega_N(prod W_N) - e^{-c}| <= (r^3/6) e^{r/sqrt N} N^{-1/2} + (r^4/8) e^{r^2/2N} N^{-1}, r = sum ||y_j||_1
  (blades unitary => |omega(x)| <= ||x||_1); limit = quasi-free state with covariance s and form sigma = omega([x, y]) in J R;
  positivity; uncertainty |sigma|^2 <= 4 s s.
- computed: polarised blocks: omega(B^k B*^k) = k! prod(1 - l/N), normal order 0, kappa_3 = 0, kappa_4 = -2/N; uncertainty equality.
Proposal: synthesis.central-limit-of-tower-fluctuation-states-with-the-kernel-unit (filed; check4 0 errors 0 findings;
validate ok). extraction.open_problem: bos.qclt-states.

## bos.dynamics
Routes: R1 finite-window Kronig/Sugawara; R2 import (excluded); R3 Luttinger with real hyperbolic Bogoliubov. Chose R1 + R3.
Kill condition (pre-registered): k-dependent remainder in [H, rho_q]; Sugawara failing on some away-from-edge state;
Luttinger commutators not closing. NOT triggered; result stronger than pre-registered expectation.
Correction to my own first sketch: the coefficient of rho_q* rho_q is 1, not 1/q (SB flagged the same).
Established:
- proved + computed (GA, every element, windows L = 1..6): sum_{q=1}^{L-1} rho_q* rho_q = sum_j j n_j - Nhat(Nhat - 1)/2,
  an algebra identity with NO edge correction; sea form sum_k (k + 1/2) n_k + M^2/2 = Q^2/2 + T. Proof: the quartic part
  is a sum over a* a* a a with alpha + beta = gamma + delta; the full sum vanishes by antisymmetry, the diagonal part is
  -Nhat(Nhat - 1), so the alpha > gamma part is Nhat(Nhat - 1)/2.
- proved: [H, rho_q*] = q rho_q* (linear dispersion) exactly; Ad e^{JtH} rho_q* = e^{Jqt} rho_q*; fails for j^2 weights.
- proved: band compression of P has weights Delta (k + 1/2) (the half-integer offset of (Q) v3 appears as the band centre);
  the null vacuum's window sea is the ground state, Q = 0.
- proved on D, computed on windows: Luttinger g4, g2 coupling (finitely many q): normal modes beta* = rho_R* + r rho_L,
  g2 r^2 - 2(1 + g4) r + g2 = 0, frequency q sqrt((1 + g4)^2 - g2^2); on windows exact on vectors edge-clean at the coupled
  depth in both branches, fails off them (computed: g4 = 1/2, g2 = 9/10, r = 1/3, omega = 6/5, 16 vectors, beta and gamma).
Proposal: synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves (filed; check4 0 errors
0 findings; validate ok). extraction.open_problem: bos.dynamics. SB computed the same window identity independently
(work/SB/sugawara_session.py, their K5 fired) and does not file it.

## Unexpected links
- The half-integer offset of the (Q) weights kappa (k + 1/2), which the store reads as "spinor fields of boost weight 1/2,
  a reading and not a consequence", appears exactly as the band centre of the compression of P on band modes of width Delta.
  With these weights the window Sugawara identity has no linear Q term (H = Q^2/2 + T).
- J Gamma = I (level pseudoscalar) makes the Klein twist of the stored modular spin-statistics entity (iv) the level's own
  element: V = (1 + I)(1 + J)^{-1}, V^2 = Gamma.

## End read of SB
SB filed synthesis.ladder-bosons-inherit-spin-statistics-from-the-single-modes (spin side) and
synthesis.ladder-states-are-locally-product-with-non-gaussian-fluctuations (qclt counter-model: ladder number states).
No overlap with my two filings: my qclt result assumes product states, theirs shows the hypothesis cannot be weakened to
local convergence; the two are complementary. My proposal 1 note cites SB's spin proposal id as a companion.

## Decisions for Leon
1. Spin on the ladder: whether to adopt "every transport mode is a spinor of the kernel plane" (one rotor e^{-theta J/2}
   acting on all modes by left multiplication) as the definition of spin in the tower. With it, U_{2 pi} = Gamma and the
   spin-statistics connection holds exactly at every N; without it, spin is per-mode data (SB's proposal). At m = 1 the
   kernel turn is the transverse rotation about the radial direction (exact); for m > 1 it is a reading. Recommendation:
   adopt as a definition, stated as such, not as a derivation.
2. Whether the band-centre reading of the half-integer offset in (Q) should be recorded as a note on
   singularity.q-joint-quasi-freeness-s-wave (maintainer edit; I did not touch it).
