# fixes-KB: fix round for synthesis.no-spin-independent-curvature-level-set-carries-the-count-to-slow-kerr

Referee R2, Proposal 2: SOUND WITH FIXES (title, one-liner, lay OVERSTATED as filed). All ten fixes applied in place
in proposals/<id>/ (id kept); the scratch copy in work/KB/<id>/ is synced. Gate run by me: runcheck only, 5/5 PASS.

New title (85 characters): "Slow Kerr (0 < a <= 4 rho/5): no spin-independent modulus level set gives A/4 exactly".
The referee's title was over 90 characters; this one keeps "modulus", the spin window and "exactly". It does not
fit rho <= M/3, which is in the one-liner, formal, technical and lay levels.

Clause label of the determinant lemma, for the sibling to cite: clause (2) of the formal statement
("Determinant lemma, and the geometry of the level set"), first display:
det h = -Sigma [Delta(R) + (1 - u^2) R'^2] for any Killing-invariant surface r = R(u), in the source's signature,
for every flow d_t + Omega d_phi; +Sigma[...] in the store's product. KA's clause (i) is its case R' = 0.

| Fix | Status | What was done |
|---|---|---|
| 1 title | applied, shortened | as above |
| 2 one-liner | applied | lower half of the bound added; scope (modulus, rho <= M/3), the untreated window and "for a/rho -> 0 the count still agrees with A_+/4 at leading order" appended; "exactly" added |
| 3 lay | applied | last sentence replaced by the referee's text |
| 4 proof of (2) | applied | Boyer-Lindquist paragraph removed; proof by the cofactor rule in the Kerr-Schild gauge alone (det g = -Sigma^2 by the rank-one rule, g^rr = Delta/Sigma, g^uu = (1-u^2)/Sigma, g^ru = 0); the sample is now called a consistency check |
| 5 general lemma | applied | clause (2) states the determinant once for r = R(u), then specialises to the level set |
| 6 item 4 | applied | exactness of the equality, Q(M,0) = sqrt(1 - rho_c/2M), both halves of the bound, the leading-order miss for a/rho bounded below, agreement for a/rho -> 0; mirrored in the technical level |
| 7 closing paragraph | applied | "and only level sets with rho <= M/3"; the modulus reading named as the stored ring count's reading and as one choice among the algebraic scalars of synthesis.c1-c2-forms-forced-one-number (cited by claimref, not added to `uses`, since no check touches it) |
| 8 "function of a/rho" | applied | reworded as the referee gives it |
| 9 "does not use rho <= a" | applied | proof and extraction note now say the stored theorem states the expression for rho <= a and it is proved here directly |
| 10 check | applied | unused premise removed from check_quarter_power_bounds (it now touches none: it is polynomial arithmetic); new function check_determinant_in_the_store_product computes one point in Cl(1,3) through GA.py in the store's product (M = 7, a = 3, r = 4, u = 3/5, value -8968726/15625 = +Sigma(Delta + (1-u^2)R'^2)), added to checked_by and coverage.yaml; one point of the general lemma with a slope off the level set added to check_level_set_determinant; its coverage entry reads "sampled, consistency check of the identity proved in the text" |

Not done, for the maintainer: the referee's note that the last sentence of the stored
synthesis.kerr-ring-count-misses-area-law ("for small spin the locus is a closed spacelike surface") holds only for
a < rho_c with sqrt(rho_c^2 - a^2) > r_-; the id rename (Leon is being asked).
Possible gate points for the orchestrator: check_quarter_power_bounds touches no premise; `uses` is unchanged from
the filed version.

check4: pending (orchestrator)
