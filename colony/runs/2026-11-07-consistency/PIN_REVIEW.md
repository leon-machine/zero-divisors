# Run 2026-11-07-consistency: reviewing the stale pins (agent PR1)

This run changed many formal statements: GA rewrites (notation), unit rewrites, decided restatements (C1, C2,
B2, B3, B4, B6, E1 and the A corrections), and status changes (B1). Dependants still pin the old versions. A
pin says "the dependant was checked against this version of the target", so it must not move blindly. You act
for Leon as maintainer. LAB = /home/claude/phys-graph. Never commit, never spawn agents, never kill processes;
at most two tp check runs; other agents share 2 CPUs.

Read: colony/BRIEF.md (pins, versions), store/conventions.md (the unit principle), DECISIONS.md (what each
decided restatement changed), apply-AP1.md and apply-AP2.md (what was changed; AP1's "H11, not repinned").

Scope: every pin `<target>@<n>` in store/*/*/entity.md with n below the target's current version. Skip any
dependant whose id is in gtg_1.txt, gtg_2.txt or gtg_3.txt (a fix round may still edit those); list their stale
pins in your report for the orchestrator.

For each stale pin:
1. Get the target's formal statement at the pinned version and now. The store/lock commit history has old
   versions: `git log --format=%H -- <target>/entity.md` and `git show <commit>:<path>`; the lock file
   store/lock records each locked version. Diff the formal level.
2. Classify: (N) notation only: GA rewrite, unit renamed by the unit principle, wording, macros, an added
   "which unit acts where" sentence, a status-neutral clarification; (R) a restatement: a changed hypothesis,
   conclusion, constant, sign, clause, or a status change.
3. (N): repin to the current version.
   (R): read the dependant's use of the target (its proof steps, citations, and premise() calls). If the use
   still holds as cited (the cited clause and what the step needs are unchanged), repin and add one sentence
   to the dependant's extraction note `maintainer_pass_pin_review` saying which change was reviewed. If the
   dependant's text quotes the old statement, update the quotation (bump the dependant's version once, +1
   relative to store/lock unless already above it, with a credit entry). If the use no longer holds, leave the
   pin, and list it under "For Leon" with the evidence.
Do not change a formal statement, status, assumes edge or link. Validate at the end with
python3 -m tp check --store store --layers 1,2,3 --keep-going --author leon; fix anything you caused.

Report: colony/runs/2026-11-07-consistency/pin-review.md: counts (N repinned, R repinned, R updated, R left),
one line per R pin, the For-Leon list, and the skipped GTG dependants' stale pins. Final reply under 300 words.
