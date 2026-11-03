# Citing every premise: instructions

Every derivation in the store lists the results its proof relies on (`uses`,
in the front matter of store/<kind>/<id>/entity.md, with pins `id@n`). The
proof text (proof-<name>.tex beside it) should name each of them with
`\claimref{<id>}` at the place where it is used, so that a reader, or an AI
following `get_proof`, sees which step uses which premise. A mechanical pass
already converted the paper's own references (\ref, citations with locators,
"Theorem 4.13") into \claimref where they point at a premise. What is left is
in your list: for each entity, each derivation name, the premises its proof
text still does not cite.

For each listed premise, read the proof and the premise's statement (its
entity.md formal level), then do exactly one of these:

1. **Cite it where it is used.** The proof uses the premise at an identifiable
   step, in words ("by the splitting lemma", "the classification gives") or
   silently (the step needs exactly what the premise states). Insert
   `\claimref{<id>}` there with the smallest possible edit: "by the splitting
   lemma" becomes "by the splitting lemma (\claimref{id})", or "by
   \claimref{id}"; a silent use gets a short parenthetical "(by
   \claimref{id})" after the clause that needs it. Never change mathematics.
2. **State its role, when the proof is a pointer or a sketch.** If the proof
   text only points to a verification run or a computation and so has no
   place for the citation, add one short closing sentence that says what the
   premise supplies, e.g. "The computation rests on \claimref{id}, which
   supplies the CAR relations of the ladder pairs." Take the role from the
   statements, never invent one.
3. **Remove the edge, if it is not a premise.** If neither the proof nor the
   statement relies on the premise (it was a context or comparison
   reference), remove it from `uses` (delete the list item, keep the rest) and
   say why in the record. Be conservative: remove only when you are sure; if
   in doubt, cite it (1 or 2).

Mechanics:
- Before editing a proof, if orig-proof-<name>.tex does not exist in the
  folder, copy proof-<name>.tex to it (never overwrite an existing one: it may
  hold the paper's original).
- After editing an entity (proof text or `uses`), increase its `version` by 1,
  once per entity, however many edits. If it was already edited by the
  mechanical pass today, bump it again only if you change it; that is fine.
- Record under `extraction:` a key `cite_pass:` with `by: ai-cite-pass`,
  `date: 2026-10-21`, `cited: [ids]`, `stated_role: [ids]`, `removed: [ids]`
  (omit empty lists) and `note:` one sentence for any judgement call.
- Do not touch pins in other entities; the maintainer repins.
- House style: no em dashes; never "honest" or "honestly"; British spelling.

Check after each batch of about ten entities, from
/home/claude/suite/transport_lab:

    python3 -m tp check --store store --layers 1-3,5

and fix every finding on your ids. To confirm a premise is now cited:

    python3 -m tp.ask get_proof '{"id": "<id>"}' | python3 -c "import json,sys; d=json.load(sys.stdin); print({k: v['premises_not_cited_in_text'] for k, v in d['proofs'].items()})"

Other agents edit other ids at the same time; edit only the entities in your
list. Do not run verify scripts or layer 4. Never read a whole paper.

Report: counts of cited, stated-role and removed premises; every removal with
its reason; and any proof where the listed premises looked wrong in a way you
did not fix.
