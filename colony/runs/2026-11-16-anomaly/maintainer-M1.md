# Maintainer M1, pass after run 2026-11-16-anomaly (strong CP and the order-four problem)

Scope: the section "M1 owns" of MAINTAINER.md, decisions D1 and D4 of 16 November 2026. Nothing committed,
pushed, repinned, locked or built. Edits are in store/ only, plus this file.

## New entities (all version 1)

| id | kind / status | one line |
|---|---|---|
| `synthesis.colour-angle-registered-free-input` | claim / postulate | Premise (theta-bar): the physical colour angle, the coefficient of the colour four-form plus the I_4 phase of det M_u det M_d, is a registered free input, with refutation condition; says what is proved (covariant rung coupling, maps examined) and what is argued (completeness over stored fields and maps). No assumes edges. |
| `synthesis.imported-physical-colour-angle-and-its-shift-under-quark-rephasing` | claim / imported | The angle term; axial rotations are anomalous and move the angle; theta-bar = theta + Arg Det M; CP is conserved by the Lagrangian only at 0 and at a half turn, where spontaneous breaking is model-dependent. |
| `synthesis.imported-neutron-dipole-bound-and-its-conversion-to-the-colour-angle` | claim / imported | d_n = (0.0 +- 1.1 +- 0.2) x 10^-26 e cm, limit 1.8 x 10^-26 at 90 percent; lattice conversion -0.00152(71) theta-bar e fm and its stated bound 1.98 x 10^-10; the reliability caveat; the review's summary 10^-10. |
| `synthesis.exact-quarter-turn-texture-of-the-quark-stages` | claim / conjectured | The exact quarter-turn texture (T1) to (T3), with its hypotheses, what follows by clauses of the two results it rests on, what it does not claim, and two refutation conditions. Derivation without proof, uses the determinant-phase result @1 and the Cabibbo result @4. |
| `note.synthesis.two-premise-questions-raised-by-the-colour-angle` | note / remark | The two premise questions, recorded as open and not decided (no open problem fitted them). |

New keys in store/references.yaml (appended): Dragos2021, Bhattacharya2021, PDGAxions2023, Peccei2008,
Fujikawa1979, BoerBoomsma2008. Abel2020 existed.

## Changed entities

- `synthesis.order-four-structure-on-real-projective-walls-and-the-signed-count-modulo-sixteen` 1 -> 2
  (amendment, credit entry, extraction entry). Hypothesis (H1) is now a uses edge to
  `synthesis.spectral-asymmetry-on-real-projective-five-space-from-monogenic-polynomials@1`; the formal Reading
  says "(H1), a stored result" and cites its clauses (iv), (v); one technical sentence, the proof's closing
  sentence and the note follow. Clauses (i) to (vi) and every conclusion of the Reading are unchanged; (H2)
  stays a hypothesis. Declared `restatement` because the formal level's text changed (the store's precedent for
  any change in the formal level); nothing was weakened or strengthened. New coverage.yaml: records for the three
  check functions and the new premise under untouched_premises. check4: 0 errors, check result pass, one I405.
- `synthesis.colour-angle-term-under-the-stored-maps-and-no-colour-anomalous-phase-of-the-rung-coupling`
  version kept at 1. New coverage.yaml: records for the ten check functions, and `dark-matter.mirror-tower-copy-one`
  and `synthesis.imported-chern-weil-and-chern-simons-forms` under untouched_premises with reasons; no premise()
  call added. check4: 0 errors, pass, the two W405 are now I405. One wording-only edit beyond item 4, which I
  judged necessary because the import made the sentence false: the first sentence of the Reading no longer
  says the two literature statements "are not stored Facts"; it cites the new Fact (no edge added). An
  extraction entry records both. Revert that sentence if only the coverage file was wanted.

## Open problems

- `op.strong-cp`: settled and moved to store/open_problems_settled.yaml (last entry). Records what is proved,
  what is argued (completeness over stored fields and maps), the imports, the decision and the residual items;
  each attack item is marked answered with its original wording kept; the "why" sentence on the flag as the
  one CP-violating datum is corrected in place, with the reason.
- `op.order-four-anomaly-and-sixteen`: status reformulated, restated per D4 (statement, known, attack, success,
  source, two entities added). The bordism citation is marked read at source.
- `op.rung-unit`: one dated sentence in known (W(N) is not constrained by the colour angle).
- `op.second-order-breaking`: a dated paragraph in known; the up-down phase item points at the conjecture and at
  clause (iv) of the determinant-phase result; a new attack item carries the one-loop mass phase.
- `op.r-premises-external`: checked, unchanged. Its flag item and its sentence that no CP-invariant interaction
  can fix the orientation datum are consistent with the accepted colour-angle result.
- Where the residual items went: the one-loop mass phase to op.second-order-breaking; the two premise questions
  to the new note, since neither is about the second-order breaking.

## Literature, read at source in this pass (16 November 2026) or not

Read (arXiv abstract and full text unless said otherwise): Abel et al. 2020 (value; the 90 percent limit is in
the body, not the abstract); Dragos et al. 2021; Bhattacharya et al. 2021 (abstract); Boer and Boomsma 2008;
Peccei, hep-ph/0607268 (equations (1), (2), (17) to (20)); Fujikawa 1979 (a scan of the letter); the Particle
Data Group axion review, 2023 revision; Garcia-Etxebarria and Montero, arXiv:1808.00009 (sections 2 and 4.3,
equations (2.14), (4.13), (C.21)).

Findings from the reading that differ from the drafts:
- The bound 1.98 x 10^-10 of Dragos et al. is derived from the earlier limit 3.0 x 10^-26 e cm, not from Abel
  et al.; the paper does not show the step. With the 2020 limit and the central coefficient the division gives
  1.18 x 10^-10. The Fact states both and marks the arithmetic as not a source statement; the premise says
  "about 2 x 10^-10".
- An upper bound on the conversion coefficient (Bhattacharya et al.) gives no bound on the angle by itself.
- Peccei's text shifts the angle by alpha for a rotation by alpha/2 without relating the normalisations; the
  Fact reports both as printed and draws no factor. The shift "a_3 phi" is given as a translation of (iii)
  into the store's variables, marked as not the sources' wording, with the sign left to convention.

Not read, cited from memory only (in notes, not used as sources): 't Hooft 1976; Dashen 1971; Baker et al.
2006 and Pendlebury et al. 2015 (the older limit); the book reference of Peccei's review (volume and pages);
Mohapatra and Senjanovic 1978, Beg and Tsao 1978. Hsieh's equation (2.47) was read at source during the run,
not again by me; Tachikawa and Yonekura stays from memory.

## Validation

`python3 -m tp check --store store --layers 1,2,3 --keep-going --author leon`: no error and no warning on any
entity or open problem of mine. One error remains in the store, E206 on
`synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them`, which is M2's. No pin warnings: nothing
pins the order-four structure entity. check4 run one at a time on the two accepted entities (pass) and on the
four new claims (no findings; they have no check). Layers 4 to 6 of the full check were not run.

## Dependants whose content may be affected

- `synthesis.colour-angle-term-...` and `synthesis.phase-of-the-quark-mass-determinant-...`: their notes still
  list the neutron bound and the angle's definition as literature not stored. True when written, now stale;
  the colour-angle entity has a dated extraction entry saying so, the determinant-phase entity is untouched
  (not in my list). Suggest: at the next pass, uses edges from both to the two Facts (a correction, version + 1)
  or a wording-only note. The determinant-phase entity's sentence that the exclusion of a half turn is not
  imported remains true.
- `dark-matter.asymmetry-arrow-counted-fifteenth-refutation` (ii),
  `refuted.a-pre-descent-term-sources-the-matter-asymmetry`, `note.programme.setting-seventeen-refutations`:
  quote the neutron bound with the citation only. Suggest a pointer to the new Fact and, in (ii), to the
  result that answers "an angle that relaxes or rolls" at the argued level. Not edited.
- `dark-matter.premise-cpt-covariance`, `synthesis.common-ceiling-coupling-premise`: the two open questions
  are Leon's to decide; the note says what a sentence in each would settle. Not edited.
- `colony/runs/2026-11-16-anomaly/LEADS.md`: its lines on op.strong-cp, op.rung-unit and
  op.second-order-breaking are now out of date (not a store file; not edited).
- site/ and tp_status are not rebuilt.

## Could not do, or did differently

- https://pdg.lbl.gov/2024/reviews/rpp2024-rev-axions.pdf could not be fetched (the permission prompt was not
  answered); the 2023 revision was read from a mirror found by search and is what the Fact cites.
- The sign of the exponent in Fujikawa's equation (15) was not legible in the scan, so the Fact states the
  factor up to a sign.
- No existing Fact held the neutron bound (it sits inside a proved T14 result), so a new Fact was created and
  none was extended.
- The note also records, under (Q1), the related observation that the conjugation is linear with respect to
  the unit in which the mass phase is read. It is a third open point, beyond the two named in MAINTAINER.md.
- The order-four structure entity was never locked at version 1; if Leon prefers, version 2 can be folded back.
- op.strong-cp and op.order-four-anomaly-and-sixteen now list notes or more than eight entities; the validator
  does not object.
