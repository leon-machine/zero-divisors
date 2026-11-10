# Fix round, run 2026-11-10-phase1

Referee reports: colony/runs/2026-11-10-phase1/verify/R1.md and verify/R2.md. Read your proposals' sections in full; the
required fixes there are your fixes, with the overrides below. Apply every fix in place in proposals/<id>/ at every level
(title, one-liner, formal, technical, lay, proof, extraction note, check). OVERSTATED proposals are restated to the
referee's true weaker statement at every level; numbers never appear above the proof text that proves them. Keep every
stored file. Run ONLY `PYTHONDONTWRITEBYTECODE=1 python3 colony/runcheck.py proposals/<id>/check.py`; never check4,
validate_draft or tp check (the orchestrator reruns them centrally). Write findings/fixes-<name>.md with
"check4: pending (orchestrator)". Rebut a fix only with a computation. Do not edit store/, commit, push or spawn agents.

## Overrides (Leon's decisions and store rules)
1. No new imported Facts. Leon decided (this run) that the lens-space inputs (cohomology rings, T Sigma + R, q1 and p1,
   the K-ring, lambda-operations, Sq^1) are NOT imported. Instead state them in the formal statement as explicit
   hypotheses ("Given the classical facts (L1)-(L3), cited from memory and not in the store: ..."), so each result is a
   conditional theorem, and say in the extraction note that deriving them is an open item. The same for completeness of
   spinor harmonics and the exact/co-exact split (horizon channels). Existing stored Facts may be cited and pinned (for
   example synthesis.imported-whitney-product-formula-and-projective-space@1,
   synthesis.imported-brst-kugo-ojima-strocchi-and-gribov@1).
2. No new assumes edges in proposals (maintainer-only, E203). Where a referee asks to add a postulate to `assumes` (for
   example (Q)@3, the window reading, C2), do not add it: name it in the extraction note under "premises used, assumes edge
   for the maintainer" and the orchestrator will put it to Leon.
3. No proposal can cite another proposal (E201). Overlap rulings that ask one proposal to cite a sibling are done by the
   maintainer after acceptance: remove the duplicated content only where the referee says it is duplicated with no loss,
   otherwise keep it, and add one sentence in the extraction note naming the sibling id as the intended citation.
4. J3 caveat (R2 points 1, 2, 5; R1 point 3): the stored postulate hawking.joint-j3-s-wave-reduction reads integer-weight
   channels as currents of the arrays; Leon has decided to narrow it to spin 2 once the horizon-channel derivation is
   accepted. State every boson-counting reading relative to J3 as R2 says.


## This run
Ignore any caveat above that names entities of an earlier run. Referee reports: verify/R1.md (entanglement), verify/R2.md
(Kerr, when it exists). Apply every numbered fix, the common fixes C1 to C6 and the overlap ruling; ids are never renamed
(fix titles). Do not delete files with shell removal commands.
Leon's decisions (DECISIONS.md): (P) is adopted as a named postulate WITH reality (omega(x-dagger) = omega(x)); the
maintainer creates the postulate after acceptance, so in the proposals (P) stays a named in-statement hypothesis, stated
verbatim and identically in all six at formal, one-liner, technical and lay level, with the extraction note saying it
is to become an assumes edge. Parity: both settings are recorded side by side (parity-even observables with two modes
per party; the one-mode Klein-twisted realisation with parity-odd elements), neither is called the physical one, and
each result says which setting it is in.
Order, because a proposal cannot cite a proposal: the base
(synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate) is fixed first, gated and
accepted into the store; the other five are then revised to cite it at version 1 (uses edge + claimref) and drop their
copies of the identity, the single-pair bound and the blade lemma, as the overlap ruling says.
- EA, step 1: the base. Fixes 1 to 8, C2 (the adjoint is defined by the chosen generators; in indefinite signature it
  depends on the split into generators of square 1 and -1, so observables, states and (P) are relative to that split;
  the 17/8 element is a unit vector of a boosted frame), C3 (pin tower.commuting-copies@5 where only the twist is used
  and write the pair state out; do not say the completion postulate is unused), C5, C6; receive the blade lemma
  (C^2 = 4 + 4K, KC = C, C^3 = 8C, the states <(1+K)(1+rC).>_0 for 8r^2 <= 1) and "anticommutation only on the state"
  with the three-mode example from the siblings (read their proofs in proposals/ and restate in place, with checks);
  prove in place that a functional violating (P) reaches 4. Report the final clause labels so the siblings can cite.
- EA, step 2 (after the base is accepted): the rationals proposal (fixes 1 to 8: "records" defined or dropped, since
  280/99 beats 82/29 at a smaller denominator than 169; (x, z) for directions, (c_u, s_u) for the rotor, (c, s) only
  for stored amplitudes; "at these settings") and the three-party proposal (fixes 1 to 8: the same-settings condition
  at every level; the 14/5 state written out; the vacuous check loop replaced; the horizon remark labelled a remark
  resting on the stored pair-state reading and empty under parity superselection).
- EB (after the base is accepted): signatures (fixes 1 to 7: the list worded correctly; the Cl(1,3) sentences say the
  result concerns two commuting pairs inside ONE copy with real or rational coefficients and nothing against Bell
  violation for two systems; scope in the title), parity (fixes 1 to 6: notation; the Dasenbrook citation reworded, it
  states no no-go; one numerical example), positivity (OVERSTATED at one-liner and technical: restate there as the
  referee words it: negative on (C-t)^2 for a range of t and on other elements combining different setting pairs,
  never inside one setting pair; "follows from positivity on" in place of "needs positivity on exactly"; the inertia
  (12, 4, 0); clause (iii) moves to the base).
Fixers run only runcheck. Write findings/fixes-<name>.md ending "check4: pending (orchestrator)".
- From verify/R2.md (Kerr; both SOUND WITH FIXES, with titles, one-liners and lay levels OVERSTATED as filed). Ids are
  kept for now (Leon is asked about renaming; if he agrees the orchestrator renames at acceptance): fix titles (at
  most 90 characters), one-liners and lay levels so the scope and the tautology lead. Leon's decision 3: (SH) is recorded
  as a hypothesis, identified with the stored horizon placement, not adopted; (C1) unchanged.
  - KB first: synthesis.no-spin-independent-curvature-level-set-carries-the-count-to-slow-kerr, fixes 1 to 10: scope
    (modulus level sets, rho <= M/3, 0 < a <= 4 rho/5, exact equality; the untreated window; "for a/rho -> 0 the count
    still agrees with A_+/4 at leading order") at title, one-liner and lay; the determinant lemma stated ONCE for a
    general Killing-invariant surface r = R(u) and proved in the Kerr-Schild gauge alone (cofactor rule, det g =
    -Sigma^2 by the rank-one rule, g^rr = Delta/Sigma, g^uu = (1-u^2)/Sigma, g^ru = 0), replacing the Boyer-Lindquist
    paragraph; both halves of the bound; one GA.py point in the store's product in the check, the unused premise
    removed. Report the clause label of the determinant lemma so the sibling can cite it.
  - KA after KB's is accepted: synthesis.stretched-horizon-count-on-kerr-gives-the-area-law-at-every-spin, fixes 1 to
    13: title, one-liner and lay lead with the cancellation (the count is a fixed multiple of the area for every spin
    because the surface gravity cancels; the Kerr entropy is no test of the density); (SH) is the three-volume form of
    the unadopted hypothesis (H), identified with (not added to) the stored placements, citing
    synthesis.c-loc-is-a-second-placement-of-the-count at its current version; only the product nu rho_0 enters and
    rho_0 = 2 is set by the Schwarzschild area law; the remainder c(a/M) rho_0^2/M^2 with c(0) = 1/12; the inner-locus
    sentence restricted (not uniform as a -> 0; needs rho_0^2 M << r_-^3; the rate tends to 12 pi M rho_0, three times
    kappa_+ rho_0 A_+, labelled computed); attribution of kappa_-, A_- and Smarr corrected; the signature sentence; the
    check ties Omega_H to the generator (null at Omega_H, not at -Omega_H) and carries one GA.py point in the store's
    product; prior art Lee and Kim hep-th/9603055 added, so area proportionality is not claimed as new; cite the
    sibling's determinant lemma at version 1.
