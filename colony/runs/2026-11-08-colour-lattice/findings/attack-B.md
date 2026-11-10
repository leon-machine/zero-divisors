# Attack B (adversarial, cross-subject): what a colour rotor lattice cannot say

Target: op.qft-non-abelian-gauge-fields, attack item "Colour", RUN.md question (3).

## Orientation (read)
- synthesis.weak-factor-rotor-lattice-strong-coupling-area-law (SU(2) (beta/4)^A, U(1) (beta/2)^A, format copied).
- synthesis.non-abelian-gauge-fixing-has-gribov-copies-and-the-weak-rotor-lattice-with-doublets-has-a-perimeter-law
  (frozen doublet: c(kappa)^P, unitary-gauge independence argument).
- Facts: synthesis.imported-wilson-lattice-gauge-theory-and-strong-coupling-confinement (i)-(iv) ((iv): compact U(1)
  deconfines and is massless at weak coupling, Guth, Froehlich-Spencer); synthesis.imported-singer-...-complementarity.
- Colour block: su(3) = traceless bivectors of the e3..e8 block commuting with J = e34 + e56 + e78
  (synthesis.field-level-brst-differential-of-the-derived-gauge-fields-is-nilpotent).
- Finiteness/cut-off premises found by search: dark-matter.p2-indifference (v2: "the deposited mode set is declared
  finite"), dark-matter.r2-one-quantum-per-unit-ball (one length unit common to towers), singularity.c1/c2 (Planck
  cells on the stretched singularity, Schwarzschild calibration only), synthesis.continuum-completion-premise (F4: real
  coefficients, the series adds the limits), synthesis.floor-regulator-keeps-the-charge-... (iv),(v): a finite floor
  keeps rotations and no boost), synthesis.series-content-induces-a-newton-coupling-only-through-an-unfixed-cut-off,
  KF premise ("no native covariant regulator").
- Gaps found by search: synthesis.tower-pairing-gap-at-fixed-charges-is-twice-the-quasiparticle-energy,
  synthesis.two-species-floor-pairing-has-a-gapped-doublet-pair-mode-that-closes-where-it-condenses,
  synthesis.uniform-pair-channel-of-a-tower-condensate-is-a-goldstone-rotor, today's window Sugawara / Luttinger modes.
- No 2026-11-01*/11-02* run folders exist in this clone; the stored entities above are their record.

## Routes
1. (Problem's own) Strong coupling on the colour lattice versus a deconfining group: compact U(1) has the same form of
   leading data (stored for SU(2)); delivers only "same form", coefficients differ; weak.
2. (Other subject: finite groups / designs, used in the stored SU(2) checks only as a computing device) Turn the device
   into a counter-model: a finite subgroup G of SU(3) whose averages agree with Haar to some degree d has *identical*
   strong-coupling coefficients wherever each link carries degree <= d, yet a finite gauge group has a different
   weak-coupling phase (no continuum, frozen at large beta). Needs: an explicit G in GA (J-commuting signed
   permutations of e3..e8 fixing the J-complex volume trivector), the invariant subspaces, and an su(3)
   annihilation test so Haar moments are derived (not imported). Fails if G is not a design to degree >= 2.
3. (Own) String breaking with colour-triplet matter at beta = 0: frozen triplet, unitary gauge; the stabiliser of a
   triplet is SU(2), so the mean link is rank one, c e1 e1^dagger, not a scalar as for the doublet; perimeter law
   (1/3) c(kappa)^P. Cheap; but the series has no colour-triplet scalar (its quarks are fermions), so it is a proxy.
4. (Cross-subject reading) The series' finiteness premises and stored gaps versus a gauge-field mass gap.

Choice: route 2 as the core (strongest, exact, and it bounds what any finite order can say), with route 4 as an argued
reading in the same proposal; route 3 executed as the second proposal (A does not cover it), extended to Wilson quarks.

## Pre-registered kill conditions (written before computing)
- K1: Delta(96) (or the chosen G) differs from SU(3) Haar on some link polynomial of total degree <= 2 -> the
  "identical leading data" claim dies for G.
- K2: the G-invariant subspace of (R^6)^{x3} is strictly larger than the su(3)-annihilated one (baryonic moment
  differs) -> degrade the claim to degree 2.
- K3: the enumerated leading coefficient of the 1x1 or 2x1 fundamental loop for G differs from (1/18)^A -> kill.
- K4: some stored gap is a spectral gap of a Hamiltonian built from gauge-field (link or connection) variables in four
  dimensions -> "nothing stored is a gauge-field mass gap" dies.
- K5: some stored premise fixes a lattice spacing for the gauge field on flat spacetime -> "the series supplies no
  fundamental spacing" dies (then state the changed question).

## Established (labels)
Proposal 1 (filed): synthesis.a-finite-subgroup-of-colour-shares-its-strong-coupling-expansion-through-link-degree-three
- COMPUTED: su(3) = the 8 bivectors of e3..e8 commuting with J and Re Omega (closed, orthogonal to J).
  G = J-commuting signed permutations of e3..e8 fixing Re Omega: order 96 (Delta(96)), each a rational even versor;
  trivial centre (the SU(3) centre omega = -1/2 + (sqrt3/2) j is irrational).
- PROVED (with computation): G-invariants of V^(x)k = su(3)-annihilated tensors for k = 1, 2, 3 (dims 0, 2, 2:
  metric + J-form; Re/Im Omega), so G averages = SU(3) Haar averages for every link polynomial of degree <= 3
  (average = orthogonal projector onto invariants; no Haar moment imported). K1, K2 not fired.
- COMPUTED: degree 4: 20 vs 12 invariants; the J-derivation has a 2-dim D^2 = -16 part on the G-invariants
  (p - q = +-4, centre-forbidden): E_G[t^4] = 1 vs 0, E_G[|t|^4] = 3 vs 2, E[(tr U)^4] = 20 vs 12. Degree 5: 80 vs 30
  (explored, not filed).
- PROVED: gluing (1/3) tr(XY) for J-linear X, Y; area-law term (beta/18)^A from the rectangle's own plaquettes,
  identical for G and SU(3) (1x1, 2x1 summed over G); K3 not fired. Tube terms of plaquette correlators (degree 2)
  agree. Caveat stated in the proof: whether G has lower-order surfaces using its missing centre is not decided.
- PROVED: (ln z)' = beta/18 + beta^2/216 + 0 beta^3 (SU(3)) vs + beta^3/972 (G); kappa_4 = 0 for SU(3); lattice
  <chi_p> = (ln z)' + O(beta^5) (cube, standard).
- COMPUTED: G's weight gapped at identity (chi <= 1/3 off 1); SU(3) none (diag(z, conj z, 1) family).
- ARGUED (reading): degree-<=3 strong-coupling data cannot separate SU(3) from a centreless finite group that
  freezes at weak coupling; with the stored compact U(1) comparison, strong coupling decides neither confinement
  nor a continuum gap. K4 not fired: stored gaps (tower pairing gap, two-species doublet pair mode, window
  Sugawara/Luttinger density waves (gapless, frequency q), free gluons at null momenta) are none of them spectral
  gaps of the 4D gauge field. K5 not fired: no stored premise gives the gauge field a lattice spacing on flat
  spacetime (F4 reals; P2 finiteness = deposited modes; C1/C2 stretched singularity, Schwarzschild calibration;
  R2 tower radius; floors keep no boost; Newton cut-off unfixed).
- Gate: check4 0 errors 0 findings, pass (35 s); validate_one ok (I305 only); registered; files identical;
  coverage.yaml copied back.

Proposal 2 (filed): synthesis.colour-triplets-give-the-fundamental-colour-loop-a-perimeter-law-at-strong-coupling
Pre-registered (before computing): K6: the frozen-triplet mean link is not rank one (not c Pi) through kappa^3, or
c != kappa/6 - kappa^3/288 -> kill (ii). K7: the Wilson-quark spin trace round a rectangle depends on its size beyond
2^(P-4), or vanishes -> kill (iii). Neither fired.
- COMPUTED: SU(3) moments of x = e3.U(e3) from the degree-4 su(3)-annihilated invariants: E[x^2] = 1/6,
  E[x^4] = 1/16, E[U x] = Pi/6, E[U x^3] = Pi/16 (G gives E[x^4] = 1/6: degree 4 not shared).
- PROVED: frozen triplet at beta = 0: <chi(U_C)> = c(kappa)^P / 3 exactly, mean link c Pi (rank one over the
  J-complex numbers; stabiliser SU(2) unbroken; contrast the weak doublet's scalar mean link), c = kappa/6 -
  kappa^3/288 + O(kappa^5) > 0.
- PROVED: n_f Wilson quark flavours (r = 1, hop factors 1 -+ d_mu in Cl(4,0), spinor trace 4<.>_0): spin trace round
  every rectangle -2^(P-1) (both orientations, all planes, R, T <= 3 computed); leading hopping term of every
  rectangular fundamental loop (n_f/6)(2 kappa)^P; walk sums on 1x1 and 2x1 patches confirm. outside_ga declared
  (Grassmann integral -> determinant -> loop expansion).
- ARGUED: with triplets the fundamental loop is no confinement criterion (colour analogue of the stored doublet
  result); the series' colour sector has quarks, so its physical question is QCD's, while the Clay problem is pure
  Yang-Mills.
- Gate: check4 0 errors 0 findings, pass (16 s); validate_one ok (I305 only); registered; files identical;
  coverage.yaml copied back.

## Proposal ids
- synthesis.a-finite-subgroup-of-colour-shares-its-strong-coupling-expansion-through-link-degree-three (filed)
- synthesis.colour-triplets-give-the-fundamental-colour-loop-a-perimeter-law-at-strong-coupling (filed)

Overlap with A (read A's draft at the end): A's synthesis.colour-rotor-lattice-haar-moments-and-strong-coupling-coefficients
also derives the SU(3) moments through degree 3 from the same 96-element group and states (beta/18)^A. My proposal 1
restates these only as the shared half of the counter-model; its own content is the degree-4 separation (centre-
forbidden moment), the beta^3 difference of the plaquette, the trivial centre, the gap at the identity and the reading.
Proposal 2 does not overlap A.

## Unexpected links
- The stored SU(2) area-law check already proves that the 24 Hurwitz units reproduce every SU(2) Haar moment through
  degree 5: so the binary tetrahedral gauge theory (finite) shares every SU(2) strong-coupling term with link degree
  <= 5, the same counter-model for the weak factor, stronger than the stored compact U(1) comparison (identical
  coefficients, not only the same form). Immediate from stored data; not filed.
- Today's current-algebra results (window Sugawara, Luttinger modes): density waves at frequency q, gapless; the
  light-ray current algebra is the opposite of a gauge-field mass gap.
- The frozen triplet's rank-one mean link (unbroken SU(2) of colour) is the strong-coupling face of SU(3) -> SU(2)
  breaking by a colour triplet scalar; the chain content under Hypothesis (S) in
  synthesis.series-content-induces-a-newton-coupling-only-through-an-unfixed-cut-off includes a complex (10,1,3),
  which carries colour; if coloured scalars are ever adopted, (ii) of proposal 2 is the relevant strong-coupling
  statement (argued, not checked).
- Finiteness: P2's "deposited mode set is declared finite" and the floors' cut-offs are the only finiteness in the
  store near fields, and the floors break boosts (stored), so no Lorentz-invariant spacing exists in the store.

## Decisions for Leon
1. Import as a Fact (maintainer-only): lattice gauge theories with a finite gauge group in four dimensions have a
   deconfined, perimeter-law phase at weak coupling (low-temperature / Peierls expansion). Cited from memory in the
   reading of proposal 1 (for Z2, Marra and Miracle-Sole 1979 is my recollection; the general finite-group statement
   needs a source). Recommendation: import if the reading is to be more than argued; otherwise leave argued.
2. Fact synthesis.imported-wilson-...(ii) states reflection positivity, analyticity and the area law at strong
   coupling, not the strong-coupling mass gap (exponential clustering, Osterwalder-Seiler). If the store is to say
   the colour lattice has a gap at small beta, extend the Fact (A's clause on plaquette correlators needs it too).
3. The closed-surface count (first closed surface = elementary cube, six plaquettes) used as standard in proposal 1
   (v): import with the Drouffe-Zuber review or accept as standard.
4. For quarks, "no order parameter / no phase boundary with fundamental fermions" is argued in proposal 2; the
   imported Fradkin-Shenker clause covers fixed-length Higgs fields only. Import a statement for fermions only if
   wanted.
5. Merge with A: both A's colour-lattice proposal and my proposal 1 derive the degree <= 3 moments from the 96-element
   group. Recommendation: keep A's as the construction; after acceptance repoint proposal 1 (maintainer repin) to use
   A's moments and keep only the counter-model content.
6. Premise reading (recommendation: no change): P2's finiteness declaration stays scoped to the descent's labels and
   is not read as a lattice spacing for fields; F4 makes the series' fields continuum fields. So the colour question
   is the continuum one, and the open problem's colour attack item could say that the series' colour sector has
   quarks (its physical question is QCD's) while the Clay problem is pure Yang-Mills.
