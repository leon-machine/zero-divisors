# fixes-C4B (fix round, referee R2 sections 6 and 7)

check4: pending (orchestrator). validate_draft: pending (orchestrator). Only runcheck.py was run.

## synthesis.georgi-jarlskog-weight-free-on-the-stored-relations (R2 6, SOUND WITH FIXES)
1. Role of (EW) and (U). Formal: new paragraph after the enumerate. It says (EW) and (U) are not premises: no step
   assumes them, and they are relations the models are shown to satisfy. It says (U) holds in its eigenvalue (top)
   reading, which the stored theorem shows consistent with (EW). It says the stored contradicts link concerns the
   entry reading, and that taking both as premises would carry that link. The technical text and the one-liner now
   say "(U) in its eigenvalue reading". The extraction note calls these relations "audited for invariance (not
   premises)" and gives the E307 reason.
2. Bottom reading. Formal (iv) and the proof now say "fails in both": sigma_1(N) = 1 against m_b/m_t = 5/6. The old
   wording was "does not separate them".
3. Existence of a model. Formal (iv) and the proof say the diagonal model satisfies every postulate:
   - (EW) and (U) top reading;
   - (H), since m_nu = -diag(1/625, 2/125, 0) has a massless lightest neutrino;
   - (M), with v_R = 1000 against doublet vevs of 1;
   - real breaking, since all data are real;
   - the face identification and the indifference premise, which speak of no coupling weight.
   The check gains three GA.checks: m_nu in models A, B and C; M_R = diag(100, 1000, 1000); and the failure of the
   bottom reading in A and C.
4. Duplicate. (ii) now cites standard-model.space-symmetric-doublet-mass-forms-two@5 (added to uses and to
   untouched_premises in coverage.yaml) as the stored span of the 10 and GJ forms with y_e/y_d free. It says what is
   added: the P_4 weight and the Clebsch identification.
5. Completeness. The proof's conclusion no longer claims that every relation is among (iii).
   - It now says the stored theorems (the six R2 found are named) hold in every model of their premises.
   - It lists the cone postulates: (F1)-(F4), slot module, indifference, face identification, (EW), (U), (H), (M),
     the Majorana-scale premise and real breaking.
   - For each, it says whether it names no coupling, or is invariant under h_mu and holds in the diagonal model.
   - The bottom reading on the model's own m_b fails in A and C alike.

runcheck: all 4 functions PASS.

## synthesis.d-term-level-free-at-fixed-n (R2 7, SOUND WITH FIXES)
1. Toy branch.
   - Formal: one sentence after the enumerate. It says the models use W = kappa N^2, whose charged pair the record
     excludes (claimref to the sum-rule result), and that they are models of the premise set and stored relations,
     not of the record.
   - One-liner: the same qualification in brackets.
   - Lay: "Both are consistent" now reads that both satisfy every assumption and stored formula, and that the simple
     potential is ruled out by collider data, which does not matter for this question.
2. Audit, in the proof (iii) and the extraction note. Added: (P), (Q), (R) (singularity.*), (R_Lambda), the Krein
   premise, R1-R3 and H1, reached through the induced-Newton result. P2, P3, sheaf tameness and (C_loc) are listed
   explicitly. None contains xi or a weak-sector scale.
3. Searched relations, in the proof's "what is proved" and the extraction note. Added:
   - synthesis.scale-free-rung-potentials-need-the-flat-physical-branch (cone Q = 0, a different locus, no G);
   - the rung-frame results;
   - the transmutation and quartic-running results;
   - the conjectured readings, by id.

runcheck: both functions PASS (no check change was required).
