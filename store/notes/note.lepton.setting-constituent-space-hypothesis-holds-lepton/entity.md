---
id: note.lepton.setting-constituent-space-hypothesis-holds-lepton
kind: note
version: 1
title: 'The constituent space: the hypothesis that holds a lepton, and where it leaves the ledger'
status: setting
subject: standard-model
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T12-lepton, the series'' standard disclaimer'
comments_on:
- lepton.hyp-c-constituent
- lepton.imported-tensor-ledger-contains-no-lepton
- lepton.imported-twistor-state-pair-system-excitations
- lepton.relative-handedness-slotted-free-sectors
locators:
  paper: T12-lepton
  number: Setting
  section: 'The constituent space: the hypothesis that holds a lepton, and where it leaves the ledger'
  line: 204
---

## formal
The tensor ledger of Fact \claimref{lepton.imported-tensor-ledger-contains-no-lepton} treats the six cells as independent fermionic modes: a state is an occupation pattern of cells, and a mixing of slots acts on each occupied cell separately. It is worth saying what this ledger is in the language of Fact \claimref{lepton.imported-twistor-state-pair-system-excitations}: $\Lambda^{\bullet}(\C^{2} \otimes W) = \Lambda^{\bullet}(W_{1} \oplus W_{2}) \cong \Sp_{1} \otimes \Sp_{2}$, the tensor product of the Dirac modules of the two twistors, each twistor excited by its own pair operators. Read on two twistors, Fact \claimref{lepton.imported-twistor-state-pair-system-excitations} produces the ledger, not something else. A lepton doublet, $(2,1)$ of weight $-3$, needs a space in which the slot vector appears once and the pair state carries the full system; the ledger has no such space (Fact \claimref{lepton.imported-tensor-ledger-contains-no-lepton}), and the natural candidate, $\C^{2} \otimes \Sp$ with the slot mixing acting on the slot alone, is not produced by the two theorems one would like to produce it. Fact \ref{fact:ladder} is proved for bare twistors, from their spinor parts, and says nothing about how a mixing acts on an excited twistor; Fact \claimref{lepton.imported-twistor-state-pair-system-excitations} concerns one twistor and carries no slot index. The step between them is a premise, and the note states it as one.

\begin{quote}
\emph{Hypothesis (C), the constituent hypothesis.} A constituent of the composite is a Dirac state in a slot, a twistor or its partner with any of its pairs excited: its state space is
\[
\Con := \C^{2} \otimes \Sp = \C^{2} \otimes \Lambda^{\bullet}W,
\]
sixteen-dimensional, with a pair $(A, B) \in U(2) \times U(3)$ acting as $A \otimes \Lambda^{\bullet}(B)$: $A$ acts on the slot vector once, and on nothing else; $B$ acts on the Dirac state. The chirality of a constituent is that of the Dirac spinor it holds (Fact \claimref{lepton.imported-twistor-state-pair-system-excitations}) up to one overall sign $\epsilon = \pm 1$ for the slotted sector relative to the free sector: $\epsilon = +1$ means a slot leaves the half alone, $\epsilon = -1$ that it reverses it. (C) leaves $\epsilon$ open; Proposition \claimref{lepton.relative-handedness-slotted-free-sectors} fixes $\epsilon = -1$. Write $\Con_{k} := \C^{2} \otimes \Lambda^{k}W$.
\end{quote}

Hypothesis (C) with $\epsilon = -1$ is the one-constituent row $j = 1$ of T12's Hypothesis (S), the five-mode Fock space $\Lambda^{\bullet}(\C^{2} \oplus W)$: there the $(1, k)$ component is $\C^{2} \otimes \Lambda^{k}W$ with exactly this action, and (S)'s chirality, the parity of $j + k$, is on that row the parity of $1 + k$, the reversed half, which is $\epsilon = -1$. With $\epsilon = +1$ the two would contradict each other on the chirality clause, which is why the bit is left open in (C) and fixed by an argument rather than stipulated. So fixed, (C) is weaker than (S) in the plain sense that (S) implies it: (C) says nothing about states with two slot modes, nothing about the statistics of pairs of constituents, and nothing about a composite state space at all. The note claims no minimality for (C) over any class of hypotheses; what it shows is that (C) is enough for the lepton (Proposition \claimref{lepton.content-constituent-space}) and exactly where any space holding one must depart from the ledger (Proposition \claimref{lepton.unit-action-cell-action}).

The automorphism group of Fact \claimref{lepton.imported-automorphism-group-section-hypercharge-generator} acts on $\Con$ through its canonical section: an automorphism is a $K$-coset of pairs, the coset's representative with $\det A \cdot \det B = 1$ is unique, and that representative acts as $A \otimes \Lambda^{\bullet}(B)$. Section \ref{sec:group} shows that among the actions of the automorphism group on $\Con$ this is the only one compatible with conjugation.

## technical
pending

## lay
pending

## one-liner
pending
