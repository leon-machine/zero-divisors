# Fixes, filer U: synthesis.kernel-bivector-is-the-unit-of-hermitian-boson-fields-on-the-tower

Verdict (verify/S.md, P1): SOUND WITH FIXES. All six fixes applied in place in proposals/<id>/; the overlap
ruling applied. No statement changed; no rebuttal.

1. Extraction: "so that this result does not hold given (N+)" -> "so that this result does not rest on (N+)".
2. One-liner: after "the commutant of the $N$ hyperbolic planes" inserted "(the radial plane $(e_{0}, e_{1})$
   counted as mode $0$; with it in the ground, $I_{4}$ also serves)".
3. Lay: "It is the only such element of the right type" -> "Counting the time-radial plane among the planes, it
   is the only such element of the right type (if that plane is left out, the field theory's own unit also works)".
4. Technical: "the datum Premise (N+) assumes" -> "which we read (argued, not proved) as the datum Premise (N+)
   assumes". Lay: "it is the same choice that the series' premise ... makes" -> "it can be read, as an argument
   rather than a proof, as the same choice that the series' premise ... makes".
5. Extraction "New here" -> "New to the store (not new mathematics)": (i), (iii), (iv) and the Lemma are standard
   Clifford and CCR algebra (centre of the even subalgebra of an even-dimensional Clifford algebra;
   Mat_{2^N}(H) = Cl(0,2) (x) Mat_{2^N}(R) has commutant H of the factor Mat_{2^N}(R); a complex structure
   commuting with a family of canonical pairs), new to the store only in this tower reading.
6. Formal (v) Lemma, last sentence: "and $u$ any unit commuting with the band modes there" -> "for any unit $u$ of
   that representation commuting with the band modes; such a $u$ is not exhibited here (the one-particle unit
   there is $I_{4}$ on $\mathfrak{h}$, not an element of the CAR algebra)".

Overlap ruling (mode-rotation formula held by ladder-bosons (i)):
- Formal (vi): U_theta is now named as the diagonal mode rotation with weights s_{2k} = 1/2, s_{2k+1} = -1/2 of the
  sibling proposal synthesis.ladder-bosons-inherit-spin-statistics-from-the-single-modes (i), cited in plain text
  (not yet in the store, so not a claimref and not in `uses`), for the product form, unitarity and action on modes.
- Proof (vi): the derivation of the product formula and of unitarity is removed and replaced by that citation; only
  the consequence U S U* = e^{theta J} S (from the cited action on v_j, w_j) and the turn of (phi, pi) are proved here.
- Extraction: records the same citation.
- Check unchanged: it still computes U, its unitarity and its action exactly, as verification of the instance.

Gates: runcheck 7/7 PASS. Style scan clean (no em or en dashes, no banned words, no \mathbb{C}).
check4: pending (orchestrator). validate_draft: pending (orchestrator).
