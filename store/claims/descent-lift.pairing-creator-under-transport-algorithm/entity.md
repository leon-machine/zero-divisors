---
id: descent-lift.pairing-creator-under-transport-algorithm
kind: claim
version: 4
title: The pairing creator under the transport algorithm
status: proved
region: descent-lift
subject: descent
tags: [transport-algorithm, pairing-and-bogoliubov, descent-map]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-descent-lift, the series'' standard disclaimer'
review: typed
about:
- obj.transport.obstruction-types
- obj.transport.equivariance
derivations:
- name: main
  uses:
  - descent-lift.imported-pinching-one-way-door@4
  - descent-lift.imported-taxonomy-type-p-rule-algorithm@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_type_p_and_annihilating_idempotents
- kind: check
  ref: check.py::check_moore_penrose_and_fock_adjoint
- kind: check
  ref: check.py::check_rung_bivector_is_cartan
- kind: check
  ref: check.py::check_reflection_exchanges_hop_and_pairing
- kind: check
  ref: check.py::check_generators_square_and_rotors
- kind: check
  ref: check.py::check_pairing_pair_identities
- kind: check
  ref: check.py::check_pinching_erases_ladder_words
locators:
  paper: T05-descent-lift
  number: Prop 6.3
  label: prop:typeP
  line: 281
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: all seven clauses in Cl(2,2): type P with hyperbolic-pair annihilating idempotents, the Penrose equations for n^dag, the Cartan bivector, the e4 reflection, X_p^2 = -P_even, X_h^2 = -P_odd and the (3/5, 4/5) rotors, the pair identities, and the pinchings. Version 3 -> 4.'
  env: proposition
  context_refs:
  - descent-lift.imported-pinching-one-way-door
  - descent-lift.imported-taxonomy-type-p-rule-algorithm
  - transport.rule-1-morita-trivial
  typing:
    by: ai-typing-pass
    added:
    - descent-lift.imported-taxonomy-type-p-rule-algorithm
    - descent-lift.imported-pinching-one-way-door
    note: 'added the taxonomy-and-algorithm fact (clauses (i) and (ii) diagnose and repair by it) and
      the pinching fact (clause (vii) applies it); did not add the root paper''s Rule 1 theorem, cited
      only for the ladder-pair setup, which the statement writes out explicitly. Levels pass: lay no longer
      says the algorithm hands back the pair annihilator (it returns no element; the annihilator is the
      pseudo-inverse), and lay and one-liner keep ''on either reading''.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    stated_role:
    - descent-lift.imported-taxonomy-type-p-rule-algorithm
    - descent-lift.imported-pinching-one-way-door
---

## formal
Take two rungs in the root paper's real form, $\Cl(2,2)$ with orthogonal basis $e_{1}, e_{2}$ of square $+1$ and $e_{3}, e_{4}$ of square $-1$, ladder pairs $f_{k} = \tfrac12(e_{k} + e_{k+2})$, $f_{k}^{*} = \tfrac12(e_{k} - e_{k+2})$, number projectors $f_{k}^{*}f_{k}$ and vacuum projector $P_{00} = f_{1}f_{1}^{*}f_{2}f_{2}^{*}$ \cite[Thm.~7.1]{ButlerT1}. Let $n = f_{1}^{*}f_{2}^{*}$ be the pairing creator, $h = f_{1}^{*}f_{2}$ the hop, and $\dagger$ the Fock adjoint, the anti-automorphism that exchanges $f_{k}$ and $f_{k}^{*}$.
\begin{enumerate}
\item[(i)] $n$ is a nonzero pure bivector with $n^{2} = 0$, the algebra is simple, and $n$ has annihilating idempotents in the sense of Fact \claimref{descent-lift.imported-taxonomy-type-p-rule-algorithm}, both non-central: $e = f_{2}f_{2}^{*}$ on the right, $n(1 - e) = n\,f_{2}^{*}f_{2} = 0$, and $f = f_{1}^{*}f_{1}$ on the left, $(1 - f)n = f_{1}f_{1}^{*}\,n = 0$. Under Step 2, which tests the element's grade first, $n$ is type P and Step 3 adjoins nothing. Both annihilating idempotents are of hyperbolic-pair form, $f_{2}f_{2}^{*} = wv$ for $(v, w) = (f_{2}^{*}, f_{2})$ and $f_{1}^{*}f_{1} = vw$ for $(v, w) = (f_{1}^{*}, f_{1})$, so under the refinement of Fact \claimref{descent-lift.imported-taxonomy-type-p-rule-algorithm} the obstruction is the type-N one carried by the adjoined null vectors $f_{1}^{*}, f_{2}^{*}$ themselves, for which the no-go theorem closes every equivariant element-level repair and the point-level repair is a further $(1,1)$ ascent, which acts on points and not on $n$. On either reading the algorithm returns no element from $n$.
\item[(ii)] The pair annihilation $n^{\dagger} = f_{2}f_{1}$ satisfies the four Penrose equations with $n$: it is the Moore--Penrose inverse for $\dagger$, and its idempotents $nn^{\dagger} = P_{11}$ and $n^{\dagger}n = P_{00}$ are the self-adjoint ones that Fact \claimref{descent-lift.imported-taxonomy-type-p-rule-algorithm} singles out where a definite form is available, the Fock form here. It annihilates the vacuum.
\item[(iii)] The bivector a rung carries, $f \wedge f^{*} = \tfrac12(ff^{*} - f^{*}f)$, squares to $+\tfrac14$ and commutes with the number operator: it is the Cartan element of the mode.
\item[(iv)] The reflection $e_{4} \mapsto -e_{4}$ extends to an automorphism of $\Cl(2,2)$ that fixes $f_{1}$, carries $f_{2}$ to $f_{2}^{*}$, $h$ to $n$, the hop generator $X_{h} = h - h^{\dagger}$ to the pairing generator $X_{p} = n - n^{\dagger}$, and $P_{00}$ to $P_{01}$.
\item[(v)] $X_{p}^{2} = -P_{\mathrm{even}}$ and $X_{h}^{2} = -P_{\mathrm{odd}}$ with $P_{\mathrm{even}} = P_{00} + P_{11}$ and $P_{\mathrm{odd}} = P_{01} + P_{10}$; so $\exp(\theta X) = (1 - P) + \cos\theta\,P + \sin\theta\,X$, and at $(\cos\theta, \sin\theta) = (\tfrac35, \tfrac45)$ both exponentials are rotors of $\mathrm{Spin}(2,2)$, unitary for $\dagger$; the pairing rotor carries $P_{00}$ to $\tfrac35 P_{00} + \tfrac45\,nP_{00}$, the singularity paper's witness state in the Fock ideal, and the hop rotor fixes $P_{00}$.
\item[(vi)] On the even sector $n$ and $n^{\dagger}$ satisfy the root paper's hyperbolic-pair identities, $n^{2} = (n^{\dagger})^{2} = 0$ and $nn^{\dagger} + n^{\dagger}n = P_{\mathrm{even}}$, and $X_{p} = n - n^{\dagger}$; the pairing rotation is the rotation of the plane this pair spans.
\item[(vii)] The root paper's pinching for either rung (Fact \claimref{descent-lift.imported-pinching-one-way-door}) erases $n$, $h$, $X_{p}$ and $X_{h}$ alike and fixes the parity sections $\sigma_{1}, \sigma_{2}, \sigma_{1}\sigma_{2}$.
\end{enumerate}

## technical
In two rungs, $\Cl(2,2)$ with ladder pairs $f_{k} = \tfrac12(e_{k} + e_{k+2})$ and $f_{k}^{*} = \tfrac12(e_{k} - e_{k+2})$, take the pairing creator $n = f_{1}^{*}f_{2}^{*}$, the hop $h = f_{1}^{*}f_{2}$ and the Fock adjoint $\dagger$. The creator is a nonzero pure bivector with $n^{2} = 0$, annihilated on each side by non-central idempotents, so Step 2 of the transport algorithm diagnoses type P and Step 3 adjoins nothing; under the hyperbolic-pair refinement it is instead the type-N obstruction of the adjoined null vectors, whose repair acts on points. On either reading the algorithm returns no element from $n$. Its Moore-Penrose inverse for $\dagger$ is the pair annihilation $n^{\dagger} = f_{2}f_{1}$, with $nn^{\dagger} = P_{11}$ and $n^{\dagger}n = P_{00}$.

The reflection $e_{4}\mapsto -e_{4}$ is an automorphism exchanging $h$ with $n$ and the hop generator $X_{h} = h - h^{\dagger}$ with the pairing generator $X_{p} = n - n^{\dagger}$. Since $X_{p}^{2} = -P_{\mathrm{even}}$ and $X_{h}^{2} = -P_{\mathrm{odd}}$, $\exp(\theta X) = (1 - P) + \cos\theta\,P + \sin\theta\,X$, and at $(\cos\theta, \sin\theta) = (\tfrac35, \tfrac45)$ both are rotors of $\Spin(2,2)$, the pairing rotor producing the singularity paper's witness state. On the even sector $n$ and $n^{\dagger}$ form a hyperbolic pair; each rung's bivector $f\wedge f^{*}$ is the mode's Cartan element; and the root paper's pinching erases $n$, $h$, $X_{p}$ and $X_{h}$ while fixing the parity sections.

## lay
The question is whether the transport procedure, run on the operator that creates a pair of particles, produces the pair-creating rotation that the earlier work had to exclude by hand. It does not: on either reading of the procedure's classification step, it returns nothing from the pair creator. The creator's partner, the pair annihilator, is its generalised inverse, a separate fact rather than an output of the procedure. The algebra itself contains the pairing rotation and the ordinary hopping rotation on equal footing, related by a reflection, and the one-way averaging map erases both.

## one-liner
Run on the pairing creator in $\Cl(2,2)$ the transport algorithm returns no element on either reading of its diagnosis, the creator's Moore-Penrose inverse for the Fock adjoint is the pair annihilation, and the pairing and hop rotors are exchanged by a reflection and erased alike by the pinching.
