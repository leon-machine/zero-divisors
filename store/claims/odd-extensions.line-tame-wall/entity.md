---
id: odd-extensions.line-tame-wall
kind: claim
version: 4
title: The $\Lambda$ line is a tame wall
status: proved
region: odd-extensions
subject: walls
tags: [cosmological-constant, degenerate-algebras, frozen-point]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14a, deposited version
review: typed
derivations:
- name: main
  uses:
  - odd-extensions.four-extensions-oriented-pair@5
  - odd-extensions.imported-tame-walls-exceptional-algebra-residue@4
  - odd-extensions.transport-constrains-frozen-point-only-through@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_gram_and_tameness
- kind: check
  ref: check.py::check_signatures_on_the_two_sides
- kind: check
  ref: check.py::check_symmetric_gauge_not_smooth
locators:
  paper: T14a
  number: Prop 10.2
  label: prop:tamewall
  line: 737
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the Gram diag(1,-1,-1,-1,-Lambda/3) in every gauge, corank one at Lambda = 0 with radical w_0, slope -1/3, the side signatures and the non-smooth symmetric gauge. Version 3 -> 4.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  env: proposition
  context_refs:
  - odd-extensions.imported-tame-walls-exceptional-algebra-residue
  - odd-extensions.transport-constrains-frozen-point-only-through
  typing:
    by: ai-typing-pass
    added:
    - odd-extensions.imported-tame-walls-exceptional-algebra-residue
    - odd-extensions.transport-constrains-frozen-point-only-through
    note: 'Added the imported tame-wall fact, whose conditions (T1) to (T3) are what the proposition verifies,
      and the theorem supplying the null-frame form of the frozen point with 2ab = Lambda/3 that the hypotheses
      rest on. Levels pass: the lay and one-liner now say tameness needs a smooth dilation gauge.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - odd-extensions.imported-tame-walls-exceptional-algebra-residue
    - odd-extensions.transport-constrains-frozen-point-only-through
---

## formal
Fix the dilation gauge by a smooth nowhere-vanishing $a(\Lambda)$ and write the frozen point in the canonical null frame as $I_{\Lambda} = a I_{0} + b\varphi$ with $2ab = \Lambda/3$ (Theorem \claimref{odd-extensions.transport-constrains-frozen-point-only-through}). Let $w_{\Lambda} = aI_{0} - b\varphi$, so that $I_{\Lambda}^{\perp}$ is spanned by the Lorentz frame and $w_{\Lambda}$. Then the family $(I_{\Lambda}^{\perp}, \text{induced form})$ over the $\Lambda$ line is a tame corank-one degeneration in the sense of Fact \claimref{odd-extensions.imported-tame-walls-exceptional-algebra-residue}:
\begin{enumerate}
\item[(i)] its Gram matrix in the frame $(e_{1}, \ldots, e_{4}, w_{\Lambda})$ is $\operatorname{diag}(1,-1,-1,-1,-\Lambda/3)$ for every $\Lambda$ and every gauge, so the degenerate locus is the point $\Lambda = 0$ (T1), the radical there is the line spanned by $I_{0}$ (T2), and the dying eigenvalue $-\Lambda/3$ crosses zero with nonzero speed (T3), $\delta(w_{0} \otimes w_{0}) = -\tfrac13\,d\Lambda$ in the parametrisation by $\Lambda$, the $3$ being that of $Q(I) = \Lambda/3$;
\item[(ii)] the signatures on the two sides are $(2,3)$ for $\Lambda < 0$ and $(1,4)$ for $\Lambda > 0$: the wall separates the anti-de Sitter and de Sitter intermediate algebras, and crossing it changes the sign of one direction's square, which is the sheaf paper's signature-change wall in a parameter rather than in spacetime;
\item[(iii)] the gauge $a = b$, which makes $I_{\Lambda}$ proportional to $I_{0} + \varphi$, is not smooth at the wall and is not defined for $\Lambda < 0$; the tame structure needs a smooth gauge, and the scalar invariants (the dying eigenvalue, its crossing speed, the signatures) do not depend on which, while the identification of the radical vector with $I_{0}$ at a fixed normalisation does, $w_{0} = a(0)\,I_{0}$.
\end{enumerate}

## technical
Fix a smooth nowhere-vanishing gauge $a(\Lambda)$ and write the frozen point as $I_\Lambda = aI_0 + b\varphi$ with $2ab = \Lambda/3$; set $w_\Lambda = aI_0 - b\varphi$. Then $I_\Lambda^\perp$ with its induced form is a tame corank-one family over the $\Lambda$ line. In the frame $(e_1, \dots, e_4, w_\Lambda)$ its Gram is $\operatorname{diag}(1,-1,-1,-1,-\Lambda/3)$ for every $\Lambda$ and every gauge, so the degenerate locus is the point $\Lambda = 0$, the radical there is spanned by $I_0$, and the dying eigenvalue $-\Lambda/3$ crosses zero at speed $-\tfrac13$.

The signatures are $(2,3)$ for $\Lambda < 0$ and $(1,4)$ for $\Lambda > 0$, so the wall separates the anti-de Sitter and de Sitter intermediate algebras: a signature-change wall in a parameter rather than in spacetime. The gauge $a = b$ is not smooth at the wall and not defined for $\Lambda < 0$; the scalar invariants do not depend on which smooth gauge is used, but the identification $w_0 = a(0)\,I_0$ does.

## lay
If the cosmological constant is treated as a dial, the algebra of directions orthogonal to the frozen point degenerates exactly when the dial reads zero. This result checks that, once the leftover scale freedom is fixed smoothly, the degeneration is of the mildest, well-behaved kind. On the negative side the algebra is the anti-de Sitter one and on the positive side the de Sitter one, so passing through zero flips the sign of one direction, as a signature-changing wall does in spacetime.

## one-liner
Over the $\Lambda$ line the complement $I_\Lambda^\perp$ of the frozen point has Gram $\operatorname{diag}(1,-1,-1,-1,-\Lambda/3)$ and, in any smooth dilation gauge, is a tame corank-one wall at $\Lambda = 0$ separating signatures $(2,3)$ and $(1,4)$.
