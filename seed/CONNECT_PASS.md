# Connecting the unconnected: instructions

Leon: "I have noticed some nodes with no connections, no dependencies or it
doesn't depend on anything. All nodes should be connected I would have
thought." Your list (seed/connect_ids_<group>.txt) holds entities with no
logical link (`uses` or `assumes`) in or out; those marked `*` have no link of
any kind. For each, find the links the mathematics actually has, in both
directions, and add them. Do not invent dependence: a link says a proof
relies on a result.

Work in /home/claude/suite/transport_lab. Useful tools (they read the store):

    python3 -m tp.ask get_claim '{"id": "<id>"}'
    python3 -m tp.ask search_claims '{"query": "...", "limit": 10}'
    python3 -m tp.ask find_text '{"pattern": "Lemma 4.2", "include_notes": true}'
    python3 -m tp.ask get_proof '{"id": "<id>"}'

and grep over store/*/*/entity.md and store/*/*/proof-*.tex. The source
paper's text is in its setting notes (store/notes/note.<region>.setting-*) and
the paper itself (../<paper>.tex; never read a whole paper, grep it and read
small ranges). `locators` in the front matter gives the paper, number, label
and line.

For each entity, in this order:

1. **Its premises.** What does its proof (or, for an import, the statement)
   rely on that the store holds? A result of the series used in the proof, a
   definition it is about, a hypothesis it assumes. Add `uses` (results),
   `assumes` (postulates, status postulate) or `about` (definitions, kind
   object) in its front matter, pinned `id@<current version>`, and cite each
   new premise in the proof text with \claimref where it is used (the
   validator warns, W215, when a premise is not cited: keep that at zero).
   Imports (status imported) carry no derivations: give them `about` links
   only.
2. **Its dependants.** Which results rely on it? Search for its label,
   number, title words and its content across proofs and statements of the
   whole store (later papers cite earlier ones by number: "T5 Prop 7.21",
   "Theorem 4.13 of [T1]"). For each genuine use, add the edge on the
   dependant's derivation (`uses` or `assumes`) and cite it with \claimref
   in the dependant's proof at that step. A postulate nothing assumes is the
   strongest signal: find the results that hold under it (their statement or
   proof says "under (X)", "assuming ...") and add `assumes` to them.
3. **Definitions (kind object).** Link them with `about` from the claims whose
   statements use the defined notion.
4. **Conjectures and refutations.** They hang from lineage
   (`motivated_by`) and `refuted_by`; also give them `about` to the
   definitions they concern and, where a conjecture's supporting evidence is
   a result in the store, `lineage.motivated_by` that result.
5. **Genuinely standalone.** Some entities are rightly unused (a classical
   fact a paper states for orientation; the last result of a line of
   argument; a prediction whose basis is outside the store). Then say so:
   record the verdict below and, if anything at all bears on it, link it with
   `about` or lineage. Never add a `uses` to make a node look connected.

Mechanics:
- Changing `derivations` (uses, assumes) or a proof is substantive: bump that
  entity's `version` by 1 once, and copy proof-NAME.tex to orig-proof-NAME.tex
  first if no orig copy exists. `about` and lineage changes are substantive
  too (bump). Other agents edit other entities at the same time; you may edit
  a dependant outside your list only to add the edge that points at an entity
  in your list (and its \claimref); keep that edit minimal.
- Record on each entity in your list under `extraction:` a key
  `connect_pass:` with `by: ai-connect-pass`, `date: 2026-10-21`,
  `added_premises: [ids]`, `added_dependants: [ids]`, `added_about: [ids]`,
  `verdict: connected | standalone`, and `note:` one sentence (why
  standalone, or any judgement call).
- Check after each batch of about ten:
      python3 -m tp check --store store --layers 1-3,5
  Fix every error and every W215 on entities you touched. E301 (a cycle)
  means an edge you added closes a loop: remove the edge that is not a real
  premise. E203 means the edge kind is wrong for its target (assumes needs a
  postulate; about needs a definition).
- House style: no em dashes; never "honest" or "honestly"; British spelling.
- Do not run verify scripts or layer 4.

Report: per entity, what you added (or standalone, and why); totals; and any
entity where the store's links look wrong in a way you did not fix.
