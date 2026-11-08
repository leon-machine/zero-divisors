---
id: sheaf.one-sided-completion
kind: claim
version: 4
title: One-sided completion
status: proved
region: sheaf
subject: walls
tags: [degenerate-algebras, hyperbolic-plane]
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
- obj.sheaf.collar-data-coupling
derivations:
- name: main
  uses:
  - sheaf.determinant-identity-blow-up-expansion@3
  - sheaf.local-freeness-constant-rank@2
  - sheaf.wall-gram@4
  assumes:
  - sheaf.tameness@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T04.py
  tags:
  - num:4.4
- kind: check
  ref: check.py::check_signature_constant_on_physical_side
- kind: check
  ref: check.py::check_wrong_coupling_sign_fails
- kind: check
  ref: check.py::check_fibres_locally_free_and_physical_type
locators:
  paper: T04
  number: Thm 4.4
  label: thm:onesided
  line: 615
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: signature (p+1,q+1) at the wall and on a grid of physical collar points and bump values for all p+q <= 5, the wrong-sign control, blade rank 2^(n+2) and Cl(2,4) = Mat_4(H). Version 2 -> 3. Sample inputs moved to module level; the Cl(2,4) centre test now ranges over len(sq) generators instead of a bare 6; no change to what is tested. Version 3 -> 4.'
  env: theorem
  typing:
    by: ai-typing-pass
    added:
    - sheaf.tameness
    note: 'the statement assumes (T1)-(T3) explicitly, so the tameness postulate is added to assumes;
      the existence of collar data from w_1 = 0 is carried by the collar-data definition and its imported
      line-bundle fact, so no edge was added for it Levels pass: the lay level now states tameness, $p
      \geq 1$ and the triviality of the radical line bundle, all of which it had dropped.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - sheaf.tameness
---

## formal
Assume (T1)-(T3), with signature $(p,q)$, $p \geq 1$, on the physical side $\Mp$, and assume the radical line bundle is trivial, $w_1(\shL) = 0$, so that collar data exist. Then there exists a smooth symmetric form $h$ on $T$ over $M$, equal to $G \perp H$ outside a collar of $\Sig$, which is nondegenerate of constant signature $(p{+}1, q{+}1)$ at every point of $\Mp$, including $\Sig$ itself. Consequently $\shC := \Cl(T, h)$ restricted to $\Mp$ is a locally free sheaf of algebras of constant rank $2^{n+2}$ whose every fibre is isomorphic to $\Cl(p{+}1, q{+}1)$; in the physical case, $\Cl(2,4) \cong \Mat_4(\HH)$.

## technical
Assume tameness (T1)-(T3), signature $(p,q)$ with $p \geq 1$ on the physical side $\Mp$, and a trivial radical line bundle, $w_1(\shL) = 0$, so that collar data exist. Then there is a smooth symmetric form $h$ on $T = T^*M \oplus \underline{\R}^2$, equal to $G \perp H$ outside a collar of $\Sig$, that is nondegenerate of constant signature $(p{+}1, q{+}1)$ at every point of $\Mp$, the wall included.

The proof takes coupling constants with $\mu\nu > 0$: on $\Sig$ the wall Gram gives the signature directly; in the collar on the physical side, after shrinking the collar, $s > 0$ and so $1 + 2\mu\nu\beta^2 s \geq 1$ in the determinant identity; outside the collar $h = G \perp H$. Consequently $\shC = \Cl(T, h)$ restricted to $\Mp$ is locally free of rank $2^{n+2}$ with every fibre isomorphic to $\Cl(p{+}1, q{+}1)$, which is $\Mat_4(\HH)$ in the physical case.

## lay
Assume a geometry degenerates along a wall in the tame way, with at least one positive direction on the physical side and with the dying direction's line consistently orientable along the wall. Then it can be repaired on that side by adding two extra dimensions and coupling them to the direction that is dying. This result shows that the coupling can be chosen so that the enlarged geometry is non-degenerate, with the same signature everywhere on the physical side, the wall itself included. The resulting family of algebras is then uniform: in the physical case every member is the algebra of four-by-four quaternion matrices.

## one-liner
Under tameness, with signature $(p,q)$, $p \geq 1$, on the physical side and a trivial radical line bundle, coupling an adjoined hyperbolic plane to the dying direction gives an ambient form of constant signature $(p{+}1, q{+}1)$ on the whole physical side, wall included.
