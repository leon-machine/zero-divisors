# Maintainer pass MB, run 2026-11-10-phase2 (10 November 2026)

Scope: MAINTAINER.md, section "MB: positivity and the Born rule", items B1 to B5. No file of section MN was touched.
In store/open_problems.yaml only the entry op.positivity-of-values was edited (eleven small replacements, the file
re-read before each). store/tombstones.yaml: one entry appended. No commit, no repin, no lock, no build, no full check.

## Validation

`tp check --store store --layers 1,2,3 --keep-going --author leon`, last run after all edits:
**1 error, 0 warnings** (baseline before my edits: 0 / 0). The one error is expected:

- `E205 one-relation.imported-envariance-born-rule`: "this id is retired and can never be reused". The tombstone is
  in place and the folder is still there, as instructed. It goes when the folder is removed.

Checks: `colony/runcheck.py` and `colony/check4.py` on one-relation.measure-indifference-borns-rule-located (check.py
changed: 5 functions PASS; check4 "0 error(s), 3 other finding(s); check result: pass", the three being I410 and two
I405 for the declared untouched premises). check4 on synthesis.records-keep-even-states-even-only-for-parity-homogeneous-observables
(coverage.yaml changed only): "0 error(s), 1 other finding(s); check result: pass". No other check.py was changed.

## Entities changed

Version raised:
- one-relation.measure-indifference-borns-rule-located: 3 -> **4** (B2, restatement; details below).
- synthesis.premise-positivity-of-values: 1 -> **2** (B3). The three clauses and the split are unchanged. Restated:
  the first sentence of "What it costs" (the counter-model does not show that positivity across settings "cannot be
  dropped": in the one-mode realisation local weights already give the bound; positivity across settings is what the
  box violates), the phrase on where the box is negative (the four configured pairs), the sentence on the split (in
  the mode algebras the stored null pairs as vectors fix it; only the isotropic subspaces leave it open). Added:
  pointers to the effects result ((P) as non-negative additive weights on effects), the splits result, the base
  result; the claimref to the retired envariance Fact replaced by the stored Born account. Technical and lay follow.
- synthesis.chsh-bound-needs-positivity-across-settings-and-anticommutation-holds-only-on-the-state: 1 -> **2** (B3).
  Title now "A box functional reaches 4: weights at four setting pairs do not bound CHSH; (P) does" (id unchanged).
  A scope paragraph in the formal level (the setting pairs are the four configured ones; weight -1/10 on
  (1/4)(1 + A_1)(1 - b), b = (3/5)B_1 + (4/5)B_2, recomputed in this entity's own labelling; citation of the
  local-weights result). Technical, lay and one-liner restated. Clauses (i) to (iii), proof and check untouched.
  Pin (P)@2; lineage: the retired Fact replaced by the Born account, local-weights result added.
- one-relation.record-chain-votes-measurement-without-collapse: 7 -> **8** (B5). Pin of the Born account 3 -> 4; each
  level and the proof now say that the branch weights hold under (P) for a state sharp on an atom, both assumed, and
  that neither is shown for the state of system and records. The two arguments, the gaps and the stance unchanged.

Version kept at 1 (accepted in this run; notes, edges, citations and clarifying phrases only; layers 1-3 accept it):
- synthesis.born-weights-under-positivity-a-state-sharp-on-an-atom-is-its-trace-functional: claimref to the retired
  Fact replaced by a reference to the Born account (formal, technical, one-liner wording), lineage entry dropped,
  note updated, (P) pinned @2.
- synthesis.positivity-of-values-is-additivity-of-non-negative-weights-on-effects: the three "intended citation"
  sentences name the stored results; lineage entries added for the Kochen-Specker, local-weights and records results
  (comparisons: all three use this result, so a uses edge would be a cycle); lineage entry for the retired Fact
  dropped; one phrase of the Scope ("imported envariance argument") reworded; (P) pinned @2.
- synthesis.splits-adapted-to-the-null-pairs-and-the-states-common-to-all-of-them: lineage entries for the records
  and effects results (the three consistent sufficient conditions for "at most 2"), note, (P) pinned @2.
- synthesis.local-weights-give-the-chsh-bound-and-do-not-fix-positivity-of-values: note (the three stored phrases are
  now restated); the quoted sentence is said to be of version 1 of (P); one clarifying phrase in clause (iii) (see
  "For Leon", item 6). No assumes edge to (P): it is compared, not assumed (referee's ruling).
- synthesis.records-keep-even-states-even-only-for-parity-homogeneous-observables: **assumes
  synthesis.premise-positivity-of-values@2 added**; first line of the proof names the premise; coverage.yaml lists
  it under untouched_premises; (P) leaves lineage, the splits result enters lineage; note updated.
- synthesis.no-two-valued-weights-on-the-atoms-of-two-modes-the-even-subalgebra-admits-them: lineage entry for the
  retired Fact dropped; note. No assumes edge (nothing is under (P)).

Store files: store/tombstones.yaml (one entry); store/open_problems.yaml (op.positivity-of-values only).

## B2 in detail: what the new route covers, and the gap

Version 4 of one-relation.measure-indifference-borns-rule-located. New title: "Born's rule located: the Dirac
density; squared-norm weights under (P) for a sharp state" (old: "The measure from indifference: Born's rule
located"). Edges: uses the Dirac-density lemma @3, the indifference Fact @4, the base result @1, the effects result
@1; **assumes (P)@2** (new); the uses edge to the envariance Fact is gone. Clauses: (a) the density (cited);
(b) the density is the squared norm of the split (in Cl(1,3) the adjoint of (P) is gamma_0 x~ gamma_0, the scalar
part of psi^dagger psi is J . gamma_0 for even psi, (1 + gamma_0)/2 is an atom; new, proved and checked on
samples); (c) the weights under (P) and sharpness, from base clause (iii): omega(E) = squared norm of E psi Pi over
that of psi Pi; (d) indifference, a premise, giving equal weights on exact orbits only. "Not a derivation of the Born
rule", "the non-contextuality assumption is relocated into (P), not removed", "sharpness is assumed", "physical
states are not shown to be sharp" stand in the formal, technical, lay and one-liner levels.

The new route does **not** cover the stored statement as worded, so the statement is narrowed. Covered: finite
Clifford algebras Cl_k(p,q) over an ordered field with one fixed split; states of (P) sharp on an atom; projectors of
the algebra self-adjoint for that split (in the mode algebras: the squared-overlap rule for all projectors). Not
covered, and said in the Scope:
1. states not sharp on an atom (sharpness assumed);
2. which projectors are outcomes of measurements;
3. the measure over space of the Dirac field: clause (b) is an identity at a point; weights of regions, infinitely
   many modes and a completion are outside a theorem on finite algebras;
4. in Cl(1,3) the atom does not determine the spinor: the atoms of psi and psi gamma_2 gamma_3 are equal (checked)
   while the spin vectors differ, so outcomes acting by right multiplication, the spin projectors among them, are
   not given weights by (c). That spin projectors are of that kind is argued, not proved;
5. the old claim that the squared norm is the ONLY assignment consistent with vacuum indifference: without (P)
   nothing stored excludes another one. The old refutation condition belonged to the envariance route and is
   restated (what can fail is (P), sharpness, or the identification of outcomes with projectors of the split).

The envariance argument (Zurek 2005) is named as prior art in the formal text (with \cite{Zurek2005}), the proof and
the note; the retired Fact's verification record is carried into the note. The fine-graining check is kept as a
comparison with the prior-art route (same numbers as clause (c)); two check functions added.

Retirement: nothing else rested on one-relation.imported-envariance-born-rule (one uses edge, now gone; the other
references were lineage entries and text in files I own, all repointed; store/ text search for the id now finds only
the tombstone, notes of maintainer passes, .tp-lock.json and .tp-layer4.json). Tombstone written **without
`replaced_by`**: the base result does not derive Zurek's theorem, and `replaced_by` makes the tools say "merged
into". This differs from the Haar precedent, where the replacement derived the Fact's content. See "For Leon", 1.

## Dependants whose CONTENT may be affected (not only pins)

- one-relation.record-chain-votes-measurement-without-collapse: edited (above).
- pred.no-objective-collapse (pins the record chain @7): content not affected (no weights in it); pin only.
- The five stored results that assume (P)@1 and were not edited: synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate,
  synthesis.signatures-in-which-commuting-observables-exceed-the-chsh-value-two,
  synthesis.chsh-with-parity-even-observables-needs-two-modes-per-party-and-no-klein-twist,
  synthesis.chsh-over-the-rationals-pure-states-on-a-circle-and-the-pell-records,
  synthesis.three-party-trade-off-of-chsh-values-and-the-local-value-two. The premise's clauses are unchanged, so
  these are pins only (repin 1 -> 2).
- Four notes of the T16 paper describe the paper's Born argument as the envariance argument transplanted:
  note.one-relation.setting-prior-art, note.one-relation.setting-introduction,
  note.one-relation.setting-levels-results, note.one-relation.setting-machine-verification. They are the paper's
  prose and were **not edited**; they now differ from the store version of Prop 6.2 (a `locator_divergence` field on
  the entity records this).
- Any document that prints the entity's old title.

## Folder to remove (orchestrator, with git)

- store/claims/one-relation.imported-envariance-born-rule/ (one file, entity.md). Left in place and unedited.

## For Leon

1. Tombstone form. Retired with no `replaced_by` and a reason saying the import was not derived. If a redirect to
   the base result is wanted, add `replaced_by:
   synthesis.born-weights-under-positivity-a-state-sharp-on-an-atom-is-its-trace-functional`; the caveat is in the
   reason either way.
2. The Born account is weaker than before in two ways that only you can accept: it no longer claims uniqueness of
   the squared norm under indifference, and it does not reach the measure over space or spin outcomes (items 3 to 5
   above). T16 Prop 6.2 as deposited has the envariance route, so store and paper now differ.
3. The record-chain vote was edited (v8), minimally. I did not add a direct assumes edge to (P) there: it enters
   through the Born account. Whether the vote should carry (P) as its own premise is yours to decide.
4. The box theorem got more than a new title: its lay level said the box gives sensible probabilities "for every
   experiment the two parties can actually perform" and fails "never within a single experiment", which the
   local-weights result contradicts, so lay, technical, one-liner and a formal scope paragraph were restated (v2).
5. op.positivity-of-values: `entities` is capped at eight, so the list now holds the premise, the CHSH base and the
   six new results; the box theorem, the signatures, Pell, three-party and parity-even results and the flag premise
   left the list (all still cited in `known` or `attack`). Attack items: 1 narrowed, 2 and 3 answered in part,
   4 done, one new item (Gleason over Q in size four). Status stays open.
6. A small mismatch found: the local-weights result calls its box functional "the functional of" the box theorem,
   but the two are built at configurations with the two settings of each party in opposite order (C_0 and C differ
   as elements). Nothing depends on it; a phrase in local-weights clause (iii) now says so.
7. The premise (P) carries lineage entries to results that assume it (the existing pattern there); layers 1-3 accept.

## Not done

- No edit to the five (P)@1 dependants, to pred.no-objective-collapse, to the T16 notes, to labels.yaml or to the
  lock files.
- `amendments` entries were not written for the version raises: earlier maintainer passes did not write them
  (maintainer_pass note plus credit entry instead), and layers 1-3 do not ask for them.
