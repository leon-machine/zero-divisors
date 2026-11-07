# Fix round, run 2026-11-07-boson-items (role: fixer in colony/BRIEF.md)

Blind referees have reviewed every proposal: verify/S.md (structure cluster)
and verify/G.md (gauge cluster). Read only the sections for proposals YOU filed,
plus the closing "Overlaps and conflicts" section of your report.

For each of your proposals:
1. Apply every fix the referee lists, in place in `proposals/<id>/`, at every level (title, one-liner, formal,
   technical, lay, proof, check). SOUND needs nothing beyond style fixes.
2. OVERSTATED: restate to the referee's weaker true statement at every level, including the title. Do not add a
   caveat to an unchanged claim. If you think the referee is wrong, rebut only with a computation, written into your
   fixes file.
3. Where the referee recommends merging, dropping or turning a proposal into a note: do it if the store schema
   allows it (a note uses `comments_on`; check an existing note in store/notes for the format and run validate_draft
   on it); to drop a proposal, move its folder to colony/runs/2026-11-07-boson-items/work/<you>/dropped/ and say so.
4. Literature the referee verified gets cited by name in the text; literature from memory stays flagged.
5. Weak checks: strengthen so the referee's perturbations fail. Exact arithmetic only.
6. Conditions: every hypothesis the result needs appears in the title or one-liner when the referee asks.

Run ONLY `python3 colony/runcheck.py proposals/<id>/check.py`; never check4.py, validate_draft (except on a new note
draft) or tp check: the orchestrator reruns the gates centrally and returns failures. One process at a time; never kill
other processes. Write colony/runs/2026-11-07-boson-items/findings/fixes-<you>.md with "check4: pending
(orchestrator)". Do not edit store/, commit, or spawn agents.

Leon's standing rules still bind: GA only; derived, not imported (prior art named, never a premise); no imaginary unit.
Overlap rulings (orchestrator, from the referees): the general mode-rotation formula U = e^{theta J sum s_j n_j} lives in
ladder-bosons (i) and the kernel-bivector proposal cites it; graded locality lives in ladder-bosons (ii) and central-limit (i)
cites it; the ladder coefficient lives in ladder-states (i) (or both cite field-theory.how-close-tower-comes-ccr) and
central-limit (iii) cites it. Cite a sibling proposal by its id in plain text if it is not yet in the store.

Gauge-cluster overlap rulings (orchestrator, from referee G): the window identity lives in the density proposal (i), extended to
unequal shifts m, l, and the photon and quasi-spin proposals cite it; the rotation about the generator is defined once, in
synthesis.ladder-bosons-inherit-spin-statistics-from-the-single-modes (i), and the photon and quasi-spin proposals cite it; the unit
J is justified by citing synthesis.kernel-bivector-is-the-unit-of-hermitian-boson-fields-on-the-tower; the photon's dispersion cites
synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves (ii) and (iii); photon (v) and quasi-spin
(iv) cross-cite (finite capacity versus mean-square contraction). Cite sibling proposals by id in plain text.
