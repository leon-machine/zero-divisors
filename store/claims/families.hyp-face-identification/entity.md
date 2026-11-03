---
id: families.hyp-face-identification
kind: claim
version: 3
title: The face identification, as a working hypothesis
status: postulate
region: families
subject: generations
tags: [face-identification, conformal-spinors]
proposed_by:
  kind: human
  author: leon (stated in the paper); entered by the build
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T13, deposited version
review: typed
lineage:
  motivated_by:
  - families.three-generations-faces-maximal-composite
locators:
  paper: T13
  number: Conj 3.1 (as a working hypothesis)
  label: ''
  line: 613
extraction:
  maintainer_pass:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 2 -> 3, by Leon''s decisions of 2 November 2026: a marked note at the formal and technical levels records that the generation number is free under the slot-module premise and anomaly freedom (at most five if both non-abelian factors are to be asymptotically free) and that three is not derived, resting on the imported three-spinor bound plus a family-symmetry reading (synthesis.slot-module-makes-the-faces-separate-composites-and-leaves-the-generation-number-free, whose clause (2) complements synthesis.faces-of-one-slot-space-are-not-three-generations-under-one-gauge-group). What the hypothesis asserts is unchanged.'
  env: hypothesis
  typing:
    by: ai-typing-pass
    note: The paper states the identification only as a conjecture; this postulate records it as the working
      hypothesis that dependent results take as given (formal text quotes the conjecture's sentence verbatim),
      linked by lineage.motivated_by since the schema has no postulate-to-conjecture edge.
  source_title: 'The face identification, as a working hypothesis'
  source_formal: |-
    Working hypothesis: the three generations are the three two-twistor faces of the maximal three-twistor system. This is the identification stated as Conjecture \claimref{families.three-generations-faces-maximal-composite}, which is not proved; the results that rely on the face identification take it as given and hold only under it.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Faces and the maximal system are now named by conformal spinors (two-spinor faces, three-spinor system) in all levels; the hypothesis is unchanged.'
---

## formal
Working hypothesis: the three generations are the three two-spinor faces of the maximal three-spinor system (three conformal spinors; the paper's three-twistor system). This is the identification stated as Conjecture \claimref{families.three-generations-faces-maximal-composite}, which is not proved; the results that rely on the face identification take it as given and hold only under it.

\emph{Note (the generation number, 2 November 2026).} Under the slot-module premise the number of generations, the number of separate composites, is free: the premise and anomaly freedom hold copy by copy for any number of them, and asymptotic freedom of both non-abelian factors, if it is required, allows one to five at one or two doublets (\claimref{synthesis.slot-module-makes-the-faces-separate-composites-and-leaves-the-generation-number-free}, clauses (3), (4)); the shared three-slot space fails the premise even for one face (clause (2) there), which complements \claimref{synthesis.faces-of-one-slot-space-are-not-three-generations-under-one-gauge-group}. Three is not derived: it rests on the imported observation-level three-spinor bound (Fact \claimref{families.imported-face-valued-bracket-quantum-numbers}) together with a family-symmetry reading, the slot $\su(3)$ of the maximal composite acting on the generation labels, which neither the premise nor the separate-composite reading implies. The hypothesis is unchanged: it identifies the generations with the faces and does not fix their number beyond that bound.
## technical
Given the three-spinor bound on the maximal composite and that a massive matter unit is a two-spinor composite, the maximal system has $\binom{3}{2} = 3$ two-spinor faces. The working hypothesis identifies the three generations with these three faces.

The identification is a conjecture, not a result. This entry records it as a premise so that results relying on it show it among the conditions they hold under; it adds nothing to the conjecture's support.

(Note, 2 November 2026: under the slot-module premise the number of generations is free and the faces are separate composites; three rests on the imported three-spinor bound and a family-symmetry reading, not on a derivation, \claimref{synthesis.slot-module-makes-the-faces-separate-composites-and-leaves-the-generation-number-free}.)
## lay
This is an assumption, not a result: the three generations of matter are taken to be the three ways of choosing two building blocks out of three. The idea is a conjecture of the families paper; here it is recorded as a premise so that every result relying on it is visibly conditional on it.

## one-liner
Working hypothesis: the three generations are the three two-spinor faces of the maximal three-spinor composite.
