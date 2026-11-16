# Referee brief, run 2026-11-16-anomaly

You are an independent referee for proposals that AI agents filed against the Physics Graph store (a claim graph
of a research programme on Clifford-algebra zero divisors as a bridge between general relativity and quantum
theory). LAB = /home/claude/phys-graph. Work only there and in your scratch folder
colony/runs/2026-11-16-anomaly/verify/work-<your-name>/. Never spawn agents, never commit, never edit store/ or
proposals/. Read colony/BRIEF.md (role: referee) first.

Blindness: you have NOT seen the agents' reasoning and must not look for it. Do not read
colony/runs/*/findings/, colony/runs/*/work/, RUN.md or LEADS.md of this run, or the other referee's report. Judge
each proposal on its own text, its premises in the store and its check.

Tools: proposals in proposals/<id>/ (entity.md, proof-main.tex, check.py);
`python3 colony/labcli.py get_claim|get_proof|get_open_problem|search_claims|find_text|cone|conventions|notation '<json>'`
(about 10 seconds a call; stored entities can be read directly in store/claims/<id>/);
`python3 colony/runcheck.py proposals/<id>/check.py`; lib/GA.py (exact Clifford algebra over Fractions; no sympy;
numpy for exploration only, never evidence). The orchestrator has run the evidence layer (check4) on every
proposal; logs in colony/runs/2026-11-16-anomaly/verify/check4/<id>.log (SUMMARY.txt has the exit codes); read
them instead of rerunning check4. Web search and fetch are allowed, and expected, for checking literature at
source. Run at most one heavy process at a time (the machine has 2 CPUs and another job is running).

For each proposal: check every proof step; confirm each cited store entity says what the proof needs at the pinned
version; read the check and break it with at least two targeted perturbations; recompute one key number by your own
route (your own script, not the proposal's code); hunt hidden hypotheses, overclaiming in title, one-liner or lay
level, "proved" where only argued, literature cited from memory, circularity, standard results presented as new,
conditions missing from the title. Say for each result whether it is transport-essential, transport-convenient or
transport-absent, and whether the proposal says so correctly. Say whether the proposals, taken together, meet the
success clause of the open problem they address (read it with get_open_problem), or only make progress.

Verdict per proposal: SOUND, SOUND WITH FIXES (list the exact fixes), OVERSTATED (give the true weaker statement),
WRONG (give the counterexample), UNCLEAR (say what decides it). Write colony/runs/2026-11-16-anomaly/verify/<your-name>.md.
Your final message: the verdicts in one line each, then the most serious finding per proposal, under 400 words.

## Referee R1: three proposals on op.strong-cp and op.matter-asymmetry-origin

1. synthesis.colour-angle-fixed-by-no-stored-conjugation-and-relaxed-by-no-stored-field
2. synthesis.phase-of-the-quark-mass-determinant-on-the-covariant-completion
3. synthesis.conditional-inheritance-of-b-minus-l-and-the-conversion-coefficient-as-a-gram-ratio

Specific points to settle:
A. In 1, the sign statements: is the grade-four part of the colour field square invariant under the stored CPT
   conjugation as that conjugation is stored (check the stored entity, not the proposal's paraphrase), and is
   "only orientation-reversing maps reverse it" a theorem or a check on instances? "Fixed by no stored conjugation"
   is a statement about everything stored: is it a proof over a named, finite list of stored premises, or a search?
   Is the list complete (look for stored conjugations, reversals and premises it omits)?
B. In 1, the colour coefficient of phase symmetries: the claim is that with the two family matrices coupled as
   stored and both invertible, every phase symmetry (doublet mixing and family-dependent charges included) has
   colour coefficient zero. Check the argument that a nonzero coefficient forces a determinant to be a single
   monomial. Try to build a counterexample: a charge assignment on quarks and doublets, compatible with the stored
   couplings and nonzero masses for all six quarks, with nonzero colour coefficient. What does the claim assume
   about scalars other than the two doublets (the store's chain has other breaking fields: do any carry a phase
   that could pair with colour)? Is "relaxed by no stored field" then proved or argued?
C. In 1, "the potential's axial phase is unbroken at the vacuum, so there is no axion", and "the second invariant
   is unconstrained": verify against the stored rung-field entities at their pinned versions.
D. In 1 and 2, the sentence that the flag is not the only CP-violating datum once the stored quark-stage phase is
   counted: correct as a statement about the store? Does either proposal contradict a stored result or the other
   proposal? Do 1 and 2 duplicate each other anywhere?
E. In 2: the bijection off the balanced frame. Does rotating one mass matrix by a unit phase stay inside every
   stored constraint (symmetric pairs, the stored sum rules, the one-type stages), so that "not fixed" is proved
   and not just plausible? Then the quarter-turn clause: state exactly its hypotheses and recompute it yourself on
   exact 3 x 3 matrices. Is it a statement about three families or about a light block? Is the "real" determinant
   allowed to be negative, and does the proposal say plainly that a half turn of the physical angle is not zero
   and what the sign depends on? Is anything about loop corrections or the bare angle claimed beyond what is shown?
F. In 3: the classification of the bilinear forms on the sixteen invariant under colour and charge (ten are
   claimed, two changing B - L): recount them yourself. Which of the six named hypotheses of the inheritance are
   stored premises, which are new, and is the word "proved" attached only to the algebra? Recompute the four
   values of the coefficient (28/79, 8/23, 12/37, 10/31) by the textbook chemical-potential method, independently
   of the Gram-ratio form, and check the general formulas at two further (N_f, N_H). Check the quoted literature
   at source (Harvey and Turner 1990; Khlebnikov and Shaposhnikov 1996; the lattice freeze-out temperature). Is the
   doublet count "one light doublet on the working branch" supported by stored entities? Recompute the quoted range
   of B - L per unit entropy. How much of the proposal repeats clause (vi) of
   synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them?

## Referee R2: two proposals on op.order-four-anomaly-and-sixteen

1. synthesis.spectral-asymmetry-on-real-projective-five-space-from-monogenic-polynomials
2. synthesis.order-four-structure-on-real-projective-walls-and-the-signed-count-modulo-sixteen

Specific points to settle:
A. In 1, redo the algebra yourself in the six-space's Clifford algebra with lib/GA.py at low degree: the dimension
   of the monogenic homogeneous polynomials of each degree (which spinor module, of which dimension, and how that
   matches "per Weyl component"), the spherical Dirac operator and its two families of eigenvalues, with the
   store's sign conventions (conventions tool). Is the general-degree statement proved or only checked to degree
   three?
B. In 1, the lift of the antipodal map: its square, the claim that its product with the store's omega is an
   involution, how it acts on each eigenspace, and the sign and normalisation of the result (eta = 1/8 in absolute
   value for which bundle; xi = 1/16 per component with which definition of xi and which treatment of zero modes).
   Compare the value with the literature at source (Hsieh, arXiv:1808.02881; Garcia-Etxebarria and Montero,
   arXiv:1808.00009; Tachikawa and Yonekura). Does the two-fold choice of structure change the conclusion?
C. In 1, the analytic step (completeness of the restricted monogenics; the Abel sum equals the continued value at
   zero): is the argument in the proof text correct and complete, and is status "proved" right for the entity with
   that clause inside it, or should the clause be marked argued or the entity split? Is the outside_ga declaration
   accurate?
D. In 2: "the signed count of omega is well defined modulo 16 on its class modulo the Standard Model group, 0 on
   sixteen components and 1 on fifteen": what exactly is defined and proved, and does the modulus 16 come from the
   store, from proposal 1, or from the literature? The wall statements: on a real projective five-space wall
   exactly one side needs an order-four twist, supplied by the jump plane's pseudoscalar; the lens space L^5(4)
   carries no such structure. Recompute the characteristic classes yourself. Two classical facts are used that the
   store does not hold: name them, check them at source, and say whether status "proved" survives with them
   unimported.
E. Together: the problem's success clause has three branches (vanishes exactly for sixteen; does not constrain the
   content; the reading is excluded). Which branch do the two proposals establish, at what level (proved, argued,
   conditional on which literature statement)? Is "constrains no stored stage" proved? Do the two proposals
   overlap or disagree in sign, normalisation or structure?
