---
id: families.source-term-linear-tilt-mass-functional
kind: claim
version: 4
title: 'The source term: the $\Lambda$-linear tilt of the mass functional'
status: proved
region: families
subject: generations
tags: [cosmological-constant, symmetry-breaking]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T13, deposited version
review: typed
derivations:
- name: main
  uses:
  - families.imported-dictionary-exact-join@5
  - families.imported-face-valued-bracket-quantum-numbers@5
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T13.py
  tags:
  - label:prop:source
- kind: check
  ref: check.py::check_source_expansion
- kind: check
  ref: check.py::check_wirtinger_gradient
- kind: check
  ref: check.py::check_phase_locking
locators:
  paper: T13
  number: Prop 4.2
  label: prop:source
  line: 643
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the source expansion with formal Lambda, the Wirtinger gradient, and the phase locking of clause (1). Version 3 -> 4.'
  env: proposition
  context_refs:
  - families.alignment-computed-thirteenth-refutation-democracy-one
  - families.imported-dictionary-exact-join
  - families.imported-face-valued-bracket-quantum-numbers
  eqrefs: 1
  typing:
    by: ai-typing-pass
    added:
    - families.imported-dictionary-exact-join
    - families.imported-face-valued-bracket-quantum-numbers
    note: 'Added the dictionary and exact join, whose deformed bracket and join term clause (1) expands,
      and the face-valued bracket, cited for the gauge argument of the reading clause (2); the alignment
      citation is a forward reference and was not added; any resulting E204 traces to mass.exact-join
      outside this group. Levels pass: lay now keeps the independence assumption, the unless-the-area-vanishes
      exception and the observation level; one-liner adds the observation level and the mass-functional
      premise.'
  source_title: 'The source term: the $\Lambda$-linear tilt of the mass functional'
  source_formal: |-
    Write the deformed bracket of Fact \claimref{families.imported-dictionary-exact-join} as $B_{\Lambda} = b + \tfrac{\Lambda}{6}\,\Omega_{\omega}$, with $b = \br{\pi^{1}\pi^{2}}$ the flat mass bracket and $\Omega_{\omega} = [\omega^{1}\omega^{2}]$ the composite's $\omega$-bracket, a length since $B_{\Lambda}$ is a mass. Two clauses at two levels.
    \begin{enumerate}
    \item \emph{(Proved.)} The join's leading term expands as
    \begin{equation}
    2|B_{\Lambda}|^{2} \;=\; 2|b|^{2} \;+\; \frac{2\Lambda}{3}\,\mathrm{Re}\bigl(\bar{b}\,\Omega_{\omega}\bigr) \;+\; \frac{\Lambda^{2}}{18}\,|\Omega_{\omega}|^{2},
    \end{equation}
    the middle term linear in $b$; its derivative in $b$ at $b = 0$ is $\tfrac{2\Lambda}{3}\Omega_{\omega}$, nonzero iff $\Lambda\Omega_{\omega} \ne 0$; and at fixed moduli the middle term is maximised in the phase of $b$ exactly when $\arg b = \arg\Omega_{\omega}$.
    \item \emph{(Reading, at observation level.)} If the effective potential for the flat bracket is built on the mass functional, so that $b$ and the vacuum value of $\Omega_{\omega}$ are treated as independent variables, then the potential contains a $\Lambda$-linear inhomogeneous source for $b$ and $b = 0$ is not an extremum unless the vacuum $\omega$-area vanishes: condensation is not a possibility the potential permits but a tilt it cannot avoid, with the phase of $b$ locked to the phase of $\Omega_{\omega}$ or to its opposite, according to the sign with which the functional enters the potential, which the reading does not fix; either way the locked phase is pure gauge under the abelian factor (Fact \claimref{families.imported-face-valued-bracket-quantum-numbers}), so no physical tension. The value of the condensate is thereby converted into one named object, the vacuum expectation of the $\omega$-area, which the framework defines but does not compute. The reading assumes what a potential for the bracket would have to be; $b$ and $\Omega_{\omega}$ are functions of the same two twistors, and their independence as vacuum variables is the assumption. What the expectation does and does not determine is settled by Proposition \claimref{families.alignment-computed-thirteenth-refutation-democracy-one}.
    \end{enumerate}
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'The two constituents are now conformal spinors; the complex conjugate bar-b is the conjugation reversing the bracket''s complex unit and is written as in the paper.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - families.imported-dictionary-exact-join
    stated_role:
    - families.imported-face-valued-bracket-quantum-numbers
---

## formal
Write the deformed bracket of Fact \claimref{families.imported-dictionary-exact-join} as $B_{\Lambda} = b + \tfrac{\Lambda}{6}\,\Omega_{\omega}$, with $b = \br{\pi^{1}\pi^{2}}$ the flat mass bracket and $\Omega_{\omega} = [\omega^{1}\omega^{2}]$ the composite's $\omega$-bracket, a length since $B_{\Lambda}$ is a mass. Two clauses at two levels.
\begin{enumerate}
\item \emph{(Proved.)} The join's leading term expands as
\begin{equation}
2|B_{\Lambda}|^{2} \;=\; 2|b|^{2} \;+\; \frac{2\Lambda}{3}\,\mathrm{Re}\bigl(\bar{b}\,\Omega_{\omega}\bigr) \;+\; \frac{\Lambda^{2}}{18}\,|\Omega_{\omega}|^{2},
\end{equation}
the middle term linear in $b$; its derivative in $b$ at $b = 0$ is $\tfrac{2\Lambda}{3}\Omega_{\omega}$, nonzero iff $\Lambda\Omega_{\omega} \ne 0$; and at fixed moduli the middle term is maximised in the phase of $b$ exactly when $\arg b = \arg\Omega_{\omega}$.
\item \emph{(Reading, at observation level.)} If the effective potential for the flat bracket is built on the mass functional, so that $b$ and the vacuum value of $\Omega_{\omega}$ are treated as independent variables, then the potential contains a $\Lambda$-linear inhomogeneous source for $b$ and $b = 0$ is not an extremum unless the vacuum $\omega$-area vanishes: condensation is not a possibility the potential permits but a tilt it cannot avoid, with the phase of $b$ locked to the phase of $\Omega_{\omega}$ or to its opposite, according to the sign with which the functional enters the potential, which the reading does not fix; either way the locked phase is pure gauge under the abelian factor (Fact \claimref{families.imported-face-valued-bracket-quantum-numbers}), so no physical tension. The value of the condensate is thereby converted into one named object, the vacuum expectation of the $\omega$-area, which the framework defines but does not compute. The reading assumes what a potential for the bracket would have to be; $b$ and $\Omega_{\omega}$ are functions of the same two conformal spinors, and their independence as vacuum variables is the assumption. What the expectation does and does not determine is settled by Proposition \claimref{families.alignment-computed-thirteenth-refutation-democracy-one}.
\end{enumerate}

## technical
Writing the deformed bracket as $B_{\Lambda} = b + \tfrac{\Lambda}{6}\,\Omega_{\omega}$, with $b$ the flat mass bracket and $\Omega_{\omega}$ the composite's $\omega$-bracket (a length), the join's leading term expands as $2|B_{\Lambda}|^{2} = 2|b|^{2} + \tfrac{2\Lambda}{3}\,\mathrm{Re}(\bar{b}\,\Omega_{\omega}) + \tfrac{\Lambda^{2}}{18}|\Omega_{\omega}|^{2}$. The middle term is linear in $b$, its gradient at $b = 0$ is $\tfrac{2\Lambda}{3}\Omega_{\omega}$, nonzero if and only if $\Lambda\Omega_{\omega} \neq 0$, and at fixed moduli it is maximal when $\arg b = \arg\Omega_{\omega}$. This clause is proved.

At observation level, if the effective potential for $b$ is built on the mass functional with $b$ and the vacuum value of $\Omega_{\omega}$ treated as independent, the potential has a $\Lambda$-linear source and $b = 0$ is not an extremum unless the vacuum $\omega$-area vanishes; the phase of $b$ locks to that of $\Omega_{\omega}$ or its opposite, which is pure gauge. The condensate's value is reduced to the vacuum expectation of the $\omega$-area, which the framework defines but does not compute; the independence of the two variables is the assumption.

## lay
Expanding the formula for a particle's mass with the cosmological constant switched on reveals an extra term that is linear in the basic mass quantity. Such a term acts like a slope that pushes the system away from zero. So, if the energy landscape is built from this formula and the two brackets in it are treated as independent, a nonzero value cannot be avoided unless the vacuum value of one of them, the $\omega$-area, vanishes. The size of that value then depends on that one quantity, which the framework names but does not compute. This second step is a reading at observation level, and the independence of the two brackets is the assumption it rests on.

## one-liner
The $\Lambda$-deformed join contains a term linear in the flat bracket, so under the observation-level reading that the potential is built on the mass functional with $b$ and the vacuum $\omega$-area independent, the potential tilts and condensation is unavoidable unless that area vanishes.
