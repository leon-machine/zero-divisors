# Referee brief, run 2026-11-16-spectrum

You are an independent referee for five proposals that AI agents filed against the Physics Graph store (a claim
graph of a research programme on Clifford-algebra zero divisors as a bridge between general relativity and quantum
theory). LAB = /home/claude/phys-graph (branch run/2026-11-16-spectrum; do not switch branches, commit or push).
Work only there and in your scratch folder `colony/runs/2026-11-16-spectrum/verify/work-R1/`. Never spawn agents.
Read the "Role: referee" section of colony/BRIEF.md and the store's conventions
(`python3 colony/labcli.py conventions '{}'`).

Blindness: you have NOT seen the agents' reasoning and must not look for it. Do not read
`colony/runs/*/findings/`, `colony/runs/*/work/`, `colony/runs/2026-11-16-spectrum/RUN.md`, or anything else in
the run folder except this file and `verify/check4/`. Judge each proposal on its own text, its premises in the
store and its check.

Tools:
- Proposals: `proposals/<id>/` (entity.md, proof-*.tex, check.py, coverage.yaml). A proposal whose id already
  exists in `store/claims/` is a corrected version: compare it with the stored one file by file.
- `python3 colony/labcli.py get_claim|get_proof|search_claims|find_text|cone|neighbourhood|conventions|notation '<json>'`
  (can be slow; plain grep over store/claims/*/entity.md is fine).
- `python3 colony/runcheck.py proposals/<id>/check.py` runs a check against the store.
- `lib/GA.py`: exact Clifford algebra over Fractions; `lib/gtg.py`: the Gauge Theory Gravity engine. No sympy.
  Floating point for exploration only, never evidence.
- The orchestrator runs the maintainer's evidence layer (check4) on every proposal; logs appear in
  `colony/runs/2026-11-16-spectrum/verify/check4/<id>.log` (they may arrive while you work; the authors' own
  check4 runs exited 0). Read them instead of rerunning check4. The machine has 2 CPUs and other checks are
  running: run one check at a time and never kill other processes.

## The proposals
The context is the open problem op.descent-state-and-spectrum (read it:
`python3 colony/labcli.py get_open_problem '{"id":"op.descent-state-and-spectrum"}'`): the series has no mechanism
for the measured primordial spectrum, and about two dozen stored negative results. The five proposals:

1. `synthesis.descent-slice-constraints-and-the-three-readings-of-a-white-deposit` (new).
2. `synthesis.quasi-free-deposit-has-white-energy-noise-unless-pure-and-stationary` (new).
3. `synthesis.exchangeable-deposits-carry-two-numbers-and-no-spectral-shape` (new).
4. `synthesis.sparse-fermion-deposit-reaches-the-amplitude-on-a-flat-slice-only-with-super-planckian-quanta` (new).
5. `synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise` (stored at version 4; proposed version 5, a
   restatement).

## Specific points to settle
For 1:
- Derive the linearised energy and momentum constraints on an arbitrary slice yourself (any formalism you trust,
  then compare with the proposal's GTG statement) and confirm the constraint as stated, with its signs, and the
  slice's scalar curvature formula.
- The growing-mode projection in the radiation era: confirm that data with uniform expansion and a white density
  contrast are, to leading order outside the Hubble length, a growing mode with conserved amplitude
  (3/2)(a_d H_d/k)^2 times the contrast (so the spectrum conversion factor is 9/4 (a_d H_d/k)^4), and that the
  flat-slice data give delta/4 plus a momentum term of relative order (a_d H_d/k). Solve the radiation-era
  perturbation equations yourself; do not trust the series quoted. Check the claimed indices -1, +1, +3 and what
  each needs.
- Recompute the thermal amplitude at the pivot by your own route at T_d = 1 MeV, 7.3e8 GeV and 1e12 GeV, and the
  temperature at which it equals A_s. State which Planck mass (reduced or not) each formula uses and whether the
  proposals are consistent with each other and with the stored finite-range result's horizon arithmetic.
- The claim that no stored premise or result selects a reading is labelled how? It must be "argued" unless the
  proposal proves it over a stated list. Look yourself for a stored selector: the time-shift result
  (synthesis.adiabatic-deposit-modulation-is-a-time-shift), standard-model.dating-descent (both readings of the
  join), the field-space premise, the tame-wall and Hadamard-deposit premises, P1. If you find one, the verdict
  changes: say so.
- Is the infrared statement (index -1 is not admissible on an unbounded slice) stated correctly and at the right
  strength? Is anything said about a ceiling on T_d stated as conditional and rough, with no low-multipole
  analysis claimed?
- Does the proposal misdescribe any stored result (the finite-range bound, clause (iv) of the quasi-free result,
  the holographic result's conversion)? Read those stored texts.
For 2:
- The formula for the white term S_E(0) and "zero exactly for pure stationary states": check the proof and find
  the precise class (gauge-invariant, homogeneous, quasi-free; what "stationary" means).
- The Cl(3,0) trace identity for the Weyl field; the exact filled-ball integrals (recompute the leading
  coefficient k_F^4 k/(8 pi^2) and the first correction by your own integration).
- The conditional statement: n_s = 1 for the filled ball under the stated conversion hypothesis, reported as a
  miss with its sigma; the amplitude 3 H_d^2/(8 pi^2 M_P^2) and what it is short by; no tuning to the measured
  tilt anywhere, and nothing in the title, one-liner or lay level that reads as a mechanism.
- The statement about the stored deposit (mixed, deep in the white regime; purification by partners): proved or
  argued, and labelled accordingly?
For 3:
- The hypothesis (a relabelling group transitive on unordered pairs) and the conclusion (covariance is two
  numbers; on a slice, white noise plus a k = 0 term, all k dependence in the embedding's form factor). Try to
  build a counter-model. Check the fermionic statements and the statement about similarity-invariant kernels.
- Is the reading drawn from it (what the pre-metric escape of the finite-range result then needs) stated as
  argued?
For 4:
- The counting bound and the energy-budget step; each conditional conversion; the criterion "quanta below the
  Planck mass" must be visibly a hypothesis and not a stored premise; the title must not claim more than the
  flat-slice readings.
For 5:
- Compare with the stored version 4: every stored file kept, every stored check function kept, no inequality or
  number of clauses (i) to (iv) changed, the amendment entry accurate, and the new conditional wording correct
  (which hypothesis the comparison with A_s and the words "index 3" need).
Across all five:
- The three readings carry different letters in different proposals. List the dictionary and say which single
  convention the store should use; flag any place where two proposals disagree on a coefficient, an index or a
  number.
- House rules: statements and proofs in geometric algebra and Gauge Theory Gravity language (flat background,
  gauge fields; a metric reading only as a labelled parenthetical) where the algebra does the work, else an
  `outside_ga` declaration with a reason; exact arithmetic in checks; no em dashes; never "honest"/"honestly";
  never "load-bearing"; Q(v) for the square of a vector; macros only from store/notation.yaml; no agent, run or
  method names in store text; literature quoted from memory flagged as such and not used in a proof step.
- Transport-essential, transport-convenient or transport-absent must be stated and be right (expect
  transport-absent).

For each proposal:
1. Read the formal statement and the proof; check every step; confirm the cited store entities
   (`derivations.uses`) say what the proof needs at the pinned version.
2. Read the check: does it test the claim as stated or something weaker? Make at least two targeted perturbations
   and confirm the check fails. Recompute one key number by your own route.
3. Hunt: hidden hypotheses; overclaiming in title, one-liner or lay levels; "proved" where the argument is only
   argued; misquoted literature; circularity; standard results presented as new; conditions missing from titles.
4. Verdict, one of: SOUND; SOUND WITH FIXES (exact fixes); OVERSTATED (give the true weaker statement, at every
   level); WRONG (counterexample or failing step); UNCLEAR (what would decide it).

Write your report to `colony/runs/2026-11-16-spectrum/verify/R1.md` as you go (one section per proposal: verdict
first, then what you checked and how, then fixes), plus closing sections "Overlaps and conflicts" and "The
physics, in one paragraph: is the slicing gap real?". Your final reply is a one-table summary (id, verdict,
one-line reason) followed by those two sections. Your final message is read by the orchestrator.
