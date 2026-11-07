# Attacker GB (cluster G, adversarial and cross-pollinating)

Status: done. Two proposals filed (bos.gauge-bosons, bos.dimension); op.r-premises-external recorded here only.

## Proposals
1. `synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins` (open_problem bos.gauge-bosons).
   validate_draft ok (no warnings); check4 0 errors, 0 findings, check pass; registered with propose_claim; coverage.yaml
   copied in.
2. `synthesis.density-modes-bosonise-only-along-one-null-direction` (open_problem bos.dimension).
   validate_draft ok (no warnings); check4 0 errors, 0 findings, check pass; registered; coverage.yaml copied in.

## Overlap with GA (read before refereeing)
GA filed `synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators`. Its (iv) (two-channel u(2)
window identity), (v) (densities are exact helicity-0 bosons) and (vi) (flip currents not canonical on one generator,
defect bound across generators) overlap with proposal 1. Proposal 1 adds: arbitrary finite channel content and
arbitrary weights; the criterion "canonical on edge-clean vectors iff the channel matrix is normal"; helicity +-1 forces
nilpotency hence non-normality; no rotation doublet of commuting canonical pair modes (normal-nilpotent argument on
M_1 -+ J M_2); the exact quasi-spin structure (|B^p Omega|^2 = (p!)^2 e_p, zero beyond q rank(M) quanta, strictly
sub-Bose for p >= 2); the Krein positivity clause. GA's contraction bound across generators is consistent with
proposal 1's quasi-spin with q rank(M) sites (no counterexample in either direction). Recommendation: cross-reference,
not merge (GA agrees in its findings).

## Target bos.gauge-bosons (proposal 1)
Routes: R1 positivity obstruction to Gupta-Bleuler; R2 helicity of pair modes (chosen, computed); R3 locality of the
Coulomb-gauge pair (argued only, below). Kill conditions KG1/KD3/KD4 pre-registered; none triggered.
Established:
- proved + computed: window identity [rho_q(M), rho_q(M')*] = sum_{k,k+q in I} a*_k M M'* a_k - sum_{k,k-q in I}
  a*_k M'* M a_k; edge-clean value q tr(M'* M) + rho_0([M, M'*]).
- proved + computed: canonical on edge-clean vectors iff [M, M'*] = 0 (iff M normal for M = M').
- proved + computed: helicity h about the generator iff [W, M] = h M; h = +-1 forces M nilpotent, never normal; the
  flip E_{+-} has commutator q + (channel-number difference) (values q +- 1 computed); no doublet of linear
  polarisations of commuting canonical pair modes.
- proved + computed: on the chiral sea a nilpotent rank-r mode at momentum q is a quasi-spin of q r two-level sites:
  |B^p Omega|^2 = (p!)^2 C(q, p) for the flip (q = 1, 2 computed), B^{q+1} Omega = 0, [rho_q, B] = q - 2p on the orbit;
  the same-channel density at q = 1 has |D^2 Omega|^2 = 2 (Bose value).
- proved: annihilators of any positive tower state have nonnegative commutator, so no pair mode is the timelike
  Gupta-Bleuler mode of (K1); (KF) is not obtainable from tower fluctuations.
- argued (R3, not filed): the Coulomb-gauge canonical pair (A_perp, E_perp) has a transverse-delta commutator that is
  nonzero at spacelike separation, while even pair densities at distinct sites commute; so A_perp and E_perp cannot
  both be local pair densities, while F = E + I4 B (local commutator) could. Not computed.

## Target bos.dimension (proposal 2)
Routes: R1 strip identity in d dimensions (chosen); R2 channels on a generator (in proposal 1); R3 Haldane patches
(not done; patch-edge corrections not computed). Kill conditions KD1, KD2 pre-registered; not triggered.
Established:
- proved + computed: [rho_q, rho_q*] = n(E_-(q)) - n(E_+(q)) on any window W in Z^d with |E_-| = |E_+| (2D windows in
  the algebra, counting up to d = 3 and an irregular window).
- proved + computed: zero density form for every state with uniform total occupation on the strips (relativistic
  sea: one filled state per momentum, any d; the 1+1 Dirac sea of both chiralities, each chirality alone giving
  +-min(q, 2N - q)) and for bounded seas away from the edges.
- proved + computed: half-space sea {k_1 < 0} on the cube: c min(q_1, 2N - q_1) prod_j (2N - |q_j|); zero for
  transverse q.
- proved + computed: the density-current term of the two-component relativistic sea equals sum over the strips of
  |k_d|/|k|: 2q for d = 1; in (4qN(N - q), 8qN^2] for d = 3 (cut-off squared, at the window edge). The lower-band
  spin expectation -k/|k| is the Pauli-algebra projector identity (checked at rational unit vectors).
- not in proposal 2 (GA's computation, offered to the fix round): on a transverse torus with graph seas
  k_1 < h(k_perp), edge-clean in every column, the value is q_1 |T| independent of q_perp and h (one line from (i):
  only direction 1 has strips).

## Target op.r-premises-external (new angle; recorded, not filed)
Routes R1 inner flip (chosen), R2 spectral positivity (chosen), R3 flag bit (cross-link only). KR1, KR2 not triggered.
Established (computed in work/GB/flip.py, N = 1, 2, 3):
- u = Gamma g1 is unitary (u u* = 1, u^2 = -1), commutes with every transport generator, fixes g1, sends g2 -> -g2,
  J -> -J, I_n -> -I_n; every unit combination Gamma(alpha g1 + beta g2) does the same (3/5, 4/5 checked). So the
  orientation flip is inner and fixes every fermion operator and every state on them.
- proved (by hand, not filed): every automorphism of the level fixing the transport subalgebra pointwise is Ad(x)
  with x a unit of the commutant H = span{1, J, Gamma g1, Gamma g2} (it preserves H, acts on its imaginary part as a
  rotation, and the level is generated by transport and Gamma g1); the parity-preserving ones are O(2): rotations about
  J (fix J) and half-turns Ad(Gamma(alpha g1 + beta g2)) (reverse J). Checked: the non-homogeneous unit
  (1 + J + Gamma g1 + Gamma g2)/2 fixes transport and maps J to the odd element Gamma g1 (N = 1, 2). So relative to all
  fermion data the even unit is fixed up to its sign and nothing else.
- argued: bosonic positivity selects the sea given the orientation (the polarised/bottom-filled state has
  omega([phi, pi_J]) = +2JM, the reversed one -2JM), and the inner flip maps the J-dynamics to the time-reversed one
  while fixing the state; so positivity of boson energy is the fermionic ground-state clause read on pairs and leaves
  the orientation free. This is U's (vi) (the flip) plus GA's clause (vii) (the sign); the O(2) classification is the
  only addition and was not filed (two-proposal cap). Recommendation: one sentence in op.r's "known".

## Unexpected links
- Proposal 1 (v) with premise (KF): the Krein form cannot come from tower fluctuations; it stays a premise.
- Proposal 2 with synthesis.imported-schwinger-term-and-mattis-lieb-density-algebra (ii)-(iii): both imported clauses
  are derived on windows and sized there (zero for finite and relativistic seas; Schwinger term at the cut-off).
- Proposal 1 (iv) is field-theory.how-close-tower-comes-ccr with n = q rank(M): the helicity-one composites are the
  same contraction as the stored quasi-spin ladder.
- GA's contraction across generators (its (vi)) and SA's central limit of fluctuation states are the same limit; a
  bridge test could upgrade GA's mean-square statement to convergence of states.

## Decisions for Leon
1. Proposal 1 and GA's photon proposal overlap on the single-generator part: cross-reference (recommended) or merge.
2. Accept that exact composite bosons of the null vacuum are helicity zero and per generator (proposals 1 and 2), so the
   photon stays elementary (field-theory.fock-space-maxwell-modes) and (KF) stays a premise? Recommendation: yes.
3. op.r-premises-external: record that bosonic positivity adds no datum and that the J flip is inner (Ad(Gamma g1)),
   with the O(2) classification; no proposal filed for it. Recommendation: one sentence in "known", citing U's (vi) and
   GA's (vii).
4. Literature cited from memory (prior art only, not premises): Frenkel and Kac 1980; Pressley and Segal 1986; Schwinger
   1959; Haldane, Houghton and Marston, Castro Neto and Fradkin (patch bosonisation). Verify if they are to be imported.
