---
id: odd-extensions.imported-copy-theorem-soldered-residue
kind: claim
version: 5
title: 'Imported: the copy theorem, and the soldered residue'
status: proved
region: odd-extensions
subject: dark-matter
tags: [mirror-sector, superselection]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14a, deposited version
review: typed
derivations:
- name: main
  uses:
  - dark-matter.mirror-tower-copy-one@8
  - dark-matter.residue-soldered-invariant-not-algebraic-one@3
  - dark-matter.superselected-hence-dark-exactly-stable@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_even_subalgebras_isomorphic
- kind: check
  ref: check.py::check_both_are_mat4c
- kind: check
  ref: check.py::check_residue_is_soldered
locators:
  paper: T14a
  number: Fact 1.3
  label: fact:copy
  line: 415
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the even-subalgebra isomorphism Cl^0(2,4) = Cl^0(4,2), both Mat(4,C), and the soldered residues 6 and 2. Version 3 -> 4. Sample inputs moved to module level; no change to what is tested. Version 4 -> 5.'
  env: fact
  context_refs:
  - dark-matter.mirror-tower-copy-one
  - dark-matter.residue-soldered-invariant-not-algebraic-one
  - dark-matter.superselected-hence-dark-exactly-stable
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: 'Restatement of three dark-matter results; kept all three uses edges as the restated sources.
      Levels pass: conditions already kept.'
  source_title: 'Imported: the copy theorem, and the soldered residue'
  source_formal: |-
    The mirror tower is a copy of this one: every input to the Standard-Model chain (the conformal spin group $\mathrm{Spin}(2,4) \cong \mathrm{Spin}(4,2)$, the twistor module with its helicity form, the complexified isotropic structure, the two-twistor mass formula) is invariant under signature reversal, because over $\C$ the ambient carries no signature and $\Cl^{0}(2,4) \cong \Cl^{0}(4,2) \cong \Mat(4,\C)$. The residue is a soldered invariant, not an algebraic one, and the one metric superselects the tower charge. \emph{Provenance:} \cite[Thms.~3.5 and 4.3, Prop.~4.1]{ButlerT14}.
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: 'Converted the twistor module and its helicity form to $\CS$ with the reversion form $h$, and the two-twistor mass formula to that of two conformal spinors. Kept ``over $\C$ the ambient carries no signature'''' and the complexified isotropic structure: these complexify the vector space, which is the argument, not the spinor unit.'
---

## formal
The mirror tower is a copy of this one: every input to the Standard-Model chain (the conformal spin group $\mathrm{Spin}(2,4) \cong \mathrm{Spin}(4,2)$, the conformal spinor module $\CS$ (twistor module) with its helicity form, the reversion form $h$, the complexified isotropic structure, the mass formula of two conformal spinors) is invariant under signature reversal, because over $\C$ the ambient carries no signature and $\Cl^{0}(2,4) \cong \Cl^{0}(4,2) \cong \Mat(4,\C)$. The residue is a soldered invariant, not an algebraic one, and the one metric superselects the tower charge. \emph{Provenance:} \cite[Thms.~3.5 and 4.3, Prop.~4.1]{ButlerT14}.

## technical
Imported from earlier in the series. Every input to the Standard-Model chain (the conformal spin group $\Spin(2,4) \cong \Spin(4,2)$, the conformal spinor module with its helicity form, the complexified isotropic structure and the mass formula of two conformal spinors) is invariant under signature reversal, because over $\C$ the ambient carries no signature and $\Cl^{0}(2,4) \cong \Cl^{0}(4,2) \cong \Mat(4,\C)$; so the mirror tower is a copy of this one. The residue is a soldered invariant rather than an algebraic one, and the one metric superselects the tower charge.

## lay
This collects three earlier results for use in the odd-extensions note. The mirror tower reproduces every ingredient of the Standard Model, because once complex numbers are allowed the difference between the two signatures disappears. Which tower matter belongs to is fixed by how the algebra is attached to spacetime, not by the algebra alone, and the single shared geometry forbids any process that changes it.

## one-liner
Imported: the mirror tower is a copy of this one because every Standard-Model input is invariant under signature reversal, the residue is a soldered rather than algebraic invariant, and the one metric superselects the tower charge.
