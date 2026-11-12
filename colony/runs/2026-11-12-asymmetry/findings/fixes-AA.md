# Fixes AA, run 2026-11-12-asymmetry (after referee report verify/R1.md)

Both proposals: SOUND WITH FIXES. Every listed fix applied in place; nothing rebutted. runcheck.py passes on both
(4 of 4 and 5 of 5 functions). check4: pending (orchestrator). validate_draft: pending (orchestrator). No commit.

## synthesis.exchange-of-set-and-clear-is-inner-and-fixed-by-no-integer-state (referee proposal 1)
- founded_on unused: removed the founded_on edge (no step uses it).
- Fix 1 (lay level false: positivity dropped): lay now says no assignment is balanced, and that every assignment
  giving no negative value to the two tests puts each switch definitely on or off.
- Fix 2 (Reading, "every integer state is oriented"): replaced by "no integer state is invariant, every integer
  state positive on the two tests puts each switch definitely on or off".
- Fix 3 and section E (class of states): formal (v) now says the argument uses only additivity, omega(1) = 1 and
  X(n_1) = 1 - n_1, and that a Q-algebra has no integer state at all, so the statement has content only on the
  integer span of the monomials. Proof gives the divisibility argument and the non-positive example (values 2, -1).
- Fix 4 (finite m): formal (i), technical and one-liner say finitely many switches; for infinitely many nothing
  here makes the exchange inner.
- Fix 5 (triviality): technical level and the note say the content is standard and elementary (particle-hole
  exchange by a product of Majorana elements; "1 is odd").
- Fix 6 and section G (do not lean on the defective stored sentence): the last sentence of the Reading no longer
  says the exchange "sees no real form". It now says that in a Witt basis with v_k = +- conjugate of w_k the
  exchange is a real isometry of R^{2,4} of determinant -1 that reverses the frozen point's action (stored
  clauses (3) first sentence and (5)), the preserving realisation being antilinear (clause (4)), and that "label"
  is proved for the algebra and not for the laws.
- Fix 7 (optional check of non-existence): check_integer_states_choose_an_orientation now asserts
  n_1 + X(n_1) = 1 and the parity fact, and exhibits the non-positive integer state 2 st_on - st_off.
  coverage.yaml says plainly that this is the input identity plus arithmetic, not a search over states.
- Title and id still fit.

## synthesis.baryon-number-centraliser-in-the-five-mode-algebra (referee proposal 2)
- Fix 1 (one-liner omitted the six): added "nor the six leptoquark bivectors, which change it by the fixed
  weight -+1/3".
- Fix 2 (lay oversold): rewritten. Names both groups outside (the six, compensable by the carrier; the 24, not),
  and carries the sentence that the anomalous weak process is not in the algebra and does change the baryon count.
- Fix 3 ((vi) wording): formal (vi) says "commutes" throughout and is retitled "The class"; "inheritance" appears
  only in the Reading, marked argued. Its last sentence now also names the six. Technical level likewise.
- Fix 4 ((ii) elementary): said in formal (ii) and the technical level, with the multiplicity count
  8^2 + 12^2 + 12^2 = 352 and 4^2 + 12^2 + 12^2 + 4^2 = 320.
- Fix 5 and section A (overlap): (v) cut to two lines (the five-mode instance of the exchange; only its action on
  the charges, T and the families is kept); (iv) restated as a corollary of (ii). The extraction note
  cross-references both sibling proposals by id and says what each holds. No uses edge added (neither is in the
  store yet). The check function for (v) is unchanged and still tests P, Gamma, chi and su(2)_L; coverage says so.
- Fix 6 (extension to the odd half is a choice): formal (i) now leads with that sentence and states that the
  stored chi form extended verbatim is off by chi/2 on all sixteen odd states; the check computes it.
- Fix 7 (literature from memory): the Reading now names the two sources of the anomalous process in the formal
  level as cited from memory and not a stored Fact.
- "Rung vector" for mode 5: the text says slot vector throughout; for s = 4 these are the stored rung vectors,
  and the second slot plane is included without a stored name.
- Checks tightened: 352 and 320 are compared with the rank of the 16 slot monomials and with the sums of squared
  multiplicities (the multiplicities 1, 3, 3, 1 are pinned literals; coverage says that comparison is arithmetic);
  pair vectors tested against all three charges; (vi) last sentence tested on all six and all 24.
- Title and id still fit.

## Left for the maintainer
- Correction of clause (3), last sentence, of synthesis.cpt-conjugation-pseudoscalar-rotor-times-complex-conjugation
  (referee section G gives the exact text): a maintainer edit, not made here.
- Import as a Fact the anomalous electroweak process (B + L changed, B - L kept); both proposals cite it from memory.
- Once the sibling proposals are accepted, the cross-references in the note of the baryon-number proposal can
  become claimrefs.
- Which operator the stored charge Q = epsilon N is (unchanged from findings/attack-AA.md, decision 1).
