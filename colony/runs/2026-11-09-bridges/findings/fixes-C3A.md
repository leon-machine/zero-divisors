# Fixes C3A (fix round), run 2026-11-09-bridges

Proposal: synthesis.no-quarter-turn-odd-map-from-the-five-sphere-to-four-components (referee R3: SOUND WITH FIXES).
All five fixes applied in place; none disputed.

1. (S) attribution (entity.md, formal): "(Steenrod)" replaced by the referee's sentence verbatim: "This is Steenrod's
   theorem in the form obtained from the acyclic-carrier construction on regular complexes by carrying the deck group
   along; that passage is part of the assumption (S) and is not derived here." (S) stays an in-statement hypothesis,
   "cited from memory and not in the store" kept, so the Fact Leon decided to import can be written to fit.
2. Comparison with the three theories: lay sentence replaced by the referee's wording; extraction note gains "(S)
   belongs to the first of the three theories; (P) is additional background."
3. Check: the product identity (M.defect(c) == set() on all 48 orbits) now runs inside the loop over orders 4, 8,
   12, 16 in check_controls_other_orders_and_trivial_action; coverage.yaml clause updated to say so.
4. Extraction note: level-of-projective-spaces citation now reads "as quoted in secondary sources, contains the
   statement proved here (level 5 at m = 3); primary texts not read", with Comment. Math. Helv. 62 (1987) 286-291 and
   64 (1989) 661-674 (bibliographic data as confirmed by the referee; not re-checked by me).
5. Extraction note: graph note that the Atiyah-Hirzebruch import enters the past cone only through the cited
   theorem, whose clauses (2), (3) used here do not depend on it.
Fix 6 of the referee: no change required.

runcheck: 8 of 8 functions PASS after the fixes.
For the maintainer: the stored "holds given" for this entity will list the Atiyah-Hirzebruch import; see fix 5.

check4: pending (orchestrator)

Addendum (central gate W413 on check_controls_other_orders_and_trivial_action): tightened without removing any
assertion. Pinned per order from module-level tables: m + 1 and m terms of Delta_1(e_5), Delta_1(e_2); theta = -m/4 on
e_2 (x) d_1; 48 orbits; 8 generators of the coboundary space; the square as a cochain; verdict == (m = 4 mod 8) ==
(coefficient odd). Orders 2, 6: denominator 2 of -m/4. Trivial action: the same cochain is not a cocycle under the
antipodal action (defect pinned). Base S^3: 4 orbits in degree 5, square zero as a cochain. runcheck 8 of 8 PASS;
check4 (one authorised run): exit 0, 0 errors, 0 other findings.

check4: pending (orchestrator)
