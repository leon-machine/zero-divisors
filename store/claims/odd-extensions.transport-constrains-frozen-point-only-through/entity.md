---
id: odd-extensions.transport-constrains-frozen-point-only-through
kind: claim
version: 2
title: The transport constrains the frozen point only through its norm
status: proved
region: odd-extensions
subject: dark-energy
tags: [transport-algorithm, frozen-point, degenerate-algebras, hyperbolic-plane]
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
  - odd-extensions.imported-minimal-completion-degenerate-algebra-rule@5
  - odd-extensions.twistor-algebra@6
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_unique_canonical_partner
- kind: check
  ref: check.py::check_norm_is_two_ab
- kind: check
  ref: check.py::check_orbits_are_level_sets
- kind: check
  ref: check.py::check_two_signs_non_isomorphic
- kind: proof
  derivation: main
locators:
  paper: T14a
  number: Thm 8.2
  label: thm:free
  line: 648
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the completion of (1,3;1) is (2,4) with a unique null partner; norm 2ab; O(1,1) orbits are the level sets; Cl(1,4) and Cl(2,3) have different centres. Version 1 -> 2.'
  env: theorem
  typing:
    by: ai-typing-pass
    note: 'Both uses (the minimal-completion Fact and the rung theorem) are premises cited in the proof
      and were kept; nothing was removed or added. Levels pass: conditions already kept.'
---

## formal
Let $W = I_{0}^{\perp}$, the degenerate space of signature $(1,3;1)$ at $\Lambda = 0$ with radical spanned by the null frozen point $I_{0}$, written $I$ in this theorem, and let $\widetilde W$ be its minimal completion. Then:
\begin{enumerate}
\item[(i)] $\widetilde W$ has signature $(2,4)$ and is the rung; the isometry of Fact \claimref{odd-extensions.imported-minimal-completion-degenerate-algebra-rule} fixing $W$ pointwise is unique, so the null partner $\varphi$ of $I$ with $Q(I,\varphi) = 1$, $Q(\varphi,\varphi) = 0$, $\varphi \perp \{I\}^{\perp} \cap W$ is canonical: the transport supplies the hyperbolic plane $\mathrm{span}(I, \varphi)$ together with a distinguished null basis of it;
\item[(ii)] every vector orthogonal to the Lorentz frame is $aI + b\varphi$ with norm $2ab$; a frozen point of cosmological constant $\Lambda$ is such a vector with $2ab = \Lambda/3$, and the sign of $\Lambda$ is the sign of the product of its components along the null generator and its canonical partner;
\item[(iii)] the isometries of the completion that fix the Lorentz frame act on the plane as $O(1,1)$, whose orbits on nonzero vectors are exactly the level sets of the norm; so the only invariant of the frozen point under the symmetries the transport supplies is its norm $\Lambda/3$: the cosmological constant, sign and magnitude, is the one modulus of the frozen point that the transport leaves free;
\item[(iv)] no symmetry of the completion carries a frozen point of positive norm to one of negative norm, and the two intermediate algebras $\Cl(I_{\Lambda}^{\perp})$ for the two signs are non-isomorphic (Theorem \claimref{odd-extensions.twistor-algebra}(iv)); the two signs are inequivalent under every symmetry the construction has, and the choice between them is decided by nothing in the transport.
\end{enumerate}

## technical
Take $W = I_{0}^{\perp}$, the degenerate space of signature $(1,3;1)$ at $\Lambda = 0$ whose radical is spanned by the null frozen point $I$. Its minimal completion $\widetilde W$ has signature $(2,4)$ and is the rung, and the isometry fixing $W$ pointwise is unique, so the null partner $\varphi$ with $Q(I,\varphi) = 1$, $Q(\varphi) = 0$ and $\varphi \perp \{I\}^{\perp} \cap W$ is canonical. Every vector orthogonal to the Lorentz frame is $aI + b\varphi$ with $Q(aI + b\varphi) = 2ab$, and a frozen point of cosmological constant $\Lambda$ has $2ab = \Lambda/3$.

The isometries of the completion fixing the Lorentz frame act on this plane as $O(1,1)$, whose orbits on nonzero vectors are exactly the level sets of the norm. So the norm $\Lambda/3$, sign and magnitude, is the one modulus of the frozen point the transport leaves free. No symmetry of the completion carries a positive norm to a negative one, the intermediate algebras $\Cl(I_{\Lambda}^{\perp})$ for the two signs are non-isomorphic, and nothing in the transport chooses between them.

## lay
When the cosmological constant is zero the frozen point becomes a vector of zero length, a degenerate spot that the series' transport completes into a larger, well-behaved space. That completion comes with a canonical plane and a preferred pair of directions in it. Every possible value of the cosmological constant corresponds to a point in this plane, and the available symmetries can move that point anywhere except to a point of different length. So the transport pins down everything about the frozen point except its length, which is the cosmological constant, and gives no reason to prefer a positive value over a negative one.

## one-liner
Completing the degenerate $\Lambda = 0$ space gives the rung with a canonical null frame, and under its symmetries the frozen point's only invariant is its norm $\Lambda/3$, the two signs being inequivalent and undecided by the transport.
