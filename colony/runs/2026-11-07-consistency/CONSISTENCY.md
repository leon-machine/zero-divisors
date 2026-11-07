# Run 2026-11-07-consistency: brief for the readers (R01-R12)

Leon (7 November 2026, 13:11): "check the whole series for consistency and ensure results/proofs are in GA
where possible". He chose a full read by subject. You are one of twelve readers acting for Leon as maintainer.
LAB = /home/claude/phys-graph (git branch consistency-and-ga). Never commit, never spawn agents, never kill
processes. Fifteen agents share 2 CPUs: run a tp check at most three times in all, never two heavy processes at
once.

## Read first
colony/BRIEF.md (store model), store/conventions.md in full (notation, normalisations, the unit principle,
the known limits), docs/gtg-dictionary.md, colony/runs/2026-11-07-ga-units/SWEEP.md (bookkeeping only).

## Your entities
colony/runs/2026-11-07-consistency/read_<G>.txt (one id per line; claims, objects, notes and predictions of
your subjects). Read every one in full: the four levels, every proof file, the derivations (uses, assumes,
pins) and the extraction notes. Batch reads in one Python process:
  cd /home/claude/phys-graph && python3 - <<'PY'
  import sys; sys.path.insert(0, '.')
  from tp.mcp_server import Lab
  lab = Lab('store')
  for eid in open('colony/runs/2026-11-07-consistency/read_<G>.txt').read().split()[:15]:
      print(lab.get_proof(id=eid))      # statement, proof steps with citations, premises, holds_given
  PY
(or read store/claims/<id>/entity.md and proof-main.tex directly; `digest(subject)` gives a subject in
dependency order). Read in dependency order where you can, so a premise is read before its users.

## What to check
1. The proof proves the formal statement as written (quantifiers, hypotheses, signs, constants), and each step's
   citation says what the step needs at the pinned version.
2. Contradictions: two results of your subjects that cannot both hold, or a result that contradicts a premise it
   cites; a status that is stronger than the proof (a "proved" result whose proof is only argued).
3. Conventions: signatures, the curvature sign (the store's, one stated flip against Doran-Lasenby), n0.ninf =
   +1 or -1 (both used; each paper's own), the boost bivector's two signs (B = n gamma0 vs B_k = gamma0 n), the
   chirality halves (T09 against T12), KMS signs, the unit principle (I4, J, I5, I7, I6, hat-I: an entity using
   two units says which acts where). Flag every place where an entity mixes conventions without saying so.
4. Notation clashes: one symbol with two meanings in one entity, or a symbol used against its stored macro.
5. Duplicates: the same result stated twice under two ids (say which is better).
6. Stale wording: a title, one-liner, lay or technical level that no longer matches the formal statement (for
   example after a restatement or the unit pass).
7. Overclaiming in plain levels relative to the formal level; hypotheses the one-liner drops.
8. Language: anything not in geometric algebra where GA does the work (gravity in Gauge Theory Gravity on flat
   spacetime with gauge fields hb and Omega, never "curved spacetime"; forms, matrices, tensor indices). The
   ids in colony/runs/2026-11-07-consistency/GA_OWNED.txt belong to three GA rewriters: do not edit them; record
   their GA issues and any other issue for them in ga-issues-<G>.md. For other entities, rewrite small stand-ins
   yourself only if it is a pure notation change.
9. Known open items to settle where they fall in your subjects (verify by exact computation with lib/GA.py in
   your scratch before stating anything):
   - synthesis.quadratic-flows-cannot-thermalise-descent: coherence-phase sign, formal (ii) against the proof;
   - synthesis.boost-evolution-on-generators-is-one-unitary-group: the one-particle Hamiltonian sign;
   - synthesis.real-structure-breaks-source-stabiliser-to-z2 (ii): an intermediate expression;
   - synthesis.hadamard-dirac-states-scale-to-the-flat-massless-vacuum-at-every-point-of-a-gravitational-field:
     proof step 7 sign and its regulator (+eps^2 against -eps^2/2 elsewhere);
   - the sign of I6 on CS: correspondence.incidence-relation-chart and
     note.correspondence.what-factor-i-what-remains-conventional say I6 acts as -(unit) on CS, against the twistor
     entities' convention line;
   - synthesis.operator-join-ordering-constants keeps I6 on a space other entities write with I4.

## What you may fix, and what you list
Fix in place (maintainer bookkeeping below): wording, typos, wrong clause numbers or citations, stale titles and
plain levels, notation clarifications, missing "which unit acts where" sentences, and a sign or constant slip in
a proof or technical level that an exact computation shows wrong while the formal statement is right (record the
computation in the extraction note). Do NOT change a formal statement's mathematics, a status, an assumes edge,
a pin target or a ledger, and do not retire anything: list each such case under "For Leon" with the evidence and
the exact proposed fix. Cross-subject conflicts (a result of yours against one in another subject) go in
xsubject-<G>.md with both ids and the evidence; do not edit the other subject's entity.

## Bookkeeping for each entity you change
version + 1 relative to its current version (once per entity in this run), a credit entry
`{name: Claude Opus 5.5, role: consistency pass, <what>, version: <new>, source: maintainer pass 2026-11-07
(consistency)}`, an extraction note `maintainer_pass_consistency: {by: maintainer-2026-11-07, date:
'2026-11-07', note: <one sentence>}`, every file kept, house style (no em dashes; never "honest"/"honestly"/
"load-bearing"; Q(v) for the square of a vector; declared macros only). A change to the one-liner, lay level or
extraction alone needs no version bump. No bare imaginary unit (the language check refuses one).
Validate: python3 -m tp check --store store --layers 1,2,3 --keep-going --author leon 2>&1 | grep -F -f
colony/runs/2026-11-07-consistency/read_<G>.txt ; fix every error or warning on entities you changed.

## Report
colony/runs/2026-11-07-consistency/consistency-<G>.md: Fixed (one line per entity: old -> new version, what),
For Leon (each with evidence and proposed fix), Duplicates, the known open items you settled, and counts.
Final reply: the counts, the For-Leon list and the cross-subject items, in under 400 words.
