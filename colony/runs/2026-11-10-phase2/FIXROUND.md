# Fix round, run 2026-11-10-phase2

Referee reports: verify/R1.md (positivity and the Born rule), verify/R2.md (the number N), verify/R3.md (the window
reading). Read your proposals' sections in full; the required fixes there are your fixes, with the rules below. Apply
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
3. A proposal cannot cite a proposal. Step 1 is everything except sibling citations; the three bases are then accepted
   into the store and step 2 turns each "sibling, intended citation" sentence into a uses edge and claimref and removes
   the duplicated content exactly as the referee's overlap ruling says.
4. "Nothing here assumes ..." and "no stored result selects ..." are labelled argued at every level unless audited over
   the full cone.

## Leon's decisions (DECISIONS.md) that shape the fixes
- Born rule: the base is to take the place of the imported envariance argument in the stored measurement account. So
  the base must carry, at every level including lay, the sentence that the non-contextuality assumption is relocated
  into (P) and not removed, that physical states are not shown to be sharp, and no sentence may say the Born rule
  "follows" or "is derived" without "under (P) and sharpness on an atom".
- Number N: the stored reading will be restated as rule-dependent. The N proposals state both rules and say nothing
  stored selects one (argued).
- Window reading: version 3 will say the equalities hold at exactly one thermal period and that the array is the twist
  one-half fibre. With R3's finding 1 the wording is "not a Killing-invariant subsystem; non-invariant subalgebras can
  carry the same occupations for any twist and select none"; use it at every level.
- Entropy count: attack item 4 closes; the counterfactual 3/(4 pi) per two-component unit is recorded as not adopted.
  Clause (v) of the window base stays counterfactual at every level and cites synthesis.de-sitter-mode-count at its
  current version.

## Assignments, step 1
- BA: the Born-weights base first (report its final clause labels), then effects and splits (splits is OVERSTATED:
  the null pairs as vectors fix the split; only the two isotropic subspaces leave a positive definite form free; add
  the non-square scales over Q; name the stored twistor-form clause (iv) in the formal text). Effects cites
  synthesis.univalence-even-extension-split clause (i) and keeps the parity-average lemma and the 14/5 formula.
- BB: local weights (scope in title; define "local products"; say it is the real-algebra failure of local tomography;
  quote the stored (P) sentence it corrects), records (title must not state the reading as theorem; cite
  synthesis.univalence-from-even-stationary-dynamics as a remark), Kochen-Specker (Meyer 1999 as prior art over the
  rationals; "no square root of 2" is true of the projectors, not the unit vectors; size-2 pointer; unify the atom
  definition on the base's).
- WA: the antiperiodic base first (variance sign change near r = 0.6249; remove the invalid "only if"; cite
  synthesis.de-sitter-mode-count and synthesis.q-splits-maximum-entropy-affine-weights clause (iv); guard the tail
  constant for r above 8), then the twist integral (OVERSTATED as above; ordering and "averages run over arrays failing
  the energy tests" at every level; restriction remark labelled argued; lay level must not call rate times length the
  light ray's entropy; check labels).
- WB: free spacing (only twist one third is an independent array: say so in title, heading of (ii) and one-liner;
  "no fourth point" is a computed scan at every level; cite the stored q-splits clause (iv) and narrow the claim to
  "the two energy equalities do not fix the slope"; the univalence point as a Remark).
- NA, NB: when verify/R2.md exists; also clear the gate's findings on the exponential-reading proposal (2) and the
  N-free proposal (3), listed in verify/final/check4-<id>.log.
