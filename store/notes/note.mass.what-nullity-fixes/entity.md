---
id: note.mass.what-nullity-fixes
kind: note
version: 5
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
- name: Claude Opus 5.5
  role: notation pass, every imaginary unit resolved as a geometric-algebra pseudoscalar (unit principle)
  version: 4
  source: maintainer pass 2026-11-07 (resolve units)
- name: Claude Opus 5.5
  role: 'GA rewrite (declared: chart-frame matrix computation)'
  version: 5
  source: maintainer pass 2026-11-07 (consistency)
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
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 4 -> 5. Not rewritten: the remark computes the real slice of the x-slot with explicit 2 x 2 matrices in the chart''s frame (K Hermitian with entries in span{1, I_6}, epsilon, the translation block x epsilon anti-Hermitian, Q = -2 det x = det K), a statement about those matrices as such, and it already gives the GA readings (the Hermitian form is the reversion form on CS, the incidence factor is I_6); declared outside_ga (bridge). No text changed.'
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Unit principle, conformal spinors'' unit: the i of the real slice (the factor i/sqrt 2 of x = (i/sqrt 2) K epsilon and the entries x^1 -+ i x^2 of K) is written I_6, the complex unit of the conformal spinor space acting by right multiplication, which the note already named as the GA reading of that i; the chart''s matrices have entries in span{1, I_6} and Hermitian conjugation is taken over it. No bare i remains in the levels, so the outside_ga declaration (bridge, for i only) is removed; the existing source_formal is kept.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: the i of the real slice stands inside the explicit complex 2 x 2 matrices of the chart''s frame (i/sqrt 2 times K epsilon, the entries of K), whose GA reading as I_6 the note already gives; a matrix computation over C placed beside its GA reading, declared as a bridge (version and levels unchanged).'
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
outside_ga:
  kind: bridge
  why: 'the remark computes the real slice of the x-slot with explicit 2 x 2 matrices in the chart frame (K Hermitian with entries in span{1, I_6}, x epsilon anti-Hermitian, Q = -2 det x = det K), a statement about those matrices as such placed beside its GA reading (the reversion form on the conformal spinors, the unit I_6)'
---

## formal
With the undetermined slot coefficient $X_{c}(x) = n_{0} + x + c\,Q(x)\,n_{\infty}$ one has $Q(X_{c}) = Q(x)(1 + 2c)$, so nullity of the point embedding for all $x$ fixes $c = -\tfrac12$. This is a statement about the coefficient, not about the chart's normalisation: rescaling the volume form $\varepsilon$ by $\kappa$ rescales $\ip{n_{0}}{n_{\infty}}$, $Q(x)$ and $Q(X_{c})$ alike, and nullity is insensitive to $\kappa$. What fixes the chart is the imported normalisation $\ip{n_{0}}{n_{\infty}} = +1$ together with $Q = Q(x)$ (Fact \claimref{mass.imported-flat-model-twistor-chart-infinity}); on the $x$-slot this reads $\ip{x}{y} = -\varepsilon_{ab}\varepsilon_{a'b'}x^{aa'}y^{bb'}$, so $Q(x) = -2\det(x^{aa'})$. The real points of the $x$-slot are, by definition, the $x$ whose translation generator $A(x\wedge n_{\infty})$ lies in $\mathfrak{su}(2,2)$ for the Hermitian form \eqref{eq:hermitian} fixed below (the reversion form $h$ on the conformal spinor space $\CS$, written in the chart's frame); by Lemma \claimref{mass.chart-form-spin-isomorphism}(2) that generator's block is $b_{x} = x\varepsilon$, and, with matrices in the chart's frame having entries in $\mathrm{span}\{1, I_6\}$, $I_6$ the complex unit of $\CS$ (acting by right multiplication, conventions) and Hermitian conjugation taken over it, $x\varepsilon$ is anti-Hermitian iff $x = \tfrac{I_6}{\sqrt2}K\varepsilon$ with $K$ Hermitian (if $x = \tfrac{I_6}{\sqrt2}K\varepsilon$ then $x\varepsilon = -\tfrac{I_6}{\sqrt2}K$; conversely $K := I_6\sqrt2\,x\varepsilon$ is Hermitian when $x\varepsilon$ is anti-Hermitian, and $x = -\tfrac{I_6}{\sqrt2}K\varepsilon^{-1} = \tfrac{I_6}{\sqrt2}K\varepsilon$). So the real points are the matrices
\begin{equation}
x^{aa'} = \frac{I_6}{\sqrt2}\,K\varepsilon, \qquad K = \begin{pmatrix} x^{0}+x^{3} & x^{1}-I_6x^{2} \\ x^{1}+I_6x^{2} & x^{0}-x^{3}\end{pmatrix},\quad \varepsilon = \begin{pmatrix} 0 & 1 \\ -1 & 0\end{pmatrix},
\end{equation}
with $(x^{0}, x^{1}, x^{2}, x^{3})$ real, on which $Q = -2\det x = \det K = (x^{0})^{2} - (x^{1})^{2} - (x^{2})^{2} - (x^{3})^{2}$; the factor $I_6$ is that of the incidence relation (the conformal pseudoscalar, the complex unit of $\CS$, so that $x^{aa'}$ is $H_x$ up to that unit and the normalisation), and the factor $\varepsilon$ is what makes the translation generators of Lemma \claimref{mass.chart-form-spin-isomorphism} anti-Hermitian for \eqref{eq:hermitian} (Lemma \claimref{mass.grip-real}). The correspondence paper's reality structure \cite[Prop.~4.5]{ButlerT9} selects the same slice up to a choice of frame in $\Sc'$, which changes no formula of this section: the computations below are polynomial identities in the chart. The script checks these statements with the slice scaled by $\sqrt2$ (so that $Q = 2\det K$ there), the normalisation $1/\sqrt2$ being a real scalar that affects no reality statement; it also confirms that the anti-Hermiticity condition on the eight real parameters of $x$ has rank four, so that the slice is all of the real locus.

## technical
pending

## lay
pending

## one-liner
pending
