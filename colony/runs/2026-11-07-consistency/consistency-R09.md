# Consistency read R09: walls, descent, programme, standard-quantities

Reader R09, 7 November 2026. All 318 entities of read_R09.txt read in full: for every claim, object, note and
quantity the front matter (derivations, assumes, pins, extraction notes), all four levels, and every proof file
(proof-main.tex, proof-standard-route.tex; orig-* and merged-* history files not reread). Order: walls (143),
programme (6), descent (126), standard-quantities (43). Hand or exact recomputation of every displayed identity
I could recompute (listed under "Checked"); one exact GA check run in scratch (pairing creator in Cl(2,2)).
tp check layers 1-3 run once after the edits: no error or warning on any R09 entity (only the pre-existing I213).

## Fixed (maintainer bookkeeping: version + 1, credit, extraction.maintainer_pass_consistency)

- dark-energy.wall-counterterm 4 -> 5: the Chern-Simons three-form was written Q(omega), the store's symbol for
  the square of a vector; now CS(omega) (and d CS) in formal, technical, one-liner and proof. Formulas unchanged.
- synthesis.wall-rung-count-is-height-of-dying-line-class 1 -> 2: proof, torus paragraph, half-angle pair (c, s)
  clashed with s = G^{-1}(u,u) of clause (2) and F; now (c, sigma) as in the twisted-induction entity.
- synthesis.lens-space-wall-rung-count-sees-the-integral-twist 4 -> 5: formal said the classical inputs were
  "cited from memory, not imported", but the derivation uses and the proof cites
  synthesis.imported-stiefel-connectivity-and-grassmannian-classification; the formal now cites that Fact. The
  closing remark's fibre coordinates (s, t) clashed with the cometric parameter t; now (y1, y2).
- three-routes.it-sheaf-risk-resolves-into-standing 6 -> 7: the proof's last sentence still said A^+ exists only
  in the twisted sense, contradicting the statement as corrected on 2026-10-23; now says sigma (quadratic in the
  ladder) and A^+ are sign-insensitive and only the ladder bundle needs the twist.
- singularity.modular-descent 7 -> 8: proof wrote the modular flow as sigma_t while sigma is the boost element of
  the same entity; now t -> Ad(rho^{Jt}).
- synthesis.univalence-from-even-stationary-dynamics 4 -> 5: Majorana generators were e_{2k-1}, e_{2k}, so e_2,
  e_3 named mode generators in the same sentence that defines J = e_2 e_3 (spacetime); Majoranas renamed mu_j in
  formal and proof; proof of (4) wrote sigma_x for a + a* while sigma_k is the parity element; now a + a*.
- singularity.purity-output-partner-commutant 4 -> 5 and state-selection.partner-purification-are-canonical 4 -> 5:
  formal now says the scalars of the mode factor are span{1, e2e3} (U2) and that J there is the modular
  conjugation, not that unit (the cited Schmidt-forcing lemma writes J = e2e3).
- descent-lift.imported-pinching-one-way-door 3 -> 4: \mathrm{Mat}_2 by hand in formal and proof; now \Mat as in
  its technical level.
- note.descent-lift.setting-machine-verification 1 -> 2: bare imaginary unit "$iN_0(...)$" (missed by the tp
  detector, which does not catch i followed by a capital) now I_4 N_0(...), as in
  descent-lift.within-supplied-dynamics-descent-has-no.
- note.state-selection.setting-gap-stated-exactly 2 -> 3: "honesty" twice (house style); now "it does not pretend
  otherwise" and "That admission".
- note.state-selection.setting-machine-verification 2 -> 3: bare "I" for the pseudoscalar now I_4.
- Extraction only, no version change: singularity.modular-structure-completed-pair (unit_note "the imaginary unit
  stays a scalar i" is stale: no i remains, the atom's unit is J); one-relation.imported-flag-arrow-superselection
  (correction note says an assumes edge to dark-matter.premise-trichotomy-exhaustive is kept; it is gone).

Pins left as they were (the brief forbids changing pin targets): these bumps leave dependants pinned at the old
versions (notation-only changes), e.g. singularity.modular-descent@7 (6 users, among them
hawking.imported-modular-descent-premises-geometric-normalisation), dark-energy.wall-counterterm@4 (5 users),
state-selection.partner-purification-are-canonical@4 (3), singularity.purity-output-partner-commutant@4 (1),
synthesis.wall-rung-count-is-height-of-dying-line-class@1 (1), descent-lift.imported-pinching-one-way-door@3 (1).

## For Leon

1. sheaf.wall-class (conjecture), clause (b) "shifting both clock coordinates by the rung", and
   note.sheaf.wall-class-posed ("advances the clock of [T1 Sec. 7]"): the rung (+1,+1) leaves d = p - q mod 8
   unchanged (note.sheaf.setting-wall-class-posed-precisely: "which fixes clock position";
   synthesis.wall-class-one-rung-obstruction: "preserves both clock positions"; tower.rigidity-clock-frozen: d
   constant along the tower). Proposed (b): "...transferring it to the next shadow wall, the rung shifting both
   signatures by (1,1) and leaving both clock positions unchanged". Also: synthesis.wall-class-one-rung-obstruction
   proves clause (a) cannot see torsion in either reading of "standard"; the conjecture as posed should be
   restated (status stays conjectured), e.g. with clause (a) replaced by the one-rung (or k-rung) completion.
2. singularity.sheaf-assembly-sheaf, formal last sentence "For w1(L) != 0 the mode bundle itself, and with it M,
   exists only in the L-twisted variant" contradicts three-routes.it-sheaf-risk-resolves-into-standing as
   corrected 2026-10-23 (M is built from Ad sigma, glues on a twisted ladder bundle, does not see the twist; its own
   technical level says sigma "does not see its sign"). Proposed: "For w1(L) != 0 the mode bundle itself exists
   only in the L-twisted variant; its even part, span{1, sigma}, is untwisted, so M is defined there as well and does
   not see the twist." Same staleness in note.three-routes.setting-metric-level-sheaf ("the obstruction that would
   have prevented gluing is precisely the standing hypothesis").
3. dark-energy.wall-counterterm (not GA-owned): whole entity in differential forms and frame components (omega^{ab},
   R^{ab}, epsilon_{abcd}); a GA rewrite is not a small stand-in. Also the formal identifies omega^{ab} with the
   rotation-gauge field Omega, while conventions.md (GTG) says Cartan-form connection values are the negative of
   Omega on vectors and results setting them beside a GTG formula must say so; CS and its value 8 p1p2p3 are odd
   under omega -> -omega in the cubic term, so the sign convention matters. Proposed: state that omega^{ab} are the
   Cartan connection forms (curvature d omega + omega ^ omega), i.e. minus Omega on vectors, after checking the
   source T10 Prop 4.11.
4. three-routes.imported-collar-data-coupling: a claim with status proved, empty derivation and no about link, which
   restates the definition obj.sheaf.collar-data-coupling verbatim. Proposed: add about: obj.sheaf.collar-data-coupling
   (or merge into the definition and repoint its three users).
5. Duplicates (below): decide merge or link.
6. Language (non-owned, not small): Pauli-string labels X_{R1}X_{L1}Z_{L2}, Z_{R_k}Z_{L_k} (proof of
   singularity.p-reduced-metric-level-reading-many, obj.singularity.multi-mode-descent, two T05 notes) and
   sigma_x sigma_y "controlled-Z" for the parity sections at two points (three-routes.support-preserving-families,
   three-routes.class-relative-no-go): GA would write products of the mode parity sections and Majorana elements.
7. Convention, harmless but unstated: singularity entities write Gamma = prod_k sigma_k with sigma_k = 2N_k - 1, the
   descent-lift entities Gamma_k = (-1)^{N_k} = -sigma_k; the two total parities differ by (-1)^N; only Ad(Gamma)
   is used.

## Duplicates

- sheaf.base-unipotents-wall == three-routes.base-unipotents-their-action-candidates (no link; sheaf's is the T4
  home). sheaf.solve-closed-radical-gauge == three-routes.radical-gauge-closes-solve (equivalent_to already set).
- sheaf.transversal-independence-wall > three-routes.change-transversal-canonical-isomorphism-completions (sheaf adds
  the cocycle and the images of k*, sigma; the three-routes "carries ladder to ladder" means to another ladder of
  the same k). sheaf.no-equivariant-value-wall > three-routes.no-equivariant-value-boundary (sheaf adds the partner
  clause); singularity.imported-no-equivariant-value-wall restates sheaf's (fine).
- singularity.modular-structure-completed-pair > hawking.modular-structure-completed-pair (twins; singularity's has
  the two-component rotor-group caveat; no restates/equivalent_to link, hawking's uses only std-algebra).
- singularity.purity-output-partner-commutant == state-selection.partner-purification-are-canonical (same theorem,
  T05 and its state-selection note; not merged).
- singularity.net-assembly-net-it-everything ~ three-routes.join-disqualified-wrong-stalks;
  singularity.sheaf-assembly-sheaf ~ three-routes.it-sheaf-risk-resolves-into-standing +
  three-routes.stalks-are-pointwise-metric-levels (three-routes.sections-are-meet already merged into
  singularity.finite-truncation-meet-big-fibres-equals). The three-routes versions carry the 2026-10-23 correction.
- singularity.imported-general-form == state-selection.imported-general-statement (equivalent_to set).

## Known open items

None of the six listed items falls in R09's entities (none of their ids is on read_R09.txt).

## Checked (selection)

Wall Gram det -2 mu nu, w and signatures; Schur complements and det h identities (one-sided, located shadow wall
trace argument, variable weight det h = c2c3(1 + rho c1), twisted det h = -det G (1 - 2 x), torus t - 2 mu nu);
infinite-wall kernel section; transversal intertwiner pairings and Phi(sigma); edge-wall q(v) on the Kasner variety,
q1q2, d(1) - d(u), p(1/u); Kasner weights (orders (-1, 1, -2)); rain coframe, L^{-1} of the null dyad, G(rho,rho);
Lambda-line Gram, signatures, residue -3, totals (2,4); one-rung D^2, J^T D J = -D, the Z' sign analysis; k-rung
ranks; lens-space O(BR) = D O(R), h_W, N(h_0); tameness block-inverse identity; corank-two Lemma B and cone lines;
KMS conventions (all match U2: tau_{J beta} = Ad(e^{-beta K}), modular flow tau_{-beta t}); Gibbs uniqueness;
graded functional; modular-descent counterexamples; transverse-bivector clauses; univalence (ii)-(v); descent-lift
C identity, W^dag W, partial-lift 7/25, Kraus ranks; pairing creator X_p, X_h, n n^dag = P11, X_p^2 = -P_even (GA,
exact); quantities: Lambda = 1.0909e-52 m^-2 (2.85e-122 Planck), M_P/sqrt(8 pi), v = 246.2196 GeV, M_sun, g*,
Omega_c/Omega_b = 5.364 +- 0.065, and every lay ratio.

## Counts

318 read in full; 12 entities changed with a version bump (9 claims, 3 notes), 2 extraction-only; 7 For-Leon
items; 9 duplicate groups; 11 GA-owned entities, issues for 5 in ga-issues-R09.md; 3 cross-subject items in
xsubject-R09.md; 0 known open items in scope.
