# Attack C3B (cluster C3, angle B: adversarial)

Targets: op.counted-mode-energy (which fields form the light-ray sea), op.qft-structural-inputs (three
generations), through the argued test: one-window recurrence of fermion parity with the zeta ordering needs
the sea's chiral central charge c = 0 mod 24.

## Orientation (direct lookups)
- The test is recorded only in the op.counted-mode-energy `known` text ("argued, not filed"); no stored entity
  derives it, no earlier run findings discuss it.
- Q v3 (singularity.q-joint-quasi-freeness-s-wave): the Killing flow at one modular period is the parity
  AUTOMORPHISM psi -> -psi; identifying the real-time recurrence with the Euclidean sign is "part of the
  reading". Automorphism level only: no c-number phase is fixed.
- (N+) v12: the carrier is CAR(L^2(R,du) x K), K arbitrary transverse and internal labels. Fermionic only.
- Window reading v1 (postulate): arrays of (Q), fermionic; fixes the energy constant (null ordering) but
  explicitly "does not fix ... which fields form the sea".
- J3 (hawking.joint-j3-s-wave-reduction): "each four-dimensional massless field", each channel a 2D mode.
- Photon null data (synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators): E_perp, two
  real fields per generator, positive flux; helicity-one pair modes are quasi-spins, not exact bosons
  (synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins): gauge null data are not
  composites of the fermion arrays.
- Spinor good part (synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays): one complex array per
  Weyl field; sixteen channels per generation (slot module V_+, which contains the neutral singlet).
- Higgs: the rung field is recorded as the elementary linear field with TWO doublets
  (synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum).

## Routes
1. (problem's own) Prove the recurrence statement on windows and test whether any stored premise implies the
   exact operator identity U(L) = P (not only the automorphism). Delivers: choice or consequence. Needs: Q v3,
   (N+), window reading, KMS results. Fails if a premise fixes the c-number phase.
2. (other subject: modular forms / 2D CFT) Read U(L) as the T transformation of the array's character at
   tau = i (beta = L = 2 pi/kappa); compare mod 24 (U(L) = P exactly), mod 12 (U(2L) = 1, or U(L) = +-P),
   and the literature (gravitational anomaly mod 24, Z16 Dai-Freed). Delivers: which modulus, prior art.
3. (own: counter-models) The content table: 16 n_g (or 15 n_g) fermion arrays, 2 per gauge boson, 1 per real
   scalar, 2 for the graviton; with light-front data mass-independent. Delivers: n_g = 3 failing / n_g = 1, 4
   passing on contents the store records (two elementary doublets).

## Choice
Routes 1 and 3 together, route 2 for the modulus and prior art. Reason: the adversarial question is whether
the verdict "n_g = 0 mod 3" is a consequence or an artefact; independence plus a store-allowed counter-model
answers it, and both are finite exact computations.

## Kill condition (pre-registered before computing)
The proposal dies if any of:
- K1: a stored premise at its pinned version fixes the c-number phase of the window evolution (implies
  U(L) = P exactly, not only U(L) P^{-1} central), or fixes dim K mod 24.
- K2: exact computation fails: a real chiral boson array's zeta-symmetric sea does not equal the
  null-ordered window value -kappa/24 at integer weights, or equals it at some non-integer offset; or the
  window evolution's phase is not exp(2 pi c/24) times the parity.
- K3: the counter-model is not store-allowed: a proved stored result removes the Higgs (both doublets) from
  the light-ray data (for example, the doublet proved to be exact bosons inside the fermion arrays' Fock space)
  AND the graviton; then only the independence part survives.
- K4: C3A has filed the same statement.

## Established (labels: proved / computed / argued)
Midway (after reading attack-C3A.md): C3A files the recurrence theorem (U = e^{2 pi J n/24} Gamma on windows),
the choice verdict (no stored premise fixes the implementer; KMS blind to the constant), 16 n_g -> 3 | n_g,
15 n_g -> 8 | n_g, and the CCR lemma (boson arrays only at integer weight). I do NOT file those. My proposal
takes the test as given and files the content dependence.

K1 did not fire: Q v3, (N+) v12, window reading v1 are automorphism-level or fix only the zero of energy
(independently confirmed by C3A). K2 did not fire (exact check passes). K3 did not fire: no stored result removes
the Higgs from the light-ray data; the store records the rung field as an ELEMENTARY linear field with eight real
components (two doublets), and the store has no graviton field (gravity enters as an equation of state,
synthesis.einstein-equations-from-c-loc-and-clausius), so eps = 0 is the store's own reading but not a theorem.
K4 did not fire (division agreed with C3A, see their file).

- PROVED (GA, exact): a real scalar component's null data on N_k are one real field per generator for every
  potential: div(f1 grad f2 - f2 grad f1) = f1 box f2 - f2 box f1 identically, V'' symmetric cancels, flux
  k.omega = f1 (k.grad) f2 - f2 (k.grad) f1 (no potential, no transverse derivative), box = (k.grad)(m.grad) -
  d1^2 - d2^2. So c = 16 n_g + 2 n_V + n_s + 2 eps for every mass matrix and potential.
- PROVED (arithmetic, complete over a period): with n_V = 12 and n_s = 4 n_h:
  one-window test (24 | c) iff eps = 0 and n_h = 2 n_g (mod 6);
  two-window test (12 | c, U(2L) = 1, the weaker operator-level recurrence) iff eps = 0 and n_g + n_h = 0 (mod 3).
  * The twelve gauge vectors contribute 24: they drop out of both tests (a d-dim algebra drops out iff 12 | d,
    resp. 6 | d; so(10) with 45 would not). The recorded "integer-weight fields fail" is entirely the Higgs (4)
    and the graviton (2), not the gauge bosons.
  * Graviton in: c = 2 mod 4, both tests fail for every n_g, n_h.
  * One doublet: one-window never; two-window at n_g = 2, 5, 8 (c = 60 at n_g = 2: U(L) = -P, U(2L) = 1).
  * Two doublets (the store's linear rung field): both tests at n_g = 1, 4, 7; n_g = 3 FAILS (c = 80).
  * No scalars (or n_h = 0 mod 6, resp. 0 mod 3): 3 | n_g.
  So counter-models found: n_g = 3 failing (two doublets) and n_g = 2 passing (one doublet, two-window).
- PROVED: per-generation count f alone: one-window iff 24/gcd(24, f) | n_g; the modulus is 3 exactly when
  f = 8 or 16 (mod 24). So the "3" is the 3 in 24 = 8 * 3 against a power of 2: the light-ray count 16 and the
  Majorana-Weyl count 8 of the literature give the same verdict, and 15 gives 8 (one-window) or 4 (two-window).
- PROVED: boson-fermion balance (b = 2f, the vanishing of the stored quartic Sakharov coefficient
  2N_V + N_S - 2N_W) gives c = 3f = 48 n_g: both tests pass for EVERY n_g; at n_g = 3 this is N_S = 72, c = 144.
- ARGUED (not filed): the recurrence condition, if imposed on the whole window evolution of a hole, includes the
  label's constant M: phase L M = 8 pi M^2 = A/2 = 2S. With S = (number of arrays) (ln 2)/2 (half ln 2 per (Q) v3
  array) recurrence would need S in pi (Z + c/24), i.e. ln 2/pi rational, false by Gelfond's theorem (e^pi
  transcendental; literature, from memory). So the condition can only be posed on the sea, not on the hole's
  Hamiltonian: a selective premise.
- ARGUED: under Higgs breaking the null-data count is unchanged (3 Goldstones become 3 longitudinal data:
  2*9 + 3*3 + 1 = 28 = 24 + 4).
- Prior art (web, 9 Nov 2026): J. Wang, arXiv:2312.14928 (c_- = 8 per family of 16 Weyl as Majorana-Weyl on a
  domain wall, framing anomaly c_- = 0 mod 24 gives N_f in 3Z; 45/15 needs an extra 3/2 sector); I. Garcia-
  Etxebarria and M. Montero, arXiv:1808.00009, JHEP 08 (2019) 003 (Z16 Dai-Freed anomaly, 16 per generation);
  Z. Wan, J. Wang, S.-T. Yau, arXiv:2605.26202 (mod-3 Pontryagin route). Difference: their c_- is the NET 4D
  chirality and is blind to bosons and vector-like pairs; the light-ray count counts every field's null data, so
  it is fragile exactly where theirs is robust.

## Proposal ids
- synthesis.light-ray-recurrence-test-verdict-on-generations-is-set-by-the-scalar-content (FILED, op.counted-mode-energy;
  bears on op.qft-structural-inputs). Gate: runcheck 5/5 pass; validate_one ok, no findings; check4 exit 0,
  0 errors, 0 other findings (no W413); log work/C3B/check4.log. coverage.yaml copied into proposals/<id>/.
- Possible overlap for the orchestrator: clause (iv) contains, as one instance of the general per-generation rule,
  "15 per generation, one-window iff 8 | n_g", which C3A also states. Everything else was divided with C3A.
- Not filed separately: the independence ("a choice, not a consequence") statement; C3A's proposal carries its
  substance (conjugation by U is the parity automorphism for every n; KMS blind to the constant). One proposal.

## Kill condition outcome
None of K1 to K4 fired.

## What I could not establish
- Which fields form the sea: the store does not decide it. (N+) v12 is a CAR premise; the photon null data are
  proved but no stored premise places them (or scalar data) in a null ground state; J3 speaks of "each massless
  field" but in its s-wave sector helicity-1 and 2 fields have no channel (l >= |h|), which would drop vectors and
  graviton but keep scalars (argued, not checked; with one doublet that reading fails the one-window test for
  every n_g).
- Anything that fixes 3 rather than 6, 9: neither test can.
- The non-abelian vector count is argued from the free field, component by component.

## Unexpected links
- Sakharov (synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations): its
  quadratic coefficient gives N_g = 3 (12 = 4 N_g) on the SAME count (16 per generation, 12 vectors) as the
  light-ray test, independent of scalars; its quartic coefficient vanishes at N_S = 72, and at that balance the
  light-ray c = 144 passes. In general boson-fermion balance makes c = 48 n_g, so the two "threes" are compatible
  only on the balanced content, where the light-ray test is blind to n_g. The Sakharov three is the stronger lead.
- C1 (op.helicity-per-boundary-mode, J3): if the sea is J3's s-wave sector, vectors and graviton contribute no
  channel and scalars do; the verdict then turns on the doublets alone (one doublet: one-window never).
- C2 (Sugawara split 32/7 + 2 + 1 + 1 + 52/7 = 16): the gauge currents' Sugawara parts live inside the sixteen
  fermion arrays; independent gauge null data are additional (helicity-one pair modes are quasi-spins, not exact
  bosons), so counting both the 16 and the 24 is not double counting.

## Decisions for Leon
1. The scope of (N+) / the light-ray sea: CAR null data only (as stored), or every field's null data (vectors,
   scalars, possibly the graviton's helicities). Recommendation: do not extend (N+) to settle a numerology test;
   if extended, the test's verdict follows from the filed table, and with a graviton it fails for every content.
2. Should the recurrence (U(L) = P, or the weaker U(2L) = 1) become a premise at all? Recommendation: no, not as a
   premise. It is a choice (C3A), it can only be posed on the sea and not on the whole hole Hamiltonian (the label's
   window phase 2S would need ln 2/pi rational; argued, Gelfond's theorem cited from memory, would need importing
   as a Fact if ever used), and on the store's own scalar content (two doublets) it rejects three generations.
   Record it as a test, with the table.
3. If the argued remark on the label phase is to be stored, import Gelfond's theorem (e^pi transcendental) as a
   Fact first (maintainer-only).
