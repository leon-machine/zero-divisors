---
id: synthesis.mirror-extensions-causal-convention
kind: claim
version: 1
title: The mirror's extensions under the causal convention
status: proved
region: synthesis
subject: dark-matter
tags: [towers-by-residue, mirror-sector, clifford-classification, obstruction-types]
proposed_by:
  kind: ai
  session: colony-2026-10-22
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
derivations:
- name: main
  uses:
  - odd-extensions.volume-element-odd-dimension@4
  - odd-extensions.doubling-or-complexification@6
  - odd-extensions.four-extensions-oriented-pair@6
  - dark-matter.towers-are-residues-single-clock-filter@5
  - dark-matter.nesting@3
  - rule2.where-obstruction-sits-commuting-square@6
  - rule2.which-residues-obstruct-which-way@6
  - rule2.rule-2-plane@4
  - odd-extensions.two-towers-one-curved-universe@6
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_mirror_extensions_causal_convention
- kind: proof
  derivation: main
extraction:
  open_problem: op.dark-sector-scopes
  note: >-
    Resolves the convention finding M6 of seed/CONTRADICTIONS_STRUCTURE.md by stating both readings
    where they meet. T14a Cor 2.4 reads time as the plus sign in both towers. T14 Prop 3.1 reads time
    as the minority sign of a causal signature; its sentence fixing "time = plus" labels this world,
    where plus is the minority sign, and is compatible with that reading. The Rule 2 note is internally
    mixed: its plane result (Prop rule-2-plane (ii)) uses the minority-sign reading, while the naming of
    the spacelike and timelike extensions in its commuting-square theorem and Cor 2.3 uses time = plus.
    T14's nesting, T14a's own Prop 9.3 and the unit-ball rule's space dimensions (D = 3, 2, 4) use the
    minority-sign reading. The algebra and residue of each extension are unchanged; what changes is
    which one is called time and which space for the mirror, and with it which of the mirror's
    extensions is its Kaluza-Klein direction.
---

## formal
Write the mirror of a signature $(p,q)$ as $(q,p)$, the reversal $g \mapsto -g$. Call T14's convention (Proposition \claimref{dark-matter.towers-are-residues-single-clock-filter}) the \emph{causal reading}: in a causal signature, $\min(p,q) = 1$, the time direction is the one generator of the minority sign, so this world $(1,3)$ has time $+$ and the mirror $(3,1)$ has time $-$. That Proposition's phrase "time $=$ plus" labels this world, whose minority sign is plus, and agrees with the causal reading there; the two readings differ only on the mirror. Call the convention of Corollary \claimref{odd-extensions.four-extensions-oriented-pair}, time $+$ in both towers, the \emph{uniform reading}.
\begin{enumerate}
\item[(i)] For $n = p + q$ odd, the central volume elements satisfy $\omega^{2}(q,p) = -\omega^{2}(p,q)$: reversal exchanges the doubled and the complexified types, and residue $r$ with $-r$.
\item[(ii)] In the causal reading the four extensions are: this world $+$ space $= \Cl(1,4)$, doubled, $r = 5$; this world $+$ time $= \Cl(2,3)$, complexified, $r = 7$; mirror $+$ time $= \Cl(3,2)$, doubled, $r = 1$; mirror $+$ space $= \Cl(4,1)$, complexified, $r = 3$. For each kind $X$, mirror $+ X$ is the reversal of this world $+ X$, so the pairs $(5,3)$ and $(7,1)$ are reversal pairs and the extension maps commute with $r \mapsto -r$. The convention-free statement is: in both towers a generator of square $-1$ doubles the shadow and a generator of square $+1$ complexifies it. In the causal reading this world's space and the mirror's time double, and this world's time and the mirror's space complexify.
\item[(iii)] In the uniform reading the same four algebras are labelled with mirror $+$ space $= \Cl(3,2)$ and mirror $+$ time $= \Cl(4,1)$; the pairs of like kind have residues $(5,1)$ and $(7,3)$, which are not reversal pairs, and the mirror $(3,1)$, still causal ($\min(p,q) = 1$), has three time directions and one space direction, which conflicts with Proposition \claimref{dark-matter.towers-are-residues-single-clock-filter}'s reading of the minority direction as time.
\item[(iv)] At the even residues $2$ and $6$ the obstructed one-dimensional extension is the one by a generator of square $-1$ (Theorem \claimref{rule2.where-obstruction-sits-commuting-square}(a)). At residue $6$ that generator is spacelike, so this world leaves residue $6$ into the obstruction through its Kaluza-Klein direction, as Corollary \claimref{rule2.which-residues-obstruct-which-way} states. At residue $2$, in the causal reading, it is timelike: the mirror's Kaluza-Klein direction gives $\Cl(4,1)$, complexified, simple, residue $3$, with no obstruction, and the mirror's obstructed extension is a second time direction, $\Cl(3,2)$ at residue $1$. The sentence of that corollary on the mirror residue $2$ holds for the extension by a generator of square $-1$, which is the mirror's Kaluza-Klein direction only in the uniform reading.
\item[(v)] In de Sitter the direction that the frozen point's complement adds (Proposition \claimref{odd-extensions.two-towers-one-curved-universe}(i)) has the space sign of each world in the causal reading: it is space for both towers, doubling ours to $\Cl(1,4)$ and complexifying the mirror's to $\Cl(4,1)$. The uniform reading labels the mirror's $\Cl(4,1)$ as an extension by time.
\end{enumerate}
T14's nesting (Proposition \claimref{dark-matter.nesting}(i), the mirror chain being ours with the signatures reversed) and the Rule 2 plane (Proposition \claimref{rule2.rule-2-plane}(ii), $\Cl(3,1)$ from $\Cl(2,1)$ by a third spatial direction of square $+1$) use the causal reading. The Rule 2 note is therefore internally mixed: its plane result uses the causal reading, while Theorem \claimref{rule2.where-obstruction-sits-commuting-square} names $\Cl(p,q{+}1)$ spacelike and $\Cl(p{+}1,q)$ timelike, which is the uniform reading for the mirror.

## technical
Two conventions meet in the dark sector. T14 calls a signature causal when it has exactly one direction of the minority sign and reads that direction as time, so the mirror $(3,1)$ has its single time of square $-1$ and three spatial directions of square $+1$. T14's phrase "time $=$ plus" labels this world, where plus is the minority sign, so it agrees with this reading. T14a's Corollary 2.4, and the Rule 2 note in its naming of spacelike and timelike extensions, instead call the plus sign time in both towers; the Rule 2 note's own plane result uses T14's reading, so that note is internally mixed. The four algebras $\Cl(1,4)$, $\Cl(2,3)$, $\Cl(3,2)$, $\Cl(4,1)$ and their residues $5, 7, 1, 3$ do not depend on the convention; their names do.

In T14's causal reading the mirror's extension by space is $\Cl(4,1)$, residue $3$, complexified, and its extension by time is $\Cl(3,2)$, residue $1$, doubled. Each of the mirror's extensions is then the metric reversal of ours of the same kind, so the residues pair as $5 \leftrightarrow 3$ and $7 \leftrightarrow 1$ and the extension maps commute with $r \mapsto -r$. Reversal in odd dimension flips the square of the central volume element, so the reversal of a doubled algebra is complexified: the rule that holds in both towers is that a generator of square $-1$ doubles and one of square $+1$ complexifies. T14a's sentence "in both towers the time generator complexifies and the space generator doubles" is true in its uniform reading, under which the mirror, still a signature with one minority direction, has three times; in the causal reading it holds for this world only, and for the mirror the roles are exchanged.

The consequence a reader meets is in the Rule 2 note: its corollary that the physical lineage leaves residue $6$ only through a spacelike Kaluza-Klein direction, and that "the same holds at the mirror residue 2". In the causal reading the mirror's spacelike extra direction gives the complexified $\Cl(4,1)$, which is not obstructed; the mirror's obstructed extension is a second time. The tower and its mirror therefore differ in which physical extension carries the Rule 2 obstruction, a difference the copy theorem does not see because it runs through even subalgebras. T14a's own de Sitter result already fits the causal reading: the added direction is spacelike for both towers, doubling ours and complexifying the mirror's. T14's nesting and the unit-ball rule's space dimensions (three for the mirror, two and four for the odd towers) also presuppose it; in the uniform reading the mirror and the residue $1$ and $3$ representatives would each have one spatial direction.

## lay
The series pairs our spacetime with a mirror world whose geometry has the opposite overall sign. Two papers describe the mirror's possible extra dimensions with opposite naming rules: one calls the plus sign "time" in both worlds, which would give the mirror three time directions; the other calls the single odd-one-out direction "time" in each world. The algebras are the same either way, but the names are not. This result shows that the second naming is the one under which our world and the mirror match each other step for step, and that the rest of the dark-matter work already uses it. Under it, an extra space dimension splits our algebra into two copies but makes the mirror's complex, so the obstruction that our world meets through an extra space dimension, the mirror meets through a second time instead.

## one-liner
Under T14's causal convention (the mirror's time is its minus sign) the mirror's space and time extensions are $\Cl(4,1)$ and $\Cl(3,2)$, reversal partners of ours ($5 \leftrightarrow 3$, $7 \leftrightarrow 1$), so a square $-1$ generator doubles and a square $+1$ one complexifies in both towers, and the mirror's Kaluza-Klein direction is unobstructed: the Rule 2 obstruction at residue $2$ is a second time.
