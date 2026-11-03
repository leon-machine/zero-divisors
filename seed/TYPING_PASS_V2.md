# Typing pass, full series (v2)

You are typing a set of claims in the Transport Lab store,
/home/claude/suite/transport_lab/store. Each entity is a folder
store/<claims|objects|questions|predictions>/<id>/ holding entity.md (YAML
front matter, then `## formal`, `## technical`, `## lay`, `## one-liner`) and,
for proved claims, proof-*.tex.

Sources: the papers are /home/claude/suite/*.tex (front matter
`locators.paper` names the paper; `locators.label` the LaTeX label;
`locators.line` the line). Papers are 30-400 KB: NEVER read a whole paper.
Use grep -n and sed -n 'a,bp'. The label map (paper:label -> store id) is
seed/extraction_report.json "label_map"; grep it, never load it whole.
`\claimref{<id>}` in a text marks a reference to another store entity.

For EACH id in your list, editing only files inside that entity's folder:

1. Edges (claims and predictions with derivations).
   - Keep a `uses` edge only if the proof or the statement's hypotheses rely
     on the target as a premise. Remove context-only, comparison or
     "see also" citations. Add premises named in `extraction.context_refs`
     when the result depends on them ("under the hypotheses of", "by").
   - Postulates (status: postulate) go in `assumes`, never `uses`. Objects
     (definitions) go in `about`, not `uses`.
   - `extraction.repair` lists edges added mechanically after extraction
     (including `transport.transport-algorithm`, added to T05 results that the
     paper says execute a step of the T1 transport algorithm). Review each:
     keep it if it is a real premise, remove it otherwise, and record which.
   - Circular reasoning: if the checker reports E301 naming your claim, read
     both proofs and remove the edge that is not a real premise.
   - Standard route (this matters for the ledger). If the paper says the result
     is ALSO obtained by standard physics without the completion (it
     "recovers", "reproduces", "inherits", "agrees with", "is classical") and
     the standard result is in the store as an imported claim, add a second
     derivation named `standard-route` whose `uses` are those imported claims,
     with a proof file proof-standard-route.tex quoting the paper's sentence
     that says so. If the standard result is not in the store, say so in the
     typing note instead.
   - Only reference ids that exist. Pins are `@<current version>` of the
     target (read its `version:`; usually 1).
   - Never change formal text, existing proof text, locators, checked_by or
     subject. Change status only as described in 2.

2. Status problems the checker reports (E107, E108, E204):
   - A proved claim with no proof text: if it restates another store claim,
     give it `uses: [that@v]` and a proof file saying "Restated from
     \claimref{that}." If the source states it as an immediate consequence of
     cited results, `uses` those and a proof file "Follows from \claimref{..}
     and \claimref{..}, as the source states." Never write mathematical proof
     content yourself. If neither applies and the source cites the literature
     for it, make it `status: imported` with `imported_from` (citation text
     from the paper's bibliography) and no derivations. Otherwise make it
     `status: conjectured` and add `lineage: {motivated_by: [ids]}`.
   - A conjecture or observation needs `lineage.motivated_by` (the claims or
     question that prompt it). An `observation` that the paper actually
     computes or proves may become proved with a derivation and proof file
     (copy the proof text verbatim from the paper).
   - Leave predictions' `kill_condition` alone; it is filled separately.

3. Levels. Replace `pending` with:
   - technical: one or two short paragraphs a mathematically literate reader
     can follow, with the key equation in $...$ maths (standard LaTeX maths or
     macros in store/notation.yaml only).
   - lay: two to four plain sentences for a curious non-specialist.
   - one-liner: one sentence stating the result.
   All levels: claim no more than the formal statement (keep its hypotheses
   and scope; say "under premise X" where it applies); no em dashes (no U+2014,
   no "---"); never "honest" or "honestly"; write the square of a vector as
   Q(v); British spelling; no paper or theorem numbers in the text.
   For objects (definitions) the levels explain the definition. For imported
   claims they explain the imported result.

3b. Title. If the `title:` is a bare locator such as "T01 Lem 2.1" or
   "T12 Prop 4.3", replace it with a short descriptive title (at most eight
   words, sentence case, no theorem numbers). Also set the one-liner if it
   still repeats the bare locator. Titles are cosmetic: no version bump.

4. Record. Set `review: typed`. Inside `extraction:` add
       typing:
         by: ai-typing-pass
         removed: [ids]      # omit if none
         added: [ids]        # omit if none
         note: one sentence on any judgement call or doubt
   Keep the existing extraction keys.

5. Check: from /home/claude/suite/transport_lab run
       python3 -m tp check --store store --layers 1-3 --keep-going --author leon
   and fix every finding naming one of YOUR ids (ignore W210, and E204 that
   is caused by a premise outside your list). Other agents edit other ids in
   parallel; touch nothing outside your folders.

Finish with a short report: edges removed/added per claim (only where
changed), status changes, standard-route derivations added, and the claims
you were least sure about.
