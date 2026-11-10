# Fixes QA, run 2026-11-10-phase3

Proposal: `synthesis.one-loop-self-energy-and-vertex-extend-with-the-ward-identity-holding-at-a-common-cut-off-length`
Referee: verify/R3.md, section 3, verdict SOUND WITH FIXES (clause (vi) and the one-liner overstated on one point).
All nine fixes applied in place in proposals/<id>/ (entity.md, proof-main.tex, check.py, coverage.yaml). Id unchanged.
No rebuttal: the referee is right on every point, including the main one.

runcheck: `PYTHONDONTWRITEBYTECODE=1 python3 colony/runcheck.py proposals/<id>/check.py`: 5 of 5 functions PASS.
check4: pending (orchestrator). validate: pending (orchestrator).

## The overstatement (fix 1), restated at every level
What I had claimed: the stored import of existence (Scharf) "is proved here / is not needed" at one loop for these
two kernels. That is false as stated. The imported clause is about time-ordered products in signature (1,3) at
every order; the pair I exhibit lives on the Euclidean section, the cylinder Q(u + v) < l^2 has no counterpart in
signature (1,3), and the store holds no Wick rotation of a three-point kernel. True statement, now at every level:
on the Euclidean section a pair obeying the identity is exhibited at one loop; the import is supported, not
discharged.
- formal (vi): the referee's sentence, plus "this result does not discharge that import; it supports it at one
  loop on the Euclidean section". The family of Ward-preserving pairs is stated "on the Euclidean section".
- formal (iii): added that the cylinder has no counterpart in signature (1,3) and the statement is Euclidean only.
- one-liner: "so on the Euclidean section a Ward-preserving pair is exhibited at one loop ...; the imported
  existence for the time-ordered products in signature (1,3) is supported, not discharged".
- technical: same, in the second sentence and where the family is stated.
- lay: "in the Euclidean (imaginary-time) form of the theory"; closing sentence now says the statement in real
  time, and higher orders, still rely on the literature.
- extraction note: the paragraph "the import is not needed" replaced by the reason it is not discharged; a flag
  added.
- proof: Step 8 and the status paragraph say the same.

## Other fixes
2. "Derived, not imposed" (fix 2). "nothing is adjusted" (technical), "with nothing adjusted" (lay) and "no
   constant was chosen" (proof Step 5) removed. Formal (iii), technical, lay, one-liner, note and proof now say the
   identity is built in by the choice of the two subtraction regions (cylinder and ball of one length), which in
   terms of the stored constants is the choice c_V = -c_2. Proof Step 5 adds the referee's two reasons (why the
   cylinder: no boundary term in the t integration; why one length: otherwise the shell remains).
3. Scope (fix 3). Title: "One-loop self-energy and vertex on the Euclidean section: Ward-obeying extensions"
   (81 characters; the referee's suggested title is over 90, so shortened with the same scope). Lay: Euclidean
   form, massive case on unchecked standard properties, magnetic moment and on-shell normalisation not treated.
   One-liner: "on-shell conditions and F_2(0) not treated", and the massive condition. Formal (ii) and (iii): the
   referee's parenthesis on the massive propagator added after "for every m >= 0". Technical: F_2(0) and the
   massive condition added.
4. Count across algebras (fix 4). Took the wording option, not the rank recomputation: (vi) is now headed "the
   stored count, carried to the Euclidean section" and says the count is made in Cl(1,3) in the momenta. The
   relation c_V = -c_2 is rederived directly in position space in proof Step 8 (two lines) and tested in the check
   (three coefficient pairs against the linear part of a test polynomial; fails for c_V = c_2). The three ranks are
   NOT recomputed in Cl(4,0); the note and coverage say so.
5. Step 5 (fix 5): the slice identity is now stated as the computation of Step 2 done in t at fixed w, with the two
   singular points distinct, not a restriction of a distribution on R^8.
6. Step 3 (fix 6): the matrix-language aside replaced by "the position-space form of the derivative of the
   propagator along n in momentum".
7. Attribution (fix 7): formal (v) and the note now give Haagensen and Latorre 1993 as quoted in eq. (36) of
   arXiv:hep-th/9709067 (checked); Freedman, Johnson and Latorre is marked from memory and not supported by the
   checked source; the flag that the vertex scale's identity with theirs is not shown is kept.
8. Krein-form premise (fix 8, FIXROUND rule 2): no edge added. The note now has "premises used, assumes edge for
   the maintainer: synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields", with the referee's
   distinction (the kernel identity needs no premise; its reading as electrodynamics does).
9. Fix 9: nothing to do beyond fix 1.

## Check changes
- Removed the two vacuous lines the referee named: the degree arithmetic `(3 + 2 - 4, 3 + 3 + 2 - 8) == (1, 0)`
  (with the companion `3 + 3 > 4`) and `const - const == 0 and const != 0`. The degrees are now listed in
  coverage as the proof's and the stored theorem's, not checked.
- Replaced the second by a computed test: F(w) = f(w, 0) - f(0, w) built from the test polynomial, F(0) = 0 with
  f(0) not zero, and its second-order part not zero.
- Added the c_V = -c_2 test of fix 4.
- coverage.yaml updated to match (clauses and omits).

## Not changed
- Clauses (i) to (v), all constants, Steps 1, 2, 4, 6, 7 of the proof: the referee recomputed them and they stand.
- No sibling citation is involved; nothing for step 2 of the fix round.

## For the maintainer
- The referee notes this result could equally be a new clause of the stored regulator-free theorem.
- If accepted, the stored theorem's flag on imported existence should NOT be lifted (my earlier "Decisions for
  Leon" item 2 in attack-QA.md said it could be noted as proved at one loop: that recommendation is withdrawn; the
  right note is "supported on the Euclidean section at one loop").
