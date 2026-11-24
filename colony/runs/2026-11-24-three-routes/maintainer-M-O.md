# Maintainer M-O, run 2026-11-24-three-routes

Files changed: store/open_problems.yaml (ten records, targeted edits, 570 lines added, 37 removed) and
colony/runs/LEDGER_HISTORY.md (one line). Nothing else touched. Open-problem records carry no version number;
"version" below is therefore the record's status after the pass. Every statement about the seven results was
taken from the stored entities (entity.md, and proof-main.tex for the wall-conjugation Reading); what comes from
the run's findings only is labelled in the records as "working notes of 24 November, not stored" with its label
(argued / computed / conjectured). No agent, run or method name is in the store text.

## Records changed

| Record | Status after | Change |
|---|---|---|
| op.positivity-of-values | open (unchanged) | `why` restated: (P) is the only stored premise about values but not the least condition for the bound, which needs only (CP). `known`: paragraph "(24 November, second pass.)" with the parity-even corollary, (RP) and D1, the (CP) certificate, the reversal on one party (argued on the scope of two fixed parties; fragile), and three unstored findings with labels. Attack: item 1 narrowed further; parity item gets the "two modes only" sentence; item of 18 November on additive weights gets a pointer; the "which projectors" item prefixed "Answered in part (24 November)" with the fork recorded per D1; split item gets the part answer on (N+) (route 5b); two new items (flag-sector form of (RP) with the exact test at three modes; non-negative local record weights at every number of copies, conjectured). `source` extended; three new ids in `entities`. |
| op.gravitational-field-at-null-momentum | partial (was reformulated) | Statement restated for D2: the requirement is met at first order by the adopted Premise (TT), cited by `\claimref`; what the lattice model shows (sufficiency in a model) and what stays open. `why`: one dated sentence. `known`: paragraph "(24 November.)" with the lattice model (all counts, lattice cone against unit-speed cone, dipole obstruction, recoil partner argued and not modelled), the composites result, the two ways, the decision with its grounds and limits, the burst ratio with the Reading's proviso, the recording route (argued, not stored). Attack: the lattice-Maxwell item gets "(24 November: done at first order ...)"; the burst-baseline item prefixed "Answered (24 November)"; new items "Closed negatively on a generator" (1b, with what is left), "Closed negatively" (1c, argued, not stored), and "New: what stays open under (TT)" (a) to (e). `source` extended; three ids added to `entities`. Not moved to open_problems_settled.yaml. |
| op.einstein-from-the-field-theory | open (unchanged) | `known`: paragraph "(24 November.)": (TT) settles nothing here but opens the helicity-two coupling route; the response way; bridge entries B1 (Clausius takes the stress as an expectation value and as given; the anomalous stress as a matter-independent term) and B2 (weights 3, 9, 36 against 1, 3, 12; 888 = 296 units; no pole without the induced Einstein-Hilbert term), labelled argued, with the arithmetic marked as not a stored result. Attack: four new items (3a under (TT); the response way; 3b; 3c). `source` extended; two ids added to `entities`. |
| op.graviton-rate-as-classical-field-process | partial (unchanged) | `known`: one dated sentence: the rate is at non-null momentum and does not depend on (TT); the statement's "no such quantum" sentence is superseded at first order; texts naming a graviton restated on the decision; burst ratio. |
| op.deposit-state-is-hadamard | open (unchanged) | `known`: paragraph "(24 November.)": the wall-conjugation result (which conjugation, no selection, the floor, Hadamard statements given the Fact, what the bundle trades, the mirror tension argued), the trace-anomaly result given (A) and (E), the two not jointly available with (A), (E), (RD), (DF), D3 in full, (O5) specific to the conformal group, the necessity route (argued, not stored). Attack: the Dirac-propagation item gets a dated D3 note; new items "Closed by its own condition" (4b), "Done" (4c), "Closed" (4a, argued, not stored), "New: wall-based selections must say what they assume at the wall". The Riemannian far-side item is unchanged. `source` extended; two ids added to `entities`. |
| op.descent-state-and-spectrum | reformulated (unchanged) | Four "New (24 November)" attack items: 2a, 2b (with the 296 flag), 2c (with the wall condition), and a pointer to 6b. |
| op.the-number-n | open (unchanged) | Two "New (24 November)" attack items: 6a (for N and v/H together) and 6c as amended (the 4b form struck). |
| op.rung-unit | partial (unchanged) | One "New (24 November)" attack item: 6a for v/H, beside the stored two-model result on a branch the record excludes. |
| op.non-gaussian-completion | reformulated (unchanged) | One "New (24 November)" attack item: 6b as amended. |
| op.derive-loc-and-r-loc | partial (unchanged) | One "New (24 November)" attack item pointing to 3a, 3b, 3c on op.einstein-from-the-field-theory, with what ends each. |
| colony/runs/LEDGER_HISTORY.md | n/a | One line for the run: targets, method, the seven results in a clause each, the withdrawn duplicate against pull request #65, D1 to D3, about 3.9M subagent tokens. |

Literature named in the new text (Weinberg 1964, 1965; Deser 1970; Weinberg and Witten 1980; McFadden and
Skenderis; Fewster and Verch 2013; Navascues and Wunderlich; Wootters and others; the Klein correspondence) is
marked "cited from memory" at each place. Boyle, Finn and Turok is marked as the stored entity marks it (arXiv
locators confirmed in review, journal reference from memory).

## Check
`python -m tp check --store store --layers 1-3 --keep-going --author leon`, run after the last edit (and after
the postulate synthesis.premise-canonical-pair-on-the-two-null-directions had appeared in store/claims/):
0 errors, 0 warnings, 120 information findings (I126 1, I213 118, I305 1), the same findings as
layers123-after-accept.log. Every `\claimref` and every `entities` id in the records resolves, the new postulate
included. The file parses as YAML with 41 records. No check.py was touched, so runcheck was not needed.

## Numbers to recompute
None in these two files. Two numbers are quoted that are arithmetic and not stored results, and are marked so:
888 (= 48 x 9 + 12 x 36 + 8 x 3) and 296 (= 888/3).

## Not done, and why
- op.gravitational-field-at-null-momentum was not moved to the settled file (instructed; see Decisions).
- The statement of op.graviton-rate-as-classical-field-process still reads "The series holds no such quantum"
  as written on 10 November; only the dated sentence was added, as instructed.
- In op.deposit-state-is-hadamard the older sentences that use the wall ("M = ma is smooth at the origin"; the
  attack item on a massive reference at a radiation origin) were not rewritten; the new paragraph and a dated
  note say they are to be read under D3.
- Route 6b was not filed on op.the-number-n: it does not name N. It is on op.non-gaussian-completion, with a
  pointer on op.descent-state-and-spectrum.
- The older attack item of op.the-number-n ("Freedom ... two-model argument") was left as posed; the new 6a
  item extends it.
- I did not read M-G's or M-H's edited entities beyond the title and one-liner of the new postulate (to check
  that the records agree with it: they do, the burst proviso included). Sentences in the records about texts
  those passes restate (the graviton note, the burst prediction, the conventions) say only that they follow the
  decision, not that the restatement is done.
- The audit of the 73 postulates, the Krein-form computation, the macroscopic-locality certificate, the
  recording route and the necessity route are findings only; the records cite them as unstored working notes.

## Decisions for Leon
1. op.gravitational-field-at-null-momentum: does adoption of (TT) meet its success clause ("derived or adopted
   as a premise with its grounds")? If yes, the record moves to the settled file and the five open tasks of its
   last attack item need a successor problem; if no, it stays partial as now.
2. op.positivity-of-values: the `why` was restated. Its old first sentence ("every stored statement about CHSH
   values holds given (P)") is no longer true, since two of the new results use no premise about values. Please
   confirm the new wording.
3. The fork on (RP) stays open by D1. The flag-sector form is filed as an untested, conjectured item; say
   whether the exact test at three modes should be run.
4. op.graviton-rate-as-classical-field-process: restate its statement and `why` for D2, or leave them as dated
   history with the new sentence.
5. Whether (A) of the trace-anomaly result is to be imported as a Fact later (kept as a named hypothesis in
   this pass, as instructed).
