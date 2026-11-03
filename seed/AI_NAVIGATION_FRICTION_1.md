# Friction report: navigating the Transport Lab through `tp.ask`

## Overall

When the question named a concept I could put into words, the store was easy to use. `search_claims`, then `get_claim` or `get_proof`, answered most questions in 2 to 4 calls. The derived fields (`effective_status`, `holds_given`, `evidence`, `past_cone_size`, `future_cone_size`) and the `refuted_by` link were the most valuable parts of the store. Without them, questions 2, 3, 4, 5 and 9 would have meant reading proofs.

The store is much weaker at questions about the whole store ("which is the most built upon", "find any proved result with an uncited premise", "all results with tag X"). There is no tool that ranks, lists or filters across all entities. Question 14 used most of my call budget: about 175 of my 243 calls went to `get_claim` one id at a time, just to read `future_cone_size`.

## Most useful tools

1. **`conventions`**. This was the best single call. It answered most of questions 6 and 7 directly: the I4 / I6 units, and known limit 1 (T05's atom anticommutes with I4). It also gave the point embedding formula for question 12 and both normalisation conventions.
2. **`search_claims`**. Ranking was good: the right result was first for questions 1, 2, 9, 4 (with `status: live`) and 5. The `status` and `subject` filters were useful.
3. **`get_claim`**. It has everything, including derived fields, `checked_by`, the `extraction.typing` notes (which explain why an edge was or was not added) and note openings.
4. **`get_proof`**. Its `premises_not_cited_in_text` / `cited_but_not_premises` fields are exactly what question 15 needed.
5. **`neighbourhood`**. Its direct `used_by` list answered question 10 in one call.
6. **`cone`**. It is correct, and its counts matched `future_cone_size`.

## Least useful

- **`digest`** and **`trail`**. They are long, and the notes in them often show only "pending". I opened one of each and used neither.
- **`list_tags`** and **`list_subjects`**. They are good for orientation, but because nothing can enumerate a tag's members, their counts cannot be acted on.

## Where I got stuck or wasted calls

1. **No store-wide ranking or listing (question 14).** No tool sorts by `future_cone_size` or returns derived fields for many ids at once. `cone` output lists only id, title, kind, status, subject, one-liner and source: no cone sizes and no edges. I had to:
   - collect past cones of several downstream results;
   - prune using the fact that a result's future cone is contained in each of its premises' future cones;
   - call `get_claim` on each surviving candidate, at about 4 s per call.

   Even so, the answer (`primer.classification-real-clifford-algebras`, future cone 203) is "the largest I found", not a guaranteed maximum. A `rank(by="future_cone_size")` tool, or a `fields=[...]` / batch-ids option on `get_claim`, would have made this one call.
2. **The tag filter needs a matching query.** `search_claims {query:"", tag:"modular-theory"}` returns `[]`. With query "modular" it returned 28 of the tag's 45 members. There is no way to list a tag's members. This is a bug or a missing feature: an empty query with a filter should list everything that matches the filter.
3. **No store-wide query for proof hygiene (question 15).** `premises_not_cited_in_text` exists only per result. I found an example on the fifth `get_proof` call by luck, after trying a result whose proof I suspected was thin. A filter like `search_claims(has_uncited_premises=true)` would be easy to offer, since the build already computes the field.
4. **Duplicate hypothesis names are not cross-linked.**
   - "Hypothesis (S)" is two entities: `standard-model.hyp-s-slot-statistics` (T12) and `dark-tower-matter.hypothesis-s-slot-statistics` (T14c, "in every tower"). There is no `equivalent_to`, `derived_from` or `specialises` link between them, so "rests on Hypothesis (S)" has two defensible answers: 120 or 127.
   - "(U)" means three different things: T14 Hypothesis (U), T14c Premise U, and the rate model's (U). Only the free-text `about` of the tag `hypothesis-u` warns about this.
   - A disambiguation field, or a `see_also` between same-named postulates, would help.
5. **Paper titles are not in the store.** The question names "One Complex Unit", but entities carry only `paper: "FT"`. Only the `conventions` prose ties "One Complex Unit" to 16 October, and only a note's "chose i = I4 (16 October)" ties FT to that date. There is no `list_papers` tool mapping T01, FT, T14c, T12-rungs and so on to titles. I matched by inference.
6. **Notes are mostly "pending".** In search results, `digest` and `trail`, notes show `one_liner: "pending"`. Their technical and lay levels are "pending" too; only `formal` has text. So `include_notes:true` search results cannot be judged without opening each note. Search should fall back to the note's formal opening.
7. **Known limits live only in prose.** T05's atom (question 7) is recorded as a convention limit, not on the atom entities. `singularity.pseudo-inverse-identities-hyperbolic-atom` has no `extraction.i4_conversion` remark, unlike `hawking.i-state`. An agent that reads the entity without reading `conventions` would miss it.
8. **Latency.** Each call takes about 3 to 4 s, and there is no batch call. My ranking loops timed out the 2-minute foreground shell limit and had to run in the background.

## Confusing conventions or data

- **Id prefix, subject and region disagree.**
  - `singularity.modular-descent` has subject descent.
  - `scrambling.clock-inventory-boundary-modes` has subject entropy.
  - `hawking.modular-structure-completed-pair` has subject descent.
  - `pred.neutrino-mass-sum-floor` has `subject: neutrinos` but `region: programme`.

  The prefix looks like a paper or section slug, but nothing documents that. I nearly searched by prefix.
- **A prediction's effective status is "proved".** `pred.neutrino-mass-sum-floor` has declared status `live` but `effective_status: "proved"`, with `evidence: "none"`. The conventions say "trust effective_status", but "proved" for a live prediction is misleading. It presumably means "its basis derivation is proved"; it should say so, or use a separate field.
- **A data slip in the neutrino prediction.** The technical level says "m1 = m2 = 0 at leading order" but gives the sum as sqrt(dm21^2) + sqrt(dm31^2), which needs m2 = sqrt(dm21^2), not 0.
- **The machine-check wording is uneven.** `checked_by: [{kind: proof}]` sits next to `kind: legacy` entries, and `evidence` takes values like `proof-only`, `pass-legacy` and `none`. `conventions` explains `pass-legacy` but not `proof-only`, and does not say that `kind: proof` means "not machine-checked". I worked it out from `transport.minimality`.
- **Some proof texts are pointers, not proofs.** The whole "proof" of `field-theory.composite-gauge-bosons-what-excluded` is a reference to a verification log ("V2 (near-immediate) and V1 (imported)"), yet the result is declared and effectively proved. The store does not separate "proof text present" from "proof outsourced to a script log".
- **Results are restated in later papers as separate "Imported:" entities**, such as `rungs.imported-totality-minimality-completion` repeating `transport.minimality`. They show up in `used_by`, `search_claims` and cone counts as separate results. That inflates cone sizes and makes "which result says X" ambiguous. Questions 1 and 2 each had two or three near-duplicates in the top results.

## What a tool should have offered

- `rank` / `top(by=future_cone_size | past_cone_size, subject?, tag?)`.
- `list(tag=..., subject=..., status=..., kind=...)` with no query needed.
- `get_claim(ids=[...], fields=[...])`, a batch call with field projection, so I would not get about 10 KB per call when I need one number.
- `cone(..., with_sizes=true)` or edges in the cone output.
- `list_papers`, mapping paper codes to titles and dates.
- A store-wide `audit` query over `premises_not_cited_in_text`, staleness and so on.
- Same-name disambiguation, for example `search_claims` flagging that "(S)" matches two postulates in different papers.
