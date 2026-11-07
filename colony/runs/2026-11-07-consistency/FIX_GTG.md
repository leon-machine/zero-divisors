# Run 2026-11-07-consistency: fix round on the GTG proofs (fixers FX1-FX3)

Blind referees reviewed the new GTG proofs. You apply referee <F>'s findings to the entities in
colony/runs/2026-11-07-consistency/referee_<F>.txt. You act for Leon as maintainer. LAB = /home/claude/phys-graph.
Never commit, never spawn agents, never kill processes; at most two tp check runs; other agents share 2 CPUs.
Another agent (pin review) is editing pins in other entities; do not touch entities outside your list.

Read: colony/runs/2026-11-07-consistency/referee-<F>.md (the findings and the referee's scratch scripts),
GTG_PROOFS.md (the provers' brief and bookkeeping), docs/gtg-dictionary.md, store/conventions.md, lib/GA.py,
lib/gtg.py, and the prover's report gtg-<P>.md for context.

For each finding:
1. Verify it yourself by exact computation (the referee may be wrong; say so with your computation if so).
2. If it is right, fix it: a sign, factor or step in a proof or technical level; an outside_ga declaration made
   exact (narrowed, widened, or removed); a check that does not detect a mutation (tighten it and confirm a
   mutant now fails); a statement in the formal level that is only notation (GA in place of forms or
   components, a unit named by the unit principle) is fine to rewrite (Leon chose to rewrite all non-GA
   entities), but a change to a formal statement's mathematics (a sign, constant, hypothesis or clause) is not:
   list it under "For Leon" with the evidence and the exact proposed text, unless items-for-gtg.md decided it.
   A false sentence in a proof that the proof does not need is removed or corrected.
3. Missing uses edges: add a uses edge only when the proof cites the entity for a step it needs and the target
   is proved, imported or a definition (adding a premise edge to a postulate or conjecture changes what the
   result rests on: list it for Leon). Pin it at the target's current version.
4. Stale pins in your entities: review each as in PIN_REVIEW.md (notation-only: repin; restatement: repin only
   if the use still holds, else list for Leon).
Bookkeeping: version stays as already bumped in this run (+1 relative to store/lock; bump only if the entity is
at its locked version), credit entry, extraction note maintainer_pass_gtg_review (findings applied and how they
were checked). runcheck each changed check, check4 on a proposals/ copy (delete it after). Validate with
python3 -m tp check --store store --layers 1,2,3 --keep-going --author leon.

Report: colony/runs/2026-11-07-consistency/fix-<F>.md: per finding, applied / disputed (with computation) /
for Leon. Final reply: counts and the For-Leon list, under 300 words.
