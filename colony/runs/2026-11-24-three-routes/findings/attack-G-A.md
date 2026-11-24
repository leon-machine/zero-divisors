# Findings, attacker G-A (constructive), run 2026-11-24-three-routes

Target: op.gravitational-field-at-null-momentum, route "palatial pair" (RUN.md, target G, items 1 and 2).
Status of this file: attack round complete. One proposal filed. Scratch: work/G-A/ (spin2.py and t*.py are the
exploration; P1/check.py and stage/<id>/ are the filed files).

## Routes
Named route (executed): give the two transverse trace-free directions at null momentum a canonical pair on
polynomials, as the stored photon has, and test it against the requirement in an exact lattice model with the
constraint structure of the first-order gravitational field.
Two alternatives (not executed here):
- 1b of ROUTES.md: the pair as a bilinear of the light-ray fermions, the commutator a Schwinger term. The sibling
  took it (proposal synthesis.helicity-two-composites-of-light-ray-fermions-on-a-generator-and-off-the-null-plane):
  argued there that such a composite is not the free part.
- A restriction instead of a pair: keep the field slaved and restrict what counts as a local operation (a
  superselection rule on the source's commuting numbers, or the recording premises making the source a number
  before a signal builds, 1c). Needs a rate or a rule the store does not hold; fails if it removes the registered
  entangling phase.
Choice: the named route, the only one of the three with an exact model inside the budget.

## Kill conditions (RUN.md, registered before computing) and their outcome
- G1 (with canonical transverse trace-free variables no dressed detection commutes with the field at every
  spacelike event): NOT MET in the model as built. Registered by me before computing, as the way G1 could fire:
  (G1a) for one mass on two sites no dressing of compact support exists: HOLDS (proved; the Hamiltonian constraint
  is a double divergence, so its source has no monopole and no dipole for a field supported in a box). I report
  it as a restriction on the matter (a mass does not move without recoil), not as G1 firing; the referee should
  judge that reading, which is argued. (G1b) for two arrangements with one mass and one centre a dressing of
  compact support exists and the dressed detection commutes at every event outside its cone: HOLDS (proved for
  the commutation, computed counts: all 202171 events).
- G2 (the first-order signal does not vanish with the free part): NOT MET. With the field's own variables the
  device multiplies the dressing by a phase whose angle is zero at every event outside the cone, so the device
  has no effect there at any order (proved); for the slaved field the signal is of first order at 1304 events.
Candour on G1b: that a dressed detection commutes outside its cone once a dressing of compact support exists is
true of every local canonical lattice model. It is not a discovery about spin two. What is specific to spin two is
(i) which rearrangements have such a dressing, (ii) that the dressing shifts h (the variable whose curvature the
constraint ties to the mass), so the momentum constraints ask nothing of it for matter at rest, (iii) that the
static slaved field is the Newtonian one and that in the gauge h(e_0) = 0 it is static only up to a displacement.

## The model (what it is and is not)
The stored first-order Einstein map, in the gauge h(e_0) = 0 of a frame, on a periodic cubic lattice: h_ii on
sites, h_ij on plaquettes, forward and backward differences placed so that every identity of the continuum holds
exactly (invariance under displacements, the contracted identity, symmetry of the Einstein operator, tr G = -D/2,
preservation of the constraints by a leapfrog step of 1/2). Four constraints: C_0 = D h - g rho per site (D a
double divergence), C_i[pi] = 0 per link. Matter: two equal masses on an axis about a centre, wide (distance 2)
or narrow (distance 1), in Cl(1,1) as in the stored models. Exact over the rationals (no quadratic extension was
needed: the lattice Poisson problem is solved from the first linear relation among the iterates of the Laplacian
on the source, and verified by applying the Laplacian).
It is NOT: gravity beyond first order (the field does not source itself; the four constraints commute, where the
full theory's do not); a model with moving matter (no momentum or stress of matter, so C_i has no matter term and
no detection that changes it is treated); Lorentz invariant (cubic symmetry; the lattice's own cone, one site a
step, wider than the cone of unit speed); a model with the rotation-gauge field or spinors; a model in which the
tower appears.
Spin two in two space dimensions has no transverse trace-free part (the stored clause (vi) in Cl(1,2); on the
lattice the fields with D h = 0 modulo displacements are the constants), so the model is three-dimensional.

## Established (proposal synthesis.spin-two-lattice-model-static-slaved-field-fails-and-dressed-pair-detection-commutes)
check4: 0 errors, 0 other findings, check result pass (eight functions). validate_draft: ok (warning E610, no ORCID
for the credit entry, as on the sibling's proposal; info I305).
- proved: (1) in the gauge h(e_0) = 0 the stored map at k = w e_0 + kappa has time-time component
  (1/2)(kappa.h(kappa) - Q(kappa) tr h), time-space part -w Pi[h](kappa), space part w^2 Pi[h] - G_kappa[h]; the
  lattice stencils have these as leading symbols. So the lattice constraints are the stored "four equations without
  second time derivative" and the lattice dynamics the other six.
- proved (count computed): (2) the structure identities; the constraints commute; a step is canonical; on fields
  with V = 0, D h = 0 the dynamics is the lattice wave equation; on 27 sites 58 = 2 x 26 + 6 free directions.
- proved: (3) no monopole and no dipole for D of a field supported in a box; one mass on two sites has no dressing
  of compact support; the pair has one, f = (1/2, -1/2, -1/2) on the diagonal at the three sites between the
  masses (D f = wide - narrow, second moment 6).
- proved (counts computed): (4) bare recombiner not an observable (fails at the 4 mass sites); dressed recombiner
  and detection commute with all constraints; [h, O_f] = g p q f X_f, [G[h], O_f] = g p q G[f] X_f; on 729 sites
  the dressed detection commutes with h on 4365 components and with the curvature on 4317 of 4374.
- proved (count computed): (5) the static slaved field with no transverse trace-free part (the Newtonian one)
  fails on 3858 of those 4317 components with every matter element that does not commute with the mass density.
- proved: (6) the constrained part of the curvature, G^L = (1/4w) u.(D h), and the transverse trace-free part fail
  separately against the dressed detection and cancel.
- proved (count computed): (7) the constraint alone does not fix a slaved field: g f P_1 is one, commutes off
  the string at one time, is not static (curvature changed on 499 components after two steps).
- computed: (8) 4913 sites, steps 0..6, detection at step 3: with the field's own variables zero commutator at
  all 202171 events outside the cone (of 206346); retarded slaved field fails at 8736 of them, which are 8736 of
  the 9310 events outside the detection's cone and inside the source's, 1304 not later than the detection, none
  before step 2. The count 8736 is the same on lattices of period 15, 17 and 19 (scratch, not in the check).
  Remark: a slaved field fitted to the detection at step 3 commutes with it and fails for a detection at step 5
  at 1252 of 198771 events.
- proved (counts computed): (9) the device, under the stored hypothesis (D): slaved, change of probability
  p q [a (cos - 1) + b sin], first order at 1304 of 115792 early events; with the field's own variables no
  effect outside the cone at any order.
- proved (count computed): (10) two space dimensions: no free part, curvature of a slaved field is its source.
- argued: the Reading (the one-mass obstruction read as recoil; f as the first-order field of the two masses
  pushed apart along the string, with pi_11 = 1/2 on the string and momentum constraint on exactly the two links
  crossed, the last two facts computed); that a dressing with curvature (not support) of compact support is also
  excluded for a dipole (continuum argument from the compactly supported cohomology of the elasticity complex,
  from memory; not shown on the lattice).
- argued, conditional on (TT): the palatial construction and its costs (next section).
Ledger: transport-absent. Standard canonical first-order gravity and standard facts about dressing; the series
contributes the question, the stored first-order map that clause (1) matches, and the matter algebra.

## Second deliverable: the palatial pair for the two directions, in the store's terms (argued; conditional on (TT))
(TT): "the two transverse trace-free directions at null momentum carry a canonical pair as the photon's modes do".
Named hypothesis, in the proposal's formal text, one-liner and Reading; not a premise.
Construction (compare field-theory.fock-space-maxwell-modes): one variable z_k per null momentum, polynomials with
coefficients in span{1, I_4}, a_k = d/dz_k, a_k^* = z_k, form <z^n, z^n'> = n! delta. The mode is the line of the
curvature R_k[n_+] over span{1, I_4} (stored clause (vi): I_4 exchanges the curvatures of n_+ and n_x; a rotation
of the transverse frame by an angle multiplies by twice the angle, helicity two). Free part of the curvature in the
form of the stored photon's field operator with R_k[n_+] in place of the null bivector; the whole first-order field
is free part plus the part fixed by the source through the four constraints and the retarded rule. Normalisation:
fixed by asking the commutator of the free part to cancel the retarded response outside the cone (what clauses (6)
and (8) show in the model); its residue is the stored positive form of two squares. NOT computed here: N_k, and the
helicity assignment of the two terms (taken over from the photon).
Compatibility with stored results:
- field-theory.no-canonical-commutation-relations-tower: no conflict, on the same footing as the photon: the pair
  is not an element of a floor. One difference worth a sentence: the dressing is the exponential of the pair,
  which is not a polynomial; it lives in the completion (as the Weyl operators of the stored lattice Maxwell model
  already do).
- Krein premise (KF): not needed in the frame's gauge with the constraints imposed (the model). A covariant gauge
  would need (K1) extended from polarisation vectors to symmetric maps; not stored, not attempted.
- Stored clause (iv) of the first-order theorem gives the healthy sign for the two directions.
Burst ratio: under (TT), and provided the state of the pair near a hole is the one regular on the future horizon
as for the other fields (not derived here), g_h = g_s = g and D = (2 + g + o)/(1 + g), the stored form; without
(TT), D = (2 + o)/(1 + g) against the standard expectation. Difference g/(1 + g): 99/50 against 49/25 at g = 2/98,
o = 0 (numbers from the stored clause (viii); nothing new computed). The kill condition of the burst prediction
does not distinguish them.
Stored texts that would be restated if (TT) were adopted (found by text search for the sentence and by the
problem record; a list, not a full reading):
1. conventions, "Gravity and the graviton": "The series holds no quantum of that field: the graviton does not
   exist here"; "no stored result is to be read as resting on a quantised gravitational field"; the last sentences
   of the Scope and Requirement paragraphs.
2. note.synthesis.where-stored-text-names-a-graviton: its lead and groups (d) processes, (e) ontology readings,
   (f) linear modes given a vacuum.
3. pred.dimmed-evaporation-bursts: the sentence "the series holds no quantum of that field ... whether g is kept
   is part of open problem ..." (g would be kept).
4. pred.no-indirect-dark-signals: "the series holds no quantum of the gravitational field".
5. dark-matter.imported-massless-graviton-production-rate: its flag paragraph.
6. open_problems.yaml: op.gravitational-field-at-null-momentum (statement and success), op.graviton-rate-as-
   classical-field-process (the two places that say "no quantum"), op.einstein-from-the-field-theory (route 3a,
   Weinberg's argument, would become available).
7. synthesis.first-order-gravitational-field-has-two-free-directions-at-null-momentum-and-four-constraints:
   the Reading's "whether the series gives these solutions any existence of their own is open".
8. synthesis.two-dimensional-lattice-maxwell-...: the Reading's closing "a suggestion by analogy and settles
   nothing" (this model replaces the analogy at first order whether or not (TT) is adopted).
Not needing restatement: pred.no-dark-radiation and synthesis.gravitational-pair-production-from-the-operator-
source-at-first-order ("with no quantum" there is a statement at non-null momentum and stays true);
pred.gravity-entangles-standard-phase (the phase does not depend on (TT)).
What (TT) does not give: a derivation of the pair (the sibling argues the light-ray composite is not it); anything
beyond first order (the standard theory of this pair is an effective one only; from memory); the state.

## Unexpected links
- The Hamiltonian constraint is minus twice the trace of the curvature, D h = -2 tr G[h], and a double divergence.
  Its conserved dipole is the conserved centre of mass. Lattice models with exactly this constraint are known
  outside gravity as models with conserved dipole (Xu 2006; Gu and Wen 2012; Pretko 2017; from memory).
- The dressing f is the time-integrated momentum of a conserved motion: pi_11 = 1/2 on the string, momentum
  constraint nonzero on exactly the two links the masses cross. A dressing of compact support therefore needs a
  conserved stress on the line between the masses, not only their mass density: a place where the whole-stress
  clause of op.einstein-from-the-field-theory meets this problem (the matter of the model has no stress, so this is
  seen only through the dressing).
- The stored two-path models have one quantum on two paths. For gravity that quantum alone has no local dressed
  detection; the registered phase (static coupling) is not affected, but any stored Reading that carries the
  two-path model to gravity should say that the superposed mass has a recoil partner (Belenchia et al. 2018 make
  the same point: the quadrupole is the leading moment; from memory).
- Two space dimensions: the slaved field's curvature is its source, site by site. The stored clause (vi) in
  Cl(1,2) and the one-dimensional clause of the lattice Maxwell model are the same phenomenon.
- The sibling's proposal argues that commutation alone does not force a canonical pair (any medium with causal
  commutators commutes). This model shows a canonical pair is sufficient at first order; it does not show it is
  necessary. The two do not conflict.
- In the gauge h(e_0) = 0 the static Newtonian field is not constant: h(n) = h_0 - n(n+1) tau^2 times a
  displacement. A reader comparing with the stored static coupling should use the curvature, not h.
- Tool: the exact solution of a lattice Poisson problem over the rationals from the Krylov relation, with no
  roots of unity; it would serve any later periodic lattice model.

## Decisions for Leon
1. (TT): adopt, reject or leave open. What this run adds: at first order, in an exact model of the stored field
   equation, (TT) is sufficient for the requirement (the dressed detection commutes and a device sees nothing
   outside the cone), and without the field's own variables the Newtonian and the retarded slaved fields fail.
   It is not shown necessary. My recommendation, for what it is worth: if (TT) is adopted, adopt it as a named
   hypothesis scoped to first order with the photon's status (a pair on polynomials, not derived from the tower),
   not as a foundation premise; if the sibling's lines leave no alternative standing, the problem's "success"
   clause would then be met by adoption with these grounds.
2. If adopted: store (TT) as a postulate with assumes edges (maintainer-only), and restate the eight items listed
   above; decide the burst wording (g kept, with the proviso on the state near the hole).
3. Whether adopted or not: the conventions' sentence that the step from the lattice Maxwell model to gravity "is
   by analogy" can now cite this model for first order.
4. The one-mass obstruction: accept the reading as recoil (a restriction on what a local detection is) or treat
   it as G1 firing for the stored two-path matter. I read it as the former; it is argued, not proved.
5. Prior art is cited from memory in the proposal's extraction note (Arnowitt, Deser and Misner 1962; Donnelly
   and Giddings 2016, 2018; Belenchia et al. 2018; Xu 2006; Gu and Wen 2012; Pretko 2017; Galley, Giacomini and
   Selby 2022; Weinberg 1964). None was read in this run. Import as Facts, or read and correct, in the maintainer
   pass.

## Left unfinished, and why
- Dressings by sums of Weyl operators: not treated (as in the stored Maxwell result).
- The exclusion of a dressing with curvature of compact support for a dipole: argued in the continuum only.
- Moving matter, the momentum constraints with a matter term, a detection that changes momentum: outside the model.
- Beyond first order: nothing. The constraints of the model commute; the non-abelian case is a different problem.
- The (TT) construction's normalisation N_k and helicity assignment: stated by analogy with the photon, not
  computed (budget went to the exact model).
- No continuum limit and no statement between the lattice's cone and the cone of unit speed.
- The potentials of the two arrangements separately (with the uniform background number) were not built; only
  their difference enters any commutator and only it was computed.
- Necessity of a pair (kill condition G3) was the sibling's side.
