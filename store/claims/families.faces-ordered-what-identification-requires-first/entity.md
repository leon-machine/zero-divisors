---
id: families.faces-ordered-what-identification-requires-first
kind: claim
version: 3
title: 'The faces ordered: what the identification requires, and the first test passed'
status: proved
region: families
subject: generations
tags: [face-identification, flavour-and-mixing, confronted-with-data]
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
  - families.alignment-computed-thirteenth-refutation-democracy-one@4
  - families.imported-face-valued-bracket-quantum-numbers@5
  - families.three-identical-families-mixing-shared-slots@8
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T13.py
  tags:
  - label:prop:ordered
- kind: check
  ref: check.py::check_faces_identical_and_direction_orders_them
- kind: check
  ref: check.py::check_texture_and_cabibbo_arithmetic
locators:
  paper: T13
  number: Prop 4.4
  label: prop:ordered
  line: 673
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the faces S3-identical and ordered by a generic direction, and the texture identity with the Cabibbo arithmetic. Version 2 -> 3.'
  env: proposition
  context_refs:
  - families.bracket-fixed-join
  - families.source-term-linear-tilt-mass-functional
  - families.three-generations-faces-maximal-composite
  typing:
    by: ai-typing-pass
    note: 'The three edges are exactly the ingredients the proof names and were kept; the condensation
      and source-term citations only locate the vacuum, and the Cabibbo pass in (2) is the classical texture
      result (GST1968, Fritzsch1978), which is not in the store as an imported claim, so no standard route
      was added. Levels pass: conditions already kept.'
  source_title: 'The faces ordered: what the identification requires, and the first test passed'
  source_formal: |-
    Two results move Conjecture \claimref{families.three-generations-faces-maximal-composite}.
    \begin{enumerate}
    \item \emph{(The missing ingredient identified, at structural level.)} Proposition \claimref{families.three-identical-families-mixing-shared-slots} makes the three faces $S_{3}$-identical, while physical families differ by mass alone; identifying faces with families therefore requires $S_{3}$ to break. The framework's only $S_{3}$-charged vacuum object is the face-valued bracket: the mass bracket is face-valued, one bracket per two-twistor face, so the vacuum of Propositions \claimref{families.bracket-fixed-join} and \claimref{families.source-term-linear-tilt-mass-functional} is a direction in face space, and its alignment spontaneously breaks $S_{3}$, ordering the faces by their overlap with it. The face identification is not an additional postulate awaiting new structure: it is the condensate's alignment, and what that expectation value does and does not determine is exactly what Proposition \claimref{families.alignment-computed-thirteenth-refutation-democracy-one} states.
    \item \emph{(The first numerical test, at observation level.)} Single-slot overlap with an aligned condensate is a nearest-neighbour Yukawa texture: direct transitions between the two faces not sharing the condensate's slots are doubly suppressed. The classic consequence of such textures is the Cabibbo relation $\theta_{C} \approx \sqrt{m_{d}/m_{s}} \approx 0.22$, against the observed $0.225$: with $m_{d} = 4.70$, $m_{s} = 93.5$ MeV \cite{PDG2024} the square root is $0.224$, and the conjecture's corollary shape, confronted with its first number, passes at the percent level the quark-mass uncertainties allow. The test inherits the standard assumptions of the texture literature and is flagged at that level; its failure at precision would have refuted the corollary, and did not.
    \end{enumerate}
    The residue is the alignment's anisotropic part, which depends on the one expectation value Proposition \claimref{families.source-term-linear-tilt-mass-functional} names.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'The two-twistor face is now the two-spinor face (a face of two conformal spinors); nothing else was in twistor form.'
---

## formal
Two results move Conjecture \claimref{families.three-generations-faces-maximal-composite}.
\begin{enumerate}
\item \emph{(The missing ingredient identified, at structural level.)} Proposition \claimref{families.three-identical-families-mixing-shared-slots} makes the three faces $S_{3}$-identical, while physical families differ by mass alone; identifying faces with families therefore requires $S_{3}$ to break. The framework's only $S_{3}$-charged vacuum object is the face-valued bracket: the mass bracket is face-valued, one bracket per two-spinor face, so the vacuum of Propositions \claimref{families.bracket-fixed-join} and \claimref{families.source-term-linear-tilt-mass-functional} is a direction in face space, and its alignment spontaneously breaks $S_{3}$, ordering the faces by their overlap with it. The face identification is not an additional postulate awaiting new structure: it is the condensate's alignment, and what that expectation value does and does not determine is exactly what Proposition \claimref{families.alignment-computed-thirteenth-refutation-democracy-one} states.
\item \emph{(The first numerical test, at observation level.)} Single-slot overlap with an aligned condensate is a nearest-neighbour Yukawa texture: direct transitions between the two faces not sharing the condensate's slots are doubly suppressed. The classic consequence of such textures is the Cabibbo relation $\theta_{C} \approx \sqrt{m_{d}/m_{s}} \approx 0.22$, against the observed $0.225$: with $m_{d} = 4.70$, $m_{s} = 93.5$ MeV \cite{PDG2024} the square root is $0.224$, and the conjecture's corollary shape, confronted with its first number, passes at the percent level the quark-mass uncertainties allow. The test inherits the standard assumptions of the texture literature and is flagged at that level; its failure at precision would have refuted the corollary, and did not.
\end{enumerate}
The residue is the alignment's anisotropic part, which depends on the one expectation value Proposition \claimref{families.source-term-linear-tilt-mass-functional} names.

## technical
The three faces are $S_{3}$-identical, while physical families differ by mass, so identifying faces with families requires $S_{3}$ to break. The only $S_{3}$-charged vacuum object is the face-valued bracket: the condensate is a direction in face space, and its alignment breaks $S_{3}$ spontaneously, ordering the faces by their overlap with it. At structural level the face identification is therefore the condensate's alignment, not an additional postulate.

At observation level, single-slot overlap with an aligned condensate gives a nearest-neighbour Yukawa texture, whose classic consequence is the Cabibbo relation $\theta_{C} \approx \sqrt{m_{d}/m_{s}}$. With $m_{d} = 4.70$ MeV and $m_{s} = 93.5$ MeV this gives $0.224$ against the observed $0.225$, a pass within the quark-mass uncertainties, under the assumptions the texture literature makes. The anisotropic part of the alignment remains open.

## lay
The three candidate families in this framework start out exactly alike, but real families differ in mass, so something must tell them apart. The paper argues that the only thing available is the direction in which the vacuum settles, which then ranks the three by how much they overlap with it. As a first check, this kind of ranking leads to a well-known approximate formula linking a quark mixing angle to a ratio of quark masses, and the numbers agree to within about a percent. The check relies on standard assumptions borrowed from earlier work on such mass patterns.

## one-liner
Ordering the identical faces into families requires breaking $S_{3}$, which the condensate's alignment does at structural level, and the resulting nearest-neighbour texture passes the Cabibbo test $\theta_{C} \approx \sqrt{m_{d}/m_{s}} \approx 0.224$ at observation level.
