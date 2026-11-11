# Applied to the store (11 November 2026)

Leon's decisions of 11 November 2026 on PROPOSALS.md: P1 stays as two clauses; (FS) supplies the field equations
of the no-echo basis; the reduction theorem is edited, not split. The changes were made by
`work/apply_edits.py` (each replacement asserted) and `tp repin`.

## New
- `synthesis.frozen-point-unique-for-the-field-space-connection` (proved, v1): the uniqueness of the frozen point
  for the (FS) connection, with the Einstein, isotropic-matter and torsion clauses, the application to towers
  (the constants $c_{r}$ stay free) and the Remark on the tower of reversed signature. Four check functions,
  adapted from the referee's script, with pinned values.

## Changed (version raised, credit, amendment and extraction note on each)
| Entity | Version | Change |
|---|---|---|
| `dark-matter.p1-single-frozen-point` | 2 to 3 | note naming the connection of (P1a) under (FS); premise unchanged |
| `synthesis.frozen-point-unique-where-weyl-has-no-kernel` | 6 to 7 | scope note (normal tractor connection) |
| `synthesis.two-frozen-points-conformally-flat` | 5 to 6 | scope note |
| `scrambling.no-echo-prediction-registered` | 2 to 3 | basis restated; assumes (FS), (C$_{\mathrm{loc}}$), (N$_{+}$); (C1) removed; all four levels |
| `transport.obstructions-are-moved-never-destroyed` | 2 to 3 | restated (strict completion, beyond the tame case, rung note); deposited text under source_formal |
| `dark-matter.d-democracy-total-mass` | 2 to 3 | note names the one exception |
| `synthesis.dark-to-baryon-total-uses-r1-r2-and-d-only-as-mass-per-unit-ball` | 1 to 2 | two stale sentences |
| `synthesis.matter-asymmetry-registered-free-input` | 3 to 4 | note on the unit of $\epsilon$ |
| `standard-model.dating-descent` | 6 to 7 | clause (i): near the onset of $\Lambda$-domination |
| `pred.dimmed-evaporation-bursts` | 6 to 7 | the odd towers' population is now a premise (wording) |
| `neutrino.double-prediction-sum-predicted-floor` | 1 to 2 | note: the condition is now (FS); opposite exposure |

`store/open_problems.yaml`, op.pre-descent-theory: two attack items (the element $\operatorname{Ad}(I_{4})$ and
P1b with the normalisation $c_{r}$; a comoving statement of the charge reading). Fourteen pins of fourteen
dependants moved to the new versions of P1, D and the no-echo prediction (the premises and the prediction's
content are unchanged).

## Checked before storing
- T1 Conjecture 7.9: the deposited wording (T01_transport_principle.tex, line 1555) is the stored formal level
  of version 2, word for word; it is now under source_formal.
- Oshita, Wang and Afshordi, "On Reflectivity of Quantum Black Hole Horizons", arXiv:1905.00464,
  JCAP 04 (2020) 016: the abstract derives a flux reflectivity equal to the Boltzmann factor from detailed
  balance and the fluctuation-dissipation theorem. Abstract only; the paper was not read.

## Not applied
- The Kasner premises (withdrawn; Leon's decision of 1 November stands).
- The words "per mode" in `dark-matter.mirror-tower-copy-one` and the formula $Q = \epsilon N$ in
  `dark-matter.stored-asymmetry-charge-not-number` are left as they are; the note on the registered premise
  names both. Editing them would move the pins of 31 dependants for a clarification.
- The `contradicts` link between Hypothesis (U) and Premise (EW): its rationale already says in which reading
  they conflict; putting the entry reading into (U)'s formal level would change a postulate under 37 results
  and is left for Leon.
- The $\eta'$ range of the charge result (18.6 to 27.8 recomputed against the stored 19 to 26): consistent if
  the floor is near $2.85 \times 10^{-4}$; the stored numbers are script-evaluated and were not changed.

## Validation
`tp check --layers 1,2,3,4`: 0 errors, 0 warnings. Layers 5 and 6: 0 errors, 0 warnings. `pytest tests`: 405
passed, 1 skipped. The lock file is not updated; that is the maintainer's step on acceptance.
