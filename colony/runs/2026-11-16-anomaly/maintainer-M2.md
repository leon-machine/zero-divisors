# Maintainer pass M2 (the asymmetry), run 2026-11-16-anomaly

Scope: section "M2 owns" of MAINTAINER.md, decision D3. Nothing committed, pushed, repinned, locked or built.

## 1. Entities created

| id | version | what |
|---|---|---|
| `synthesis.imported-anomalous-weak-process-changes-b-plus-l-and-keeps-b-minus-l` | new, 1 | Fact (a): each left-handed doublet's fermion number changes by N[A], so Delta B = Delta L = 3 N[A] for three generations (B - L kept, B + L violated); the process is faster than the expansion for T_c < T < about 10^12 GeV. With a reading: a charge changes by A_2(X)/2 per generation. |
| `synthesis.imported-equilibrium-baryon-number-as-a-fraction-of-b-minus-l` | new, 1 | Fact (b): Khlebnikov and Shaposhnikov eqs. (17) to (19), the Debye mass (12), the counting rule, where the relation is taken; the closed forms of Harvey and Turner; the conventions under which the theorem's Gram ratio reproduces them. |
| `synthesis.imported-lattice-crossover-and-freeze-out-of-the-anomalous-weak-process` | new, 1 | Fact (c): crossover T_c = 159 +- 1 GeV, rate in both phases, freeze-out T_* = 131.7 +- 2.3 GeV with its criterion. |

Three Facts, not one: three sources of different standing (a selection rule, an equilibrium relation, a lattice
number), each pinned by a different clause. Also new: `coverage.yaml` in the theorem's folder; six keys appended to
`store/references.yaml` (tHooft1976, KuzminRubakovShaposhnikov1985, RubakovShaposhnikov1996, HarveyTurner1990,
KhlebnikovShaposhnikov1996, DOnofrioRummukainenTranberg2014), by one read-modify-write.

## 2. Entities changed

| id | version | what |
|---|---|---|
| `synthesis.conditional-inheritance-of-b-minus-l-and-the-conversion-coefficient-as-a-gram-ratio` | 1 -> 2 | Three uses edges (the Facts), three assumes edges (Premise (R)@1, real breaking@2, the registered premise@6). Formal: (A) "literature and not stored" -> "imported (Fact ...)", with the colour process marked as not part of the Facts; (v) and (vii) cite the Facts. No clause, hypothesis or conclusion changed. Proof cites the six new premises. Check: four `premise()` lines (the three Facts and Premise (R), each where its content is used). Amendment kind `restatement` because the formal text changed (the tooling's definition); in substance it is a change of links. |
| `synthesis.matter-asymmetry-registered-free-input` | 5 -> 6 | Restated per D3: one light doublet on the level branch (argued), (B - L)/s between 2.45e-10 (symmetric-phase end, 28/79, where the stored mirror check sits) and 2.68e-10 (broken-phase end, 12/37), conditional on the three Facts, on the doublet count and on equilibrium after the descent (hypothesis (T), not shown). Premise, naming and refutation condition unchanged. No edge drawn from it. |
| `synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them` | 1 kept | Wording: last sentence of (v), two citations in (vi), one technical sentence now cite the Facts by claimref (text only). |
| `op.matter-asymmetry-origin` | partial, kept | source, statement, known ((g), (h) corrected; new (i), (j), (k); "what is not stored" rewritten), attack (items 2, 3, (a), (e) updated; new (W), (T), (Gr); relaxing angle answered), entities (+ the theorem). |
| `op.qft-structural-inputs` | kept | One sentence in known under the doublet count, with the theorem's id. |

`dark-tower-matter.mirrors-composition` is not touched.

## 3. Validation

- `tp check --layers 1,2,3 --author leon`: one finding on my entities, **E206** on the abelian-charges result
  ("substantive fields changed without a version bump"). It is the consequence of the rule "a wording-only change
  keeps the version": the lock hashes the formal level. It clears at `tp lock`. The alternative, version 2, would
  break the pins of the theorem and of M1's colour-angle result. Left as instructed; the orchestrator decides.
- `runcheck.py` on the theorem's check: 7 of 7 pass. `check4.py` on its folder: 0 errors, 2 information findings
  (I405, the two postulates excused in coverage.yaml). No W405, no W124.
- No pin warnings: nothing pinned the registered premise before; nothing pins the theorem.
- Layer 5 run alone (27 s, not the full check): nothing on my entities. Three W503 on M1's accepted results
  (order-four structure, one-liner; spectral asymmetry, technical and lay), for information.
- The theorem was accepted but never locked, so the lock holds no version 1 of it.

## 4. Literature: what was read at source, and how

All reading was through the web fetch tool, which returns an extraction of the page or PDF, not the file: direct
download is refused by the proxy. Formulas are therefore transcriptions by that extraction. Cross-checks made: KS
(17) reduces to (18) and (19); its phi/T = 1.2 to 1.5 matches its own m_W^2/m_D^2 = 0.2 to 0.3 through eq. (12)
(0.196 to 0.307); the Gram ratio reproduces (18), (19) on n_f = 1..6, n_s = 0..6 in exact arithmetic.

Read: 't Hooft, PRL 37, 8 (abstract, publisher's page). Rubakov and Shaposhnikov, hep-ph/9603208, eqs. (2.2) to
(2.5), section 3, reference list. Khlebnikov and Shaposhnikov, hep-ph/9607386, eqs. (6), (12), (14), (16) to (19)
and the paragraph after. Harvey and Turner: abstract (publisher's page and index record) and the scanned March
1990 preprint. Kartavtsev hep-ph/0511059 eq. (13a); Buchmuller hep-ph/0101102 eqs. (10), (53). D'Onofrio,
Rummukainen and Tranberg, arXiv:1404.3565, abstract and eqs. (2), (7), (8), (9). Arnold and McLerran 1987
(attribution only).

**Not read**, and said so in the Facts:
- Kuzmin, Rubakov and Shaposhnikov 1985: neither text nor abstract. The publisher's DOI page and the INSPIRE
  record were blocked (permission prompt not answered); open records carry no abstract. Clause (b) of the first
  Fact is stated as the 1996 review of two of its authors states and attributes it.
- The body of the published article of Harvey and Turner. Its closed forms are stated as three sources read quote
  them.

## 5. Findings at source that bear on stored text (for Leon)

1. The March 1990 preprint of Harvey and Turner does not carry the quoted closed form: as far as the scan reads,
   its eq. (9) is (16N + 4m)/(44N + 13m), which is the same Gram ratio with one per boson state in place of two
   (52/145 at N = 3, m = 1, against 28/79). Recorded in the Fact's provenance note.
2. Khlebnikov and Shaposhnikov attribute the symmetric form (18) to their 1988 paper and the form (19) to Harvey
   and Turner, Dolgov, Dreiner and Ross, Nelson and Barr; Kartavtsev and Buchmuller attribute 28/79 to Harvey and
   Turner. The theorem's note attributes both to Harvey and Turner; not changed.
3. Khlebnikov and Shaposhnikov say what decides between the two ends is phi against T, not T against T_c, and that
   for a crossover (17) is to be used at phi/T of about 1.2 to 1.5, "roughly midway". On that estimate c is 0.341
   to 0.344 and (B - L)/s is 2.53e-10 to 2.55e-10 (my arithmetic, **not stored**; the lattice paper gives no
   phi/T at T_*). The Fact records the source's sentence (clause (f)); the premise keeps the full bracket of D3.
   Narrowing it is a decision.
4. "About 10^12 GeV" in hypothesis (A) is now sourced (review, section 3) and no longer from memory.

## 6. Dependants whose content (not pins) may be affected

All four carry wording that calls the process or the coefficient "not a stored Fact" or leaves the doublet count
open. None is mine; none was edited. Suggested: wording-only updates citing the Facts.
- `dark-matter.stored-asymmetry-charge-not-number`: "(a coefficient that is not a stored Fact, 28/79 for one light
  doublet and 8/23 for two)" and "(not a stored Fact)".
- `synthesis.baryon-number-centraliser-in-the-five-mode-algebra`: "(literature cited from memory, not a stored
  Fact: 't Hooft 1976; Kuzmin, Rubakov and Shaposhnikov 1985)".
- `synthesis.mirror-temperature-measures-deposit-under-r`: "c ... (not a stored Fact; 28/79 for one light doublet,
  8/23 for two)"; its charge per unit entropy is now the bracket.
- `dark-tower-matter.mirrors-composition`: its note calls the doublet count an open attack item. The check stays
  (decision of 12 November); the note could say it sits at the symmetric-phase end. Whether its check should
  `use` the equilibrium Fact is Leon's call.
- The theorem's own `extraction.note` still says "not imported" and "no assumes edges"; the new maintainer entry
  states that it replaces those sentences. The note itself is kept as the record of the proposal.

## 7. Not done, and why

- Kuzmin, Rubakov and Shaposhnikov 1985 and the body of Harvey and Turner 1990 not read (section 4).
- The colour anomalous process ("likewise the colour four-form and A_3") is not imported: D3 does not name it.
  Hypothesis (A) now says so.
- The washout estimate (Fukugita and Yanagida) and gravitational-wave leptogenesis stay cited from memory in (W)
  and (Gr): not named by D3.
- No rate, no thermal history, nothing computed beyond the exact cross-checks above.
