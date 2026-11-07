# Consistency pass R02 (thermality, second half), 7 November 2026

Scope: the 42 ids of read_R02.txt (2 GA-owned: hadamard-dirac-states..., normality-on-the-closed-generator...).
Read in full, in dependency order: every entity.md (front matter, derivations, extraction notes, formal, technical, lay,
one-liner) and every proof-main.tex of the list (the 13 imported Facts and the 3 postulates have no proof file). check.py
files were read only where a sign question needed it (schwarzschild, killing-horizon). Exact computations in
/tmp/claude-0/-home-claude/23cbb9be-73ca-5537-8211-47496476158a/scratchpad/R02/ (step7.py, ks.py, pg.py; all checks pass).
Validation: `tp check --layers 1,2,3 --author leon`, run twice; final run: 0 errors, 0 warnings on R02 ids (I213 infos only,
pre-existing).

## Fixed (old -> new version)
- local-normality-at-the-edge-gives-the-null-ground-state 3 -> 4: "Beyond one flat chart" sentence (formal, technical) for the
  edge, which the flags entry recorded without the sentence the conventions require; difference quotient Q(u, v) renamed
  q(u, v) (house symbol Q(v)).
- microlocal-condition-on-a-generator-gives-the-local-null-ground-state 5 -> 6: same flat-chart sentence; dated marker on the
  proof Reading's "no restriction theorem is in the store" (computed since 1 November).
- point-spectrum-boost-admits-no-half-sided-translations 4 -> 5: (Q)'s weights brought to version 3, kappa(k + 1/2); the
  technical level said (Q)'s flow returns to the identity after one modular period (true only at version 2; at version 3 it
  is the parity automorphism).
- positive-null-energy-gives-r-premises 7 -> 8: bare `icP_{jl}` in proof (iv) written `JcP_{jl}` (the windows' unit).
- geometric-modular-conjugations-on-a-generator-give-the-null-ground-state 4 -> 5: proof Step 8 labelled clause (v), is (vi);
  stray parenthesis in Step 7; digamma written with the field letter psi in formal (vi)(b).
- modular-data-on-a-generator-fix-neither-the-translation-lift-nor-the-sign-of-i 4 -> 5: title had a bare i ("sign of i" ->
  "the unit's sign"); formal (iv) and proof Step 4 now say the unindexed J is the transverse bivector, not a modular
  conjugation J_a, and that B = gamma_0 gamma_3 is the B_k = gamma_0 n sign of the conventions.
- q-splits-maximum-entropy-affine-weights 5 -> 6: (Q-w) and "(Q)'s choice" (sea at a site) labelled as (Q) version 2; version 3
  is the other class of (iv).
- s-wave-array-is-a-boundary-mode-set 4 -> 5: the "under (Q)" conclusions (zero mode in the trace) labelled as (Q) version 2.
- null-ordering-of-counted-units-is-zeta-symmetric 3 -> 4: garbled technical sentence repaired; edge-scaling result cited as
  the Theorem it is (was "Proposition").
- r-le-i-independent-spectrum-condition-separates 4 -> 5: bare `alpha_{ip}` in proof (M2) written `alpha^k_{Jp}`.
- restricted-dirac-hadamard-parametrix-...-bounded-kernel 3 -> 4: bare "the sign of $i$" in the proof's conventions written as
  the unit I_4; lay level updated (the two restrictions are now shown to agree modulo a bounded kernel).
- weyl-flat-fields-...-schwarzian (no bump, lay only): "for particles with mass it is still an assumption" updated ((HS) is a
  theorem).
- field-strength-cancels-... (no bump, one-liner only): "leading Hadamard coefficient cited from memory" -> imported Fact.
Each bumped entity has a credit entry and `extraction.maintainer_pass_consistency`; all files kept.
Stale pins created (statements unchanged; 22 edges, for re-confirmation and `tp repin`): users of positive-null-energy@7
(boost-evolution, collapsing-hole-flux, killing-horizon, null-ordering, schwarzschild, stationary-horizon, thermality),
microlocal@5 (bulk-hadamard, dirac-states-restrict, field-strength, modular-data, weyl-flat), local-normality@3
(clausius-on-the-action-shell, microlocal, normality-on-closed, weyl-flat), point-spectrum@4 (c-loc-modular-clause,
positive-null-energy), restricted-dirac@3 (dirac-causal-propagator, hadamard-scaling-limit), q-splits@5 (cutoff-count),
geometric-modular@4 (modular-data).

## For Leon
1. **schwarzschild-horizon-translations-are-no-conformal-symmetry: the gauge is the outgoing chart.** Formal: "ingoing
   (Kerr-Schild) gauge hb^{-1}(a) = a - (M/r)(a.k)k, k = e_0 + xhat, which covers ... the future horizon". Exactly
   (ks.py, at r = 2M, M = 1/2): with k = e_0 + xhat the outgoing radial direction is exactly null (Q = 0) and the ingoing one is
   not (Q = -4); the inaffinity of d_t is Gamma^0_00 = -kappa; with k = e_0 - xhat it is +kappa and the ingoing ray is null.
   So the stated field is the outgoing (white-hole) chart, containing the past horizon, which is why (v) and the check find
   (K.D)K = -kappa K (the store sign gives +kappa on the future horizon: dictionary sec. 8, positive-null-energy (iii)). Proof
   (iv) uses the ingoing form with v = t + r, which this field does not have; proof (v) writes d lambda/dv = c e^{kappa v}, which
   contradicts its own (K.D)K = -kappa K (gives e^{-kappa v}). The conclusion is time-reflection symmetric and stands.
   Proposed fix (keeps check.py): "the outgoing (Kerr-Schild) gauge ..., which covers the exterior, the past horizon r = 2M
   and the white-hole interior"; (v) "On the past horizon ... the time translation acts as lambda -> e^{-kappa tau} lambda";
   proof (iv) in u = t - r with g = f du^2 + 2 du dr; proof (v) d lambda/du = c e^{-kappa u}; one sentence that the future
   horizon follows by the time reflection (as the flag already says). Alternative: k = e_0 - xhat, +kappa, and the check's
   -1/2 becomes +1/2. Also: add the "Beyond one flat chart" sentence (flag present, sentence missing); and repoint
   positive-null-energy@7 (cited only for the dilation of its setup) to null-vacuum-on-a-horizon-generator@1 (i): it would
   drop (N+) from holds_given.
2. **killing-horizon-value-factor-is-the-generator-boost (iv), (iii): sign of kappa needs beta > 0.** `(K.D)K = beta(r_h)
   f'(r_h)/2 K` (pg.py); kappa = f'/2 holds only for beta(r_h) = +1, which the proof assumes and the formal (beta^2 = 1 - f)
   does not state; for de Sitter that is the contracting chart (past horizon, -H), while the store's future cosmological
   horizon (expanding chart beta = -rH) has +H. Proposed: "beta = +\sqrt{1 - f}" in (iv), "-H for de Sitter in this chart,
   which contains the past cosmological horizon (the expanding chart gives +H on the future one)", and in (iii) "for either
   sign of kappa (future and past horizons)" in place of "(the eternal hole's horizon and the cosmological horizon)".
   Also holds_given (c1, c2, L, P, R, N+) comes from boost-evolution / affine-cell / positive-null-energy for a geometric
   statement; consider repointing to null-vacuum-on-a-horizon-generator.
3. **thermality-of-every-future-half-generator-fixes-the-period-and-the-null-ground-state holds given (N+)** although the
   statement assumes no premise: it cites positive-null-energy@7 only for null-vacuum facts and stationary-horizon-state@4
   only for the half-thermal products. Proposed: repoint to null-vacuum-on-a-horizon-generator@1 (ii), (iii) and
   stationary-generator-states-and-the-edge-scaling@1 (iii) (and the formal's "Theorem positive-null-energy(i)" claimref).
   This also removes (N+) from geometric-modular-conjugations (which inherits it only through this edge).
4. **normality-on-the-closed-generator (GA-owned)** and through it **modular-data**: same pattern (ga-issues-R02.md, item 1);
   modular-data also inherits c1, c2, L, P, R, N+ from wedge-reflections, cited only for I_4 B = J.
5. **local-normality (v): "the shell value is ln 9/8 on every square [s, 2s]^2"** for the cross-edge block
   (I_4/2pi)(u - v)^{-1}: ln(9/8) is the integral of (u + w)^{-2} (proof (v)); the integral of |R|^2 is (2pi)^{-2} ln(9/8).
   Proposed: "the integral of $|2\pi R/I_{4}|^{2}$ over every square $[s, 2s]^{2}$ is $\ln\tfrac98$".
6. **Label clash H_+ (restricted-dirac, field-strength) against hadamard-dirac (i).** hadamard-dirac: omega(psi psi^dagger)
   has H_+ with sigma_+ carrying -I_4 0; omega(psi^dagger psi) = -(R D + m)H_- e_0 with +I_4 0. restricted-dirac writes
   G_par = (R D + m)H_+ e_0 regularised with sigma + I_4 eps(t - t') (the sigma_- form, right for the psi* psi ordering of
   W_0) and fixes the constant by the flat comparison. Conclusions unaffected; proposed: one sentence in restricted-dirac's
   formal "here H_+ is the boundary value with +I_4 eps, the sigma_- of Theorem hadamard-dirac (i); sign and constant fixed by
   the flat comparison", or write -(R D + m)H_- e_0.
7. **positive-null-energy proof (iii)** computes surface gravity from Christoffel symbols of Eddington-Finkelstein and
   outgoing charts (with a one-sentence GTG pointer). GA rewrite: (K.D)K = Omega(e_t).K = (f'/2)beta K from the stored PG
   connection (as killing-horizon (iv) does). Not a pure notation change.
8. **n-plus-null-ground-state** formal (1) uses kappa for a constant Hermitian operator on K beside kappa the surface gravity
   (scope note, beta = 2 pi/kappa). Proposed rename to mu (postulate with 23 users, so not done).
9. Complex-field stand-ins `\C` (not flagged by the language check): geometric-modular proof Step 2 ("\C 1"),
   phase-flow V_\C, point-spectrum End(Lambda \C^F), q-splits l^2(W) (x) \C^n and (\C^2)^{(x)|W|}, r-le-i \C^2 (x) \C^2.
   Proposed: span{1, I_4} or span{1, J} as each entity's unit (and perhaps a galang pattern for `\C`).
10. Minor notation: the boost rotor is named B (the conventions' boost bivector letter) in stationary-generator-states (i),
   stationary-horizon-state (i), positive-null-energy (iii), (v); positive-null-energy uses D for both the covariant
   derivative and the dilation rotor; state-selection uses Q_k = e^{omega_k p} beside Premise (Q) and Q(v);
   field-strength-cancels uses R for the spinor transport rotor (ii) and for a smooth kernel (iii); the BFS Fact nests items
   (a)-(d) inside its clause (a) of clauses (a)-(e).
11. hadamard-scaling-limit-premise: "Theorem (HS) ... (version 4 ...)" and "Version 4 (this one)" while the entity is at
   version 6; proposed "statement version 4".
12. hadamard-dirac (GA-owned): Step 7 slips, stale lay, "Premise (HS)" label (ga-issues-R02.md).

## Duplicates (by design, restatements after the 7 November splits)
- positive-null-energy (i), (ii) restate null-vacuum-on-a-horizon-generator (ii), (iii) for the state (N+) supplies; the
  null-vacuum entity is the better home (premise-free).
- stationary-horizon-state (i) to (iii) restate stationary-generator-states-and-the-edge-scaling (i) to (iii) verbatim, with
  claimrefs; the latter is the better home. Neither pair is marked `restates`; worth recording so counts take each once.
No other duplicates found.

## Known open items settled
- hadamard-dirac-states... proof Step 7: both the I_4 sign (+ written, - needed for the psi psi^dagger ordering) and the
  regulator (+eps^2 written, -eps^2/2 needed; +eps^2 gives real zeros at z_0 = 0) are slips; formal right; exact evidence
  step7.py; fix proposed in ga-issues-R02.md. The other five listed open items are not in R02's subjects.

## Incident
While quoting the credit roles I had added (one contained ": " and broke YAML), a store-wide regex also requoted the
already-written consistency credit line of seven other readers' entities (cabibbo-from-one-type..., lens-space-wall...,
counted-unit-energy-at-half-offset, wall-rung-count..., sds-clausius..., real-structure-breaks..., univalence-from-even...).
Restored within seconds to the unquoted text they had before (the regex only matched unquoted lines); all seven parse. A
checkpoint commit taken in that window may hold the quoted form, so those seven files now differ from HEAD in that one line
only (same YAML value).

## Counts
42 read in full; 11 version bumps, 2 level-only fixes (13 entities changed); 0 edits to GA-owned or other subjects' entities
(apart from the incident above); For Leon 12; duplicates 2 pairs (by design); cross-subject/cross-reader 6
(xsubject-R02.md); GA issues for the rewriters on 2 entities (ga-issues-R02.md); open items settled 1; tp check runs 2.
