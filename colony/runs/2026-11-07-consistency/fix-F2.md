# Fix round, fixer FX2: referee F2's findings on gtg_2 (run 2026-11-07-consistency)

Brief: FIX_GTG.md with F = F2, P = 2. Entities: referee_F2.txt (11). Acting for Leon as maintainer.
I made no commits, spawned no agents and killed no processes. I ran tp check once.

Scratch (my scripts):
`/tmp/claude-0/-home-claude/23cbb9be-73ca-5537-8211-47496476158a/scratchpad/FX2/`
- `e9_frame.py`: Euclidean frame trivector on the instantons.
- `e10_theta.py`: both null expansions on the SdS horizon cross-section.
- `mut.py`: textual and STORE_SIGN mutants, run in scratch copies.
- `pins.py`, `diffs.py`, `wdiff.py`: pin review (formal at the lock commit 79c425d against now).
- `ed.py`: front-matter edits.

Versions: every entity was already one above store/.tp-lock.json in this run, so none was bumped. Each changed
entity has a credit entry (source "maintainer pass 2026-11-07 (GTG review fixes)") and an
`extraction.maintainer_pass_gtg_review` note.

Changed checks: 7 entities, listed below. Each passed colony/runcheck.py, then check4 on a proposals/ copy (each copy
was deleted afterwards). Six of the seven changes only add premise() calls for uses edges added here (W405 otherwise).

## Validation

- check4: 0 errors on all seven changed checks. dark-energy.frozen-point-makes-stelle-west-vector has two information
  findings, I410 (legacy checks) and I405 (excused).
- `python3 -m tp check --store store --layers 1,2,3 --keep-going --author leon`: 0 errors, 0 warnings, and no finding
  on any of my ids.

## The two substantive findings

### synthesis.promoted-norm-weyl-clock-flat-weight

**(iii) The Cl(4,0) frame-equation sign.** Applied.
- Verified exactly on the torsion-solved S^4, S^2 x S^2 and CP^2 (`e9_frame.py`, now in the check).
- Setup: F = calR + (Lambda/3) id, which is calR - l^-2 D with D = -id.
- 2 d_b ^ F(I(a ^ b)) = 2(G(a) - Lambda a) I = 0, while G(a) + Lambda a = 2 Lambda a is not zero.
- The identities d_b ^ calR(I(a ^ b)) = G(a) I and d_b ^ (I(a ^ b)) = -3 a I hold.
- The unit S^4 has calR(B) = -B, Lambda = 3 and scalar -12. I also derived the S^2 case by hand on Cl(s, s): calR(J) = -s J.
- The proof now writes the Euclidean form, says that the Lorentzian form keeps + Lambda, and traces it: s(calR) = 4 Lambda, so s(F) = 0.

**(iv) The de Sitter sign.** Applied.
- The text now reads calR(B) = (Lambda/3) B on Cl(1,3), not (Lambda/3) D.
- Checked with the flat-slicing de Sitter field: calR = +1/4 id at H^2 = 1/4.

**The instanton check.** Applied.
- I confirmed the old check passes with gtg.STORE_SIGN flipped.
- It now asserts Lambda = 3, 1, 6, calR(B) = -B on every plane of S^4, and the Euclidean frame trivector.
- These mutants now fail: the flipped sign, G + Lambda a in place of G - Lambda a, and F = calR - (Lambda/3) id. The unmutated check passes.

**Formal level: not reached.** Formal (iii) speaks only of "the trace of the full frame equation", with no sign. Formal (iv)
says "locally the de Sitter field". The setting's F^ab = R^ab - l^-2 e^a ^ e^b is in the form convention where spheres
are positive, so S^4 has F = 0.

**Other items.**
- uses: synthesis.imported-gtg-dictionary@2 added (Weyl duality, row 5). Miskovic-Olea not added: disputed, since it is
  cited as prior work, as the 2026-10-22 pass decided.
- Repinned henneaux@6 and kasner-wall@8 (N).

### synthesis.series-wald-entropy-changes-without-flux-on-local-horizons

**(i) "Both null second fundamental forms vanish".** Applied.
- The sentence is false. `e10_theta.py` used the SdS PG field at (r_b, Lambda) = (1, 3/4), (2, 3/16), (1/2, 3/2).
- chi^(xi)(e_A, e_B) = 0, but theta of n = e0 - e1 is -4/r_b.
- The step needs only chi^(xi) = 0, so the sentence was corrected and now names the bifurcation surface.
- The check now asserts chi^(xi) = 0 and theta_n = -4/r_b. Three mutants fail.
- The false parenthetical came from item G6's wording; the G6 note is annotated.

**Formal level: not reached.** Its (i) assumes the second fundamental form vanishes along one null normal, and its
cross-section clause names xi.

**Other items.**
- The K-convention sentence is made exact: it holds because the vectors of a spacelike plane of Cl(1,3) square to -1.
- outside_ga widened to the formal's component displays.
- uses: dictionary@2 added. c-loc is not added (For Leon).
- Repinned euler-term@5, einstein-equations@8 and sds-clausius@5.

## Per finding, other entities

**1. dark-energy.frozen-point-makes-stelle-west-vector**
- Applied: the translational sign is -(D_aB - D_bA) ^ V/l^2, checked exactly in Cl(2,4).
- Applied: the factor 4, eps_abcd X^ab Y^cd = 4 <(X ^ Y) I4^-1>, checked on three random pairs. The formal "~" absorbs it.
- Applied: outside_ga now names formal (ii)'s form displays.
- Applied: the gtg-tractor@1 edge (with a premise() call), and stelle-west-vector@6 repinned.

**2. pairing.regular-frame**
- Applied: the formal and technical levels now state the four bivectors Omega(e_c), with the forms as a labelled reading (notation).
- Applied: std-algebra@2 added to uses, and three pins repinned (N, N, and two-frames (i) unchanged).

**3. pairing.static-frame**
- Applied: std-algebra@2 added, and two pins repinned.
- "as F -> 0" is a formal clause, so it is For Leon.

**4. singularity.transport-schwarzschild-fibre**
- Applied: xi is written as sqrt(r) grad r + sqrt(2M) grad t_PG in formal (4) and the technical level, with T4's one-form as the reading.
- Applied: outside_ga removed.

**5. synthesis.einstein-condition**
- Applied: the unit is named in the formal: T_x + T_x I_7 for the tractor space, and the mu slot with I_7, not I_5. The brief
  counts naming a unit as notation, which resolves P2's For-Leon item.
- Applied: outside_ga now lists the index displays of (4), (6) and (7) exactly.
- Applied: gtg-tractor@1, std-algebra@2 and dictionary@2 added, and tractor-connection@3 repinned.

**6. synthesis.euler-entropy**
- Applied: Omega_S = -omega_S J and calR_S(J) = K J in formal (i) and the technical level (checked by hand on a profile field).
- Applied: the outside_ga why made exact.
- Applied: chern-weil@1 added, and eight pins repinned (R: dictionary, use holds). c-loc is For Leon.
- Disputed: the remark's soldering sign. Its F is series-wald's F_abcd, which is minus the Fact's Lorentz block, so the
  sign is consistent. The remark now names which F it uses.

**7. synthesis.macdowell-mansouri-principle**
- For Leon: the l^2 = 3/|Lambda| display.
- Applied: the optional item, GA maps in the formal setup.
- Applied: six pins repinned. positive-structure is R (A3), and the cited trace calR = 4 Lambda is unchanged.

**8. synthesis.promoted-norm-one-global-pair**
- Applied: outside_ga now names H^4(M) = 0 for (iv).
- Applied: henneaux@6 repinned.

**11. synthesis.taub-nut**
- Applied: dictionary@2 repinned (R, use holds).

## For Leon

1. **macdowell-mansouri-principle, formal setting.** With l^2 = 3/|Lambda| the display gives D_aV = (3/(Lambda l^2)) hb^-1(a),
   which is -hb^-1(a) on the anti-de Sitter branch. Clauses (i) to (iv) are unaffected, because the Lorentz block is
   quadratic in 1/l^2.
   - Replace "Let $\Lambda \neq 0$, $\ell^{2} = 3/|\Lambda|$, and let" with "Let $\Lambda \neq 0$, and let".
   - Replace "$A(a) = \Omega(a) - \hb^{-1}(a)\wedge V/\ell^{2}$" with
     "$A(a) = \Omega(a) - \tfrac{\Lambda}{3}\,\hb^{-1}(a)\wedge V$ (that is $\Omega(a) + \hb^{-1}(a)\wedge V/Q(V)$, so that $D_{a}V = \hb^{-1}(a)$ on both branches)".
2. **static-frame, formal.** Replace "Every class vanishes at $F = 0$" with "Every class tends to $0$ as $F \to 0$ (the static
   gauge is not defined on the horizon locus)". Make the same change in the technical level.
3. **Postulate edges not added.**
   - series-wald and euler-entropy cite synthesis.c-loc-local-horizon-premise.
   - My recommendation: no edge. Both state what (Loc) excludes or refutes, and neither rests on it.
4. **For the orchestrator.** These targets' formal levels changed in notation only: regular-frame, transport-schwarzschild-fibre,
   einstein-condition, euler-entropy and macdowell-mansouri-principle. Their versions are unchanged, so dependants
   pinned at the current version stay valid.
