# Run 2026-11-07-consistency: brief for the GA rewriters (tensor, forms, matrices)

Leon (7 November 2026): results and proofs in geometric algebra wherever possible; he chose to rewrite every
entity that still uses tensor indices, differential forms or explicit matrices. You act for Leon as maintainer.
LAB = /home/claude/phys-graph (branch consistency-and-ga). Never commit, never spawn agents, never kill
processes; fifteen agents share 2 CPUs (at most three tp check runs in all).

Read first: store/conventions.md in full (especially "The language: geometric algebra", "The imaginary units"
and the unit principle), docs/gtg-dictionary.md (the store's GTG transcription), docs/ALGEBRA_CORE.md,
colony/BRIEF.md (store model, check rules), colony/runs/2026-11-07-ga-units/SWEEP.md (bookkeeping only).

Your entities: colony/runs/2026-11-07-consistency/ga_<kind>.txt (id, folder, which notations were detected).
You own them for this run; readers will send you issues on them in ga-issues-*.md files (read those at the
start and again before you finish, and address each).

## How to rewrite
- Gravity: Gauge Theory Gravity on flat spacetime, gauge fields hb and Omega (docs/gtg-dictionary.md); the
  field strength R(a ^ b) in place of Riemann components; covariant derivatives as D = hb(nabla) + Omega
  terms; no "curved spacetime". Christoffel symbols, g_{mu nu}, R_{mu nu rho sigma} appear only as a labelled
  reading "(in components: ...)" after the GA statement, or not at all.
- Forms: a p-form is a p-vector field; d is nabla ^ (or D ^ in GTG); the Hodge star is duality with the
  pseudoscalar; integrals over surfaces with the directed measure.
- Matrices: a linear map is written as a Clifford element or an outermorphism acting by the geometric product;
  Pauli and Dirac matrices become the vectors of Cl(3,0) and Cl(1,3) (Hestenes); a matrix representation stays
  only as a labelled reading. Leave Gram matrices, mass matrices, rate tensors and explicit numerical matrices
  that are the point of the result (the conventions allow them); a cross product becomes the outer product's
  dual.
- Imported Facts: restate in GA; the source's form goes to extraction.source_formal with a sentence on the
  translation; keep the status imported.
- The mathematics must not change. Where the rewrite is more than notation (a different but equivalent form),
  verify the equivalence exactly with lib/GA.py in your scratch and say so in the extraction note. If a GA form
  is not exact or not possible (the result is about components or matrices as such), leave it and declare
  `outside_ga: {kind: bridge | imported | other, why: ...}` with the precise reason; list it in your report.
- Units by the unit principle; never a bare imaginary unit.

## Bookkeeping
version + 1 relative to the current version (once per entity in this run), credit entry {name: Claude Opus
5.5, role: GA rewrite (<what>), version: <new>, source: maintainer pass 2026-11-07 (consistency)}, extraction
note maintainer_pass_ga_rewrite, every file kept, no change of status, links, pins, assumes or ledger. Do not
edit check.py unless a check's premise() calls must follow a citation change (then runcheck it).
Validate with python3 -m tp check --store store --layers 1,2,3 --keep-going --author leon 2>&1 | grep -F -f
<your id list>, and galang.scan on each entity (no unexcused stand-in left).

## Report
colony/runs/2026-11-07-consistency/ga-<kind>.md: one line per entity (old -> new version, what was rewritten,
what stays and why), "Not rewritten" with reasons, "Possible errors found", the reader issues you addressed.
Final reply: counts and the Not-rewritten list, under 300 words.
