# fixes-WA: fix round, step 1 (referee R3). Run 2026-11-10-phase2

check4: pending (orchestrator). validate: pending (orchestrator). Only runcheck was run: base 5/5 pass, twist 4/4 pass.
No rebuttals: every R3 finding on the two proposals is accepted. Sibling references are NOT yet citations (step 2).

## 1. synthesis.antiperiodic-array-against-the-light-ray-continuum-at-window-length-r (base; SOUND WITH FIXES)
1. False closing sentence on the variance: replaced at the formal level ("ln Z and the entropy differ at every finite
   length; the variance exceeds the continuum's for r >= 1 and equals it at one shorter length found, r about 0.625");
   clause (iv) now states the sign change with a certified bracket r* in (1/2, 5/8) (new check lines:
   v(1/2) - pi/12 in (-0.1150, -0.1148), v(5/8) - 5 pi/48 > 0); technical and one-liner say so; lay scoped "at one
   thermal cycle and beyond". Uniqueness of the zero is not proved and the proof says so (the referee's 0.624869 is
   quoted as a floating value only).
2. Invalid "only if" in (v): removed; replaced by the referee's true statement (the deficit is the 1/rho-weighted
   integral of the energy difference and is nonzero; equal energies at one temperature give no equality of
   entropies); the inference about counting stays labelled argued, in statement and proof.
3. synthesis.de-sitter-mode-count@3 added to uses, cited in (v) and its proof with "scales as N^2 whatever the
   residue ... a change of coefficient only"; premise() call added in the residue check.
4. synthesis.q-splits-maximum-entropy-affine-weights@6 (iv) added to uses, cited where r is introduced (formal and
   proof); premise() call added (variance check).
5. "Nothing here assumes ..." relabelled argued, clause level, with the cone's content named, in the extraction note
   and the proof's Status; continuum values "defined with the state that (N+) selects".
6. One-liner and technical: "two are that one identity and the third is r = 1/r".
7. Fixed-spacing sentence: "comparison family, not a state selected by (N+)" added (formal and proof).
8. Symbol clash: remainder renamed epsilon(r); Clausius integration variable is varrho.
9. Check: `assert r <= 8` guard in array().
10. Status by clause recorded in the formal closing sentence, the extraction note and the proof: (i) to (iv) proved
    given the imported Fact; (v) computed; its last sentence argued. The status field stays "proved".
Also: the Ramanujan attribution is marked unconfirmed in the note. Clause (v) stays counterfactual at every level
(unchanged wording) and names its unit (per unit of two components; 3/(2 pi) per component).
FINAL CLAUSE LABELS (base): (i) proved given the imported theta identities; (ii) proved given the identities;
(iii) proved given the identities (values certified); (iv) proved given the identities (values certified; the
crossing in (1/2, 5/8) certified by bracket, its uniqueness not proved); (v) computed, counterfactual, last sentence
argued; independence from (Q), (N+), the window reading: argued.

## 2. synthesis.light-ray-continuum-is-the-twist-integral-of-arrays-and-window-values-are-twist-averages (OVERSTATED -> restated)
1. "Not a subsystem" restated at every level (formal (i), closing paragraph, technical, lay, one-liner, extraction
   note) to: not a Killing-invariant subsystem; non-invariant subalgebras can carry the same occupations for any twist
   and select none. The referee's counter-construction is in the statement of (i) and proved in the proof.
2. Ordering and failing arrays: title now "... boost-ordered values are averages" (90 characters; the id is
   unchanged); heading of (iv), technical, one-liner and lay carry "boost ordering; the null-ordered sea value is not
   a twist average; at r = 1 every averaged array except twist 1/2 fails the stored energy equalities"; the formal
   level adds that at r = 1/2 the fibres 1/4, 3/4 pass (a null set).
3. Lay: "entropy per unit time, multiplied by the length of the stretch".
4. Restriction content labelled argued at technical, lay and in the formal closing paragraph.
5. Extremality: every level now says the two end values and "every value between is taken"; "extremes not proved".
6. Duplication of the base: NOT done (step 2). To do then: cite the base for the dual forms and Delta(M), delete the
   repeated derivation in (iv), and drop "given the imported theta identities" for the density integrals.
7. synthesis.q-splits-maximum-entropy-affine-weights@6 (iv) added to uses and cited in (ii) (statement and proof);
   premise() call added.
8. "Nothing here assumes ..." relabelled argued, clause level (note and Status).
9. GA.check labels corrected to (i),(iii) / (iii) / (iv) / (v); `assert r <= 8` guard in half().
10. Sea additivity stated for every twist, with proof line and three exact check cases.
11. Orientation fixed: (ii) states phi(L) = e^{-2 pi I_4 delta} phi(0) with eigenfunctions e^{-I_4 varpi tau}; the
    hedging sentence in the proof is removed.
Final labels (twist): (i) proved (including the non-invariant counter-construction); (ii) classical, boundary form
computed; (iii) proved; (iv) identity proved, values given the imported identities, boost ordering; (v) certified
bounds, intermediate values by continuity, extremality not proved; Remark argued.

## For the orchestrator
- Both proposals gained a uses edge (base: de-sitter-mode-count@3, q-splits@6; twist: q-splits@6), each touched by a
  premise() call. The twist title is exactly 90 characters.
- Maintainer note relayed from R3 (outside these proposals): the window reading's "What it is for (i)" and refutation
  condition (b) should carry "at spacing kappa" if the sibling free-spacing result is accepted.
