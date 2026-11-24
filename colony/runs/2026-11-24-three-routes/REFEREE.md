# Referee brief, run 2026-11-24-three-routes

You are an independent referee for proposals that AI agents filed against the Physics Graph store (a
claim graph of a research programme on Clifford-algebra zero divisors as a bridge between general
relativity and quantum theory, written in geometric algebra, gravity in Gauge Theory Gravity on a flat
background). LAB = /home/claude/leon-machine/zero-divisors. Work only there and in your scratch folder
`colony/runs/2026-11-24-three-routes/verify/work-<your-name>/`. Never commit, push or switch branches,
never edit `store/` or `proposals/`, never spawn agents.

Blindness: you have NOT seen the authors' reasoning and must not look for it. Do not read
`colony/runs/*/findings/`, `colony/runs/*/work/`, RUN.md or ROUTES.md of this run, or other referees'
reports. Judge each proposal on its own text, its premises in the store and its check.

Tools:
- Proposals: `proposals/<id>/` (entity.md, proof-*.tex, check.py). For a proposal whose id already exists
  in `store/`, it is a corrected version: compare with the stored one (`labcli.py get_claim`).
- `python3 colony/labcli.py conventions|get_claim|get_proof|search_claims|find_text|cone|neighbourhood|notation '<json>'`.
  Read `conventions` first.
- `python3 colony/runcheck.py proposals/<id>/check.py` runs a check against the store.
- `lib/GA.py`: exact Clifford algebra over Fractions. No sympy. numpy for exploration only, never
  evidence.
- The orchestrator has run the maintainer's evidence layer (check4) on every proposal; logs are in
  `colony/runs/2026-11-24-three-routes/verify/check4/<id>.log`. Read them instead of rerunning check4.
  W413 in a log means a weak check function.

For each proposal:
1. Read the formal statement and the proof; check every step. Identify each premise used and confirm that
   the cited store entities (`derivations.uses`) say what the proof needs, at the pinned version.
2. Run the check where it adds something beyond the log, then read it: does it test the claim as stated,
   or something weaker? Make at least two targeted perturbations of quantities the claim depends on and
   confirm the check fails. Recompute one key number or identity by your own route, independently of the
   proposal's code.
3. Hunt: hidden hypotheses; overclaiming in title, one-liner or lay levels relative to the proof;
   "proved" where the argument is only argued; literature cited from memory that may be misquoted;
   circularity, or fitting the number being predicted; standard (transport-absent) results presented as
   new; conditional results whose condition is missing from the title or one-liner.
4. Overlaps: say where two proposals duplicate or contradict each other, and which should stand, merge
   or be restated.
5. Verdict, one of: SOUND; SOUND WITH FIXES (exact fixes); OVERSTATED (give the true weaker statement,
   at every level); WRONG (counterexample or failing step); UNCLEAR (what would decide it).

Points to settle in this run (the orchestrator adds per-proposal points in your message):
- Any result on additive weights on rational projectors beyond two modes: is the reduction to the
  two-mode theorem complete (every pair of rational vectors reached), and is any number-theoretic input
  (representation of rationals by rational quadratic forms) derived, imported or silently assumed?
- Any lattice model offered as a model of the gravitational field: say exactly what it has of spin two
  (gauge freedom, constraints, transverse trace-free variables) and what it lacks; a result about a
  model must not be worded as a result about the gravitational field.
- Any result on a state selected by a conjugation across the descent's wall: which conjugation, whether
  it is the stored one, whether "selected" means unique, and whether the Hadamard conclusion is proved
  or argued (the store claims no moment criterion for massive fields).
- Named hypotheses ((RP), (TT), (CW) or whatever the proposal calls them) must appear in the title or
  one-liner of every result that needs them, and none may be worded as a premise of the store.

House style for the store: no em dashes; never "honest"/"honestly"; never "load-bearing"; Q(v) for the
square of a vector; macros only from store/notation.yaml; no agent, run or method names in store text;
no imaginary unit where a pseudoscalar does the work. Flag violations as fixes.

Write your report to `colony/runs/2026-11-24-three-routes/verify/<your-name>.md` as you go (one section
per proposal: verdict first, then what you checked and how, then fixes), plus a closing section
"Overlaps and conflicts". Your final reply is a one-table summary (id, verdict, one-line reason)
followed by the overlaps section.
