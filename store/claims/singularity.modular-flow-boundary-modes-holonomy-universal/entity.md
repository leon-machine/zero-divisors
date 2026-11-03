---
id: singularity.modular-flow-boundary-modes-holonomy-universal
kind: claim
version: 2
title: The modular flow of the boundary modes as a holonomy, and its universal temperature
status: proved
region: singularity
subject: thermality
tags: [modular-theory, hawking-temperature, kasner]
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
review: typed
derivations:
- name: main
  uses:
  - singularity.imported-general-form@1
  - singularity.imported-interior-collar-kasner-form@6
  - singularity.modular-structure-completed-pair@5
  - singularity.plane-rate@4
  assumes:
  - singularity.r-regularity-fixed-locus@3
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:13.2
- kind: check
  ref: check.py::check_t_line_holonomy_rate
- kind: check
  ref: check.py::check_hubble_normalised_limit_six_pi
- kind: check
  ref: check.py::check_sphere_rate_and_noncommuting_boosts
locators:
  paper: T05
  number: Prop 13.2
  label: prop:holonomy
  line: 2445
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the GTG t-line transport Omega(d_t) = (A''/2) B_1 as a boost at rate 1/(2r^2) with horizon value kappa, the Hubble-normalised series limit 1/3 (beta_H = 6 pi) and sphere value 3 pi, and the pairwise non-commuting limiting boosts with Gibbs densities in distinct spans. Version 1 -> 2. Wording fix (Leon 2026-10-23): (iii) states B_1 x B_2 = -R_12 with the commutator product (AB - BA)/2, for the earlier bracket [B_1, B_2] (formal and technical).'
  env: proposition
  typing:
    by: ai-typing-pass
    note: 'Kept all edges: the collar Fact, the completed pair, the rate and (R) for (i) and (ii), and
      the general-form Fact as the store''s nearest import of the modular-group uniqueness used in (iii).
      Levels pass: the lay level and one-liner now name Premise (R), which fixes the period of the modular
      flow matched to the horizon holonomy.'
---

## formal
In the collar of Fact \claimref{singularity.imported-interior-collar-kasner-form}:
\begin{enumerate}
\item[(i)] the transport along a $t$-line at fixed $r$ is a boost in the plane $B_1$ of the completed pair, with rapidity per unit Killing time $|A'(r)|/2 = 1/(2r^2)$ (in general units $M/r^2$), an identity of rational functions; at the horizon $r = 1$ it equals $\tfrac12 = \kappa$, the rate of Proposition \claimref{singularity.plane-rate}, so the modular flow of Theorem \claimref{singularity.modular-structure-completed-pair} with the period of Premise \claimref{singularity.r-regularity-fixed-locus} is the $t$-line holonomy at the horizon; inside, the rate grows as $r^{-2}$ and the Killing-time KMS period $2\pi/(|A'|/2) = 4\pi r^2$ shrinks with it;
\item[(ii)] Hubble-normalised, the same rate is $\tau\,|A'|/(2\sqrt{A}) = \tfrac13 S(r)/\sqrt{1 - r} = \tfrac13 + \tfrac{4}{15}r + \cdots$ with $\tau = \tfrac23 r^{3/2} S(r)$, whose limit at the exceptional set is $|p_1| = \tfrac13$; the period $2\pi$ of the boost's rapidity divided by this limit is
\[
\beta_{\mathrm{H}} \;=\; \frac{2\pi}{|p_1|} \;=\; 6\pi ,
\]
independent of $M$ and of the position on the exceptional set. If the KMS state of the boundary modes on the completed pair extends to a KMS state of the $t$-line holonomy flow on the collar, then its inverse temperature in Hubble-normalised time at the exceptional set is this $\beta_{\mathrm{H}}$; whether it so extends is open (Section \ref{sec:conclusion});
\item[(iii)] for the sphere directions the corresponding number would be $2\pi/p_2 = 3\pi$. The limiting boosts $B_1$, $B_2$, $B_3$ pairwise fail to commute, $B_1 \times B_2 = -R_{12} \neq 0$ (commutator product, $A \times B = (AB - BA)/2$), so no two of the three limiting flows have proportional generators. Consequently, on any von Neumann algebra carrying the three flows as automorphism groups, a faithful normal state that is KMS at some $\beta \neq 0$ for one of them is KMS at no $\beta' \neq 0$ for either other, by the uniqueness of the modular group; at $\beta = 0$ a trace is KMS for every flow, and is excluded. This series constructs no such algebra for the collar; on the one algebra this paper does construct, the matrix factor of Theorem \claimref{singularity.modular-structure-completed-pair}, only $B_1$ acts. The direction the modular flow of the boundary modes selects is $B_1$, the $t$-direction, by (i).
\end{enumerate}

## technical
In the interior collar in Kasner form, the transport along a $t$-line at fixed $r$ is a boost in the plane $B_1$ of the completed pair, with rapidity per unit Killing time $|A'(r)|/2 = 1/(2r^2)$ (in general units $M/r^2$). At the horizon $r = 1$ this is $\tfrac12 = \kappa$, so the modular flow of the completed pair at the period of Premise (R) is the $t$-line holonomy at the horizon; inside, the rate grows as $r^{-2}$ and the Killing-time KMS period $4\pi r^2$ shrinks with it. Hubble-normalised, the rate tends to $|p_1| = \tfrac13$ at the exceptional set, giving $\beta_{\mathrm{H}} = 2\pi/|p_1| = 6\pi$, independent of $M$ and of the position. If the KMS state of the boundary modes extends to a KMS state of the $t$-line holonomy flow on the collar, this is its Hubble-normalised inverse temperature there; whether it so extends is open.

For the sphere directions the corresponding number would be $2\pi/p_2 = 3\pi$, but the limiting boosts $B_1$, $B_2$, $B_3$ pairwise fail to commute, $B_1 \times B_2 = -R_{12} \neq 0$ (commutator product, $A \times B = (AB - BA)/2$). By uniqueness of the modular group, on any von Neumann algebra carrying the three flows a faithful normal state that is KMS at some $\beta \neq 0$ for one of them is KMS at no $\beta' \neq 0$ for another. No such algebra is constructed for the collar; on the matrix factor of the completed pair only $B_1$ acts, and the direction the modular flow selects is $B_1$, the $t$-direction.

## lay
Inside a black hole, the natural evolution of the boundary modes can be read as the twist picked up by moving forward in time at fixed radius. At the horizon this twisting rate is exactly the surface gravity, so that, with the period fixed by the regularity premise (R), the modes' clock is tied to the geometry. Near the singularity, measured in the natural expansion time there, it would give the same inverse temperature, $6\pi$, for every black hole, provided the thermal state extends that far, which is left open. The other two directions would give different values, but no single state could be thermal for all of them, and only the time direction is actually realised.

## one-liner
The $t$-line transport in the interior collar is a boost in the completed pair's plane whose rate is $\kappa$ at the horizon, matching the modular flow at the period of (R), and whose Hubble-normalised limit at the exceptional set gives $\beta_{\mathrm{H}} = 6\pi$ if the KMS state extends to the collar, and the non-commuting limiting boosts leave $B_1$, the $t$-direction, as the one the modular flow selects.
