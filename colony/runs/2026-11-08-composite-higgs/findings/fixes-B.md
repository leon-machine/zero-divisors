# Fixes B (fix round after referee H)

Both proposals were rated SOUND WITH FIXES. Every required fix is applied in place. Each proposal was then put
through the gate again (runcheck, check4, validate_one) and re-registered: the old folder was moved aside, the stored
files are byte-identical to the validated ones, and coverage.yaml was copied back. Gate processes were run one at a
time.

## synthesis.uniform-pair-channel-of-a-tower-condensate-is-a-goldstone-rotor
- Title: "Finite Goldstone bound: a pairing-type condensate's uniform pair channel is a rotor". The referee's wording
  ("Finite Goldstone bound: for pairing-type elements the uniform pair channel of a condensate is a rotor") is 101
  characters, over the 90-character limit (E124). This shorter title keeps the same scope.
- Technical level: now opens "For pairing-type elements, whose pair commutator [X, X*] is a function of the charges".
  It adds "The doublet floor and coupled condensates, where [X, X*] is not a function of the charges, are not covered",
  and scopes the reading to pairing-type elements.
- Lay level: states that the result does not cover a doublet of paired fermions on one stack or two coupled
  condensates. The composite-Higgs sentence is now marked "As a reading (argued, on this model)".
- Formal and proof reading, and the lay level: "or a non-uniform mode" is replaced by "or a mode outside the
  condensate's pair channel (such as a particle-number-conserving hopping doublet)".
- (iv)(c): the range is now n in {0, ..., floor(n_b/2)} (so that K >= 0), in both the formal statement and the proof.
  The K < 0 case is not claimed.
- Proof (iv): the line now reads "gamma <= (n_b + 1)/2 <= n_b - 1/2", so a minimiser n* <= n_b - 1 can always be
  chosen. The tie at n_b = 2, K = 0 (E(1) = E(2)) is noted as the degenerate coupling n = 1 of (c). The formal
  statement now says "an integer nearest gamma".
- Note:
  - Pairing rotations are cited as prior art (Bes and Broglia, Nucl. Phys. 80 (1966) 289; Bohr and Mottelson,
    Nuclear Structure II).
  - The fact that "P + P* stays on the band" is credited to stored tower-pairing-gap (ii) and taken out of "New here".
    What remains new there is the explicit quasi-spin norms of the two neighbouring components.
  - "The finite Goldstone theorem" is now "a finite Goldstone (rotor) bound, a gaplessness statement only where G
    times the step of c tends to 0".
- Premises: tower.structure-tower-c-norms@10 is added to uses, cited in the formal statement and the proof for
  v* = w, and touched by premise() in check_no_order_parameter_in_a_sector.
- One-liner: scoped to "a pairing-type tower element ([X, X*] a function of the charges)".
- Gate: runcheck 4/4 pass; check4 exit 0, 0 errors, 0 other findings (no W413); validate_one ok with no codes (I305
  info only); re-registered.

## synthesis.even-composite-doublet-needs-a-singlet-constituent-and-its-pair-modes-are-quasi-spins
- The M^2 = 0 hypothesis is restored above the formal level, with the wording "when M^2 = 0 (for example a single
  doublet-singlet hopping, or nonzero hypercharge with all doublet channels of one hypercharge)":
  - One-liner, technical level and note now carry it.
  - "Charged, nilpotent, never normal, never a canonical boson" is kept without the hypothesis.
  - The note records the referee's counterexample: M = E_{up,s} + E_{s,down} has M^2 = E_{up,down} and norms
    1, 2, 6, 18 at q = 1.
- Labelling: clause (ii) is presented as a corollary of synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins
  (iii), (iv), read with isospin weights, at the one-liner and technical levels (claimref at the technical level).
  The title is unchanged: adding "(corollary)" would exceed 90 characters.
- Lay level: "is never an exact boson because it carries charge, and for the simplest such pair it behaves like a finite bank
  of two-state switches".
- Premises: tower.structure-tower-c-norms@10 is added to uses, cited for v* = w in the formal statement and the proof,
  and touched by premise() in check_doublets_are_odd_in_the_doublet_modes.
- Check: check_charged_pair_modes_are_quasi_spins now also asserts the counterexample exactly. M2 has T_3 weight 1/2,
  M2^2 = E_{up,down}, and the norms at q = 1 are 1, 2, 6, 18. This matches the referee's m2.py. coverage.yaml is
  updated.
- Gate: runcheck 3/3 pass; check4 exit 0, 0 errors, 0 other findings (no W413); validate_one ok with no codes (I305
  info only); re-registered.

## Not applied, with reason
- Both title changes are shortened from the referee's wording to stay within E124. The scope is unchanged.
