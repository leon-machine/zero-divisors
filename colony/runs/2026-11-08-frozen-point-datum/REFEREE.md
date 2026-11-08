# Referee brief, run 2026-11-08-frozen-point-datum

You are an independent referee for proposals filed against the Transport Lab store (a claim graph of a research
programme on Clifford-algebra zero divisors as a bridge between GR and quantum theory, written in geometric algebra).
LAB = /home/claude/phys-graph. Work only there and in `colony/runs/2026-11-08-frozen-point-datum/verify/work-<your-name>/`.
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
`colony/runs/2026-11-08-frozen-point-datum/verify/` if present; do not rerun check4. WebSearch/WebFetch are allowed to check
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

## Referee F (the frozen point): one proposal
- synthesis.frozen-point-datum-is-h
Context replacing the paragraph above on the four postulates: this result says exactly which frozen-point (de Sitter)
constructions of the store need a square root of Lambda/3 in the base field K (characteristic 0), proves that each of
those in clause (ii) exists exactly when Lambda/3 is a square in K, that all hold when Lambda = 3H^2 with H in K, gives
counterexamples over Q, and states constructions needing more than H with their own exact conditions (clause (v)).
Its extraction note lists stored results affected on a rational reading; the store keeps them stated over R.
Points to settle:
1. Re-derive each equivalence in (ii) (both directions, over a general K), and each condition in (v): the bifurcation sphere
   (a point iff d is a sum of three squares?), the SO(1,4) similarity (iff d a sum of two squares?), the complexified mirror,
   the sqrt 3 and sqrt 2 cases. Recompute the counterexamples: Lambda = 7/3 (no rational point on the sphere: check the
   descent), Lambda = 6 (the rational point e1 + e2, and the discriminants 8 and -8).
2. Is the reflection-versor proof of the one-dimensional cancellation complete? Any hidden use of a square root?
3. Spot-check the extraction note's list: pick five listed results and confirm each really needs H (or the stated extra
   condition) when read over Q, and two results NOT listed that mention Lambda and confirm they are safe.
4. No imaginary unit (quadratic fields written as span{1, u} with u a GA element, or by discriminant); is that done
   correctly in the check?
Write your report to colony/runs/2026-11-08-frozen-point-datum/verify/F.md (summary table: id, verdict, one-line reason).
