---
id: note.synthesis.residue-and-the-prediction
kind: note
version: 2
title: The residue, the s-wave weights and the boundary-mode prediction
status: remark
subject: entropy
proposed_by:
  kind: ai
  session: residue-2026-10-22
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
comments_on:
- pred.boundary-mode-density
- scrambling.residue-each-convention
- singularity.q-joint-quasi-freeness-s-wave
- synthesis.residue-from-mode-entropy
extraction:
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: >-
      Version 1 -> 2, note only, text unchanged. The note records the residue under Premise (Q) version 2,
      weights kappa k. Premise (Q) version 3 (Leon's decision of 23 October) takes kappa(k + 1/2), adopted
      with the reading of the modes as spinor fields of boost weight 1/2 under (N+), not derived. At that
      offset the one weight assignment the series makes does give the registered value under one reading of
      the count: one array carries exactly (1/2) ln 2 (synthesis.half-integer-weight-array-carries-half-ln2),
      so two arrays per registered mode give 1/(4 ln 2), about 0.3607, with no zero-weight mode. This rests
      on the area-law hypothesis and on an offset fixed by decision, so it neither meets nor fails the
      prediction's kill condition and is no confirmation of it. The note's statements that (Q) does not give
      the registered value, and that a derivation fixing the weights as (Q) does would refute (IC), apply to
      version 2's weights.
  note: Records, beside the registered prediction, what the attempt of 22 October 2026 found. The prediction itself is unchanged.
---

## formal
The calibration residue was not derived (Theorem \claimref{synthesis.residue-from-mode-entropy}). Under the area-law hypothesis it is the reciprocal of four times the counted modes' mean thermal entropy, so the registered value $\kappa_{c} = 1/(4\ln 2)$ of Prediction \claimref{pred.boundary-mode-density} is the case in which every counted mode has zero Killing weight. The one weight assignment the series makes, the s-wave convention of Premise \claimref{singularity.q-joint-quasi-freeness-s-wave}, does not give that value under any reading of which modes are counted. Counting arrays gives $0.3470$ against $0.3607$, about four per cent low; counting every mode drives the residue up without bound; counting only the zero-weight modes leaves $0.0272$ nats per array outside the area law. Since (Q) is adopted for one step only and the result is a conditional reformulation, this neither meets nor fails the prediction's kill condition. It does mark where the prediction is exposed: a derivation that fixed the weights as (Q) does would return a residue other than the registered one and so, by the kill condition, refute the intrinsic-clock premise (IC).

## technical
pending

## lay
pending

## one-liner
pending
