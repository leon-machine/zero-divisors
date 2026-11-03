---
id: lepton.hyp-c-constituent
kind: claim
version: 2
title: 'Hypothesis (C): the constituent hypothesis'
status: postulate
region: lepton
subject: standard-model
tags: [hypotheses-s-r-c]
proposed_by:
  kind: human
  author: leon (stated in the paper); entered by the build
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T12-lepton, the series'' standard disclaimer'
review: typed
locators:
  paper: T12-lepton
  number: Hypothesis (C)
  label: ''
  line: 209
extraction:
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Converted ''a twistor or its partner'' to ''a conformal spinor or its partner'' (twistor or dual twistor named once) at every level. The constituent space, its complex structure and the U(2) x U(3) action are the Fock structure and are kept.'
  source_title: |-
    Hypothesis (C): the constituent hypothesis
  source_formal: |-
    \emph{Hypothesis (C), the constituent hypothesis.} A constituent of the composite is a Dirac state in a slot, a twistor or its partner with any of its pairs excited: its state space is
    \[
    \Con := \C^{2} \otimes \Sp = \C^{2} \otimes \Lambda^{\bullet}W,
    \]
    sixteen-dimensional, with a pair $(A, B) \in U(2) \times U(3)$ acting as $A \otimes \Lambda^{\bullet}(B)$: $A$ acts on the slot vector once, and on nothing else; $B$ acts on the Dirac state. The chirality of a constituent is that of the Dirac spinor it holds (Fact \claimref{lepton.imported-twistor-state-pair-system-excitations}) up to one overall sign $\epsilon = \pm 1$ for the slotted sector relative to the free sector: $\epsilon = +1$ means a slot leaves the half alone, $\epsilon = -1$ that it reverses it. (C) leaves $\epsilon$ open; Proposition \claimref{lepton.relative-handedness-slotted-free-sectors} fixes $\epsilon = -1$. Write $\Con_{k} := \C^{2} \otimes \Lambda^{k}W$.
  env: hypothesis
  typing:
    by: ai-typing-pass
    note: Stated in a quote block as the note's premise; formal text is the quote verbatim with its references
      written as claimrefs (the proposition fixing the sign assumes (C) itself, and is only named here,
      not used).
---

## formal
\emph{Hypothesis (C), the constituent hypothesis.} A constituent of the composite is a Dirac state in a slot, a conformal spinor or its partner (a twistor or its dual) with any of its pairs excited: its state space is
\[
\Con := \C^{2} \otimes \Sp = \C^{2} \otimes \Lambda^{\bullet}W,
\]
sixteen-dimensional, with a pair $(A, B) \in U(2) \times U(3)$ acting as $A \otimes \Lambda^{\bullet}(B)$: $A$ acts on the slot vector once, and on nothing else; $B$ acts on the Dirac state. The chirality of a constituent is that of the Dirac spinor it holds (Fact \claimref{lepton.imported-twistor-state-pair-system-excitations}) up to one overall sign $\epsilon = \pm 1$ for the slotted sector relative to the free sector: $\epsilon = +1$ means a slot leaves the half alone, $\epsilon = -1$ that it reverses it. (C) leaves $\epsilon$ open; Proposition \claimref{lepton.relative-handedness-slotted-free-sectors} fixes $\epsilon = -1$. Write $\Con_{k} := \C^{2} \otimes \Lambda^{k}W$.

## technical
Hypothesis (C) takes a constituent of the composite to be a Dirac state in a slot: a conformal spinor or its partner with any of its pairs excited. Its state space is $\Con = \C^{2} \otimes \Sp = \C^{2} \otimes \Lambda^{\bullet}W$, sixteen-dimensional, with $(A, B) \in U(2) \times U(3)$ acting as $A \otimes \Lambda^{\bullet}(B)$, so the slot mixing acts on the slot vector once and on nothing else.

The chirality of a constituent is that of the Dirac spinor it holds, up to one overall sign $\epsilon = \pm 1$ for the slotted sector relative to the free sector. The hypothesis leaves $\epsilon$ open; a separate argument fixes $\epsilon = -1$. The graded pieces are $\Con_{k} = \C^{2} \otimes \Lambda^{k}W$.

## lay
This is an assumption, not a result: each building block of a composite particle is one basic spinor state, with any of its internal pairs excited, sitting in one of two slots, and mixing the slots acts on that block as a whole rather than on each of its parts separately. It leaves open one sign, the relative handedness of slotted and free states, which is settled by a later argument. The companion note's results on the lepton hold under it.

## one-liner
Premise (C): a constituent is a Dirac state in a slot, with state space $\Con = \C^{2} \otimes \Lambda^{\bullet}W$ and the slot mixing acting once on the slot vector.
