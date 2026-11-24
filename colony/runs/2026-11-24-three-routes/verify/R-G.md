# Referee R-G report, run 2026-11-24-three-routes

Blind review per REFEREE.md. I read only the two proposals, their premises in the store (all pinned at the current
store version, all `proved`), the conventions and the open problem, and the check4 logs (both: 0 errors, 0 other
findings, pass; no W413). Scratch code is in `verify/work-R-G/`. None of it imports the proposals' checks:
p1_lat.py, p1_A.py, p1_C.py, p1_E.py, p1_F.py, p1_sym.py (proposal 1) and p2_fock.py, p2_null.py (proposal 2).

| id | verdict | one-line reason |
|---|---|---|
| synthesis.spin-two-lattice-model-static-slaved-field-fails-and-dressed-pair-detection-commutes | SOUND WITH FIXES | Every clause I recomputed is right (58, 132, 57/22, 3858/4317, 202171, 8736, 9310, 1304, 115792; clause (1) symbols). The fixes: the title overstates ("spin two", "one mass has no dressing"); the lay level speaks of gravity, not the model; the G1 kill condition was met for one mass and the text should say so plainly; counts are relative to the lattice cone, which is twice the wave speed; a missing lemma (compact curvature rules out a dipole) should be added. |
| synthesis.helicity-two-composites-of-light-ray-fermions-on-a-generator-and-off-the-null-plane | SOUND WITH FIXES | Clauses (i) to (v) are right and independently reproduced. The fixes: (v) does not state that J commutes with the medium; (iii) uses an unnormalised vector; the Reading's conclusions rest on the lowest specific modes, an unconstrained model and an unproved "two ways" classification, so the one-liner's "a composite ... is not the free part" must be narrowed. |

---

## Proposal 1: synthesis.spin-two-lattice-model-static-slaved-field-fails-and-dressed-pair-detection-commutes

**Verdict: SOUND WITH FIXES.**

### What I checked, and how

Premises. The cited results say what the proof needs, at the pinned versions: the first-order theorem's formula for
the Einstein map (Ric(a) = -1/2[(a.k)(u - tau k) - Q h(a) + (a.u)k], tr Ric = -(k.u - Q tau)), its clauses (iv), (v),
(vi), (viii); the slaved-field theorem's [P_1, O] = pq e_2; set and clear; the device theorem's hypothesis (D) and its
clause (2); the Newtonian coupling's commuting arrangement numbers. All are at the current version and `proved`.

My own implementation of every stencil (p1_lat.py: forward and backward differences by numpy roll on integer arrays;
ranks mod two 31-bit primes; dyadic floats, which are exact here, for the dynamics):
- Clause (2) identities hold on random integer fields on 125 sites: G[delta_xi] = 0, D delta_xi = 0,
  <pi, delta_xi> = -2 sum xi.C[pi], C_i[G h] = 0, G symmetric for the weighted pairing, tr G = -Dh/2, and
  D p = sum b_i C_i[pi].
- Ranks. On L = 3: 162 components, displacement rank 78, D rank 26, free 58, as stated. On L = 4 (not in the
  proposal): 384, 189, 63, free 132 = 2*63 + 6, so there are two free pairs per nonzero momentum there too, including
  the momenta at pi. In two space dimensions, L = 4 gives 48, 30, 15, free 3, and L = 5 gives 75, 48, 24, free 3.
- Clause (1), by my own route in GA.py. I took the stored formula for G_k at k = w e_0 + kappa with h(e_0) = 0 and
  compared it with the leading symbols on random rational samples, writing every map by its matrix in
  h(a) = sum M_mn (a.e_m)e_n. The time-time component is -D_kappa/2, the time-space component is w C_kappa[Pi], and
  the space-space component is w^2 Pi - G_kappa. All three agree.
- Clause (3) and (4). D f = rho_w - rho_n. The monopoles are 2 and 2, the dipoles 0 and 0, the second moments 8
  and 2. G[f] is nonzero on 57 components at 22 sites, and f on 9 components.
- Clause (5). I solved for the exact potential difference mod p (dense elimination, two primes) and cross-checked
  with an FFT. kappa is nonzero on 3858 of the 4317 components off the support of G[f], as stated.
- Clause (8). I wrote my own evolution, its inverse, and my own depth and cone bookkeeping (BFS on the one-step
  influence graph, starting from the components of f). The counts: 206346 events, 202171 outside the detection's
  cone, G[S] zero at all of them, G[R] nonzero at 8736 of them, the first at step 2, 1304 not later than the
  detection, 9310 outside the detection's cone and inside the source's, and 115792 outside and not later. All
  match. If the BFS starts from all components at the string sites instead, the counts change (200960, 8045, ...),
  so the proposal's "data on the string" means the components of f. Fix (6) asks for that to be said.
- Two perturbations of the proposal's check, each with the full check rerun:
  (a) f_33 = -1/2 changed to -1/4: six of the eight functions fail.
  (b) the stencil -s_i s_j h_kk in G_ij changed to -s_i b_j h_kk: the clause (2), (5)/(6)/(7), (8) and (9)
  functions fail. **But check_lattice_operators_are_the_stored_first_order_map... still passes.** The leading-symbol
  comparison of clause (1) cannot tell s from b (both have symbol kappa). The exact lattice identities of (2) are
  what pin the stencils. The coverage file already says "to leading order only", so this is not a defect, but
  clause (1) should not be read as fixing the stencils.

### What the model has of spin two, and what it lacks (point 1)

It has:
- the gauge freedom: three lattice displacements per site, under which G and D are exactly invariant;
- the four constraints: the Hamiltonian constraint D h = g rho, a lattice double divergence, and three momentum
  constraints C_i[pi] = 0, all commuting and preserved by the step;
- two free pairs at each nonzero lattice momentum (the transverse trace-free ones), exactly, on 27 and on 64 sites;
- the stored first-order Einstein map as its leading symbol, to leading order in the spacing;
- no free part in two space dimensions, as clause (vi) of the stored theorem requires.

It lacks:
- rotation symmetry. Only the cube's symmetry is present, so "helicity two" has no lattice meaning; it exists only
  in the continuum symbol, through stored clause (vi).
- Lorentz covariance. The frame gauge h(e_0) = 0 and the explicit time step break it.
- the self-coupling. The constraints are abelian, and the field does not source itself.
- matter momentum and stress. The C_i have no matter term and T_ij = 0, so the motion that makes the two
  arrangements is not modelled.
- the rotation-gauge field Omega of Gauge Theory Gravity, and spinors.
- the unit-speed cone (see point c).
- asymptotic charges. On the torus the total mass is cancelled by the uniform rho-bar, so moments are defined only
  on a box.

Wording. The formal clauses, "What the model is and is not", the technical level and the one-liner are worded as
statements about the model. Three places are not:
- The **title** says "Lattice spin two" and "one mass has no dressing".
- The **lay** level says "A gravitational field with no freedom of its own is not pinned down...", "The natural
  choice, the ordinary Newtonian field, fails..." and "In gravity the attached field can be kept to a small region
  only when...". Each is a statement about gravity, not about the model.
- The first **Reading** says the dipole conclusion "is new and belongs to spin two". It is new relative to the
  stored Maxwell model. It is standard in the literature, as the proposal's own prior art (Donnelly and Giddings;
  Pretko) shows.

### (a) One mass on two sites

The mathematics of clause (3) is right: for f' supported in a box with margin, D f' has no monopole and no dipole.
The Reading goes further than (3): "its detection dressed by any field fails to commute with the curvature at a
distance". (3) covers compact f' only, and the Reading says the curvature version is "not shown on the lattice".
It can be shown on the lattice, in a few lines:

- Let G[f'] vanish outside a box with margin. Then C_i[G[f']] = 0 gives <G[f'], delta_xi> = 0 for every xi defined
  on the box.
- For the quadratic xi_i = 2 x_l x_i - delta_il |x|^2, delta_xi = 4 x_l delta plus a constant field. I computed
  this exactly (p1_E.py).
- Constant fields are displacements of linear xi.
- Hence sum tr G[f'] = 0 and sum x_l tr G[f'] = 0, and D f' = -2 tr G[f'] has no monopole and no dipole.

So no dressing of any support whose curvature is confined to a box exists for a rearrangement with a dipole. This
should be stated and proved. It is what supports the "any field" sentence.

Which reading does the mathematics support? The obstruction lives in the Hamiltonian constraint alone. It applies
equally to the slaved variant and the canonical one, and it is the conservation of the mass dipole (the boost
charge that a dressing cannot screen). So it is not evidence against the field's own variables; to that extent the
authors' reading holds. But it is a failure of the dressed-detection test for that class of detections. By the
registered kill condition G1 ("with the field's own variables no dressed detection commutes with the field at every
event outside the cone"), **G1 is met for one mass moved alone and not met for the pair**. The extraction note
admits that the single-mass case was "registered beforehand as the way the condition could be met", but then
reports it only "as a restriction on the matter". That is a reinterpretation after the fact and must be said in
those words. Two further corrections:
- "restriction on the matter" should be "restriction on which detections are local": the mass dipole is a charge
  of the constraint, not a property of the matter model.
- The case that motivates the problem (pred.gravity-entangles-standard-phase, a single mass in a superposition of
  two places) is the dipole case. The model's dressing reaches commutation there only by including the recoil
  partner, whose dressing reaches that partner. This is argued, not modelled: the model has no matter momentum.

The title's "dressed pair commutes" is accurate for the pair in the canonical variant, outside the lattice cone.
"One mass has no dressing" is false as written: it has non-compact dressings, for example the Newtonian phi delta.

### (b) Is "commutes outside the cone once a compact dressing exists" specific to spin two?

No. It is ordinary finite propagation of any local canonical lattice model: [G(n), O_f] = g pq G[S(n)] X_f, and S
vanishes beyond the stencil's reach. The text says so in the extraction note and at the end of the first Reading.
The technical and lay levels and the one-liner do not, and they present it as a finding. Add the qualifier there.

### (c) The lattice cone against the unit-speed cone

The scheme moves one site per step along each axis, so the lattice cone reaches distance n at step n (I confirmed
this: the support of G[R(n)] reaches distance n from the source's curvature support). A wave of unit speed moves half
a site per step. The lattice cone contains the unit-speed cone, so "outside the cone of the detection" in the lattice
sense is conservative, and the commutation result is unaffected.

The phrase "inside the cone of the source event" is a different matter: it is lattice-cone dependent. Of the 8736
failures, 5246 lie farther from the source's curvature support than n/2, that is, outside the unit-speed cone of the
source (my count, p1_F.py). Those events would be spacelike to both source and detection in the continuum. The
stored Maxwell model's "none spacelike to the source" used an exact cone; this one does not.
"What the model is and is not" says the cone is the lattice's. The one-liner and technical levels should say
"the lattice's cone" wherever a count is given.

### (d) Hypothesis (TT)

(TT) is named, said not to be stored and not derived, and used only in the "Reading under (TT)". No proved clause
needs it. It appears in the one-liner; it is not in the title, which is acceptable because the title's clauses do
not need it. Nothing is worded as the series adopting it: "What (TT) costs" is conditional throughout, and the
extraction note leaves adoption to the maintainer. No fix needed here, apart from the lay sentence noted above.

### Other findings

- Proof (1): "on $e^{I\kappa\cdot x}$-type functions" uses an undefined unit I. Write "on plane waves", or name the
  unit.
- Clause (10): "its curvature is $g\rho_s$" is undefined in two space dimensions, where the space-space Einstein map
  vanishes identically and the check defines no G for d = 2. Say "its spatial scalar curvature D h is g rho_s".
- Literature, from memory. Weinberg 1964 (Phys. Rev. 135 B1049) is the universality of soft helicity-two couplings.
  The use stated, "would become available to the problem of deriving the field equation", is closer to Weinberg 1965
  (Phys. Rev. 138 B988) or Deser 1970. Check before storing. The other citations (ADM 1962; Donnelly and Giddings
  2016, 2018; Belenchia et al. 2018; Xu 2006; Gu and Wen 2012; Pretko 2017; Galley, Giacomini and Selby 2022) look
  correctly attributed for the uses made.
- House style: no em dashes, no banned words, no bare imaginary unit; agent and run names appear only in the
  credit metadata.

### Fixes (exact)

1. Title: "Lattice first-order gravity: slaved field fails; with canonical variables the dressed pair commutes; one
   mass has no localised dressing".
2. Lay level:
   - "A gravitational field with no freedom of its own" becomes "In the model, a field with no freedom of its own";
     do the same for the Newtonian sentence.
   - "In gravity the attached field can be kept..." becomes "In the model (and, by an argument, in weak gravity
     generally) the attached field can be kept...".
   - "passed everywhere" becomes "passed everywhere outside the measurement's reach on the grid".
3. Technical level and one-liner: write "the lattice's cone (one site a step, twice the wave speed)". After the
   dressed-pair statement add "as in any local canonical lattice model once a dressing of compact support exists".
4. Add a proved clause (3'), with the proof above: if G[f'] vanishes outside a box with margin, D f' has no monopole
   and no dipole. So for one mass on two sites no dressing has curvature confined to a box. Use (3') for the
   Reading's "dressed by any field" sentence, and drop "is not shown on the lattice".
5. Extraction note and Reading: state "By the registered condition G1 is met for one mass moved alone, and not met
   for the pair; reading the former as a restriction on which detections are local is argued after the
   computation." Replace "restriction on the matter" accordingly. Add that the motivating experiment is of the
   single-mass type.
6. First Reading: "One conclusion is new and belongs to spin two" becomes "One conclusion is new relative to the
   stored Maxwell model (it is standard; see the prior art)". Define "data on the string" in (8) as the components
   on which f is nonzero.
7. Proof (1): name the unit or drop it. Clause (10): "spatial scalar curvature D h".
8. Check the Weinberg 1964 citation against Weinberg 1965 and Deser 1970.

---

## Proposal 2: synthesis.helicity-two-composites-of-light-ray-fermions-on-a-generator-and-off-the-null-plane

**Verdict: SOUND WITH FIXES.**

### What I checked, and how

Premises. These are at their current versions and say what is used: the helicity-one result's (iii) rule
[W, M] = hM and its (iv) quasi-spin; light-ray (iv) weights of plus or minus one half; CAR on tower planes;
fluctuation forms (vi). The first-order theorem is a mention in the Reading only, as the note says.

- (i) holds: the weights are plus or minus one half, so w_alpha - w_beta lies in {-1, 0, 1}, and helicities add
  under the rotation automorphism.
- (ii), by my own Fock code (p2_fock.py: occupation patterns, Jordan-Wigner signs, no reuse of the proposal's
  code). Two flavours give 1, 4, 10 at q = 2, 3, 4, which is C(q+1, 3). One species gives 1, 8, 36, 120 at
  q = 4..7, which is C(q+3, 7). X_q Omega = 0 and V_q Omega = 0. I checked the generating-function steps by hand
  (sum d^2 t^d = t(1+t)/(1-t)^3; dividing by 1 - t^2 gives t/(1-t)^4; squaring gives t^2/(1-t)^8), and the identity
  sum a(q-a) = (q^3 - q)/6.
- (iii) reproduced: 1, 0, 3 at q = 2 and 4, 2, 10 at q = 3, **as normalised expectations**. psi_1 has squared norm
  2, so the raw values at q = 3 are 4, 4, 10. The commutator of rho_q(id) gives 4q on all three vectors.
  (X_q*)^2 Omega = 0 at q = 2, 3 and is nonzero at q = 4.
- (iv) holds in GA.py over the rationals on 200 random samples, parallel pairs included (p2_null.py). I also redid
  the algebra by hand.
- (v). The identity [phi_n(t), O_H] = W_<^{-1}[phi^0, W_>=^{-1} O W_>=]W_< is immediate from O_H = W^{-1}OW with
  W = W_>= W_<. The vanishing condition holds, and so does the first-order form (sign checked: K^{-1}OK = O +
  gJ[J_s, O]phi). The six failing events follow by hand from the ring's adjacency. The response -sin a reproduces by
  hand.
- Perturbations of the check:
  (a) the coefficient (k2-k1)(l2-l1) replaced by (k2-k1): check_sea_values fails.
  (b) the source times {0, 1} changed to {0, 2}: check_causal_medium fails on the event set. Its internal rule
  assertion still passes, as it should.

### Findings

1. Hidden hypothesis in (v). For K_t' to be a unit with inverse K_t'^* and for "phi^0_n(t) commutes with W_>=" to
   follow, J must commute with every phi^0 and with the matter factor, and J^* = -J. The check asserts this for its
   model (J = g_0 g_1 commutes with every h_x and with e_1, e_2), but the general statement says only "any algebra
   that commute with the matter factor". Add "and with J".
2. (iii) wording. Say "normalised expectations" (or use psi_1/sqrt 2). "The total density mode rho_q(id) ... has 4q"
   should be "the commutator [rho_q(id), rho_q(id)^*] has expectation 4q".
3. Scope of the Reading's (a). The proof covers two specific families, X_q (two flavours) and V_q (one species). The
   non-number commutator is shown for X_q at q = 2, 3 only, and not for V_q. No statement covers general linear
   combinations of helicity-two four-fermion modes, other flavour structures, or six or more fermions. "On one
   generator a composite ... is such a field only at helicity zero" is therefore argued from examples, not proved.
   Worse, "a commutator that is not a number" holds for any composite of free fields (phi^2 of a free boson
   included), so by itself it says little. The Reading is labelled argued, but the one-liner's "argued from these,
   a composite of light-ray fermions is not the free part" generalises beyond what was computed. Weinberg and Witten
   1980, cited only as prior art, is the general tool here, and the text should say whether its hypotheses (a
   Lorentz-covariant conserved stress) hold.
4. Reading (b) is kinematics: two massless constituents have Q(P) >= 0, with zero only for collinear momenta. This is
   standard. The collinear sector that remains is exactly the on-generator sector, so (b) depends on (a) and
   inherits its scope.
5. Reading (c) and its "two ways and not three".
   - (v) is proved in a model with no constraint linking the field to the source. Where the field must satisfy the
     gravitational constraints, proposal 1 (clauses (5), (6)) shows that the constrained part is an equal-time
     matter element. It fails at a distance on its own and must be cancelled by something that shifts the field.
     The Reading does not address this. Whether a non-canonical medium can supply that shift is not shown (lattice
     gauge theories with compact or finite groups suggest it can).
   - The "two ways" classification is, by the proof's own admission, "not a classification proved here".
   - "A composite of light-ray fermions as the free part is neither" conflicts in tone with (v). A causal composite
     medium would meet the commutation requirement by (v), and so falls under the second way, the response of the
     stored quantum fields. Restate: "a composite of light-ray fermions does not supply the state-independent linear
     response of a canonical free part; as a causal medium it would meet commutation (by (v)) and belongs to the
     second way."
6. (v) "where a response linear in the source would give -a" silently normalises the commutator function to 1. Say
   so, or drop it.
7. Literature, from memory.
   - de Broglie's neutrino theory of light is usually dated 1932 to 1934. Jordan 1935 and Pryce 1938 are correctly
     attributed (Pryce: the neutrino photon fails Bose statistics and transversality).
   - Weinberg and Witten 1980 is correct for the stated use.
   - Level-one current algebra: in su(2)_1, :J^+J^+: = 0, and the first charge-two field has weight 4. Both are
     consistent with the computed C(q+3, 7), which vanishes below q = 4.
   - Sakharov's induced gravity: 1967.
   Nothing looks misquoted.
8. House style: clean. Q(v) is used, |p_perp|^2 = -Q(p_perp) is defined, and the unit is J throughout.

### Fixes (exact)

1. (v): "self-adjoint elements of any algebra that commute with the matter factor and with J".
2. (iii): "normalised expectation"; "the commutator of rho_q(id) with its adjoint has expectation 4q".
3. One-liner: replace "argued from these, a composite of light-ray fermions is not the free part of the stored
   lattice result" with "argued from these, the lowest helicity-two four-fermion modes on a generator are not a free
   part in the sense of the stored lattice result's clause (4)". Make the matching change in the technical level's
   last paragraph and in the maintainer decision in the note.
4. Reading (c): restate as in finding 5. Add that (v) is shown without constraints and that the constrained case is
   proposal 1's territory.
5. Reading (a): call the helicity-two statement "for the families X_q and V_q". Add that a non-number commutator is
   generic for composites.

---

## Overlaps and conflicts

- **No duplication.** Proposal 1 is a constrained first-order lattice model. Proposal 2 is about composites on a
  generator, two-particle kinematics, and an unconstrained medium identity. They share only the stored premises
  (the slaved-field theorem and set and clear).
- **No mathematical contradiction.** Proposal 1 shows that a canonical pair *suffices* in its model, and itself says
  that commutation once a compact dressing exists holds in any local canonical lattice model, not because of spin
  two. Proposal 2's (v) shows that a canonical pair is not *necessary* for commutation in an unconstrained model.
  The two are consistent and complementary. Both also agree on what the canonical pair buys: proposal 1's Reading
  under (TT) fixes N_k by requiring the free part's commutator to cancel the retarded response, which is proposal
  2's "state-independent linear response".
- **Tension 1: the constraint.** Proposal 2's Reading (c) ("any medium with causal commutators, coupled at a point,
  gives it exactly"; "two ways and not three") is drawn from a model without a constraint. Proposal 1 shows that
  with the gravitational constraint the bare detection is not an observable, and that the constrained part fails at
  equal time and must be cancelled by a dressing conjugate to the field. Proposal 2's Reading should be restricted
  to unconstrained coupling, or should cite proposal 1 for the constrained case. Neither proposal shows whether a
  non-canonical medium can carry the dressing.
- **Tension 2: the single mass.** Proposal 1's no-dressing result for one mass (a constraint charge, the mass dipole)
  is independent of what the free part is made of. So it applies to proposal 2's alternatives too: no medium,
  canonical or composite, gives a localised observable for an isolated single-mass dipole rearrangement. Neither
  text says this, and both should if the open problem is restated from them.
- **Recommendation.** Both stand as separate entries after their fixes. If both are stored, proposal 2's Reading (c)
  should cite proposal 1 for the constrained case. Proposal 1's note should cite proposal 2's (v) as the reason the
  commutation result is not specific to canonical variables either.
