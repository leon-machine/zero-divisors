# Run 2026-11-07-consistency: applying the decisions (agents AP1 and AP2)

You act for Leon as maintainer. LAB = /home/claude/phys-graph (branch consistency-and-ga). Never commit, never
spawn agents, never kill processes; other agents share 2 CPUs (at most three tp check runs).

Read: colony/runs/2026-11-07-consistency/DECISIONS.md in full (the reconciled items, with evidence and proposed
fixes, and at the end Leon's answers), store/conventions.md, colony/BRIEF.md (store model), CONTRIBUTING.md and
docs/CONTRIBUTING-rules.md (what maintainers do), colony/runs/2026-11-07-consistency/CONSISTENCY.md (bookkeeping).

Your share:
- AP1: categories A (every formal correction, applied exactly as the evidence supports; record the computation
  in the extraction note), G (stale wording) and H.
- AP2: categories B, C, D, E and F, and Leon's answers 2-7: the new postulate for the mirror's common ceiling
  coupling (costed, named, with assumes edges from the six results), the charged-lepton reality clause, the status
  changes, the restatements, the rem:recording postulate with its assumes edges, the wall-class restatement, the
  links (uses edges, equivalent_to or restates links, repoints to premise-free results), duplicate links (no
  retirements), and the conventions lines (store/conventions.md).
Copy the format of existing entities of the same kind for anything new (postulates: grep "status: postulate" in
store/claims/*/entity.md; a new postulate needs `extraction` saying it was adopted by Leon on 2026-11-07 and what
it costs).

Ownership: before editing an entity, check colony/runs/2026-11-07-consistency/claimed-apply.txt; if the other
apply agent has claimed it, put your item for it in items-for-<other>.md instead; otherwise append the id and edit.
The ids in colony/runs/2026-11-07-consistency/gtg_1.txt, gtg_2.txt and gtg_3.txt belong to three GTG provers
working now: do not edit them; write each of your items on them, with the decision text, into
colony/runs/2026-11-07-consistency/items-for-gtg.md.

Bookkeeping per changed entity: version + 1 relative to store/lock unless the entity is already above its locked
version in this run (then keep it); a credit entry for that version; an extraction note
maintainer_pass_decisions (by maintainer-2026-11-07, date, one sentence and, for a correction, the evidence);
keep every file; no bare imaginary unit; house style. A formal correction is a restatement; if a check's assertion
encodes the wrong value, fix the check exactly and runcheck it, then check4 on a proposals/ copy (delete after).
Validate with python3 -m tp check --store store --layers 1,2,3 --keep-going --author leon (grep your ids).

Report: colony/runs/2026-11-07-consistency/apply-<AP>.md: each item done (entity, old -> new version), items
passed to others, anything you could not apply exactly and why. Final reply: counts and the could-not-apply list.
