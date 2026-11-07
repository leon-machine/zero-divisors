---
id: synthesis.interacting-fields-of-causal-perturbation-theory-keep-the-spin-statistics-connection-at-even-ghost-number
kind: claim
version: 3
title: 'Causal perturbation theory keeps spin-statistics at even ghost number'
status: proved
region: synthesis
subject: quantum-fields
tags: [car-algebra, gauge-fields, recovers-known-physics, superselection, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-02-qft-full
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
review: draft
imported_from:
- citation: 'M. Dütsch and K. Fredenhagen, A local (perturbative) construction of observables in gauge theories: the example of QED, Commun. Math. Phys. 203 (1999), 71--105; arXiv:hep-th/9807078.'
  key: DutschFredenhagen1999
  locator: 'Sec. 2: causality (2.2), Poincare covariance (N1) (2.3), interacting fields (2.7), Proposition 2, locality (2.25), footnote 3; Sec. 4.1, (4.3); Sec. 4.3, Theorem 4'
  doi: 10.1007/s002200050606
- citation: 'H. Epstein and V. Glaser, The role of locality in perturbation theory, Ann. Inst. H. Poincare A 19 (1973), 211--295.'
  key: EpsteinGlaser1973
- citation: 'S. Hollands, Renormalized quantum Yang-Mills fields in curved spacetime, Rev. Math. Phys. 20 (2008), 1033--1172; arXiv:0705.3340.'
  key: Hollands2008
  locator: 'Secs. 3.7 and 4.1.2 (interacting fields; not read beyond the introduction)'
- citation: 'D. Buchholz and J. E. Roberts, New light on infrared problems: sectors, statistics, symmetries and spectrum, Commun. Math. Phys. 330 (2014), 935--972; arXiv:1304.2794.'
  key: BuchholzRoberts2014
  locator: 'Abstract and introduction'
  doi: 10.1007/s00220-014-2004-2
derivations:
- name: main
  uses:
  - synthesis.locality-of-the-attached-free-fields-fixes-their-statistics@4
  - field-theory.second-quantisation@5
  - field-theory.imported-tower-limit@3
  - synthesis.one-loop-qed-in-the-spacetime-algebra@4
  - synthesis.self-adjoint-brst-charge-needs-a-krein-form-and-the-tower-supplies-the-ghosts@3
  - synthesis.imported-epstein-glaser-extension-theorem-and-ward-preserving-time-ordered-products@1
  assumes:
  - synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_rotation_by_two_pi_is_minus_one_on_spinor_values_and_one_on_tensor_values
- kind: check
  ref: check.py::check_interaction_monomials_are_lorentz_scalars_even_in_spinors_and_ghosts
- kind: check
  ref: check.py::check_feynman_gauge_potential_is_local_only_in_the_krein_form
- kind: check
  ref: check.py::check_rotation_by_two_pi_equals_the_grading_exactly_at_even_ghost_count
- kind: check
  ref: check.py::check_first_order_interacting_fields_keep_parity_spin_and_graded_locality
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - field-theory.imported-standard-field-theory
  - synthesis.modular-period-on-values-is-the-dual-plane-turn
  - synthesis.imported-free-field-spin-statistics-and-guido-longo-theorem
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The unit of Bogoliubov''s interacting-field formula and of its n-th order coefficient I_4^n/n! is now the field theory''s unit I_4, the complex unit of the free fields'' Fock space (numbers read in span{1, I_4}); no bare i remains.'
  maintainer_pass:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 1 -> 2, by Leon''s decisions of 2 November 2026: an assumes edge to the Krein premise synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields@2, since the result assumes the Gupta-Bleuler (indefinite) form of the free Feynman-gauge potential, clause (K1), as the hypothesis under which that potential is local (stated in the formal level; now named there and in the proof); a uses edge to the imported Fact synthesis.imported-epstein-glaser-extension-theorem-and-ward-preserving-time-ordered-products@1 (Epstein-Glaser, Duetsch-Fredenhagen 1999, Hollands 2008), which pins the causal perturbation theory the result applies; the text citations of synthesis.wedge-reflections-compose-to-the-two-pi-rotor-so-geometric-modular-conjugations-give-interacting-spin-statistics become claimrefs (formal, technical, proof) and a plain id (note), with no edge. Statement unchanged; the axioms used and the covering-group assumption are as before.'
  open_problem: op.qft-structural-inputs
  note: >-
    The attack line "spin and statistics for interacting fields: replace the Jost-point import by a premise
    the series already holds". Answer for the perturbative theory: the interacting fields of causal
    perturbation theory inherit the statistics of the free fields order by order (standard: Dutsch and
    Fredenhagen 1999 for QED with spinors and ghosts; Hollands 2008 for Yang-Mills with coupled ghosts, cited
    from memory), and covariance under the covering group carries the spin; what is new is the bookkeeping on the
    series' own field list in the spacetime algebra (the 2 pi rotor as the loop of four quarter turns, the
    interaction monomials of the stored QED, two-doublet and BRST results, the tower ghosts) and the exact
    statement of where the connection fails (odd ghost count, the Krein case of the free-field result). What
    remains beyond perturbation theory is a nonperturbative premise, discussed in
    synthesis.wedge-reflections-compose-to-the-two-pi-rotor-so-geometric-modular-conjugations-give-interacting-spin-statistics.
    For electrically charged fields the nonperturbative charge classes are localised in hypercones
    (Buchholz and Roberts 2014, abstract read: Bose or Fermi type, covariant, positive energy; a
    spin-statistics theorem was not found in what was read). Kill conditions registered before computing: an odd or non-invariant interaction monomial, a
    failure of the graded Jacobi identity for even L, a ghost-number-zero monomial whose grading differs
    from its 2 pi eigenvalue; none fired. Transport-absent: the inheritance is standard causal perturbation
    theory; the series supplies the field list and the tower ghosts.
  flags:
  - 'Dutsch and Fredenhagen 1999 read in the arXiv text (ar5iv): Prop. 2 and (2.25) state graded locality of interacting fields, the anticommutator appearing only when both fields have an odd number of spinor fields or both an odd number of ghost fields (their convention: free spinors commute with free ghosts, footnote 3); (N1) is covariance under the proper orthochronous Poincare group itself, so covariance under its covering group is an assumption here; (N3) is the Wick expansion; in their QED the ghosts do not couple; journal volume and pages from memory'
  - 'Epstein and Glaser 1973 cited from memory (existence of causal, covariant time-ordered products); all-orders graded locality with a coupled ghost vertex (Yang-Mills) is cited to Hollands 2008 from memory, the paper located (arXiv:0705.3340) but its Secs. 3.7 and 4.1.2 not read'
  - 'locality of the free potential in Feynman gauge with the Gupta-Bleuler (Krein) form is not covered by the stored free-field result, which treats the field strength at positive norm; it is a condition here, with the degree-0 polarisation sum computed'
  - 'the store''s free-field statistics result is for massless fields; the series'' masses enter through the rung field''s Yukawa couplings and its vacuum value, two-spinor insertions of even parity, so the perturbation can be posed around massless free fields; locality of the massive free Dirac field is standard, cited from memory'
  - 'the statement is about formal power series; no convergence and no nonperturbative vacuum are claimed'
---

## formal
Units and signature of the store; $\Cl(1,3)$ with $I_{4} = \gamma_{0}\gamma_{1}\gamma_{2}\gamma_{3}$. The attached free fields are the Dirac spinor values $\psi$ of Proposition \claimref{field-theory.second-quantisation}, on which a Lorentz rotor $R$ acts by $\psi \mapsto R\psi$; the gauge potentials and their gradients, vector values with $x \mapsto Rx\tilde R$; palatial scalars, any number of doublets; and the Faddeev-Popov ghosts $c$, $\bar c$, scalar CAR modes on tower planes (\claimref{synthesis.self-adjoint-brst-charge-needs-a-krein-form-and-the-tower-supplies-the-ghosts}, Fact \claimref{field-theory.imported-tower-limit}). Their statistics are those of \claimref{synthesis.locality-of-the-attached-free-fields-fixes-their-statistics}: anticommuting spinors, commuting scalars and field strengths, anticommuting ghosts in the indefinite form; for the potential itself in Feynman gauge, which that result does not cover, we assume the Gupta-Bleuler (indefinite) form, clause (K1) of Premise \claimref{synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields}, in which its polarisation sum is $-a\cdot b$, of degree $0$ in $k$, and it is local as a commuting field (computed in (i)). Let the interaction density $\mathcal{L}$ be a sum of the monomials (i) below, and let the interacting field of a Wick polynomial $A$ be Bogoliubov's $A_{\mathrm{int}}(x) = \frac{\delta}{I_{4}\,\delta h(x)}S(\mathcal{L})^{-1}S(\mathcal{L} + hA)\big|_{h = 0}$ (the complex unit of the free fields' Fock space is the field theory's unit $I_{4}$, numbers read in $\mathrm{span}\{1, I_{4}\}$), a formal power series, with time-ordered products that are graded symmetric and preserve the Grassmann parity, factorise causally, satisfy the Wick expansion (the free-field condition (N3) of \cite{DutschFredenhagen1999}), and, as an assumption, are covariant under a representation $U$ of the covering group of the Poincar\'e group (\cite{DutschFredenhagen1999} state covariance, (N1), for the Poincar\'e group itself; Epstein and Glaser \cite{EpsteinGlaser1973}, Fact \claimref{synthesis.imported-epstein-glaser-extension-theorem-and-ward-preserving-time-ordered-products}; \cite{DutschFredenhagen1999}, (2.2), (2.3), (2.7)). Then:
\begin{enumerate}
\item[(i)] \emph{(The interaction density; computed.)} The rotor of the loop of four quarter turns in the plane $\gamma_{1}\gamma_{2}$ is $-1$: it fixes every vector and bivector value and negates every spinor value. The vector vertex $\langle\psi\gamma_{0}\tilde\psi A\rangle_{0}$, the axial vertex $\langle\psi\gamma_{3}\tilde\psi A\rangle_{0}$, the scalar and pseudoscalar Yukawa terms and mass insertions $\langle\psi\tilde\psi\rangle_{0}\phi$, $\langle\psi\tilde\psi I_{4}\rangle_{0}\phi$, the scalar gauge couplings, the quartic, the non-abelian cubic and quartic terms, the gauge fixing $\langle\nabla A\rangle_{0}^{2}$ and the ghost terms $\langle\nabla\bar c\,\nabla c\rangle_{0}$, $\langle\nabla\bar c\,A\rangle_{0}c$ are Lorentz scalars, each with an even number of spinor factors (so $U(2\pi)$ acts on $\mathcal{L}$ as $+1$) and with as many ghost as antighost factors; nothing depends on the number of scalar doublets. The free Feynman-gauge potential has the polarisation sum $-a\cdot b$, independent of $k$ and indefinite, and the bracket factor of the stored locality result vanishes for it as a commuting field.
\item[(ii)] \emph{(Wick monomials; proved.)} On a Wick monomial with $n_{\psi}$ spinor and $n_{c} + n_{\bar c}$ ghost factors, $U(2\pi)$ acts as $(-1)^{n_{\psi}}$ and the Grassmann parity is $(-1)^{n_{\psi} + n_{c} + n_{\bar c}}$; they agree if and only if $n_{c} + n_{\bar c}$ is even, in particular at ghost number zero, and two such monomials on disjoint modes anticommute exactly when both have $U(2\pi) = -1$.
\item[(iii)] \emph{(Interacting fields; proved given the imported axioms.)} Every order of $A_{\mathrm{int}}$ is a retarded product of copies of $\mathcal{L}$ with $A$; by parity preservation it has the Grassmann parity of $A$, and by covariance under the covering group its $2\pi$ eigenvalue is that of $A$; the interacting fields are graded-local with that parity (\cite{DutschFredenhagen1999}, Proposition 2, (2.25), for QED, where the ghosts do not couple; for a coupled ghost vertex, Yang-Mills, \cite{Hollands2008}, cited from memory), the first order following from the graded Jacobi identity for even $\mathcal{L}$ and the light-cone lemma of the proof. Hence, if the time-ordered products satisfy these conditions, then on every interacting field with an even number of ghost factors, in particular the interacting field of every Wick polynomial of ghost number zero, the statistics operator equals $U(2\pi)$ to every order: the spin-statistics connection holds in perturbation theory with no Jost-point or modular premise. Ghost fields of odd ghost count have the opposite sign, the Krein exception of the free-field result.
\item[(iv)] \emph{(What remains; argued.)} The statement concerns formal power series. Beyond perturbation theory a premise remains (the Jost point of Fact \claimref{field-theory.imported-standard-field-theory}, or a modular premise, \claimref{synthesis.wedge-reflections-compose-to-the-two-pi-rotor-so-geometric-modular-conjugations-give-interacting-spin-statistics}); for electrically charged fields the nonperturbative charge classes are localised in hypercones \cite{BuchholzRoberts2014}, where a spin-statistics theorem is not supplied by the sources read.
\end{enumerate}

## technical
The question is whether the spin-statistics connection of interacting fields needs the Jost-point theorem. In perturbation theory it does not. Interacting fields are built from the free fields by Bogoliubov's formula, each order a retarded product of the Wick polynomial with copies of the interaction density, and causal perturbation theory proves that interacting fields are graded-local with the free grading and covariant whenever the time-ordered products are (standard: Epstein-Glaser; Dütsch-Fredenhagen for QED with spinors and ghosts; Hollands for Yang-Mills). The conditions used are graded symmetry and parity preservation, causal factorisation, the Wick expansion and covariance under the covering group, the last assumed (the standard axiom is stated for the Poincar\'e group); the free potential in Feynman gauge is taken in its indefinite form, where it is local. The series' part is the bookkeeping on its own field list, done exactly in the spacetime algebra: the rotation by $2\pi$ is the rotor $-1$, which negates spinor values and fixes vector, bivector and scalar values; every monomial of the series' interaction (vector and axial vertices, Yukawa and mass insertions with any number of doublets, scalar and non-abelian gauge couplings, gauge fixing, ghost terms) is a Lorentz scalar with an even number of spinors and as many ghosts as antighosts. So an interacting field keeps both the Grassmann parity and the $2\pi$ eigenvalue of its Wick polynomial, and the two agree exactly when the number of ghost factors is even, in particular at ghost number zero. The first-order locality step reduces, by the graded Jacobi identity for an even interaction and a light-cone lemma, to free graded locality, checked exactly on the tower's CAR modes.

So the Jost import is needed only beyond perturbation theory, where a premise remains (the Jost point or a modular premise, \claimref{synthesis.wedge-reflections-compose-to-the-two-pi-rotor-so-geometric-modular-conjugations-give-interacting-spin-statistics}); electrically charged fields add an infrared obstacle there.

## lay
Particles of half-integer spin obey the exclusion rule and those of whole-number spin do not. For the series' free particles this tie was already derived; the question was whether it survives interactions. In the standard step-by-step construction of interacting fields, it does: each step combines the free fields with the interaction, and every term of the series' interaction contains matter fields in pairs, so turning a field by a full circle and exchanging two fields give the same sign before and after the interaction is switched on. The bookkeeping fields used to fix gauges are the one exception, as they were for free fields, and they always appear in pairs in anything physical. What the step-by-step construction does not give is a statement about the full theory beyond that expansion; there a deeper assumption is still needed.

## one-liner
If interacting fields are built by causal perturbation theory from the attached free fields (time-ordered products graded symmetric, parity preserving, causal, with the Wick expansion and covariant under the covering group; the Feynman-gauge potential in its indefinite form), then every series interaction monomial is a Lorentz scalar with even spinor and ghost counts, interacting fields keep the parity and $2\pi$ eigenvalue $(-1)^{n_{\psi}}$ of their Wick polynomials, and the grading equals $U(2\pi)$ to every order on fields of even ghost count, in particular at ghost number zero; the Jost import is needed only beyond perturbation theory.
