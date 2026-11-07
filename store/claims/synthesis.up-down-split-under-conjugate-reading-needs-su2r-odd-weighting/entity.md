---
id: synthesis.up-down-split-under-conjugate-reading-needs-su2r-odd-weighting
kind: claim
version: 3
title: 'An up-down split under the conjugate reading needs $T_{3R}$-odd weighting'
status: proved
region: synthesis
subject: standard-model
tags: [flavour-and-mixing, seesaw-and-majorana, symmetry-breaking, representation-theory]
proposed_by:
  kind: ai
  session: 2026-10-31-all-open
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
  - standard-model.one-vev-vector-relations-breaking-pattern@7
  - standard-model.invariant-pairing-five-modes@5
  - standard-model.hyp-s-slot-statistics@9
  - standard-model.yukawa-pattern-two-rung-module@5
  - standard-model.generation-ten-under-pati-salam@7
  - standard-model.automorphisms-preserve-slot-pair-split-are@6
  - standard-model.majorana-element@7
  - families.doublet-direction-module-georgi-jarlskog-clebsch@6
  - synthesis.georgi-jarlskog-majorana-moment-map@3
  - synthesis.georgi-jarlskog-square-of-majorana-element@3
  - synthesis.georgi-jarlskog-is-rung-vector-times-pair-part-of-majorana-square@2
  - synthesis.neutral-singlet-bit-decided-by-gauge-algebra-leaving-u5@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_t3r_even_weightings_never_split_up_from_down
- kind: check
  ref: check.py::check_parts_of_the_square_under_the_conjugate_reading
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - standard-model.one-vev-vector-relations-breaking-pattern
  - synthesis.second-doublet-of-one-family-coupling-gives-no-quark-mixing
extraction:
  maintainer_pass_weak_scale:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 3 (Leon''s decision of 2026-11-01 on the Yukawa form): a marked note says that the conjugate reading stands for the su(2)_R-covariant completion (Y on c and Ytilde on c* as wholes; synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix), that the per-sector reading used here is its leading mass reading and not su(2)_R covariant, and that under the completion one rung vector already splits up from down by 2m(c)(|Y|^2 - |Ytilde|^2). The clauses are unchanged.'
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Version 2: uses edges to synthesis.georgi-jarlskog-is-rung-vector-times-pair-part-of-majorana-square@2 (the split of G_4 into P_4, X_4 and R_4, which the proof also derives) and to synthesis.neutral-singlet-bit-decided-by-gauge-algebra-leaving-u5@2 (the Pati-Salam stage forces the halving (-1)^N with nu^c the empty state, on which the Dirac-neutrino clauses depend), each now cited where it enters; the pin of synthesis.georgi-jarlskog-square-of-majorana-element moves to version 3, whose clause (iv) now states the zero multiple used in (iii) here. Content unchanged.'
  open_problem: op.rung-unit
  note: >-
    The problem's fourth line of attack: find what splits up-type from down-type masses under the reading of
    up-type masses through the conjugate c*. Under that reading one rung coupling gives m_u = m_d at tree
    level, and a second vev of the same family coupling gives M_u a multiple of M_d
    (synthesis.second-doublet-of-one-family-coupling-gives-no-quark-mixing). This result asks the same
    question one level down, for composites c g of the rung vector with a diagonal weighting g, read the
    way the stored reading reads c: down-type and charged-lepton entries from w_4 g, up-type and
    Dirac-neutrino entries from v_4 g with the same magnitude. Down-type pairs (L, e^c), (Q, d^c) and up-type
    pairs (L, nu^c), (Q, u^c) share the doublet and differ only in the singlet, whose T3R is +1/2 for e^c,
    d^c and -1/2 for nu^c, u^c, while |B - L| is the same; so the even part of g in T3R gives equal up and
    down entries and the odd part opposite ones. The 10 and every f(B - L), in particular the
    Georgi-Jarlskog composite w_4 P_4
    (\claimref{synthesis.georgi-jarlskog-is-rung-vector-times-pair-part-of-majorana-square}), never split up from
    down: the 126 route's (15,1,1) composite keeps m_u = m_d under this reading. The split of G_4 into its pair-only part P_4 and rung-only part R_4 is derived in the proof (it is also
    the subject of the filed-alongside synthesis.georgi-jarlskog-is-rung-vector-times-pair-part-of-majorana-square). The Majorana element is the
    T3R-highest weight of an su(2)_R triplet, and its square carries T3R-odd parts: the moment-map component
    mu_R = T3R/4 and the (15,1,3) part X_4 = 8 mu_R mu_P. X_4 enters up and down with opposite signs, so the
    degree-four part G_4 of T T^dag gives up-type and Dirac-neutrino entries only (-(3/16) times the up-type
    Georgi-Jarlskog form, |m_nu^D| = 3 |m_u|) and no down-type or charged-lepton entry; through degree four
    the square gives the down sector the 10 relation and the up sector that 126-type form alone. So a vev
    along T is, in form, a source of the up-down split that the stored no-go asks for, provided its family
    matrix is not that of the 10 (argued: the composite inherits the family structure of the Majorana sector,
    which the stored residual-S2 and S3 results constrain; reading, argued: with an S3-invariant Majorana sector it is
    family-blind on the light plane and cannot by itself produce the hierarchy). Which degree truncation or
    Pati-Salam projection of the square a dynamics selects is not derived; the whole square gives no entry.
    The reading of composites through c* is the stored reading extended to c g, stated as such. Scope: the sixteen here is the even half, the particle half fixed by the slot-module premise, whose chirality clause requires the chirality to commute with the Pati-Salam algebra of the chain; with CPT and anomaly freedom that forces this halving (\claimref{synthesis.neutral-singlet-bit-decided-by-gauge-algebra-leaving-u5}). In the vacuum-swapped halving the neutral singlet has no odd-grade pairing with its half, so the Dirac-neutrino entries (L, nu^c) stated here do not exist there, while the charged-fermion entries are unchanged. Transport-absent.
---

## formal
Under Hypothesis (S), on the module of Proposition \claimref{synthesis.georgi-jarlskog-majorana-moment-map}, let $c = a\,v_{4} + b\,w_{4}$ be the rung vector of Corollary \claimref{standard-model.one-vev-vector-relations-breaking-pattern}, with down-type and charged-lepton masses read from $c$ and up-type and Dirac-neutrino masses through $c^{*} = \bar{b}\,v_{4} + \bar{a}\,w_{4}$. For a diagonal weighting $g$ read the same way (down-type and charged-lepton entries from $b\,w_{4}g$, up-type and Dirac-neutrino entries from $\bar{b}\,v_{4}g$), with mass forms $B(\psi, X\varphi)$ on the sixteen (Lemma \claimref{standard-model.invariant-pairing-five-modes}), the sixteen being the particle half $\pm(-1)^{N}$ of Proposition \claimref{standard-model.hyp-s-slot-statistics}, with $\nu^{c}$ the empty state (the halving the Pati-Salam stage of the chain forces, Theorem \claimref{synthesis.neutral-singlet-bit-decided-by-gauge-algebra-leaving-u5}(iii); the Dirac-neutrino statements need that halving), write the symmetric entries relative to those of the $10$ forms of $w_{4}$ and $v_{4}$ on the same species pairs (Theorem \claimref{standard-model.yukawa-pattern-two-rung-module}). Let $T$, $\mu_{P}$, $\mu_{R}$, $\chi$, $X_{4} = 8\mu_{R}\mu_{P}$ and the degree-four part $G_{4}$ of $TT^{\dagger}$ be as in Propositions \claimref{standard-model.majorana-element}, \claimref{synthesis.georgi-jarlskog-majorana-moment-map} and \claimref{synthesis.georgi-jarlskog-square-of-majorana-element}, and let $P_{4}$ and $R_{4}$ be the pair-only and rung-only parts of $G_{4}$, so that $G_{4} = P_{4} + X_{4} + R_{4}$ with $P_{4} = \tfrac{3}{32}(B - L)(-1)^{N_{P}}$ and $R_{4} = -\tfrac{1}{32}\chi$ (derived in the proof). Then:
\begin{enumerate}
\item[(i)] for $g = h(T_{3R}, B - L)$ the down-type entries are $e + o$ and the up-type entries $e - o$ on each sector, $e$ and $o$ the contributions of the parts of $h$ even and odd in $T_{3R}$; so a $T_{3R}$-even weighting gives $m_{u} = m_{d}$ and $m_{\nu}^{D} = m_{e}$, and in particular the $10$ and every $f(B - L)$, among them $P_{4}$, never split up-type from down-type entries;
\item[(ii)] relative to the $10$ (lepton, quark): $P_{4}$ gives $(\tfrac{3}{32}, -\tfrac{1}{32})$ in both sectors; $X_{4}$ gives $(-\tfrac{3}{32}, \tfrac{1}{32})$ down and $(\tfrac{3}{32}, -\tfrac{1}{32})$ up; $\mu_{R} = \tfrac14 T_{3R}$ gives $(\tfrac{1}{16}, \tfrac{1}{16})$ down and $(-\tfrac{1}{16}, -\tfrac{1}{16})$ up; $R_{4}$ and $\mu_{P}$ give no symmetric entry;
\item[(iii)] hence $G_{4}$ gives no down-type or charged-lepton entry and up-type entries equal to $-\tfrac{3}{16}$ times the up-type Georgi-Jarlskog form $v_{4}(B - L)\chi$ of Proposition \claimref{families.doublet-direction-module-georgi-jarlskog-clebsch}(iv), so $|m_{\nu}^{D}| = 3|m_{u}|$ for this contribution; and the square through degree four, $\tfrac{1}{32} + \tfrac12\mu + G_{4}$, gives the down sector the $10$ relation ($m_{e} = m_{d}$) with weight $\tfrac{1}{16}$ and the up sector that $126$-type form alone; the whole square $TT^{\dagger}$ gives no entry.
\end{enumerate}
So under the conjugate reading the up-down split of a rung composite is carried by its $\su(2)_{R}$-odd part, and the degree-four part of the square of the Majorana element, whose orientation in $\su(2)_{R}$ is that of $T$, supplies one that acts on the up sector alone; it is a truncation that no stored dynamics selects, and the whole square gives no entry on the sixteen.

\emph{Note (the covariant completion, 2026-11-01).} The conjugate reading stands for the $\su(2)_{R}$-covariant completion of the coupling: one family matrix $Y$ on $c$ and one $\tilde{Y}$ on $c^{*}$, each on the whole vector, $M_{d} = bY + \bar{a}\tilde{Y}$, $M_{u} = aY + \bar{b}\tilde{Y}$ (\claimref{synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix}). The per-sector reading used here (down-type entries from $c$ or $c\,g$, up-type entries from $c^{*}$ or its weighting, one family matrix) is its leading mass reading, equal to it up to relative corrections $e^{-2\eta}$ on the lift family, and is not $\su(2)_{R}$ covariant: it vanishes on the $a$ half of $c$, which the right-handed $\su(2)$ carries into the $b$ half. The clauses above are statements about that leading reading; under the completion an independent $\tilde{Y}$ splits up from down already for one rung vector, by $\tr H_{u} - \tr H_{d} = 2m(c)(\|Y\|^{2} - \|\tilde{Y}\|^{2})$ (loc. cit.), the $T_{3R}$-odd channel of (i) in another guise (\claimref{synthesis.conjugate-reading-up-down-split-is-t3r-odd-or-cp-odd}).

## technical
The series reads up-type masses through the conjugate of the rung vector, and under that reading one rung coupling gives up and down quarks equal masses. The question here is which dressings of the rung coupling can split them. An up-type mass term and the matching down-type term share the left-handed doublet and differ only in the right-handed singlet: $u^{c}$ and $\nu^{c}$ have right-handed isospin $-\tfrac12$, $d^{c}$ and $e^{c}$ have $+\tfrac12$, and they have the same size of $B - L$. A dressing that does not distinguish the sign of the right-handed isospin therefore gives equal up and down masses; this covers the plain $10$ and every function of $B - L$, including the Georgi-Jarlskog composite. A dressing odd in that isospin gives opposite contributions. The square of the Majorana element contains such odd pieces, because the Majorana element itself points along one direction of right-handed isospin. Adding its degree-four pieces (a truncation of the square that nothing in the stored structure selects; the whole square gives no mass entry), the down-type contributions cancel exactly and the up-type ones add: the result feeds up-type quark and Dirac neutrino masses only, in the ratio $3$ between them. Whether a dynamics selects this piece, and with which family matrix, is not derived.

## lay
In this framework, under its conjugate reading, the up-type quarks (up, charm, top) and the down-type quarks (down, strange, bottom) get their masses from one coupling read in two ways, which at first order makes them equal, against the observed large ratio of top to bottom. This result shows that any correction that does not tell left-right isospin apart keeps them equal, and that the square of the heavy object that gives neutrinos their large mass does tell it apart: one natural part of it feeds only the up-type quarks and the neutrinos. How large that part is, and how it is shared among the three families, is not decided.

## one-liner
Under the $c^{*}$ reading applied to composites $c\,g$, $T_{3R}$-even weightings ($10$, any $f(B - L)$, the Georgi-Jarlskog $P_{4}$) give $m_{u} = m_{d}$, $T_{3R}$-odd ones opposite up and down entries; $X_{4}$ and $\mu_{R}$ are odd, so the degree-four part of $TT^{\dagger}$ (a truncation; the whole square gives nothing) gives up-type entries $-\tfrac{3}{16}$ times the up-type Georgi-Jarlskog form ($|m_{\nu}^{D}| = 3|m_{u}|$) and no down-type entry.
