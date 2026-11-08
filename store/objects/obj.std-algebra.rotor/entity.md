---
id: obj.std-algebra.rotor
kind: object
version: 3
title: Rotors
status: defined
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- rotors-and-stabilisers
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
  version: 3
  source: run 2026-11-08-foundation-layer
review: typed
trust: ai-proposed
about:
- obj.std-algebra.pin-spin
- obj.std-algebra.reversion
founded_on:
- synthesis.continuum-completion-premise@2
locators:
  sources:
  - key: DoranLasenby2003
    locator: 'Ch. 4 (foundations of geometric algebra: rotors, versors)'
  - key: HestenesSobczyk1984
    locator: Ch. 3 (versors, rotors and the bivector algebra)
extraction:
  maintainer_pass_2026_11_08_foundation:
    by: ai-maintainer-pass
    note: >-
      Version 2 -> 3. Leon's decision of 8 November 2026: the foundation layer. Founded on synthesis.continuum-completion-premise: the algebra it is stated in rests on the foundation. Foundation postulates are reported as what a result rests on, separately from the premises it holds given (store/conventions.md, "The foundation").
  by: algebra-core-2026-10-26
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Version 2: wording note for degenerate Q added at the formal and technical levels: the group of even R with R R~ = 1 and R V R~ = V can be larger than the rotors (the even versors), as e^{f_1 f_2} = 1 + f_1 f_2 in Cl(0,0,2) shows (std-algebra.bivector-exponential-in-spin (iii)). The definition itself is unchanged.'
---

## formal
A \emph{rotor} is an even versor $R$ with $R \tilde{R} = 1$. Rotors form a group under the geometric product, with $R^{-1} = \tilde{R}$, and act on $V$ by $x \mapsto R x \tilde{R}$ ($= \Ad_R(x)$, since $R$ is even). Scaled to unit factors, a rotor is an element of $\Spin^{+}(V, Q)$. The definition does not require $Q$ to be nondegenerate. \emph{Note (degenerate $Q$).} The group $\{R \in \Cl^{+} : R\tilde{R} = 1,\ R V \tilde{R} = V\}$ contains the rotors and can be larger when $Q$ is degenerate: in $\Cl(0,0,2)$ every vector is null, so the only versor is $1$, while $R = e^{f_1 f_2} = 1 + f_1 f_2$ is even, has $R\tilde{R} = 1$ and fixes every vector (\claimref{std-algebra.bivector-exponential-in-spin}(iii)). A statement about that larger group says so; a rotor is always an even versor.

## technical
A rotor is a product of an even number of invertible vectors whose reverse is its inverse. It acts on vectors by the two-sided sandwich $R x \tilde{R}$, which is an even number of reflections. The rotors are the group $\Spin^{+}$, and they make sense in degenerate algebras too, where they include translations. In a degenerate algebra the even elements with $R\tilde{R} = 1$ that map vectors to vectors can be more than the rotors: in $\Cl(0,0,2)$, where every vector is null, $1 + f_1 f_2$ is such an element but no product of invertible vectors.

## lay
A rotor is the algebra's way of encoding a rotation or a boost. It is a product of an even number of arrows, and applying it twice from both sides of an arrow turns the arrow. Undoing it means writing the product backwards.

## one-liner
A rotor is an even versor with $R\tilde{R} = 1$; rotors form $\Spin^{+}$ and act by $x \mapsto R x \tilde{R}$.
