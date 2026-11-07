---
id: synthesis.taub-nut-cauchy-horizon-is-taub-point-with-complex-residue
kind: claim
version: 2
title: 'The Taub-NUT Cauchy horizon as a Taub point with complex residue'
status: proved
region: synthesis
subject: interior
tags: [kasner, limits, rotors-and-stabilisers, horizons]
proposed_by:
  kind: ai
  session: 2026-10-31-all-open
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 2
  source: maintainer pass 2026-11-07 (GA units)
review: draft
about:
- obj.interior.weighted-blow-up-hubble-normalisation-admissible
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.imported-gtg-dictionary@1
  - synthesis.bkl-bounce-invariant-holonomy-and-bound@2
  - synthesis.bkl-bounces-no-framewise-invariant@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_bianchi_ix_frame_formulas
- kind: check
  ref: check.py::check_taub_nut_vacuum
- kind: check
  ref: check.py::check_horizon_limit
- kind: check
  ref: check.py::check_generated_algebra
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.bkl-bounce-invariant-holonomy-and-bound
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Group F: the complex mass m + il (formal, technical, one-liner) is written m + Il with the entity''s pseudoscalar I = e0e1e2e3 = I_4, the unit of the duality component it already uses (kappa I B_3), numbers read in span{1, I}; no bare i remains.'
  open_problem: op.generic-weighted-limit
  note: >-
    The new content is the limit at a non-flat Taub point. The Taub region of Taub-NUT is a vacuum Bianchi IX
    field (two equal scale factors) in synchronous gauge whose approach toward t = t_+ shrinks one scale factor
    linearly in the proper time while the other two tend to a constant, so its Kasner weights tend to the Taub
    point (0, 0, 1). Its Hubble-normalised values converge, but not to the Taub Kasner model: on the shrinking
    axis the value is -B_3 + kappa e1e2 = -(1 - kappa I) B_3, kappa = t_+/l = cot(phi/2) with phi the argument of
    the complex mass m + il, because the rotation term of the slices' connection on that axis is of the same
    order as the expansion; on the other two axes the values tend to zero. So at a non-flat Taub point the
    residue acquires a duality (pseudoscalar) component fixed by the NUT parameter; the value of kappa is a
    computed observation and is not interpreted here. The values generate a one-dimensional algebra. For the
    first attack line of the problem (extend the billiard-invariant holonomy limit near the Taub point) this is a
    second, non-flat witness that the return hypothesis of clause (iii) of
    synthesis.bkl-bounce-invariant-holonomy-and-bound cannot be dropped; the flat Kasner field (1, 0, 0), recorded
    in synthesis.bkl-bounces-no-framewise-invariant (ii), already shows that. The locus t = t_+ is the Cauchy
    horizon of Taub-NUT, beyond which the field extends analytically into the NUT region (Misner 1963, cited from
    memory, not proved here and not used in (i) to (iv)); read with it, the Taub point is where the
    weighted-limit programme meets op.cauchy-horizon-transport, and any extension of clause (iii) near the Taub
    point must exclude such approaches by a dynamical hypothesis (for vacuum Bianchi IX, Ringstrom's curvature
    blow-up theorem, cited from memory, not used). The Taub-NUT metric (Taub 1951; Newman, Tamburino and Unti
    1963) and the Bianchi IX potential (Misner 1969) are cited from memory; the check verifies the field
    equations directly, so neither is a premise. Transport-essential in its object (the Hubble-normalised
    rotation-gauge field), classical in its solution.
---

## formal
Let $\sigma_{1}, \sigma_{2}, \sigma_{3}$ be the left-invariant one-forms of $SU(2)$ with $d\sigma_{1} = -\sigma_{2}\wedge\sigma_{3}$ and cyclically, and let a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) have derived metric $N^{2}dT^{2} - \sum_{l}a_{l}(T)^{2}\sigma_{l}^{2}$ with $N = a_{1}a_{2}a_{3}$, physical orthonormal frame $e_{0}$, $e_{l}$ dual to $N\,dT$, $a_{l}\sigma_{l}$, $B_{l} = e_{0}e_{l}$, $I = e_{0}e_{1}e_{2}e_{3}$, $\alpha_{l} = \log a_{l}$, $C = \alpha_{1}'\alpha_{2}' + \alpha_{2}'\alpha_{3}' + \alpha_{3}'\alpha_{1}'$, and $G^{-1}(\xi, \eta) = \sum\xi_{l}\eta_{l} - \tfrac12(\sum\xi_{l})(\sum\eta_{l})$.
\begin{enumerate}
\item[(i)] \emph{(Diagonal Bianchi IX in harmonic time.)} The field equations $\mathcal{R}(a) = 0$ hold if and only if $\alpha_{l}'' = -\sum_{m}G^{-1}_{lm}\,\partial V/\partial\alpha_{m}$ and $C = V$, with $V = \tfrac14\sum_{l}e^{4\alpha_{l}} - \tfrac12\sum_{i<j}e^{2(\alpha_{i} + \alpha_{j})}$. The rotation-gauge field has $\Omega(e_{0}) = 0$ and, with $H_{k} = \alpha_{k}'/N$ and $\mu_{i} = a_{i}/(a_{j}a_{k})$,
\[
\Omega(e_{k}) \;=\; -H_{k}B_{k} + \tfrac12(\mu_{i} + \mu_{j} - \mu_{k})\,e_{i}e_{j} \qquad ((i, j, k) \text{ cyclic}).
\]
\item[(ii)] \emph{(Taub-NUT.)} For constants $m$ and $l > 0$ put $U(t) = (-t^{2} + 2mt + l^{2})/(t^{2} + l^{2})$ and $t_{\pm} = m \pm \sqrt{m^{2} + l^{2}}$. On $t_{-} < t < t_{+}$ (where $U > 0$) the scale factors $a_{1} = a_{2} = \sqrt{t^{2} + l^{2}}$, $a_{3} = 2l\sqrt{U}$ with $dT = dt/(2lU(t^{2} + l^{2}))$ solve the equations of (i): this is the Taub region of the Taub-NUT field, with derived metric $U^{-1}dt^{2} - (2l)^{2}U\sigma_{3}^{2} - (t^{2} + l^{2})(\sigma_{1}^{2} + \sigma_{2}^{2})$.
\item[(iii)] \emph{(The limit at $t_{+}$.)} Let $\tau$ be the proper time to the locus $t = t_{+}$, reached at finite $\tau$, with $\tau$ increasing away from it as in Definition \claimref{obj.interior.weighted-blow-up-hubble-normalisation-admissible}. As $\tau \to 0$ the Kasner weights $\tau H_{l}$ tend to the Taub point $(0, 0, 1)$ and the Hubble-normalised values converge:
\[
\widehat\Omega_{\tau}(e_{1}),\ \widehat\Omega_{\tau}(e_{2}) \to 0, \qquad \widehat\Omega_{\tau}(e_{3}) \to -B_{3} + \kappa\,e_{1}e_{2} = -(1 - \kappa I)B_{3}, \qquad \kappa = \frac{t_{+}}{l} = \cot\frac{\varphi}{2},
\]
with $\varphi = \arg(m + Il) \in (0, \pi)$. The limit values generate the one-dimensional Lie algebra $\R(1 - \kappa I)B_{3}$, and the error relative to the Taub Kasner model $-B_{3}\otimes\hat\theta^{3}$ tends to $\kappa IB_{3}\otimes\hat\theta^{3} \neq 0$.
\item[(iv)] \emph{(Consequence.)} The approach never returns close to a Kasner model with $1 \le u \le 2$, and the conclusion of clause (iii) of \claimref{synthesis.bkl-bounce-invariant-holonomy-and-bound} (accumulation values generating $\Lambda^{2}W$) fails for it: the return hypothesis cannot be dropped, as the flat Kasner field $(1, 0, 0)$ of \claimref{synthesis.bkl-bounces-no-framewise-invariant}(ii) already shows; Taub-NUT is a non-flat witness. Its one-dimensional algebra is the Taub point's $\R B_{3}$ rotated by the duality factor $1 - \kappa I$, which is absent for the flat Kasner field ($\kappa I B_{3}$ is the slices' rotation term).
\end{enumerate}
The sign of $\kappa$ against $I$ depends on the orientation of $\sigma$ relative to the frame and on the sign of $l$; its magnitude does not. The locus $t = t_{+}$ is the Cauchy horizon of Taub-NUT (Misner 1963, cited from memory, not proved here and not used in (i) to (iv)).

## technical
Taub-NUT's Taub region is an exact vacuum solution with the symmetry of the three-sphere and two equal scale factors. In the synchronous gauge of its homogeneous slices the approach to $t = t_{+}$ shrinks one direction linearly while the other two stay finite, so its Kasner weights tend to the Taub point of the Kasner circle. The normalised connection converges there, but not to the flat Kasner value: on the shrinking axis it is the boost along that axis plus a rotation in the plane of the other two, a complex boost $-(1 - \kappa I)B_{3}$, because the slices' connection on that axis is of the same order as the expansion. The coefficient $\kappa$ is the cotangent of half the argument of the complex mass $m + Il$ (numbers are read in $\mathrm{span}\{1, I\}$, $I = e_{0}e_{1}e_{2}e_{3}$), so the NUT parameter appears in the limit as a duality component. One element generates a one-dimensional algebra, not $\Lambda^{2}W$; this is a second, non-flat witness, after the flat Kasner field, that the bounce-invariant holonomy result needs its return hypothesis. The locus reached is the Cauchy horizon of Taub-NUT, beyond which the field continues (cited from the literature, not proved here).

## lay
Near the special direction-pattern where only one direction collapses, the simplest model is empty flat space seen from a moving family of observers. This result looks at a genuinely curved solution, Taub-NUT, that reaches the same pattern. Its rescaled gravitational field settles to a boost combined with a twist, where the flat model has no twist, and the size of the twist is set by the solution's two charges, its mass and its NUT parameter. The field there produces only a single transformation, not every Lorentz transformation. In the literature the place reached is a horizon beyond which spacetime continues, not a true singularity.

## one-liner
On the Taub region of Taub-NUT, a vacuum field in synchronous gauge, the Hubble-normalised rotation-gauge field converges at $t = t_{+}$ to the Taub point with values $(0, 0, -(1 - \kappa I)B_{3})$, $\kappa = t_{+}/l = \cot(\varphi/2)$, $\varphi = \arg(m + Il)$, not to the Taub Kasner model, and generates a one-dimensional algebra; the Taub point there is a Cauchy horizon (Misner 1963, cited from memory).
