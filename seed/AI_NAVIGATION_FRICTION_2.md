# Friction report (run 2)

52 logged calls in total, counting the `tools` listing. I answered all 15 questions. On none did I get badly stuck. Most of the friction came from fields that were missing or inconsistent, not from navigation.

## Most useful
- **`conventions`.** This was the single best call. It answered most of Q6 and the "why" of Q7 (known limit 1) outright. It warned about namesakes (S)/(U), which saved me from conflating them in Q3 and Q8. It also gave the T01 point embedding, which I then confirmed in the store for Q12. Reading it first is good advice and the tool description says so.
- **`search_claims`.** The first hit was correct for Q1, Q2 and Q5. Showing future_cone_size, evidence and source in each hit row let me answer Q1 and Q2 almost without a second call.
- **`list_entities` with filters.** `kind=prediction`, `status=refuted`, `tag=...`, `uncited_premises=true` and `sort_by=future_cone_size` each answered a question (Q4, Q9, Q11, Q14, Q15) in one call. Showing holds_given in the prediction list was ideal for Q4.
- **`get_proof`.** Its `premises_not_cited_in_text` / `cited_but_not_premises` per proof, together with per-step `cites`, made Q15 verifiable rather than taken on trust.
- **`neighbourhood`.** This is the quickest way to get direct used_by (Q10).

## Least useful or confusing
1. **Restatement marking barely works.** The conventions say restatements ("Imported: ...") are marked `restates` and can be dropped with `exclude_restatements`. In practice:
   - `exclude_restatements` removed only 4 of 882 entities.
   - Every "Imported:" claim I looked at had `restates: null`, for example rungs.imported-totality-minimality-completion and correspondence.imported-forced-completion-fibre-quadric.

   So the counts the store tells you to trust ("count each result once") are not obtainable. In Q3 I had to estimate the count without restatements by grepping titles for "Imported:". In Q14 I could not tell whether the primer's classification is effectively a restatement.
2. **`fields` silently drops fields it does not know.** `list_entities ... fields:["refuted_by"]` and `get_claims ... fields:["restates","restated_by"]` returned rows without those keys and with no error. I could not tell whether a field was empty, unsupported or misspelled. `refuted_by` needed a separate `get_claim` call.
3. **`used_by` is a count in summaries but there is no list of ids** in `get_claim.derived`. To get the direct dependants I had to use `neighbourhood`, which also returns 12 "nearby" entries I did not need. `get_claim` should list used_by ids, or `cone` should take a `depth: 1`.
4. **Important facts hide in `front_matter.extraction`.** The decisive statement for Q7, that T05's atom keeps a scalar i because I4 anticommutes with its modes, lives in `extraction.unit_note`. That field is not searchable and not mentioned in any tool description; I found it only by dumping the whole front matter. If the convention limit is pointed to "under extraction", search should index it or `get_claim` should surface it.
5. **Notes' levels are mostly "pending".** For notes, technical, lay and one-liner are the literal string "pending", and `formal` holds the whole text. With `notes_text=true` the text appears again in `notes[].text` on the parent claim. That is workable but confusing: I first thought `notes_text` did nothing, because on the note itself the output looked identical.
6. **"Results" is never defined.** `list_papers` says FT has 24 results. `list_entities paper=FT include_notes=true` gives 37. Only by counting by hand did I see that 24 = 23 claims + 1 object, and the 13 notes are excluded. The word "results" should be defined, or each count broken down by kind.
7. **`cone` returns a bare list, not an object** with a total, unlike `list_entities`. My first parser failed. There was also no per-kind breakdown. For Q3 I wanted "claims vs predictions vs restatements", and the tool could have offered that.
8. **Search for formulas is weak.** For Q12 the T01 point embedding lives in a *setting note*, not in a claim or object. `search_claims` excludes notes by default. Even with `include_notes`, my query ("point embedding lift of a point null vector n0 ninf") ranked T05's fibrewise lift and T12's frozen point above it, and did not return T01's setting at all. I found it only by listing all 133 T01 entities and grepping titles for "model". A definition this central (it is in the conventions!) should arguably be an `obj.*` entity, or the conventions page should cite the entity id.
9. **The data contains a possible inconsistency.** pred.neutrino-mass-sum-floor's technical level says "m1 = m2 = 0 at leading order" and then "m2 = sqrt(dm^2_21)". The second reads as the sub-leading value, but the text does not say so, so I flag it.
10. **Some proof-carrying claims have no premises.** transport.minimality (future cone 137) and primer.classification-real-clifford-algebras (future cone 203) both have derivations with no `uses`, so their past cones are 0. That is probably fine for foundations, but the primer topping the "most built upon" ranking is an artefact of where the edges were drawn. It is used directly by only 2 entities. Ranking by future cone with no notion of restatement or expository duplication makes Q14 fragile.
11. **The `uncited_premises` flag fires on 304 proved results**, about a third of the store. Many are proofs whose text "only points to a verification run", or imports. A filter to exclude the `reference`-kind proofs would make it a usable hygiene signal; right now it is mostly noise.

## What a tool should have offered
- `get_claim` returning used_by and uses as id lists, plus `refuted_by`, `restates` and `namesakes` consistently in `get_claims` / `list_entities` fields.
- `cone` with `depth`, a `total`, and a group-by on kind or restatement.
- Search over notes on by default for definitional/formula queries, or a `find_formula`/`notation`-style lookup that maps a symbol (X(x), I4, I6) to the entity defining it. The `notation` tool returns macros, not where they are defined.
- A working restatement detector, or at least a `title_prefix` / `is_import_fact` flag.

## Wasted calls
About 6:
- two `get_claims` / `list_entities` calls whose requested fields came back missing;
- one `cone` call I had to re-parse;
- three object/note reads hunting for the T01 formula before I listed all T01 entities;
- a search for the T05 atom that returned related results but not the definition (I did not need it in the end).
