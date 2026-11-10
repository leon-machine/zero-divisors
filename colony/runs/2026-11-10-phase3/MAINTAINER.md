# Maintainer pass after run 2026-11-10-phase3 (acting for Leon, the maintainer)

The eight proposals of the run are in `store/claims/` on branch run/2026-11-10-phase3, and Leon approved the edits
below (colony/runs/2026-11-10-phase3/DECISIONS.md, items 1 to 12). Three maintainer agents with disjoint files: MD
(dark energy, spectrum, gap entries), MM (dark matter), MQ (quantum field theory and the graviton position). Edit
`store/` directly in LAB = /home/claude/phys-graph. Never touch the user's computer; never spawn agents; never commit
or push; no shell removal commands (a retirement is done as colony/runs/2026-11-09-bridges/MAINTAINER.md did it: read
how, follow it, and leave folder removal to the orchestrator, listing it in your report). store/open_problems.yaml is
shared by all three: small targeted edits of your own entries only, re-reading the file immediately before each edit,
never rewriting the whole file. 2 CPUs shared: one heavy process at a time.

Background to read: DECISIONS.md; verify/R1.md, R2.md, R3.md (overlap rulings and "for the maintainer" items); the
fixers' notes findings/fixes-*.md; findings/bridges.md; findings/attack-*.md sections "Decisions for Leon". Nothing
dated or quoted from outside the store goes into store text unless a stored Fact holds it or you verify it on the web
and cite the source in the entity's own citation format.

## Rules
- Read `CONTRIBUTING.md`, `docs/CONTRIBUTING-rules.md`, `store/conventions.md`; copy the format of existing entities.
- Changing an existing entity: version + 1, keep every file in its folder (orig-proof-main.tex in particular), add a
  `maintainer_pass` entry under `extraction` with a key not already present (for example `maintainer_pass_2026_11_10`)
  with `by: maintainer-2026-11-10`, `date: '2026-11-10'` and a one-sentence note of what changed and why; keep
  `proposed_by` and `credit`. Add a credit entry {name: Claude Fable 5.2, role: <what changed>, version: <new>,
  source: maintainer pass of 2026-11-10} if the change is substantive (statement, premise wording, a bound), not for
  notes.
- An entity accepted in this run (version 1) edited only in its extraction note, uses/assumes
  edges or citations stays at its version if `tp check` layers 1-3 accept that; otherwise bump.
- assumes edges: the list `assumes:` under the derivation, pinned `id@version` (see
  store/claims/dark-energy.imported-walls-sphere-theorem/entity.md). When an in-statement hypothesis becomes an
  imported Fact, cite the Fact and keep the hypothesis's label in the text. If a check then has an untouched premise,
  record it under `untouched_premises` in coverage.yaml as earlier passes did.
- House style: no em dashes; never "honest"/"honestly"/"load-bearing"; Q(v); macros only from store/notation.yaml; no
  agent, run or method names in store text (`by:` fields excepted).
- After changing a check: `PYTHONDONTWRITEBYTECODE=1 python3 colony/runcheck.py <folder>/check.py` and
  `python3 colony/check4.py <folder>` (one at a time; 2 CPUs shared).
- Validation after your edits: `PYTHONDONTWRITEBYTECODE=1 python3 -m tp check --store store --layers 1,2,3 --keep-going
  --author leon 2>&1 | tail -40`; fix every error or new warning on YOUR files. Do not run the full check, `tp repin`, `tp lock` or `tp build` (the orchestrator does).
- Write colony/runs/2026-11-10-phase3/maintainer-<your name>.md: every entity changed (old -> new version, one line
  each), dependants whose CONTENT may be affected (not only pins), and anything not done and why. Your final reply is
  a short summary of that file including your layers 1-3 result.
- Where an instruction below turns out to be false to the mathematics as stored, do not force it: do the true weaker
  edit, and report the difference for Leon.

- Write colony/runs/2026-11-10-phase3/maintainer-<your name>.md: every entity changed (old -> new version, one line
  each), dependants whose CONTENT may be affected (not only pins), and anything not done and why. Your final reply is
  a short summary of that file including your layers 1-3 result.
- Where an instruction below turns out to be false to the mathematics or to the store's rules, do not force it: do
  the true weaker edit, and report the difference for Leon.

## MD: dark energy, spectrum, gap entries
D1 (decisions 1, 4). pred.dark-energy-w-minus-one: new version with the registered kill condition: refuted when two
   independent surveys each exclude (w0, wa) = (-1, 0) at five sigma, each survey allowed the shared CMB prior, by
   the collaboration's published frequentist distance, Bayesian evidence recorded beside it; say plainly the rule is
   conservative; keep the stored "at any epoch" wording as the model-independent reading beside the w0-wa form. Add
   an observation row for November 2026 with the values in findings/attack-DA.md (each with its arXiv source; verify
   on the web the ones you store). Record, labelled argued (a search of the store, not a proof): the series has no
   fallback for w different from -1; name the stored w = -1/4 branch
   (synthesis.unit-ball-clauses-hold-at-one-epoch-unless-hidden-direction-co-expands (ii)) and why it is not one.
   The same sentence in the field-space premise's refutation clause and Premise (N). Cite the released-norm result.
D2 (decision 11). Add assumes edges to the field-space premise (FS) on the action results that state field equations
   with matter (at least synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part and
   synthesis.frozen-point-field-space-is-the-gtg-pair-and-its-omega-equation-is-the-torsion-equation; check each by
   reading that its statement does use (FS); do not add an edge where it does not). Version + 1 each. Report the new
   size of (FS)'s future cone. Do not add edges to Premise (N) (not decided).
D3 (decision 8). op.descent-state-and-spectrum (find the exact id): record what was examined (the criterion, the
   ledger, the Kasner scalar sector; moduli, pair channel, density waves, horizon arrays examined and not candidates,
   argued), the corrected statement (no stored mode equation gives an index within three standard deviations of the
   measured one without a chosen number; the Kaluza-Klein potential at the vacuum end is red, index -1), that the
   survey is argued and five stored index results are outside the ledger, and the rule that a future index match
   counts only with a second number (amplitude or running). The series' position stays "no mechanism"; the problem
   stays open. Point the "not covered" sentences of the two stored Kasner results to the Kasner scalar-sector result.
D4 (decision 2). Two new open-problem entries in the file's format: strong CP (what the graph holds: nothing, and a
   constant early theta-angle is excluded as the source of the asymmetry: find and cite the stored result; what a
   result would need) and the matter asymmetry (a registered free input, inherited and not generated: cite; whether
   any stored dynamics could generate it, or a proof none can). No entry for a quantised graviton.
D5. pred.gravity-entangles-standard-phase: add the sentence that the prediction concerns the phase only, makes no
   claim about a mediator and is not a test of a quantised gravitational field (the series holds none); add a
   November 2026 observation row (status unchanged) from the web-checked items in findings/attack-DA.md only.
D6. pred.neutrino-mass-sum-floor: its kill condition does not name the cosmological model the bound is derived in
   (bridges lead 2): add that the bound is read in the model with w = -1, the series' own; note the anticorrelated
   exposure in one sentence, labelled argued. Do not change the prediction.
D7. Citations among the three accepted results of your area (lineage where comparison only).

## MM: dark matter
M1 (decision 10). Apply the re-typings: (a) P4: retire as a postulate after giving clause (v) of
   dark-matter.mirror-tower-copy-one its actual premises (R2 found an untyped forward reference: fix that first),
   then repoint P4's two assumes edges to that clause; (b) U: re-type as a definition (find how the store types a
   definition: obj.* or kind definition; if the id rules prevent a clean re-typing, keep the entity and mark it
   with the store's own mechanism, and report); (c) the six simulation premises C, S1 to S5: model specification,
   with S2 and C recorded as premises of two exclusive readings (W) and (C); S1's second clause is a stored theorem
   (cite); S3 states its window of xi; (d) D: a note that D with R1 and R2 forces one quantum per de Sitter ball
   (argued), that D belongs to the de Sitter reading and is not counted with R1 to R3, and that it is the one
   dark-matter postulate naming the de Sitter radius (so it shares the exposure of w = -1 in content: text only);
   (e) P1: split into its three clauses within the entity (metric, orientation, common N) with the status of each as
   R2 and the attackers found (do not create three entities unless the store's rules require it). The flag premise
   is left alone. Where a re-typing would break edges or the layout, do the nearest clean thing and report.
M2 (decision 5). Two new postulate entities, in the format of the subject's postulates: the single-ideal clause
   (dark-matter.status-rule (vi)) and the population of the odd towers (say that it is inferred from the number it
   helps fit). Add them as assumes edges on the statements of the total that use them, and on the unit-ball result
   of this run with P1 as its extraction note lists. Version + 1 where statements change.
M3 (decision 9). R3: state that its unit is each tower's own cell radius, so R2 also supplies R3's unit. The
   unit-ball result of this run then holds only in the fixed-common-length reading, not adopted: make its entity say
   so in the same words at every level if it does not already (it stays version 1 if only notes change).
M4. The statement of the count: on dark-matter.unit-ball-rule and the subject's setting note, replace any sentence
   of the form "N postulates support the ratio" by what the audit found (the closed form's cone; the total remains a
   fit: two shares against one measured number; which ingredients were chosen with the number known, quoting the
   store only). H1: a note pointing to the constituent-momentum result (the formula is forced up to a real factor
   given quadraticity and covariance; H1 is weakened, not retired).
M5. dark-matter.imported-massless-graviton-production-rate is MQ's file; do not edit it.

## MQ: quantum field theory and the graviton position
Q1. The stored curved-field theorem
   synthesis.vacuum-polarisation-kernel-on-a-gravitational-field-has-the-flat-leading-part-and-no-weyl-term-of-degree-four:
   the protraction identity becomes a cited theorem in place of a hypothesis; clause (iv) "leaves Z_3" becomes "two
   transverse local covariant extensions differ by Z_3; existence not proved"; drop the first Hadamard transport
   equation from what the reduction waits for; clause (iv) stays argued as a whole. The flat theorem's clause (v)
   likewise. Repoint, as citations only, the entities that impose or assume the first Bianchi identity (R3 and
   fixes-QB list them); fix the wording of entities that equate "torsion-free" with "obeys the first Bianchi
   identity" (the converse fails). One line for the identity in docs/ALGEBRA_CORE.md with the claim id.
Q2. The local-covariance Fact: sourcing fixed as R3 says (scalar-field sources; add Zahn arXiv 1210.4031 and
   1311.7661 for the Dirac field at the level verified; align the wording on dependence on the metric with what the
   sources say; verify on the web what you store). No new import of existence.
Q3. The stored regulator-free vacuum-polarisation result and op.qft-loops-and-renormalisation: note that a
   Ward-obeying pair of extensions is exhibited on the Euclidean section at one loop for self-energy and vertex
   (supported, not discharged: the import for time-ordered products in signature (1,3) stays); reword "floors are
   excluded for every weighting" to "excluded as a covariant regulator"; add an attack item for the torsion case.
Q4. The scope note (text drafted in findings/attack-QA.md, Q4): store it as a note in the store's note format,
   scoped to the matter and gauge sector on the classical GTG background; neither a continuum interacting theory nor
   an emergent-covariance cut-off theory is claimed; prior-art names only where you verify them on the web.
Q5 (decision 12). Add to store/conventions.md, verbatim, as its own short section headed "Gravity and the graviton":
   "Gravity in this series is the classical gauge field of Gauge Theory Gravity. The series holds no quantum of that
   field: the graviton does not exist here. Where stored text says graviton it names a helicity-2 channel of the
   classical field, a counting convention, or prior art; no stored result is to be read as resting on a quantised
   gravitational field, and results that import such a process are flagged."
Q6 (decision 6). Flag now, derive later. dark-matter.imported-massless-graviton-production-rate: new version with a
   flag in the store's own mechanism (a scope or caveat paragraph at every level): it imports a process of a
   quantised gravitational field, which the series does not hold; its dependants rest on it conditionally. New
   open problem (suggested id op.graviton-rate-as-classical-field-process): derive the rate as radiation of the
   classical gauge field sourced by matter, or show it vanishes; list what rests on it (the two live predictions
   pred.no-dark-radiation and pred.no-indirect-dark-signals, the dimmed-burst baseline, the dependants: get them
   with `cone`); attack items; first computation. On the two predictions and pred.dimmed-evaporation-bursts add one
   sentence each pointing to the open problem; change no prediction, status or number. From findings/bridges.md
   lead 6 take the list of the 51 entities naming a graviton: do NOT edit them; store the list, grouped as there, in
   the open problem's `known` or in a note it cites, so later runs can work through it.
Q7. Citations among the three accepted results of your area; the Krein-form premise as an assumes edge on the
   one-loop result if its statement uses it (read; report).
