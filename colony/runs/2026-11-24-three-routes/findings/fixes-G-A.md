# Fix round, G-A (referee report verify/R-G.md, proposal 1)

## synthesis.spin-two-lattice-model-static-slaved-field-fails-and-dressed-pair-detection-commutes
Verdict: SOUND WITH FIXES (counts reproduced by the referee). All eight listed fixes applied in place, at every
level; nothing rebutted. No conclusion reversed; one statement strengthened (3a), one outcome restated (G1).
Files changed: entity.md, proof-main.tex, check.py, coverage.yaml.
runcheck: 9 of 9 functions pass (one function added), about 7 seconds. check4: pending (orchestrator).
validate_draft: pending (orchestrator). The check has a new function, so the central mutation test should be rerun.

What changed:
1. Title. The referee's title is over 90 characters; same content in 86: "Lattice first-order gravity: slaved
   field, dressed pair, no local dressing of one mass". "Spin two" and "one mass has no dressing" are gone. The id
   is kept: its slug (static slaved field fails, dressed pair detection commutes) asserts nothing false, though it
   still begins "spin-two-lattice-model"; a rename to "first-order-gravity-lattice-model-..." is a maintainer
   choice.
2. G1 stated plainly, in the extraction note, the first Reading and the technical level: by the registered
   condition G1 is met for one mass moved alone and not met for the pair; reading the former as a restriction on
   which detections are local (the mass dipole is a charge of the constraint that no dressing screens) is argued
   after the computation. "Restriction on the matter" is removed everywhere. Added: the obstruction is in the
   Hamiltonian constraint alone, so it holds for the slaved variant and whatever the free part is made of; the
   motivating experiment (one mass on two paths) is of the single-mass type and needs its recoil partner, which is
   argued and not modelled.
3. New proved clause (3a), the referee's lattice lemma, proved and checked exactly here: if G[f'] vanishes outside
   a box, D f' has no monopole and no dipole, whatever the support of f'. Proof in the text (pairing of G[f'] with
   displacements vanishes by the contracted identity; the displacement by xi_i = 2 x_l x_i - delta_il |x|^2 is
   4 x_l delta plus a constant field, exactly, with the constant -2 on the component ll and -1 on the pairs with
   l; constant fields are displacements by linear xi; D = -2 tr G). New check function
   check_curvature_confined_to_a_box_rules_out_a_dipole_of_the_constraint_source: the displacement identity on
   125 sites for each l; a field of unbounded support with confined curvature pairs to zero with the quadratic
   displacements and the constants and has D with no monopole and no dipole; and, as the example of a non-compact
   dressing of one mass, the Newtonian one has curvature on 3590 of 4212 components outside the 27 sites about
   the centre (computed). The Reading's "dressed by any field" now rests on (3a); "is not shown on the lattice"
   is dropped. Candour: the sampled field in the check is a compact field plus a displacement plus a constant,
   for which the conclusion also follows from (3); the general statement is the proof's, and the coverage record
   says so.
4. Model wording. Lay level rewritten with the referee's replacements ("In the model, ...", "In the model (and,
   by an argument, in weak gravity generally) ...", "everywhere outside the measurement's reach on the grid") and a
   sentence that a grid has no rotations and its own speed limit. Technical level and one-liner say "the lattice's
   cone (one site a step, twice the wave speed)" wherever a count is given, and say that the commutation of the
   dressed pair holds "as in any local canonical lattice model once a dressing of compact support exists".
5. Cones. Clause (8) now says that every cone and count is the lattice's, defines depth from the nine components
   on which f is nonzero, and gives the split against a cone of unit speed. Recomputed: with d the Euclidean
   distance from a component's base site to the 22 sites where G[f] is nonzero, 3490 of the 8736 failures have
   d <= n/2 and 5246 have d > n/2 (the referee's count, reproduced); of the 3490, 671 are not later than the
   detection and 3423 have d > |n - 3|/2. These are in the check. The text says that the 5246 are events where a
   wave of unit speed from the source has not arrived, that the stored Maxwell model's "none spacelike to the
   source" does not carry over, and that the statement surviving a change of cone is the one about the 3490.
   Note for the record (scratch, not in the proposal): the split depends on where distance is measured from.
   From the three string sites instead of the support of G[f] it is 617 inside and 8119 outside. I kept the
   referee's measure because a curvature component reads h within one site, so the support of G[f] is the set of
   sites whose curvature the source data touch; the clause names the measure.
6. First Reading: "new and belongs to spin two" is now "new relative to the stored Maxwell model (it is
   standard; see the prior art in the note)"; the technical ledger says nothing here is new to the literature and
   lists what is new relative to the store.
7. Minor. Proof (1): "plane wave of wave vector kappa" in place of the undefined unit; clause (1) and its proof
   say the leading symbols do not tell a forward from a backward difference and that the stencils are fixed by
   the identities of (2) (the referee's surviving perturbation; the coverage record names it). Clause (10):
   "its spatial scalar curvature D h is g rho_s". Clause (3): the coordinates are now x_k (they were written s_k,
   clashing with the forward difference). "What the model is and is not": no rotations (helicity two has no
   lattice meaning), no Lorentz covariance, no charges at infinity on the periodic lattice, the motion between
   arrangements not modelled.
8. Weinberg: cited as "Weinberg 1964, 1965, and Deser 1970; from memory, the reference to be checked". I could
   not read the papers here, so I did not choose among them.
Overlaps: the extraction note cites the result filed alongside (the helicity-two composites entity, its clause on
a medium with causal commutators) in text only, as the reason the commutation is not specific to canonical
variables either. Nothing merged, nothing added to `uses`.
Bridge B3: no sentence of the proposal contradicts it ("the registered entangling phase does not depend on (TT)"
stays true); no text change. Listed below as a decision.

## Repin on acceptance
None. Every pin is to a stored version.

## Next steps (leads, not pursued)
- B3: the premise list of pred.gravity-entangles-standard-phase (P-v, "no free radiative part").
- Whether a medium that is not canonical can carry the dressing in a model with the constraint (the referee's
  tension 1): neither proposal shows it.
- Moving matter: momentum constraints with a matter term, so that the recoil of a single mass is modelled and not
  argued.
- The same failure counts in a scheme whose cone is the unit-speed cone (an exact-cone discretisation), to remove
  the 5246 precursor events instead of setting them aside.
- Read Weinberg 1964, 1965 and Deser 1970 and fix the citation; read the other prior art cited from memory.

## Decisions for Leon
1. (TT): adopt, reject or leave open (unchanged from the attack round; sufficient at first order in the model, not
   shown necessary).
2. The outcome of G1: met for one mass moved alone. Accept the reading that this restricts which detections are
   local (argued), or count it against the route for the single-mass experiment.
3. B3 (bridge pass): the registered prediction's kill condition refers to premises P-i to P-vi, of which P-v (no
   free radiative part) the conventions' requirement of 18 November already rejects. Restate the kill condition
   with P-v replaced by its successor, or say why P-v stays. The phase itself stands.
4. Whether to rename the id (it still begins "spin-two-lattice-model").
5. Prior art cited from memory: import as Facts or correct, in the maintainer pass.

## Second pass (verify/R-2.md, item 1)
Verdict: SOUND WITH FIXES; (3a) and every count of clause (8) reproduced by the second referee. All five fixes
applied in place; nothing rebutted. runcheck: 9 of 9 pass. check4 and validate_draft: pending (orchestrator).
1. Clause (8), last sentence: what survives a change of cone is the 3423 failures that are inside the unit-speed
   cone of the source event and also outside the unit-speed cone of the detection, 604 of them not later than the
   detection; the other 67 of the 3490 are at the step of the detection at sites where G[f] is nonzero. Verified
   here and now in the dynamics check: 3423, 604, 67, and that all 67 have n = 3 and d = 0. The proof, the
   technical level and the coverage record carry the same numbers.
2. Clause (8) definitions: the base site of a component (the site at which it is indexed in the stencils, the
   plaquette components included); d to the nearest of the 22 sites; least-image Euclidean distance on the
   periodic lattice; the two cones defined by d <= n/2 and d > |n - n_d|/2, inequalities as written; 3423 said to
   count events outside the unit-speed cone of the detection.
3. One-liner: "3423 of these also outside the detection's" added; "no dressing by one Weyl operator of compact
   support or of confined curvature".
4. Title: "Lattice model of first-order gravity: slaved field, dressed pair, the dipole obstruction" (88
   characters). The referee's opening is used; "no local dressing of one mass" did not fit in 90 with it, and
   "the dipole obstruction" names clauses (3), (3a) without asserting more than they do.
No new decisions for Leon.
