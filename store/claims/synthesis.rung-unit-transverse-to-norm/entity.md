---
id: synthesis.rung-unit-transverse-to-norm
kind: claim
version: 3
title: 'A change of rung unit is transverse to the norm'
status: proved
region: synthesis
subject: standard-model
tags: [frozen-point, ladder-pairs, undetermined-input]
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
  - transport.totality@3
  - standard-model.transported-frozen-point@5
  - standard-model.imported-tower-commuting-copies-fock-module@5
  - odd-extensions.transport-constrains-frozen-point-only-through@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_rung_unit_transverse_to_norm
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - standard-model.what-derived-what-not
extraction:
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 3: a marked note fixes the Hubble unit of v/H (H^2 = Lambda/3, that is H_0 sqrt(Omega_Lambda), against H_0; a factor of order one, about 0.2 in ln(v/H)); the balanced frame mu = H has H^2 = Lambda/3. Nothing else is changed.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  open_problem: op.rung-unit
  note: 'Filed alongside, synthesis.rung-unit-is-frame-boost, which proves that the rung summand is split, that the rung unit is the boost of its frame, and the conjugation norm of the boosted rung component with its minimum; this entity cites that formula and does not restate it. It adds three things. (1) The boost changes nothing that transport can see, not only the rung component''s norm but every clause of the totality theorem, which holds verbatim in the boosted frame. (2) A change of rung unit moves the transported rung component along a level set of its norm, Klein-orthogonally to it, whereas a change of the cosmological constant moves it off; read as a statement about tangent directions, a dynamical rung unit, if there were one, would move along a direction orthogonal to the norm mode, consistent with standard-model.imported-norm-frozen-point-not-field and dark-energy.point-infinity-has-no-physical-fluctuation, which give the norm no local degree of freedom (a reading, not a theorem about fields). (3) The two doublet directions of the transported frozen point, H_d-type from the lift and H_u-type from the reciprocal''s lift, are the same construction in two frames related by the boost H^{-2}, exchanged by the involution mu -> H^2/mu whose fixed point is the balanced frame mu = H. Transport-convenient. It neither fixes v/H nor supplies a Lagrangian.'
---

## formal
Let $I$ be a frozen point of the ground space with $Q(I) = \Lambda/3$, let $(e_{+}, e_{-})$ be the orthonormal pair adjoined by the next completion, $v = \tfrac12(e_{-} + e_{+})$, $w = \tfrac12(e_{+} - e_{-})$, $\nO' = -w$, $\nInf' = 2v$ as in Proposition \claimref{standard-model.transported-frozen-point}, and $*$ the conjugation of Fact \claimref{standard-model.imported-tower-commuting-copies-fock-module} ($v^{*} = w$; on the real rung plane it fixes $e_{+}$ and negates $e_{-}$), with $\|y\|_{*} = y^{*}\cdot y$. For $\mu > 0$ let $X_{\mu}(x) = \mu\,\nO' + x + \frac{Q(x)}{2\mu}\,\nInf'$, $c_{\mu} = -\mu w + \frac{\Lambda}{3\mu}v$ the rung component of $X_{\mu}(I)$, and $B_{s}$ the boost $v \mapsto sv$, $w \mapsto w/s$ fixing the ground.
\begin{enumerate}
\item \emph{(Transport cannot see the unit.)} $B_{s}$ is an isometry, $(B_{s}v, B_{s}w)$ again satisfies $v^{2} = w^{2} = 0$, $vw + wv = 1$, and $X_{\mu} = B_{1/\mu}\circ X_{1}$; every clause of Fact \claimref{transport.totality} holds for $X_{\mu}$ with $\iota_{\mu}[N] = [e_{+}^{(\mu)}Ne_{+}^{(\mu)}]$, $e_{+}^{(\mu)} = B_{1/\mu}e_{+}$. Every function of rung-plane vectors with both null components nonzero that is invariant under all $B_{s}$ is a function of the norm and the sign of the $w$-coefficient, and $Q(c_{\mu}) = -\Lambda/3$ for every $\mu$.
\item \emph{(The unit is transverse to the norm.)} $\bigl(\tfrac{d}{d\mu}c_{\mu}\bigr)\cdot c_{\mu} = 0$ and $\bigl(\tfrac{\partial}{\partial\Lambda}c_{\mu}\bigr)\cdot c_{\mu} = -\tfrac16$ (so $\tfrac{\partial}{\partial\Lambda}(Q(c_{\mu})) = -\tfrac13$): a change of the rung unit moves $c_{\mu}$ along a level set of the norm, Klein-orthogonally to $c_{\mu}$, and a change of $\Lambda$ moves it off.
\item \emph{(The two doublet lifts are mirror frames.)} $c_{1}$ and $c_{\Lambda/3}$ are the rung components of Proposition \claimref{standard-model.transported-frozen-point}(i) and (ii), so for $\Lambda > 0$ the reciprocal's rung component is the lift's in the boosted frame, $c_{\Lambda/3} = B_{3/\Lambda}c_{1}$. With $H^{2} = \Lambda/3$, the involution $\mu \mapsto H^{2}/\mu$ of the units exchanges $c_{1}$ and $c_{\Lambda/3}$, and its fixed point is the balanced frame $\mu = H$.
\end{enumerate}

\emph{Note (the Hubble unit).} Here $H$ is the de Sitter rate of $\Lambda$, $H^{2} = \Lambda/3$, that is $H_{0}\sqrt{\Omega_{\Lambda}}$, the $H$ of $N = M_{P}/H$; some texts quote $v/H$ with $H_{0}$, which differs from it by the factor $\sqrt{\Omega_{\Lambda}}$, of order one ($v/H \approx 2.1 \times 10^{44}$ against $v/H_{0} \approx 1.7 \times 10^{44}$; $\ln(v/H)$ changes by about $0.2$). No number here depends on the choice.

## technical
The lift that carries the frozen point into the next rung needs a unit $\mu$, and changing $\mu$ is a boost of the rung plane. The boost preserves the quadratic form, the anticommutation relations of the rung's mode pair, and the totality theorem clause by clause, so nothing transport defines can fix the unit; the rung component keeps the norm $-\Lambda/3$, the only invariant of its boost orbit. A change of unit moves the rung component along the level set of its norm, orthogonally to it in the tractor metric, while a change of $\Lambda$ moves it off that level set. So a dynamical rung unit, if there were one, would move along a direction orthogonal to the norm mode of the frozen point, which carries no local degree of freedom. The two doublet directions the transported frozen point produces, from the lift and from the reciprocal's lift, are the same component in two frames related by the boost $H^{-2}$, exchanged by the involution $\mu \mapsto H^{2}/\mu$, whose fixed point is the balanced frame $\mu = H$ singled out by the conjugation norm (filed alongside, synthesis.rung-unit-is-frame-boost).

## lay
In the series the Higgs field's size is measured in a unit that the step carrying the cosmological point into the next layer has to choose, and changing that unit is a hyperbolic rotation of the new layer. That rotation leaves every geometric statement of the step unchanged, so the geometry cannot choose the unit. It is also a different direction from a change of the cosmological constant, so if the unit were promoted to a field, its changes would point in a different direction from those of the cosmological constant. The two Higgs directions that the step produces turn out to be the same thing seen in two frames, mirror images of each other about the frame matched to the cosmological scale.

## one-liner
The lift's unit $\mu$ is a boost $B_{1/\mu}$ under which every clause of totality holds and the rung component keeps norm $-\Lambda/3$; $(dc_{\mu}/d\mu)\cdot c_{\mu} = 0$, so the rung unit is transverse to the norm mode, and $\mu \mapsto H^{2}/\mu$ exchanges the $H_{d}$- and $H_{u}$-type lifts about the balanced frame $\mu = H$.
