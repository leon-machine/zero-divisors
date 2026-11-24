# Maintainer pass, run 2026-11-24-three-routes (after Leon's decisions of 24 November 2026)

LAB = /home/claude/zero-divisors (branch run/2026-11-24-three-routes, from main at f9f3bee). Seven results of this
run are placed in store/claims/ (ids in accept.log). Read first: colony/BRIEF.md (Standards), colony/POLICIES.md,
and colony/runs/2026-11-18-navigate/MAINTAINER.md for the bookkeeping, style and check rules of a maintainer pass
(they apply unchanged: version + 1 on every changed entity, every stored file kept, an `amendments` entry
{version, kind: restatement | correction, defect: at least 30 characters, evidence: a check function of the
entity or of the result the change rests on}, a credit entry {name: Claude Fable 5.2, role: <what changed>,
version: <new>, source: 'maintainer pass of 2026-11-24 (run 2026-11-24-three-routes)'} with every existing credit
entry unchanged, and an `extraction` entry under the key maintainer_pass_2026_11_24_three_routes saying what was
changed and on whose decision). Then this run's REPORT.md, findings/bridges.md, the fixes files findings/fixes-*.md
(sections "Decisions for Leon", "Repin on acceptance", "Next steps") and the referee reports verify/R-*.md.
You are not blind. Take every statement from the stored entities as accepted (labcli get_claim, or the files in
store/claims/), never from first drafts in findings.

## Leon's decisions of 24 November 2026 (binding)
D1. (RP), the reading that every self-adjoint projector with rational coefficients can label a record: NAMED
    HYPOTHESIS. It is not adopted and not rejected. It stays a hypothesis of the results that use it; (P) stays the
    postulate; the fork (all rational projectors, or products of local outcomes only) is recorded on the open
    problem.
D2. The canonical pair on the two null directions: ADOPTED. Premise (TT): at first order, at each nonzero null
    momentum, the two transverse trace-free directions that the first-order equations of the gravitational gauge
    field leave free carry a canonical pair on polynomials, one mode over span{1, I_4} per null momentum, as the
    stored photon modes do (field-theory.fock-space-maxwell-modes). It has the photon's status: a pair on
    polynomials, not an element of a floor of the tower, not derived from the tower. Scope: first order only. It is
    a postulate of the series from this date, by Leon's decision, with these grounds and limits to be stated in
    it: the series requires no signal outside the light cone (conventions, 18 November 2026); a field with no
    variables of its own fails that (the stored lattice results); in the stored lattice model of the first-order
    field the field's own canonical variables with a dressed detection meet it (sufficiency in a model, at first
    order); it is not shown necessary, the other way named being the gravitational field as the response of the
    stored quantum fields, for which the store holds no result; one mass moved alone has no localised dressing
    (the dipole obstruction), whatever the free part is made of. This reverses the sentence of 10 November 2026
    that the series holds no quantum of the gravitational gauge field and posits none: from 24 November the series
    posits states on the two free directions at first order and nothing more (no quantised geometry beyond first
    order, no element of the tower, no self-coupling). The registered entangling phase is unchanged. The burst
    ratio is (2 + g + o)/(1 + g).
D3. The radiation-type descent hypothesis: RESTATED FOR THE COLLAR ONLY. It is a hypothesis about a Cauchy collar
    of the descent (a smooth scale factor, Weyl-flatness, the conformal vacuum an admissible reference there). It
    is not a statement that the field is the exact radiation field down to the wall. A result that uses the wall
    itself (a mass term linear in conformal time through it, a continuation across it, the wall as the initial
    slice of half of Minkowski space) must name what it assumes there.
Defaults taken without asking, to be carried out as stated: (CW) is not adopted and stays a named hypothesis of its
result; (A) and (E) stay named hypotheses of the trace-anomaly result, nothing is imported; no literature cited
from memory is imported as a Fact in this pass (the flags stay); op.gravitational-field-at-null-momentum is NOT
moved to the settled file (see M-O); no status of any stored claim is promoted.

## Ownership (disjoint; touch nothing outside your list)

### M-G: the gravitational field (store/conventions.md, the new postulate, and the entities named here)
1. Create the postulate entity for D2. Id: synthesis.premise-canonical-pair-on-the-two-null-directions. Copy the
   format of an existing postulate of the series (for example synthesis.hadamard-deposit-premise or
   synthesis.premise-positivity-of-values: status postulate, four levels, what it delivers, what it does not,
   what would refute it). State D2 exactly, with its grounds and limits, citing by \claimref the stored
   first-order theorem (two free directions, four constraints), the stored photon modes, the three lattice
   results of 18 November and this run's lattice model of first-order gravity and helicity-two composites result.
   Its refutation clause must be candid: say what in the series would refute or retire it (for example a stored
   result meeting the requirement with no states on the two directions; a conflict with a stored theorem; a
   failure beyond first order) and that no accessible observation distinguishes it from the standard account.
   Ledger: transport-absent. `proposed_by` and credit as for a maintainer entity created on Leon's decision.
2. store/conventions.md, section "Gravity and the graviton": add a dated paragraph "Decision (24 November 2026)"
   stating D2, and restate every sentence of the section that it contradicts (the "no quantum" sentences and the
   closing sentences of Scope and Requirement), keeping the earlier decisions visible as dated history and not
   erased. Say what the word graviton now names in stored text: the mode of (TT) at first order.
3. This run's two G results, now stored: turn "filed alongside, <id>" text citations into \claimref (both
   directions), cite the new postulate where their Reading speaks of the hypothesis (TT) (it is now the adopted
   premise; their proved clauses do not depend on it; do NOT add an assumes edge to a proved clause that holds
   without it: add one only for a clause that needs it, and say which), and fix the stale id of the lattice model
   wherever the old id survives in text.
4. The stored entities that D2 restates (find them with find_text for "graviton", "no quantum", "variables of its
   own", and from findings/fixes-G-A.md and attack-G-A.md, section on what would be restated):
   note.synthesis.where-stored-text-names-a-graviton (groups on processes, ontology readings, polarisation counts);
   the Reading of synthesis.first-order-gravitational-field-has-two-free-directions-at-null-momentum-and-four-constraints
   (which of its two burst ratios now holds); the closing Reading of
   synthesis.two-dimensional-lattice-maxwell-coulomb-slaved-field-fails-and-string-dressed-detection-commutes
   (the step to gravity is no longer by analogy only: cite the lattice model, at first order);
   pred.dimmed-evaporation-bursts (the ratio (2 + g + o)/(1 + g), with a proviso if the state near the hole is
   not addressed); pred.no-indirect-dark-signals if it rests on the old sentence; the flag on
   dark-matter.imported-massless-graviton-production-rate. Do not touch pred.gravity-entangles-standard-phase
   except to add one dated sentence that its premise (P-v) was restated by the registration's third addendum of
   12 October 2026 (the phase is computed at the instantaneous order) and that (TT) does not change the phase.
   Where a prediction's numbers would change, do not recompute them in this pass: say what changes and list it in
   your report under "Numbers to recompute".
   Do not strengthen any statement. If a stored sentence says more than D2 licenses, restate it to D2.

### M-H: the deposit state and the values results (the entities named here only)
1. D3. Find every stored entity that states or uses the radiation-type descent (find_text "radiation-type",
   "radiation type", "radical-normal", "initial slice"): at least synthesis.hadamard-deposit-premise (its
   statement of the descent's normal form and its note), the tame-wall result
   synthesis.radical-normal-tame-wall-is-a-regular-initial-surface-whose-smoothness-selects-no-state (the clause on
   the power law with a tame conformal bracket and the sentence that the physical side is a flat half-space with
   Cauchy slices), synthesis.deposit-over-the-conformal-vacuum-is-hadamard-exactly-when-every-occupation-moment-is-finite,
   synthesis.massive-dirac-instantaneous-vacuum-and-non-smooth-descents-are-not-hadamard. Restate the hypothesis
   for the collar only wherever it is stated, in one consistent sentence, and add where a result uses the wall
   itself what it assumes there. A theorem about a prescribed field (the tame wall as geometry) is not changed:
   only say that with the whole expected stress as source the exact radiation field is not a solution, citing
   the stored trace-anomaly result with its hypotheses (A) and (E). Change no mathematics.
2. This run's two H results, now stored: turn the plain-text ids of each other into \claimref, with the
   reciprocal sentences the referees worded (verify/R-H.md, "Overlaps and conflicts"; verify/R-2.md).
3. This run's three values results, now stored (the even-projector corollary; the (RP) bound; the (CP) and
   reversal result): turn "filed alongside" citations into \claimref; the (RP) result's "not carried out here"
   sentence stays. On synthesis.no-two-valued-weights-on-the-atoms-of-two-modes-the-even-subalgebra-admits-them:
   one dated sentence that three modes suffice (the corollary's clause on two-valued weights), version + 1.
   On synthesis.premise-positivity-of-values: one dated sentence (no change to the premise) that the bound
   2 sqrt 2 follows already from (CP), which (P) implies and which does not imply (P), with the \claimref; and,
   as fixes-P-B.md recommends, one sentence that (P) is not asserted for Krein expectation values on floors
   carrying ghost or regulator modes, ONLY if that sentence is a plain consequence of stored text you can cite;
   otherwise list it in your report as a decision for Leon and do not write it.
   Do not write (RP) into any premise (D1).

### M-O: store/open_problems.yaml and colony/runs/LEDGER_HISTORY.md only
Update, in the file's own style (dated "(24 November.)" paragraphs under `known`; dated "Answered", "Answered in
part", "Done", "Closed negatively", "New" prefixes on attack items; entities lists extended with the new ids;
status changed only where stated here):
- op.positivity-of-values (main already records that more than two modes is done and the first step false; do
  not repeat it): the parity-even form from three modes on and what it does to the item "tied to the parity
  item" (two modes only); (RP) is (P) on projectors, a relocation (D1: a named hypothesis; the fork recorded);
  the sum of four recorded correlators is bounded under (RP) with no assumption on the value of the element C;
  the bound needs only (CP); the reversal on one party: (P) is not implied by any condition on the weights of
  local records, argued on the scope of a laboratory pair for the other premises, and fragile (one unitary
  mixing the parties' modes); the Krein-form premise and (P) are not one premise (computed, not stored); (N+)
  does not supply the split (argued, not stored); the recording premises do not imply macroscopic locality
  (argued, certificate computed, not stored). Restate the "why" sentence that (P) is the only premise between the
  algebra and the quantum bound. New attack items: the flag-sector form of (RP), an exact test at three modes;
  whether a functional whose local record weights are non-negative at every number of copies is a state or the
  reversal of one (conjectured).
- op.gravitational-field-at-null-momentum: D2. The statement is restated: the requirement is met at first order
  by the adopted premise (TT) (cite the postulate id synthesis.premise-canonical-pair-on-the-two-null-directions,
  which M-G creates), with what the lattice model shows (sufficiency in a model; the counts; the lattice cone and
  the unit-speed cone) and what stays open: a derivation of (TT) or a proof that the response way fails; anything
  beyond first order; the single-mass dipole obstruction and the recoil partner (argued, not modelled);
  dressings by sums of Weyl operators; moving matter. Status: partial. Do NOT move it to
  open_problems_settled.yaml (whether its success clause is met by adoption is put to Leon). Attack items: the
  composite on the generators closed negatively on a generator (what is left: smeared contraction over many
  generators, transverse-derivative bilinears); the recording route closed negatively (argued); the burst
  baseline item answered by D2.
- op.einstein-from-the-field-theory: under (TT) the route through the coupling of a helicity-two mode is open
  (new attack item, route 3a of ROUTES.md, with its prior art named from memory); G-B's second way; the bridge
  entries B1 and B2 of findings/bridges.md (the stored Clausius theorem takes the stress as an expectation value
  and as given; the stored content's spin-two response has no pole at null momentum without the induced
  Einstein-Hilbert term), labelled argued; routes 3b and 3c as attack items.
- op.graviton-rate-as-classical-field-process: one dated sentence on what D2 changes for it (the rate at non-null
  momentum does not depend on (TT); the stored text that names a graviton is restated by M-G).
- op.deposit-state-is-hadamard: the wall-conjugation result ((CW) selects no state; the floor; which conjugation;
  what the bundle with purity, least occupation and orientation trades; the mirror tension, argued) and the
  trace-anomaly result (given (A) and (E)); D3; the necessity route gives nothing the store requires (argued, not
  stored); obstruction (O5) is specific to the conformal group (one sentence); the two results cannot hold with
  all of (A), (E), (RD), (DF). Attack items: route 4b closed by its own condition; 4c done; 4a closed (argued);
  wall-based selections must say what they assume at the wall; the Riemannian far side for the massive Dirac
  field stays as it is.
- op.descent-state-and-spectrum, op.the-number-n (and op.rung-unit, op.non-gaussian-completion where a route
  names them), op.derive-loc-and-r-loc: add as "New (24 November)" attack items the routes of ROUTES.md that were
  not run (2a, 2b, 2c, 3b, 3c, 6a, 6b, 6c), each in two or three sentences with what would end it, AS AMENDED by
  the section "Changes to ROUTES.md" of findings/bridges.md (for example 6c no longer depends on route 4b; 2c
  must say what it assumes at the wall; 5b is partly answered: (N+) does not supply the split). Literature named
  there is from memory: say so in each item.
- colony/runs/LEDGER_HISTORY.md: one line for this run in the file's style (targets, method, the seven results in
  a clause each, the decisions D1 to D3, the duplicate withdrawn against pull request #65, about 3.9M subagent
  tokens).

## Rules for all three
- Everything truthful to the stored results as accepted; no statement stronger than its source. Keep the labels
  proved / computed / argued / conjectured. Where a finding is "argued" or "computed, not stored", say so.
- House style: no em dashes; never "honest"/"honestly"; never "load-bearing"; Q(v) for the square of a vector;
  macros only from store/notation.yaml; no imaginary unit where a pseudoscalar does the work; no agent, run or
  method names in store text (dated decisions are attributed to Leon by name and date, as the store does).
- Checks: `python3 colony/runcheck.py` on any check you touch; `python -m tp check --store store --layers 1-3
  --keep-going --author leon` after your last edit (about 15 seconds; it must end with 0 errors, and no new
  warnings against colony/runs/2026-11-24-three-routes/layers123-after-accept.log). No layer 4, no check4, no
  `tp accept`, no repin, no lock, no commit, no push, no spawning agents. Never kill a process you did not start.
- Write colony/runs/2026-11-24-three-routes/maintainer-<your name>.md: every entity or record changed with its
  new version and one line on the change; "Numbers to recompute"; "Not done, and why"; "Decisions for Leon".
  Your final reply is that file in brief.
