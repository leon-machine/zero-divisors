# Fix round, run 2026-11-09-bridges

Referee reports: colony/runs/2026-11-09-bridges/verify/R1.md and verify/R2.md. Read your proposals' sections in full; the
required fixes there are your fixes, with the overrides below. Apply every fix in place in proposals/<id>/ at every level
(title, one-liner, formal, technical, lay, proof, extraction note, check). OVERSTATED proposals are restated to the
referee's true weaker statement at every level; numbers never appear above the proof text that proves them. Keep every
stored file. Run ONLY `PYTHONDONTWRITEBYTECODE=1 python3 colony/runcheck.py proposals/<id>/check.py`; never check4,
validate_draft or tp check (the orchestrator reruns them centrally). Write findings/fixes-<name>.md with
"check4: pending (orchestrator)". Rebut a fix only with a computation. Do not edit store/, commit, push or spawn agents.

## Overrides (Leon's decisions and store rules)
1. No new imported Facts. Leon decided (this run) that the lens-space inputs (cohomology rings, T Sigma + R, q1 and p1,
   the K-ring, lambda-operations, Sq^1) are NOT imported. Instead state them in the formal statement as explicit
   hypotheses ("Given the classical facts (L1)-(L3), cited from memory and not in the store: ..."), so each result is a
   conditional theorem, and say in the extraction note that deriving them is an open item. The same for completeness of
   spinor harmonics and the exact/co-exact split (horizon channels). Existing stored Facts may be cited and pinned (for
   example synthesis.imported-whitney-product-formula-and-projective-space@1,
   synthesis.imported-brst-kugo-ojima-strocchi-and-gribov@1).
2. No new assumes edges in proposals (maintainer-only, E203). Where a referee asks to add a postulate to `assumes` (for
   example (Q)@3, the window reading, C2), do not add it: name it in the extraction note under "premises used, assumes edge
   for the maintainer" and the orchestrator will put it to Leon.
3. No proposal can cite another proposal (E201). Overlap rulings that ask one proposal to cite a sibling are done by the
   maintainer after acceptance: remove the duplicated content only where the referee says it is duplicated with no loss,
   otherwise keep it, and add one sentence in the extraction note naming the sibling id as the intended citation.
4. J3 caveat (R2 points 1, 2, 5; R1 point 3): the stored postulate hawking.joint-j3-s-wave-reduction reads integer-weight
   channels as currents of the arrays; Leon has decided to narrow it to spin 2 once the horizon-channel derivation is
   accepted. State every boson-counting reading relative to J3 as R2 says.


## This run
Referee reports: verify/R2.md (finite averages, dark-tower coefficients, curvature coupling) and verify/R1.md (rung
counts, curved-field kernel, order-four element, mass terms; when it exists). Read your proposals' sections in full and
apply every numbered fix; ids are never renamed (fix titles instead). Ignore any assignment or caveat above that names
entities of an earlier run.
- Quarter-turn design (C1A): fixes 1-8. "Rotor" only for bivector generators; the invariant-measure strengthening (fix 6)
  and the parity-sector corollary (fix 7) go in with checks. Leon has decided to retire the imported Haar mean-purity
  Fact in favour of this derived result: say in the extraction note exactly which dependants can cite it (powers of two
  only) and which cannot.
- Finite averages at order four and on a parity sector (C1B): fixes 1-8, the overlap ruling (clause (ii) becomes the
  blade-state case of the design statement, named as intended citation), and verify the referee's limit step before
  upgrading (iii) to proved; if you cannot verify it, keep "computed".
- Dark-tower coefficients (C1A): fixes 1-8; retitle; (iv) argued and consistent with the three stored results, which
  enter `uses` at their current versions.
- Curvature coupling (C1A): verdict OVERSTATED. Restate at EVERY level (title, one-liner, formal, technical, lay,
  reading, note, check) to the referee's weaker statement, scoped to gauge parameter one, with the free-gauge-parameter
  counter-statement alpha = 1/3 + 4 xi included as a clause; delete the massive-vector sentence with its proof and check
  lines (fix 3); numerology disclaimer (fix 6).
- Bridge leads to fold in where they touch your text (findings/bridges.md, B1-B7): in particular B1 for the mass-terms
  and order-four proposals (every mass form on the sixteen has odd Clifford grade, so all anticommute with the
  pseudoscalar; what a Dirac term keeps is the pseudoscalar times the centre of su(2)_L).
Fixers run only runcheck. Write findings/fixes-<name>.md ending "check4: pending (orchestrator)".
- From verify/R1.md:
  - Definite-side rung count (C2A): fixes 1-8 (Stolz's level formula as prior art replacing the wrong recollection; the
    extra obstruction-theory background stated as an extension of the stored (G); "does not obstruct" wording for d = 0
    mod 8; cross-reference to the three-rung sibling by name in the extraction note). Leon has asked for the classical
    inputs (T) to be derived, not imported; a separate attacker is attempting the specific obstruction in the cell model.
    Keep the lower bound conditional on (T), stated exactly as fix 6 words it.
  - Three rungs (C2B): fixes 1-5 (title scope: dimension five and more, dimension five given the spin class; the
    extension of (G); 4 <= k <= 5 on L^5(4)). The twisted cohomology stays in this proposal; the rung-count sibling
    names it as intended citation.
  - Curved-field kernel (C2A): verdict OVERSTATED with one coefficient WRONG. Restate at EVERY level to the referee's
    weaker statement (a)-(d): correct the sign and coefficient (D_x U = +(1/12) Riem(xi) R in the store's convention
    Riem(B) = -R(h(B)); gauge Omega = -(1/2) Riem(z ^ a)); the check must test the gauge's field strength against the
    stored sign and carry the de Sitter test; define Pi_6 or state Weyl squared at degree 2 through the Van Vleck
    determinant; scope (normal coordinates at x', transported index, torsion-free, one loop, parametrix trace form,
    time-ordered kernel) in title or one-liner; the freedom is 15 local terms per index pair with coefficient FUNCTIONS
    of x' unless local covariance with scaling is added; status: (i) and corrected (ii) proved, (iii) and (iv) argued.
    Leon has decided to import both the scaling-degree rules and local covariance with scaling (maintainer pass): state
    in the extraction note exactly which rules and which form of local covariance the result would need, including the
    additions the referee lists (sd of sigma^-k log^j sigma, subadditivity, the first Hadamard transport equation), so
    the Fact is written to fit. If you dispute the sign, rebut only with a computation against the stored convention.
  - Order-four element (C2B): fixes 1-6 (omega = -I(-1)^N on the stored conventions with a state evaluation in the check;
    the Dirac sentence "modulo the Standard Model group" with its check; omega = exp(-(pi/2) I X), classical attribution;
    the two readings marked argued).
  - Mass terms as pair terms (C1B): fixes 1-6 (title scope and no "only"; "among the six listed charges"; the gap
    theorem's clause (iii) and the softened sentences; cross-reference to the order-four sibling by name).
- From verify/R3.md (all four SOUND WITH FIXES):
  - No odd map (C3A): fixes 1-5 (the attribution sentence for (S); the corrected comparison with the three theories;
    the product identity for orders 8, 12, 16 in the check; the secondary-source wording with volume and pages; the
    note on the inherited Atiyah-Hirzebruch dependence). Leon has decided to import (S) as one Fact (maintainer pass):
    keep it an in-statement hypothesis, worded exactly as fix 1 says, so the Fact can be written to fit.
  - Mode split (C3B): fixes 1-9 (the sector mean entropy is the two-block case of Bianchi et al. equation (45): remove
    it from "new here"; the parity average is the total-parity form, a definition here, the stored theorem being
    single-mode; Delta's size; name descent-lift.imported-fermionic-operations-are-even-reduced; conditional inputs at
    every level; "at version 3" in the fate table). Direction ruling: keep the two eviction entities self-contained and
    this entity citing them. The sector lemma's home is the finite-averages sibling (it will be accepted): keep the
    short lemma inline for now and say in the extraction note that it is cut to a citation after acceptance.
  - Two corrected eviction entities (C3B): fixes as numbered (total-parity wording; stale notes "(through version 3;
    removed at version 4)"; amendments text, including for the Catalan entity the second sentence recording that the
    stored upper bound was verified, not proved; the check docstring). "At Leon's request" is now accurate: Leon
    confirmed on 9 November (DECISIONS item 5); cite that.
