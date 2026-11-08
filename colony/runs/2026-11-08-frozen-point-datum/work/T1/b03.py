import sys; sys.path.insert(0, "/home/claude/phys-graph/colony/runs/2026-11-08-frozen-point-datum/work/T1")
from rt import start, bump, edit
E = "obj.synthesis.cosmological-horizon-boundary-modes"
start(E)
edit(E, "entity.md", [
 ("Let $\\Lambda > 0$, fix a static observer, and let",
  "Let $\\Lambda = 3H^{2}$ with $H > 0$ in the base field, fix a static observer, and let"),
])
print(bump(E,
 note="the definition's hypothesis Lambda > 0 restated as Lambda = 3H^2 with H > 0 in the base field, the hypothesis under which the completed pair of synthesis.cosmological-horizon-completed-pair exists (its clause (v): over the series' rational scalars Lambda > 0 is not enough, Lambda = 7/3 having no pair; synthesis.frozen-point-datum-is-h (ii)(b), (iv)); e_W = W/H as there. Nothing else changed.",
 defect="The definition assumed only Lambda > 0, under which the completed pair it copies need not exist over the series' rational scalars (it exists exactly when Lambda/3 is a nonzero square, Lambda = 3H^2)."))
