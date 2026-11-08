# Referee brief, run 2026-11-08-composite-higgs

You are an independent referee for proposals filed against the Transport Lab store (a claim graph of a research
programme on Clifford-algebra zero divisors as a bridge between GR and quantum theory, written in geometric algebra).
LAB = /home/claude/phys-graph. Work only there and in `colony/runs/2026-11-08-composite-higgs/verify/work-<your-name>/`.
Never spawn agents, never commit or push, never edit store/ or proposals/.

Blindness: do NOT read `colony/runs/*/findings/`, `colony/runs/*/work/`, RUN.md, or the other referee's report. Judge each
proposal on its own text, its premises in the store and its check.

Tools: `python3 colony/labcli.py get_claim|get_proof|search_claims|find_text|cone|neighbourhood|conventions|notation '<json>'`;
`python3 colony/runcheck.py proposals/<id>/check.py`; `lib/GA.py` (exact Clifford algebra over Fractions); sympy for
exploration only, never as evidence. check4 has been run on every proposal (all exit 0, no warnings); logs are in
`colony/runs/2026-11-08-composite-higgs/verify/` if present; do not rerun check4. WebSearch/WebFetch are allowed to check
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

Context: these proposals attack the store's open problem op.qft-bosons-and-the-rung-field (read it in store/open_problems.yaml):
whether the tower has a gapped composite scalar doublet beyond mean field. Prior stored results to check against:
synthesis.tower-pairing-gap-at-fixed-charges-is-twice-the-quasiparticle-energy, synthesis.rung-field-is-odd-in-the-tower-and-its-modes-carry-no-even-doublet,
field-theory.composite-scalars-mean-field-level, synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins,
synthesis.kernel-bivector-is-the-unit-of-hermitian-boson-fields-on-the-tower.

## Referee H (the composite Higgs): three proposals
- synthesis.two-species-floor-pairing-has-a-gapped-doublet-pair-mode-that-closes-where-it-condenses
- synthesis.uniform-pair-channel-of-a-tower-condensate-is-a-goldstone-rotor
- synthesis.even-composite-doublet-needs-a-singlet-constituent-and-its-pair-modes-are-quasi-spins
Points to settle:
1. The two-species floor: re-derive the band formula, the doublet quantum omega_D and its commutator, the binding below the
   pair-breaking threshold, the "two phases on the band" claim (coexistence only at omega_D = 0). Which clauses are proved
   for every n_b and which are computed for n_b <= 6 and conjectured (the spectrum of the pair sum W): is that split stated
   at every level, including title and one-liner? Is "gapped only while it does not condense" proved or argued?
2. The Goldstone bound: re-derive the second-difference bound across charge sectors at finite size; check its hypotheses
   ([X, X*] a function of the charges only) and that the single-shell value 2G is attained; is the claim "a condensate's
   uniform pair channel is a rotor" scoped to those hypotheses (B reports it does not cover the doublet floor or coupled
   condensates: is that limit stated)?
3. The parity rule: is "an even doublet needs an odd number of singlet factors" correct and new against the rung result; is
   clause (ii) a restatement of the stored helicity-one theorem (then say so) or new content?
4. Consistency across the three and with the stored results; overclaiming about the Higgs at any level (the elementary
   reading is the store's; neither proposal should claim more than "argued" about it).
Write your report to colony/runs/2026-11-08-composite-higgs/verify/H.md (summary table: id, verdict, one-line reason).
