# Agent S: filing log (run 2026-11-08-frozen-point-datum, Stage 1)

## Filed
- **synthesis.frozen-point-datum-is-h** v1, "The frozen point's datum is H" (proposals/synthesis.frozen-point-datum-is-h/:
  entity.md, proof-main.tex, check.py, coverage.yaml, proposal.json). Status proved; uses
  mass.de-sitter-scale-frozen-point@6 and synthesis.de-sitter-static-boost-frozen-point@6 (premise() in every check
  function that relies on them); open_problem op.frozen-point-rational-datum; credit Leon Butler (direction), Claude Opus
  5.5 (proposal and drafting, run 2026-11-08-frozen-point-datum).
- Gate: runcheck 11/11 pass; check4 exit 0, 0 errors, 0 other findings (no W413; the first run had one W413 on the
  Lambda = 6 check, strengthened and rerun: verify/final/S-check4.log, and on the registered folder
  verify/final/S-check4-registered.log); validate_one ok, no E/W codes (only I305; verify/final/synthesis.frozen-point-datum-is-h.validate.json);
  propose_claim ok (verify/final/S-propose.log), hand-made folder moved aside to work/S/aside/, the three files compared
  identical (cmp), coverage.yaml copied back and parses.
- Statement in brief: over any field K of characteristic 0, Lambda != 0, d = Lambda/3: (i) everything rational in Lambda
  holds; (ii) ten constructions are each equivalent to d in K^2 (null vector of the boost plane, null eigen-directions,
  unit boost, unit W, R_h and kappa, the horizon point on the observer's radial line, I-perp isometric to the standard
  (1,4) space, Cl(I-perp) = Cl(1,4), the mirror's Cl(4,1)); (iii) with H all hold, witnesses rational in H; (iv) over Q,
  Lambda = 7/3 (no rational point on the bifurcation sphere at all) and Lambda = 6 (centres of discriminants 8 and -8);
  (v) own conditions: sphere point iff d is a sum of three squares; similarity to SO(1,4) iff d is a sum of two squares
  (fails at Lambda = 9); mirror complexified iff -d not a square (with H: -1 not a square); sqrt|Lambda| rescaling and
  Cl(1,3) + <+-1/3> = Cl(2,3), Cl(1,4) need sqrt 3; anti-de Sitter datum H' (Lambda = -3H'^2); operator join's matched
  scale needs sqrt 2 besides H.
- Kill conditions (pre-registered): K1 fired twice (the bifurcation sphere has rational points at Lambda = 6; SO(1,4)
  needs only a sum of two squares), so those two left the "exactly when" list: the RUN brief's phrasing "the
  bifurcation sphere has a K-point ... exactly when Lambda/3 is a square" is false as stated, and the theorem keeps only
  the point on the observer's radial line in (ii). K2 did not fire.
- Sweep: findings/sweep.md, checks work/S/sweep_checks.py (11 functions, all pass). Scan tools work/S/scan.py,
  ctx2.py, ctx3.py; raw data work/S/scan.json, cand.txt, rest_near.txt, sqrt_args.txt.

## What was already stored
- synthesis.cosmological-horizon-completed-pair, synthesis.de-sitter-entropy-pi-n-squared, de-sitter-mode-count,
  de-sitter-horizon-translation-is-conformal-null-rotation, de-sitter-temperature-frozen-point-norm,
  positive-null-energy-gives-r-premises, smallness-monomials-exact-hierarchy-casimir and others already take Lambda = 3H^2
  (class D), and most affected checks already sample Lambda = 3H^2 or Lambda/3 a square. No stored entity proves the
  square-class statement; the scratch evidence (work/realplace_tests.py) was re-proved, not cited; its "SO(1,4) as a
  group over Q iff Lambda/3 is a sum of two rational squares" is now proved in GA for the similarity reading.

## Decisions for Leon
- D1 (datum on the anti-de Sitter side). Lambda = 3H^2 forces Lambda >= 0 over an ordered field; the Lambda < 0
  clauses (two towers, translation bivectors, ascents, exceptional algebra) need H' with Lambda = -3H'^2.
  Recommendation: state those clauses with H', i.e. the datum is H with Lambda = 3 eps H^2, eps = +-1.
- D2 (statements written over R^{2,4}). synthesis.frozen-point-complement-window-lowest-causal is stated over R (Sylvester).
  Recommendation: restate it with Lambda = 3H^2 so its census holds over Q too (sweep B17); otherwise class A(R).
- D3 (group labels, 20 rows G1-G20). Their exact condition is "Lambda/3 a sum of two squares", weaker than a square.
  Recommendation: add the hypothesis Lambda = 3H^2 (Lambda = -3H'^2 for SO(2,3)) rather than renaming to SO(I-perp).
- D4 (exceptional algebra (i), sweep C1). Recommendation: normalise by H and H' (exact Cl(1,4), Cl(2,3), no sqrt 3) and
  keep the sheaf paper's sqrt|Lambda| rescaling as a remark with its sqrt 3 condition.
- D5 (literature import). dark-energy.imported-macdowell-mansouri-theorem-stelle-west (sweep B14) is an imported Fact:
  restating it is maintainer-only.
- D6 (mass datum). mass.weight-polynomial-two-series (C4) needs nu = sqrt(m^2/H^2 - 9/4) in K, a condition on m/H that H
  does not supply. Recommendation: take the weight (nu) as the datum, m^2 = (9/4 + nu^2) H^2, consistent with the
  mass-weight dictionary.
- D7 (wording). 19 statements over R by content still write sqrt(Lambda/3) or sqrt(3/Lambda) (sweep section 4).
  Recommendation: rewrite them to H, 1/H in the maintainer pass, for uniformity (no change of content).
- D8 (scope). Constant irrationals (sqrt 2, sqrt 3, sqrt 6 normalisations in the family, neutrino and Fock-model results)
  are not data and were classed A; whether the foundation's Q also asks for those to be restated is open.
- Note: the two sqrt 2 rows (C2 line-tame-wall gauge a = b, C3 operator join pair form) cannot be had over Q with any
  single rational datum together with H: H in Q and sqrt(Lambda/6) in Q are incompatible.
