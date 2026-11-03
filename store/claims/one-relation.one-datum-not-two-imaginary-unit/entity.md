---
id: one-relation.one-datum-not-two-imaginary-unit
kind: claim
version: 3
title: 'One datum, not two: the imaginary unit is the rest frame read through the law'
status: proved
region: one-relation
subject: one-relation
tags: [pseudoscalar-and-centre]
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
  - one-relation.odd-square-roots-chiral-phase@5
  - std-algebra.duality@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_commutant_of_c
- kind: check
  ref: check.py::check_complex_structures_are_a_two_sheeted_hyperboloid
- kind: check
  ref: check.py::check_j_to_gamma0_bijection
- kind: check
  ref: check.py::check_joint_commutant_is_the_spin_plane_u1
- kind: check
  ref: check.py::check_alignment_and_ideal_picture
locators:
  paper: T16
  number: Lem 5.6
  label: lem:onedatum
  line: 787
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.duality where the proof uses them. Version 2 -> 3.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the commutant of C in Cl^+ (dimension 4), J^2 = -1 iff a = 0 and d^2 - b^2 - c^2 = 1 on a 6^4 grid, the bijection J -> CJ onto unit timelike vectors orthogonal to u, the joint commutant span{1, J}, the realignment rotor and the ideal picture. Version 1 -> 2.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: 'Kept the odd-roots lemma: the statement and proof use its representation freedom and its rotor to align the laboratory frame.'
---

## formal
Align the representative so that $C = Iu$. The complex structures the descent of step (4) needs are the constant even $J$ with $J^{2} = -1$ commuting with $C$, so that the plane-wave factor $\exp(-Jp \cdot x)$ passes through $C$. The commutant of $C$ in $\Cl^{+}(1,3)$ is four-dimensional, spanned by $1$ and the three bivectors of the $3$-space orthogonal to $u$ (for $u = \gamma_{3}$: $1, \gamma_{0}\gamma_{1}, \gamma_{0}\gamma_{2}, \gamma_{1}\gamma_{2}$); the pseudoscalar, though even and a square root of $-1$, anticommutes with $C$ and is excluded. On the commutant $J^{2} = -1$ iff the scalar part vanishes and the bivector part has unit timelike-signature norm, a two-sheeted hyperboloid. The map $J \mapsto \gamma_{0} := CJ$ is a bijection from that hyperboloid onto the unit timelike vectors orthogonal to $u$, with inverse $J = C^{-1}\gamma_{0}$. So, given the law, choosing the imaginary unit and choosing the rest frame are one choice, not two. The joint commutant of $(C, J)$ in $\Cl^{+}(1,3)$ is $\mathrm{span}\{1, J\}$, whose rotors form the $U(1)$ of rotations in the spin plane, Hestenes' electromagnetic phase, which minimal coupling already uses. Any laboratory frame can be aligned: if the laboratory's $\gamma_{0}$ is not orthogonal to the representative's $u$, a rotor of the freedom of Lemma \claimref{one-relation.odd-square-roots-chiral-phase} realigns $u$, and that freedom is used up there, once, and is not to be counted again as the empty freedom of step (3).

## technical
Align the representative so that $C = Iu$. The complex structures the descent needs are the constant even $J$ with $J^{2} = -1$ commuting with $C$. The commutant of $C$ in $\Cl^{+}(1,3)$ is four-dimensional, spanned by $1$ and the three bivectors of the $3$-space orthogonal to $u$; the pseudoscalar anticommutes with $C$ and is excluded. On the commutant, $J^{2} = -1$ cuts out a two-sheeted hyperboloid, and $J \mapsto \gamma_{0} = CJ$ is a bijection onto the unit timelike vectors orthogonal to $u$, with inverse $J = C^{-1}\gamma_{0}$.

So, given the law, choosing the imaginary unit and choosing the rest frame are one choice, not two. The joint commutant of $C$ and $J$ is $\mathrm{span}\{1, J\}$, whose rotors are the $U(1)$ of the spin plane, the electromagnetic phase. A laboratory frame not orthogonal to $u$ is aligned once by the rotor freedom of the odd-roots lemma, which is then used up.

## lay
Quantum mechanics uses an imaginary unit, and nonrelativistic physics uses a rest frame. In this algebraic form of the electron's equation, once the law is fixed, picking one automatically picks the other. So the imaginary unit is not an extra ingredient that has to be put in by hand.

## one-liner
Given the law with $C = Iu$, the admissible imaginary units $J$ correspond one to one with unit timelike rest-frame vectors orthogonal to $u$, via $\gamma_{0} = CJ$.
