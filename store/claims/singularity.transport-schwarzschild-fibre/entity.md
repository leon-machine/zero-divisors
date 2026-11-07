---
id: singularity.transport-schwarzschild-fibre
kind: claim
version: 9
title: The transport, on the Schwarzschild fibre
status: proved
region: singularity
subject: completion
tags: [schwarzschild, transport-algorithm, null-directions]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
- name: Claude Opus 5.5
  role: 'GA rewrite (declared outside_ga)'
  version: 9
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'GTG proof: lift and reflection in e+ in Cl(2,4), dual norm as Q(hb^T(xi)) from the gauge field; exact check'
  version: 9
  source: maintainer pass 2026-11-07 (GTG proofs)
review: typed
about:
- obj.singularity.fibrewise-conformal-lift
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - sheaf.one-sided-completion-singularity@4
  - sheaf.schwarzschild-degeneration-boundary-tame@6
  - singularity.cones-fold@4
  - singularity.degeneration-exactly@2
  - transport.descent-read-out-map@2
  - transport.swap-rescale-normal-form@4
  - transport.totality@3
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:5.2
- kind: check
  ref: check.py::check_static_fibre_lift_incidence_involution
- kind: check
  ref: check.py::check_invertible_directions_return_reciprocal
- kind: check
  ref: check.py::check_null_directions_go_ideal
- kind: check
  ref: check.py::check_dying_direction_dual_norm_and_read_out
- kind: check
  ref: check.py::check_gtg_dual_norm_of_the_dying_direction_from_the_engine
locators:
  paper: T05
  number: Prop 5.2
  label: prop:lift
  line: 1535
extraction:
  maintainer_pass_gtg_proof:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Proof rewritten in GTG and the conformal model: (1) X_p(x) = n0 + hb^{-1}(x) + Q_p(x) ninf/2 is null, iota is the reflection N -> e+ N e+ = -(2t n0 + X + (s/2) ninf), a versor (quadric preserved, involution); (2), (3) read-out X/s; (4) the one-forms read as background gradients (dr = -e_r, dt_PG = e_t), hb^T(a) = a - beta (a . e_r) e_t gives hb^T(xi) = -sqrt(r) e_r and Q*(xi) = -r at every radius, the static labels giving the same value through hb^T(grad t_s) = gamma^0/sqrt f, hb^T(grad r) = sqrt f gamma^1; cometric and Gram components kept as a labelled reading. Checked exactly: the existing GA checks for (1) to (4) and the new check_gtg_dual_norm_of_the_dying_direction_from_the_engine (hb^T from the shared engine''s PG and static gauge fields: hb^T(xi) = -sqrt(r) e_r, Q* = -r at 3 masses x 4 radii, inside, on and outside the horizon; Q*(grad t_s) = 1/f; read-out -hb^T(xi)/r). Version kept at 9 (already above the lock in this run). outside_ga narrowed to the definition of xi in the imported weighted coframe.'
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Declared outside_ga (other) and left in its language: Clause (4) and the proof work with the weighted Painleve-Gullstrand coframe and the cometric components ((g_p^{-1})^{tt} = 1/f, (g_p^{-1})^{rr} = -f) of the sheaf construction, whose GTG reading Q*_p(k) = Q(hb^T(k)) is stated; the weighted coframe is a construction on the degenerate cometric, outside the invertible region (reader R11).'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the static-gauge Gram of Q_p, incidence and involution of iota = e+ . e+, the classical reciprocal off the cone, ideal points on the radial null direction, and Q*(k) = -r from hb^T in PG and static gauges with the read-out failing only at r = 0. Version 5 -> 6. The formal level restated: convention made explicit (coverage judge C12): the values in (2) to (4) hold after identifying a background vector x with its physical vector hb^{-1}(x) and a covector xi with hb^T(xi); the identification sentence is added before (1), no change of claim. Version 6 -> 7. The technical level restated: convention made explicit (coverage judge C12): lift written with hb^{-1}(x), read-out values written as hb^{-1}(x)/Q_p(x), [hb^{-1}(x) + n_inf/2] and -hb^T(xi)/r. Check strengthened: iota slots pinned as s = -Q_p(x), t = -1/2; sample x moved to module level. Version 7 -> 8.'
  env: proposition
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
  typing:
    by: ai-typing-pass
    removed:
    - transport.transport-algorithm
    added:
    - transport.swap-rescale-normal-form
    - obj.singularity.fibrewise-conformal-lift
    note: 'Removed the mechanically added transport-algorithm edge (the paper says this executes Step
      4 of the algorithm, but the proof uses totality, descent and the coordinate form of the reciprocal,
      not the algorithm), added the swap-and-rescale normal form that supplies the formula for iota, and
      kept cones-fold and degeneration-exactly with some doubt, since they enter only through the identification
      of xi with the dying direction. Levels pass: conditions already kept.'
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    cited:
    - transport.swap-rescale-normal-form
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement: the point p lies in the invertible region of the Schwarzschild gravitational field (hb, Omega) on flat spacetime, the fibre is the background vectors at p, Q_p(x) = Q(hb^{-1}(x)) is the square of the physical vector over x (whose Gram in the static gauge is the derived metric g_p), and the dual norm is Q^*_p(xi) = Q(hb^T(xi)), the derived cometric. Clauses (1)-(4) unchanged. Proof: one opening sentence pointing to the GTG dictionary Fact.'
outside_ga:
  kind: other
  why: 'Clause (4) names the generator xi by its one-form in the weighted Painleve-Gullstrand coframe of the imported sheaf theorem (T4 Thm 8.7), a construction on the degenerate cometric at E outside the invertible region; the computation itself is in GA (xi a background gradient with physical covector hb^T(xi) = -sqrt(r) e_r).'
---

## formal
Fix $p$ in the invertible region of the Schwarzschild gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), take $T_pM$ to be the background vectors at $p$, and write $Q_p(x) := Q(\hb^{-1}(x))$ for the square of the physical vector over $x$ and $Q^*_p(\xi) := Q(\hb^{T}(\xi))$ for the dual norm of a covector. Vectors and covectors are read in the physical space: the gauge field carries the flat background to the physical vectors, a vector $x$ to $\hb^{-1}(x)$ and a covector $\xi$ to $\hb^{T}(\xi)$, the lift $X_p(x)$ carries $\hb^{-1}(x)$ in its vector slot, and the values in (2) to (4) are taken through this identification ($x/Q_p(x)$ is the physical vector $\hb^{-1}(x)/Q_p(x)$, $x + \tfrac12 \nInf$ is $\hb^{-1}(x) + \tfrac12 \nInf$, and $\xi/r$ is $\hb^{T}(\xi)/r$). In the static gauge the Gram of $Q_p$ is the derived metric $g_p = \operatorname{diag}(f, -f^{-1}, -r^2, -r^2\sin^2\theta)$ with $f = 1 - 2M/r$. Then:
\begin{enumerate}
\item[(1)] $X_p(x)$ satisfies the incidence condition for every $x \in T_pM$, and $\iota$ preserves it and is an involution.
\item[(2)] \emph{(Invertible directions: the transport returns to the original space.)} If $Q_p(x) \neq 0$ then $\dsc\bigl(\iota(X_p(x))\bigr) = x/Q_p(x)$, the classical reciprocal.
\item[(3)] \emph{(Null directions: the transport does not return.)} If $Q_p(x) = 0$, that is if $x$ is physically null, in particular for the radial null direction $x = \et + f\,\er$, then $\iota(X_p(x)) = [\,x + \tfrac12 \nInf\,]$, an ideal point, and $\dsc$ is undefined on it.
\item[(4)] \emph{(The dying direction, and where the descent fails.)} Let $\xi := k = \sqrt r\,dr + \sqrt{2M}\,dt_{\mathrm{PG}}$ be the generator of the radical line of the degeneration in the weighted Painlev\'e-Gullstrand coframe of \cite[Thm.~8.7]{ButlerT4}, in the static chart $\xi = \sqrt{2M}\,dt_s + (\sqrt r/f)\,dr$. Its dual norm is $Q^*_p(\xi) = -r$ exactly, at every radius, the horizon included: nonzero for every $r > 0$ and tending to $0$ as $r \to 0^+$. Consequently $\iota(X_p(\xi))$ descends at every point $r > 0$, to $\dsc = -\xi/r$, and converges, as $r \to 0^+$, to an ideal point at which $\dsc$ is undefined. The read-out fails exactly on $E$ and nowhere else in the physical closure.
\end{enumerate}

## technical
Fix a point $p$ in the invertible region of the Schwarzschild gravitational field on flat spacetime, whose gauge field $\hb$ carries the flat background to the physical vectors (a vector $x$ to $\hb^{-1}(x)$, a covector $\xi$ to $\hb^{T}(\xi)$), with $Q_p(x) = Q(\hb^{-1}(x))$ the square of the physical vector over the background vector $x$, whose Gram in the static gauge is the derived metric $g_p = \operatorname{diag}(f, -f^{-1}, -r^2, -r^2\sin^2\theta)$ with $f = 1 - 2M/r$, and lift $x \in T_pM$ through its physical vector, $X_p(x) = (1, \hb^{-1}(x), \frac12 Q_p(x))$, in the homogeneous coordinates $(s, x, t)$ of the completion $\Cl(2,4)$. Every lift satisfies the incidence condition $Q_p(x) = 2st$, and the transported reciprocal $\iota(s,x,t) = (2t, x, \frac12 s)$ preserves it and is an involution. If $Q_p(x) \neq 0$ the read-out returns the classical reciprocal, $\dsc(\iota(X_p(x))) = \hb^{-1}(x)/Q_p(x)$, the physical vector over $x/Q_p(x)$. If $Q_p(x) = 0$, for instance on the radial null direction $\et + f\,\er$, the image is the ideal point $[\hb^{-1}(x) + \frac12 \nInf]$ and $\dsc$ is undefined there.

For the generator $\xi = \sqrt{2M}\,dt_s + (\sqrt r/f)\,dr$ of the radical line of the degeneration, taken from the weighted Painlev\'e-Gullstrand coframe, the dual norm, the derived cometric $Q^{*}_p(\xi) = Q(\hb^{T}(\xi))$, is exactly $-r$ at every radius, the horizon included. Hence $\iota(X_p(\xi))$ descends to $\dsc = -\hb^{T}(\xi)/r$, the physical covector over $-\xi/r$, at every $r > 0$ and converges, as $r \to 0^{+}$, to an ideal point at which $\dsc$ is undefined: the read-out fails exactly on $E$ and nowhere else in the physical closure.

## lay
At each point of a non-rotating black hole away from its centre, the series' repair is carried out explicitly on the space of directions. Ordinary directions go up into the enlarged space and come back down as their usual reciprocals, while light-like directions go up to points at infinity that have nothing below them. The one direction that dies at the singularity can be brought back down at every radius, however close to the centre, and fails to come back only in the limit at the centre itself. So the read-out breaks down exactly at the singularity and nowhere else, the horizon included.

## one-liner
On the Schwarzschild fibre the transported reciprocal returns the classical reciprocal on invertible directions, sends null directions to ideal points, and descends on the dying direction at every $r > 0$ with $Q^{*}_p(\xi) = -r$, so the read-out fails exactly on $E$.
