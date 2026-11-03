# Levels pass: keep every condition visible

An independent review found that the technical, lay and one-liner levels
sometimes drop a condition the formal statement carries (about one entity in
five among conditional results). This pass fixes that for a list of entities.

Work in /home/claude/suite/transport_lab. Each entity is
store/<claims|predictions>/<id>/entity.md (YAML front matter, then `## formal`,
`## technical`, `## lay`, `## one-liner`). Edit through tp.model's
parse_entity_text and dump_entity in one script of your own (keep it, and a
backup of every folder you change, in a private folder
/tmp/claude-0/-home-claude/f5c21aa3-33bd-54d7-a8e9-4d9b5d6a3726/scratchpad/levels-<group>/).
Other agents edit other ids in parallel: touch only your ids.

For each id:

1. Read the formal statement and the front matter (`derivations[].assumes`,
   `status`, `extraction.typing.note`).
2. List the conditions the result holds under:
   - every hypothesis, premise or assumption the formal statement names or
     states ("Under Hypothesis (S)", "Assume (IC)", "given P1 to P4", "if the
     state is regular", "for modes of nonzero weight");
   - every postulate in its own `assumes` edges (not those further back in
     its past cone, unless the formal names them);
   - level qualifiers: "at leading order", "at observation level", "at record
     level", "conditional", "for a non-rotating black hole", "within the
     quasi-free class", "up to gauge".
3. Check the technical, lay and one-liner levels. Each must keep every
   condition from step 2, in words suited to its reader: the lay level may say
   "assuming the slots behave like the pairs (Hypothesis (S))" or "if the
   regularity premise holds"; the one-liner may compress, but must not drop a
   condition ("Under (S), ..."). Also check that no level claims more than the
   formal statement, misstates a number or a sign, or widens the scope.
4. Rewrite only the sentences that need it. Never change the formal text,
   proofs, edges, status, locators or titles. A level that reads `pending`
   gets written from scratch.
5. Add one sentence to `extraction.typing.note`: "Levels pass: ..." saying
   what you changed, or "Levels pass: conditions already kept."

The review's specific findings are in /tmp/claude-0/review/store_review.md:
fix any that name your ids.

House rules: no em dashes, never the words "honest" or "honestly", British
spelling, Q(v) for the square of a vector, maths in $...$ with macros
declared in store/notation.yaml.

When done, run
    python3 -m tp check --store store --layers 1-3,5 --keep-going --author leon
and make sure nothing names your ids at E level; W503 findings on your ids
should be gone or be false positives you can explain. Report: how many ids
needed changes, by level, the most serious fixes, and anything unsure.
