---
id: sheaf.invariant-form-t3
kind: claim
version: 2
title: The invariant form of (T3)
status: proved
region: sheaf
subject: walls
tags: [tameness]
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
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_radical_and_tangential_vanishing
- kind: check
  ref: check.py::check_independent_of_extension
- kind: check
  ref: check.py::check_scales_by_c_squared
locators:
  paper: T04
  number: Lem 2.2
  label: lem:invariantT2
  line: 383
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: in a polynomial model, d g_k on the wall kills tangent vectors, is the same for five extensions of k, and scales by c^2 under k -> c k. Version 1 -> 2.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: 'No edges: the lemma assumes only the first two tameness conditions, while the tameness postulate
      as a whole defines its third condition through this lemma, so the postulate was deliberately not
      added to assumes. Levels pass: the lay level now states the hypotheses (T1) and (T2), a smooth wall
      with a smooth corank-one radical line, which it had dropped.'
---

## formal
Assume (T1) and (T2). Extend a local spanning section $k$ of $\shL$ to a covector field on a neighbourhood of $\Sig$ in $M$, and let $g_k := G(k,k)$, a smooth function vanishing on $\Sig$. Then:
\begin{enumerate}
\item $dg_k|_\Sig$ annihilates $T\Sig$, hence is a section of the conormal bundle $N^*\Sig$;
\item $dg_k|_\Sig$ is independent of the chosen extension of $k$;
\item under $k \mapsto ck$ ($c$ a nonvanishing function), $dg_k|_\Sig$ scales by $c^2|_\Sig$.
\end{enumerate}
Consequently the assignment $k \otimes k \mapsto dg_k|_\Sig$ is a well-defined bundle map
\[
\delta \;:\; \shL \otimes \shL \;\longrightarrow\; N^*\Sig
\]
over $\Sig$, canonically attached to the degeneration. Both sides are line bundles, so $\delta$ is nowhere zero if and only if it is an isomorphism $\shL^{\otimes 2} \cong N^*\Sig$; hypothesis (T3) is exactly the demand that the degeneration itself identify the square of the dying line with the conormal line.

## technical
Assume the wall $\Sig$ is a smooth closed hypersurface and the radical lines of $G$ along it form a smooth line bundle $\shL$ of corank one. Extend a local spanning section $k$ of $\shL$ off $\Sig$ and set $g_k = G(k,k)$, which vanishes on $\Sig$. Then $dg_k|_\Sig$ annihilates $T\Sig$, so it is a section of the conormal bundle; it does not depend on the extension of $k$; and under $k \mapsto ck$ it scales by $c^2|_\Sig$.

Hence $k \otimes k \mapsto dg_k|_\Sig$ is a well-defined bundle map $\delta : \shL \otimes \shL \to N^*\Sig$, canonically attached to the degeneration. Both sides are line bundles, so $\delta$ is nowhere zero exactly when it is an isomorphism $\shL^{\otimes 2} \cong N^*\Sig$, and the transversality condition of tameness is precisely this demand.

## lay
Suppose a geometry degenerates along a smooth wall, losing exactly one direction there in a smooth way (the first two tameness conditions). That direction loses its length as one crosses the wall, and how fast it does so can be measured without arbitrary choices, giving a canonical quantity on the wall. Asking that this quantity never vanish, so that the degeneration is first order, is the same as asking that the square of the dying direction match the direction across the wall.

## one-liner
Given a smooth wall with a smooth corank-one radical line, the differential of $G(k,k)$ along the wall defines a canonical bundle map $\delta : \shL^{\otimes 2} \to N^*\Sig$, and transversality is exactly the demand that it be an isomorphism.
