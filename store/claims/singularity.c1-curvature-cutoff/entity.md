---
id: singularity.c1-curvature-cutoff
kind: claim
version: 5
title: 'C1: curvature cutoff'
status: postulate
region: singularity
subject: entropy
tags: [entropy-premises, schwarzschild]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
- name: Claude Fable 5.2
  role: 'scope note at Leon''s decision of 10 November 2026: the class of placements called forced fails on Kerr at both ends of the spin range'
  version: 5
  source: maintainer pass of 2026-11-10
review: typed
locators:
  paper: T05
  number: Axiom 10.1
  label: ax:cutoff
  line: 2133
extraction:
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version 4 -> 5. Scope note added at Leon''s decision of 10 November 2026 (the premise is unchanged): on Kerr the class of placements that the note on form calls forced fails at both ends of the spin range (synthesis.no-spin-independent-modulus-level-set-gives-the-area-law-exactly-on-slow-kerr for slow rotation, synthesis.kerr-ring-count-misses-area-law for a >= 2(2M)^{2/3}), and a count placed at the horizon is a multiple of the area by construction (synthesis.stretched-horizon-count-on-kerr-is-a-multiple-of-the-area-by-construction), whose hypothesis (SH) is not adopted.'
  maintainer_pass_2:
    by: maintainer-2026-10-24
    date: '2026-10-24'
    note: 'Referee fixes to the GTG wording pass (2026-10-24): ''a gravitational field of nonvanishing field strength'' (gauge-independent) in place of ''a nonvanishing gravitational field''; global content read on several charts of flat spacetime, each with its own gravitational field, glued by displacement and rotation gauge transformations (complexified charts for the half-flat manifold, the conformal compactification for a conformal boundary); ''not carried by the store''s one-chart fields'' in place of ''no single gravitational field carries''; equivalence statements weakened where the old text was weaker; remaining curved-spacetime phrases in lay text restated. Wording only. Version 3 -> 4.'
  env: axiom
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Version 3 adds a scope sentence, at Leon's decision of 23 October (cutoff premises as a Schwarzschild calibration only), that (C1) with (C2) and (IC) is read as a calibration on the Schwarzschild family, since read literally the count fails the area law on Schwarzschild-de Sitter (u/(3u-2) times A_b/4 over the hole's modular period, synthesis.cutoff-count-is-not-a-local-density-on-sds) and on Kerr (synthesis.kerr-ring-count-misses-area-law); away from Schwarzschild the horizon placement with a flat-data density is the count. The premise itself is unchanged on the Schwarzschild family.
  maintainer_pass_2026_10_22:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: Version 2 adds a note, at Leon's decision to keep (C1) and (C2) rather than replace them by (C2'), that their forms are forced by an algebraic curvature criterion plus isometry invariance leaving one constant (synthesis.c1-c2-forms-forced-one-number) and that (C2') on the exceptional set is equivalent at leading order (synthesis.exceptional-boundary-measure-one-calibration); the premise itself is unchanged.
  typing:
    by: ai-typing-pass
    note: Postulate; no edges.
---

## formal
The q-number boundary mode space of the singularity is supported on the stretched singularity, the surface on which the curvature reaches the Planck scale: $2M/r^3 = 1$ in Planck units, i.e.\ $r_c = (2M)^{1/3}$.

\emph{Note (form and calibration).} The form of this premise is forced, not chosen: an algebraic (pointwise) curvature criterion at a mass-independent value selects a member of the family $r_c^{3} = 2M/\lambda$, of which this premise is $\lambda = 1$, and, with an isometry-invariant density for Premise \claimref{singularity.c2-cell-density}, the leading count sees the threshold $\lambda$ and the density $\nu$ only through the one number $\kappa_{s} = \nu\lambda^{-1/2}$ (Theorem \claimref{synthesis.c1-c2-forms-forced-one-number}). At leading order this premise together with (C2) is equivalent to (C2$'$), the modes carried by the exceptional set itself with $\nu' = \tfrac23\kappa_{s}$ modes per Planck area of its Kasner measure $\mu_{E} = 12\pi M$ per unit Killing time; the two differ only at relative order $(2M)^{-2/3}$ (Theorem \claimref{synthesis.exceptional-boundary-measure-one-calibration}). The premise is kept as stated.

\emph{Scope (Schwarzschild calibration).} This premise, with Premise \claimref{singularity.c2-cell-density} and the intrinsic-clock premise (IC) (Premise \claimref{scrambling.intrinsic-clock-ic-flagged-premise}), is read as a calibration of the count on the Schwarzschild family only. Read literally on other holes the count fails the area law: on a Schwarzschild-de Sitter hole, with the counted epoch read as the hole's modular period, it is $u/(3u - 2)$ times $A_{b}/4$, $u = 2M/r_{b}$, for every $\Lambda > 0$, and no horizon's period gives $A_{b}/4$ (Theorem \claimref{synthesis.cutoff-count-is-not-a-local-density-on-sds}); for a spinning hole with $a \ge 2(2M)^{2/3}$ the cutoff locus is a timelike tube beyond the inner horizon and the literal count misses the area law by a factor of order $M^{-1/3}$ (Theorem \claimref{synthesis.kerr-ring-count-misses-area-law}). Away from the Schwarzschild family the count is read through the horizon placement, the modes on the horizon with a density fixed by flat tangent data, as clause (Loc) of Premise \claimref{synthesis.c-loc-local-horizon-premise} states. On Kerr the class of placements that the Note calls forced fails at both ends of the spin range: besides the tube at $a \ge 2(2M)^{2/3}$, at slow rotation ($0 < a \le \tfrac45\rho$, $\rho \le M/3$) no level set $|z| = \rho$ of the modulus of the curvature scale chosen independently of the spin, with any density, gives $A_{+}/4$ exactly at zero and at nonzero spin (Theorem \claimref{synthesis.no-spin-independent-modulus-level-set-gives-the-area-law-exactly-on-slow-kerr}); the window between the two regimes and criteria that use the phase of the complex scale are not treated. A count placed at fixed proper distance from the Kerr horizon locus is a fixed multiple of the area by construction, so it cannot fail and tests nothing; it is a hypothesis of Theorem \claimref{synthesis.stretched-horizon-count-on-kerr-is-a-multiple-of-the-area-by-construction} and is not adopted. This premise is unchanged.

## technical
Postulate: the q-number boundary mode space of the singularity is supported on the stretched singularity, the interior surface on which the curvature reaches the Planck scale, $2M/r^3 = 1$ in Planck units, so that $r_c = (2M)^{1/3}$.

It is taken as an axiom of the count, not derived: it fixes the surface on which the boundary modes are counted.

Its form is forced: any algebraic, mass-independent curvature criterion picks a slice $r_c^{3} = 2M/\lambda$, and this premise is the member $\lambda = 1$; with the uniform density of (C2) the leading count depends on the two premises only through one number, $\nu\lambda^{-1/2}$. At leading order the pair is equivalent to counting the modes on the exceptional set itself with its Kasner measure, with a single calibration constant, the premise (C2$'$). The series keeps (C1) and (C2) as they are.

The premise is read as a calibration on the Schwarzschild family only. Read literally elsewhere the count misses the area law: on a Schwarzschild-de Sitter hole, counted over the hole's own modular period, it exceeds a quarter of the horizon area by the factor $u/(3u - 2)$, $u = 2M/r_{b}$, and on fast-spinning holes the cutoff surface is a tube beyond the inner horizon whose literal count misses the area law by a factor of order $M^{-1/3}$; on slowly spinning holes no surface of fixed field-strength modulus, chosen independently of the spin, gives the area law exactly at zero and nonzero spin, so the class of placements that is forced on Schwarzschild fails on Kerr at both ends of the spin range. Elsewhere the count is the placement of the modes on the horizon with a density fixed by flat data.

## lay
This assumption says where the quantum degrees of freedom near a black hole's singularity live: on the surface inside the black hole where the gravitational field strength (curvature) reaches the Planck scale. That surface sits at a radius growing like the cube root of the mass. It is an assumption of the counting, not a derived result, and it is used only to calibrate the count on non-rotating black holes in otherwise empty space; on spinning black holes, or with a positive cosmological constant, read literally it gives the wrong entropy.

## one-liner
Postulate: the boundary mode space lies on the stretched singularity $r_c = (2M)^{1/3}$, where the curvature $2M/r^3$ reaches the Planck value; read as a Schwarzschild calibration only.
