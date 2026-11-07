---
id: synthesis.plane-wave-weak-null-crossing-null-shell-ambiguity
kind: claim
version: 5
title: 'Plane waves realise the weak null crossing, its ambiguity a null shell'
status: proved
region: synthesis
subject: interior
tags: [tractors, horizons, limits, null-directions, curvature-and-field-equations]
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
- name: Claude Opus 5.5
  role: GA rewrite (Rosen plane wave connection, conormal and Schouten map in GA)
  version: 5
  source: maintainer pass 2026-11-07 (consistency)
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.tractor-transport-weak-null-crossing@5
  - interior.imported-tractor-connection@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_store_sign
- kind: check
  ref: check.py::check_rosen_schouten
- kind: check
  ref: check.py::check_flat_scales
- kind: check
  ref: check.py::check_model_integrability
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - interior.filtration-cauchy-horizon-read-literature
  - interior.imported-mass-inflation-stability
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Covectors, Christoffel symbols and the Schouten tensor to GA in the formal and technical levels: a gauge for the Rosen field is named (hb^{-1}(e_u) = gamma_0 + gamma_1, hb^{-1}(e_v) = (gamma_0 - gamma_1)/2, hb^{-1}(e_x) = a gamma_2, hb^{-1}(e_y) = a gamma_3); du becomes the parallel null physical gradient n = hb^T(grad u), the Christoffel symbols the rotation-gauge field Omega(hb(gamma_A)) = -(a_u/a) n ^ gamma_A (A = 2, 3; zero on gamma_0, gamma_1), and the Schouten tensor the map P(v) = (a_uu/a)(v . n) n; components stay as labelled readings and the proof keeps its component computation, now saying so. Checked exactly with lib/gtg.py in the maintainer scratch at two rational second-order jets of a(u): Omega solved from the torsion condition is the displayed one, it satisfies the GA structure equation, and the store-sign Schouten map is (a_uu/a)(v . n) n. Statement unchanged.'
  maintainer_pass_2:
    by: maintainer-2026-10-24
    date: '2026-10-24'
    note: 'Gauge Theory Gravity wording pass at Leon''s request (2026-10-24): curved-spacetime and conformally-flat wording restated in terms of the gravitational field on flat spacetime (a nonvanishing gravitational field; the Weyl part of the field strength vanishes, the conformally flat derived metric kept as a reading; global content read on an atlas of flat charts patched by gauge transformations). Wording only; statements, proofs'' arguments and checks unchanged. Version 3 -> 4.'
  maintainer_pass_gtg:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Tractor wording completed by the lead: the tractor transport is that of the Cl(2,4) tractor gauge field of the plane-wave gravitational field on flat spacetime. Content unchanged.'
  open_problem: op.cauchy-horizon-transport
  note: >-
    Supplies an exact spacetime class in which every hypothesis of the stored crossing theorem holds,
    including the divergent branch with Christoffel symbols integrable but not square-integrable (the
    Luk-Oh type of failure), and identifies the theorem's one-parameter ambiguity there: relative to the
    transport selected by the metric's own Rosen factor, which is the tractor transport of the conformal
    structure in a C^1-compatible chart where that structure is smooth and flat, the other transports are
    those computed in flat scales with a kink at the crossing, whose Schouten tensor is a null shell; the
    parameter is the jump of a Wronskian. Plane waves are not perturbed Reissner-Nordstrom or Kerr Cauchy
    horizons: this is a model class, not the astrophysical case. Lead (argued, not proved): in spherical
    symmetry the area radius r solves the same Jacobi-type equation along the outgoing null direction
    (Raychaudhuri), so it may play the role of the Rosen factor and select the transport there; whether it
    does depends on the Luk-Oh profile, which is the open spherical question. The identification of the
    store's sign convention (Ric = Lambda g for de Sitter) with minus the Ricci tensor of the round-sphere-
    positive convention is calibrated in the check on de Sitter space.
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement: the plane wave is a gravitational field (hb, Omega) on flat spacetime with derived metric g = 2 du dv - a^2 (dx^2 + dy^2); Levi-Civita transport along geodesics is D-transport along free-fall worldlines; the Christoffel symbols are the connection components; field-strength wording in lay. Clauses (1)-(4) unchanged; tractor wording left to the lead; check unchanged. Proof: one opening sentence pointing to the GTG dictionary Fact.'
---

## formal
Let $J$ be an open interval containing $u_c$, $a : J \to (0, \infty)$ continuous, smooth on $J \setminus \{u_c\}$, with $a_u := da/du$ integrable on $J$, and let $(\hb, \Omega)$ be the gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), on the region $J \times \R^3$ of background labels $(u, v, x, y)$, whose derived metric is
\[
g = 2\,du\,dv - a(u)^2\,(dx^2 + dy^2)
\]
(signature $(1,3)$), in the gauge $\hb^{-1}(e_u) = \gamma_0 + \gamma_1$, $\hb^{-1}(e_v) = \tfrac12(\gamma_0 - \gamma_1)$, $\hb^{-1}(e_x) = a\,\gamma_2$, $\hb^{-1}(e_y) = a\,\gamma_3$. Write $\tilde u(u) := \int_{u_c}^{u} a(s)^{-2}\,ds$ and $\eta := 2\,d\tilde u\,dv - dx^2 - dy^2$. Then:
\begin{enumerate}
\item \emph{(The hypotheses hold.)} $g$ is continuous; the physical gradient $n = \hb^{T}(\nabla u) = \tfrac12(\gamma_0 - \gamma_1)$ of the label $u$ is a $D$-parallel null vector (in components the covector $du$); the rotation-gauge field is $\Omega(\hb(\gamma_A)) = -(a_u/a)\,n\wedge\gamma_A$ for $A = 2, 3$ and zero on $\gamma_0$, $\gamma_1$ (in components, the nonzero Christoffel symbols $a_u/a$ and $a\,a_u$), so $D$-transport, the Levi-Civita transport of $g$, extends continuously across $u = u_c$ along every free-fall worldline (geodesic of $g$); and in the store's convention the Schouten map is $\Sch(v) = (a_{uu}/a)\,(v\cdot n)\,n$ off $u_c$ (in components $\Sch = (a_{uu}/a)\,du \otimes du$). Along every causal geodesic with $\nu := n\cdot k \neq 0$, $k = \hb^{-1}(\gamma')$ its physical velocity (in components $\nu = du(\gamma')$), the decomposition of Theorem \claimref{synthesis.tractor-transport-weak-null-crossing} holds with this $n$, $S = a_{uu}/a$ and $R = 0$, and its Tipler-type condition is $\int_J |u - u_c|\,|a_{uu}|\,du < \infty$.
\item \emph{(The derived metric supplies a removal scale.)} $y = a \circ u$ solves the removal equation $y'' = \nu^2 S y$, and the scale it induces is $a^{-2} g = \eta$, flat on each side; $u \mapsto \tilde u$ is a $C^1$ change of coordinate with $C^1$ inverse, in whose chart the conformal class $[g] = [\eta]$ is the smooth flat one across $\tilde u = 0$. Every admissible removal solution is $y = a\,(\alpha + \beta_\pm \tilde u)$ on the two sides, with $\alpha > 0$ common and Wronskian $a\,y_u - a_u\,y = \beta_\pm$.
\item \emph{(The ambiguity is a null shell.)} The transports selected by $y$ and by $a$ differ by $\exp(c N_n)$, inserted at the crossing in the gauge of $a$, with $c = (\beta_+ - \beta_-)/(\alpha\,a(u_c)^2)$; in the chart $(\tilde u, v, x, y)$ the scale of $y$ is $(\alpha + \beta_\pm\tilde u)^{-2}\eta$, flat on each side, whose Schouten map is $v \mapsto -(\varphi''/\varphi)\,(v\cdot\tilde n)\,\tilde n$, $\tilde n$ the physical gradient of $\tilde u$ (in components $-\varphi''/\varphi\; d\tilde u \otimes d\tilde u$), with $\varphi = \alpha + \beta_\pm \tilde u$, a null shell of strength $-(\beta_+ - \beta_-)/\alpha$ at $\tilde u = 0$ when $\beta_+ \neq \beta_-$. The transport selected by $a$ is the tractor transport (the transport of the $\Cl(2,4)$ gauge field of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}) of the smooth conformal structure in that chart; the others are those of the same structure computed in a scale with a null shell at the crossing.
\item \emph{(An explicit divergent model.)} For $a = 1 + (u_c - u)^{1/2}$ on $u < u_c$, continued by any positive solution beyond, $a_u$ is integrable but not square-integrable, $S = -\tfrac14 t^{-3}(1 + t)^{-1}$ with $t = (u_c - u)^{1/2}$ has a fixed sign and is not integrable, and the Tipler-type integral is finite: the derived metric is continuous, its rotation-gauge field (in components, its Christoffel symbols) fails to be locally square-integrable, and the divergent branch (3) of Theorem \claimref{synthesis.tractor-transport-weak-null-crossing} occurs, with divergence in the $N_n$ slot in the splitting of $g$.
\end{enumerate}

## technical
The stored crossing theorem says that tractor transport across a null hypersurface where the Schouten tensor has a non-integrable rank-one null part exists modulo a one-parameter group $\exp(\R N_n)$, under hypotheses (continuous Levi-Civita transport, a parallel null conormal, a Tipler-type bound) whose realisation by any gravitational field was open. Plane-wave gravitational fields with vanishing Weyl part, gravitational fields on flat spacetime whose derived metric has the Rosen form $g = 2\,du\,dv - a(u)^2(dx^2 + dy^2)$, with $a$ continuous and $a_u$ integrable, realise all of them exactly: the rotation-gauge field is $-(a_u/a)\,n\wedge\gamma_A$ on the two transverse frame vectors (Christoffel symbols $a_u/a$ and $a a_u$), the Schouten map is $v \mapsto (a_{uu}/a)(v\cdot n)n$ in the store's sign convention, with $n$ the parallel null physical gradient of $u$, and the profile $a = 1 + (u_c - u)^{1/2}$ gives a rotation-gauge field that is integrable but not square-integrable, a non-integrable Schouten coefficient of fixed sign, and finite tidal deformation. The metric supplies its own solution of the removal equation, $y = a$, whose scale $a^{-2}g$ is the flat metric $2\,d\tilde u\,dv - dx^2 - dy^2$ in the $C^1$ coordinate $\tilde u = \int du/a^2$. All other admissible solutions are $a(\alpha + \beta\tilde u)$ with possibly different slopes $\beta$ on the two sides, and by the stored comparison formula their transports differ from that of $a$ by $\exp(cN_n)$ with $c$ proportional to the jump of $\beta$, the Wronskian against $a$. In the flat chart their scales are flat on each side with a kink at the crossing, so their Schouten tensor carries a null shell there. In this class the ambiguity of the stored theorem is therefore the strength of a null shell sitting on the crossing, which the metric's own chart cannot exclude because the Schouten coefficient is not integrable there; in the chart where the conformal structure is smooth the shell-free transport is singled out. In the classification by power profiles filed alongside, synthesis.crossing-transport-tipler-threshold-sharp, the model's Schouten coefficient $S \sim (u_c - u)^{-3/2}$ is the power profile with $\beta = \tfrac14$, its case (b) (Tipler-integrable, not integrable): this class realises that case by an explicit spacetime. Plane waves are a model, not the perturbed Cauchy horizons of charged or rotating holes. The exact checks calibrate the sign convention on de Sitter space, compute the Rosen Schouten tensor and Christoffel symbols for the model and for a generic rational profile, verify the flatness of $a^{-2}g$ and of $(1 + 3w)^{-2}\eta$, the shell coefficient of $\varphi^{-2}\eta$, the Wronskian identity, and the integrability pattern of the model.

## lay
Inside charged and rotating black holes the inner horizon is expected to be a weak singularity: the gravitational field stays continuous but its rates of change blow up. The series has a theorem saying its transport survives such a crossing up to one undetermined number, provided several conditions hold, and it was not known whether any gravitational field meets them. This result gives an explicit family that does: gravitational plane waves of pure radiation with a sharp but weak front. In that family the undetermined number has a clear meaning. It measures how much of an infinitely thin sheet of radiation one allows to sit exactly on the front, something the singular field cannot see in its own coordinates. In a coordinate system where the shape of light cones is smooth, the choice with no such sheet stands out. Whether the same holds at real black-hole inner horizons is not settled by this model.

## one-liner
Plane-wave gravitational fields with vanishing Weyl part, derived metric $2\,du\,dv - a^2(dx^2 + dy^2)$ with continuous $a$ and integrable $a_u$ satisfy every hypothesis of the weak null crossing theorem, including Christoffel symbols that are not square-integrable, and the theorem's one-parameter transport ambiguity is there the strength of a null shell at the crossing, absent for the transport selected by the Rosen factor $a$ in the chart where the conformal structure is smooth.
