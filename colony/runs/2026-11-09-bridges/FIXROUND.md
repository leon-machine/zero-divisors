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
