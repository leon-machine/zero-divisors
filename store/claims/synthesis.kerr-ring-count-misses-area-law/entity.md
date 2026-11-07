---
id: synthesis.kerr-ring-count-misses-area-law
kind: claim
version: 6
title: 'For Kerr the literal curvature-cutoff count misses the area law'
status: proved
region: synthesis
subject: entropy
tags: [kerr, mode-counting, boundary-modes]
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
  role: 'GA rewrite (Kerr-Schild gauge field; unit named I_4)'
  version: 6
  source: maintainer pass 2026-11-07 (consistency)
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - interior.imported-kerr-schild-form-kerr-gauge@2
  - interior.complex-scale-inverse-cube-killing-spinor@6
  - synthesis.kerr-ring-double-cover-data@3
  - singularity.stretched-singularity-count@7
  - scrambling.epoch-modular-period-two-unknowns-become@6
  - synthesis.imported-kerr-surface-gravity-entropy@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_kerr_schild_data
- kind: check
  ref: check.py::check_tube_determinant
- kind: check
  ref: check.py::check_averages_and_bound
- kind: check
  ref: check.py::check_regime_and_ctc
- kind: check
  ref: check.py::check_count_ratio
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - interior.duality-monodromy-fibration-over-ring
  - scrambling.mode-count
  - scrambling.area-law-test
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The Kerr field is stated by its Kerr-Schild gauge field hb(a) = a + H(a.k)k with derived metric g(a,b) = a.b - 2H(a.k)(b.k) (Q(k) = 0), the oblate-coordinate line element in the source''s signature (-,+,+,+) kept as its labelled component reading; Delta = Sigma g^{rr} is read as -Sigma Q(hb^T(nabla r)) in the store''s product and the induced metric on the tube as the Gram matrix of the physical tangent vectors; the unnamed unit I of z = r - I a u, z = rho e^{I psi} and rho(c + I s) is written I_4, the spacetime pseudoscalar that is the unit I of the Walker-Penrose scale in interior.complex-scale-inverse-cube-killing-spinor (numbers in span{1, I_4}); the component computations of the proof are Gram-matrix computations and stay; the mathematics is unchanged.'
  maintainer_pass_2:
    by: maintainer-2026-10-24
    date: '2026-10-24'
    note: 'Gauge Theory Gravity wording pass at Leon''s request (2026-10-24): curved-spacetime and conformally-flat wording restated in terms of the gravitational field on flat spacetime (a nonvanishing gravitational field; the Weyl part of the field strength vanishes, the conformally flat derived metric kept as a reading; global content read on an atlas of flat charts patched by gauge transformations). Wording only; statements, proofs'' arguments and checks unchanged. Version 4 -> 5. Referee fixes to the GTG wording pass (2026-10-24): ''a gravitational field of nonvanishing field strength'' (gauge-independent) in place of ''a nonvanishing gravitational field''; global content read on several charts of flat spacetime, each with its own gravitational field, glued by displacement and rotation gauge transformations (complexified charts for the half-flat manifold, the conformal compactification for a conformal boundary); ''not carried by the store''s one-chart fields'' in place of ''no single gravitational field carries''; equivalence statements weakened where the old text was weaker; remaining curved-spacetime phrases in lay text restated. Wording only.'
  correction:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'W503: the lay level and one-liner now state the spin threshold a >= 2(2M)^{2/3} of the formal statement as a condition (assuming, if). Version 2 -> 3.'
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Maintainer pass: the Kerr surface gravity and the Bekenstein-Hawking entropy A_+/4, cited from memory, are now the imported Fact synthesis.imported-kerr-surface-gravity-entropy, added to uses and cited in the statement, proof and check. Version 1 -> 2.'
  open_problem: op.kerr-ring
  note: >-
    Attack 2 of op.kerr-ring (repeat the slice count over the ring and compare with the Kerr entropy), run
    as a refutation test of the counting rule. The rule tested is the Schwarzschild one read literally:
    (C1) at the locus where the curvature scale reaches the Planck value, read with the complex scale
    M|z|^{-3} of interior.complex-scale-inverse-cube-killing-spinor; (C2) with nu per Planck cell; the
    epoch a period of the horizon (under (IC), the outer modular period). Outcome: the count scales as
    M^{5/3} at fixed a/M, the Kerr entropy as M^2. Inputs from the literature, now the imported Fact synthesis.imported-kerr-surface-gravity-entropy: the Kerr surface gravity
    kappa_+ = (r_+ - r_-)/(2(r_+^2 + a^2)) and the Bekenstein-Hawking entropy A_+/4 of the Kerr horizon
    (Bardeen, Carter and Hawking 1973; Hawking 1975). Clause (3) needs only that the epoch is proportional
    to M at fixed a/M and that the entropy is A_+/4; the explicit ratio in (4) uses kappa_+. The horizon
    area A_+ = 4 pi (r_+^2 + a^2) and the horizon radii are computed from the stored Kerr-Schild form.
    Argued, not proved here: for a well below rho_c the (C1) locus is a closed surface on each sheet with
    volume rate close to the Schwarzschild 8 pi M, so as a function of spin at fixed M the count drops from
    order M to order M^{2/3} between a of order M^{1/3} and a of order M^{2/3}, while the entropy changes
    by a relative amount of order a^2/M^2; for a solar-mass hole that window is a spin J/M^2 of order
    10^{-25}. Reading: the (C1) locus of a rotating hole lies beyond the Cauchy horizon, the region that
    the stored mass-inflation import (interior.imported-mass-inflation-stability) makes unstable, and its
    far-sheet half lies in Carter's region of closed timelike curves; so either the boundary modes of a
    rotating hole are not on the curvature-cutoff locus, or the density or epoch rule changes with spin
    and must supply a factor of order M^{1/3}. Transport-absent: the computation uses the Kerr geometry
    and the counting premises, not the completion. It does not touch the fibration conjecture.
  flags:
  - 'beyond one flat chart: the r < 0 sheet of Kerr (the double cover through the disc bounded by the ring)'
  maintainer_pass_gtg:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity (FLAG): the Kerr field on flat spacetime in the Kerr-Schild gauge, its derived metric in the statement''s declared signature (-,+,+,+), the oblate eta being the flat background; horizons -> horizon loci; induced metric from the derived metric. The double cover and the r < 0 sheet through the disc carry the Section 14 flag sentence and a flags entry. Items 1-4 unchanged; proof given a pointer.'
---

## formal
Let $0 < a \le M$ and take the Kerr gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) in the Kerr-Schild gauge of Fact \claimref{interior.imported-kerr-schild-form-kerr-gauge}; its gauge field is $\hb(a) = a + H\,(a\cdot k)\,k$, $\hb^{-1}(a) = a - H\,(a\cdot k)\,k$, with $k$ a null vector field of the flat background, so the derived metric is $g(a,b) = \hb^{-1}(a)\cdot\hb^{-1}(b) = a\cdot b - 2H\,(a\cdot k)(b\cdot k)$ (as $Q(k) = 0$). In oblate coordinates $(t, r, u, \phi)$ of the flat background, $u = \cos\theta$, and in the source's signature $(-,+,+,+)$, which reverses the sign of every product, this reads (in components)
\[
g = \eta + 2H\,k\otimes k,\quad
\eta = -dt^2 + \tfrac{\Sigma}{P}\,dr^2 + \tfrac{\Sigma}{1 - u^2}\,du^2 + P(1 - u^2)\,d\phi^2,\quad
k = -dt - \tfrac{\Sigma}{P}\,dr + a(1 - u^2)\,d\phi,
\]
with $H = Mr/\Sigma$, $\Sigma = r^2 + a^2u^2 = |z|^2$, $P = r^2 + a^2$, $z = r - I_4au$ the double-cover coordinate of Proposition \claimref{synthesis.kerr-ring-double-cover-data} (a number of $\mathrm{span}\{1, I_4\}$, $I_4$ the spacetime pseudoscalar, the unit $I$ of the Walker-Penrose scale $r - Ia\cos\theta$ of Proposition \claimref{interior.complex-scale-inverse-cube-killing-spinor}), and horizon loci at $r_\pm = M \pm \sqrt{M^2 - a^2}$, the roots of $\Delta = r^2 - 2Mr + a^2 = -\Sigma\,Q(\hb^{T}(\nabla r))$ (the store\'s product), where the physical gradient of $r$ is null (in components, source\'s signature, $\Delta = \Sigma\, g^{rr}$). Read the curvature-cutoff postulate with the Kerr scale $|\mathfrak M| = M|z|^{-3}$ of Proposition \claimref{interior.complex-scale-inverse-cube-killing-spinor}: the stretched singularity is $2M|z|^{-3} = 1$, i.e. $|z| = \rho_c := (2M)^{1/3}$ in Planck units, as $r_c = (2M)^{1/3}$ for Schwarzschild in Proposition \claimref{singularity.stretched-singularity-count}. Assume $a^2 \ge 8M\rho_c$ (equivalently $a \ge 2\rho_c^2$; it forces $M \ge 32$). Put $\varepsilon = \rho_c^2/a^2$ and $\delta = 2M\rho_c/a^2 \le \tfrac14$.
\begin{enumerate}
\item \emph{(Where the locus is.)} On the double cover the locus is the tube $z = \rho_c e^{I_4\psi}$, $\psi \in [0, 2\pi)$, times the orbits of $\partial_t$ and $\partial_\phi$; both sheets ($\cos\psi > 0$ and $< 0$) meet it, glued across the disc. It lies in $|r| \le \rho_c < a^2/2M \le r_-$: beyond the inner horizon. In $r_- \le r \le r_+$ the curvature scale never reaches the Planck value, since there $|z| \ge r_- > \rho_c$.
\item \emph{(Its geometry.)} In the coordinates $(t, \psi, \phi)$ the metric $h$ that the derived metric induces on the tube of any radius $\rho \le a$, the Gram matrix of the physical tangent vectors $\hb^{-1}(\partial_t), \hb^{-1}(\partial_\psi), \hb^{-1}(\partial_\phi)$ in the source's signature, satisfies, identically,
\[
\det h \;=\; -\rho^4\Bigl[\,1 + \frac{\rho^2}{a^2}\cos 2\psi - \frac{2M\rho}{a^2}\cos^3\psi\,\Bigr],
\]
also with $\partial_t$ replaced by any Killing flow $\partial_t + \Omega\partial_\phi$. At $\rho = \rho_c$ the bracket is at least $\tfrac12$, so the tube is timelike, unlike the spacelike slice $r = r_c$ of Schwarzschild; at $\psi = \pi$ ($r = -\rho_c$, $u = 0$) one has $g(\partial_\phi, \partial_\phi) = \rho_c^2 + a^2(1 - \rho_c^2) < 0$, a closed timelike orbit of the axial Killing field.
\item \emph{(Its volume rate.)} The three-volume of the tube per unit Killing time is
\[
V' \;=\; 4\pi^2\rho_c^2\,(1 - \eta), \qquad 0 \le \eta \le \frac{\varepsilon^2}{4} + \frac{5\delta^2}{32},
\]
on the double cover (both sheets), against $V' = 8\pi M$ for Schwarzschild. Reading the rule on Kerr is an extension: on a timelike three-surface, counting Planck cells per unit Killing time over both sheets is a choice (the Schwarzschild slice is spacelike and the reading is unambiguous there); counting one sheet only replaces $V'$ by $\tfrac12 V'(1 + O(\delta))$ and leaves every exponent below unchanged. Under the count rule of Proposition \claimref{singularity.stretched-singularity-count}, $\nu$ modes per Planck cell over an epoch $\Delta t$, the count is $N = \nu V'\Delta t$. The horizon cross-section has area $A_+ = 4\pi(r_+^2 + a^2) = 8\pi M r_+$. If $\Delta t = \tau M$ with $\tau$ depending on $a/M$ only (every period of the Kerr horizons is of this form), then
\[
\frac{N}{A_+/4} \;=\; \frac{2\pi\nu\,\tau\,\rho_c^2\,(1 - \eta)}{r_+},
\]
which at fixed $a/M \in (0, 1)$ tends to zero as $M^{-1/3}$; reaching $A_+/4$ would need $\Delta t$ of order $M^{4/3}$, which is no horizon period.
\item \emph{(With the series' calibration.)} With the epoch at the outer modular period $\Delta t = 2\pi/\kappa_+$, $\kappa_+ = (r_+ - r_-)/(2(r_+^2 + a^2))$ (Fact \claimref{synthesis.imported-kerr-surface-gravity-entropy}), and $\nu = 1/16\pi$ (the value that Proposition \claimref{scrambling.epoch-modular-period-two-unknowns-become} derives from the Schwarzschild area law under (IC)),
\[
\frac{N}{A_+/4} \;=\; \frac{\pi}{2}\,\frac{\rho_c^2\,(1 - \eta)}{\sqrt{M^2 - a^2}} \;=\; \frac{\pi}{2}\,\frac{(2M)^{2/3}(1 - \eta)}{\sqrt{M^2 - a^2}} ,
\]
against exactly $1$ for Schwarzschild, where $V' = 2\pi/\kappa = 8\pi M$. So the identity $V' = 2\pi/\kappa$ behind the Schwarzschild count (the stretched singularity keeping the horizon's clock) does not hold on Kerr in this regime, and the counting rule read literally on Kerr contradicts the Kerr entropy. For small spin ($\rho_c > r_-$) the locus is instead a closed surface between the horizons, spacelike as in Schwarzschild; that regime is not treated here.
\end{enumerate}

\emph{Beyond one flat chart.} The $r < 0$ sheet of Kerr, reached through the disc bounded by the ring (the double cover on which items 1 to 4 place and count the tube), is global and is not carried by a single gravitational field $(\hb, \Omega)$ on flat spacetime; the statements above that hold on the invertible region are in GTG, and the $r < 0$ sheet is read on the manifold assembled from the derived metric's charts.

## technical
Read the Schwarzschild counting rule literally on the Kerr field on flat spacetime (Kerr-Schild gauge), for spin $a \ge 2(2M)^{2/3}$: the boundary modes sit where the curvature scale $M|z|^{-3}$ reaches the Planck value, $\nu$ per Planck cell, counted over a horizon period. For $a \ge 2(2M)^{2/3}$ that locus is a thin tube $|z| = \rho_c = (2M)^{1/3}$ around the ring on the double cover, lying entirely beyond the inner horizon locus; between the horizon loci the field strength stays sub-Planckian. The tube is timelike, and its far-sheet half contains closed timelike orbits of the axial Killing field. The induced metric has the closed-form determinant $-\rho^4[1 + (\rho^2/a^2)\cos 2\psi - (2M\rho/a^2)\cos^3\psi]$, whose correction terms average to zero, so the volume per unit Killing time is $4\pi^2\rho_c^2$ up to a relative error at most $\varepsilon^2/4 + 5\delta^2/32$: of order $M^{2/3}$, independent of $a$, where Schwarzschild has $8\pi M$. With any epoch proportional to $M$ the count then grows as $M^{5/3}$ while the Kerr entropy $A_+/4 = 2\pi M r_+$ grows as $M^2$; with the series' calibration the ratio is $(\pi/2)(2M)^{2/3}/\sqrt{M^2 - a^2}$ up to that error. Counting one sheet only halves $V'$ at leading order and leaves the exponent unchanged. The Schwarzschild coincidence $V' = 2\pi/\kappa$ fails on Kerr. The exact checks verify the Kerr-Schild data, the determinant identity on rational points of the tube, the circle averages and the square-root bounds, the regime inequalities, and the count ratio at sample holes, where it halves each time $M$ grows by $8$ at fixed $a/M$. Its $r < 0$ sheet, reached through the disc bounded by the ring, is global: no single gravitational field on flat spacetime carries it, so that part is read on several charts of flat spacetime, each carrying its own gravitational field, glued on overlaps by displacement and rotation gauge transformations.

## lay
The series counts a black hole's hidden quantum modes on the surface deep inside where the curvature reaches the Planck scale, and for a non-rotating hole that count gives exactly the known black hole entropy. This result repeats the count, read literally, assuming the hole spins faster than a very small threshold. There the Planck-curvature surface is a thin tube around the ring singularity, lying beyond the hole's inner horizon, in a region that is unstable and even contains closed time loops. The tube's size grows only like the two-thirds power of the mass, so the count grows like the mass to the five-thirds power, while the rotating hole's entropy grows like the mass squared. Read literally, the counting rule fails for rotating holes, so at least one of its ingredients must change with spin.

## one-liner
For Kerr, if $a \ge 2(2M)^{2/3}$, the Planck-curvature locus $|z| = (2M)^{1/3}$ is a timelike tube beyond the inner horizon with volume rate $4\pi^2(2M)^{2/3}(1 - \eta)$, so the counting rule read literally gives $N/(A_+/4) = (\pi/2)(2M)^{2/3}(1 - \eta)/\sqrt{M^2 - a^2}$, of order $M^{-1/3}$, against $1$ for Schwarzschild.
