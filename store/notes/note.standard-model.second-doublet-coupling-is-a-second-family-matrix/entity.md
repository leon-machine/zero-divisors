---
id: note.standard-model.second-doublet-coupling-is-a-second-family-matrix
kind: note
version: 1
title: The second doublet coupling must be a second family matrix
status: remark
subject: standard-model
proposed_by:
  kind: ai
  session: maintainer-2026-10-26
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
comments_on:
- standard-model.bidoublet-complex
- synthesis.second-doublet-of-one-family-coupling-gives-no-quark-mixing
extraction:
  note: Maintainer note (Leon's decision of 2026-10-26, note only). It records how Proposition standard-model.bidoublet-complex is to be read in the light of synthesis.second-doublet-of-one-family-coupling-gives-no-quark-mixing; the proposition's statement and version are left as they are.
---

## formal
Proposition \claimref{standard-model.bidoublet-complex} says that $m_{t} \ne m_{b}$ needs a second independent doublet coupling and that a complex bidoublet, carrying two electroweak doublets, supplies one. Read with Theorem \claimref{synthesis.second-doublet-of-one-family-coupling-gives-no-quark-mixing}, "independent" must mean a second family matrix, not a second vev of the same one. If every coupling entering $M_{u}$ and $M_{d}$ is a multiple of one family matrix $Y$ (one rung coupling read through $c^{*}$ with any number of doublet vevs, or a complex bidoublet with a single Yukawa matrix), then $M_{u} = rM_{d}$ for one complex number $r$: every family has the same up/down mass ratio and the CKM matrix is the identity, against the record. So the complex bidoublet with one Yukawa matrix supplies the up/down scale ratio ($m_{t}/m_{b}$ through the ratio of its two vevs) but not the family pattern; the up/down split family by family, and any quark mixing, need a second family matrix not proportional to the first, with $\det[H_{u}, H_{d}] \ne 0$ for three families (Fact \claimref{synthesis.imported-jarlskog-commutator-identity}). This is the standard single-$10$ relation of $SO(10)$ model building, applied to the $c^{*}$ reading.

## technical
pending

## lay
pending

## one-liner
pending
