---
id: synthesis.faces-of-one-slot-space-are-not-three-generations-under-one-gauge-group
kind: claim
version: 2
title: 'The faces of one slot space are not three generations'
status: proved
region: synthesis
subject: generations
tags: [face-identification, no-go, flavour-and-mixing, car-algebra]
proposed_by:
  kind: ai
  session: 2026-11-01-qft
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 2
  source: maintainer pass 2026-11-07 (GA units)
review: draft
derivations:
- name: main
  uses:
  - families.three-identical-families-mixing-shared-slots@8
  - standard-model.hyp-s-slot-statistics@9
  - synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_joint_stabiliser_keeps_the_common_line
- kind: check
  ref: check.py::check_weak_weights_of_the_other_faces
- kind: check
  ref: check.py::check_face_halves_span_twenty_eight
- kind: check
  ref: check.py::check_separate_pair_modes_span_forty_six
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - families.three-generations-faces-maximal-composite
  - families.hyp-face-identification
  - families.three-identical-families-mixing-shared-slots
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The unit in the slot-mixing generators T_j = (i/2) sigma_j and Y = (i/2) 1 became I_4, slot coefficients and matrix entries read in span{1, I_4}, and the mode spaces C^3, C^2 are written span{1, I_4}^3, span{1, I_4}^2; no bare i remains. By Leon''s ruling R3 the slot-space reading is stated once in R3''s words: numbers and the module''s complex structure in span{1, I_4}, the module read on the tower''s floors (notational).'
  open_problem: op.qft-structural-inputs
  note: >-
    The problem's three-generations input read as a field-theory statement: three generations are three
    copies of the content under one gauge group, 48 independent one-particle states of one Fock space. The
    stored face construction gives copies isomorphic under the slot permutations, which do not commute with
    the weak group. Tested in the single-state-space reading, in which the faces share slot modes (the
    reading on which the stored mixing-by-shared-slot picture rests). Two obstructions, both exact: no Lie
    algebra acting on the slots makes two face planes irreducible (two distinct planes in three dimensions
    meet in a line, which would be invariant), and the faces' chirality halves overlap, all three sharing
    the four slot-free states. The face identification therefore needs the faces read as three composites
    with their own slots, where the shared slot is a correspondence of labels. Transport-absent. Not a
    refutation of the conjecture in that second reading. Kill conditions registered before computing (two
    face planes irreducible for one algebra; the halves spanning 48) did not fire. The count 28 assumes one
    pair system shared by the faces; with separate pair modes per face it is 46, still short of 48.
---

## formal
Let $S = \mathrm{span}\{1, I_4\}^{3}$ be the slot space (numbers and the module's complex structure are read in $\mathrm{span}\{1, I_4\}$, the module read on the tower's floors, where $I_4$ commutes with the tower vectors) of the three-spinor composite with basis the three slots, $S_{F}$ for each two-element $F \subset \{1,2,3\}$ the plane of the face $F$, $W$ the pair modes, and read the face copies of Theorem \claimref{families.three-identical-families-mixing-shared-slots} in one state space: the face-$F$ copy is the subspace $V_{F} = \Lambda^{\bullet}(S_{F} \oplus W)$ of $V = \Lambda^{\bullet}(S \oplus W)$, generated from the common vacuum by the slot modes of $F$ (under Hypothesis (S), Theorem \claimref{standard-model.hyp-s-slot-statistics}, for each face).
\begin{enumerate}
\item For every Lie algebra $\mathfrak{g}$ acting linearly on $S$, at most one face plane is an irreducible $\mathfrak{g}$-invariant subspace. In particular, if the weak $\su(2)$ acts on the slots, as the slot mixing $U(2)$ of a face does (Theorem \claimref{synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus}, generators $T_{j}$ and $Y$), at most one face's slots form a weak doublet; for the weak group of face $\{1,2\}$ the even halves of the faces $\{1,3\}$ and $\{2,3\}$ have $T_{3}$ multisets $\{0: 8, \tfrac12: 8\}$ and $\{-\tfrac12: 8, 0: 8\}$ and are not invariant.
\item With one pair system $W = \mathrm{span}\{1, I_4\}^{3}$ shared by the three faces and chirality the parity of the mode number (Hypothesis (S)), the three faces' even halves, sixteen states each, span $28$ of the $32$ even states of $V$: the four slot-free states lie in all three faces, the twelve one-slot states in two faces each, the twelve two-slot states in one face each. With the half chosen face by face the span is at most $40$; the face modules span $56$ of $64$. If instead each face has its own pair modes $W_{F} \cong \mathrm{span}\{1, I_4\}^{3}$ (the slots still shared), the faces' even halves have only the vacuum in common and span $46$, at most $47$ with halves chosen face by face.
\item Hence, whenever the faces share slot modes, they cannot be three generations, which need one gauge group acting alike on $3 \times 16 = 48$ independent states (by (1) for the gauge group, and by (2) for the count with either pair system); the face identification needs the faces read as three composites, each with its own slots and pair modes.
\end{enumerate}

## technical
Read the three faces of the three-spinor composite inside one state space $V = \Lambda^{\bullet}(S \oplus W)$, $S = \mathrm{span}\{1, I_4\}^{3}$ the slots, the face-$F$ copy being $V_{F} = \Lambda^{\bullet}(S_{F} \oplus W)$ under Hypothesis (S). The robust statement is the gauge-group one: any Lie algebra acting linearly on $S$ leaves at most one face plane irreducible, since two distinct face planes meet in a slot line that would be invariant in both; so at most one face is a weak doublet, and under the weak group of face $\{1,2\}$ the other faces' halves are not invariant. It holds whatever the pair modes.

The faces' chirality halves also overlap. With chirality the mode-number parity and one pair system shared by the faces they span $28$ of the $32$ even states (the four slot-free states common to all three faces, the one-slot states shared pairwise, only the two-slot states face-specific), at most $40$ with halves chosen face by face; with separate pair modes per face they span $46$, at most $47$; in every case fewer than the $48$ of three generations. With shared slots the faces are not three generations under one gauge group; the identification needs three composites with separate slots.

## lay
One proposal in the series says the three families of matter particles are the three ways of choosing two of the three building blocks of a largest composite. In a quantum field theory, three families means three separate copies of the particle content, all feeling the same forces in the same way. If the three choices live in one shared set of states, this fails twice: the weak force can treat only one of the three pairs as a doublet, because any two pairs share a block, and the shared blocks make the copies overlap, giving at most 28 distinct states (46 if each pair keeps its own colour modes) where three families need 48. The idea survives only if the three pairs are three separate composites.

## one-liner
If the three faces of the three-spinor composite share one state space, they are not three generations: at most one face plane is irreducible for any algebra acting on the slots, so at most one face is a weak doublet, and the faces' chirality halves span 28 states with one shared pair system, 46 with separate pair modes, never 48.
