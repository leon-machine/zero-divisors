---
id: synthesis.crossing-transport-tipler-threshold-sharp
kind: claim
version: 5
title: 'The Tipler condition is sharp at a null crossing'
status: proved
region: synthesis
subject: interior
tags: [tractors, horizons, limits, null-directions]
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
  role: 'consistency pass, unit of the complex exponents named'
  version: 5
  source: maintainer pass 2026-11-07 (consistency)
review: draft
derivations:
- name: main
  uses:
  - interior.imported-tractor-connection@2
  - synthesis.tractor-transport-weak-null-crossing@4
  - interior.sign-fixed-internally@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_subsystem
- kind: check
  ref: check.py::check_commutator
- kind: check
  ref: check.py::check_euler
- kind: check
  ref: check.py::check_power_profiles
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - interior.filtration-cauchy-horizon-read-literature
  - interior.imported-mass-inflation-stability
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The complex exponents 1/2 +- I omega used an undeclared I; they are numbers of span{1, I_4}, the field theory unit (conventions U1), now written so; notation only.'
  maintainer_pass_2:
    by: maintainer-2026-10-24
    date: '2026-10-24'
    note: 'Gauge Theory Gravity wording pass at Leon''s request (2026-10-24): curved-spacetime and conformally-flat wording restated in terms of the gravitational field on flat spacetime (a nonvanishing gravitational field; the Weyl part of the field strength vanishes, the conformally flat derived metric kept as a reading; global content read on an atlas of flat charts patched by gauge transformations). Wording only; statements, proofs'' arguments and checks unchanged. Version 3 -> 4.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the tractor transport is that of the Cl(2,4) gauge field of a gravitational field on flat spacetime read in the splitting of the derived metric; content unchanged. Check untouched.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  open_problem: op.cauchy-horizon-transport
  note: >-
    Sharpens synthesis.tractor-transport-weak-null-crossing in the pure-radiation case R = 0: its gauge
    equation y'' = nu^2 S y is the transport equation of the n-component <n, mu> of the middle slot, so
    the hypotheses of that theorem are a trichotomy with no gap for S of fixed sign. Sign convention: the
    store's Schouten tensor is minus the Bailey-Eastwood-Gover one (interior.sign-fixed-internally; along a
    null geodesic a parallel tractor has sigma'' = P(l, l) sigma), so focusing matter (null energy condition)
    has S <= 0 here, and S >= 0 is the defocusing, energy-condition-violating sign. In particular the
    spherical scalar-field term reads P_VV = -4 pi (d_V phi)^2 in the store's sign (the stored theorem's note
    writes it with the opposite sign); only |S| enters the integrability statements. The case R != 0 is not covered here: the forcing terms
    nu <R, mu> + (<n, R> sigma)' enter w'' and need R with integrable derivative along the curve (argued,
    not proved). Reading of the literature, argued and cited from memory, not part of the proof: in
    spherical symmetry with a massless scalar field the singular part has |P_VV| = 4 pi (d_V phi)^2
    (P_VV = -4 pi (d_V phi)^2 in the store's sign), so
    |S| in L^1 along the ray is exactly d_V phi in L^2 along it, the H^1 threshold of Christodoulou's
    formulation of strong cosmic censorship. For asymptotically flat Reissner-Nordstrom with Price-law
    tails (field decaying like v^-p in advanced time, V = -exp(-kappa_- v)) the profile is
    |V|^-2 (log 1/|V|)^-q with q = 2p + 2 > 1: case (b), transport defined modulo one nilpotent direction,
    divergence in the bottom slot. For Reissner-Nordstrom-de Sitter with exponential decay rate alpha
    the profile is |V|^(2 beta - 2) with beta = alpha/kappa_- (Cardoso, Costa, Destounis, Hintz and
    Jansen, Phys. Rev. Lett. 120 (2018) 031103; Hintz and Vasy 2017): case (a), unique transport, exactly
    when beta > 1/2, the regime in which that literature finds strong cosmic censorship violated in its
    H^1 form; case (b) for beta <= 1/2. Neither class reaches case (c), which needs a Tipler-strong null
    singularity; there, with the physical (focusing) sign, the n-component of the middle slot has no finite
    nonzero limit, and at the inverse-square edge it is crushed to zero, the tractor form of Tipler's
    volume crush (crushing in general is not proved). An exact realisation of case (b) is the conformally
    flat plane-wave class, filed alongside, synthesis.plane-wave-weak-null-crossing-null-shell-ambiguity,
    whose model profile is beta = 1/4 with the focusing sign. Remaining hypotheses (continuity of Levi-Civita transport, comparability of affine
    parameter and Kruskal V, no surface layer) are those of the stored theorem and stay unverified for
    these solutions; for Kerr (Dafermos-Luk, vacuum) S = 0 and the question is the Levi-Civita one.
    Transport-convenient: the content is the Jacobi equation of a null congruence read in the tractor slots.
---

## formal
Let $\gamma$, $s_c$, $n$, $\nu = n(\gamma') \neq 0$ and the parallel frame be as in Proposition \claimref{synthesis.tractor-transport-weak-null-crossing}, with tractor transport $x' = Ax$, $A = E_{\gamma'} + N_{\Sch(\gamma',\cdot)}$, in the splitting of the scale $g$, the derived metric of the gravitational field (Fact \claimref{interior.imported-tractor-connection} (on flat spacetime the $\Cl(2,4)$ gauge field $\Omega_{T}$ of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection})), and suppose the Schouten tensor is pure radiation along $\gamma$:
\[
\Sch(\gamma', \cdot) \;=\; S\,\nu\,n \qquad (R = 0),
\]
with $S$ locally integrable off $s_c$ and of fixed sign near $s_c$. In the store's sign convention focusing matter has $S \le 0$. For a parallel tractor $x = (\sigma, \mu, \rho)$ put $w := \ip{n}{\mu}$.
\begin{enumerate}
\item \emph{(The gauge equation is a transport equation.)} $w' = -\nu\rho$ and $\rho' = -\nu S w$, so $w'' = \nu^2 S\,w$ and $\rho = -w'/\nu$: the equation $y'' = \nu^2 S y$ of the stored theorem is the transport equation of the $n$-component of the middle slot.
\item \emph{(Trichotomy, on a side of $s_c$.)} (a) If $\int |S| < \infty$, every $w$ and $\rho$ has a finite limit at $s_c$. (b) If $\int |S| = \infty$ but $\int |s - s_c|\,|S| < \infty$, every $w$ has a finite limit, and $\rho$ is unbounded unless $w(s_c) = 0$, a condition cutting out a line in the $(w, \rho)$-data. (c) If $\int |s - s_c|\,|S| = \infty$, no $w$ has a finite nonzero limit at $s_c$, so no solution of $y'' = \nu^2 S y$ stays positive with a positive limit and the removal of the stored theorem is unavailable. For $S \ge 0$ (defocusing) the tractors with $w$ bounded have $(w, \rho)$-data on at most a line, and for all others $\ip{n}{\mu}$ is unbounded. Hence the Tipler-type condition is exactly the threshold between a divergence confined to the bottom slot $\rho$ (removable modulo $\exp(\R N_n)$) and the loss of the middle slot's null component.
\item \emph{(The edge profile.)} For $S = \pm C|s - s_c|^{-2}$, $C > 0$, the solutions are $w = |s - s_c|^{e}$ with $e(e - 1) = \pm\nu^2 C$. Defocusing ($+$): $e = k$ or $1 - k$ with $k > 1$, so $w$ is unbounded off a line. Focusing ($-$): $\mathrm{Re}\,e \in (0, 1)$ for both roots (real if $\nu^2 C \le \tfrac14$, equal to $\tfrac12 \pm I_{4}\omega$ (numbers read in $\mathrm{span}\{1, I_{4}\}$) with $\omega^2 = \nu^2 C - \tfrac14$ otherwise), so every $w$ tends to $0$ (the null component of the middle slot is crushed) while $\rho = -w'/\nu$ diverges like $|s - s_c|^{\mathrm{Re}\,e - 1}$; for $\nu^2 C > \tfrac14$ every solution has zeros accumulating at $s_c$. When $e$ is real, $y = |s - s_c|^{e}$ gives $|f| = e/(\nu|s - s_c|)$, and in the variables $(1 - fN_n)x$ the coefficient is $E_{\gamma'} + f\,D$ with $D = [E_{\gamma'}, N_n]$ in the Levi part $\mathfrak g_0$, $D^3 = \nu^2 D$, eigenvalues $0, \nu, -\nu$, each twice: the residual singularity is a simple pole in $\mathfrak g_0$ with residue eigenvalues $0, \pm e$.
\item \emph{(Profile classes.)} For $|S| = C|s - s_c|^{2\beta - 2}$, $C, \beta > 0$: the Tipler integral is finite for every $\beta$; case (a) holds iff $\beta > \tfrac12$; for $\beta < \tfrac12$ the gauge function behaves as $|f| \sim \nu C|s - s_c|^{2\beta - 1}/(1 - 2\beta)$, the bottom-slot divergence rate. For $|S| = C|s - s_c|^{-2}(\log 1/|s - s_c|)^{-q}$, $q > 0$: $S$ is never integrable; case (b) iff $q > 1$, case (c) iff $q \le 1$.
\end{enumerate}

## technical
Along a causal geodesic crossing a null hypersurface where the Schouten tensor is pure radiation along a parallel null covector $n$, the tractor transport, that of the $\Cl(2,4)$ gauge field of the gravitational field on flat spacetime, contains a closed two-dimensional subsystem: the $n$-component $w = \ip{n}{\mu}$ of the middle slot and the bottom slot $\rho$ obey $w' = -\nu\rho$, $\rho' = -\nu S w$. So the Jacobi-type equation that the stored crossing theorem uses as a gauge device is itself the transport equation of $w$. For $S$ of fixed sign this gives a sharp trichotomy: $S$ integrable means unique transport; $S$ not integrable but $|s - s_c|S$ integrable means $w$ continuous and $\rho$ divergent, the stored case with its one-parameter nilpotent ambiguity; $|s - s_c|S$ not integrable means no $w$ has a nonzero limit, so the null component of the middle slot is lost: it diverges for the defocusing sign and, at the inverse-square edge, is crushed to zero for the focusing sign, which is the physical one in the store's convention. At the edge the residual singularity, after the best nilradical gauge, is a simple pole in the Levi part. Case (b) is realised exactly by the plane-wave gravitational fields with vanishing Weyl part (filed alongside, synthesis.plane-wave-weak-null-crossing-null-shell-ambiguity; profile $\beta = 1/4$). For power-law profiles $|s - s_c|^{2\beta - 2}$ the transport is unique exactly when $\beta > 1/2$; for logarithmically corrected inverse-square profiles the Tipler condition holds exactly when the log power exceeds one. The checks verify the subsystem identities on five frames, the cube relation and eigenvalue multiplicities of the commutator, the gauge identity, the Euler (both signs, including the complex exponents) and Frobenius solutions in exact exponent arithmetic, and the integrals.

## lay
Inside a charged or rotating black hole, perturbations pile up at the inner horizon. The series asks whether its basic transport operation still makes sense across that surface. An earlier result showed it does, up to one unavoidable ambiguity, provided a certain integral of the tidal stress stays finite. This result shows that the condition is exactly right: when the integral is finite the ambiguity is the only damage, and when it is infinite the damage spreads to a more important part of the transported object, which then has no finite nonzero value at the horizon: it blows up when the matter defocuses light, and in the sharpest focusing case it is squeezed to nothing. The same equation that the earlier proof used as a trick turns out to be the equation of motion of one part of the transported object. If the perturbation profiles reported in the literature on charged black holes apply along the crossing path (which, like the other technical hypotheses of the earlier result, is not checked here), the transport survives there, and it is fully unique exactly in the regime where those papers find the inner horizon to be continuable.

## one-liner
For pure-radiation Schouten tensor $S\nu n$ along a crossing geodesic, $w = \ip{n}{\mu}$ obeys $w'' = \nu^2 S w$ with $\rho = -w'/\nu$, so for $S$ of fixed sign the transport is unique iff $S \in L^1$, diverges only in $\rho$ iff $|s - s_c|S \in L^1$, and otherwise loses the middle slot's null component (divergent for the defocusing sign, crushed to zero at the inverse-square edge for the focusing one).
