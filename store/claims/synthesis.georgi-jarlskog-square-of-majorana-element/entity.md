---
id: synthesis.georgi-jarlskog-square-of-majorana-element
kind: claim
version: 3
title: Under (S), the Georgi-Jarlskog composite is the (15,1,3) part of the square of the Majorana element
status: proved
region: synthesis
subject: standard-model
tags: [flavour-and-mixing, seesaw-and-majorana, representation-theory, spinor-modules]
proposed_by:
  kind: ai
  session: 2026-10-22-toe
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
  - synthesis.georgi-jarlskog-majorana-moment-map@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_gj_square_of_majorana_element
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.georgi-jarlskog-majorana-moment-map
  - standard-model.majorana-element
extraction:
  maintainer_pass_2026_10_31:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Version 3: clause (iv) corrected from "w_4 G_4 gives only the 10 relation" to "w_4 G_4 has no symmetric form (the 10 relation with multiple zero)", as synthesis.georgi-jarlskog-is-rung-vector-times-pair-part-of-majorana-square (iv) finds; the proof of (iv) now shows it directly (G_4 = 4 mu^2 - 5/64 is 5/16, -1/16, 1/16 on total mode number 0, 2, 4, and the rung vector couples only mode numbers 2 and 4), the technical level says the same, and the check asserts the symmetric form is zero instead of some multiple of the 10 form. The earlier wording suggested a nonzero 10 term; no other clause changed.'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 1 -> 2.'
  open_problem: op.pair-sector-current
  note: 'The stored moment-map result writes the Georgi-Jarlskog composite as the rung vector times the product of the two Pati-Salam components of the moment map of T, which is quartic in T. This result shows the same operator, up to the factor 8, is the pair-rung (15,1,3) part of the grade-four component of T T^dag, so it already appears at second order in a vev along T, not only at fourth order through the moment map. Which polynomial in T and its adjoint is the composite is a reading: at unit vev the two expressions are the same operator. A comparison with the induced (15,2,2) of Pati-Salam field theory is a literature recollection (Babu and Mohapatra 1993, cited from memory, unverified, not used). On the reading that the composite is the square, one vev along T gives the right-handed Majorana mass linearly and the Georgi-Jarlskog term quadratically. With an S_3-invariant Majorana sector, the 126 is family-blind on the light plane (filed alongside, synthesis.residual-s2-fixes-120-family-form); if the vev along T carries that family matrix, the quadratic composite inherits a family matrix built from it and does not single out the second family either, so it cannot by itself supply the second-family factor 3. The open coefficient here is the same open number as the 126 doublet vev of the Majorana-scale analysis filed alongside (synthesis.majorana-scale-is-126-doublet-vev). The coefficient, and so the 126 to 10 ratio, is still not fixed: the unsplit square gives no symmetric form (the 10 relation with multiple zero, as corrected in version 3), and the Pati-Salam split carries an undetermined weight. Transport-absent: Spin(10) and Pati-Salam representation theory on the module; the series content is that T and the slot/pair split are derived.'
---

## formal
Under Hypothesis (S), on the five-mode module with the pairing of Lemma \claimref{standard-model.invariant-pairing-five-modes}, let $T = v_{1}v_{2}v_{3}v_{4}v_{5}$ be the Majorana element of Proposition \claimref{standard-model.majorana-element}, $T^{\dagger}$ its adjoint, $\mu = \mu(T)$, $\mu_{P}$, $\mu_{R}$ its moment map and the Pati-Salam components of Proposition \claimref{synthesis.georgi-jarlskog-majorana-moment-map}, and $T_{\mathrm{GJ}} = w_{4}(B - L)\chi$ as in Proposition \claimref{families.doublet-direction-module-georgi-jarlskog-clebsch}. Expand operators in the monomials of the ten Majorana generators $a_{i} = v_{i} + w_{i}$, $b_{i} = v_{i} - w_{i}$, graded by degree. Then:
\begin{enumerate}
\item[(i)] $TT^{\dagger}$ is the projector onto the full state; its components of degree $0$, $2$ and $4$ are $\tfrac{1}{32}$, $\tfrac12\mu$ and $G_{4} = 4\mu^{2} - \tfrac{5}{64}$;
\item[(ii)] the part $X_{4}$ of $G_{4}$ whose monomials contain generators of both the pair and the rung modes is $X_{4} = 8\,\mu_{R}\mu_{P}$; it commutes with $\su(2)_{L}$ and with $B - L$ but not with $v_{4}v_{5}$, so it lies in the $(15,1,3)$ of the degree-four component;
\item[(iii)] $w_{4}X_{4} = \tfrac{3}{32}\bigl(T_{\mathrm{GJ}} - w_{4}(B - L)\bigr)$, whose mass form has symmetric part $\tfrac{3}{32}$ times the Georgi-Jarlskog form (ratio $|y_{e}/y_{d}| = 3$) and antisymmetric part $-\tfrac{3}{32}$ times the grade-three form;
\item[(iv)] $w_{4}G_{4}$ has no symmetric form: the symmetric part of its mass form is the $10$ form with multiple zero (as Theorem \claimref{synthesis.georgi-jarlskog-is-rung-vector-times-pair-part-of-majorana-square}(iv) also finds), since $G_{4}$ takes opposite values $\mp\tfrac{1}{16}$ on the two states of each pair the rung vector couples;
\item[(v)] under $T \mapsto cT$, $X_{4} \mapsto |c|^{2}X_{4}$, while $w_{4}\mu_{R}\mu_{P} \mapsto |c|^{4}\,w_{4}\mu_{R}\mu_{P}$.
\end{enumerate}
So the composite that carries the Georgi-Jarlskog factor is, up to the factor $8$, the $(15,1,3)$ part of the square $TT^{\dagger}$ of the Majorana element: it already appears at second order in a vev $c$ along $T$, not only at fourth order through the moment map, while the Majorana mass of $\nu^{c}$ is linear in $c$. Reading the composite as this part of the square, its strength relative to the rung vector's $10$ term is of order $|c|^{2}$; which polynomial in $T$ and $T^{\dagger}$ the dynamics selects is not derived, and the coefficient is not fixed.

## technical
Under Hypothesis (S) the square $TT^{\dagger}$ of the Majorana element is the projector onto the fully occupied state, the product of the five occupation numbers. Expanded in the Clifford monomials of the ten Majorana generators it has a scalar part $\tfrac{1}{32}$, a bivector part equal to half the moment map, and a degree-four part $4\mu^{2} - \tfrac{5}{64}$, a polynomial in the moment map that, multiplied into the rung vector, gives no symmetric mass form at all (the relation of a single $10$ with multiple zero): it takes opposite values on the two states of each pair the rung vector couples.

Split along Pati-Salam, the degree-four part has a piece built from both the pair and the rung modes, and that piece is exactly $8\mu_{R}\mu_{P}$, an $\su(2)_{L}$ singlet in the $(15,1,3)$. The rung vector times it is $\tfrac{3}{32}(T_{\mathrm{GJ}} - w_{4}(B - L))$: the Georgi-Jarlskog $126$ form with ratio $3$ plus the grade-three form with equal moduli, the composite of the stored moment-map result. That composite was written as a product of two moment-map components, quartic in $T$; this shows the same operator is also the $(15,1,3)$ part of $TT^{\dagger}$, so it already appears at second order in a vev along $T$. Read that way, a vev $c$ along $T$ gives the right-handed Majorana mass at first order and the Georgi-Jarlskog term at second order, $|c|^{2}$; which polynomial is the physical composite is a reading, not derived. The coefficient of the Pati-Salam split, and so the size of the $126$ relative to the $10$, is not determined. If the vev carries an $S_{3}$-invariant family matrix, the term is family-blind on the light plane and does not by itself single out the second family.

## lay
Under the framework's slot hypothesis (S), the element that gives the right-handed neutrino its large mass also, when squared, contains the ingredient behind the factor of three between the muon and strange-quark masses at high energy. An earlier result found that ingredient as a product of four copies of this element; here it appears already in the square, the piece of the square that mixes the quark-lepton charge with the right-handed weak charge. So, read this way, if this element acquires a value that breaks the symmetry, the neutrino mass appears in proportion to that value and the factor-of-three term already in proportion to its square. On its own the term does not pick out the second family of particles. How large the factor-of-three term is compared with the ordinary mass term is still not fixed.

## one-liner
Under (S), the pair-rung degree-four part of $TT^{\dagger}$ is $8\mu_{R}\mu_{P}$, a $(15,1,3)$, and $w_{4}$ times it is $\tfrac{3}{32}(T_{\mathrm{GJ}} - w_{4}(B - L))$, so the Georgi-Jarlskog composite already appears at second order in a vev along the Majorana element (as part of $TT^{\dagger}$), not only at fourth order through the moment map; its coefficient is not fixed.
