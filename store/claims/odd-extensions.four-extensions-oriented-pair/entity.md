---
id: odd-extensions.four-extensions-oriented-pair
kind: claim
version: 6
title: The four extensions of the oriented pair
status: proved
region: odd-extensions
subject: tower
tags: [towers-by-residue, mirror-sector, clifford-classification]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14a, deposited version
- name: Claude Opus 5.5
  role: 'consistency pass, the complex unit of the complexified rows named'
  version: 6
  source: maintainer pass 2026-11-07 (consistency)
review: typed
about:
- obj.odd-extensions.single-extension
derivations:
- name: main
  uses:
  - odd-extensions.doubling-or-complexification@5
  - odd-extensions.imported-representatives-dimension-nearest-four-types@4
  - odd-extensions.volume-element-odd-dimension@3
  - std-algebra.sta-matrix@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_omega_squares_and_residues
- kind: check
  ref: check.py::check_structures
- kind: check
  ref: check.py::check_even_parts_are_the_stated_shadows
- kind: check
  ref: check.py::check_convention_free_rule
- kind: proof
  derivation: main
locators:
  paper: T14a
  number: Cor 2.4
  label: cor:four
  line: 454
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 5 -> 6. The table writes Cl(1,3) (x) C and Cl(3,1) (x) C without the unit; the formal level now says it is the extension''s central volume element omega (omega^2 = -1, commuting with every vector; +-I_5 for Cl(2,3)), not the shadow''s pseudoscalar; mathematics unchanged.'
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.sta-matrix where the proof uses them. Version 4 -> 5.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: omega^2, structure, even subalgebra type and residue of each of the four extensions, with Wedderburn types from division corners, and the convention-free rule. Version 3 -> 4.'
  maintainer_pass_2026_10_22:
    by: ai-maintainer-pass
    note: 'A10 follow-up: points the table at synthesis.mirror-extensions-causal-convention, stating that its labels are the uniform convention and how the mirror rows read under T14 causal convention; mathematics unchanged.'
  source_formal: "The single extensions of this world and its mirror are, with their residues,\n\\[\n\\begin{array}{lllll}\n\\toprule\n\\text{extension} & \\text{algebra} & \\omega^{2} & \\text{structure} & r \\\\\n\\midrule\n\\text{this world} + \\text{space} & \\Cl(1,4) & +1 & \\Cl(1,3) \\oplus \\Cl(1,3) & 5 \\\\\n\\text{this world} + \\text{time}  & \\Cl(2,3) & -1 & \\Cl(1,3) \\otimes \\C \\cong \\Mat(4,\\C), \\ \\Cl^{0} \\cong \\Cl(3,1) & 7 \\\\\n\\text{mirror} + \\text{space}     & \\Cl(3,2) & +1 & \\Cl(3,1) \\oplus \\Cl(3,1) & 1 \\\\\n\\text{mirror} + \\text{time}      & \\Cl(4,1) & -1 & \\Cl(3,1) \\otimes \\C \\cong \\Mat(4,\\C), \\ \\Cl^{0} \\cong \\Cl(1,3) & 3 \\\\\n\\bottomrule\n\\end{array}\n\\]\nIn both towers the generator of the time sign complexifies and the generator of the space sign doubles."
  env: corollary
  typing:
    by: ai-typing-pass
    note: 'All three uses are invoked in the proof and kept; no standard-route sentence in the source.
      Levels pass: conditions already kept.'
---

## formal
The single extensions of this world and its mirror are, with their residues,
\[
\begin{array}{lllll}
\toprule
\text{extension} & \text{algebra} & \omega^{2} & \text{structure} & r \\
\midrule
\text{this world} + \text{space} & \Cl(1,4) & +1 & \Cl(1,3) \oplus \Cl(1,3) & 5 \\
\text{this world} + \text{time}  & \Cl(2,3) & -1 & \Cl(1,3) \otimes \C \cong \Mat(4,\C), \ \Cl^{0} \cong \Cl(3,1) & 7 \\
\text{mirror} + \text{space}     & \Cl(3,2) & +1 & \Cl(3,1) \oplus \Cl(3,1) & 1 \\
\text{mirror} + \text{time}      & \Cl(4,1) & -1 & \Cl(3,1) \otimes \C \cong \Mat(4,\C), \ \Cl^{0} \cong \Cl(1,3) & 3 \\
\bottomrule
\end{array}
\]
In both towers the generator of the time sign complexifies and the generator of the space sign doubles. In the complexified rows the complex unit is the extension's central volume element $\omega$ ($\omega^{2} = -1$, commuting with every vector; $\omega = \pm I_{5}$ for $\Cl(2,3)$, Theorem \claimref{std-algebra.complexification-is-the-odd-extension}), not the shadow's pseudoscalar $e_{1}e_{2}e_{3}e_{4}$. The labels follow the uniform convention (time a generator of square $+1$, space one of square $-1$, in both towers); in T14's causal convention the mirror's time is its minus sign, so its space and time extensions are $\Cl(4,1)$ and $\Cl(3,2)$, each the reversal of ours of the same kind, and the convention-free rule is that a generator of square $-1$ doubles and one of square $+1$ complexifies (Proposition \claimref{synthesis.mirror-extensions-causal-convention}).

## technical
The single extensions of this world's $\Cl(1,3)$ and the mirror's $\Cl(3,1)$ are: this world plus space, $\Cl(1,4)$ with $\omega^{2} = +1$, doubled to $\Cl(1,3) \oplus \Cl(1,3)$, residue $5$; this world plus time, $\Cl(2,3)$ with $\omega^{2} = -1$, equal to $\Cl(1,3) \otimes \C \cong \Mat(4,\C)$ with even part $\Cl(3,1)$, residue $7$; mirror plus space, $\Cl(3,2)$ with $\omega^{2} = +1$, doubled to $\Cl(3,1) \oplus \Cl(3,1)$, residue $1$; mirror plus time, $\Cl(4,1)$ with $\omega^{2} = -1$, equal to $\Cl(3,1) \otimes \C \cong \Mat(4,\C)$ with even part $\Cl(1,3)$, residue $3$.

In both towers the time generator complexifies the shadow and the space generator doubles it. These labels are the uniform convention; in T14's causal convention, where the mirror's time is its minus sign, the mirror's two rows exchange labels and become the reversals of ours.

## lay
Our spacetime algebra and its mirror image can each be extended by one extra direction, of time type or of space type, giving four algebras. Adding a space direction produces two identical copies of the original algebra side by side, while adding a time direction produces the original algebra with complex numbers allowed. Each of the four lands on a different odd value of the series' mod-eight charge.

## one-liner
The four single extensions of $\Cl(1,3)$ and $\Cl(3,1)$ are $\Cl(1,4)$, $\Cl(2,3)$, $\Cl(3,2)$, $\Cl(4,1)$ with residues $5, 7, 1, 3$, the space generator doubling the shadow and the time generator complexifying it in both towers.
