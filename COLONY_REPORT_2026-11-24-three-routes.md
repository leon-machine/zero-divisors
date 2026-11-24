# Report, run 2026-11-24-three-routes

Request (Leon, 23 and 24 November 2026): the most consequential open problems; three attack routes for each of
six; then run the three routes recommended first (5a, 1a, 4b of ROUTES.md).

Method: the standing method with one problem per cluster: a constructive and an adversarial attacker on each of
three problems (six attackers, Claude Fable 5.2), one bridge pass after the attack round, three blind referees
(Claude Opus 5.5), one fix round, a second blind pass (Claude Opus 5.5) on the clauses added or restated in the
fix round (R-2.md). Seven proposals filed; all seven SOUND WITH FIXES at first review, fixes applied, central
check4 and validate_draft clean after the fixes (verify/check4-final, verify/validate). The adversarial attackers
also worked routes 1b, 1c, 4a, 4c, 5c and part of 5b.

## What was established

### P. op.positivity-of-values (routes 5a, 5c, part of 5b)
1. synthesis.additive-weights-on-the-rational-projectors-of-two-or-more-modes-are-linear. R-P SOUND WITH FIXES.
   - proved, given the stored two-mode theorem: for every N >= 4 a function on the symmetric idempotents of
     Mat_N(Q) that adds on orthogonal ones, with values in any rational vector space and no sign condition, is the
     restriction of a linear functional; hence in Cl_Q(l,l) for every l >= 2. With non-negativity and
     normalisation the weights are exactly the restrictions of the states of (P).
   - proved in the entity, nothing imported: every positive rational is a sum of four rational squares.
   - proved: for l >= 3 the statement holds on the even subalgebra alone; for l = 2 it fails there.
   - Kill condition P2 FIRED: the pair e_1, (0,1,1,1,2,0,0,0) of Q^8 lies in no four-dimensional rational
     subspace similar to the standard one (determinant 7). The first step named in the problem record is false;
     the proof goes one vector at a time and needs no Hasse-Minkowski.
   - Prior art unread: Mushtari 2001 (abstract only). No novelty is claimed.
2. synthesis.under-rp-record-weights-bound-the-chsh-sum-of-correlators-on-two-modes. R-P SOUND WITH FIXES.
   Conditional on Hypothesis (RP) (every self-adjoint rational projector can label a record).
   - proved: C is a rational combination of four rational projectors but of no commuting family (C^3 = 8C);
     the sum of four separately recorded correlators is bounded, S^2 < 8, with no assumption on the value of the
     element C. P3: first clause did not fire, second fired literally, its stated consequence does not hold.
   - argued: (RP) with non-negative context-independent additive weights is (P) on projectors: it relocates (P)
     into a statement about records and derives neither.
3. synthesis.local-records-give-the-chsh-bound-without-positivity-and-reversal-on-one-party-keeps-them (title:
   "Under (CP) local records bound CHSH without (P) and do not fix (P): reversal on one party"). R-P SOUND WITH
   FIXES; one overstated clause restated (the reversed functional agrees with the state on records, not on every
   product of local observables).
   - proved: a certificate linear in C; under (CP), non-negativity on four squares, lambda(C)^2 <= 8. (P) implies
     (CP) and not conversely: the quantum bound needs strictly less than (P).
   - proved: reversal on one party is a linear involution; the reversed functional keeps the weight of every
     palindromic sequence of local records at every number of modes, and violates positivity.
   - argued (a reading of 73 prose postulates): on the scope of a laboratory pair the reversed functional passes
     every premise other than (P). P4 fires on that scope only; it is fragile (one unitary mixing the parties'
     modes and a local record gives a negative weight).
   - computed, findings only: the Krein-form premise and (P) are not one premise; (N+) does not supply the split;
     the recording premises do not imply macroscopic locality.
   Ledger: transport-absent, all three.

### G. op.gravitational-field-at-null-momentum (routes 1a, 1b, 1c)
4. synthesis.spin-two-lattice-model-static-slaved-field-fails-and-dressed-pair-detection-commutes (title:
   "Lattice first-order gravity: slaved field, dressed pair, no local dressing of one mass"). R-G SOUND WITH
   FIXES.
   - The model: the stored first-order Einstein map in the gauge h(e_0) = 0 on a periodic cubic lattice in three
     space dimensions, exact over the rationals; four commuting constraints; two transverse trace-free pairs per
     nonzero momentum. Not a model of anything beyond first order, of moving matter, or of Lorentz covariance.
   - proved, counts computed: the static slaved field fails to commute (3858 of 4317 components); the retarded
     slaved field fails at 8736 of 9310 events outside the detection's lattice cone and inside the source's
     (5246 of them outside the source's unit-speed cone); with the field's own variables the dressed pair
     detection commutes at all 202171 events outside the lattice cone and a coupled device has no effect outside
     it at any order.
   - proved: one mass on two sites has no dressing of compact support, and none whose curvature stays in a box.
     G1: met for one mass moved alone, not met for the pair. G2 not met.
   - Limits stated in the entity: sufficiency at first order, not necessity; the commutation once a compact
     dressing exists is generic to local canonical lattice models.
5. synthesis.helicity-two-composites-of-light-ray-fermions-on-a-generator-and-off-the-null-plane. R-G SOUND WITH
   FIXES; claims narrowed.
   - proved: no fermion bilinear on one generator has helicity two; sea values C(q+1,3) and C(q+3,7) for the
     lowest four-fermion modes; Q(p1 + p2) for two null momenta vanishes only for parallel momenta; an exact
     identity giving commutation for any causal medium coupled at a point with no constraint.
   - argued: the lowest helicity-two four-fermion modes are not a free part in the sense of the stored lattice
     result; commutation alone does not force a canonical pair, a state-independent linear response does; two
     ways are named (a canonical pair; the field as the response of the stored quantum fields), the list not
     shown complete.
   - argued, findings only: the recording route removes the registered phase with the signal (route 1c ends).
     G3 did not fire.
   Ledger: transport-absent, both.

### H. op.deposit-state-is-hadamard (routes 4b, 4c, 4a)
6. synthesis.wall-conjugation-invariance-on-a-radiation-type-descent-floors-the-dirac-deposit-and-selects-none.
   R-H SOUND WITH FIXES. Conditional on (RD), (DF), (CW), none a stored premise.
   - proved: the stored conjugation cannot serve (it reverses energy, exchanges no sides and fixes only the
     tracial state); the route needs the wall reflection with charge conjugation. H1 FIRED: a disk of invariant
     states per mode in the class of homogeneous, isotropic, helicity-diagonal, charge-symmetric states.
   - proved given classical Weber-function facts cited from memory: a floor n0 = (1 - sqrt(1 - q))/2,
     q = exp(-pi k^2/(m a')), attained by one Fock state; confirmed numerically by the referee to seven digits.
     The floor state is Hadamard given the imported Fact on adiabatic states (one step argued).
   - argued: an invariant quasi-free state forces equal occupations on the two sides (mirror ratio 1 against the
     stored cap 0.448); no stored theorem is contradicted.
   - Prior art: Boyle, Finn and Turok (arXiv:1803.08930) already state the free function for spinors and the
     least-occupation choice; the floor profile is theirs.
7. synthesis.trace-anomaly-leaves-no-exact-radiation-field-at-a-tame-wall. R-H SOUND WITH FIXES; the sign of the
   trace confirmed by the referee against Mottola and Vaulin (arXiv:gr-qc/0604051).
   - proved given (A) (the standard anomalous trace, not imported) and (E) (the whole expected stress is the
     source): the exact radiation field solves the field equation for no state; on power laws the order t^-4
     cancels only for p other than 1/2.
   - computed: Euler weight 1008 (1016 with the doublets), alpha = 127/(720 pi^2); the anomalous share of the
     density is below 1.7e-15 at the stored ceiling and of order one near one Planck time.
   - The chain does not break on the collar. Statements that use the wall itself are outside (A) with (E).
   - findings only: the necessity route (4a) gives nothing the store already requires.
   The two H results cannot hold with all of (A), (E), (RD), (DF); both say so and cross-cite.
   Ledger: transport-absent, both.

## Kill conditions
P1 no. P2 FIRED. P3 split. P4 fires on a stated scope, argued. G1 met for one mass, not for the pair. G2 no.
G3 no. H1 FIRED. H2 no for the floor state, yes for another invariant state. H3 no stored theorem contradicted;
an argued tension with the cold mirror. H4 fired for (CW) alone.

## Cross-links (findings/bridges.md; all argued unless marked)
- computed: the stored channel weights (1, 3, 12) are a third of the Weyl-square anomaly weights (3, 9, 36).
- The stored Clausius theorem takes the stress as an expectation value and as given; whether the anomalous
  stress is a source is the content of "whole" in (E).
- The orientation datum of the wall result is the stored (N+) orientation datum; the split of (P) is a
  different datum.
- The recording premises do not say (RP); a flag-sector form of it is an untested lead.
- CORRECTED after reading the registration: the bridge pass reported that pred.gravity-entangles-standard-phase
  is conditional on a rejected premise (P-v, "no free radiative part"). The third addendum of 12 October 2026
  to the registration already restated (P-v) as "the phase is computed at the instantaneous order" and withdrew
  the original wording. Nothing is to be restated in the registration; the stored prediction could name the
  restated premise.

## Decisions for Leon
1. (RP): adopt, or keep as a named hypothesis (recommended: named hypothesis; as a premise it replaces (P)).
2. (TT), a canonical pair on the two null directions: adopt, reject, or leave open with both ways recorded
   (recommended: leave open; sufficiency is shown in a model, necessity is not).
3. (CW): recommended not adopted.
4. The radiation-type hypothesis: restate for the collar only (recommended), with (A) and (E) kept as named
   hypotheses of the anomaly result.
5. Rename the lattice result's id (it begins "spin-two-lattice-model") before acceptance.
6. The problem records: the "why" of op.positivity-of-values ((P) is not the only premise between the algebra
   and the bound), its false first step, the two ways on op.gravitational-field-at-null-momentum, the (O5)
   wording and the attack items of ROUTES.md as amended by the results.

## Not done
Mushtari 2001, Galley-Giacomini-Selby 2022, Fewster-Verch 2013 and the other memory citations were not read
(Boyle-Finn-Turok and Mottola-Vaulin were, in part, by an attacker and a referee). The baseline `tp check` and
the maintainer pass are recorded in MAINTAINER notes if run. Nothing was pushed: this session had read access
only.

## Supersession check against main at f9f3bee (asked by Leon, 24 November, during close-out)
Pull request #65 (run 2026-11-24-number-theory) was merged while this run was in progress. Compared:
- Result 1 of this run (additive weights for two or more modes) is SUPERSEDED by the stored
  synthesis.additive-weights-on-the-rational-projectors-are-linear-in-every-size-from-four: the same theorem, the
  same route (one reflection per vector, four squares, three hyperplanes) and the same counterexample to the
  pairwise step (the number 7). The stored version has more (the one-mode counterexample, the four-square theorem
  as its own entity, Mushtari 2001 read, the two-mode theorem reviewed line by line). This run's proposal has one
  clause the stored entity lacks: (vii), from three modes on additive weights on the projectors of the even
  subalgebra alone are linear, and for two modes they are not. The proposal is to be withdrawn and (vii) refiled
  against the stored entity if Leon wants it. The two derivations were independent and agree.
- Results 2 and 3 (the (RP) bound on the sum of correlators; (CP) and the reversal on one party) are not
  superseded. The stored two-mode theorem they pin is still version 1 (only its note changed). Each should cite the
  stored size-four result in place of the proposal filed alongside, and each can now be extended past two modes.
- Results 4 to 7 (both G, both H) are untouched: main changed op.positivity-of-values, op.wall-class-invariant and
  op.residue-killing-weights only.
- The record of op.positivity-of-values on main already says that more than two modes is done and that the named
  first step is false. Still new from this run for that record: the quantum bound needs only (CP), which is
  strictly weaker than (P); the reversal on one party; (RP) is (P) on projectors.
- The baseline `tp check` at 58338e0 was stopped unfinished after about 80 minutes (a full layer-4 run on a fresh
  clone, slowed by the attackers); the base has moved, so a baseline is to be taken on f9f3bee before any
  maintainer pass. Nothing has been applied to `store/`.

## After the change of base (rebased onto f9f3bee, 24 November, at Leon's instruction)
- The duplicate proposal is withdrawn (folder kept in withdrawn/).
- New proposal, a corollary of the stored size-four theorem:
  synthesis.additive-weights-on-the-even-projectors-are-linear-from-three-modes-on. The even subalgebra is two
  blocks of size 2^(l-1); for l >= 3 additive weights on the even projectors alone are linear, and with the sign
  condition they are the states of (P) that vanish on odd elements; for l = 2 this fails.
- The (CP) and reversal result: clause (iii) extended from a first party of two modes to m >= 2, with a uses edge
  to the stored size-four theorem and a new check (three modes of four).
- The (RP) result: cites the stored size-four theorem for the extension, not carried out there.
- The four G and H proposals revalidated against the new base unchanged.
- Central check4 and validate_draft clean on all seven (verify/check4-rebased, verify/validate-rebased). A third
  blind pass (Claude Opus 5.5, R-3.md) covers the new corollary and the extended clause.
- A baseline `tp check` on f9f3bee was started (baseline-f9f3bee.log); see MAINTAINER notes for whether it
  finished. Nothing is applied to `store/`.
- Third pass (R-3.md): both items SOUND WITH FIXES, fixes applied. The corollary gained clause (v), no two-valued
  additive weight on the even projectors for l >= 3 (the referee's proof, verified and checked exactly), and says
  that vanishing on odd elements is a choice of extension. Final gates clean (verify/check4-rebased2).

## Leon's decisions of 24 November 2026 and the maintainer pass
D1. (RP) stays a named hypothesis: not adopted, not rejected, written into no premise; the fork is on the record
    of op.positivity-of-values.
D2. The canonical pair on the two null directions is ADOPTED as Premise (TT), a postulate with the photon's
    status, at first order only (synthesis.premise-canonical-pair-on-the-two-null-directions). The conventions'
    section on gravity carries the decision; the sentences of 10 and 18 November are kept as dated history.
D3. The radiation-type descent hypothesis is restated for the collar only.
Defaults taken without asking: (CW), (A) and (E) stay named hypotheses of their results; nothing is imported;
op.gravitational-field-at-null-momentum is partial and not moved to the settled file; the lattice result's id was
renamed (it began "spin-two-lattice-model"); this run's seven results enter at version 1.

Carried out by three maintainer agents with disjoint ownership (MAINTAINER.md; maintainer-M-G.md, maintainer-M-H.md,
maintainer-M-O.md), text only: no proof, check or status changed in any stored result.
- New: the postulate (TT). Changed, version + 1: thirteen stored entities (the conventions' dependants on gravity:
  the first-order theorem's Reading, the lattice Maxwell result's Reading, the graviton note, the burst and
  no-indirect-signals predictions, the imported production rate, one dated sentence on the entangling-phase
  prediction; for D3: the Hadamard deposit premise, the tame-wall result, the two moment results; and the
  no-two-valued-weights result and the premise (P), one dated sentence each). store/conventions.md.
- store/open_problems.yaml: ten records (positivity, the gravitational field at null momentum, Einstein's
  equations, the graviton rate, the deposit state, the spectrum, the number N, the rung unit, the non-Gaussian
  completion, (Loc)); the routes of ROUTES.md not run are filed as attack items, as amended by the results.
- Repin: 29 edges in 24 dependants whose pinned statements are unchanged.

Checks in the workspace, after the last edit: layers 1, 2, 3, 5 and 6 of the whole store as the maintainer, 0 errors
(three warnings, all on entities this run did not touch: two W503 on results of pull request #65, one W501);
`tp check-one` (layer 4) on all 42 new, changed and repinned results that carry checks, every check passing
(verify/check-one/summary.txt); the 468 unit tests. A full layer-4 run of the whole store was not completed in the
workspace (the stored layer-4 record is keyed to another Python version); the pull request's required check runs
it. Lock, layer-4 record, build and site are left for the merge, as the pull request template asks.

## Decisions still with Leon (from the maintainer reports)
1. Does adopting (TT) meet the success clause of op.gravitational-field-at-null-momentum? If yes the record moves
   to the settled file and its open tasks need a successor.
2. Should pred.dimmed-evaporation-bursts `assume` (TT)? Its ratio now keeps g on the strength of the premise; no
   edge was added.
3. The state of the pair near a hole: extend the Hadamard deposit premise to it, or keep the proviso.
4. pred.gravity-entangles-standard-phase: restate its scope sentence, lay level, one-liner and kill condition to
   D2 (only one dated sentence was added).
5. Stored entities outside the pass that still carry the position of 10 November (listed in maintainer-M-G.md):
   restate in a later pass, or leave the conventions as the reading rule.
6. (P) and Krein expectation values: whether to write the scope sentence (not a consequence of stored text).
7. The title of the wall-conjugation result still says "radiation-type descent"; it assumes more than the collar
   hypothesis and says so in a dated note.
8. Hypothesis (A): import as a Fact later, or keep named. Literature cited from memory throughout is still to be
   read (Galley, Giacomini and Selby; Weinberg; Deser; Fewster and Verch; Navascues and Wunderlich).
9. documents/trail-thermality quotes an old one-liner and needs regenerating at the merge.
