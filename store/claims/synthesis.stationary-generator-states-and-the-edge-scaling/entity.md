---
id: synthesis.stationary-generator-states-and-the-edge-scaling
kind: claim
version: 1
title: 'Stationary generator states and the scaling about the edge'
status: proved
region: synthesis
subject: thermality
tags: [car-algebra, modular-theory, horizons, needs-continuum]
proposed_by:
  kind: ai
  session: maintainer-2026-11-07
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: split out of synthesis.stationary-horizon-state-is-its-own-edge-scaling-limit so that its users rest only on the analysis
  source: maintainer pass 2026-11-07
review: draft
about:
- obj.hawking.continuum-mode-space
derivations:
- name: main
  uses:
  - synthesis.null-vacuum-on-a-horizon-generator@1
  - hawking.i-state-continuum@5
  - hawking.imported-quasi-free-kms-reduces-two@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_boost_is_the_car_scaling_about_the_edge
- kind: check
  ref: check.py::check_kernels_homogeneous_and_differ_only_at_the_edge_scale
- kind: check
  ref: check.py::check_off_the_edge_every_member_is_locally_the_vacuum
- kind: check
  ref: check.py::check_cross_edge_block
- kind: proof
  derivation: main
extraction:
  note: >-
    The carrier content of synthesis.stationary-horizon-state-is-its-own-edge-scaling-limit, its clauses (i)
    to (iii), stated on one generator with no horizon: the weight-1/2 boost is the scaling about the edge
    point (and the local boost rotor of Cl(1,3) dilates each generator of a null plane about its edge point),
    a stationary state is its own scaling limit at the edge so that it is locally the null vacuum there
    exactly when it is the null vacuum, and the stationary half-thermal products are locally the null vacuum
    at every point off the edge but differ from it at the edge by a kernel homogeneous of degree -1. The
    null-line form of the Kay-Wald uniqueness argument and of the Fredenhagen-Haag scaling-limit condition
    (cited from memory); transport-absent.
  maintainer_pass_clause_split:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Referee fix of 7 November 2026, folded into version 1: in the proof of (iii) the symbol of the boost ground state (c = infinity) is chi_(0,infinity)(w), that is chi_(-infinity,0)(h), not chi_(-infinity,0)(w) (a sign slip inherited from synthesis.stationary-horizon-state-is-its-own-edge-scaling-limit, whose proof of (iii) now cites this result and no longer carries the sentence). Created at Leon''s decision of 7 November 2026 (third cut, option (b)) to split the premise-free carrier content out of synthesis.stationary-horizon-state-is-its-own-edge-scaling-limit, so that the local-normality and microlocal results, which use only that content, no longer inherit (N+) through it. Clauses (i), (ii) and (iii) are its (i), (ii) and (iii), with the identification of each horizon''s flow with the boost and the reading of (ii) as (N+) left there; (iii) is included because the microlocal result''s example (iii)(c) and the local-normality result use the half-thermal products. Proofs moved; four of its check functions copied with the premise call moved to the null-vacuum result. Units per Leon''s rulings R2 and R4: I_4 throughout; nothing is declared.'
---

## formal
Units $\hbar = c = 1$. On one null generator with affine parameter $u \in \R$, take the continuum mode space $\CAR(L^{2}(\R, du)\otimes K)$ of Definition \claimref{obj.hawking.continuum-mode-space}, $\{\psi(u), \psi^{*}(v)\} = \delta(u - v)\otimes\id_{K}$ (numbers are read in $\mathrm{span}\{1, I_{4}\}$, $I_{4}$ the unit of the mode space), with the boost about the edge point $u = 0$, $\beta_{t}(\psi(u)) = e^{\kappa t/2}\psi(e^{\kappa t}u)$, $\kappa > 0$ (Theorem \claimref{synthesis.null-vacuum-on-a-horizon-generator}(i)). Write $W_{\omega}(u, v) = \omega(\psi^{*}(v)\psi(u))$, and $\omega_{0}$ for the null vacuum, $W_{0}(u, v) = \tfrac{I_{4}}{2\pi}(u - v + I_{4}0)^{-1}\otimes\id_{K}$, the gauge-invariant quasi-free ground state of the null translations (Theorem \claimref{synthesis.null-vacuum-on-a-horizon-generator}(ii)). For a point $u_{0}$ and $\lambda > 0$ let $\sigma^{u_{0}}_{\lambda}(\psi(u_{0} + x)) = \lambda^{1/2}\psi(u_{0} + \lambda x)$; the \emph{scaling limit} of $\omega$ at $u_{0}$ is the gauge-invariant quasi-free state with two-point function $\lim_{\lambda \to 0^{+}}\lambda\,W_{\omega}(u_{0} + \lambda x, u_{0} + \lambda y)$ (as distributions), when the limit exists, and $\omega$ is \emph{locally the null vacuum at $u_{0}$} if that limit exists and is $\omega_{0}$ (the series' local form of (N$_{+}$) at $u_{0}$). Call $\omega$ stationary if $\omega\circ\beta_{t} = \omega$ for all $t$.
\begin{enumerate}
\item[(i)] \emph{(The boost is the scaling about the edge.)} $\beta_{t} = \sigma^{0}_{e^{\kappa t}}$. Among the weights $\lambda^{p}$, only $p = \tfrac12$ makes $\sigma_{\lambda}$ preserve the anticommutator. In $\Cl(1,3)$ (store signature) the rotor $B = \cosh\tfrac{\lambda}{2} + \sinh\tfrac{\lambda}{2}\,e_{1}e_{0}$ sends $\ell = e_{0} + e_{1}$ to $e^{\lambda}\ell$, $n = e_{0} - e_{1}$ to $e^{-\lambda}n$ and fixes $e_{2}, e_{3}$: on the null plane $\{u\ell + y\}$ it dilates every generator about its own edge point.
\item[(ii)] \emph{(A stationary state is its own scaling limit at the edge.)} A stationary gauge-invariant quasi-free $\omega$ is its own scaling limit at the edge. Hence $\omega$ is locally the null vacuum at the edge if and only if $\omega = \omega_{0}$, that is, if and only if $\omega$ is the gauge-invariant quasi-free ground state of the null translations. The same holds with the weaker condition that $W_{\omega} - W_{0}$ be a bounded function on some neighbourhood of $(0, 0)$ (in each $K$-component): a function homogeneous of degree $-1$ and bounded near the origin vanishes. The null vacuum $\omega_{0}$ is its own scaling limit at every point.
\item[(iii)] \emph{(Off the edge every stationary thermal state is locally the vacuum.)} For $c \in (0, \infty]$ let $\omega_{c}^{\times}$ be the product, over the two halves $u > 0$ and $u < 0$, of the quasi-free states KMS at rapidity period $2\pi c$ for the boost future-directed on each half ($c = \infty$: the ground state of that boost). Each is stationary, even and gauge-invariant quasi-free. On $u, v > 0$, with $y = \ln(u/v)$,
\[
W_{c}(u, v) = \frac{I_{4}}{2\pi}\,\frac{(uv)^{-1/2}}{2c\,\sinh\!\big((y + I_{4}0)/2c\big)}, \qquad \text{Mellin symbol } (1 + e^{-2\pi c w})^{-1} \text{ on } u^{-1/2 + I_{4}w},
\]
the I-state of Theorem \claimref{hawking.i-state-continuum} at period $2\pi c$ (the mirror image on $u, v < 0$), $W_{1} = W_{0}$ there. The difference $D_{c} = W_{c} - W_{0}$ is $\tfrac{I_{4}}{2\pi}(uv)^{-1/2}g_{c}(y)$ with $g_{c}$ analytic for $|\mathrm{Im}\,y| < 2\pi\min(c, 1)$, $g_{c}(y) = -\tfrac{1}{24}(c^{-2} - 1)\,y + O(y^{3})$. So every $\omega_{c}^{\times}$ is locally the null vacuum at every point $u_{0} \neq 0$ of every generator. The scaling limit at $u_{0} \neq 0$ involves only the block of the two-point function on the half containing $u_{0}$, so the same holds for every stationary gauge-invariant quasi-free state whose restrictions to the two halves are those of $\omega_{c}^{\times}$, whatever its cross-edge block; for $c \neq 1$ none of these is $\omega_{0}$, since its half restrictions differ from those of $\omega_{0}$. The cross-edge block of $\omega_{c}^{\times}$ vanishes while that of $\omega_{0}$ is $\tfrac{I_{4}}{2\pi}(u - v)^{-1}$; so $\omega_{c}^{\times} \neq \omega_{0}$ for every $c$, including $c = 1$, where both halves are the I-state at $2\pi$. For $c \neq 1$ the difference on each half, and for every $c$ the cross-edge difference, is homogeneous of degree $-1$, nonzero and unbounded on every neighbourhood of the edge.
\end{enumerate}
These are statements about states on the carrier of one generator and the dilation about one of its points; they assume no premise. Which horizon flow acts on the carrier as $\beta_{t}$, and which state a horizon's modes are in, are separate matters (Theorem synthesis.stationary-horizon-state-is-its-own-edge-scaling-limit and Premise (N$_{+}$)).

## technical
On the continuum of one null generator, the boost about a point, with the weight $\tfrac12$ that the anticommutator forces, is exactly the scaling map about that point used to define scaling limits. So a state invariant under the boost is its own scaling limit at the point: it is locally the null vacuum there if and only if it is the null vacuum, and a difference from the vacuum that stays bounded near the point already forces equality. Away from the point the condition says much less: the product states that are thermal on each half of the generator, at any period, are locally the null vacuum at every other point, and differ from the vacuum at the point itself by a kernel homogeneous of degree $-1$, unbounded there. These statements concern the carrier and one dilation; which horizon flow is that dilation, and which state a horizon's modes are in, are not part of them.

## lay
Along a light ray of a horizon, zooming in on a point and the horizon's own boost about that point turn out to be the same operation. So a state that does not change under the boost looks, at that point, exactly as it does everywhere, and it looks like the vacuum close to the point only if it is the vacuum. Thermal states that are unchanged by the boost can look like the vacuum everywhere except at that one point. This result proves these facts about states on the light ray, without assuming anything about a black hole.

## one-liner
On the continuum carrier of a null generator the weight-$\tfrac12$ boost about a point is the scaling map about it, so a stationary gauge-invariant quasi-free state is its own scaling limit there and is locally the null vacuum at that point if and only if it is the null vacuum (a bounded difference suffices), while the stationary half-thermal products are locally the vacuum everywhere off the point and differ from it there by an unbounded degree $-1$ kernel.
