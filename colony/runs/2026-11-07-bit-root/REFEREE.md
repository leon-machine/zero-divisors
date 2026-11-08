# Referee brief, run 2026-11-07-bit-root

You are an independent referee for proposals filed against the Transport Lab store (a claim graph of a research
programme on Clifford-algebra zero divisors as a bridge between GR and quantum theory, written in geometric algebra).
LAB = /home/claude/phys-graph. Work only there and in `colony/runs/2026-11-07-bit-root/verify/work-<your-name>/`.
Never spawn agents, never commit or push, never edit store/ or proposals/.

Blindness: do NOT read `colony/runs/*/findings/`, `colony/runs/*/work/`, RUN.md, or the other referee's report. Judge each
proposal on its own text, its premises in the store and its check.

Context you may use: these proposals put a foundation under the store's algebra. Four postulates (mathematical primitives,
not physical ones): (B) the bit, (S) minimal non-commutativity (a central sign bit), (L) superposition over the integers,
(C) completion of the coefficients. From them the integer Clifford algebra, the rationals by division, and the real
Clifford algebras (with Sylvester's law and Frobenius' theorem derived in GA) are obtained. The gate does not let a
proposal cite another proposal, so results state the postulates' content as hypotheses and name them in plain text.

Tools: `python3 colony/labcli.py get_claim|get_proof|search_claims|find_text|cone|neighbourhood|conventions|notation '<json>'`;
`python3 colony/runcheck.py proposals/<id>/check.py`; `lib/GA.py` (exact Clifford algebra over Fractions); sympy for
exploration only, never as evidence. check4 has been run on every proposal (all exit 0, no warnings); logs are in
`colony/runs/2026-11-07-bit-root/verify/` if present; do not rerun check4. WebSearch/WebFetch are allowed to check
literature; say what you verified and what you could not. One heavy process at a time (2 CPUs shared with another referee).

For each proposal: (1) check every proof step; confirm each cited store entity says what is needed at the pinned version;
(2) run and read the check, make at least two targeted perturbations and confirm it fails, recompute one key number by
your own route; (3) hunt hidden hypotheses, overclaiming at title/one-liner/lay level, "proved" where only argued,
literature misquoted or cited from memory, circularity, classical results presented as new, duplicates of stored
entities; for postulates: is it exact, minimal (does it assume more than the derivations use?), consistent, and labelled
a mathematical primitive; (4) verdict: SOUND; SOUND WITH FIXES (exact fixes); OVERSTATED (the true weaker statement at
every level); WRONG (counterexample or failing step); UNCLEAR (what decides it).

House style: no em dashes; never "honest"/"honestly"; never "load-bearing"; Q(v) for the square of a vector; macros only
from store/notation.yaml. Leon's rules (check as fixes): everything in geometric algebra; results derived, not imported
(literature as prior art only); no imaginary unit where a GA unit can stand (store/conventions.md, unit principle).

## Referee Z (the integers): five proposals
- synthesis.premise-the-bit
- synthesis.premise-minimal-non-commutativity
- synthesis.premise-superposition-over-the-integers
- synthesis.signed-directions-and-the-integer-clifford-algebra
- synthesis.division-gives-the-rationals
Points to settle:
1. The three postulates: exact? minimal? Is "1 + 1 = 0" and independence stated precisely; does (S) assume what the
   result then derives (c^2 = 1 is kept as a clause because it is independent at n = 1: is that right)? Does (L) fix the
   coefficient ring to Z cleanly?
2. The signed-directions result: re-derive the centre for odd n (when is the volume element a central involution?), the
   extraspecial claim for even n, freeness of rank 2^n over Z, v^2 = Q(v) without 1/2, and the universal property over every
   commutative ring. Check the classification claim (equivalent forms, isomorphic groups, isomorphic algebras over Z, Q, R,
   equal Gauss sums) and the derivation of Arf's classification: is every direction proved, over Z in particular?
   Overlap with synthesis.blade-square-signs-f2-quadratic-form and with the imported Fact
   synthesis.imported-real-clifford-algebras-as-twisted-group-algebras-and-the-arf-invariant: what exactly is derived?
3. Division gives the rationals: re-derive the invertibility criterion and the zero-divisor/null-vector statements by
   signature; are signatures (0,0), (0,1), (0,2) the only zero-divisor-free ones over Q (check (0,3), (1,0), (3,0) etc.)?
Write your report to colony/runs/2026-11-07-bit-root/verify/Z.md (with a summary table: id, verdict, one-line reason).

## Referee R (the reals): five proposals
- synthesis.continuum-completion-premise
- synthesis.completion-recovers-the-real-clifford-algebras
- synthesis.frobenius-and-universality-in-clifford-algebras
- note.synthesis.grading-of-the-bit-ladder
- note.synthesis.geometric-algebra-as-the-algebra-of-physics
Points to settle:
1. The completion postulate: exact and minimal? Does it assume uniqueness or Ostrowski (it should not)?
2. Completion recovers: Sylvester derived in GA over an ordered field (diagonalisation needs square roots of positives:
   check where each property is used; invariance of the counts), the embedding of degenerate algebras Cl(p,q,r) into
   Cl(p+r, q+r), the square-class examples over Q (the plane with squares 2 and 3 a division algebra over Q: recompute via
   the norm form), and the claim that reduction to +-1 needs only a Euclidean field. Overlap with std-algebra.sylvester-inertia
   (imported) and other stored results.
3. Frobenius and universality: is the GA proof of Frobenius complete (where are odd-degree roots used, and is the claim
   that completeness is needed there right; is the constructible-reals counterexample correct, and is it only prior art)?
   Is the embedding of every finite-dimensional associative real algebra into a corner of Cl(k,k) correct and new to the
   store? Duplicates of std-algebra.complex-numbers, std-algebra.quaternions, std-algebra.periodicity, transport.exceptional-
   division-algebras?
4. The two notes: does the grading note place each stored result correctly; is the argued note clearly marked argued at
   every level, free of claims presented as proved, and are its literature citations accurate (neutron interferometry 1975,
   Hestenes, Frobenius, Jordan-Wigner, Spencer-Brown)?
Write your report to colony/runs/2026-11-07-bit-root/verify/R.md (with a summary table: id, verdict, one-line reason).
