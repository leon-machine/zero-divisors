---
id: synthesis.no-spin-independent-curvature-level-set-carries-the-count-to-slow-kerr
kind: claim
version: 1
title: 'Slow Kerr (0 < a <= 4 rho/5): no spin-independent modulus level set gives A/4 exactly'
status: proved
region: synthesis
subject: entropy
tags: [kerr, mode-counting, boundary-modes, no-go]
proposed_by:
  kind: ai
  session: 2026-11-10-phase1
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-10-phase1
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - interior.imported-kerr-schild-form-kerr-gauge@2
  - interior.complex-scale-inverse-cube-killing-spinor@6
  - synthesis.imported-kerr-surface-gravity-entropy@2
  - singularity.stretched-singularity-count@8
  - scrambling.epoch-modular-period-two-unknowns-become@6
  - synthesis.kerr-ring-count-misses-area-law@6
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_level_set_determinant
- kind: check
  ref: check.py::check_determinant_in_the_store_product
- kind: check
  ref: check.py::check_regime_and_bracket_bounds
- kind: check
  ref: check.py::check_quarter_power_bounds
- kind: check
  ref: check.py::check_count_ratio
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.kerr-ring-count-misses-area-law
  - synthesis.c1-c2-forms-forced-one-number
  - synthesis.cutoff-count-is-not-a-local-density-on-sds
extraction:
  open_problem: op.kerr-ring
  note: >-
    Attack item 2 of op.kerr-ring, the regime the stored ring count leaves out (small spin, where the cutoff locus is
    a closed spacelike surface between the horizon loci); that result records the qualitative behaviour there as
    argued, and this one proves it with two-sided bounds and for every level set of the modulus of the curvature
    scale, not only the Planck one. Scope: level sets of the modulus M|z|^{-3} only. On Kerr an algebraic curvature
    scalar can also depend on the phase of the complex scale (the Kretschmann scalar is a multiple of the scalar part
    of its square), so criteria that use the phase are not covered; and the regime is a <= 4 rho/5 with rho <= M/3,
    so with the stored ring count (a >= 2 rho_c^2) the window between is still untreated. The comparison is of the
    ratio Q(M,a)/Q(M,0), in which the density cancels, because at a = 0 the literal count meets the area law only at
    leading order in rho/2M. Inputs from the literature are those of the imported Kerr Fact (surface gravity, area,
    Bekenstein-Hawking entropy). The determinant lemma of clause (2) is stated for a general Killing-invariant surface r = R(u) and proved in the Kerr-Schild gauge alone (cofactor rule and the rank-one rule); it is the same expression as clause (2) of the stored ring count, which states it for rho <= a, and it is proved here directly, so the sampled determinant in the check is a consistency check. The bounds on the integral are elementary and are in the proof; the integral itself
    is not evaluated in closed form. Transport-absent: the computation uses the Kerr gauge field and the counting
    premises, not the completion. Intended citation, filed in the same session and not cited here: the result that
    the Schwarzschild count does not determine its restatement in horizon data.
---

## formal
Let $0 < a < M$ and take the Kerr gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) in the Kerr-Schild gauge of Fact \claimref{interior.imported-kerr-schild-form-kerr-gauge}, with the notation of Theorem \claimref{synthesis.kerr-ring-count-misses-area-law}: gauge field $\hb(b) = b + H\,(b\cdot k)\,k$, $H = Mr/\Sigma$, $\Sigma = r^{2} + a^{2}u^{2} = |z|^{2}$, $z = r - I_{4}au$, oblate coordinates $(t, r, u, \phi)$ of the flat background, $u = \cos\theta$, horizon loci $r_{\pm} = M \pm \sqrt{M^{2} - a^{2}}$, and curvature scale of modulus $|\mathfrak M| = M|z|^{-3}$ (Proposition \claimref{interior.complex-scale-inverse-cube-killing-spinor}). Fix $\rho$ with $\rho \le M/3$ and let $0 < a \le \tfrac45\rho$; put $\varepsilon = a^{2}/\rho^{2} \le \tfrac{16}{25}$ and $\delta = \tfrac52\,a^{2}/(\rho(2M - \rho))$. The Planck level set of Postulate \claimref{singularity.c1-curvature-cutoff}, $\rho = \rho_{c} = (2M)^{1/3}$, is in this range when $M \ge 8$.
\begin{enumerate}
\item \emph{(Where the level set is.)} On the sheet $r > 0$ the level set $|z| = \rho$ of the curvature scale is the surface $r = R(u) := \sqrt{\rho^{2} - a^{2}u^{2}}$, $u \in [-1, 1]$, times the orbits of $\partial_{t}$ and $\partial_{\phi}$. It is closed and lies strictly between the horizon loci: $r_{-} \le a^{2}/M < \tfrac35\rho \le R(u) \le \rho < M \le r_{+}$. At $a = 0$ it is the Schwarzschild slice $r = \rho$.
\item \emph{(Determinant lemma, and the geometry of the level set.)} Let $r = R(u)$, $u \in (-1, 1)$, be any surface invariant under the two Killing flows, in any region where $\Sigma \neq 0$, and let $h$ be the metric the derived metric induces on it in the coordinates $(t, u, \phi)$: the Gram matrix of the physical tangent vectors $\hb^{-1}(\partial_{t})$, $\hb^{-1}(\partial_{u} + R'\partial_{r})$, $\hb^{-1}(\partial_{\phi})$, in the source's signature $(-,+,+,+)$. Then, with $\Delta(r) = r^{2} - 2Mr + a^{2}$,
\[
\det h \;=\; -\Sigma\,\bigl[\Delta(R) + (1 - u^{2})\,R'^{2}\bigr] ,
\]
identically in $M$, $a$, $u$, $R$ and $R'$, and also with $\partial_{t}$ replaced by any Killing flow $\partial_{t} + \Omega\,\partial_{\phi}$, $\Omega$ constant. In the store's product, which reverses the sign of every product, the Gram determinant is $+\Sigma[\Delta(R) + (1 - u^{2})R'^{2}]$. On the level set of item 1, $\Sigma = \rho^{2}$ and $R' = -a^{2}u/R$, so
\[
\det h \;=\; \rho^{2}\,B(u), \qquad B(u) \;=\; R\,(2M - R) - a^{2} - \frac{(1 - u^{2})\,a^{4}u^{2}}{R^{2}} ,
\]
and $(1 - \delta)\,R\,(2M - \rho) \le B \le R\,(2M - \rho)$ with $B > 0$, so the level set is spacelike, as the Schwarzschild slice is. With $R = \rho\cos\psi$, $au = \rho\sin\psi$ this is the expression of Theorem \claimref{synthesis.kerr-ring-count-misses-area-law}(2), which states it for $\rho \le a$; here it is proved directly, for $\rho > a$ as well.
\item \emph{(Its volume rate.)} The three-volume per unit Killing time, $V'(M, a, \rho) = 2\pi\int_{-1}^{1}\sqrt{\det h}\,du$, satisfies
\[
(1 - \delta)\Bigl(1 - \frac{\varepsilon}{3}\Bigr) \;\le\; \frac{V'(M, a, \rho)}{V'(M, 0, \rho)} \;\le\; 1 - \frac{\varepsilon}{12}, \qquad V'(M, 0, \rho) = 4\pi\rho^{3/2}\sqrt{2M - \rho},
\]
the last being the Schwarzschild slice volume, $8\pi M\sqrt{1 - \rho_{c}/2M}$ at $\rho = \rho_{c}$ (Proposition \claimref{singularity.stretched-singularity-count}). More precisely $V'(M, a, \rho)/V'(M, 0, \rho)$ lies between $(1 - \delta)\,G(\varepsilon)$ and $G(\varepsilon)$, $G(\varepsilon) = \tfrac12\int_{-1}^{1}(1 - \varepsilon u^{2})^{1/4}\,du$.
\item \emph{(The count.)} Count $\nu$ modes per Planck cell of the level set over the outer modular period $2\pi/\kappa_{+}$ (the rule of Proposition \claimref{singularity.stretched-singularity-count} with the epoch of Theorem \claimref{scrambling.epoch-modular-period-two-unknowns-become}, read with the Kerr surface gravity of Fact \claimref{synthesis.imported-kerr-surface-gravity-entropy}): $N = \nu V'\cdot 2\pi/\kappa_{+}$, and write $Q(M, a) = N/(A_{+}/4) = 2\nu V'/\sqrt{M^{2} - a^{2}}$. Then
\[
\frac{Q(M, a)}{Q(M, 0)} \;\le\; \frac{1 - \varepsilon/12}{\sqrt{1 - a^{2}/M^{2}}} \;<\; 1 ,
\]
whatever $\nu$. So no density $\nu$ and no level set $\rho(M) \le M/3$ chosen independently of the spin give the Kerr entropy $A_{+}/4$ both at $a = 0$ and at any $a$ with $0 < a \le \tfrac45\rho(M)$. The area law needs $V'(M, a, \rho)/V'(M, 0, \rho) = \sqrt{1 - a^{2}/M^{2}}$, a function of $a/M$; the count's ratio is at most $1 - a^{2}/(12\rho^{2})$ and, up to the factor $1 - \delta$, is the function $G(a^{2}/\rho^{2})$. The equality asked for is exact. At the stored density $\nu = 1/16\pi$ and $\rho = \rho_{c}$ the Schwarzschild count is $Q(M, 0) = \sqrt{1 - \rho_{c}/2M}$, equal to $1$ at leading order only. By item 3 the spin lowers $Q$ by a factor between $(1 - \delta)(1 - \varepsilon/3)/\sqrt{1 - a^{2}/M^{2}}$ and $(1 - \varepsilon/12)/\sqrt{1 - a^{2}/M^{2}}$: for $a/\rho$ bounded below this is a miss at leading order in $1/M$ (the deficit is at least $1 - (1 - \varepsilon/12)/\sqrt{1 - a^{2}/M^{2}}$, which tends to $\varepsilon/12$ as $\rho/M \to 0$), and for $a/\rho \to 0$ the count agrees with $A_{+}/4$ at leading order. At the Planck level set with $a = \tfrac45\rho_{c}$ the ratio $Q(M, a)$ is at most $\tfrac{71}{75}/\sqrt{1 - a^{2}/M^{2}}$ times its Schwarzschild value $Q(M, 0)$ for every $M \ge 8$, while the spin there is $a/M = \tfrac45(2M)^{1/3}/M$, which tends to zero as $M$ grows.
\end{enumerate}
The regime is that of slow rotation in the sense $a \le \tfrac45\rho$; with Theorem \claimref{synthesis.kerr-ring-count-misses-area-law}, which treats $a \ge 2\rho_{c}^{2}$, the literal cutoff count is shown to miss the area law at both ends of the spin range, and the window $\tfrac45\rho_{c} < a < 2\rho_{c}^{2}$ between is not treated. Only level sets of the modulus of the curvature scale are covered, and only level sets with $\rho \le M/3$. Reading Postulate \claimref{singularity.c1-curvature-cutoff} on Kerr through the modulus is the reading of Theorem \claimref{synthesis.kerr-ring-count-misses-area-law}; it is one choice among the algebraic curvature scalars of Theorem \claimref{synthesis.c1-c2-forms-forced-one-number}, which on Kerr are not functions of $|z|$ alone.

## technical
For a Kerr field of mass $M$ and spin parameter $a$, take the surface on which the modulus of the curvature scale, $M|z|^{-3}$, has a fixed value, $|z| = \rho$, with $\rho \le M/3$ and $0 < a \le \tfrac45\rho$. It is a closed spacelike surface between the two horizon loci, $r = \sqrt{\rho^{2} - a^{2}u^{2}}$, and the determinant of its induced metric is $\rho^{2}[R(2M - R) - a^{2} - (1 - u^{2})a^{4}u^{2}/R^{2}]$ exactly, the case $R' = -a^{2}u/R$ of the general formula $-\Sigma[\Delta(R) + (1 - u^{2})R'^{2}]$ for a Killing-invariant surface $r = R(u)$.

Its three-volume per unit Killing time is at most $1 - a^{2}/(12\rho^{2})$ times the Schwarzschild value $4\pi\rho^{3/2}\sqrt{2M - \rho}$ and at least $(1 - \delta)(1 - a^{2}/(3\rho^{2}))$ times it, $\delta = \tfrac52 a^{2}/(\rho(2M - \rho))$. Counted with any fixed density over the outer modular period, the ratio of the count to $A_{+}/4$ is therefore smaller than its Schwarzschild value by the factor $(1 - a^{2}/12\rho^{2})/\sqrt{1 - a^{2}/M^{2}} < 1$ or more.

So, in this regime of slow rotation and for level sets of the modulus of the curvature scale with $\rho \le M/3$, no density and no level set chosen independently of the spin reproduce the Kerr entropy exactly at zero and at nonzero spin: the count depends on the spin through $a/\rho$ (and weakly through $\rho/M$), the area law through $a/M$. The equality refuted is exact; the Schwarzschild count itself meets the area law only at leading order. For $a/\rho$ bounded below the miss is of leading order in $1/M$, at least $\varepsilon/12$ in the limit; for $a/\rho \to 0$ the lower bound shows the count still agrees with $A_{+}/4$ at leading order. For the Planck level set $\rho_{c} = (2M)^{1/3}$ this holds for $M \ge 8$. With the stored result for $a \ge 2\rho_{c}^{2}$ the literal count misses the area law at both ends of the spin range; the window between is not treated.

## lay
The series counts a black hole's quantum modes on an inner surface where the gravitational field strength reaches a fixed value, and for a non-rotating hole that count matches the hole's entropy. An earlier result showed the same rule fails for fast-spinning holes. This one treats very slow rotation, and any fixed value of the field strength, not only the Planck one: the counting surface is then a slightly flattened closed surface inside the hole, and its volume, hence the count, drops with spin on a far smaller scale of spin than the entropy does. So no version of the rule of the kind covered here (surfaces on which the size of the field strength is fixed, lying deep inside the hole, at spins small compared with the size of that surface) reproduces the entropy of rotating holes exactly, and the shortfall is a few per cent when the spin parameter is comparable to the surface's size, however large the hole. For still smaller spin the shortfall shrinks to nothing. Rules that use the direction as well as the size of the field strength, and a middle range of spins, are not covered.

## one-liner
For Kerr with $0 < a \le \tfrac45\rho$, $\rho \le M/3$, the level set $|z| = \rho$ of the curvature scale's modulus has volume rate at most $1 - a^{2}/(12\rho^{2})$ times Schwarzschild's, and at least $(1 - \delta)(1 - a^{2}/(3\rho^{2}))$ times it, so no spin-independent density and level set of this kind give $A_{+}/4$ exactly at zero and nonzero spin; only modulus level sets with $\rho \le M/3$ are covered, the window $\tfrac45\rho_{c} < a < 2\rho_{c}^{2}$ is untreated, and for $a/\rho \to 0$ the count still agrees with $A_{+}/4$ at leading order.
