---
id: std-algebra.complex-numbers
kind: claim
version: 2
title: The complex numbers inside Clifford algebras
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- dictionaries
- pseudoscalar-and-centre
proposed_by:
  kind: ai
  session: algebra-core-2026-10-26
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 2
  source: maintainer pass 2026-11-07 (GA units)
review: typed
trust: ai-proposed
about:
- obj.std-algebra.clifford-algebra
- obj.std-algebra.even-subalgebra
derivations:
- name: main
  uses:
  - std-algebra.orthogonal-anticommute@1
  - std-algebra.z2-grading@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_two_copies_of_the_complex_numbers
locators:
  sources:
  - key: DoranLasenby2003
    locator: Ch. 2 (geometric algebra in two and three dimensions)
outside_ga:
  kind: bridge
  why: 'the result identifies the complex numbers a + b i with Cl(0,1) and with the even part of the plane, so it names the abstract field C and its unit i to connect them with geometric algebra'
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (bridge): the result identifies the complex numbers a + b i with Cl(0,1) and with the even part of the plane, so it names the abstract field C and its unit i to connect them with geometric algebra.'
  referee_fixes: '2026-10-26: "rotates" corrected to "rotates and scales" (a pure rotation for a^2 + b^2 = 1) (referee part 1, point 5).'
  by: algebra-core-2026-10-26
---

## formal
(i) $\Cl(0,1) = \R 1 \oplus \R e_1$ with $e_1^{2} = -1$ is isomorphic to $\C$ by $a + b e_1 \mapsto a + b\,\mathrm{i}$. (ii) The even subalgebra $\Cl^{+}(2,0) = \R 1 \oplus \R e_1 e_2$ is isomorphic to $\C$ by $a + b\, e_1 e_2 \mapsto a + b\, \mathrm{i}$; the unit bivector $e_1 e_2$ is the imaginary unit of the plane, and $e_1 (a + b\, e_1 e_2) = a e_1 + b e_2$ rotates $e_1$ by the angle of $a + b\,\mathrm{i}$ and scales it by $|a + b\,\mathrm{i}|$ (a pure rotation when $a^{2} + b^{2} = 1$).

## technical
The complex numbers appear twice: as the algebra of one direction squaring to minus one, and as the even part of the plane, where the unit bivector squares to minus one and acts on vectors by rotation through a right angle. Complex multiplication is the geometric product, and the imaginary unit has a geometric meaning: an oriented plane.

## lay
The imaginary unit $\mathrm{i}$ is the oriented unit square of a plane. Multiplying an arrow in the plane by it turns the arrow through a right angle, and complex numbers are numbers plus multiples of that square.

## one-liner
$\Cl(0,1) \cong \C$ and $\Cl^{+}(2,0) = \operatorname{span}\{1, e_1 e_2\} \cong \C$, the unit bivector playing $\mathrm{i}$.
