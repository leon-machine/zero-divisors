# Physics Graph roadmap (written as the Transport Lab roadmap)

Planned improvements, from the review of 2026-10-23: the store judged as a central, AI-written and
human-readable record that could grow to all of physics, and judged by how easily an AI agent works
with it. Each item says what changes, why, and how we know it is done. Phases are ordered by what
they unlock; items within a phase are independent.

Evidence behind the plan (run 2026-10-23-gtg):
- The check writers found about 27 misstated statements. The statement-versus-check judge (I502)
  is not configured, so nothing compared statements with checks before then.
- The GTG curvature engine and the Fock core were pasted into dozens of checks, and the Omega sign
  drifted between restaters until two referees and a fix round aligned it.
- The rule that a check function must contain an `assert` was neither in the brief nor in a fast
  check. 523 functions passed `runcheck` and then failed the hour-long `tp check`.
- The full check prints 4,507 W405 warnings, which bury 162 W413 warnings that matter.
- Every check-writing agent wrote its own `wire.py` to edit entity YAML. `tp accept` cannot update
  an existing id.
- A run costs about 15M tokens, much of it spent rebuilding context for each result.
- The lab page is 15.5 MB against a 16 MB limit.

## Phase 1: tooling for agents (no change to the store format)

1. **Structured edit commands.** `tp bump <id> --note "..."`, `tp wire-check <id>`,
   `tp restate <id> --level formal --from file`, and `tp accept --update`. Each validates the
   change, bumps the version once per day, writes the maintainer note and keeps every stored file.
   Agents never edit YAML by hand.
   *Done when:* a check-writing or restating brief needs no hand edits of `entity.md`, and
   `wire.py` scripts disappear from run folders.
2. **Fast linter.** `tp lint <check.py | id>` applies every static and evidence rule that does not
   need the mutation run, in about a second:
   - an assertion in every check function;
   - the GA import, and no floats or `math`;
   - literals present inside check functions;
   - premises touched against premises declared;
   - the house-style scan on entity text.
   Briefs require it before an agent reports back.
   *Done when:* nothing that `tp lint` passes fails a static rule in the full check.
3. **Context bundle.** `tp context <id>` writes one compact file with:
   - the statement at all levels;
   - each premise's one-liner and statement;
   - the conventions and notation the result uses;
   - the shared library functions available;
   - one example check from the same subject.
   *Done when:* briefs point agents at the bundle instead of at folders, and tokens per result drop
   measurably against the 2026-10-23 runs.
4. **Quieter, ranked warnings.**
   - Suppress expected W405s by rule: literature `-external` entries, restatement premises, and
     premises cited only at another level.
   - Print warnings ranked by severity, with counts per code.
   *Done when:* a clean store's full check fits on one screen, and W413 is visible.
5. **Parallel, cached evidence layer.** Run layer 4 across processes, cache by check source and
   premise sources, and sample mutants adaptively.
   *Done when:* a full check after a 600-entity change takes minutes, not an hour.

## Phase 2: trust in what is stored

6. **A vetted shared library.** `lib/gtg.py` (the gauge fields hb and Omega, the field strength,
   the store sign calR(B) = -R(hb(B)), standard fields, the tractor gauge field), `lib/fock.py`
   (CAR, Jordan-Wigner, sparse exact matrices) and `lib/series.py`, each with its own tests and
   mutation run.
   - The store's conventions (DICTIONARY.md sections C1 to C11) become code that checks import.
   - Checks that paste engine copies are migrated to import the library.
   *Done when:* no check carries a private copy of the GTG or Fock engine, and a sign changes in
   one place.
7. **Coverage record on each check.** A structured field per check function:
   - kind: exact, complete enumeration, sampled or partial;
   - the statement clauses it covers;
   - what it leaves out, which today lives only in docstrings.
   Then configure the statement-versus-check judge (I502) to compare each function with the clauses
   it claims.
   *Done when:* the page shows per result which clauses are machine-checked and how, and a sampled
   check is never displayed as a proof.
8. **Visible trust level.** One field per entity: AI-proposed, AI-refereed, human-read,
   human-checked, externally published. Filled from existing review data where possible, with
   `ai_involved: unknown` resolved. The page shows it and filters by it, and `tp sign <id>` records
   Leon's sign-off.
   *Done when:* every entity has a level and a reader can list what a human has checked.
9. **Contradiction detection.** Flag results that state the same quantity with different values,
   or the same convention with opposite signs (needs item 10 for quantities and item 6 for
   conventions).
   *Done when:* the decimal drift and sign drift corrected by hand on 2026-10-23 would have been
   flagged automatically.

## Phase 3: structure for all of physics

10. **Quantities as their own entries.** A `quantity` kind, holding:
    - value, uncertainty, units and source (PDG table, CODATA, paper DOI), with a date;
    - a link from each result that cites it, instead of a decimal written into LaTeX.
    Dimensional consistency is checked, and a record-value update flags exactly the predictions it
    moves.
    *Done when:* M_P, the lepton masses, M_Z and the cosmological values used by checks come from
    quantity entries, and no check hard-codes a record value.
11. **Machine-readable statement payload.** Next to the LaTeX formal level, an optional structured
    assertion: the equation or identity as a GA or polynomial expression, with its free symbols.
    Checks can then be generated or cross-checked from it, and agents stop reading numbers out of
    prose.
    *Done when:* new numeric and identity claims carry a payload that the linter evaluates against
    the check.
12. **Namespaces and imported standard physics.**
    - Namespaces per programme, so the Transport Papers are one tenant of the store.
    - Standard physics entered once, as imported Facts citing textbooks or DOIs, and checked where
      a finite core exists.
    - A definitions layer much larger than today's 40 objects.
    - Store-wide notation and units registries.
    *Done when:* a second programme can be added without touching the first, and standard results
    are imported once, not restated per paper.
13. **Proof-assistant tier.** Where mathlib already covers the algebra (Clifford algebras,
    quadratic forms, the real classification), add Lean proofs as a stronger kind of evidence than
    exact Python checks, shown as such on the page.
    *Done when:* the transport and tower core results have a Lean proof or a recorded reason why
    not.

## Phase 4: delivery

14. **Split and lazy-load the page.** Move the per-result text levels, proofs, notes and run
    records out of the single HTML file into data files fetched on demand, as the check scripts
    already are.
    *Done when:* the page is a few MB and has room to grow.
15. **Per-result pages and history.** A stable link per result (today `#<id>` works inside the
    artifact), with its version history and what changed, from git.
16. **Pyodide on a self-hosted page.** On a host that allows WebAssembly downloads (GitHub Pages,
    or a private equivalent), replace Brython with Pyodide. The browser then runs the real CPython,
    and the Brython workarounds (Fraction parsing and hashing, `dict.setdefault`) can go.
    - Decision needed first: GitHub Pages on most plans makes the site public.
    *Done when:* every check runs in the browser with results identical to the recorded run.
17. **Browser-run results in the record.** Already started: browser runs are saved with the page.
    Next, show the comparison with the recorded run on the page, and fold disagreements into
    `tp check` as information-level findings.

## Status after the run of 2026-10-23 (roadmap)

| item | status |
|---|---|
| 1 edit commands | done: `tp bump`, `note`, `wire-check`, `restate`, `sign`, `accept --update` (one bump per entity between locks) |
| 2 fast linter | done: `tp lint` (reuses the full check's rules; whole store static pass about 20 s) |
| 3 context bundle | done: `tp context <id> --for check|restate|read` (4-5x smaller than the files it replaces) |
| 4 quieter warnings | done: W405 from 4,507 to about 100, each suppression an I405 with its reason; ranked summary |
| 5 parallel evidence layer | done: process pool (`--jobs`), cache keyed on the lib modules a check imports; 1.9x on 2 CPUs |
| 6 shared library | done: lib/gtg.py, lib/fock.py, lib/series.py with tests; 155 of 182 checks migrated (the rest keep claim-specific or dense code); follow-ups in colony/runs/2026-10-23-roadmap/LIBRARY-FOLLOWUPS.md |
| 7 coverage records | done: coverage.yaml for all 761 checks (2,405 functions: 586 exact, 73 complete, 1,568 sampled, 178 partial); judged by agents; 46 findings fixed |
| 8 trust level | schema, validation, `tp sign` and the page are done; levels not yet derived for existing entities (all AI-proposed until signed) |
| 9 contradiction detection | done: W510 (quantity drift, same-quantity disagreement, decimal drift, C10 sign patterns) |
| 10 quantities | started: 30 quantity entities (standard programme), `tp quantity`; checks still carry literals (map in work/A9/quantity-users.json) |
| 11 statement payload | pilot: 10 claims, evaluated by `tp lint` |
| 12 programmes | done: transport-papers and standard, subjects, MCP filter, docs/PROGRAMMES.md; standard physics not yet moved into its programme |
| 13 Lean | not attempted (no Lean toolchain reachable from the workspace) |
| 14 split page | done: 15.5 MB to 2.7 MB, data loaded per subject |
| 15 history and links | done: History section, Copy link |
| 16 Pyodide | deferred: page stays a private artifact (Leon's decision, 2026-10-23) |
| 17 browser-run results | done: stored per result, compared on the page; library shipped to the browser runner |

## Weak checks (2026-10-23, after the roadmap run)
The 162 W413 weak-check warnings are resolved: sample inputs moved out of check functions, and about
90 functions gained exact asserts for values they had not pinned (normalisations, attained bounds,
counts, conditions that could switch off). `tp mutants <id>` shows which literals a check fails to
pin; `tp bump` refuses while a check is broken. Full check: 0 errors, 8 warnings. Report:
colony/runs/2026-10-23-weakchecks/REPORT.md.

## Already done on 2026-10-23
- Gravity restated in Gauge Theory Gravity throughout; 17 results flagged as global.
- An own exact check for 761 of the 777 proved results, with mutation testing in the full check.
- The page shows each result's check script, the last recorded CPython run (`tp.checkruns`), and
  a run in the browser (Brython, with three engine faults worked around and diagnosed by probes and
  state traces).
