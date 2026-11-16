# Maintainer pass M1, run 2026-11-16-spectrum

Items M1 to M4 of MAINTAINER.md, carried out in `store/` on branch run/2026-11-16-spectrum. Nothing committed.
No check.py edited, no number, status or premise (`assumes`) list changed, no id or title changed.

Validation: `python3 -m tp check --store store --layers 1,2,3 --keep-going --author leon` ends at
0 errors, 0 warnings (122 information findings: 120 I213, 1 I126, 1 I305, as before the pass apart from the
I305 count). Layer 4, `tp repin`, `tp lock`, `tp build` and the site build were not run, as instructed. The
background layer-4 run started before these edits and has not seen them; no check file changed, so its
verdicts on the checks stand, but its premise-coverage findings for P2 and P4 predate their new uses edge.

Short names below: P1 = synthesis.descent-slice-constraints-and-the-three-readings-of-a-white-deposit,
P2 = synthesis.quasi-free-deposit-has-white-energy-noise-unless-pure-and-stationary,
P3 = synthesis.exchangeable-deposits-carry-two-numbers-and-no-spectral-shape,
P4 = synthesis.sparse-fermion-deposit-reaches-the-amplitude-on-a-flat-slice-only-with-super-planckian-quanta,
P5 = synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise.

## Entities changed

| Entity | Version | What changed |
|---|---|---|
| P1 | 1 -> 1 | Pin to P5 moved 4 -> 5. Clause (vii) and the proof's (vii) now say the unconditional reading of clause (iv) is the version-4 wording and that version 5 states the comparison with A_s and the index under (FR). |
| P2 | 1 -> 1 | Pin to P5 moved 4 -> 5. `uses` edge to P1@1 added. "filed alongside, <id>" in clause (iv) and in the proof turned into `\claimref` to P1; extraction note updated. coverage.yaml lists P1 under `untouched_premises` with a reason. (UE_Phi) kept: no clash with store/notation.yaml or with any other stored letter. |
| P3 | 1 -> 1 | Pin to P5 moved 4 -> 5. Nothing else. |
| P4 | 1 -> 1 | Pin to P5 moved 4 -> 5. `uses` edge to P1@1 added. "filed alongside" phrases in clause (iv), the technical level and the proof turned into `\claimref` to P1; extraction note updated (also its "the reading the stored clause uses at its version 4", now "used unnamed at its version 4 and names at its version 5"); the proof's "enter as hypotheses" now reads "which reading holds is a hypothesis", since the coefficients come from a declared premise. coverage.yaml lists P1 under `untouched_premises`. |
| P5 | 5 -> 5 | "filed alongside, <id>" in the conversion note and in the proof turned into `\claimref` to P1. No `uses` edge (see "Could not do"). coverage.yaml wording only. |
| synthesis.adiabatic-deposit-modulation-is-a-time-shift | 2 -> 3 (restatement) | D3(a). The flat patch is named Hypothesis (LC), a hypothesis of the result and not a premise, in the formal statement, the technical level, the one-liner and the proof; the patch's curvature (equivalently the slice's expansion datum, left free) is recorded as a fourth local datum set to zero by that hypothesis; `\claimref` to P1, no edge. |
| synthesis.finite-range-descent-deposit-cannot-seed-cmb | 5 -> 6 (restatement) | D3(b). Closing sentence of the formal statement now speaks of "a deposit whose zeta has finite range", plus one sentence: whether a matter deposit of finite range has such a zeta depends on the slice datum (it does under (FR); index +1 under (FM); under (UE) the zeta is the potential of the matter excess, of infinite range, index -1), with `\claimref` to P1, no edge. Same qualifier at the technical and lay levels, the one-liner and the extraction note. Proof: "reduced Planck mass" said in words at the second place where M_P is the reduced value (the first already said it). |
| synthesis.holographic-thermal-fluctuations-fall-short-in-the-descent-window | 2 -> 2 | D3(c). One marked note at the technical level: the string-gas conversion is the reading (UE) of P1 (variant (UE_Phi) of P2), a hypothesis here, so the extensive-capacity index -1 here and the index 3 of P5's clause (iv) under (FR) are the same white noise read through different slice data. |
| store/open_problems.yaml, op.descent-state-and-spectrum | status unchanged (reformulated) | D3(d), D1, D2, D4. See below. |
| store/open_problems.yaml, op.deposit-state-is-hadamard | status unchanged (open) | M3: one parenthesis after "a finite-range deposit cannot seed the CMB": the bound is on a zeta of finite range, which a matter deposit of finite range has under (FR) of P1; the series leaves the slice free. Nothing else in that problem needed the qualifier. |

Every changed entity carries `extraction.maintainer_pass_2026_11_16`. The two raised entities carry an
`amendments` entry (kind restatement, since the formal level changed) and a credit entry (Claude Fable 5.2,
version, source: maintainer pass 2026-11-16 (spectrum)); every earlier credit entry is unchanged.

### op.descent-state-and-spectrum, in detail
- `source`: appended "the slice-datum results and Leon's decisions of 16 November".
- `known`, earlier sentences qualified, each by a few words: the finite-range bound is stated for a deposit
  whose zeta has correlations of range R; "finite range ... gives n_s - 1 -> 3" is for a zeta of finite range
  (a matter deposit has one under (FR), not under (UE)); "finite range gives 3" in the slice-correlator sentence
  is "finite range of zeta"; the hot half-KMS members are "of finite range in zeta under (FR)"; the shot term
  below 1e-77 is "of the contrast", read as the curvature perturbation under (FR) (both places); attack lines 1
  and 2 are closed for dense quasi-free deposits "under the flat-slice readings"; (viii) names Hypothesis (LC).
  The Kasner sentences that say "index 3" were left alone: they are mode-equation indices, not the flat reading.
- `known`, new paragraph "Results and Leon's decisions of 16 November": the constraint and the slice datum (P1);
  the three readings with indices -1, +1, +3; the thermal brackets under (UE) (1 MeV, the 7.3e8 GeV ceiling,
  A_s between 3.6e9 and 3.7e9 GeV, 12 to 13 at 1e12 GeV and "not a perturbation"); the rough conditional ceiling
  near 1e9 GeV; the (FM) bound 4e-41; that (vii)'s conversion is (UE); no premise found that selects a reading
  (argued) and none adopted (D1); P2; P3 with its two white cases and its boundary; P4 with (QP) as a hypothesis
  of that result only; the three ledger rows -1, +1 and 0; the position unchanged, no mechanism.
- `attack`: item 3 marked closed on flat slices under (QP) and open under (UE); two items added (the slice
  datum; the analysis of the largest observed scales under (UE)), in the brief's wording.
- `entities`: P1, P2, P3, P4 added (12 in all; the validator sets no upper limit, other problems list up to 16).
- The statement is untouched, including the sentence on the frozen point's deposit.
- The file had no trailing newline and still has none.

## Dependants not repinned (listed, as instructed)
Layers 1 to 3 raise no warning for a pin below the current version, so these do not show in the check output.

Pinned to synthesis.finite-range-descent-deposit-cannot-seed-cmb@5 (now 6):
standard-model.dating-descent, synthesis.adiabatic-deposit-modulation-is-a-time-shift, P1, P2, P3, P4, P5,
synthesis.frozen-point-geometry-reads-descent-as-vacuum,
synthesis.kasner-approach-gives-horizon-exit-and-index-three,
synthesis.pati-salam-chain-defects-cannot-source-spectrum,
synthesis.red-tilt-criterion-on-power-law-stages-and-the-index-ledger-of-the-stored-sources.

Pinned to synthesis.adiabatic-deposit-modulation-is-a-time-shift@2 (now 3): none (it is cited by claimref only).

Still pinned to P5@4 (raised to 5 by the run, not by this pass; outside M1's list):
synthesis.adiabatic-deposit-modulation-is-a-time-shift,
synthesis.local-conversion-cannot-redden-a-gaussian-spectator,
synthesis.kasner-hidden-scale-coupled-scalars-stay-blue,
synthesis.deposit-over-the-conformal-vacuum-is-hadamard-exactly-when-every-occupation-moment-is-finite.

## Dependants whose content, not only the pin, may be affected
1. synthesis.frozen-point-geometry-reads-descent-as-vacuum: clause on the three classes and its proof call a
   hot half-KMS member "a thermal deposit of finite range, the stored bound's class ... index 3". That is the
   passage from a matter deposit to zeta, the reading (FR), unnamed. Not among the four entries of D3; left
   untouched. It needs the same few words when its pin is reviewed.
2. synthesis.pati-salam-chain-defects-cannot-source-spectrum, clause (iv) and proof: deposited monopoles as "a
   deposit whose correlations have finite range, the class bounded by" the finite-range Theorem. Same passage,
   same remark.
3. P1, clause (vii): it describes the finite-range result "(version 5)", the time-shift result "(version 2)" and
   the holographic result "(version 2)". Those descriptions stay accurate for the versions named. When P1 is
   repinned to finite-range@6, (vii) should add that version 6 states the closing sentence for a zeta of finite
   range and that the time-shift result names (LC) at version 3.
4. synthesis.adiabatic-deposit-modulation-is-a-time-shift, proof, Setting: "below 1e-77 at the pivot for dense
   deposits; a deposit that carries the measured amplitude must therefore contain a classical component" rests
   on P5's comparison with A_s, which version 5 states under (FR) (it survives under (FM); under (UE) the
   thermal deposit reaches A_s near 3.6e9 GeV, with the wrong index). Its pin to P5 stays at 4; the sentence
   needs "(on a flat slice)" or similar when that pin is reviewed. I did not touch it: outside item (a).
5. P3, clause (ii), and synthesis.kasner-approach-gives-horizon-exit-and-index-three use "the finite-range class"
   for a white spectrum of a matter observable or of a spectator field. P3's last formal sentence already says
   the conversion to zeta is not decided there; the Kasner result is a mode-equation index. Low risk; listed
   for the pin review.
6. The other dependants use clauses (i) to (iv) of the finite-range result (the bracket of X, no exit after the
   descent, the comoving length), which are unchanged: P2, P4, P5, standard-model.dating-descent, the red-tilt
   criterion, and the time-shift result's clause (iii) (a delay field is zeta itself).

## Could not do, or chose not to, and why
- P5 `uses` P1: not added. P1 uses P5 (clause (vi) and the check), so the edge would close a cycle. P5 cites
  P1 by `\claimref` in the note and the proof only, as the brief foresaw.
- New uses edges and the checks: P2's and P4's check.py do not call `premise()` on P1, and I did not edit them
  (no brief item forces it). The edge is excused in each coverage.yaml under `untouched_premises`, which is
  what layer 4 accepts in place of W405. Layer 4 was not run by me, so this is unconfirmed by a run.
- Reduced Planck mass in the finite-range result: store/notation.yaml has no macro for it, so the proof says
  "reduced Planck mass" in words and keeps the symbol M_P, as the brief directs. The referee asked for
  \bar M_P, which P1, P2 and P4 write as plain LaTeX; changing the symbol is a one-line edit if preferred.
- Holographic note: placed at the technical level so that the version stays at 2 (a note at the formal level
  changes the substantive hash and would force version 3, as in the pointer notes of earlier passes). The
  formal statement already opens with "Assume the conversion ...", so nothing at the formal level was unnamed.
- Title and id of the finite-range result ("A finite-range descent deposit cannot seed the measured amplitude")
  kept: not asked, and the id is in use across the store.
- M4: the referee's store-edit items are all covered above (pins, P1's clause (vii), the citation of P1 from
  P5, the finite-range closing sentence, the open problem's text, the reduced-mass notation). The literature
  the attackers cite from memory (Zel'dovich and Peebles, Magueijo and Pogosian, Tod, York, Torquato, Gioev and
  Klich, the Planck running) is used in no proof step; no import was created.
- op.pre-descent-theory says the spectrum's carrier is "forced out of the dense quasi-free class". That
  conclusion stands in all three readings for a deposit with a white term (P5 version 5), so it was left.

## Scratch
colony/runs/2026-11-16-spectrum/work/M1/: `edit_open_problems.py` (the exact replacements made in
store/open_problems.yaml; it asserts every match is unique and will not run twice) and
`open_problems.before.yaml` (the file before the pass).
