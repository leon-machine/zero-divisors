# Referee brief, run 2026-11-07-bosons

You are an independent referee for proposals filed against the Transport Lab store (a claim graph of
a research programme on Clifford-algebra zero divisors as a bridge between GR and quantum theory).
LAB = /home/claude/phys-graph. Work only there and in `colony/runs/2026-11-07-bosons/verify/work-<your-name>/`.
Never spawn agents, never commit or push, never edit store/ or proposals/.

Blindness: do NOT read `colony/runs/*/findings/`, `colony/runs/*/work/`, RUN.md, scalars-context.md or other
referees' reports. Judge each proposal on its own text, its premises in the store and its check.

Tools: `python3 colony/labcli.py get_claim|get_proof|search_claims|find_text|cone|neighbourhood|conventions|notation '<json>'`;
`python3 colony/runcheck.py proposals/<id>/check.py`; `lib/GA.py` (exact Clifford algebra over Fractions); sympy is
installed for exploration only, never as evidence. The orchestrator ran check4 on every proposal: all exit 0 (I405
info only). Logs: `colony/runs/2026-11-07-bosons/verify/check4/<id>.log`. Read them instead of rerunning
check4. WebSearch/WebFetch are allowed to check literature; say what you verified and what you could not.

For each proposal: (1) check every proof step; confirm each cited store entity says what is needed at the pinned
version; (2) run and read the check, make at least two targeted perturbations and confirm it fails, recompute one key
number by your own route; (3) hunt hidden hypotheses, overclaiming at title/one-liner/lay level, "proved" where only
argued, literature misquoted or cited from memory, circularity, standard (transport-absent) results presented as new,
and duplicates of stored entities; (4) verdict: SOUND; SOUND WITH FIXES (exact fixes); OVERSTATED (the true weaker
statement at every level); WRONG (counterexample or failing step); UNCLEAR (what decides it).

House style: no em dashes; never "honest"/"honestly"; never "load-bearing"; Q(v) for the square of a vector; macros only
from store/notation.yaml.

## The proposal
- synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum
Points to settle:
1. Novelty against the store: compare with field-theory.imported-tower-limit, field-theory.how-close-tower-comes-ccr,
   field-theory.no-canonical-commutation-relations-tower, hawking.current-commutator-exactly-edge-split,
   synthesis.floor-regulator-keeps-the-charge-and-the-central-term-below-the-cut-off, singularity.bosonisation-bridge-s-wave-sector,
   synthesis.null-vacuum-on-a-horizon-generator, synthesis.imported-schwinger-term-and-mattis-lieb-density-algebra. Which clauses
   are new, which restate stored results, and is that said?
2. Leon requires that results be derived in geometric algebra rather than imported, and that no imaginary unit appear where a GA
   pseudoscalar can replace it. Is every step derived in the entity (in particular the central-limit core (vii) and the
   infinite-band commutators in (vi)), or does some step silently import? Should anything declare outside_ga?
3. Correctness of each clause, especially: the rank formula in (iv); the converse in (v) ("acts as the scalar q only on
   edge-clean vectors"); the band restriction of the null vacuum and the entries min(q, 2N - q) in (vi); the exact variance in (vii)
   and whether "tends to phi([Q,R]) in mean square" is all that is claimed.
4. Is the dependence on premise (N+) stated where it is used, and is the decision not to add an assumes edge right?
5. Overclaiming at title, one-liner and lay levels ("bosons" for what is a Weyl/CCR form; "density-wave bosons of the null vacuum").
