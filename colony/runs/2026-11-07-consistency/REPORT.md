# Run 2026-11-07-consistency: the whole series checked for consistency, results and proofs in GA

Leon (7 November 2026, 13:11): "Can you check the whole series for consistency and ensure results/proofs are in
GA where possible". He chose a full read by subject and a rewrite of every entity still written outside GA, and
on the reconciled findings chose the recommended answer to each of the eight decisions (DECISIONS.md, end).

## What was done

1. **Full read by subject (readers R01-R12; CONSISTENCY.md).** About 2,270 entities read in full: formal,
   technical, lay and one-liner levels, every proof file, uses, assumes, pins and extraction notes. About 190
   were fixed in place (wording, citations, notation, stale plain levels, sign or constant slips in proofs where
   the formal statement was right, each recorded with its computation). Reports: consistency-R*.md, xsubject-R*.md.
2. **The six known open items, all settled.** quadratic-flows phase (formal (ii) wrong, corrected under A1);
   boost-evolution (two slips that cancel, corrected under A2); real-structure (ii) (fixed); hadamard-dirac step 7
   (-eps^2/2 and the I4 sign); the sign of I6 on CS (orientation-dependent: I6 = I4E acts on CS as +I7 in the
   entity's own frame, script work-R10/i6_attachment_frame.py); the operator-join unit sentence.
3. **GA rewrite (GA_REWRITE.md, GA_ROUND2.md).** Tensor, forms and matrix stand-ins rewritten in GA: gravity in
   Gauge Theory Gravity on flat spacetime (hb, Omega, R(a ^ b) in the store sign), forms as multivector fields,
   matrices as Clifford elements; reports ga-tensor.md, ga-forms.md, ga-matrices.md, ga2-gravity.md,
   ga2-matrices.md.
4. **Decisions applied (APPLY.md; apply-AP1.md, apply-AP2.md).** All 16 formal corrections (A16 found already
   right by exact computation, recorded); categories B-H; Leon's answers 2-7: the costed premise
   synthesis.common-ceiling-coupling-premise (P2 unchanged) with six assumes edges; the charged-lepton reality
   clause; the two scrambling estimates lowered to conjectured (8 results that only analyse the spreading law now
   mention it instead of using it, so they stay proved); the no-coupling and wall-class restatements; the
   recording postulate one-relation.recorded-sectors-superselected-premise; the Zurek envariance import
   (one-relation.imported-envariance-born-rule, checked against the arXiv text); 14 conventions lines.
5. **GTG proofs for the 34 gravity results whose proofs still worked in components (GTG_PROOFS.md; gtg-1/2/3.md).**
   29 full GTG proofs, 4 partial, 1 not achievable (dark-energy.walls-free-sector: rank counts where hb is
   degenerate, outside the GTG definition), plus 1 definition with nothing to prove. Each new main proof has exact
   check functions (Fractions, lib/GA.py and lib/gtg.py), mutation-tested by check4; the component computation is
   kept as a labelled reading and in orig-proof-main.tex. The Ellis-MacCallum frame formula, previously cited from
   memory, is now derived in GTG as an exact polynomial identity.
6. **Blind review and fix round (REFEREE_GTG.md, FIX_GTG.md).** Three referees recomputed every doubtful step in
   their own scripts: 7 ACCEPT, 24 ACCEPT WITH FIXES, 0 REJECT. Every finding was re-verified and applied
   (about 55), two disputed with computation. Substantive ones: the Euclidean frame field equation sign and the de
   Sitter sign in synthesis.promoted-norm-weyl-clock-flat-weight (its check did not detect a flipped store sign;
   now it does); a false "both null second fundamental forms vanish" in series-wald (only chi along xi vanishes,
   theta_n = -4/r_b); two wrong conformal products in the frozen-point stiffness proof; a converse-of-the-Fact step
   in two-frozen-points; a vacuous MacDowell-Mansouri check (removed); the wrong null vector in positive-structure
   (iii). None reached a formal statement except as listed under For Leon. docs/gtg-dictionary.md gained the
   Euclidean sign (unit S^4: calR(B) = -B, Einstein is calR(a) = -Lambda a).
7. **Pin review (PIN_REVIEW.md, pin-review.md).** 751 stale pins at the start; 576 notation-only repins, 106
   restatement repins after reading the dependant's use (each noted), 4 quotations updated, 0 left; the 70 on the
   GTG entities were reviewed in the fix round and at close-out (0 left; the build reports 0 stale claims).
8. **Language check.** The bare-unit detector now also catches 3iI_2, 2iJ, a lone iq and Q(i), and no longer
   flags an index pair such as $ij$ (tests added). At close-out `tp ga-report` found three entities using notation
   outside GA with nothing declared: sheaf.wall-fibre-black-hole and note.sheaf.remark-965 now name the quotient
   Cl(1,2) = Cl(3,0), the Pauli algebra (isomorphism stated in the proof, checked exactly), in place of
   Mat_2(C); the Haefner-Nicolas import declares its source's L^2 tensor C^2. The report now lists none.

## GA coverage, stated plainly

Of 2,269 entities, 40 declare outside_ga: 22 bridge (results whose point is the standard form beside the GA one),
6 imported (a source's own formalism), 12 other. The 12 "other" are where GA is not reached: the walls-free
sector (degenerate soldering), the boundary-mode first law (iv) (small-ball expansions in components; a GTG
proof needs a second-order normal gauge not derived here), the global clauses of the promoted-norm pair and the
frozen-point integrand (cohomology, the Chern-Simons form and integrals beyond one flat chart), the Chern-Simons
gauge variation in the Euler edge term, index displays in the einstein-condition and series-wald results, the
Kasner-wall coframe setting, the frozen-point Stelle-West form displays, a machine-verification note and the
rule-2 fusing plane. Each declaration says exactly what remains and why. `tp ga-report` lists no undeclared use.

## For Leon

Formal statements the reviews found wrong or imprecise (exact text in the named report):
1. synthesis.positive-structure-... (iii): the null vector is l = grad(t + x1) = e0 - e1, not e0 + e1; the
   conclusion stands (fix-F3.md).
2. synthesis.macdowell-mansouri-principle-...: l^2 = 3/|Lambda| gives the wrong sign on the anti-de Sitter
   branch; write A(a) = Omega(a) - (Lambda/3) hb^-1(a) ^ V; clauses (i)-(iv) unaffected (fix-F2.md).
3. pairing.static-frame-...: "vanishes at F = 0" should be "tends to 0 as F -> 0 (the static gauge is not defined
   on the horizon locus)" (fix-F2.md).
4. synthesis.frozen-point-unique-...: the Consequently clauses need c != 0 (fix-F3.md).
5. synthesis.nondiagonal-kasner-...(i): the GTG proof fixes the sign left "up to the sign convention" (fix-F1.md).
Links and premises:
6. Two of the six new ceiling-coupling assumes edges (which-towers-can-carry-arrow, no-coupling-rule) cite the
   premise for scope only; you may drop them (apply-AP2.md).
7. c-loc-local-horizon-premise: no edge recommended from series-wald or euler-entropy (fix-F2.md).
8. dark-energy.imported-frozen-point-geometry names the tractor theorem, which rests (through stelle-west) on
   this Fact; make that sentence a text-only remark (fix-F1.md).
9. The mirror's theta angle was read as one of the couplings the ceiling premise equates; if not, the asymmetry
   remark should say nothing in the store equates the angles (pin-review.md).
10. synthesis.mirror-asymmetry-route-one (iii) says P2 does not reach the temperature; tower-charge proves that only
    on finite windows or when its sum converges (pin-review.md).
Formal restatements in GA not made without a decision: the weighted blow-up object's display, the two-form and
four-form definitions in frozen-point-integrand (gtg-3.md); index expressions marked as readings in three formal
levels (gtg-1.md). Deferred wording (H5): kappa -> mu in the n-plus-null postulate (23 users) and a few double
letters (apply-AP1.md). references.yaml would restore WeinbergQFT1 on a rebuild until T12-lepton's bib is merged.

## Checks

- `tp check --store store --full --keep-going --author leon` (all six layers, every check rerun, 37 min):
  0 errors, 9 warnings, all from this run's last edits (6 W405 on new uses edges, now touched by premise() in
  the GTG checks; 3 W503 wording, fixed). Log: final-check-full.log.
- After the close-out edits, all six layers with the layer-4 cache: 0 errors, 0 warnings (final-check.log).
- `tp build`: 2,269 entities, 7,113 edges, 0 errors, 0 stale claims. `tp.site` rebuilt. `tp lock` written;
  layers 1-3 after the lock: 0 errors, 0 warnings.
- Unit tests: 393 passed, 1 skipped.

## Second round (Leon's answers of 17:31; DECISIONS.md "second round"; APPLY2.md, apply2-D1/D2/D3.md)

- The five formal corrections applied as worded, each verified exactly first (positive-structure 3 -> 4,
  macdowell-mansouri-principle 3 -> 4, static-frame 8 -> 9, frozen-point-unique 5 -> 6, nondiagonal-kasner 4 -> 5;
  the Kasner sign recomputed independently from the Christoffel symbols).
- The two scope-only ceiling-coupling edges dropped (which-towers, no-coupling-rule 5 -> 6); route one (iii)
  scoped to finite windows or a convergent sum (3 -> 4); the frozen-point Fact's sentence naming the tractor theorem
  made a text remark (6 -> 7; two-frozen-points 4 -> 5 now cites the Fact's display); the theta reading and the
  no-edge c-loc decision recorded.
- The last formal notation outside GA rewritten, each old form a labelled reading proved equal exactly: the weighted
  blow-up object (declaration withdrawn), the frozen-point integrand's two- and four-forms, and the index readings
  of black-hole-data, frozen-point stiffness and collapsing-hole (four new checks, mutation-tested).
- The deferred renames: kappa -> mu in synthesis.n-plus-null-ground-state; the double letters of R01, R02 and R04
  (the rung-field Hermitian norm is \mathsf{N} in all 14 entities); d Omega^2 written out beside the gauge field.
- The anti-de Sitter question raised by D1 on five related texts (A = Omega - hb^-1 ^ V/l^2): checked, no error;
  they define l^2 = 3/Lambda with its sign, so l^2 < 0 on the anti-de Sitter branch and the formulas hold.
- Pins: every pin on a changed entity reviewed (36 + 102 + 13), 0 stale; build 0 stale claims.
- Checks: all six layers (layer-4 cache), 0 errors, 0 warnings (final-check-2.log); build 0 errors; lock
  rewritten; 393 tests pass.
- Small items (Leon, 18:25: "Do the small items"): boost-evolution's rotor B_lambda renamed G_lambda (5 -> 6)
  and hadamard-scaling-limit's region U renamed \mathcal{O} (7 -> 8); the sign of l^2 = 3/Lambda (negative on
  the anti-de Sitter branch) named in the four texts that use l (imported MacDowell-Mansouri 3 -> 4,
  frozen-point-makes-stelle-west 6 -> 7, odd-extensions frozen point 7 -> 8, the five-dimensional reduction 3 -> 4;
  frozen-point-action-is-bf writes no l in its levels); the weighted blow-up object checked against dictionary
  section 14 and not flagged (the tau = 0 boundary is a limit of the collar, which section 14 lists as not beyond
  one chart), recorded in its extraction. 44 dependant pins repinned (notation only). All six layers 0 errors,
  0 warnings (final-check-3.log); build 0 stale claims; lock rewritten; 393 tests pass.
