# Attack B (adversarial): the Standard Model gauge algebra in the u(16) channel currents

Target: op.qft-non-abelian-gauge-fields, attack item "The current algebra along generators".
Statement under attack: "the Standard Model gauge algebra acts inside exact u(16) level-one channel
currents per light ray and generation".

## Answer (one paragraph)
The statement holds, but carries less than it seems. The channels are complex (Witt pairs, unit J), every
generator of s(u(2) + u(3)) is block diagonal on the isotypic components of the slot module and anti-Hermitian
over span{1, J}, so the gauge currents are pair currents in u(16), never pair-creation terms of so(32)
(proved); no gauge generator connects the two chirality arrays of a light ray (proved: the gauge algebra acts
on the internal index, chirality and the rotation about the generator on the spinor values). The levels relative
to the five-mode trace form are 4 for all three factors (computed: tr_{V+}(rho(T) rho(T')) = 4 tr_5(t t') on the
whole 12 x 12 Gram matrix). What fails: (a) the abelian level is a number only after choosing the scale of Y
(10/3 with the stored Y, 4 relative to the five modes, 120 for integral charges 6Y); only the ratios
tr T3^2 : tr Y^2 : tr Q^2 = 3 : 5 : 8 are fixed (proved, computed); (b) there is no relation between levels and
anomaly cancellation per generation: an explicit inner particle-hole reversal of the channels of whole
components (a product of vectors) maps the window gauge currents of any gauge-commuting CPT halving exactly to
those of any other, fixes the energy, the sea and the edge-clean vectors, and reverses only the rotation weights
of the reversed channels; all 32 halvings have the same window current algebra, but only the two parity
halvings are anomaly-free (proved, computed). The anomaly is visible only with the rotation weights, as a
weighted cubic trace. Exactness on windows is that of the stored identity: the operator identity carries edge
terms; the central term is exact on edge-clean vectors, a set every gauge zero mode preserves.

## Orientation (read)
- synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators (iv): window identity for
  j^{xy}_m, u(n) level one on edge-clean vectors; channel weights +-1/2, unit J.
- synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins (i): matrix form
  [rho_q(M), rho_q(M')*] exact, edge-clean value q tr(M'*M) + rho_0([M, M'*]).
- synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves (i), (iii).
- synthesis.slot-module-light-ray-arrays-are-weyl-components (ii): 16 channels per generation and light ray.
- synthesis.spin10-clause-content-is-the-neutral-singlet-choice (ii): the 32 gauge-commuting halvings.
- synthesis.cpt-closure-forces-slot-module-and-chirality (4): anomaly-free halvings +-(-1)^{n+k}.
- synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays (iii), (iv); synthesis.triangle-anomaly-... (v), (vi).

## Routes
1. (The problem's own) Write the gauge generators as 16 x 16 channel matrices on V_+ and test each failure
   mode in turn: complex structure, chirality, levels, edge terms, anomalies.
2. (Other subject: CPT halvings and anomaly theory in the standard-model subject) Compare the current-algebra
   data over all 32 gauge-commuting halvings: if equal while anomaly freedom differs, the levels carry no
   anomaly information.
3. (Own) Particle-hole conjugation of a channel on a window as an exact inner automorphism: test whether it
   intertwines the gauge currents of a halving with those of the halving that conjugates one component.
Chosen: 1 for the quick tests, then 2 + 3 together (3 gives 2 as a corollary at the level of the whole window
algebra, not only traces).

## Pre-registered kill conditions (written before computing) and outcomes
- K1 (real vs complex): the u(16) reading dies if some gauge generator needs pair-creation bilinears.
  OUTCOME: not killed (proved: block diagonal on components, number-conserving; over real coefficients alone
  the anti-Hermitian pair currents at q = 0 span only so(16); J is needed for u(16) and for the hypercharge J Y).
- K2 (chirality): dies if some gauge generator fails to commute with the chirality grading of the channels.
  OUTCOME: not killed (proved; in the Dirac reading the conjugate components sit in the other array via the
  particle-hole reversal, still block diagonal).
- K3 (abelian level): "the abelian level is a number" dies under rescaling of Y. OUTCOME: killed (trivially, and
  computed: 10/3, 4, 120 for three natural normalisations; ratios 3 : 5 : 8 fixed).
- K4 (anomalies): "levels encode anomaly cancellation per generation" dies if two halvings with identical levels
  differ in anomaly freedom. OUTCOME: killed (computed over all 32: identical 12 x 12 trace form, 2 anomaly-free;
  proved at the level of the whole window algebra by the particle-hole reversal).
- K5 (window form): the window central term for gauge currents dies if an edge term survives on vectors
  edge-clean in every channel. OUTCOME: not killed (the stored matrix identity applies with M = rho_+(T); the
  depth-d edge-clean set is invariant under the global gauge group: the filled bottom levels pick up det U,
  the empty top levels are fixed). Argued for invariance, proved for the identity (stored).

## Computed, not filed (overlaps the constructive side)
- The u(n)_1 window Sugawara identity is exact on every window, no edge correction, generalising the stored
  one-channel identity: sum_k k n_k = (1/(n+1))(A + B) + (1/(2(n+1)))(Z1 + Z2) - N/2 with
  A = sum_{q>=1} sum_{x,y} j^{xy}_q* j^{xy}_q, B = sum_{q>=1} J0_q* J0_q, Z1 = sum_{xy} j^{xy}_0 j^{yx}_0,
  Z2 = N^2 (computed exactly on the full Fock space for (n, L) = (2, 4), (3, 3), (2, 5), (4, 2)). Coefficients
  1/(n+1) are the su(n)_1 Sugawara constant in the trace-orthonormal basis.
- But the split into commuting parts fails off edge-clean vectors: [B, j^{01}_q] != 0 on the window (computed,
  n = 2, L = 4, 6); it vanishes on vectors edge-clean at enough depth (proved sufficient: lowering modes with
  q <= D and 3D >= L - 1, using [S_p, S_q] = 0 for same-direction partial shifts), and for raising modes with
  q > L/2 it fails at every depth (L = 6, q = 4, 5: nonzero at depth 3). The constructive side is computing the
  same split (its work folder tests [H_f, J_m] on the sea and near the edge), so this is left to it.

## Filed
- synthesis.light-ray-gauge-currents-of-a-generation-do-not-see-its-anomaly-cancellation
  "Light-ray gauge currents of a generation do not see its anomaly cancellation".
  Clauses: (i) pair currents in u(16), partner blocks -M^T in dual bases, traces; (ii) the particle-hole
  reversal phi_C = Ad(prod u_x), u_x a product of 2L vectors, exact map of the window gauge currents between
  halvings, fixing energy, sea and edge-clean sets, reversing rotation weights; (iii) trace form 4 tr_5 on all
  32 halvings, anomaly-free exactly for the two parity ones, anomaly = weighted cubic trace; (iv) abelian
  normalisation 10/3, 4, 120, 48 and the ratios 3 : 5 : 8, 3/8.
  Gate: runcheck 4/4 pass; check4 exit 0, 0 errors, 0 other findings (no W413); validate_one ok, no codes;
  registered with propose_claim (moved aside first, files identical, coverage.yaml copied back, check4 rerun
  clean). Labels: (i), (ii), (iv) proved; (iii) proved from (ii) with the 32-pattern count computed.
  Ledger: transport-absent.

## Unexpected links
- The particle-hole reversal is the window form of CPT on the light ray: the light-ray data are the pairs
  (representation, rotation weight) modulo (R, w) ~ (R-bar, -w), which is the four-dimensional chiral content;
  the anomaly coefficients are exactly the invariants of this equivalence that are odd in the charges.
- The trace form 4 tr_5 on every halving is the so(10) embedding index (16 has Dynkin index 4 relative to the
  five modes): the level equality of the three factors is the sin^2 theta = 3/8 relation, and it holds equally
  for the 30 anomalous halvings.

## Decisions for Leon
1. Normalisation of the abelian level (recommend: state levels relative to the trace form of the five internal
   modes, where all three factors have level 4, and quote tr Y^2 = 10/3 for the stored Y; never "the" U(1)
   level without the normalisation).
2. Whether the open problem's 8 November paragraph should add: "the levels and the window current algebra are
   the same for all 32 gauge-commuting halvings; anomaly cancellation is not a property of the current algebra
   along one generator" (recommend yes, citing the filed proposal if accepted).
3. Unit identification on the channels: the slot module is read over span{1, I4}, the channels over span{1, J};
   the gauge currents need I4 -> +J or -J on the matrix entries. By clause (ii) with every component reversed
   the two choices give unitarily equivalent current algebras with all rotation weights reversed, so the choice
   is a convention tied to the orientation of the rotation weights (recommend: I4 -> J, the particle half with
   the weight of the left-handed chirality, stated once in conventions).

## Sibling's findings (read midway and at the end)
The constructive side's draft (work folder only, not yet filed when this was written) states the trace form
4 tr_5 on the parity halving, the u(n) window Sugawara identity, the factor split on localised window vectors
with failure at the edge, adjoint Casimirs and central charges, and the conformal embedding so(10) in su(16) at
level two of the vacuum module. No contradiction with the filed proposal: it shares only the number 4 tr_5,
which here is a corollary used to state halving independence (all 32), not a separate result. The split's edge
behaviour computed here (above) is left to that side and not filed.
