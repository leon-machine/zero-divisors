---
id: conformal.principal-case
kind: claim
version: 3
title: The principal case
status: proved
region: conformal
subject: completion
tags: [degenerate-algebras, conformal-model, forcing-and-uniqueness]
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
  - conformal.minimal-nondegenerate-completion@6
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_minimal_completion_is_cga
- kind: check
  ref: check.py::check_completion_unique_fixing_v
- kind: check
  ref: check.py::check_pga_embeds_in_cga
locators:
  paper: T02
  number: Cor 3.1
  label: cor:pga
  line: 217
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: about the core definitions it is stated in. Version 2 -> 3.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: every nondegenerate one-vector completion of R^(n,0,1) has signature (n+1,1), uniqueness fixing V, and the embedding of Cl(n,0,1) in Cl(n+1,1). Version 1 -> 2.'
  env: corollary
  typing:
    by: ai-typing-pass
    note: "Single premise is the minimal completion theorem specialised to one null generator; the paper presents the PGA to CGA identification as new, so no standard route."
about:
- obj.std-algebra.projective-algebra
- obj.std-algebra.conformal-algebra
---

## formal
$\mathrm{PGA} = \Cl(3,0,1)$ has minimal nondegenerate completion $\Cl(4,1) = \mathrm{CGA}$, uniquely: the engineering community's two standard algebras are a degenerate algebra and its unique minimal completion. Likewise in the plane, $\Cl(2,0,1)$ completes minimally to $\Cl(3,1)$; and in general the $n$-dimensional Euclidean PGA $\Cl(n,0,1)$ completes minimally to the $n$-dimensional CGA $\Cl(n{+}1,1)$.

## technical
Apply the minimal completion theorem with $(p,q,r) = (n,0,1)$. The Euclidean projective algebra $\Cl(n,0,1)$, with one null generator, has a minimal nondegenerate completion of dimension $n+2$ and signature $(n+1,1)$, unique up to an isometry fixing the original space, so $\Cl(n,0,1) \hookrightarrow \Cl(n+1,1)$, the $n$-dimensional conformal algebra.

For $n = 3$ this says that $\mathrm{PGA} = \Cl(3,0,1)$ completes minimally and uniquely to $\mathrm{CGA} = \Cl(4,1)$, and for $n = 2$ that $\Cl(2,0,1)$ completes to $\Cl(3,1)$.

## lay
Engineers and graphics programmers use two geometric algebras: projective geometric algebra, which has one degenerate direction standing for the plane at infinity, and conformal geometric algebra, which has two extra directions. They are usually treated as separate design choices. This result shows that the conformal algebra is the unique smallest nondegenerate enlargement of the projective one, in any number of dimensions, in the sense of enlarging the underlying space.

## one-liner
The $n$-dimensional Euclidean projective geometric algebra $\Cl(n,0,1)$ has the $n$-dimensional conformal geometric algebra $\Cl(n+1,1)$ as its unique minimal nondegenerate completion; in particular PGA completes uniquely to CGA.
