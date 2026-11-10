# Fixes B, run 2026-11-09-three

Proposal: synthesis.capacity-and-sakharov-readings-leave-the-generation-number-free (referee R1, SOUND WITH FIXES).
All edits in place in proposals/<id>/ (entity.md, proof-main.tex, check.py, coverage.yaml); id unchanged; no rebuttals.

- C1 APPLIED. Formal (i): the false sentence ("all of helicity 0") is replaced by the referee's wording (at most n
  members over span{1, J} for normal families with [M, M'^*] = 0; a member with a definite helicity has helicity 0;
  the diagonal units attain n), with the referee's counterexample E+- + E-+ stated. Proof: criterion now cited to
  clause (ii) of the quasi-spin theorem; the finite-dimensional Fuglede step is given in two lines (a normal matrix
  is a polynomial in its adjoint); the "definite helicity implies helicity 0" step and the counterexample are added.
  Check docstring corrected, and the counterexample is now checked exactly (normal, weight commutator E+- - E-+, not
  a multiple of it). Coverage updated.
- C2 APPLIED (restricted and labelled, no 24-postulate audit, as the fix round directs). Proof paragraph headed
  "Independence (argued)"; last sentence replaced by the referee's; "No stored premise requires the zero" is now
  "None of the cited results requires the zero (argued)". Formal reading, technical, lay and extraction note say
  "the stored results cited" and that the remaining premises were not audited.
- C3 APPLIED. One-liner ends "neither rule is required by the stored results cited (argued)"; title is now
  "Capacity and induced-gravity readings do not fix the generation number" (id kept).
- C4 APPLIED. Formal setting and proof (iii): the graviton sentence now reads: no stored graviton field or dynamics;
  it occurs in J1 (kinematics) and in J3's channel-reduction clause (premise for spin 2), so eps = 1 is the reading
  of J3's species list. Reading and proof (iii): the qualification with synthesis.array-ln2-is-zero-mode-doublet-one-tower
  (iv) is added as the referee words it (the store has the upper bound per array; J3 read injectively with (iv) is
  the capacity inequality with eps = 1; no stored text states injectivity; either way a lower bound, and by (i) not
  exact for helicity +-1, +-2). The sibling horizon-channels result is named in the extraction note as the intended
  citation for the maintainer (a proposal cannot cite a proposal, E201); J3 itself is not added to assumes
  (maintainer-only) and is reached through hawking.helicity-lift-joints-itemised@6, already in uses.
- C5 APPLIED. Clause (i) is labelled a corollary of clauses (ii) and (iii) of the quasi-spin theorem, with the new
  parts named (no helicity +-2 from weights +-1/2; the bound n).
- C6 APPLIED. Check label reworded ("-3 minimal-scalar units", no mixed units). Extraction note states that status
  proved covers clauses (i) to (v) and that the tag no-go is meant in that sense only.
- Defect 6 (optional) APPLIED: the proof now says the zero in xi_R exists for every n_g (B linear with nonzero slope).

For the maintainer / Leon (from the referee, unchanged by the fixes): whether J3's identification is meant
injectively; whether xi_R and the gauge parameter stay open data; no-go or record of variants.

runcheck: 4/4 PASS after the edits. House-style scan of the folder: clean.
check4: pending (orchestrator)
