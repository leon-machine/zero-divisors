---
id: odd-extensions.mirror-inside-complexified-extension-absent-doubled
kind: claim
version: 4
title: The mirror inside the complexified extension, and absent from the doubled one
status: proved
region: odd-extensions
subject: tower
tags: [mirror-sector, grading-and-parity, towers-by-residue]
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
about:
- obj.odd-extensions.single-extension
derivations:
- name: main
  uses:
  - odd-extensions.doubling-or-complexification@5
  - odd-extensions.imported-representatives-dimension-nearest-four-types@4
  - std-algebra.sta-matrix@1
  - std-algebra.pauli-algebra@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_time_extension_of_this_world
- kind: check
  ref: check.py::check_space_extension_of_this_world
- kind: check
  ref: check.py::check_mirror_extensions
- kind: proof
  derivation: main
locators:
  paper: T14a
  number: Thm 3.1
  label: thm:mirror
  line: 481
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.sta-matrix, std-algebra.pauli-algebra where the proof uses them. Version 3 -> 4.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the shadow, bivector and Wick copies in Cl(2,3), Cl(1,4) and the mirror''s extensions, their Wedderburn types, intersections and spans. Version 2 -> 3.'
  env: theorem
  typing:
    by: ai-typing-pass
    note: 'Both uses are invoked in the proof and kept. Levels pass: conditions already kept.'
---

## formal
In $\Cl(2,3)$, the time extension of this world with $e_{5}^{2} = +1$:
\begin{enumerate}
\item[(i)] the generators $e_{1}, \ldots, e_{4}$ generate a copy of $\Cl(1,3)$, this world's shadow;
\item[(ii)] the bivectors $e_{\mu}e_{5}$, $\mu = 1, \ldots, 4$, anticommute pairwise, square to $(-1, +1, +1, +1)$, and generate the whole even subalgebra, which is a copy of $\Cl(3,1)$, the mirror's shadow;
\item[(iii)] the two copies meet exactly in the even part of the shadow, $\Cl^{0}(1,3) \cong \Mat(2,\C)$, of dimension eight, the Lorentz algebra with its Weyl spinors; and together with $\omega$ they span everything, $\Cl(2,3) = \Cl(1,3) \oplus \omega\,\Cl(1,3)$;
\item[(iv)] no automorphism of $\Cl(2,3)$ carries the copy of $\Cl(1,3)$ onto the copy of $\Cl(3,1)$; the natural map between their generating sets is multiplication by the central $\omega$, $e_{\mu} \mapsto \omega e_{\mu}$, which squares to $-e_{\mu}^{2}$ (the Wick rotation) and is complex-linear, not an automorphism of the real algebra.
\end{enumerate}
In $\Cl(1,4)$, the space extension with $e_{5}^{2} = -1$: the generators $e_{\mu}$ and the bivectors $e_{\mu}e_{5}$ both generate copies of $\Cl(1,3)$, the elements $\omega e_{\mu}$ generate a third, and $\Cl(3,1)$ admits no unital embedding into $\Cl(1,4)$ at all. The same statements hold for the mirror's two extensions with the roles of $\Cl(1,3)$ and $\Cl(3,1)$ exchanged.

## technical
In $\Cl(2,3)$, this world's time extension with $Q(e_{5}) = +1$, the generators $e_1, \ldots, e_4$ generate a copy of this world's $\Cl(1,3)$, while the bivectors $e_\mu e_5$ anticommute pairwise with squares $(-1,+1,+1,+1)$ and generate the whole even subalgebra, a copy of the mirror's $\Cl(3,1)$. The two copies meet exactly in $\Cl^{0}(1,3) \cong \Mat(2,\C)$, of dimension eight, and $\Cl(2,3) = \Cl(1,3) \oplus \omega\,\Cl(1,3)$. No automorphism of $\Cl(2,3)$ carries one copy onto the other: the natural map $e_\mu \mapsto \omega e_\mu$, a Wick rotation reversing each square, is complex-linear and not an automorphism of the real algebra.

In the space extension $\Cl(1,4)$, with $Q(e_{5}) = -1$, the generators $e_\mu$, the bivectors $e_\mu e_5$ and the elements $\omega e_\mu$ all generate copies of $\Cl(1,3)$, and $\Cl(3,1)$ admits no unital embedding into $\Cl(1,4)$. The mirror's two extensions behave the same way with $\Cl(1,3)$ and $\Cl(3,1)$ exchanged.

## lay
When our spacetime algebra is extended by an extra time direction, the mirror world's algebra appears inside the result, sharing with ours exactly the part that describes Lorentz rotations and spinors. Even so, no symmetry of the enlarged algebra turns ours into the mirror's; the link between them is a Wick rotation, which needs complex numbers. When the extra direction is of space type instead, the mirror's algebra cannot be found inside at all.

## one-liner
The time extension $\Cl(2,3)$ contains both $\Cl(1,3)$ and the mirror $\Cl(3,1)$, meeting in $\Cl^{0}(1,3)$ and related only by a complex-linear Wick rotation, while the space extension $\Cl(1,4)$ admits no unital copy of $\Cl(3,1)$.
