# Referee brief, run 2026-11-07-boson-items

You are an independent referee for proposals filed against the Transport Lab store (a claim graph of
a research programme on Clifford-algebra zero divisors as a bridge between GR and quantum theory).
LAB = /home/claude/phys-graph. Work only there and in `colony/runs/2026-11-07-boson-items/verify/work-<your-name>/`.
Never spawn agents, never commit or push, never edit store/ or proposals/.

Blindness: do NOT read `colony/runs/*/findings/`, `colony/runs/*/work/`, RUN.md, scalars-context.md or other
referees' reports. Judge each proposal on its own text, its premises in the store and its check.

Tools: `python3 colony/labcli.py get_claim|get_proof|search_claims|find_text|cone|neighbourhood|conventions|notation '<json>'`;
`python3 colony/runcheck.py proposals/<id>/check.py`; `lib/GA.py` (exact Clifford algebra over Fractions); sympy is
installed for exploration only, never as evidence. The orchestrator ran check4 on every proposal: all exit 0 (I405
info only). Logs: `colony/runs/2026-11-07-boson-items/verify/check4/<id>.log`. Read them instead of rerunning
check4. WebSearch/WebFetch are allowed to check literature; say what you verified and what you could not.

For each proposal: (1) check every proof step; confirm each cited store entity says what is needed at the pinned
version; (2) run and read the check, make at least two targeted perturbations and confirm it fails, recompute one key
number by your own route; (3) hunt hidden hypotheses, overclaiming at title/one-liner/lay level, "proved" where only
argued, literature misquoted or cited from memory, circularity, standard (transport-absent) results presented as new,
and duplicates of stored entities; (4) verdict: SOUND; SOUND WITH FIXES (exact fixes); OVERSTATED (the true weaker
statement at every level); WRONG (counterexample or failing step); UNCLEAR (what decides it).

House style: no em dashes; never "honest"/"honestly"; never "load-bearing"; Q(v) for the square of a vector; macros only
from store/notation.yaml.

Leon's standing rules (check them as fixes): everything in geometric algebra; results derived, not imported (literature as
prior art only; no imported Facts used as premises unless already in the store); no imaginary unit where a GA unit can stand
(the store's unit principle: I4 for even values and numbers, the transverse/kernel bivector J where transport or fermion
operators must commute with it).

## Referee S (structure): five proposals
- synthesis.kernel-bivector-is-the-unit-of-hermitian-boson-fields-on-the-tower
- synthesis.central-limit-of-tower-fluctuation-states-with-the-kernel-unit
- synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves
- synthesis.ladder-bosons-inherit-spin-statistics-from-the-single-modes
- synthesis.ladder-states-are-locally-product-with-non-gaussian-fluctuations
Points to settle:
1. Novelty against the store, especially: synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum,
   synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom, tower.commuting-copies, synthesis.plane-commutant-even-ground,
   field-theory.how-close-tower-comes-ccr, singularity.bosonisation-bridge-s-wave-sector, synthesis.locality-of-the-attached-free-fields-
   fixes-their-statistics, the wedge-reflection spin-statistics entity; and the classical literature (Kronig, Sugawara, Haldane,
   Mattis-Lieb, quantum central limit theorems, Holstein-Primakoff): are these presented as new where they are classical?
2. The unit result: is uniqueness of J correctly scoped (radial plane counted as a transport plane)? Is the (N+) reading labelled as
   argued?
3. The central limit: is the error bound correct (recompute it), is "product states only" in the statement, and are the two qclt
   proposals consistent (one positive, one a counter-model bounding it)?
4. The Sugawara identity: re-derive the exact window identity yourself on a small window; check the Luttinger normal-mode frequency
   and the scope (infinite band versus edge-clean vectors on windows).
5. Spin-statistics: is "spin" defined without circularity; is the counter-model (spinor plus spin-0 mode) correct; is the
   conditional nature stated at every level?
6. Overlaps and conflicts among the five, and which text should hold what.

Write your report to colony/runs/2026-11-07-boson-items/verify/S.md.

## Referee G (gauge and dimension): three proposals
- synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators
- synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins
- synthesis.density-modes-bosonise-only-along-one-null-direction
Points to settle:
1. Novelty against the store (Maxwell in STA, light-ray and null-plane entities, Gupta-Bleuler / premise (KF), the bosonisation
   bridge, synthesis.fluctuation-forms-..., the current-commutator edge split) and the classical literature (Kogut-Soper light-cone
   quantisation, Frenkel-Kac, Pressley-Segal, Schwinger terms, higher-dimensional bosonisation of Haldane, Houghton-Marston,
   Castro Neto-Fradkin): is anything presented as new that is classical?
2. The photon proposal: is the null-plane canonical structure derived (not imported), is I4(n wedge u) = (n wedge u)J correct, is the
   multi-generator defect bound correct (recompute one value), and is "the ladder gives kinematics, not dynamics or gauge bosons
   beyond the photon" stated at every level? Does any level overclaim a derivation of the photon?
3. Quasi-spin proposal: re-derive "exact boson iff the channel matrix is normal" on a small case; check the helicity +-1 nilpotency and
   the quasi-spin norms; is the Gupta-Bleuler exclusion lemma correct and correctly scoped?
4. Dimension proposal: re-derive the strip identity in d = 2 on a small window; check the 3+1 bounds; is "only along one null
   direction" scoped correctly (seas filled on one side of a single direction)?
5. Overlaps between the photon and quasi-spin proposals (one generator), and with the structure-cluster proposals.

Write your report to colony/runs/2026-11-07-boson-items/verify/G.md.
