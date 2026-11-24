# Referee brief R3, run 2026-11-24-number-theory: imports, one derived result, three amendments

You are a blind referee. LAB = /home/claude/zero-divisors (branch run/2026-11-24-number-theory; `git diff HEAD`
and `git status` show exactly what this round changed relative to the last commit). Read `colony/BRIEF.md`
first (standards, tools, "Role: referee"). Do NOT read `colony/runs/2026-11-24-number-theory/findings/`,
`.../work/`, `.../RUN.md`, `.../REPORT.md`, `.../verify/referee-R1.md` or anything under
`.../verify/scratch-R2/`. Do not edit anything under `store/`. Do not spawn agents. Do not run
`colony/check4.py` or `python -m tp check`. One CPU-heavy process at a time; never kill a process you did not
start. Scratch files in `colony/runs/2026-11-24-number-theory/verify/scratch-R3/`. Write your report to
`colony/runs/2026-11-24-number-theory/verify/referee-R3.md`.

To run a check: `python3 colony/runcheck.py store/claims/<id>/check.py` from the repository root. Stored
entities: `store/claims/<id>/entity.md`, `proof-main.tex`, `check.py`, `coverage.yaml`.

## What to review (all under store/claims/)

### 1. Four new imported Facts (status: imported; no checks; cited from memory or through secondary sources)
 a. synthesis.imported-stolz-level-of-real-projective-spaces-under-the-quarter-turn
 b. synthesis.imported-hurwitz-zeta-values-and-dirichlet-l-functions-as-hurwitz-sums
 c. synthesis.imported-class-number-formula-at-zero-for-negative-discriminants
 d. synthesis.imported-zeta-of-a-real-quadratic-field-at-minus-one-as-a-divisor-sum
For each: is the mathematical statement a correct classical theorem exactly as written (ranges, signs,
normalisations, definitions such as "reduced form", "w(D)", "fundamental discriminant", the equivalence of the
two formulations of the level, the clause on removing Euler factors "for all s")? Test numerically with your own
code wherever a statement can be tested (b, c, d certainly; for a, test what can be tested: the small cases
m = 1, 2 by explicit maps, consistency with bounds). Use web search and fetch to check the bibliographic data
and, where you can reach them, the statements (for a: any source giving Stolz's theorem; the entry says the paper
itself was not read). Is each entry candid about what was and was not read? Is anything imported that is
stronger than what the using results need?

### 2. One new derived result
 synthesis.definite-side-rung-count-on-every-quarter-turn-lens-wall-is-the-level
Check the derivation from the stored reduction (clause (1) and the opening paragraph of
synthesis.definite-side-rung-count-on-the-quarter-turn-lens-wall-of-dimension-five, version 1) and the import;
the translation of residues from m = n + 1 to n; the listed values; clause (ii) (does the stored sufficiency
clause give k <= e(L) on every side? is the lower bound quoted at the right version?); clause (iii) and its
proof; clause (iv) (is it worded as a remark only?). Is "proved" the right status for a result whose whole
content is an import plus a stored reduction? Overclaiming in title, one-liner, lay level?

### 3. Three amendments to stored results
 a. synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height, version 2 -> 3 (restatement of clause
    (2); new uses edge to synthesis.order-of-the-doubled-dying-line-on-quarter-turn-lens-walls-is-a-valuation-
    in-the-ring-of-the-quarter-turn; proof gains a paragraph; coverage excuse). Is the restated clause correct
    and consistent with clauses (1), (3), (4) and with every level (technical, lay, one-liner)? Is the
    `amendments` entry accurate? Is there any circularity: the order result must not rest on this one (check
    its `uses`, its clause (iii), now a pointer, and its proof and check). The dependant
    synthesis.three-rungs-do-not-complete-the-quarter-turn-lens-walls-on-any-side had its pin moved from @2 to
    @3: does what it uses of this result still hold at version 3?
 b. synthesis.window-energy-tests-with-free-spacing-admit-twists-half-third-and-quarter, version 1 -> 2
    (Remark 1 restated to point at synthesis.thermal-test-on-the-ground-conic-holds-at-exactly-three-points,
    which uses this theorem; no edge is drawn for the remark). Is that sound (no circular dependence of
    statements)? Are the lay level and one-liner now accurate?
 c. synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear: wording of its
    `extraction.note` only (the sentence on "more than two modes"); version kept. Is the new wording accurate?

### 4. Two results changed inside this round (not yet merged)
 a. synthesis.character-sums-over-the-twist-fibres-of-an-array-are-dirichlet-l-values: its three hypotheses are
    now the imported Facts 1b, 1c, 1d. Do the statement, proof and check still fit together? Does each clause
    cite the right clause of the right import?
 b. synthesis.order-of-the-doubled-dying-line-on-quarter-turn-lens-walls-is-a-valuation-in-the-ring-of-the-
    quarter-turn: clause (iii) turned into a pointer; one check function renamed. Anything left that claims
    more than a pointer?

### Across
House style (no em dashes; never "honest", "load-bearing", "clever"; Q(v) for the square of a vector; no agent,
run or method names in statements). `outside_ga` declarations accurate? Anything in the diff that should not be
there?

## Report
Per item: verdict (SOUND / SOUND WITH FIXES / OVERSTATED / WRONG / UNCLEAR), the exact fixes (quote the text and
the replacement), what you recomputed or looked up, and for literature the reading level (paper, abstract,
secondary). Never quote more than a short phrase from a source. End with what only the maintainer can decide.
Your final message back: under 350 words, verdicts and the serious findings, and the report's path.
