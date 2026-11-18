# Maintainer report: the energy per creation event (run 2026-11-18-leads)

Leon's decision of 18 November 2026, 14:04: adopt the computed mean energy per creation event in the gravitational
floor, in place of the stored convention (3T per event, energy fraction 4Y). Carried out on the store in place.
Nothing was committed or pushed, no agent was spawned, layer 4, check4 and validate_draft were not run. Every number
below was recomputed here (exact brackets in the checks; the decimals quoted are from those brackets).

## Result in one paragraph

The floor is now defined, proved and checked with the mean energy per event: 7.873 T (produced real scalar), 7.890 T
(chiral fermion or vector), 7.889 T (a copy of the Standard Model's content) for the bath (4, 45, 12); energy
fraction (4/3)(E/T) Y, about 10.5 Y; prefactor 9.6e-4 -> 1.23e-3. Every floor rises by 1.273. Thirteen entities were
changed and one number in store/open_problems.yaml. No headline conclusion is lost. Three stated bounds failed at the
new floors and are restated weaker, and one stated equality (the floor at the rescue temperature equals the hot
deposit) no longer holds and is restated as a ratio of 1.27. Layers 1 to 3: 0 errors, 0 warnings.

## The computation (stored in dark-matter.seeding-gravity-floor-dark-towers-temperature)

- Leg weights. In the rate integral of clause (v) of the pair-production theorem the inner integral is W_ij s^2/M^4,
  the measure is E1 E2 dE1 dE2 dcos, and the angular integral of s^2 is (32/3) E1^2 E2^2: each incoming leg is
  weighted by E^3 f(E), independently. Moments: Gamma(k+1) zeta(k+1) T^(k+1) for Bose, (1 - 2^-k) times that for Fermi.
- Mean energy of a leg: 4 zeta(5)/zeta(4) T = 3.8322 T (Bose); (15/16)(24)/((7/8)(6)) = 30/7, so
  (30/7) zeta(5)/zeta(4) T = 4.1060 T (Fermi). Events: 7.6645 T (Bose pair), 8.2119 T (Fermi pair).
- zeta(4) = pi^4/90 (Machin bracket of pi; compared in the check with the partial-sum bracket of zeta(4));
  zeta(5) in (1.0369277, 1.0369278), from the partial sum to 60 terms with the tail between 1/(4 x 61^4) and
  1/(4 x 60^4). zeta(5)/zeta(4) = 0.958057.
- Weights for the bath (4, 45, 12), zero curvature couplings: Bose part (c_j 148 + 20 tau_j)/225, Fermi part
  49 x 45 c_j/4800 = 2205 c_j/4800. Scalar: 168/225 and 2205/4800 (Bose share 0.619). Fermion and vector: 148 c_j/225
  and 2205 c_j/4800 (Bose share 0.589). Copy of the content: 41964/225 and 283 x 2205/4800 (Bose share 0.589). The
  check confirms that the two parts sum to the theorem's printed rationals and that 49/4800 = 3 (7/8)^2/225.
- E/T: 7.872984 (scalar), 7.889576 (fermion, vector, any number of them), 7.889323 (copy). For any bath and
  content 7.66 < E/T < 8.22.
- Energy fraction: (4/3)(E/T) Y, since s/rho = 4/(3T); 10.497 Y (scalar) to 10.519 Y (vector); the proof also gets
  it from the energy equation (same integrand as the yield).
- Prefactor of xi_floor at c = 1, g_d = 16, 6e14 GeV: 9.625149e-4 at 3T -> 1.225073e-3 (scalar), 1.225718e-3
  (fermion, vector), 1.225708e-3 (copy): "1.23e-3", between 1.225 and 1.226e-3 for these, between 1.21 and 1.24e-3
  for any bath (1.2169e-3 Bose end, 1.2381e-3 Fermi end). Ratio to the old prefactor: (E/3T)^(1/4) = 1.2728 to 1.2735.

Note on the brief: it lists nine vectors with the Standard Model's content at 7.889 T. Nine vectors have the single
vector's value, 7.8896 T, which is 7.890 at four figures; the copy is 7.8893 T. Stored accordingly.

## Entities changed

| entity | version | what |
|---|---|---|
| dark-matter.seeding-gravity-floor-dark-towers-temperature | 5 -> 6 | floor defined with the mean energy; mean stated, proved, checked (new function check_mean_energy_per_event); "3T per event", "8Y", 2^(1/4) and the "computed in the review" sentence removed |
| dark-matter.coefficients-floors-they-give-what-gravity | 5 -> 6 | all floor-built numbers; the paragraph on the two energy counts and the review sentence removed |
| dark-matter.stored-asymmetry-charge-not-number | 12 -> 13 | floor and eta' at the floor |
| dark-matter.radiation-audit-what-theorem-closes-what | 9 -> 10 | floor in parts per ten thousand; margin at the floor |
| simulations.imported-mirror | 7 -> 8 | floor; its own check recomputes with the mean energy |
| synthesis.mirror-temperature-measures-deposit-under-r | 2 -> 3 | clause (i), closing sentence, proof of (iii); convention qualifier and review sentence removed |
| synthesis.adiabatic-deposit-modulation-is-a-time-shift | 4 -> 5 | one quoted bound |
| dark-tower-matter.mirrors-composition | 4 -> 5 | quoted present floor and quoted eta' at the floor; clauses (i) to (iii) untouched |
| dark-matter.mirror-share-one-how-fragile | 9 -> 10 | quoted present floor |
| simulations.s3-mirror-cluster | 3 -> 4 | present floor now named in the window clause (see "Stale quotes", item 3) |
| pred.no-dark-radiation | 5 -> 6 | the sentence quoting the floor; kill condition, threshold, status untouched |
| dark-matter.open-channels-their-costs | 6 -> 7 | not in the earlier list: stale floor quotes (see "Stale quotes", item 1) |
| dark-matter.population-count-one-share-half-percent | 7 -> 8 | not in the earlier list: stale floor quote (item 1) |
| store/open_problems.yaml | | op.pre-descent-theory: "below 2.5e-5" -> "below 3.1e-5"; nothing else in the file |

Bookkeeping on each: version + 1; amendment (kind restatement) with the defect; credit entry with source
'maintainer pass of 2026-11-18 (run 2026-11-18-leads)'; extraction note under maintainer_pass_2026_11_18_energy; every
earlier credit, amendment and extraction entry kept. Evidence is named where the entity has a check bearing on the
change (the first six); none for the other seven. Pins between the changed entities were moved to the new versions.
Coverage files updated for the six with checks, with a dated line saying the new numbers were not judged again.

## Numbers, old -> new

Common inputs: Y = c T^3/(3 kappa_s M_P^3), kappa_s = 145.26, M_P = 2.435e18 GeV, T = 6e14 GeV, g* = 100;
xi^4 = (4/3)(E/T) Y g*/g_d.

| where | quantity | old | new | computation |
|---|---|---|---|---|
| seeding | energy per event | 3 T (convention) | 7.873 T, 7.890 T, 7.889 T | above |
| seeding | energy fraction | 4 Y | (4/3)(E/T) Y, 10.49 Y to 10.52 Y | 4/3 x 7.873, 4/3 x 7.890 |
| seeding | prefactor of xi_floor | 9.6e-4 | 1.23e-3 (1.2251 to 1.2257e-3) | 9.625149e-4 x (E/3T)^(1/4) |
| coefficients (i) | nine vectors' floor, g_d = 18 | 6.4e-4 | 8.1e-4 (8.1183e-4) | c = 0.21649, E = 7.8896 T |
| coefficients (ii) | mirror's floor, g_d = 106.75 | 5.2e-4 | 6.6e-4 (6.6206e-4) | c = 0.56793, E = 7.8893 T |
| coefficients (ii) | eta' at the floor | 4.4 (4.36) | 2.1 (2.1121) | 6.12938e-10/(6.6206e-4)^3 |
| coefficients (ii) | coefficient with eta' = 1 at the floor | about 4, 7 times the mirror's | about 1.5 (between 1.539 and 1.54), 2.7 times | (8.4945e-4/7.6265e-4)^4 = 1.539 |
| coefficients (iii) | floor at the rescue temperature | 4e-3, equal to the hot deposit | 5.4e-3 (5.405e-3), 1.27 times the hot deposit 4.2e-3 (4.244e-3) | xi^4 = (4/3)(7.8893)(8.6608e-11)(100/106.75) |
| coefficients (iv) | mirror's Delta N_eff at the floor | 5.4e-13, below 1e-12 | 1.4e-12 (1.4308e-12), below 2e-12 | 7.4472 x (6.6206e-4)^4 |
| coefficients (iv) | nine vectors' at their floor | 6.5e-12, below 1e-11 | 1.7e-11 (1.7213e-11), below 2e-11 | 2.2016 x 18 x (8.1183e-4)^4 |
| coefficients lay | "about two thousand times colder" | 1923 | "about fifteen hundred" (1510) | 1/6.6206e-4 |
| stored-asymmetry (iii) | floor; eta' at the floor | 5.2e-4; 4.4 | 6.6e-4; 2.1 | as above |
| radiation-audit | floor in words | five to six parts in ten thousand | seven to eight | 6.6e-4, 8.1e-4 |
| radiation-audit | mirror channel's margin at the floor | 5.5138e11 | 2.0967e11 (still "eleven orders") | 0.3/1.4308e-12 |
| imported-mirror | floor; eta' in its check | 5.2e-4; 4.36 | 6.6e-4; 2.11 | its own bracket, E/T in (7.889, 7.890) |
| mirror-temperature (i) | mirror's floor under (R), at 1e13 GeV | below 2.5e-5 | below 3.1e-5 (3.071e-5; 3.075e-5 from the figure 6.63e-4) | 6.6206e-4 x (1/60)^(3/4) |
| mirror-temperature (i) | below the helium edge 3e-3 by | more than 120 | more than 97 (97.5 to 97.7) | 3e-3/3.075e-5 |
| mirror-temperature (i) | nine vectors' floor under (R) | below 3.0e-5, 101 to 102 times below | below 3.8e-5 (3.766e-5), 79 to 80 times | 8.12e-4 x (1/60)^(3/4) |
| mirror-temperature, closing | share of xi^4 at the helium edge without (R) | below 9.1e-4 | below 2.4e-3 (2.385e-3) | (6.63e-4/3e-3)^4 |
| mirror-temperature, proof (iii) | the same share under (R) | below 1e-8 | below 2e-8 (1.098e-8 to 1.104e-8) | (3.07e-5/3e-3)^4 |
| mirror-temperature technical | "about one part in a thousand" | | "within a quarter of a percent" | 2.385e-3 < 1/400 |
| adiabatic-deposit | floor neglected in the deposit law | below 2.5e-5 | below 3.1e-5 | from mirror-temperature (i) |
| mirrors-composition | quoted present floor; quoted eta' | 5.2e-4; 4.4 | 6.6e-4; 2.1 | quotes |
| mirror-share-one-how-fragile | quoted present floor | 5.2e-4 | 6.6e-4 | quote |
| s3-mirror-cluster | present floor | (5.2e-4 in the version-3 record only) | 6.6e-4, in the formal level | quote |
| pred.no-dark-radiation | floor in its sentence | 5.2e-4, eleven orders | 6.6e-4, eleven orders | 2.1e11 |
| open-channels-their-costs | floor in words; at a coefficient of ten | about three parts in ten thousand; 1.1e-3 | about seven; 1.4e-3 (1.356e-3) | 1.2257e-3 x 10^(1/4) x (16/106.75)^(1/4) |
| population-count | nine vectors' floor in words | about three and a half parts in ten thousand | about eight | 8.1e-4 |
| open_problems.yaml | op.pre-descent-theory | below 2.5e-5 | below 3.1e-5 | from mirror-temperature (i) |

Unchanged, as the brief says (they count events or quanta, not energy), and verified by running their checks
untouched: the coefficients, the yield 1.95e-14 (3.9e-14 quanta), the shortfall 4442 (2221), the rescue temperature
9.9e15 GeV (16.4 times the ceiling), c* and the margins of synthesis.seeding-remainder-excludes-perturbative-pati-salam,
synthesis.untuned-fit-caps-lightest-heavy-neutrino, synthesis.pati-salam-monopoles-bound-descent-history. Also
unchanged: the hot deposit (4.2e-3, eta' 0.008 there, 1e-8 bound), the crossover xi = 8.5e-4, the ceiling-range factor,
"at least 1e7 times ours", "eight orders or more across the interval".

One quantity in a quanta-counting clause does depend on the energy: the floor at the rescue temperature in
coefficients (iii) (item 2 below).

## Conclusions that changed (item 4 of the brief)

1. coefficients (iv), two bounds fail. "Below 1e-12" (mirror) and "below 1e-11" (nine vectors) are false at the
   new floors (1.43e-12, 1.72e-11). Restated as below 2e-12 and below 2e-11, with the values. "Far below any
   measurement" stands.
2. coefficients (iii), an equality is lost. The statement had the floor at the rescue temperature equal to the
   hot-deposit value, "as it must be". That held only because both sides took 3T per unit. Now the floor there is
   5.4e-3 and the hot deposit, which takes 3T per unit of baryon number by its own estimate and was not touched, is
   4.2e-3: ratio (E/3T)^(1/4) = 1.27. Restated at all levels with the reason. The mirror-temperature proof referred to
   "the identity of" that clause for the hot deposit; it now points to the stored-asymmetry proposition's value.
3. mirror-temperature, one bound in the proof of (iii) fails. Under (R) the floor's share of xi^4 at the helium
   edge is 1.1e-8, not below 1e-8; restated as below 2e-8 (also in the formal closing sentence). "The floor drops
   out" under (R) stands.
4. mirror-temperature (i) and the closing sentence: every bound weakened by 1.27 in xi (2.6 in xi^4), listed in the
   table. No inequality between the floor and the helium edge flips (97 times below under (R); the floor at the
   ceiling is 4.5 times below it).
5. eta' at the mirror's floor is 2.1 and not 4.4. It does not cross one: the floor 6.6e-4 is still below the
   crossover 8.5e-4, and the mirror is still charge-dominated at the floor. The margin in the coefficient shrinks
   from a factor 7 to a factor 2.7.
6. radiation-audit and pred.no-dark-radiation: still eleven orders at the floor (2.1e11); nothing changes in words
   except the floor.

Nothing was strengthened.

## Stale quotes found (grep of the whole store, notes excluded)

1. Two entities outside the earlier pass's list still carried floors from the first imported coefficients, in
   words: dark-matter.open-channels-their-costs ("about three parts in ten thousand", "1.1e-3 even for a coefficient
   of ten", formal and technical) and dark-matter.population-count-one-share-half-percent ("about three and a half
   parts in ten thousand" for nine vectors, clause (iii)). Corrected to the present values with bookkeeping
   (6 -> 7, 7 -> 8). Their source_formal fields (deposited statements) were left.
2. dark-matter.open-channels-their-costs also says burning reheats the mirror's plasma "by 3.0 to 3.2" near the
   floor. That is the deposited paper's figure at xi = 2.8 to 3.2e-4 (eta' 19 to 26). I reproduced it off the record
   from the formulas in the stored-asymmetry proof (floating point: 2.99 and 3.18), and the same formulas at
   eta' = 2.11 give about 1.9. I did not store 1.9 (no check of it exists); the sentence now says the factor is the
   one at xi = 2.8 to 3.2e-4 and is not recomputed at the present floor, the same treatment the neutron-rich
   composition received.
3. simulations.s3-mirror-cluster quoted the present floor only inside its version-3 amendment record. I did not
   rewrite that record; the formal level now names the present floor (6.6e-4) and the new amendment says the record
   of version 3 gives the value of that pass. If a number in a model specification is unwanted, drop the four words
   and keep the note.
4. Other hits, all listed and left: records of earlier versions in front matter (amendment defects, extraction
   notes, dated judge lines in coverage files, source_formal); "3T" where it is the hot deposit's own estimate or the
   deposited paper's convention named as such; unrelated matches (the remainder 4.364, X = 5(B - L) - 4Y, 2^(1/4) in a
   neutrino result, "120" family matrices).
5. Notes (excluded by the brief) still quote the deposited paper's figures "at the floor":
   note.dark-matter.setting-dark-stable-counted, note.simulations.setting-composition-recombination,
   note.dark-matter.setting-successor-problems, note.dark-matter.setting-predictions-collected,
   note.dark-matter.halo-built-collisionless-sheets-cold-dark ("of order 1e-4"). Not touched.
6. Not resolvable here: the series script verify_T14.py (listed in checked_by of four of these entities) still
   evaluates 9.6e-4 at 3T per event with the first coefficients; the seeding proof now says so. The T14 paper has the
   same. documents/ and site/ are generated and show the old numbers until rebuilt.

## Checks

- Every changed check passes under colony/runcheck.py: seeding (6 functions, one new), coefficients (4),
  stored-asymmetry (4), radiation-audit (4), simulations.imported-mirror (4), mirror-temperature (1). The checks of
  the Pati-Salam, untuned-fit, monopole, open-channels and population-count entities pass untouched.
- Exact arithmetic only (Fractions, integer powers, Machin bracket of pi, partial-sum bracket of zeta(5) with exact
  tail bounds). The seeding export xi8_bracket(c, gd, energy, T) now takes the bracket of E/T as its third argument,
  so a caller that omits it raises; new exports ZETA5, rate_parts, event_energy, EVENT_ENERGY; the coefficients
  export cosmo() gains floor8_nine, energy, energy_nine. simulations.imported-mirror does not cite the seeding
  proposition, so its check recomputes E/T itself from typed parts (its stored practice for the coefficients).
- Perturbation test (the validator's sampling, literal + 1 at eight evenly spaced positions, on copies in /tmp, 12
  changed functions): none survives all, none more than three of eight. I replaced one-sided brackets by rounding
  pins in the coefficients, seeding and mirror-temperature checks to get there (before that, three functions had
  five or six survivors).
- `python -m tp check --store store --layers 1-3 --keep-going --author leon`, once, after the last edit:
  0 errors, 0 warnings, 122 information findings (I126 x 1, I213 x 120, I305 x 1: "this change touches 14 entities;
  27 claims and 7 documents depend on them and need re-confirmation").

## Left for the orchestrator

- Stale pins in entities I did not touch (24): dark-tower-matter.mirrors-temperature-p2 (seeding 5 -> 6,
  stored-asymmetry 12 -> 13); synthesis.seeding-remainder-excludes-perturbative-pati-salam (seeding 5 -> 6,
  coefficients 5 -> 6, population-count 7 -> 8; it uses only the yield); dark-matter.mirror-share-assembled
  (mirror-share 9 -> 10, population-count 7 -> 8, stored-asymmetry 12 -> 13); simulations.halo-shapes and
  simulations.merger (imported-mirror 7 -> 8, s3-mirror-cluster 3 -> 4);
  synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them (mirrors-composition 4 -> 5, stored-asymmetry
  12 -> 13); synthesis.conditional-inheritance-of-b-minus-l-and-the-conversion-coefficient-as-a-gram-ratio
  (mirrors-composition 4 -> 5); synthesis.dark-to-baryon-total-uses-r1-r2-and-d-only-as-mass-per-unit-ball
  (population-count 7 -> 8, mirror-share 9 -> 10); dark-matter.total-function-thickness (population-count 7 -> 8);
  dark-tower-matter.r1-has-no-mechanism-odd-towers (mirror-share 9 -> 10);
  synthesis.cold-mirror-needs-non-equilibrium-descent (open-channels 6 -> 7); and stored-asymmetry 12 -> 13 in
  synthesis.no-rule-p2-licenses-gives-the-thickness-of-r3,
  synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping,
  synthesis.tower-charge-sector-label-temperature-not, pred.no-indirect-dark-signals. None of these quotes a changed
  number in its body.
- The composition at the present floor is still not computed (scripts not in the lab). Off the record: the
  Fermi-energy ratio of mirrors-composition (i) scales as xi^-4, which puts it near 2.7 at 6.6e-4 (84 at 2.8e-4, 49 at
  3.2e-4), so degeneracy at seeding is marginal there, less clear than at 5.2e-4 (where it was near 7).
- The pair-production theorem's check exports nothing; the E^3 leg weight is read from its proof. If an export of
  the Bose and Fermi parts is added there, the seeding check could read them in place of recomputing the closed form.
- The theorem's Reading still says the floors rise "by a factor between 1.6 and 1.8" from the corrected
  coefficients; that is the coefficient effect alone and remains true, but the floors have now risen by a further
  1.27 from the energy. Not my entity; no change made.

## For the main session's memory (where learned)

- Decision of 18 November 2026, 14:04: the gravitational floor uses the computed mean energy per creation event,
  not 3T per event (MAINTAINER-energy.md of this run). Stored: prefactor 1.23e-3; mirror's floor 6.6e-4, nine
  vectors' 8.1e-4, eta' at the mirror's floor 2.1 (this pass).
- The hot deposit keeps its own estimate of 3T per unit of baryon number, so it no longer coincides with the floor
  at the rescue temperature (this pass; a decision may be wanted on whether the hot deposit should follow).

## Follow-up: composition at the present floor

Same day, after the orchestrator ran the papers suite's two scripts with 5.2e-4, 6.6e-4 and 8.1e-4 added to their
grids (work/housekeeping/MIR_rerun_extended_grid_output.txt, CHECK_COS_rerun_extended_grid_output.txt). I read both
outputs and took every number below from them. No version was raised a second time: in each entity the amendment,
the credit role and the extraction note written in this pass were extended. No check was touched (the scripts are not
in the store; the coverage files of mirrors-composition, stored-asymmetry and open-channels say so).

Figures read from the outputs (printed floor 2.8e-4 / 3.2e-4 -> present floor 6.6e-4):

| quantity | 2.8e-4 / 3.2e-4 | 6.6e-4 | also 5.2e-4, 8.1e-4 |
|---|---|---|---|
| Fermi energy over thermal deposit (CHECK_COS, rhoF/rho_th) | 84 / 49 | 2.7 | 7.1, 1.2 (0.99 at 8.5e-4) |
| mu/T' at seeding; mu_q/T' at T' near 0.4 GeV (CHECK_COS) | 23.4 / 17.8 (both) | 3.5; 3.7 | 6.3; 6.4 and 2.0; 2.2 |
| neutron fraction, L/B = -51/28 (MIR E2) | 1.000 / 0.999 | 0.957 (T'_f 18 MeV, n/p 22.3) | 0.984, 0.916 |
| neutron fraction, L = 0 | 0.965 / 0.954 | 0.832 (T'_f 111 MeV, n/p 4.96) | 0.887, 0.771 |
| neutron fraction, L_e/B = +0.875 (outside the clause) | 0.415 / 0.406 | 0.324 | 0.360, 0.312 |
| thermal-rate table (MIR E1): eta' late; mu_q/T' at freeze-out | 27.8 / 18.6; 10 / 8.6 | 2.12; 1.76 | 4.34; 4.9 and 1.15; 1.09 |
| helium branch (MIR E3): T'_D; eta'(T'_D); n_B; reheat | 0.246 / 0.234 MeV; 27.9 / 18.7; 1.32e31 / 7.57e30; 3.23 / 2.96 | 0.185 MeV; 2.13; 4.26e29; 1.86 | reheat 2.16, 1.64 |

These agree with the orchestrator's reading. Two remarks on it: the stored "18 to 23" is the CHECK_COS quantity
(23.4, 17.8), so the comparable present figure is 3.5 to 3.7; the MIR thermal-rate table gives a different, smaller
ratio at its own freeze-out temperature (10 and 8.6 before, 1.76 now), recorded in the proof text. And my off-record
estimate of the reheat in the first pass (about 1.9) is confirmed at 1.86.

What was changed:

1. dark-tower-matter.mirrors-composition (stays 5), clause (i) at all four levels and the proof text. The figures at
   2.8 to 3.2e-4 are kept. Added at 6.6e-4: still neutron-rich for L <= 0, 96 percent neutrons (L/B = -51/28) and 83
   percent (L = 0); Fermi energy over thermal deposit 2.7; quark chemical potential 3.5 times the temperature at
   seeding and 3.7 at T' near 0.4 GeV; beta equilibrium still lasts into the hadron phase (freeze-out at 18 and 111
   MeV). "Charge-dominated and degenerate from the moment it is seeded" is kept for the lower values and stated as
   holding at the present floor only in the weaker form (the charge dominates by a factor near three, not fifty or
   more). The proof text records the run (one line changed per script, 24 checks, the comparison rows at 5.2e-4 and
   8.1e-4, the helium-branch line with the reheat). The composition after decay and capture is still not computed.
   The entity does not speak of the nine vectors' floor, so 8.1e-4 appears only as a comparison row in the proof.
2. simulations.imported-mirror (8): formal, technical, lay, one-liner and my extraction note.
   simulations.s3-mirror-cluster (4): formal and technical (neutron-rich at both values, with the two ranges).
   dark-matter.mirror-share-one-how-fragile (10): caveat of (i) and technical.
   dark-matter.stored-asymmetry-charge-not-number (13): clause (i), the caveat, technical, lay, and the proof text.
   dark-matter.open-channels-their-costs (7): the reheat, "3.0 to 3.2 at 2.8 to 3.2e-4 and 1.9 at the present floor".

Conclusions that leaned on "96 to 100 percent", on the degeneracy or on a reheat near 3:

- stored-asymmetry (i): the argument that the hot-plasma conversion coefficient cannot be assumed for the mirror
  cited a plasma degenerate from seeding. At the present floor the plasma is still degenerate there, moderately
  (mu/T' = 3.5 against 18 to 23). Restated with that figure; the conclusion ("not shown") is unchanged, the support
  for it is weaker.
- stored-asymmetry, caveat: "the burning branch is not the floor's composition" now rests on a computed value
  (83 to 96 percent neutrons) instead of on the floor lying below the helium interval. Stands.
- mirror-share-one-how-fragile: "the half-percent bracket does not cover the floor" stands (neither branch
  describes an 83 to 96 percent neutron endpoint).
- open-channels: "the bound is met on either reading by eight orders or more" does not need a reheat near 3. With
  the reheat, 7.447 (6.6e-4 x 1.86)^4 = 1.7e-11 at the present floor, ten orders below the cap (decimal, in the note,
  not in a check).
- stored-asymmetry proof: its nucleosynthesis brackets (bottleneck, density, reheating factor, "a baryon density
  eleven orders above ours") were evaluated at 2.8 to 3.2e-4. The proof now says so and gives the rerun's values at
  6.6e-4 (0.185 MeV, eta' 2.13, density 18 to 31 times lower, reheat 1.86). I did not restate "eleven orders" at the
  present floor: the comparison density of our sector is not in the outputs.
- Not done as asked, with the reason: the reheat "1.6 at the nine vectors' floor" is not quoted in open-channels.
  The script's row at 8.1e-4 is the mirror's content placed at that ratio; 8.1e-4 is the floor of a nine-vector
  content, which has no copied nucleosynthesis, and it is not a floor of the mirror. The figure (1.64) is in the
  mirrors-composition proof text as a comparison row and in the open-channels note.

Third grep ("recomputed", "96" near "neutron", "degenerate", "reheat"), notes excluded: no statement body still says
"not recomputed at the present floor". Left untouched, for the orchestrator:

- store/open_problems.yaml, op.matter-asymmetry-origin, attack item: "the stored computation finds the mirror's
  plasma degenerate from the moment it is seeded at the floor". A wording, not a quoted number, so outside what I may
  change in that file. At the present floor it should read "moderately degenerate (mu/T' = 3.5)".
- synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them ("the mirror tower, whose plasma the cited
  Computation finds degenerate") and
  synthesis.conditional-inheritance-of-b-minus-l-and-the-conversion-coefficient-as-a-gram-ratio ("whose plasma the
  cited Computation finds degenerate, so that (T) fails there"). Not my entities. The second draws a conclusion from
  the degeneracy; whether (T) fails at mu/T' = 3.5 as it does at 18 to 23 is for its owner to state.
- Notes that carry the printed-floor composition or reheat: note.dark-matter.setting-dark-stable-counted,
  note.simulations.setting-composition-recombination. (Other notes matching "neutron" concern the dipole bound or
  neutron-star mergers.)
- dark-matter.mirror-share-one-how-fragile/coverage.yaml says the neutron-rich composition at the floor "is not
  computed" by that check: still true, left.

Checks: none changed. runcheck on mirrors-composition's check passes (1 function). Layers 1 to 3, run once after the
last edit: 0 errors, 0 warnings, 122 information findings.

For the main session's memory (where learned): at the mirror's present floor 6.6e-4 the supplementary scripts give
a neutron-rich mirror for L <= 0 (83 to 96 percent neutrons), only moderately degenerate (Fermi energy over thermal
deposit 2.7), and a helium-branch reheat of 1.86 (rerun outputs in this run's work/housekeeping folder).
