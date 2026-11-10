# Attack DA: dark energy exposure (Cluster D) and the gravity-entanglement literature check

Status: complete (attack round). Labels: proved / computed / argued / conjectured / imported.
Proposal filed (1 of 2 allowed):
`synthesis.norm-released-locally-on-isotropic-fields-tracks-dust-and-never-accelerates`
(check4: 0 errors, 0 warnings, 3 info I405; validate ok, no findings; registered with propose_claim; coverage.yaml
copied). Work files: work/DA/ (cones.py, cones_future.json, group.py, cone_table.tsv, the proposal's source folder).

## Pre-registered kill conditions (written before any computation)

- D1 (statement, no computation). Kill: the stored prediction's kill condition already names a region and a
  significance. Then D1 is a no-op and is reported as such. RESULT: not met. The stored condition names neither.
- D2 (cone audit). Kill for "the exposure is contained": if the forward cone of the field-space premise (FS) or of the
  frozen-point identification contains results outside gravity/dark energy that have no restatement without it
  (for example the Standard Model mass results or the dark-matter ratio), the exposure is NOT contained and is
  reported as wide. Grouping rule fixed in advance: a result "falls" if its statement asserts w = -1, a constant
  Lambda or the parallel frozen point as fact about the world; "survives restated" if it is a conditional or
  structural statement whose proof does not use the constancy of the norm on matter regions; "untouched" if (FS)
  and the frozen-point identification are not in its past cone. RESULT: not met; the exposure is narrow by edges and
  moderate by content (below).
- D3 (fallback). Claim to test: no stored structure permits w different from -1 in a way compatible with the data.
  Kill: any stored structure that gives a dark-energy density evolving with w near -1 and no contradiction with
  another stored result. First computation, fixed in advance: the locally released norm on the flat FLRW
  gravitational field with dust, torsion solved rather than set to zero. Kill for the proposal "the local release
  is no fallback": an accelerating solution, or a dark-energy equation of state within the region the surveys
  prefer. RESULT: not met. The release gives w = 0 tracking with deceleration 1/2 (proved on the isotropic family).

## Leon's decisions received during the run (DECISIONS.md, first round)
1. Threshold fixed: two independent surveys each excluding (w0, wa) = (-1, 0) at five sigma. D1 drafts exactly that.
2. The series' position is that the graviton does not exist. The literature check below reports experimental
   status only and quotes the stored prediction in the series' own terms.

## D1. The stored prediction and its registration as a region

Stored (read directly from store/predictions/pred.dark-energy-w-minus-one/entity.md, version 4, status live):
- formal: "Dark energy cannot evolve: w = -1 exactly, at every epoch; registered with its one condition, that on
  matter-filled regions the gravitational connection, the Cl(2,4) connection that preserves the frozen point I,
  keeps it parallel in the physical scale, <X, I> = 1 (Proposition dark-energy.vacuum-region-registration-condition
  (iii)); in that form the condition is the field-space premise (FS) ... which the store adopts."
- kill_condition.threshold, verbatim: "A confirmed detection of $w \neq -1$ at any epoch, with no parameter
  available to absorb it"; data_source: "DESI DR2 with CMB and supernovae"; registered: "2026-08 (T17 stance table,
  row 2)".
- basis: one derivation, uses dark-energy.vacuum-region-registration-condition@8 (proved; its clause (iii) assumes
  synthesis.field-space-premise-parallel-frozen-point@1, status postulate).
- The same refutation clause appears in two premises: (FS) refutation condition (a), and Premise (N)
  (synthesis.number-n-registered-free-input: "refuted by ... a confirmed w != -1").

What is missing in the stored condition: "confirmed" has no significance, no number of surveys, no parametrisation;
the data source names one release.

### Data as of 10 November 2026 (checked on the web today; sources at the end)
| Source | Combination | w0 | wa | Distance from (-1, 0) |
|---|---|---|---|---|
| DES full survey, arXiv:2605.27221 (v2, June 2026) | all DES (3x2pt + SN + DES BAO) | -0.84 +/- 0.10 | -0.44 +0.60/-0.55 | 2.2 sigma |
| same | all DES + DESI DR2 BAO, no CMB | -0.84 +0.06/-0.07 | -0.53 +0.33/-0.28 | 2.3 sigma |
| same | all DES + CMB, no DESI BAO | -0.74 +/- 0.08 | -1.10 +0.42/-0.36 | 2.8 sigma |
| same | CMB + DESI BAO | -0.54 +0.19/-0.07 | -1.40 +0.29/-0.50 | 2.9 sigma |
| same | SN + BAO + CMB, no 3x2pt | -0.80 +0.05/-0.06 | -0.72 +0.22/-0.20 | 3.2 sigma |
| same | all data (DES + DESI BAO + CMB) | -0.82 +/- 0.05 | -0.63 +0.21/-0.18 | 3.0 sigma (3.4 with neutrino mass free) |
| DESI DR2, arXiv:2503.14738 | DESI BAO + CMB | -0.42 +/- 0.21 | -1.75 +/- 0.58 | 3.1 sigma |
| same | + Pantheon+ / Union3 / DESY5 | -0.838 / -0.667 / -0.752 | -0.62 / -1.09 / -0.86 | 2.8 to 4.2 sigma (range over the three samples) |
| DESI DR2 Lyman-alpha full shape, arXiv:2607.27410 | DESI + CMB; + SN | not in abstract | | 2.7; 3.2 sigma |
| Supernovae Unite, arXiv:2609.05053 | Unite SN + CMB + DES and DESI BAO | -0.861 +0.044/-0.042 | -0.60 +0.17/-0.19 | 3.3 (MAP), 3.1 (max. likelihood); Bayesian evidence weak |

The DES paper's own range is 2.2 to 3.2 sigma by combination, as RUN.md says; best fits always at w0 > -1, wa < 0.
No DESI DR3 result and no later full-survey release was found (searched today). The 4.2 sigma end of the DESI range
used the original DES five-year supernova sample, since recalibrated (DES-Dovekie); the later combinations sit at
3.0 to 3.3. No single survey alone exceeds 2.2 sigma; everything at 3 sigma shares the CMB or mixes DES and DESI.

Verdict against the threshold Leon fixed: NOT MET, by a wide margin. No survey alone excludes (-1, 0) at five
sigma; none reaches three without external data.

### Draft registration text (maintainer-only; for pred.dark-energy-w-minus-one, version 4 -> 5)
kill_condition:
  threshold: "Two independent surveys each exclude the point (w0, wa) = (-1, 0) at five standard deviations or
    more, in the two-parameter form w(a) = w0 + wa(1 - a), with no parameter available to absorb the result."
  data_source: "Stage IV dark-energy surveys with their own low-redshift distance or growth data (at present DESI
    and the Dark Energy Survey; later Euclid, Rubin, Roman)"
  registered: "2026-11-10 (threshold fixed by Leon Butler, run of 10 November 2026; supersedes the wording of
    2026-08, T17 stance table, row 2)"
Proposed note for the formal level: "Note (the registered region, 10 November 2026). The prediction is the single
point (w0, wa) = (-1, 0) of the plane of the two-parameter form w(a) = w0 + wa(1 - a). The series counts it refuted
when two independent surveys each exclude that point at five standard deviations or more. The significance is the
collaboration's published distance of the point from its posterior or likelihood (the two-parameter Delta chi-squared
converted to standard deviations). Two surveys are independent when their late-time data (galaxy, supernova and
lensing samples) are disjoint. As of the registration date no survey alone exceeds 2.2 standard deviations and the
largest combined value in a current analysis is 3.4."
Proposed new observation row: date 2026-11; dataset "DES full survey (3x2pt, supernovae, BAO), alone and with DESI
DR2 BAO and CMB"; result "DES alone: w0 = -0.84 +/- 0.10, wa = -0.44 +0.60/-0.55, 2.2 sigma from (-1, 0); with DESI
BAO and CMB: w0 = -0.82 +/- 0.05, wa = -0.63 +0.21/-0.18, 3.0 sigma; 2.3 to 3.2 sigma as single probes are dropped.";
verdict contested; source "DES Collaboration, arXiv:2605.27221 (2026)".
The same sentence should replace clause (a) of (FS)'s refutation condition and the last clause of Premise (N).

Three points the text above decides silently, each Leon's (listed under Decisions):
(a) whether a shared CMB prior is allowed in each survey's five sigma (the draft does not forbid it; the present
3 sigma values all need it); (b) which statistic counts (frequentist distance, as drafted, or Bayesian evidence:
the Unite paper has 3.3 sigma with weak evidence); (c) that the region is tied to the two-parameter form: the
stored wording "at any epoch" is wider, and a five sigma exclusion of w = -1 in a binned or constant-w analysis
would not meet the drafted text.

### What would change at other thresholds (argued, from the table)
- Three sigma, two surveys, shared CMB allowed: nearly met now (DESI BAO + CMB 3.1; all DES + CMB without DESI
  2.8). Strict independence with no shared external data: not met (DES alone 2.2).
- Three sigma from any one combined analysis: met since 2025.
- Five sigma from one combined analysis: not met (maximum 4.2, on a superseded supernova calibration).
- Five sigma from two independent surveys (the adopted rule): far; the constraint has to tighten by roughly a
  factor two per survey with the central values fixed. This is the conservative end, and it means the series
  will count w = -1 as standing through releases that the field may describe as discoveries. That is a cost of
  the rule and should be said where the rule is registered.

## D2. What falls with it

Method: `cone` (future) through the Lab class over twelve roots (work/DA/cones.py, cones_future.json); a text scan
of the whole store for entities naming (FS); a table of the 226 entities of the forward cone of the frozen-point
geometry (work/DA/cone_table.tsv) with text flags (FS, w, Henneaux-Teitelboim, N, de Sitter, cosmology). Status of
the grouping: argued. Edges are audited over the full cone; the verdict per group is by the pre-registered rule
applied to flags and to the statements of about twenty entities read in full, not to all 226.

Counts (computed):
- Future cone of (FS), synthesis.field-space-premise-parallel-frozen-point: 2 entities
  (dark-energy.vacuum-region-registration-condition, pred.dark-energy-w-minus-one). One assumes edge in the store.
- Future cone of Premise (N) and of programme.n-parameter-of-the-laws: 0 each.
- Future cone of dark-energy.frozen-point-makes-stelle-west-vector (dark energy as the norm of the frozen point):
  155. Of the frozen-point geometry Fact: 226 (216 proved, 7 live predictions, 3 conjectured). Of the
  Henneaux-Teitelboim Fact: 79.
- Entities naming (FS) in text: 13, of which 1 assumes it by an edge.

First finding (computed): the exposure is under-recorded by edges. The (FS) entity says "the store's gravitational
action is the imported functional plus (FS); what carries Einstein's equations is (FS), not the integrand", yet
no Einstein-subject result has an assumes edge to it, and
synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part (future cone 14) does not name it. Likewise Premise
(N) is used in text by about fifty results and assumed by none.

What a confirmed w != -1 refutes, logically (argued): the conjunction of (1) (FS), (2) the reading that ALL of the
dark energy is the frozen point's norm, (3) the stored matter content having no component with w different from
-1 at late times. It does not refute the frozen-point geometry (mathematics), nor Einstein's equations with a
conserved source: a new matter component would absorb it at the price of a new premise, and the measured best fits
(w crossing -1) are not reachable by one minimally coupled scalar (literature, from memory).

| Group (subject; cone size; flagged FS/w/HT/N) | Verdict | Why |
|---|---|---|
| The prediction, its registration clause (iii), (FS) refutation (a), Premise (N)'s last clause | FALLS | They assert w = -1 or carry it as refutation condition |
| dark-energy, kind-of-number and promotion results (41; 17): under-action-written-norm-parameter-laws, promoted-norm-one-global-pair, promoted-norm-weyl-clock-flat-weight, einstein-route-makes-n-initial-data, trichotomy, number-n-free-at-fixed-d-term-level, dating-descent (conjectured) | SURVIVE RESTATED as mathematics of the functional; their physical reading FALLS | Each is a theorem about the action or a classification of N; with Lambda not constant, N = M_P/H is not a number and "parameter or initial data" has no referent |
| dark-energy, spectrum results (Kasner, deposit, descent window; about 15) | UNTOUCHED, except hypothesis (F) of synthesis.frozen-point-geometry-reads-descent-as-vacuum (the late stage is the frozen point's de Sitter field), which FALLS with a constant Lambda | They are no-go results on the early universe |
| einstein (36; 15): the action results (macdowell-mansouri principle, field space is the GTG pair, symmetric slot frozen, infinitely stiff, Weyl-squared on transport, Chern-Simons reduction, stelle-west-norm-is-no-local-output) | SURVIVE as theorems; the claim that the stored action is the law of gravity FALLS with (FS) | Proofs are about functionals; none uses data. The store would have no gravitational action |
| einstein: Clausius route (einstein-equations-from-c-loc-and-clausius, inverse problem, c-loc results) | SURVIVE; Lambda stays an integration constant | The route takes any conserved source; evolving dark energy would be a source the series does not have |
| entropy and thermality (37; 9): de-sitter-entropy-pi-n-squared, de-sitter-mode-count, de-sitter-temperature-frozen-point-norm, cosmological-horizon results, sds-clausius-fixes-area-constant | SURVIVE RESTATED at fixed Lambda; application to the actual future horizon FALLS or becomes conditional | They are statements on the de Sitter or Schwarzschild-de Sitter field; with evolving dark energy a late de Sitter stage is not given |
| black-hole residue, interior, walls, quantum-fields, one-relation, programme, towers, generations, neutrinos, clifford-structure (about 80; 8) | UNTOUCHED | In the cone through the frozen point as a conformal-geometry object (boost, infinity, tractor transport), not through its norm on matter regions |
| dark-matter (45; 3) | UNTOUCHED, with one exception | In the cone through the single frozen point of the descent (P1). Exception reported by the dark-matter attacker (attack-MA.md, Unexpected links): postulate D (democracy) uses the de Sitter radius as a constant of the laws; the two results under D go if Lambda moves; the fitted ratio 5.364 does not use D |
| standard-model (4; 2): constant-d-term-level-fixes-weak-scale-against-planck-under-promotion, d-term-level-free-at-fixed-n | SURVIVE RESTATED | Conditional on the promotion and on N being a number |
| Outside the cone: neutrino.double-prediction-sum-predicted-floor, pred.neutrino-mass-sum-floor | COUPLED (see Unexpected links) | Its confrontation is stated "within w = -1" |

Result against the pre-registered kill: the exposure is contained. Nothing in the Standard Model, mass, family or
dark-matter-ratio results falls. What falls is (FS) and with it the store's only gravitational action, the
registered status of N, and the physical reading of the late de Sitter stage; about fifty results need a
restated premise ("at fixed Lambda", "on the de Sitter field") and none is a theorem that becomes false.

## D3. The fallback question

Routes considered: (1) cite the stored promotion result; (2) compute the stored local release with matter on FLRW
(own route; chosen for the proposal, because it is the one stored structure in which the norm can vary in time and
the store had only its vacuum, constant-norm, torsion-free values); (3) search for another evolving structure
(modulus, deposit, tower).

(1) The Henneaux-Teitelboim promotion gives w = -1 exactly. Stored, proved:
synthesis.promoted-norm-one-global-pair (ii): varying the three-form gives d lambda = 0, "no local fluctuation of
(I, V, lambda) survives". One step added in the proposal's clause (vii) (proved, two lines): under the stored matter
hypothesis (Mat) the three-form term contains neither frame nor matter, so the frame equation is Einstein's with
that constant and the Lambda term has p = -rho; the same for any promoted function g(lambda) with g' != 0. The
Clausius route also gives a constant (synthesis.einstein-equations-from-c-loc-and-clausius: "Lambda an integration
constant"). The promotion changes which solution, never Lambda within a solution.

(2) The local release (the proposal; proved on the stated family, check exact). On homogeneous isotropic
reflection-invariant gravitational fields with flat slices, hb^{-1}(e_0) = n e_0, hb^{-1}(e_i) = s e_i,
Omega(e_i) = y e_i e_0, with the norm u = 3/Lambda a field varied at fixed (hb, Omega) and matter under (Mat):
- density u eps(F, F) = 24 n s^3 u (alpha - 1/u)(beta - 1/u), alpha = y'/(n s), beta = y^2/s^2;
- equations: 3 beta = 3/u + rho~, 2 alpha + beta = 3/u - p~, alpha beta = 1/u^2, 2s(s' - n y) = u' y^2. The rate
  of the norm enters only the last (it sources torsion); the first three are algebraic;
- elimination: Lambda (rho~ - 3p~) = rho~ (rho~ + 3p~), which is exactly the stored clock density of
  synthesis.promoted-norm-weyl-clock-flat-weight (v) set to zero, now without assuming constant norm or zero torsion;
- dust: Lambda = 8 pi G rho at all times, H^2 = (4 pi G/3) rho (half the Friedmann value), y = -2 s'/n, deceleration
  parameter 1/2, the cosmological term scales as a fluid with w = 0; no accelerating solution, no constant norm;
- radiation: no solution (-2 rho~^2 = 0); barotropic: Lambda = rho~ (1 + 3w)/(1 - 3w);
- vacuum: F = 0 and u(t) is a free function, H = +/- u^{-1/2} + u'/(2 n u): any expansion history, no prediction.
So the release permits w != -1 only in the forms "w = 0, never accelerating" (excluded by the supernova Hubble
diagram) or "anything, unpredicted". With the stored exclusion of Schwarzschild-de Sitter
(synthesis.stelle-west-norm-is-no-local-output (iv)) it is not a fallback. Scope limits: the bare functional
(c_3 = c_5 = 0), flat slices, no axial torsion, one fluid for the solutions, (Mat).

(3) Search for anything else (argued; text search of claims, notes, predictions and open problems for quintessence,
rolling, modulus, evolving, decaying, interacting, time-dependent Lambda): no stored entity proposes an evolving
dark-energy density. The hits are the prediction itself, the registration clause, the neutrino result (which says
the series "cannot use that option"), two refuted entries on other topics, and imported bounds. Specifically:
- a rolling modulus: none stored; standard-model.imported-norm-frozen-point-not-field and
  dark-energy.point-infinity-has-no-physical-fluctuation say the norm is not a field; (FS) reading (R3) says a
  frozen point of finite stiffness adds a Weyl square, not a scalar potential;
- the descent's deposit: stored as radiation-like or vacuum plus shot noise at the descent, with no late-time
  component (synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise, synthesis.finite-range-descent-deposit-cannot-seed-cmb);
- the tower: enters dark matter (w = 0) and the counts for N, with no pressure of its own stored;
- the promoted norm's conjugate time advances with matter but is the variable conjugate to Lambda, not a density.

Plain statement: under the stored premises the series has no fallback. No stored structure permits a dark-energy
equation of state different from -1 that is compatible with an accelerating universe. A confirmed w != -1 at the
registered threshold would refute (FS) and the frozen-point reading of dark energy, and the series would need a new
premise.

One thing outside the store that the record should name (prior art; abstract checked on the web, body from
memory): Westman and Zlosnik, "Exploring Cartan gravity with dynamical symmetry breaking" (arXiv:1302.1103, Class.
Quantum Grav. 31 (2014) 095004) report that polynomial actions in which the Stelle-West vector is fully dynamical,
with derivative terms, give "the extensively studied Peebles-Ratra rolling quintessence model" for one choice. The
store's three-term family (c_1, c_3, c_5) is the transcription of that family and is evaluated in the store only on
torsion-free fields of constant norm. So a literature fallback exists in the neighbourhood of the stored action; it
is not stored, it would contradict (FS) reading (R3) (infinite stiffness), and adopting it after a detection would
be a fit. Whether to compute it now, before the data decide, is Leon's call.

## Side task: experimental status of gravity-mediated entanglement (web, 10 November 2026)

What the stored prediction claims, in the series' own terms (pred.gravity-entangles-standard-phase, version 1,
live, review draft): "Gravity entangles two masses, each held in a superposition of two places, by the standard
phase Phi = (G m_A m_B / hbar) int (1/r_11 + 1/r_22 - 1/r_12 - 1/r_21) dt, under the element reading and premises
P-i to P-vi." Kill condition as stored: "A null result at a sensitivity that resolves the standard phase on the
experiment's geometry, with coherence kept for the duration, refutes the element reading together with premises
P-i to P-vi." The accompanying note (note.field-theory.setting-gravitys-source-registered-prediction) states the
mechanism: under the element reading "the geometry's coefficients lie in a commuting algebra of the matter's number
operators. The masses are the field theory's fermions; gravity is not quantised here." The prediction was first
registered under the value reading as no entanglement and inverted on 12 October 2026. Its basis is a working note,
not a series paper (flag already on the entity).

Experimental status: no experiment has observed, or attempted at the needed sensitivity, entanglement of two masses
through gravity. Two separate frontiers exist and neither is near the other:
- Gravity of small source masses (classical regime). Two gold spheres of about 90 mg (Westphal et al., Nature 2021;
  from memory and a search snippet). A levitated magnetic particle of about 0.43 mg sensing kilogram sources about
  half a metre away at attonewton force level (Fuchs et al., Science Advances, February 2024; journal and
  attonewton level checked, the mass from memory). Newtonian attraction between two 7.6 mg silicon plates at 0.65 to
  1.55 mm with a miniature torsion pendulum, consistent with Newton's law (An et al., Nature Communications,
  22 October 2026; via a news report, the paper itself not read). All are classical measurements with no
  superposition of the source.
- Mass in spatial superposition. Matter-wave interference of sodium nanoparticles of more than 7,000 atoms, mass
  above 170,000 Da (about 3 x 10^-22 kg), macroscopicity 15.5 (Pedalino et al., arXiv:2507.21211; published in
  Nature in 2026 according to search results, not confirmed by me).
- The gap. The original proposals need two masses of order 10^-14 kg each in superpositions of order 100
  micrometres held for seconds (Bose et al. 2017, Marletto and Vedral 2017; figures from memory). Demonstrated
  superposed mass is about eight orders of magnitude below that; demonstrated gravitating source mass is about eight
  orders above. Current work is design and simulation: a chip-based magnetic levitation and superposition scheme for
  nanodiamonds of 10^-19 to 10^-15 kg (Xiang et al., arXiv:2601.06608, simulation only); a mass-independent scheme
  with two Stern-Gerlach interferometers (Braccini, Serafini and Bose, arXiv:2602.19306, theory); two milligram
  optomechanical oscillators coupled by gravity at ultra-cryogenic temperature, with sensitivity estimates and no
  measurement (Bonaldi et al., arXiv:2607.18351).
- Against the stored observations rows: both are still accurate; "No experiment has reached gravity-mediated
  entanglement" stands. The stored kill condition is neither met nor probed.

Where the literature's framing differs from the stored one: the literature presents the effect as a witness that
gravity is a quantum mediator, and often as evidence for graviton exchange (the argument that a classical mediator
acting locally cannot entangle). That inference is itself disputed in print: Aziz and Howl (Nature 646, 813, 2025)
claim a classical gravitational interaction with quantised matter fields produces entanglement; Marletto and
Vedral (arXiv:2510.19969), Marletto, Oppenheim, Vedral and Wilson (arXiv:2511.07348) and Gundhi, Infantino and
Bassi (arXiv:2604.19696) dispute that claim on different grounds. The stored prediction takes no side in that
dispute and makes no statement about a mediator: it predicts the standard phase from the element reading, with the
gravitational gauge fields not quantised. So a positive result would agree with the stored prediction and with
every account that predicts the standard Newtonian phase, and would not discriminate the element reading from
them; only a null at resolving sensitivity bears on it. A suggested wording for the entity is under Decisions.

Places in the store where a graviton is counted or named, met during this work (reported, not extended, per
decision 2): synthesis.promoted-norm-one-global-pair (clause (ii), "the graviton still carries no ...
polarisation", and its lay level "the graviton count is untouched"), which the proposal cites for d lambda = 0
only; by text search also
synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional, hawking.joint-j3-s-wave-reduction,
dark-matter.imported-gravity-only-coupling, dark-matter.seeding-gravity-floor-dark-towers-temperature,
scrambling.imported-collars-coframe-exceptional-set-helicity, synthesis.dimmed-burst-time-rescaled-copy,
synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet,
synthesis.collapse-in-vacuum-regular-at-future-horizon-selects-hawking-temperature, and a number of notes (correspondence, hawking, dark-matter, dark-energy, mass, standard-model settings). I did not
read these for how the word is used.

## Unexpected links
- The released norm's equation is the promoted norm's clock density set to zero, exactly, with torsion and a
  varying norm included (proposal clause (iii)). The stored display was derived on torsion-free solutions of
  constant norm; it holds unchanged because the frame and norm equations are algebraic in the norm.
- The two cosmological predictions are coupled. neutrino.double-prediction-sum-predicted-floor says the series
  cannot relax the cosmological neutrino-mass bound by letting dark energy evolve. The data combination that
  most prefers w != -1 is the one that pushes the neutrino mass sum low under w = -1 (the DES paper quotes
  sum < 0.18 eV at 95 per cent with (w0, wa) free). The series is exposed on both at once: holding w = -1 keeps
  the tight bound against its own floor. Not computed here.
- Dark-matter postulate D (democracy) is the one dark-matter premise tied to a constant Lambda (found by the
  dark-matter attacker, attack-MA.md); it belongs in the exposure list.
- In vacuum the released functional is degenerate on isotropic fields (F = 0, norm free): the same degree-one
  structure in the released scale that the stored result names for the Chern-Simons radion.

## Decisions for Leon
1. Registration (maintainer-only). Adopt the drafted kill condition, note and observation row for
   pred.dark-energy-w-minus-one, and the same sentence in (FS) refutation (a) and Premise (N). Recommendation: yes.
2. Three clauses the five sigma rule leaves open: (a) may each survey use a shared CMB prior (recommend: yes, say
   so; otherwise no present or planned survey can reach five sigma alone on (w0, wa)); (b) frequentist distance or
   Bayesian evidence (recommend: the collaboration's published frequentist distance, with the evidence recorded
   beside it); (c) the region is tied to the two-parameter form, narrower than the stored "at any epoch"
   (recommend: keep the form, add "or an equivalent model-independent exclusion of constant dark-energy density at
   the same significance").
3. Record the exposure by edges (maintainer-only, new assumes edges): the results that present the frozen-point
   functional as the law of gravity carry no assumes edge to (FS), and no result assumes Premise (N). Recommendation:
   add (FS) to the action results that state field equations with matter (at least
   synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part and
   synthesis.frozen-point-field-space-is-the-gtg-pair-and-its-omega-equation-is-the-torsion-equation), so the cone
   shows what the data would take.
4. The plain statement "the series has no fallback for w != -1" on the prediction and in the dark-energy setting
   note (maintainer text; the proposal supplies the citable part). Recommendation: yes.
5. Whether to compute the dynamical Stelle-West family with derivative terms (the literature's quintessence route)
   now, as a pre-registered analysis, or to leave it uncomputed. Recommendation: leave it and say so; computing a
   fallback before a detection weakens the registration, and adopting one after is a fit.
6. Hypothesis (Mat) carries the dust result (matter sees the frame hb^{-1}, not the norm). If matter were coupled
   to the rescaled frame the result changes. It is the stored hypothesis; no action unless Leon prefers the other.
7. Gravity-entanglement prediction (maintainer text): add to pred.gravity-entangles-standard-phase a sentence that
   the prediction concerns the phase only, makes no claim about a mediator and does not treat the effect as a
   test of a quantised gravitational field; add the observation row of 2026-11 (status unchanged; An et al. now
   published 22 October 2026). Its basis is still a working note outside the store; importing the element reading
   as a stored entity is a separate decision.
8. No open-problem entry exists for the dark-energy exposure; the proposal has no extraction.open_problem. Either
   leave it so or add a housekeeping entry.

## Sources (web, read today unless marked)
- DES Collaboration, arXiv:2605.27221 (abstract and tables via fetch).
- DESI Collaboration, DR2 BAO, arXiv:2503.14738; DR2 Lyman-alpha full shape, arXiv:2607.27410.
- Camilleri et al., Supernovae Unite, arXiv:2609.05053.
- Westman and Zlosnik, arXiv:1302.1103 (abstract).
- An et al., Nature Communications 2026, DOI 10.1038/s41467-026-78187-4 (via techno-science.net report).
- Fuchs et al., Science Advances 2024 (ADS record 2024SciA...10K2949F).
- Pedalino et al., arXiv:2507.21211. Xiang et al., arXiv:2601.06608. Braccini, Serafini, Bose, arXiv:2602.19306.
  Bonaldi et al., arXiv:2607.18351.
- Marletto and Vedral, arXiv:2510.19969; Marletto, Oppenheim, Vedral, Wilson, arXiv:2511.07348; Gundhi, Infantino,
  Bassi, arXiv:2604.19696; Aziz and Howl, Nature 646, 813 (2025) (via those papers and a news report).
- From memory, not checked: Westphal et al. 2021 details; Bose et al. 2017 and Marletto-Vedral 2017 parameter
  values; the statement that a single minimally coupled scalar cannot cross w = -1.
