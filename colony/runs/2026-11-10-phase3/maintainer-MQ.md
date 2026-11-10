# Maintainer MQ, run 2026-11-10-phase3: quantum field theory and the graviton position

Scope: section MQ of MAINTAINER.md (Q1 to Q7). Nothing committed, pushed, locked, repinned or built. No folder
is to be removed on my account.

## Validation

- Layers 1-3 (`tp check --layers 1,2,3 --keep-going --author leon`): 1 error, 0 warnings. The one error is
  E205 on dark-matter.p4-democracy-asymmetry-over-oriented-towers (the retirement of section MM: the folder is
  still present). Nothing on my files. Baseline before the pass was 0 errors, 0 warnings.
- store/open_problems.yaml parses (38 problems); every claimref and entity id in my two entries resolves.
- Checks changed and rerun: the curved-field kernel result (one `premise()` line added): runcheck 6 of 6 pass,
  check4 0 errors, pass. The one-loop self-energy and vertex result (assumes edge, coverage entry, one proof
  sentence; check.py unchanged): runcheck all pass, check4 0 errors, pass.
- Not run: full check, layer 4 across the store, repin, lock, build.

## Entities changed (old -> new version)

Version raised (each has a credit entry and a `maintainer_pass_2026_11_10*` note):
- synthesis.vacuum-polarisation-kernel-on-a-gravitational-field-has-the-flat-leading-part-and-no-weyl-term-of-degree-four
  1 -> 2. Protraction identity cited as the stored theorem (uses edge, claimref in formal and proof, premise()
  in the check); statement adds that the identity alone does not give vanishing torsion; clause (iv) now says
  two transverse local covariant extensions differ by Z_3 and existence is not proved, stays argued as a whole;
  the first Hadamard transport equation is confined to one coefficient at degree four of clause (iii).
- synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator-and-ward-preserving-extensions-differ-only-by-the-renormalisation-constants
  4 -> 5. Clause (v) likewise (cites the kernel and freedom results and the local-covariance Fact by name, no new
  uses edge since those results depend on this one); clause (iii) records the Euclidean one-loop pair as
  supporting, not discharging, the import; the flag on imported existence kept and reworded; floors "excluded
  as a covariant regulator, not as a cut-off whose limit is shown to be covariant" (technical and note).
- synthesis.imported-local-covariance-with-scaling-of-time-ordered-products 1 -> 2. Sourcing: scalar-field
  scope in the clauses; the 2001 paper proves uniqueness and defers existence of the time-ordered products to
  the 2002 paper; regularity reworded from "smooth dependence" to continuity under smooth variations plus
  analytic dependence; Zahn arXiv:1210.4031 and arXiv:1311.7661 added with DOIs, abstract level only. No
  existence statement added.
- synthesis.frozen-point-integrand-gives-einstein-only-with-the-symmetric-slot-frozen 2 -> 3. The one place
  found that wrote "torsion-free (the curvature obeys the first Bianchi identity)" as one condition, in the
  formal statement (twice) and the proof: now "torsion-free; what the proofs use of this is the identity, which
  does not by itself give vanishing torsion". No clause, value or check changed.
- dark-matter.imported-massless-graviton-production-rate 2 -> 3. Flag paragraph at all four levels and an
  `extraction.flags` entry; rate, coefficients and provenance unchanged.
- pred.no-dark-radiation 3 -> 4, pred.no-indirect-dark-signals 4 -> 5, pred.dimmed-evaporation-bursts 5 -> 6.
  One sentence each (formal and technical) pointing to the new open problem. No prediction, status, kill
  condition or number changed.

Version kept (accepted in this run, not in the lock):
- synthesis.curved-field-vacuum-polarisation-freedom-is-five-local-covariant-constants-of-which-one-is-transverse:
  pins moved (kernel @2, flat result @5, local-covariance Fact @2); the sentences calling the identity a
  hypothesis of the kernel result updated; note.
- synthesis.protraction-identity-of-the-curvature-operator-from-vanishing-torsion: note only (where the
  identity is now cited).
- synthesis.one-loop-self-energy-and-vertex-extend-with-the-ward-identity-holding-at-a-common-cut-off-length:
  `assumes` edge to synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields@3, one formal
  sentence, one proof sentence, coverage `untouched_premises` entry, flat result pinned @5.

Notes only, version kept (extraction notes, nothing hashed):
- correspondence.no-real-lorentzian-vacuum-half-flat, interior.filtration-cauchy-horizon-read-literature,
  synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared, pairing.loop-classes-are-weyl-components:
  a note naming the stored protraction theorem.
- synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields: a note that one more result assumes
  it and how its Note of 2 November is to be read.

New:
- store/notes/note.synthesis.scope-of-the-quantum-field-theory-perturbative-on-a-classical-field (Q4).
- store/notes/note.synthesis.where-stored-text-names-a-graviton (the 51 entities, seven groups, each id a
  claimref so the validator checks it).
- store/open_problems.yaml: new entry op.graviton-rate-as-classical-field-process (placed after op.odd-towers);
  op.qft-loops-and-renormalisation edited (source, a second dated paragraph in `known`, attack items 1 to 3
  restated, the protraction item marked done, a new item for the torsion case, four ids added to `entities`).
- store/conventions.md: section "Gravity and the graviton", Leon's text verbatim, before "Working with the store".
- docs/ALGEBRA_CORE.md: one line (follow-up 6) with the identity and its claim id.

## Pins the orchestrator must move

Only one bumped entity has dependants outside my files:
dark-matter.imported-massless-graviton-production-rate @2 -> @3 in
- dark-matter.seeding-gravity-floor-dark-towers-temperature
- dark-matter.coefficients-floors-they-give-what-gravity
- synthesis.untuned-fit-caps-lightest-heavy-neutrino
- synthesis.seeding-remainder-excludes-perturbative-pati-salam
The rate and coefficients are unchanged, so the uses hold as cited; what changed is that the Fact is flagged.
All other pins to my bumped entities are in my own three run entities and are already moved. No stored entity
pins the three predictions or the frozen-point entity.

## Dependants whose content may be affected

- The 30 entities in the future cone of the rate Fact (computed today: 28 claims and the two predictions; the
  decision text says 31). They now rest on a flagged import. None is edited except the two predictions. The
  full list is in the open problem's `known`.
- synthesis.dimmed-burst-time-rescaled-copy: not in that cone; its baseline "this tower plus gravitons" counts
  emission of a quantised field through g. Not edited; named in the open problem.
- The Krein premise's formal list "Results that use it" does not name the one-loop result, and its Note (a)
  still says the regulator-free self-energy and vertex are "imported, not computed". Changing the formal text
  raises the premise's version and touches every result that assumes it, so I left an extraction note only.

## Done differently from the brief, and why

1. Q1 "repoint as citations": for the four entities R3 and the fixer list I added extraction notes, not proof
   text. In three of them the identity is a defining condition on a linear map in a check, and in the fourth it
   is read through the imported dictionary, so no premise is replaced; a claimref in the proofs would have
   raised four versions and their dependants' pins for no change of content.
2. Q1 wording: the equating sentence was in
   synthesis.frozen-point-integrand-gives-einstein-only-with-the-symmetric-slot-frozen, not in the two entities
   the attacker named from memory. synthesis.curvature-only-tractor-actions-are-macdowell-mansouri and
   synthesis.frozen-point-action-is-bf-transport-broken-by-the-blade-i-wedge-x were read: they use the identity
   for a torsion-free field and do not equate the two; unchanged.
3. Q4 prior art: only two items are named, both checked on the web today (Jaffe's survey on constructive field
   theory; Aizenman and Duminil-Copin, arXiv:1912.07973). The draft's other names and literature statements
   (divergence of the series, lattice chirality, Balaban, Gross-Neveu and the rest) are left out because I did
   not verify them. I added item (5), elementary or composite gauge bosons, from the findings' own list.
4. Q2: verified at abstract level for all four papers, plus the first 100 000 characters of the 2001 text
   (scalar-field restriction, continuity and analyticity, existence deferred). Journal volumes and pages of the
   two Hollands and Wald papers remain unverified and the locators say so.
5. Q7 Krein edge: added. The formal statement did not name the premise (only the one-liner did); it now does
   in one sentence.

## For Leon

- Conventions against the store. The new section says results that import a quantised-gravity process "are
  flagged". Only the rate Fact is flagged. Unflagged places of the same kind: the dimmed-burst result (emission
  into gravitons, the term g) and note.standard-model.what-settled-what-gravitational-channel-cannot (graviton
  loops). Two further groups fit none of the three readings: the ontology readings of the dark-energy no-go
  (the graviton as a collective mode, or fundamental) and the Kasner coupled-modes result, whose proof gives
  linear modes of the gravitational field a vacuum state. All are listed in the new note, none edited.
- The one-loop result holds for every gauge parameter, while the earlier pass recorded that clause K1 of the
  Krein premise fixes the gauge parameter at one. With the assumes edge the result is partly outside the
  premise's own reading. I did not restrict it.
- Whether to update the Krein premise's formal list and Note (a) (a version bump with a wide repin).
- The open problem's attack items (operator source beyond the static limit with a Green function of the
  linearised field equations; mean-field source as the alternative) are my framing from the stored operator
  Newtonian coupling. They are routes, not results; nothing is computed.
- op.qft-loops-and-renormalisation now lists 14 entities; the file header says 2 to 8 (it had 10). The
  validator accepts it.
- Existence of a transverse local covariant extension on a gravitational field is still not imported
  (decision pending from the attackers' list); every curved-field statement stays conditional on it.
