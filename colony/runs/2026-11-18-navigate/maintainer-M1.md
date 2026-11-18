# Maintainer report M1, run 2026-11-18-navigate

Restatement of the four direct users of the production rate, and of the dependants that quote their
numbers, after Leon's decision D3 of 18 November 2026. Nothing was committed or pushed. No agent was spawned.
Layer 4, check4.py and validate_draft were not run.

## Result in one paragraph

All four are restated with the coefficients of clause (v) of
synthesis.gravitational-pair-production-from-the-operator-source-at-first-order. No headline conclusion of the
four is lost, but several stated bounds were false at the new coefficients and are weakened, every margin
shrinks, and one dependant's conclusion (the mirror ends neutron-rich at the gravitational floor) is no longer
established at the present floor because the scripts that computed it are not in the lab. Nine dependants were
changed. Layers 1 to 3: 0 errors, 0 warnings.

## Coefficients used (exact, then rounded)

alpha/pi^3 from the closed form (1/17280)[(c_j(N_s + 12 N_v) + 5 tau_j N_s)/225 + 49 c_j N_w/4800] at (4, 45, 12),
recomputed inside each check and compared with the printed rationals:

| content | exact | value |
|---|---|---|
| real scalar | 5789 pi^3/82944000 | 2.16405e-3 |
| chiral fermion | 16087 pi^3/82944000 | 6.01367e-3 |
| real massless vector | 16087 pi^3/20736000 | 2.40547e-2 |
| Standard-Model content | 1519247 pi^3/82944000 | 0.567928 |
| nine vectors | 9 x 16087 pi^3/20736000 | 0.216492 |
| 22 vectors (odd towers) | 22 x 16087 pi^3/20736000 | 0.529203 |
| four Standard-Model contents | 1519247 pi^3/20736000 | 2.27171 |

Note on the brief: it gives the scalar as 2.1640e-3. The value is 2.16405e-3, which rounds to 2.1641e-3 at five
figures; I wrote 2.164e-3. pi is never a decimal in the checks: the two dark-matter checks use their Machin
bracket, the two synthesis checks use 333/106 < pi < 355/113 at the end that weakens each statement (their stored
practice), and the docstrings say so.

The new theorem's check exports nothing, so the checks cannot read the coefficients from it. Each check calls
premise() for it and recomputes the closed form itself. If the orchestrator adds an EXPORTS to that check, the
four could read from it instead.

## The four

### 1. dark-matter.seeding-gravity-floor-dark-towers-temperature, version 4 -> 5

No formula and no number changed (the statement is symbolic in c; its check holds no coefficient).
- The rate is cited as Theorem (v) (Fact for the published values), with the (OS) sentence once in the formal level.
- Gamma counts creation events of two quanta. Y is now called the yield of events, and the number of quanta is 2Y.
- The floor keeps the stored energy convention (3T per event, energy fraction 4Y). The other count (3T for each of
  the two quanta: 8Y, ratio larger by 2^(1/4) = 1.189) is stated beside it, with "the stated value is a floor on
  either count".
- "graviton-mediated production" became "gravitational pair production" where the rate is introduced (wording
  that goes with the new citation; also in entity 3's proof and entity 2's technical level and one-liner).
- Check: premise() for the theorem in the two functions that take the rate; new export QUANTA_PER_EVENT = 2; the
  identities 3 x (2/45) x 30 = 4, the 8Y count, and 1.189^4 < 2 < 1.190^4.

Conclusions that changed: none. One decision is open (see "Could not decide", item 1).

### 2. dark-matter.coefficients-floors-they-give-what-gravity, version 4 -> 5

All numbers follow from xi^4 = 4Y g*/g_d, Y = c T^3/(3 kappa_s M_P^3), T = 6e14 GeV, kappa_s = 145.26, M_P = 2.435e18 GeV,
which give xi = 9.625e-4 c^(1/4) (16/g_d)^(1/4) and Y = 3.4333e-14 c.

| clause | quantity | old | new | computation |
|---|---|---|---|---|
| (i) | c, nine vectors | 0.021 | 0.2165 | 9 x 2.4055e-2 |
| (i) | xi_floor, nine vectors, g_d = 18 | 3.5e-4 | 6.4e-4 (6.375e-4) | 9.625e-4 x 0.2165^(1/4) x (16/18)^(1/4) |
| (ii) | c, mirror | 0.053 to 0.078 | 0.568 | 1519247 pi^3/82944000; bracket closed, each fermion weighted once |
| (ii) | xi_floor, mirror, g_d = 106.75 | 2.8 to 3.2e-4 | 5.2e-4 (5.199e-4) | 9.625e-4 x 0.568^(1/4) x (16/106.75)^(1/4) |
| (ii) | eta' at the floor | 19 to 26 | 4.4 (4.362) | 6.129e-10/(5.199e-4)^3 |
| (ii) | eta' = 1 at c about 4 | unchanged | unchanged; now 7 times the mirror's c | 4/0.568 = 7.04 |
| (iii) | yield Y at the ceiling | 1.8 to 2.7e-15 | 1.95e-14 events | 3.4333e-14 x 0.568 |
| (iii) | shortfall against 8.7e-11 | 3 to 5e4 | 4.4e3 (2.2e3 against the 2Y quanta) | 8.661e-11/1.950e-14 = 4442 |
| (iii) | rescue temperature | 31.9 to 36.2 x ceiling, 1.9 to 2.2e16 GeV | 16.4 x ceiling, 9.9e15 GeV | 4442^(1/3) = 16.44 |
| (iii) | floor at rescue = hot deposit | 4e-3 | unchanged | independent of c |
| (iv) | mirror Delta N_eff at the floor | below 1e-13 | 5.4e-13, below 1e-12 | 7.447 x (5.199e-4)^4 |
| (iv) | mirror at the hot deposit | below 1e-8 | unchanged | independent of c |
| (iv) | nine vectors at their floor | below 1e-12 | 6.5e-12, below 1e-11 | 2.202 x 18 x (6.375e-4)^4 |
| lay | floor "a few thousand times colder" | | "about two thousand times colder" | 1/5.2e-4 = 1923 |
| lay | shortfall "tens of thousands" | | "a few thousand" | 4442 |

Added sentence (formal, technical, proof, check): on the two-quanta energy count of entity 1 every xi_floor^4
doubles, so eta' at the mirror's floor is 2.6 and the two radiation values are 1.1e-12 and 1.3e-11.

Conclusions that changed:
- The two bounds of (iv) at the floors, below 1e-13 and below 1e-12, are false at the new coefficients. They are
  restated one order weaker. On the two-quanta energy count even the new round bounds are exceeded (1.1e-12,
  1.3e-11), which the statement says. "Far too small to detect" stands.
- The shortfall of (iii) is one order smaller (thousands, not tens of thousands). "Gravity heats the dark towers
  and does not populate them" stands.
- eta' at the floor is 4.4, not 19 to 26. It is still above one (charge-dominated), by a factor 7 in c instead of
  about 50 to 75.
- source_formal (the deposited statement) was left as it was.

### 3. synthesis.seeding-remainder-excludes-perturbative-pati-salam, version 2 -> 3

Unchanged conditions on c: A^(1/4) = 1.217e12 GeV, c* = 13.49, c > 63.7.

| quantity | old | new | computation |
|---|---|---|---|
| c* in vector species | about 5900 | about 560 (561.0) | 13.4949/2.40547e-2 |
| c* in Standard-Model contents | not stated | more than 23 (23.76) | 13.4949/0.567928 |
| c, odd towers' 22 vectors | 0.051 | 0.529 | table above |
| c, four Standard-Model contents | 0.312 | 2.27 | table above |
| seeding temperature over the cap, vectors | above 4.0 (4.04) | above 2.2 (2.247) | (13.4949/0.5292)^(1/4) |
| the same, four contents | above 2.5 (2.56) | above 1.5 (1.561) | (13.4949/2.2717)^(1/4) |
| T_desc at the largest content | above 1.36e12 GeV at c <= 0.312 | above 8.3e11 GeV at c <= 2.28 | 1.217e12/(2 x 2.28)^(1/4) = 8.328e11 |
| f_J needed | above 32 | above 19.6 (19.62) | 8.338e11/4.25e10 |
| m_D needed, cap 5.2 GeV | above 8.2 GeV | above 6.4 GeV (6.42) | (49.4 meV x 8.338e11 GeV)^(1/2) |
| tolerance in v_R | up to 2.5 | up to 1.5 (1.56) | same ratio as the margin |
| (iii) threshold "any c >= ..." | 0.051 | 0.529 | the vectors' c |
| (iii) at the ceiling, (M_3/660)^4 against A/(2c) at the vectors' c | smaller, by 30 in c | smaller, by 2.9 in c | 7.05e47 against 2.07e48 |

The factor 2 in c T^4 >= A/2 is now the two quanta of each event, exact, where it was "the yield bracket of the
imported rate". The requirement is unchanged in form.

Conclusions that changed:
- The exclusion of (i) and (ii) stands at every content considered, with margins 2.2 and 1.5 where 4.0 and 2.5
  stood. The Dirac mass needed, 6.4 GeV, is now 23 percent above the perturbative cap 5.2 GeV (it was 58 percent).
- The lay sentence "cannot all hold for any plausible amount of hidden matter" is weakened to "for the hidden
  matter the series considers": the threshold is the equivalent of 24 Standard-Model contents against at most 4,
  where it was about 170.
- Clause (iii): the caveat that the factor-66 clause holds only at the common low scale is now true for the
  vectors alone. At c = 2.27 the inequality reverses ((M_3/660)^4 = 6.29e47 > A/(2c) = 4.83e47), so for four
  Standard-Model contents the signpost is met with the factor 66 on both readings. The crossover lies between
  c = 1.5 and 1.8. This enlarges the surviving branch, so it is stated in the formal and technical levels and
  the proof, and checked.
- Proof parenthesis on T14's signpost: none of the contents has c <= 0.14 any more, so "above 2e12 GeV" is said to
  belong to the first imported coefficients (the form gives under 1.44e12 GeV at c >= 0.529).

### 4. synthesis.untuned-fit-caps-lightest-heavy-neutrino, version 1 -> 2

Unchanged: alpha < 7.3e8 GeV, the factor 26, c > 3.9e12, "more than 1400-fold for c <= 1", the tuned rows.

| quantity | old | new | computation |
|---|---|---|---|
| contents with c <= 1 | "several hundred vector species" | 41 vector species; one Standard-Model content (0.568); the 22 vectors (0.529) | 41 x 0.024055 = 0.986, 42 x 0.024052 = 1.010 |
| margin at four Standard-Model contents (c = 2.27) | covered by "c <= 1" | more than 1100-fold (1145) | (A/(2 x 2.272))^(1/4)/7.29e8 |

The factor 2 on the yield is the two quanta of each event, as in entity 3.

Conclusions that changed: none in substance. The stated margin for c <= 1 no longer covers the largest content
the companion result considers, so its margin (1100-fold) is added.

## Dependants

Pins: in the dependants I edited, I moved the pins to the entities restated in this pass, because the edit was
the re-check. All other stale pins are left for the orchestrator (list below).

| entity | outcome |
|---|---|
| dark-matter.stored-asymmetry-charge-not-number | changed, 11 -> 12 (restatement): yield 1.8 to 2.7e-15 -> 3.9e-14 quanta (1.95e-14 events); "more than four orders too few" -> "more than three" (ratio 2221 counting every quantum); floor 2.8 to 3.2e-4 -> 5.2e-4; eta' at the floor 19 to 26 -> 4.4; degeneracy and neutron fraction worded as computed at xi = 2.8 to 3.2e-4; check and coverage updated |
| dark-tower-matter.mirrors-composition | changed, 3 -> 4 (restatement): clause (i) stated at xi = 2.8 to 3.2e-4, where it was computed, and marked as not recomputed at 5.2e-4; quoted floor and eta' corrected; no number of (i) to (iii) changed |
| dark-matter.radiation-audit-what-theorem-closes-what | changed, 8 -> 9 (restatement): mirror channel margin at the floor twelve orders -> eleven (4.02e12 -> 5.51e11); floor "a few parts in ten thousand" -> "about five to six"; check coefficient 0.07786 -> 1519247 pi^3/82944000 |
| simulations.imported-mirror | changed, 6 -> 7 (restatement): floor 2.8 to 3.2e-4 -> 5.2e-4 at three levels and in the proof text; neutron-rich composition stated at T14's printed floor; check recomputed (eta' at the floor 19 to 26 -> 4.36) |
| synthesis.mirror-temperature-measures-deposit-under-r | changed, 1 -> 2 (restatement): under (R) the mirror's floor below 1.5e-5 -> 2.5e-5, 200 -> 120 times below the helium edge; nine vectors below 1.7e-5 -> 3.0e-5, 184 to 185 -> 101 to 102 times; without (R) 1.3e-4 -> 9.1e-4 of xi^4 at the helium edge ("one part in ten thousand" -> "one part in a thousand"); check now compares its two floor figures with the coefficients export |
| synthesis.adiabatic-deposit-modulation-is-a-time-shift | changed, 3 -> 4 (restatement): the quoted floor bound 1.5e-5 -> 2.5e-5, formal level and proof; nothing else |
| synthesis.pati-salam-monopoles-bound-descent-history | changed, 1 -> 2 (restatement): clause (iv) c = 0.312 -> c <= 2.28; T_d > 1.36e12 GeV -> 8.3e11 GeV; 32 v_R -> 20 v_R; "about 3e9 vector species" -> "about 3e8"; conclusion unchanged (still more than 40 times the threshold 2.0e10 GeV) |
| pred.no-dark-radiation | changed, 4 -> 5: the sentence saying the rate is flagged and pointing to the open problem is replaced by one saying the rate is derived in the store with corrected coefficients (floor 5.2e-4, eleven orders at the floor); kill condition, threshold and status untouched |
| pred.no-indirect-dark-signals | changed, 5 -> 6: the sentence on "graviton exchange" now says the pair-to-pair transition and its rate are derived in the store from the operator source (clauses (ii), (v)); kill condition, threshold and status untouched |
| pred.dimmed-evaporation-bursts | not affected: its sentence concerns emission into the helicity-2 channels (the term g of the burst baseline), which the new theorem does not settle and the open problem still lists |
| dark-tower-matter.mirrors-temperature-p2 | cites only (stale pins: seeding@4, stored-asymmetry@11) |
| dark-matter.mirror-share-assembled | cites only (stale pin: stored-asymmetry@11) |
| synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them | cites only (stale pins: stored-asymmetry@11, mirrors-composition@3) |
| synthesis.conditional-inheritance-of-b-minus-l-and-the-conversion-coefficient-as-a-gram-ratio | cites only (stale pin: mirrors-composition@3). One clause in its "not shown" list says the cited Computation finds the mirror's plasma degenerate; that finding is now stated at xi = 2.8 to 3.2e-4. For the pin review |
| synthesis.no-rule-p2-licenses-gives-the-thickness-of-r3 | cites only (stale pin: stored-asymmetry@11) |
| synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping | cites only (stale pin: stored-asymmetry@11) |
| synthesis.tower-charge-sector-label-temperature-not | cites only (stale pin: stored-asymmetry@11) |
| synthesis.holographic-thermal-fluctuations-fall-short-in-the-descent-window | cites only: quotes 7.3e8 GeV, unchanged (stale pin: untuned-fit@1) |
| synthesis.pati-salam-chain-defects-cannot-source-spectrum | cites only: quotes 7.3e8 GeV, unchanged (stale pin: untuned-fit@1) |
| simulations.halo-shapes | cites only (stale pin: imported-mirror@6) |
| simulations.merger | cites only (stale pin: imported-mirror@6) |
| synthesis.cold-mirror-needs-non-equilibrium-descent | not affected |
| synthesis.mirror-asymmetry-route-one | not affected |
| synthesis.indifference-is-curie-plus-single-valuedness | not affected |
| synthesis.antiperiodic-array-against-the-light-ray-continuum-at-window-length-r | not affected |
| synthesis.light-ray-continuum-is-the-twist-integral-of-arrays-and-window-values-are-twist-averages | not affected |
| synthesis.window-energy-tests-with-free-spacing-admit-twists-half-third-and-quarter | not affected (its 1e-12 is an interval width) |
| synthesis.colour-angle-term-under-the-stored-maps-and-no-colour-anomalous-phase-of-the-rung-coupling | not affected (its 1e-13 is a displacement of the angle) |
| synthesis.exponential-reading-of-the-tower-is-the-iterated-fock-functor-not-the-ascent | not affected ("floor" there is a floor of the tower) |
| synthesis.invariant-forms-on-the-fock-module-and-the-pair-counts-of-a-next-level | not affected (same) |

Conclusions that changed in dependants:
- stored-asymmetry (ii): "more than four orders too few" was false at the new coefficients; it is "more than three".
- mirrors-composition (i), and through it stored-asymmetry's caveat and imported-mirror: "neutron-rich at the
  gravitational floor" is established only at xi = 2.8 to 3.2e-4. That range is now below the floor at the top of
  the ceiling range (5.2e-4) and is the floor only for a lower reheating temperature. At 5.2e-4 the composition
  is not computed. What still follows from the stored text: the floor lies below the helium interval, so the
  burning branch is not the floor's composition.
- radiation-audit: eleven orders at the floor, not twelve. "Eight orders or more across the interval" stands.
- mirror-temperature: every bound of clause (i) weakened by a factor of about 1.7; the floor still drops out
  under (R) (it changes xi^4 at the helium edge by less than 1e-8).

## Layers 1 to 3

`python -m tp check --store store --layers 1-3 --keep-going --author leon`, run once after the last edit:
0 errors, 0 warnings, 122 information findings (I126 x 1, I213 x 120, I305 x 1). I305: "this change touches 19
entities; 20 claims and 9 documents depend on them and need re-confirmation". The stale pins are not reported
one by one at these layers; they are the ones in the table above.

Every changed check passes under colony/runcheck.py (11 files, 35 functions). I also perturbed the changed
functions on copies in /tmp, with the validator's own sampling (literal + 1 at eight evenly spaced positions):
no function survives all perturbations, and none survives more than half (worst cases 4 of 8).

## Could not decide (for Leon or the orchestrator)

1. The energy convention of the floor. With Gamma counting events of two quanta, the stored "energy fraction 4Y"
   means 3T per event. If each quantum carries 3T the fraction is 8Y and every floor rises by 2^(1/4) = 1.19
   (mirror 6.2e-4, nine vectors 7.6e-4), eta' at the floor falls to 2.6, and the two radiation values at the
   floors double. I kept the stored convention, as the brief says, and stated the other count beside it. The mean
   energy per event is not computed anywhere in the store; it needs the energy-weighted collision integral.
2. dark-tower-matter.mirrors-composition clause (i) needs recomputing at xi = 5.2e-4 with the MIR and CHECK_COS
   scripts, which are not in the lab. Not part of any statement: the two stored ends 49 and 84 of the
   Fermi-energy ratio follow xi^-4 ((3.2/2.8)^4 = 1.71 = 84/49), which would put that ratio near 7 at 5.2e-4, so
   the mirror is probably still charge-dominated at seeding there; the freeze-out ratio and the neutron fraction
   do not scale simply.
3. Legacy evidence. verify_T14.py still evaluates 1.9e-4, 1.1e-3, 2.3e-3 (line 1161 and Part K). It stays listed
   in checked_by of entities 1 and 2, stored-asymmetry and the audit (I removed nothing from front matter). It
   will pass at layer 4 but no longer tests the stated numbers. The T14 paper text has the same old numbers.
4. Stale quotes outside the cone, not touched:
   - synthesis.majorana-scale-free-on-pati-salam-route, clause (iii): "M_3 > 1.36e12 GeV" should read 8.3e11 GeV;
     its conclusion (the window lies wholly above 4 pi v_R = 5.35e11 GeV) still holds. It quotes the number
     without a derivation edge, so it is not in the cone.
   - store/open_problems.yaml (orchestrator's): op.odd-towers (1.36e12), op.pre-descent-theory (1.5e-5 and
     1.36e12), op.matter-asymmetry-origin (1.8 to 2.7e-15, four orders).
   - Setting notes from the papers: note.dark-matter.setting-successor-problems ("above about 2e12 GeV" and
     "near 1e5 GeV" for the seeding signpost), note.dark-matter.setting-dark-stable-counted and
     note.simulations.setting-composition-recombination (freeze-out and recombination figures "at the floor").
   - documents/ and site/ (generated) still show the old numbers.
5. Coverage judges. I updated clauses and omits and appended a dated line to each judge note saying the new
   numbers were not judged again; the verdicts are the earlier judge's.
6. Amendment evidence is named for every changed entity that has a check bearing on the change. None is named
   for mirrors-composition, adiabatic-deposit and the two predictions, which have no such check.
7. In entity 3 clause (iii), the "satisfied" comparisons use A at the same lower ends as the exclusion (stored
   practice). I verified off the record that the new statement at c = 2.27 also holds with A at its upper ends
   (5.04e47 < 6.29e47); the check does not test that.

## For the main session's memory (where learned)

- Decision D3 of 18 November 2026, "fix everything now": the Fact is amended to version 4 and its four direct
  users are restated in the same pull request (MAINTAINER.md of this run).
- The store's production coefficients are now those of the derived theorem, per creation event of two quanta;
  the Weyl-or-Dirac bracket is closed (MAINTAINER.md; the theorem's clause (v)).
- The mirror's gravitational floor at the ceiling is 5.2e-4 and eta' there is 4.4 (this pass).
