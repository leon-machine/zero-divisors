# Referee H report, run 2026-11-08-composite-higgs (the composite Higgs)

Blindness kept: I did not read findings/, work/, RUN.md, verify/final/ or the other referee's report. check4 was not rerun.
Every check was run with `PYTHONDONTWRITEBYTECODE=1`; no `__pycache__` is left in proposals/. My scripts and logs are
in `verify/work-H/` (`fock.py` is my own Jordan-Wigner occupation-number model, written independently of the
proposals' GA exterior model).

## Summary

| id | verdict | one-line reason |
|---|---|---|
| synthesis.two-species-floor-pairing-has-a-gapped-doublet-pair-mode-that-closes-where-it-condenses | OVERSTATED | Clauses (i) to (ix) check out, but they are statements about the band and about gaps between sector minima. The band need not hold the ground state at fixed N even when omega_D > 0 (exact counterexamples at n_b = 5, 6, 7, P = 3). The return quanta are gapped doublets in the condensed band. Isospin-one levels lie below the pair-breaking threshold. So "closes where it condenses" and "never both" hold only on the band. |
| synthesis.uniform-pair-channel-of-a-tower-condensate-is-a-goldstone-rotor | SOUND WITH FIXES | (i) to (iv) are correct. The fixes: scope the title and the technical level to the (iii) hypothesis; give the K >= 0 range in (iv)(c); fix a false inequality at n_b = 2; credit the classical pairing rotation and the stored "P + P* stays on the band"; make the reading consistent with the gapped uniform hopping doublet of the first proposal. |
| synthesis.even-composite-doublet-needs-a-singlet-constituent-and-its-pair-modes-are-quasi-spins | SOUND WITH FIXES | (i) is correct: an elementary generalisation of the stored rung clause (2). (ii) is a corollary of the stored helicity-one theorem. The one-liner, the technical level and the note drop the hypothesis M^2 = 0 under which "quasi-spin of q rank(M) sites" holds, and I have a counterexample when M^2 != 0. |

## Checks run, perturbations, own recomputations

All three checks pass as filed (logs `run1.log`, `run-*.log`; proposal 1 runs in 13 s).

Targeted perturbations (copies in `work-H/pert/`, log `pert.log`). Every one fails where it should, and only there:
- P1a: omega_D with (n_b - P) in place of (n_b - P + 1): `check_doublet_quanta_ladder_charges_and_canonical_defect` FAIL.
- P1b: X_2 = (P-1)m + 2 in place of + 3: `check_threshold_binding_and_the_pair_sum_spectrum` FAIL.
- P1c: Casimir identity with n_b + 1 in place of n_b + 2: `check_casimir_identity_for_the_pair_sum` FAIL.
- P2a: second difference bound G in place of 2G: `check_variational_bounds_on_every_sector` FAIL (so the bound is attained in the check's data).
- P2b: Rayleigh quotient 2K + G(c + 1): `check_variational_bounds_on_every_sector` FAIL.
- P3a: edge-clean values swapped: `check_charged_pair_modes_are_quasi_spins` FAIL.
- P3b: Casimir 2 in place of 3/4 on the doublet-odd part: `check_doublets_are_odd_in_the_doublet_modes` FAIL.

Own route (exact unless I say "numerical, exploration"):
- Proposal 1: in my occupation-number model the band levels E(nS, n) appear as exact levels, and the band is the global
  ground state where expected (for example -18 at n_b = 4, P = 2 in both phases). Numerically, for exploration, the
  conjectured X and X_2 also hold at n_b = 7 for every P (`conj7.log`: top eigenvalues 7|0, 12|9, 15|13, 16|15,
  15, 13, 9, exactly as conjectured). This supports the conjecture but does not prove it.
- Proposal 2: I computed the second difference of the sector ground energies over all sectors on my own model: the
  maximum is exactly 2G (n_b = 3, 4, 5).
- Proposal 3: I computed the quasi-spin norms for M = E_{up,s} myself: 1, 1, 0 (q = 1) and 1, 2, 4, 0 (q = 2), matching
  the check.

## 1. synthesis.two-species-floor-pairing-has-a-gapped-doublet-pair-mode-that-closes-where-it-condenses: OVERSTATED

### Steps verified
- (i) I recomputed [t_-, B_1*] = B_2*, [Z_2*, S*] = B_2*, [Z_2*, B_2*] = 0 and [t_+, Z_2*] = Z_1* by hand from the
  anticommutators: correct.
- (ii) The boson description of the symmetric even sector is correct: pi*pi = n_ij(n_0 + 1) = n_ij(n_b - P + 1), and
  the band formula E(nS, n) = K_psi(2nS + n) + K_chi n - (G_S nS + G_D n)(n_b - P + 1) is correct. Isospin n/2 holds.
- (iii) Per block, [w_3 v_1, w_1 v_3] = n_1 - n_3: correct. E(P - n, n) - E(P, 0) = n omega_D with
  omega_D = (K_chi - K_psi) + (G_S - G_D)(n_b - P + 1): correct. The J fields follow from stored kernel-bivector (ii), (v)
  at v1: correct. The defect 2n/P is correct.
- (iv) The slope argument is correct. The stretched-sector statement follows from stored
  tower-pairing-gap@2 (i), (ii) on modes 2, 3. Exact inertia agrees: 1 level below the threshold in (0, P, P).
  Note that the stretched sector holds exactly the total-isospin-P/2 levels at N_psi = N_chi = P, so the clause does
  cover every isospin-zero (amplitude) excitation of the condensate.
- (v) E_th follows from stored tower-pairing-gap (i) with chi as a spectator: correct. E_D - E_th = -G_D(n_b - P + 1),
  E_D - E(P,0) = omega_D and E_th - E(P,0) = (K_chi - K_psi) + G_S(n_b - P + 1): correct. The reduction to V_P by
  isospin is correct.
- (vi) I redid the normal ordering: C_3 = 3N - Q and sum rho rho = n_b N + Q with the same Q; the rest follows.
  Correct.
- (vii) The bound for the lowest level is correct. The second-level bound uses Weyl's inequality
  lambda_2(A+B) >= lambda_1(A) + lambda_2(B) (increasing order), which is correct as stated.
- (viii) The arithmetic from X and X_2 to the stated bounds is correct. The computed values are certified in the check
  for n_b <= 6, and my numerics agree at n_b = 7.
- (ix) Correct algebra.
- The pseudo-Goldstone point is right: at G_S = G_D and K_chi = K_psi, H = KN - GW, and W commutes with u(3) by (vi).

### The proved/computed/conjectured split
The formal level states the split correctly ("(i) to (vii) and (ix) without its last sentence proved for every n_b;
(viii) computed for n_b <= 6 and conjectured beyond"). The one-liner and the technical level state it too. The title does
not need it, since the existence of the mode and its quantum are proved for all n_b. The lay level drops it and claims
more ("the model can be solved exactly"): only the band is solved exactly.

### What is overstated (found by computation, certified exactly)
1. **The band is not the ground state at fixed N in part of the singlet regime.** The doublet gap of (viii) is defined
   as (lowest level with N_chi = 1) minus (lowest level with N_chi = 0). That is a gap between sector minima. It is an
   excitation gap of the ground state only if the ground state at N = 2P has N_chi = 0, and that fails in exactly the
   range m = n_b - P + 1 >= 3 where (viii) says "the doublet gap is exactly omega_D". At K = 0 and G_S = 1, a rational
   trial vector in the N_chi = 2 sector (2,2,2) has an exact Rayleigh quotient below the singlet band E(P,0)
   (`cert1.py`, `cert.log`):
   - n_b = 5, P = 3, G_D = 1/2 (omega_D = 3/2): RQ = -1254/137 = -9.153 < -9;
   - n_b = 6, P = 3, G_D = 4/5 (omega_D = 4/5): RQ = -12.344 < -12;
   - n_b = 7, P = 3, G_D = 9/10 (omega_D = 1/2): RQ = -15.0183 < -15.

   The proposal's own `sector_matrix` and `inertia` give the same result at n_b = 5, P = 3, G_D = 1/2 (`cross.py`):
   inertia of H - E(P,0) on (2,2,2) is (990, 10, 0), so 10 levels lie below the singlet band, while (3,3,0) gives
   (99, 0, 1).

   On a grid (numerical), the singlet band stops being the ground state at G_D/G_S of about 0.46 (n_b = 5, P = 3) and
   about 0.74 (n_b = 6, P = 3). At low filling (P <= 2, n_b <= 7) it stays the ground state up to omega_D = 0, and the
   doublet band takes over beyond that.

   So, at these fillings, "gapped only while it does not condense" and "closes where it condenses" hold on the band
   only. The Reading ("In the singlet-condensed phase the ground state is a sector vector ... the doublet is a massive
   composite") and the technical level ("If omega_D > 0 the doublet is gapped and does not condense") assume a ground
   state that is false there. The note's "Not claimed" sentence is wrong in both directions. The band also fails as
   ground state with omega_D > 0. Conversely, with a doublet condensate the doublet band is the ground state at low
   filling (n_b = 4, 5, 6, P = 2; G_D = 1.2 G_S and G_D = 3 G_S).
2. **"Never both" is contradicted by the proposal's own return quanta.** In the doublet-condensed band, the Z_2 quanta
   are even, uniform, isospin doublets, gapped at -omega_D > 0. The text excludes them only because they carry the
   unbroken N_psi - N_chi. The true statement is: "no gapped doublet neutral under the unbroken N_psi - N_chi coexists
   with a doublet condensate on the band".
3. **Sub-threshold levels in the condensed phase.** At the condensate's charges, levels of lower total isospin
   (isospin-one excitations of the condensate) lie far below the pair-breaking threshold. Exact inertia (`cert3.py`,
   `cert3.log`), K = 0, G_S = 1, G_D = 3, where the doublet band is the ground state:
   - n_b = 4, P = 2: the stretched sector (0,2,2) has 1 level below E(0,P) + G_D n_b = -6, while (1,1,2) has 16;
   - n_b = 5, P = 2: 1 level against 25.

   The formal clause, restricted to the stretched sector, is true. But the formal "its collective excitations at fixed
   P are return quanta" (true only on the band), the one-liner's "no sub-threshold amplitude level" (true only if
   amplitude means isospin zero) and the lay's "no extra bound particle appears below the energy needed to break a
   pair" (false) all overstate it.
4. Smaller points:
   - The Reading's "light only if G_D is tuned to G_S" is false when K_chi != K_psi. The mode is light near
     omega_D = 0, that is at G_D = G_S + (K_chi - K_psi)/(n_b - P + 1).
   - In (iv), "B_1* and B_2* take it to the doublet band of P + 1 pairs at the same energy" reads as if E(0, P+1) =
     E(0, P). It should read "both at energy E(0, P+1)".
   - The lay's "The mass shrinks to zero as the two pairing strengths become equal" needs "when the two kinds have
     equal energy".
   - The global-ground-state statement in the note and Reading ("computed") has no check function. Either check it or
     replace it with the certified counterexamples above.

### Exact fixes required (the true weaker statement at every level)
- **Title:** "On the symmetric band of a two-species floor the doublet pair mode is gapped and closes where the band's
  doublet condenses" (or equivalent wording that says "of the band").
- **One-liner:** add "on the band" to the omega_D < 0 sentence, and replace "no sub-threshold amplitude level" with
  "no sub-threshold level of the condensate's isospin". Add: "the band need not hold the ground state at fixed N, even
  for omega_D > 0".
- **Formal:**
  - (iv): write "on the band, its excitations at fixed P are return quanta" and "both at energy E(0, P+1)".
  - Add a computed clause (x), with a check function. It records the exact counterexamples (n_b, P, G_D/G_S) = (5,3,1/2),
    (6,3,4/5), (7,3,9/10), each at K = 0 with omega_D > 0, where the sector (2,2,2) has a level below E(P,0). It also
    states that the gap of (viii) is a gap between sector minima, and an excitation gap only where the singlet band is
    the ground state.
- **Reading:**
  - "light only near omega_D = 0 (at K_chi = K_psi, G_D near G_S)".
  - Replace "never both" with "on the band, no gapped doublet neutral under the unbroken N_psi - N_chi alongside a
    doublet condensate; the return quanta are gapped doublets charged under it".
  - Scope the singlet-phase sentence to the couplings where the singlet band is the ground state.
- **Note:** rewrite the "Not claimed" sentence on the global ground state as described in item 1.
- **Technical:** "on the band, if omega_D > 0 ...".
- **Lay:**
  - "its symmetric band can be solved exactly; the rest is computed for up to six blocks".
  - "as the two pairing strengths become equal and the two kinds have the same energy".
  - "no extra bound state of the condensate's own isospin".
  - Mark the last sentence as a reading about the band.

Literature: I verified Bardasis-Schrieffer, Phys. Rev. 121 (1961) 1050 (title "Excitons and plasmons in
superconductors", DOI 10.1103/PhysRev.121.1050). I did not check NJL, Bardeen-Hill-Lindner, Kaplan-Georgi or Howe
online. Their citations match my knowledge, and the proposal correctly marks them "cited from memory" and not used.

## 2. synthesis.uniform-pair-channel-of-a-tower-condensate-is-a-goldstone-rotor: SOUND WITH FIXES

### Steps verified
- (i) and (ii) are elementary and correct; the equality case is right.
- (iii) I re-derived [XX*, X] = -XC and [XX*, X*] = CX*. Then [H, X] = eps X + GXC, and the quotients are
  eps + Gc(s) and -eps - Gc(s - h). The second-difference bound and the ground-sector corollary are correct at every
  size. The hypotheses ([H_0, X] = eps X, and C acting as a scalar on each sector) are stated and are all that is used.
  The check also tests H_0 with L(N_a - N_c)^2 + R D added, which is a good test of generality.
- (iv) For the stored single shell, C = N - n_b (stored how-close@4: [P, P*] = n_b - N), so the step is 2 and the bound
  is 2G. It is attained, because the band is a parabola with curvature G. The global ground state follows from stored
  tower-pairing-gap@2 (i) with K >= 0. My own sector computation gives a maximum second difference of exactly 2G.
- The scope requested in point 2 of the brief is stated in the formal Reading ("The doublet floor and inter-condensate
  couplings, where [X, X*] is not a function of the charges, are not treated here") and in the note. It is not stated
  in the title, the technical level or the lay level.

### Problems
1. The title "the uniform pair channel of a pairing condensate is a rotor" and the technical reading "a condensate's
   uniform composite scalar is its Goldstone rotor" are unscoped. They are proved only under (iii) and for the single
   shell.
2. (iv)(c) lists n in {0, ..., n_b - 1}, but K = G(n_b/2 - n) >= 0 needs n <= n_b/2, and the proof's bound
   E(p) + Ks + Gps >= E(p) uses K >= 0. My numerics suggest the statement still holds for K < 0 (n_b = 4, 5, 6 with
   n = n_b - 1, and n_b = 5 with n = 3), but this is not proved.
3. In the proof of (iv), "gamma <= (n_b + 1)/2 < n_b - 1/2 for n_b >= 2" is false at n_b = 2, K = 0, where the two sides
   are equal and E(1) = E(2) = -2G (my run confirms the tie between sectors (1,1) and (2,2)). The conclusion survives:
   that point is the degenerate coupling n = 1 of (c).
4. Prior art and duplication.
   - The rotor E(n) = G(n - gamma)^2 - G gamma^2 is the classical pairing-rotational band of nuclear physics
     (pairing rotations, with a moment of inertia set by 1/G; Bes and Broglia, Nucl. Phys. 80 (1966) 289, "Pairing
     vibrations", verified to exist online; Bohr and Mottelson, Nuclear Structure II, from memory). It should be named
     as prior art next to Anderson's tower of states.
   - "The uniform channel P + P* moves only along the band and does not reach [the threshold]" is already stored in
     tower-pairing-gap@2 (ii). The "weights of the uniform channel" are therefore not new beyond the explicit quasi-spin
     norms, and the note should say so.
   - "The finite Goldstone theorem" in the note overstates (iii), which is a bound for one class of elements. It
     becomes a gaplessness statement only when G times the step of c tends to 0.
5. The Reading says "a gapped composite doublet would have to be one that does not condense, or a non-uniform mode".
   The first proposal's return quanta Z_2 = sum_b w_1 v_3 are uniform, even, isospin doublets, and are gapped in a
   doublet-condensed band. They are particle-number-conserving hoppings, not pair-channel modes. The Reading (and the
   lay level, "it would have to be some other mode, or a doublet that does not condense") should say "a mode outside
   the condensate's pair channel".
6. Minor: (i) to (iii) use the positive Fock inner product with v* = w. The proposal cites ladder-pairs@4 and
   imported-tower-limit@3, and neither fixes the adjoint. It should cite the store entity that does, as the first
   proposal does with kernel-bivector.

### Exact fixes required
- **Title:** "Finite Goldstone bound: for pairing-type elements the uniform pair channel of a condensate is a rotor".
- **Technical:** add the sentence "The doublet floor and coupled condensates, where [X, X*] is not a function of the
  charges, are not covered". Do the same in the lay level ("in this model" is not enough).
- **(iv)(c):** use n in {0, ..., floor(n_b/2)}, or drop K >= 0 there and prove it.
- **Proof (iv):** write gamma <= n_b - 1/2 and choose the minimiser n* <= n_b - 1, with the tie at n_b = 2, K = 0
  covered by (c).
- **Note:**
  - Add pairing rotations (Bes-Broglia 1966, Bohr-Mottelson) as prior art.
  - Credit stored tower-pairing-gap (ii) for "P + P* stays on the band" and remove it from "New here".
  - Replace "the finite Goldstone theorem" with "a finite Goldstone (rotor) bound".
- **Reading and lay:** replace "or a non-uniform mode" with "or a mode outside the condensate's pair channel (such as
  a particle-number-conserving hopping doublet)". In the lay level, mark the composite-Higgs sentence as a reading
  (argued).
- **Premises:** cite the entity that fixes the adjoint v* = w.

## 3. synthesis.even-composite-doublet-needs-a-singlet-constituent-and-its-pair-modes-are-quasi-spins: SOUND WITH FIXES

### Steps verified
- (i) Monomial basis, splitting by (p_D, p_S), invariance under ad T_j and ad Y, and the ad T_3 weights in
  p_D/2 + Z: all correct. So every half-integer-isospin element is odd in the doublet modes, and an even one is odd in
  the singlet modes. The answer to point 3 of the brief: yes, "an even doublet needs an odd number of singlet factors"
  is correct. The tensor-product identification and the Casimir multiplicities (3 dim A_S^{p_S}) are correct; the check
  confirms dimensions 16 and 64. I verified the four bilinear doublets with their signs (for example
  [T_-, a_s* a_down] = -a_s* a_up) and their hypercharges.
- Is (i) new against the rung result? It is an elementary generalisation of stored rung@3 clause (2) (no singlets) to
  any number of doublet species and singlets. It turns the parity part of the stored step 5 (argued there) into a
  proof. The note says this correctly. The representation theory is classical (the Yukawa structure), and the note
  marks it as orientation.
- (ii) The nilpotency argument for a weight-charged M is exactly stored helicity-one@1 (iii), whose note already
  records that the weights may be any real numbers. The edge-clean values q +- 1 and the mutual commutator are direct
  instances of the stored window identity (i). The answer to point 3 of the brief: clause (ii) is a restatement of the
  stored theorem applied with the isospin and hypercharge weights. Its only new content is two explicit evaluations.
  The note says so, but the title and the one-liner present it as a co-equal result.

### Problem: the M^2 = 0 hypothesis is dropped above the formal level
The formal (ii) correctly requires M^2 = 0 for the quasi-spin norms. But the one-liner ("every component of a doublet
of pair densities is charged, nilpotent and a quasi-spin of q rank(M) sites"), the technical level ("on the sea it is a
quasi-spin of q rank M sites") and the note drop it. A T_3 = +1/2 component need not have M^2 = 0. Take
M = E_{up,s} + E_{s,down}: it has T_3 weight +1/2, it forms a doublet with E_{down,s} - E_{s,up}, and
M^2 = E_{up,down} != 0. On the window of `m2.py` with q = 1, the norms |B^p Omega|^2 are 1, 2, 6, 18, against the
formula (p!)^2 C(2, p) = 1, 2, 4, 0, so B^3 Omega != 0 although q rank(M) = 2. With hypercharge, the same happens for
two doublet species with Y_delta = Y_s + 1/2 and Y_delta' = Y_s - 1/2. M^2 = 0 does hold for a single doublet-singlet
hopping, and for any component of nonzero hypercharge when all doublet channels have the same hypercharge.

### Exact fixes required
- **One-liner, technical and note:** add "when M^2 = 0 (for example a single doublet-singlet hopping, or nonzero
  hypercharge with all doublet channels of one hypercharge)" to the quasi-spin statement. "Charged, nilpotent, never
  normal, never a canonical boson" stands without it.
- **Lay:** "for the simplest such pair, a finite bank of two-state switches".
- **Labelling of (ii):** make it a corollary of synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins
  (iii) and (iv) at the one-liner and technical levels, for example "...; by the stored helicity-one theorem read with
  isospin weights, ...". Optionally retitle "An even composite doublet needs a singlet constituent; its pair modes are
  quasi-spins (corollary)".
- **Minor:** v* = w is attributed to ladder-pairs@4, which does not state it. Cite the adjoint's source.

## 4. Consistency across the three proposals and with the stored results, and the Higgs claims
- The first proposal's doublet quanta (Z_1*, Z_2*) = (v_3 w_2, w_1 v_3) are the third proposal's hopping doublet
  (a_s* a_down, -a_s* a_up). Its B_alpha* are the third proposal's particle-particle doublet, and its J-field defect 2n/P
  is the quasi-spin capacity the third proposal describes. These agree. The third proposal's parity rule is realised by
  the first.
- The second proposal excludes the doublet floor, consistently with the first proposal's [B_a, B_b*], which is not a
  function of the charges. Its reading ("or a non-uniform mode") is not consistent with the first proposal's gapped
  uniform return quanta; fix 5 above repairs it.
- With the stored results:
  - The first proposal reduces to field-theory.composite-scalars-mean-field-level (2) on modes 1, 2 and to
    tower-pairing-gap (i), (ii) in the stretched sector.
  - The second proposal's (iv) repeats tower-pairing-gap (ii) in part (see fix 4 above).
  - The third generalises rung (2) and specialises helicity-one (iii) and (iv).

  Every pinned version is current: imported-tower-limit@3, composite-scalars@5, tower-pairing-gap@2,
  kernel-bivector@1, how-close@4, rung@3, helicity-one@1, ladder-pairs@4. The parts used say what is needed.
- The Higgs: none of the three contradicts the store's elementary reading, and every Higgs statement in the formal
  readings is marked "argued". The overreach is at the lay levels. The first proposal's last lay sentence, "never a
  condensed doublet together with a light bound scalar of the Higgs kind", is true only on the band and for neutral
  doublets of the condensate's isospin. The second proposal's "a composite Higgs built from a condensate of this kind
  cannot be the condensate's own uniform mode" is unmarked. Both need "(argued; on this model)" wording, as in the
  fixes above.
- House style: no em dashes and none of the banned words, Q(e) used, J (not an imaginary unit) as the unit,
  everything in the CAR on tower planes. No issues.
