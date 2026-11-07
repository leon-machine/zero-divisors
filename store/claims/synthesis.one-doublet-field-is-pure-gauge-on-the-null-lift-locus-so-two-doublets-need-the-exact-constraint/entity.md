---
id: synthesis.one-doublet-field-is-pure-gauge-on-the-null-lift-locus-so-two-doublets-need-the-exact-constraint
kind: claim
version: 3
title: 'A one-doublet field is pure gauge on the null-lift locus'
status: proved
region: synthesis
subject: quantum-fields
tags: [symmetry-breaking, gauge-fields, mass-generation, no-go]
proposed_by:
  kind: ai
  session: 2026-11-02-qft-full
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
review: draft
derivations:
- name: main
  uses:
  - standard-model.ten-transported-ambient-space-doublets-are@2
  - synthesis.rung-unit-is-frame-boost@2
  - synthesis.rung-field-on-the-lift-locus@2
  - synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus@3
  - synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_one_doublet_subspaces_are_the_graphs
- kind: check
  ref: check.py::check_graphs_meet_the_lift_locus_in_one_frame
- kind: check
  ref: check.py::check_one_doublet_field_on_the_lift_locus_is_pure_gauge
- kind: check
  ref: check.py::check_radial_mode_of_a_one_doublet_field_changes_q
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum
  - synthesis.rung-unit-is-frame-boost
  - synthesis.rung-field-on-the-lift-locus
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The unit of the U(2) generators T_j = (I_4/2) sigma_j, Y = (I_4/2) 1 and of the check''s basis maps (I_4, 0), (0, I_4) is now the field theory''s unit I_4, which commutes with the rung vectors; the complex numbers of the statement are said to be span{1, I_4} (the stored C of R_C); no bare i remains.'
  maintainer_pass:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 1 -> 2: the two text citations in the technical level (the quartic-running result and the B-mixing result, both now in the store) become claimrefs; no edge added (cross-references, not premises). Pin of synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum moved to @3 (dated note excluding the transmutation branch; the spectrum used here unchanged). Statement, proof and check unchanged.'
  open_problem: op.qft-structural-inputs
  note: >-
    The doublet count of the field theory, asked as whether two doublets follow from the series' structure.
    The rung summand's representation (one doublet of hypercharge one half and its conjugate) is fixed by the
    ten; the question is whether the rung field may take values in a four-dimensional invariant real subspace
    (one doublet) or needs all eight real components (two). Kill conditions registered before computing: a
    one-doublet subspace containing the lift point and tangent to the rung unit; a one-doublet subspace
    meeting the locus in more than one gauge orbit. Neither fired. Standard content: in two-doublet language
    the rung unit is the direction that changes the ratio of the two vacuum values at fixed bilinear, which a
    single doublet does not have. New: the stored identification of the neutral physical scalar with the rung
    unit (the frame boost) is that direction, so the doublet count follows from three readings taken exactly
    (a hard null-lift constraint, the Higgs exactly the rung unit, a linear field). At finite constraint
    coupling the distinction is of relative order H^2/v^2, and the hard limit lies outside perturbation theory,
    so the count is a consequence of those readings, not of the field theory at finite coupling.
    Transport-convenient: the rung summand and the lift locus come from transport; the argument is
    representation theory.
---

## formal
In the setting of Theorem \claimref{synthesis.rung-field-on-the-lift-locus}: $\mathcal{R}_{\C} = (H_{4} \oplus H_{5}) \otimes \C$ (the field theory's unit $I_{4}$ commutes with the rung vectors, and numbers are read in $\mathrm{span}\{1, I_{4}\}$, which is the $\C$ of this statement) with $c = \sum_{a}(\alpha_{a}v_{a} + \beta_{a}w_{a})$, $Q(c) = \alpha^{\mathsf T}\beta$, $N(c) = \tfrac12(|\alpha|^{2} + |\beta|^{2})$, $m(c) = \tfrac12(|\alpha|^{2} - |\beta|^{2})$, the slot mixing $U(2)$ acting by $\alpha \mapsto X\alpha$, $\beta \mapsto \bar{X}\beta$ (generators $T_{j} = \tfrac{I_{4}}{2}\sigma_{j}$, $Y = \tfrac{I_{4}}{2}\mathbf{1}$), $H^{2} = \Lambda/3$, the null-lift locus $L = \{Q(c) = -H^{2}\}$, the lift family $c_{\lambda} = -\lambda w_{4} + \tfrac{H^{2}}{\lambda}v_{4}$ and the rung unit $u_{\lambda} = dc_{\lambda}/d\lambda$. Call a \emph{one-doublet subspace} a $U(2)$-invariant real subspace of $\mathcal{R}_{\C}$ of real dimension four, and a one-doublet field a field valued in one.
\begin{enumerate}
\item \emph{(Classification.)} The real-linear $U(2)$-equivariant maps from the doublet $\C^{2}$ (generators $T_{j}$, $Y$) to $\mathcal{R}_{\C}$ are $\gamma \mapsto (p\gamma, q\bar{\gamma})$, $p, q \in \C$, a real four-dimensional space, and each nonzero one is injective. The one-doublet subspaces are $D_{0} = \{\beta = 0\}$, $D_{\infty} = \{\alpha = 0\}$ and the graphs $G_{a} = \{\beta = a\bar{\alpha}\}$, $a \in \C \setminus \{0\}$.
\item \emph{(One orbit, one frame.)} $Q$ vanishes on $D_{0}$ and $D_{\infty}$, which miss $L$. On $G_{a}$, $Q(\alpha, a\bar{\alpha}) = a|\alpha|^{2}$ and $m/N = (1 - |a|^{2})/(1 + |a|^{2})$; so $G_{a}$ meets $L$ only when $a = -r$, $r > 0$, and then $G_{-r} \cap L = \{|\alpha|^{2} = H^{2}/r\}$ is one $U(2)$-orbit, a three-sphere, which contains $c_{\lambda}$ exactly when $\lambda^{2} = rH^{2}$. The frame of a vacuum on $G_{-r} \cap L$ is fixed by $r$.
\item \emph{(Pure gauge on the locus.)} At $c_{\lambda}$ the tangent spaces of $G_{-r}$ and of $L$ meet in the tangent space of the gauge orbit, of dimension three. So the rung unit $u_{\lambda}$ and the charged plane of Theorem \claimref{synthesis.rung-field-on-the-lift-locus}(3) lie in no one-doublet subspace through $c_{\lambda}$, and the smallest $U(2)$-invariant real subspace containing $c_{\lambda}$ and $u_{\lambda}$ is $\mathcal{R}_{\C}$.
\item \emph{(The one physical mode leaves the locus.)} In $G_{-r}$ the complement of the gauge orbit at $c_{\lambda}$ for $\operatorname{Re}(x^{*}\cdot y)$ is the line of $c_{\lambda}$, along which $dQ = 2Q(c_{\lambda}) = -2H^{2} \neq 0$: a direction normal to $L$, while $Q(c_{\lambda}, u_{\lambda}) = 0$.
\item \emph{(Size of the distinction; computed.)} The one-doublet subspace through $c_{\lambda}$ is $G_{-r}$ with $r = \lambda^{2}/H^{2}$; its radial direction $c_{\lambda}/\lambda = (\tfrac{H^{2}}{\lambda^{2}}e_{4}, -e_{4})$ and the rung unit $u_{\lambda} = (-\tfrac{H^{2}}{\lambda^{2}}e_{4}, -e_{4})$ differ by $\tfrac{2H^{2}}{\lambda^{2}}e_{4}$ in the $\alpha$-coefficient, a relative angle of order $H^{2}/\lambda^{2}$ (of order $H^{2}/v^{2}$ at the stored vacuum, where $\lambda^{2}$ is of the order of the weak scale squared); and along the radial direction the term $k_{10}|Q + H^{2}|^{2}$ of the linear field adds a mass squared of order $k_{10}H^{4}/\lambda^{2}$.
\end{enumerate}
Hence a field whose restriction to $L$ carries the rung unit and the charged pair of Theorem \claimref{synthesis.rung-field-on-the-lift-locus}(3) takes values in all of $\mathcal{R}_{\C}$. The count of two doublets follows if the null-lift constraint is imposed exactly (the limit $k_{10} \to \infty$ of the linear field of Theorem \claimref{synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum}), the neutral physical scalar is exactly the rung unit (Theorem \claimref{synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus}(3)) and the field is linear; it does not follow at finite $k_{10}$, where by (5) a one-doublet field reproduces the rung-unit direction to relative order $H^{2}/\lambda^{2}$. The representation $\mathcal{R}_{\C}$, one doublet and its conjugate, is fixed by the ten (Proposition \claimref{standard-model.ten-transported-ambient-space-doublets-are}); it does not by itself choose between a field in a real form (one doublet; the tower's conjugation fixes $G_{1}$, which misses $L$, Theorem \claimref{synthesis.rung-unit-is-frame-boost}(5)) and a field in all of $\mathcal{R}_{\C}$ (two).

## technical
The rung field takes values in the complexified rung summand: eight real components that carry one weak doublet of hypercharge one half and its conjugate, which as a complex field are two hypercharge-one-half doublets. The four-dimensional pieces a single doublet could occupy are classified exactly. They are the two complex doublets, on which the null-lift form $Q$ vanishes, and the graphs $\beta = a\bar{\alpha}$, on which $Q = a|\alpha|^{2}$ and the ratio of the hypercharge moment map to the norm is constant. A graph reaches the null-lift locus only for real negative $a$, and then in a single gauge orbit at a single frame set by $a$. On the exact locus, therefore, a one-doublet field is pure gauge. The rung unit, the frame boost that the stored theory identifies with the neutral physical scalar, is not tangent to any one-doublet piece through the vacuum, and neither is the charged pair. The smallest invariant space containing the vacuum and the rung unit is the whole summand. The single physical mode a one-doublet field has is its radial direction, which changes $Q$.

The count of two doublets is a consequence of three readings, each taken exactly: the null-lift constraint imposed as a hard constraint, the Higgs identified exactly with the rung unit, and a linear field. At any finite constraint coupling the distinction is tiny. The radial direction of the one-doublet piece through the vacuum differs from the rung unit by a relative angle of order $H^{2}/v^{2}$, about $10^{-88}$ at the stored frame. The constraint term shifts its mass squared only by an amount of order $k_{10}H^{4}/v^{2}$. The hard limit $k_{10} \to \infty$ is not a perturbative decoupling. The rung quartics run to strong coupling within a few TeV on the transmutation branch (\claimref{synthesis.rung-field-quartics-run-to-strong-coupling-within-a-few-tev-on-the-transmutation-branch}). The decoupling that flavour allows, through the level, makes the whole second doublet heavy and leaves one light doublet at low energy (\claimref{synthesis.covariant-rung-coupling-gives-the-normal-pair-tree-level-b-meson-mixing-that-excludes-the-transmutation-branch}). In two-doublet language the rung unit is the standard direction that changes the ratio of the two vacuum values, which a single doublet lacks. The ten fixes the representation but not the count: the tower's conjugation selects a one-doublet real form that misses the locus.

## lay
In this framework the Higgs field lives in an eight-dimensional space whose directions come from the geometry that transport adds. The Standard Model uses one Higgs doublet, which has four real directions. This result asks whether four of the eight directions could be enough here. If the framework's vacuum condition is imposed exactly, they are not. Any four-direction slice that respects the weak and hypercharge symmetries either never meets that condition or meets it only along directions that are pure gauge, which the massive W and Z bosons absorb. The particle the framework identifies with the observed Higgs boson, a change of the frame in which the vacuum is read, points out of every such slice. If the condition is only approximate, as it is in a field theory with finite couplings, one doublet can imitate that particle to about one part in $10^{88}$. So the need for a second doublet rests on taking the condition and the identification exactly, not on anything measurable at present.

## one-liner
A one-doublet field meets the null-lift locus only in pure gauge, so a field carrying the rung unit and the charged pair on the exact locus fills the whole rung summand: two doublets follow only from an exact constraint, the Higgs exactly the rung unit and a linear field; at finite coupling one doublet reproduces the rung-unit direction to relative order $H^{2}/v^{2}$, about $10^{-88}$.
