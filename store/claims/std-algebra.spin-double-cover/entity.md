---
id: std-algebra.spin-double-cover
kind: claim
version: 1
title: Spin double-covers the special orthogonal group
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- rotors-and-stabilisers
- spinor-modules
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
review: typed
trust: ai-proposed
about:
- obj.std-algebra.pin-spin
- obj.std-algebra.rotor
- obj.std-algebra.clifford-group
derivations:
- name: main
  uses:
  - primer.twisted-adjoint-action@3
  - primer.centre@2
  - std-algebra.cartan-dieudonne@1
  - std-algebra.reflection@1
  - std-algebra.inverse-of-vector@1
  - std-algebra.orthogonal-anticommute@1
  - std-algebra.z2-grading@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_spin_homomorphism_and_kernel
- kind: check
  ref: check.py::check_kernel_is_plus_minus_one
locators:
  sources:
  - key: Lounesto2001
    locator: Ch. 17 (spin groups and spinor spaces)
  - key: Porteous1995
    locator: the Clifford group, Pin and Spin
  - key: LawsonMichelsohn1989
    locator: Ch. I, Sec. 2
extraction:
  referee_fixes: '2026-10-26: states that SO+ is the kernel of the spinor norm (identity component cited, not proved); proof now shows explicitly that R R~ = 1 forces an even number of factors with prod Q > 0, putting the image in SO+ (referee part 2, point 1).'
  by: algebra-core-2026-10-26
---

## formal
Let $(V, Q)$ be nondegenerate of dimension $n \ge 1$. The twisted adjoint action gives surjective homomorphisms with kernel $\{\pm 1\}$:
\begin{equation}
\Pin(V, Q) \to \mathrm{O}(V, Q), \qquad \Spin(V, Q) \to \mathrm{SO}(V, Q), \qquad \Spin^{+}(V, Q) \to \mathrm{SO}^{+}(V, Q).
\end{equation}
Here $\mathrm{SO}^{+}$ is the kernel of the spinor norm, as defined in \claimref{obj.std-algebra.pin-spin}; for nondegenerate $V$ it is the identity component of $\mathrm{SO}(V, Q)$, a standard fact cited there and not proved in the store. A versor of $k$ factors acts with determinant $(-1)^{k}$. For a rotor, $\Ad_R(x) = R x \tilde{R}$. Nondegeneracy is needed for the kernel: for degenerate forms $\Ad$ has a larger kernel or a smaller image.

## technical
Every isometry of a nondegenerate space comes from a product of unit vectors, and exactly two such products, $g$ and $-g$, give the same isometry. Even products give the isometries of determinant one; even products with $R\tilde{R} = 1$, the rotors, give the subgroup $\mathrm{SO}^{+}$. So each rotation or boost has exactly two rotors, $\pm R$.

## lay
Every rotation, and every Lorentz boost, is produced by a rotor, and by exactly two of them, which differ by a sign. This two-to-one relation is the origin of spin one-half: a full turn of space changes the sign of the rotor.

## one-liner
For nondegenerate $Q$, $\Ad$ maps $\Pin \to \mathrm{O}$, $\Spin \to \mathrm{SO}$ and $\Spin^{+} \to \mathrm{SO}^{+}$ onto, each with kernel $\{\pm 1\}$.
