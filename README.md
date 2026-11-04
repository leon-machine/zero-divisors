# Transport Lab

A store of granular, verified claims covering the whole Transport Papers
series (T0 to T17, T14a, T14b, T14c, the companion notes and the field-theory
note "One Complex Unit"), organised by subject
rather than by paper. Documents, the map, the prediction scoreboard, the
refutation record and the lab notebook are all generated from it. The papers
on Zenodo stay the frozen published record; this store is the living one.
The design document is "Transport Lab: Knowledge Store Design".
A result is in the graph only once it is in store/, with its proof and checks.
Releases are archived on Zenodo as "Zero Divisors: Physics Graph"; RELEASING.md says how a release
is made (merging a pull request is not a release).

## Layout

    store/              the source of truth: one folder per entity
      claims/<id>/      entity.md (front matter + four levels), proof-*.tex, check.py
      objects/<id>/     definitions
      predictions/<id>/ predictions with kill conditions and dated observations
      questions/<id>/
      notes/<id>/       remarks, worked examples and the papers' running text (settings):
                        commentary on results, used by nothing
      subjects.yaml     the subject tree the map and documents are organised by
      config.yaml       transport roots, house style, governance, legacy script folder
      notation.yaml     macro registry (from the papers' preambles)
      notebook.yaml     the lab notebook: pre-registered runs and their outcomes
      labels.yaml       every \label of the series and what now carries it (tp.notes)
      tags.yaml         the tag vocabulary: cross-cutting themes, several per result
      tombstones.yaml   retired ids, never reused
      .tp-lock.json     accepted state (written by `tp lock` after a merge)
    tp/                 the toolkit (Python 3.10+, needs PyYAML and jsonschema)
    lib/                GA.py (copy of the suite's) and tp_premise.py
    tests/              validator, document and MCP tests; every rule has a test that makes it fire
    recipes/            document recipes
    documents/<doc>/    stored documents: blocks, manifest, rendered .tex/.md,
                        audit, overrides, changelog, versions/vN snapshots, redlines
    proposals/          drafts submitted through the MCP server, awaiting `tp accept`
    build/              graph.json, store.sqlite, report.md (generated)
    site/               page templates and the built site (transport_lab.html)
    seed/               extraction inputs and reports, typing and prose instructions

## Commands (run from this folder)

    python -m tp check  --store store [--layers 1-6] [--author NAME] [--no-mutants]
    python -m tp build  --store store [--no-mutants]
    python -m tp lock   --store store
    python -m tp repin  --store store [--ids a,b]     re-confirm stale pins after review
    python -m tp doc    recipes/falling-in.yaml --store store
    python -m tp regen  falling-in --store store
    python -m tp audit  falling-in --store store
    python -m tp accept PROPOSAL_ID --store store            (after review; then tp lock)
    python -m tp.site                                  build site/transport_lab.html
    python -m tp.mcp_server --store store              MCP server over stdio
    python -m tp.gate   recipes/falling-in.yaml ../G00_transport_papers_guide.tex
    python -m tp.gate3  recipes/t02-regenerated.yaml seed/GATE3_T02.md
    python -m tp.references --suite .. --store store   rebuild the reference registry
    python -m tp.notes --suite .. --store store        extract remarks and examples, rebuild labels.yaml
    python -m tp.settings --suite .. --store store     store the papers' running text as setting notes
    python -m tp.recreate [--papers T01,T02]           regenerate papers from the store and gate them
    python -m tp.tags apply seed/tag_assignment_*.yaml write tag assignments into the store
    python -m tp.tags report                           tag counts and untagged results
    python -m unittest discover -s tests -t .

`--author` defaults to the `TP_AUTHOR` environment variable. Layer 4 runs the
series verify scripts (from the suite folder, `../..` relative to the store,
and the run folders under "Claude outputs" that `legacy_extra_dirs` in
store/config.yaml lists) once and caches the result by content hash in
`store/.tp-cache`. A legacy tag `id:A1.1` names a check by the identifier at
the start of its name, for runs whose checks carry no paper labels.

## The site

`site/transport_lab.html` is one self-contained page.

- **Universe**: every result as a point in a 3D ball, placed so that each sits
  next to what it rests on and what rests on it (see `tp/layout.py` for the
  mathematics and its measured quality). Colour is the subject, in five hue
  families. Choose a category to light it up and walk its guided trail;
  choose a collection (a paper of the series, or a generated document) to
  see where its results sit; click a point to read it with its statement,
  proof, machine checks, premises and dependants, its remarks and examples,
  and copy it for an AI. Drag the reader's left edge to widen it.
- **Documents**: the generated documents, readable in the page.
- **The record**: predictions with their kill conditions, the refutations,
  and the lab notebook.

The arrangement never depends on the papers: they are optional collections.
Trails are stored documents (`recipes/trail-<subject>.yaml`) with
AI-written prose that the audit checks against the claims.

    python -m tp.layout        recompute build/layout.json after the store changes
    python -m tp.site          rebuild the page

## The MCP server

Register `python -m tp.mcp_server --store <path to store>` as a stdio MCP
server, with this folder as the working directory (or with PYTHONPATH set to
it). CONTRIBUTING.md has the set-up for Claude Code and other clients. Findings
come in as pull requests (see CONTRIBUTING.md); nothing enters until the maintainer
has reviewed it.
Tools: conventions, notation, list_programmes, list_subjects, find_text,
list_papers, list_entities, get_claims, list_tags, list_open_problems,
get_open_problem, search_claims, get_claim, cone, neighbourhood, get_proof,
trail, digest, validate_draft, propose_claim, list_proposals, generate_doc,
regenerate_doc.
For an AI reading the store, `digest` returns a whole subject in dependency
order with statements, premises and proofs; `neighbourhood` and `trail` are
the quick ways to move around it.

- A draft is validated against a temporary copy of the store (layers 1, 2, 3
  and 5). Every finding the draft introduces is reported, including ones it
  causes on other entities. Evidence checks (layer 4) never run over MCP,
  because they execute code; they run when a maintainer reviews the proposal.
- `propose_claim` writes the draft to `proposals/<id>/` and nothing else; it
  enters the store only when a maintainer runs `tp accept`. Ids and proof file
  names are checked before anything touches the disk.
- `generate_doc` and `regenerate_doc` write only generated documents under
  `documents/` (and the recipe under `recipes/`), never the store.

## Security model

- Store text is checked for LaTeX that reads files, defines macros or makes
  links (`\input`, `\def`, `\href` and the like are refused, E111), because it
  is compiled by LaTeX and typeset on the site. The site escapes every value
  and runs MathJax with its safe extension.
- `check.py` files run in a separate interpreter under an audit hook that
  refuses network access, process spawning, writes and deletions outside a
  temporary folder, frame and gc inspection, and ctypes. The result line is
  marked with a per-run secret, so a check cannot print a forged pass. The hook
  stops accidents and casual misuse; it is not a boundary against hostile code,
  so CI runs layer 4 inside a container with no network and the repository
  mounted read-only.
- In CI the toolkit, `store/config.yaml` and the lock come from the base
  branch, so a pull request cannot change the rules it is judged by.
  `governance.github_logins` lists the GitHub logins with maintainer rights;
  set it to your login before the first pull request.
- The people rules (layer 6) apply to new entities as well as to changes: a
  contributor cannot add an imported or postulate entity, or a proved claim in
  a core region.

## Working rules

- The store is the source of truth. `tp.extract` seeds an empty store only
  and refuses to overwrite one.
- Never hand-write derived fields (effective status, ledger, staleness,
  cones): the validator rejects them.
- A substantive edit (statement, derivations, status, evidence) bumps
  `version`; cosmetic edits (wording of the technical, lay or one-liner
  levels, or the subject) do not.
- Edges pin versions (`id@n`). Revising a premise flags every edge pinned to
  its old version; `tp repin` moves them on once the dependants are checked.
  Moving a pin is a review act, not a change of content, so it needs no
  version bump. Editing a `check.py` is a change of evidence and does.
- A check passes the mutation test if at least one perturbation of its
  integer literals makes it fail (E408 otherwise); if more than half survive
  it is flagged as weak (W413).
- A killed prediction supports nothing: claims that use it lose their
  support, and everything in its past cone is flagged for review (W306).
- Effective status names what a result stands on: `proved`, `conditional`,
  `conjectured` or `unsupported` for derived claims; postulates, imports and
  definitions keep their own names. A generated document shows a declared
  proved result that rests on something weaker as a conjecture (D111).
- After a change is accepted, run `tp lock` so the next submission is
  compared against it.

## Notes and references

Remarks, examples and the papers' running text are entities of kind `note`
(status `remark`, `example` or `setting`). A setting is one run of a paper's
prose between two environments: it introduces notation, motivates and places
the next result, and comments on that result. A recreated paper
(`include: {settings: attached}`, `prose: paper`) prints them in the paper's
order, so it reads as the paper does. A note `comments_on` the results it discusses; nothing may use a
note, so it never changes what the graph proves. Documents attach notes after
the results they discuss (`include: {notes: attached}`); the site shows them
under each result.

Store text keeps a paper's own `\ref` where no entity carries the label (a
section, a table, an equation stated in running text). `store/labels.yaml`
records what carries every label, and `tp/labels.py` rewrites such references
for a reader without the paper: a section by its title, a short equation
written out, a table or long equation by the result it accompanies. Documents
and the site use the same resolver.

## Subjects and tags

Every result has one `subject` (store/subjects.yaml), which places and colours
it on the map. Tags (store/tags.yaml, 79 in five groups: structures, methods,
physics, hypotheses, record) are a second, multi-valued facet for themes that
cut across subjects; a bridging result keeps its home subject and carries a
tag for the other side. Unknown tags are errors (E211), unused ones warnings
(W212), and each build lists the results whose logical neighbours mostly sit
in another subject (I213), as candidates for a tag or a new subject. On the
site, choosing a tag lights up its results; MCP has `list_tags` and a `tag`
filter on `search_claims`. Tags are cosmetic: changing them bumps no version.

## Geometric algebra

The store states results in geometric algebra wherever the series allows it.
Twistor language was converted using the dictionary in seed/GA_DICTIONARY.md
(grounded in the twistor_ga run: twistor space is the minimal left ideal of
the even conformal algebra, its complex unit is the conformal pseudoscalar
I6 = I4 E, acting by right multiplication). The field theory's unit is I4 (One
Complex Unit's choice; seed/I4_PASS.md): the bare quantum-mechanical i was
converted where it acts on the series' own operators, and kept, with a
recorded reason, where it is complex analysis, an imported Hilbert space, a
number, or sits next to a spacetime vector. The paper's wording is kept on each converted entity as
`extraction.source_formal`, `extraction.source_title` and `orig-proof-*.tex`.

## Changes from the design document

- The entity file is `entity.md` for every kind, not `claim.md`.
- Claims can have status `postulate`; `assumes` edges must point at one.
- `checked_by` may be `kind: proof` (proof text only, not machine-checked)
  or `kind: legacy` (tagged checks in a series verify script), besides new
  `check` functions and Lean proofs.
- A conditional derivation does not make a claim proved. A conditional result
  names its condition as a postulate and assumes it, and the build reports
  every claim's "holds given" set.
- Results that standard physics also reaches carry a `standard-route`
  derivation, so the ledger reads them as convenient rather than essential.
- The "maths renders" check is structural (braces, environments, `\left`/`\right`,
  declared macros). A full render runs on the site, where MathJax is loaded.
- Layer 5's AI judge is a hook that is off; the deterministic parts
  (duplicates, number checks) run.

## Open problems

`store/open_problems.yaml` lists the problems the store does not yet settle, for
other agents and readers to attack: the papers' own successor problems, open
conjectures, and the tensions and gaps found by review. Each entry has an id
(`op.<slug>`), area (a subject), kind (research, consistency, housekeeping),
difficulty (tractable, substantial, frontier), status (open, partial,
reformulated, settled), the statement, why it matters, what is known, routes of
attack, what would settle it, and the entities to start from. The validator
checks every entity id and `\claimref` in it (E216) and its shape (E217). The
site shows it under "Open problems", next to an automatic list of every
conjecture and open question; agents read it with the MCP tools
`list_open_problems` and `get_open_problem`, and a draft that works on a problem
records its id under `extraction.open_problem`.

