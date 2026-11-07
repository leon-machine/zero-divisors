# Bridge survey brief (read in full before starting)

You are one of three bridge-hunters in a read-only survey of the Transport Lab, a claim graph of
Leon Butler's Transport Papers (Clifford-algebra zero divisors as a bridge between general
relativity and quantum theory; gravity as Gauge Theory Gravity on flat space with gauge fields
hb and Omega). Each hunter takes one open problem. The goal is cross-pollination: results in
OTHER subjects of the graph that could supply a premise, a technique, an obstruction, a
counter-model or an independence argument for your problem, or two results that are one
structure read two ways. Nothing is filed: this is a survey. Do not edit anything under
`/home/claude/phys-graph` and do not run check4, validate_draft, propose_claim or tp check.

## The lab
- Clone: `/home/claude/phys-graph` (`store/` holds the entities). Read `colony/BRIEF.md` there for
  the store model only (the attacker/referee procedure in it does not apply to you).
- Tools: every lab MCP tool. `labcli.py` reloads the store each call (about 8 seconds), so batch
  your lookups in one Python process instead:
  ```
  cd /home/claude/phys-graph && python3 - <<'EOF'
  import sys, json; sys.path.insert(0, '.')
  from tp.mcp_server import Lab
  lab = Lab("store")
  r = lab.search_claims(query="...", limit=10)
  print(json.dumps(r, indent=1, default=str)[:4000])
  EOF
  ```
  Methods: conventions(), get_open_problem(id), get_claim(id, notes_text=False), get_proof(id),
  get_claims(ids, fields), search_claims(query, subject, tag, status, limit),
  find_text(pattern, regex, include_notes, limit), cone(id, direction='past'|'future', limit),
  neighbourhood(id, k), list_entities(subject, tag, status, kind, sort_by, descending, limit,
  fields), list_subjects(), list_tags(), digest(subject, level, limit), trail(subject).
  Truncate printed output; never dump whole digests into your context.
- The full records of all 32 open problems are JSON files beside this brief
  (`/tmp/claude-0/-home-claude/23cbb9be-73ca-5537-8211-47496476158a/scratchpad/bridges/op.*.json`):
  statement, why, known, attack routes, success criterion, linked entities, work in store. Read
  yours in full first, and skim the others' `known`/`attack` fields where they touch yours.
- Earlier run working history: `colony/runs/2026-11-06-edge-normality/` (REPORT.md, findings/)
  and `colony/runs/2026-10-22-toe/REPORT.md`. Do not re-propose what is settled there.

## Method
1. Orient: your problem record, its linked entities (get_claim), their past and future cones,
   what exactly is open (the residual after everything already proved).
2. Name the problem's key objects and structures abstractly (e.g. "a positivity condition on a
   one-parameter group", "a grading by a Clifford element", "a state selected by a fixed
   point"). Then search for those structures in every other subject, not only by the
   problem's own vocabulary. `list_subjects()` gives the map; walk at least six subjects
   outside your problem's own.
3. For each candidate bridge, test it by lookup: read the statement and proof of the far
   result, check its premises (holds_given) so a bridge does not smuggle in the premise you
   are trying to derive (circularity: check with cone), and decide whether it actually
   supplies what is missing. A bridge that only restates the gap is rejected.
4. Grade each lead: STRONG (the far result supplies a precise missing step; say what remains
   to prove), PLAUSIBLE (the structures match; a definite computation would decide it, name
   it and its kill condition), WEAK/REJECTED (say why in one line). Also record any
   obstruction or independence evidence: a far result showing the problem cannot be solved
   on its present premises is as valuable as a route.
5. Where a cheap exact computation (Fractions and `lib/GA.py`, in your scratch folder) would
   decide whether a lead is worth pursuing, you may do it, but keep it short; label it
   computed, and do not go further than a screening check.

## Standards
Candour over enthusiasm: say plainly when nothing in the graph helps. Label every statement
proved (in store), computed (by you, exact), argued, or speculative. Separate imported results
from the series' own. Flag any literature you cite from memory. Say for each lead whether it
would be transport-essential, convenient or absent. Watch for circularity and for fitting the
number being predicted. All mathematics stated in geometric algebra (multivectors, rotors,
outermorphisms; gravity in GTG on flat space; never "curved spacetime"); other formalisms only
as labelled parenthetical readings. House style in your report: no em dashes; never the words
"honest", "honestly" or "load-bearing".

## Output
Write `/tmp/claude-0/-home-claude/23cbb9be-73ca-5537-8211-47496476158a/scratchpad/bridges/<your-problem-id>.md`:
1. The residual: what exactly is still open, in three to five sentences, with entity ids.
2. Leads, best first: for each, the two (or more) entity ids, the subject it comes from, what it
   supplies, what remains, grade, pre-registered kill condition for the deciding computation,
   ledger (essential/convenient/absent).
3. Obstructions and independence evidence found.
4. Links to the other two problems in this survey (op.hypothesis-s, op.r-premises-external,
   op.deposit-state-is-hadamard) and to any other open problem.
5. Rejected candidates, one line each.
6. Subjects walked.
Keep it under about 1800 words. Your final message back should be a 200-word summary of the
top three leads with grades and entity ids.
