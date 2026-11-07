---
id: synthesis.scale-free-rung-potentials-need-the-flat-physical-branch
kind: claim
version: 2
title: 'Scale-free rung potentials need the flat physical branch'
status: proved
region: synthesis
subject: standard-model
tags: [symmetry-breaking, undetermined-input, gauge-fields, frozen-point]
proposed_by:
  kind: ai
  session: 2026-11-01-weak-scale
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
  - synthesis.rung-field-on-the-lift-locus@3
  - synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus@4
  - synthesis.rung-unit-transverse-to-norm@3
  - synthesis.rung-field-charged-scalar-sum-rule@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_quartic_invariants_restrict_to_five_couplings
- kind: check
  ref: check.py::check_family_potential_scaling_and_frame_bound
- kind: check
  ref: check.py::check_gildener_weinberg_admissibility
- kind: check
  ref: check.py::check_flat_ray_tree_masses
- kind: check
  ref: check.py::check_d_term_with_norm_quartic_is_not_admissible
- kind: check
  ref: check.py::check_rung_unit_is_the_conformal_dilatation
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus
  - synthesis.rung-unit-second-free-number
extraction:
  maintainer_pass_qft_full:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 1 -> 2, by Leon''s decision of 2 November 2026 on the weak scale: a marked note records the transmutation branch, reached through the flat physical branch, as excluded under the decided coupling reading; the tree-level statements are unchanged.'
  open_problem: op.rung-unit
  note: >-
    The classical-scale-invariance reading of the problem's first and second lines of attack: can the weak
    scale come from no constant at all, by dimensional transmutation (Coleman-Weinberg, Gildener-Weinberg),
    rather than from the level xi? The tree-level half is settled here exactly. A rung potential with no
    dimensionful constant is a U(2)-invariant quartic form; on the null-lift locus it is a quadratic form in
    (N, m) plus terms of order H^2 N, H^2 m and H^4 that the locus itself induces, five couplings in all, and
    the level-zero D-term is one of them. The joint rescaling of the field and of H maps the lift family to
    itself and the potential by s^4, so the potential sees the rung unit only through the frame t = 2 eta.
    Clause (5) restates the stored X_mu = B_{1/mu} o X_1 as X_mu(x) = mu X_1(x/mu): the null-plane boost is the
    standard dilator of the conformal model (Hestenes; Doran and Lasenby, from memory), so the rung unit is the
    would-be scalon; this is a reading, not a new structural result. At a
    charge-preserving critical point on the physical half the coefficient K_+ = a + b - e of the physical
    branch is bounded by 2(|d| + |f|) e^-t + |K_-| e^-2t, so a tree-level vacuum at v/H ~ 2 x 10^44 (H^2 =
    Lambda/3; v/H_0 is about 1.7 x 10^44, the two differing by sqrt(Omega_Lambda), a factor of order one) needs
    K_+ to vanish to about 10^-88 of |d| + |f| (10^-176 of |K_-| when d = f = 0): tree level gives v/H of
    order a ratio of couplings unless the
    potential sits on the Gildener-Weinberg condition K_+ = 0. On the cone Q = 0 (the H -> 0 limit) the flat
    physical ray is admissible (potential bounded below by zero) exactly when e >= 0 and 2a >= e; then the
    neutral mode is massless at tree level and the charged pair has (2a - e) v^2; the mirror ray is flat too
    exactly when e = 0, so a c*-even potential leaves the two branches degenerate at tree level (under the
    per-sector reading (not su(2)_R covariant), where only beta couples to fermions, the mirror branch has tiny
    fermion entries; under the su(2)_R-covariant completion they are of order |alpha|). The
    level-zero D-term plus kappa N^2 is flat only at kappa = -(g^2 + g'^2)/8, where the charged mass squared
    is M_W^2 - M_Z^2 < 0 and the potential is negative inside the cone, so the W = kappa N^2 family is not a
    transmutation endpoint; a scale-free moment-map quartic (kappa' m^2 with kappa' <= e/2 - g'^2/8) is
    required. The level xi, a constant of dimension mass squared, is absent by hypothesis: transmutation
    trades it for the running of K_+, which this result does not compute. Transport-convenient: the locus,
    the family and the mirror are the series'; the classification, the flat direction analysis and the
    dilator reading are standard. The same stored boost is read as the flow of 2 T_3R at real rapidity on the
    ten in synthesis.majorana-scale-not-carried-by-rung-frame-boost; the two readings agree on
    the rung plane. Literature cited from memory: S. Coleman and E. Weinberg, Phys. Rev. D 7
    (1973) 1888; E. Gildener and S. Weinberg, Phys. Rev. D 13 (1976) 3333.
---

## formal
In the setting of \claimref{synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus}: the complexified rung summand with $c = \sum_{a}(\alpha_{a}v_{a} + \beta_{a}w_{a})$, $Q(c) = \alpha^{\mathsf T}\beta$, $N = \tfrac12(|\alpha|^{2} + |\beta|^{2})$, $m = \tfrac12(|\alpha|^{2} - |\beta|^{2})$, the slot mixing $U(2)$, the conjugation $c \mapsto c^{*}$, the null-lift locus $L = \{Q(c) = -H^{2}\}$, $H^{2} = \Lambda/3$, the lift family $c_{\lambda}$ with $\eta = \log(\lambda/H)$, $t = 2\eta$, and its physical half $\lambda \ge H$ (on which, read through $c^{*}$, every tree Dirac entry is $\lambda$, \claimref{synthesis.rung-field-on-the-lift-locus}(5)), the gauge masses $M_{W}^{2} = \tfrac12 g^{2}N$, $M_{Z}^{2} = \tfrac12(g^{2} + g'^{2})N$, and $v^{2} = 2N$. Call a potential \emph{scale-free} if it is a real $U(2)$-invariant polynomial on $\mathcal{R}_{\C}$ homogeneous of degree four. Masses are Hessians on the locus divided by the kinetic coefficient of the stored Hermitian term.
\begin{enumerate}
\item \emph{(Five couplings.)} The real scale-free potentials are $V = \sum_{i}k_{i}I_{i}$ over $I_{1..10} = |\alpha|^{4}, |\beta|^{4}, |\alpha|^{2}|\beta|^{2}, |\alpha|^{2}\operatorname{Re}Q, |\alpha|^{2}\operatorname{Im}Q, |\beta|^{2}\operatorname{Re}Q, |\beta|^{2}\operatorname{Im}Q, \operatorname{Re}Q^{2}, \operatorname{Im}Q^{2}, |Q|^{2}$. On $L$,
\[
V = aN^{2} + bm^{2} + eNm + H^{2}(dN + fm) + c_{0}H^{4},
\]
with $a = k_{1} + k_{2} + k_{3}$, $b = k_{1} + k_{2} - k_{3}$, $e = 2(k_{1} - k_{2})$, $d = -(k_{4} + k_{6})$, $f = -(k_{4} - k_{6})$, $c_{0} = k_{8} + k_{10}$; the conjugation changes $(e, f)$ to $(-e, -f)$. The D-term action is scale-free exactly when its level $\xi$ vanishes, and then $(a, b, e, d, f, c_{0}) = (\tfrac18 g^{2}, \tfrac18 g'^{2}, 0, 0, 0, -\tfrac18 g^{2})$.
\item \emph{(The frame, and the flat condition.)} Along the family $V(c_{\lambda}) = H^{4}\bigl[a + c_{0} + (a + b)\sinh^{2}t - \tfrac{e}{2}\sinh 2t + d\cosh t - f\sinh t\bigr]$, and the joint rescaling $(c, H) \mapsto (sc, sH)$ maps $c_{\lambda}$ to $c_{s\lambda}$ and $V$ to $s^{4}V$: a scale-free potential sees the rung unit only through the frame $t$. Let $K_{\pm} = a + b \mp e$. If $K_{+} < 0$, $V$ decreases without bound along the physical half. At every critical point of $V$ along the family with $t \ge 0$,
\[
K_{+} \le 2(|d| + |f|)e^{-t} + |K_{-}|e^{-2t}, \qquad \text{and for } K_{+} > 0,\quad e^{t} \le \frac{2(|d| + |f|) + \sqrt{K_{+}|K_{-}|}}{K_{+}};
\]
since $N^{*}/H^{2} = \cosh t \le e^{t}$, a charge-preserving tree-level critical point at $N^{*} = \tfrac12 v^{2}$, $N^{*}/H^{2} \approx 2 \times 10^{88}$ (with $H^{2} = \Lambda/3$; about $1.4 \times 10^{88}$ if $H$ is read as $H_{0}$, the two differing by a factor of order one), needs $K_{+} \le 2(|d| + |f|)H^{2}/N^{*} + |K_{-}|H^{4}/N^{*2}$. The half $t \le 0$ is the same with $K_{+}$ and $K_{-}$ exchanged and $f \mapsto -f$.
\item \emph{(The Gildener-Weinberg flat ray, on the cone $Q = 0$.)} On the cone $L_{0} = \{Q = 0\}$, the limit $H \to 0$, with orbit cone $|m| \le N$, a scale-free potential is $V_{4} = aN^{2} + bm^{2} + eNm$. It is nonnegative on the cone and vanishes on the physical ray $m = -N$ if and only if $K_{+} = 0$, $e \ge 0$ and $2a \ge e$; the mirror ray $m = N$ then carries $V_{4} = 2eN^{2}$, flat as well exactly when $e = 0$ (so for every $c^{*}$-even potential). On the flat physical ray of $L_{0}$ the neutral mode is massless, the charged pair has $m_{\pm}^{2} = 2(2a - e)N = (2a - e)v^{2}$, and the two do not mix.
\item \emph{(The norm quartic fails.)} For the level-zero D-term plus $\kappa N^{2}$ the physical ray is flat only at $\kappa = -\tfrac18(g^{2} + g'^{2})$, and there $m_{\pm}^{2} = -\tfrac12 g'^{2}N = M_{W}^{2} - M_{Z}^{2} < 0$ and $V < 0$ inside the cone: the potential is unbounded below and the family $W = \kappa N^{2}$ is not a flat-ray endpoint. With a moment-map quartic $\kappa'm^{2}$ and $eNm$ added the flat ray is admissible exactly when $e \ge 0$, $2a \ge e$, which requires $\kappa' \le \tfrac12 e - \tfrac18 g'^{2}$.
\item \emph{(The rung unit is the dilatation; a restatement.)} With the lift's null pair $n_{0}' = -w$, $n_{\infty}' = 2v$ and $X_{\mu}(x) = \mu n_{0}' + x + \tfrac{Q(x)}{2\mu}n_{\infty}'$ (\claimref{synthesis.rung-unit-transverse-to-norm}), $X_{\mu}(x) = \mu X_{1}(x/\mu)$, which restates the stored $X_{\mu} = B_{1/\mu}\circ X_{1}$ through the standard fact that the null-plane boost is the dilator of the conformal model: a change of the rung unit is the conformal dilatation of the ground point by $1/\mu$, and the flat ray of (3) is the orbit of the rung unit.
\end{enumerate}

\emph{Note (the transmutation branch excluded, 2 November 2026).} The flat physical branch of (iii) is the route by which a scale-free rung potential would reach the weak scale through one loop. Under the decided coupling reading of the rung field (the $\su(2)_{R}$-covariant completion with complex symmetric family matrices), that transmutation branch is recorded as excluded, by the three strikes collected in Theorem \claimref{synthesis.transmutation-of-the-rung-field-needs-a-charged-pair-near-450-gev}: the diphoton rate, neutral B-meson mixing and strong coupling of the quartics at a few TeV. The branch with a level is the working branch. The tree-level statements here are unchanged.

## technical
A potential for the rung field with no dimensionful constant is a quartic form invariant under the slot mixing. On the locus where the frozen point's lift is null it reduces to a quadratic form in the Hermitian norm and the hypercharge moment map, plus terms of order $H^{2}$ and $H^{4}$ that the locus induces: five couplings. Rescaling the field together with the cosmological scale maps the lift family to itself, so such a potential sees the rung unit only through the frame. At tree level the frame it selects is a ratio of couplings: a tree-level vacuum at the weak scale, about $10^{88}$ in units of $H^{2}$, needs the coefficient of the physical branch to vanish to that precision. Exact vanishing is the Gildener-Weinberg condition, under which the physical branch is a flat direction and quantum corrections choose the scale by dimensional transmutation; the flat direction is the orbit of the rung unit, which in the conformal model is the standard dilatation of the ground point (a restatement of the stored boost). On the cone $Q = 0$, the limit of small $H$, the flat direction is bounded below exactly when two inequalities hold; then the neutral mode is massless at tree level and the charged pair has mass squared $(2a - e)v^{2}$. A potential even under the rung conjugation leaves the mirror branch flat too; under the per-sector reading (not su(2)_R covariant) the fermion entries there are tiny, under its su(2)_R-covariant completion they are not. The level-zero D-term with a norm quartic, the form behind the $117$ GeV point, cannot be made flat without a tachyonic charged pair, $M_{W}^{2} - M_{Z}^{2}$: a quartic in the moment map is needed.

## lay
Could the weak scale come from nothing, as the strong-interaction scale does, by the slow running of a coupling? The first condition is a potential for the series' Higgs candidate with no built-in mass scale. This result lists all such potentials and shows that, without quantum effects, they put the weak scale at most a modest factor from the cosmological scale, unless one combination of couplings vanishes almost exactly. When it vanishes exactly the potential is flat along the very direction that changes the weak scale, which in the series' geometry is a rescaling; quantum corrections then pick the scale. The flat direction is stable only for some couplings, and the simplest choice, the one behind an earlier prediction of a charged scalar near 117 GeV, is not among them: it makes the charged scalar's mass squared negative.

## one-liner
A scale-free rung potential is $aN^{2} + bm^{2} + eNm + H^{2}(dN + fm)$ on the null-lift locus and sees the rung unit only as the frame; a tree-level weak-scale vacuum needs $a + b - e$ to vanish to about $10^{-88}$, and on the cone $Q = 0$ the Gildener-Weinberg flat ray is admissible iff $e \ge 0$, $2a \ge e$, with tree masses $m_{h} = 0$, $m_{\pm}^{2} = (2a - e)v^{2}$, and the D-term with $\kappa N^{2}$ fails with $m_{\pm}^{2} = M_{W}^{2} - M_{Z}^{2}$.
