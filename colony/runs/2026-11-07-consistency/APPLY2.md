# Run 2026-11-07-consistency: applying Leon's second-round answers (agents D1-D3)

You act for Leon as maintainer. LAB = /home/claude/phys-graph (branch consistency-and-ga). Never commit, never
spawn agents, never kill processes; at most two tp check runs each; three agents share 2 CPUs.

Read: colony/runs/2026-11-07-consistency/DECISIONS.md, section "Leon's answers, second round" (your items), the
reports it names, store/conventions.md, docs/gtg-dictionary.md, colony/BRIEF.md, PIN_REVIEW.md (how to review a
dependant's pin).

Shares:
- D1: answers 1, 2, 4, 5 (record only), 6, and 3 (record only: add one sentence to the extraction of the
  asymmetry remark that Leon confirmed the reading).
- D2: answer 7.
- D3: answer 8 (the H5 lists are in apply-AP1.md "Could not apply exactly" item 2 and the reader reports it cites).
Ownership: before editing an entity, check colony/runs/2026-11-07-consistency/claimed-round2.txt; if another agent
has claimed it, write your item for it into items-for-<agent>.md and let them apply it; otherwise append the id and
edit. Read items-for-<you>.md before you finish.

Bookkeeping: the store was re-locked at fb48481, so every changed entity goes to its locked version + 1 (once in
this round), with a credit entry for that version and an extraction note maintainer_pass_decisions_2 (by
maintainer-2026-11-07, date, what and why; for a formal change, the evidence). A formal change: fix any check
whose assertion encodes the old statement (runcheck, then check4 on a proposals/ copy, deleted after). After your
edits, review every pin on the entities you bumped as PIN_REVIEW.md says (notation: repin; restatement: read the
dependant's use; repin if it holds, update a quotation if the dependant quotes the old text, else list it for
Leon). Dropping an assumes edge changes holds_given: check the result's one-liner, lay and technical levels no
longer state the dropped condition. House style; no bare imaginary unit.
Validate: python3 -m tp check --store store --layers 1,2,3 --keep-going --author leon (0 errors, 0 warnings on
your ids).

Report: colony/runs/2026-11-07-consistency/apply2-<D>.md: each item (entity, old -> new version, what), pins
reviewed, anything not applied exactly and why. Final reply under 250 words.
