---
id: sheaf.exceptional-algebra-deformation-normal-cone
kind: claim
version: 5
title: 'The exceptional algebra: deformation to the normal cone'
status: proved
region: sheaf
subject: walls
tags: [degenerate-algebras, limits]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T04, deposited version
review: typed
derivations:
- name: main
  uses:
  - sheaf.blade-basis-degenerate-forms-included@5
  - sheaf.degeneration-sheaf@6
  assumes:
  - sheaf.tameness@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T04.py
  tags:
  - num:6.1
- kind: check
  ref: check.py::check_rescaled_limit_and_signature
- kind: check
  ref: check.py::check_special_fibre_is_the_limit_algebra
- kind: check
  ref: check.py::check_limit_independent_of_choices
locators:
  paper: T04
  number: Prop 6.1
  label: prop:exceptional
  line: 750
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: rescaled Gram polynomial in sqrt(t) with limit G0|V1 + Gdot(k,k) of signature (p,q) for all p+q <= 4, the limit Clifford algebra, and independence of complement, k-scale and t-scale. Version 3 -> 4. Check strengthened: the special-fibre comparison at s = 0 is made unconditional (it ran only if 0 was in the sample list); sample inputs moved to module level. Version 4 -> 5.'
  env: proposition
  unresolved_refs:
  - rem:coords
  typing:
    by: ai-typing-pass
    added:
    - sheaf.tameness
    note: 'Both edges are real premises (the signature of the complement block and the polynomial structure
      constants); the statement invokes the transversality condition of tameness, so the tameness postulate
      was added to assumes. Levels pass: all three levels now state the tameness premise (its transversality
      condition (T3)), which the lay and one-liner had dropped.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - sheaf.tameness
---

## formal
Fix $x \in \Sig$ and a transversal curve through $x$ with parameter $t$, so that $G(t) = G_0 + t\dot G + O(t^2)$ with radical of $G_0$ spanned by $k$ and $\dot G(k,k) \neq 0$ by (T3). Rescale anisotropically: fix a complement $V_1$ of the radical and send $k \mapsto k/\sqrt{t}$. Then the rescaled forms converge as $t \to 0^+$ to the nondegenerate form $\hat G := G_0|_{V_1} \perp \dot G(k,k)$ on $V_1 \oplus \R k$: the cross terms are suppressed by $\sqrt{t}$, and the dying direction re-enters with its rate of degeneration as its metric coefficient. On the physical side the limit has signature $(p, q)$. The rescaled Clifford family is therefore a continuous family of nondegenerate algebras through $t = 0$, and its special fibre $\shE(x) := \Cl(V_1 \oplus \R k, \hat G)$, the \emph{exceptional algebra} at $x$, is independent of the choice of complement and of the scales of $k$ and $t$ up to canonical isomorphism.

## technical
At a wall point $x$, take a transversal curve with $G(t) = G_0 + t\dot G + O(t^2)$, the radical of $G_0$ spanned by $k$ and $\dot G(k,k) \neq 0$ by the transversality condition (T3) of the tameness premise. Fix a complement $V_1$ of the radical and rescale $k \mapsto k/\sqrt{t}$. As $t \to 0^+$ the rescaled forms converge to the nondegenerate form $\hat G = G_0|_{V_1} \perp \dot G(k,k)$: the cross terms are $O(\sqrt t)$, and the dying direction returns with its rate of degeneration as its coefficient. On the physical side $\hat G$ has signature $(p,q)$.

So the rescaled Clifford algebras form a continuous family of nondegenerate algebras through $t = 0$, whose special fibre is the exceptional algebra $\shE(x) = \Cl(V_1 \oplus \R k, \hat G)$. Up to canonical isomorphism it does not depend on the complement, on the scale of $k$ or on the scale of $t$.

## lay
Assume the wall is tame, so that at the wall one direction of the geometry loses its length at a nonzero rate. If that direction is stretched at exactly the right rate as the wall is approached, the geometry has a well-behaved, non-degenerate limit. The algebra of this limit, the exceptional algebra, depends only on the wall point and not on the choices made to build it.

## one-liner
Under tameness, rescaling the dying direction by $1/\sqrt{t}$ along a transversal gives the nondegenerate limit form $G_0|_{V_1} \perp \dot G(k,k)$, of signature $(p,q)$ on the physical side, whose Clifford algebra is canonically independent of the choices.
