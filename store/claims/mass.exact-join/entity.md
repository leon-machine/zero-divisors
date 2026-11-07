---
id: mass.exact-join
kind: claim
version: 8
title: The exact join
status: proved
region: mass
subject: mass
tags: [frozen-point, conformal-spinors]
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
  version: 8
  source: maintainer pass 2026-11-07 (GA units)
review: typed
about:
- obj.mass.grip-mass-composite
derivations:
- name: main
  uses:
  - correspondence.incidence-relation-chart@7
  - mass.chart-form-spin-isomorphism@6
  - mass.de-sitter-scale-frozen-point@6
  - mass.imported-flat-model-twistor-chart-infinity@7
  - mass.mass-symplectic-area-two-twistor-formula@3
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T11.py
  tags:
  - label:thm:grip
- kind: check
  ref: check.py::check_deformed_bracket_is_pairing_with_frozen_point
- kind: check
  ref: check.py::check_mass_is_grip_norm_identity_in_lambda
- kind: check
  ref: check.py::check_flat_shadow_is_symplectic_area
- kind: check
  ref: check.py::check_point_supported_composite
- kind: check
  ref: check.py::check_massless_locus
locators:
  paper: T11
  number: Thm 5.6
  label: thm:grip
  line: 706
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The chart''s complex unit, which the proof''s convention line already read as I_6 but wrote i, is now written I_6 in p(x), k(x), their components, the pairings and t_jj = r_j + I_6 s_j, numbers read in span{1, I_6}; no bare i remains.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: B_Lambda as the pairing with I_Lambda, m^2 = 2|B|^2 + Lambda C/3 from the grip as an identity in Lambda, the flat shadow, the point-supported composite and the massless locus. Version 5 -> 6. Check strengthened: massless-locus closed form matched to the grip norm, bounds m^2 >= 0 and det K <= 0 shown attained, line count pinned; samples moved to module level. Version 6 -> 7.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  maintainer_pass_2026_10_22:
    by: ai-maintainer-pass
    note: 'A6 follow-up: clause (5) multiple of the identity is zero (proved in synthesis.many-twistor-join (v)); formal and technical now say h = 0. The equivalence is unchanged.'
  i4_conversion:
    by: ai-i4-pass
    date: 2026-10-21
    converted: []
    kept:
    - 'the factors i in p(x), k(x) and their products: the chart''s complex unit, set to I6 by the earlier GA pass (twistor unit)'
    - 't_jj = r_j + i s_j: real and imaginary parts of a complex number'
  env: theorem
  unresolved_refs:
  - rem:nullity
  eqrefs: 5
  typing:
    by: ai-typing-pass
    added:
    - obj.mass.grip-mass-composite
    note: 'All five uses are cited in the proof and kept (the area formula for the flat-shadow clause); the grip definition was added under about, and the unresolved nullity remark is not a store entity.'
  source_title: 'The exact join'
  source_formal: |-
    Let $I_{\Lambda} = n_{\infty} + \lambda n_{0}$ with $\lambda = \Lambda/6$ be the frozen point of Lemma \claimref{mass.de-sitter-scale-frozen-point}, and $Z^{1}, Z^{2}$ two twistors.
    \begin{enumerate}
    \item \emph{(The deformed bracket.)} The pairing of the composite against the frozen point is
    \begin{equation}
    B_{\Lambda} := \ip{I_{\Lambda}}{Z^{1}\wedge Z^{2}} = \br{\pi^{1}\pi^{2}} + \frac{\Lambda}{6}\,[\omega^{1}\omega^{2}],
    \end{equation}
    and at $\Lambda = 0$ it is the classical contraction of the composite with the infinity twistor.
    \item \emph{(The mass.)} The grip $P = M(I_{\Lambda})$ has squared length
    \begin{equation}
    m^{2} = \ip{P}{P} = 2\,|B_{\Lambda}|^{2} + \ip{I_{\Lambda}}{I_{\Lambda}}\, C = 2\,|B_{\Lambda}|^{2} + \frac{\Lambda}{3}\, C .
    \end{equation}
    \item \emph{(The flat shadow.)} At $\Lambda = 0$, $m^{2} = 2|\ip{I}{Z^{1}\wedge Z^{2}}|^{2} = 2|\br{\pi^{1}\pi^{2}}|^{2}$: Proposition \claimref{mass.mass-symplectic-area-two-twistor-formula}, read as the squared pairing of the composite against the frozen point.
    \item \emph{(The point-supported composite.)} If both twistors lie on the incidence line of the point $x$, the composite bivector is $\br{\pi^{1}\pi^{2}}X(x)$ and $B_{\Lambda} = \sigma(x)\br{\pi^{1}\pi^{2}} = \bigl(1 - \tfrac{\Lambda Q(x)}{12}\bigr)\br{\pi^{1}\pi^{2}}$: the flat bracket read in the de Sitter scale.
    \item \emph{(The massless locus.)} For $\Lambda > 0$, $m^{2} \ge 0$, and $m^{2} = 0$ if and only if $B_{\Lambda} = 0$ and $h$ is a multiple of the identity. The doubled composite $Z^{2} = Z^{1}$ has $B_{\Lambda} = 0$ and $m^{2} = \tfrac{\Lambda}{3}\,(\bar{Z}\cdot Z)^{2}$, so it is massless only when its constituent is null; and there are massless composites that are not doubled, for instance $Z^{1} = e_{1} + e_{4}$, $Z^{2} = \alpha e_{1} + \beta e_{4}$ with $\alpha \neq \beta$.
    \end{enumerate}
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Formal, technical, lay and one-liner levels and the proof moved to conformal spinors in CS, with the incidence line as L_x and the infinity twistor as n_infinity; the proof''s chart halves \Sc, \Sc'' are written \Som, \Spi (\Sc renders as \CS does) and a convention line reads the chart''s i as I6. The component computation itself is kept as in the paper, in the chart''s I6-complex components.'
---

## formal
Let $I_{\Lambda} = n_{\infty} + \lambda n_{0}$ with $\lambda = \Lambda/6$ be the frozen point of Lemma \claimref{mass.de-sitter-scale-frozen-point}, and $Z^{1}, Z^{2} \in \CS$ two conformal spinors (twistors).
\begin{enumerate}
\item \emph{(The deformed bracket.)} The pairing of the composite against the frozen point is
\begin{equation}
B_{\Lambda} := \ip{I_{\Lambda}}{Z^{1}\wedge Z^{2}} = \br{\pi^{1}\pi^{2}} + \frac{\Lambda}{6}\,[\omega^{1}\omega^{2}],
\end{equation}
and at $\Lambda = 0$ it is the classical contraction of the composite with the point at infinity $n_{\infty}$, read as a bivector of $\CS$ (Penrose's infinity twistor).
\item \emph{(The mass.)} The grip $P = M(I_{\Lambda})$ has squared length
\begin{equation}
m^{2} = Q(P) = 2\,|B_{\Lambda}|^{2} + Q(I_{\Lambda})\, C = 2\,|B_{\Lambda}|^{2} + \frac{\Lambda}{3}\, C .
\end{equation}
\item \emph{(The flat shadow.)} At $\Lambda = 0$, $m^{2} = 2|\ip{I}{Z^{1}\wedge Z^{2}}|^{2} = 2|\br{\pi^{1}\pi^{2}}|^{2}$: Proposition \claimref{mass.mass-symplectic-area-two-twistor-formula}, read as the squared pairing of the composite against the frozen point.
\item \emph{(The point-supported composite.)} If both spinors lie on the line $L_{x}$ of the point $x$, the composite bivector is $\br{\pi^{1}\pi^{2}}X(x)$ and $B_{\Lambda} = \sigma(x)\br{\pi^{1}\pi^{2}} = \bigl(1 - \tfrac{\Lambda Q(x)}{12}\bigr)\br{\pi^{1}\pi^{2}}$: the flat bracket read in the de Sitter scale.
\item \emph{(The massless locus.)} For $\Lambda > 0$, $m^{2} \ge 0$, and $m^{2} = 0$ if and only if $B_{\Lambda} = 0$ and $h$ is a multiple of the identity; that multiple is zero, so the condition is $B_{\Lambda} = 0$ and $h = 0$ (\claimref{synthesis.many-twistor-join}(v)). The doubled composite $Z^{2} = Z^{1}$ has $B_{\Lambda} = 0$ and $m^{2} = \tfrac{\Lambda}{3}\,(\bar{Z}\cdot Z)^{2}$, so it is massless only when its constituent is null; and there are massless composites that are not doubled, for instance $Z^{1} = e_{1} + e_{4}$, $Z^{2} = \alpha e_{1} + \beta e_{4}$ with $\alpha \neq \beta$.
\end{enumerate}

## technical
With the frozen point $I_{\Lambda} = n_{\infty} + \tfrac{\Lambda}{6}n_{0}$ and two conformal spinors $Z^{1}, Z^{2} \in \CS$, the pairing of the composite against the frozen point is the deformed bracket $B_{\Lambda} = \ip{I_{\Lambda}}{Z^{1}\wedge Z^{2}} = \br{\pi^{1}\pi^{2}} + \tfrac{\Lambda}{6}[\omega^{1}\omega^{2}]$. The grip $P = M(I_{\Lambda})$ has squared length $m^{2} = 2|B_{\Lambda}|^{2} + \tfrac{\Lambda}{3}C$, with $C$ the internal $\mathfrak{su}(2)$ Casimir of the Gram matrix $h$; at $\Lambda = 0$ this is the two-spinor area formula $m^{2} = 2|\br{\pi^{1}\pi^{2}}|^{2}$.

For two spinors on the line $L_{x}$ of a point $x$, $B_{\Lambda} = \bigl(1 - \Lambda Q(x)/12\bigr)\br{\pi^{1}\pi^{2}}$, the flat bracket read in the de Sitter scale. For $\Lambda > 0$, $m^{2} \ge 0$, with equality exactly when $B_{\Lambda} = 0$ and $h$ is a multiple of the identity, a multiple that is in fact zero ($h = 0$, proved in the many-constituent join); the doubled composite has $m^{2} = \tfrac{\Lambda}{3}(\bar{Z}\cdot Z)^{2}$, and there are massless composites that are not doubled.

## lay
The framework reads mass in two ways: from how a composite grips the one built-in cosmological scale, and from how misaligned its two constituents are. This theorem joins the two readings exactly. The mass squared is twice the squared size of a slightly deformed misalignment, plus a tiny correction, proportional to the cosmological constant, that depends on how the constituents overlap. Without a cosmological constant the familiar two-constituent area formula returns.

## one-liner
For two conformal spinors the grip on the frozen point has $m^{2} = 2|B_{\Lambda}|^{2} + \tfrac{\Lambda}{3}C$, with $B_{\Lambda} = \br{\pi^{1}\pi^{2}} + \tfrac{\Lambda}{6}[\omega^{1}\omega^{2}]$.
