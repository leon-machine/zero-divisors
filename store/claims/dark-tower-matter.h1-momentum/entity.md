---
id: dark-tower-matter.h1-momentum
kind: claim
version: 2
title: 'Premise H1: a constituent''s momentum'
status: postulate
region: dark-tower-matter
subject: dark-matter
tags: [dark-tower-premises]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T14c, the series'' standard disclaimer'
- name: Claude Fable 5.2
  role: 'note pointing to the uniqueness of the constituent momentum: the formula is forced up to a real factor, H1 weakened and not retired'
  version: 2
  source: maintainer pass of 2026-11-10
review: typed
about:
- obj.dark-tower-matter.ideals-fields-momentum
locators:
  paper: T14c
  number: Premise 2.6
  label: prem:H1
  line: 220
extraction:
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version 1 -> 2. Maintainer item M4 of 10 November 2026: a note at every level points to synthesis.constituent-momentum-is-the-unique-spin-covariant-quadratic-vector-on-the-spinor-ideal (the formula is forced up to a real factor given quadraticity and covariance under the connected spin group, in the causal towers of dimension three to five) and lists what stays premised (spinor part and intertwining map, quadraticity and covariance, normalisation, additivity). No edge: the result does not have H1 in its past cone and H1 is a postulate. The premise is unchanged.'
  env: premise
  typing:
    by: ai-typing-pass
    note: 'Postulate; no edges. The statement names the Standard-Model paper as its four-dimensional instance;
      that statement (its Fact 2.1) is not in the store as a separate entity. Levels pass: levels written
      from scratch, keeping every condition and level qualifier of the formal statement.'
---

## formal
A constituent has a spinor part $\psi$ in the tower's spinor ideal $S$ (Definition \claimref{obj.dark-tower-matter.ideals-fields-momentum}), carried by a map $T \to S$ that intertwines the action of the tower's spin group, so that the field of $T$ acts on $S$ through it; its momentum is the vector part of $\psi e_{t}\rev{\psi}$. In dimension four this is T12's Fact 2.1 in the even algebra; in dimensions three and five it is a premise.

\emph{Note (what of H1 is forced).} In the causal towers of dimension three to five the quadratic vectors of one constituent's spinor part that are covariant under the connected spin group form one real line, spanned by this momentum (Theorem \claimref{synthesis.constituent-momentum-is-the-unique-spin-covariant-quadratic-vector-on-the-spinor-ideal}). So, given a spinor part and a momentum that is quadratic and covariant, the formula is forced up to a real factor. H1 is weakened by that result, not retired: what stays premised in dimensions three and five is that a constituent has a spinor part in $S$ carried by an intertwining map, that its momentum is a quadratic covariant vector of it, the normalisation, and the additivity of momenta over constituents, which covariance does not force.

## technical
H1 takes a constituent to carry a spinor part $\psi$ in the tower's spinor ideal $S$, through a map from the conformal constituent ideal $T$ to $S$ that intertwines the action of the tower's spin group, so that the field of $T$ acts on $S$ through it; its momentum is the vector part $\langle \psi e_t\rev{\psi}\rangle_1$. In dimension four this is the Standard-Model paper's statement written in the even algebra; in dimensions three and five it is a premise, not a theorem.

Note: given a spinor part and a quadratic, spin-covariant momentum, the formula is forced up to a real factor in the causal towers of dimension three to five (the constituent-momentum uniqueness result). H1 is weakened, not retired: the spinor part, quadraticity and covariance, the normalisation and additivity over constituents stay premised.

## lay
This is an assumption, not a result: a constituent's motion is read from a spinor in the tower's own algebra, linked to the constituent in the larger conformal algebra in a way that respects the tower's rotations. In our four-dimensional world this is already established; in three and five dimensions it is assumed. A later result shows that the formula itself is not a free choice: once the motion is read from such a spinor in a way that respects rotations and boosts, it is the only possibility up to an overall factor. What remains assumed is that the spinor exists, that the reading has that form, and that motions of several constituents add.

## one-liner
Premise H1: a constituent's momentum is the vector part of $\psi e_t\rev{\psi}$ for its spinor part $\psi \in S$, linked to $T$ by a spin-intertwining map; a premise in dimensions three and five, where the formula is forced up to a real factor once the momentum is quadratic and covariant.
