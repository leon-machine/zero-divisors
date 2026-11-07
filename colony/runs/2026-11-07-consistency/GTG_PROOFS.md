# Run 2026-11-07-consistency: GTG proofs for the declared gravity results (provers P1-P3)

Leon chose (7 November): the gravity results whose proofs still work in components, forms or tractor slots get
proofs in Gauge Theory Gravity, checked exactly and reviewed blind before they replace the component proofs. You
act for Leon as maintainer. LAB = /home/claude/phys-graph (branch consistency-and-ga). Never commit, never spawn
agents, never kill processes; other agents share 2 CPUs (at most three tp check runs).

Read: docs/gtg-dictionary.md, store/conventions.md (curvature sign, the unit principle), lib/gtg.py and lib/GA.py
(the shared exact engines), colony/BRIEF.md (check rules), colony/runs/2026-11-07-consistency/ga-forms.md (the
forms rewriter's GA torsion equation, a tool you can reuse), and for each of your entities its current text, its
extraction notes and the reports that mention it (grep the id in colony/runs/2026-11-07-consistency/*.md).

Your entities: colony/runs/2026-11-07-consistency/gtg_<P>.txt. For each:
1. Write a proof in GTG: flat spacetime, gauge fields hb and Omega, covariant derivative, field strength R(a ^ b)
   in the store's sign, Weyl and Ricci maps as linear functions of bivectors and vectors, tractors as Cl(2,4)
   vectors with the tractor gauge field; forms as multivector fields. It must prove the same formal statement.
2. Make it the main proof (proof-main.tex); keep the component computation, shortened, as a labelled reading at
   the end ("In components: ..."), or drop it if the GA proof makes it redundant. Keep orig-proof-main.tex and every
   other file.
3. Add exact check functions for the GTG computation (lib/GA.py, lib/gtg.py, Fractions only, premise() for each
   premise used, mutation-sensitive) beside the existing ones; runcheck, then check4 on a proposals/ copy (delete it
   after).
4. Remove the outside_ga declaration if no stand-in remains; otherwise narrow it.
5. Apply any item for your entities in colony/runs/2026-11-07-consistency/items-for-gtg.md (the decided formal
   corrections and wording; read it at the start and again before you finish).
If a GTG proof is not achievable without new mathematics you cannot verify exactly, keep the component proof and
the declaration, and say why in your report. Never change a formal statement except as items-for-gtg.md decides.

Bookkeeping: version + 1 relative to store/lock unless already above it in this run (then keep); credit entry;
extraction note maintainer_pass_gtg_proof saying what was proved how and what was checked; no change of status,
links or assumes except as decided. Validate with python3 -m tp check --store store --layers 1,2,3 --keep-going
--author leon (grep your ids).
Report: colony/runs/2026-11-07-consistency/gtg-<P>.md: per entity, GTG proof written (yes/no), checks added,
declaration removed or kept and why, items applied. Final reply: counts and the not-achieved list.
