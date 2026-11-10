# Fix round, run 2026-11-10-phase3

Referee reports: verify/R1.md (dark energy and the spectrum), verify/R2.md (dark-matter premises), verify/R3.md (quantum field
theory). Read your proposals' sections in full; the required fixes there are your fixes, with the rules below. Apply
every fix in place in proposals/<id>/ at every level (title, one-liner, formal, technical, lay, proof, extraction note,
check). OVERSTATED proposals are restated to the referee's true weaker statement at every level. Ids are never renamed
(fix titles, at most 90 characters). Run ONLY `PYTHONDONTWRITEBYTECODE=1 python3 colony/runcheck.py proposals/<id>/check.py`;
never check4, validate or tp check (the orchestrator reruns them centrally). Write findings/fixes-<name>.md listing each
fix and how it was applied, with "check4: pending (orchestrator)". Rebut a fix only with a computation. Do not edit
store/, commit, push or spawn agents; no shell removal commands; guard every large power.

## Rules
1. No new imported Facts and no new postulates. Stored entities may be cited and pinned at their current versions.
2. Assumes edges are maintainer-only: if a referee asks for one (for example (P) on the records proposal) and the edge
   is not already in the proposal, name it in the extraction note under "premises used, assumes edge for the maintainer".
3. A proposal cannot cite a proposal. Step 1 is everything except sibling citations; the cite-first results (the protraction identity; the Kasner scalar sector) are then accepted
   into the store and step 2 turns each "sibling, intended citation" sentence into a uses edge and claimref and removes
   the duplicated content exactly as the referee's overlap ruling says.
4. "Nothing here assumes ..." and "no stored result selects ..." are labelled argued at every level unless audited over
   the full cone.

## Leon's decisions (DECISIONS.md) and rules that shape the fixes
- The graviton does not exist in the series. No level of any proposal presents quantisation of the gravitational
  gauge fields as a goal or gap, extends a stored counting of a graviton, or uses a vacuum for tensor modes as the
  series' own structure (tensor-to-scalar remarks are prior-art comparisons, labelled so, or removed).
- Numbers quoted from memory (the Planck running of the index, bounds, dates of papers) do not appear in a statement
  level or carry a significance unless a stored Fact holds them: move them to the extraction note, flagged, or
  phrase without the number. Nothing dated from outside the store (for example when a section entered a paper) may
  be stated; quote the store.
- OVERSTATED means restate to the referee's true weaker statement at every level. Prior art the referee found
  (for the released norm: Alexander, Cortes, Liddle, Magueijo, Sims, Smolin 2019, arXiv 1905.10380 and 1905.10382)
  is cited and the novelty narrowed.
- The bridge findings (findings/bridges.md) apply where they touch your proposal: the released norm is the stored
  clock density set to zero by definition (what is new and can fail is that the frame equations keep their form
  with torsion and varying norm: make the check test that); the stored theorem synthesis.frozen-phase-spectrum-not-red
  already holds the exact-w = -1 no-go and is cited, not restated; the stored w = -1/4 branch of
  synthesis.unit-ball-clauses-hold-at-one-epoch-unless-hidden-direction-co-expands (ii) is named wherever a level
  says no stored structure evolves; "(P1)" and "(P2)" name different premises in different subjects: say which.

## Assignments, step 1
- DA: the released-norm proposal (OVERSTATED: scope in the title; "never accelerates" only where proved; the
  2019 prior art; the bridge points above).
- SA: the red-tilt base (OVERSTATED: one false sentence at four levels: the Kaluza-Klein potential at the stored
  vacuum end p = 1/2 has index -1, red with no chosen number; the true statement is "no stored mode equation gives an
  index within three standard deviations of the measured one on three axes alike without a chosen number"; the
  ledger's completeness labelled argued with the five stored results the referee lists named; clause (vi) sign not
  derived). Do not add the Kasner row yet (step 2).
- SB: the Kasner scalar sector (fixes; GA language in place of components; the closing sentence conditional).
- MA: the unit-ball base (OVERSTATED: clause (i) needs R3's thickness as one fixed common length; state the reading
  at every level against the store's wording, give the own-cell-radius example where the total moves (7.06), add P1
  to the audit and every other premise the referee lists).
- MB: the constituent-momentum result (scope in title, one-liner and lay; restated and classical content labelled).
- QB: the protraction identity first (converse fails; credit the source for its steps; classical), report its final
  clause labels; then the curved-field freedom (OVERSTATED at title and lay: every level says "if a transverse
  local covariant extension exists" and "given the imported Fact, sourced for scalar fields"; it does not close the
  stored argued clause). The citation of the protraction identity is step 2.
- QA: the one-loop result (clause (vi) and one-liner: "on the Euclidean section"; the identity is built in by the
  choice of subtraction regions: say so; textbook).
