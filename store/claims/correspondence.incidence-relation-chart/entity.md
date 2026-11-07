---
id: correspondence.incidence-relation-chart
kind: claim
version: 5
title: "The incidence relation is the chart"
status: proved
region: correspondence
subject: conformal-spacetime
tags: [conformal-spinors, conformal-model, dictionaries]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T09, deposited version
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 5
  source: maintainer pass 2026-11-07 (GA units)
review: typed
derivations:
- name: main
  uses:
  - correspondence.chiral-planes-summand-spaces@5
  - correspondence.imported-stabilisers-flat-model@3
  - correspondence.skew-lines-splittings-hyperbolic-planes-one@4
  - correspondence.spinor-identification@7
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T09.py
  tags:
  - label:thm:incidence
- kind: check
  ref: check.py::check_expansion_and_chart
- kind: check
  ref: check.py::check_coverage_of_the_affine_chart
- kind: check
  ref: check.py::check_consequences_incidence_and_stabilisers
locators:
  paper: T09
  number: Thm 4.2
  label: thm:incidence
  line: 445
outside_ga:
  kind: bridge
  why: 'clause (4)(iii) sets Penrose''s incidence relation omega = i x pi, in its source''s notation, beside its real-algebra form, and records that I_6 acts as -i on the complex module CS of Cl(2,4)_C'
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (bridge): clause (4)(iii) sets Penrose''s incidence relation omega = i x pi, in its source''s notation, beside its real-algebra form, and records that I_6 acts as -i on the complex module CS of Cl(2,4)_C.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the Pluecker expansion, the chart phi with Q(m) = -2 det A and P(A) = X(m(A)), coverage of the chart, the incidence lines ker c(X(-x)) of A_x = (1/2) ninf x, and the stabiliser census (parabolic of dimension 11 = stabiliser of S_omega). Version 3 -> 4. Wording fix (Leon 2026-10-23): (4)(iii) displays the incidence relation as omega = (1/2) x ninf pi (= -(1/2) ninf x pi; the earlier (1/2) ninf x pi is the relation of the point -x) and says a factor of i, with I6 = e0 e1 e2 e3 e4 e5 acting as -i on CS (formal and technical); the check now tests A_x = (1/2) x ninf with m(A_x) = x.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  env: theorem
  outside_pilot_cites:
  - ButlerT6
  typing:
    by: ai-typing-pass
    removed:
    - correspondence.reality-conjugation-twistor-form-factor
    note: 'Removed the reality edge (E301): the theorem only restates the later reality proposition in
      clause (4)(iii) and points to it for the real locus, while that proposition''s proof genuinely uses
      this theorem; doubt: clause (4)(iii) is then carried by the reality proposition rather than by an
      edge here. The incidence relation and Klein correspondence are classical (Penrose, Klein) but no
      imported claim for them is in the store, so no standard route.'
  source_title: "The incidence relation is the chart"
  source_formal: |-
    Fix bases $\pi_1, \pi_2$ of $\Spi$ and $e_1, e_2$ of $\Som$ with $\pi_1\wedge\pi_2 = N_0$ and $e_1 \wedge e_2 = N_\infty$. For a linear map $A: \Spi \to \Som$ let $L_A := \{A\pi + \pi : \pi \in \Spi\}$ be its graph line and
    \[
    P(A) \;:=\; (A\pi_1 + \pi_1)\wedge(A\pi_2 + \pi_2) \;\in\; \Lambda^2\T
    \]
    its Pl\"ucker bivector, normalised by $P(0) = N_0$. Then:
    \begin{enumerate}
    \item \emph{(Expansion.)} $P(A) = N_0 + \varphi(A) + (\det A)\, N_\infty$, where $\varphi(A) := A\pi_1\wedge\pi_2 + \pi_1\wedge A\pi_2$ lies in the mixed slot $\Som\wedge\Spi$ and $\det$ is taken in the chosen bases.
    \item \emph{(The chart, term by term.)} $\varphi$ is a linear isomorphism onto the mixed slot $= \{\nO,\nInf\}^\perp \otimes \C$, and satisfies $\ip{\varphi(A)}{\varphi(A)} = -2\det A$. Writing $m(A) := \varphi(A)$ as a vector of $\{\nO,\nInf\}^\perp\otimes\C$, the Pl\"ucker bivector is exactly the completion's point embedding, complexified:
    \[
    P(A) \;=\; \nO \,+\, m(A)\,-\,\tfrac12\,\ip{m(A)}{m(A)}\,\nInf \;=\; X\bigl(m(A)\bigr).
    \]
    In particular every $P(A)$ is null, as a Pl\"ucker bivector must be, and the nullity of $P(A)$ is equivalent to the identity $\det A = -\tfrac12\ip{m(A)}{m(A)}$: the quadratic term of the chart is a determinant.
    \item \emph{(Coverage.)} $A \mapsto L_A$ is a bijection from $\operatorname{Hom}(\Spi, \Som)$ onto the lines of $\PT$ skew to $L_\infty$, and $[P(A)]$ ranges exactly over the points of the Klein quadric with $\ip{P}{\nInf} \neq 0$: the affine chart of the complexified conformal compactification, with the lines meeting $L_\infty$ as the points at infinity; the real locus is cut out in Proposition \claimref{correspondence.reality-conjugation-twistor-form-factor}(5).
    \item \emph{(Consequences.)} (i) The null pair adjoined by the Witt completion is the pair of skew lines $(L_\infty, L_0)$ (Proposition \claimref{correspondence.skew-lines-splittings-hyperbolic-planes-one}). (ii) The splitting of a twistor into its $(\omega, \pi)$ parts along $\T = \Som\oplus\Spi$ is the Witt completion seen at spinor level: the same datum in a third language. (iii) Penrose's incidence relation $\omega = ix\pi$ is the case $A = i\hat x$ of the chart map, with $\hat x$ Hermitian for the twistor form (Proposition \claimref{correspondence.reality-conjugation-twistor-form-factor}(5)). (iv) The stabiliser of the infinity line $L_\infty$ in $\mathfrak{so}(V_\C)$ is the stabiliser of the ray of $\nInf$: the Poincar\'e parabolic, with its Levi factor acting on $\Som \oplus \Spi$ as the two chiral $2$-dimensional representations, one plane the doublet of each $\mathfrak{sl}(2,\C)$ factor of the complexified Lorentz algebra and trivial for the other (Lemma \claimref{correspondence.chiral-planes-summand-spaces}(1)).
    \end{enumerate}
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: "Renamed twistor space to the conformal spinor space (\\CS, \\PCS) and, in clause (4)(iii), converted the factor $i$ of the incidence relation to the complex unit $I_6$ of \\CS and named the real-algebra form $\\omega = \\tfrac12 n_\\infty x\\,\\pi$ (TWGA E1.5e, E1.7); since $\\hat x$ is Hermitian exactly when $-\\hat x$ is, the clause holds for either sign of the unit. The complexified chart ($V_\\C$, the complexified compactification and Lorentz algebra) is kept as in the original."
  i4_conversion:
    by: ai-i4-pass
    date: 2026-10-21
    converted: []
    kept:
    - "the factor $i$ of the incidence relation $\\omega = ix\\pi$: the conformal spinors unit $I_6$, set by the earlier pass"
---

## formal
Fix bases $\pi_1, \pi_2$ of $\Spi$ and $e_1, e_2$ of $\Som$ with $\pi_1\wedge\pi_2 = N_0$ and $e_1 \wedge e_2 = N_\infty$. For a linear map $A: \Spi \to \Som$ let $L_A := \{A\pi + \pi : \pi \in \Spi\}$ be its graph line and
\[
P(A) \;:=\; (A\pi_1 + \pi_1)\wedge(A\pi_2 + \pi_2) \;\in\; \Lambda^2\CS
\]
its Pl\"ucker bivector, normalised by $P(0) = N_0$. Then:
\begin{enumerate}
\item \emph{(Expansion.)} $P(A) = N_0 + \varphi(A) + (\det A)\, N_\infty$, where $\varphi(A) := A\pi_1\wedge\pi_2 + \pi_1\wedge A\pi_2$ lies in the mixed slot $\Som\wedge\Spi$ and $\det$ is taken in the chosen bases.
\item \emph{(The chart, term by term.)} $\varphi$ is a linear isomorphism onto the mixed slot $= \{\nO,\nInf\}^\perp \otimes \C$, and satisfies $Q(\varphi(A)) = -2\det A$. Writing $m(A) := \varphi(A)$ as a vector of $\{\nO,\nInf\}^\perp\otimes\C$, the Pl\"ucker bivector is exactly the completion's point embedding, complexified:
\[
P(A) \;=\; \nO \,+\, m(A)\,-\,\tfrac12\,Q(m(A))\,\nInf \;=\; X\bigl(m(A)\bigr).
\]
In particular every $P(A)$ is null, as a Pl\"ucker bivector must be, and the nullity of $P(A)$ is equivalent to the identity $\det A = -\tfrac12Q(m(A))$: the quadratic term of the chart is a determinant.
\item \emph{(Coverage.)} $A \mapsto L_A$ is a bijection from $\operatorname{Hom}(\Spi, \Som)$ onto the lines of $\PCS$ skew to $L_\infty$, and $[P(A)]$ ranges exactly over the points of the Klein quadric with $\ip{P}{\nInf} \neq 0$: the affine chart of the complexified conformal compactification, with the lines meeting $L_\infty$ as the points at infinity; the real locus is cut out in Proposition \claimref{correspondence.reality-conjugation-twistor-form-factor}(5).
\item \emph{(Consequences.)} (i) The null pair adjoined by the Witt completion is the pair of skew lines $(L_\infty, L_0)$ (Proposition \claimref{correspondence.skew-lines-splittings-hyperbolic-planes-one}). (ii) The splitting of a conformal spinor (a twistor) into its $(\omega, \pi)$ parts along $\CS = \Som\oplus\Spi$ is the Witt completion seen at spinor level: the same datum in a third language. (iii) The incidence relation (Penrose's $\omega = ix\pi$; in the real algebra $\omega = \tfrac12 x\,\nInf\,\pi$, real-linear in $x$) is the case $A = I_6\hat x$ of the chart map, with $I_6$ the complex unit of $\CS$ (a factor of $i$: with $I_6 = e_0e_1e_2e_3e_4e_5$, $I_6$ acts as $-i$ on $\CS$) and $\hat x$ Hermitian for the invariant Hermitian form $\Sigma$ (the twistor form) of Proposition \claimref{correspondence.reality-conjugation-twistor-form-factor}(5)). (iv) The stabiliser of the infinity line $L_\infty$ in $\mathfrak{so}(V_\C)$ is the stabiliser of the ray of $\nInf$: the Poincar\'e parabolic, with its Levi factor acting on $\Som \oplus \Spi$ as the two chiral $2$-dimensional representations, one plane the doublet of each $\mathfrak{sl}(2,\C)$ factor of the complexified Lorentz algebra and trivial for the other (Lemma \claimref{correspondence.chiral-planes-summand-spaces}(1)).
\end{enumerate}

## technical
Fix bases with $\pi_1\wedge\pi_2 = N_0$ in $\Spi$ and $e_1\wedge e_2 = N_\infty$ in $\Som$. For a linear map $A: \Spi\to\Som$ the graph line $L_A$ has Pl\"ucker bivector $P(A) = (A\pi_1 + \pi_1)\wedge(A\pi_2 + \pi_2)$, which expands as $P(A) = N_0 + \varphi(A) + (\det A)\,N_\infty$ with $\varphi(A)$ in the mixed slot $\Som\wedge\Spi$. The map $\varphi$ is a linear isomorphism onto $\{\nO,\nInf\}^\perp\otimes\C$ with $Q(\varphi(A)) = -2\det A$, so writing $m(A) = \varphi(A)$ one gets $P(A) = \nO + m(A) - \tfrac12 Q(m(A))\,\nInf = X(m(A))$: the Pl\"ucker bivector is exactly the completion's point embedding, complexified, and its nullity is the identity $\det A = -\tfrac12 Q(m(A))$.

The map $A \mapsto L_A$ is a bijection onto the lines of $\PCS$ skew to $L_\infty$, and $[P(A)]$ ranges exactly over the points of the Klein quadric with $\ip{P}{\nInf} \neq 0$, the affine chart of the complexified conformal compactification. Consequently the adjoined null pair is the pair of skew lines $(L_\infty, L_0)$, the splitting of a conformal spinor into $(\omega, \pi)$ is the Witt completion at spinor level, the incidence relation (Penrose's $\omega = ix\pi$, in the real algebra $\omega = \tfrac12 x\,\nInf\,\pi$) is the chart map at $A = I_6\hat x$ with $I_6$ the complex unit of $\CS$ and $\hat x$ Hermitian for the invariant form $\Sigma$, and the stabiliser of $L_\infty$ is the Poincar\'e parabolic, whose Levi factor acts on $\Som$ and $\Spi$ as the two chiral doublets.

## lay
Penrose described a spacetime point by a line in a three-dimensional complex projective space, through his incidence relation. This theorem shows that, written out term by term, the coordinates of that line are exactly the null vector by which the completed algebra represents the point, so the incidence relation is the completion's coordinate chart. The quadratic term of the chart is a determinant, the lines meeting a fixed line at infinity are the points at infinity, and the symmetries fixing that line are those of flat spacetime.

## one-liner
The Pl\"ucker bivector of the incidence line of a map $A$ is exactly the completion's null point embedding $X(m(A))$, so Penrose's incidence relation is the completion's affine chart, with a determinant as its quadratic term.
