# Maintainer file M2, run 2026-11-12-asymmetry (decisions D2 and D3)

Scope: the registered premise on epsilon, the charge Proposition, the open problem entry, and a list (no edits)
of stored text touched by the mirror consequence and by the naming. Nothing committed. The two CPT entities were
not touched.

Validation after the edits: `python3 -m tp check --store store --layers 1,2,3 --keep-going --author leon`:
0 errors, 0 warnings, 121 information findings (I213 x 119, I126, I305; none on my entities). No pin warning was
printed at these layers for the dependants of the two raised versions; the pins are listed in section 2.
`python3 colony/check4.py store/claims/dark-matter.stored-asymmetry-charge-not-number`: pass (0 errors; the
check and the coverage file were not edited).

## 1. Entities changed

| entity | version | what changed |
|---|---|---|
| `synthesis.matter-asymmetry-registered-free-input` (postulate) | 4 -> 5 | restatement: Q = epsilon N named as B - L; value made conditional |
| `dark-matter.stored-asymmetry-charge-not-number` (proved) | 10 -> 11 | restatement of clauses (i) and (ii): three objects named apart |
| `store/open_problems.yaml`, `op.matter-asymmetry-origin` only | n/a | status open -> partial; statement, known, attack, entities, source |

Each claim has the amendments entry (kind restatement), the credit entry at the new version, and
`extraction.maintainer_pass_2026_11_12`. `proposed_by` unchanged; all earlier credit entries unchanged;
`orig-proof-main.tex` untouched.

### 1.1 synthesis.matter-asymmetry-registered-free-input, 4 -> 5
- Formal, first paragraph: the valuation sentence no longer says the value "is fixed by the measured baryon
  density, equivalently 8.7e-11 baryons per unit entropy". It now says the charge is the total B - L, the record
  fixes the baryons per unit entropy, and the datum is B - L per unit entropy, related to it through a
  coefficient that is conditional and not a stored Fact.
- New paragraph "The naming and the value (restated 2026-11-12)": the three objects (residue label r, B - L,
  baryon number); the naming is a decision, not derived; the reason (24 slot-pair generators change n_B and
  carry B - L, mixed weak coefficient 2 on n_B and 0 on B - L, Majorana element the only stored term that
  changes B - L), citing the two accepted claims. Value: if the anomalous weak process equilibrated after the
  descent, (B - L)/s = 8.7e-11 / c; c = 28/79 (one light doublet, the value the mirrors-composition check uses)
  gives 2.45e-10; c = 8/23 (two, the bidoublet) gives 2.50e-10. Neither is chosen and no number is registered
  for (B - L)/s. If the process did not equilibrate, the record does not fix the datum through c (stated as not
  excluded). Protection of B - L by Premise (R), with the Majorana element the exception, labelled argued.
- "What it is for": "the mirror's equal baryon charge" -> "the mirror's equal charge B - L"; the exchange for
  the baryon density is said to pass through c.
- Refutation conditions kept word for word. One sentence added on how they read for the named datum: the
  conversion of an inherited B - L into baryon number is not a production of epsilon; an in-framework dynamics
  producing the B - L is. This follows the consequence Leon accepted under D2 (baryons per unit entropy derive
  from a free B - L value); it is an addition, so please confirm.
- The 2026-11-11 unit note is kept; two sentences appended: read it with B - L for the conserved charge, and
  n_B' = n_B needs the equal ratio in the mirror, not shown.
- Technical, lay, one-liner restated to match.
- No assumes or uses edges added (the entity has none). Lineage unchanged.

### 1.2 dark-matter.stored-asymmetry-charge-not-number, 10 -> 11
- (i): Q = epsilon N, temperature-independent, kept. Added: the three objects named apart; Q is B - L by the
  maintainer's decision (a naming, not a result of the Proposition). What holds at any mirror temperature is
  the equal B - L. `f_2 = 1` is an equality of baryon number and is now conditional on the mirror's ratio of
  baryon number to B - L equalling this tower's (not shown: c is a hot-plasma number, 28/79 or 8/23, not a
  stored Fact; the mirror is degenerate from the start at the floor). "Equal baryon number" in (iii) and the
  comparison in (iv) are said to be read under the same condition; (iii) and (iv) themselves are not edited.
- (ii): three statements. Between towers: superselection of r and the gravitational channel (numbers
  unchanged), with the sentence that superselection of r implies nothing within a tower. Within a tower, B - L:
  only the Majorana element changes it among stored terms (one family); Premise (R) protects it; "is the
  descent's and is not produced afterwards given that Premise" is labelled argued and not proved, with what is
  missing (no rate, real breaking for the non-thermal injection, one family). Within a tower, baryon number:
  "cannot be produced afterwards" is not asserted; the 24 slot-pair generators and the anomalous weak
  equilibrium (imported statement, not a stored Fact, used by the mirrors-composition check) are cited. The
  black-hole sentence is kept verbatim.
- Technical, lay, one-liner restated. A paragraph appended to `proof-main.tex` saying what of the restated
  clauses is a naming, what is cited, and what is argued.
- Not changed: `check.py`, `coverage.yaml`. Note for Leon: `check_charge_reading_against_thermal_reading` sets
  the two towers' charges equal, so it tests the equal B - L and not the equality of baryon number; its coverage
  line still quotes "(i) f_2 = 1 at any mirror temperature". A one-line coverage edit (the judge would need to
  re-agree) is recommended, not done.
- Edges not drawn, for Leon to decide: (a) no `uses` edge to
  `synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them`: that claim already `uses` this one
  at @10, so an edge back would close a cycle; the new text cites it by `\claimref` only; (b) no `uses` edge to
  `synthesis.baryon-number-centraliser-in-the-five-mode-algebra`; (c) no `assumes` edge to
  `neutrino.r-descent-reheats-below-lower-heavy`: the sentence resting on it is labelled argued, and an edge
  would change "holds given" for the twelve dependants.

### 1.3 op.matter-asymmetry-origin
- `status`: open -> **partial**. Reason: the file uses `partial` for 20 problems with accepted partial results
  and `open` for problems with none of their own (for example op.strong-cp). The problem is not settled; the
  success clause is unchanged. MAINTAINER.md says the problem "stays OPEN"; if that was meant literally, change
  the one word back.
- `statement`: names the charge as B - L, says how the baryon density relates to it, and says that exact
  conservation is not available so the proof sought is a conditional inheritance of B - L.
- `known`: existing text kept; the "charge of the descent" sentence now records the three objects; channel (a)
  is labelled as production from the other tower. Added items (d) to (h): the exchange is inner and no integer
  state is invariant, orientation must exist, sign a label for the algebra and not for the laws; one chirality,
  flag conjugate antilinear, joint label (orientation, sign of J, arrow) argued; one family, only hypercharge
  survives; exact conservation fails for n_B, n_L and B - L, so the no-go as first worded is false, and the
  store's own check uses a dynamics that produces baryon number; the naming, with the mirror consequence. The
  "not stored" list is rewritten.
- `attack`: item 1 (heavy pair) verbatim. Item 2 (enumerate) kept, with two sentences added saying the
  one-family selection rules are now stored and what remains. Item 3 reworded to the conditional B - L
  inheritance theorem with the premises section F lists. New items (a) anomalous weak process and light
  doublets, (b) Majorana washout with and without (R), (c) rate bound for the 24, (d) the mirror, (e)
  completeness beyond one family. The relaxing-angle item kept verbatim, last.
- `entities`: the four accepted claims added (11 ids; the header says 2 to 8, other entries carry up to 16 and
  the validator does not object).
- `source`: date and decisions appended.
- `success` and `why` not edited. Note: the second branch of `success` ("no stored dynamics after the descent
  can generate or erase it") now reads for B - L; attacker AB recommended rewording it explicitly. Left for
  Leon.

## 2. Dependants

### 2.1 Pins on the raised versions (not repinned)
`dark-matter.stored-asymmetry-charge-not-number@10` is pinned by twelve entities:
synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them, synthesis.no-rule-p2-licenses-gives-the-thickness-of-r3,
simulations.imported-mirror, dark-tower-matter.mirrors-temperature-p2, dark-tower-matter.mirrors-composition,
synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping,
synthesis.mirror-temperature-measures-deposit-under-r, dark-matter.mirror-share-assembled,
synthesis.adiabatic-deposit-modulation-is-a-time-shift, dark-matter.radiation-audit-what-theorem-closes-what,
synthesis.tower-charge-sector-label-temperature-not, pred.no-indirect-dark-signals.
`synthesis.matter-asymmetry-registered-free-input` has no pinned dependant (it is cited unpinned).

### 2.2 The mirror share and the equality "by the copy theorem" (task item 4; nothing edited)

| entity (version, status) | sentence affected | recommendation |
|---|---|---|
| `dark-matter.mirror-tower-copy-one` (v10, proved), (v) | "the asymmetry per mode is equal in the two towers, $\epsilon_{2} = \epsilon_{6}$ ... under them the asymmetry stored in an oriented tower is the charge $Q = \epsilon N$, a sector label of the descent" | scope note: the equality proved is of B - L. Also reword "a sector label of the descent": the sector label is the residue r; Q is a datum of the descent |
| same, (iii) | "with the equal asymmetry per mode of (v) its tower factor is $f_{2} = 1$ up to the ratio of mean mass per baryon of the two sectors" | restatement: "$f_{2} = 1$ up to the ratio of mean mass per baryon, and given that the mirror's baryon number per unit of B - L equals this tower's, which is not shown" |
| same, closing sentence of (v) | "The share of one in (iii) rests on P1, P2, the common ceiling coupling, the charge reading (C$\epsilon$) on the first route, and the copy." | restatement: add the equal ratio to the list. This is the sentence D2 falsifies as written |
| `dark-matter.mirror-share-assembled` (v9, proved) | "$f_{2} = \epsilon_{2}/\epsilon_{6} \cdot n_{2}/n_{6} \cdot m_{2}/m_{6} = 1\cdot 1\cdot 1 = 1$, $\Omega_{\mathrm{mirror}} = \Omega_{b}$, exactly on the proton-only branch"; "(premised on P2.) $\epsilon_{2} = \epsilon_{6}$ by the audit along the same orbit" | restatement: the first factor is one for B - L; for baryons it is the ratio of the two conversion coefficients, a fourth factor with its own standing (open). "Exactly" becomes conditional |
| `dark-matter.mirror-share-one-how-fragile` (v7, proved), (i) | "hence $f_{2} = 1$ under P4, which Theorem ...(v) discharges for the mirror, an isomorphism of theories rather than a one-loop statement"; "So $f_{2} = 1$ is exact, protected by the common-ceiling-coupling premise, and fragile." | restatement: add the second exposure (the conversion ratio); "exact" holds for the mass factor only |
| `dark-matter.population-count-one-share-half-percent` (v7, proved), (i) | "The asymmetric dark matter is the mirror tower's alone ... and its share is exactly one (Theorem ...(iii), assembled ...)" | scope note pointing to the condition; the count itself is untouched |
| `synthesis.common-ceiling-coupling-premise` (v1, postulate) | "the share of one holds given P1, P2 (for the asymmetry ratio), this premise (for the mass ratio) and the copy" | scope note: and the equal conversion ratio |
| `synthesis.dark-to-baryon-total-uses-r1-r2-and-d-only-as-mass-per-unit-ball` (v2, proved) | "Proposition ...(i) gives $f_{2} = 1$ from Premises P1, P2, the common ceiling coupling and the copy of content, with P4 discharged for the mirror" | scope note |
| `dark-matter.unit-ball-rule` (v6, proved) | "The mirror's share of one is derived separately (Proposition ...)" | scope note: derived conditionally |
| `dark-matter.asymmetry-arrow-counted-fifteenth-refutation` (v8, proved), (iii), (iv) | "The value is common to this tower and the mirror by Theorem ...(v), under that clause's premises."; "The count uses only the equality of $\epsilon$ across the reversal orbit ..., not its provenance." | (iii) untouched (true of B - L). (iv): scope note, since the count now also uses the equal conversion ratio |
| `dark-matter.which-towers-are-populated` (v2, conjectured) | "a descent that filled one filled the other, at the same asymmetry" | untouched |
| `dark-matter.d-democracy-total-mass` (v3, postulate) | "the asymmetry is equal in this tower and the mirror by Theorem ...(v)" | untouched |
| `synthesis.mirror-asymmetry-route-one` (v4, proved), (ii) | "gives $\epsilon_{2} = +\epsilon_{6}$ exactly when the mirror is oriented by $\Phi W$" | untouched (a statement about the sign of the inherited datum) |
| `synthesis.indifference-is-curie-plus-single-valuedness` (v1) | "common asymmetry per mode" as an instance of P2 | untouched |
| notes `note.dark-matter.setting-predictions-collected` (v3: "The mirror share is exactly one"), `setting-levels-results` (v2), `setting-contribution` (v1) | the paper's running text | untouched as records of the paper; a note comment if Leon wants the site to show the condition |

The first prediction of the dark-matter paper (the mirror share exactly one, hence one of the 5.364 units) is the
physical consequence: with D2 it is conditional until attack item (d) is done.

### 2.3 Stored text that asserts baryon number specifically is inherited, conserved or equal (nothing edited)

| entity (version) | sentence | recommended wording |
|---|---|---|
| `synthesis.adiabatic-deposit-modulation-is-a-time-shift` (v2) | "the charge reading ..., under which the deposited charge is fixed by the descent's data independently of the tower's temperature and the mirror carries the same baryon charge as this tower" | "... and the mirror carries the same charge B - L as this tower". Its use of "charge per unit entropy uniform" then concerns (B - L)/s; baryon isocurvature follows only through a uniform c |
| `synthesis.baryon-number-centraliser-in-the-five-mode-algebra` (v1, accepted today), Reading | "that an element of the mode algebra commuting with $n_{B}$ is a dynamics conserving the baryon charge, and so that the charge is inherited on that class, is the reading (argued)" | "... and so that baryon number, which is not the inherited charge by the decision of 12 November, is unchanged on that class" |
| `synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them` (v1, accepted today), Reading | "Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number} speaks of baryon number. On (vi) these are reconciled only if the datum of the descent is the total $B - L$" | "... spoke of baryon number at version 10 and names the charge as B - L from version 11"; its pin is @10, so a repin with this wording |
| `dark-matter.open-channels-their-costs` (v6) | "A cold mirror with our baryon number is what the framework predicts once that seeded temperature is taken as a free datum of the descent" | "A cold mirror with our B - L, and with our baryon number if its conversion ratio equals ours, ..." |
| `dark-tower-matter.mirrors-composition` (v3) | "the Fermi energy its baryon number must carry exceeds the floor's thermal deposit by 49 to 84 ... for a copied lepton number $L \leq 0$ (our tower's sphaleron value $L/B = -51/28$, or zero)" | scope note only (D3: the check is not to change): the mirror's baryon number is taken equal to ours and L as copied; with B - L the copied datum both are conditional, and this is the computation attack item (d) must redo |
| `simulations.imported-mirror` (v6); `dark-matter.stored-asymmetry-charge-not-number` (iii) (not restated) | "its baryon-to-photon ratio is $\eta' = \eta/\xi^{3}$"; "With $\eta$ ... and equal baryon number" | scope note: equal baryon number is the conditional of (i); in my entity it is covered by the sentence added to (i) |
| `dark-matter.coefficients-floors-they-give-what-gravity` (v4) | "(the same energy per unit of baryon number either way)" | untouched (energy bookkeeping; the hot-deposit estimate is per unit of baryon number in the source) |
| `note.dark-matter.setting-r1-r3-d-attacked-unit` (v1); `note.dark-matter.what-rule-has-has-not` (v1) | "this tower's filling is set by baryon number, a conserved charge the odd towers cannot carry" | "... set by baryon number, which the odd towers cannot carry" (drop "a conserved charge"), or untouched as the paper's text |
| `dark-matter.asymmetry-arrow-counted-fifteenth-refutation` (v8) | no sentence at any level names baryon number as the inherited charge; it speaks of "its asymmetry" and $\epsilon$ | one sentence in the 2026-11-01 note of (iv): "the registered datum is named as B - L from version 5 of the Premise" |
| `dark-matter.superselected-hence-dark-exactly-stable` (v5), step 1 | "The tower charge $r$ is superselected in the frozen phase" | untouched; it is already about r. Both attackers asked for a clause "r is the residue label, not a charge within a tower"; optional |
| `neutrino.r-descent-reheats-below-lower-heavy` (v1) | "the descent's $B - L$ is untouched" | untouched; now the stored source of the protection |

## 3. Other content consequences
- `dark-matter.radiation-audit-what-theorem-closes-what`, `dark-tower-matter.mirrors-temperature-p2`,
  `synthesis.mirror-temperature-measures-deposit-under-r`, `synthesis.tower-charge-sector-label-temperature-not`,
  `synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping`,
  `synthesis.no-rule-p2-licenses-gives-the-thickness-of-r3`, `pred.no-indirect-dark-signals`: they use the charge
  reading (temperature independence, the common N) or clause (iii), none of which changed. Expected: repin
  after a look, no content change. `synthesis.mirror-temperature-measures-deposit-under-r` speaks of energy
  "per unit charge"; its hot-deposit arithmetic uses n_B/s, so with the datum (B - L)/s the estimate of xi moves
  by the fourth root of 1/c (about 1.3); worth a scope note.
- The dark-to-baryon total: the mirror's one unit of the 5.364 is conditional until attack item (d).

## 4. Not done, and why
- The anomalous weak process and c are not imported (D3). No number is registered for (B - L)/s.
- The stored check of `dark-tower-matter.mirrors-composition` is unchanged (D3).
- No edit to any entity in sections 2.2 and 2.3 (task item 4: list only).
- No edges added to the charge Proposition (cycle with the abelian-charges claim; see 1.2).
- `coverage.yaml` of the charge Proposition not edited (see 1.2).
- `success` of the open problem not reworded (see 1.3).
- No commit, no repin, no lock, no build.

# Second pass (Leon's decisions of 12 November 2026 on the mirror share)

Decisions applied: (1) the results stating `f_2 = 1` as exact are restated as conditional; scope notes on the
dependants; the 5.364 total is said to be conditional wherever a restated result or note touches it, no number
changed. (2) `partial` for op.matter-asymmetry-origin is confirmed (no edit needed). Nothing committed by me,
nothing repinned.

The condition is named the same way in the three restated results, one labelled paragraph with identical wording:

> *Hypothesis (equal conversion).* The mirror's ratio of baryon number to B - L equals this tower's. It is not
> shown, and it is a stated hypothesis of this result, not a registered premise: the inherited charge is the
> total B - L, and the copy equates the two towers' B - L, not their baryon number (Proposition
> dark-matter.stored-asymmetry-charge-not-number (i), version 11). The mirror's unit of the observed
> dark-to-baryon total 5.364 is conditional on it.

No assumes edge was added and the validator did not ask for one.

## S1. Restated (version + 1, amendments entry kind restatement, credit entry, extraction entry)

| entity | version | what changed |
|---|---|---|
| `dark-matter.mirror-tower-copy-one` | 10 -> 11 | (iii): `f_2 = 1` and `Omega_mirror = Omega_b` under the Hypothesis; (v): the equality proved is of B - L, the Hypothesis added to what the share of one rests on; technical, lay, one-liner; two sentences of the proof |
| `dark-matter.mirror-share-assembled` | 9 -> 10 | opening, (iii), (iv): the product is one under the Hypothesis, the asymmetry factor is one as a ratio of B - L; technical, lay, one-liner; two sentences of the proof |
| `dark-matter.mirror-share-one-how-fragile` | 7 -> 8 | (i): `f_2 = 1` under the Hypothesis; (ii) closing sentence: "exact" now said of the mass factor; level line; technical, lay, one-liner; first sentence of the proof |

Only three results were restated: the brief says "the four results" and then names three entities (the copy
theorem's two clauses make the fourth sentence). `dark-matter.population-count-one-share-half-percent` ("its share
is exactly one") got a scope note, as listed in the brief; if it was meant as the fourth restatement it is a
small edit to (i).

Kept on purpose: in (v) of the copy theorem the words "a sector label of the descent" stay, because the audit
of P2 runs on sector labels; a parenthesis now says the charge is the total B - L, not the residue label r and
not baryon number. My first-pass recommendation to reword that phrase is withdrawn.

Checks of the three: none asserts the asymmetry factor. They compute the mode ratio, the mean-mass ratio
(0.995), the one-loop factors and the coupling window; their labels speak of the mass factor of `f_2`, which the
restated statements keep. No check, label or coverage line of the three was edited. `check4` on each: pass.

## S2. Scope notes (version kept, formal text untouched; `extraction.maintainer_pass_2026_11_12`)

`dark-matter.population-count-one-share-half-percent`, `synthesis.common-ceiling-coupling-premise`,
`synthesis.dark-to-baryon-total-uses-r1-r2-and-d-only-as-mass-per-unit-ball`, `dark-matter.unit-ball-rule`,
`synthesis.adiabatic-deposit-modulation-is-a-time-shift`, `dark-matter.open-channels-their-costs`,
`dark-tower-matter.mirrors-composition` (check unchanged), `simulations.imported-mirror`,
`synthesis.mirror-temperature-measures-deposit-under-r` (the xi factor of about (1/c)^(1/4), roughly 1.3, is
written as an estimate, not computed in the store and not checked),
`dark-matter.asymmetry-arrow-counted-fifteenth-refutation`.

Deviation, the fifteenth refutation: the brief asked for a one-sentence pointer in its note with the version
kept. The note is part of the formal text, and the validator refused the added sentence there (E206,
"substantive fields changed without a version bump"). I removed the sentence and put the pointer in the
extraction note, version 8 kept. If Leon wants it visible in the formal note, that needs version 9 with an
amendments entry and one more lagging pin set.

These notes live in the extraction block, so they are in the record and not in the rendered statement. A
reader of the site sees the condition only on the three restated results and on the charge Proposition.

## S3. Wording fixes in today's accepted claims (version 1 kept, pins not moved)

- `synthesis.baryon-number-centraliser-in-the-five-mode-algebra`, Reading: "is a dynamics conserving the baryon
  charge, and so that the charge is inherited on that class" -> "is a dynamics conserving baryon number, and so
  that baryon number is unchanged on that class", with a parenthesis that the inherited charge is B - L from
  version 11 of the charge Proposition.
- `synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them`, Reading: "speaks of baryon number"
  -> "spoke of baryon number at version 10, the version used here; from version 11 it names the charge as the
  total B - L and keeps the three objects apart"; and "the stored sentence ..." -> "the sentence of version 10
  ..., and version 11 is restated so".
The validator accepted both at version 1.

## S4. Coverage of the charge Proposition

`dark-matter.stored-asymmetry-charge-not-number/coverage.yaml`, `check_charge_reading_against_thermal_reading`:
the clause quoted is now "(i) the mirror carries the same charge Q = eps N (the total B - L) at any mirror
temperature", and `omits` says the check tests the equal B - L only and does not touch the equality of baryon
number. **The judge has not re-agreed**: the `judge` block still carries the verdict of 2026-10-23 on the old
line, and the `omits` text says so. `check.py` unchanged; `check4`: pass.

## S5. Pins that now lag (not repinned)

- `dark-matter.stored-asymmetry-charge-not-number@10` (now 11), twelve: dark-matter.mirror-share-assembled,
  dark-matter.radiation-audit-what-theorem-closes-what, dark-tower-matter.mirrors-composition,
  dark-tower-matter.mirrors-temperature-p2, pred.no-indirect-dark-signals, simulations.imported-mirror,
  synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them,
  synthesis.adiabatic-deposit-modulation-is-a-time-shift, synthesis.mirror-temperature-measures-deposit-under-r,
  synthesis.no-rule-p2-licenses-gives-the-thickness-of-r3,
  synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping,
  synthesis.tower-charge-sector-label-temperature-not.
- `dark-matter.mirror-tower-copy-one@10` (now 11), twenty-one:
  dark-matter.asymmetry-arrow-counted-fifteenth-refutation, dark-matter.coefficients-floors-they-give-what-gravity,
  dark-matter.mirror-share-assembled, dark-matter.mirror-share-one-how-fragile,
  dark-matter.mode-counts-two-modules-which-one, dark-matter.no-coupling-rule-odd-towers-follows,
  dark-matter.open-channels-their-costs, dark-matter.population-count-one-share-half-percent,
  dark-matter.radiation-audit-what-theorem-closes-what, dark-matter.stored-asymmetry-charge-not-number,
  dark-tower-matter.mirrors-composition, dark-tower-matter.mirrors-temperature-p2,
  odd-extensions.imported-copy-theorem-soldered-residue,
  standard-model.imported-sectors-superselection-mirror-copy, simulations.imported-mirror,
  synthesis.dimmed-burst-time-rescaled-copy,
  synthesis.field-strength-heat-kernel-coefficients-of-the-dark-towers-fix-no-scale-ratio,
  synthesis.gauge-algebra-by-tower, synthesis.mirror-asymmetry-route-one,
  synthesis.mirror-temperature-measures-deposit-under-r, synthesis.tower-charge-sector-label-temperature-not.
- `dark-matter.mirror-share-one-how-fragile@7` (now 8), five: dark-matter.mirror-share-assembled,
  dark-matter.population-count-one-share-half-percent, dark-tower-matter.r1-has-no-mechanism-odd-towers,
  simulations.imported-mirror, synthesis.dark-to-baryon-total-uses-r1-r2-and-d-only-as-mass-per-unit-ball.
- `dark-matter.mirror-share-assembled@9` (now 10): no pinned dependant.
- `synthesis.matter-asymmetry-registered-free-input@4` (now 5): no pinned dependant.

The restated results lag on each other: the assembled share pins the copy theorem @10, the fragility result @7
and the charge Proposition @10; the fragility result pins the copy theorem @10; the charge Proposition pins the
copy theorem @10. Their new text cites the charge Proposition "version 11" in words while the assembled share's
edge stays at @10. Content to look at on repin, beyond the entities already noted: the two imported restatements
of the copy theorem (`odd-extensions.imported-copy-theorem-soldered-residue`,
`standard-model.imported-sectors-superselection-mirror-copy`) and `simulations.imported-mirror`, if they repeat
the share of one.

## S6. Left open
- The equality of the two conversion ratios: attack item (d) of op.matter-asymmetry-origin, unchanged.
- The notes that carry the paper's running text ("The mirror share is exactly one" in
  `note.dark-matter.setting-predictions-collected`, and the like) were not in the brief and are untouched.
- Edges on the charge Proposition, the `success` clause of the open problem: as in the first pass.
