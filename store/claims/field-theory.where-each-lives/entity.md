---
id: field-theory.where-each-lives
kind: claim
version: 4
title: Where each imaginary unit lives
status: proved
region: field-theory
subject: quantum-fields
tags: [pseudoscalar-and-centre, conformal-spinors, chirality]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of FT, the series'' standard disclaimer'
- name: Claude Opus 5.5
  role: 'consistency pass, how the conformal spinors'' unit acts stated'
  version: 4
  source: maintainer pass 2026-11-07 (consistency)
review: typed
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_TWGA.py
  tags:
  - id:E1.1
  - id:E1.2a
  - id:E1.2b
  - id:E1.3a
  - id:E1.3b
  - id:E1.3c
  - id:E1.3d
  - id:E1.4a
  - id:E1.4b
  - id:E1.4c
  - id:E1.4d
  - id:E1.4e
  - id:E1.5a
  - id:E1.5b
  - id:E1.5c
  - id:E1.5d
  - id:E1.5e
  - id:E1.6a
  - id:E1.6b
  - id:E1.6c
  - id:E1.6d
  - id:E1.7a
  - id:E1.7b
  - id:E1.7c
  - id:E1.7d
  - id:E3.1a
  - id:E3.1b
  - id:E3.1c
  - id:E3.2a
  - id:E3.2b
  - id:E3.2c
  - id:E3.2d
  - id:E3.2e
  - id:E3.2f
- kind: check
  ref: check.py::check_centres_and_I6
- kind: check
  ref: check.py::check_conformal_spinor_ideal_and_commutant
- kind: check
  ref: check.py::check_two_chiral_doublets
- kind: check
  ref: check.py::check_massless_complex_structure_is_pseudoscalar
locators:
  paper: FT
  number: Prop 4.1
  label: prop:units
  line: 122
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the centres of Cl+(1,3) and Cl+(2,4), CS as a minimal left ideal with commutant span{1, I6}, the two Lorentz-invariant E-doublets with I6 = +-I4, and the pseudoscalar as the massless fields'' complex structure. Version 2 -> 3.'
  env: proposition
  source_formal: '\begin{enumerate}

    \item The centre of $\Cl^+(1,3)$ is $\mathrm{span}\{1, I_4\}$, and the centre of $\Cl^+(2,4)$ is $\mathrm{span}\{1,
    I_6\}$ with $I_6 = I_4E$, where $E = e_+e_-$ is the bivector of the ascended plane, $E^2 = 1$, $[I_4,
    E] = 0$.

    \item Twistor space is the minimal left ideal $\Cl^+(2,4)P$; the commutant of the twistor action is
    $\mathrm{span}\{1, I_6\}$, so the twistor''s $i$ is $\pm I_6$.

    \item At a point, twistor space splits as $L_0 \oplus L_\infty$, the $E = \pm 1$ eigenspaces, both
    Lorentz-invariant, and $I_6 = +I_4$ on $L_0$ and $-I_4$ on $L_\infty$: the two chiral doublets.

    \item For massless fields the field''s complex structure is the pseudoscalar: $\pm I_4$ by helicity
    sector for Maxwell, and on the chiral subspaces of the Weyl field $I_4$ agrees with Hestenes'' right
    $\IS$ up to the chirality sign. A mass term anticommutes with $I_4$.

    \end{enumerate}'
  source_title: Where each $i$ lives
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: 'Converted (2) and (3): twistor space is now the conformal spinor space S (twistor space named
      once), the twistor action is the action of Cl+(2,4) on it, and the twistor''s i is its complex unit;
      (1) and (4) were already geometric algebra. The title''s ''i'' is now ''imaginary unit''. The proof
      cites run checks and prior art only and needed no change.'
  typing:
    by: ai-typing-pass
    note: 'No edges: exact computation. The proof credits (1) to (3) to Arcaute, Lasenby and Doran and
      (4) to standard spacetime algebra; neither is in the store as an imported claim, so no standard-route
      derivation was added. Levels pass: levels written from scratch, keeping every condition and level
      qualifier of the formal statement.'
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 3 -> 4. Clarification: clause (2) and the technical level now say that the unit I6 of CS acts by right multiplication (the store conventions), equal on CS to left multiplication since I6 is central in Cl+(2,4) (clause (1)). Mathematics, status and links unchanged.'
---

## formal
\begin{enumerate}
\item The centre of $\Cl^+(1,3)$ is $\mathrm{span}\{1, I_4\}$, and the centre of $\Cl^+(2,4)$ is $\mathrm{span}\{1, I_6\}$ with $I_6 = I_4E$, where $E = e_+e_-$ is the bivector of the ascended plane, $E^2 = 1$, $[I_4, E] = 0$.
\item The conformal spinor space (twistor space) $\CS$ is the minimal left ideal $\Cl^+(2,4)P$; the commutant of the action of $\Cl^+(2,4)$ on $\CS$ is $\mathrm{span}\{1, I_6\}$, so the complex unit of $\CS$ is $\pm I_6$, acting by right multiplication (on $\CS$ the same as left multiplication, $I_6$ being central in $\Cl^+(2,4)$), the conventions' unit of the conformal spinors.
\item At a point, $\CS$ splits as $L_0 \oplus L_\infty$, the $E = \pm 1$ eigenspaces, both Lorentz-invariant, and $I_6 = +I_4$ on $L_0$ and $-I_4$ on $L_\infty$: the two chiral doublets.
\item For massless fields the field's complex structure is the pseudoscalar: $\pm I_4$ by helicity sector for Maxwell, and on the chiral subspaces of the Weyl field $I_4$ agrees with Hestenes' right $\IS$ up to the chirality sign. A mass term anticommutes with $I_4$.
\end{enumerate}

## technical
The centre of $\Cl^+(1,3)$ is $\mathrm{span}\{1, I_4\}$ and that of $\Cl^+(2,4)$ is $\mathrm{span}\{1, I_6\}$, with $I_6 = I_4E$ for the ascended plane's bivector $E = e_+e_-$, $E^2 = 1$, $[I_4, E] = 0$. The conformal spinor space $\CS = \Cl^+(2,4)P$ has commutant $\mathrm{span}\{1, I_6\}$, so its complex unit is $\pm I_6$, acting by right multiplication; at a point it splits into the Lorentz-invariant $E = \pm 1$ eigenspaces $L_0 \oplus L_\infty$, on which $I_6 = +I_4$ and $-I_4$: the two chiral doublets.

For massless fields the complex structure is the pseudoscalar, $\pm I_4$ by helicity sector for Maxwell, and on the chiral subspaces of the Weyl field $I_4$ agrees with Hestenes' right $\IS$ up to the chirality sign; a mass term anticommutes with $I_4$.

## lay
Every square root of minus one the field theory needs is an element of the real geometric algebra. The conformal spinors' unit is the conformal volume element, which on the spinors at a point becomes the spacetime volume element with a sign set by chirality. For massless fields the unit is the spacetime volume element, which agrees with Hestenes' choice up to that sign, while a mass term does not commute with it.

## one-liner
In real geometric algebra the conformal spinors' unit is $\pm I_6 = \pm I_4E$, equal to $\pm I_4$ on the two chiral doublets, and a massless field's unit is $\pm I_4$, with which a mass term anticommutes.
