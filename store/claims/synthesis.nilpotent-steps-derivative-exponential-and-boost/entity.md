---
id: synthesis.nilpotent-steps-derivative-exponential-and-boost
kind: claim
version: 1
title: 'Nilpotent steps: dual-number derivative, nilpotent exponential and nilpotent boost'
status: proved
region: synthesis
subject: clifford-structure
tags: [null-directions, degenerate-algebras, hyperbolic-plane, classical-theorem]
proposed_by:
  kind: ai
  session: 2026-11-06-edge-normality
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: run 2026-11-06-edge-normality
review: draft
derivations:
- name: main
  uses:
  - std-algebra.radical-ideal-and-quotient@2
  - std-algebra.witt-basis-car@1
  - singularity.pseudo-inverse-identities-hyperbolic-atom@4
  - conformal.minimal-nondegenerate-completion@6
  - transport.regularity-localises-zero-divisors-idempotents@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_dual_number_derivative
- kind: check
  ref: check.py::check_derivative_through_a_generalised_inverse
- kind: check
  ref: check.py::check_product_of_null_steps_is_the_exponential
- kind: check
  ref: check.py::check_boost_scales_the_null_vector
- kind: proof
  derivation: main
extraction:
  note: >-
    From Leon's working document "Scalars and the Continuum: Review and Extensions" (6 November
    2026), the item "limits as null steps" and the derivative through the Witt partner, re-proved and
    re-checked here; not an attack on an open problem. The identities are the
    first-order truncations of the derivative and of the exponential, exact for rational functions and
    nilpotent arguments only; no limit of analysis is removed. In clause (ii), that the
    Witt partner is a generalised inverse is Proposition singularity.pseudo-inverse-identities-hyperbolic-atom,
    and that it is the Moore-Penrose one is T01's remark on the hyperbolic atom
    (note.transport.setting-hyperbolic-atom-matrix-algebra-moore) and clause (ii) of
    descent-lift.pairing-creator-under-transport-algorithm. Realisations in (iii): products of disjoint pairs from one family of mutually
    orthogonal null vectors need 2N such vectors, so Cl(2N,2N); with Jordan-Wigner twisted null vectors
    b_i = v_i pi_1 ... pi_{i-1}, pi_j = v_j w_j - w_j v_j, N steps with nonzero product already exist in
    Cl(N,N). Ledger: (i) and the exponential identity of (iii) are
    transport-absent (dual numbers, the nilpotent exponential); (ii), the realisations in (iii) and (iv)
    are transport-convenient, the nilpotent steps being the null vectors and ladder pairs of the
    nondegenerate algebras the ascent produces. Cited from memory and not used: dual numbers and the
    derivative (Clifford 1873; forward-mode automatic differentiation).
---

## formal
Coefficients and the point $x$ are rational, and $f$ is a rational function with rational coefficients, regular at $x$.
\begin{enumerate}
\item[(i)] \emph{(The dual-number derivative.)} For any element $n$ of an algebra with $n^{2} = 0$, $f(x + n) = f(x) + f'(x)\,n$; in particular in $\Cl(0,0,1)$, with generator $\rho$, $f(x + \rho) = f(x) + f'(x)\,\rho$.
\item[(ii)] \emph{(Through a generalised inverse.)} A vector $\rho$ of the radical of $\Cl(p,q,r)$, $r \ge 1$, satisfies $\rho\,x\,\rho = 0$ for every $x$, so it has no generalised inverse and the step in (i) cannot be divided by. If instead $n^{2} = 0$ and $g$ is a generalised inverse of $n$ ($ngn = n$), then $gn$ is idempotent and
\[
g\,\big(f(x + n) - f(x)\big) = f'(x)\,gn .
\]
In the minimal completion, which is nondegenerate and so von Neumann regular, $\rho$ becomes a null vector $n$ with a Witt partner $m$ ($nm + mn = 1$, $nmn = n$), and $m(f(x + n) - f(x)) = f'(x)\,mn$; in $\Cl(1,1)$, for the anti-automorphism exchanging $n = \tfrac12(e_{+} + e_{-})$ and $m = \tfrac12(e_{+} - e_{-})$, the partner is the generalised inverse whose idempotent $mn$ is self-adjoint.
\item[(iii)] \emph{(The nilpotent exponential.)} Let $b_{1}, \dots, b_{N}$ commute pairwise with $b_{i}^{2} = 0$, and $\varepsilon = b_{1} + \dots + b_{N}$. Then $\varepsilon^{k} = k!\,e_{k}(b_{1}, \dots, b_{N})$ with $e_{k}$ the elementary symmetric polynomial, $\varepsilon^{N+1} = 0$, and
\[
\prod_{i=1}^{N}(1 + b_{i}) \;=\; \sum_{k=0}^{N}\frac{\varepsilon^{k}}{k!} \;=\; \exp\varepsilon ,
\]
a finite sum. Such steps with nonzero product exist in $\Cl(0,0,2N)$ ($b_{i} = \rho_{2i-1}\rho_{2i}$), in $\Cl(2N,2N)$ (products of disjoint pairs of $2N$ mutually orthogonal null vectors), and already in $\Cl(N,N)$: for Witt pairs $v_{i}, w_{i}$ and $\pi_{j} = v_{j}w_{j} - w_{j}v_{j}$, the steps $b_{i} = v_{i}\pi_{1}\cdots\pi_{i-1}$.
\item[(iv)] \emph{(The nilpotent boost.)} In $\Cl(1,1)$ let $B = e_{t}e_{r}$, $Q(e_{t}) = 1$, $Q(e_{r}) = -1$, and $l_{\pm} = e_{t} \pm e_{r}$. For scalars $\alpha, \beta$ and $R = \alpha + \beta B$, $R\,l_{+}\widetilde{R} = (\alpha - \beta)^{2}\,l_{+}$ and $R\,l_{-}\widetilde{R} = (\alpha + \beta)^{2}\,l_{-}$; the boost with $R^{2} = \tfrac54 + \tfrac34 B$ sends $l_{+}$ to $\tfrac12 l_{+}$ and $l_{-}$ to $2\,l_{-}$. Over the ring $\R[d]/(d^{2})$, realised by $d = s\,\rho_{1}\rho_{2}$ in $\Cl(1,1,2)$,
\[
\exp(\tfrac12 dB)\,l_{\pm}\,\exp(-\tfrac12 dB) = (1 \mp d)\,l_{\pm} ,
\]
so a boost of rapidity $d$ scales a null vector by $1 - d$. Here $d$ is a scalar of $\R[d]/(d^{2})$ and $\exp(-\tfrac12 dB)$ is the inverse of $\exp(\tfrac12 dB)$; the reversion of $\Cl(1,1,2)$ fixes the grade-$4$ element $dB$, and conjugation by $R$ and $\widetilde{R}$ with that reversion leaves $l_{\pm}$ fixed.
\end{enumerate}
No limit is removed: derivatives of functions that are not rational, and the exponential of an element that is not nilpotent, still need analysis.

## technical
The first-order truncations behind two limits of analysis, the derivative and the exponential, are exact identities when the step is nilpotent; this covers rational functions and nilpotent arguments only. A square-zero step $n$ turns every rational function into its first-order expansion, $f(x + n) = f(x) + f'(x)n$, so the derivative is read off as a coefficient. A degenerate direction cannot be divided by, since $\rho x \rho = 0$ for every $x$; after the completion the step becomes a null vector with a generalised inverse, any one of which turns the difference into the derivative times an idempotent, and the Witt partner is the one with a self-adjoint idempotent. Several commuting square-zero steps multiply to the exponential of their sum, a finite polynomial, because every power of the sum is $k!$ times an elementary symmetric polynomial; such steps are products of orthogonal null vectors in $\Cl(2N,2N)$, and Jordan-Wigner twisted null vectors already in $\Cl(N,N)$. Over the dual numbers a boost of nilpotent rapidity $d$ scales a null vector by $1 - d$, the first-order form of the scaling $e^{-\phi}$; with rational $\cosh\phi = \tfrac54$ the finite scaling is exactly $\tfrac12$.

## lay
Calculus usually gets a derivative by letting a step shrink towards zero. In these algebras there are nonzero quantities whose square is exactly zero, and using one of them as the step gives the derivative of any formula built from arithmetic, and the exponential of such a step, exactly; for other functions, and for the number pi, a limit is still needed. Dividing by such a step is impossible in the degenerate algebra, but after the series' repair step the step gains a partner that divides by it as far as possible, leaving the derivative times a projection.

## one-liner
For a square-zero step the first-order expansion is exact: $f(x + \rho) = f(x) + f'(x)\rho$ for rational $f$ in $\Cl(0,0,1)$, and after the completion a generalised inverse $g$ of the null step gives $g(f(x + n) - f(x)) = f'(x)\,gn$; for commuting square-zero $b_{i}$, $\prod(1 + b_{i}) = \exp(\sum b_{i})$, a finite sum (realised by orthogonal null vectors in $\Cl(2N,2N)$, or by twisted null vectors already in $\Cl(N,N)$); and over $\R[d]/(d^{2})$ a boost of rapidity $d$ scales a null vector by $1 - d$. No limit is removed: derivatives of non-rational functions and the exponential of a non-nilpotent element still need analysis.
