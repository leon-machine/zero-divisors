# Items for the GTG provers (from the apply agents)

Decided by Leon on 7 November 2026 (DECISIONS.md, "Leon's answers" 1: apply all of category A and the routine items).
Each is a formal correction or wording on an entity in gtg_1/2/3.txt; apply it in your version bump, with the
evidence in your extraction note (or a separate maintainer_pass_decisions note: by maintainer-2026-11-07, date
'2026-11-07', one sentence plus the evidence). Written by AP1.

## A3 (gtg_3) synthesis.positive-structure-and-natural-scale-actions-do-not-select-the-almost-einstein-scale (formal (ii), proof (ii), check)
- Defect: sign slip. The entity writes $\sqrt{|g|}\,\mathcal{R} = -6\varphi\Box\varphi$, the restricted action
  $\int(6\,\eta(\partial\varphi,\partial\varphi) - 2\Lambda\varphi^4)$ and the Euler-Lagrange equation
  $\Box\varphi = -\tfrac23\Lambda\varphi^3$, and the proof says "the store's convention flips it, which changes nothing below",
  false for $\Lambda \ne 0$. It contradicts synthesis.twistor-flat-fields-give-nordstrom-not-einstein (i).
- Evidence (reconciler, checked exactly; R03 v/r03_checks.py): the store-sign scalar of $\varphi^2\eta$ is
  $6\Box\varphi/\varphi^3$ ($\Box = \partial_t^2 - \nabla^2$); for the stored de Sitter scale $\sigma = 1 - \Lambda Q/12$,
  $\varphi = 1/\sigma$: $\Box\sigma = -\tfrac23\Lambda$, $(\partial\sigma)^2 = \Lambda^2 Q/36$, so
  $\Box\varphi = -\Box\sigma/\sigma^2 + 2(\partial\sigma)^2/\sigma^3 = +\tfrac23\Lambda\varphi^3$.
- Fix (R03's text): formal (ii) and proof (ii): $\sqrt{|g|}\,\mathcal{R} = 6\varphi\Box\varphi$ (store sign), restricted action
  $\int(-6\,\eta(\partial\varphi,\partial\varphi) - 2\Lambda\varphi^4)$ up to boundary terms, Euler-Lagrange equation
  $\Box\varphi = \tfrac23\Lambda\varphi^3$ (the trace $\mathcal{R} = 4\Lambda$), and in the proof "the index convention's scalar
  is $-\mathcal{R}$" in place of "changes nothing below". The $\Lambda = 0$ counter-models and every conclusion are unaffected.
  check.py: docstring and label to the store sign; if an assertion encodes $-\tfrac23\Lambda$ or $-6\varphi\Box\varphi$ as the
  store-sign value, fix it exactly, then runcheck and check4 on a proposals/ copy (delete after). Kind: restatement.

## A6 (gtg_1) synthesis.killing-horizon-value-factor-is-the-generator-boost (iii), (iv)
- Defect: the sign of $\kappa$ needs $\beta(r_h) = +1$, which the proof assumes and the formal ($\beta^2 = 1 - f$) does not say.
- Evidence (R02 pg.py, exact): $(K\cdot D)K = \beta(r_h)f'(r_h)/2\,K$, so $\kappa = f'/2$ only for $\beta(r_h) = +1$. For de Sitter
  that is the contracting chart (past cosmological horizon, $-H$); the GTG dictionary's expanding chart ($\beta = -rH$) gives $+H$
  on the future horizon.
- Fix: in (iv) "$\beta = +\sqrt{1 - f}$" (in place of "$\beta(r)^2 = 1 - f(r)$"); "$-H$ for de Sitter in this chart, which contains
  the past cosmological horizon (the expanding chart gives $+H$ on the future one)"; in (iii) "for either sign of $\kappa$ (future
  and past horizons)" in place of "(the eternal hole's horizon and the cosmological horizon)". Same in the proof and technical
  level where they repeat it. Kind: restatement.
- AP2 also has D2 on this entity (repoint holds_given to synthesis.null-vacuum-on-a-horizon-generator); AP2 writes that item here.

## A11 (gtg_1) synthesis.macdowell-mansouri-is-the-frozen-point-reduction-of-five-dimensional-chern-simons (iii)
- Already applied by the forms rewriter at version 3 ("$F = -\mathcal{W}$, $\mathcal{W}$ the Weyl map in the store's sign",
  $\mathcal{W}(\sigma) = +2M/r^3\,\sigma$; $48m^2$ unchanged). Nothing to do; keep that text.

## G6 (gtg_2) synthesis.series-wald-entropy-changes-without-flux-on-local-horizons, proof (i)
- Defect: proof (i) evaluates on "the bifurcation sphere of a Schwarzschild-de Sitter hole", while the formal is on a
  cross-section of the horizon locus (the GTG dictionary's bifurcation rule).
- Fix (R03 B): "on a cross-section $\{t = t_0, r = r_b\}$ of the horizon locus in the Painleve-Gullstrand chart (both null second
  fundamental forms vanish on the Killing horizon)". Wording in the proof; no version change on its own.

## D2 (gtg_1) synthesis.killing-horizon-value-factor-is-the-generator-boost: repoint the premises of a geometric statement (written by AP2)
- Decision (DECISIONS D2, routine; Leon's answer 1): holds_given (c1, c2, L, P, R, N+) reaches this geometric result through
  synthesis.boost-evolution-on-generators-is-one-unitary-group@4, synthesis.affine-cell-boost-spreads-without-scrambling@3
  and synthesis.positive-null-energy-gives-r-premises@7, which it cites only for the weight-1/2 dilation of the generator
  (proof (iii): the value factor e^{-kappa t/2} with u -> e^{kappa t}u preserves the canonical kernel; "the dilation D_{kappa t}").
  synthesis.null-vacuum-on-a-horizon-generator@1 (i) states exactly that, premise-free: among the dilations
  psi(u) -> e^{lambda w0} psi(e^lambda u) exactly those with Re w0 = 1/2 preserve the anticommutator, so beta_t is an
  automorphism, and beta_t nu_a beta_{-t} = nu_{e^{kappa t} a}.
- Fix: in derivations/main/uses replace those three pins by `synthesis.null-vacuum-on-a-horizon-generator@1`; in the formal,
  technical and proof text cite \claimref{synthesis.null-vacuum-on-a-horizon-generator}(i) where the dilation or the value
  factor's weight is cited (the formal's "the boost B_{kappa t} of the generator plane of Theorem boost-evolution (ii)" can
  keep boost-evolution as a text mention without an edge, or cite null-vacuum (i)); in check.py change
  premise("synthesis.boost-evolution-on-generators-is-one-unitary-group") (lines 139 and 309) and
  premise("synthesis.affine-cell-boost-spreads-without-scrambling") (line 310) to
  premise("synthesis.null-vacuum-on-a-horizon-generator") (keep one call per function), then runcheck (E404 otherwise).
  This drops (N+) and the boundary-mode premises from its holds_given. Note: affine-cell is now at version 4 (AP2, B1
  consequence: a uses edge became a mention), so if you keep any pin to it, pin @4.

## H5 (notation, routine, optional at your bump). R01 item 5
- synthesis.cosmological-horizon-completed-pair (gtg_1) (iii): "up to a phase" and a bar on a number with no unit named;
  the boundary-mode object uses hat-I. Fix: name the unit of the phase (span{1, J} or the hat-I of the boundary-mode object,
  whichever the clause uses) in one parenthesis.
- synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet (gtg_1): rho and U are normalised differently
  from its companion collapse-in-vacuum (rho = r - 2M, U = -rho e^{rho/2M} there against rho = r/2M,
  U = -e^{-kappa t}(s - 1)e^{s^2/2 + s} here). Fix: one sentence stating this entity's normalisation and that the
  companion's differs. No content change.
