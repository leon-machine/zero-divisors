# Contradictions audit: values and conditions

**Resolutions (maintainer decisions of 21 October 2026, seed/DECISIONS_2026-10-21.md).**
H1, H2: superseded by T14c; the T14 claims are narrowed and carry caveats, the
T14c results record `lineage.supersedes`, and `pred.no-dark-radiation` now says
it needs a cold mirror, an exception to P2. H3: `standard-model.dating-descent` is
conditional on the Henneaux-Teitelboim promotion. M1: the T16 Fact
distinguishes the clocks' period from the state's modular period, which holds
under (R). M2: `pred.boundary-mode-density` is stated in the capacity
convention, nu = 1/(16 pi ln 2), the 1-nat form as conversion; T08's area-law
result names its convention. M3: the trichotomy's exhaustiveness and CPT
covariance are now store postulates assumed where used (the trichotomy itself
left as it is). M4: (U) and (EW) are linked by `contradicts`; no result rests on
both (the validator now checks this, E307). M5: the real-breaking assumption is
a postulate. L1: P4 removed where clause (v) discharges it.
Resolved since, as the store stood on 26 October 2026 (op.small-findings, settled): M6: `dark-matter.imported-gravity-only-coupling` is now a proved restatement of the T10 chain (`dark-energy.acoustic-no-go-one-way-grip`), so the Indifference premise, tameness and (Q) enter its holds-given, and `dark-matter.superselected-hence-dark-exactly-stable`, `pred.dark-matter-direct-detection-null` and `pred.no-indirect-dark-signals` carry the s-wave scope, the Indifference premise and (Q) at every level (op.dark-sector-scopes, settled). M7: `pred.dimmed-evaporation-bursts` names only this tower and the mirror as populated by the series' own results and states the dimming through `synthesis.dimmed-burst-time-rescaled-copy`: a factor D = (2 + g + o)/(1 + g) on the primary tail, about two from the mirror, more if the odd towers are populated. M8: `lepton.self-conjugacy-forces-determinant-one-group` states the untwisted scope (the twisted spectrum is self-conjugate under the whole group), with `note.lepton.abstract` and the bearing on `lepton.what-self-conjugacy-says-about-thirteenth`. M9: as STRUCTURE M2. M10: `refuted.the-number-n-is-a-coincidence-dirac` and `refuted.the-number-n-is-a-mystery-of-largeness` state their observation-level strength (op.t12-n-after-the-count, settled). M11: `dark-matter.unit-ball-rule` calls the 5.364 agreement a fit at every level, as `dark-matter.status-rule` records. M12: `scrambling.mode-count`, the area-law test, the integer-holographic form, `pred.boundary-mode-density` and `scrambling.no-echo-prediction-registered` now hold given (C1) (and (C2) where they count), which are in their past cones. L2: `dark-matter.coefficients-floors-they-give-what-gravity` (31.9 to 36.2 times the ceiling); the eta-prime half dissolved, 19 to 26 and 0.008 being exact under the unrounded floors and the stored hot-deposit xi. L3: `pred.no-neutrinoless-double-beta` gives the ranges 1.3 to 1.7 and 3.5 to 3.9 meV. L4: `dark-matter.imported-composition-simulated`, `note.programme.setting-seventeen-refutations` (seventeen conjectures, sixteen refutations) and `note.dark-matter.setting-predictions-collected` (T14's conditions 6, 7, 2, 3 and 4). L5: `note.programme.setting-seventeen-refutations` (about 10.2 percent, exact one-loop 78761/379488). L6: `scrambling.epoch-modular-period-two-unknowns-become` ((C3) and (IC) agree only at epsilon = e^{-(4 pi + 8/3 - 2 ln 2)}, about 9.7e-7). L7: `dark-matter.two-reductions` and `dark-matter.democracy-de-sitter-radius-unit-ball`. L8: `pred.no-objective-collapse` (the one-liner carries the record-chain premises). Every finding of this report is resolved or recorded.


Scope: every claim, prediction and object in `store/` (about 880 results), read
through `tp.ask` (`get_claim`, `cone`, `find_text`) and grep over the entity
files and `build/graph.json`. Nothing under `store/`, `tp/` or `documents/` was
changed, and no verify script was run. Each finding below was checked by
reading both (or all) entities named; candidates that dissolved on reading are
listed at the end so they are not re-raised.

Severity: **high**, the store asserts both sides; **medium**, a reader is
likely to be misled (a dropped condition, an unmarked convention, or a
hypothesis another result shows to fail); **low**, cosmetic or arithmetic
slips that change no conclusion.

Counts: **3 high, 12 medium, 8 low** (23 findings).

## Summary table

| # | Sev. | Topic | Main ids | Kind |
|---|---|---|---|---|
| H1 | high | Mirror temperature against P2; feeds the no-dark-radiation prediction | `dark-matter.mirror-tower-copy-one`, `dark-matter.stored-asymmetry-charge-not-number`, `dark-matter.open-channels-their-costs`, `dark-tower-matter.mirrors-temperature-p2`, `pred.no-dark-radiation` | genuine contradiction |
| H2 | high | Mirror composition at the gravitational floor: helium or neutrons | `simulations.imported-mirror`, `dark-matter.mirror-share-one-how-fragile`, `dark-tower-matter.mirrors-composition` | genuine contradiction |
| H3 | high | N "fixed at the origin" against "N is not initial data under the action as written" | `standard-model.dating-descent`, `dark-energy.under-action-written-norm-parameter-laws`, `programme.n-parameter-of-the-laws` | dropped condition (conjecture stated unconditionally against a proved result) |
| M1 | medium | Modular period 8πM "unconditionally" against the (R)-dependence of the modular period | `one-relation.imported-single-mode-thermality-modular-period`, `scrambling.clock-inventory-boundary-modes`, `state-selection.rate-discharge-hypothesis-iii`, `singularity.why-calibration-cannot-be-internal` | wording slip (clock period read as the state's modular period) |
| M2 | medium | Boundary-mode count at the area law: N = S_BH or N = S_BH/ln 2 | `scrambling.area-law-test`, `singularity.area-law-test`, `scrambling.epoch-modular-period-two-unknowns-become`, `pred.boundary-mode-density` | normalisation difference, unmarked in the entities |
| M3 | medium | The seventeenth refutation rests on the trichotomy's exhaustiveness, which T10 proves fails | `dark-matter.orientation-arrow-seventeenth-refutation`, `dark-energy.four-alternatives-are-exhaustive-three-are`, `dark-matter.imported-trichotomy-descents-data` | hypothesis refuted elsewhere; not in holds_given |
| M4 | medium | Neutrino Dirac entry in the heavy direction: Hypothesis (U) against Premise (EW); scale of M_R | `dark-matter.hyp-u-equal-rank-one-eigenvalues`, `standard-model.premise-ew-equal-weight`, `standard-model.what-angle-asks-neutrino-sector`, `note.neutrino.valuation-m-both-ends-hypothesis-u` | incompatible premises plus a running-scale convention |
| M5 | medium | Neutrino predictions name (H) only | `pred.neutrino-mass-sum-floor`, `pred.no-neutrinoless-double-beta`, `pred.leptonic-cp-trivial`, `neutrino.rank-one-seesaw-ordering-sum-double` | dropped conditions |
| M6 | medium | Gravity-only coupling: conditional import whose conditions do not propagate | `dark-matter.imported-gravity-only-coupling`, `dark-matter.superselected-hence-dark-exactly-stable`, `pred.dark-matter-direct-detection-null`, `pred.no-indirect-dark-signals` | dropped conditions and scope |
| M7 | medium | Dimmed bursts assert six populated towers | `pred.dimmed-evaporation-bursts`, `dark-matter.which-towers-are-populated` | level states more than its basis |
| M8 | medium | Self-conjugacy and the thirteenth generator | `lepton.self-conjugacy-forces-determinant-one-group`, `lepton.what-self-conjugacy-says-about-thirteenth`, `standard-model.under-s-composites-state-space-spinor` | scoping (untwisted action) unstated |
| M9 | medium | N against the universe's boundary-mode count (10^60 or 10^120) | `standard-model.what`, `standard-model.largeness-number-universes-boundary-modes`, `standard-model.why-large` | genuine numerical inconsistency (conjecture level) |
| M10 | medium | Refutations 10 and 11 carried by conjectures | `refuted.the-number-n-is-a-coincidence-dirac`, `refuted.the-number-n-is-a-mystery-of-largeness`, `standard-model.one-number-explain`, `standard-model.why-large` | status strength mismatch |
| M11 | medium | Unit-ball rule: proved and "matching" against "a fit, not a prediction" | `dark-matter.unit-ball-rule`, `dark-matter.status-rule` | level of claim differs |
| M12 | medium | The stretched singularity: a postulate in T05, a definition in T08 | `singularity.c1-curvature-cutoff`, `singularity.c2-cell-density`, `obj.scrambling.stretched-singularity`, `scrambling.mode-count`, `scrambling.no-echo-prediction-registered` | dropped conditions |
| L1 | low | The premises of the mirror share f2 = 1 are listed four ways | `dark-matter.mirror-share-assembled`, `dark-matter.population-count-one-share-half-percent`, `dark-matter.mirror-share-one-how-fragile`, `dark-matter.mirror-tower-copy-one` | wording |
| L2 | low | Arithmetic of η′ and of the deposit ratio | `dark-matter.stored-asymmetry-charge-not-number`, `dark-matter.coefficients-floors-they-give-what-gravity` | arithmetic slip |
| L3 | low | m_ββ point values against ranges | `pred.no-neutrinoless-double-beta`, `neutrino.rank-one-seesaw-ordering-sum-double` | uncertainty dropped |
| L4 | low | Refutation numbering and counting | `note.programme.setting-seventeen-refutations`, `dark-matter.imported-composition-simulated`, `note.dark-matter.setting-predictions-collected` | naming collision |
| L5 | low | "Ten percent, exactly" | `note.programme.setting-seventeen-refutations`, `standard-model.spectrum-run` | wording slip |
| L6 | low | Two premises fix the counted epoch at different values | `singularity.c3-counted-epoch`, `scrambling.intrinsic-clock-ic-flagged-premise` | scoping; no supersedes link |
| L7 | low | De Sitter reading results proved in an excluded setting | `dark-matter.democracy-de-sitter-radius-unit-ball`, `dark-matter.two-reductions`, `dark-matter.thickness-not-gravitational-quantity` | scoping |
| L8 | low | Prediction one-liner drops its premises | `pred.no-objective-collapse` | dropped condition (one level) |

No result in the store uses a refuted claim through a `uses` or `assumes`
edge, and no prediction is `killed`; item 3 of the brief therefore turns up
only the indirect cases H1 (a live prediction resting on a premise that
another result shows forces its kill condition), M3 (a result resting on a
premise shown false in general) and M10 (refutations whose refuters are only
conjectured).

---

## High

### H1. The mirror's temperature: a free datum in T14, fixed at one by P2 in T14c

- `dark-matter.mirror-tower-copy-one` (proved), (iv): "a coupling difference
  at the ceiling would be an uncaused distinction between the two members of
  one orbit, which the audit forbids"; (v): "$\epsilon_{2} = \epsilon_{6}$ ...
  by the audit, as in (iv), a difference between two continuous data of one
  reversal orbit being an uncaused distinction".
- `dark-matter.stored-asymmetry-charge-not-number` (proved), (iii): "The
  mirror's temperature ratio $\xi = T'/T$ is a datum of the descent, bounded
  below by the gravitational floor ... and above by the $\Neff$ cap at
  $0.448$".
- `dark-matter.open-channels-their-costs` (proved): "A cold mirror with our
  baryon number is what the framework predicts."
- `dark-tower-matter.mirrors-temperature-p2` (proved, T14c): "Applied with the
  same reach, P2 gives $\xi = T'/T = 1$ and $\Delta\Neff = \tfrac{8}{7}(\tfrac{11}{4})^{4/3} + 3.044 = 7.45$
  at recombination, excluded by a factor of about $25$. T14's mirror, cold
  from the gravitational floor upward, is therefore an exception to P2 that
  T14 neither states nor costs."

Why they conflict: T14 uses P2 to equate two continuous descent data of the
reversal pair (ceiling coupling, asymmetry per mode) and treats a third datum
of the same kind (the deposit per unit charge, hence ξ) as free. T14c proves
that P2 with T14's own reach forces ξ = 1, which the CMB excludes. Both are
`proved`; the T14 entities do not mention the exception, and
`dark-tower-matter.towers-built` lists "a P2 exception for the mirror's
temperature" as a choice the series does not make.

Consequence for item 3: `pred.no-dark-radiation` holds given
`dark-matter.p2-indifference` (its `holds_given` lists it) and needs the
mirror cold (`dark-matter.radiation-audit-what-theorem-closes-what`: "the
mirror tower is open by theorem ... and closes only if it is cold"). On T14c's
result, the premise set the prediction rests on gives ΔN_eff = 7.45, which is
the prediction's kill condition ("One confirmed massless dark species"). The
prediction's levels say only "conditionally on the dark towers' open channels
closing".

Verdict: genuine contradiction between proved results, recorded by T14c and
not reconciled in T14 or in the prediction. **High.**

### H2. The mirror's composition at the gravitational floor

- `simulations.imported-mirror` (proved, restates T14 Thm 4.3, Props 4.6, 4.7,
  6.2): "Its temperature ratio $\xi = T'/T$ lies between the gravitational
  floor, $2.8$ to $3.2 \times 10^{-4}$, and the hot-deposit estimate, about
  $4 \times 10^{-3}$ ... on the expected (burning) branch it is helium, on the
  alternative it is protons."
- `dark-matter.mirror-share-one-how-fragile` (proved), (i): "a mirror burnt
  entirely to helium (the completion limit of ... the burning branch) gives
  $931.8$ MeV, so $f_{2}$ is $0.995$ in that limit".
- `note.dark-matter.setting-predictions-collected`, row 14: "The mirror sector
  is helium-dominated with $\eta'$ between about $0.008$ and $26$" (26 is the
  floor value).
- `dark-tower-matter.mirrors-composition` (proved, T14c), (i): "At the floor
  ... for a copied lepton number $L \leq 0$ ... the mirror ends $96$ to $100$
  percent neutrons"; (ii): "Between $\xi \approx 3 \times 10^{-3}$ and
  $2 \times 10^{-2}$ ... the mirror is helium"; closing line: "the thermal
  up-down ratio T14 assumes there is inconsistent with its own $\eta' > 1$."

Why they conflict: over ξ from 2.8 × 10^-4 to about 3 × 10^-3 (the floor and
most of T14's carried interval) the store says both "helium on the expected
branch" and "neutron-rich". T14c names the T14 assumption that fails. The
burning-branch value 0.995 and the T14b galaxy simulations, which model a
helium mirror at the floor, rest on the T14 side.

Verdict: genuine contradiction between proved results. The share itself moves
by under a percent (neutrons would give a mean mass per baryon near 939.6 MeV,
f2 ≈ 1.003), but the composition the simulations test does change. **High.**

### H3. N "fixed at the origin" against "N is not initial data under the action as written"

- `standard-model.dating-descent` (conjectured), (ii): "The framework then
  answers, as its own claim: the descent froze at the beginning ... the frozen
  point, hence $\Lambda$, hence $N$, was fixed at the origin and has been
  constant since, which is exactly the registered stance $w = -1$." One-liner:
  "the framework proposes, at observation level, that the descent froze at the
  origin, fixing $\Lambda$ and $N$ ever since."
- `dark-energy.under-action-written-norm-parameter-laws` (proved), (iii):
  "therefore $N$ is (P), a parameter of the laws, and not (I): clause (3) of
  the Standard-Model paper's classification, ``$N$ is initial data'', is false
  for the action as written."
- `programme.n-parameter-of-the-laws`: "it is initial data of the descent,
  dated to the origin, only if the Henneaux-Teitelboim promotion is adopted, a
  decision recorded open."

Why they conflict: "fixed at the origin and constant since" is the (I)
reading, as the T10 remark `note.dark-energy.what-clause-3-requires-what-it`
itself says ("which is the (I) reading: a constant of integration ... the
action as written does not deliver that reading"). That remark comments on the
T10 results, not on `standard-model.dating-descent`, and no edge joins them,
so the T12 entity states the reading with no condition at any level. It also
calls w = −1 "exactly the registered stance" without the registration's
condition (`pred.dark-energy-w-minus-one`: "registered with its one
condition").

Verdict: the conjecture drops the Henneaux-Teitelboim condition and so asserts
what a proved result denies for the only action the series has. **High**
(conjecture-level on one side, but stated as "its own claim").

---

## Medium

### M1. "The modular period β = 8πM unconditionally"

- `one-relation.imported-single-mode-thermality-modular-period` (proved):
  "its exactness holds under the singularity paper's declared premises (P) and
  (R), and the value of $T_{H}$ follows from (R). The entropy paper's clock
  inventory of the singularity's boundary modes gives the modular period
  $\beta = 8\pi M$ unconditionally."
- `state-selection.rate-discharge-hypothesis-iii` (proved): "Under (P), (R)
  and the geometric modular condition the modular period in rapidity is
  $2\pi$, so $T = \kappa/2\pi = 1/8\pi M = \TH$".
- `state-selection.rate-rigidity-temperature-not-algebra-intrinsic` (proved):
  "no condition formulated in the algebra and its flow alone can fix the
  temperature."
- `singularity.why-calibration-cannot-be-internal` (proved): "on the singular
  side the connection rate diverges ... and offers no finite period to be
  identified with $2\pi$ ... no strengthening of the framework's statements at
  the singular boundary can supply (R)."

Why they conflict: the T16 restatement calls the period of the T08 clocks (a
flow normalised to rapidity and converted at the horizon rate κ, with the 2π
taken from the Euclidean continuation) "the modular period" and says it holds
unconditionally, while T05 and its companion prove that the state's modular
period equals that value only under (R) and the geometric modular condition,
and that nothing at the singular boundary supplies (R). Within one sentence
T16 has "T_H follows from (R)" and "β = 8πM unconditionally", which a reader
cannot both take with β = 1/T_H.

Verdict: wording slip (clock period against the state's modular period), not
a contradiction in the mathematics. **Medium.**

### M2. The boundary-mode count at the area law: N = S_BH or N = S_BH/ln 2

- `scrambling.area-law-test` (proved, T08), all four levels: "$N = \SBH = 4\pi M^2$
  if and only if $\nu\,\Delta t = M/2$: the count reproduces the
  Bekenstein-Hawking entropy, coefficient included". No convention is named in
  the entity.
- `singularity.area-law-test` (proved, T05): "let $C := N_{\mathrm{6a}}\ln 2$
  be its boundary-mode capacity in nats ... $C = S_{\mathrm{BH}}$ if and only
  if $\nu\,\Delta t = M/(2\ln 2)$ ... It is the capacity, not the bare count,
  that ... compare with $S_{\mathrm{BH}}$; the count itself then reads
  $N_{\mathrm{6a}} = S_{\mathrm{BH}}/\ln 2$."
- `scrambling.epoch-modular-period-two-unknowns-become` (proved): "$\nu = 1/16\pi$
  in the 1-nat convention ($\nu = 1/(16\pi\ln 2)$ in T5's capacity
  convention ...; Section ... shows the capacity convention is the one with
  physical content".
- `pred.boundary-mode-density` (live): registered as "$\nu = 1/16\pi$ in the
  1-nat convention, equivalently one boundary-mode fermion per four Planck
  cells"; title "One boundary-mode fermion per four Planck cells" and lay "one
  elementary fermionic mode for every four Planck-sized patches" name no
  convention.

Why they conflict: the same count at the same area-law condition is S_BH in
T08 and S_BH/ln 2 in T05. The 1-nat convention that reconciles them appears
only in the note `note.scrambling.density-factor-stated-full`, not in
`scrambling.area-law-test`. The registered prediction is stated in the
convention its own source says lacks physical content; in the capacity
convention the count is A/(4 ln 2), about 1.44 fermions per four Planck cells,
so the title and lay statement are false there.

Verdict: normalisation difference, unmarked in the entities, carried into a
registered prediction. **Medium.**

### M3. The seventeenth refutation rests on the trichotomy's exhaustiveness

- `dark-matter.orientation-arrow-seventeenth-refutation` (proved): "on three
  premises: that CPT conjugation is an isomorphism of every kinematic
  structure ...; Hypothesis (S) ...; and, for the last step only, the
  trichotomy's exhaustiveness". One-liner: "Under CPT covariance of the
  kinematic structures, Hypothesis (S) and the trichotomy's exhaustiveness,
  the particle-antiparticle orientation ... is initial data".
- `dark-energy.four-alternatives-are-exhaustive-three-are` (proved): "the
  inference ``not kinematic, not dynamical, therefore initial data'' is valid
  only if (P) is excluded."
- `dark-matter.imported-trichotomy-descents-data` (proved), (4): "the three
  are not exhaustive"; and, for the bit: "the CPT covariance of the
  structures ... leaves no room within them, so the bit is data if it is
  anything".

Why they conflict: the seventeenth refutation names as a premise a statement
the store proves false in general. T14's trichotomy fact supplies a separate
argument that closes the gap for the bit, but the orientation result, its
restatement `one-relation.imported-flag-arrow-superselection` ("initial data
under three stated premises"), `refuted.the-particle-antiparticle-orientation-is-determi`
and the T17 table still cite exhaustiveness. Neither exhaustiveness nor CPT
covariance of the gauge sector is a store postulate, so the derived
`holds_given` of the orientation result ({indifference, tameness, (S)}) does
not show them.

Verdict: a hypothesis refuted elsewhere, rescued only in another entity's
prose; scoping. **Medium.**

### M4. The neutrino's Dirac entry in the heavy direction, and the scale of M_R

- `dark-matter.hyp-u-equal-rank-one-eigenvalues` (postulate): "the neutrino's
  Dirac eigenvalue $m_{D}$ there is the common leading-order value, which the
  top retains and the second-order breaking splits for the down-type and
  charged-lepton sectors." Valued in `dark-matter.ceiling-valued-inherited-success`
  as $3.5 \times 10^{11}$ to $6 \times 10^{14}$ GeV, "with (U) read at a common
  low scale (read at the ceiling, the running ... lowers both ends by about an
  order of magnitude, a systematic the range does not include)".
- `standard-model.premise-ew-equal-weight` (postulate): "in a family basis in
  which the symmetric part of $M_{u}$ is diagonal with $(M_{u})_{33} = m_{t}$,
  $(M_{\nu})_{33} = 0$".
- `standard-model.what-angle-asks-neutrino-sector` (proved): "$v_{R} = 4.2 \times 10^{10}$
  GeV ... $m_{D} = \sqrt{m_{3}f_{J}v_{R}} = 1.44\sqrt{f_{J}}$ GeV", so
  $M_R = f_J v_R \approx 4.2 \times 10^{10} f_J$ GeV.
- `note.neutrino.valuation-m-both-ends-hypothesis-u`: "the bottom-like end of
  the range above ... the series' Pati-Salam route selects the bottom one".

Why they conflict: (U) sets the neutrino's leading Dirac eigenvalue in the
heavy (aligned) direction to the top's value, or to a split value like the
bottom's; (EW) sets the neutrino's Dirac entry in the top's direction to zero.
Both ends of (U) are nonzero there, so the two premises cannot hold together
in a basis where the heavy directions coincide, which the democratic alignment
gives at leading order. T14's mirror-share fragility and radiation audit rest
on (U); T12's fits (`standard-model.fits-record-level`) rest on (EW); no entity
records the clash. Separately, the T15 remark's "selects the bottom one"
compares T12's running values at M_I (`note.standard-model.setting-weak-angle-pati-salam-route-2`:
"$m_{b}(M_{I}) = 1.37$ GeV") with T14's low-scale range: the Pati-Salam value
at f_J = 1 is about 4 × 10^10 GeV, an order below the stated bottom end
3.5 × 10^11 GeV, the systematic T14 says its range excludes.

Verdict: incompatible premises in different papers (a hypothesis-level
tension, not two asserted results), plus a scale-convention mismatch in the
remark that joins them. **Medium.**

### M5. The neutrino predictions name Premise (H) only

- `pred.neutrino-mass-sum-floor`: "The neutrino mass sum lies at the
  oscillation floor, approximately $0.059$ eV, with normal ordering; the sum
  is a prediction under the hierarchy premise (H)." One-liner: "Under Premise
  (H) ...".
- `pred.no-neutrinoless-double-beta`, one-liner: "Under Premise (H),
  $m_{\beta\beta}$ is a few meV".
- `pred.leptonic-cp-trivial`, one-liner: "Under the real-breaking assumption
  ...".
- Their derived `holds_given` (from `get_claim`): (H), (M)
  `neutrino.m-framework-realises-majorana-term-scale`, the working hypothesis
  `families.hyp-face-identification`, the indifference premise and (S); for
  the CP prediction also (U), (R) of T15 and P1 to P4.
- `neutrino.imported-indifference-faces-democratic-alignment-rank`: "Under the
  indifference premise, the conjectural face picture of the families and the
  Gram-square reading".

Why they conflict: the normal ordering and the floor follow from the rank-one
seesaw, which needs (M) and the democratic alignment, which needs the face
picture that the store holds as a conjecture
(`families.three-generations-faces-maximal-composite`, conjectured). The
prediction texts present normal ordering as unconditional and the sum as
conditional on (H) alone; the lay level of `pred.leptonic-cp-trivial` says
"the normal ordering, which the framework also predicts". The real-breaking
assumption has no store postulate (the typing note says so), so it never
appears in any `holds_given`.

Verdict: dropped conditions; the stated condition sets are strict subsets of
what the results rest on. **Medium.**

### M6. The gravity-only coupling: an import whose conditions do not propagate

- `dark-matter.imported-gravity-only-coupling` (imported): "Imported at the
  acoustic no-go's mixed level, conditional on the Indifference premise and
  premise (Q): within the s-wave current algebra, matter that gravitates on
  this metric and carries no shared gauge charge does nothing else
  observable." Derived `holds_given`: [] (status imported, no `uses`).
- `dark-matter.superselected-hence-dark-exactly-stable` (proved), one-liner:
  "Under P1, the sector decomposition and the wall-sequence theorem's
  hypotheses ..., the tower charge is exactly superselected, so dark-tower
  matter only gravitates and is exactly stable."
- `pred.dark-matter-direct-detection-null`, `pred.no-indirect-dark-signals`:
  "Conditionally on the single-frozen-point premise".

Why they conflict: "only gravitates" is the import's conclusion, which holds
within the s-wave current algebra and under the Indifference premise and (Q).
Because the import is typed `imported` although its source is the series'
own T10 result (`dark-energy.acoustic-no-go-one-way-grip`), its conditions and
scope stop there: the superselection result and both predictions show P1 (and
P2, P3, tameness) only, and their levels drop the s-wave scope.

Verdict: dropped conditions and scope. **Medium.**

### M7. Dimmed bursts assert "all six populated towers, five of them dark"

- `pred.dimmed-evaporation-bursts` (live, basis_status proved): "the hole
  radiates into all six populated towers, five of them dark, so the visible
  burst is dimmed by the ratio of total to visible light degrees of freedom."
- `dark-matter.which-towers-are-populated` (conjectured): "the population of
  the four odd towers is an observation-level inference from the observed
  dark-to-baryon ratio, granted the framework"; "Nothing derived in this paper
  depends on the odd towers being populated".
- Its basis `dark-matter.parallel-boundary-mode-spaces-one-wall`: "of order the
  tower count if the towers are comparable".

Why they conflict: the prediction states as fact a population count the store
holds as a conjecture, and the size of the dimming depends on it. With only
this tower and the mirror populated (the derived case) the burst is still
dimmed, so the qualitative prediction survives; the stated count and "five of
them dark" do not follow from the basis.

Verdict: the prediction states more than its basis. **Medium.**

### M8. Self-conjugacy and the thirteenth generator

- `lepton.self-conjugacy-forces-determinant-one-group` (proved): "the largest
  subgroup of $U(2) \times U(3)$ under which the constituent spectrum is
  closed under conjugation is exactly the automorphism group of the hierarchy,
  $S(U(2) \times U(3))$, twelve-dimensional." No level names the action.
- `lepton.what-self-conjugacy-says-about-thirteenth` (conjectured): "In the
  action twisted by $(\det A \cdot \det B)^{-1/2}$ that the Standard-Model
  paper now uses, the dual of every component is a component, so
  self-conjugacy does not exclude the thirteenth generator".
- `standard-model.under-s-composites-state-space-spinor` (proved): the
  automorphism rule "returns thirteen generators", the extra one anomaly-free
  "in the action the generation carries".
- `note.lepton.abstract`: "the constituent spectrum is self-conjugate exactly
  for the determinant-one group, which ... removes the thirteenth generator".

Why they conflict: the proved theorem holds in the untwisted action; in the
twisted action, which T12 says the state space carries, its conclusion fails.
The theorem's levels and the note's abstract state it without that scope.

Verdict: scoping difference left unstated. **Medium.**

### M9. N against the universe's boundary-mode count

- `standard-model.what` (conjectured): "the de Sitter horizon entropy is of
  order $N^{2}$, so that $N$ is the square root of the pair capacity of the
  universe's own boundary mode space"; one-liner: "$N$ is indicated to be the
  square root of the universe's horizon mode count".
- `standard-model.largeness-number-universes-boundary-modes` (conjectured),
  technical: "this number, on the indication that the de Sitter horizon
  entropy is of order $N^{2}$, counts the modes of the universe's own
  horizon".
- `standard-model.why-large` (conjectured): "why the universe's boundary mode
  space is ... so small, of order $10^{60}$".

Why they conflict: one entity puts the horizon mode count at N² (about
10^120, the value the T12 script brackets as $2^{398} < 10^{120} < 2^{399}$),
the other two make N itself (about 10^60) the count or the size of the mode
space, citing the same indication.

Verdict: genuine numerical inconsistency (a factor of two in the exponent) at
conjecture level. **Medium.**

### M10. Refutations 10 and 11 are carried by conjectures

- `refuted.the-number-n-is-a-coincidence-dirac`: `refuted_by`
  `standard-model.one-number-explain`, which is `conjectured`.
- `refuted.the-number-n-is-a-mystery-of-largeness`: `refuted_by`
  `standard-model.why-large`, `conjectured`, one-liner "At observation level
  and on an unproved exponential reading of the tower".
- `note.programme.setting-measure-two-numbers-one-bit`: "(the Dirac reading is
  refuted by the $w = -1$ prediction)", a live, conditional prediction.

Why they conflict: every other refuted entity is refuted by a `proved`
result; these two carry `refuted` status on observation-level conjectures, and
the T17 note names a third refuter for the Dirac reading. A reader trusting
"refuted" takes the corrections as established.

Verdict: status-strength mismatch. **Medium.**

### M11. The unit-ball rule: proved and "matching", or a fit

- `dark-matter.unit-ball-rule` (proved): "$\frac{\Omega_{\mathrm{dark}}}{\Omega_{b}} = \frac{11\pi + 16}{3\pi} = 5.36432\ldots$
  against the observed $5.364 \pm 0.065$"; lay: "Under its three premises the
  rule gives a dark-to-ordinary matter ratio of about 5.364, matching the
  observed value."
- `dark-matter.status-rule` (conjectured): "The relation was found by solving
  ... for the observed value, not predicted ... The closed form is one of
  fourteen equally simple candidates in the error bar ... Its tier is
  observation level on R1 to R3".

Why they conflict: the value is the same (5.3643, also 5.364 in
`simulations.imported-unit-ball-rule-family` and 4.364 for the remainder in
`dark-matter.population-count-one-share-half-percent`), but the rule's own
levels present a derived match, while the status entity says the match is
built in. The status entity does not `comments_on` the rule.

Verdict: the level of claim differs between the two entities. **Medium.**

### M12. The stretched singularity: a postulate in T05, a definition in T08

- `singularity.c1-curvature-cutoff` (postulate): "The q-number boundary mode
  space of the singularity is supported on the stretched singularity ...
  $r_c = (2M)^{1/3}$"; `singularity.c2-cell-density` (postulate): "$\nu$
  fermionic modes per Planck cell".
- `obj.scrambling.stretched-singularity` (defined) and
  `scrambling.mode-count` (proved, `holds_given` []): "Let $\nu$ be the number
  of fermionic modes per Planck cell of the stretched singularity ... $N = 8\pi\nu M\Delta t$".
- `scrambling.no-echo-prediction-registered` (live, `holds_given` []): "The
  framework's quantum structure lies at the stretched singularity, $r_c = (2M)^{1/3}$".

Why they conflict: T05's count `singularity.stretched-singularity-count` holds
"Under (C1) and (C2)"; T08's restated count, its area-law test, the
integer-holographic corollary, `pred.boundary-mode-density` (`holds_given`
only (IC)) and the no-echo prediction place the boundary modes on the slice
and count ν per cell with neither postulate in their past cones. Only two
entities in the store `assume` C1.

Verdict: dropped conditions. **Medium.**

---

## Low

### L1. The premises of the mirror share f2 = 1 are stated four ways

`dark-matter.mirror-share-assembled`: "Under Premises P1, P2 and P4, ...
Hypothesis (S) ..."; `dark-matter.population-count-one-share-half-percent`:
"Under P1 to P4" (no (S), though its `holds_given` contains it);
`dark-matter.mirror-share-one-how-fragile`: "Under the democracy of the
asymmetry the mirror share is exactly one"; `dark-matter.mirror-tower-copy-one`
(v): "Premise P4 is discharged for the mirror, and the share of one in (iii)
rests on P1, P2 and the copy", while (iv) calls the common coupling "the one
place P2 applies across towers" and (v) applies P2 again to ε. The value is
the same everywhere; the condition sets disagree, and P4 is both discharged
and listed. Wording; **low**.

### L2. Arithmetic of η′ and of the deposit ratio

`dark-matter.stored-asymmetry-charge-not-number` (iii): "$\eta' = \eta/\xi^{3}$
runs from $19$ to $26$ at the floor down to about $0.008$ at the hot deposit",
with η = 6.1 × 10^-10, ξ floor 2.8 to 3.2 × 10^-4 and hot deposit 4 × 10^-3.
These give 18.6 to 27.8 and 0.0095. The 26 recurs in the T14 predictions table
and in `dark-tower-matter.mirrors-composition`.
`dark-matter.coefficients-floors-they-give-what-gravity`: "$T_{\mathrm{desc}}$
between $1.9$ and $2.2 \times 10^{16}$ GeV, thirty to thirty-six times the
ceiling" against a ceiling of 6 × 10^14 GeV gives 32 to 37. Neither changes a
conclusion. Arithmetic slip; **low**.

### L3. m_ββ: point values against ranges

`pred.no-neutrinoless-double-beta`: "$m_{\beta\beta}$ at $1.5$ or $3.7$ meV
under premise (H) and the real-breaking assumption"; its basis
`neutrino.rank-one-seesaw-ordering-sum-double`: "$3.5$-$3.9$ meV at relative
phase $0$ or $1.3$-$1.7$ meV at relative phase $\pi$, at $\sin^{2}\theta_{12} \in (0.295, 0.319)$
...". Same value, uncertainty dropped. **Low**.

### L4. Refutation numbering and counting

T14 numbers its own refutation conditions: `dark-matter.imported-composition-simulated`
"(Section \ref{sec:premises}, refutation 6)", `note.dark-matter.setting-predictions-collected`
"refutations 6, 7, 2, 3 and 4 above". The series' sixth refutation is the
internal ladder (`note.programme.setting-seventeen-refutations`, row 6;
`note.standard-model.sixth-refutation-ladder-not-gauge-group`). The T17 note
is titled "Seventeen refutations" but records "sixteen were refuted" (the store
holds sixteen refuted entities, which matches), and it `comments_on` only one
of them. The ordinals that are cited (first, fifth, sixth, eighth, ninth,
thirteenth to seventeenth) agree with the table everywhere. Naming collision;
**low**.

### L5. "Ten percent, exactly"

`note.programme.setting-seventeen-refutations`, row 14: "The one-loop run
differs from the measured value by ten percent, exactly". From
`standard-model.spectrum-run`, 78761/379488 = 0.2075 against 0.2312 is a
10.25 percent miss; "exactly" refers to the exact rational, not to the ten
percent. Wording slip; **low**.

### L6. Two premises fix the counted epoch at different values

`singularity.c3-counted-epoch` (postulate): "the causal epoch: the portion of
the singularity in the causal future of a single horizon-crossing", with
$\Delta t(\varepsilon) = 2M(\ln(1/\varepsilon) - \tfrac83 + 2\ln 2)$
(`scrambling.area-law-test`); `scrambling.intrinsic-clock-ic-flagged-premise`
plus the clock inventory give $\Delta t = \beta = 8\pi M$. They agree only at
one ε (about 10^-6). Both are "of order one Schwarzschild time" and T08 says
the epoch "is then derived rather than" assumed, but there is no `supersedes`
link, and T05 results still hold given C3. Scoping; **low**.

### L7. De Sitter reading results proved in an excluded setting

`dark-matter.democracy-de-sitter-radius-unit-ball` (proved): "with the
thickness one de Sitter radius ... the total is the unit-ball rule's";
`dark-matter.two-reductions` (proved) computes the reductions of a metric
fifth direction. `dark-matter.thickness-not-gravitational-quantity` (proved):
"the reductions of Proposition \claimref{dark-matter.two-reductions}, which
needed a metric fifth direction to be well posed, describe a setting that is
itself excluded". The two results' levels do not say so. The values agree
(`dark-matter.status-rule` (iv) quotes the same 5.000, 5.667, 4.333). Scoping;
**low**.

### L8. A prediction one-liner drops its premises

`pred.no-objective-collapse`, one-liner: "No objective-collapse signature ...
will be found at any sensitivity." Its technical and lay levels keep "under its
premises" and "under that account's premises", and `holds_given` lists the
recording premise, P1 to P4 and (S). One level only; **low**.

---

## Checked and consistent (not findings)

These were compared across every result that states them and agree, so they
need not be re-audited:

- Hawking temperature and normalisation: $T_H = \kappa/2\pi = 1/8\pi M$,
  $\kappa = 1/4M$, $\beta = 2\pi/\kappa = 8\pi M$, $\beta/2\pi = 4M$ in every
  T05, T07, T08, T16 and companion-note statement; the sample point
  $e^{-\omega/T} = 9/16$.
- Dark-matter ratio $(11\pi + 16)/(3\pi) = 5.3643$ (5.364), floor $5.255$ at
  $c = \sqrt{\pi/2}$, remainder $4.364\,\Omega_b$ ($\Omega h^2 = 0.0976$),
  shares 18.6, 24.9 and 15.8 percent, "about 81 percent" outside the mirror,
  1.24 above the $0.8\,\Omega_b$ bound.
- ΔN_eff: $7.447\,(T'/T_\gamma)^4$, cap 0.3, threshold 0.448 (0.47 at
  coefficient 6.40), "excluded by a factor of about 25" for ξ = 1.
- Neutrinos: sum 0.059 eV (0.0593) at normal-ordering floor, $m_1 \lesssim 0.1$
  meV from $m_1/m_2 \lesssim 0.01$, m_ββ hull 1.3 to 3.9 meV, rung scale
  $3.5 \times 10^{11}$ to $6 \times 10^{14}$ GeV in T14, T15 and the T14
  introduction, $m_D = 1.44\sqrt{f_J}$ GeV, $f_J \approx 4000$ for a top-like
  $m_D(M_I) = 92$ GeV.
- Weak angle: 3/8 over the derived generation under (S) (9/26 without the
  lepton doublet), $r_0 = 218/115$, one-loop $78761/379488 = 0.2075$,
  supersymmetric $6539/28320 = 0.2309$, $M_U \approx 7 \times 10^{14}$ GeV on
  derived content; the chain's one- and two-loop tables and the proton bound
  ratios; $X = 2Y - \tfrac52(B - L) = 2T_{3R} - \tfrac32(B - L)$.
- w = −1 always carried with its registered condition, apart from H3.
- Residues and signatures: $\Cl(1,3) \cong \Mat_2(\HH)$ (residue 6),
  $\Cl(3,1) \cong \Mat_4(\R)$ (residue 2), $\Cl(2,4) \cong \Mat_4(\HH)$, the
  odd extensions' residues 5, 7, 1, 3, type C exactly at $p - q \equiv 1 \pmod 4$,
  the field of residue $r + 1$, sterile residues 0 and 4, the flag a bit
  exactly at tower dimension $0 \bmod 4$.
- Counts: the 12- and 17-dimensional automorphism algebras, 13 generators
  under (S), three ladder pairs, the eight-dimensional Dirac module, real and
  complex capacities, the 16 refuted entities against the T17 table.
- Echo delay $8M\ln(M/m_P)$: 35 ms at $10\,M_\odot$, 0.1 to 0.25 s at 30 to
  $70\,M_\odot$; the three cutoff constants $2^{1/3}$, $48^{1/6}$,
  $(3/2)^{2/3}2^{1/3}$; slice volume $8\pi M$.
- Smaller numbers: the Schwinger bound (1.3 × 10^5 solar masses,
  7.5 × 10^-6 of extremal), $d_b \approx 0.98$ m, the weak-scale miss of 44 to
  105 orders, N of order 10^60 for $M_P/H$.
