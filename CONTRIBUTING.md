# Exploring the Physics Graph, and sending findings

Anyone can explore the Physics Graph, and findings are welcome. Every result is
reviewed by the maintainer before it enters: nothing is added to `main`, or to the
published site, until it has been read and merged.

## Explore it with an AI

Python 3.11 or later, from a clone of this repository:

    pip install pyyaml jsonschema          # scikit-learn too, for meaning-based search

Claude Code:

    claude mcp add --env PYTHONPATH="$PWD" physics-graph -- python -m tp.mcp_server --store "$PWD/store"

The Claude desktop app, or any client that runs stdio MCP servers:

    "physics-graph": {
      "command": "python",
      "args": ["-m", "tp.mcp_server", "--store", "/path/to/phys-graph/store"],
      "env": {"PYTHONPATH": "/path/to/phys-graph"}
    }

On Windows, `register_mcp.ps1` registers the server with the desktop app. Then ask
the agent to call `conventions` first. The tools are listed in README.md and on the
site's Explore with AI page.

## Found something?

First, have your AI call `conventions`: it explains how a result is stored, the
notation, the two imaginary units and the house rules for proofs and checks.

If you or your AI find something substantive (an error, a gap in a proof, a new
result, a sharper check), send it in the graph's own format, so it can be checked
and added directly: one folder per result, `store/<kind>/<id>/`, containing

- `entity.md`: the statement at four levels, its premises pinned to the versions
  read (`id@n`), who proposed it, whether an AI was involved, and a `credit`
  list: your name as you want it shown, and the AI model, with its version, that
  drafted the proof or amendment;
- `proof-main.tex`: the proof, citing each premise with `\claimref{id}`;
- `check.py`: a machine check in exact arithmetic, using `GA.py`.

The format is set out in `docs/CONTRIBUTING-rules.md`, with a complete worked
example in `docs/example-contribution/`. A correction to an existing result can be
the edited `entity.md`, with its `version` raised, and a note of what changed and why.

```yaml
credit:
- name: Ada Lovelace
  role: idea and direction
- name: Claude Opus 5.5
  role: proof and drafting
```

### By pull request

1. Fork this repository on GitHub and make a branch in your fork.
2. Add your result folder (or edit an existing one) under `store/`. Commit only
   result folders: not `build/`, `site/`, `store/.tp-lock.json` or
   `store/.tp-layer4.json`, which the maintainer updates when merging.
3. Run `python -m tp check --store store --keep-going` on your copy.
4. Open a pull request against `main` and fill in the checklist.

The same checks then run on GitHub: the unit tests and validator layers 1 to 6,
with the rules taken from `main` (so a pull request cannot change the rules it is
judged by), and every contributed `check.py` run in a sealed container with no
network and the repository read-only. For a first contribution the maintainer
approves the run before it starts. Nothing enters `main` until the maintainer has
reviewed and merged it; the published site is rebuilt from `main` after that.

By sending a result you agree to its publication under CC BY 4.0,
credited to you by name, with the model you state. The model is shown as you give
it; it cannot be checked from here.

## Credit in the graph

Every result names who did what. Results from the papers credit Leon Butler with
the idea, the direction and the review, and Claude Fable 5 with the mathematics
and the drafting, as each paper's authorship disclosure states. Results proposed
in AI sessions name the model from the commit that added them. Where no model is
on record the credit says so rather than guessing (`python -m tp credit`).

## The full rules

The rules a contribution follows (entity format, check.py, the six validator layers,
what only a maintainer may do) are in `docs/CONTRIBUTING-rules.md`.

## Licences

Entity content: CC BY 4.0. Code (`tp/`, `lib/`, `tests/`, `site/`): MIT, as in
`LICENSE-CODE.txt`.
