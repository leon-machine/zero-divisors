---
id: synthesis.limits-as-null-steps
kind: claim
version: 1
title: Limits as null steps
status: proved
region: synthesis
subject: clifford-structure
tags: [limits, null-directions, rotors-and-stabilisers, needs-continuum]
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
  - std-algebra.radical-ideal-and-quotient@1
  - std-algebra.witt-basis-car@1
  - std-algebra.bivector-exponential@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_dual_number_derivative
- kind: check
  ref: check.py::check_product_of_null_steps_is_the_exponential
- kind: check
  ref: check.py::check_boost_scales_the_null_vector
- kind: check
  ref: check.py::check_half_angle_rotors_and_archimedes
- kind: check
  ref: check.py::check_taylor_denominators
- kind: proof
  derivation: main
extraction:
  note: >-
    From Leon's working document "Scalars and the Continuum: Review and Extensions" (6 November
    2026), the item "limits as null steps", re-proved and re-checked here; not an attack on an open
    problem. Clauses (i) to (iii) are exact identities; clause (iv) is exact for the rotors and
    Archimedes' recursion, while the bounds on pi and the rate of the gap are numerical (classical
    analysis, $\sin\theta < \theta < \tan\theta$), stated in the proof and not checked; clause (v)
    is checked to degree 21 only. Correction to the source: N commuting square-zero products of
    pairs of orthogonal null vectors need 2N mutually orthogonal null vectors, so Cl(2N,2N), not
    Cl(N,N) (the source's own example, N = 3 in Cl(6,6), is of this form). Ledger: (i), (iv) and
    (v) are transport-absent (dual numbers, the half-angle formula and Archimedes' polygons are
    classical); (ii) and (iii) are transport-convenient, the nilpotent steps being realised by the
    null vectors of the nondegenerate algebras the ascent produces, and the first-order boost being
    the null scaling (1 - d). Cited from memory and not used: dual numbers and the derivative
    (Clifford 1873; forward-mode automatic differentiation); Archimedes' Measurement of a Circle;
    that every Taylor coefficient of tan has odd denominator (2-adic valuation of the tangent
    numbers).
---

## formal
\begin{enumerate}
\item[(i)] \emph{(The derivative.)} In $\Cl(0,0,1)$, with generator $\rho$, $\rho^{2} = 0$, every rational function $f$ with rational coefficients regular at a rational $x$ satisfies $f(x + \rho) = f(x) + f'(x)\,\rho$.
\item[(ii)] \emph{(The exponential.)} Let $b_{1}, \dots, b_{N}$ commute pairwise and satisfy $b_{i}^{2} = 0$, and $\varepsilon = b_{1} + \dots + b_{N}$. Then $\varepsilon^{k} = k!\,e_{k}(b_{1}, \dots, b_{N})$ with $e_{k}$ the elementary symmetric polynomial, $\varepsilon^{N+1} = 0$, and
\[
\prod_{i=1}^{N}(1 + b_{i}) \;=\; \sum_{k=0}^{N}e_{k}(b) \;=\; \sum_{k=0}^{N}\frac{\varepsilon^{k}}{k!} \;=\; \exp\varepsilon .
\]
Such steps exist in $\Cl(0,0,2N)$, $b_{i} = \rho_{2i-1}\rho_{2i}$, and in the nondegenerate $\Cl(2N,2N)$, $b_{i} = n_{2i-1}n_{2i}$ for $2N$ mutually orthogonal null vectors $n_{j}$.
\item[(iii)] \emph{(The boost.)} In $\Cl(1,1)$ let $B = e_{t}e_{r}$, $Q(e_{t}) = 1$, $Q(e_{r}) = -1$, and $l_{\pm} = e_{t} \pm e_{r}$. For even $R = \alpha + \beta B$, $R\,l_{+}\widetilde{R} = (\alpha - \beta)^{2}\,l_{+}$ and $R\,l_{-}\widetilde{R} = (\alpha + \beta)^{2}\,l_{-}$. For a nilpotent central rapidity $d$ ($d^{2} = 0$, for instance $d = s\,\rho_{1}\rho_{2}$ in $\Cl(1,1,2)$), $\exp(\tfrac12 dB)\,l_{\pm}\exp(-\tfrac12 dB) = (1 \mp d)\,l_{\pm}$: to first order a boost is the null step $1 - d$ on $l_{+}$. The boost with $R^{2} = \tfrac54 + \tfrac34 B$ ($\cosh\phi = \tfrac54$) sends $l_{+}$ to exactly $\tfrac12 l_{+}$ and $l_{-}$ to $2\,l_{-}$.
\item[(iv)] \emph{(Half-angle rotors.)} In $\Cl(2,0)$ with $I = e_{1}e_{2}$, every rotor $R$ of the plane satisfies $(1 + R)^{2} = 2(1 + \langle R\rangle_{0})\,R$, so $\sqrt{R} = (1 + R)/\lvert 1 + R\rvert$ with $\lvert 1 + R\rvert^{2} = (1 + R)(1 + R)^{\sim} = 2(1 + \langle R\rangle_{0})$ whenever $R \ne -1$. Starting from the half turn $R_{0} = I$, the rotors $R_{k+1} = (1 + R_{k})/\lvert 1 + R_{k}\rvert$ have $\langle R_{k}\rangle_{0} = c_{k} = \tfrac12 r_{k}$ and $\langle R_{k}I^{-1}\rangle_{0} = s_{k}$ with $r_{1}^{2} = 2$, $r_{k+1}^{2} = 2 + r_{k}$ and $s_{k+1} = s_{k}/(2c_{k+1})$, all in the field generated over $\Q$ by nested square roots of $2$. The numbers $L_{k} = 2^{k+1}s_{k}$ and $U_{k} = L_{k}/c_{k}$ satisfy Archimedes' recursion $U_{k+1}(U_{k} + L_{k}) = 2U_{k}L_{k}$, $L_{k+1}^{2} = U_{k+1}L_{k}$, from $L_{1}^{2} = 8$, $U_{1} = 4$. Reading $R_{k} = \exp(\theta_{k}I)$, $\theta_{k} = \pi/2^{k+1}$, through the exponential chart, $L_{k} < \pi < U_{k}$ and $4^{k}(U_{k} - L_{k}) \to \pi^{3}/8$.
\item[(v)] \emph{(Which denominators.)} The Taylor coefficients of $\tan$ and $\arctan$ at $0$ through degree $21$ have odd denominators, while the coefficient $1/k!$ of $\exp$ has every prime $p \le k$ in its denominator.
\end{enumerate}

## technical
Several limits of analysis are exact identities once the small step is a nilpotent element of a Clifford algebra. A degenerate direction $\rho$ with $\rho^{2} = 0$ turns every rational function into its first-order expansion, $f(x + \rho) = f(x) + f'(x)\rho$, so the derivative is read off as a coefficient. Several commuting square-zero steps multiply to the exponential of their sum with no limit taken: $\prod(1 + b_{i}) = \exp(\sum b_{i})$, because every power of the sum is $k!$ times an elementary symmetric polynomial and the series stops. In the nondegenerate algebras the series builds, such steps are products of orthogonal null vectors, so no degenerate direction is needed. A boost with nilpotent rapidity $d$ scales a null vector by $1 - d$, the first-order form of the exact scaling $e^{-\phi}$; with rational $\cosh\phi = \tfrac54$ the scaling is exactly $\tfrac12$.

Square roots of rotors are algebraic: $(1 + R)^{2} = 2(1 + \langle R\rangle_{0})R$. Halving the half turn repeatedly produces rotors whose components are nested square roots of $2$, and the inscribed and circumscribed polygon semi-perimeters built from them obey Archimedes' recursion exactly; that they bracket $\pi$ uses the exponential chart and classical analysis, and is stated as numerics. The tangent and arctangent series, which underlie the rational half-angle chart, have only odd denominators to degree $21$, while the exponential's denominators contain every prime.

## lay
Calculus normally gets derivatives and exponentials by letting a step shrink towards zero. In these algebras there are nonzero quantities whose square is exactly zero, and using one of them as the step makes the shrinking unnecessary: the change of a function over such a step is exactly its derivative times the step, and multiplying many such steps together gives exactly an exponential. Halving a rotation again and again produces numbers built from repeated square roots of two, and these are exactly Archimedes' perimeters of polygons that close in on the number pi.

## one-liner
With nilpotent steps the limits of analysis become identities: $f(x + \rho) = f(x) + f'(x)\rho$ in $\Cl(0,0,1)$, $\prod(1 + b_{i}) = \exp(\sum b_{i})$ for commuting square-zero $b_{i}$ (realised by orthogonal null vectors in $\Cl(2N,2N)$), a boost of nilpotent rapidity $d$ scales a null vector by $1 - d$, and the half-angle rotors $(1 + R)/\lvert 1 + R\rvert$ from the half turn give Archimedes' recursion for $\pi$ in nested square roots of $2$.
