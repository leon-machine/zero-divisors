# Referee brief R2, run 2026-11-24-number-theory: the stored two-mode theorem, line by line, and its prior art

You are a blind referee. LAB = /home/claude/zero-divisors (a git clone; branch run/2026-11-24-number-theory).
Read `colony/BRIEF.md` first (standards, tools, the section "Role: referee"). Do NOT read
`colony/runs/2026-11-24-number-theory/findings/`, `.../work/`, `.../RUN.md`, `.../REPORT.md` or
`.../verify/referee-R1.md`. Do not edit anything under `store/`. Do not spawn agents. Do not run
`colony/check4.py` or `python -m tp check`. One CPU-heavy process at a time; never kill processes you did not
start. Scratch files go in `colony/runs/2026-11-24-number-theory/verify/scratch-R2/`. Write your report to
`colony/runs/2026-11-24-number-theory/verify/referee-R2.md`.

## Why
A new result (additive weights on rational projectors are linear in every size n >= 4) rests entirely on one
stored theorem, which was accepted on 18 November with review state "draft" and has not had a line-by-line
review by a second reader:

    store/claims/synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear/
        entity.md   proof-main.tex   check.py   coverage.yaml

Its clause (iii): every function on the symmetric idempotents of M_4(Q) that adds on orthogonal ones, with
values in a rational vector space and no sign condition, is the restriction of a linear functional. If true and
new, this answers (for n = 4, in a signed form) a question posed as open in the literature (Mushtari 2001,
"Problem G"), so it deserves a hostile reading.

## Part 1: the theorem
Read the statement and the whole proof. For clause (iii) in particular:
1. State the logical skeleton of the proof in your own words (five or six steps) and say for each step whether
   it is proved on paper, carried by a finite computation in the check, or argued.
2. Step by step, look for gaps. Points that need a decision: (a) the passage from additive weights to frame
   functions and to a linear map on the group algebra of rational rotors modulo frame relations; (b) that the 24
   octahedral rays span a copy of M_3(Q) in the quotient (rank 15 of the relations; what exactly is the
   quotient); (c) the identity of 34 frames that puts the ray of 2 + B_1 in the span: verify it yourself, in
   exact arithmetic, from the certificate in check.py, by your own code (each listed set is an orthogonal frame
   of Q^4; the rational combination of frame indicators equals the indicator of (2,1,0,0) plus a combination
   supported on octahedral rays); (d) factorisation of integer rotors of norm 5^k into the six rotors 2 +- B_k
   and a unit (the table modulo 5; the induction); (e) "for any rational half turn, a suitable power of 2 + B_1 is
   conjugated by it to an integer rotor of norm a power of 5": is the existence of the exponent proved for
   EVERY rational bivector, including those whose norm is divisible by 5 or by 2? (f) the commutant argument
   (the class of a half turn is its rotation matrix times a central factor); (g) the frame relation of an
   orthogonal triple forcing the factor to be 1; (h) that half turns generate the group of rational rotors
   modulo scalars, and how the result passes from generators to all rays.
3. Is the conclusion for values in an arbitrary rational vector space V justified, or only for V = Q?
4. Try to refute it. Search for an additive weight on the rays of Q^4 that is not a quadratic form: for
   instance functions of the primitive integer vector modulo 2, 4, 8, 3 or 5; of the 2-adic or 5-adic valuation
   of r.r; of the class of r.r modulo squares. A finite exact test: take all primitive integer rays with entries
   in a box (say |entries| <= 3 or 4), all orthogonal frames among them, and compute the dimension of the space
   of functions on those rays whose sum over every frame is constant; compare with 10 (quadratic forms) and
   report how the excess behaves as the box grows. (The stored theorem says the excess must be killed by frames
   reaching outside the box; say whether your numbers are consistent with that.)
5. Run the stored check (`python3 colony/runcheck.py store/claims/<id>/check.py`), read it against
   coverage.yaml, and break it with at least three targeted perturbations (copies in your scratch folder).
6. Clauses (i), (ii), (iv), (v): check each briefly.

Verdict for the stored theorem: SOUND, SOUND WITH FIXES (exact fixes), OVERSTATED (true weaker statement), WRONG
(counterexample), or UNCLEAR (what decides it). If any step is argued and not proved, say exactly which, and
whether status "proved" is justified.

## Part 2: prior art
The entity's note says the prior art was read through abstracts and a summary only. Try to read it properly,
using web search and fetch:
- D. Kh. Mushtari, "Some remarks on measures on orthogonal rational projections and the rational sphere",
  Lobachevskii J. Math. 9 (2001) 47-53. Find the text. What exactly is Problem G? What are Propositions 3 and 4?
  Does the paper prove anything for n = 4 that overlaps clause (iii)?
- D. Mushtari, Int. J. Theor. Phys. 34 (1995) 1627 and Mat. Zametki 64 (1998) 584: what is proved (signed
  measures on all rational idempotents)? Does clause (iii) follow from it? (The note says it does not.)
- Any later work that solves Problem G or the n = 4 case: search for Gleason-type theorems over the rationals
  ("rational sphere", "Q^n", "frame function", "orthogonal rational projections"), including Godsil and Zaks,
  Meyer, Havlicek-Krenn-Summhammer-Svozil, Hamhalter, Dvurecenskij, and anything citing Mushtari 2001.
Report, for each source, whether you read the paper itself, an abstract, or a secondary description, and quote
nothing longer than a short phrase. State plainly whether a claim of novelty for clause (iii) is supportable,
unsupported, or contradicted.

## Report
`verify/referee-R2.md`: verdict line; the skeleton; numbered answers to Part 1 points 1-6 with what you
recomputed; exact fixes if any; Part 2 findings with the reading level of each source; a short list of what only
the maintainer can decide. Your final message back: under 350 words, the verdict, the most serious findings,
the prior-art conclusion, and the path of the report.
