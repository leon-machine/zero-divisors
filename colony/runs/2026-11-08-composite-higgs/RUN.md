# Run 2026-11-08-composite-higgs: what is specific to this run

LAB = /home/claude/phys-graph. Run folder: colony/runs/2026-11-08-composite-higgs/ (findings/, work/<name>/, verify/).
Read colony/BRIEF.md and colony/POLICIES.md; this file overrides them. Baseline: baseline.log (0 errors, 0 warnings).

## Target
op.qft-bosons-and-the-rung-field (store/open_problems.yaml; read its statement, known (including the 8 November paragraph)
and attack items). Question: is there, on the tower, a GAPPED composite scalar of helicity zero carrying the charges of a
doublet, beyond mean field? Known constraints (read each entity first):
- exact pair bosons exist on a generator's filled sea, helicity 0, gapless (linear dispersion), also with a Luttinger
  coupling (synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum,
  synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves,
  synthesis.central-limit-of-tower-fluctuation-states-with-the-kernel-unit, synthesis.ladder-states-are-locally-product-with-non-gaussian-fluctuations);
- the unit of Hermitian boson fields is the kernel bivector J (synthesis.kernel-bivector-is-the-unit-of-hermitian-boson-fields-on-the-tower);
- channel-resolved pair densities can carry a canonical pair (synthesis.density-modes-bosonise-only-along-one-null-direction);
- mean field: NJL-type gap equation (field-theory.composite-scalars-mean-field-level); for one species on a single shell the
  pair-breaking threshold is twice the quasiparticle energy (synthesis.tower-pairing-gap-at-fixed-charges-is-twice-the-quasiparticle-energy);
- the rung field is odd in the tower and its modes carry no even doublet
  (synthesis.rung-field-is-odd-in-the-tower-and-its-modes-carry-no-even-doublet); an elementary local rung scalar with a
  positive norm is palatial (synthesis.locality-of-the-attached-free-fields-fixes-their-statistics).
The open route recorded in the store: a light multi-species composite, two-condensate pairing (a doublet-singlet fermion
condensate). Success: an exact finite statement (a gap with an explicit bound, the charges, the parity of the composite,
whether it can be a doublet) or an obstruction; either is a result.

## Pairs
Attacker A (constructive): build the two-condensate model on finite towers (two species, doublet and singlet channels, a
pairing or particle-hole interaction), compute exactly its spectrum: whether the lowest collective pair mode of the
doublet channel is gapped (bound state below the pair-breaking threshold, with the gap's dependence on the couplings) and
its charges; take the infinite-tower limit only with an explicit error statement.
Attacker B (adversarial): find the obstructions: is an even composite doublet excluded on the tower (parity, the rung's
oddness, the edge identity, the Goldstone count of a broken symmetry), does any gap close in the collective limit, is the
helicity-zero mode necessarily gapless (a Goldstone mode) when the condensate breaks a continuous symmetry.
Both: everything in GA (unit J, no imaginary unit), derived not imported (literature such as Nambu-Jona-Lasinio,
Bardeen-Hill-Lindner top condensation, Anderson-Higgs, Goldstone, BCS collective modes is prior art in the extraction note
only), exact checks (Fractions, lib/GA.py). Up to 2 proposals each; read your sibling's findings midway and at the end.

## Gate and rules
As BRIEF.md and the previous runs: check4.py exits 0 with no warnings (no W413); validate_one ok
(colony/runs/2026-11-06-edge-normality/verify/final/validate_one.py <dir> colony/runs/2026-11-08-composite-higgs/verify/final);
register with `python3 colony/labcli.py propose_claim @<abs draft json>` (move aside first; copy coverage.yaml back; quote
YAML strings containing ": "); a proposal cannot cite another proposal (E201). House style: no em dashes; never
"honest"/"honestly"/"load-bearing"; Q(v) for squares; no agent or run names in store text. Credit {name: Claude Opus 5.5,
role: proposal and drafting, source: run 2026-11-08-composite-higgs}. One gate process at a time; 2 CPUs shared; never kill
other processes; do not edit store/, commit, push or spawn agents. Findings: findings/attack-A.md, findings/attack-B.md.
