---
id: conformal.minimal-nondegenerate-completion
kind: claim
version: 6
title: Minimal nondegenerate completion
status: proved
region: conformal
subject: completion
tags: [degenerate-algebras, hyperbolic-plane, forcing-and-uniqueness]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T02, deposited version
review: typed
derivations:
- name: main
  uses:
  - conformal.blade-basis-persists-under-degeneracy@4
  - conformal.witt-extension-theorem@1
  - std-algebra.functoriality@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T02.py
  tags:
  - num:2.3
- kind: check
  ref: check.py::check_no_completion_below_m_plus_r
- kind: check
  ref: check.py::check_minimal_completions_signature
- kind: check
  ref: check.py::check_minimal_completion_unique_fixing_w
- kind: check
  ref: check.py::check_embedding_into_cl_p_plus_r_q_plus_r
locators:
  paper: T02
  number: Thm 2.3
  label: thm:main
  line: 155
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.functoriality where the proof uses them. Version 5 -> 6.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the lower bound m + r by rank for 30 radical cases (diagonal and non-diagonal Grams), signature (p+r, q+r) of every sampled minimal completion, the explicit normalisation fixing W to the model, and the embedding Cl(p,q,r) -> Cl(p+r,q+r). Version 3 -> 4. Check strengthened: sample inputs moved to module level and the values the mutation test could not see pinned. Version 4 -> 5.'
  env: theorem
  typing:
    by: ai-typing-pass
    added: [conformal.blade-basis-persists-under-degeneracy]
    note: "Witt extension kept (uniqueness step); added the blade-basis fact because the stated embedding of the degenerate algebra into the completed one rests on the Setup argument that uses it, which the paper lists as one of the two imports of its proofs."
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - conformal.blade-basis-persists-under-degeneracy
    note: "Silent use: the blade basis is what makes the map of Clifford algebras induced by a completion injective, which the statement's embedding needs."
about:
- obj.std-algebra.hyperbolic-plane
---

## formal
Let $(W,B)$ be as in the Setup: radical of dimension $r \geq 1$, nondegenerate part of signature $(p,q)$, $m = \dim W = p + q + r$. Then $(W,B)$ admits a completion, and:
\begin{enumerate}
\item every completion satisfies $\dim \widetilde W \geq m + r$;
\item completions of dimension exactly $m + r$ exist, and every such has signature $(p{+}r,\, q{+}r)$;
\item any two minimal completions are isometric by an isometry fixing $W$ pointwise.
\end{enumerate}
Consequently $\Cl(p,q,r)$ embeds in $\Cl(p{+}r, q{+}r)$, minimally so among the embeddings induced by completions (no completion of dimension below $m + r$ exists), and the minimal ambient algebra is unique up to an isomorphism fixing the image of $\Cl(p,q,r)$.

## technical
Let $(W,B)$ be a real quadratic space with radical $R$ of dimension $r \geq 1$ and nondegenerate part of signature $(p,q)$, so $m = \dim W = p+q+r$. A completion is a nondegenerate quadratic space $(\widetilde W, Q)$ containing $W$ with $Q|_W = B$. Every completion has $\dim \widetilde W \geq m + r$, because the pairing $\rho \mapsto Q(\rho,\cdot) \bmod W$ embeds $R$ in $(\widetilde W/W)^*$. The bound is attained by $W \oplus R^*$ with each radical vector paired to its dual, and every completion of dimension $m+r$ has signature $(p+r,q+r)$: the orthocomplement of the nondegenerate part is a sum of $r$ hyperbolic planes.

Any two minimal completions are isometric by an isometry fixing $W$ pointwise, by the Witt extension theorem. Hence $\Cl(p,q,r) \hookrightarrow \Cl(p+r,q+r)$, minimal among the embeddings induced by completions, with the ambient algebra unique up to an isomorphism fixing the image of $\Cl(p,q,r)$.

## lay
A geometric algebra built on a degenerate metric has directions that pair to zero with everything, and division fails along them. This result says how to enlarge the space so that the metric becomes nondegenerate: each degenerate direction needs exactly one new partner direction, and the enlarged metric gains one positive and one negative direction for each degenerate one. The smallest such enlargement is unique up to a symmetry that leaves the original space untouched. Minimality here is among enlargements of the underlying space, not among all algebras.

## one-liner
A real quadratic space with radical of dimension $r$ and nondegenerate part of signature $(p,q)$ has minimal nondegenerate completions of exactly $r$ extra dimensions, all of signature $(p+r,q+r)$ and unique up to an isometry fixing the space, so $\Cl(p,q,r)$ embeds in $\Cl(p+r,q+r)$, minimally among completion-induced embeddings.
