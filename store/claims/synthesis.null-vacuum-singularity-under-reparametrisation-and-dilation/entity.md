---
id: synthesis.null-vacuum-singularity-under-reparametrisation-and-dilation
kind: claim
version: 1
title: 'Null-vacuum singularity under reparametrisation and dilation'
status: proved
region: synthesis
subject: thermality
tags: [car-algebra, horizons, needs-continuum]
proposed_by:
  kind: ai
  session: maintainer-2026-11-07
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: split out of synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet so that its users rest only on the analysis
  source: maintainer pass 2026-11-07
review: draft
outside_ga:
  kind: complex-analysis
  why: 'the generator kernels (i/2 pi)(U - U'' + i0)^{-1}, their reparametrised forms and the weight-h kernels (U - U'' + i0)^{-2h} are boundary values of scalar kernels; the prefactor and the boundary value carry one complex unit, so writing the prefactor alone as I_4 would split it; kept as in the result it was split from'
about:
- obj.hawking.continuum-mode-space
derivations:
- name: main
  uses:
  - synthesis.null-vacuum-on-a-horizon-generator@1
  - hawking.imported-quasi-free-kms-reduces-two@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_regular_reparametrisation_keeps_the_ground_state_singularity
- kind: check
  ref: check.py::check_scaling_limit_is_the_ground_state
- kind: proof
  derivation: main
extraction:
  note: >-
    The two kernel lemmas of synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet (its (iii)
    and (iv)), stated on one generator with no horizon, gauge field or premise: the weight-1/2 null-vacuum
    kernel changes by a Schwarzian term, continuous and zero on the diagonal, under a regular
    reparametrisation, and a state whose kernel is the null-vacuum kernel plus a remainder bounded near a
    point tends to the null vacuum under the weight-1/2 dilation about that point. Standard in kind (the
    chiral two-point function's Schwarzian covariance; the Fredenhagen-Haag mechanism, cited from memory);
    transport-absent.
  maintainer_pass_clause_split:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Created at Leon''s decision of 7 November 2026 to split the premise-free lemmas out of synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet, so that synthesis.local-normality-at-the-edge-gives-the-null-ground-state and synthesis.normality-on-the-closed-generator-gives-the-vacuum-folium-not-the-ground-state, which cite only these lemmas, no longer inherit J3 and the counting and local-horizon premises through that result. Numbering: its (iii) is (i) here and its (iv) is (ii) here, with the Killing flow beta_tau written as the dilation delta_epsilon, epsilon = e^{-kappa tau}, and the Boulware example left there. Proofs moved; the two checks are copied from its check functions with the premise call moved to the null-vacuum result. Notation as in the source: i in the kernels, declared.'
---

## formal
On the continuum mode space $\CAR(L^{2}(\R, dU)\otimes K)$ of one null generator with a parameter $U$ (Definition \claimref{obj.hawking.continuum-mode-space}), with fields of weight $\tfrac12$, $\{\psi(U), \psi^{*}(U')\} = \delta(U - U')\otimes\id_{K}$:
\begin{enumerate}
\item[(i)] \emph{(The singularity is the same in every regular parameter.)} For the weight-$\tfrac12$ fields of the carrier and a $C^{3}$ reparametrisation $\xi$ of the generator with $\xi' > 0$, the null-vacuum kernels of Theorem \claimref{synthesis.null-vacuum-on-a-horizon-generator}(ii) in the two parameters differ by a kernel continuous across the diagonal and vanishing on it:
\[
\frac{\xi'(U)^{1/2}\,\xi'(U')^{1/2}}{\xi(U) - \xi(U') + i0} \;-\; \frac{1}{U - U' + i0} \;=\; \frac{S_{\xi}(U)}{12}\,(U - U') + O\bigl((U - U')^{2}\bigr), \qquad S_{\xi} = \frac{\xi'''}{\xi'} - \frac32\Bigl(\frac{\xi''}{\xi'}\Bigr)^{2},
\]
the squared ratio of the two kernels being $1 + \tfrac16 S_{\xi}(U)(U - U')^{2} + O((U - U')^{3})$. The kernel $1/(U - U' + i0)$ is covariant in this way only with the weight $\tfrac12$ (with weight $0$ or $1$ attached to it the difference is singular on the diagonal unless $\xi' \equiv 1$); a weight-$h$ field with its own kernel $(U - U' + i0)^{-2h}$ has the continuous remainder $\tfrac{h}{6}S_{\xi}(U)(U - U')^{2 - 2h} + \dots$ for every $h \le 1$, equal to $S_{\xi}/6$ on the diagonal at $h = 1$. Where $\xi'$ vanishes the ratio vanishes. Hence the class of gauge-invariant quasi-free states on the carrier whose two-point kernel is the null-vacuum kernel plus a remainder bounded near a point of the generator is the same in every regular parameter.
\item[(ii)] \emph{(The dilation limit is the null vacuum.)} Let $\omega$ be a gauge-invariant quasi-free state on $\CAR(L^{2}(\R, dU)\otimes K)$ whose two-point kernel is $W_{0}(U, U') + R(U, U')$, with $W_{0}(U,U') = \tfrac{i}{2\pi}\tfrac{1}{U - U' + i0}\otimes\id_{K}$ the kernel of the null vacuum $\omega_{0}$ for the $U$-translations (Theorem \claimref{synthesis.null-vacuum-on-a-horizon-generator}(ii), written with $i$ for its unit $I_{4}$) and $R$ bounded on a neighbourhood of $(0, 0)$. Let $\delta_{\varepsilon}(\psi(U)) = \varepsilon^{1/2}\psi(\varepsilon U)$, $\varepsilon > 0$, be the weight-$\tfrac12$ dilation about $U = 0$ (an automorphism, Theorem \claimref{synthesis.null-vacuum-on-a-horizon-generator}(i)). Then for all $f, g \in L^{1}\cap L^{2}$, $\lim_{\varepsilon\to 0^{+}}\omega(\delta_{\varepsilon}(\psi^{*}(f)\psi(g))) = \omega_{0}(\psi^{*}(f)\psi(g))$, and by quasi-freeness (Fact \claimref{hawking.imported-quasi-free-kms-reduces-two}) $\omega\circ\delta_{\varepsilon} \to \omega_{0}$ on the whole carrier: under the dilation the singular part is invariant and the remainder's contribution is $\varepsilon\iint \bar f(x')g(x)R(\varepsilon x, \varepsilon x')\,dx\,dx' \to 0$. The condition is sufficient, not necessary: the proof uses only $\varepsilon\iint\bar f g R(\varepsilon x, \varepsilon x') \to 0$, which holds for every bounded $R$ and also for every finite-rank change of the symbol (the dilated test functions tend weakly to zero), so states outside the class can have the same limit. A remainder homogeneous of degree $-1$ is unbounded near the origin and survives the limit unchanged.
\end{enumerate}
Both are statements about kernels on one generator; they assume no premise.

## technical
On one null generator the null vacuum's two-point kernel, carried by fields of weight $\tfrac12$, keeps its singularity under every regular change of parameter: the two kernels differ by the Schwarzian of the reparametrisation times the separation, continuous across the diagonal and zero on it, and only the weight $\tfrac12$ gives this. So the class of states whose kernel is the null-vacuum kernel plus a remainder bounded near a point does not depend on the parameter. Under the weight-$\tfrac12$ dilation about a point, the singular part is invariant and a bounded remainder scales away, so every state in the class tends to the null vacuum; the condition is sufficient, not necessary, and a remainder homogeneous of degree $-1$ survives. These are the two lemmas behind the late-time Hawking state on the ingoing sheet, stated here without the horizon.

## lay
Along a light ray, the vacuum of a spin-one-half field has a characteristic short-distance singularity. This result shows two things about it: relabelling the points of the ray smoothly does not change the singularity, only adds a smooth correction; and zooming in on a point turns any state with that singularity plus a bounded correction into the vacuum. Both are facts about the vacuum's two-point function alone, with no assumption about black holes.

## one-liner
On a null generator the weight-$\tfrac12$ null-vacuum kernels in two regular parameters differ by $\tfrac{1}{12}S_{\xi}(U)(U - U') + O((U - U')^{2})$, so the class "null-vacuum kernel plus a remainder bounded near a point" is parameter-free, and every state in it tends to the null vacuum under the weight-$\tfrac12$ dilation about that point.
