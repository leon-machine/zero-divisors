---
id: transport.pinching-kernel
kind: claim
version: 3
title: The pinching, and its kernel
status: proved
region: transport
subject: descent
tags: [descent-map]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T01, deposited version
review: typed
derivations:
- name: main
  uses:
  - transport.rule-1-morita-trivial@6
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T01.py
  tags:
  - num:7.5
- kind: check
  ref: check.py::check_conditional_expectation_onto_commutant
- kind: check
  ref: check.py::check_kernel_is_ladder_sector
- kind: check
  ref: check.py::check_round_trip_and_defect
locators:
  paper: T01
  number: Prop 7.5
  label: prop:pinching
  line: 1513
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: for every base Cl(p,q) with p + q <= 3: the pinching is a conditional expectation onto the computed commutant A + A ff*, its kernel is PB(1-P) + (1-P)BP = Af* + Af, the round trip and its Peirce reading, and the interposition formula. Version 1 -> 2. Check strengthened: round trip equals a f f* exactly on even blades and differs on odd ones (iff form); sample shifts moved to module level. Version 2 -> 3.'
  typing:
    by: ai-typing-pass
    note: 'Kept the Rule-1 Morita theorem, whose matrix picture and Peirce coordinates the statement and
      proof are built on; no other edges. Levels pass: the lay now says the round trip is the identity
      under the natural corner identification and the grade involution under the Peirce one.'
  env: proposition
---

## formal
Define the pinching $E : B \to B$, $E(x) = PxP + (1-P)x(1-P)$. Then:
\begin{enumerate}
\item $E$ is an idempotent linear map whose image is the commutant $C = \{x \in B : xP = Px\} = A \oplus A\,ff^*$, on which it restricts to the identity, and $E$ is a $C$-bimodule map: $E(cxc') = c\,E(x)\,c'$ for $c, c' \in C$, with $E(1) = 1$: a conditional expectation onto $C$.
\item Its kernel is exactly the adjoined ladder sector:
\[
\ker E \;=\; PB(1-P) \,\oplus\, (1-P)BP \;=\; A f^* \,\oplus\, A f .
\]
In particular $E(f) = E(f^*) = 0$: the pinching erases precisely the pair the ascent adjoined, and nothing else.
\item The round trip is exact on transported elements: for $a \in A$, $E(a) = a$, and the corner read-out $D(x) = PxP$, identified with an $A$-valued map through the natural corner isomorphism $E_{22}BE_{22} = A\,f^*f \cong A$ ($a \mapsto a\,f^*f$), satisfies $D(a) = a$: ascent-then-descent is the \emph{identity} on the base. (In the Peirce coordinates of Theorem \claimref{transport.rule-1-morita-trivial}, which identify the $(2,2)$ block with the $(1,1)$ corner by conjugating with $E_{12} = f$, the same round trip reads as the grade involution $\hat{a}$; the two corner identifications differ by exactly the grade twist of the embedding $a \mapsto \mathrm{diag}(a,\hat a)$, and either way the map is an automorphism, faithful.) The multiplicative defect of $D$ on general elements is the exact interposition formula
\[
D(xy) - D(x)D(y) \;=\; P\,x\,(1-P)\,y\,P .
\]
\end{enumerate}

## technical
In the Rule-1 completion $B \cong \Mat_2(A)$ with descent projector $P = f^*f$, the pinching $E(x) = PxP + (1-P)x(1-P)$ is an idempotent, unital, $C$-bimodule map onto the commutant $C = \{x \in B : xP = Px\} = A \oplus A\,ff^*$: a conditional expectation onto $C$. Its kernel is exactly the adjoined ladder sector $PB(1-P) \oplus (1-P)BP = Af^* \oplus Af$, so in particular $E(f) = E(f^*) = 0$.

On transported elements the round trip is exact: $E(a) = a$, and the corner read-out $D(x) = PxP$ satisfies $D(a) = a$ under the natural corner isomorphism; in Peirce coordinates the same map reads as the grade involution, still an automorphism. On general elements $D$ fails to be multiplicative by exactly $D(xy) - D(x)D(y) = Px(1-P)yP$.

## lay
After moving up to the completed algebra there is a canonical way to come back down: keep the blocks that commute with a chosen projector and discard the rest. What is discarded is exactly the new ladder pair that the completion added, and every element of the original algebra comes back unchanged under the natural identification of the corner (under the other standard identification it comes back as its grade involution, still faithfully). Coming back down does not respect multiplication in general, and the result gives the exact correction term.

## one-liner
The pinching by the descent projector is a conditional expectation onto its commutant whose kernel is exactly the adjoined ladder sector, and it returns transported elements unchanged.
