---
id: rule2.imported-completion-spacetime-algebra-spinors
kind: claim
version: 5
title: 'Imported: the completion of the spacetime algebra, and its spinors'
status: proved
region: rule2
subject: completion
tags: [conformal-spinors, spinor-modules, ladder-pairs]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T17-rule2, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - correspondence.fock-model-complexified-ascended-algebra@7
  - correspondence.spinor-identification@7
  - transport.minimality@4
  - transport.no-go-level-elements@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_forced_completion_of_spacetime_algebra
- kind: check
  ref: check.py::check_fock_module_irreducible
- kind: check
  ref: check.py::check_chirality_halves
- kind: check
  ref: check.py::check_real_minimal_left_ideal_with_unit_i6
locators:
  paper: T17-rule2
  number: Fact 1.4
  label: fact:twistor
  line: 113
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: about the core definitions it is stated in. Version 4 -> 5.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: Cl(1,3) -> Cl(2,4), the irreducible Fock module of Cl(2,4)_C, its chirality halves, and the real minimal left ideal with complex unit I6. Version 3 -> 4.'
  env: fact
  context_refs:
  - correspondence.fock-model-complexified-ascended-algebra
  - correspondence.spinor-identification
  - transport.minimality
  - transport.no-go-level-elements
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: The four uses are exactly the cited root-paper no-go and minimality and correspondence Fock-model
      and spinor results; E204 is inherited from the spinor identification, outside this list.
  source_title: 'Imported: the completion of the spacetime algebra, and its spinors'
  source_formal: |-
    The forced completion of the spacetime algebra is $\Cl(1,3) \hookrightarrow \Cl(2,4)$, and the complexified $\Cl(2,4)$ acts irreducibly on the Fock space of three fermionic ladder pairs, whose chirality halves are Penrose's twistor space and its conjugate dual. \emph{Provenance:} \cite[Thms.~4.2 and 4.13]{ButlerT1}; \cite[Thms.~3.1 and 3.4]{ButlerT9}.
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: 'Converted the chirality halves to the conformal spinor space $\CS$ and its conjugate dual, with the real-algebra reading $\Cl^+(2,4)P$ over $I_6$ (TWGA E1.3). Kept the complexified $\Cl(2,4)$ and its Fock space, since that is the cited construction (Chevalley''s, in T1 and T9) and is not a pure renaming.'
about:
- obj.std-algebra.spacetime-algebra
- obj.std-algebra.conformal-algebra
- obj.std-algebra.minimal-left-ideal
---

## formal
The forced completion of the spacetime algebra is $\Cl(1,3) \hookrightarrow \Cl(2,4)$, and the complexified $\Cl(2,4)$ acts irreducibly on the Fock space of three fermionic ladder pairs, whose chirality halves are the conformal spinor space $\CS$ (Penrose's twistor space; in the real algebra it is the minimal left ideal $\Cl^+(2,4)P$, whose complex unit is $I_6$) and its conjugate dual. \emph{Provenance:} \cite[Thms.~4.2 and 4.13]{ButlerT1}; \cite[Thms.~3.1 and 3.4]{ButlerT9}.

## technical
The forced completion of the spacetime algebra is $\Cl(1,3) \hookrightarrow \Cl(2,4)$. The complexification of $\Cl(2,4)$ acts irreducibly on the Fock space of three fermionic ladder pairs, of complex dimension $2^3 = 8$, and the two chirality halves of that space are the conformal spinor space $\CS$, a minimal left ideal of the even algebra with complex unit $I_6$, and its conjugate dual.

The statement restates earlier series results.

## lay
The smallest enlargement of the spacetime algebra that repairs division by zero adds two dimensions. Its spinors can be built like the states of three fermion modes, and splitting them by handedness gives exactly the four-dimensional spinors of conformal geometry, which Penrose found, and their dual.

## one-liner
The forced completion of $\Cl(1,3)$ is $\Cl(2,4)$, whose complexification acts irreducibly on a three-mode fermionic Fock space with chirality halves the conformal spinor space and its conjugate dual.
