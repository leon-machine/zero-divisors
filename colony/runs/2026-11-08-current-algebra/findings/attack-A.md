# Attack A (constructive): op.qft-non-abelian-gauge-fields, the current algebra along generators

Status: two proposals filed (below). Scripts: work/A/ (explore1-10.py exploratory; proposal folders
work/A/synthesis.standard-model-currents-of-the-sixteen-channels-levels-and-window-sugawara-split/ and
work/A/synthesis.window-energy-of-one-generation-is-exactly-the-so10-sugawara-energy/; gate logs check4_p1.log,
check4_p2.log).

## Settling first: complex channels and u(16), or real and so(32)

Settled, in agreement with B (attack-B.md, K1 not killed):
- Each channel of a light ray is one tower mode per level, a complex fermion, with the kernel unit J of the tower
  level (unit principle U2) as the scalar of operators, as in the stored pair currents.
- The gauge generators act on V_+ = Lambda^even C^5 by number-conserving bilinears; they map V_+ into V_+ (proved and
  checked) and so lie in the u(16) of pair currents c*_x c_y. No pairing bilinears c c, c* c* are needed for the gauge
  algebra. (B adds: over real coefficients alone the anti-Hermitian q = 0 pair currents span only so(16); J is needed.)
- so(32) is not needed for the gauge currents; but the so(10) that does use pair bilinears of the five INTERNAL modes
  (not of the channels) carries the whole su(16) energy (P2 below).
- Unit matching: the slot module's numbers (span{1, I4}) are carried to J on the channels by the identification of the
  occupation basis with the channels (decision for Leon; B's decision 3 says the same).

## Routes and results (labelled)
1. (Own) Window quadratic forms. PROVED and computed: for any symmetric tensor C of pair-current coefficients,
   Phi(C) = sum C (2 sum_{q>=1} j_{-q} j_q + j_0 j_0) = sum_l (2l + 1) K_C c* c - Q(A_C)/2 exactly on every window,
   K_C = sum_y C_{xy,yu}, A_C(a,b,c,d) = C_{ac,bd} - C_{ad,bc} (the stored one-channel antisymmetrisation argument with
   the channel tensor carried along). Corollary: (n + 1) sum (k + 1/2) n = level-one u(n) Sugawara form on every window,
   no edge term (generalises the stored one-channel identity). [P2 (i), (ii); B computed the u(n) identity too and
   left it to A.]
2. (Problem's own) Embedding and levels. PROVED: tr_16(rho X rho X') = 4 tr_5(XX') + 4 tr X tr X' on gl(5),
   tr rho X = 8 tr X; on the gauge algebra the channel trace form is 4 x the C^5 form: su(3) level 4, su(2) level 4,
   tr rho(Y)^2 = 10/3 for Y = (3n - 2k)/6. Factors trace-orthogonal and traceless (commute with each other and with N on
   edge-clean vectors). All 16 channels left-handed, one rotation weight: every u(16) current has helicity 0, so the
   gauge currents are of density type (exact; no collective flip-current defect). [P1 (i), (ii). The number 4 tr_5
   also appears in B's filed proposal as a corollary for all 32 halvings; the abelian normalisation discussion is B's.]
3. Sugawara split. PROVED (derivation from the current algebra, no import), computed: lambda (adjoint Casimir in the
   trace-dual basis) su(3) 3/2, su(2) 1, Y and N 0, su(16) 32; H_f = (2 + lambda)^{-1}(2 sum_{q>=1} J^A_{-q} J_{A,q} +
   J^A_0 J_{A,0}); [H_f, X_m] = -m X_m on D and on K-local window vectors with min(s, L - s) >= 3(K + |m|); H_c commutes
   with all gauge and number currents there; fails on an edge vector (computed). Central values from
   ||L^f_{-2} Omega||^2 = dim f/(2 + lambda): su(3) 32/7, su(2) 2, Y 1, N 1, total 16, coset 52/7, parts orthogonal.
   Virasoro relations themselves NOT derived. [P1 (iii), (iv)]
4. (Other subject: spin10 claim) so(10) of all bilinears of the five modes. PROVED (finite tensor identity, computed on
   all 16^4 entries): Casimir in the 16 is 45/16, A_so10 = -3 A_N, lambda = 4, hence H = H_so10 + H_N EXACTLY ON EVERY
   WINDOW AND EVERY VECTOR (H_su16 = H_so10): an exact finite form of the conformal embedding so(10)_4 in su(16)_1.
   The u(5) part alone fails. Consequence: the remainder of the energy after the gauge factors and N is
   H_so10 - sum H_f, a function of the so(10) currents alone, exactly on windows. [P2 (iii), (iv)]
   Argued (not filed as proved): A_so10 is a multiple of Delta because Lambda^2 of the half-spinor is irreducible (120).
   Correction to an earlier note of mine: this does NOT single out the halving +-(-1)^N; the identity is a property of
   the spinor embedding of so(10) in gl(16), and the swap of the neutral singlets carries it to the vacuum-swapped half.

## Question (3): what this gives for the four-dimensional Yang-Mills field (argued)
- A current algebra along each generator separately (kinematics) with a 1+1-dimensional energy (the compression of the
  null translation to the band, up to scale): the matter currents to which a light-front gauge field would couple, at
  level 4 per generation (N_g generations: level 4 N_g by additivity of the trace form, argued).
- Not the gauge field: no transverse dynamics, no gauge potential, no Gauss law, no Yang-Mills action; the stored photon
  result already showed helicity +-1 relations only collectively.
- Anomalies: the levels are quadratic traces and positive; the 4D anomaly conditions are cubic. The only exact link is
  tr rho(Y) = 0 <-> vanishing Y-N central term. B filed that the window current algebra is the same for all 32
  halvings while only 2 are anomaly-free (so the levels do not see anomaly cancellation).

## Kill conditions (pre-registered) and outcome
- K1 (no exact window identity): not triggered; exists for every n (and for so(10) exactly).
- K2 (chirality mixing): not triggered; no gauge generator leaves V_+.
- K3 (trace form not uniform): not triggered; factor 4 on all of the gauge algebra.

## Filed
- P1 synthesis.standard-model-currents-of-the-sixteen-channels-levels-and-window-sugawara-split
  "Standard Model currents of the sixteen channels of a light ray, levels and Sugawara split".
  Gate: runcheck 5/5 pass; check4 exit 0, 0 errors, 0 other findings; validate_one ok, no codes; registered with
  propose_claim, files identical, coverage.yaml copied.
- P2 synthesis.window-energy-of-one-generation-is-exactly-the-so10-sugawara-energy
  "On every window one generation's channel energy is the so(10) Sugawara energy".
  Gate: runcheck 4/4 pass; check4 exit 0, 0 errors, 0 other findings; validate_one ok, no codes (after adding the
  premise citations W215 asked for); registered, files identical, coverage.yaml copied.
  P2 does not cite P1 (E201); P1 no longer contains the u(n) window identity or the so(10) clause (moved to P2).

## Unexpected links
- The so(10) of the slot module (stored as the Spin(10) form of the chirality clause) is the algebra whose Sugawara
  energy is the whole su(16) energy of a generation's light-ray channels: the slot module's internal so(10) is
  dynamically complete along a generator.

## Decisions for Leon
1. Unit matching on the channels (I4 of the slot module carried to J of the tower level): accept as a matching, stated
   once (recommended; same as B's decision 3).
2. Follow-on (not a premise): derive the Virasoro relations of the factor parts on D, so the central values of P1 (iv)
   become central charges in the full sense.
3. Possible open-problem note: the energy along a generator of one generation is exactly so(10) Sugawara plus number
   (P2), and the Standard Model coset carries central value 52/7 (P1).
