---
id: one-relation.odd-square-roots-chiral-phase
kind: claim
version: 5
title: Odd square roots of $-1$, and the chiral phase
status: proved
region: one-relation
subject: one-relation
tags: [pseudoscalar-and-centre, chirality, forcing-and-uniqueness]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T16, deposited version
review: typed
derivations:
- name: main
  uses:
  - std-algebra.pseudoscalar-commutation@1
  - primer.sign@3
  - std-algebra.vector-squares@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_square_of_an_odd_element
- kind: check
  ref: check.py::check_rotors_move_u_over_the_hyperboloid
- kind: check
  ref: check.py::check_chiral_phase
- kind: check
  ref: check.py::check_even_part_of_c_excludes_invertible_even_solutions
locators:
  paper: T16
  number: Lem 5.5
  label: lem:oddroots
  line: 779
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.pseudoscalar-commutation, primer.sign, std-algebra.vector-squares where the proof uses them. Version 4 -> 5.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: (v + Iw)^2 = Q(v) + Q(w) - 2I(v^w), the roots (cos t + sin t I)u, rotors carrying gamma_3 over the unit spacelike hyperboloid, the chiral phase C -> C e^{2tI} with the Takabayasi shift, and the parity argument forcing C odd. Version 2 -> 3. Check strengthened: singular annihilator element pinned at left-multiplication rank 8 of 16 (Mat(2,H) rank 1); oddness of gamma^mu psi over every gamma^mu. Version 3 -> 4.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  env: lemma
  typing:
    by: ai-typing-pass
    removed: [one-relation.imported-square-roots-real-clifford-algebras]
    note: 'Removed the square-roots Fact, which the proof itself calls context and not a step.'
---

## formal
An odd element of $\Cl(1,3)$ is $C = v + Iw$ with $v, w$ vectors, and $C^{2} = Q(v) + Q(w) - 2I\,(v \wedge w)$. Hence $C^{2} = -1$ if and only if $v \wedge w = 0$ and $Q(v) + Q(w) = -1$, that is $C = (\cos t + \sin t\, I)\,u$ with $u$ a unit spacelike vector. Two freedoms act on this set. The representation freedom $\psi \mapsto \psi R$ for a constant rotor $R$ carries $C$ to $\tilde{R}CR$ and moves $u$ over the whole one-sheeted hyperboloid of unit spacelike vectors, on which $\mathrm{Spin}^{+}(1,3)$ is transitive. The chiral phase $\psi \mapsto \psi\exp(tI)$ carries $C$ to $C\exp(2tI)$, because $I$ anticommutes with odd elements, and so removes $t$; it is not a rotor, its reverse being itself and not its inverse, and it shifts the Takabayasi angle by the constant $2t$. Consequently, for the single free fermion with minimal electromagnetic coupling that this section treats, and in that scope only, every first-order covariant law $\nabla\psi = m\psi C$ on $\Cl^{+}(1,3)$ whose square is Klein-Gordon at mass $m$ is the Dirac-Hestenes equation up to a constant field redefinition, the parity of the fields forcing $C$ to be odd (a law with an even part of $C$ admits no even solution invertible anywhere); with Yukawa or weak couplings the chiral phase of a mass is physical and the redefinition is not free.

## technical
An odd element of $\Cl(1,3)$ is $C = v + Iw$ with $v, w$ vectors, and $C^{2} = Q(v) + Q(w) - 2I(v \wedge w)$. So $C^{2} = -1$ exactly when $C = (\cos t + \sin t\, I)u$ with $u$ a unit spacelike vector. Constant rotors $\psi \mapsto \psi R$ move $u$ over the whole hyperboloid of unit spacelike vectors, and the chiral phase $\psi \mapsto \psi\exp(tI)$ sends $C$ to $C\exp(2tI)$, removing $t$; it is not a rotor, and it shifts the Takabayasi angle by $2t$.

Since $\psi$ is even and $\nabla$ odd, an even part of $C$ would leave no even solution invertible anywhere, so $C$ is odd. Hence, for a single free fermion with minimal electromagnetic coupling only, every first-order covariant law $\nabla\psi = m\psi C$ on $\Cl^{+}(1,3)$ squaring to Klein-Gordon at mass $m$ is the Dirac-Hestenes equation up to a constant field redefinition. With Yukawa or weak couplings the chiral phase is physical and the redefinition is not free.

## lay
An earlier result says the constant factor in the electron's law must square to minus one. This one lists every allowed factor and shows that, for a single free electron, they all give the same equation seen in a rotated frame or with a harmless constant phase. Once other interactions are included, that phase is no longer harmless.

## one-liner
The odd square roots of $-1$ in $\Cl(1,3)$ are $(\cos t + \sin t\,I)u$ with $u$ unit spacelike, so for a single free minimally coupled fermion every Klein-Gordon-squaring first-order law is Dirac-Hestenes up to a constant redefinition.
