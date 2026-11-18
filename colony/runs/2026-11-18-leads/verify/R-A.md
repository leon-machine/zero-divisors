# Referee report, group A (run 2026-11-18-leads)

Blind referee. Read: the three proposal folders, the store (files and git diff of the working tree), the
check4 logs (all three present, 0 errors). Not read: findings/, work/, RUN.md, ATTACK.md, LEADS-source.md.
Scratch: /tmp/referee-A/ (a1.py, a2.py, a4.py and perturbed copies of checks). sympy not used.

| item | verdict |
|---|---|
| A1 heating coefficients / chain's bath | WRONG in clause (iii) and in the Reading's conclusion; (i), (ii) sound |
| A2 rotation weights | SOUND WITH FIXES (wording of (v), title, Reading) |
| A3 spreading law restatement | SOUND WITH FIXES, but a duplicate of stored theorems; recommend not raising status on this id |
| A4 energy per event (maintainer pass) | SOUND; two wording fixes |

---

## A1. synthesis.heating-coefficients-across-curvature-couplings-and-on-the-chains-bath

### Verdict: WRONG (clause (iii), the Reading's last sentences, technical, lay, one-liner); (i) and (ii) SOUND.

**The error.** Clause (iii) changes the bath to the chain's content (N_s, 48, 21) in the production
coefficient c but keeps the threshold c* = 13.4949 of the Pati-Salam clause, which was computed with
kappa_s = 145.3, i.e. g_* = g_s = 100, the Standard Model's bath. The stored yield
(dark-matter.seeding-gravity-floor-dark-towers-temperature, formal) is Y = c T^3/(3 kappa_s M_P^3) with
kappa_s = sqrt(pi^2 g_*/90)(2 pi^2/45) g_s, and the Pati-Salam threshold is c* = A/(2 M_3^4) with
A = 3 kappa_s M_P^3 (rem m_p eta) (its check.py, lines 60-72). So c* is proportional to kappa_s, i.e. to
g^{3/2} of the same bath. With the proposal's own assumption (all species massless), the chain's bath
has g = N_s + (7/8)(2)(48) + 2(21) = 190, 194, 314 for N_s = 64, 68, 188, and c* rises by (g/100)^{3/2}:
to 35.3, 36.4, 75.1. The proposal grep-tests clean: neither entity, proof nor check mentions g_* or the
kappa_s of the new bath (check.py line 73-83 hard-codes kappa = 145.3).

Recomputed by my own route (/tmp/referee-A/a1.py; c from clause (v) of the rate theorem, c* from the
stored inputs, kappa_s(g) from the stored formula):

| N_s = 188 | proposal (g = 100) | consistent (g = 314) |
|---|---|---|
| c* | 13.49 | 75.1 |
| margin, 22 odd-tower vectors (c = 1.158) | 1.84-1.85 | 2.84 |
| margin, four SM contents (c = 5.087) | 1.27-1.28 | 1.96 |
| c* in vector species / SM contents | 256 / 10 | about 1430 / 59 |
| four chain copies, xi = 0 (c = 15.89) | 0.96, "fails" | 1.47, holds |
| four chain copies, xi = 1/6 (c = 10.25) | 1.07 | 1.65 |
| interval of one xi with c < c* | (0.0215, 0.3118) | (-0.140, 0.474) |

For N_s = 64, 68: margins 2.51, 2.52 (vectors), 1.74, 1.75 (four SM), 1.50, 1.51 (chain copies at xi = 0);
interval (-0.264, 0.597) and (-0.255, 0.588).

Counterexample to the stated conclusion "it fails at the tree-level value and holds at the conformal
one": at N_s = 188, xi = 0, c = 15.89 < c*(g = 314) = 75.1. The direction of the whole of (iii) is
reversed: the chain's larger bath raises the yield's dilution (H and s) faster than it raises c, so the
stored margins 2.2 and 1.5 become larger on the chain, not smaller. The "above" halves of the margin
brackets are true only as weak lower bounds; the "below" halves, the counts 256/10, "c > c* (margin 0.96)",
and the interval endpoints are false.

**True weaker statement for (iii).** With the bath (N_s, 48, 21) massless in both the rate and the
expansion/entropy (g_* = g_s = N_s + 126): the per-vector coefficient rises by 1.70, 1.71, 2.19
(correct as stated); the threshold rises by (g/100)^{3/2} = 2.62, 2.70, 5.56; every margin the clause states
rises (values above); four copies of the chain's content satisfy the exclusion at both xi = 0 and xi = 1/6
and fail only for |1 - 6 xi| beyond about 1.84 (N_s = 188). The coupling question then does not decide
the clause on either stored reading. The Reading's "dependence that matters" paragraph must go.

**Other points.**
- (a) (i) checked: alpha_j linear in (c_j, tau_j); the scalar-to-scalar weight with two couplings I recomputed
  by direct integration of the stored bracket: spin-two part (1/16)(4 pi)(4/45)(1/4) = pi/180, trace part
  (1/36)(4 pi)(1/4) tau_1 tau_2 = 5 pi tau_1 tau_2/180, cross term zero because the integral of
  cos^2 - 1/3 vanishes. (ii) recomputed: SM copy 1519247/82944000 exactly,
  conformal shift 5120/4557741 exactly, four SM contents at the window ends 13.447-14.313, crossing of c* at
  xi = 1.52399 (inside the window, between 1.5239 and 1.5241 as stated), central c* 14.44. All agree.
  "Increases with every |1 - 6 xi|" should read "does not decrease" (it is constant if the other side's
  tau vanishes).
- (b) Content: 21 vectors, 48 Weyl, -36 + N_s = 28, 32, 152 confirmed in
  synthesis.series-content-induces-a-newton-coupling-only-through-an-unfixed-cut-off@2 (ii) and
  standard-model.chain@8. But the Pati-Salam clause (i) is "with the (15,2,2) at the record's central
  values" (M_I = 1.9e10); only N_s = 188 is that chain. N_s = 64, 68 belong to the chains without the
  (15,2,2), whose two-loop M_I (9.2e10, 1.4e11) are not the clause's; quoting them as the clause's bath is
  off-scope. "1.1e16 GeV, the least of the stored unification scales" is false: the two-loop table has
  7.9e15 and, with the (10bar,3,1) light, 8.9e14 (harmless: 6e14 is below both). Massless counting at
  T up to 5.3e11 = 28 M_I is fair for the gauge and scalar content (symmetric phase); the right-handed
  neutrinos (M_3 ~ T at the comparison point) are not massless, a few-percent effect. So the massless count
  does not overstate the bath materially; the defect is that the bath was changed in only one of the two
  places it enters.
- (c) "Four copies of the chain's own content": no stored statement asks about it (grep of the store); it is
  the proposal's construction and should be labelled so.
- (d) The Reading's assignment "the stored reading is the tree-level value 0" is stored only for the rung
  field's doublets (Reading of synthesis.no-single-curvature-coupling-...@1, itself argued); extending it to
  the bath's and copies' scalars, then saying the chain's scalars' couplings are not fixed, is argued and
  internally uneven.
- Cross-item: the same omission bears on A4's floors at 6e14 GeV if the chain holds there (the floors use
  the SM bath with g = 100): xi_floor scales as (c g^{-1/2})^{1/4}, about 1.05 times higher for a vector
  content at N_s = 188. Small, but the floors' scope sentence should say the bath is the SM's.
- Perturbations: (1) chain fermions 48 -> 45: chain check fails; (2) c* multiplied by kappa(314)/kappa(100):
  chain check fails (it encodes the omission); (3) factor 5 -> 4 in the trace term: (ii) checks fail, the
  integration check still passes (it is independent). The check is sensitive, but it cannot see the
  missing g dependence.
- Status: (i) proved; (ii) computed; (iii) as written, not acceptable. Transport-absent, as stated.

**Fixes.** Recompute c* with kappa_s(g) of the chain's bath in (iii), check.py and every level; replace the
Reading's final conclusion; restrict the clause's bath to N_s = 188 (or say which chain the other two
belong to); correct "least of the stored unification scales"; label the four-copies case as the
proposal's construction.

---

## A2. synthesis.rotation-weights-of-pair-sources-fix-the-channel-weights-and-forbid-a-fermion-trace

### Verdict: SOUND WITH FIXES.

- (i) Checked by hand: on k^perp with e^i = -e_i the pairing is minus the sum of Q(T(e_i)), positive;
  tr P = <P,P> = 3, <T,P> = tr T, so B = <T°,T°> + (1/3 - 1/2) t1 t2. Correct.
- (ii) Schur for the real, absolutely irreducible spin-2 representation of SO(3): the 1/5 and the zero mean
  are right. The script's rank 24 on V tensor V is an exact finite computation; acceptable as proof.
- (iii) Own computation in GA.py (/tmp/referee-A/a2.py, k = 2e0, s = 4): scalar trace (1 - 6 xi)s and
  trace-free norm 8/3 = s^2/6 at xi = 0, 1/6, 1/3; fermion components trace-free, norms summing to 4 = s^2/4;
  vector sources: uu+vv and uv-vu vanish identically, uu-vv and uv+vu nonzero, all trace-free, total
  32 = 2 s^2. Confirmed.
- (iv) My own route: direct angular integration (exact polynomial fit in cos theta at rational points on
  the circle, verified on held-out points) of the summed B^2/s^4 with the stored sources, rotating the
  second pair. All nine W_ij/pi equal (c_i c_j + 5 tau_i tau_j)/180 (1/30, 1/60, 1/15, 1/20, 1/5, 4/5 ...),
  and scalar-scalar at xi = (1/3, 1/2) gives 7/60 as the formula. (iv) reproduces the stored clause (iv).
- (v) True and proved, but it is a two-line tautology (the trace is rotation invariant, tr L_b T = 0). All
  content sits in the hypothesis "whose two-quantum element is a pair of weight one"; "whatever its form"
  is correct only as a conditional. Say so in the statement.
- (vi) Checked by hand: tr G = -R in four dimensions, gamma = 1/(1 + 3 mu Q), interaction
  -(gamma/6) t1 t2. Correct; weights carry gamma^2.
- (c) Reading. The step "the stored trace statement is a source mu((a.k)k - Q(k)a)R" rests on the
  remembered state-independence of the free-field trace (Wald) plus reading the anomaly's Box R term as a
  local response; it is argued, labelled argued, and used in no proof step: acceptable. But "the correction
  to the chiral-fermion coefficient from the stored trace statement is zero, at the next order in G as well"
  is misleading as worded: the Reading itself says the trace-free vacuum response at the same order G^3
  rescales every c_i c_j, so the fermion coefficient does change at next order; only the trace-anomaly part
  is zero. Reword. The interacting-theory paragraph is inside "Reading (argued)": acceptable, though its
  "no order in couplings" should be marked as resting on the helicity of the state, not on (v).
- Duplication: the stored Weyl-flat theorem (synthesis.weyl-flat-variations-...@1, note and clause (v))
  already says, argued, that for massless fields every state-dependent part of the stress lies in the
  trace-free channel. The extraction note says the anomaly remark is in "clause (v) of the first-order
  theorem"; it is clause (v) of the Weyl-flat theorem, not of the rate theorem. Fix the pointer.
- (d) Title: "forbid a fermion trace" claims more than (v): replace by "... forbid a trace part for a chiral
  pair's source" or add "of weight one".
- Perturbations: fermion source 1/4 -> 1/3; scalar curvature term -2 xi Q -> -3 xi Q; vector norm 2 -> 3.
  Each fails three of four check functions. Status "proved" right for (i)-(vi).

---

## A3. scrambling.spreading-law-chaos-bound-saturated (v6 conjectured -> v7 proved)

### Verdict: SOUND WITH FIXES as mathematics; a duplicate of stored theorems. I recommend against raising
the status on this id (keep it conjectured, as the entity for T08 Asm 6.1, and point to the theorems).

- (a) Is anything new? No. (a) is synthesis.affine-cell-boost-spreads-without-scrambling@4 (i), (ii)
  verbatim with m = N; (b) is the rotor arithmetic already in this entity's v3 check and
  synthesis.phase-flow-is-time-rotor-flow-kms-continuation@4 (ii), (v); (c) is kappa beta = 2 pi from
  synthesis.positive-null-energy-gives-r-premises; (d) is synthesis.boost-evolution-on-generators-is-one-
  unitary-group@6 (v). The closing paragraph of the one-unitary-group theorem already states in full
  "t_* = kappa^-1 ln N = (beta/2 pi) ln N is the time for one affine cell to cover N cells, ln N units of
  rapidity" and "the chaos bound is met, not saturated". "Proved" is formally earned (each step cites a
  proved premise), but the restated entity is a second copy of stored theorems under the id of a paper
  assumption whose actual content (the window law) is now clause (e), unproved. A status field "proved"
  on the entity that the T08 locator (Asm 6.1) points to will be read as "T08's assumption is proved".
- Misquote in (a): it says "the boost time evolution is the unitary dilation (D_t f)(U) = e^{-kappa t/2}
  f(e^{-kappa t}U) (Theorem one-unitary-group)". That theorem at v6 says the opposite orientation:
  alpha_lambda(a(f)) = a(D_{-lambda} f), "the dilation of [the affine-cell result] with the time parameter
  reversed" (its formal (ii) and its correction note), and (vi) allows e^{+-kappa t}. Under the cited
  theorem's orientation forward Killing time compresses a cell; one cell covers N cells at t = -kappa^-1 ln N.
  The count |t_*| is unaffected, but "covers N cells at Killing time t_*" needs "in the direction of time in
  which the flow dilates the affine parameter", or cite the affine-cell theorem's convention and note the
  stored sign difference (which is between the two stored theorems, not introduced here).
- (b) The stored title is already "The spreading law, and the chaos bound met, not saturated" (since v5);
  it is not false. Only the id slug says "saturated"; the proposal could say in the text that the id is
  historical.
- (c) (e) is clearly headed "What is not proved; an estimate" and the scope paragraph says so; the lay text
  is careful. Acceptable, subject to the status concern above.
- Perturbations: dilation replaced by contraction (the cited theorem's orientation): the affine-cell check
  fails, confirming the check encodes one orientation; kappa = 1/(2M): rate check fails. The check is
  arithmetic restating stored clauses; check_rate_is_modular_rate touches scrambling.mode-count, not the
  (N+) theorem it rests on.
- Dependant scrambling.return-delay-scrambling-log-recovered pins @6; noted by the proposal.

**Fixes (if accepted at all).** Correct the orientation sentence in (a); or, preferred, keep v6's status,
add a sentence pointing to the affine-cell and one-unitary-group theorems for the proved readings.

---

## A4. Maintainer pass: dark-matter.seeding-gravity-floor-dark-towers-temperature v5 -> v6 and dependants

### Verdict: SOUND. Two wording fixes.

- (a) E^3 weighting: d^3p1 d^3p2/(E1 E2) f1 f2 times a function of s only, since by clause (iv) the
  angular integral of B^2/s^4 is a constant W_ij for every channel and |M| = 8 pi G|B|/s, so the integrated
  squared amplitude is W_ij s^2 times a constant; the angle integral of s^2 gives (32/3) E1^2 E2^2. So the
  weight is E1^3 f1 E2^3 f2 in every channel, both legs of one species (same statistics). Moments:
  Gamma(k+1) zeta(k+1), times (1 - 2^-k) for Fermi. Recomputed (a4.py): legs 3.8322 T, 4.1060 T; events
  7.6645 T, 8.2119 T; scalar 7.8730 T, fermion and vector 7.8896 T, SM copy 7.8893 T. All as stored.
  Hidden hypotheses, all inherited from the rate theorem: massless legs, no thermal masses, no
  Bose enhancement or Pauli blocking of the produced species.
- (b) The produced pair carries E1 + E2 exactly (four-momentum conservation, all of k into the pair);
  counted once per event. Energy fraction: d(rho_d/rho) = (E s/rho) dY = (4/3)(E/T) dY at g_* = g_s, constant
  E/T, so (4/3)(E/T) Y. Correct.
- (c) Prefactor 1.2256e-3 (old convention 9.62e-4); mirror floor 6.620e-4, nine vectors 8.118e-4;
  eta' = 2.10 to 2.12 (eta 6.1 to 6.15e-10); crossover c between 1.53 and 1.56; T for Y = 8.7e-11:
  16.46 times the ceiling, floor there 5.41e-3. Under (R) (cap 1e13 GeV): mirror floor 3.07e-5, 97.7 times
  below 3e-3; share of xi^4 at the helium edge 2.37e-3 without (R), 1.1e-8 under (R). Delta N_eff
  1.43e-12 and 1.72e-11. All agree with the stored figures.
- (d) The three changed conclusions are stated consistently at formal, technical, lay and one-liner in
  dark-matter.coefficients-floors-they-give-what-gravity v6 and in
  synthesis.mirror-temperature-measures-deposit-under-r v3 (formal and closing).
- (e) The hot deposit's "3T per unit of baryon number" is a different quantity (the descent's deposit per
  unit charge, an order-of-magnitude stipulation; the stored-asymmetry formal says only "of order the
  reheating temperature"). Not an inconsistency, but coefficients (iii) now compares a computed 7.9 T with a
  stipulated 3T and draws "no longer equal": add that the hot deposit's 3T is a stipulation, so the ratio
  1.27 carries no physical weight.
- (f) Spot checks: dark-tower-matter.mirrors-composition v5 and dark-matter.stored-asymmetry-charge-not-number
  v13 quote 6.6e-4 and 2.1 consistently; pred.no-dark-radiation's 2.1e11 margin is consistent with 1.4e-12.
  A store-wide grep found no surviving 9.6e-4, 5.2e-4, 6.4e-4, "4Y" or eta' = 4.4 outside history notes.
  The rate theorem's Reading ("floors rise by 1.6 to 1.8") is still true as a statement about the
  coefficient alone, but the total rise against the imported floors is now about 2.0 to 2.3; consider
  adding "at a fixed energy per event". The mirrors-composition rerun (83-96 percent neutrons at 6.6e-4) I
  did not verify (legacy scripts).
- Perturbations of the floor's check (in scratch): E^2 in place of E^3 weights, and Fermi legs given Bose
  moments: both make check_mean_energy_per_event and check_floor_prefactor_and_scaling fail. The E^3
  derivation itself is in the proof text, not computed by the check (the check takes the moment ratios as
  given).
