---
id: synthesis.georgi-jarlskog-is-rung-vector-times-pair-part-of-majorana-square
kind: claim
version: 2
title: 'Pure Georgi-Jarlskog from the pair part of the Majorana square, under (S)'
status: proved
region: synthesis
subject: standard-model
tags: [flavour-and-mixing, seesaw-and-majorana, representation-theory, spinor-modules]
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
  - standard-model.invariant-pairing-five-modes@5
  - standard-model.majorana-element@7
  - families.doublet-direction-module-georgi-jarlskog-clebsch@6
  - standard-model.grade-three-georgi-jarlskog-direction@5
  - synthesis.georgi-jarlskog-majorana-moment-map@3
  - synthesis.georgi-jarlskog-square-of-majorana-element@3
  - standard-model.automorphisms-preserve-slot-pair-split-are@7
  - standard-model.generation-ten-under-pati-salam@7
  - standard-model.yukawa-pattern-two-rung-module@6
  - standard-model.hyp-s-slot-statistics@9
  - synthesis.neutral-singlet-bit-decided-by-gauge-algebra-leaving-u5@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_pati_salam_split_of_the_square
- kind: check
  ref: check.py::check_rung_vector_times_pair_part_is_georgi_jarlskog
- kind: check
  ref: check.py::check_even_and_odd_pair_weightings
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.georgi-jarlskog-square-of-majorana-element
  - synthesis.georgi-jarlskog-majorana-moment-map
extraction:
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Version 2: a uses edge to synthesis.neutral-singlet-bit-decided-by-gauge-algebra-leaving-u5@2, which shows that the Pati-Salam stage of the chain forces the halving (-1)^N with nu^c the empty state, on which the Dirac-neutrino clauses depend; the formal statement and proof (ii) now cite it where the halving is fixed. The pin of synthesis.georgi-jarlskog-square-of-majorana-element moves to version 3, whose clause (iv) was corrected to the zero multiple this result finds; nothing used here changed. Content unchanged.'
  open_problem: op.pair-sector-current
  note: >-
    The problem's first line of attack: derive the relative weight of the terms of one polynomial along the
    Majorana element and test whether it gives the factor 3. The stored square result isolates the pair-rung
    (15,1,3) part X_4 of the degree-four component G_4 of T T^dag, whose product with the rung vector
    carries the Georgi-Jarlskog form together with an equal-modulus grade-three (120) form. This result
    splits the rest of G_4: its pair-only part is 4 mu_P^2 - 3/64 = (3/64)(3(B - L)^2 - 1) =
    (3/32)(B - L)(-1)^{N_P}, a (15,1,1), and its rung-only part is -chi/32, the Pati-Salam singlet. On the
    sixteen the rung parity chi is minus the pair parity, so the rung vector times the pair part is
    -(3/32) T_GJ there as an operator: the Georgi-Jarlskog operator is literally w_4 times the (15,1,1)
    part of the square, with no grade-three admixture and no 10 component. Given the (15,1,1) part, the factor 3 is not fitted:
    for any weighting f(B - L) of the rung vector, the even part gives the 10 with weight one quarter of the
    trace of f over a Pati-Salam quartet and the odd part gives a 120 form, and pair elements of degree two
    and four are traceless on each quartet; so every pair-only element of positive degree below six that is
    even in B - L gives pure Georgi-Jarlskog. The test asked for is answered in two parts: the square's own
    (15,1,1) part gives the factor 3 exactly; but no weighting internal to the square fixes its coefficient
    relative to the 10, because the symmetric forms of the three degree-four parts cancel (w_4 G_4 has no
    symmetric form at all, which sharpens the stored statement that the unsplit square gives only the 10
    relation: the multiple is zero), and the scalar part together with the pair part, 1/32 + PP, gives the
    rung vector a lepton-only form (y_d = 0). So the 126 coefficient relative to the 10 is the weight a
    dynamics gives to the (15,1,1) projection of the square, the open number, now located in one Pati-Salam
    component. That Pati-Salam invariance allows an independent coupling per component is argued, not
    checked. The Pati-Salam (15,2,2) origin of the Georgi-Jarlskog Clebsch is standard (Georgi and Jarlskog
    1979, cited from memory, not used). Scope: the sixteen here is the even half, the particle half fixed by the slot-module premise, whose chirality clause requires the chirality to commute with the Pati-Salam algebra of the chain; with CPT and anomaly freedom that forces this halving (\claimref{synthesis.neutral-singlet-bit-decided-by-gauge-algebra-leaving-u5}). In the vacuum-swapped halving the neutral singlet has no odd-grade pairing with its half, so the Dirac-neutrino entries (L, nu^c) stated here do not exist there, while the charged-fermion entries are unchanged. Transport-absent: Clifford algebra of the ten on the module; the
    series content is that T, the pairing and the slot/pair split are derived.
---

## formal
Work on the module $\Lambda^{\bullet}(W \oplus R_{2})$ of Proposition \claimref{synthesis.georgi-jarlskog-majorana-moment-map}, with $\beta_{i} = v_{i} \wedge w_{i} = n_{i} - \tfrac12$, $\mu_{P} = \tfrac18(\beta_{1} + \beta_{2} + \beta_{3})$, $\mu_{R} = \tfrac18(\beta_{4} + \beta_{5})$, $B - L = -\tfrac{16}{3}\mu_{P}$, $\chi = -(-1)^{N_{R}}$, $N_{P}$ the pair number, the Majorana element $T = v_{1}\cdots v_{5}$ of Proposition \claimref{standard-model.majorana-element}, $T_{\mathrm{GJ}} = w_{4}(B - L)\chi$ as in Proposition \claimref{families.doublet-direction-module-georgi-jarlskog-clebsch}, and mass forms $B(\psi, X\varphi)$ on the sixteen with the pairing of Lemma \claimref{standard-model.invariant-pairing-five-modes}. Here and below the sixteen is the particle half $(-1)^{N}$ of Proposition \claimref{standard-model.hyp-s-slot-statistics}, in which the empty state is $\nu^{c}$, the halving that the Pati-Salam stage of the chain forces (Theorem \claimref{synthesis.neutral-singlet-bit-decided-by-gauge-algebra-leaving-u5}(iii)); the Dirac-neutrino statements need that halving. Let $G_{4}$ be the degree-four part of $TT^{\dagger}$ in the Majorana monomials (Proposition \claimref{synthesis.georgi-jarlskog-square-of-majorana-element}), and split it by support into the pair-only part $P_{4}$, the pair-rung part $X_{4}$ and the rung-only part $R_{4}$. Then:
\begin{enumerate}
\item[(i)] \emph{(The split.)} $P_{4} = 4\mu_{P}^{2} - \tfrac{3}{64} = \tfrac{3}{64}\bigl(3(B - L)^{2} - 1\bigr) = \tfrac{3}{32}(B - L)(-1)^{N_{P}}$, which commutes with $\su(2)_{L}$, $\su(2)_{R}$, $\su(3)$ and $B - L$ but not with the pair bracket $v_{1}v_{2}$, so it lies in the $(15,1,1)$; $X_{4} = 8\mu_{R}\mu_{P}$, in the $(15,1,3)$ (stored); and $R_{4} = 4\mu_{R}^{2} - \tfrac{1}{32} = -\tfrac{1}{32}\chi$, the Pati-Salam singlet of Proposition \claimref{standard-model.automorphisms-preserve-slot-pair-split-are}.
\item[(ii)] \emph{(Pure Georgi-Jarlskog.)} On the sixteen $\chi = -(-1)^{N_{P}}$, so $w_{4}P_{4} = -\tfrac{3}{32}T_{\mathrm{GJ}}$ there, as operators. Its mass form is $-\tfrac{3}{32}$ times the Georgi-Jarlskog form, symmetric, with no antisymmetric ($120$) part and no $10$ component, $|y_{e}/y_{d}| = 3$; likewise $v_{4}P_{4}$ gives $-\tfrac{3}{32}$ times the up-type form of that proposition, $|m_{\nu}^{D}| = 3|m_{u}|$.
\item[(iii)] \emph{(Why $3$.)} For a weighting $f(B - L)$ of the rung vector, the even part of $f$ gives the symmetric form $x\,(10) + y\,(\mathrm{GJ})$ with $x = \tfrac14\bigl(3f(\tfrac13) + f(1)\bigr)$, a quarter of the trace of $f$ over a Pati-Salam quartet ($B - L = \tfrac13, \tfrac13, \tfrac13, -1$, Proposition \claimref{standard-model.generation-ten-under-pati-salam}), and $y = \tfrac34\bigl(f(\tfrac13) - f(1)\bigr)$, with no antisymmetric part; the odd part gives an antisymmetric form and no symmetric one, the grade-three form of Proposition \claimref{standard-model.grade-three-georgi-jarlskog-direction} for $f = B - L$. Pair-only Majorana monomials of degree two and four have zero trace on each pair-parity half of $\Lambda^{\bullet}W$ (each quartet); the degree-six one does not. Hence an even pair weighting gives the pure Georgi-Jarlskog form exactly when it is traceless on the quartet, as $P_{4}$ is.
\item[(iv)] \emph{(The square does not fix the coefficient.)} $w_{4}X_{4}$ gives $+\tfrac{3}{32}$ times the Georgi-Jarlskog form and $-\tfrac{3}{32}$ times the grade-three form (stored); $w_{4}R_{4}$ has no symmetric form; so the symmetric form of $w_{4}G_{4}$ vanishes identically. The scalar part of $TT^{\dagger}$ with the pair part, $w_{4}(\tfrac{1}{32} + P_{4})$, gives a lepton-only form, $\tfrac18$ of the $10$ form on $(L, e^{c})$ and zero on $(Q, d^{c})$.
\end{enumerate}
So the Georgi-Jarlskog operator is the rung vector times the $(15,1,1)$ part of the square of the Majorana element, at second order in a vev along $T$ and without the grade-three term that the $(15,1,3)$ composite carries; the factor $3$ is the quartet tracelessness of that part. The square, taken whole or truncated by degree, does not supply the weight of the $(15,1,1)$ part relative to the $10$; that weight is the open coefficient.

## technical
The problem asks whether one polynomial along the Majorana element fixes how strongly the $126$ enters the second family's mass relative to the $10$, and whether it produces the Georgi-Jarlskog factor $3$. The stored result found the Georgi-Jarlskog composite inside the square $TT^{\dagger}$ of the Majorana element as its pair-rung part, but with an equal-strength $120$ term attached. Here the remaining degree-four parts are computed. The pair-only part is a function of $B - L$ alone, and on the sixteen it equals $\tfrac{3}{32}(B - L)$ times the pair parity, which there is minus the rung parity; so the rung vector times it is exactly the Georgi-Jarlskog operator, with no $120$ and no $10$ part. The reason is a trace: any weighting of the rung coupling by a function of $B - L$ gives a $10$ part proportional to its trace over a Pati-Salam quartet, and the pair-space elements of degree two and four are traceless there. Given the square's own $(15,1,1)$ part, the factor $3$ therefore follows, with nothing fitted; which part a dynamics picks is open. The coefficient does not: the three degree-four parts give Georgi-Jarlskog terms that cancel, the whole degree-four component gives no symmetric mass at all, and keeping the scalar part alongside gives masses to leptons only. What a dynamics must supply is the weight of one Pati-Salam component of the square.

## lay
In this framework one hypothetical heavy object, the Majorana element, gives the right-handed neutrino its large mass. Squaring it produces several pieces that differ in how they transform under the larger symmetry of the model. One piece, combined with the ordinary Higgs coupling, produces exactly the classic three-to-one ratio between the masses of a charged lepton and a down-type quark, which the second family shows approximately when the masses are run to a high scale (a recollection from the literature, not used), and nothing else. Given that piece, the ratio three follows from the structure; which piece a dynamics picks is open. How strongly that piece enters, compared with the ordinary coupling, is still not decided by anything in the model.

## one-liner
The degree-four part of $TT^{\dagger}$ is $(4\mu_{P}^{2} - \tfrac{3}{64}) + 8\mu_{R}\mu_{P} - \tfrac{1}{32}\chi$, of Pati-Salam types $(15,1,1)$, $(15,1,3)$, $(1,1,1)$; on the sixteen $w_{4}(4\mu_{P}^{2} - \tfrac{3}{64}) = -\tfrac{3}{32}T_{\mathrm{GJ}}$, pure Georgi-Jarlskog with no $10$ or $120$ part, because degree-two and degree-four pair elements are traceless on the quartet; the symmetric forms of the three parts cancel, so the $126$ coefficient relative to the $10$ is the unfixed weight of the $(15,1,1)$ part.
