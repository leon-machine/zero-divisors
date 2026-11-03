---
id: interior.stabiliser-rotates-parabolic-reductive
kind: claim
version: 2
title: The stabiliser rotates from parabolic to reductive
status: proved
region: interior
subject: einstein
tags: [frozen-point, rotors-and-stabilisers, cosmological-constant]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T06, deposited version
review: typed
derivations:
- name: main
  uses:
  - interior.non-null-stabilisers-section-they-act@4
  - interior.scale-tractor-leaves-cone@7
  - interior.stabilisers-flat-model@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_stabiliser_dimension_and_shape
- kind: check
  ref: check.py::check_reductive_or_parabolic
- kind: check
  ref: check.py::check_section_and_polar_infinity
locators:
  paper: T06
  number: Prop 4.10
  label: prop:stabiliser
  line: 556
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: in Cl(2,4) for five values of Lambda, Q(I) = Lambda/3, a 10-dimensional stabiliser with invariant form (4,6) so(1,4), (6,4) so(2,3) or (3,3,4) Poincare with nilradical ninf ^ W, the pseudosphere section, and spacelike or timelike polar infinity. Version 1 -> 2.'
  typing:
    by: ai-typing-pass
    note: 'All three uses are the results the proof combines; the no-go theorem is cited only to name the transvections, so it was not added.'
  env: proposition
---

## formal
The stabiliser of the frozen point $I_g$ in the structure group of the completion is:
\begin{enumerate}
\item for $\Lambda = 0$: the stabiliser of a null vector, the Poincar\'e group $SO(1,3) \ltimes \R^4$ (Proposition \claimref{interior.stabilisers-flat-model}), a group with $4$-dimensional nilradical: the parabolic situation, whose transvections are the obstruction structure of \cite{ButlerT1};
\item for $\Lambda > 0$: the de Sitter group $SO(1,4)$, reductive, acting on the Einstein section as its isometry group, with conformal infinity the spacelike polar $3$-sphere $\ip{X}{I} = 0$;
\item for $\Lambda < 0$: the anti-de Sitter group $SO(2,3)$, reductive, with timelike polar infinity.
\end{enumerate}
In short: $\Lambda$ measures precisely the failure of infinity to be parabolic.

## technical
The squared norm $Q(I_g) = \Lambda/3$ of the frozen point decides which orbit it lies on, and the flat-model stabiliser computations then identify its stabiliser in the structure group. For $\Lambda = 0$ it is the Poincar\'e group $SO(1,3) \ltimes \R^4$, with four-dimensional nilradical: the parabolic case, whose transvections are the obstruction structure of the series' element-level no-go theorem.

For $\Lambda > 0$ it is the de Sitter group $SO(1,4)$, reductive, acting on the Einstein section as its isometry group, with spacelike polar infinity the $3$-sphere $\ip{X}{I} = 0$; for $\Lambda < 0$ it is the anti-de Sitter group $SO(2,3)$, reductive, with timelike polar infinity. So $\Lambda$ measures precisely the failure of infinity to be parabolic.

## lay
The symmetries that keep the frozen point fixed change character with the cosmological constant. With no cosmological constant they are the symmetries of flat spacetime, translations included; with a positive or negative one they become the symmetries of de Sitter or anti-de Sitter space, with no translations. The cosmological constant thus measures how far infinity is from the flat-space kind.

## one-liner
The stabiliser of the frozen point is the Poincar\'e group for $\Lambda = 0$, the de Sitter group $SO(1,4)$ for $\Lambda > 0$ and the anti-de Sitter group $SO(2,3)$ for $\Lambda < 0$.
