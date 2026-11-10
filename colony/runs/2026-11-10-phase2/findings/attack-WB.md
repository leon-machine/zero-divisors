# attack-WB: cluster W, angle B (adversarial). Run 2026-11-10-phase2

Status: pre-registration below was written before any computation (13:07); results sections added after.
Labels used below: stored / proved / computed / argued / conjectured.

## Pre-registered kill conditions (one per target)

Thesis under attack (phase 1, Leon's decision of 10 November): "the window reading equates mean Killing energy
only; the entropy mismatch (1/2) ln 2 against pi/6 is a difference of objects and harms no stored result."

W1 (the exact comparison; base statement is WA's). My adversarial claim to test: the energy match is NOT robust.
 K-W1: I assert that along the Gibbs family of an array at fixed spacing kappa (temperature varied, window fixed),
 the array's symmetric-ordered mean energy equals the continuum's extensive window energy measured from the null
 ground state at exactly two points (the ground state and the Hawking temperature) and nowhere else, and that the
 entropy deficit (1/2) ln 2 - pi/6 is the Clausius integral of that energy mismatch. KILLED if the difference
 D(x) = E_array - E_continuum (x = window length / thermal length) has another zero in 0 < x < infinity, or if
 the identity "integral of beta dD from the ground state to the Hawking point = (1/2) ln 2 - pi/6" fails. If
 killed, the clause "in every state" of the window reading could hold on a larger family than I claim and my
 objection to it falls.

W2 (construction; conventions). Adversarial claim: the verdict "array entropy (1/2) ln 2, energy 0" depends on
 choices put in by hand (window length, boundary condition, ordering).
 K-W2: I assert that among circles of length L = m (2 pi/kappa)/n ... precisely: for window length r thermal
 periods and twist (boundary phase) delta, the pair (energy match with the null ground state at the ground state,
 energy match at the Hawking temperature) holds ONLY at r = 1, delta = 1/2. KILLED (as an objection) if that
 uniqueness holds: then the choice is forced by the energy reading itself and "put in by hand" is wrong.
 CONFIRMED as an objection if another (r, delta) passes both energy tests with a different entropy.
 Second test: periodic boundary condition (delta = 0) and Dirichlet-type restriction: entropy value; the question
 is whether any natural boundary condition gives pi/6 or (1/2) ln 2. Pre-registered expectation: none gives pi/6
 exactly at r = 1 (pi/6 is transcendental against values built from theta constants); killed if one does.

W3 (absolute S against differences; the 3/(4 pi) number; pred.boundary-mode-density).
 K-W3: I assert there exists at least one stored result in the future cone of the window reading, or among the
 count's results, that uses, beyond mean Killing energy, one of: (a) a continuum window entropy, (b) the array's
 energy variance set against a continuum value, (c) an identification of array states with continuum states
 other than at the ground state and the Hawking state. KILLED if the audit of every stored dependant (list
 below, each read in full, clause by clause) finds no such use: then "category mistake at every use" is the
 established verdict and I report that as the result. The audit list is fixed BEFORE reading: every entity whose
 files name synthesis.window-reading-array-killing-energy, their used_by closure, and the count's entities named
 in RUN.md cluster W.
 Number check: 3/(4 pi) units per Planck area per component in place of 1/(4 ln 2): KILLED as a stored-number
 correction if my recomputation gives a different value or a dependence on the two-array unit that the phase 1
 note missed.
 Prediction: I assert pred.boundary-mode-density's kill condition is not touched. KILLED if its text, quoted,
 is met by the exact W1 statement (a derivation from boundary modes returning another residue).

W4 (the premise that would equate entropies).
 K-W4: I assert that NO premise can equate entropy as well as energy at fixed spacing: equality of mean energies
 on the whole Gibbs family forces equality of entropies (Clausius integration from the ground state), and the
 energies differ off two points, so the extension is inconsistent, not merely unadopted. KILLED if there is a
 consistent one-parameter rescaling (for example window length tied to temperature) under which both match.
 Sub-test (two-array unit): the ratio (array entropy)/(continuum entropy) is unit-independent. KILLED if some
 grouping (n arrays against n components, or arrays against both chiralities) changes the ratio.

## Orientation and routes (after reading; scratch in work/WB/)
Read directly under store/: window reading v2; null-ordering v4 (formal, check); residue-requires v1 (formal, proof
(i)); one-window-parity-recurrence (formal (i), proof passages naming the reading); light-ray-recurrence and the two
entities above it (word-level audit, see W3); clausius-is-window-first-law v3 (formal, all seven clauses);
(C_loc) v6 (formal in full); clausius-route-newton-constant v4 (formal); eviction-window v7 (formal); one-liners of
the count's entities; pred.boundary-mode-density v3; op.residue-killing-weights; the imported theta Fact v2; (Q) v3
(weight clause passages). Not read in full: hawking.i-state-continuum, positive-null-energy (iv), residue-each-convention
(taken from the phase 1 bridge note, which quotes them).
Routes. (1) The problem's own: audit the dependants for a use beyond mean energy. (2) From another subject
(thermality/Clausius): Clausius integration along the Gibbs family turns "energies equal at every temperature" into
"entropies equal", so the entropy mismatch must show up as an energy mismatch somewhere. (3) Own: leave the array's
spacing free and ask whether the two stored energy equalities still single out the array (modular fixed points).
Choice: (3) for the proposal (it is the only one with a new exact statement and it does not overlap WA's base
statement, which fixes twist 1/2 and varies r); (1) and (2) reported as findings.

## Results

### W2 / "different window length, boundary condition": K-W2 objection CONFIRMED in part (proved + computed)
proved (exact identity; eta-quotient involutions from the stored theta Fact (b); rigorous rational enclosures):
with spacing kappa/r and twist delta, compared with the continuum over the array's own window of r thermal periods,
- ground test (sea = boost ground state's window energy) holds exactly on (delta - 1/2)^2 = (1 - r^2)/12;
- both tests (ground, and thermal energy = 0 at the Hawking temperature) hold at (r, delta) = (1, 1/2), (1/2, 1/4),
  (sqrt(2/3), 1/3) and mirrors; these are fixed points of tau -> -1/tau for theta_3/eta (twice) and of
  sigma -> -1/(6 sigma) for eta(2s)eta(3s)/(eta(s)eta(6s));
- entropies at the Hawking temperature: (1/2) ln 2, (1/4) ln 2, 0.29379..; per thermal period 0.3466, 0.3466, 0.3598.
  None is pi/6. So even among arrays passing BOTH stored energy equalities the entropy per unit Killing time is
  not unique.
- (Q)'s parity clause alone keeps (1, 1/2) and the two half-arrays (Pell equation m^2 - 3p^2 = 1 for the ground
  test; thermal test fails for m >= 7, proved by a bound); (Q)'s particle-hole clause, or its spacing, keeps only
  (1, 1/2).
computed, not proved: no fourth point on the conic (floating scan, step 0.005).
Candid reading: this does NOT break any stored result. The stored uniqueness (null-ordering (ii), window reading
"What it is for" (i)) is stated at spacing kappa and stands. What it changes is the reading of "the half offset is
singled out by (N+)": the selection uses the spacing (slope clause) of (Q) as an input; with the spacing free the same
two energy equalities admit twist 1/4 at spacing 2 kappa and twist 1/3 at spacing kappa sqrt(3/2), and under (Q)'s
parity clause alone a half-array (1/4) ln 2 survives, for which "two arrays per unit" would read "four".
Boundary conditions for the entropy: periodic (delta = 0) at r = 1 gives S = 0.7204 (stored ln 2 + eps) and fails
both energy tests. My pre-registered sub-expectation "no boundary condition gives pi/6 exactly at r = 1" is KILLED:
by continuity in the twist (0.3466 at 1/2, 0.7204 at 0) some twist does, and WA brackets it in (6/25, 1/4). That
twist fails both energy tests at r = 1 (only 1/2 is on the conic there) and is not particle-hole symmetric. On the
conic itself no point gives pi/6 (computed: S per thermal period stays below 0.37).
Proposal: synthesis.window-energy-tests-with-free-spacing-admit-twists-half-third-and-quarter (see "Proposals").

### W1 (WA's base statement; my adversarial test K-W1): SURVIVED, reported as a finding, not filed
computed (scratch floats; proof sketch exact): fix the array (spacing kappa, twist 1/2) and vary the temperature.
Take the continuum at the same temperature, energy over the window measured from the null ground state:
E_cont = (pi/12) L (1/beta'^2 - 1/beta^2). With x = L/beta' and P(y) = sum_k (k+1/2)/(e^{2 pi y (k+1/2)} + 1),
modularity gives x^2 P(x) + P(1/x) = (1 + x^2)/48 and
  D(x) = E_array - E_cont = (pi/(12 L)) (1 - 48 x^2 P(x)) = (pi/(12 L)) (48 P(1/x) - x^2).
D < 0 for 0 < x < 1, D > 0 for x > 1 (x^2 P(x) is strictly decreasing for x >= 1 since t^2/(e^{2 pi t} + 1)
decreases for t >= 1/2; the other half by the second form). So the energies agree at exactly two temperatures:
zero (the ground test) and Hawking (the thermal test). And since dS = beta dE for both objects with S -> 0 at
zero temperature, integral of beta' dD from zero temperature to Hawking = (1/2) ln 2 - pi/6 = -0.17702 (quadrature
-0.177025). The entropy deficit IS the Clausius integral of the energy mismatch off the two matched states.
K-W1 not killed. This is the same one-parameter family as WA's r (only L/beta' matters) with a different
continuum comparison (WA: continuum at Hawking temperature, window varied; here: window fixed, both at beta').
I have not filed it; if WA's W1 does not include the temperature form, one clause there would carry it.

### W4: K-W4 SURVIVED (argued from the above)
No premise can equate entropy as well as energy for the stored array: equal mean energies along the Gibbs family
would force equal entropies, and the energies differ at every temperature other than the two matched ones. The
only rescaling that keeps both tests, tying the window to the temperature (L = beta' always), makes the array's
weights beta' omega = 2 pi (k + 1/2) temperature-independent, which is what (Q) already says; then there is no
thermal family to integrate over and the entropy stays (1/2) ln 2. So "the continuum's entropy for the count" is not
an unadopted extension of the reading; it is inconsistent with the reading's own energy clause off two states.
Consequence for the wording of the window reading v2: its formal says the array's Killing energy "in every state"
is the continuum's over the window. No map from array states to continuum states is given, and with the natural
one on Gibbs states (equal temperature) the clause fails except at two states. The dependants use exactly those two
states (sea: the constant -kappa/24; Hawking: 0). Suggested wording fix below.
Two-array unit (sub-test): ratio array/continuum entropy is 3 ln 2/pi = 0.6619 per component for every grouping
(1/(2 u ln 2) against 3/(2 u pi) units per Planck area at mean u arrays per unit). Not killed.

### W3: K-W3 KILLED (my assertion of a stored use beyond mean energy is false): category mistake at every use
Audit list fixed before reading; result per entity:
- synthesis.null-ordering-of-counted-units-is-zeta-symmetric v4: uses the sea's energy and the Hawking state's
  energy. Two states, mean energy only. No entropy, no variance.
- synthesis.one-window-parity-recurrence...-twenty-four-arrays: uses the reading for the additive constant
  -kappa/24 of each array's Hamiltonian (the sea's energy), then the array's own spectrum. 0 occurrences of
  entropy/variance; says the KMS state is unchanged by the constant. The recurrence itself is a property of the
  twisted circle that the continuum does not have (stored as a strengthening outside the reading). Energy only.
- synthesis.light-ray-recurrence-test-verdict..., synthesis.capacity-and-sakharov-readings...,
  synthesis.mass-terms-are-pair-terms...: 0 occurrences of entropy, Gibbs, KMS, variance, thermal (word-level audit,
  not a clause-by-clause read). Energy constant only.
- synthesis.the-residue-requires-two-arrays...: names the reading in the premise-by-premise independence audit
  only; the entropy used is the array's (1/2) ln 2.
- Count entities (residue-from-mode-entropy, half-integer-weight..., counted-unit-energy..., residue-each-convention,
  de-sitter-mode-count, pred.boundary-mode-density): array (point-spectrum) entropies only; absolute values.
- synthesis.clausius-is-window-first-law-plus-boost-charge-conservation v3: the nearest thing to a real use.
  Clause (2): Delta S_F = beta dQ - S(rho'||rho_I) on a point-spectrum window; clause (7): the same first law on the
  continuum for entropy differences (type III, imported Fact). First order: both objects obey dS = beta dE, no
  mismatch. Second order: the defect is (dE)^2/(2 Var) for Gibbs-family changes, and the variances differ
  (0.798 against 0.524 per component per window), so the two carriers disagree at order dQ^2. The store uses the
  defect only as "two orders beyond the balance" (Consequence paragraph). So: a real second-order difference
  between the carriers, used nowhere. Clause (7) also states that "a point-spectrum discretisation replaces h by an
  operator whose second quantisation is no longer the boost flux", which is the stored acknowledgement that the
  array's Hamiltonian is not the continuum's boost charge; the window reading's "in every state" sits uneasily
  beside it (wording, not a contradiction: the reading's cost paragraph says the same).
- synthesis.c-loc-local-horizon-premise v6: the one place where the continuum carrier and an ABSOLUTE entropy
  meet. Its modes are "the continuum mode space ... one carrier per light ray"; (Loc) integrated reading gives
  S[cut] = integral of eta dA, eta = 1/4 "with no mode count"; "One mode set, per light ray": the cutoff windows
  are "discretisations of the per-light-ray carrier". Here the entropy is a premise about the cut, not computed
  from the continuum state, so pi/6 is not used. But it means the store has two absolute entropies of one mode
  set (the count's N ln 2 and (Loc)'s eta A) that agree by calibration, with the continuum as carrier of the
  second. Not a mismatch; the place a future one would appear.
- Eviction results: per-pair entropies h_k of point-spectrum modes; no continuum flux.
Absolute against differences: absolute values are used by the count (N_epoch ln 2 = S_BH, the residue, the de
Sitter mode count, the hole-mass label Z = e^{-A/4}) and by (Loc) in its integrated reading; differences only by
the Clausius/Einstein route and clausius-is-window-first-law.
Number check: continuum entropy demanded -> 3/(2 pi) components per Planck area, 3/(4 pi) = 0.2387 units of two
components per Planck area (RUN.md's "3/(4 pi) ... per component" is per two-component unit), against
1/(4 ln 2) = 0.3607. Ratio 3 ln 2/pi, unit-independent.
pred.boundary-mode-density, kill condition quoted: "A derivation of the calibration residue from the boundary
modes returning any other value, which refutes the intrinsic-clock premise (IC)". Not touched: nothing here
derives a residue; 3/(4 pi) follows only from an entropy identification that is inconsistent with the energy
clause (W4), and the twist-1/3 and half-array alternatives are excluded by clauses of (Q), not derived.

## Sibling WA (pre-registration read 13:20; interim note to me read 13:50)
WA files P1 synthesis.antiperiodic-array-against-the-light-ray-continuum-at-window-length-r (the W1 base statement;
it includes the temperature form of my K-W1 function and the conditional residue arithmetic) and P2
synthesis.light-ray-continuum-is-the-twist-integral-of-arrays-and-window-values-are-twist-averages. I file neither;
P1 is the intended citation of my proposal for the comparison at twist 1/2. WA left to me: the Clausius-integral
form (finding above, not filed), the (r, delta) question (my proposal), the audit (W3 above).
Tests of WA's claims against my computations, and where WA is exposed:
- P1 "each of the three energy comparisons holds only at r = 1": true AT TWIST 1/2. With the twist free the same
  comparisons hold at (1/2, 1/4) and (sqrt(2/3), 1/3) (my proposal). P1 must carry "at twist one half" in title,
  one-liner and lay level, or it is overstated.
- P1 uniqueness at twist 1/2: agrees with my scan (thermal test value negative for r < 1, positive for r > 1) and
  with my exact proof of the temperature form (two zeros only: ground state and Hawking).
- P1 conditional residue 3/(4 pi) per two-component unit, 3/(2 pi) per component: agrees with mine. By my W4 the
  condition ("if the continuum's entropy were demanded") is not a consistent extension of the reading's energy
  clause; P1 should present the arithmetic as counterfactual, not as an available alternative count.
- P2 twist averages equal the continuum's values: not recomputed by me. Two exposures. (a) WA reports the twist
  average of the zeta sea as 0, while the continuum's boost ground state over the window is -kappa r/24 in the null
  ordering: so the twist integral reproduces the continuum in the BOOST ordering, and the null-ordering constant is
  not a twist average; P2 should say which ordering its "window values" are in, since the window reading is a
  statement in the null ordering. (b) Averages run over arrays that fail the stored energy tests (at r = 1 only
  twist 1/2 passes), so "pi r/6 is the twist average" does not make pi/6 the entropy of any admissible array.
- P2 "the antiperiodic array on M r periods is the product of M arrays on r periods with twists (2j+1)/(2M)":
  consistent with my half-arrays (M = 2 gives twists 1/4, 3/4 at r = 1/2). My clause (iv) adds that for M >= 3 the
  factors individually fail the ground test, and that under the parity clause only M = 1, 2 pass both tests.
- WA's W2 kill ("antiperiodic condition derived from (N+)/(Q)"): the energy equalities derive twist 1/2 only given
  the spacing kappa; with the spacing free they do not (my proposal).

## Proposals
1. synthesis.window-energy-tests-with-free-spacing-admit-twists-half-third-and-quarter (op.residue-killing-weights).
   runcheck: 4 functions pass. check4 / validate / propose: see final lines of this file.

## Unexpected links
- The three passing twists are 1/2, 1/3, 1/4: levels 4, 4 and 6 of eta quotients; twist 1/6 lies on no real window.
  Under the parity clause the ground test is the Pell equation m^2 - 3p^2 = 1, the same kind of Pell structure as
  the phase 1 CHSH denominator law (there X^2 - 2Y^2); no deeper link claimed.
- Evaporation ledger (argued, from stored numbers; other subject: eviction/thermality): per window per component
  the outgoing energy in the boost ordering is kappa/24 (stored: the array's energy above its sea), so Clausius
  gives a drop of the hole's entropy of pi/12 per array-window, while the array carries (1/2) ln 2: the stored
  E/(TS) = pi/(6 ln 2) = 0.755 per unit is "arrays removed from the count per array radiated". The continuum
  would radiate pi/6 of entropy per window per component (ratio 2 to the hole's loss, the standard 1+1 value, from
  memory); the arrays give 6 ln 2/pi = 1.324. No stored result states an entropy flux of the radiation per
  window, so there is no stored mismatch, but any future statement of the radiated entropy rate has to choose
  between 0.3466 and 0.5236 per channel per period. This is the first place I would expect the question to bite.
- pi/3 per two-component unit is within 5 per cent of the 1-nat convention (3/(4 pi) = 0.2387 against 1/4). A
  coincidence as far as I can see.

## Decisions for Leon
1. Wording of synthesis.window-reading-array-killing-energy (version 3): replace "its Killing energy, in every
   state, is the Killing energy of the continuum over that window" by a statement about the two states actually
   used (the sea and the Hawking state), or define the state map. Recommendation: restrict to the two states; with
   equal-temperature matching the clause is false elsewhere (finding W1/W4).
2. Whether to record in the window reading / null-ordering result that the selection of the half offset takes the
   spacing kappa from (Q) as input (my proposal, if accepted, is the citation). Recommendation: yes, one sentence.
3. Assumes edge: my proposal names (Q) v3 by claimref for the wording of its parity and particle-hole clauses,
   which are explicit hypotheses of clause (iv), and declares no edge to it (the validator refuses a postulate in
   `uses`, and new assumes edges are the maintainer's). Recommendation: no edge needed; add one only if the
   maintainer wants the citation tracked.
4. If a radiated-entropy-rate statement is ever added to the store, decide which object's entropy it is (see
   Unexpected links). No action needed now.
5. No new postulate or imported Fact is requested. Literature cited from memory as prior art only (Koehler 2011;
   Ginsparg 1988; the interval entropy formula quoted in phase 1).

## Gate status (final)
synthesis.window-energy-tests-with-free-spacing-admit-twists-half-third-and-quarter: runcheck 4/4 pass; check4 exit 0,
0 errors, 0 warnings (log: work/WB/check4.log; a first run gave W413 on the thermal check, fixed by pinning its
literals); validate_one ok (verify/final/); registered with propose_claim (accepted_for_review true, I305 only);
coverage.yaml copied back. Working copy kept in work/WB/<id>/. Total proposals from WB: 1.
