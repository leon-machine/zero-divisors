# Fixes A: synthesis.geometric-modular-conjugations-on-a-generator-give-the-null-ground-state

Referee P verdict: SOUND WITH FIXES. All five fixes applied in place in proposals/<id>/ (entity.md,
proof-main.tex, check.py), together with Leon's decision 3 and the overlap split. The id is unchanged; only the title changed.
Script used: colony/runs/2026-11-06-edge-normality/work/A/fix/apply_fixes.py.

1. Title (fix 1): now "Field-level geometric modular conjugations on a generator give the null ground state"
   (84 characters). The one-liner says "at the field level" too.
2. Purity criterion (fix 2): added imported_from Araki1970 (Publ. RIMS 6 (1970/71) 385-442), flagged as cited
   from memory. The locator says only the direction "pure implies projection" is used. Formal (i) is now
   "proved, given Powers-Stormer and the purity criterion". Step 2 states that the criterion is not in the
   pinned Powers-Stormer Fact, which supplies only the factor property. A flag is added, and so is the status
   line. Decision for Leon (the referee's): add the criterion as a clause of
   synthesis.imported-powers-stormer-takesaki-disjointness.
3. Converse (fix 3): formal (v) is now "imported from memory". The pinned Fact
   angle.imported-theorems-deliver-their-hypotheses (and the stored KMS theorem) give only the modular group.
   Borchers' J U(s) J = U(-s) is pointed to Fact
   synthesis.imported-kuckert-modular-pct-spin-statistics-and-borchers-theorem(ii). The field-level twisted
   reflection rests on BGL1993 and BJL2002, both cited from memory. Step 7 adds that the sign from the
   continuation agrees with Step 4's proved positivity: this is a consistency check, not a proof. The
   extraction note and the status line say the same.
4. (vi)(c) local normality (fix 4): replaced with the trace-class route. chi_O(T_S - T_0)chi_O is X*X - Y*Y with
   X, Y Hilbert-Schmidt, so it is a difference of positive trace-class operators. The Powers-Stormer inequality
   (Fact (c)) and criterion (Fact (a)) then give local quasi-equivalence on every bounded interval. The formal
   now says "generator-Hadamard at every point, locally normal on every bounded interval".
5. Technical level (fix 5): it now says that, unlike the stored thermality theorem (which assumes no class), this
   result assumes the state gauge-invariant and quasi-free: it trades the modular group for the class
   assumption. The extraction note and lay level say the same.
6. Leon's decision 3 (sign of i is an open datum): eta is described as the orientation of the field
   algebra's imaginary unit relative to time. The series does not fix it, and (N+) assumes it. eta = -1 is a
   named assumption of the equivalence with (N+), not a convention. This is stated in formal (iv) and (v),
   the one-liner, the technical and lay levels, the extraction note and a new flag. Nothing states i = I_4.
7. Overlap split: the field-level result, the converse, sharpness (vi)(a) and (c), and the band example stay
   here. Step 8(d) and the net-level remark cite the companion proposal
   synthesis.modular-data-on-a-generator-fix-neither-the-translation-lift-nor-the-sign-of-i (to be retitled
   "Net-level modular data on a generator fix neither the translation lift nor the sign of i") as plain text,
   because it is not yet in the store, and do not reprove it.
8. Check, weak spot: the near-vacuous line "leading term of the band difference" (2 x 1/2 == 1) is replaced by
   an independent route. The s-series of int_0^2 sin(ps) dp is computed by exact integration of p^{2k+1} over
   [0, 2] and must equal the series of (1 - cos 2s)/s. check_charge_symmetry_and_the_states_it_admits is left
   as is (the referee listed it as not an error).

runcheck: all 5 functions pass (python3 colony/runcheck.py proposals/<id>/check.py).
check4: pending (orchestrator). validate_draft: pending (orchestrator).
Style scan: no em dashes. Neither banned word occurs.
