# Findings, cluster W (walls), run 2026-11-18-leads

One attacker, both angles. Problem: op.eigenbundle-class-of-degenerations (all four attack items), with
op.wall-class-invariant, op.kerr-ring (first item) and op.order-four-anomaly-and-sixteen read against it.
Labels: proved / computed / argued / conjectured / from memory. Kill conditions are written here before the
computation they govern; outcomes are filled in after.

## Orientation (lookups made)
get_open_problem: op.eigenbundle-class-of-degenerations, op.wall-class-invariant, op.kerr-ring,
op.order-four-anomaly-and-sixteen. get_claim: synthesis.strict-completions-exist-exactly-when-the-signature-does-
not-jump (v1), synthesis.wall-class-one-rung-obstruction (v3), sheaf.wall-class (v3), sheaf.tameness,
sheaf.conservation-degeneracy-absolute-form (v4), synthesis.wall-rung-count-is-height-of-dying-line-class (v2),
synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial (v2), the three Kerr ring results,
std-algebra.spin-double-cover, the imported bundle Facts (real line bundles, Whitney formula and projective space,
Stiefel connectivity, line bundles classified), dark-matter.residue-soldered-invariant-not-algebraic-one,
synthesis.order-four-structure-on-real-projective-walls-and-the-signed-count-modulo-sixteen. Previous run:
REPORT.md, findings/attack-main.md of 2026-11-18-navigate.

## Routes considered (for the class of an isolated degeneration, leads 1 and 4)
R1 (the problem's own): a cell model of the two-sphere and a cocycle for the second Stiefel-Whitney class.
   Delivers a class in the stored cellular language. Needs the stored cellular background and the stability of
   the class under adding trivial directions (the imported Whitney formula) and an identification of the cocycle
   with the class of the bundle. Fails if the identification has to be imported.
R2 (from another subject, std-algebra.spin-double-cover): clutching function of the eigenbundle on the equator
   and its lift to rotors. A stably trivial bundle has a contractible clutching loop of rotations; a contractible
   loop lifts to a closed loop of rotors; the eigenbundle's loop is one full turn in a plane, whose rotor lift ends
   at -1. Delivers the stable statement with no characteristic class imported. Needs only the lifting of a
   homotopy through the two-sheeted cover, which can be written out. Fails if the clutching function computed
   from the family is not a full turn.
R3 (own): for sufficiency, the rotation homotopy F (+) F^{-1} ~ 1 in the orthogonal group of doubled rank: it
   contracts any pair of trivialised eigenbundles once as many positive directions are added as the total rank.
   Delivers an explicit completion. Needs frames of the two stabilised eigenbundles on the sphere. Fails to give
   the least number of added directions.
Chosen: R2 for lead 1 (self-contained, and it is the store's own object: the rotor of the full turn is -1), R3 for
lead 4. R1 is not pursued: it would add an imported identification that R2 does not need.

## Kill conditions (registered before computing)
K1 (lead 1). The claim "the positive eigenbundle of the position vector on the least module of Cl(3,0) is not
   stably trivial" is killed if the clutching function, computed exactly from three symmetric anticommuting
   generators on R^4 with hemisphere frames P(x)v (v in the +1 and -1 eigenspaces of E_3), is not a rotation
   through one full turn in a single plane (for instance if it is the identity, or a turn in two planes), or if
   its rotor lift returns to +1. Then the bundle may be stably trivial and the lead flips to "find that it is".
K1b (lead 1, larger modules). The claim "on 4k dimensions the obstruction is present exactly for k odd" is
   killed if on two copies of the least module no fourth symmetric anticommuting generator exists (exact search
   of the commutant), or if the rotor lift for k = 2 ends at -1.
K2 (lead 2). The claim "the relative eigenbundle class of a tame wall is the dying line, and agrees with
   (w(Sigma), w_1(L))" is killed if on an explicit tame wall (the twisted line over a circle,
   G = P_perp + s P_L) the positive eigenbundle on the two sides does not differ by a line with the holonomy of L,
   or if the necessary condition that transfer gives for k rungs differs from the stored necessity clause
   (N of rank k - 1 with L (+) N stably trivial of rank k) on any of the stored cases: the Whitney bound x^k = 0,
   the two-rung statement, the K-theory bound 2^{k-1}(1 - xi) = 0. A disagreement is then the result.
K3 (lead 3, as the brief registers it). The reading "the winding number three is an invariant of a completion" is
   killed if the stored winding is defined for a connection (or a field-strength scale) and not for a family of
   symmetric forms, and no completion statement of the stored theorem applies to the Kerr cometric at the ring
   (for instance because the Kerr-Schild cometric does not degenerate there). Second condition, for the cover:
   the reading "the forced double cover is the degree-one class of [[x,y],[y,-x]]" is killed if the stored
   potential H is not an odd function of a unit section of that family's positive eigenline in the stored normal
   coordinate w (exact identity to test: H = M <1, z>/Q(z) with z^2 = w and z spanning the positive eigenline of
   Re(w~ v^2); and H^2 single valued).
K4 (lead 4). The claim "over R^m, with the degeneration inside a ball, a completion with a fixed exterior form
   exists whenever the positive eigenbundle is stably trivial on the bounding sphere" is killed if the explicit
   family Phi_t = (F (+) 1) R_t (1 (+) F^{-1}) R_t^{-1} fails to be orthogonal, fails to join F (+) F^{-1} to the
   identity, or gives a degenerate form at some sample point of a worked example (two copies of [[x,y],[y,-x]]).
   The unstable counter-claim "vanishing with the given K_0 suffices without further directions" is killed by the
   family Re(w~^2 v^2) (winding two) if its eigenlines are trivial and no completion of rank two exists.
K5a (lead 5a). "A jump with equal residues is invisible to the tower classification" is killed if some stored
   invariant of the tower classification (residue, algebra type, graded type, even subalgebra) differs between
   the two sides of x id in rank four. The scope claim "exactly the jumps by a multiple of four eigenvalues" is
   killed if a jump by two eigenvalues leaves the residue unchanged.
K5b (lead 5b). "The link to the sixteen of the order-four problem runs through real K-theory of the wall" is
   killed (as a link, leaving a resemblance) if the eigenbundle class of the projective wall RP^5 with
   tautological dying line has order different from sixteen in the stable group. Test: N copies of the line are
   trivial when R^N carries five anticommuting complex structures (exact construction), and 4 copies are not
   stably trivial by the stored Whitney formula.

## Kill conditions: outcomes
K1  not fired. Computed exactly: the clutching function is gamma = [[c, s], [-s, c]] at x = (c, s, 0), one full
    turn in one plane; the rotor cos(a/2) + sin(a/2) f1f2 runs from 1 to -1 (work/W/P1/check.py).
K1b not fired. Two copies of the least module of Cl(3,0) are the least module of Cl(4,0), and e4 is a fourth
    symmetric anticommuting generator; on one copy the linear system has only the zero solution; for k planes the
    lift ends at (-1)^k.
K2  not fired: agreement. On the twisted wall of the cylinder the eigenbundles differ across the wall by the dying
    line; the condition transfer gives for k rungs is the stored necessity clause, and the Whitney bound and the
    K-theory identity (1 - xi)^k = 2^(k-1)(1 - xi) follow from it (work/W/P3/check.py).
K3  first condition FIRED: the stored winding is the winding of the field-strength scale and of the normalised
    limit of the connection, sections of a plane on which the duality rotations act; it is not defined for a
    family of symmetric forms, and the Kerr-Schild cometric eta^-1 + 2H k k has the determinant and signature of
    eta^-1 wherever H is finite (computed at 24 rational points on both sheets and for coefficients of size 10^6): there is no
    degeneration set at the ring, only a divergence, so no stored completion statement applies. The reading "the
    winding three is an invariant of a completion" is dead. Second condition not fired: the identity
    H = M <1, z>/Q(z), z spanning the positive eigenline of Re(w~ v^2), holds exactly, H is odd under the deck map
    and H^2 = M^2 (1 + Re w/|w|)/(2|w|) is a function of w (work/W/kerr_ring.py).
K4  not fired. The rotation family is orthogonal and joins F (+) F^-1 to the identity; the worked completion on R^8
    has signature (6,2) at 19 angles and 12 radii. The unstable counter-claim is killed as registered: the
    winding-two family has trivial eigenlines and no completion of rank two (proved with the lifting lemma), and
    one added direction completes it (work/W/P2/check.py).
K5a not fired, scope corrected. The residue, and so the algebra of the stored table, agree on the two sides of
    x id in rank four.
    Two sign changes move the residue by four, so the invisible jumps are those by a multiple of FOUR eigenvalues,
    not every even jump (work/W/lead5.py).
K5b FIRED: the class of the tautological line over RP^5 has order eight in the stable group, not sixteen (eight
    copies are trivialised by five anticommuting complex structures on R^8, built exactly; four copies are not
    stably trivial by the stored Whitney formula). Order sixteen first occurs on RP^8.

## Results, lead by lead

### Lead 1 (m = 3). PROVED. Proposal 1
synthesis.position-vector-eigenbundle-in-codimension-three-has-a-class-of-order-two (check4: 0 errors).
- proved: on the least module S = Cl(3,0)(1+e3)/2 the positive eigenbundle of the position vector over the
  two-sphere is pi(x)S; its clutching function on the equator is one full turn; neither eigenbundle is stably
  trivial (the stable statement, not only the unstable one). Method: a trivialisation after adding N directions
  gives a contractible loop of rotations; a contractible loop lifts to a closed loop of rotors (lemma proved in the
  text from std-algebra.spin-double-cover and compactness); the lift of the full turn ends at -1.
- proved: no completion with a fixed exterior form, with any added directions, for any bounded U (stored transfer
  clause). Strict completions exist (the double).
- proved: on k copies the class is (-1)^k; for k even the family is repaired on the same module by the fourth
  generator of Cl(4,0), with no added direction. So a fixed-form completion exists iff k is even: a class of order
  two and of degree two.
- from memory, not used: this sign is w_2 and is the whole reduced real K-group of the two-sphere.
- out of reach here: codimension five and the other residues 1, 2, 3, 5 mod 8 beyond m = 3. Reason: for m = 5 the
  class has infinite order and lives on the four-sphere; a proof in these terms needs an integer invariant of a
  three-sphere of rotations that survives stabilisation (the degree of the clutching map into the unit
  quaternions and its stability), which the store does not hold. First step: import the third homotopy group of
  the rotation groups, or the first Pontryagin class, as one Fact; or import the periodicity theorem itself.
Ledger: transport-convenient.

### Lead 4 (sufficiency). PROVED. Proposal 2
synthesis.fixed-form-completion-over-a-ball-exists-iff-the-eigenbundle-is-stably-trivial (check4: 0 errors).
- proved: over R^m, for a family degenerating only inside a ball B, a completion with a fixed exterior form,
  standard outside B and nondegenerate everywhere, exists iff the positive eigenbundle is stably trivial on the
  sphere. Necessity is the stored transfer clause; sufficiency is explicit: with frames F of the two stabilised
  eigenbundles, (F (+) 1) R_t (1 (+) F^-1) R_t^-1 joins F (+) F^-1 to the identity and is used along the radius.
  Cost: N = n + c + c' added positive directions (an upper bound).
- proved: the added directions are needed in general. [[x^2-y^2, 2xy],[2xy, y^2-x^2]] has trivial eigenlines and
  no completion of rank two; one added positive direction completes it. So the attack item's question, read
  literally ("after adding the form's eigenspaces"), has the answer no for the given form and yes after flat
  directions are added.
- not treated: bases other than R^m; neighbourhoods that are not balls (a ring with a solid torus: the exterior
  is not a sphere and the condition is an extension problem over it); the least number of added directions;
  completions restricting to G inside U.
Ledger: transport-absent in proof (textbook rotation homotopy), transport-convenient in use.

### Lead 2 (tame walls). PROVED: agreement. Proposal 3
synthesis.eigenbundle-class-of-a-corank-one-wall-is-the-dying-line (check4: 0 errors).
- proved: across a compact corank-one sign-changing wall with a product collar the positive eigenbundle loses the
  dying line L and the negative one gains it. The eigenbundle class of the wall is L: rank = signature jump
  (residue: the clock mismatch 2), isomorphism class = w_1(L). It is the stored pair (w(Sigma), w_1(L)), neither
  finer nor coarser. (T3) and smoothness are not used; hypotheses are stated directly and no assumes edge is
  proposed.
- proved: transfer across the wall for every two-sided completion nondegenerate everywhere, with no condition
  along the wall: G-bar_- (+) (K_ph)_- = G-bar_- (+) L (+) (K_far)_-, and the mirror statement for the positive
  parts. With k rungs on the physical side this is a necessary condition of the same FORM as the stored necessity
  clause of the rung count, with N the negative eigenbundle of the far side's exterior form. (Corrected in the fix
  round: the stored clause is one-sided and has no far form; it is not rederived, and its N is not identified by
  this result. The lower bounds of the same form hold for the two-sided count.)
- proved (one example): on the twisted wall of the cylinder one rung fails on either side, and an explicit
  two-rung two-sided form is nondegenerate everywhere, its far form carrying a negative line twisted like L.
- argued, not proved: the same rotation gives a two-sided k-rung completion whenever L embeds in a trivial bundle
  of rank k with a complement that extends over the far exterior. Not decided: whether the two-sided rung count
  equals the stored one-sided count k(Sigma).
- Lens-space rung counts: no disagreement found (the referee's cross-check agrees: with q = 0 two rungs fail on
  L(4,1), with q >= 1 the condition can hold). The stored one-sided counts do not follow from this result. No new
  rung count is obtained.
- Draft restatement of sheaf.wall-class clauses (a) and (c): work/W/wall_class_restatement_draft.md. Not filed
  (the proposal cap is used, and restating a conjecture is Leon's decision).
Ledger: transport-absent.

### Lead 3 (Kerr ring). Negative result for the winding; identification for the cover. No proposal.
- computed and proved (exact algebra, work/W/kerr_ring.py): with w the stored normal coordinate of the ring and
  z^2 = w, the plane family G_w(v, v) = Re(w~ v^2), which is [[x,y],[y,-x]] in the coordinates (Re w, Im w), has
  positive eigenline R z and negative eigenline R Iz, with eigenvalue Q(z) = |w|. The stored double cover is the
  orientation cover of that eigenline, and the Kerr-Schild potential is H = M <1, z>/Q(z): linear in the unit
  eigenvector, hence odd under the deck map, with H^2 = M^2 <1, P_+ 1>/|w| a function of w. So yes: the forced
  cover is the degree-one class of the two-dimensional example pulled back by w. Caveat stated: a punctured
  plane has one nontrivial double cover, so the identification of classes is forced by parity alone; what is not
  forced is that H is a function of the eigenvector of that family.
- argued (on stored statements): the winding three is the homogeneity degree of the field-strength scale -M z^-3
  in the eigenvector z; a class of degree one of a real line is a parity. The potential (degree one) and the
  curvature (degree three) carry the class; a field of even degree (the stored remark on a Kerr-Newman Maxwell
  field, degree two) does not. Three is therefore not an invariant of the cover or of any completion; only its
  parity is, and it is the holonomy -1 already stored.
- kill condition K3 (first part) fired: no completion statement applies, because the Kerr cometric does not
  degenerate at the ring. A statement of that kind would need a family of symmetric forms degenerating on the
  ring; the rescaled cometric on the blown-up cover degenerates on the whole exceptional set and was not treated.
- Out of reach: attack item 1 of op.kerr-ring proper (the bundle of exceptional algebras in the sense of T4's
  Prop 6.1). Reason: it concerns the connection's limit algebra, to which the eigenbundle class does not speak.
  First step: decide whether the conjecture's "winding number three as an invariant" is to be restated as the
  parity (the class) plus the degree of the field.

### Lead 5a (even rank jump invisible to the tower classification). Confirmed with a corrected scope. No proposal.
- proved (stored clause (7) with dark-matter.residue-soldered-invariant-not-algebraic-one(i), plus an exact
  enumeration): the residue agrees across a jump by a multiple of four eigenvalues, and with it everything the
  stored classification reads off the residue and the dimension (the algebra, its even subalgebra); a jump by two moves the residue by four and is visible. The brief's "even rank
  jump" should read "rank jump divisible by four". In dimension four the only pair is (4,0), (0,4); in dimension
  six (6,0)/(2,4), (5,1)/(1,5), (4,2)/(0,6): the physical tower's floor (2,4) shares its residue with (6,0).
- what it means for stored statements (searched by phrase across all claims: same or equal residue, separate
  residues, between towers, within a tower, inter-tower; the roughly 45 claims that mention both walls and
  residues were not each read in full): none found that asserts the converse "equal residues, hence no wall between". The statements at risk in wording are those
  that call the walls "the mod-8 shadow walls that separate residues" (dark-matter.superselected-hence-dark-
  exactly-stable, standard-model.imported-sectors-superselection-mirror-copy): true of tame walls, each of which
  moves the residue by two; the conserved label is the signature (the stored soldering theorem says so), and one
  residue class contains several signatures of one dimension from dimension four on. No correction is needed; the
  coarse part of the wall class should be called the signature jump, with the clock mismatch as its residue (in
  the draft restatement).
Ledger: transport-essential as a caution on the residue label; nothing new proved beyond the enumeration.

### Lead 5b (link to the sixteen through real K-theory). A resemblance, with one real common mechanism. No proposal.
- computed: the position-vector family on a module of dimension N trivialises N copies of the tautological line
  over the projective space of the sphere (g(-x) = -g(x), g(x) invertible). With five anticommuting complex
  structures on R^8, eight copies are trivial over RP^5; four are not stably trivial (stored Whitney formula). So
  the eigenbundle class of the projective wall RP^5 has order eight. Order sixteen occurs first on RP^8.
- argued: the sixteen of op.order-four-anomaly-and-sixteen is the stored 1/16 = (1/2)(1/8) on RP^5, the half
  coming from the group of order two; the eight there is a spinor count in six dimensions. It is not the order of
  the wall's eigenbundle class, and the period-eight clock plays no part in it. Common ground: both are counts of
  Clifford module dimensions over a projective space. The literature's route from the bordism group to real
  K-theory (from memory, not in the store) was not tested and cannot be with stored tools.
- out of reach: a derivation of the modulo-sixteen statement from the wall theory. First step: none proposed; the
  problem's own open question is a premise (whether omega is gauged), not a class.

## Unexpected links
- The obstruction in codimension three is the rotor of the full turn, -1: the same element that the stored
  spin-statistics result uses (synthesis.wedge-reflections-compose-to-the-two-pi-rotor-...). Not tested further.
- The position vector trivialises multiples of the tautological line over projective spaces, so the isolated
  degeneration in codimension n + 1 bounds the order of the class of the projective wall RP^n; the stored
  rung-count results on projective and lens walls use the same odd maps written in Clifford algebras.
- Kerr: H is the fixed-axis component of the unit eigenvector of the plane family in the ring's normal coordinate.
  Bears on op.kerr-ring (interior), not on this problem's success clause.
- For other clusters: nothing found that supplies or needs a premise in G, H, L1 or L2, except that L1's
  starting leads (run 2026-11-16-anomaly) meet lead 5b: the order-eight result above could be added to the
  "known" paragraph of op.order-four-anomaly-and-sixteen.

## Decisions for Leon
1. sheaf.wall-class: restate clauses (a) and (c) as drafted (coarse part = signature jump; (c) = the transfer
   class, proved for the pair on compact walls), or keep the conjecture and add a note.
2. op.eigenbundle-class-of-degenerations: after review, mark items 1, 2 and 4 answered and item 3 answered in the
   negative; what stays open is codimension five and beyond. Import the periodicity theorem (or the homotopy
   groups it rests on) as one Fact, or leave the higher codimensions cited.
3. Kerr: record in op.kerr-ring and in the note of interior.duality-monodromy-fibration-over-ring that the
   winding three is the degree of the field strength in the eigenvector and that only its parity is a class; or
   leave the conjecture's wording.
4. Proposal 3 states its hypotheses directly and proposes no assumes edge on sheaf.tameness; if uniformity with
   the other wall results is wanted, the edge is a maintainer edit.
5. Whether the two-sided rung count (proposal 3, clause (4)) is to be a stored notion beside the one-sided
   k(Sigma); their equality is open.

## Files
Proposals: proposals/synthesis.position-vector-eigenbundle-in-codimension-three-has-a-class-of-order-two,
proposals/synthesis.fixed-form-completion-over-a-ball-exists-iff-the-eigenbundle-is-stably-trivial,
proposals/synthesis.eigenbundle-class-of-a-corank-one-wall-is-the-dying-line (each: entity.md, proof-main.tex,
check.py, coverage.yaml; check4 exit 0, validate_draft ok). Work: work/W/P1, P2, P3 (sources of the proposals),
work/W/kerr_ring.py, work/W/lead5.py, work/W/wall_class_restatement_draft.md.
Process note: check4 on proposal 2 overlapped for a few seconds with another cluster's check4 (my test for a
running gate did not block the command); later runs waited for a free slot. Nothing under store/ was edited.

## Fix round (referee report verify/R-C.md; all three SOUND WITH FIXES; no conclusion reversed)
Details in findings/fixes-W.md. Corrections to what this file said above:
- Lead 1: the lifting lemma had a gap (the rotors were taken to be the closed set of even R with R R~ = 1
  preserving vectors without proof that this is the group of the cited double cover). Closed with the stored
  centre and the kernel step of the stored proof. Clause (6): it is clause (4) with W0 = 0 that excludes every
  repair on the least module; the linear system excludes only repairs of the form x + b E.
- Lead 4: the statement fixed K0 too loosely. It now fixes K0 = 1_c (+) (-1_c') (+) 1_N, and adds, with proof and
  a check, that every fixed form of that signature follows by a constant change of basis.
- Lead 2: the proposal does not identify the N of the stored one-sided clause and does not rederive the stored
  wall results; the class is relative across the collar; naturality and conservation are not shown. The sentences
  above that said otherwise are corrected in place. The restatement draft no longer records clause (c) as proved.
No fix declined.
