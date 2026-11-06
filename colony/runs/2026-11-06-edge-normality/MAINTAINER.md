# Maintainer pass after run 2026-11-06-edge-normality (acting for Leon, the maintainer)

LAB = /home/claude/phys-graph. Leon has accepted all five proposals of this run (now in store/ via `tp accept`):
- synthesis.geometric-modular-conjugations-on-a-generator-give-the-null-ground-state (field-level CGMA, A)
- synthesis.modular-data-on-a-generator-fix-neither-the-translation-lift-nor-the-sign-of-i (net-level no-go, B)
- synthesis.blade-square-signs-f2-quadratic-form
- synthesis.nilpotent-steps-derivative-exponential-and-boost
- note.one-relation.two-presentations-differ-over-the-integers
Read colony/runs/2026-11-06-edge-normality/DECISIONS.md (Leon's decisions), verify/P.md and verify/G.md (referee reports,
for the requested notes and imports), findings/fixes-*.md. Edit store/ directly. Never touch the user's computer; never
spawn agents; never commit.

## Rules (as colony/runs/2026-10-22-toe/MAINTAINER.md)
Read CONTRIBUTING.md and store/conventions.md; copy the format of existing entities of the same kind (postulates: grep
`status: postulate`; imported Facts: grep `status: imported`; open problems: store/open_problems.yaml header). Changing an
existing entity: version + 1, keep every file in its folder (orig-proof-main.tex in particular), add a `maintainer_pass` (or
`correction`) entry under `extraction` with `by: maintainer-2026-11-06`, date '2026-11-06', and one sentence on what changed
and why; keep `proposed_by`. New entities: copy what existing maintainer-made entities use; `ai_involved: 'yes'`. New
imported Facts state the source precisely; extraction note says "cited from memory, not checked against the source" unless
verified (WebSearch/WebFetch allowed; the referees verified some, see below). House style: no em dashes; never
"honest"/"honestly"; never "load-bearing"; Q(v) for the square of a vector; macros only from store/notation.yaml; no mention
of agents, colony or runs in store text (changelog `by:` fields excepted). Exact arithmetic in any check you touch; after
changing a check run runcheck.py then check4.py on it (one at a time). Validate with
`python3 -m tp check --store store --layers 1,2,3 --keep-going --author leon 2>&1 | tail -40` and fix every error or new
warning on entities you touched. Do NOT run tp repin, tp lock, tp build or the full check.

## Edits
1. synthesis.n-plus-null-ground-state (postulate; Leon's decisions 1-3; do not change its status):
   (a) Lift: the affine null translations act on the fields by parallel transport along the generator (zero flat
       connection); say this excludes the Fermi-sea states, citing the net-level no-go entity.
   (b) Record the stationarity-free equivalent form: within gauge-invariant quasi-free states, field-level geometric
       modular action at cuts whose doubled differences generate a dense subgroup, with eta = -1, is equivalent to the
       ground-state clause (cite the field-level CGMA entity), as the KMS form was recorded on 2 November. (N+) stays the
       postulate.
   (c) Name the residual datum: the orientation of the imaginary unit relative to time (null vacuum versus the filled
       positive-energy sea) is assumed by (N+); the series does not fix it (Leon did NOT adopt i = I_4).
2. store/open_problems.yaml, op.r-premises-external: keep status `reformulated`; update `known` (append a dated paragraph,
   6 November) with what the two physics entities establish, and update `attack`/`success` so the remaining target is:
   derive field-level geometric modular action (or the ground-state clause) from a principle of the series, and the sign
   datum; net-level routes are closed. Add the two entities to `entities`. Follow referee P's "Effect on the open problems".
   op.null-positivity-curved-horizons item (ii): append the same restatement (a further state condition that gives the
   positivity with no stationarity or conformal symmetry, posed but not derived on the eternal hole; net-level conditions
   cannot give it).
3. Imported Facts the accepted entities rely on (routine; create as imported Facts, or add a clause to an existing Fact
   where the referee suggested it):
   - Buchholz, Florig, Summers, Lett. Math. Phys. 49 (1999) 337 (arXiv math-ph/9909003), Props 3.5 and 3.6 and the remark
     that CGMA alone does not give a ground state: verified by two agents.
   - Yafaev, Hankel sign criterion, arXiv:1303.4040 (Anal. PDE 8 (2015)): abstract verified; Theorem 4.7 not verified.
   - Loewner's theorem (operator monotone functions are Pick functions): from memory.
   - Purity criterion for gauge-invariant quasi-free CAR states (pure iff the symbol is a projection; Araki 1970/71): from
     memory; referee P suggested a clause of synthesis.imported-powers-stormer-takesaki-disjointness.
   - Brunetti, Guido, Longo 1993 and Baumgaertel, Jurke, Lledo 2002 (field-level twisted modular conjugation of the chiral
     Fermi field): from memory.
   - Ovsienko arXiv:1601.07664 (2016) and Elduque, Rodrigo-Escudero arXiv:1801.07002 (Adv. Appl. Clifford Algebras 2018):
     verified by referee G.
   Then wire each accepted entity's derivation/imports to the Facts it uses, if the schema expects that (check how existing
   entities cite imported Facts), without adding `assumes` edges.
4. Cross-reference A's and B's entities to each other with \claimref now that both are stored (they currently cite each
   other in plain text).
5. Anything else the referees asked for as notes or wording on stored entities (verify/G.md: a wording note on
   one-relation.two-presentations is now the accepted note; nothing more unless G.md lists it).

Write colony/runs/2026-11-06-edge-normality/maintainer.md: every entity created, changed or retired, old -> new version, one
line each; dependants whose content might be affected; anything not done and why. Your final reply is that file.
