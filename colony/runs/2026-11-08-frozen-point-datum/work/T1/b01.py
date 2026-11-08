import sys; sys.path.insert(0, "/home/claude/phys-graph/colony/runs/2026-11-08-frozen-point-datum/work/T1")
from rt import start, bump, edit
E = "synthesis.de-sitter-static-boost-frozen-point"
start(E)
edit(E, "entity.md", [
 ("Put $B_{\\Lambda} := e_{0}\\wedge W = e_{0}W$. Then, for every real $\\Lambda$:",
  "Put $B_{\\Lambda} := e_{0}\\wedge W = e_{0}W$. Then, for every $\\Lambda$ in the base field (ordered where a sign is used; in (iii) $\\Lambda = 3H^{2}$):"),
 ("\\item[(iii)] For $\\Lambda > 0$ the static patch has its Killing horizon at $R_{h} = \\sqrt{3/\\Lambda}$ with surface gravity $\\kappa_{\\Lambda} = \\sqrt{\\Lambda/3}$, so\n\\[\n\\kappa_{\\Lambda}^{2} \\;=\\; B_{\\Lambda}^{2} \\;=\\; Q(I_{\\Lambda}) ;\n\\]\nwith $H = \\sqrt{\\Lambda/3}$, $B_{\\Lambda} = H\\,u$",
  "\\item[(iii)] For $\\Lambda = 3H^{2}$ with $H > 0$ in the base field, the static patch has its Killing horizon at $R_{h} = 1/H$ with surface gravity $\\kappa_{\\Lambda} = H$, so\n\\[\n\\kappa_{\\Lambda}^{2} \\;=\\; B_{\\Lambda}^{2} \\;=\\; Q(I_{\\Lambda}) \\;=\\; H^{2} ;\n\\]\n$B_{\\Lambda} = H\\,u$"),
 ("period $2\\pi/\\kappa_{\\Lambda} = 2\\pi/\\sqrt{Q(I_{\\Lambda})}$, the counterpart",
  "period $2\\pi/\\kappa_{\\Lambda} = 2\\pi/H$, the counterpart"),
 ("so the static time closes with period $2\\pi/\\sqrt{-\\Lambda/3}$ and there is no horizon.",
  "so the static time closes with period $2\\pi/H'$, where $\\Lambda = -3H'^{2}$ with $H' > 0$, and there is no horizon."),
 ("For $\\Lambda > 0$ its horizon sits at $R = \\sqrt{3/\\Lambda}$ with surface gravity $\\sqrt{\\Lambda/3}$: the surface gravity squared is the frozen point's norm.",
  "For $\\Lambda = 3H^{2}$, $H > 0$, its horizon sits at $R = 1/H$ with surface gravity $H$: the surface gravity squared is the frozen point's norm."),
 ("smooth exactly when imaginary time has period $2\\pi/\\sqrt{Q(I)}$.",
  "smooth exactly when imaginary time has period $2\\pi/H$."),
])
edit(E, "proof-main.tex", [
 ("\\emph{Step 4 (horizon, surface gravity, period).} For $\\Lambda > 0$, $f(R_{h}) = 0$ at $R_{h} = \\sqrt{3/\\Lambda}$.",
  "\\emph{Step 4 (horizon, surface gravity, period).} For $\\Lambda = 3H^{2}$, $H > 0$, $f(R) = 1 - H^{2}R^{2}$ and $f(R_{h}) = 0$ at $R_{h} = 1/H$."),
 ("so $\\kappa_{\\Lambda} = \\Lambda R_{h}/3 = \\sqrt{\\Lambda/3}$ and $\\kappa_{\\Lambda}^{2} = \\Lambda/3 = B_{\\Lambda}^{2}$. With $H = \\sqrt{\\Lambda/3}$ and $e_{W} = W/H$,",
  "so $\\kappa_{\\Lambda} = \\Lambda R_{h}/3 = H$ and $\\kappa_{\\Lambda}^{2} = \\Lambda/3 = B_{\\Lambda}^{2}$. With $e_{W} = W/H$,"),
 ("$B_{\\Lambda} = Hu$ is $H$ times a unit boost in the plane of $e_{0}$ and $e_{W}$.",
  "$B_{\\Lambda} = Hu$ is $H$ times a unit boost in the plane of $e_{0}$ and $e_{W}$. Every quantity here is rational in $H$, so it is defined over any base field containing $H$; with only $\\Lambda$ given, $R_{h}$, $\\kappa_{\\Lambda}$, $e_{W}$ and $u$ exist over the base field exactly when $\\Lambda/3$ is a square there (the result synthesis.frozen-point-datum-is-h, clauses (ii) and (iii))."),
 ("the two points $x = \\pm\\sqrt{12/\\Lambda}\\,e_{0}$, where",
  "the two points $x = \\pm(2/H)\\,e_{0}$, where"),
 ("$\\exp(tB_{\\Lambda}/2)$ is periodic in $t$ with period $4\\pi/\\sqrt{-\\Lambda/3}$, its conjugation action with period $2\\pi/\\sqrt{-\\Lambda/3}$;",
  "with $\\Lambda = -3H'^{2}$, $H' > 0$, $B_{\\Lambda}^{2} = -H'^{2}$ and $\\exp(tB_{\\Lambda}/2)$ is periodic in $t$ with period $4\\pi/H'$, its conjugation action with period $2\\pi/H'$;"),
])
print(bump(E,
 note="clause (iii) and its proof (Step 4) restated with H as the datum: For Lambda = 3H^2 with H > 0 in the base field, R_h = 1/H, kappa_Lambda = H, e_W = W/H, u = e_0 e_W, period 2 pi/H (the definition H = sqrt(Lambda/3) dropped); the off-chart fixed points written -+(2/H) e_0; the preamble reads 'for every Lambda in the base field (ordered where a sign is used; in (iii) Lambda = 3H^2)'; clause (iv) and Step 5 write the Lambda < 0 period with H', Lambda = -3H'^2 (2 pi/H', 4 pi/H'); the technical level likewise. With the foundation's scalars in Q, sqrt(3/Lambda) and sqrt(Lambda/3) exist only when Lambda/3 is a rational square (synthesis.frozen-point-datum-is-h (ii), (iv)); with H every quantity of (iii) is rational in H. Clauses (i), (ii), (v) unchanged (rational in Lambda). The check already samples Lambda = 3H^2 at H = 1, 2, 1/3 and Lambda = -3H'^2, so it is unchanged.",
 defect="Clause (iii) defined H, R_h and kappa_Lambda as square roots of Lambda/3 and 3/Lambda, which exist over the series' rational scalars only when Lambda/3 is a rational square (for Lambda = 7/3 or 6 the unit boost, e_W and R_h do not exist over Q); the datum is now H with Lambda = 3H^2.",
 evidence="check.py::check_horizon_surface_gravity_and_bifurcation_sphere"))
