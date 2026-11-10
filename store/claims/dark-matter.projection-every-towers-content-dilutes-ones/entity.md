---
id: dark-matter.projection-every-towers-content-dilutes-ones
kind: claim
version: 3
title: 'Projection: every tower''s content dilutes as this one''s'
status: proved
region: dark-matter
subject: dark-matter
tags: [matter-asymmetry]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14, deposited version
review: typed
derivations:
- name: main
  assumes:
  - dark-matter.p1-single-frozen-point@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T14.py
  tags:
  - label:lem:projection
- kind: check
  ref: check.py::check_projected_dilution_matches_this_tower
- kind: check
  ref: check.py::check_single_sheet_reading_is_excluded
locators:
  paper: T14
  number: Lem 6.1
  label: lem:projection
  line: 542
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: projected matter and radiation densities a^-3 and a^-4 for D = 2, 3, 4, co-expanding or static, at exact sample scale factors; single-sheet reading a^-2, a^-3. Version 2 -> 3.'
  typing:
    by: ai-typing-pass
    note: 'Kept the P1 assumption; the reduced-response proposition is cited only to justify the sheets
      moving in perturbations, which the background dilution does not use, and it already uses this lemma,
      so it was not added. Levels pass: the lay level now names P1 and the co-expanding-or-static and
      sheet conditions, which the one-liner also gains.'
  env: lemma
  context_refs:
  - dark-matter.reduced-response-gravity-needs-supporting-stress
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-matter.p1-single-frozen-point
---

## formal
Read Premise \claimref{dark-matter.p1-single-frozen-point} as the sourcing rule: the one metric is the four-dimensional one, a tower shares its three spatial directions and its time, and the tower's contribution to the metric's source is its energy per unit of the shared three-volume, its content taken homogeneous along every direction it has. Then, for a tower of any dimension, with the extra directions (if any) either co-expanding with the shared scale factor $a$ or static, and with a missing shared direction (the three-dimensional towers, which contain two of the three shared spatial directions) filled by a family of sheets, comoving in the background and displaced with the matter in perturbations (Proposition \claimref{dark-matter.reduced-response-gravity-needs-supporting-stress}), one per unit of comoving length along the missing direction, the projected energy density of non-relativistic matter dilutes as $a^{-3}$ and that of radiation (the zero modes along any static extra direction) as $a^{-4}$, exactly as in this tower. No tower is diluted away or into prominence relative to this one.

## technical
Read Premise P1 as the sourcing rule: a tower contributes to the one four-dimensional metric its energy per unit of shared three-volume, its content taken homogeneous along every direction it has. Suppose any extra directions either co-expand with the scale factor $a$ or are static, and a missing shared direction (in the three-dimensional towers) is filled by a comoving family of sheets, one per unit comoving length. Then the projected density of non-relativistic matter dilutes as $a^{-3}$ and that of radiation as $a^{-4}$, exactly as in this tower.

In the co-expanding case the density per $D$-volume goes as $a^{-D}$ for matter and $a^{-(D+1)}$ for radiation, and integrating over $e = D - 3$ extra directions of length proportional to $a$ restores $a^{e}$. A single sheet of fixed thickness would instead give $a^{-2}$ and $a^{-3}$, violating the rule's homogeneity clause. No tower is diluted away or into prominence relative to this one.

## lay
Hidden sectors with more or fewer dimensions than ours might thin out at a different rate as the universe expands, which would make them fade away or come to dominate. This result shows that, under the paper's rule for how such sectors feed gravity (its reading of Premise P1, one shared metric), provided any extra directions either grow with ours or stay fixed in size, and with a sector that lacks one of our directions counted as a family of evenly spaced sheets, their matter and radiation thin out exactly as ours do. Their share relative to ordinary matter therefore stays fixed over cosmic time.

## one-liner
Under the sourcing rule read from P1, with any extra directions co-expanding or static and a missing direction filled by comoving sheets, every tower's projected matter dilutes as $a^{-3}$ and its radiation as $a^{-4}$, as in this tower.
