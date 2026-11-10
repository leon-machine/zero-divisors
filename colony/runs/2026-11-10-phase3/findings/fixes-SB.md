# fixes-SB: fix round, step 1

Proposal: `synthesis.scalar-sector-at-the-isotropic-scalar-kasner-point-obeys-the-spectator-equation`
(referee R1, verdict SOUND WITH FIXES). All fixes applied in place in proposals/<id>/. No rebuttal.
runcheck: all five functions pass. check4: pending (orchestrator).

## Referee fixes
1. (F1) Formal closing sentence made conditional, in the referee's wording: "So, given the vacuum hypothesis of
   (iv), ... under that hypothesis it is not an artefact of reading a spectator or of the time slicing." The phrase
   "no number is free in it" is gone.
2. (F2) Clause (i) restated in the stored GA form: the equations are R(a) = -8 pi G (a . hat-grad phi) hat-grad phi
   with hat-grad phi = hb^T(grad phi), holding to first order if and only if the three relations hold; the
   components of Ric = -8 pi G dphi dphi on the derived metric are a labelled reading, with each relation tied to
   the vector a and the contraction that gives it. Proof and technical level say the same. No outside_ga
   declaration was added (the restatement route of the fix).
3. (F3) zeta named the comoving curvature perturbation (often written calligraphic R; agrees with the
   uniform-density variable only outside the Hubble length) in (iii), technical, one-liner and proof; added that it
   is not constant outside the Hubble length (order-zero logarithm) in (iii), technical and proof.
4. (F4) Prior art: Brustein, Gasperini, Giovannini, Mukhanov, Veneziano, Phys. Rev. D 51 (1995) 6744 added to the
   extraction note, flagged as from memory and not checked. "A textbook computation placed in the collection's
   setting" added at technical and lay; the note says the result is classical.
5. (F5) Tag `no-go` removed. One-liner now says "with a normalisation free of k".

## Rules of FIXROUND.md
- Tensor modes: the tensor-to-scalar remark (48) is deleted from the extraction note; the comparison with the
  cross modes' index is removed from clause (iv), from the proof of (iv) and from the technical level. No level
  now uses a vacuum for tensor modes. The uses edge to the stored coupled-modes result stays: clause (i) cites its
  component reading and the note cites its "not covered" list.
- Numbers from memory: none at a statement level. The note's flagged references (Bardeen, Mukhanov, Sasaki, the
  pre-big-bang paper, Khoury et al.) carry no number and no significance.
- No new Facts, postulates or assumes edges. The sibling base is still named in the note only (step 2 is the
  base's side).

## Check
- The two arithmetic-identity lines the referee noted are replaced by one line computed from the background
  rates: zeta/u = H tau = 1/3 and the friction of zeta from the pump field, 3 H tau = 1, which fails if the
  exponent is perturbed. It remains a light test; the proof carries the statement.

## Final clause labels (for the base's citation)
(i) lapse and shift are forced, and the reduced equation; (ii) order zero; (iii) the comoving curvature
perturbation, zeta = u/3, pump field z = 3 q a; (iv) index, conditional on the stored adiabatic vacuum with a
normalisation independent of k: local index in [2, 3]. The row for the base: scalar sector at the isotropic point,
(f, kappa, P) = (0, 0, 1/3), order 0 by (ii), index in [2, 3] by (iv) under its vacuum hypothesis.

## Findings file
The remark on tensor ratios in findings/attack-SB.md (R1 remark, R5 item 4) is a prior-art comparison only and is
not in the proposal.

## After the central gate (W215)
validate: W215, the proof never cited synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling
(its only proof citation, the cross-mode sentence of (iv), was removed under the tensor-mode rule). Fix: the premise
is kept in uses and cited by \claimref in the "Setting and signs" paragraph of proof-main.tex, at the step that
uses it: the component reading of the field equations on the derived metric, in which its clause (i) computes the
linearised equation on the same backgrounds. The premise() call and coverage are unchanged. runcheck: five
functions pass. check4 and validate: pending (orchestrator).
