---
id: note.mass.what-nullity-fixes
kind: note
version: 3
title: What nullity fixes
status: remark
subject: dark-energy
proposed_by:
  kind: extraction
  session: notes-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T11, deposited version
comments_on:
- mass.de-sitter-scale-frozen-point
- mass.imported-flat-model-twistor-chart-infinity
- mass.chart-form-spin-isomorphism
- mass.grip-real
locators:
  paper: T11
  number: Rem 5.2
  label: rem:nullity
  line: 622
extraction:
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  i4_conversion:
    by: ai-i4-pass
    date: 2026-10-21
    converted: []
    kept:
    - 'the factor i of the incidence relation and the Pauli-matrix chart x^{aa''}: the twistor''s unit I6 and complex matrices, not the field''s unit'
  source_title: 'What nullity fixes'
  source_formal: |-
    With the undetermined slot coefficient $X_{c}(x) = n_{0} + x + c\,Q(x)\,n_{\infty}$ one has $\ip{X_{c}}{X_{c}} = Q(x)(1 + 2c)$, so nullity of the point embedding for all $x$ fixes $c = -\tfrac12$. This is a statement about the coefficient, not about the chart's normalisation: rescaling the volume form $\varepsilon$ by $\kappa$ rescales $\ip{n_{0}}{n_{\infty}}$, $\ip{x}{x}$ and $\ip{X_{c}}{X_{c}}$ alike, and nullity is insensitive to $\kappa$. What fixes the chart is the imported normalisation $\ip{n_{0}}{n_{\infty}} = +1$ together with $Q = \ip{x}{x}$ (Fact \claimref{mass.imported-flat-model-twistor-chart-infinity}); on the $x$-slot this reads $\ip{x}{y} = -\varepsilon_{ab}\varepsilon_{a'b'}x^{aa'}y^{bb'}$, so $Q(x) = -2\det(x^{aa'})$. The real points of the $x$-slot are, by definition, the $x$ whose translation generator $A(x\wedge n_{\infty})$ lies in $\mathfrak{su}(2,2)$ for the Hermitian form \eqref{eq:hermitian} fixed below; by Lemma \claimref{mass.chart-form-spin-isomorphism}(2) that generator's block is $b_{x} = x\varepsilon$, and $x\varepsilon$ is anti-Hermitian iff $x = \tfrac{i}{\sqrt2}K\varepsilon$ with $K$ Hermitian (if $x = \tfrac{i}{\sqrt2}K\varepsilon$ then $x\varepsilon = -\tfrac{i}{\sqrt2}K$; conversely $K := i\sqrt2\,x\varepsilon$ is Hermitian when $x\varepsilon$ is anti-Hermitian, and $x = -\tfrac{i}{\sqrt2}K\varepsilon^{-1} = \tfrac{i}{\sqrt2}K\varepsilon$). So the real points are the matrices
    \begin{equation}
    x^{aa'} = \frac{i}{\sqrt2}\,K\varepsilon, \qquad K = \begin{pmatrix} x^{0}+x^{3} & x^{1}-ix^{2} \\ x^{1}+ix^{2} & x^{0}-x^{3}\end{pmatrix},\quad \varepsilon = \begin{pmatrix} 0 & 1 \\ -1 & 0\end{pmatrix},
    \end{equation}
    with $(x^{0}, x^{1}, x^{2}, x^{3})$ real, on which $Q = -2\det x = \det K = (x^{0})^{2} - (x^{1})^{2} - (x^{2})^{2} - (x^{3})^{2}$; the factor $i$ is that of the incidence relation, and the factor $\varepsilon$ is what makes the translation generators of Lemma \claimref{mass.chart-form-spin-isomorphism} anti-Hermitian for \eqref{eq:hermitian} (Lemma \claimref{mass.grip-real}). The twistor paper's reality structure \cite[Prop.~4.5]{ButlerT9} selects the same slice up to a choice of frame in $\Sc'$, which changes no formula of this section: the computations below are polynomial identities in the chart. The script checks these statements with the slice scaled by $\sqrt2$ (so that $Q = 2\det K$ there), the normalisation $1/\sqrt2$ being a real scalar that affects no reality statement; it also confirms that the anti-Hermiticity condition on the eight real parameters of $x$ has rank four, so that the slice is all of the real locus.
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: 'Kept the explicit complex $2 \times 2$ matrices of the real slice, which are a computation in the chart''s frame; added the GA readings that the Hermitian form is the reversion form on $\CS$ and the incidence factor $i$ is $I_6$ (TWGA E1.7), and called T9 the correspondence paper.'
---

## formal
With the undetermined slot coefficient $X_{c}(x) = n_{0} + x + c\,Q(x)\,n_{\infty}$ one has $Q(X_{c}) = Q(x)(1 + 2c)$, so nullity of the point embedding for all $x$ fixes $c = -\tfrac12$. This is a statement about the coefficient, not about the chart's normalisation: rescaling the volume form $\varepsilon$ by $\kappa$ rescales $\ip{n_{0}}{n_{\infty}}$, $Q(x)$ and $Q(X_{c})$ alike, and nullity is insensitive to $\kappa$. What fixes the chart is the imported normalisation $\ip{n_{0}}{n_{\infty}} = +1$ together with $Q = Q(x)$ (Fact \claimref{mass.imported-flat-model-twistor-chart-infinity}); on the $x$-slot this reads $\ip{x}{y} = -\varepsilon_{ab}\varepsilon_{a'b'}x^{aa'}y^{bb'}$, so $Q(x) = -2\det(x^{aa'})$. The real points of the $x$-slot are, by definition, the $x$ whose translation generator $A(x\wedge n_{\infty})$ lies in $\mathfrak{su}(2,2)$ for the Hermitian form \eqref{eq:hermitian} fixed below (the reversion form $h$ on the conformal spinor space $\CS$, written in the chart's frame); by Lemma \claimref{mass.chart-form-spin-isomorphism}(2) that generator's block is $b_{x} = x\varepsilon$, and $x\varepsilon$ is anti-Hermitian iff $x = \tfrac{i}{\sqrt2}K\varepsilon$ with $K$ Hermitian (if $x = \tfrac{i}{\sqrt2}K\varepsilon$ then $x\varepsilon = -\tfrac{i}{\sqrt2}K$; conversely $K := i\sqrt2\,x\varepsilon$ is Hermitian when $x\varepsilon$ is anti-Hermitian, and $x = -\tfrac{i}{\sqrt2}K\varepsilon^{-1} = \tfrac{i}{\sqrt2}K\varepsilon$). So the real points are the matrices
\begin{equation}
x^{aa'} = \frac{i}{\sqrt2}\,K\varepsilon, \qquad K = \begin{pmatrix} x^{0}+x^{3} & x^{1}-ix^{2} \\ x^{1}+ix^{2} & x^{0}-x^{3}\end{pmatrix},\quad \varepsilon = \begin{pmatrix} 0 & 1 \\ -1 & 0\end{pmatrix},
\end{equation}
with $(x^{0}, x^{1}, x^{2}, x^{3})$ real, on which $Q = -2\det x = \det K = (x^{0})^{2} - (x^{1})^{2} - (x^{2})^{2} - (x^{3})^{2}$; the factor $i$ is that of the incidence relation (in geometric algebra the conformal pseudoscalar $I_6$, the complex unit of $\CS$, so that $x^{aa'}$ is $H_x$ up to that unit and the normalisation), and the factor $\varepsilon$ is what makes the translation generators of Lemma \claimref{mass.chart-form-spin-isomorphism} anti-Hermitian for \eqref{eq:hermitian} (Lemma \claimref{mass.grip-real}). The correspondence paper's reality structure \cite[Prop.~4.5]{ButlerT9} selects the same slice up to a choice of frame in $\Sc'$, which changes no formula of this section: the computations below are polynomial identities in the chart. The script checks these statements with the slice scaled by $\sqrt2$ (so that $Q = 2\det K$ there), the normalisation $1/\sqrt2$ being a real scalar that affects no reality statement; it also confirms that the anti-Hermiticity condition on the eight real parameters of $x$ has rank four, so that the slice is all of the real locus.

## technical
pending

## lay
pending

## one-liner
pending
