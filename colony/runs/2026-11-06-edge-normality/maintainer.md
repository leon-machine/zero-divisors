# Maintainer pass after run 2026-11-06-edge-normality (by: maintainer-2026-11-06)

Validation: `python3 -m tp check --store store --layers 1,2,3 --keep-going --author leon`, before and after: 0 errors,
0 warnings (baseline also 0/0). No check.py was changed. Coverage records changed for A and B, so I ran
colony/check4.py once each on A, B and blade-square, one at a time: 0 errors, check result pass for all three; the new
premises show as I405 (excused). Not run: tp repin, tp lock, tp build, the full check. Nothing committed.

## Created (new imported Facts, version 1, proposed_by ai/maintainer-2026-11-06, ai_involved 'yes')
- synthesis.imported-buchholz-florig-summers-geometric-modular-action-and-modular-stability (new -> 1): CGMA (a)-(d), Modular Stability, Props 3.5, 3.6, and "CGMA does not imply a ground state". Checked by me against the arXiv text; journal data (LMP 49 (1999) no. 4, 337-350, DOI 10.1023/A:1007695205044) and BS1993 against Crossref.
- synthesis.imported-loewner-theorem-and-yafaev-hankel-sign-criterion (new -> 1): Loewner's bibliographic data checked (Crossref), statement from memory. Yafaev: Anal. PDE 8 (2015) 183-221 (Crossref); abstract checked. **Finding:** the Laplace-representation theorem is Theorem 4.7 in the arXiv version but Theorem 4.9 in the journal version (in the journal, 4.7 is a different result). Both numbers are now recorded in the Fact, and in A's locator and proof.
- synthesis.imported-modular-conjugation-of-the-chiral-fermi-field-is-the-twisted-reflection (new -> 1): BGL1993 (Bisognano-Wichmann for conformal nets) and BJL2002 (twisted duality M(q)' = Z M(q^perp) Z*), with abstracts and Crossref data checked. Clause (c), the field-level twisted reflection with a constant phase, is cited from memory, and the value of the phase is excluded from the Fact.
- synthesis.imported-real-clifford-algebras-as-twisted-group-algebras-and-the-arf-invariant (new -> 1): Ovsienko arXiv:1601.07664 (Prop 3.1 twisting function, Theorem 1, the Arf remark), checked on arXiv. Elduque and Rodrigo-Escudero, AACA 28 (2018) no. 2, art. 41, DOI 10.1007/s00006-018-0862-y, checked against the Zaragoza repository record. No journal reference was found for Ovsienko.

## Changed
- synthesis.imported-powers-stormer-takesaki-disjointness 2 -> 3: added clause (d), Araki's purity criterion (pure iff the symbol is a projection), with an Araki1970 entry (Crossref-checked, DOI 10.2977/prims/1195193913). The statement is checked only secondhand: Keyl-Matsui-Schlingemann-Werner math-ph/0604071 Sec. 6.1 has both directions in self-dual form; Boeckenhauer hep-th/9407079 Sec. 3.1 has the "if" direction. The locator within Araki was not checked. Title shortened (E124), and a version-3 credit entry added (W221). Clauses (a)-(c) unchanged.
- synthesis.n-plus-null-ground-state 9 -> 10 (postulate status kept; Leon's decisions 1-3):
  - (a) The statement now says the affine null translations act on the fields by parallel transport, i.e. the zero flat connection on K (as already defined). A new "two data the premise supplies" paragraph says this excludes the Fermi seas, citing B (ii), (iv).
  - (b) A marked 6 November note records field-level geometric modular action, at cuts whose differences generate a dense subgroup with eta = -1, as an equivalent stationarity-free form within gauge-invariant quasi-free states (citing A (iv), (v), converse imported). It says the form can be posed, but is not derived, on the eternal hole, and that net-level forms are excluded (citing B). The technical level has a matching parenthetical.
  - (c) The orientation of i relative to time (null vacuum versus filled positive-energy sea) is named as a datum (N+) assumes and the series does not fix. i = I_4 is not adopted.
  - Technical, lay and one-liner each got a sentence. Version-10 credit entries added (Leon: decisions; Claude Opus 5.5: drafting).
- synthesis.geometric-modular-conjugations-on-a-generator-give-the-null-ground-state 1 -> 2:
  - main now uses the Loewner/Yafaev, chiral-Fermi and BFS Facts @1, and Powers-Stormer @3.
  - Formal, status line and proof (Steps 2, 5, 7, 8(d)) cite them with \claimref, and B with \claimref instead of plain text.
  - imported_from locators updated; purity and converse flags updated.
  - coverage.yaml untouched_premises: entries added for the three new Facts.
  - Statement, proof argument and check unchanged.
- synthesis.modular-data-on-a-generator-fix-neither-the-translation-lift-nor-the-sign-of-i 1 -> 2:
  - main now uses A@2 (the vacuum's phase from A's Step 4), the chiral-Fermi Fact, the BFS Fact, and Powers-Stormer @3.
  - Plain-text "field-level result filed alongside" replaced by \claimref to A in formal, technical, status and proof.
  - coverage.yaml: three untouched_premises entries added, and the "filed alongside" wording fixed.
  - Lay sentence "The mirror data acting on the fields themselves do fix both pieces of information" changed to say they fix the lift and record the orientation as a sign that must be assumed. This was referee P's wording, but it contradicts Leon's decision 3. Revert if unwanted.
- synthesis.blade-square-signs-f2-quadratic-form 1 -> 2: added a `standard-route` derivation (proof-standard-route.tex) using the Ovsienko/Elduque Fact. This follows the store's standard-route pattern, so W405 is exempt (I405 confirmed). The extraction note now names the Fact instead of "verified by the referee". Statement, main proof and check unchanged.
- store/open_problems.yaml, op.r-premises-external (status stays reformulated):
  - `source` extended; a dated 6 November paragraph appended to `known` (A's equivalent form, net-level routes closed by B, the two data, the A^G remark).
  - New first `attack` item: derive field-level geometric modular action, or the ground-state clause, plus the sign datum; net-level routes closed. It points to the wedge-reflection result as a place to look.
  - `success` extended: A does not meet it; a no-go must reach beyond net level.
  - A and B added to `entities`. To keep the header's 2-8 limit I removed synthesis.imported-kay-wald-uniqueness-and-no-go and synthesis.attachment-conformal-energy-is-generated-by-z; both are still \claimref'd in `known`. Restore them if Leon prefers 10 entities.
- op.null-positivity-curved-horizons: `source` extended. One sentence appended to `statement` and a dated paragraph to `known`: item (ii) is restated as field-level CGMA_{-1} on the generators, posed but not derived on the eternal hole, with the orientation entering as the assumed eta = -1; net-level conditions cannot give it. Item (ii) stays open; entities unchanged.
- Retired: none.

## Dependants whose content may be affected
- (N+) v10: assumed by synthesis.positive-null-energy-gives-r-premises (pins @9), and through it the (N+) holds-given cone (layer 1-3 counts 34 claims and 3 documents behind all the entities changed in this pass). What (N+) asserts is unchanged (nu was already the plain translation), so moving the pin should be a formality.
- Powers-Stormer v3 (clause added; (a)-(c) unchanged): pinned @2 by synthesis.local-normality-at-the-edge-gives-the-null-ground-state, synthesis.microlocal-condition-on-a-generator-gives-the-local-null-ground-state, synthesis.normality-on-the-closed-generator-gives-the-vacuum-folium-not-the-ground-state and synthesis.tower-charge-sector-label-temperature-not. For them repinning is a formality.
- A v2: now pinned @2 by B. No other dependants of A, B or blade-square.

## Not done, and why
- Repin, lock, build and the full six-layer check: not done, as instructed.
- Referee P's optional line on (N+) about the A^G observation (the Fermi seas are ground states on the gauge-invariant observables): this was marked a decision for Leon, and DECISIONS.md does not take it. It appears only in the op.r-premises-external `known` text.
- Pre-existing W413 on B (check_fermi_sea_is_a_local_gauge_transform_of_the_vacuum: 5 of 8 perturbations pass; already in the fix-round check4 log). No check was changed.
- Store text from the run, not on my edit list, left unchanged:
  - All five accepted entities carry `credit.source: run 2026-11-06-edge-normality`. Presumably `tp credit` normalises this at commit to the Co-Authored-By form.
  - synthesis.nilpotent-steps-derivative-exponential-and-boost says "(the referee's construction)".
  - note.one-relation.two-presentations-differ-over-the-integers says "on referee advice" and "the referee recomputed it". It also names the withdrawn draft id synthesis.hyperbolic-plane-integral-orders-and-partner-inverse, which is not in the store.
  - The id synthesis.nilpotent-steps-* is kept, as accepted.
- Still from memory: Loewner's statement; the circle-net form of BGL and the field-level clause (c) of the chiral-Fermi Fact; where in Araki's paper the purity criterion stands; Buchholz-Summers 1993 content.
- Noticed, not changed: A's formal (v) gives the modular group as the boost at rapidity -2 pi t, while B's proof set-up says 2 pi t. This is probably a sign convention for t, but it is worth a look.
