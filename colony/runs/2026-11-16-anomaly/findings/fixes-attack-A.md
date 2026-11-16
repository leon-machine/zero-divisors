# fixes-attack-A: fix round, run 2026-11-16-anomaly

Fixer for three proposals. Every referee point is listed with what was done. Only `runcheck.py` was run.
No rebuttals: every referee point was accepted; the one counterexample (negative delta) was reproduced
(Theta = 83417600/3 at delta_u = -5) and is now in the check.

## 1. synthesis.phase-of-the-quark-mass-determinant-on-the-covariant-completion (R1 no. 2, SOUND WITH FIXES)
- Fix 1 (sign hypothesis; orchestrator's note). FIXED. The quarter-turn clause no longer assumes delta_q > 0.
  Formal (iv) states the hypotheses as hypotheses (one-type symmetric stages; c_q real; delta_q real and nonzero,
  either sign) and the rule true for every sign: Theta = (c_u c_d)^3 (d_u d_d)^2 (t_u t_d)^2 R_u R_d with
  R_q = (p_q - 2r_q)^2 + delta_q p_q^2 real, sigma = sgn(c_u c_d R_u R_d); at the quarter turn Theta has sign
  -sigma. R_q < 0 and R_q = 0 (a massless quark) are named. Proof and one-liner changed to match.
  Check: the rule is computed on delta_u in {1/5, -5, -1/2, -7} and both signs of c_u against the closed form;
  the referee's counterexample is pinned (R_u = -4, Theta = +83417600/3 with c_u c_d > 0); R_u = 0 gives Theta = 0.
- Fix 2 (c_q real is an added hypothesis). FIXED, formal (iv), Reading, technical, one-liner.
- Fix 3 (half turn). FIXED at the formal level, as the orchestrator asked, and in Reading, technical, lay,
  one-liner and note: "real determinant" is two cases of different standing; a half turn conserves the
  conjugation, the stored neutron bound (linear near zero) does not exclude it, its exclusion is unimported
  literature and model-dependent (arXiv:0806.1669, the source the referee checked).
- runcheck: 4 of 4 pass.

## 2. synthesis.conditional-inheritance-of-b-minus-l-and-the-conversion-coefficient-as-a-gram-ratio (R1 no. 3, SOUND WITH FIXES)
- Fix 1 (gravitational channel). FIXED. Clause (i) now gives the right traces: tr(B - L) = 0 on the sixteen and
  -1 per family on the fifteen (the plasma under (R)), likewise the cube; tr Y^2 (B - L) = tr Y (B - L)^2 = 0 on
  both (stated). A new named hypothesis (Gr), not stored: the gravitational four-form's pairing with B - L on the
  fifteen changes B - L by less than the inherited value; what is known of it is labelled argued (the four-form
  vanishes on a homogeneous isotropic background) and literature from memory (gravitational-wave leptogenesis,
  Alexander, Peskin and Sheikh-Jabbari 2006); no rate computed. (Gr) is added to the hypothesis list, to clause
  (iii) and its completeness sentence, to the summary, technical, lay, one-liner and note (now seven hypotheses,
  four not stored). Check: the five traces are computed on the sixteen and the fifteen.
- Fix 2 (doublet count is argued). FIXED: one-liner "N_H = 1 (argued)", lay "argued, not proved, to select",
  technical and summary likewise.
- Fix 3 (broken-phase convention). FIXED in formal (v) and proof: two helicities of the weak boson and the charged
  component of each doublet, the literature's massless convention; the alternative count gives 10/31.
- Fix 4 (Kartavtsev). FIXED in the note: equation (13a) carries a Higgs-mass factor; the form used is its
  massless limit.
- Fix 5 (wording of (iv)). FIXED: "21 numbers: the 16 state charges, the four slot-operator charges and the
  charge of v_4 w_5".
- Vacuous check (referee; orchestrator's note). FIXED. The assertion 18*132 < 2500 < 19*132 is removed. In its
  place the check computes, from the Gram ratio, the coefficient with a second doublet at weight eps
  (c = 28/79 - 48 eps/(79(79 + 13 eps)), three values of eps), an exact upper bound on the weight of a boson of
  mass at least 18 temperatures ((250/81)(1 - 2^-18)^-2 exp(-72/5), derived in the proof by the 3-4-5
  inequality, the exponential bounded by a partial sum), and the resulting shift of c (between 1e-8 and 2e-8).
  The two quoted inputs enter only through their ratio being at least 18. The count stays argued: the inputs are
  a stored bound stated as approximate and a literature temperature.
- runcheck: 7 of 7 pass.

## 3. synthesis.spectral-asymmetry-on-real-projective-five-space-from-monogenic-polynomials (R2 no. 1, SOUND WITH FIXES)
- Fix 1 (named background). FIXED. Formal statement carries "Background (CA)": (CA1) density, (CA2) essential
  self-adjointness of the Dirac operator on a closed manifold, (CA3) the Mellin lemma; clauses say which
  statements are proved given (CA). (Named (CA), not (A), because A is the antipodal lift in the same statement.)
  outside_ga extended to the completeness step of (iii). Proof (iii) now uses (CA2) explicitly. One-liner says
  "given classical analysis named as background".
- Fix 2 ("per Weyl component"). FIXED: "per component of the sixteen (one copy of the five-dimensional spinor
  module)"; the reading as one four-dimensional Weyl field is called the literature's inflow statement, not imported.
- Fix 3 (unit principle). FIXED in formal (iv), technical and proof: J is matched with +I on W_+, a matching on
  this module and not an identification; W_- is the opposite matching with every sign of xi reversed.
- Fix 4 (checks). FIXED. premise("standard-model.hyp-s-slot-statistics") removed from the three mathematical
  checks; it is touched only where the ten generators of Hypothesis (S) are used (omega). New check
  check_spectrum_on_polynomials_of_each_parity computes the sign pattern: for k <= 3 the eigenvalue of D on every
  block x^j M_(k-j) is found by applying D, the values are distinct and the dimensions add up to dim P_k (whole
  spectrum on P_k); for k <= 2 the same spectrum is found again from exact ranks of D - lambda on all of P_k
  (the referee's method; k = 3 by ranks takes about a minute and is left out); the sign of each eigenvalue is
  compared with the parity of the degree, and the signed multiplicities with the partial sums of the series.
  The spinor arithmetic uses sparse matrices so the whole file runs in about 4 seconds.
- Fix 5 (attribution). FIXED in the note: Brackx, Delanghe and Sommen 1982; Delanghe, Sommen and Soucek 1992
  (from memory); Garcia-Etxebarria and Montero, arXiv:1808.00009, section 4.3 and equation (2.14) (their eta is
  this xi; checked at source in review). Technical and lay levels no longer read as new mathematics.
- runcheck: 6 of 6 pass.

## New decisions for Leon created by the fixes
1. Hypothesis (Gr), B - L proposal. With the heavy singlet out of the plasma, B - L has a nonzero gravitational
   pairing (trace -1 per family). Options: leave it a hypothesis of the theorem; add it as a premise; or add a
   channel "gravitational four-form" to the attack list of op.matter-asymmetry-origin. Recommendation: the last.
   Note for that item (argued, not computed): the series holds a CP-odd datum (the flag) and gravity is its
   subject, so a parity-odd curvature background at the descent would be an in-framework source of B - L and would
   bear on the registered premise's refutation condition.
2. Determinant-phase proposal: the quarter-turn reading now carries three explicit hypotheses (one-type symmetric
   stages, c_q real, delta_q real) and a sign sigma that nothing stored fixes. If you record the reading as a
   conjecture, record these with it. Whether to import the status of a half-turn angle (arXiv:0806.1669 and the
   hadron-spectrum literature) is yours; nothing is imported.
3. Spectral-asymmetry proposal: the background (CA) is named and not imported. Import its three items as Facts,
   or keep it as a named background in the manner of the stored lens-space theorem.

check4: pending (orchestrator)
