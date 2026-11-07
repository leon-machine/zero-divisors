---
id: note.odd-extensions.one-operator-sees-difference
kind: note
version: 2
title: the one operator that sees the difference
status: remark
subject: tower
proposed_by:
  kind: extraction
  session: notes-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14a, deposited version
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 2
  source: maintainer pass 2026-11-07 (GA units)
comments_on:
- odd-extensions.two-towers-one-curved-universe
- odd-extensions.belongs-tower
- odd-extensions.boost-dilation-ratio-gauge
locators:
  paper: T14a
  number: Rem 9.4
  label: rem:onesees
  line: 725
extraction:
  source_formal: |-
    ... $e_{5}$ is the real pseudoscalar in one tower and the pseudoscalar times a central complex unit in the other, which in the physicists' notation is $\gamma_{5}$ against $i\gamma_{5}$, an anti-Hermitian against a Hermitian bilinear. ...

    The source writes $i$ for the central pseudoscalar of the complexified extension ($I_5$ for $\Cl(2,3)$).
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'By the unit principle (U3, U5) the physicists'' i gamma_5 is written I_5 gamma_5, their complex unit read as the central pseudoscalar of the complexified extension (std-algebra.complexification-is-the-odd-extension; I_5 for Cl(2,3)); the source''s sentence moves to source_formal and the outside_ga declaration is removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (bridge): the note compares gamma_5 with i gamma_5 in the physicists'' gamma-matrix notation of the complexified Dirac algebra, where the central complex unit is a scalar of the complexification.'
  i4_conversion:
    by: ai-i4-pass
    date: '2026-10-21'
    converted: []
    kept:
    - '$\gamma_5$ against $i\gamma_5$ and "a central complex unit": gamma-matrix notation in the complexified
      algebra (complex matrices, complexified algebra)'
---

## formal
An operator linear in $e_{5}$ alone, a term $\bar\psi e_{5}\psi$, is the one place the doubling would show: $e_{5}$ is the real pseudoscalar in one tower and the pseudoscalar times a central complex unit in the other, the central pseudoscalar of the complexified extension (\claimref{std-algebra.complexification-is-the-odd-extension}; $I_5$ when the extension is $\Cl(2,3)$), which in the physicists' notation, with their complex unit read as that central pseudoscalar, is $\gamma_{5}$ against $I_5\gamma_{5}$, an anti-Hermitian against a Hermitian bilinear. But $e_{5}$ is the unit Stelle-West direction, unsoldered by Proposition \claimref{odd-extensions.belongs-tower}(i) and pure gauge by Fact \ref{fact:goldstone}; so either a coupling to it can be physical, in which case Fact \ref{fact:goldstone} is being read too strongly in Proposition \claimref{odd-extensions.boost-dilation-ratio-gauge}(iii), or it cannot, in which case the mirror sector is observationally identical to this one at every level the series reaches. The note takes the second reading, consistently with Proposition \claimref{odd-extensions.boost-dilation-ratio-gauge}, and records the operator as the one place the first reading would show; the Hermiticity statement depends on a Dirac-representation convention the note does not fix.

## technical
pending

## lay
pending

## one-liner
pending
