# attack-SB (adversarial, cluster S)

Status: done. Labels: proved / computed / argued / conjectured. Proposals filed: 2 (cap 2).

**Counterexamples to SA's claims: none found.** My earlier note warned that SA's planned window Sugawara might claim an
edge failure (and a coefficient 1/q). SA's filed check uses the whole-window identity T = sum_q rho_q* rho_q with
coefficient 1, which agrees with my computation, so the warning no longer applies. I spot-checked SA's
synthesis.central-limit-of-tower-fluctuation-states-with-the-kernel-unit (ii)(d): s(phi, phi) = p1 + p2 - 2 p1 p2 and
sigma(phi, pi) = 2J(p1 - p2) agree with the block values, and the positivity bound (p1 - p2)^2 <= (p1 + p2 - 2 p1 p2)^2
holds for all occupations (the gap is 2 p2 (1 - p1) >= 0 for p1 >= p2). My proposal 2 bounds SA's result from outside
(the hypotheses cannot be weakened); it does not contradict it.

## bos.spin-statistics

Orientation. The store holds spin-statistics from locality for the attached free fields
(synthesis.locality-of-the-attached-free-fields-fixes-their-statistics) and the modular route (wedge reflections,
Guido-Longo and Kuckert, which are imported). Nothing covers the ladder itself.

Routes: (1) the kernel rotor exp(theta J/2) as the definition of spin; (2) the diagonal mode rotation
U(theta) = exp(theta J L), L = sum s_j n_j; (3) locality (store) as the cross-link; (4) the level's own rotors.
Choice: route 2, with 1 and 4 as the no-go part and 3 as the cross-link.
Kill conditions K1 to K3, registered before computing: NONE fired.

Established:
- PROVED and computed (N = 1, 2, 3; all 5^N weight assignments in {-1/2, 0, 1/2, 1, 3/2}): U(2 pi) = prod of e_j f_j over
  the half-integer modes. Ad U(2 pi) = Ad Gamma if and only if every s_j is half-integer, and then U(2 pi) = Gamma
  exactly. In that case every even element (hopping, pairing, density, collective sums) has integer spin and Bose
  statistics at every N, with no limit needed.
- PROVED and computed: a COUNTER-MODEL. Give each block a spinor lower mode and a spin-0 upper mode. The hopping
  element then has half-integer spin, commutes across blocks, and its normalised sum climbs the stored
  Holstein-Primakoff ladder ([B, B*] = 1 - 2k/N, checked for N_b = 1..3). In the limit this is a boson of half-integer
  spin. The spin-0 mode is a fermion of integer spin.
- PROVED: the tower's own rotations give integer spin to everything. Ad exp(phi J) fixes the transport algebra. The
  real rotation of two modes has L = (e0e1 - f0f1)/2, weights +-1 and exp(2 pi L) = 1.
- Conclusion: the collective limit neither produces nor repairs spin-statistics. It holds for the bosons exactly when it
  holds for the single modes, and the single-mode spinor assignment is a datum. For the attached free fields that datum
  comes from locality with a positive norm, a continuum input (ARGUED by citing the store).
Proposal: synthesis.ladder-bosons-inherit-spin-statistics-from-the-single-modes (check4 0 errors 0 warnings; validate ok).
SA dropped its overlapping kernel-turn clauses in favour of this one (see attack-SA.md).

## bos.qclt-states

Routes: (1) a moment/partition proof for product states (constructive; SA's, not filed by SB); (2) a counter-model using
the Holstein-Primakoff ladder states; (3) the Weyl unit I_n = J Gamma instead of J (ARGUED only, not computed: in
mixed-parity product states it gives a mixture of the Gaussian and its J-conjugate); (4) sharpness of N^{-1/2}
(SA covers it with kappa_3).
Choice: route 2. Kill condition K4: NOT fired.

Established (PROVED, computed for N = 1..4 in the session and N = 1..3 in the check):
- With psi_k = (K*)^k P_pol: K psi_k = k(N - k + 1) psi_{k-1}, and
  omega_k(B*^m B^m) = (k)_m (N-k+1)(N-k+2)...(N-k+m)/N^m, which is 0 for m > k. Off-diagonal moments vanish.
- Every finite marginal tends to the polarised product state. The weight of m blocks off the polarised projector is
  <= km/(N - k + 1); the polarised projector is minimal, so by Cauchy-Schwarz |omega_k(X) - omega_0(X)| <= (2 sqrt(eps) + eps)||X||.
- Pair correlations are k(N - k)/(N(N - 1)) for every pair of blocks; summed over partners they give k(N - k)/N -> k.
- The limit fluctuation state is the k-boson number state. It is not quasi-free for k >= 1: k(k-1) against 2k^2.
- Conclusion: the local limit state does not fix the fluctuation limit. The QCLT for states needs the product structure
  (or uniform clustering) at each N. The tower's boson number states are the ladder vectors, not fluctuations of product states.
Proposal: synthesis.ladder-states-are-locally-product-with-non-gaussian-fluctuations (check4 0 errors 0 warnings; validate ok).

## bos.dynamics

Route 2 (an obstruction to Sugawara on finite windows) was chosen. Kill condition K5 FIRED, so the obstruction is dead
(COMPUTED, M = 2..7):
- Allowing both orderings, the identity holds trivially, because edge commutators are linear in n.
- With the normal-ordered form alone, H0 = sum_j j n_j = sum_{q=1}^{M-1} rho_q* rho_q + N(N-1)/2 holds EXACTLY on every
  window, with [H0, rho_q] = -q rho_q. Equivalently, with weights j - M/2 + 1/2,
  H = Q^2/2 + sum rho* rho - M^2/8, where Q = N - M/2.
- Outline of a proof (ARGUED): the quadratic part of sum rho*rho gives sum_j j n_j, and the quartic part gives the
  charge term.
- Consequence: the density-wave dynamics need no limit. Only the canonical normalisation of [rho_q, rho_q*] does.
  This is SA's target and SA's dynamics proposal carries it; SB does not file it.
Script: work/SB/sugawara_session.py.

## Unexpected links
- The 2 pi rotation of the ladder is a product of plane volume elements e_j f_j: tower.volume-elements-planes is the
  spin object.
- The spinor assignment of tower modes is the content the locality result
  (synthesis.locality-of-the-attached-free-fields-fixes-their-statistics (iii)) supplies to the ladder.
- The boson number states (and so any "one-photon" state of a density wave) live on the ladder vectors, which are
  exchangeable but not product states. QCLT (SA) gives only quasi-free states.

## Decisions for Leon
1. Spin on the ladder is a datum, not derived. Recommendation: record it as such and take the spinor assignment of tower
   modes from the stored locality result (continuum input). Do not present spin-statistics of the collective bosons as
   a consequence of the ladder alone.
2. Whether the series wants a premise or note saying that tower modes are spinors of the transverse plane: it would make
   the bosons' integer spin a theorem on the ladder. Recommendation: a note citing the twistor attachment and locality
   rather than a new postulate.
3. Route 3 of qclt (using the level pseudoscalar I_n as the Weyl unit gives a parity mixture, not a Gaussian) was argued
   but not checked. It supports the rule never to identify I_n with J. Worth a short check in a later run if wanted.
