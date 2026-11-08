import sys; sys.path.insert(0, "/home/claude/phys-graph/colony/runs/2026-11-08-frozen-point-datum/work/T1")
from rt import start, bump, edit, h_block, LAB
E = "odd-extensions.two-towers-one-curved-universe"
start(E)
edit(E, "entity.md", [
 ("and its frozen point has norm $-Q(I)$. Then:\n\\begin{enumerate}",
  "and its frozen point has norm $-Q(I)$. Let $\\Lambda = 3H^{2}$ in a de Sitter universe and $\\Lambda = -3H'^{2}$ in an anti-de Sitter one, with $H, H' > 0$ in the base field, which is ordered (it is enough that $-1$ is not a square in it), and let $e_{5}$ be the unit vector $HV$ (de Sitter) or $H'V$ (anti-de Sitter) along the Stelle-West vector $V$, $Q(V) = -3/\\Lambda$, so that $Q(e_{5}) = -1$ or $+1$. Then:\n\\begin{enumerate}"),
 ("and that element is the unit vector along $V$, which Proposition",
  "and that element is the unit vector $HV$ (respectively $H'V$) along $V$, which Proposition"),
 ("and its frozen point has norm $-Q(I)$. In de Sitter the intermediate algebras",
  "and its frozen point has norm $-Q(I)$. With $\\Lambda = 3H^{2}$ (de Sitter) or $\\Lambda = -3H'^{2}$ (anti-de Sitter), in de Sitter the intermediate algebras"),
 ("That generator is the unit vector along $V$, outside",
  "That generator is the unit vector $HV$ (respectively $H'V$) along $V$, outside"),
])
edit(E, "proof-main.tex", [
 ("the doubling or complexification is Corollary \\claimref{odd-extensions.four-extensions-oriented-pair}.",
  "the doubling or complexification is Corollary \\claimref{odd-extensions.four-extensions-oriented-pair}. That corollary is about the standard forms, and $I^{\\perp}$ is one over the base field because of the datum: $W = V/Q(V)$ is parallel to $V$ with $Q(W) = -\\Lambda/3$, so with $\\Lambda = 3H^{2}$ the vectors $e_{0}, \\dots, e_{3}$ and $e_{5} = HV$ ($Q(e_{5}) = -H^{2}\\cdot 3/\\Lambda = -1$) are an orthonormal basis of $I^{\\perp}$ of squares $(1,-1,-1,-1,-1)$, and with $\\Lambda = -3H'^{2}$ so are $e_{0}, \\dots, e_{3}, H'V$ with squares $(1,-1,-1,-1,1)$; with only $\\Lambda$ given, the volume element on $e_{0}, \\dots, e_{3}, W$ squares to $\\Lambda/3$, and over $\\Q$ with $\\Lambda/3$ not a square (for instance $\\Lambda = 6$) the centre is a quadratic field of discriminant neither $\\pm 4$ nor a square, so neither reading holds (the result synthesis.frozen-point-datum-is-h, clauses (ii)(i), (ii)(j), (iv) and (v)(e)). The complexified readings need $-1$ not a square in the base field (its clause (v)(c)), which holds over an ordered field."),
 ("The script verifies the signatures of the mirror's $I^{\\perp}$ on the same rational instances,",
  "The script verifies, with $\\Lambda = 3H^{2}$ and $\\Lambda = -3H'^{2}$ at rational $H, H'$, the unit $e_{5}$, the orthonormal basis of $I^{\\perp}$ and the squares of its volume element in both forms, and at $\\Lambda = 6$ and $7/3$ that this square is $\\Lambda/3$, not a rational square; it also verifies the signatures of the mirror's $I^{\\perp}$ on the same rational instances,"),
])
p = f"{LAB}/proposals/{E}/check.py"
t = open(p).read()
t = t.replace('''The consequence (no derived quantity uses e5) rests on the cited propositions and is not recomputed.
"""''', '''The consequence (no derived quantity uses e5) rests on the cited propositions and is not recomputed.
(iv) The datum: with Lambda = 3H^2 (de Sitter) and Lambda = -3H'^2 (anti-de Sitter), e5 = W/H (W/H') is a unit vector of
    I-perp and the volume element on e0..e3, e5 squares to +1 (-1), in the mirror to -1 (+1); at Lambda = 6 and 7/3
    the volume element on e0..e3, W squares to Lambda/3, not a rational square.
"""''', 1)
assert "(iv) The datum" in t
t = t.rstrip("\n") + "\n" + h_block("check_the_datum_makes_the_fifth_generator_a_unit",
      ["odd-extensions.imported-frozen-point", "odd-extensions.doubling-or-complexification"])
open(p, "w").write(t)
print(bump(E,
 note="the hypothesis made explicit: Lambda = 3H^2 (de Sitter) or Lambda = -3H'^2 (anti-de Sitter) with H, H' > 0 in an ordered base field (or one where -1 is not a square), and e5 defined as the unit vector HV (resp. H'V) along the Stelle-West vector V, Q(V) = -3/Lambda; the closing sentence and the technical level name that unit. The proof says why I-perp is the standard form over the base field (the orthonormal basis e0..e3, HV) and that with only Lambda given the centre is the field of omega^2 = Lambda/3 (over Q at Lambda = 6 neither doubled nor Cl(4,1)'s), citing synthesis.frozen-point-datum-is-h (ii)(i), (ii)(j), (iv), (v)(c), (v)(e). Check: new function check_the_datum_makes_the_fifth_generator_a_unit (the conformal-model frozen point at Lambda = 3H^2, -3H'^2 for rational H, H', and the failure at Lambda = 6, 7/3); the earlier functions unchanged (their sample frozen points have |Q(I)| = 4, a square). Clauses (i) to (iii) otherwise unchanged.",
 defect="The statement took the de Sitter and anti-de Sitter types Cl(1,4), Cl(4,1), Cl(2,3), Cl(3,2) and the unit fifth generator V/|V| from the sign of Lambda alone; over the series' rational scalars they need Lambda/3 (resp. -Lambda/3) to be a square, so the datum is now H with Lambda = 3H^2 (H' with Lambda = -3H'^2) and e5 = HV (H'V).",
 evidence="check.py::check_the_datum_makes_the_fifth_generator_a_unit"))
