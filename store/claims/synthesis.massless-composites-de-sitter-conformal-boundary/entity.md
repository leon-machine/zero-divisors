---
id: synthesis.massless-composites-de-sitter-conformal-boundary
kind: claim
version: 2
title: Massless composites sit on the conformal boundary of de Sitter space, and the condensation source vanishes at those with zero flat bracket
status: proved
region: synthesis
subject: mass
tags: [frozen-point, conformal-spinors]
proposed_by:
  kind: ai
  session: 2026-10-22-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
derivations:
- name: main
  uses:
  - mass.exact-join@7
  - mass.de-sitter-scale-frozen-point@6
  - families.source-term-linear-tilt-mass-functional@4
  - synthesis.many-twistor-join@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_massless_composites
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - mass.exact-join
  - synthesis.operator-join-ordering-constants
  - families.bracket-fixed-join
extraction:
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 1 -> 2.'
  open_problem: op.operator-join
  note: 'Settles the classical half of successor problem (4) of the mass paper: whether the condensation seed is supported on the massless locus. The ordering constants were computed earlier (synthesis.operator-join-ordering-constants) and contain no term linear in the bracket; this result locates the massless locus geometrically and evaluates the source term on it. The identification of totally null twistor planes with real points of Minkowski space is classical twistor geometry (Penrose; cited from memory, not used: the proof works with the anti-Hermitian condition directly). Transport-convenient: the frozen point I_Lambda and its scale function sigma are the series objects; the rest is the chart algebra of the exact join. Massless here is the classical grip; on the locus h = 0, so the conformal Casimir C_2 of the composite vanishes and the grip and the de Sitter mass agree there. The bound r <= 2 for massless spans also appears in the three-twistor result filed alongside (synthesis.three-twistor-composites-massive), which (4) here refines into the classification of the massless planes. Not addressed: the quantum massless locus (the spectrum of the operator join on positive-energy modules).'
---

## formal
Let $\Lambda > 0$, $\lambda = \Lambda/6$, and let $Z^{1}, Z^{2}$ be conformal spinors with $Z^{1}\wedge Z^{2} \neq 0$, $b = \br{\pi^{1}\pi^{2}}$ the flat bracket, $\Omega_{\omega} = [\omega^{1}\omega^{2}]$, $h$ the Gram matrix and $m^{2} = 2|B_{\Lambda}|^{2} + \tfrac{\Lambda}{3}C$ the squared grip of Theorem \claimref{mass.exact-join}.
\begin{enumerate}
\item[(1)] If $b \neq 0$ there is a unique $\mu: \Spi \to \Som$ with $\omega^{i} = \mu\pi^{i}$; then $h_{il} = \overline{\pi^{i}}\cdot(\mu + \mu^{\dagger})\pi^{l}$, $\Omega_{\omega} = \det(\mu)\, b$ and $B_{\Lambda} = (1 + \lambda\det\mu)\, b$. The span is the line $L_{x}$ of Theorem \claimref{mass.exact-join}(4) with $\det\mu = -\tfrac12 Q(x)$, so $1 + \lambda\det\mu = \sigma(x)$, the scale function of Lemma \claimref{mass.de-sitter-scale-frozen-point}. If $\mu + \mu^{\dagger} = 0$ (the line is totally null), then $h = 0$ and $m^{2} = 2\,\sigma(x)^{2}\,|b|^{2}$.
\item[(2)] The composite is massless if and only if either (a) $b \neq 0$, $\mu + \mu^{\dagger} = 0$ and $\sigma(x) = 0$: the line of a point on the hypersurface $\sigma = 0$ where the de Sitter metric $\sigma^{-2}\eta$ is not defined, its conformal boundary; or (b) $b = 0$ and the span is $\{(\omega, 0), (0, \pi)\}$ with $\overline{\omega}\cdot\pi = 0$. Both types are the totally null planes $X = Z^{1}\wedge Z^{2}$ with $\ip{I_{\Lambda}}{X} = 0$, the conformal boundary of the de Sitter region; type (b) is the two-sphere of that boundary at the chart's infinity, where $\ip{n_{\infty}}{X} = \ip{n_{0}}{X} = 0$. On the locus $h = 0$, so the conformal Casimir of the composite vanishes and the grip and the de Sitter mass agree. The span $\pi^{1} = \pi^{2} = 0$ is not massless: there $m^{2} = 2\lambda^{2}|\Omega_{\omega}|^{2} > 0$.
\item[(3)] On (a), $\Omega_{\omega} = -b/\lambda$, so the derivative in $b$ of the source term of Proposition \claimref{families.source-term-linear-tilt-mass-functional}, $\tfrac{2\Lambda}{3}\Omega_{\omega}$, equals $-4b$, and the source term itself equals $-4|b|^{2}$; on (b), $b = \Omega_{\omega} = 0$. Hence on the massless locus $b = 0$ if and only if $\Omega_{\omega} = 0$: the derivative of the source at $b = 0$ vanishes at every massless composite with $b = 0$, and massless composites carrying a nonzero source have $b \neq 0$ and lie on the boundary component (a). In this sense the condensation seed, the tilt at $b = 0$, is not supported on the massless locus.
\item[(4)] For $N$ constituents, the composite is massless if and only if all the $Z^{i}$ lie in one plane of type (a) or (b), or are multiples of one null conformal spinor.
\end{enumerate}

## technical
For two conformal spinors and a positive cosmological constant, a massless composite needs a zero Gram matrix and a zero deformed bracket. When the flat bracket $b$ is nonzero, the composite's plane is the line $L_{x}$ of a point, $\omega = \mu\pi$, and the zero Gram matrix says $\mu$ is anti-Hermitian, the condition that the line be totally null. On such a line the deformed bracket is the flat one times the de Sitter scale function, $B_{\Lambda} = \sigma(x)\,b$, and the squared grip is exactly $m^{2} = 2\sigma(x)^{2}|b|^{2}$: the flat mass multiplied by the conformal factor that turns the flat metric into de Sitter's. So the composite is massless exactly where $\sigma(x) = 0$, on the conformal boundary of the de Sitter chart. The remaining massless composites have $b = 0$ and form a sphere's worth of planes spanned by $(\omega, 0)$ and $(0, \pi)$ with $\overline{\omega}\cdot\pi = 0$: the part of the same boundary that lies at the chart's infinity, since in general massless means a totally null plane $X$ with $\ip{I_{\Lambda}}{X} = 0$. The plane $\pi = 0$ itself is massive for $\Lambda > 0$. On the whole locus the Gram matrix vanishes, so the grip and the de Sitter mass agree there.

On the boundary component, $\Omega_{\omega} = -(6/\Lambda)\,b$, so the source term of the families paper's condensation tilt equals $-4|b|^{2}$ and its derivative in $b$ equals $-4b$; on the sphere both brackets vanish. On the massless locus the flat bracket vanishes exactly where $\Omega_{\omega}$ does, so the tilt evaluated at $b = 0$ is zero at every massless composite that has $b = 0$; the massless composites that do carry a nonzero source have $b \neq 0$ and lie on the boundary component inside the chart. Together with the absence of bracket-linear ordering constants, this decides the successor question: the seed is neither on the massless locus nor in the ordering constants. With more constituents the massless ones all lie in one such plane, since a totally null subspace of $\CS$ has dimension at most two.

## lay
A composite of two of the framework's basic spinor objects can have zero mass in a universe with a positive cosmological constant only in a special position: the point of spacetime it represents must lie on the boundary at infinity of de Sitter space, where the de Sitter distance scale vanishes. Away from that boundary its mass is its flat-space mass multiplied by the same scale factor that turns flat spacetime into de Sitter spacetime. The term that, in the framework's account of how a condensate forms, tips the system away from zero is computed on these massless composites: it is never present at a massless composite whose flat-space mass is zero. So the condensate's starting push, evaluated where the flat-space mass is zero, does not come from the massless composites; the massless composites that do feel the push already have a nonzero flat-space mass and sit on the boundary.

## one-liner
For $\Lambda > 0$ a two-spinor composite with nonzero flat bracket is massless iff its line is a real point with $\sigma(x) = 0$, the conformal boundary of de Sitter space, where $m^{2} = 2\sigma^{2}|b|^{2}$ in general; the derivative of the condensation source at $b = 0$ vanishes at every massless composite with $b = 0$, and massless composites carrying a nonzero source have $b \neq 0$ and lie on that boundary.
