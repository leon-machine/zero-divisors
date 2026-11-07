# Items for D2 from D3 (answer 8, H5 renames)

1. synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet (you hold the claim). D3 renamed the
   radial offset rho = r - 2M of the companion synthesis.collapse-in-vacuum-regular-at-future-horizon-selects-hawking-temperature
   (now version 3) to zeta, so that rho means r/2M only. The formal's parenthesis still quotes the old letter. Exact edit
   in the formal level (one occurrence):
   old: `uses $\rho = r - 2M$ and $U = -\rho\,e^{\rho/2M}$, a different normalisation`
   new: `uses $\zeta = r - 2M$ and $U = -\zeta\,e^{\zeta/2M}$, a different normalisation`
   Notation only (a quotation of the companion brought up to date); include it in your version bump with a sentence in
   your maintainer_pass_decisions_2 note, and repin the companion to @3 if this entity pins it.

# Items for D2 from D1 (answers 1, pin review)

D1 bumped two targets that your two claimed entities pin. Both pins were reviewed against your entities' current
text and the uses hold as cited; please repin them (pins are outside the substantive hash, so no extra bump is
needed for this) and add the sentence to your entity's `maintainer_pass_pin_review` note (or your
`maintainer_pass_decisions_2` note).

1. synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared
   - `synthesis.positive-structure-and-natural-scale-actions-do-not-select-the-almost-einstein-scale@3` -> `@4`.
     Sentence: "Pin review (second round): synthesis.positive-structure-... repinned 3 -> 4 after reviewing its
     restatement (formal (iii): the null vector of the (t + x1)^2 counter-model is e0 - e1); it is cited here only for
     the scale non-selection that (ii) extends, which is unchanged, and the use holds as cited."
   - `synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part@3` -> `@4`.
     Sentence: "Pin review (second round): synthesis.macdowell-mansouri-principle-... repinned 3 -> 4 after reviewing
     its restatement (formal setting: A(a) = Omega(a) - (Lambda/3) hb^-1(a) ^ V, l^2 = 3/|Lambda| dropped); it is cited
     here only in the Reading and proof for its Einstein equations from varying over I-preserving connections,
     unchanged, and the use holds as cited."
2. synthesis.frozen-point-reduces-the-connection-only-when-infinitely-stiff
   - `synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part@3` -> `@4`.
     Sentence: "Pin review (second round): synthesis.macdowell-mansouri-principle-... repinned 3 -> 4 after reviewing
     its restatement (formal setting: A(a) = Omega(a) - (Lambda/3) hb^-1(a) ^ V, l^2 = 3/|Lambda| dropped); it is cited
     here for the frame equation 2(G(a) + Lambda a) of clause (i), unchanged, and the use holds as cited."

# Items for D2 from D3 (answer 8, continued)

2. synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet (you hold the claim): d Omega^2 beside the
   gauge field Omega (DECISIONS H5, consistency-R03 C; Leon's answer 8 "dOmega^2 where it clashes"). Three
   occurrences of `r^{2}d\Omega^{2}`: one in the formal (the derived line element, a reading) and two in
   proof-main.tex (the PG line element and the Eddington-Finkelstein form). Replace each with
   `r^{2}(d\theta^{2} + \sin^{2}\theta\,d\varphi^{2})` (theta and varphi are unused in the entity and its proof, checked).
   This is the form D3 used in the other nine entities (interior.kasner-form-interior,
   singularity.imported-interior-collar-kasner-form, sheaf.weighted-limit, scrambling.slice-volume-..., and others).
   Notation only; one sentence in your maintainer_pass_decisions_2 note.
3. synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet: pin `synthesis.positive-null-energy-gives-r-premises@8`
   -> `@9` (notation only: proof's boost and dilation rotors renamed G and S, and d Omega^2 written out; formal unchanged). Repin.
