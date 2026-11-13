# Referee brief, run 2026-11-12-rung-state

You are an independent referee. LAB = /home/claude/phys-graph (a git clone on branch test/rung-state-forced-or-datum).
Do not commit, push, switch branches, spawn agents, or edit anything under store/. Your scratch folder is
colony/runs/2026-11-12-rung-state/verify/work-R/. Do not read colony/runs/2026-11-12-rung-state/work/.
Read colony/BRIEF.md (the "Role: referee" section and the Standards) first.

The work under review was written by another AI model in one session, for the maintainer (Leon), who asked: could
there be a mechanism for the collapse of the wave function in this framework, building on the tower of transport
steps, and if not, say so. Two new claims in store/claims/:
  1. synthesis.state-of-a-new-rung-unique-symmetric-extension-is-the-half-weight
  2. synthesis.selector-candidates-on-the-tower-integer-states-parity-deterministic-laws
Each has entity.md (statement at four levels), proof-main.tex, check.py, coverage.yaml. The pre-registrations are
colony/runs/2026-11-12-rung-state/PREREGISTRATION.md and PREREGISTRATION-2.md (committed before the computations;
`git log --stat` shows the order), and RESULT.md records the first outcome.

Tools: `python3 colony/labcli.py get_claim|get_proof|search_claims|find_text|cone|conventions '<json>'`;
`python3 colony/runcheck.py <abs path>/check.py`; lib/GA.py (exact Clifford algebra over Fractions; no sympy).
The stored claim the question came from is one-relation.record-chain-votes-measurement-without-collapse; the premise
used is synthesis.premise-positivity-of-values.

Do all of the following.
A. For each claim: check every proof step; confirm each cited store entity says what the proof needs; read the
   check and break it with at least two targeted perturbations; recompute at least two key numbers by your own
   route in your own code (for example: the uniqueness of the invariant extension; the two rotor classes; the five
   integer states; the centre of the even subalgebra; 9/25, 16/25 and 24/25). Report anything wrong, unproved,
   or weaker than stated.
B. Hidden hypotheses and overclaiming: is "symmetry of the step" (the sign changes of the new generators) the
   right group, too small, or too large, and does the uniqueness in claim 1 (ii) survive other reasonable choices
   (all isometries of the new plane; only those preserving the adjoint; the exchange alone)? Does anything depend
   on working over Q? Do the titles, one-liners and lay levels say more than the proofs?
C. The pre-registrations: were the kill conditions fair tests, or written so the predicted outcome was the only
   possible one? Say plainly if a hypothesis was a straw man.
D. The conclusion drawn: "the stored content holds no selector; one could be added only as new premises". Is
   that supported by what was computed, or is it broader than the evidence (four named candidates, finite towers)?
E. Look for a mechanism yourself. Spend real effort here: is there a candidate the author missed, in the store
   (search it: descent, eviction, pinching, the one-way door, modular period, horizons and boundary modes, the
   orientation bit, the infinite tower and disjoint representations, the integer forms, positivity (P)) or outside
   it (name the literature; say when you cite from memory)? For each candidate you find: what it would deliver
   (ending interference, selecting, both), what it needs, and whether a quick exact computation supports or kills
   it; run the computation if it is small.
F. Verdict per claim: SOUND, SOUND WITH FIXES (exact fixes), OVERSTATED (give the true weaker statement), WRONG
   (counterexample), UNCLEAR (what decides it). And a one-paragraph answer to the maintainer's question in your own
   words: is there a mechanism, and how confident should he be in the answer given what was and was not checked.

Write colony/runs/2026-11-12-rung-state/verify/R-opus.md. Final message to the orchestrator: the two verdicts with
main reasons, the answer to E (candidates found and what happened to each), and the paragraph of F.
