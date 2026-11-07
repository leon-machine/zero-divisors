---
id: mass.weight-polynomial-two-series
kind: claim
version: 6
title: The weight polynomial and the two series
status: proved
region: mass
subject: mass
tags: [representation-theory]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T11, deposited version
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 6
  source: maintainer pass 2026-11-07 (GA units)
review: typed
derivations:
- name: main
  uses:
  - mass.imported-unitary-representations-de-sitter-group@3
  - mass.mass-weight-dictionary@4
  proof: proof-main.tex
- name: standard-route
  uses:
  - mass.imported-unitary-representations-de-sitter-group@3
  proof: proof-standard-route.tex
checked_by:
- kind: legacy
  script: verify_T11.py
  tags:
  - label:cor:series
- kind: check
  ref: check.py::check_massless_pair_and_shadow_symmetry
- kind: check
  ref: check.py::check_conformally_coupled_weight
- kind: check
  ref: check.py::check_real_weights_complementary_series
- kind: check
  ref: check.py::check_principal_series_and_expansion
locators:
  paper: T11
  number: Cor 3.2
  label: cor:series
  line: 478
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The de Sitter weight -3/2 +- i nu, a physical number, is written -3/2 +- I_4 nu with numbers read in span{1, I_4}; the Gaussian rationals of the check are named Q(I_4); no bare i remains.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: roots 0 and -3 and the shadow symmetry as polynomial identities, n(n-2)/4 at w = 1 - n/2, the complementary-series window, and the principal-series expansion. Version 4 -> 5.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  i4_conversion:
    by: ai-i4-pass
    date: 2026-10-21
    converted: []
    kept:
    - 'the de Sitter weight -3/2 +- i nu (a complex number labelling a principal-series representation, not an operator unit)'
  env: corollary
  context_refs:
  - mass.imported-unitary-representations-de-sitter-group
  eqrefs: 1
  typing:
    by: ai-typing-pass
    added:
    - mass.mass-weight-dictionary
    - mass.imported-unitary-representations-de-sitter-group
    note: 'The corollary is the algebra of the dictionary''s formula and names its series by the de Sitter representation Fact, so both were added; the paper identifies the formula with the de Sitter mass formula, so a standard-route through that import was added, though item (2), the conformal coupling, is called classical with no imported claim in the store.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - mass.imported-unitary-representations-de-sitter-group
---

## formal
In $n = 4$, with $\Delta := -w$ and $H^{2} = \Lambda/3 > 0$, the dictionary reads $m^{2} = \Delta(3-\Delta)H^{2}$, the de Sitter mass formula of Fact \claimref{mass.imported-unitary-representations-de-sitter-group}, whose two series are named below by that Fact; what is proved here is the algebra of $-w(w+3)$:
\begin{enumerate}
\item $m = 0$ exactly for $w \in \{0, -3\}$, the shadow pair $w \leftrightarrow -3-w$ preserving $m^{2}$;
\item the conformally coupled scalar $w = 1 - n/2 = -1$ has $m^{2} = 2H^{2}$; in general dimension $w = 1 - n/2$ gives $m^{2} = \tfrac{n(n-2)}{4}Q(I)$;
\item for real $w$, $m^{2} = \bigl[\tfrac94 - (w + \tfrac32)^{2}\bigr]H^{2} \le \tfrac94 H^{2}$, with equality at $w = -\tfrac32$; $m^{2} \ge 0$ exactly for $w \in [-3, 0]$, where $m$ runs over $[0, 3H/2]$, the complementary series $0 < m < 3H/2$ together with its two endpoints (the massless pair and the $\nu = 0$ member of the principal series); a real weight outside $[-3,0]$ gives $m^{2} < 0$, outside both series of Fact \claimref{mass.imported-unitary-representations-de-sitter-group} that this paper uses;
\item for $m > 3H/2$ the weight is complex,
\begin{equation}
w = -\frac32 \pm I_4\nu, \qquad \nu = \sqrt{\frac{m^{2}}{H^{2}} - \frac94}, \qquad \nu = \frac{m}{H} - \frac98\,\frac{H}{m} + O\!\Bigl(\frac{H^{3}}{m^{3}}\Bigr),
\end{equation}
the principal series (numbers are read in $\mathrm{span}\{1, I_4\}$): the real part is universal and the mass lies in the imaginary part.
\end{enumerate}

## technical
In four dimensions, with $\Delta = -w$ and $H^{2} = \Lambda/3 > 0$, the dictionary reads $m^{2} = \Delta(3-\Delta)H^{2}$, the de Sitter mass formula, and the result is the algebra of $-w(w+3)$. The mass vanishes exactly for $w \in \{0, -3\}$, a shadow pair under $w \leftrightarrow -3-w$; the conformally coupled weight $w = 1 - n/2$ gives $m^{2} = \tfrac{n(n-2)}{4}Q(I)$, which is $2H^{2}$ for $n = 4$.

For real $w$, $m^{2} = \bigl[\tfrac94 - (w + \tfrac32)^{2}\bigr]H^{2} \le \tfrac94 H^{2}$, nonnegative exactly for $w \in [-3, 0]$, the complementary series with its endpoints; a real weight outside that interval gives $m^{2} < 0$. For $m > 3H/2$ the weight is complex, $w = -\tfrac32 \pm I_4\nu$ (numbers are read in $\mathrm{span}\{1, I_4\}$) with $\nu = \sqrt{m^{2}/H^{2} - \tfrac94}$: the principal series, with universal real part.

## lay
The framework's mass rule turns one number, the weight, into a mass. This result maps out what the rule allows. Real weights only give masses up to a tiny threshold set by the expansion rate of the universe; anything heavier needs a complex weight, with a fixed real part and an imaginary part that carries the mass. These two regimes match the two standard families of particles in de Sitter space.

## one-liner
Under $m^{2} = -w(w+3)H^{2}$, real weights give $0 \le m \le 3H/2$ exactly on $[-3, 0]$, and $m > 3H/2$ needs $w = -\tfrac32 \pm I_4\nu$ (numbers are read in $\mathrm{span}\{1, I_4\}$), the principal series.
