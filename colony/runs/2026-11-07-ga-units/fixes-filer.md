# Fix round, filer, run 2026-11-07-ga-units

Every fix in referee.md is applied in place in `proposals/<id>/`, and every file is kept. Only `colony/runcheck.py` was run. I made no rebuttals.

- **Pins:** all current. fock-space-maxwell-modes@4, positive-conformal-energy@6, two-families@6, cpt-closure@1, even-slots@3 and blade-square-signs@2 are unchanged since filing.
- **Newly cited, not used:** light-ray-good-part-of-a-spinor-is-two-chirality-arrays, where-each-lives, arrow-frequency-are-one-bit-level, imported-flag-arrow-superselection, cpt-conjugation-pseudoscalar-rotor-times-complex-conjugation, tower.commuting-copies and orientation-relocated. They are cited with \claimref only. Most of them carry premises (several carry many), so putting them in `uses` would add those to holds_given.
- **Scans:** the style scan and the bare-i detector are clean. Every \claimref resolves.

check4: pending (orchestrator)
validate_draft: pending (orchestrator)

## 1. synthesis.massless-frequency-sign-relative-to-i4-is-not-the-chirality (SOUND WITH FIXES)
**Check:** runcheck gives 30 pass, 0 fail.

1. **Duplication.** (i) and (ii) are now presented as restated for use, citing light-ray-good-part (iii)-(iv) and where-each-lives (4). The claim "a general proof of the sampled clause (iii)" is dropped from formal, technical, Step 1 and the note.
2. **Chirality wording.** (v), the technical level and the one-liner now say "the chirality Gamma (label e = -Gamma)". A sentence states that its identification with the doublets' handedness (I6 against I4 on L_0, L_inf, where-each-lives (3)) is assumed, not shown. This is also added as a flag; the lay level is adjusted to match.
3. **Time reversal.** A sentence is added in (iv), Step 4 and the technical level: the reversal that (N+) calls time reversal is the I4-linear PT, which flips s; the antilinear T keeps s.
4. **Premise wording.**
   - The technical level now says the result "uses fock-space-maxwell-modes only for the chirality label".
   - The projectors chi_e are attributed to that result's check.
   - Added to (ii) and Step 2: s = -gamma s_H, where s_H is the frequency sign relative to R_{I sigma3}. A new check covers it.
5. **chi_e test.** The test now uses the premise's literal IS3 = {(1, 2): -1}, and asserts ISIG3 == IS3. Under the referee's perturbation (I sigma3 replaced by I sigma1), the (ii) chi_e checks now fail, as do the C and CP checks (verified on a perturbed copy in scratch).
6. **Sign convention.** It is now stated that B_k = g0 n is minus the light-ray entity's boost bivector n g0, and that both give the same S_k.

## 2. synthesis.z-adapted-witt-flags-energy-sign-and-family-are-independent (OVERSTATED, restated)
**Check:** runcheck gives 14 pass, 0 fail.

The proposal is restated on every level to the referee's weaker statement:
- **Title:** "Energy sign and family of the $Z$-adapted Witt flags".
- **Statement:**
  - Z psi = -s0 psi I6, and I6 psi = omega(J_s) psi I6, where omega = -s0 s1 s2 is the orientation of J_s relative to I6. This is the family.
  - As functions on the eight flags, s0 and the family are independent.
  - On each conjugate pair {W_s, W_-s}, which are the two values of the stored bit (J against -J), both flip, and s0 omega = -s1 s2 stays fixed.
  - Read as the energy sign of the flag's vacuum, the (N+) datum is therefore the stored flag bit up to the descent's kinematic sign s1 s2. This reading is labelled argued.
  - It is consistent with one-relation.arrow-frequency-are-one-bit-level and one-relation.imported-flag-arrow-superselection.

Referee fixes 1 to 8:
- (i) now reads "in CS = Cl+(2,4)P (respectively its odd counterpart)".
- (ii) states the identification of the attachment's unit with +R_{I6} as a convention, citing orientation-relocated (3): with -R_{I6}, T+ and T- exchange.
- (iii) defines the family as omega(J_s). The wrong parenthesis is replaced by "with the opposite orientation of I6 the family reads +s0 s1 s2 for the same s, and (ii) is unchanged".
- The conjugate-flag clause cites cpt-conjugation (2)-(3).
- Ledger wording: the algebra is transport-absent, and the derived essential label is inherited from positive-conformal-energy, which is used only for the frame and Z.
- **New checks:**
  - omega(J_s) computed from e0 ^ Je0 ^ e1 ^ Je1 ^ e3 ^ Je3 = omega I6, and equal to -s0 s1 s2;
  - the conjugate-pair relation: s0 and the family both flip under s -> -s, s1 s2 stays invariant, and s0 * family = -s1 s2, checked on the kernels themselves.
- The family check function is renamed to check_the_family_is_the_orientation_and_flips_with_the_energy_sign_on_conjugate_pairs, and checked_by is updated.
- The extraction note says that the earlier reading is withdrawn. A third flag records the restatement after the OVERSTATED verdict.

**The id is unchanged.** The slug "...-are-independent" is kept so that `proposals/<id>` and every file stay in place. It is still true as a statement about functions on the eight flags, but it now under-describes the result. The maintainer may want to rename it at acceptance (decision for Leon). Because of the OVERSTATED verdict, this one goes to Leon individually (POLICIES 4).

## 3. synthesis.fock-slot-module-is-cpt-closed-only-over-one-doublet (SOUND WITH FIXES)
**Check:** runcheck gives 13 pass, 0 fail.

1. **Technical:** the level now says "fixes the statistics (fermionic) and the number of doublets (one); the unique vacuum is part of the Fock clause".
2. **Unique vacuum:**
   - (iv) adds "(the unique vacuum is part of the Fock clause)".
   - The note now reads "replaces the one-doublet part of (G); the unique vacuum is kept, inside the Fock clause".
   - Step 5 says the unique vacuum is not derived.
3. **Lay:** now "a more natural assumption, which keeps the single empty state, does the rest of the job".
4. **Hypercharge argument:** added to (iii), Step 4 and the technical level. Y is bounded below by -1 and unbounded above, and conjugation negates Y, so the symmetric module fails CPT closure itself. A new check covers it: for b = 1 and n <= 6, Y has minimum -1 and maximum 3, and -3 is absent.
5. **Overlap with the theorem:** it is stated in (iv), Step 5 and the note that for b = 1 the conclusion is clause (3) of the theorem.

## 4. synthesis.joint-clifford-clause-is-a-klein-convention-on-the-composite-space (SOUND WITH FIXES, minor)
**Check:** runcheck gives 18 pass, 0 fail.

1. **Step 1 identification test.** It works in the labelled basis x_K x_J f:
   - v_i Gamma_W and w_i Gamma_W keep the pair label, with a sign independent of K, so they act as a (x) 1;
   - the slot vectors carry (-1)^k.

   Under the referee's reordering perturbation (slot creators to the left), the a (x) 1 test now fails, as it should (verified on a perturbed copy in scratch).
2. **Cross bivectors.** A sentence is added in (v) and Step 5: the 24 cross bivectors depend on the convention. The residual sign c = -1 acts on them by Ad of the slot parity (-1)^n = e0 f0 e1 f1, which has reverse norm 1 and is the central -1 of the slot U(2), an element of Spin(10). So the Spin(10) of clause (f) is canonical as a subgroup. A new check covers it: U is the slot parity, U U~ = 1, Ad(U) flips the slot Majoranas, fixes the pair ones and negates all 24 cross bivectors.
3. **Twisting device.** tower.commuting-copies is now cited for it, read backwards, next to even-slots-need-a-spectator-generator (iii).

## Decisions for Leon
- Proposal 2 has been restated after an OVERSTATED verdict, so it goes to Leon individually. Optionally, its id slug could be renamed at acceptance.
- The referee's notation point: the store has two opposite normalisations of the boost bivector of a null generator. Proposal 1 now states which one it uses. A notation note in conventions.md would prevent sign slips.
