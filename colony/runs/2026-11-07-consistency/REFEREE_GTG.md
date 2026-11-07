# Run 2026-11-07-consistency: blind referees for the new GTG proofs (referees F1-F3)

Leon chose (7 November): each new Gauge Theory Gravity proof is checked exactly and reviewed blind before it
replaces the component proof. You are a referee. You have not seen the prover's work or report; do not read
colony/runs/2026-11-07-consistency/gtg-*.md or any extraction note named maintainer_pass_gtg_proof until your
verdicts are written. LAB = /home/claude/phys-graph. Never commit, never spawn agents, never kill processes, and
do not edit store/ (you report; a fix round edits). Other agents share 2 CPUs: at most two tp check runs.

Read: docs/gtg-dictionary.md, store/conventions.md (curvature sign, unit principle, the two boost-bivector signs),
lib/GA.py and lib/gtg.py.

Your entities: colony/runs/2026-11-07-consistency/referee_<F>.txt (ids whose proof-main.tex is a new GTG proof).
For each, read the formal statement (entity.md), proof-main.tex, the component proof it
replaces (git show 4160435:<entity folder>/proof-main.tex) and check.py, then:
1. Does the GTG proof prove the formal statement as written: every clause, quantifier, hypothesis, sign and
   constant? Is each step valid in GTG (h-bar and Omega as gauge fields on flat spacetime, the torsion equation,
   R(a ^ b) in the store's sign, Ricci/Weyl/Schouten maps, tractors as Cl(2,4) vectors)? Does each citation
   say what the step needs at its pinned version?
2. Recompute independently in your own scratch script (lib/GA.py, lib/gtg.py, Fractions or sympy rationals) the
   key identity of every step a reader could doubt. Do not reuse the check functions; write your own.
3. Read the new check_gtg_* functions: do they test the proof's computation (not a restatement of the answer),
   would they fail under a sign or factor mutation (try one or two mutations in a scratch copy, never in store/)?
4. Does the "In components" reading, if kept, agree with the GTG proof?
5. Language: any remaining tensor index, form or matrix doing work the GA could do; any bare imaginary unit; any
   "curved spacetime"; house style (no em dashes).

Verdict per entity: ACCEPT, ACCEPT WITH FIXES (list each exact fix), or REJECT (the gap, with your computation).
Report: colony/runs/2026-11-07-consistency/referee-<F>.md, one section per entity, with your scratch script
paths. Final reply: the verdict counts and each fix or rejection in one line, under 300 words.
