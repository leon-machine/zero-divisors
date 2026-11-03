---
id: field-theory.orientation-relocated
kind: claim
version: 6
title: The orientation is relocated
status: proved
region: field-theory
subject: quantum-fields
tags: [conformal-spinors, chirality, pseudoscalar-and-centre]
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
review: typed
about:
- obj.field-theory.single-algebra-field
derivations:
- name: main
  uses:
  - field-theory.where-each-lives@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_SMC.py
  tags:
  - id:C6a
  - id:C6b
  - id:C6c
  - id:C6d
  - id:C6e
- kind: check
  ref: check.py::check_e_plus_maps_halves_and_swaps_doublets
- kind: check
  ref: check.py::check_unit_J_distinguishes_halves
- kind: check
  ref: check.py::check_sign_of_unit_relocates_orientation
locators:
  paper: FT
  number: Prop 10.2
  label: prop:orientation
  line: 274
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: e_+ maps T onto T'' commuting with I4 and Lorentz rotors and swapping the E-doublets, J = right I6 making the halves inequivalent with J = +-I4 on ker n_0, and the sign of the unit relocating the orientation. Version 4 -> 5. Check strengthened: ker n_0 asserted 4-dimensional in each half so the -J doublet tests cannot pass vacuously; n_0 and sample count moved to module level. Version 5 -> 6.'
  env: proposition
  source_formal: '\begin{enumerate}

    \item Left multiplication by $e_+$ maps the even half $T$ of the twistor module onto the odd half
    $T''$, commutes with $I_4$ and with Lorentz rotors, and swaps the $E$-doublets: $i = I_4$ and Lorentz
    symmetry alone do not tell $T$ from $T''$.

    \item The twistor''s unit that commutes with Clifford multiplication is right multiplication by $I_6$,
    $J$; with $J$ the two halves are inequivalent (twistors and dual twistors), and on the momentum doublet
    $\ker n_0$, the $E = +1$ doublet of both halves, $J = +I_4$ in $T$ and $J = -I_4$ in $T''$.

    \item The commutant fixes the twistor''s unit only up to sign. So with the field''s unit $I_4$, which
    half''s momentum spinors are complex-linear is the relative sign of the two units.

    \end{enumerate}'
  source_title: The orientation is relocated
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: Converted 'twistor module', 'the twistor's unit' and 'twistors and dual twistors' to the conformal
      spinor module, its unit and conformal spinors and their duals, keeping the twistor names once in
      parentheses; the mathematics (e_+, I4, I6, E-doublets, ker n_0) was already geometric algebra and
      is unchanged. The proof cites run checks only and needed no change.
  typing:
    by: ai-typing-pass
    added:
    - field-theory.where-each-lives
    note: 'Added where each unit lives, whose clause (2) (the commutant span{1, I6}, so the unit is fixed
      up to sign) clause (3) uses. Levels pass: levels written from scratch, keeping every condition and
      level qualifier of the formal statement.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    stated_role:
    - field-theory.where-each-lives
---

## formal
\begin{enumerate}
\item Left multiplication by $e_+$ maps the even half $T$ of the conformal spinor module of $\Cl(2,4)$ (the twistor module) onto the odd half $T'$, commutes with $I_4$ and with Lorentz rotors, and swaps the $E$-doublets: $i = I_4$ and Lorentz symmetry alone do not tell $T$ from $T'$.
\item The conformal spinors' unit that commutes with Clifford multiplication is right multiplication by $I_6$, $J$; with $J$ the two halves are inequivalent (conformal spinors and their duals, the twistors and dual twistors), and on the momentum doublet $\ker n_0$, the $E = +1$ doublet of both halves, $J = +I_4$ in $T$ and $J = -I_4$ in $T'$.
\item The commutant fixes the conformal spinors' unit only up to sign. So with the field's unit $I_4$, which half's momentum spinors are complex-linear is the relative sign of the two units.
\end{enumerate}

## technical
Left multiplication by $e_+$ maps the even half $T$ of the conformal spinor module onto the odd half $T'$, commutes with $I_4$ and the Lorentz rotors and swaps the $E$-doublets, so $i = I_4$ and Lorentz symmetry alone cannot tell the halves apart. The unit commuting with Clifford multiplication is right multiplication by $I_6$, $J$; with it the halves are inequivalent, and on the momentum doublet $\ker n_0$, the $E = +1$ doublet of both halves, $J = +I_4$ in $T$ and $J = -I_4$ in $T'$.

Since the commutant fixes $J$ only up to sign, with the field's unit $I_4$ the question of which half's momentum spinors are complex-linear is the relative sign of $J$ and $I_4$.

## lay
The Standard-Model paper's matter keeps one binary choice, an orientation that tells particles from antiparticles. Fixing the field's imaginary unit does not remove it: the two halves of the conformal spinor space look the same to that unit and to relativity. The choice reappears as the relative sign between the field's unit and the conformal spinors' own unit.

## one-liner
With $i = I_4$ the two halves of the conformal spinor module are not told apart by $I_4$ and Lorentz symmetry, and which half is complex-linear becomes the relative sign of $I_4$ and the spinors' unit $\pm I_6$.
