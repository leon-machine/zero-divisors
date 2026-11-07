---
id: note.odd-extensions.added-axis-pseudoscalar
kind: note
version: 3
title: the added axis is the pseudoscalar
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
- name: Claude Opus 5.5
  role: notation pass, imaginary units resolved by the unit principle (U1 to U6)
  version: 3
  source: maintainer pass 2026-11-07 (resolve units)
comments_on:
- odd-extensions.four-extensions-oriented-pair
locators:
  paper: T14a
  number: Rem 2.5
  label: rem:pseudo
  line: 475
extraction:
  source_formal: |-
    In the complexified case the fifth generator is $e_{5} = \pm\,\omega\,\omega'^{-1}$, that is $i\gamma_{5}$ in the physicists' notation, and the algebra is the complexified Dirac algebra.

    The source writes $i$ for the central pseudoscalar of the complexified extension ($I_5$ for $\Cl(2,3)$).
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'By the unit principle (U3, U5) the physicists'' i gamma_5 is written I_5 gamma_5, their complex unit read as the central pseudoscalar omega of the complexified extension (std-algebra.complexification-is-the-odd-extension; omega = +-I_5 for Cl(2,3)); the source''s sentence moves to source_formal and the outside_ga declaration is removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (bridge): the note names the fifth generator of the complexified case in the physicists'' notation, i gamma_5, beside its geometric-algebra form +-omega omega''^{-1}.'
  i4_conversion:
    by: ai-i4-pass
    date: '2026-10-21'
    converted: []
    kept:
    - '$i\gamma_5$: physicists'' gamma-matrix notation for the complexified Dirac algebra (complex matrices,
      complexified algebra)'
---

## formal
In the doubled case the fifth generator is nothing new: on each summand it acts as the pseudoscalar $\omega' = e_{1}e_{2}e_{3}e_{4}$ of the shadow, up to sign, so the extra space direction of $\Cl(1,4)$ is the chirality operator of $\Cl(1,3)$ promoted from a $4$-blade to a vector, with the choice of sign the only datum the extension adds. In the complexified case the fifth generator is $e_{5} = \pm\,\omega\,\omega'^{-1}$, where the central pseudoscalar $\omega$ ($\omega^{2} = -1$) is the unit of the complexification (\claimref{std-algebra.complexification-is-the-odd-extension}; for this world the extension is $\Cl(2,3)$ and $\omega = \pm I_5$); in the physicists' notation, with their complex unit read as that central pseudoscalar, it is $I_5\gamma_{5}$, and the algebra is the complexified Dirac algebra.

## technical
pending

## lay
pending

## one-liner
pending
