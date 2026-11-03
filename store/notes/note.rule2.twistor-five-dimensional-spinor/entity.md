---
id: note.rule2.twistor-five-dimensional-spinor
kind: note
version: 2
title: 'The conformal spinor space as a five-dimensional spinor'
status: remark
subject: completion
proposed_by:
  kind: extraction
  session: notes-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T17-rule2, the series'' standard disclaimer'
comments_on:
- rule2.imported-five-dimensional-chern-simons-shift
- rule2.imported-completion-spacetime-algebra-spinors
- rule2.imported-rule-2-matrix-units-forgotten
locators:
  paper: T17-rule2
  number: Rem 3.6
  label: rem:twistorKK
  line: 229
extraction:
  source_title: 'The twistor as a five-dimensional spinor'
  source_formal: |-
    The Fock space of Fact \claimref{rule2.imported-completion-spacetime-algebra-spinors} is the complex spinor of $\Cl(2,4)$; as a module over $\Cl(1,4)_\C = \Mat_4(\C) \oplus \Mat_4(\C)$ it is $\varepsilon_+ \oplus \varepsilon_-$ halves, one copy of each inequivalent five-dimensional representation, since the odd element $\nu$ maps each half onto the other (Fact \claimref{rule2.imported-rule-2-matrix-units-forgotten}); the two halves restrict to the same module over $\Cl^0(1,4) \cong \Cl(1,3)$, the Dirac spinor. The chirality halves of the six-dimensional spinor are a different splitting, by the six-dimensional volume element, which the odd elements of $\Cl(1,4)$ do not preserve; each chirality half restricted to $\mathrm{Spin}(1,4) \subset \mathrm{Spin}(2,4)$ is the five-dimensional Dirac spinor, the fundamental $\HH^2 = \C^4$ of $Sp(1,1) \subset SU(2,2)$. So twistor space, as a representation of the five-dimensional Lorentz group (which is also the four-dimensional de Sitter group), is a five-dimensional Dirac spinor. This is standard group theory and the script does not check it; it is recorded because it is the spinor-side form of the square of Figure \ref{fig:square}.
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: 'Converted the title and the concluding sentence (twistor space is now the conformal spinor space $\CS$). Kept the complexified algebra $\Cl(1,4)_\C = \Mat_4(\C) \oplus \Mat_4(\C)$, the complex Fock spinor and its chirality halves: the argument splits the complexified module by the odd element $\nu$ and by the complexified volume element, which is not a pure renaming to the $I_6$-structure.'
---

## formal
The Fock space of Fact \claimref{rule2.imported-completion-spacetime-algebra-spinors} is the complex spinor of $\Cl(2,4)$; as a module over $\Cl(1,4)_\C = \Mat_4(\C) \oplus \Mat_4(\C)$ it is $\varepsilon_+ \oplus \varepsilon_-$ halves, one copy of each inequivalent five-dimensional representation, since the odd element $\nu$ maps each half onto the other (Fact \claimref{rule2.imported-rule-2-matrix-units-forgotten}); the two halves restrict to the same module over $\Cl^0(1,4) \cong \Cl(1,3)$, the Dirac spinor. The chirality halves of the six-dimensional spinor are a different splitting, by the six-dimensional volume element, which the odd elements of $\Cl(1,4)$ do not preserve; each chirality half restricted to $\mathrm{Spin}(1,4) \subset \mathrm{Spin}(2,4)$ is the five-dimensional Dirac spinor, the fundamental $\HH^2 = \C^4$ of $Sp(1,1) \subset SU(2,2)$. So the conformal spinor space $\CS$ (twistor space), as a representation of the five-dimensional Lorentz group (which is also the four-dimensional de Sitter group), is a five-dimensional Dirac spinor. This is standard group theory and the script does not check it; it is recorded because it is the spinor-side form of the square of Figure \ref{fig:square}.

## technical
pending

## lay
pending

## one-liner
pending
