---
id: synthesis.koide-middle-mass-bound-closes-the-remaining-quark-dressing-class
kind: claim
version: 1
title: 'Koide middle-mass bound and the remaining quark dressing class'
status: proved
region: synthesis
subject: generations
tags: [flavour-and-mixing, no-go, confronted-with-data]
proposed_by:
  kind: ai
  session: 2026-11-09-solvable
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: run 2026-11-09-solvable
review: draft
derivations:
- name: main
  uses:
  - families.linear-conjecture-refuted-data@3
  - synthesis.mass-ordered-dressing-cannot-spoil-koide@2
  proof: proof-main.tex
quantities:
- quantity.up-quark-mass@1
- quantity.charm-quark-mass@1
- quantity.top-quark-mass@1
- quantity.down-quark-mass@1
- quantity.strange-quark-mass@1
- quantity.bottom-quark-mass@1
- quantity.up-quark-mass-mz@1
- quantity.charm-quark-mass-mz@1
- quantity.top-quark-mass-mz@1
- quantity.down-quark-mass-mz@1
- quantity.strange-quark-mass-mz@1
- quantity.bottom-quark-mass-mz@1
checked_by:
- kind: check
  ref: check.py::check_middle_mass_lemma
- kind: check
  ref: check.py::check_up_sector_charm_to_top_ratio_is_below_the_bound
- kind: check
  ref: check.py::check_remaining_class_thresholds
- kind: check
  ref: check.py::check_stored_corner_bound_covers_the_class
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.mass-ordered-dressing-cannot-spoil-koide
extraction:
  maintainer_pass:
    by: maintainer-2026-11-09
    date: '2026-11-09'
    note: 'Note only: the stored theorem synthesis.mass-ordered-dressing-cannot-spoil-koide had the last sentence of its (iv) corrected in its version 2, so the note now records that correction instead of calling the sentence a misstatement; statement unchanged.'
  open_problem: op.gram-square-and-face-space
  note: >-
    Attack on item 1 of op.gram-square-and-face-space, "decide whether the quark brackets satisfy the Koide
    relation at all ... test the remaining class (D2 > D3 > D1)". The stored theorem
    synthesis.mass-ordered-dressing-cannot-spoil-koide shows that dressings favouring the lighter quarks cannot turn
    Koide brackets into the measured masses and that a Koide bracket needs max_j D3/Dj at least R* (its (iv)), and
    in its version 1 stated that neither (ii) nor (iv) treats the class D2 > D3 > D1; the proof of (iv) holds for
    every rho_j = D3/Dj in (0, R], so with R = D3/D1 it covers the class, and that sentence was corrected in its
    version 2. This result sharpens the
    class bounds, adds a parameter-free necessary condition for Koide (the middle entry is at least 17/2 - 6 sqrt 2
    of the largest), and applies it to the up quarks, where m_c/m_t is below that bound at both stored mass sets,
    so the class D2 > D3 > D1 forces the up bracket above the charm bracket. All quark masses are stored quantities
    (PDG 2024 for the own-scale values; the running masses at M_Z as stored). What is decided: no ordering of the
    dressing factors escapes the need for a dressing that favours the heaviest quark, by at least R* over both
    lighter ones or, in the remaining class, by at least R_1 (7.88 to 4799.8) over the lightest. What is not
    decided: whether such a dressing exists; no stored premise gives a quark dressing law (the selectivity
    observation is conjectured, with an empty past cone), and every Koide class contains brackets, so data and
    store together cannot decide the question; the decision needs a dressing law. Prior art, cited from memory and
    not used: Y. Koide, Lett. Nuovo Cim. 34 (1982) 201 (the relation); the observation that the quark triples miss
    the relation is standard (for example W. Rodejohann and H. Zhang, Phys. Lett. B 698 (2011) 152). The
    middle-mass bound is elementary: it is the degenerate point theta = 0 of the standard trigonometric
    parametrisation of Koide triples, sqrt(m_k) proportional to 1 + sqrt(2) cos(theta + 2 pi k/3) (R. Foot,
    hep-ph/9402242 (1994), cited from memory), where (1 - 1/sqrt 2)/(1 + sqrt 2) = 3/sqrt 2 - 2; it was not found
    in the store. Transport-absent (an inequality on the Koide
    quotient and stored data).
---

## formal
Let $Q(m) = \sum_{k}m_{k}/(\sum_{k}\sqrt{m_{k}})^{2}$ for positive triples, the quotient of Proposition \claimref{families.linear-conjecture-refuted-data}, and let $t_{*} = 3/\sqrt{2} - 2$, the positive root of $2t^{2} + 8t - 1$, so that $t_{*}^{2} = \tfrac{17}{2} - 6\sqrt{2} \in (0.01471, 0.01472)$. As in Theorem \claimref{synthesis.mass-ordered-dressing-cannot-spoil-koide}, label a sector's measured masses $m = (m_{1}, m_{2}, m_{3})$ in increasing order and call $b$ a bracket of $m$ under the dressing $D$ if $m_{k} = D_{k}b_{k}$ with $D_{k} > 0$; it is a Koide bracket if $Q(b) = \tfrac23$. The mass values are the stored quantities: own scale ($m_{u}$, $m_{d}$, $m_{s}$ at $2$ GeV, $m_{c}(m_{c})$, $m_{b}(m_{b})$, $m_{t}$ direct) and the running masses at $M_{Z}$.
\begin{enumerate}
\item[(i)] \emph{(Middle-mass bound.)} Every positive triple with $Q = \tfrac23$ has its middle entry at least $t_{*}^{2}$ times its largest entry, with equality exactly when its two smaller entries are equal.
\item[(ii)] \emph{(The up quarks.)} $m_{c}/m_{t} \in (0.00737, 0.00738)$ at own scale and $(0.00360, 0.00361)$ at $M_{Z}$, both below $t_{*}^{2}$, while $m_{s}/m_{b}$ lies above it at both. Hence no triple $(x, m_{c}, m_{t})$ with $0 < x \le m_{c}$ satisfies the Koide relation, whatever $x$; every Koide bracket of the up sector with $D_{c} \ge D_{t}$ has $b_{u} > b_{c}$; and a Koide bracket of the up sector with the bracket order kept, $b_{u} \le b_{c} \le b_{t}$, needs $D_{t}/D_{c} \ge t_{*}^{2}m_{t}/m_{c}$, which lies in $(1.99, 2.00)$ at own scale and $(4.08, 4.09)$ at $M_{Z}$.
\item[(iii)] \emph{(The class $D_{2} > D_{3} > D_{1}$.)} Part (iv) of Theorem \claimref{synthesis.mass-ordered-dressing-cannot-spoil-koide} applies to this class with $R = D_{3}/D_{1}$, so a Koide bracket in it needs $D_{3}/D_{1} \ge R^{*}$. The sharp bound is $D_{3}/D_{1} \ge R_{1}$, $R_{1}$ the least $R$ with $Q(Rm_{1}, m_{2}, m_{3}) \le \tfrac23$: $R_{1} \in (7.88, 7.89)$ (down, own scale), $(11.00, 11.01)$ (down, $M_{Z}$), $(2010.2, 2010.3)$ (up, own scale), $(4799.8, 4799.9)$ (up, $M_{Z}$). In the class $D_{1} > D_{3} > D_{2}$ a Koide bracket needs $D_{3}/D_{2} \ge R_{2}$, $R_{2}$ the least $R$ with $Q(m_{1}, Rm_{2}, m_{3}) \le \tfrac23$: $R_{2} \in (2.19, 2.20)$, $(2.63, 2.64)$, $(9.36, 9.37)$, $(19.33, 19.34)$ in the same order. Both classes contain Koide brackets in both sectors, so these are thresholds and not exclusions; in the up sector a Koide bracket of the class $D_{2} > D_{3} > D_{1}$ has $b_{u}/b_{t} \ge R_{1}m_{u}/m_{t} > b_{c}/b_{t}$, the bracket order reversed, as (ii) requires.
\item[(iv)] \emph{(No ordering of the factors escapes.)} In both quark sectors and at both sets of values, a Koide bracket needs, whatever the order of its dressing factors, $\max_{j \le 2}D_{3}/D_{j} \ge R^{*}$, with $R^{*}$ in the intervals of the stored theorem, $(1.88, 1.89)$, $(2.19, 2.20)$, $(8.67, 8.68)$ and $(17.5, 17.6)$ in the same order as in (iii), the least value being reached only with $D_{1} = D_{2}$; with $D_{2} > D_{3} > D_{1}$ the heaviest is favoured over the lightest by at least $R_{1}$, and in the up sector the bracket order of $u$ and $c$ is then reversed.
\end{enumerate}
So the remaining class of the stored theorem gives no escape: a Koide bracket for either quark sector needs a dressing that favours the heaviest quark, and none of the classes is excluded by the data alone. Whether the quark brackets satisfy the relation is decided only by a dressing law, which no stored premise supplies.

## technical
The stored theorem on mass-ordered dressing leaves open, in its own words, dressings that raise the middle quark mass and lower the lightest relative to the heaviest. Its corner bound in fact covers them: the bound holds whatever the light factors are, as long as neither exceeds the corner value, and in that class only the lightest factor exceeds one. The sharp bound in the class is larger: the lightest quark must be suppressed relative to the heaviest by at least $7.88$ (down quarks at own scale) and about $2010$ (up quarks at own scale), and by more at the $Z$ mass. A short exact lemma adds a parameter-free necessary condition: in any triple satisfying Koide's relation the middle mass is at least $17/2 - 6\sqrt{2}$, about $0.0147$, of the largest, with equality only when the two lighter masses coincide. The charm-to-top ratio is $0.0074$ at own scale and $0.0036$ at the $Z$ mass, both below that bound, so no value of the up-quark mass below the charm mass makes the up triple satisfy the relation, and any Koide bracket in which the charm is dressed up at least as much as the top must put the up bracket above the charm bracket. Keeping the bracket order needs the top favoured over the charm by about $2$ at own scale and $4.1$ at the $Z$ mass. The down quarks pass the lemma ($m_{s}/m_{b}$ about $0.022$). Every class contains Koide brackets, so the data decide nothing by themselves: the question is whether a dressing that favours the heaviest quark by these factors exists, and the store has no dressing law.

## lay
A formula due to Koide fits the electron, muon and tau masses remarkably well but fails for both families of quarks. One idea is that the quarks' underlying masses obey it and the strong force then shifts them. An earlier result showed that the known strong-force effects shift them the wrong way, and that only an effect favouring the heaviest quark could work; it left one kind of shift unexamined. This result examines it and finds no way out: that kind of shift also needs the heaviest quark strongly favoured, by a factor of at least about eight for the down-type quarks and about two thousand for the up-type quarks. It also proves a simple fact about any three numbers satisfying the formula: the middle one is at least about one and a half percent of the largest. The charm quark is well under one percent of the top quark's mass, so the up-type quarks would fail the formula whatever the up quark's mass below the charm mass, and the shift would have to reorder the up and charm quarks underneath. The data alone cannot settle whether quark masses obey the formula underneath; that needs a rule for the shift, which the series does not have.

## one-liner
Every Koide triple has its middle entry at least $\tfrac{17}{2} - 6\sqrt{2} \approx 0.0147$ of its largest, which $m_{c}/m_{t}$ ($0.0074$, $0.0036$ at $M_{Z}$) violates, so no up triple with $x \le m_{c}$ is Koide; the stored corner bound covers the class $D_{2} > D_{3} > D_{1}$, whose sharp threshold is $D_{3}/D_{1} \ge 7.88$ (down) and $2010$ (up, bracket order of $u$ and $c$ reversed): no ordering of the dressing factors escapes a dressing favouring the heaviest quark, and the data alone cannot decide the question.
