# Attack C2A (constructive), cluster C2

Status: done; three proposals filed ((a), (b), (c)); Koide left to C2B (filed there). Scripts: work/C2A/ (band.py, explore1-4.py, higgs_explore.py; proposal
folders; gate logs check4_virasoro.log, check4_brst.log).

Split with C2B (proposed; C2B's work folder holds the Koide material): C2A files at most one proposal each on
(a) Virasoro of the Sugawara parts, (b) Higgs-sector BRST, (c) the joint Clifford clause of op.hypothesis-s.
Koide (op.gram-square-and-face-space item 1) is left to C2B (a data check, likely negative).

## Target (a): op.qft-non-abelian-gauge-fields, Virasoro relations of the Sugawara parts on the band domain D

Stored: synthesis.standard-model-currents-of-the-sixteen-channels-levels-and-window-sugawara-split (iii), (iv):
H_f and L^f_{-2} Omega only; central values 32/7, 2, 1, 1, 52/7 defined as 2 dim f/(2 + lambda); Virasoro not derived.

Routes.
1. (Problem's own) Define L^f_n for all n on D by the normal-ordered Sugawara sum, derive Virasoro from the exact
   level-four current algebra on D (algebraic Sugawara computation), then GKO for the remainder using the free
   bilinear L_n of the sixteen channels. Needs: exact current algebra on D (no edge), local finiteness on D.
   Fails if the band commutator carries an edge or sea term on D.
2. (Other subject: so(10) energy) Use H = H_so10 + H_N (stored P2) to get the coset as so(10)_4 / (su(3)_4 + su(2)_4 +
   u(1)), so the coset Virasoro is a coset of so(10); needs the so(10) Sugawara Virasoro on D first (same work).
3. (Own) Window route: exact Virasoro on finite windows with an edge operator; would be stronger but the stored
   result already shows the split fails at the window edge, so only D is in reach.
Choice: route 1, with the so(10) form of the coset as a remark (route 2 adds no new computation needed for the item).

Kill condition K-a (registered before computing): the item is refuted (filed as an obstruction instead) if, on an
exact implementation of D (semi-infinite band, fermion signs counted from the top level), any of the following is
nonzero on a test vector: [L^f_m, L^f_n] - (m - n) L^f_{m+n} - (c_f/12)(m^3 - m) delta_{m+n,0} for f = su(3), su(2),
Y, N; [L^f_m, L^{f'}_n] for f != f'; [L^c_m, J(rho X)_n] for X in the gauge algebra; or the coset's Virasoro with
c = 52/7. Also killed if the free bilinear L_n of the band is not Virasoro at c = 16 there.

Outcome (a). K-a did NOT fire. Established on D, realised exactly (semi-infinite sea, signs counted from the top
level; CAR checked as GA plane relations):
- (proved) [L^f_n, X_m] = -m X_{m+n} for every n (the stored case n = 0), by a cutoff telescoping on each vector;
  (proved) [L^f_m, L^f_n] = (m - n) L^f_{m+n} + (c_f/12)(m^3 - m) delta, c_f = 2 dim f/(2 + lambda): 32/7, 2, 1, 1;
  the reordering constant is computed in closed form, d(m^3 - m)/6, Lambda terms cancel.
- (proved) band energy L_n (bilinear, weight k + 1/2 + n/2) Virasoro at c = 16, shifts every pair current.
- (proved, GKO derived) remainder L^c = L - sum L^f commutes with the gauge currents and parts, Virasoro at 52/7;
  all five unitary on D.
- (proved) L_n = L^so10_n + L^N_n at every mode on D (Delta = coset of so(10) + N in u(16) has c = 0 and Delta_0 = 0
  by the stored window identity, hence Delta_n = 0): the remainder is the so(10)_4 / gauge coset.
- (computed) everything above on sample vectors; vacuum norms (c/12)(m^3 - m) for m = 2, 3; u(2)_1 Sugawara = free
  L_n on D for 2 channels (exploration only).
Proposal: synthesis.gauge-factor-sugawara-parts-satisfy-virasoro-relations-on-the-band.
Gate: runcheck 7/7 pass; check4 exit 0, 0 errors, 0 other findings; validate_one ok, no codes (I305 info);
registered with propose_claim, files identical, coverage.yaml copied. Ledger: transport-absent (as algebra).
The problem stays partial (only item (a) is solved, and only on D; C2B's A1: no window realises the relations with
c != 0, by a trace argument, which agrees with the statement being on D only).

## Target (b): op.qft-non-abelian-gauge-fields, Higgs-sector BRST

Routes.
1. (Problem's own) Extend the stored jet-algebra differential with s phi = -g rho(c) phi on the two doublets
   (eight real scalars, real antisymmetric action), phi = v + h; nilpotency on all fields; 't Hooft-Feynman fermion
   Psi with F^a = nabla.A^a - xi g kappa^{ab} <rho(T_b) v, h>; exactness, cancellation of the vector-Goldstone mixing
   up to a total derivative, Goldstone and ghost masses xi times the vector mass matrix on the Goldstone space.
2. (Other subject: the quartet result (v)) Read the one-particle Q_1 of the massive vectors (beta^2 = Q(p)) off the
   quadratic part of the field-level s, so the field-level and state-space constructions agree.
3. (Own) GA doublets: a doublet as an even element of Cl(3,0) (left su(2), right hypercharge bivector), so s phi is a
   GA product; checks the hypercharge embedding the stored differential left open.
Choice: route 1 with 3 for the representation and 2 as a consistency clause.

Kill condition K-b: killed if s^2 != 0 on some scalar generator for the two doublets with the stored hypercharge;
or if nilpotency needs a condition on the vacuum v; or if no choice of the sign/normalisation of the 't Hooft term
cancels the A-Goldstone mixing up to a total derivative for both doublets at once (for general v1, v2).

Outcome (b). K-b did NOT fire: s^2 = 0 on all fields for every constant vacuum (eight formal components) and every
hypercharge normalisation; the 't Hooft term with the minus sign cancels the mixing up to an explicit total
derivative for every v and xi.
- (proved) doublets as even elements of Cl(3,0): stored weak bivectors on the left, hypercharge y e_12 on the right,
  real orthogonal representation (left hypercharge fails); s(D phi) = -g rho(c) D phi; kinetic term and the four
  quadratic invariants s-closed; Psi_xi exact, s(s Psi) = 0; masses at xi = 1: vector = Goldstone = ghost (nonzero
  spectra of kappa^{-1} W^T W and W kappa^{-1} W^T); neutral aligned vacuum: rank 3, eigenvalues v^2, v^2,
  v^2 (1 + 4y^2/3) relative to the stored kappa (no mass ratio claimed: y and kappa_u1 are normalisations).
Proposal: synthesis.field-level-brst-of-the-two-doublets-and-the-thooft-feynman-gauge.
Gate: runcheck 5/5 pass; check4 exit 0, 0 errors, 0 other findings; validate_one ok (I305 info); registered, files
identical, coverage.yaml copied. Ledger: transport-absent.
Trimmed after the orchestrator's duplicate check: retitled "'t Hooft gauge fixing of the two scalar doublets:
exactness, mixing and common masses"; nilpotency restated as a lemma for (iv); the rank-3 statement reduced to "as
stored"; the mention of C2B's proposal id removed from the note (E201 spirit). check4 rerun once on proposals/: exit
0, 0 errors, 0 other findings; validate_one ok.
Overlap with C2B: C2B's synthesis.higgs-sector-brst-does-not-fix-the-breaking-pattern-of-two-doublets (i) also states
s^2 = 0 for every v with the same GA doublets (their weak basis e23, e31, e12; mine the stored BRST bivectors). Theirs
is the vacuum condition at quadratic order, the rank theorem and the independence pair; mine the full jet-level
nilpotency, invariance, exactness and 't Hooft mixing and masses. Suggest their first sentence of (i) cite mine on
acceptance (C2B proposes the same). The breaking pattern stays an input: the item stays partial.

## Target (c): op.hypothesis-s, the joint Clifford clause (f) from the sign bit

Routes.
1. (Problem's own) Show (f) on V is equivalent to: the ten Majorana operators of the Klein-twisted slot modes and of
   the pair modes, with -1, form a group of signed directions (F2), the sign bit acting as -1 (F3); identify what
   (f) adds (adjoint, signature) and show each is supplied (inversion of G is the Fock adjoint; the (5,5) signature is
   the modes' own).
2. (Other subject: central products of extraspecial groups) The untwisted slot and pair groups commute: their
   central product is extraspecial, hence by the stored classification a group of signed directions on other
   generators (the Klein twist as a group-theoretic fact).
3. (Own) Search for a counter-model: ten operators on V meeting the F2/F3 instance but not (f).
Choice: 1 with 2 as the mechanism and 3 as the kill test.

Kill condition K-c: killed (clause asks more) if there exist operators on V satisfying the F2/F3 instance statement
(distinct slot and pair directions sharing one sign bit, sign acting as -1) built from the given slot and pair
operators for which (f) fails, or if the CAR adjoint is not the group inverse on V.

Outcome (c). K-c did NOT fire (no operators meet the instance and violate (f): the two are equivalent on V).
- (proved) CAR of the five twisted slot and pair modes <=> their ten real Majoranas with -1 form a group of signed
  directions (F2) with the sign bit acting as -1 (F3); |G| = 2^11, blades trace-orthogonal, Cl_Z(5,5) faithful on V.
  The two systems' sign bits are both the operator -1 of V; the joint content is F2c for the 24 slot-pair pairs.
- (proved) signature forced by the modes (5,5); Gauss sum 2^5 as for (10,0), so Cl_Z(5,5) = Cl_Z(10,0) (stored viii).
- (proved) adjoint = group inverse on all of G; commutant of G on Q^32 is Q, so the invariant form is the Fock form.
- (proved) untwisted operators generate the same group (pair parity = -product of the six pair Majoranas) but are not
  signed directions: the clause's content is the choice of directions in G (canonical up to a unit, stored Klein).
Proposal: synthesis.joint-clifford-clause-is-an-instance-of-the-signed-direction-postulates.
Gate: runcheck 5/5; check4 exit 0, 0 errors, 0 other findings; validate_one ok after fixing E203 (postulate F2 was in
uses; now referenced through the signed-directions theorem) and W215; registered, files identical, coverage copied.
Ledger: transport-absent. op.hypothesis-s stays open on its other items.

Bridge lead L4 (tested): the constants -c_f/24 of the five parts add to -16/24 = 16 x (-1/24) only by additivity of
the central charges (needs the 52/7 remainder; the gauge parts alone give -(60/7)/24); on D every part annihilates
the sea, so the -c/24 shift is a convention, not a band quantity. Added to the Virasoro proposal as a remark (not a
proved clause), with the window scope (trace argument: no c != 0 Virasoro on a finite window), validate ok, files
copied to proposals/ (entity text only; check unchanged, check4 not rerun).

## Unexpected links
- The remainder 52/7 is the so(10)_4 / (su(3)_4 + su(2)_4 + u(1)) coset, at every mode (Virasoro proposal (iv)):
  the slot module's so(10) carries all of the light-ray energy apart from fermion number, so any c = 0 mod 24 sea
  test (C3) counts 16 per generation whatever the gauge split.
- Clause (f) and the foundation: the composite's ten Majoranas are an n = 10 instance of (F1)-(F3); the twisted and
  untwisted conventions are two generating sets of one extraspecial group 2^{1+10}.

## Decisions for Leon
1. Premise restatement (recommended): record clause (f) of standard-model.slot-module-hypothesis as "the ten
   Majorana combinations of the slot and pair modes are distinct directions of one group of signed directions
   (Premises F1 to F3), the sign bit acting as -1", citing the new proposal and the Klein-convention result; it
   then carries no content on V beyond the foundation (a premise decision, maintainer-only).
2. Open-problem note for op.qft-non-abelian-gauge-fields: item (a) settled on D (central charges in the full sense,
   band only); item (b) settled for the differential and the 't Hooft-Feynman gauge with the vacuum as input, the
   breaking pattern being C2B's result (a potential choice, not a BRST output). The problem stays partial.
3. Duplicate handling: C2B's Higgs proposal (i) restates s^2 = 0 for every vacuum; both are self-contained; C2B
   suggests its first sentence cite mine after acceptance.
4. Literature named from memory (no imports needed): Sugawara 1968, Kac 1990, GKO 1985/86, Schellekens-Warner 1986,
   Bais-Bouwknegt 1987, 't Hooft 1971, Fujikawa-Lee-Sanda 1972, BRS 1976, Kugo-Ojima 1979, Gorenstein 1968.
