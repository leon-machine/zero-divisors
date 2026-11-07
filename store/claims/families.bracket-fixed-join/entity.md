---
id: families.bracket-fixed-join
kind: claim
version: 5
title: The bracket is fixed by the join
status: proved
region: families
subject: mass
tags: [conformal-spinors, cosmological-constant]
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
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 5
  source: maintainer pass 2026-11-07 (GA units)
review: typed
derivations:
- name: main
  uses:
  - families.imported-dictionary-exact-join@6
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T13.py
  tags:
  - label:prop:condensation
- kind: check
  ref: check.py::check_fixed_bracket_identity_in_lambda
- kind: check
  ref: check.py::check_bracket_from_composites
- kind: check
  ref: check.py::check_bracket_nonzero_iff_mass_above_casimir_term
locators:
  paper: T13
  number: Prop 4.1
  label: prop:condensation
  line: 631
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The de Sitter weight -3/2 +- i nu, a physical number, is written -3/2 +- I_4 nu with numbers read in span{1, I_4}; no bare i remains.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: |B|^2 = m^2/2 - Lambda C/6 = (Lambda/6)(nu^2 + 9/4 - C) as an identity in Lambda and on grip-computed composites, and B != 0 iff m^2 > Lambda C/3. Version 2 -> 3. Fix round: check_bracket_from_composites runs at all three Lambda values (was two), matching its docstring. Version 3 -> 4.'
  i4_conversion:
    by: ai-i4-pass
    date: 2026-10-21
    converted: []
    kept:
    - 'the de Sitter weight -3/2 +- i nu (a complex number labelling a principal-series representation, not an operator unit)'
  env: proposition
  context_refs:
  - families.imported-face-valued-bracket-quantum-numbers
  eqrefs: 2
  outside_pilot_cites:
  - ButlerT11
  typing:
    by: ai-typing-pass
    removed:
    - families.source-term-linear-tilt-mass-functional
    note: 'The source-term proposition appears only in the closing commentary on the mass paper''s open
      question and is not a premise; the face-valued bracket Fact (a context_ref) feeds only the flagged
      observation-level sentence, which the proof does not establish, so it was not added as a use. Levels
      pass: the lay now keeps Lambda > 0, the ''C of order one'' qualifier, the consistency level of the
      identity and the observation level (with its reservation) of the condensate reading; the one-liner
      keeps Lambda > 0 and both levels.'
  source_title: 'The bracket is fixed by the join'
  source_formal: |-
    For the two-twistor composite of mass $m$ at $\Lambda > 0$, the exact join of Fact \claimref{families.imported-dictionary-exact-join} fixes the deformed bracket:
    \begin{equation}
    |B_{\Lambda}|^{2} \;=\; \frac{m^{2}}{2} - \frac{\Lambda}{6}\,C \;=\; \frac{\Lambda}{6}\Bigl(\nu^{2} + \frac{9}{4} - C\Bigr),
    \end{equation}
    the second form for a composite on the principal series, $w = -\tfrac32 \pm i\nu$. Consequently $B_{\Lambda} \ne 0$ if and only if $m^{2} > \Lambda C/3$, which for $C$ of order one is every composite heavier than the Hubble scale; the flat bracket $\br{\pi^{1}\pi^{2}}$ is then nonzero up to the $\Lambda$-suppressed $\omega$-area of the join. The identity is a rewriting of the join and says nothing about a vacuum: it converts the matter programme's open equation into the equation the broken phase must satisfy, at consistency level, without supplying the potential that selects the phase, the $W$ and $Z$ masses, or the weak mixing angle. At observation level, and flagged as such: read with Fact \claimref{families.imported-face-valued-bracket-quantum-numbers}, the nonvanishing bracket is a charged singlet with a fixed modulus, the shape of a condensed order parameter, with the reservation recorded in that Fact about what it is an order parameter \emph{of}.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'The composite is now one of two conformal spinors in all levels; the i in the principal-series weight is the complex weight of a density and is kept.'
---

## formal
For the composite of two conformal spinors (twistors) of mass $m$ at $\Lambda > 0$, the exact join of Fact \claimref{families.imported-dictionary-exact-join} fixes the deformed bracket:
\begin{equation}
|B_{\Lambda}|^{2} \;=\; \frac{m^{2}}{2} - \frac{\Lambda}{6}\,C \;=\; \frac{\Lambda}{6}\Bigl(\nu^{2} + \frac{9}{4} - C\Bigr),
\end{equation}
the second form for a composite on the principal series, $w = -\tfrac32 \pm I_4\nu$ (numbers are read in $\mathrm{span}\{1, I_4\}$). Consequently $B_{\Lambda} \ne 0$ if and only if $m^{2} > \Lambda C/3$, which for $C$ of order one is every composite heavier than the Hubble scale; the flat bracket $\br{\pi^{1}\pi^{2}}$ is then nonzero up to the $\Lambda$-suppressed $\omega$-area of the join. The identity is a rewriting of the join and says nothing about a vacuum: it converts the matter programme's open equation into the equation the broken phase must satisfy, at consistency level, without supplying the potential that selects the phase, the $W$ and $Z$ masses, or the weak mixing angle. At observation level, and flagged as such: read with Fact \claimref{families.imported-face-valued-bracket-quantum-numbers}, the nonvanishing bracket is a charged singlet with a fixed modulus, the shape of a condensed order parameter, with the reservation recorded in that Fact about what it is an order parameter \emph{of}.

## technical
For a two-spinor composite of mass $m$ at $\Lambda > 0$, the exact join $m^{2} = 2|B_{\Lambda}|^{2} + \tfrac{\Lambda}{3}C$ can be solved for the deformed bracket: $|B_{\Lambda}|^{2} = \tfrac{m^{2}}{2} - \tfrac{\Lambda}{6}C = \tfrac{\Lambda}{6}\bigl(\nu^{2} + \tfrac94 - C\bigr)$, the second form for a composite on the principal series $w = -\tfrac32 \pm I_4\nu$ (numbers are read in $\mathrm{span}\{1, I_4\}$). Hence $B_{\Lambda} \neq 0$ exactly when $m^{2} > \Lambda C/3$, which for $C$ of order one is every composite heavier than the Hubble scale, and the flat bracket $\br{\pi^{1}\pi^{2}}$ is then nonzero up to the $\Lambda$-suppressed $\omega$-area.

The identity is a rewriting of the join and says nothing about a vacuum: it gives, at consistency level, the equation a broken phase must satisfy, without the potential that selects the phase, the $W$ and $Z$ masses or the weak mixing angle. At observation level only, read with the bracket's quantum numbers, the nonzero bracket has the shape of a condensed order parameter, a charged singlet of fixed modulus, with the question of what it is an order parameter of left open.

## lay
With a positive cosmological constant, the framework has an exact formula for the mass of a particle made of two conformal spinors. Turned around, the formula fixes the size of a quantity called the bracket and shows that, for typical values of the remaining invariant, it cannot vanish for anything heavier than the scale of cosmic expansion. Read at observation level only, alongside the bracket's charges, that looks like the signature of a condensate, similar in shape to the Higgs field's value, though what it would be a condensate of is left open. The result itself is only a rewriting, at consistency level: it does not choose a vacuum or predict the W and Z masses.

## one-liner
For a two-spinor composite at $\Lambda > 0$, the exact join fixes the deformed bracket as $|B_{\Lambda}|^{2} = m^{2}/2 - \Lambda C/6$, so it is nonzero exactly when $m^{2} > \Lambda C/3$; the identity is a consistency-level rewriting, and its condensate reading is observation level only.
