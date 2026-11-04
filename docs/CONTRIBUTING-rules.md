# Contributing to the Physics Graph

The store is the source of truth for the Transport Papers' results. Anyone can
propose a result, evidence, a question or an edit, working alone or with an AI.
Only reviewed changes reach the published graph. The site's Contribute page
(`#contribute`) says the same for readers; this file is the full rule set.

## The route

1. **Get a copy and connect your AI** to the MCP server (below).
2. **Read before writing.** The agent should call `conventions` first, then
   `list_open_problems` and `get_open_problem` for somewhere to start, and
   `get_claim`, `get_proof` and `cone` to read what a result rests on.
3. **Write each new result as a folder** under `store/claims/<id>/` (or
   `objects/`, `predictions/`, `questions/` for those kinds): `entity.md`, a
   proof file, and a `check.py`. A result that needs new premises brings their
   folders too.
4. **Check it yourself.** `validate_draft` runs layers 1, 2 and 3 (and 5 on
   request) against a temporary copy of the store and reports every finding the
   draft introduces, including findings it causes on other entities. Then run
   the evidence locally: `python -m tp check --store store --layers 4`. The MCP
   server never runs code.
5. **Open a pull request** that adds the folders. The checks in
   `.github/workflows/check.yml` run the tests and all six validator layers,
   with the toolkit and rules taken from the base branch, and run layer 4 in a
   container with no network and the repository mounted read-only. A failing
   check blocks the merge. A maintainer reviews and merges.

`propose_claim` validates a draft and, if it is clean, files it under
`proposals/<id>/` in the same copy, for a maintainer working there to accept
with `python -m tp accept <id>` (which validates layers 1 to 4 again). It sends
nothing anywhere. From outside the repository, the pull request is the way in;
a `proposals/<id>/` folder can be moved into `store/claims/` for it unchanged.

## Connecting an AI

Python 3.11 or later, from the repository folder:

    pip install pyyaml jsonschema          # scikit-learn too, for meaning-based search

Claude Code:

    claude mcp add --env PYTHONPATH="$PWD" physics-graph -- python -m tp.mcp_server --store "$PWD/store"

The Claude desktop app, or any client that runs stdio MCP servers:

    "physics-graph": {
      "command": "python",
      "args": ["-m", "tp.mcp_server", "--store", "/path/to/phys-graph/store"],
      "env": {"PYTHONPATH": "/path/to/phys-graph"}
    }

On Windows, `register_mcp.ps1` registers the server with the desktop app.
The tools are listed, with their arguments, by the server itself and on the
site's Contribute page; `tests/test_mcp.py` keeps the list in README.md in step
with the server.

## What every entity needs

- `id`: a dotted slug naming the idea, never a paper number. Retired ids
  (`store/tombstones.yaml`) can never be reused.
- `kind`, `status`, `version` (1 for a new entity), `title`, `subject` (one of
  `store/subjects.yaml`).
- `proposed_by` (`kind: human` or `ai`, with `author`) and `ai_involved`
  (`'yes'`, `'no'` or `'unknown'`). Both are mandatory. Quote the value:
  YAML reads a bare `yes` as true, and the validator rejects it (E116).
- `credit`: a list of `{name, role}`, naming each person and the AI model (with its
  version) and what each did. The names are shown on the result. An amendment keeps
  every entry already there and adds its own, each with `version:` set to the version
  it made (E603 if an earlier entry is dropped or altered, E604 if the version is raised
  with no entry for it; for maintainers these are the warnings W220 and W221).
- Its premises in `derivations` (`uses`, and `assumes` for postulates), each
  pinned to a version (`id@n`).
- Evidence in `checked_by`: a `check.py` function, a series verify script
  (`legacy`), a Lean proof, or `proof` (proof text only).
- The four levels: formal, technical, lay, one-liner. A level may be the word
  `pending`; the entity then cannot appear in documents at that level.
- `extraction.open_problem`: the problem's id, for work on an open problem.

`docs/example-contribution/` is a complete worked example that passes every
layer; `tests/test_contrib_example.py` keeps it passing.

## Rules for check.py

- Exact arithmetic only: integers and `fractions.Fraction`, no floating point.
- Import `GA` (lib/GA.py) and reach each premise only through
  `tp_premise.premise("id")`, which records the dependency.
- Each check function returns a bool and reports through `GA.check(label, ok)`.
- A check must actually test something: at least one perturbation of its
  integer literals must make it fail, and a check that survives most
  perturbations is flagged as weak.
- It runs in a separate interpreter under an audit hook that refuses network
  access, process spawning, writes outside a temporary folder, frame and gc
  inspection, and ctypes. The hook stops accidents; the container in CI is
  the boundary against hostile code.

## The six layers

| Layer | What it checks | Where it runs |
|---|---|---|
| 1 shape | schema, ids, the four levels, house style, safe LaTeX, declared macros | `validate_draft`, `tp check`, CI |
| 2 references | premises exist and are pinned to current versions, allowed link kinds, proofs cite what they use | `validate_draft`, `tp check`, CI |
| 3 whole store | no cycles, no claim stronger than its weakest premise, no contradiction between proved claims, no fitted prediction, staleness | `validate_draft`, `tp check`, CI |
| 4 evidence | runs check.py files and the series verify scripts, with the perturbation test | `tp check`, CI (container), `tp accept`; never over MCP |
| 5 meaning | near-duplicates, stated numbers against stored quantities | `validate_draft` on request, `tp check`, CI |
| 6 people | who may do what (below) | CI, by the pull request author's login |

Other rules the validator enforces:

- No circular reasoning, and no prediction fitted to the data it predicts.
- No file access, macro definitions or links in LaTeX (`\input`, `\def`,
  `\href` and the like).
- House style: no em dashes, no "honest"/"honestly", Q(v) for the square of
  a vector, every macro declared in `store/notation.yaml`.

## What the checks do not establish

- A check confirms a statement on exact cases; it does not prove the general
  statement. The proof does, and it is read at review.
- Lean evidence is recorded but not run: there is no Lean toolchain in the
  checks yet (W411).
- Layer 5's AI judge (statement against check, overclaiming, citations) is a
  hook that is off. Those comparisons are made at review.
- Every entity carries a trust level (`ai-proposed`, `ai-refereed`,
  `human-read`, `human-checked`, `published`), shown and filterable on the
  site. A new contribution starts at `ai-proposed` when an AI was involved.

## What only a maintainer may do

- Promote a core claim to proved, or change any status to imported or postulate.
  The same applies to new entities: a new imported or postulate entity, or a new
  proved claim in a core region, needs a maintainer.
- Add or remove an `assumes` edge (what the programme rests on).
- Declare a ledger class, or retire an id.

## Licences

Entity content: CC BY 4.0. Code (`tp/`, `lib/`, `tests/`, `site/`): MIT, as in
the series' `LICENSE-CODE.txt`.
