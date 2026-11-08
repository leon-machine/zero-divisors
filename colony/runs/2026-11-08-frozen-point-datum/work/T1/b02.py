import sys; sys.path.insert(0, "/home/claude/phys-graph/colony/runs/2026-11-08-frozen-point-datum/work/T1")
from rt import start, bump, edit
E = "synthesis.cosmological-horizon-completed-pair"
start(E)
edit(E, "entity.md", [
 ("the past and future endpoints $i^{-}$ and $i^{+}$ of the static observer's worldline, at $x = \\mp\\sqrt{12/\\Lambda}\\,e_{0}$, where",
  "the past and future endpoints $i^{-}$ and $i^{+}$ of the static observer's worldline, at $x = \\mp(2/H)\\,e_{0}$, where"),
 ("\\item[(v)] \\emph{Existence, and the mirror.} A real pair exists exactly when $\\Lambda > 0$: for $\\Lambda = 0$ the plane of $B_{0} = e_{0}\\nInf$ is degenerate, and for $\\Lambda < 0$ the plane of $B_{\\Lambda}$ is definite and has no real null vectors (its complexification",
  "\\item[(v)] \\emph{Existence, and the mirror.} A pair over the base field $K$ exists exactly when $\\Lambda/3$ is a nonzero square in $K$, that is $\\Lambda = 3H^{2}$ with $H \\neq 0$ in $K$ (over an ordered $K$ this needs $\\Lambda > 0$, and $\\Lambda > 0$ is not enough: for $\\Lambda = 7/3$ over $\\Q$ there is none): for $\\Lambda = 0$ the plane of $B_{0} = e_{0}\\nInf$ is degenerate, and for $\\Lambda < 0$ over an ordered $K$ the plane of $B_{\\Lambda}$ is definite and has no null vectors over $K$ (its complexification"),
 ("conformal infinity, $x = \\mp\\sqrt{12/\\Lambda}\\,e_{0}$, where the scale",
  "conformal infinity, $x = \\mp(2/H)\\,e_{0}$, where the scale"),
 ("A real pair exists only for $\\Lambda > 0$. In the mirror,",
  "A pair over the base field exists only when $\\Lambda/3$ is a nonzero square there, $\\Lambda = 3H^{2}$. In the mirror,"),
 ("Killing time acts at rapidity $\\kappa_{\\Lambda} = \\sqrt{\\Lambda/3}$.",
  "Killing time acts at rapidity $\\kappa_{\\Lambda} = H$, $\\Lambda = 3H^{2}$."),
])
edit(E, "proof-main.tex", [
 ("$|x_{0}| < \\sqrt{12/\\Lambda}$, the rotor flow",
  "$|x_{0}| < 2/H$, the rotor flow"),
 ("\\emph{Step 5 (existence, and the mirror).} For $\\Lambda = 0$,",
  "\\emph{Step 5 (existence, and the mirror).} A pair of (iii) consists of null vectors of the plane of $e_{0}$ and $W$, whose form is $Q(ae_{0} + bW) = a^{2} - \\tfrac{\\Lambda}{3}b^{2}$ ($a, b \\in K$). For $\\Lambda \\neq 0$ a nonzero null vector has $b \\neq 0$ (else $a = 0$ too) and then $\\Lambda/3 = (a/b)^{2}$, so a pair exists over $K$ only when $\\Lambda/3$ is a nonzero square $H^{2}$ in $K$, and then (iii) gives one. For $\\Lambda = 7/3$ over $\\Q$, $\\Lambda/3 = 7/9$ is not a square ($7$ is not), so there is none although $\\Lambda > 0$ (the result synthesis.frozen-point-datum-is-h, clauses (ii)(b) and (iv)). For $\\Lambda = 0$,"),
 ("For $\\Lambda < 0$, $Q(W) = -\\Lambda/3 > 0$, so the plane of $e_{0}$ and $W$ is definite and has no null vector.",
  "For $\\Lambda < 0$ over an ordered $K$, $Q(W) = -\\Lambda/3 > 0$, so the plane of $e_{0}$ and $W$ is definite and has no null vector."),
])
print(bump(E,
 note="clause (v) restated over the base field K: a pair exists exactly when Lambda/3 is a nonzero square in K, Lambda = 3H^2 with H != 0 (over an ordered K this needs Lambda > 0, and Lambda = 7/3 over Q, Lambda > 0, has none), for Lambda < 0 over an ordered K the plane is definite; proof Step 5 proves the existence condition from Q(a e_0 + b W) = a^2 - (Lambda/3) b^2. Clause (iv) and the technical level write the endpoints as x = -+(2/H) e_0 (was -+sqrt(12/Lambda) e_0), the proof the worldline as |x_0| < 2/H; the one-liner reads kappa_Lambda = H. Clauses (i) to (iii) were already stated with Lambda = 3H^2, and the check already uses rational H, so it is unchanged. The existence condition is the theorem synthesis.frozen-point-datum-is-h (ii)(b), with the counterexample of its (iv).",
 defect="Clause (v) said a real pair exists exactly when Lambda > 0; over the series' rational scalars Lambda > 0 is not enough (Lambda = 7/3 gives none), the exact condition being that Lambda/3 is a nonzero square, Lambda = 3H^2, and clause (iv) and the one-liner wrote sqrt(12/Lambda) and sqrt(Lambda/3) for 2/H and H.",
 evidence="check.py::check_completed_pair"))
