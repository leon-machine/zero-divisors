# fixes-SA (fix round)

check4: pending (orchestrator). runcheck.py: both proposals, every function PASS after the fixes.

## synthesis.central-limit-of-tower-fluctuation-states-with-the-kernel-unit (SOUND WITH FIXES)
1. Title: "Central limit of tower fluctuation states for product block states, with the kernel unit" (88 characters;
   the referee's longer version with "and collective brackets" exceeds the 90-character limit, so that tail was dropped;
   the brackets stay in the one-liner and formal (i)).
2. Bound: the norm sum is now nu = sum_j ||y_j||_1 in formal (ii)(c) and proof (c); the display reads
   (nu^3/6) e^{nu/sqrt N} N^{-1/2} + (nu^4/8) e^{nu^2/2N} N^{-1}.
3. Trace claim restricted to transport elements (formal (i), technical, proof): "no commutator of elements of T_J
   equals a nonzero element of span{1, J} (in the whole level J = [g1, g2]/2 is a commutator)". The check now
   computes [g1, g2] = 2J and tr([g1, g2]) = 2J != 0.
4. Proof (d): added the cumulant expansion log omega(e^{Jty}) = -kappa_2 t^2/2 - J kappa_3 t^3/6 + O(t^4), giving
   omega_N(W_N(x)) = e^{-c}(1 - J kappa_3/(6 sqrt N) + O(1/N)): a nonzero kappa_3 makes the error exactly of order
   N^{-1/2} (leading coefficient e^{-c}|kappa_3|/6, matching the referee's own number 0.014227).
5. Proof (iii): telescoping K psi_{j+1} = K* K psi_j + (N - 2j) psi_j from the stored [B, B*] on the ladder, giving
   (l + 1)(N - l); cites synthesis.ladder-states-are-locally-product-with-non-gaussian-fluctuations (i) (plain id) and
   field-theory.how-close-tower-comes-ccr (now a declared premise @4, touched by the polarised check). Formal (iii),
   technical and proof: "on the hopping pair (phi, pi) the limit is the Fock vacuum"; the other fields are
   deterministic in the polarised state.
6. Extraction: "New to the store"; the Cushen-Hudson theorem named as the content of (ii) for identical product blocks
   (with the unit J and an elementary explicit bound; rates are in the literature); R. L. Hudson, A quantum-mechanical
   central limit theorem for anti-commuting observables, J. Appl. Probab. (1973), as prior art for odd elements (located
   by search, volume and pages not verified).
7. Overlap ruling: graded locality cited to synthesis.ladder-bosons-inherit-spin-statistics-from-the-single-modes (ii)
   in formal (i), technical, proof (i) and extraction; ladder coefficient cited as in 5.

## synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves (SOUND WITH FIXES)
1. Formal (iv): "do not hold on every vector off that subspace (the check exhibits one where they fail; on others, such
   as the vector with both families empty, they still hold)".
2. Lay: "a changed common speed (slower or faster, depending on the two couplings)".
3. Extraction: Schoenhammer and Meden, Am. J. Phys. (1996), doi:10.1119/1.18339, eq. (38) named as prior art for
   finitely many fermions on levels bounded below; the window form "new to the store, not to the literature";
   "New to the store: (i)".
4. Check: [H, gamma*] = (6/5) gamma*, gamma* = rho_L* + (1/3) rho_R, added to the same 16-vector loop (passes), so the
   proof's sentence is now true. Also found and repaired: the one-particle check "T acts as j on v_j Omega_0", which the
   proof cites, had not reached the filed check (an earlier edit was skipped by a failed shell step); it is now in
   check_window_sugawara_identity_holds_as_an_algebra_identity and passes. The tautological band-occupation line is
   replaced by the band average of chi_(-inf,0) computed from the interval endpoints, (min(hi, 0) - min(lo, 0))/Delta.
