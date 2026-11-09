# Fixes C3A: synthesis.one-window-parity-recurrence-of-the-light-ray-sea-needs-twenty-four-arrays (R2 section 1, SOUND WITH FIXES)

All edits in place in proposals/<id>/ (entity.md, proof-main.tex, check.py, coverage.yaml; every stored file kept;
the work/C3A copy is synced). Title unchanged.

1. "Stored premises leave it open": I took the proof route (bridge lead L3), not only the weaker wording.
   - The one-liner now says "not implied by (Q), the KMS condition, (N+) or the window reading", and "independent of the cone's postulates (two models)".
   - New clause (v), "Two models of the cone", in the formal, technical and proof sections. M_1 and M_3 have one and three separate generations, n_x = 0. The slot-module premise and anomaly freedom hold for any number of copies, by synthesis.slot-module-makes-the-faces-separate-composites-and-leaves-the-generation-number-free@2 (3), which is now in `uses`.
   - The proof audits every other postulate in R2's cone list, with ids and versions: (P), (Q), (R), (R_Lambda), (N+), the window reading, J3, Krein, rung-unit, indifference, P2, P3, R1-R3, H1 and the four foundation postulates. Each is stated per mode, array, generator, channel, composite, field or tower. None names a count of generations or of arrays (searched: "generation" occurs only in the slot-module hypothesis, of one composite, and in a list of uses in the Krein premise). The face-identification hypothesis is not in the cone.
   - Caveat stated in the proof: whether the indifference premise forbids choosing a generation number at all is left open. The audit is of wording, not a computation.
   - The conditions differ: U = e^{4 pi J/3} Gamma, which is not +-Gamma, in M_1; U = Gamma in M_3.
   - New check function check_two_models_of_the_cone_differ_on_the_condition computes the M_1 phase exactly as -1/2 - (sqrt3/2) J, its order 3, and the M_3 phase 1.
2. J3. New paragraph "Relative to J3" in (iv) of the formal and the proof. J3 is in the cone through null-ordering and the collapse result. It reads integer-weight channels as currents of the arrays, so under J3 they add nothing to n, and (i)-(iii) are the whole count. (iv) is now titled "a reading outside J3" and is stated as outside J3 and outside the CAR scope of (N+) and the window reading. The closing paragraph, the "Not decided" list, the lay text, the one-liner and the extraction note now say the same.
3. Assumes edges: not added (FIXROUND override 2). The extraction note has "Premises used, assumes edge for the maintainer: singularity.q-joint-quasi-freeness-s-wave@3 and synthesis.window-reading-array-killing-energy@1". At present they reach the claim through the null-ordering and counted-unit results.
4. Sign of Gamma: Gamma is now normalised by Gamma = +1 on the sea, stated in (ii) of the formal and in the proof. U = +-Gamma iff 12 | n, which on 16 n_g is again 3 | n_g. A check line was added to the joint-flow function: phase +-1 exactly at multiples of 12 for n <= 96.
5. Finite windows: the formal (ii), the proof and the extraction note now say that (i) is exact on finite windows, and that the constant of (ii) is the band value fixed by the window reading, not a finite-window sum.
6. Prior art (extraction note rewritten):
   - Wang arXiv:2312.14928 is now described with c = 1/2 per Weyl fermion, so c_- = 8 per family and 8 n_g = 0 mod 24. Its conclusion 3 | n_g agrees with (iii); its fifteen-component case (45/2) does not match (8 | n_g here).
   - Added Garcia-Etxebarria and Montero's baryon-triality Z9 anomaly ("only cancels if the number of generations is a multiple of 3"; the abstract was checked on the web), with JHEP 08 (2019) 003.
   - The Wan-Wang-Yau sentence is reworded to its abstract: (B+L)-gauge-gravitational anomaly cancelled by a Z3 TQFT, with N = N_c = N_f = 3 the minimal solution (abstract read only).
   - "The arithmetic 16 n_g = 0 mod 24 is prior art" is replaced by "the conclusion 3 | n_g is prior art by two routes".
7. The GA.check label of check_integer_weight_content_on_the_light_ray now says what the function asserts: "equal to -1/12 only at delta = 0; with c_B real components and 16 n_g arrays, U = Gamma iff 8 | c_B and n_g = c_B/8 mod 3".

runcheck (PYTHONDONTWRITEBYTECODE=1 python3 colony/runcheck.py proposals/<id>/check.py): all 5 functions PASS.
check4: pending (orchestrator). I did not run check4 or validate_draft. The new function's literals (16, 1, 3, the explicit phase) are each sensitive to perturbation by construction, but the mutation test is the orchestrator's.
