---
id: families.three-identical-families-mixing-shared-slots
kind: claim
version: 8
title: Three identical families, mixing by shared slots
status: proved
region: families
subject: generations
tags: [flavour-and-mixing, conformal-spinors]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T13, deposited version
review: typed
derivations:
- name: main
  uses:
  - families.imported-one-derived-generation-hypothesis-s@7
  - families.imported-face-valued-bracket-quantum-numbers@5
  - standard-model.hyp-s-slot-statistics@9
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T13.py
  tags:
  - label:prop:identical
- kind: check
  ref: check.py::check_three_faces_meet_in_one_slot
- kind: check
  ref: check.py::check_slot_permutations_carry_copies
- kind: check
  ref: check.py::check_overlap_structure_single_slot
locators:
  paper: T13
  number: Prop 3.2
  label: prop:identical
  line: 617
extraction:
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: families.imported-one-derived-generation-hypothesis-s repinned 6 -> 7 after reviewing its G3 restatement (Hypothesis (S) is now derived in the store from the slot-module premise, where it was called a structural premise; the construction is unchanged); the use here holds as cited.'
  maintainer_pass_qft_full:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 7 -> 8, by Leon''s decisions of 2 November 2026: a marked note at the formal and technical levels records the generation number as free (n_g independent of the slot-module premise and of anomaly freedom; at most five if both non-abelian factors are to be asymptotically free), three not derived but resting on the imported three-spinor bound plus a family-symmetry reading, and cites clause (2) of synthesis.slot-module-makes-the-faces-separate-composites-and-leaves-the-generation-number-free as a complement to the stored faces theorem. Statement, proof, checks and edges unchanged.'
  maintainer_pass_faces:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 6 -> 7, by Leon''s decision of 2026-11-01: a marked note at the end of the formal and technical levels restating the face identification as three composites with separate slots, since in one slot space under one gauge group at most one face is a weak doublet and the faces'' chirality halves span 28 (shared pair system) or 46 to 47 (separate pair modes) of the 48 states three generations need (synthesis.faces-of-one-slot-space-are-not-three-generations-under-one-gauge-group). Statement, proof and checks unchanged (the faces as slot subsets and their isomorphic copies stand); no edge added.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: three faces at the bound meeting pairwise in one slot (disjoint faces for 4 to 6 slots), S3 transitive with slot permutations carrying composites, brackets and the face U(2) actions from one face to another, and the overlap matrix with no zero entry. Version 4 -> 5. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 5 -> 6.'
  env: proposition
  context_refs:
  - families.imported-face-valued-bracket-quantum-numbers
  typing:
    by: ai-typing-pass
    added:
    - families.imported-face-valued-bracket-quantum-numbers
    - standard-model.hyp-s-slot-statistics
    note: 'Added the face-valued bracket Fact because the count of three faces rests on its three-twistor
      bound; the observation-level mixing clause has no premise in the store and is left as a reading.
      Hypothesis pass: assumes standard-model.hyp-s-slot-statistics added because its statement holds
      under Hypothesis (S) (the lepton copy). Levels pass: the lay and one-liner now say the lepton part
      of each copy holds under Hypothesis (S).'
  source_title: 'Three identical families, mixing by shared slots'
  source_formal: |-
    Let the face-$F$ copy of the content be the two-twistor composite on the slots $F \subset \{1,2,3\}$, with the construction of Fact \claimref{families.imported-one-derived-generation-hypothesis-s} applied to it. Then the faces, three of them given the three-twistor bound of Fact \claimref{families.imported-face-valued-bracket-quantum-numbers}, carry identical fermion content whatever their number: the symmetric group $S_{3}$ of slot permutations acts transitively on the faces and carries the face-$F$ copy isomorphically onto the face-$\sigma(F)$ copy, so the three copies of $(2,3)$, and under Hypothesis (S) of $(2,3) \oplus (2,1)$, are isomorphic. Any two faces share exactly one twistor slot. At observation level, and flagged as such: inter-family mixing is therefore mediated by single-slot overlap, the structure of a mixing matrix with no vanishing entries and suppressed double transitions, the CKM shape. What remains conjectural is only the identification of the faces with the physical families; the multiplicity three (given the imported bound), the identity of the copies, and the intersection count are as stated.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Composites, faces, slots and the three-spinor bound are now named by conformal spinors in all levels and in the proof; the combinatorics is unchanged.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - families.imported-face-valued-bracket-quantum-numbers
    stated_role:
    - standard-model.hyp-s-slot-statistics
    note: 'the assumed Hypothesis (S), not on the cite list, was also uncited; given a one-sentence role.'
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
Let the face-$F$ copy of the content be the composite of two conformal spinors (twistors) on the slots $F \subset \{1,2,3\}$, with the construction of Fact \claimref{families.imported-one-derived-generation-hypothesis-s} applied to it. Then the faces, three of them given the three-spinor bound of Fact \claimref{families.imported-face-valued-bracket-quantum-numbers}, carry identical fermion content whatever their number: the symmetric group $S_{3}$ of slot permutations acts transitively on the faces and carries the face-$F$ copy isomorphically onto the face-$\sigma(F)$ copy, so the three copies of $(2,3)$, and under Hypothesis (S) of $(2,3) \oplus (2,1)$, are isomorphic. Any two faces share exactly one spinor slot. At observation level, and flagged as such: inter-family mixing is therefore mediated by single-slot overlap, the structure of a mixing matrix with no vanishing entries and suppressed double transitions, the CKM shape. What remains conjectural is only the identification of the faces with the physical families; the multiplicity three (given the imported bound), the identity of the copies, and the intersection count are as stated.

\emph{Note (the face identification restated, 2026-11-01).} The identification is restated as three composites with separate slots: each face is its own two-spinor composite, with its own slot and pair modes, and the three are not subspaces of one slot space. Read in one state space with shared slots the faces are not three generations under one gauge group (\claimref{synthesis.faces-of-one-slot-space-are-not-three-generations-under-one-gauge-group}): any Lie algebra acting linearly on the three slots leaves at most one face plane irreducible, so at most one face is a weak doublet, and the faces' chirality halves span $28$ states with one pair system shared by the faces, or $46$ to $47$ with separate pair modes, of the $48 = 3 \times 16$ that three generations need.

\emph{Note (the generation number, 2 November 2026).} Under the slot-module premise the number of generations, the number of separate composites, is free: the premise and anomaly freedom hold copy by copy for any number of them, and asymptotic freedom of both non-abelian factors, if it is required, allows one to five at one or two doublets (\claimref{synthesis.slot-module-makes-the-faces-separate-composites-and-leaves-the-generation-number-free}, clauses (3), (4)); the shared three-slot space fails the premise even for one face (clause (2) there), which complements \claimref{synthesis.faces-of-one-slot-space-are-not-three-generations-under-one-gauge-group}. Three is not derived: it rests on the imported observation-level three-spinor bound (Fact \claimref{families.imported-face-valued-bracket-quantum-numbers}) together with a family-symmetry reading, the slot $\su(3)$ of the maximal composite acting on the generation labels, which neither the premise nor the separate-composite reading implies. The statement above, which counts the faces given that bound, is unchanged.
## technical
A face is a two-element subset $F \subset \{1,2,3\}$ of the slots of the maximal three-spinor system, and the face-$F$ copy is the construction of one derived generation applied to the two-spinor composite on those slots. Because that construction refers only to its own two slots, a slot permutation $\sigma \in S_{3}$ carries the face-$F$ copy term by term onto the face-$\sigma(F)$ copy; as $S_{3}$ acts transitively on two-element subsets, all copies are isomorphic: copies of $(2,3)$, and under Hypothesis (S) of $(2,3) \oplus (2,1)$. Given the imported three-spinor bound there are $\binom{3}{2} = 3$ faces, and two distinct faces meet in exactly one slot, $|F \cap F'| = 1$.

At observation level only, this suggests that mixing between families is mediated by the shared slot, so that every entry of a mixing matrix is populated and double transitions are suppressed, the shape of the CKM matrix. No mixing matrix is defined, and the identification of faces with physical families remains a conjecture. (Note, 2026-11-01: the identification is restated as three composites with separate slots; in one shared slot space at most one face is a weak doublet under one gauge group and the faces' chirality halves span at most $47$ of the $48$ states three generations need, \claimref{synthesis.faces-of-one-slot-space-are-not-three-generations-under-one-gauge-group}.) (Note, 2 November 2026: the number of generations is free under the slot-module premise and anomaly freedom, at most five if both non-abelian factors are to be asymptotically free; three is not derived, resting on the imported three-spinor bound and a family-symmetry reading, \claimref{synthesis.slot-module-makes-the-faces-separate-composites-and-leaves-the-generation-number-free}.)
## lay
If the largest allowed composite is made of three conformal spinors and a massive particle uses two of them, there are three ways to choose the pair. Each choice carries an exact copy of the same set of particles, because relabelling the spinors maps one copy onto another; the copies include the lepton doublet if the slots behave like the pairs (Hypothesis (S)). Any two choices share exactly one spinor, which hints at why quark families mix the way they do, though that hint and the matching of choices to real families are not proved.

## one-liner
Given the three-spinor bound, the three two-spinor faces carry isomorphic copies of the fermion content (with the lepton doublet under (S)) and pairwise share exactly one slot, which at observation level suggests a CKM-shaped mixing.
