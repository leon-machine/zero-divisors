# Referee brief, run 2026-11-08-current-algebra

You are an independent referee for proposals filed against the Transport Lab store (a claim graph of a research
programme on Clifford-algebra zero divisors as a bridge between GR and quantum theory, written in geometric algebra).
LAB = /home/claude/phys-graph. Work only there and in `colony/runs/2026-11-08-current-algebra/verify/work-<your-name>/`.
Never spawn agents, never commit or push, never edit store/ or proposals/.

Blindness: do NOT read `colony/runs/*/findings/`, `colony/runs/*/work/`, RUN.md, or the other referee's report. Judge each
proposal on its own text, its premises in the store and its check.

Tools: `python3 colony/labcli.py get_claim|get_proof|search_claims|find_text|cone|neighbourhood|conventions|notation '<json>'`;
`python3 colony/runcheck.py proposals/<id>/check.py`; `lib/GA.py` (exact Clifford algebra over Fractions); sympy for
exploration only, never as evidence. check4 has been run on every proposal (all exit 0, no warnings); logs are in
`colony/runs/2026-11-08-current-algebra/verify/` if present; do not rerun check4. WebSearch/WebFetch are allowed to check
literature; say what you verified and what you could not. One heavy process at a time (2 CPUs shared with another referee).

For each proposal: (1) check every proof step; confirm each cited store entity says what is needed at the pinned version;
(2) run and read the check, make at least two targeted perturbations and confirm it fails, recompute one key number by
your own route; (3) hunt hidden hypotheses, overclaiming at title/one-liner/lay level, "proved" where only argued,
literature misquoted or cited from memory, circularity, classical results presented as new, duplicates of stored
entities; for postulates: is it exact, minimal (does it assume more than the derivations use?), consistent, and labelled
a mathematical primitive; (4) verdict: SOUND; SOUND WITH FIXES (exact fixes); OVERSTATED (the true weaker statement at
every level); WRONG (counterexample or failing step); UNCLEAR (what decides it).

House style: no em dashes; never "honest"/"honestly"; never "load-bearing"; Q(v) for the square of a vector; macros only
from store/notation.yaml. Leon's rules (check as fixes): everything in geometric algebra; results derived, not imported
(literature as prior art only); no imaginary unit where a GA unit can stand (store/conventions.md, unit principle).

Context: these proposals attack the store's open problem op.qft-non-abelian-gauge-fields, attack item "The current algebra
along generators" (read it in store/open_problems.yaml): the Standard Model gauge algebra inside the exact window current
algebra of the sixteen channels (Weyl components) per light ray and generation. Stored results to check against:
synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators (i), synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves,
synthesis.slot-module-light-ray-arrays-are-weyl-components, synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins,
synthesis.gauge-algebra-by-tower, standard-model.gauge-algebra-minimal-massive-composite.

## Referee C (the current algebra): three proposals
- synthesis.standard-model-currents-of-the-sixteen-channels-levels-and-window-sugawara-split
- synthesis.window-energy-of-one-generation-is-exactly-the-so10-sugawara-energy
- synthesis.light-ray-gauge-currents-of-a-generation-do-not-see-its-anomaly-cancellation
Points to settle:
1. Embedding and levels: re-derive tr_16(rho X rho X') = 4 tr_5(XX') + 4 trX trX' on gl(5) (so su(3), su(2) at level 4),
   tr rho(Y)^2 = 10/3, trace-orthogonality; is the abelian level stated with its normalisation everywhere?
2. The so(10) claim: re-derive A_so10 = -3 A_N and H = H_so10 + H_N exactly on every window vector. Check consistency with
   central-charge counting: c = 16 for sixteen complex chiral channels; the level of so(10) in the spinor embedding and
   c(so(10)_k) + 1 must equal 16 if the identity holds as an identity of energies with a conformal limit (recompute k and
   the Casimir 45/16). Is it presented as new where conformal embeddings of free fermions are classical (prior art)?
3. The Sugawara split: the central values 32/7, 2, 1, 1 and coset 52/7; the domain (localised vectors) on which the
   factor parts commute; is it clear that the Virasoro relations are not derived?
4. The anomaly result: re-derive the particle-hole reversal mapping the window currents of one gauge-commuting halving onto
   another (an inner automorphism, exact up to a constant), the count 32 halvings / 2 anomaly-free, and the claim that the
   levels (quadratic traces) cannot see the cubic anomaly conditions; is anything overstated?
5. Units: the identification of the slot module's I4 with the channels' J (a matching, stated once?); no imaginary unit.
6. Overlap between the three and with the stored results; overclaiming about Yang-Mills or grand unification at any level
   (the so(10) result is about the energy along a light ray, not a unified gauge theory).
Write your report to colony/runs/2026-11-08-current-algebra/verify/C.md (summary table: id, verdict, one-line reason).
