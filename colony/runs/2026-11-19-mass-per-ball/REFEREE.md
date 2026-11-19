# Referee brief, run 2026-11-19-mass-per-ball (blind)

You are the referee of this run. LAB = /home/claude/phys-graph (a git clone; branch run/2026-11-19-mass-per-ball).
Read colony/BRIEF.md (role: referee, and the standards) and colony/POLICIES.md first. Do not read
colony/runs/2026-11-19-mass-per-ball/RUN.md, DECISIONS.md, findings/ or work/. Do not edit anything under store/.
Do not commit, push, or run `tp check`, `tp repin`, `tp lock`, `tp build`. Do not spawn agents. One heavy process at a
time (2 CPUs). You may run `PYTHONDONTWRITEBYTECODE=1 python3 colony/runcheck.py <folder>/check.py` and your own
scratch scripts under colony/runs/2026-11-19-mass-per-ball/verify/scratch/ (exact arithmetic, fractions only).
The check4 logs of the three changed checks are in colony/runs/2026-11-19-mass-per-ball/verify/check4-*.log: read
them, do not rerun check4.

## What changed (a maintainer's edits of stored entities, not proposals)
The maintainer adopted one reading of a premise and restated what follows. `git diff c188ddcd -- store/` shows every
change; `git show c188ddcd:store/claims/<id>/entity.md` shows an entity as it was. Changed, under store/claims/:

1. dark-matter.e-equal-mass-per-unit-ball  (new postulate, version 1)
2. dark-matter.r3-one-cell-per-unshared-direction  (2 -> 3, the unit of thickness restated)
3. dark-matter.unit-ball-rule  (6 -> 7: statement, proof-main.tex, check.py, coverage.yaml)
4. dark-matter.contact-mechanism-returns-r3  (3 -> 4: statement, proof-main.tex, check.py, coverage.yaml)
5. synthesis.dark-to-baryon-total-uses-r1-r2-and-d-only-as-mass-per-unit-ball  (2 -> 3: status sentences only)
6. dark-matter.status-rule  (5 -> 6: clause (viii) and marked notes)
7. synthesis.unit-ball-clauses-hold-at-one-epoch-unless-hidden-direction-co-expands  (1 -> 2: clause (v), proof, check)
8. Notes: dark-matter.r1-equal-mass-per-quantum and dark-matter.r2-one-quantum-per-unit-ball (version kept),
   dark-matter.d-democracy-total-mass (3 -> 4), dark-matter.odd-towers-populated (1 -> 2), and the record of
   op.thickness-deposit-rule in store/open_problems.yaml (the paragraph dated 19 November).

## For each of 1 to 7: a verdict
SOUND, SOUND WITH FIXES (give the exact fix), OVERSTATED (give the true weaker statement), WRONG (give the
counterexample) or UNCLEAR (say what decides it). Check every proof step; check that each cited premise says what is
needed at the version now stored; break each changed check with at least two targeted perturbations and say what
happened; recompute the key numbers by your own route.

## Points to settle, specifically
A. unit-ball rule (iii). Is the equivalence right as stated: "there is a length d for which E holds with s = t = d
   if and only if s = t, f_3D = V_3/V_2 and f_5D = V_3/V_4"? Is anything hidden (positivity, the forms of f_3D and
   f_5D in the sourcing rule, the mirror, the two members of each odd pair)? Is "the three-dimensional share holds
   whatever the two densities are" true, and is the sentence "the two premises ... add nothing to it" a fair
   statement of what was proved, or too strong or too weak?
B. unit-ball rule (ii) and (iv). Does (ii) follow from the proof of (i) as claimed? Is (iv) right, and is it used
   correctly where other entities cite it (the premise E, the status observation (viii), the democracy premise's
   note)? In particular: is "the democracy premise is E at the de Sitter radius" what the mass-per-ball theorem's
   clause (ii) actually says, with the same qualification?
C. contact mechanism. Do (i) to (iii) go through with no use of a quantum's mass or number? Is clause I
   (indivisibility) still a meaningful clause when read on mass elements, or is it now empty and should be said to
   be? Is the formula of (iv), V_3/V_D (a_r/d)^(D-3), right in both dimensions, and consistent with the formula
   quoted in R3 version 3, (m_r/m_6)(V_3/V_D)(a_6/a_r)^3? Does the result still deserve its title?
D. premise E. Is every sentence of it true to the entities it cites? Is its "refutation condition" right? Does it
   overstate or understate what the adoption costs?
E. epoch theorem (v). Are the two scalings right in the theorem's own setting, and is "clause (iv) does not carry
   over" right?
F. Dependants not restated. These pin the old versions and were left as they are on the ground that their
   hypotheses (R1, R2 and R3 together) are stronger than the new ones, so their statements stay true:
   dark-matter.total-function-thickness, dark-matter.democracy-de-sitter-radius-unit-ball,
   dark-matter.two-roots-are-chord-arc-quarter, dark-tower-matter.imported-unit-ball-rule,
   dark-tower-matter.five-dimensional-towers, dark-tower-matter.population, dark-tower-matter.survival-sheets,
   simulations.imported-unit-ball-rule-family, simulations.cluster-bound-two-dimensions,
   simulations.effective-cross-section-sheet-matter, synthesis.lowest-causal-residues-zero-four-content,
   synthesis.no-rule-p2-licenses-gives-the-thickness-of-r3, dark-matter.two-reductions.
   For each: is its statement still true with R3 at version 3 and the rule at version 7, so that moving its pin is
   right? Name any whose statement or proof becomes false or misleading (for instance one that assumes R3 without R2
   and uses a tower's own cell radius, or one that calls R1 to R3 "the premises of the total").
G. Anything stale left elsewhere in store/ that still says R3's unit is each tower's own cell radius, or that the
   total rests on R1 to R3, as a present-tense fact (search the store; historical notes dated before 19 November are
   not stale).
H. Overclaiming at the title, one-liner and lay levels of 1 to 7; house style (no em dashes; never "honest",
   "honestly", "load-bearing"; no agent, run or method names in store text); geometric-algebra language rules.

Write colony/runs/2026-11-19-mass-per-ball/verify/R1.md: per entity the verdict and the fixes, then A to H, then
"For the maintainer" (anything Leon must decide). Your final reply is a short summary of that file.
