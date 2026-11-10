# Attack A (angle A, constructive), run 2026-11-09-three

Status: attack round done. Two proposals filed (T2, T1); T3 nothing filed (kill condition fired; B filed the no-go).
Kill conditions below were written before any computation. Outcomes are at the end of each target.

## T2 op.helicity-per-boundary-mode, attack item 1: spin 2 at the horizon

Routes.
- R1 (problem's own): import Regge-Wheeler, Zerilli, Chandrasekhar as a Fact. Maintainer-only; not taken.
- R2 (GTG, chosen): perturb the gauge field of the stored static Schwarzschild field, hb^{-1}(e_mu) -> hb^{-1}(e_mu)
  + eps k(e_mu), with eps nilpotent (first order exact), solve Omega from the torsion-free condition and read the
  Ricci vector of the perturbed field with lib/gtg.py at jet points. Odd parity (Regge-Wheeler gauge, m = 0, generic
  jets of h0(t,r), h1(t,r)): get the three linearised vacuum equations in closed form, then the master function
  Q = f h1/r and the 2D equation as an explicit combination of them, and the converse (reconstruction of h0, h1 from Q).
  Even parity: Chandrasekhar intertwiner (exact rational-function identity) plus, if cheap, a span check that the
  Zerilli equation of the Zerilli-Moncrief function lies in the span of the linearised equations at jet points.
- R3 (other subject): the Weyl bivector map's perturbation (Teukolsky/Bardeen-Press in GA). Boost weight 2, potential
  does not vanish at the horizon without the Chandrasekhar-Sasaki-Nakamura rescaling. Longer; not taken.
- R4 (own): uniform near-horizon Rindler argument for all spins. Leading order only; weaker.

Kill condition (pre-registered). R2 dies for odd parity if (a) the perturbed GTG Ricci components, for generic jets,
are not the closed-form expressions (the route then has no exact handle), or (b) the 2D operator applied to Q = f h1/r
is not an exact combination of the linearised vacuum equations with potential f(l(l+1)/r^2 - 6M/r^3), or (c) the
potential divided by f is singular or the reconstruction of (h0, h1) from Q fails (the 2D equation would then not be
equivalent to the vacuum equations on the channel). For even parity: the intertwiner clause dies if
(d/dr_* + w)(RW operator) != (Zerilli operator)(d/dr_* + w) as an exact identity; the span check dies if the Zerilli
equation is not in the span at a generic point (then even parity is reported as cited only). If (a) to (c) fire,
file nothing on T2.

Outcome (T2). Kill conditions (a), (b), (c) did not fire; the intertwiner and span conditions did not fire.
Proposal: synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional (title now "Odd-parity
gravitational channels are two-dimensional at the horizon; even parity one way"). Gate: runcheck 5/5; check4 exit 0,
0 errors, 0 findings (draft folder, registered folder, and again after the edits below); validate ok (info I213, I305);
registered with propose_claim; coverage.yaml copied. Uses pairing.imported-schwarzschild-connection-curvature@7 and
the lower-spin channel theorem @1 (for f = C e^{2 kappa r*}).
- computed (1): first-order GTG Ricci vector of the odd-parity field (Regge-Wheeler gauge, m = 0) has the classical
  components E_t, E_r, E_theta. Scope after B's exposure (1): for generic jets and generic angular data it is an
  identity of rational functions of sqrt f (every radius) at three polar angles, M = 1 and 9/8, and an identity in
  tan(theta/2) (every angle) at two radii; degree one in L with three L tested (one non-harmonic). NOT a single joint
  identity in (r, theta): a bivariate run (work/A/sym2.py) did not finish in 10 minutes and is not evidence.
- proved from (1): RW[Q] = (f/r)(E_r + d_r(f E_theta) - 2 f E_theta / r), Q = f h1/r, V = f(L/r^2 - 6M/r^3);
  d_t E_t = -f d_r E_r - (2f/r) E_r - (L-2)(f/r^2) E_theta; on a channel of frequency omega != 0 the Regge-Wheeler
  equation is EQUIVALENT to the three vacuum equations (reconstruction h1 = rQ/f, d_t h0 = f d_r(rQ)).
- computed, one direction only (3): for even parity (RW gauge, Zerilli-Moncrief function) the Zerilli expression lies
  in the span of the first-order Ricci components and their first derivatives (rank 18 either way; 19 with a wrong
  potential), at two points, L = 6 and 7/2. Coefficients of the combination not exhibited. Converse cited (C3).
- proved (4): V_o = W^2 - W' - c^2, V_e = W^2 + W' - c^2, W = 3Mf/(r(lam r + 3M)) + c, c = lam(lam+1)/(3M);
  d_{r*} + W intertwines; inverse on real-frequency channels; kernel only at d_t^2 = +c^2 (non-oscillating).
- proved (5): V_o/f = (L-3)/(4M^2), V_e/f = (4 lam^2 + 4 lam + 3)/(4M^2 (2 lam + 3)) at r = 2M, positive; rate
  e^{2 kappa r*}, as for spins 0 and 1.
- cited from memory: tensor-harmonic completeness and m-independence (C1), reachability of the RW gauge (C2), the
  even-parity reconstruction (C3); Regge-Wheeler 1957, Zerilli 1970, Moncrief 1974, Chandrasekhar 1983.
- not established: even parity in both directions; l = 0, 1 (no channel); other gauges and charts (the statement is a
  Killing-frame one); uniformity in l; J3's current-boson identification and partial-wave lift.
B's exposures (read after filing) applied in place in proposals/: (1) radius identity, (2) title, one-liner, clause
(5) and lay now say odd derived, even conditional, (3) Killing-frame scope, (4) l >= 2 scope with the l = 0 pole at
r = 3M and the l = 1 degeneracy. Bridge lead R10 (one superpotential in Chandrasekhar's F form): same structure as my
W, confirmed by B independently; R11 not tested.
Ledger: transport-absent. Next step: exhibit the even-parity combination symbolically and derive (C3); a joint
identity for (1).

## T1 op.wall-class-invariant, attack item 4: derive the lens-space inputs

Routes.
- R1 (chosen): cellular. The Z4-equivariant cell structure of S^{2n+1} (one free cell per dimension), its chain
  complex over Z[Z4], an explicit equivariant diagonal approximation checked as a chain map in exact integer
  arithmetic, and from it the integral, mod-2 and mod-4 cup products of L^{2n+1}(4); Bocksteins from the cochain
  complex; the Euler class of the quarter-turn plane bundle as a cellular obstruction cocycle; T Sigma + R from the
  equivariant splitting of the ambient space.
- R2 (other subject): Gysin sequence of the circle fibration over CP^n. Needs H^*(CP^n) and the Gysin sequence as
  imports; shorter text but moves the citation, does not remove it.
- R3 (own, for the K-theory input): replace the full K-ring by what the stored result uses: a lower bound on the
  order of 2^{k-1}(1 - xi) in K(L). Candidates: Chern classes (too weak, checked by hand: (1+2y)^2 = 1), the
  character map on a finite skeleton, the Atiyah-Hirzebruch filtration. Decide after the cohomology part.

Kill condition (pre-registered). R1 dies if the diagonal approximation fails the chain-map identity in Z[Z4] x Z[Z4]
at any n <= 4, or if the derived ring is not Z[y]/(4y, y^{n+1}) in even degrees with x^2 = 0 mod 2 (which would
contradict the stored conditional results, a finding in itself). For the spin class and the K-ring: if no derivation
at reasonable length exists, say so, state exactly which hypothesis stays cited, and do not present a partial
derivation as discharging it.

Outcome (T1). Kill condition did not fire: the diagonal is a chain map for k <= 9 and group orders 2, 3, 4 (all
parity cases occur for k <= 5), and the derived rings are the stored ones.
Proposal: synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure. Gate: runcheck
6/6; check4 exit 0, 0 errors, 0 findings (a W413 on the diagonal check was removed by tightening it); validate ok
after renaming an index letter the GA-language scan read as an imaginary unit (E609); registered; coverage.yaml
copied; outside_ga declared (kind other: algebraic topology). No premises.
- proved given background (G) (cellular cohomology, invariant cochains, comparison theorem, Euler class and w1 as
  primary obstructions; general and classical, not derived): the cell complex; the diagonal; cup coefficient 6 for
  two odd degrees and 1 otherwise; H^even(Z) = Z[y]/(4y, y^{n+1}); H^*(Z2) = Lambda[x] x Z2[u]/(u^{n+1}), x^2 = 0;
  mod 4 the degree-one square is 2 eps_2; top-degree products by restriction from L^{2n+3}; beta x = 2y; the mod-2
  Bockstein vanishes; w1(L) = x; e(eta) = +-y, e(L + L) = +-2y; T Sigma + R = (n+1) eta.
- proved given (K1) (Atiyah-Hirzebruch filtration of K-theory, with c1 as the symbol of a line minus 1; cited):
  K(L^{2n+1}(4)) = Z[chi]/(chi^4 - 1, (chi-1)^{n+1}), BOTH halves (relations hold; none further, by the count 4^n on
  both sides). Computed in the presentation: ord(1 - chi^2) = 2^{floor((n+1)/2)}, n = 1..9 (agrees with R8).
- NOT derived: the spin class q1 (2 q1 = p1, natural, stable). It needs H^4(BSpin; Z); I found no derivation at
  reasonable length and no weaker derived statement that carries the stored use (q1(L + L) != 0 forces L + L not
  stably trivial). The lambda-operations and (K1) itself are also not derived.
Hypotheses discharged (stated in the proposal's note for the maintainer): two-rung result: (L1) in full; (L2) not;
(L3) given (K1). K-theory result: (L3) replaced by the direct x^2 = 0; (L2) given (K1); (L1) not. So neither stored
result becomes unconditional: the first still rests on q1, the second on general K-theory.
Not reached: the exact rung count on L^5(4) (bridge lead R7, the equivariant index; untested).
Ledger: transport-absent.

## T3 op.qft-structural-inputs, attack item 1: the generation number

Routes.
- R1 (lead a, capacity): per-light-ray registration, 2 n_V + n_s + 2 eps <= 16 n_g.
- R2 (lead b, Sakharov): N_V = N_W/4.
- R3 (own): an independence statement by two models over the joint cone of the premises, in the form used for
  synthesis.bott-shifted-model-leaves-the-odd-towers-dimension-free.

Kill condition (pre-registered). A conditional theorem "n_g = 3 under X, Y, Z" is filed only if every premise X, Y, Z
is a stored entity (postulate or proved) or a clearly named new reading, AND the counting rule can be shown fixed
before the count (it appears in the store before 9 November in a form that already determines the count). If the rule
was fixed after seeing 34 <= 48, or if a store-allowed content passes at n_g = 2, the theorem is not filed as a
derivation; the deliverable is then the independence statement with the conditional table. What would have counted as
failure of lead (a): a bound satisfied at n_g <= 2 on the store's content, or violated at n_g = 3.

Outcome (T3). Kill condition FIRED, on both counts. (i) The capacity rule was written down on 9 November in the same
paragraph as its count (bridge L1(c) of the earlier run), so it was not fixed before the count. (ii) A store-allowed
content passes at n_g = 2: the recorded content without a graviton gives 32 <= 32, and the store has no graviton
field. Lead (b) fails the first clause too: no stored premise requires the quadratic coefficient to vanish (bridge R3,
confirmed by B), and its zero sits on the surface xi_R = 1/6, alpha = 1 (R2). The two leads also need opposite
treatments of the graviton (R1). So no theorem "n_g = 3 under X, Y, Z" is defensible, and I filed nothing: B filed the
no-go synthesis.capacity-and-sakharov-readings-leave-the-generation-number-free, which contains everything I would
have put in an independence statement (argued: I did no computation on T3 beyond checking the arithmetic above; I
relied on B's reading of the cones). What B's claim does not contain and I did not do: a two-model proof over the
listed joint cone in the form of the Bott-shift result (B labels its independence "argued"); bridge R5.

## Unexpected links
- T2 and T3: the spin-2 channels exist only for l >= 2 and come two per (omega, l, m); any per-channel count of the
  graviton (the capacity reading's eps = 1) is therefore not uniform in l (argued; agrees with bridge R4).
- T2 and the lower spins: the pair (V_o, V_e) is a Darboux pair under one superpotential, the same structure as the
  stored Dirac pair V_+- = W^2 +- dW/dr_*; for spin 2 the superpotential tends to a nonzero constant c at the horizon
  where the Dirac one tends to zero, which is why the spin-2 rate is e^{2 kappa r*} and not e^{kappa r*} (computed).
- T1 and the stored 2-periodicity of the cyclic resolution: the coefficient 6 = C(4,2) against 1 = C(2,2) is the
  whole difference between x^2 = 0 on the quarter-turn spaces and x^2 != 0 on projective space (proved given (G)).
- T1 and K-theory: with the cohomology ring in the store, the K-ring is a counting corollary of the Atiyah-Hirzebruch
  filtration; the same count would give K of any lens space with even cohomology (argued).

## Decisions for Leon
1. (T1) Background (G) and (K1). The derivation rests on general cellular cohomology (G) and, for K-theory, on the
   Atiyah-Hirzebruch filtration (K1). Recommendation: accept (G) as background of the topology the store already
   uses, and import (K1) and the lambda-operations as one Fact (general K-theory), which then makes the lens-space
   K-ring a stored theorem and lifts hypotheses (L2), (L3) of the two stored results.
2. (T1) The spin class q1 is not derived and I see no short derivation. Recommendation: import it as a Fact
   (H^4(BSpin; Z) generated by q1, 2 q1 = p1, natural and stable), or keep the two-rung result conditional on it.
   This reverses "derive, not import" for this one item only.
3. (T1) After acceptance, restate the two conditional results (version + 1) to cite the new claim for (L1) and for
   x^2 = 0 in place of the memory citations. Maintainer work; I did not file corrected versions.
4. (T2) J3 version 2 keeps the channel-reduction clause as premise for spin 2. With the proposal accepted it is
   derived for odd parity and conditional on a cited reconstruction for even parity. Recommendation: narrow J3's
   channel clause to "even parity, as far as (C3)" or leave it and add a note; do not drop it.
5. (T2) (C1) to (C3) are cited from memory, as (C1), (C2) of the lower-spin theorem are. Recommendation: one imported
   Fact for the tensor-harmonic and Zerilli reconstruction results, or an open item to derive (C3).
6. (T3) Nothing to decide from my side beyond B's list: no generation theorem exists on these leads without a new
   premise.
