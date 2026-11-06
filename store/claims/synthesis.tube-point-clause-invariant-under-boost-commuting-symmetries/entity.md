---
id: synthesis.tube-point-clause-invariant-under-boost-commuting-symmetries
kind: claim
version: 1
title: 'The tube-point clause: invariance under boost-commuting symmetries'
status: postulate
region: synthesis
subject: one-relation
tags: [conformal-spinors, frozen-point, horizons]
proposed_by:
  kind: ai
  session: maintainer-2026-10-31
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
lineage:
  motivated_by:
  - synthesis.de-sitter-field-fixes-the-observer-tube-point
  - synthesis.wick-rotated-boost-selects-observer-tube-point
  - synthesis.imported-de-sitter-invariant-hadamard-state-unique
extraction:
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: >-
      New costed clause, registered by Leon's decision of 2026-10-31 to adopt the selection rule argued in the
      reading of synthesis.de-sitter-field-fixes-the-observer-tube-point as a costed clause: taken as given, with
      its cost (the hypothesis gap from the de Sitter Hadamard uniqueness theorem to the series' CAR modes, and
      its reach, one-horizon fields only) and a refutation condition stated. It fixes rho^2 = 12/Lambda for
      Lambda > 0 and leaves rho free for Lambda <= 0. An assumes edge from the de Sitter tube-point result is
      added with it.
---

## formal
\emph{The tube-point clause (costed).} Let a state of the series' modes and a wedge with boost $K$ be given, with the compatible tube point $m = x_{\perp} + i\rho u$ over the wedge's bifurcation plane that the boost-KMS data and the ascent pair fix up to the scale $\rho$ (Theorem \claimref{synthesis.wick-rotated-boost-selects-observer-tube-point}). In a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) of which $K$ generates a symmetry, $m$ is invariant under every symmetry of the field that commutes with $K$, acting on tube points complex-linearly.

\emph{What it is for.} It is the selection rule of the reading of Theorem \claimref{synthesis.de-sitter-field-fixes-the-observer-tube-point}, adopted. In the de Sitter field ($\Lambda > 0$) the symmetries commuting with $K$ are $K$ and a transverse $\so(3)$, and the compatible tube points they fix are exactly one boost orbit, foot at the scale's centre and $\rho^{2} = 12/\Lambda$ (that theorem, (i) and (ii)); so the clause fixes $\rho$ there, and the frozen-point and surface-gravity candidates are one tube point when $\rho = 1/\kappa$ is read as the physical norm of the boost generator (in chart length $\rho_{\Lambda} = 2/\kappa$, the factor $2$ being the local scale $\sigma = 2$). In that field the condition is equivalent to the complexified Stelle-West vector $X(m)/\sigma(m) - \tfrac{3}{\Lambda}I_{\Lambda}$ being purely imaginary (that theorem, (vii)). For the pure-dilation fields with $\Lambda \le 0$ it fixes no tube point and $\rho$ stays free (that theorem, (vi)). It decides fields with one horizon only: in a static region bounded by two horizons it does not say which horizon's boost is the observer's, and the candidates separate there, as in the Schwarzschild-de Sitter field with lapse $f = 1 - 2M/r - \tfrac{\Lambda}{3}r^{2}$ at $\Lambda = M = \tfrac37$, horizons at $r = 1$ and $r = 2$ and $\kappa_{b}/\kappa_{c} = \tfrac85$; for the Schwarzschild field it is not computed. Where it decides, it ties the scale to $\Lambda$ and supplies no unit independent of it.

\emph{What it costs.} It is adopted, not derived from the series' structure. The argument for it runs through the uniqueness of the de Sitter-invariant Hadamard state of a massive scalar (Fact \claimref{synthesis.imported-de-sitter-invariant-hadamard-state-unique}): a state with the symmetry of the field, and a rule assigning tube points covariantly, return a point fixed by the field's symmetries commuting with the boost. The series' boundary modes are CAR fermions, outside that theorem's hypotheses, so the clause carries the hypothesis gap from that theorem to the series' modes. Fields with more than one horizon need a further premise assigning an observer's tube point to one horizon (per observer or per horizon).

\emph{Refutation condition.} The clause is false if any of the following is established: (a) a state of the series' modes on a horizon of the de Sitter field, satisfying the series' other premises, whose compatible tube point is not fixed by the transverse $\so(3)$, for example one whose data fix $\rho^{2} \neq 12/\Lambda$; (b) a derivation from the series' premises of a rule fixing $\rho$ that disagrees with the clause on a field with one horizon; (c) a proof that the series' horizon states on the de Sitter field are not invariant under the field's symmetries commuting with the boost.

## technical
A state of the series reads its capacities at a point of the complexified spacetime, its tube point, which the state's thermal data on a wedge fix up to one scale $\rho$. This clause fixes the scale by symmetry: the tube point must be left in place by every symmetry of the gravitational field that commutes with the wedge's boost. In the de Sitter field those symmetries are the boost and the rotations about the observer, and the only tube points they fix sit at $\rho^{2} = 12/\Lambda$, where the frozen-point and surface-gravity candidates agree as physical lengths. For a vanishing or negative cosmological constant nothing is fixed. The clause is a costed choice: its support is the uniqueness of the symmetric Hadamard state for a massive scalar, which the series' fermionic boundary modes do not satisfy as stated, and it says nothing about which horizon an observer between two horizons belongs to, as in Schwarzschild-de Sitter with surface gravities in the ratio $8/5$. It would be refuted by a series state on de Sitter whose tube point the rotations move, by a derived rule that disagrees with it, or by a proof that the series' horizon states lack the field's symmetry.

## lay
Each observer in this framework is attached to a point of a complexified copy of spacetime, and the framework's thermal data fix that point except for one length. This assumption fixes the length by symmetry: the point must not move under the symmetries of the gravitational field that leave the observer's horizon in place. In a universe with a positive cosmological constant that picks one length, the size set by the cosmological constant; with zero or negative cosmological constant it picks none, and with two horizons it cannot say which horizon counts. It is adopted with these limits stated, and could be overturned by a calculation or derivation that disagrees with it.

## one-liner
Costed clause: a state's tube point is invariant under the field's symmetries commuting with its wedge's boost; in de Sitter this fixes $\rho^{2} = 12/\Lambda$ (frozen-point and surface-gravity candidates one tube point as physical lengths), for $\Lambda \le 0$ it leaves $\rho$ free, it decides one-horizon fields only (Schwarzschild-de Sitter, $\kappa_{b}/\kappa_{c} = 8/5$, needs a further premise), and it carries the hypothesis gap from the massive-scalar Hadamard uniqueness theorem to the series' CAR modes.
