# fixes-KA: fix round on synthesis.stretched-horizon-count-on-kerr-gives-the-area-law-at-every-spin

Referee R2: SOUND WITH FIXES (id, title and one sentence of (vi) OVERSTATED as filed). Fixes applied in place in
proposals/<id>/ (entity.md, proof-main.tex, check.py, coverage.yaml). The id and folder are NOT renamed here (the
orchestrator renames to synthesis.stretched-horizon-count-on-kerr-is-a-multiple-of-the-area-by-construction).
New title (81 characters): "On Kerr a stretched-horizon count is a fixed multiple of the area by construction".

1. Id/title: title rewritten, the cancellation leads; id left for the orchestrator. APPLIED (title).
2. One-liner: the referee's wording, with "(not adopted)" and "no test of the density". APPLIED.
3. Lay: the referee's replacement; "product of packing density and distance"; one sentence that area proportionality
   is known from the literature. APPLIED.
4. (SH) identified with the modes of hypothesis (H) and the cutoff modes, not added; cites
   synthesis.c-loc-is-a-second-placement-of-the-count, added to uses @3, touched in the check (doubling arithmetic).
   APPLIED.
5. (SH) is a three-volume form of (H) at one nat per mode, consistent with (Loc) at eta = 1/4 and not a clause of it:
   statement, clause (iv), technical level and extraction note. APPLIED.
6. Clause (iii): nu rho_0 = 1/8 pi is the value at which (SH) reproduces the Schwarzschild area law, no stored premise
   fixes rho_0; remainder c(a/M) rho_0^2/M^2 with c(0) = 1/12 (derived in the proof for Schwarzschild, outside; sign
   reversed inside); c for a > 0 labelled computed numerically (referee's values). APPLIED.
7. Clause (vi) first sentence restricted (0 < a < M, fixed a/M, side r > r_-; not uniform as a -> 0; needs
   rho_0^2 M << r_-^3; rate -> 12 pi M rho_0 = 3 kappa_+ rho_0 A_+, labelled computed, with the referee's table in the
   proof); synthesis.exceptional-boundary-measure-one-calibration added to uses @2 and touched; technical level
   qualified likewise. APPLIED.
8. Attribution: only kappa_+, A_+, Omega_H, J, T_H, S from the Fact; kappa_-, A_- are notation for a > 0; Smarr
   "classical; verified directly in the proof, not imported". APPLIED.
9. Clause (iv): "norm-gradient form of the surface gravity ... equivalent classically ... verified here directly".
   APPLIED (statement, proof, technical).
10. Signature sentence added (store's product: +Delta Sigma, Q(K) = Delta Sigma / P^2 at Omega = a/P); "stored"
    dropped from the g^{rr} relation. APPLIED. The identity g(K,K) = -Delta Sigma / P^2 is asserted at four rational
    points in the check (sampled, not proved symbolically).
11. Technical: "the third, 2 nu kappa A, is the rate of (SH) itself and agrees by construction". APPLIED.
12. Check: (a) generator null and orthogonal to d_phi on the locus at Omega_H = a/P_+, not null at -a/P_+, and the
    cross-section area element P_+^2, at three latitudes for five holes; (b) one point in Cl(1,3) through GA.py with
    the store's product and hb^{-1}(b) = b - H (b.k) k: Gram determinant +Delta Sigma = -14911/25 at
    M = 7, a = 3, r = 4, u = 3/5 (the referee's value), Q(k) = 0 asserted; (c) docstring clause numbers and
    "two stored forms and the area form" corrected. APPLIED. runcheck: 4/4 PASS.
13. Literature: 't Hooft 1985 and Susskind-Thorlacius-Uglum 1993 with the referee's checked references; Lee and Kim
    hep-th/9603055 added as direct prior art (journal reference not given, unchecked); area proportionality removed
    from the "what is new" list. APPLIED.
Sibling lemma: clause (i) and the proof now cite clause (2) of
synthesis.no-spin-independent-modulus-level-set-gives-the-area-law-exactly-on-slow-kerr (uses @1 + claimref), and
clause (iii) uses its exact integrand sqrt(Sigma |Delta(R) + (1 - u^2) R'^2|) in place of the O(delta) estimate; a
two-line rank-one derivation of the case R' = 0 is kept in parentheses. The check does not call premise() for it (it
is not in the store yet, and the check recomputes R' = 0 itself); coverage.yaml lists it under untouched_premises.
NOTE for the orchestrator: the uses edge @1 will only validate once that entity is in the store.
Not applied: nothing. Not done by me: rename of id/folder; check4, validate_draft (not run, as instructed).
coverage.yaml updated for the new assertions.

check4: pending (orchestrator)
