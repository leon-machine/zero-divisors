---
id: simulations.mirror-galaxy
kind: claim
version: 1
title: The mirror in the Galaxy
status: conjectured
region: simulations
subject: dark-matter
tags:
- mirror-sector
- halos-and-clusters
- confronted-with-data
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14b, deposited version
review: typed
lineage:
  motivated_by:
  - simulations.imported-milky-ways-mass-budget
  - simulations.imported-mirror
locators:
  paper: T14b
  number: Obs 9.1
  label: obs:galaxy
  line: 587
extraction:
  typing:
    by: ai-typing-pass
    note: 'Kept conjectured (a computed model result at observation level, no proof text); added the imported
      mirror fact to motivated_by, since the proton and helium branches tested come from it. Levels pass:
      the lay and one-liner now keep the computed, observation-level qualifier, and say the helium branch
      can survive only if (not survives if) the bulge holds more than its share, the verdict also turning
      on unfixed choices.'
  env: observation
  context_refs:
  - simulations.imported-milky-ways-mass-budget
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants: []
    added_about: []
    verdict: standalone
    note: Its semi-analytic Galaxy model is set up in its own section, not under S1 to S5 or C, so no
      premise was added; lineage to its imports already present.
---

## formal
Over the $24$ set-ups:
\begin{enumerate}
\item[(i)] The proton-only branch, at the feedback a hydrogen population has ($F = 1$), puts $47$ to $56\ \Msun\,\mathrm{pc^{-2}}$ of gas and stars at the Sun and $(15$ to $18) \times 10^{9}\ \Msun$ in the bulge volume. It fails every combination of bounds and normalisations.
\item[(ii)] The helium branch without star formation settles $48$ to $117\ \Msun\,\mathrm{pc^{-2}}$. It fails.
\item[(iii)] The helium branch with stars at $F = 1$ gives $23$ to $42\ \Msun\,\mathrm{pc^{-2}}$ and $(7$ to $13) \times 10^{9}\ \Msun$. It fails. At equal feedback it settles $49$ to $85$ percent as much as our sector, because it cools more slowly.
\item[(iv)] The helium branch at the helium-star feedback, $F = 3.6$ to $7.3$ with yield $yF$, gives $5.6$ to $20\ \Msun\,\mathrm{pc^{-2}}$ of gas and stars, $1$ to $8$ of gas, and $(1.8$ to $6.2) \times 10^{9}\ \Msun$ in the bulge volume; with yield $y$, $4.2$ to $14$, $1$ to $7$ and $(1.3$ to $4.2) \times 10^{9}\ \Msun$. Whether it passes depends on choices the data and the model do not fix. The first is how much of the bulge's dark mass, $3.1 \times 10^{9}\ \Msun$ (Fact \claimref{simulations.imported-milky-ways-mass-budget}), may be mirror: $0.6 \times 10^{9}$ if it is shared in proportion to the composition, $3.1 \times 10^{9}$ if the collisionless towers contribute nothing there, up to $8.3 \times 10^{9}$ if a mirror bar can hide within the stellar mass-to-light uncertainty. Every floor computed here exceeds $0.6 \times 10^{9}$, so on the proportional reading the bulge excludes the helium branch at every $F$ and yield; it survives in the bulge only on the other two, which require over twice the proportional share ($1.33/0.6 = 2.2$ times with yield $y$, $1.78/0.6 = 3.0$ with $yF$): held as dark mass, over $43$ percent of the bulge's dark mass with yield $y$ and $57$ percent with $yF$; otherwise hidden within the stellar mass-to-light uncertainty. The others are the normalisation of the mirror's gas, the bounds at the Sun, the yield and the IMF.

With yield $yF$, the numbers of converged set-ups that pass the lenient bounds at the Sun (thin gas below $5.59$, gas and stars below $15\ \Msun\,\mathrm{pc^{-2}}$) and each reading of the bulge room are as follows, given as ranges over the two black-hole cuts and the two disk scales (\file{verdict\_output.txt} has every count):
\begin{center}\small
\begin{tabular}{llccc}
\toprule
IMF shape & normalisation & room $8.3$ & room $3.1$ & room $0.6$ \\
\midrule
ours & total & $8$ to $9$ of $11$ or $12$ & $0$ to $4$ & $0$ \\
ours & component & $0$ to $2$ & $0$ to $1$ & $0$ \\
best shift & total & all ($9$ or $10$) & $5$ to $8$ & $0$ \\
best shift & component & $2$ to $8$ & $0$ to $7$ & $0$ \\
\bottomrule
\end{tabular}
\end{center}
\item[(v)] With yield $yF$ even the most favourable case leaves at least $5.6\ \Msun\,\mathrm{pc^{-2}}$ at the Sun and $1.78 \times 10^{9}\ \Msun$ in the bulge volume; with yield $y$, at least $4.2$ and $1.33 \times 10^{9}\ \Msun$.
\end{enumerate}
Computed; observation level.

## technical
A model of the Galaxy with a mirror sector, over $24$ set-ups, compares the mirror gas and stars settled at the Sun and in the bulge with the observed mass budget. The proton-only branch, the helium branch without star formation, and the helium branch with stars at hydrogen-like feedback ($F = 1$) all fail; at equal feedback the helium branch settles $49$ to $85$ percent as much as our sector, because it cools more slowly.

At helium-star feedback, $F = 3.6$ to $7.3$, the helium branch leaves $5.6$ to $20\ \Msun\,\mathrm{pc^{-2}}$ of gas and stars at the Sun with yield $yF$ ($4.2$ to $14$ with yield $y$) and $(1.3$ to $6.2) \times 10^{9}\ \Msun$ in the bulge volume. Whether it passes depends on choices the data and the model do not fix, first how much of the bulge's dark mass may be mirror: on the proportional share, $0.6 \times 10^{9}\ \Msun$, it is excluded at every $F$ and yield, and it survives only if the mirror holds over twice that share. Computed; observation level.

## lay
A model of our Galaxy including the mirror sector asks how much mirror gas would cool and settle into the disk and the central bulge. In most versions far too much settles, contradicting measurements of the Galaxy's mass. Only a helium mirror with strong stellar feedback comes close, and it can survive only if the bulge can hide more mirror matter than a proportional share allows; even then the verdict turns on choices the data and the model do not fix. These are computed model results, at observation level.

## one-liner
In a Galaxy model the proton and low-feedback helium mirror branches put too much matter in the disk and bulge, and the high-feedback helium branch can survive only if the bulge holds over twice its proportional share of mirror matter (computed, observation level).
