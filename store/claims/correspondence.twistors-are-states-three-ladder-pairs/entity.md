---
id: correspondence.twistors-are-states-three-ladder-pairs
kind: claim
version: 6
title: "Conformal spinors are the states of three ladder pairs"
status: proved
region: correspondence
subject: conformal-spacetime
tags: [conformal-spinors, ladder-pairs, two-readings, spinor-modules]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T09, deposited version
review: typed
derivations:
- name: main
  uses:
  - correspondence.fock-model-complexified-ascended-algebra@7
  - correspondence.imported-ladder-pairs-fock-modules-over@1
  - correspondence.spin-representation@6
  - std-algebra.vector-squares@1
  - std-algebra.blade-basis@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T09.py
  tags:
  - label:thm:states
- kind: check
  ref: check.py::check_every_conformal_spinor_is_pure
- kind: check
  ref: check.py::check_vacuum_of_own_three_pair_system
- kind: check
  ref: check.py::check_states_not_operators_and_disjoint_families
locators:
  paper: T09
  number: Thm 5.3
  label: thm:states
  line: 672
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.vector-squares, std-algebra.blade-basis where the proof uses them. Version 5 -> 6.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: every sample conformal spinor is pure with W_u determining u, Spin-equivariance of W_u, u is the vacuum of its own three CAR pairs with Lambda U'' -> Lambda W an isomorphism, and joint kernels of maximal isotropics are one-parity lines. Version 3 -> 4. Sample inputs moved to module level; no change to what is tested. Version 4 -> 5.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  env: theorem
  typing:
    by: ai-typing-pass
    note: 'All three uses are proof premises (transitivity from the spin representation, irreducibility from the Fock model, the ladder-pair normalisation from the imported fact); the paper''s remark calls clause (1) classical (Cartan, Chevalley), but that covers one clause only, so no standard-route derivation was added although the Cartan purity import is in the store.'
  source_title: "Twistors are the states of three ladder pairs"
  source_formal: |-
    Let $u \in \T\setminus\{0\}$ and define its \emph{annihilator space} $W_u := \{v \in V_\C : c(v)u = 0\}$.
    \begin{enumerate}
    \item $W_u$ is a maximal totally isotropic ($3$-dimensional) subspace of $V_\C$: \emph{every} twistor is a pure spinor. Moreover $W_u$ determines $u$ up to scale (the joint kernel of $c(W_u)$ is the line $\C u$), so $[u] \mapsto W_u$ is an injection of $\PT$ into the maximal isotropic subspaces, equivariant for the spin action.
    \item For any maximal isotropic complement $U'$ dual to $W_u$, the map $\Lambda^\bullet U' \to \Lambda^\bullet W$, $\xi \mapsto c(\xi)u$, is a linear isomorphism: $u$ is the Fock vacuum of the three-ladder-pair system built on $(W_u, U')$, every state of the module is generated from $u$ by its own pair operators, and $\T$ (respectively $\T'$) is what the even (respectively odd) products generate. The pair system is canonical given $u$ up to the choice of dual complement.
    \item Ambient vectors act on twistor states as sums of three fermionic creation and annihilation operators; twistors are therefore not \emph{operators} of the pair algebra but its \emph{states}. The annihilator spaces of $\T$-spinors and of $\T'$-spinors are disjoint families (no maximal isotropic annihilates both a nonzero even and a nonzero odd spinor).
    \end{enumerate}
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: "Renamed twistors and twistor space to conformal spinors and the conformal spinor space (\\CS, \\CSm, \\PCS) in all levels and the proof. The annihilator spaces are still taken in the complexified $V_\\C$ of the Fock model, as in the original."
---

## formal
Let $u \in \CS\setminus\{0\}$ and define its \emph{annihilator space} $W_u := \{v \in V_\C : c(v)u = 0\}$.
\begin{enumerate}
\item $W_u$ is a maximal totally isotropic ($3$-dimensional) subspace of $V_\C$: \emph{every} conformal spinor (twistor) is a pure spinor. Moreover $W_u$ determines $u$ up to scale (the joint kernel of $c(W_u)$ is the line $\C u$), so $[u] \mapsto W_u$ is an injection of $\PCS$ into the maximal isotropic subspaces, equivariant for the spin action.
\item For any maximal isotropic complement $U'$ dual to $W_u$, the map $\Lambda^\bullet U' \to \Lambda^\bullet W$, $\xi \mapsto c(\xi)u$, is a linear isomorphism: $u$ is the Fock vacuum of the three-ladder-pair system built on $(W_u, U')$, every state of the module is generated from $u$ by its own pair operators, and $\CS$ (respectively $\CSm$) is what the even (respectively odd) products generate. The pair system is canonical given $u$ up to the choice of dual complement.
\item Ambient vectors act on conformal spinor states as sums of three fermionic creation and annihilation operators; conformal spinors are therefore not \emph{operators} of the pair algebra but its \emph{states}. The annihilator spaces of $\CS$-spinors and of $\CSm$-spinors are disjoint families (no maximal isotropic annihilates both a nonzero even and a nonzero odd spinor).
\end{enumerate}

## technical
For a nonzero conformal spinor $u \in \CS$, the annihilator $W_u = \{v \in V_\C : c(v)u = 0\}$ is a maximal totally isotropic, three-dimensional subspace of the complexified ambient space, so every conformal spinor is a pure spinor. The joint kernel of $c(W_u)$ is the line $\C u$, so $[u] \mapsto W_u$ embeds $\PCS$ into the maximal isotropic subspaces, equivariantly for the spin action.

For any isotropic complement $U'$ dual to $W_u$, the map $\Lambda^\bullet U' \to \Lambda^\bullet W$, $\xi \mapsto c(\xi)u$, is a linear isomorphism: $u$ is the Fock vacuum of the three fermionic ladder pairs built on $(W_u, U')$, with even products generating $\CS$ and odd ones $\CSm$. Ambient vectors act as sums of three creation and annihilation operators, so conformal spinors are states of the pair algebra rather than its operators, and no maximal isotropic subspace annihilates both a nonzero even and a nonzero odd spinor.

## lay
The four-component spinors of the conformal algebra are the objects Penrose built his theory on. This result shows that, inside the completed algebra of the series, each such spinor is the empty state (the vacuum) of a system of three fermionic ladder pairs that the spinor itself singles out. Every other state of the module is reached from it by those ladder operators, so these spinors are the states the operators act on, not the operators themselves.

## one-liner
Every nonzero conformal spinor is a pure spinor, the Fock vacuum of the three fermionic ladder pairs fixed by its annihilator, so conformal spinors are states of the pair algebra and not its operators.
