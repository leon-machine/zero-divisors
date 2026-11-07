---
id: one-relation.schr-odinger-slow-shadow
kind: claim
version: 8
title: Schrödinger as the slow shadow
status: proved
region: one-relation
subject: one-relation
tags:
- recovers-known-physics
- limits
- ledger-audit
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T16, deposited version
- name: Claude Opus 5.5
  role: 'GA rewrite (cross product in the Pauli identity)'
  version: 8
  source: maintainer pass 2026-11-07 (consistency)
review: typed
derivations:
- name: main
  uses:
  - one-relation.arrow-frequency-are-one-bit-level@4
  - one-relation.form-law-forced-square@3
  - one-relation.imported-flag-arrow-superselection@7
  - one-relation.imported-condensate-derived-content@3
  - one-relation.odd-square-roots-chiral-phase@5
  - one-relation.one-datum-not-two-imaginary-unit@3
  - one-relation.vector-derivative-covariant-first-order-operator@4
  - standard-model.hyp-s-slot-statistics@9
  - std-algebra.vector-squares@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T16.py
  tags:
  - label:prop:slowshadow
- kind: check
  ref: check.py::check_vector_derivative_is_covariant
- kind: check
  ref: check.py::check_klein_gordon_square
- kind: check
  ref: check.py::check_imaginary_unit_and_rest_frame_are_one_datum
- kind: check
  ref: check.py::check_pauli_identity
locators:
  paper: T16
  number: Prop 5.2
  label: prop:slowshadow
  line: 749
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The Pauli identity is written ab = a.b + a ^ b in Cl(3,0), the bivector a ^ b named as the bivector whose I_3-dual is the axial vector of vector algebra, instead of the I_3 times axial-vector form (the same identity); the vector derivative gamma^mu d_mu is the algebra''s own and stays; notation only.'
  maintainer_pass_2:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.vector-squares where the proof uses them. Version 6 -> 7.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: Lorentz matrices of six rotors; the Klein-Gordon square (C = gamma_0 gamma_1 gamma_2, C^2 = -1) and the plane-wave kernel of p psi = m psi gamma_0, dimension 4 on shell and 0 off it; the imaginary unit commutes with C and C J is the rest frame, boosts changing both together; Pauli identity on all basis pairs. Version 5 -> 6.'
  env: proposition
  context_refs:
  - one-relation.imported-condensate-derived-content
  typing:
    by: ai-typing-pass
    added:
    - one-relation.imported-condensate-derived-content
    - standard-model.hyp-s-slot-statistics
    note: 'Added the condensate Fact, the source of the mass and of the potential''s connection; the nonrelativistic
      descent (Pauli, Schroedinger) is standard and imported in the paper, but no such standard claim
      is in the store, so no standard-route derivation. Hypothesis pass: assumes standard-model.hyp-s-slot-statistics
      added because its statement holds under Hypothesis (S). Levels pass: the lay now names Hypothesis
      (S) for the orientation, the observation level of the mass''s source, the structural level, the
      two imports and the single-free-fermion scope; the one-liner keeps the structural and observation
      levels.'
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    cited:
    - one-relation.imported-condensate-derived-content
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
about:
- obj.mass.grip-mass-composite
---

## formal
The laboratory equation is the algebra's own first-order operator viewed from inside a rest frame. The chain, in four steps, with each input's provenance declared.
\begin{enumerate}
\item \emph{(The operator; proved.)} The first-order operator is the vector derivative $\nabla = \gamma^{\mu}\partial_{\mu}$, unique up to an invertible constant factor among covariant constant-coefficient first-order operators acting by left multiplication (Lemma \claimref{one-relation.vector-derivative-covariant-first-order-operator}): native to the Clifford presentation, no postulate.
\item \emph{(The mass comes from the condensate; sourced. The form of the law; forced, given first order.)} The equation of motion is the Dirac-Hestenes equation $\nabla\psi\, I\sigma_{3} = m\,\psi\gamma_{0}$, Hestenes' real form of the Dirac equation \cite{Hestenes1967, Hestenes1975}. What is imported is one sentence, that the law is first order, Dirac's factorisation of the mass shell; the form is then forced: a first-order covariant law $\nabla\psi = m\psi C$ with constant right factor squares to Klein-Gordon at mass $m$ iff $C^{2} = -1$ (Lemma \claimref{one-relation.form-law-forced-square}), and every odd such $C$ is the Dirac-Hestenes factor up to the representation freedom and a constant chiral phase, the latter a field redefinition for the single free minimally coupled fermion treated here (Lemma \claimref{one-relation.odd-square-roots-chiral-phase}). Its mass parameter is the mass of Fact \claimref{one-relation.imported-condensate-derived-content}: applying $\nabla$ twice gives $\nabla^{2}\psi = -m^{2}\psi$, so every component of a solution is a Klein-Gordon field $(\Box + m^{2})\psi = 0$ of the same $m$, which is the quantity the mass-weight dictionary quantifies as the composite's grip on the frozen point. That $\Lambda \neq 0$ makes condensation unavoidable is the families paper's observation-level reading (Fact \claimref{one-relation.imported-condensate-derived-content}); the mass term is therefore sourced at the level of that reading and of the dictionary, and no higher.
\item \emph{(The imaginary unit is the rest frame read through the law; one datum, proved. The time orientation is the flag; sourced under Hypothesis (S). The rest frame is not sourced.)} In Hestenes' form the unit imaginary is the bivector $I\sigma_{3} = \gamma_{2}\gamma_{1}$, a spacelike plane in the rest space of $\gamma_{0}$, which squares to $-1$ and commutes with $\gamma_{0}$; it is not the boost plane, which squares to $+1$. Given the law, the complex structures the descent can use are the even $J$ with $J^{2} = -1$ commuting with the right factor, and $J \mapsto \gamma_{0} = CJ$ is a bijection between them and the unit timelike vectors orthogonal to the law's spacelike datum: choosing the imaginary unit and choosing the rest frame are one choice (Lemma \claimref{one-relation.one-datum-not-two-imaginary-unit}), so the imaginary unit is not a third postulate to be imported. The pair $(\gamma_{0}, I\sigma_{3})$ on the right of the equation is fixed only up to the representation freedom $\psi \mapsto \psi R$ for constant rotors $R$, which Hestenes identifies as physically empty and which Lemma \claimref{one-relation.one-datum-not-two-imaginary-unit} uses up once, to align the law's datum with the laboratory; the residual freedom is the $U(1)$ of the spin plane, the electromagnetic phase. What the series fixes is therefore not the plane and not the frame vector $\gamma_{0}$ but a single bit: the particle-antiparticle orientation, which is the sign convention separating positive-frequency from negative-frequency solutions, and which Fact \claimref{one-relation.imported-flag-arrow-superselection} identifies with the arrow of time and argues to be initial data under three premises, one of them the open Hypothesis (S); the orientation is sourced under (S) and not otherwise. The \emph{rest frame} of the nonrelativistic limit, the choice of which timelike $\gamma_{0}$ the laboratory is at rest in, is the laboratory's own, and nothing in this series selects it: the frozen point is de Sitter-invariant and singles out no time direction, and since the law fixes only $C$ of the triangle $(C, J, \gamma_{0})$, any theorem selecting $\gamma_{0}$ would break that invariance; the frame is state data or observer data, never law data. Given the law, the frequency sign and the direction of the frame's time are one bit, not two (Corollary \claimref{one-relation.arrow-frequency-are-one-bit-level}).
\item \emph{(The nonrelativistic descent; imported.)} For excitations near the mass gap, factor the rest phase $\psi = \varphi\exp(-I\sigma_{3}mt)$ in the laboratory's frame and expand in $|\mathbf{p}|/m$: at first order the Pauli equation, with the gyromagnetic ratio $g = 2$ automatic, an inherited check passed; suppressing the spin sector, the Schr\"odinger equation in a potential, the potential entering as the electrostatic component of the one gauge connection by minimal coupling, which is, on the Standard-Model paper's observation-level reading of its forced connection, a holonomy constraint rather than an ansatz (Fact \claimref{one-relation.imported-condensate-derived-content}). The algebraic input of the $g = 2$ step is the Pauli identity $\mathbf{a}\mathbf{b} = \mathbf{a}\cdot\mathbf{b} + \mathbf{a}\wedge\mathbf{b}$ in the rest space $\Cl(3,0)$, whose antisymmetric part, the bivector $\mathbf{a}\wedge\mathbf{b}$ (whose $I_{3}$-dual is the axial vector of vector algebra), is what doubles the spin coupling relative to the orbital one.
\end{enumerate}
Structural level: the nonrelativistic descent in step (4) is the standard one and is imported as such, and first-orderness is the one dynamical import; the framework's contribution is that of the three postulated inputs, the mass is fixed by the condensate at its Fact's level, the orientation half of the time split is fixed by the flag under Hypothesis (S) with the arrow-equals-frequency identification proved at $\Cl(1,3)$ level, the imaginary unit is carried by the rest frame and is not a separate input, and the rest frame is declared unsourced: of three postulates, one is sourced, one is half sourced, and the third was not a postulate. Nonrelativistic quantum mechanics is the Dirac shadow of the frozen phase, seen slowly, from a frame the laboratory supplies.

## technical
The laboratory equation is the algebra's first-order operator viewed from a rest frame, in four steps. (1) The vector derivative $\nabla = \gamma^{\mu}\partial_{\mu}$ is the unique covariant first-order operator up to an invertible constant. (2) Importing only that the law is first order, its form is forced to the Dirac-Hestenes equation $\nabla\psi\, I\sigma_{3} = m\,\psi\gamma_{0}$ for the single free minimally coupled fermion, and its mass is the condensate's mass at the level of the imported reading, since $\nabla^{2}\psi = -m^{2}\psi$. (3) The imaginary unit $I\sigma_{3}$ is the rest frame read through the law, the frequency sign and time direction are one bit sourced by the flag under Hypothesis (S), and the rest frame itself is unsourced. (4) The standard nonrelativistic descent, imported, gives the Pauli equation with $g = 2$ and then the Schr\"odinger equation in a potential.

Of the three postulated inputs (mass, time split, imaginary unit), one is sourced, one is half sourced, and the third was not a separate postulate. The level is structural, with first-orderness the one dynamical import.

## lay
The everyday equation of quantum mechanics, Schr\"odinger's, is shown to be the slow-motion limit of the relativistic electron equation, which is itself built from the basic algebra of spacetime. The paper tracks where each ingredient comes from, at a structural level: the mass from an earlier mechanism, at the observation level that mechanism's reading holds; the orientation half of the direction of time from an earlier argument that holds if the slots behave like the pairs (Hypothesis (S)); and the imaginary unit from the choice of rest frame. Only the first-order form of the law and the standard slow-motion expansion are imported, for a single free fermion. The rest frame itself is supplied by the laboratory, not derived.

## one-liner
Nonrelativistic quantum mechanics is the slow limit of the Dirac-Hestenes equation, at structural level, with the operator forced, the mass sourced by the condensate at its reading's observation level, the time orientation sourced under Hypothesis (S), the imaginary unit tied to the rest frame, and the rest frame unsourced.
