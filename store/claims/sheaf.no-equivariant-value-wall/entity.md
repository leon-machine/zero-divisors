---
id: sheaf.no-equivariant-value-wall
kind: claim
version: 5
title: No equivariant value at the wall
status: proved
region: sheaf
subject: walls
tags: [no-go, ladder-pairs]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T04, deposited version
review: typed
about:
- obj.three-routes.candidates-base-unipotents
derivations:
- name: main
  uses:
  - sheaf.base-unipotents-wall@3
  - sheaf.solve-closed-radical-gauge@3
  - sheaf.transversal-independence-wall@4
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T04.py
  tags:
  - num:10.4
- kind: check
  ref: check.py::check_theta_is_automorphism_fixing_k
- kind: check
  ref: check.py::check_dual_action_translates_candidates
- kind: check
  ref: check.py::check_no_theta_fixed_ladder_partner
- kind: check
  ref: check.py::check_partners_attached_injectively
locators:
  paper: T04
  number: Thm 10.4
  label: thm:novalue
  line: 1376
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: theta = ghat Phi^-1 is an automorphism of (T,h_u) fixing k, its dual action is a free translation of candidates, Fix(theta) is orthogonal to k, and candidates give distinct partners. Version 4 -> 5.'
  env: theorem
  context_refs:
  - sheaf.transversal-independence-wall
  - transport.no-go-level-elements
  typing:
    by: ai-typing-pass
    added: [sheaf.transversal-independence-wall]
    note: "Added transversal independence, whose intertwiner and partner formula the automorphism and the partner clause are built from; the comparison with the no-repair theorem of the root paper is an analogy, not a premise, and was not added."
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - sheaf.transversal-independence-wall
---

## formal
At a point of $\Sig$ with the collar constants $\mu, \nu$ and the bump held fixed, call a vector $u'$ with $k(u') = 1$ a \emph{candidate value} for the dying direction $k$; the candidates form an affine space over $\ker k$. For every $\lambda \in \ker k$ the composite $\theta_\lambda := \hat g_\lambda \circ \Phi_\lambda^{-1}$, with $\hat g_\lambda := g_\lambda \oplus \id$ on $T = T^*M \oplus \operatorname{span}\{\nO, \nInf\}$, is an automorphism of the completed structure $(T, h_u, k)$: an $h_u$-isometry restricting to $g_\lambda$ on $T^*M$ and fixing $k$, hence an automorphism of the completed Clifford algebra preserving its grading and its degeneration subalgebra. Its contragredient action on vectors, $(\theta_\lambda|_{T^*M})^{-\mathsf{T}} = \id - \lambda \otimes k$, translates every candidate by $-\lambda$. A natural assignment of a candidate value, one per completed structure and commuting with automorphisms, would therefore be a fixed point of a free translation action of $(\ker k, +)$: none exists. Nor is a ladder partner for $k$ any more canonical than a value: for $\lambda \neq 0$, $h_u(k, x) = 0$ for every $x \in \operatorname{Fix}(\theta_\lambda)$, whereas a ladder partner has $h_u(k, x) = \tfrac12$; and the construction attaches to each candidate $u' = u + v$ the partner $\Phi_v(k^*) = k^* + \tfrac12\tilde v$ of Theorem \claimref{sheaf.transversal-independence-wall}, injectively in $v$. An analogue of the no-repair theorem of \cite[Thm.~4.2]{ButlerT1} thus holds at the wall itself, where the base form carries no hyperbolic partner for $k$ and that theorem's hypotheses fail.

## technical
At a wall point, with the collar constants and bump fixed, a candidate value for the dying direction $k$ is a vector $u'$ with $k(u') = 1$; the candidates form an affine space over $\ker k$. For each $\lambda \in \ker k$ the composite $\theta_\lambda = \hat g_\lambda \circ \Phi_\lambda^{-1}$ is an automorphism of the completed structure $(T, h_u, k)$, hence of the completed Clifford algebra with its grading and degeneration subalgebra, and on vectors it acts by $\id - \lambda \otimes k$, translating every candidate by $-\lambda$.

A natural assignment of a candidate value, commuting with automorphisms, would be a fixed point of a free translation action of $\ker k$, so none exists. A ladder partner for $k$ is no more canonical: for $\lambda \neq 0$ every $x$ fixed by $\theta_\lambda$ has $h_u(k,x) = 0$, whereas a partner has $h_u(k,x) = \tfrac12$, and distinct candidates give distinct partners. This is an analogue at the wall of the fibre-level no-repair theorem, whose hypotheses fail there.

## lay
To repair the wall one has to pick a direction to pair with the dying one. This result shows that the repaired structure has symmetries that move any such choice to a different one, so no choice can be singled out naturally. The same holds for the partner element used in the repair: it is a choice, not something the geometry provides.

## one-liner
The completed structure at the wall has automorphisms that translate candidate values of the dying direction freely, so no equivariant value, and no canonical ladder partner, exists.
