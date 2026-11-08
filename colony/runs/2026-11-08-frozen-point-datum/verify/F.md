# Referee F report: synthesis.frozen-point-datum-is-h

Referee F, run 2026-11-08-frozen-point-datum. Blind: findings/, work/, RUN.md and the other referee's report not read.
Work files: `colony/runs/2026-11-08-frozen-point-datum/verify/work-F/` (p1.py to p7.py perturbations, own.py and ads.py
independent recomputations).

## Summary

| id | verdict | one-line reason |
|---|---|---|
| synthesis.frozen-point-datum-is-h | SOUND WITH FIXES | Every clause (i) to (v) re-derived over a general K of characteristic 0 and correct; the fixes are an incomplete affected-results list in the extraction note, an SO(1,4)/SO(2,3) remark that claims more than clause (v) proves, one missing line in (v)(c), and one-liner wording. |

## 1. Proof steps, re-derived

Premises at pinned versions: `mass.de-sitter-scale-frozen-point@6` gives I_Lambda = n_inf + (Lambda/6) n_0, X(x), sigma = 1 - Lambda Q(x)/12, Q(I) = Lambda/3, all polynomial in Lambda. `synthesis.de-sitter-static-boost-frozen-point@6` gives W, B = e0 W, B^2 = Lambda/3, the slice x = r e1 with sigma and areal radius R = r/sigma, R_h = sqrt(3/Lambda), kappa = sqrt(Lambda/3), e_W = W/H, u = e0 e_W, and the bifurcation sphere {x0 = 0, Q(x) = -12/Lambda}. Both say what the proof uses.

(i) Rechecked by hand: Q(I) = d, Q(W) = -d, <W, I> = 0, B^2 = -Q(e0)Q(W) = d; half ad_B sends e0 to -W and W to -d e0 (Be0 = -W, e0B = W; BW = -d e0, WB = d e0) and kills vectors orthogonal to both; characteristic polynomial t^2 - d. Centre of the five-dimensional algebra: span{1, omega}, sign (-1)^10 = +1, so omega^2 = prod Q = d and omega'^2 = -d. Correct.

(ii) Each direction checked over a general K:
- (b): a^2 - d b^2 = 0 with (a, b) nonzero forces b nonzero and d = (a/b)^2. Correct.
- (c): Pi nondegenerate since d is nonzero; ad_B preserves Pi, kills Pi-perp, so t x_perp = 0 and t^2 = d. Eigenvectors are null (a = -tb, Q = (t^2 - d) b^2 = 0). Correct.
- (d), (e), (f), (g): (cB)^2 = c^2 d, Q(cW) = -c^2 d, R_h^2 = 1/d, r^2 = 4/d. Correct.
- (h) to (i) by induced isomorphism; (i) to (a): an idempotent a + b omega with b nonzero has a = 1/2, d b^2 = 1/4. Correct.
- (j) to (a): (a + b omega')^2 = a^2 - d b^2 + 2ab omega' = -1 gives ab = 0; a = 0 gives d = (1/b)^2. The b = 0 branch is in fact impossible (an injective map cannot send omega_1 to a scalar), and the proof's treatment of it is also valid. Correct.
- (a) to all: witnesses of (iii) recomputed (Q(v) = (1 - 1)/4 = 0, vv* + v*v = 1, v*v - vv* = e0 e_W = u, ad v = -Hv, sigma = 2 at x = (2/H) e1, R = 1/H). Correct.

(iv) Lambda = 7/3: 36/7 = 4/d; y = 7x/6 gives sum y_i^2 = 7; A^2 + B^2 + C^2 = 7 D^2, gcd 1; D odd gives 7 mod 8, impossible (sums of three squares mod 8 miss 7); D even forces A, B, C even. Descent correct. Lambda = 6: Q(e1 + e2) = -2 = -12/6, on S_6; centres omega^2 = 2 (field Q(sqrt 2), discriminant 8) and omega'^2 = -2 (discriminant -8) against omega_1^2 = -1 (discriminant -4); an isomorphism needs a^2 = -1 or b^2 = 1/2, impossible in Q. Correct.

(v)(a) Sum y_i^2 = d with y = d x/2. Correct, and 7/9 = 7 (1/3)^2 is not a sum of three rational squares.
(v)(b) Forward: T recomputed, Q(Te0) = d, Q(Te1) = -d, Te0 and Te1 orthogonal, Q(Te2) = Q(Te3) = -(a^2 + b^2), Q(TW) = -d^2, det T = d^3. Converse: (det T)^2 = c^5 d, so c = d s^2; d Q = <d, -d, -d, -d, -d^2> = <1,-1> perp <-d,-d> perp <-1>; three one-dimensional cancellations give <d, d> = <1, 1>, which represents d. Correct. Lambda = 9 descent modulo 3 correct.
(v)(c) Correct, but see fix 3.
(v)(d) Q(W/c) = -sgn(Lambda)/3; centre comparison gives 3 a square in both signs; converse by t W/c. Correct.
(v)(e) Correct; definiteness a^2 + |d| b^2 > 0 over an ordered field.
(v)(f) Correct as stated (the condition is on s^2). Stored proof of `synthesis.operator-join-point-spectrum-on-positive-energy-modules` has B = [pi pi] + lambda [omega omega], so only s^2 enters B; the oscillator definitions themselves carry s, sqrt 2 and sqrt hbar, which the note rightly treats as constant normalisations (optional remark below).

## 2. The reflection-versor cancellation

Complete. Q(z - y) + Q(z + y) = 4c is nonzero, so one of n = z -+ y is anisotropic; 2<z, z -+ y> = Q(z -+ y) uses only Q(z) = Q(y); -n x n^{-1} = x - 2<x, n> n / Q(n) checked from xn + nx = 2<x, n>; y0-perp = U because <y0, y0> = c is nonzero. Only division by 2 and by Q(n) is used; no square root anywhere. The repeated cancellation (by <1>, <-1>, <-1>) each has c nonzero. This is the standard reflection proof of Witt cancellation, correctly credited to Witt as prior art.

## 3. The check

`python3 colony/runcheck.py proposals/synthesis.frozen-point-datum-is-h/check.py`: 11 PASS, exit 0, all exact over Fractions with lib/GA.py; no sympy. Several functions are reductions of the proof's identities at samples (as coverage.yaml says, kind sampled); the decisive arithmetic (residue tables mod 8, 4, 3) is complete.

Perturbations (each run in work-F; all fail as they should):
- p1: W = n_inf - (Lambda/3) n_0: 9 functions FAIL.
- p2: (1 + d)/2 to (1 + d)/3 in T e1: similarity check FAIL.
- p3: 7 D^2 to 6 D^2 in the three-square search: Lambda = 7/3 check FAIL (6 = 1 + 1 + 4).
- p4: reflection without the minus sign: similarity check FAIL.
- p5: mirror extension with u^2 = +1 in place of -1: mirror check FAIL.
- p6: delta = 3 in place of 2 at Lambda = 6: quadratic-extension check FAIL.
- p7: e1 + e0 in place of e1 + e2 as the sphere point: Lambda = 7/3 check FAIL.

Independent recomputation (own.py, own bitmask Clifford product, not GA.py): omega^2 and omega'^2 at Lambda = 6, 7/3, -3, 27/4 are 2, -2; 7/9, -7/9; -1, 1; 9/4, -9/4, as stated. Similarity of <1,-1,-1,-1,-d> to <1,-1,-1,-1,-1> recomputed by Hasse invariants at p = 2, 3, 5, 7 with c = d (cross-check only, Hasse-Minkowski is literature): similar for d = 2, 5, 1/2, not for d = 3, 7/9, agreeing with "d a sum of two squares". ads.py: <1,-1,-1,-1,-d>, d < 0, similar to <1,1,-1,-1,-1> for d = -2, -5, -1/2, not for -3, -7/9, -6: "-d a sum of two squares", which supports fix 2. A rational search (denominators up to 12) finds no representation of 7 by three squares.

## 4. No imaginary unit

Correct. Quadratic fields are span{1, u}, u = f1 f2 with f1^2 = 1, f2^2 = -delta, so u^2 = delta; u is a bivector on generators disjoint from e0..e5, so it commutes with every blade of Cl(2,4), and span{1, u} times Cl(2,4) is Cl(2,4) over Q(sqrt delta). For delta = -1 the check appends (1, 1) to the reversed squares, u^2 = -1. No i, no complex arithmetic, `is_square_K` decides squares in Q(sqrt delta) correctly. I_4 could not stand here (it anticommutes with e0..e3, odd elements of the mirror's algebra), so an external commuting unit is the right choice. (Optional: for delta = -1 the convention's U3 would take the central pseudoscalar of an odd extension; f1 f2 is an equally valid GA unit, no fix required.)

## 5. Extraction note spot-check

Listed, confirmed to need H (or the stated extra condition) on a rational reading:
1. `synthesis.cosmological-horizon-completed-pair` (iv), (v): x = -+sqrt(12/Lambda) e0 and "a real pair exists exactly when Lambda > 0" (over Q: exactly when d is a square, clause (ii)(b)). Confirmed.
2. `odd-extensions.two-towers-one-curved-universe` (i) to (iii): doubled Cl(1,4) / complexified Cl(4,1) is (ii)(i), (ii)(j), (v)(c); (ii), (iii) use the unit fifth generator W/H. Confirmed (AdS side needs H' by (v)(e)).
3. `odd-extensions.line-tame-wall` (iii): a = b with 2ab = Lambda/3 gives a^2 = Lambda/6 = H^2/2, needs sqrt 2 besides H. Confirmed.
4. `odd-extensions.exceptional-algebra-residue-completion-both-sides` (i): w/sqrt|Lambda| with Cl(1,3) perp <+-1/3>; (v)(d) applies, needs sqrt 3. Confirmed.
5. `dark-matter.imported-frozen-point-de-sitter-radius`: radius ell and the label SO(1,4). Confirmed (the label needs the qualifier of fix 2).
Also looked at `interior.stabiliser-rotates-parabolic-reductive`, `mass.five-broken-generators`, `odd-extensions.two-readings-which-which`, `synthesis.operator-join-point-spectrum-on-positive-energy-modules` (2), `mass.weight-polynomial-two-series`: as described.

Not listed, confirmed safe:
- `interior.scale-tractor-leaves-cone`: I_g = n_inf + (Lambda/6) n_0, Q = Lambda/3, polynomial in Lambda.
- `odd-extensions.transport-constrains-frozen-point-only-through`: 2ab = Lambda/3 rational; O(1,1) acts transitively on each level set over any field ((a, b) = (t, c/2t) from (1, c/2)); non-isomorphism of the two signs' algebras over Q follows from that over R.
- (Also safe: `dark-energy.cosmological-constant-does-not-change-residue`, polynomial in Lambda; the temperature, entropy and mode-count results are stated with Lambda = 3H^2 or need pi, hence the completion, anyway.)

Not listed, but they need H on a rational reading in the same sense as listed items (found by grepping store entity.md files for explicit square roots of Lambda):
- `dark-energy.under-action-written-norm-parameter-laws` (formal (i), technical, one-liner): N = M_P sqrt(3/Lambda).
- `synthesis.promoted-norm-one-global-pair` (iv): N = M_P sqrt(3/Lambda).
- `synthesis.einstein-route-makes-n-initial-data` (formal): N = M_P sqrt(3/Lambda).
- `mass.mass-weight-dictionary` (formal, technical): "every mass in the theory is sqrt(Lambda) times a factor fixed by the weight"; with H that is sqrt 3 H, so as written it needs sqrt 3 besides H (or reads as H times a factor).
(Numerical or inequality uses such as `dark-matter.thickness-not-gravitational-quantity` (ell ~ 10^26 m) and `synthesis.cutoff-count-is-not-a-local-density-on-sds` (M < 1/(3 sqrt Lambda), equivalently 9 Lambda M^2 < 1) are harmless.)

## 6. Other points

- Hidden hypotheses: none found. Lambda nonzero and characteristic 0 are stated and are what is used (division by 2, 3, 6, d).
- Overclaiming: title and lay are fine. The extraction note's sentence on the SO(1,4) labels goes beyond clause (v) (fix 2). The one-liner's "the isometry type of I-perp ... exist" is loose (fix 4).
- Literature: discriminant / Hasse classification, Witt cancellation and Legendre's three-square theorem are named as background only and the proof relies on none of them (the one-dimensional cancellation and the descents are proved in the text). I did not check them on the web; the statements as named are the standard ones.
- Duplicates: none; `op.frozen-point-rational-datum` is the open problem it addresses, and the note correctly says it settles only the mathematical half (nothing is restated).
- House style: no em or en dashes, no banned words, Q(v) used, macros (Cl, nO, nInf, ip, R, Q) all in store/notation.yaml.
- Housekeeping: a `__pycache__/check.cpython-313.pyc` appeared in the proposal folder at 09:22:18, the time of my first runcheck run; I did not remove it (no edits to proposals/), and the main session may delete it.

## Required fixes

1. Extraction note, affected list: add `dark-energy.under-action-written-norm-parameter-laws`, `synthesis.promoted-norm-one-global-pair` (iv) and `synthesis.einstein-route-makes-n-initial-data` (N = M_P sqrt(3/Lambda), which is M_P/H with the datum H) to "need H", and `mass.mass-weight-dictionary` (sqrt(Lambda) times a factor: sqrt 3 besides H, or restate as H) to "needing more than H"; or state the criterion under which statements of physical magnitudes are excluded and apply it uniformly (then `dark-matter.imported-frozen-point-de-sitter-radius` would leave the list too). State how the list was compiled.
2. Extraction note, stabiliser labels: clause (v)(b) proves the condition only for an identification induced by a similarity of the forms. Write "need d (or -d) a sum of two squares for an identification induced by a similarity (clause (v)(b))"; for the anti-de Sitter side either add to (v)(e) one sentence with its proof ("a similarity of I-perp onto <1, 1, -1, -1, -1> exists iff -d is a sum of two squares in K", the (v)(b) argument with -d) or drop "(SO(2,3), so(2,3) on the anti-de Sitter side)" from the parenthesis. If the stronger reading (every group or Lie algebra isomorphism) is wanted, it is classical for odd dimension but not proved here, and must be said so.
3. Proof of (v)(c): add the line that span{1, omega'} with d nonzero has no nonzero nilpotent ((a + b omega')(a - b omega') = a^2 + d b^2), so "no idempotent other than 0, 1" is equivalent to "a field".
4. One-liner (and the matching phrase in (iii)'s summary sentence if desired): "the isometry type of I_Lambda-perp" to "the isometry of I_Lambda-perp with <1, -1, -1, -1, -1>".

Optional: the Setting sentence "the identities of their clauses (i) are polynomial" understates it (the Lemma's three clauses and the Proposition's (ii) and (v) are polynomial too; (iii) and (iv) are the ones analysed); in (v)(f) a sentence that the module's own s, sqrt 2 and sqrt hbar are constant normalisations, and only s^2 enters the pair form.
