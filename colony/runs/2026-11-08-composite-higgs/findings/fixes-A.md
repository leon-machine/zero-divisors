# Fixes A: synthesis.two-species-floor-pairing-has-a-gapped-doublet-pair-mode-that-closes-where-it-condenses

Referee verdict (verify/H.md): OVERSTATED. The clauses (i) to (ix) hold, but they are statements on the band, and
the doublet gap is a gap between sector minima. Restated to the weaker statement at every level. The id is
unchanged.

## Fixes and where they went
1. **Title.** It is now "Two-species floor band: the doublet pair mode is gapped until the band's doublet condenses"
   (90 characters, quoted in the YAML).
2. **One-liner.**
   - The omega_D < 0 sentence is now "on the band".
   - "no sub-threshold amplitude level" became "no sub-threshold level of the condensate's isospin".
   - Added: "the band need not hold the ground state at fixed N, even for omega_D > 0".
3. **Formal (iv).**
   - "both at energy E(0, P + 1)".
   - "on the band, its excitations at fixed P are return quanta".
   - The stretched sector is identified as exactly the isospin-P/2 levels at N_psi = N_chi = P, so the clause now
     reads "no level of the condensate's own isospin lies below pair breaking".
4. **Formal (viii).** The doublet gap is now called "the gap between sector minima".
5. **New computed clause (x)**, with the new check function
   `check_band_need_not_hold_the_ground_state_and_condensate_levels_below_threshold`. It certifies two things exactly:
   - **Singlet regime.** At (n_b, P, G_D/G_S) = (5, 3, 1/2), (6, 3, 4/5), (7, 3, 9/10), with K = 0 and omega_D > 0,
     the sector (2, 2, 2) has a level below E(P, 0). The certificate is congruence diagonalisation on the
     43-dimensional subspace invariant under permutations of blocks 2..n_b; the subspace symmetric in all blocks has
     none. E(P, 0) is confirmed as the N_chi = 0 minimum at n_b = 5.
   - **Doublet-condensed regime** (G_D = 3, n_b = 4, 5, P = 2). The stretched sector has 1 level below the threshold
     and the sector (1, P - 1, P) has n_b^2 (16, 25), all but one of isospin below P/2, and none below the band.
   - The clause states that the gap of (viii) is an excitation gap only where the singlet band is the ground state.
   - The closing sentence now also says that (x) is computed exactly at the couplings listed.
6. **Reading (formal and proof).**
   - "light only near omega_D = 0", given explicitly as G_D = G_S + (K_chi - K_psi)/(n_b - P + 1), replacing
     "tuned to G_S".
   - "never both" became "on the band no gapped doublet neutral under the unbroken N_psi - N_chi accompanies a
     doublet condensate; the return quanta are gapped doublets charged under it".
   - The singlet-phase ground-state sentence is scoped to where the singlet band is the ground state. In floating
     point that is P <= 2 with n_b = 4, 5, and it fails at the couplings of (x); I rechecked this myself (ex7.py),
     and it is labelled as not part of the proof.
7. **Note.**
   - The "Not claimed" sentence on the global ground state is rewritten. It now says the global ground state is not
     determined, cites the counterexamples of (x), restates the sector-minima gap, and confines the
     doublet-condensed statements to the band and the stretched sector.
   - Clause (x) is added to the list of results new to the store.
8. **Technical.**
   - Added "On the band, if omega_D > 0 ...".
   - Added a sentence on the off-band levels and the sector-minima gap.
9. **Lay.**
   - "the model's symmetric band can be solved exactly, and the rest is computed for up to six blocks".
   - "as the two pairing strengths become equal and the two kinds have the same energy".
   - "no extra bound state of the condensate's own isospin".
   - Added a sentence that the band is not always the lowest arrangement.
   - The final sentence is marked "Read on the band (an interpretation, not a proof)".
10. **Proof.**
    - Step (iv): "both at energy E(0, P + 1)", the stretched-sector isospin identification, and a pointer to (x).
    - A new step (x) describes the certificates.
    - The Reading is restated as in 6.
11. **coverage.yaml.** Added an entry for the new function.

## Gate
- runcheck: 8/8 pass.
- check4: 0 errors; 1 other finding, I405 (info: the rung-odd premise is declared and untouched, as recorded in
  coverage.yaml); mutants ok.
- validate_one: ok, no codes (only the I305 info).
- Re-registered with propose_claim. The previously filed folder was moved aside to
  work/A/aside/<id>.v-filed. entity.md, proof-main.tex and check.py are identical to the drafts, and coverage.yaml is
  copied back.
