---
id: singularity.chains-state-class-stability
kind: claim
version: 7
title: The chain's state class, and its stability
status: proved
region: singularity
subject: descent
tags: [thermal-premises, entanglement, modular-theory]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
review: typed
about:
- obj.singularity.geometric-modular-condition-g
derivations:
- name: main
  uses:
  - singularity.exact-equilibrium-over-determines-boundary-modes@5
  - singularity.kms-uniqueness-factor@5
  - singularity.number-diagonal-dynamics-models-scrambling-derived@4
  - singularity.parity-protection@2
  - singularity.rate-discharge-hypothesis-iii@5
  proof: proof-main.tex
  assumes:
  - singularity.p-univalence@2
  - singularity.r-regularity-fixed-locus@3
  - singularity.l-boundary-mode-locality@2
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:7.32
- kind: check
  ref: check.py::check_members_are_even_with_gibbs_kms_marginals
- kind: check
  ref: check.py::check_class_invariant_under_number_diagonal_dynamics
- kind: check
  ref: check.py::check_product_member_and_unbounded_correlation
locators:
  paper: T05
  number: Cor 7.32
  label: cor:stateclass
  line: 1984
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: members of C are even with Gibbs KMS marginals, number-diagonal dynamics keeps C while hopping leaves it, and the product member plus pure members with correlation and deficit growing with the number of pairs. Version 4 -> 5. check.py docstring (3) reworded ((G) is rho = e^(-beta K_geo)/Z, not E_N-fixedness); added a diagonal correlated member that is in C and E_N-fixed (fix round 2026-10-23). Version 5 -> 6. Check strengthened: hopping control pins the moved populations exactly; sample dynamics and the hop moved to module level. Version 6 -> 7.'
  env: corollary
  context_refs:
  - singularity.eviction-window-thermal-product-radiation-entropy
  typing:
    by: ai-typing-pass
    removed:
    - transport.transport-algorithm
    added:
    - singularity.l-boundary-mode-locality
    - singularity.p-univalence
    - singularity.r-regularity-fixed-locus
    note: 'kept the five series premises the proof invokes; added (P), (R) and (L_E) to assumes because
      clauses (1) and (2) are stated under them; the eviction-window theorem is cited for what the rate
      model later does with the freedom, not as a premise, so it was not added; removed the mechanical
      repair edge to the transport algorithm: the section frames its results as a step of that algorithm,
      but the proof is a self-contained computation and does not use it as a premise Levels pass: conditions
      already kept.'
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
---

## formal
Let $\mathcal{C}$ be the set of even states of the boundary modes every single-mode marginal of which is the Gibbs state of $K_k$ at $\beta = 2\pi/\kappa$. Then:
\begin{enumerate}
\item under (P) and (R) the state of the boundary modes lies in $\mathcal{C}$, and every member of $\mathcal{C}$ satisfies (P) and (R);
\item $\mathcal{C}$ is invariant under every internal dynamics that (L$_E$) permits: a state placed in $\mathcal{C}$ at injection stays in $\mathcal{C}$ thereafter, whatever the boundary modes write;
\item $\mathcal{C}$ contains the product state $e^{-\beta K_{\mathrm{geo}}}/Z$, which is its only member satisfying (G), and it contains states of arbitrarily large total correlation $C(\varrho)$ and descent deficit; (R) constrains none of the correlations.
\end{enumerate}
So the premises fix the marginals once and for all, and leave the joint state exactly as free as Steps 5 and 6b need it; the rate model then exercises that freedom across the window/radiation cut, its window marginal being itself the product member at every stage (Theorem \claimref{singularity.eviction-window-thermal-product-radiation-entropy}(1)).

## technical
Let $\mathcal{C}$ be the set of even states of the boundary modes all of whose single-mode marginals are the Gibbs state of $K_k$ at $\beta = 2\pi/\kappa$. Under premises (P) and (R) the state of the boundary modes lies in $\mathcal{C}$, and every member of $\mathcal{C}$ satisfies (P) and (R). Every internal dynamics that (L$_E$) permits is conjugation by a diagonal unitary, which commutes with the total parity and preserves every marginal, so $\mathcal{C}$ is invariant: a state placed in it at injection stays in it, whatever the boundary modes write.

The class contains the product state $e^{-\beta K_{\mathrm{geo}}}/Z$, its only member satisfying (G), and also states of arbitrarily large total correlation $C(\varrho)$ and descent deficit; (R) constrains none of the correlations. So under these premises the marginals are fixed once and for all, while the joint state is left free.

## lay
Under the two premises adopted for the boundary modes, each mode on its own must look thermal at the Hawking temperature and carry no coherence between being empty and occupied. This result shows that the set of states meeting those conditions is closed under every internal evolution the locality premise allows. The set contains the simple uncorrelated thermal state, but also states with as much correlation between modes as one likes, so the premises pin down each mode individually while leaving the correlations open.

## one-liner
Under (P) and (R) the boundary modes lie in the class of even states with Gibbs marginals at $\beta = 2\pi/\kappa$, a class stable under every dynamics (L$_E$) permits that contains the (G) product state and arbitrarily correlated states.
