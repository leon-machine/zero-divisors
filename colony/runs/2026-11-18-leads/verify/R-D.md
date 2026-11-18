# Referee report, group D (the gravitational field), run 2026-11-18-leads

Blind referee. I read only: the three proposal folders, the store (via labcli and store/conventions.md), and the
check4 logs. I did not read findings/, work/, RUN.md, ATTACK.md or LEADS-source.md. Scratch: /tmp/referee-D/
(d1.py, d1b.py, d1c.py: my own component computations for D1; d2.py, d2dyn.py, d2dyn_h1.py: my own lattice
for D2; d3.py: my own lattice and Cl(1,2) computation for D3; p1, p2, q1, q2, r1, r2, r3: mutants).

check4 logs: D1 0 errors, pass; D2 0 errors, pass; D3 0 errors, 3 I405 notes (survey-only premises declared
and untouched, as intended), pass. `runcheck.py` passes all functions of all three on the unmodified checks.

| item | verdict |
|---|---|
| D1 first-order field: two free directions, four constraints | SOUND WITH FIXES |
| D2 constraint and dressing / transverse part (lattice Maxwell) | OVERSTATED (clauses right; id, one-liner and clause (4) carry a hidden hypothesis) |
| D3 slaved-field failure as a first-order signal; store survey | SOUND WITH FIXES (proved core is small; headline negative is a survey; must state plainly that the model signals faster than light) |

---------------------------------------------------------------------------------------------------------------

## D1. synthesis.first-order-gravitational-field-has-two-free-directions-at-null-momentum-and-four-constraints

**Verdict: SOUND WITH FIXES.**

### Recomputed by my own route
Independent of the GA curvature formula: linearised Riemann in components,
R_abcd = 1/2 (k_b k_c h_ad + k_a k_d h_bc - k_a k_c h_bd - k_b k_d h_ac), Einstein = Ric - 1/2 eta R, on the 10
symmetric h, exact Fractions (/tmp/referee-D/d1.py, d1b.py, d1c.py).
- Kernel: 6 at null k = (1,0,0,1), (5,3,0,4), (13,3,4,12); 4 at timelike (2,1,0,0), (3,1,1,1) and spacelike
  (1,2,0,0), (1,0,1,1). Rank 4 at null, 6 off the cone. Confirms (i) and the "two free directions" count.
- Image at null k: every column is conserved (G_ab k^b = 0), has G_11 = G_22 and G_12 = 0 (TT-free); rank 4 =
  10 - 4 - 2. Confirms (ii).
- Other dimensions: Cl(1,2) kernel 3 = displacements only; Cl(1,4) kernel 10 = 5 displacements + 5 TT. Confirms (vi)'s counts.
- Constraint degrees with k = (w, 3, 0, 4): max degree in w is 0 for G_00, 1 for G_0i, 2 for all six spatial
  components. Confirms (v): "four constraints" is right (one Hamiltonian, three momentum).
- B on conserved sources: signature (2 positive, 0 negative, 4 null) at both null samples; (5,1) at timelike;
  (3,3) at spacelike; static B = 1/2 m1 m2. Confirms (iv).
- (vii) arithmetic: B_N for scalar pairs = (1/2) tau s^2, squared 1/4 tau_i tau_j s^4, times 4 pi and 1/4 gives
  pi/4 = (pi/180) 45; alpha = (pi^3/17280)(45*4/225) = pi^3/21600; copy pi^3/5400; ratios 3840/5789 and
  15360/1519247 = 1.011 percent. Correct.
- (viii): (2 + 2/98)/(1 + 2/98) = 99/50, 2/(1 + 2/98) = 49/25. Correct, consistent with the stored burst theorem
  @2 clause (iv) (D = (2 + g + o)/(1 + g)).

### Proof steps
(i) to (v) are proved in the proof text, not only sampled: the kernel characterisation h(k) = tr(h) k/2 and
independence of the four conditions, the direct sum with G_k, symmetry of G_k by the explicit bilinear formula,
image = annihilator of the kernel, the null-frame expansion for (iii)/(iv), the divisibility argument for the
pole (F(w) polynomial vanishing at both roots of Q(k)), and the degree argument for (v) (e0.G(e0) = kappa.G(kappa)/w^2
is a polynomial, hence constant). I checked each. Premises used are read at the pinned versions: Weyl-flat @1
(i) ker R_p = G_p and (iii) conserved sources annihilate G_p; pair-production @1 clause (i) and the Ricci form;
Newtonian coupling @4 for the normalisation; Maxwell modes @5 for the comparison only; burst theorem @2 (iv).

### Perturbations
- p1: Einstein map with trace coefficient 1 in place of 1/2: image and constraint checks fail; kernel check still
  passes (correct: Ric - tr Ric id has the same kernel in four dimensions), so the kernel check alone does not
  pin the 1/2.
- p2: n_+ built with + in place of - (a traceful map): kernel, image, pole and pseudoscalar checks fail.

### Issues
1. Free part (standing decision). The formal clauses do not decide whether the field has a free part with
   states; (viii) lists options. But the lay text does: "except in two components that travel at the speed of
   light" and "They are the two polarisations of a gravitational wave." Under (OS) nothing in the series
   travels in those components; they are kernel directions at null momentum. Fix: "two components at null
   momentum that the source does not fix; in standard physics these are the two polarisations of a
   gravitational wave; whether the series gives them any existence of their own is open." In the Reading,
   "A solution without source exists only in those two components" should read "the first-order equation has
   solutions without source only in those two components".
2. Helicity two. Not asserted in the formal clauses. The Reading's "of helicity two" is justified by the proved
   sentence in (i) (a rotation of m1, m2 rotates n_+, n_x by twice the angle); cite (i) there.
3. (vii) labels. The identification of B_N = 1/2 tr tr with the interaction of a field varied only within the
   Weyl-flat class rests on stored Weyl-flat (iii) (one condition on the trace) plus an argued step (Lorentz
   invariance, second order, constant from the Newtonian limit). Label that identification argued, or present
   B_N as a definition. "The static coupling and the entangling phase do not test the trace-free channel" is
   right for those two. Outside the series, light deflection already tests that channel classically (photons are
   trace-free; standard, from memory). Scope the sentence to the stored results.
4. Technical level: "two percent at most" holds only for holes hot enough to emit at least massless neutrinos,
   photons and the two components (the Page 1976 mix). A colder hole emitting only photons has a larger g.
   Qualify it.
5. Duplication: stored Weyl-flat @1 clause (ii) already names N_p, "the two transverse trace-free (helicity-two)
   directions", and G_p + N_p as an invariant class (computed at one null p). D1 (i) is the proved, general form.
   Say so in the extraction note.

"proved" is the right status for the entity: (i) to (v) are proved, and (vi) to (viii) are correctly labelled.
Ledger transport-absent: agreed.

---------------------------------------------------------------------------------------------------------------

## D2. synthesis.constraint-and-dressing-do-not-restore-commutation-for-a-slaved-field-and-the-transverse-part-does

**Verdict: OVERSTATED.** The clauses compute what they say. The id and the one-liner state a general claim
("constraint and dressing do not restore commutation; the transverse part does") that the model shows only for
particular choices. Clause (4) also carries a hidden hypothesis.

### (a) Lattice model rerun, perturbed, recomputed
- My own lattice (/tmp/referee-D/d2.py: sites, links, div, grad, graph Laplacian, exact solve):
  7 x 7 box, 84 links, 82 off the string, kappa nonzero on 76 of them. Reproduced.
- My own dynamics (d2dyn.py: E += h curl^T curl A, A -= h E, 13 x 13, n_d = 5, 0 <= n <= 10, distance by
  plaquette-sharing): 2750 spacelike events; string-dressed coefficient S = 0 at all 2750; slaved retarded
  difference nonzero at 878, first at step 4 (44, 86, 120, 152, 166, 164, 146 at steps 4 to 10). Reproduced.
  With h = 1 my code gives the same 0 and 878, so the counts do not depend on the step.
- Commutators recomputed by hand and in GA: [P1, e2] = e1 (P1 = (1 - e12)/2); [G_a, U] = -g q e1; for
  p, q = 3/5, 4/5, [P1, O] = 12/25 e2 = pq e2; [E_l, O_f] = g pq f_l X_f from O_f = p^2 P1 + q^2 P2 + pq(vW(gf) + wW(-gf)).
- Mutants: q1 (dress the detection by kappa instead of chi in the off-string check): fails, as it should (this
  is clause (5)). q2 (STEP = 1): the dynamics check fails, but on its hard-coded sample values (-7/64, -15/256),
  which depend on h. The counts do not depend on h (see above).

### (b) Which dressings
- With no transverse variable the observable algebra is the matter algebra. Every "dressing" is then a matter
  element, so dressing means nothing new there. The general statement is one line, and the proof should give it
  in place of the single bare O: [E_l, O'] = g kappa_l [P1, O'] for every matter element O'. So every detection
  that does not commute with the charge fails on the 76 links.
- With transverse variables only two dressings are examined: the Coulomb dressing kappa fails and the string chi
  succeeds. Nothing is shown for "all dressings". The title's "do not" is a statement about one model, one
  charge configuration and these two dressings.
- Hidden hypothesis in (4). "No transverse variable" is read as E^T = 0, and the proof writes E_l = g Sum_s K_l(s) rho_s.
  But a field with no variable of its own may carry a transverse part that is a matter element. Counterexample:
  E_l = g chi_l P1 + (a number field f0 with div f0 = g delta_b plus background). It satisfies the constraint
  exactly, lies in the matter algebra, and [E_l, O] = g chi_l pq e2 vanishes on every link off the string. So the
  equal-time failure in (4) belongs to the Coulomb choice, not to every slaved field that satisfies the
  constraint. The robust failure is the dynamical one in (7): a slaved field that also obeys the field equation
  cannot stay string-shaped (static transverse E drives A, which drives E) and relaxes to kappa. Fix: state (4)
  for the Coulomb slaved field, and make (7) the statement that the constraint does not restore commutation for
  a slaved field obeying the field equation.

### (c) The transverse part
In the 2+1 model the transverse part is the curl part (36 dimensions in the 7 x 7 box: 84 - 48). On the chain
(6) there is none, and the slaved field then commutes outside the interval. So "except in one space dimension"
belongs in the title as well. The carry-over to the gravitational field is labelled argued in the Reading, and
the standard facts are flagged as cited from memory. The extraction note's sentence "if it does, the constraint
and the dressing of observables do not supply that, and the two free components need variables of their own"
reads as a conclusion for gravity. It should carry "argued" too, and for gravity it depends on the hidden
hypothesis above (in gravity the constraints also leave the TT data undetermined).

### (d) Stored or new; relation to gauge theory gravity
A new model: lattice Maxwell with a Gauss constraint in two space dimensions, against the stored 1+1 scalar
model. It does not overstate the relation to gauge theory gravity: it says "not a model of spin two", and
outside_ga is declared correctly. The Reading's identification of the gravitational constraints with D1 (v) is
consistent with D1.

### D2 further: which operator carries the retarded failure
The failure is carried by the source operator. [E^sl_l(n), O] = (E^(a) - E^(b))_l(n) pq e2 comes from
[P1, O] = pq e2. P1 is the charge at a. It is constant in time (the quantum is at rest), so P1 at the source
event (step 0, at the string) does not commute with the detection O (step 5, at the same sites). That pair is
timelike, not spacelike. I checked that every one of the 878 failing events lies in the forward cone of the
source event (distance from the string <= n) and outside the cone of the detection. This is the standard
Yang-Feldman/Peierls mechanism: the field at x depends on J(y), y in the past of x, and J(y) fails to commute
with O(z), z in the future of y. It is not a lattice artefact. The step has an exact cone, and the count is the
same at h = 1/2 and h = 1. In a 2+1 continuum the retarded Green function fills the inside of the cone, so
J+(source) \ J(detection) is nonempty and the failure survives. Only the number 878 depends on the box, the
window and the step. The text should say where the 878 events lie and which operator carries the failure.

### True weaker statement
"In a two-dimensional lattice Maxwell model with a Gauss constraint and one quantum on two sites:
(a) with no transverse variable, the Coulomb slaved field fails to commute with every detection that does not
commute with the charge, on 76 of 82 links; and the retarded slaved field that satisfies the field equation fails
at 878 of 2750 spacelike events, all of them in the forward cone of the source;
(b) with canonical transverse variables, the string-dressed detection commutes at all spacelike events and the
Coulomb-dressed one does not;
(c) on a chain the slaved field commutes outside the interval."
Rename the id along these lines. Change the one-liner's closing clause to "the constraint and the Coulomb
dressing do not restore commutation in two dimensions; canonical transverse variables with a string dressing do."

Status: (1) to (6) are proved in the text (the counts computed exactly). (7) is correctly computed. "proved" is
right for the restated claim, not for the id's general one. Ledger transport-absent: agreed.

---------------------------------------------------------------------------------------------------------------

## D3. synthesis.slaved-field-failure-is-a-first-order-signal-from-a-classical-source-and-no-stored-premise-bounds-it

**Verdict: SOUND WITH FIXES.** The proved content is (1) and (2), which are correct and short. The survey is
honestly labelled in the formal text but stated as fact in the id and the one-liner. The text should say in
plain words that the model predicts faster-than-light signalling.

### Recomputed
- My own lattice (d3.py: phi(t+1) = phi(n+1) + phi(n-1) - phi(t-1), unit kick at (0, t'), t' = 0..5, t_d = 8,
  grid |n| <= 18, 0 <= t <= 18): 502 spacelike events, S nonzero at 172; 252 not later than the detection, S
  nonzero at 32 (all at t >= 5, including equal-time events (+-1, 8)); max |S| = 3. Reproduced.
- Signal formula in Cl(1,2) by my own construction (V = P1 + e^{I theta} P2, cos theta = 3/5, sin theta = 4/5,
  p, q = 5/13, 12/13, three states): <V^-1 O V> - <O> equals pq[a(cos theta - 1) + b sin theta] exactly in
  all three. The bound |sin(theta/2)| and its equality case are checked algebraically.
- Gravitational numbers: G/(hbar c) = 6.674e-11/(1.0546e-34 x 2.998e8) = 2.111e15 kg^-2;
  D|1/r1 - 1/r2| = Dd/(D^2 - d^2/4) = 112500/186875 = 0.602; Phi_w = 2.111e15 x 1e-28 x 0.602 = 1.27e-13;
  runs 4/Phi^2 = 2.5e26; 1 kg at 1 m: 21.1 x 2.5e-4 = 5.3e-3; order one at about 190 kg; tonne 5.3. Cutoff
  level for a tonne at 0.1 m: 3.9e-91, unit level at 7e-32 m, inside 2GM/c^2 = 1.5e-24 m. All correct.
- Mutants: r1 (t_d = 7): the signal and count checks fail. r2 (state not at the extremum): the bound-equality
  check fails. r3 (path separation doubled): the size check fails.

### (a) Signal, units, order, classical source
The change of probability is computed exactly, to all orders, in the dimensionless lattice model. The
first-order term is lambda g S (c1 - c2) pq b: first order in the product of the device strength and the
coupling. In the gravitational reading theta = Phi_w is first order in G (G m_A m_B). "Classical source" is
defined by (D): a c-number lambda in place of J. In (5) the mass m_B at a definite position is classical by
stipulation. The 140 later events (Alice to Bob) are argued in the proof's parenthesis, not computed; label them so.

### (b) "No stored premise bounds it"
The formal (S) is labelled "a survey ... not part of the proved clauses". The proof names what was read (the
locality theorem clause 1, Dimock (a), the causal-perturbation theorem (i), (Loc)) and a text search ("commutation
at spacelike separation, signalling and a least length"). That is the right form. The id and the one-liner,
however, state "no stored premise ... implies commutation or bounds the failure" as fact. Reword both as the
outcome of a survey with its scope: "a survey of the stored locality statements and the cutoff premises
(listed) found none that ...".

Provenance gap: (C1), (C2) and (C_loc) are read "at the pinned versions", but no versions are pinned for them
(not in uses, by design, to avoid edges). Name the versions read in the text: C1 @5, C2 @4, C_loc @6.

My own attempt at a bound. (C1) places modes on 2M/r^3 = 1, inside a hole. (C2) is a density per Planck cell
there. (Loc) is an entropy density on local horizons with no mode count. None mentions a body away from a hole,
a product of masses, or a phase. A Planck-length floor on the localisation of either body changes Phi_w only at
relative order l_P/d, because Phi_w depends on D|1/r1 - 1/r2|, which is about d/D. The only bound I could form,
that the device not be a black hole (m_B < Dc^2/2G, about 7e26 kg at 1 m), is not a stored premise and is
irrelevant at these masses. I could not derive a bound, so the negative stands as a survey outcome.

### (c) Status
"proved" is right only for (1), (2) and (4) (from the stored result). (3) and (6) are computed, (5) is argued,
and (S) is a survey. The entity can stay proved only if the headline becomes the proved statement, for example
"In the stored lattice model, given (D), the slaved field's failure is a first-order change of the detection
probability by a classical source at a spacelike event; a survey (scope listed) finds no stored statement
implying commutation or bounding it."

### (d) Hypothesis (D)
As stated: Bob holds a c-number source lambda, couples to the field by the model's own coupling, and evolution
is by units, V = exp(-I lambda phi_n(t)). It is the standard minimal assumption that a field is observed by
local coupling to it, so in that sense it is a modelling assumption and not an exotic one. But since the slaved
phi is an element of A's algebra, (D) is precisely the grant to Bob of a unitary on A's path degree of freedom,
exp(-I lambda g S J), from a spacelike event. Given the stored commutator, the conclusion is a one-line
consequence of (D): signalling follows from non-commutation plus local unitary couplings. (D) carries the whole
step from the stored result to the conclusion. The text should say this rather than present the signal as a
discovery about the model.

### (e) The size estimate: superluminal or retarded?
The estimate is about a signal outside the light cone. Phi_w counts only the phase accumulated in the window
T <= D/c, while Bob's placement is spacelike to Alice's detection. That phase is zero in standard physics, where
B's field reaches A only after D/c. The text keeps the two apart in (5) and in the lay text ("shifts at once,
before any signal at the speed of light could arrive"). Even when the detection is later than D/c, the slaved
model has an extra phase Phi_w relative to the retarded Newtonian one, so the superluminal part is never hidden
by the ordinary influence.

Plainly: the model as stored, with the element reading extended beyond the static limit (as in the stored
result's Reading) and with (D), implies a faster-than-light signal of order one once m_A m_B D|1/r1 - 1/r2| reaches
the Planck mass squared. That is about 190 kg at 1 m against a 1e-14 kg superposition at 250 micrometres. What
produces it is the absence of the field's own variables. The field at Bob's event is a function of A's path
operator, so Bob's coupling is a coupling to A. It is not the lattice dispersion (the lattice has an exact cone),
and in the lattice it is not an instantaneous part (the field is retarded; the signal needs Bob in the forward
cone of the source events, which all 32 early events are). In (5) the instantaneous reading of the static coupling
gives the same number, since the superposition is older than D/c.

Is it refuted by everyday experience? Not as stated. It needs a superposed mass of at least about 1e-14 kg (not
yet achieved; the largest superpositions are about 1e-23 kg, from memory), and the source placed within about
3 ns. For a moving source the text's argued v/c factor makes it about 1e-5 for a tonne at 1 km/s. With present
atom interferometers and kilogram source masses, Phi_w is below about 1e-9 (my estimate, inputs from memory).
But it violates relativistic causality in principle at accessible source masses, and it is not small for the
proposed mesoscopic superpositions with an ordinary source. The Reading's phrase "(5) is the size of what is being
accepted" should become "(5) is the size of a faster-than-light signal that the slaved reading predicts".

Further fixes:
1. Double counting. If both bodies couple to each other's slaved fields, the Newtonian phase is counted twice
   after D/c unless each takes half. The parenthetical "half of this" should say why: it is the formulation
   consistent with Newton's law at late times, so the numbers are 6.4e-14 and 2.6e-3 under it.
2. (6) is trivially true (the cutoff surface lies inside a hole). Keep it as a remark, not a clause.
3. Lay: "an ordinary mass will do" should add "next to a superposed mass far heavier than any yet made".

Ledger transport-absent: agreed. No circularity found: the past cone is the stored lattice result and the
static coupling.

---------------------------------------------------------------------------------------------------------------

## Across the group
- Consistency: D1 (v) supplies the "four constraints" that D2's Reading uses, and D1 (ii) and the Reading
  supply the "two components" that D2 and D3 point to. No contradiction among the three.
- All three respect the standing decisions in the formal clauses, but D1's lay text and D2's extraction note
  lean toward the free part. D3 states (OS)-type extensions as hypotheses.
- The common mechanism (D2 further, D3 (e)): a slaved field inherits the source operator's failure to commute
  with its own later detection. That pair is timelike. The failure appears at events in the source's forward cone
  and outside the detection's cone. It is continuum physics, not a lattice artefact.
