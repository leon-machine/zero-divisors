# Referee F1: blind review of ten new GTG proofs (run 2026-11-07-consistency)

Brief: REFEREE_GTG.md. List: referee_F1.txt. I did not read gtg-*.md or any maintainer_pass_gtg_proof note
before writing the verdicts below (the entity.md files were read for their formal statements, uses and
checked_by; the extraction notes were skipped).

Scratch scripts (own code, not the check functions; lib/GA.py products, lib/gtg.py jets and torsion solver,
Fractions only), copied to `colony/runs/2026-11-07-consistency/work-F1/`:

- `referee_F1_checks.py`: independent recomputations, sections E1 to E10 below; **120 checks, 120 as
  expected** (lines marked "expected False" are mutations, or lines of a proof that are disproved).
- `run_mut.py`: mutation runs of the new check functions on scratch copies (never in store/); it writes the
  copies to `$MUT_DIR` (default /tmp).
- `run_new_checks.py`: runs the twelve new check functions directly (tp_premise configured on store/);
  all twelve pass. No `tp check` run was used.

Original locations: /tmp/claude-0/-home-claude/23cbb9be-73ca-5537-8211-47496476158a/scratch/F1/.

| Entity | Verdict |
|---|---|
| dark-energy.gravity-pre-metric-forces-degenerate-exactly | ACCEPT |
| dark-energy.stelle-west-vector-frozen-point | ACCEPT WITH FIXES (1) |
| synthesis.black-hole-data-do-not-fix-field-equations | ACCEPT (one optional tightening) |
| synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet | ACCEPT WITH FIXES (1, check only) |
| synthesis.cosmological-horizon-completed-pair | ACCEPT |
| synthesis.frozen-point-reduces-the-connection-only-when-infinitely-stiff | ACCEPT WITH FIXES (1) |
| synthesis.killing-horizon-value-factor-is-the-generator-boost | ACCEPT WITH FIXES (2) |
| synthesis.macdowell-mansouri-is-the-frozen-point-reduction-of-five-dimensional-chern-simons | ACCEPT WITH FIXES (2) |
| synthesis.nondiagonal-kasner-residue-weighted-shear | ACCEPT WITH FIXES (1) |
| synthesis.two-frozen-points-conformally-flat | ACCEPT WITH FIXES (1) |

Counts: ACCEPT 3, ACCEPT WITH FIXES 7, REJECT 0. Language scan of all ten proofs: no em dashes, no bare
imaginary unit (every isolated "i" is a clause label), no "curved spacetime", no Pauli or Dirac matrices or
cross products; component expressions appear only as labelled readings or as statement-level data.

---

## 1. dark-energy.gravity-pre-metric-forces-degenerate-exactly: ACCEPT

**The star.** Reading a two-form as a background bivector $F$, the physical field strength is $\hb^T(F)$, its
dual $I\hb^T(F)$, read back by $\hb^{-T}(X) = I\hb(I^{-1}X)/\det\hb$: $\hb^{-T}(I\hb^T F) = I\,\hb\hb^T(F)/\det\hb$,
so with the background orientation ${*}_gF = |\det\hb|^{-1}I\,\mathcal G(F)$, $\mathcal G = \hb\hb^T$,
$g^{\mu\nu} = e^\mu\cdot\mathcal G(e^\nu)$. Correct, including the sign: with $\epsilon_{0123} = +1$ one has
$I(e_c\wedge e_d) = \tfrac12\epsilon_{abcd}e^a\wedge e^b$, so the component star is exactly
$\sqrt{|g|}\,I\,\mathcal G(F)$. E1 recomputes, against my own component star (own Levi-Civita symbol and inverse
metric), on three non-diagonal fields with $\det\hb = -1/14, 1/31, -3/2$: equality of the 6x6 maps; the inverse
adjoint formula; the physical dual read back equals $\mathrm{sgn}(\det\hb)$ times the star (so the $|\cdot|$ is
the orientation normalisation the proof says it is); ${*}^2 = -1$ (from $\mathcal G(I\mathcal G F) =
\det\mathcal G\,IF$, $\det\mathcal G = (\det\hb)^2$, rederived from $\mathcal G^{-1}(B) = I\mathcal G(I^{-1}B)/\det
\mathcal G$ for the symmetric $\mathcal G$); invariance under $\hb\to\lambda\hb$ ($\lambda = 3, 2/5$) and under a
boost rotation gauge; two non-conformal fields with different stars. Mutations $\mathcal G = \hb^T\hb$ and
$\det\hb$ for $|\det\hb|$ fail, as they should.

**The wall.** Argument (3) is valid: if ${*}_g$ had a finite limit, $I\mathcal G_s = |\det\hb_s|{*}_g \to 0$,
contradicting $I\mathcal G_0 \ne 0$. E1 tests a non-diagonal family $\hb_s = C\,\mathrm{diag}(1,s,1,1)\,D$
(not the check's diagonal one): GA star = component star at $s = 10^{-1,-2,-3}$, entries growing by about ten
per decade, $|\det\hb_s|{*} - I\mathcal G_0 = O(s)$, and $I\mathcal G_0$ of rank 3 on bivectors.

**(1).** Bianchi, $\langle F\wedge F\rangle = \nabla\wedge\mathcal C$, the 2/3, and compact algebras as bivectors
of some $\Cl(n,0)$ with the scalar part as an invariant form: correct. The variation now reads
$2\int\nabla\wedge\langle\delta A\wedge F\rangle + 2\int\langle\delta A\wedge D\wedge F\rangle$; the plus sign is the
right one (graded Leibniz for a one-form, $d(\alpha\wedge\beta) = d\alpha\wedge\beta - \alpha\wedge d\beta$); the
component proof at 4160435 had a minus. It is harmless either way, since the term is zero.

**Checks.** The three new functions pass; the cometric-duality check compares against an independent
component star (a real test), and my two mutations of it are caught. The "In components" reading agrees.

## 2. dark-energy.stelle-west-vector-frozen-point: ACCEPT WITH FIXES

**Mathematics.** All correct. E2 recomputes in $\Cl(2,4)$: $Q(X) = 0$, $\langle X,I\rangle = 1$,
$\langle V,I\rangle = 0$, $Q(V) = -3/\Lambda$, slots of $V$ and $W$ ($\Lambda = 3/4, -5/2, 12$);
$\Theta(A) = -\nInf\wedge A + \tfrac\Lambda6\nO\wedge A = A\wedge W$; $(A\wedge W)\cdot\nO = A$;
$(A\wedge W)\cdot I = 0$; $[A\wedge W, B\wedge W] = \tfrac\Lambda3 A\wedge B$; and, for a generic $\Sch$ and
$\Omega$, the slots of $\Omega_T(a)\times Y$ are the Fact's display
$(\nabla\sigma - \mu_a,\ D\mu + g\rho - P\sigma,\ \nabla\rho + P\mu)$. The mutation $+\nInf\wedge A$ gives
$DX = -A$, and it is caught both by mine and by the new check.

**Circularity.** `synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection` uses this entity (@5), and
the Fact `dark-energy.imported-frozen-point-geometry` that this proof uses also *names* that theorem in its
formal text ("The tractor connection is, on flat spacetime, the gauge field ... of Theorem [tractor theorem]").
The derivation avoids the loop in substance. It defines $\Omega_T(a) = \Omega(a) + \Theta(A)$, computes its action
slot by slot, and matches it to the Fact's component display, using only that display and
$P = \tfrac\Lambda6 g$. It says so ("the computation uses nothing else"). The citation in its opening sentence,
however, does not:

- **Fix 2.1.** The opening sentence attributes "tractors as vectors of $\Cl(2,4)$, the tractor connection as a
  $\Cl(2,4)$ gauge field" to Fact `synthesis.imported-gtg-dictionary`. That Fact (v2, clauses (i) to (vi)) says
  nothing about tractors. Replace with: "The proof is in Gauge Theory Gravity: flat spacetime with the
  gravitational field $(\hb,\Omega)$ on its invertible region (physical vectors, derived metric and $D$ as in Fact
  \claimref{synthesis.imported-gtg-dictionary}), and tractors as vectors of $\Cl(2,4)$. That the tractor
  connection is a $\Cl(2,4)$ gauge field is not assumed: the next paragraph derives it from the display of Fact
  \claimref{dark-energy.imported-frozen-point-geometry} alone, and uses neither that Fact's sentence naming
  synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection nor that theorem, which uses the present
  result." (Optional: the dictionary is \claimref'd but not in `uses`; adding it at @2 is harmless, as it has no
  uses of its own.)

**Check.** `check_tractor_gauge_field_slots_and_bracket` tests the computation itself: generic $P$, generic
$\Omega$, the slot readout through $Z\cdot\nO$ and $Z\cdot\nInf$, and the operator commutator against the
commutator product. The "In components" reading agrees.

## 3. synthesis.black-hole-data-do-not-fix-field-equations: ACCEPT

**Wald sign.** Correct. I checked it independently from three sides (E3):

- By C11 and C7, $\mathcal S_\sigma(B) = -\langle B\sigma\rangle\sigma$ is *exactly* the curvature operator whose
  Riemann tensor in the statement's convention, $(-,+,+,+)$ with spheres positive, is $\epsilon_{ab}\epsilon_{cd}$
  ($\epsilon_{tr} = 1$, $\epsilon_{ab}\epsilon^{ab} = -2$). On every frame quadruple,
  $\mathrm{Riem}^\circ_{(+---)}(u,v,w,z) = (w\wedge z)\cdot\mathcal S_\sigma(u\wedge v) = -\epsilon_{uv}\epsilon_{wz}$.
  So $E^{abcd}\epsilon_{ab}\epsilon_{cd} = \tfrac{d}{dt}L(\mathcal R + t\mathcal S_\sigma)$ holds with constant 1,
  and no calibration is needed.
- The Ricci map of $\mathcal S_\sigma$ is $-P_\sigma$ and its scalar is $-2$. So the Einstein term gives
  $-1/8\pi G$ and $S = A/4G$.
- On the component side, $\delta R_{ab} = g^{cd}\epsilon_{ca}\epsilon_{db}$ gives
  $\tfrac{d}{dt}(R_{ab}R^{ab}) = -2(R^t{}_t + R^r{}_r)$ for arbitrary diagonal mixed Ricci.

Mixed components agree between the statement's convention and the store sign, as the formal says.
Reissner-Nordström from the PG gauge field at $r = 5/2 = r_+$ and $9/2$ gives the store Ricci map
$(-q,-q,q,q)$, $q = Q^2/r^4$, so the entropy shift is $4\pi\beta(R^t{}_t + R^r{}_r)A = -8\pi\beta Q^2A/r_+^4$.
Schwarzschild: $\mathcal R = (M/2r^3)(B + 3\sigma B\sigma)$, Ricci-flat, $K = 48M^2/r^6$.

**(i).** The argument for the field equations is valid at the level of the original: every term carries $f_k$,
$\partial f_k$ or $\mathcal P_f$, of degree at least 1 in the Ricci map, or a $D$-derivative of $\mathcal P_f$.

**Check.** The mutation $\mathcal S_\sigma \to -\mathcal S_\sigma$ is caught.

**Optional tightening.** In (ii), replace "(the chain rule, with the sign fixed by the Einstein term and
confirmed against the component contraction)" by "(the chain rule: by Fact
\claimref{synthesis.imported-gtg-dictionary}'s sign identification, $\mathrm{Riem}^{\circ}(u,v,w,z) =
(w\wedge z)\cdot\mathcal S_\sigma(u\wedge v) = -\epsilon_{uv}\epsilon_{wz}$ in $(+,-,-,-)$, so $\mathcal S_\sigma$ is
exactly the curvature operator whose Riemann tensor in the statement's convention is
$\epsilon_{ab}\epsilon_{cd}$)". The calibration is then a consequence, not a step. This is not required: the
proportionality is evident and the Fact fixes the constant.

## 4. synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet: ACCEPT WITH FIXES (check only)

**Proof (ii).** Correct. E4 recomputes it by hand: $\Omega(e_t) = (M/r^2)\sigma_r$ and $\Omega(e_r) = -\beta'\sigma_r$,
both matching the engine's torsion solution; $\hb^{-1}(x') = (\gamma_1 - \gamma_0)/(1+\beta)$, null;
$\Omega(x') = \beta\sigma_r/(2r(1+\beta))$; $D_{x'}k = 0$ at $(M,r) = (1,8), (3/2,3), (1,2)$; and
$(K\cdot D)K = K/4M$ at $r = 2M$. The rest of (i) to (vi) is unchanged from 4160435.

- **Fix 4.1 (check).** In `check_gtg_ingoing_generator_is_affine_and_horizon_rate` the control "the same
  worldline parametrised by t is not affinely parametrised" uses `kt = {(0,): 1, (1,): -1 - beta}`. That is the
  background tangent $e_t - (1+\beta)e_r$, not the physical velocity, which is
  $\hb^{-1}(e_t - (1+\beta)e_r) = \gamma_0 - \gamma_1$ (E4). Replace with
  `kt = {(0,): gtg.Jet.const(1, 4), (1,): gtg.Jet.const(-1, 4)}`. The control still holds:
  $D_{x_t}(\gamma_0 - \gamma_1) = \tfrac{\beta}{2r}(\gamma_0 - \gamma_1) \ne 0$. My mutation run with this
  replacement passes.

## 5. synthesis.cosmological-horizon-completed-pair: ACCEPT

Step 1 is new, and its algebra is right. $\hb^T(\nabla\wedge f^a) = -\nabla\sigma\wedge\gamma^a$ is solved by
$\omega(A) = \nabla\sigma\wedge A$, so $\Omega(a) = (c/\sigma)x\wedge a$ with $c = -\Lambda/6$. The
$x\wedge a$, $x\wedge b$ terms cancel; $2\sigma - cQ(x) = 2$; and with $\hb(B) = \sigma^2B$ one gets
$\mathcal R(B) = \tfrac\Lambda3B$. The C11 reading $-\tfrac\Lambda3(g_{ac}g_{bd} - g_{ad}g_{bc})$ is also right. E5
verifies this through the general dilation of section 10 (with $(s,m,r) = (1,0,\Lambda/6)$) and the C11
reading separately. The frame form of the torsion equation is consistent with C10: for the synchronous
case it reproduces $\omega(\gamma_i) = -H_i\gamma_0\wedge\gamma_i$. The check uses the engine's torsion solution,
and the mutation of the sign of $\Omega$ is caught. Steps 2 to 5 are unchanged.

## 6. synthesis.frozen-point-reduces-the-connection-only-when-infinitely-stiff: ACCEPT WITH FIXES

The GTG change is the setting paragraph: forms as linear maps of physical vectors and bivectors, the store-sign
operator with the Ricci contraction (also with torsion), Weyl square, Euler density, $\mathcal D$. These are
right, and `check_gtg_readings_of_the_curvature_operator` confirms them against the index readings.

- **Fix 6.1.** Proof (i), carried over from the component proof: "$(\nInf\wedge\nO)\cdot\nInf = -\nO$,
  $(\nInf\wedge\nO)\cdot\nO = \nInf$" is wrong. With $(u\wedge w)\cdot Y = u(w\cdot Y) - w(u\cdot Y)$ and
  $\nO\cdot\nInf = 1$, the values are $(\nInf\wedge\nO)\cdot\nInf = \nInf$ and $(\nInf\wedge\nO)\cdot\nO = -\nO$
  (E6: the proof's two values fail, the corrected ones hold). The displayed results
  $DI(a) = \rho a - S(a) + \beta(a)(\nInf - \rho\nO)$ and $DX(a) = a - \beta(a)\nO$ are right, and they follow
  only from the corrected values: the proof's values would give $\beta(\rho\nInf - \nO)$ and $+\beta\nInf$. The
  other four contractions on that line are right.

## 7. synthesis.killing-horizon-value-factor-is-the-generator-boost: ACCEPT WITH FIXES

**Signs.** All correct, and checked by E7 with the engine's torsion-solved field.

- De Sitter with $\beta = +Hr$ ($= +\sqrt{1-f}$): $\beta(r_h) = 1$ and $(K\cdot D)K = -HK$. The stuck radial ray
  at $r_h$ is the outgoing one ($dr/dt = 1 - \beta = 0$), so the chart's horizon is the past cosmological
  horizon, consistent with the dictionary (section 11) and with $\kappa < 0$ for a future-directed $K$ there.
- The expanding chart $\beta = -Hr$: $K = \gamma_0 - \gamma_1$, the ingoing ray is stuck, and $+H$.
  The relation is $(K\cdot D)K = \beta(r_h)\tfrac{f'}{2}K$.
- Schwarzschild-de Sitter ($H^2 = 1/7$, $M = 3/7$): $f(1) = f(2) = 0$, with $\kappa = 2/7$ and $-5/28$.
- Schwarzschild: $1/4$.
- $\Omega(e_t) = -\beta\beta'\sigma_r$ for independent rational $\beta$, $\beta'$.
- At the horizon, $k\cdot m = 1$, $k\wedge m = \sigma_r$, $F_K = -\Omega(e_t) = -\kappa\,k\wedge m$, $K\cdot F_K = \kappa K$
  and $F_K^2 = \kappa^2$.

The check ties $f'$ to the engine: flipping the sign of de Sitter's $f'$ and $\kappa$ together is caught.
(i) to (iii) are unchanged.

- **Fix 7.1 (citation).** Proof (iv) cites Definition (d) for the physical frame vectors of the label
  directions ($\hb^{-1}(e_\vartheta) = r\gamma_2$, ...). Clause (d) is the derived metric. Cite the coframe of
  Fact \claimref{sheaf.gauge-field-cometric}, as written out in singularity.connection-bivector-computed clause 2,
  or state the frame vectors as the field's definition in the labels $(t,r,\vartheta,\varphi)$.
- **Fix 7.2 (citation).** The frame form of the torsion equation is attributed to Fact
  `synthesis.imported-gtg-dictionary`(ii), which states the Levi-Civita derivative and parallel transport, not
  the torsion equation. Cite Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}(f),
  $D\wedge\hb^T(a) = \hb^T(\nabla\wedge a)$, applied to $a = f^a$ with $D = \sum_b\gamma^bD_{\hb(\gamma_b)}$.
- Note (no change asked). The displayed $\omega(\gamma_2)$ and $\omega(\gamma_3)$ carry the polar frame's rotation
  ($\gamma_1\wedge\gamma_2/r$, $\cot\vartheta\,\gamma_2\wedge\gamma_3/r$). This is the constant-frame label reading
  the store already uses in singularity.connection-bivector-computed. $\Omega(e_t)$ and $\kappa$, the content
  of (iv), do not depend on it.

## 8. synthesis.macdowell-mansouri-is-the-frozen-point-reduction-of-five-dimensional-chern-simons: ACCEPT WITH FIXES

The proof's mathematics is unchanged from 4160435, and it is fine. The new language paragraph is accurate.

**Does the new check test anything? No.** `fmul_bg` keeps the grade-additive part of `GA.blade_mul(a, b,
BG5)`. For disjoint blades, that sign is the reordering sign alone, whatever the squares, so `fmul_bg` is the
Grassmann product `fmul` identically (E8: four signatures, identical products). The mutations `BG5 = (7, 3, -2,
5, 11)` and `BG5 = (0, 0, 0, 0, 0)` both **still pass**. Its asserts `fmul_bg(th, th) == fmul(th, th)` are
identities, and `L5 == lovelock(...)` with $L_5 = (3\lambda/Q(V))\epsilon(I,V,F,F)$ repeats
`check_chern_simons_five_form_reduces_to_the_frozen_point_functional`.

- **Fix 8.1.** Remove `check_gtg_reduction_with_base_forms_as_background_multivectors` from `checked_by`, and
  remove the sentence about it from the extraction note. Alternatively, replace it with a check of what the
  reading adds: for a sample polynomial $\Cl(2,4)$ connection on the five-dimensional background, $\nabla\wedge$
  of the transgression form equals $P(F,F,F) - P(F_0,F_0,F_0)$.

**Does the declaration say exactly what remains? No.** It names the transgression and variation formulas "as
theorems about differential forms" as the only stand-in. In the proof, however:

- those formulas are read with the base forms as background multivector fields ($d = \nabla\wedge$, exterior
  product = outer product);
- the two Facts they come from carry no `outside_ga` declaration of their own;
- the remaining component expressions ($C_{abcd}C^{abcd}$, index readings) are permitted components.

So no stand-in remains. The same move withdrew `outside_ga` from dark-energy.gravity-pre-metric-forces-degenerate-exactly.

- **Fix 8.2.** Withdraw `outside_ga` (record the reason in the extraction note). If Leon prefers to keep it, its
  `why` must name what is actually outside GA. It must also list every imported formula used, not two of
  them: $d\,\mathrm{CS}_5 = P(F,F,F)$ (five-dimensional Fact (a)), the transgression (Chern-Weil (b)) and the
  variation (Chern-Weil (c)).

## 9. synthesis.nondiagonal-kasner-residue-weighted-shear: ACCEPT WITH FIXES

**Boost-block sign.** Definite and correct. I redid the torsion equation by hand.

- The $a = 0$ equation gives $c = 0$ and $k$ symmetric.
- The $\gamma^0$-legs of $a = l$ give $k_{lm} + \rho_{ml} = -\tau^{-1}B_{lm}$ (the proof's
  $\tau^{-1}B_{lm} = -k_{lm} + \rho_{lm}$), using $\rho\cdot\gamma^l = \sum_p\rho_{pl}\gamma_p$.
- Hence $\omega(\gamma_m) = -\tau^{-1}\sum_l\mathrm{sym}(B)_{lm}\gamma_0\wedge\gamma_l$ (display sign) and
  $\omega(\gamma_0) = +\tau^{-1}\sum_{l<m}\mathrm{antisym}(B)_{lm}\gamma_l\wedge\gamma_m$.
- For $G = 1$ this is C10's $-H_i\gamma_0\wedge\gamma_i$, with Cartan $\omega^{l0} = +\tau^{-1}\mathrm{sym}(B)e^m$
  (the dictionary's $\omega^{i0} = H_ie^i$). Then $(\gamma_m\cdot D)\gamma_0 = \tau^{-1}\sum_l
  \mathrm{sym}(B)_{lm}\gamma_l$.

E9 tests this with the engine on three shears not in the check, $G = 1 + c\tau^qN$
($c,q = (2,1/3), (-1/2,5/7), (3,1)$, $N$ in three different slots, non-diagonal constant $\theta_0$). Both
blocks and $\tau K = \mathrm{sym}(B)$ match. The mutation $+\mathrm{sym}(B)$ is caught, by mine and by the new
check. (iv): the store-sign Ricci and Einstein readings along $\gamma_0$ are consistent with
$\mathrm{Ric}^\circ_{00} = -\partial_\tau\mathrm{tr}K - \mathrm{tr}K^2$, and the check confirms them.

- **Fix 9.1 (citation).** As in 7.2: the frame torsion equation is Definition
  \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}(f), not Fact `synthesis.imported-gtg-dictionary`(ii).
- Optional (Leon's call, a formal change). The GTG computation now fixes the sign that formal (i) leaves "up to
  the sign convention": $\omega(\gamma_0) = +\tau^{-1}\mathrm{antisym}(B)$ in the displayed sign.

## 10. synthesis.two-frozen-points-conformally-flat: ACCEPT WITH FIXES

The $\Cl(2,4)$ computation is right: $-(\nInf\wedge a)\cdot Y$ gives the Fact's flat-scale display, the parallel
tractors are $\sigma\nInf + (m - rx) + r\nO$, the norm is $2rs + Q(m)$, $(\nInf\wedge a)\times(\nInf\wedge b) = 0$,
and the stabilisers have dimension 15, 10 and 6. The mutation $+\nInf\wedge a$ is caught.

- **Fix 10.1.** "By the Fact, a parallel tractor of norm $\Lambda/3 \ne 0$ is the scale tractor of an Einstein
  scale with that $\Lambda$ where $\sigma \ne 0$" uses the converse of what the Fact states. The Fact gives:
  Einstein implies a parallel tractor of norm $\Lambda/3$ (and the iff only for the null, vacuum case). The
  check fills the gap numerically. The proof can fill it in one line, which I verified exactly at four
  $(s,m,r)$, including $s < 0$ and $r < 0$ (E5/E10). Replace the sentence with: "Directly: for
  $\hb^{-1}(a) = a/\sigma$ the torsion equation gives $\Omega(a) = (\nabla\sigma\wedge a)/\sigma$, and with
  $a\cdot\nabla(\nabla\sigma) = -r\,a$ the field strength is $R(a\wedge b) = -(2r\sigma + Q(\nabla\sigma))\,
  \sigma^{-2}a\wedge b = -Q(I)\,\sigma^{-2}a\wedge b$ (the norm computed above), so $\mathcal R(B) = -R(\sigma^2B)
  = Q(I)\,B$: the derived metric $\sigma^{-2}\eta$ is Einstein with $\Lambda = 3Q(I)$."

---

Memory: nothing used or new.
