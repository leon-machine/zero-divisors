# Referee brief 3, run 2026-11-12-rung-state (a short pass on the fixes)

LAB = /home/claude/phys-graph (branch test/rung-state-forced-or-datum). Do not commit, push, switch branches,
spawn agents, or edit anything under store/. Scratch: colony/runs/2026-11-12-rung-state/verify/work-R3/.

The second review (verify/R2-opus.md) found two mathematical errors, one of them introduced by a fix made after
the first review, and judged one claim overstated. The author has applied the fixes. Fixes have introduced errors
before, so check the changes themselves. The changes are the uncommitted working-tree differences against commit
c19c7d973e34230d83842477ff8930562a14320a: run `git status --short` and `git diff c19c7d973e34230d83842477ff8930562a14320a -- store/claims` (one claim folder was renamed:
synthesis.infinite-strings-tail-classes-and-no-reading-law-inside-the-algebra is now
synthesis.infinite-strings-tail-classes-and-reading-rules-linear-and-not; read the new folder in full).

Do this:
1. For every fix listed in the "Verdicts" of verify/R2-opus.md for claims 1 to 4: was it applied, and applied
   correctly? List any not applied.
2. Read every sentence that is new or changed in the four entity.md files and four proof-main.tex files. For each
   new mathematical statement, verify it (by hand or by your own exact computation). Pay particular attention to:
   claim 1 (ii) "Dependence on the group" and its two counterexamples; claim 1 (iv) the step moving the two-valued
   weight; claim 3 (iii) the corrected c = 0 statement and the non-uniformity statement; claim 3 Reading's last
   sentence (the ignorance reading in the limit); claim 4 (i) the three orbits under finite changes and rung
   permutations and the statement that no single rung's value is constant on a class; claim 4 (ii) the symmetric
   state as a factor state disjoint from every string state; claim 4 (v) the comparison rule and its frequency
   ceil(2^n a^2)/2^n; claim 4 (vi) the agreement of the two rules; claim 4 Reading.
3. Titles, one-liners, technical and lay levels of the four claims as they now stand: any sentence that says more
   than its proof.
4. The new or changed check functions: do they test what they say? Break two.
Report only problems and a one-line "correct" per item checked; no summary of what the claims say.
Write colony/runs/2026-11-12-rung-state/verify/R3-opus.md. Final message: the list of problems with exact fixes
(or "none"), and for each of the four claims one of: READY, or NOT READY with the reason.
