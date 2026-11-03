---
id: sheaf.wall-gram
kind: claim
version: 3
title: The wall Gram
status: proved
region: sheaf
subject: walls
tags: [hyperbolic-plane, degenerate-algebras]
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
about:
- obj.sheaf.collar-data-coupling
derivations:
- name: main
  uses:
  - sheaf.degeneration-sheaf@6
  - std-algebra.sylvester-inertia@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T04.py
  tags:
  - num:4.2
- kind: check
  ref: check.py::check_block_gram_and_determinant
- kind: check
  ref: check.py::check_hyperbolic_plane_and_orthocomplement
- kind: check
  ref: check.py::check_orthogonal_splitting_and_wall_signature
locators:
  paper: T04
  number: Lem 4.2
  label: lem:wallgram
  line: 562
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.sylvester-inertia where the proof uses them. Version 2 -> 3.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: block Gram and determinant -2 mu nu, hyperbolic plane and w, orthogonal splitting and wall signatures (p+1,q+1) or (p,q+2) for all p+q <= 6. Version 1 -> 2.'
  env: lemma
  unresolved_refs:
  - rem:coords
  typing:
    by: ai-typing-pass
    note: 'kept the edge to the degeneration sheaf, which supplies the signature (p-1,q) of the induced
      form; added about: obj.sheaf.collar-data-coupling since the block entries are the collar coupling.
      Levels pass: conditions already kept.'
---

## formal
At a point of $\Sig$ (where $\beta = 1$, $\lambda = 0$, and $k$ spans the radical), let $V_1 := \{\alpha \in T^*M : \alpha(u) = 0\}$. Then $T = V_1 \oplus \operatorname{span}\{k, \nO, \nInf\}$, the two summands are $h$-orthogonal, and:
\begin{enumerate}
\item $h|_{V_1} = G|_{V_1}$ is nondegenerate of signature $(p{-}1, q)$ (physical-side convention of Remark \ref{rem:coords});
\item the Gram matrix of $(k, \nO, \nInf)$ is
\[
\begin{pmatrix} 0 & \nu & \mu \\ \nu & 0 & -1 \\ \mu & -1 & 0 \end{pmatrix},
\qquad \det = -2\mu\nu \neq 0 ,
\]
so the block is nondegenerate for every nonzero $\mu, \nu$;
\item inside the block, $\operatorname{span}\{k, \nO\}$ is a hyperbolic plane, and its $h$-orthocomplement in the block is spanned by $w = k + \nu\,\nInf - \mu\,\nO$ with $h(w,w) = 2\mu\nu$. Hence the block has signature $(2,1)$ if $\mu\nu > 0$ and $(1,2)$ if $\mu\nu < 0$;
\item consequently $h|_\Sig$ is nondegenerate of signature $(p{+}1, q{+}1)$ if $\mu\nu > 0$, and $(p, q{+}2)$ if $\mu\nu < 0$.
\end{enumerate}

## technical
At a point of $\Sig$, where $\beta = 1$, $\lambda = 0$ and $k$ spans the radical, set $V_1 = \{\alpha \in T^*M : \alpha(u) = 0\}$. Then $T = V_1 \oplus \operatorname{span}\{k, \nO, \nInf\}$ is an $h$-orthogonal splitting, and $h|_{V_1} = G|_{V_1}$ is nondegenerate of signature $(p{-}1, q)$. The block $(k, \nO, \nInf)$ has Gram matrix $\begin{pmatrix} 0 & \nu & \mu \\ \nu & 0 & -1 \\ \mu & -1 & 0 \end{pmatrix}$ with determinant $-2\mu\nu \neq 0$.

Inside the block, $\operatorname{span}\{k, \nO\}$ is a hyperbolic plane whose orthocomplement is spanned by $w = k + \nu\,\nInf - \mu\,\nO$ with $Q(w) = h(w,w) = 2\mu\nu$, so the block has signature $(2,1)$ if $\mu\nu > 0$ and $(1,2)$ if $\mu\nu < 0$. Hence $h|_\Sig$ is nondegenerate of signature $(p{+}1, q{+}1)$ if $\mu\nu > 0$ and $(p, q{+}2)$ if $\mu\nu < 0$.

## lay
On the wall, the enlarged geometry splits into two independent pieces: the ordinary directions that survive the degeneration, and a three-dimensional block made of the dying direction and the two added ones. A direct calculation shows that this block is never degenerate, whatever non-zero coupling strengths are used. The sign of the product of the two coupling constants decides how many directions of each sign the repaired geometry has.

## one-liner
On the wall the ambient form splits orthogonally into the surviving directions and a nondegenerate three-dimensional coupled block, giving signature $(p{+}1, q{+}1)$ when $\mu\nu > 0$ and $(p, q{+}2)$ when $\mu\nu < 0$.
