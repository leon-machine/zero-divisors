---
id: obj.std-algebra.pin-spin
kind: object
version: 2
title: Pin and Spin
status: defined
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
- name: Claude Opus 5.5
  role: 'maintainer pass, foundation layer'
  version: 2
  source: run 2026-11-08-foundation-layer
review: typed
trust: ai-proposed
about:
- obj.std-algebra.clifford-group
- obj.std-algebra.even-subalgebra
founded_on:
- synthesis.continuum-completion-premise@2
locators:
  sources:
  - key: Lounesto2001
    locator: Ch. 17 (spin groups and spinor spaces)
  - key: Porteous1995
    locator: the Clifford group, Pin and Spin
  - key: LawsonMichelsohn1989
    locator: Ch. I, Sec. 2
extraction:
  maintainer_pass_2026_11_08_foundation:
    by: ai-maintainer-pass
    note: >-
      Version 1 -> 2. Leon's decision of 8 November 2026: the foundation layer. Founded on synthesis.continuum-completion-premise: the algebra it is stated in rests on the foundation. Foundation postulates are reported as what a result rests on, separately from the premises it holds given (store/conventions.md, "The foundation").
  referee_fixes: '2026-10-26: SO+ stated to mean the kernel of the spinor norm throughout; its equality with the identity component cited, not proved (referee part 2, point 1).'
  by: algebra-core-2026-10-26
---

## formal
Let $(V, Q)$ be a real quadratic space. The groups
\begin{equation}
\Pin(V, Q) = \{ u_1 \cdots u_k : Q(u_i) = \pm 1 \}, \qquad \Spin(V, Q) = \Pin(V, Q) \cap \Cl^{+}, \qquad \Spin^{+}(V, Q) = \{ R \in \Spin(V, Q) : R \tilde{R} = 1 \}
\end{equation}
are the versors of unit vectors, the even ones, and the even ones of reverse-norm $+1$. For a versor of unit vectors $g \tilde{g} = \prod_i Q(u_i) = \pm 1$ (\claimref{std-algebra.inverse-of-vector}). We write $\Pin(p,q)$, $\Spin(p,q)$, $\Spin^{+}(p,q)$ for $\R^{p,q}$; $\mathrm{O}(p,q)$, $\mathrm{SO}(p,q)$ are the isometries and those of determinant $1$, and $\mathrm{SO}^{+}(p,q)$ is the subgroup of $\mathrm{SO}(p,q)$ of products of reflections $s_{u_1} \cdots s_{u_{2m}}$ with $\prod Q(u_i) > 0$ (the kernel of the spinor norm). In the store $\mathrm{SO}^{+}$ always means this kernel. For nondegenerate $V$ it is the identity component of $\mathrm{SO}(V, Q)$, a standard fact cited from Porteous and from Lounesto, Ch. 17, and not proved here.

## technical
Pin is the group of products of unit vectors (vectors squaring to $\pm 1$), Spin its even part, and $\Spin^{+}$ the even products whose reverse-norm $R\tilde{R}$ is $+1$, equivalently those with an even number of negative-square factors. On the orthogonal side, $\mathrm{SO}^{+}$ is defined as the proper isometries built from an even number of reflections in negative-square vectors.

## lay
Pin and Spin are the groups of products of unit-length arrows. Spin keeps the products with an even number of factors; these act on space as rotations and boosts rather than mirror images.

## one-liner
$\Pin$ = versors of unit vectors, $\Spin = \Pin \cap \Cl^{+}$, $\Spin^{+} = \{R \in \Spin : R\tilde{R} = 1\}$.
