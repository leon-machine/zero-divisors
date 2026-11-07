# Consistency pass R01: thermality, first half (133 entities)

Read in full: all 133 ids of read_R01.txt (front matter with derivations, pins and extraction notes;
formal, technical, lay and one-liner levels; every proof file), in dependency order. Background read:
colony/BRIEF.md, store/conventions.md (whole), the GA_REWRITE and SWEEP briefs, the GTG dictionary
conventions section. Exact computations in scratch (lib/GA.py, Fractions):
/tmp/claude-0/-home-claude/23cbb9be-73ca-5537-8211-47496476158a/scratchpad/r01/verify/boost_sign.py (8 checks, pass) and
/tmp/claude-0/-home-claude/23cbb9be-73ca-5537-8211-47496476158a/scratchpad/r01/verify/planck_offset.py (12 checks, pass).
tp check (layers 1-3, one run): no error or warning on any R01 entity (only the pre-existing I213 notes).

## Fixed

- hawking.imported-penrose-transform 2 -> 3: complexified Minkowski space was complexified with I_4
  (u + I_4 w is a vector plus a trivector; Q of it is not a number); by U3 it is the central unit
  I_5 = I_4 e of Cl(2,3), and the levels now say the twistor region is complex over I_6, not identified.
- state-selection.where-fermi-dirac-comes 5 -> 6: "R_2pi = -1 acts as +1 on A_ev and -1 on A_od" named
  no action; conjugation by -1 is trivial on both sectors (euclidean-partner (2), euclidean-rotor (2)),
  so read as conjugation it contradicted them. Formal, technical and proof now say: applied factor by
  factor to ladder words (the action check_even_sector_periodic_odd_sector_antiperiodic tests), it is the
  grading automorphism. Wording only.
- note.decisions.two-boost-flows 3 -> 4: parenthetical said euclidean-rotor (3) keeps its source's formal
  unit; that clause is now written with I_5 (generator I_5 sigma = e_2 e_3 e outside Cl(1,3)).
- note.angle.setting-machine-verification 1 -> 2: two bare units the detector misses, "(iB)~(iB) = 1" and
  "the endpoint iB", written I_5 B (as in angle.wedge-reflection-translations-are-ascent (ii)).
- synthesis.array-ln2-is-zero-mode-doublet-one-tower (no bump; title, one-liner, lay, extraction): they
  said "Under (Q)", but the doublet exists only at (Q) version 2 (weights kappa k); at the pinned
  version 3 (kappa(k + 1/2)) there is none. Now "(Q) version 2"; formal/technical listed below.

Dependants now behind a pin (repin is Leon's): hawking.homogeneity-ordering-shift,
hawking.helicity-lift-joints-itemised, scrambling.imported-collars-coframe-exceptional-set-helicity,
standard-model.imported-twistor-charge-helicity (all @2 on the Penrose Fact);
synthesis.half-integer-weight-array-carries-half-ln2 (@5 on where-fermi-dirac).

## For Leon

1. synthesis.boost-evolution-on-generators-is-one-unitary-group (known open item, settled). The field
   formula of (ii), alpha_l(psi_m(u)) = e^{-l/2} psi_m(e^{-l} u) (verified: B k B~ = e^l k, B~ k B = e^{-l} k,
   B Lambda(m) = e^{-l/2} Lambda(m)), with the proof's antilinear smearing a(f) = int conj(f) psi_m du,
   gives alpha_l(a(f)) = a(D_{-l} f), not a(D_l f) as (ii) displays (exact log-lattice model in
   boost_sign.py). Then a(f_w) -> e^{-I_4 w l} a(f_w): clause (iii)'s phase and its one-particle
   Hamiltonian +kappa w are right (and match obj.hawking.continuum-mode-space, tau_t(a(f)) = a(e^{I_4 t h} f)).
   The proof of (iii) reaches it by pulling e^{-I_4 w l} out of the antilinear a without conjugation:
   two compensating slips. With a(D_l f) as displayed the Hamiltonian would be -kappa w.
   Proposed fix (formal (ii), proof (ii), (iii)): "alpha_l(a(f)) = a(D_{-l} f), (D_l f)(u) = e^{-l/2} f(e^{-l} u)
   ... it is the dilation of Proposition synthesis.affine-cell-boost-spreads-without-scrambling with the time
   parameter reversed"; proof (iii): "a(D_{-l} f_w) = a(e^{I_4 w l} f_w) = e^{-I_4 w l} a(f_w), a being antilinear".
   (v) and (vi) are unaffected (they hold for all real l).
2. Premise (Q) offset, stale displays (Leon's 23 October decision kept them as "note only"; the formal
   levels do not say so). Each states kappa k (Q version 2) while (Q)@3 says kappa(k + 1/2):
   - angle.imported-singularity-papers-state-selection: formal and proof "the s-wave array ... has weights
     kappa k with its sea level at k = 0 (by q-joint)", assumes Q@3; technical says "the convention of
     premise (Q)", false at v3. Fix: "(the source paper's convention, version 2 of premise (Q); version 3
     adopts kappa(k + 1/2))" in formal, technical and proof.
   - singularity.bosonisation-bridge-s-wave-sector: (2), (3), technical and proof call kappa k "(Q)'s weight
     clause". Fix: "(Q)'s weight clause, affine in k (kappa k at version 2, kappa(k + 1/2) at version 3)";
     the Planck value m/(e^{beta kappa m} - 1) holds at both offsets (planck_offset.py: detailed balance and
     window sums exact at both).
   - synthesis.array-ln2-is-zero-mode-doublet-one-tower: formal "Assume (Q) ... weights kappa k" and
     technical "With the (Q) weights": add "in its version 2".
   - synthesis.boundary-mode-premises-finite-models: formal "(Q) is ... with omega_k = kappa k": add "(version 2;
     at version 3 the zero-weight example of (iii) has no analogue on the array, as the extraction note says)".
   - obj.hawking.boundary-mode-algebra-windows-boost-dynamics: "the array's weights kappa k ... the one
     zero-frequency mode": add "(at version 2 of premise (Q); version 3 has no zero-frequency mode)".
   - singularity.universality-temperature-under-g, proof: the k = 0 exclusion "under (Q)'s linear assignment"
     is version 2; add the same label.
   - singularity.q-joint-quasi-freeness-s-wave (postulate): "weights symmetric under k -> -1-k" means
     omega_{-1-k} = -omega_k; worth writing (a bump of a widely pinned postulate, so not done).
3. pairing.two-frames-share-vacuum-selected-transport (ii) cites, in formal and proof, the regular-frame
   classes of pairing.regular-frame-class-vanishes-horizon-changes without a uses edge; that result uses
   this one (a cycle). Proposed: say "computed in the regular frame by pairing.regular-frame-..., which
   builds on (i) here" (mention), as boost-evolution (vi) does for its successor.
4. GA language, not owned by the GA rewriters (not a pure notation change, so not edited):
   singularity.computed (proof in Christoffel components Gamma^r_tt, g^rr; formal also has a dangling
   \ref{app:metric}); synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet (formal
   parenthetical Gamma^r_rr = 0 and proof (ii) in g^{vr}, Gamma; the companion collapse-in-vacuum result
   already does the same parallel transport in GTG and could be cited); synthesis.cosmological-horizon-
   completed-pair (proof step 1 in Riemann, Weyl, Kulkarni-Nomizu components; GA: R(B) = (Lambda/3)B from
   the frozen point); pairing.regular-frame-class-vanishes-horizon-changes and pairing.static-frame-only-
   expansion-survives (connection one-forms omega^a_b, structure equations d theta + omega ^ theta);
   obj.pairing.pairing-class-transport, pairing.pairing-class-transverse-derivative-null-direction,
   note.pairing.setting-transport-moves-vacuum-transverse-derivative ("the Levi-Civita connection nabla",
   forms omega^ab; the bivector Omega(X) is the GTG Omega, same sign); pairing.two-frames-share-vacuum
   (Lorentz matrix, Lambda^T eta Lambda = eta).
5. Notation (minor): synthesis.dirac-causal-propagator-... uses U for the region (formal) and for the
   Hadamard coefficient Delta^{1/2} R (proof); collapse-in-vacuum and its companion collapsing-hole-flux
   use rho and U with different normalisations (rho = r - 2M, U = -rho e^{rho/2M} against rho = r/2M,
   U = -e^{-kappa t}(s - 1)e^{s^2/2 + s}); cosmological-horizon-completed-pair (iii) "up to a phase", a bar on a
   number, with no unit named (the boundary-mode object uses hat-I). Dangling paper \ref{...} remain in
   several formal levels (i-state-continuum, helicity-lift, matching-steps-4b-4c).

## Duplicates

None to merge. Near-duplicate restatements, kept by design: dark-energy.imported-s-wave-current-algebra
and hawking.imported-s-wave-bosonic-sector both restate singularity.bosonisation-bridge-s-wave-sector (the
better statement); their "-external" entities cite Pressley-Segal and Frenkel-Kac for the same
correspondence. Near-duplicate remarks: note.state-selection.dictionary and the second paragraph of
note.singularity.cost-r-dictionary (same dictionary line, T05 and its state-selection note);
note.state-selection.true-price-r and the first paragraph of note.singularity.cost-r-dictionary (the
latter is fuller). Checked and not duplicates: the two rate-discharge theorems (titles distinguished),
the collar trio (three hypotheses, (C), (E), (R_loc)).

## Known open items in these subjects

- boost-evolution one-particle Hamiltonian sign: settled, For Leon 1. The other five listed items are not
  in this half.

## Counts

Read in full 133; changed 5 (4 version bumps, 1 non-substantive); For Leon 5 groups (14 entities);
GA-owned issue file entries 1; cross-subject items 2; tp check runs used 1.
