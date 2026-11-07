---
id: note.mass.setting-machine-verification
kind: note
version: 3
title: Machine verification
status: setting
subject: einstein
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T11, deposited version
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
comments_on:
- mass.imported-frozen-point-tractor-connection
- mass.imported-thomas-operator
- mass.weight-polynomial-two-series
- mass.de-sitter-scale-frozen-point
locators:
  paper: T11
  number: Setting
  section: Machine verification
  line: 850
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'By the unit principle (U3) the chart on Lambda^2 C^4 is written on Lambda^2 S^+, the exterior square of twistor space, which is the complexified conformal vector space with the central unit I_7 of Cl(3,4) (std-algebra.complexification-is-the-odd-extension); the weight keeps I_4; the two units are kept distinct and the note says which acts where; the outside_ga declaration is removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The complex weight -3/2 +- i nu is now -3/2 +- I_4 nu, read in span{1, I_4} (the script''s Gaussian rationals standing for Q(I_4)); the chart on Lambda^2 C^4, the exterior square of twistor space, stays complex: it is the complexified conformal vector space, whose unit must commute with vectors.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
---

## formal
Every computational identity asserted in this paper has been verified in exact arithmetic by the script \texttt{verify\_T11.py} \cite{ButlerVerifyT11}, which imports the series' shared library \texttt{GA.py}: exact rationals and Gaussian rationals, exact rank, rational functions in a formal variable, and exact truncated power series. No floating point is used anywhere; thirty-nine checks, all passing, organised in five parts keyed to statement tags.

\emph{Part A: the dictionary.} The pairing $I \cdot D\sigma$ is formed slot by slot from Facts \claimref{mass.imported-frozen-point-tractor-connection} and \claimref{mass.imported-thomas-operator}, with $\sigma$ and $\Box\sigma$ as formal coordinates, and $m^{2}$ is read off the resulting Klein-Gordon equation: $m^{2} = -w(w+n-1)Q(I)$ on a $144$-point rational grid in $(w, n, J)$, with a separate check that the opposite sign fails at every grid point where $m^{2} \neq 0$; in $n = 4$, $Q(I) = \Lambda/3$, $\rho_{I} = \Lambda/6$ and $m^{2} = -w(w+3)\Lambda/3$ as rational-function identities in a formal $\Lambda$. Corollary \claimref{mass.weight-polynomial-two-series}: the conformally coupled scalar's $m^{2} = 2\Lambda/3$ from the pairing; the massless weights $w = 0$ and $w = 1-n$, and no others among four further test values; the shadow symmetry $m^{2}(w) = m^{2}(1-n-w)$ and the closed form $\tfrac{n(n-2)}{4}Q(I)$ at $w = 1 - n/2$ for four values of $n$; the completed square $-w(w+3) = \tfrac94 - (w+\tfrac32)^{2}$ as a polynomial identity, with $m^{2} \ge 0$ at six real weights inside $[-3,0]$ and $m^{2} < 0$ at six outside; and $w = -\tfrac32 \pm I_4\nu$ (numbers read in $\mathrm{span}\{1, I_4\}$, the Gaussian rationals standing for $\mathbb{Q}(I_4)$) solving the dictionary in exact Gaussian rationals.

\emph{Part B: the area.} On exact Gaussian-rational spinor instances: a single twistor's momentum is null; $p^{2} = 2|\br{\pi^{1}\pi^{2}}|^{2}$ on all ten pairs with the imaginary part identically zero; aligned spinors give a null composite.

\emph{Part C: the chart and the de Sitter scale.} The chart on $\Lambda^{2}\CS$, the exterior square of twistor space, which is the complexified conformal vector space; its unit commutes with every conformal vector and is the central pseudoscalar $I_7$ of the odd extension $\Cl(3,4)$ (\claimref{std-algebra.complexification-is-the-odd-extension}), not the $I_4$ of the weight in Part A: $\ip{n_{0}}{n_{\infty}} = +1$ with both null; $Q(x) = -2\det x$ and the orthogonality of the slots; $Q(X_{c}) = Q(1+2c)$ with $c$ undetermined (Remark \claimref{note.mass.what-nullity-fixes}). Lemma \claimref{mass.de-sitter-scale-frozen-point}: every slot of the flat tractor connection on $(\sigma, \nabla\sigma, -\tfrac14\Box\sigma)$ vanishes and the norm is $\Lambda/3$, as rational-function identities in $\Lambda$ at rational points; $\ip{X(x)}{n_{\infty} + \lambda n_{0}} = 1 - \lambda Q/2$ at rational points and three values of $\lambda$, with the inverted order giving $\lambda - Q/2$, and the six point embeddings of the uniqueness argument of exact rank six; the ambient pairing of $n_{\infty} + \lambda n_{0}$ with itself formed and equal to $2\lambda$ at four values, with $2\lambda = \Lambda/3$, and the vector null, hence simple by Fact \claimref{mass.imported-flat-model-twistor-chart-infinity}, exactly at $\lambda = 0$. Theorem \claimref{mass.exact-join}(1) and (4): both blocks of the deformed bracket on all ten twistor pairs, the assembled $B_{\Lambda}$ at $\Lambda = 3$, the point-supported factor $\sigma(x)$ at two points and two values of $\Lambda$, and the wedge identity $Z^{1}\wedge Z^{2} = \br{\pi^{1}\pi^{2}}X(x)$ for twistors built on the incidence line $\mu_{x}\pi + \pi$, at four points and two spinor pairs.

\emph{Part D: the grip theorem.} The spin isomorphism is solved exactly: for each rotation $R_{U\wedge V}$ the construction needs, the script finds the traceless $A$ whose action on every basis bivector equals that of the rotation. The nine rotations whose matrices Lemma \claimref{mass.chart-form-spin-isomorphism} displays (the grading, four translations, four special conformal generators) are compared with these solutions entry by entry. The moment map \eqref{eq:moment} and the grip of Definition \claimref{obj.mass.grip-mass-composite} are then built from these solutions, on ten twistor pairs: at $\Lambda = 0$, $Q(P) = 2|\br{\pi^{1}\pi^{2}}|^{2}$ and $P \perp n_{\infty}$; the grip on $n_{0}$, $M(n_{0})$, has squared length $2|[\omega^{1}\omega^{2}]|^{2}$; the cross term $\ip{P_{\infty}}{P_{0}}$ equals $p\cdot k - d^{2}$ with the three forms in the components of the proof, $\det t = \overline{\br{\pi^{1}\pi^{2}}}[\omega^{1}\omega^{2}]$, and equals $2\,\mathrm{Re}(\br{\pi^{1}\pi^{2}}\overline{[\omega^{1}\omega^{2}]}) + C$; and the theorem itself, $Q(P) = 2|B_{\Lambda}|^{2} + 2\lambda C$, as an identity in $\lambda$ (all three coefficients of the quadratic), with $m^{2}$ real, $P \perp I_{\Lambda}$, and $P_{\Lambda} = P_{\infty} + \lambda P_{0}$ recomputed independently at three values of $\lambda$. The identities for $C$ in \eqref{eq:gram} and its nonnegativity. Lemma \claimref{mass.grip-real}: on four real points of the slice \eqref{eq:realslice}, every generator of a real pair (grading, translations, special conformal, Lorentz) has $\Sigma A$ anti-Hermitian, the commutator identity of the proof holds on all sixteen pairs of points, and the grip on $I_{\Lambda}$ has real pairing with $n_{\infty}$, $n_{0}$ and the four real vectors on all ten pairs, and the anti-Hermiticity condition on the eight real parameters of $x$ has rank four (Remark \claimref{note.mass.what-nullity-fixes}). The doubled composite's $m^{2} = 2\lambda(\bar{Z}\cdot Z)^{2}$ on all five twistors and the non-doubled massless pair of Theorem \claimref{mass.exact-join}(5). Proposition \claimref{mass.casimir-form-join}: both Casimirs formed from the exact moment components in adapted bases, the decomposition (1), the value (2) and the closed form (3) on four pairs, and $\tr\mathsf{E}^{2} = 1$ on the grading element. Lemma \claimref{mass.five-broken-generators}: the dimensions $10$, $6$, $5$ by exact rank, and the five matrices $A(e_{a}\wedge I_{\Lambda})$ traceless, independent, with $\Omega A$ antisymmetric.

\emph{Part E: the weight.} $\nu^{2} = 6|B_{\Lambda}|^{2}/\Lambda + C - \tfrac94$ on three pairs at two values of $\Lambda$, real and positive there; the expansion $\sqrt{1 - \tfrac94\epsilon^{2}} = 1 - \tfrac98\epsilon^{2} - \tfrac{81}{128}\epsilon^{4} + \cdots$, $\epsilon = H/m$, as an exact truncated power series.

What the script does not check: the conformal invariance of the Thomas operator (imported, Fact \claimref{mass.imported-thomas-operator}); the flat-model dictionary and the spin isomorphism as theorems (imported, Fact \claimref{mass.imported-flat-model-twistor-chart-infinity}; the script solves the isomorphism on the basis but does not prove it is one); Schur's lemma behind Lemma \claimref{mass.invariant-forms-simple-lie-algebra} (imported); the de Sitter classification against which Corollary \claimref{mass.weight-polynomial-two-series} is read (imported, Fact \claimref{mass.imported-unitary-representations-de-sitter-group}); the ``only if'' of the massless locus in Theorem \claimref{mass.exact-join}(5), which is the positivity argument of the proof; the normalisation $1/\sqrt2$ of the real slice \eqref{eq:realslice}, which the script carries as a scalar; the identification of the real form in Lemma \claimref{mass.five-broken-generators} (that the stabiliser is $\mathfrak{so}(1,4)$, that the five are the de Sitter translations, and the match with the action paper's Goldstone count), the script working over the Gaussian rationals, with no real-form check beyond the anti-Hermiticity checks of Lemma \claimref{mass.grip-real}; the $N$-constituent formulas of successor problem (5); and Proposition \claimref{mass.casimir-form-join}(2) beyond $N = 2$.

## technical
pending

## lay
pending

## one-liner
pending
