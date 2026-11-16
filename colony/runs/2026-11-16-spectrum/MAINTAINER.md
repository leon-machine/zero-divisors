# Maintainer pass after run 2026-11-16-spectrum (acting for Leon, the maintainer)

Leon has accepted the run's five proposals (now in store/claims/):
  P1 synthesis.descent-slice-constraints-and-the-three-readings-of-a-white-deposit            (new, v1)
  P2 synthesis.quasi-free-deposit-has-white-energy-noise-unless-pure-and-stationary            (new, v1)
  P3 synthesis.exchangeable-deposits-carry-two-numbers-and-no-spectral-shape                   (new, v1; ids kept)
  P4 synthesis.sparse-fermion-deposit-reaches-the-amplitude-on-a-flat-slice-only-with-super-planckian-quanta (new, v1)
  P5 synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise                                    (v4 -> v5, restatement)
and made these decisions on 16 November 2026:
  D1. The descent slice is left free. No reading is adopted: the slice's expansion datum (its local density
      parameter) is a free datum of the descent. (UE) and (LC), and the flat-slice readings (FR) and (FM), are
      named hypotheses, never premises. Stored results that need a reading name it as a hypothesis.
  D2. The ceiling on the descent temperature under (UE), roughly 1e9 GeV, is a conditional remark inside P1 (already
      there), and an attack item is added to op.descent-state-and-spectrum for the proper analysis of the largest
      observed scales.
  D3. Reword the four stored entries that use or imply the flat-slice reading without naming it (list below).
  D4. "Deposit quanta lie below the Planck mass" is Hypothesis (QP) of P4 only, not a clause of the
      Hadamard-deposit premise.
  D5. The ids of P3 and P4 are kept.
The open problem op.descent-state-and-spectrum is NOT settled and keeps its status (reformulated): the series still
records no mechanism for the measured spectrum.

You are the one maintainer agent of this pass. Edit store/ directly in LAB = /home/claude/phys-graph (branch
run/2026-11-16-spectrum). Never spawn agents, never commit or push, never touch anything outside LAB. You are not
blind: read verify/R1.md (the referee's report, in particular "Overlaps and conflicts" and "Not covered by any
proposal"), findings/attack-SA.md, findings/attack-SB.md, findings/fixes-SA.md and findings/fixes-SB.md of this run
for the material and for the "Repin on acceptance" lists.

## Work
M1. Edges and pins among the accepted results (routine, listed by the fixers under "Repin on acceptance"):
    - P1, P2, P3, P4 pin synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise at version 4 where they use it:
      move the pins to version 5 (no content change; check each text that describes "the version-4 wording" still
      reads correctly, and where P1 clause (vii) describes the stored clause (iv), make it say what version 5 now
      states: the comparison holds under (FR)).
    - Add P1 to `derivations.uses` of P2, of P4 and of P5 (each rests on P1's conversion), and turn the
      "filed alongside, <id>" phrases in P2, P4 and P5 into \claimref{...} to P1. Check for cycles first (P1 cites
      the quasi-free result; if P1 `uses` it, P5 cannot `use` P1: then keep the claimref in text only and say so in
      your report). Do not add any `assumes` edge.
    - P2 names its 9/4 variant "(UE_Phi)": keep the name unless it clashes with notation.
M2. D3, wording only, the least that carries the decision; no number, status or premise list changes:
    (a) synthesis.adiabatic-deposit-modulation-is-a-time-shift: name its flat-patch hypothesis as (LC) and say that
        a patch has a fourth local datum, its curvature (equivalently the slice's expansion datum), which the
        result sets to zero by hypothesis; point to P1.
    (b) synthesis.finite-range-descent-deposit-cannot-seed-cmb: the bound is about a zeta of finite range. Where
        the text says a deposit of finite range (thermal, pairs across a horizon) gives index 3, say "a deposit
        whose zeta has finite range", and add one sentence: whether a matter deposit of finite range has a zeta
        of finite range depends on the slice datum (P1): under (FR) it does; under (FM) the index is +1; under (UE)
        the zeta is the potential of the matter excess, of infinite range, index -1. Write the reduced Planck mass
        as the store's notation has it where the text writes M_P for the reduced value (check store/notation.yaml;
        if there is no macro for the reduced mass, say "reduced Planck mass" in words).
    (c) synthesis.holographic-thermal-fluctuations-fall-short-in-the-descent-window: one note that the conversion
        it takes from the string-gas Fact is the (UE) conversion of P1, so its verdict and the quasi-free clause
        (iv) (under (FR)) read the same white noise through different slice data.
    (d) store/open_problems.yaml, op.descent-state-and-spectrum:
        - `known`: add a dated paragraph "Results and Leon's decisions of 16 November" stating: the slice datum and
          the constraint (P1); the three readings and their indices (-1 under (UE), +1 under (FM), +3 under (FR));
          the thermal deposit's amplitude under (UE) at the pivot (the brackets P1 states, including A_s near
          3.6e9 to 3.7e9 GeV and "not a perturbation" at 1e12 GeV) and the rough conditional ceiling; that no
          stored premise selects a reading (argued) and none is adopted (D1); P2 (white energy noise unless pure
          and stationary; the filled ball gives n_s = 1 exactly under (UE), a miss at 8.3 to 8.4 sigma, amplitude
          short by more than 1e17 on the window, and the stored deposit is mixed (argued)); P3 (exchangeable
          deposits, with its two white cases and its boundary); P4 (attack item 3 closed on flat slices under
          Hypothesis (QP), open under (UE)). Qualify the earlier sentences of `known` that state "index 3", "below
          1e-77 at the pivot" or "finite range gives 3" with "(under (FR))" or the precise reading, changing as
          little as possible. Add three rows to the ledger sentence of the 10 November paragraph or state them in
          the new paragraph: -1, +1 and 0 (the last for a deposit the stored state rules do not produce).
        - `attack`: mark item 3 (sparse or energetically broad quasi-free deposits) as closed on flat slices under
          (QP) and open under (UE); add two items: (i) "The slice datum: find what in the series fixes the
          expansion datum of the descent slice (a locality premise would select (LC); a junction rule at the join
          would fix the slice data), without fixing it in order to obtain a spectrum"; (ii) "Under (UE), carry out
          the analysis of the largest observed scales that turns the rough ceiling on the descent temperature,
          near 1e9 GeV, into a bound with a stated confidence."
        - `entities`: add P1, P2, P3, P4. `source`: append "the slice-datum results and Leon's decisions of
          16 November". Status unchanged.
        The statement's sentence "a deposit set by the frozen point reads the observed modes as inside its horizon
        and gives the vacuum's spectrum" stays.
M3. The open problem op.deposit-state-is-hadamard mentions "op.descent-state-and-spectrum" and the infrared datum:
    read it and add at most one sentence if (and only if) one of its statements now needs the (FR) qualifier.
M4. Anything the referee listed under fixes that the fixers could not do because it needed store edits.

## Rules
- Read CONTRIBUTING.md, docs/CONTRIBUTING-rules.md and `python3 colony/labcli.py conventions '{}'`; copy the format
  of existing entities and of the open-problem file's header comment.
- Changing an existing entity: version + 1 when a statement level changes; keep every file in its folder
  (orig-proof-main.tex in particular); add an `amendments` entry {version, kind: correction | restatement, defect,
  evidence?} and a credit entry {name: Claude Fable 5.2, role: <what changed>, version: <new>, source: maintainer
  pass 2026-11-16 (spectrum)}, keeping every existing credit entry unchanged; add under `extraction` an entry
  `maintainer_pass_2026_11_16: {by: maintainer-2026-11-16, date: '2026-11-16', note: <one or two sentences>}`.
  Keep `proposed_by` as it is. A change confined to pins, uses edges or a note keeps the version (follow what the
  stored entities did in earlier passes if the tool demands otherwise).
- Change the least that carries the decision. Do not strengthen any statement. Label argued as argued.
- House style: no em dashes; never "honest"/"honestly"; never "load-bearing"; Q(v) for the square of a vector;
  macros only from store/notation.yaml; no mention of agents, runs or method names in store text (changelog `by:`
  and `source:` fields excepted). Geometric algebra and Gauge Theory Gravity language; declare outside_ga where
  needed.
- Exact arithmetic in any check you touch (you should not need to touch any); if you do, run
  `python3 colony/runcheck.py <folder>/check.py` then `python3 colony/check4.py <folder>` (one at a time).
- Validation: after your edits run
  `python3 -m tp check --store store --layers 1,2,3 --keep-going --author leon 2>&1 | tail -40`
  and fix every error or new warning on the entities you edited (pin warnings on dependants of entities whose
  version you raised are expected: list them, do not repin). Do not run the full check, `tp repin`, `tp lock`,
  `tp build` or the site build.
- Write colony/runs/2026-11-16-spectrum/maintainer-M1.md: every entity changed with old -> new version and one line
  each; dependants whose CONTENT (not just pins) may be affected; anything you could not do and why. Your final
  reply: a short summary of that file.
