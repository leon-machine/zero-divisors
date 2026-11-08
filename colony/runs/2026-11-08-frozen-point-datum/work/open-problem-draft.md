# Draft open problem: the frozen point's rational datum (to log when the store is free)

Proposed id: op.frozen-point-rational-datum (area: completion / dark-energy)

Statement: Over Q, Q(I_Lambda) = Lambda/3, so statements that normalise by it, use the static boost's null
eigen-directions, or name an algebra type built on it hold only when Lambda/3 is a rational square (for SO(1,4) as
a group over Q, a sum of two rational squares). Decide the series' rational datum: H (Lambda = 3H^2) or Lambda; restate
the affected results accordingly.

Affected (exact checks, 7 Nov 2026, scratchpad/realplace/realplace_tests.py, 30 checks, 0 failures):
- odd-extensions.exceptional-algebra-residue-completion-both-sides (i): Cl(1,3)+<+1/3> ~ Cl(2,3) false over Q and Q(i)
  (centres Q(sqrt-3) vs Q(i)); true over Q(sqrt 3) and R.
- synthesis.cosmological-horizon-completed-pair: no rational null directions unless Lambda/3 square (Lambda = 7/3: no
  rational point on the bifurcation sphere); clause (v) becomes "iff Lambda/3 a nonzero square".
- synthesis.de-sitter-static-boost-frozen-point (iii): unit boost, null eigen-directions, R_h need H in the field.
- synthesis.mirror-extensions-causal-convention (v) (audit E0): "doubles ours to Cl(1,4), complexifies the mirror's"
  needs Lambda/3 square (Lambda/3 = 2: centres Q(sqrt2), Q(sqrt-2)). Same for odd-extensions.two-towers-one-curved-universe (i).
- dark-matter.imported-frozen-point-de-sitter-radius (audit E0): label "SO(1,4)" (also frozen-point-field-space,
  curvature-only-tractor-actions, imported-grip-area-casimir-form; identities themselves survive).
- synthesis.operator-join-point-spectrum-on-positive-energy-modules: rational H and the unitary pair form together need Q(sqrt 2).
Safe: transport spine with +-1 generators (Cl_Q(p,q) mirrors Cl_R); type criteria "N iff pq != 0", "C iff p-q = 1 mod 4"
describe +-1 forms only. Caution: Q(i) as base field breaks twistor-algebra (iv) non-isomorphisms.
Fix: take H (or kappa_Lambda) as the rational datum, Lambda = 3H^2.
Audit note: the finitist audit's E1 "eliminable" is right for the sqrt removals but pins Lambda's square class for
frozen-point statements; two E0 rows carry the dependence with no sqrt in the text.
