---
id: sheaf.edge-wall
kind: claim
version: 4
title: The edge of the wall
status: proved
region: sheaf
subject: walls
tags: [kasner]
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
- obj.sheaf.variable-order-algebra-strict-diagonal-data
derivations:
- name: main
  uses:
  - sheaf.collision-census@2
  - sheaf.local-freeness-constant-rank@2
  - sheaf.variable-weight-boundary-tameness-completion-forced@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_positive_pair_collision_is_exchange_fixed_point
- kind: check
  ref: check.py::check_ordering_change_forces_taub_edge
- kind: check
  ref: check.py::check_dying_order_maximal_at_schwarzschild
- kind: check
  ref: check.py::check_edge_gram_nondegenerate_and_sheaf_rank
- kind: check
  ref: check.py::check_chamber_package_across_the_edge
- kind: check
  ref: check.py::check_no_module_crosses_the_edge
locators:
  paper: T04
  number: Thm 9.13
  label: thm:edge
  line: 1295
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the exchange identity p(1/u), the witness curve and its Taub crossing, the dying-order identity and series consistency, the Lorentzian edge Gram with Clifford rank 16, the v < 0 chamber package, and the failed gluing exponents. Version 3 -> 4.'
  env: theorem
  context_refs:
  - sheaf.local-freeness-constant-rank
  unresolved_refs:
  - rem:wallcomplex
  typing:
    by: ai-typing-pass
    removed:
    - sheaf.schwarzschild-degeneration-boundary-tame
    added:
    - sheaf.collision-census
    - sheaf.local-freeness-constant-rank
    note: 'The Schwarzschild boundary-tameness theorem enters only as a consistency check of the dying
      order, so it was removed; the collision census (the census the proof invokes by name) and local
      freeness at constant rank (cited with by for the constant rank sixteen) were added. Levels pass:
      lay and one-liner now keep the strict diagonal class.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - sheaf.collision-census
    - sheaf.local-freeness-constant-rank
---

## formal
Let the exponents of strict diagonal data vary smoothly on the constraint variety.
\begin{enumerate}
\item \emph{Positive-pair collisions are interior to the theory.} A collision $p_2 = p_3$ occurs only on the orbit of the Schwarzschild triple, Definition \claimref{obj.sheaf.variable-order-algebra-strict-diagonal-data} admits it, and Theorem \claimref{sheaf.variable-weight-boundary-tameness-completion-forced} holds across it verbatim. The rational identity $p(1/u) = (p_1, p_3, p_2)(u)$ of the classical parametrisation exhibits the collision as the fixed locus of the positive-pair exchange, fixed point $u = 1$.
\item \emph{Ordering changes force Taub edges.} If the negative exponent changes axis across a locus $Z \subset E$, then on $Z$ the triple is the Taub triple: by the census, the exponent crossing zero forces a second exponent to zero with it. On the witness curve $q(v) := \bigl(-v,\, v(1+v),\, 1+v\bigr)/(1+v+v^2)$, which lies on the variety identically in $v$, axis $1$ is the dying axis for $v > 0$, axis $2$ for $v < 0$, $q(0)$ is the Taub triple, and $q_1q_2 = -v^2(1+v)/(1+v+v^2)^2$: the two crossing exponents vanish jointly to second order at the edge.
\item \emph{The wall ends on the edge.} On each side of $Z$ (each \emph{chamber}) the forced weights and the entire package of Theorem \claimref{sheaf.variable-weight-boundary-tameness-completion-forced} hold with the chamber's own dying axis; the dying order $d = -2p_{\min}$ obeys the exact identity
\[
d(1) - d(u) \;=\; \frac{2(u-1)^2}{3(1+u+u^2)},
\]
so it is \emph{maximal}, $d = \tfrac23$, exactly at the Schwarzschild triple, and tends to zero at the edge. On $Z$ itself the weighted Gram is $\operatorname{diag}(1,-c_1,-c_2,-c_3)$: nondegenerate Lorentzian, corank zero. The radical line bundle has rank one on the chambers and rank zero on $Z$ (the degeneration sheaf itself keeps its constant rank sixteen, by Proposition \claimref{sheaf.local-freeness-constant-rank}; it is its ideal that vanishes): the wall ends on the edge, and no completion is needed there.
\item \emph{No module crosses the edge.} The two chamber modules coincide on $Z$, both weight assignments degenerating to $(0,0,0,1)$, but they are isomorphic over no neighbourhood of an edge point: the transition between them is diagonal with entries $\tau^{p_1}$ and $\tau^{-p_2}$, whose exponents are both negative on a chamber, so it is a unit over $\mathcal{A}$ on neither side. The forced weights jump as axis labels across $Z$; the invariant object is the wall complex of Remark \ref{rem:wallcomplex}.
\end{enumerate}

## technical
Let the exponents of strict diagonal Kasner data vary smoothly on the constraint variety. A collision $p_2 = p_3$ of the positive pair happens only on the orbit of the Schwarzschild triple, which the theory admits, and the variable-weight package holds across it. If the negative exponent changes axis across a locus $Z$, then on $Z$ the triple is the Taub triple $(0,0,1)$, because an exponent cannot cross zero alone. On each side of $Z$ (each chamber) the forced weights and the completion hold with that chamber's dying axis, and the dying order $d = -2p_{\min}$ satisfies $d(1) - d(u) = 2(u-1)^2 / (3(1+u+u^2))$, so it is maximal, $d = \tfrac23$, exactly at the Schwarzschild triple and tends to zero at the edge.

On $Z$ the weighted Gram is $\operatorname{diag}(1,-c_1,-c_2,-c_3)$, nondegenerate Lorentzian: the radical line has rank one on the chambers and rank zero on $Z$, so the wall ends there and needs no completion, while the degeneration sheaf keeps its constant rank. The two chamber modules coincide on $Z$ but are isomorphic over no neighbourhood of an edge point, since the transition between them has entries $\tau^{p_1}$ and $\tau^{-p_2}$, both with negative exponent on a chamber.

## lay
In an anisotropic singularity of the simplest, strictly diagonal kind, the rates at which different directions shrink can vary smoothly from place to place. Where two rates meet, either nothing special happens, or the wall of degeneration simply stops: on that edge the geometry is non-degenerate and needs no repair. On either side the repair works as before, but the two descriptions cannot be glued together across the edge.

## one-liner
For strict diagonal Kasner data with smoothly varying exponents, positive-pair collisions are harmless, while a change of dying axis happens only on a Taub edge where the wall ends, the weighted Gram is nondegenerate and the two chamber modules do not glue.
