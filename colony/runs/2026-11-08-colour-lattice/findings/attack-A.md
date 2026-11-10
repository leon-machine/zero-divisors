# Attack A (constructive): the colour rotor lattice

Target: op.qft-non-abelian-gauge-fields, attack item "Colour"; RUN.md questions (1) and (2).

## Orientation (read)
- synthesis.weak-factor-rotor-lattice-strong-coupling-area-law (format copied: SU(2) rotors of Cl(3,0), finite-group
  designs for Haar moments, tree gauge + Haar change of variables, (beta/4)^A; weight exp(beta <U_p>_0)).
- Colour block of synthesis.field-level-brst-differential-of-the-derived-gauge-fields-is-nilpotent: su(3) = the
  eight traceless bivectors of the e3..e8 block commuting with J = e34 + e56 + e78 (gen(3)..gen(8) of Cl(9,0)).
- Fact synthesis.imported-wilson-lattice-gauge-theory-and-strong-coupling-confinement (i) beta = 2N/g^2 checked,
  (ii) Osterwalder-Seiler, (iii) Elitzur, (iv) compact U(1).
- Sibling B (findings/attack-B.md, read at start): B's route 2 uses Delta(96) as a counter-model (finite group with
  the same strong-coupling coefficients). Overlap risk: the Haar-moment derivation. Division proposed: A files the
  SU(3) construction, the derived Haar moments and the strong-coupling coefficients; B files the counter-model
  statement (finite G versus SU(3)) and does not restate the Haar derivation as its result.

## Routes
1. (Problem's own) Wilson lattice with colour rotors; Haar moments derived by invariant theory: for a finite
   subgroup G of SU(3), the G-average and the Haar average of a tensor power are both orthogonal projectors onto
   invariants; SU(3)-invariants are contained in G-invariants; exhibit the su(3)-annihilated tensors (delta, J in
   degree 2; Re/Im of the J-complex volume form in degree 3) and show the G-invariant dimension equals their number
   -> equal projectors, exact. G = Delta(96) = J-commuting signed permutations of e3..e8 times quarter turns, all of
   whose rotors are rational. Delivers degree <= 3 exactly. Fails if G has extra invariants (kill A1).
2. (Other subject: spinors) Spin(6) = SU(4) acting on the minimal left ideal of the pure-spinor idempotent E;
   SU(3) = stabiliser of E (RE = E); fundamental character from the scalar and pseudoscalar parts of the rotor,
   chi = 4<R>_{0+6} - 1 (the 4 = 3 + 1). Delivers the det = 1 condition at rotor level and the rotor form of the
   action. Needs a torus (conjugation) argument. Used inside route 1, not alone.
3. (Own) Weyl integration on the maximal torus with exact Fourier coefficients: gives every moment and higher orders
   of u(beta) = beta/18 + ..., but rests on the Weyl integration formula (an import). Rejected for the core.

Choice: route 1 with route 2 for the construction (det = 1 in GA, rotor form of the plaquette action).

## Pre-registered kill conditions (written before computing)
- A1: the G-invariant subspace of (R^6)^{x k} has dimension other than 0, 2, 2 for k = 1, 2, 3, or the su(3)
  annihilated subspace is not spanned by delta, J (k = 2) and Re Omega, Im Omega (k = 3) -> the derivation of the
  Haar moments by this G dies (fall back to another G or degrade).
- A2: the leading coefficient of the 1x1 or 2x1 fundamental loop with weight exp((beta/3) Re tr U_p) is not
  (beta/18)^A -> claim (v) dies.
- A3: 4<R>_0 - 1 differs from Re tr of the vector action (half the real trace) on any element of the lift -> the
  rotor form of the action is dropped.
- A4: glueball: the tube coefficient of the plaquette-plaquette connected correlator at separation t is not
  (1/2)(beta/18)^{4t} for Re tr observables, or a connected contribution of lower order exists -> the decay-rate
  clause is dropped to "argued".

## Kill conditions: outcome
A1 did not fire (G-invariant dims 0, 2, 2; su(3)-fixed tensors delta, j, Re/Im Omega). A2 did not fire (1x1 = 1/18,
2x1 = 1/324 in tree gauge over G; 1x1, 3x1, 2x2 = 18^-1, 18^-3, 18^-4 by contracting the degree-2 moment). A3 did not
fire (4<R>_0 - 1 = Re tr on all 96 elements and 36 conjugated torus rotors). A4 did not fire (tube 18^-5, 18^-9 for
t = 1, 2; lower orders excluded by a proof, the slab argument).

## Overlap with B and re-centring (orchestrator, midway)
B filed synthesis.a-finite-subgroup-of-colour-shares-its-strong-coupling-expansion-through-link-degree-three (su(3),
Delta(96), Haar = G-average to degree 3, gluing 1/3, (beta/18)^A for 1x1, 2x1, ln z series, degree-4 discrepancy) and
synthesis.colour-triplets-give-the-fundamental-colour-loop-a-perimeter-law-at-strong-coupling. My first draft
(synthesis.colour-rotor-lattice-haar-moments-and-strong-coupling-coefficients) headlined the Haar moments: withdrawn
before filing. Re-centred on what B does not have; the moments stay inside my check as a lemma (clause (iii)),
because a proposal cannot cite a proposal. The degree-4 remark and the "finite G shares the expansion" reading were
removed from my text.

## Established (labels)
Proposal (filed): synthesis.colour-centre-flux-bounds-polyakov-lines-and-the-leading-glueball-tube
- (i) proved + computed: colour rotors = rotors of the block with RE = E, E = prod (1 + I P_k)/2 the pure-spinor
  idempotent; {B : BE = 0} = su(3) exactly (computed); RE = E implies R commutes with J (proved: f(J) - J in su(3),
  orthogonal to J, same norm) and det = 1 (proved: exp(-phi J/2) E = exp(3 phi I/2) E); at vector level det = 1 iff
  f(Re Omega) = Re Omega (proved; quarter turn j sends Re Omega -> -Im Omega, computed).
- (ii) proved (torus) + computed: chi = 4(<R>_0 + <R>_6) - 1 (I standing for j); Wilson weight exp(beta w),
  w = (4<U>_0 - 1)/3, so 1 - w = (4/3)(1 - <U>_0): the action is the scalar part of the plaquette rotor, as for SU(2).
- (iii) lemma, proved + computed: degree 1, 2, 3 moments (cubic = (Re Omega Re Omega + Im Omega Im Omega)/24, wedge
  form /4), int R dR = E (new: left-regular invariants dim 8 = E Cl+), character moments and gluing on G x G.
- (iv) proved + computed in Q(sqrt 3): centre rotor z = -prod(1/2 - (sqrt3/2) P_k), zE = E, z^3 = 1, central,
  w(z) = -1/2; N-ality vanishing; single-link centre change => Z3 two-chain of charges on every surviving term.
- (v) proved: projection of the Z3 chain onto the loop's plane => no term of order < A for every R x T rectangle,
  unique order-A term, leading (beta/18)^A (tree gauge + gluing). N-ality zero: three coincident lines joined by
  the volume form = 1 identically. Adjoint perimeter screening: argued only.
- (vi) proved + computed: <P> = <PP> = 0 at every beta (global centre); <P(x) P(y)bar> = (1/9)(beta/18)^(N_t r)
  (computed N_t = 1, 2 at r = 1); baryonic junction <PPP> at the three neighbours of a site = (1/27)(beta/18)^(3 N_t)
  (computed N_t = 1), carried by int chi^3 = 1; lower orders excluded by per-slab Z3 1-chain bounds (Steiner star).
- (vii) proved + computed: connected plaquette correlator = (1/18)(beta/18)^(4t) + O(beta^(4t+1)); no connected term
  below 4t (proof: parameters s_tau per slab, C = 0 at s_tau = 0 by factorisation, per-slab degree 0 or >= 4 by the
  girth of Z^3); leading decay rate 4 ln(18/beta). Argued/cited: uniform-in-t gap at small beta (Osterwalder-Seiler
  convergent expansion; clustering statement not in the imported Fact).
- Stated in the entity: finite-order lattice statements only; continuum needs beta -> infinity; no bearing on the
  Yang-Mills mass-gap problem.

## Gate
validate_one ok (I305 only); check4 exit 0, 0 errors, 0 other findings, check result pass (log work/A/check4.log);
registered with propose_claim (accepted_for_review); coverage.yaml copied back; files identical to work/A/.
Second read of attack-B.md at the end: B's proof notes it does not decide whether a centreless G has lower-order
surfaces; my clause (iv)-(v) settles the lower-order question for SU(3) itself through its centre (complementary,
not a duplicate). No further overlap.

## Unexpected links
- Pati-Salam: standard-model.automorphisms-preserve-slot-pair-split-are gives Spin(4) x Spin(6). The colour rotors are
  the Spin(6) = SU(4) rotors fixing the pure spinor E, and the spinor 4 = 3 + 1 under colour; the singlet E is the
  "lepton as fourth colour" direction. That is why the triplet character is the rotor's scalar part minus the
  singlet. Argued reading; not used.
- Zero divisors: E is a non-central idempotent (type P in transport.exhaustiveness-every-zero-divisor-annihilated-
  idempotent); SU(3) is its stabiliser among the rotors of the block. A reading only, transport-absent.
- Both stored lattices (weak, colour) have the Wilson action as the scalar part of the plaquette rotor:
  beta(1 - <U>_0) for SU(2), (4 beta/3)(1 - <U>_0) for SU(3).

## Decisions for Leon
- Import as a Fact (maintainer): the strong-coupling exponential clustering / mass gap at small beta for Wilson lattice
  gauge theories (Osterwalder-Seiler 1978; cited from memory, to be checked; possibly also Schor or Muenster 1981 for
  m = -4 ln u + O(u)), if the store should state the uniform-in-t version of clause (vii). The current Fact (ii)
  covers analyticity and the area law only.
- Prior art cited from memory in the note (not premises): Wilson 1974, Creutz 1983, Drouffe-Zuber 1983, Muenster 1981,
  Svetitsky-Yaffe 1982, Osterwalder-Seiler 1978.
- Overlap with B: both proposals compute the degree <= 3 Haar moments via the same Delta(96); mine states them only as
  a lemma. If the maintainer prefers, after acceptance my lemma (iii) could be shortened to a citation of B's
  accepted entity in a version 2.
