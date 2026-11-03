# Typing pass instructions (Transport Lab pilot)

You are typing a set of draft claims that were extracted mechanically from the
Transport Papers' LaTeX. The store is at /home/claude/suite/transport_lab/store.
Each claim is a folder store/claims/<id>/ holding entity.md (YAML front matter,
then `## formal`, `## technical`, `## lay`, `## one-liner`) and, for proved
claims, proof-main.tex.

Sources: the papers are /home/claude/suite/T0*.tex. They are 30-400 KB: NEVER
read a whole paper. Use grep -n on the label (front matter `locators.label`)
and read only the lines you need (sed -n 'a,bp'). The map from paper labels to
store ids is seed/extraction_report.json -> "label_map" (keys like
"T05:thm:rate"); use grep on that file, do not load it whole.

For EACH claim id in your list, do all of the following, editing only files
inside that claim's folder:

1. Edges (front matter, derivation `main`).
   - Read the formal statement and proof-main.tex. `\claimref{<id>}` marks a
     reference to another store entity.
   - Keep a `uses` edge only if the proof (or the statement's hypotheses)
     relies on the target's content as a premise. Remove edges that cite the
     target only for context, comparison, or "see also".
   - Look at `extraction.context_refs` (references made in the statement):
     if the result logically depends on one (e.g. "under the hypotheses of
     Theorem X", "by Proposition Y"), add it to `uses`.
   - Postulates (status: postulate) go in `assumes`, never `uses`.
   - Pins stay `@1`. Only reference ids that exist (ls store/claims,
     store/objects). Objects (definitions) belong in `about`, not `uses`.
   - If the proof clearly gives two independent routes to the result, you may
     split into two derivations (names: lower-case-hyphen), each with its own
     proof file `proof-<name>.tex` containing the relevant part of the proof
     text copied verbatim from proof-main.tex. Only do this when it is clear.
   - Never change status, formal text, proof text, locators or checked_by.

2. Levels. Replace `pending` with:
   - technical: one or two short paragraphs a mathematically literate reader
     can follow, with the key equation in $...$ maths. Use only standard LaTeX
     maths or macros listed in store/notation.yaml.
   - lay: two to four plain sentences for a curious non-specialist. No
     symbols unless essential.
   - one-liner: one sentence stating the result.
   Rules for all levels: claim no more than the formal statement says (no
   overclaiming, keep its hypotheses and scope); no em dashes (no U+2014 and
   no "---"); never use the words "honest" or "honestly"; write the square of
   a vector as Q(v); British spelling; do not mention paper numbers or
   theorem numbers in the text (locators already carry them).

3. Record what you did. Set `review: typed`. Inside the `extraction:` mapping
   add:
       typing:
         by: ai-typing-pass
         removed: [ids removed from uses/assumes]
         added: [ids added]
         note: one sentence on any judgement call or doubt
   (omit removed/added if empty). Keep the existing extraction keys.

4. Check your work: from /home/claude/suite/transport_lab run
       python3 -m tp check --store store --layers 1-3 --keep-going
   and fix every finding that names one of YOUR ids. Ignore findings on other
   ids (other agents are editing them in parallel). Do not edit any file
   outside your claims' folders.

Finish with a short report: per claim, edges removed/added, and any claim
where you were unsure whether an edge is a real premise.
