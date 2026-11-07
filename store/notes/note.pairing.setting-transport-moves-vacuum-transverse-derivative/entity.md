---
id: note.pairing.setting-transport-moves-vacuum-transverse-derivative
kind: note
version: 2
title: Transport moves the vacuum by the transverse derivative of its null direction
status: setting
subject: thermality
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-pairing, the series'' standard disclaimer'
- name: Claude Opus 5.5
  role: 'unit resolution pass, the complex null vector written with the central unit I_5 of Cl(2,3)'
  version: 2
  source: maintainer pass 2026-11-07 (resolve units)
comments_on:
- pairing.pairing-class-transverse-derivative-null-direction
locators:
  paper: T05-pairing
  number: Setting
  section: Transport moves the vacuum by the transverse derivative of its null direction
  line: 279
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Unit principle U3: the complex null vector m = e_2 + i e_3 needs a unit commuting with every spacetime vector; it is written m = e_2 + I_5 e_3 with I_5 = I_4 e the central unit of Cl(2,3) (std-algebra.complexification-is-the-odd-extension, cited as a mention). Declaration removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Group F (found by the language check''s bare-unit detector): nothing replaced; the i stays and is declared outside_ga (other): m = e_2 + ie_3 is a complex null vector transverse to the null direction; its i must commute with the spacetime vectors, which no pseudoscalar does.'
---

## formal
Let a vacuum field be given on a region: a null direction field $\ell(x)$ with a transverse complex null vector $m(x)$, and let $\nabla$ be the Levi-Civita connection. In an orthonormal frame with $\ell = e_{0} + e_{1}$ and $m = e_{2} + I_{5}e_{3}$ of constant components, $I_{5} = I_{4}e$ the central unit of the odd extension $\Cl(2,3)$, which commutes with every vector (\claimref{std-algebra.complexification-is-the-odd-extension}), $\nabla_{X} e_{b} = \omega^{a}{}_{b}(X)\,e_{a}$, and the connection acts on the Clifford fibre by the bivector
\[
\Omega(X) \;=\; \sum_{a<b}\omega^{ab}(X)\,e_{a}e_{b}, \qquad \omega^{ab} = \omega^{a}{}_{c}\,\eta^{cb},
\]
in the sense that $\nabla_{X} v = \tfrac12[\Omega(X), v]$ for every vector $v$ of constant frame components. The spin transport of the vacuum along $X$ is the spin action of the same $\Omega(X)$.

## technical
pending

## lay
pending

## one-liner
pending
