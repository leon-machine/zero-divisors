---
id: synthesis.modular-period-on-values-is-the-dual-plane-turn
kind: claim
version: 2
title: 'The modular period on values is the dual-plane turn'
status: proved
region: synthesis
subject: quantum-fields
tags: [modular-theory, car-algebra, thermal-premises, no-go, recovers-known-physics]
proposed_by:
  kind: ai
  session: 2026-11-01-qft
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
  - field-theory.second-quantisation@5
  - field-theory.where-each-lives@3
  - field-theory.boost-modes@3
  - hawking.modular-structure-completed-pair@3
  - synthesis.local-boost-temperature-is-local-regularity@3
  - synthesis.boost-evolution-on-generators-is-one-unitary-group@2
  - singularity.euclidean-rotor-where-it-lies@4
  - synthesis.imported-free-field-spin-statistics-and-guido-longo-theorem@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_dual_plane_identity
- kind: check
  ref: check.py::check_sign_over_one_modular_period
- kind: check
  ref: check.py::check_kms_period_is_statistics_blind
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - field-theory.imported-standard-field-theory
  - synthesis.boost-evolution-on-generators-is-one-unitary-group
extraction:
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 1 -> 2, by Leon''s list of imports of 2026-11-01: a uses edge to the imported Fact synthesis.imported-free-field-spin-statistics-and-guido-longo-theorem@1 (the Guido-Longo theorem, Thm 2.11 of arXiv:funct-an/9406005), which replaces the in-text citation; the pin of singularity.euclidean-rotor-where-it-lies moves to @4 (a marked wording note on its clause (3) recording this result''s reading on values; content unchanged). Statement and check unchanged.'
  open_problem: op.qft-structural-inputs
  note: >-
    The problem's spin-statistics input, attacked from outside the series: the modular spin-statistics theorem
    of Guido and Longo (Commun. Math. Phys. 172, 1995, arXiv funct-an/9406005, imported in
    synthesis.imported-free-field-spin-statistics-and-guido-longo-theorem: for a
    modular covariant field net with the Reeh-Schlieder property and normal Bose/Fermi commutation relations,
    the field-net theorem of Section 2, Thm 2.11, gives Gamma = U(2 pi); modular covariance is a primitive assumption, positive energy is
    derived). The series' contribution is the reading with i = I4: the continued boost rotor on even values is
    a real rotor of the dual plane, the angular plane I sigma_r of the stored Euclidean-rotor result, so the
    KMS period and the 2 pi rotation are one element on values (and not on points, where I4 anticommutes with
    vectors). The KMS period alone is statistics-blind (exact, one CAR and one CCR mode). Bisognano-Wichmann
    (memory: J. Math. Phys. 16 (1975) 985 and 17 (1976) 303) is not used as a premise, since its proof starts
    from Wightman fields with the normal commutation relations; using it would be circular. Standard content
    (complexified Lorentz algebra: the boost generator is +-i times the rotation generator on the chiral
    spinors) re-derived in the formalism. Transport-absent; the i = I4 reading is the only series-specific
    content.
---

## formal
Work in $\Cl(1,3)$ with the store's signature, $I_{4} = e_{0}e_{1}e_{2}e_{3}$, and the field theory's unit $i = I_{4}$ (Proposition \claimref{field-theory.second-quantisation}(4)), central in the even subalgebra $\Cl^{+}(1,3)$ (Proposition \claimref{field-theory.where-each-lives}(1)). Let $B$ be a unit timelike plane, $B^{2} = 1$, the plane of a wedge's boost, with boost rotor $S(\lambda) = \exp(-\lambda B/2)$.
\begin{enumerate}
\item[(i)] \emph{(The dual plane.)} $B^{*} = I_{4}B$ is a unit spacelike 2-blade, $(B^{*})^{2} = -1$, commuting with $B$ and with $I_{4}$; it commutes with the vectors of $B$ and anticommutes with those of $B^{*}$. Continued to complex rapidity $\lambda + I_{4}\theta$, $S(\lambda + I_{4}\theta) = S(\lambda)R(\theta)$ with $R(\theta) = \exp(-\theta B^{*}/2) = \cos\tfrac{\theta}{2} - B^{*}\sin\tfrac{\theta}{2}$, the real rotor of the dual plane.
\item[(ii)] \emph{(One period and half a period on values.)} $R(2\pi) = -1$ and $R(4\pi) = 1$: over one modular period the continued boost multiplies every even element (a spinor value, left action) by $-1$ and fixes every bivector and scalar value (conjugation), and a bivector built from a spinor, $\psi F_{0}\tilde\psi$, returns to itself; on a value carrying $2s$ spinor factors the factor is $(-1)^{2s}$. $R(\pi) = -B^{*}$, whose conjugation fixes the vectors of $B$ and reverses those of $B^{*}$: the turn by $\pi$ of the dual plane. On points the continuation is not this rotor, since $I_{4}$ anticommutes with vectors; on values it is. On vector arguments the complexified boost at half the period reverses the vectors of $B$ and fixes those of $B^{*}$, so it differs from the dual turn by the total inversion $x \mapsto -x$.
\item[(iii)] \emph{(The period is statistics-blind.)} For a single mode with weight $w$ under a phase flow and $x = e^{-2\pi w}$, the Gibbs state of a CAR mode (the completed pair of Proposition \claimref{hawking.modular-structure-completed-pair}) and that of a CCR mode both satisfy the KMS relation at rapidity period $2\pi$, $\omega(a^{*}a) = x\,\omega(aa^{*})$, with occupations $x/(1 + x)$ and $x/(1 - x)$. So (R$_{\mathrm{loc}}$) of Theorem \claimref{synthesis.local-boost-temperature-is-local-regularity}, stated for a quasi-free phase flow on CAR windows, takes the statistics as given and cannot supply them.
\item[(iv)] \emph{(Under modular covariance, through an imported theorem.)} If the vacuum's modular group of each wedge algebra of a field net is the wedge's boost at rapidity $-2\pi t$ acting covariantly on values (modular covariance), and the net has the Reeh-Schlieder property and normal Bose or Fermi commutation relations with grading $\Gamma$, then $\Gamma = U(2\pi)$ (Guido and Longo, the field-net theorem of Section 2, Thm 2.11, imported: Fact \claimref{synthesis.imported-free-field-spin-statistics-and-guido-longo-theorem}(iii)). $U(2\pi)$ acts as $(-1)^{2s}$ on spin-$s$ values by representation theory alone, so under modular covariance the fields of odd $2s$ are odd and anticommute and those of even $2s$ commute; (i) and (ii) only re-express $U(2\pi)$ as the continued wedge boost over one modular period and are not needed for this conclusion. Under that premise the spin-statistics input of Fact \claimref{field-theory.imported-standard-field-theory} can be traded for modular covariance of the wedge algebras; modular covariance is not a premise of the store. For the attached free fields the statistics follow instead from locality with a positive norm (\claimref{synthesis.locality-of-the-attached-free-fields-fixes-their-statistics}).
\end{enumerate}

## technical
With the field theory's unit $i = I_{4}$, which commutes with every even element, a boost rotor $\exp(-\lambda B/2)$ continued to imaginary rapidity $I_{4}\theta$ is $\exp(-\theta I_{4}B/2)$, and $I_{4}B = B^{*}$ is the unit spacelike plane dual to $B$. So on values the continuation is a real rotation of the dual plane: one full modular period $2\pi$ is the rotation by $2\pi$, which is $-1$ on spinor values and $+1$ on bivector and scalar values, $(-1)^{2s}$ in general, and half a period is the turn by $\pi$ of the dual plane, the rotation in the Bisognano-Wichmann form of the modular conjugation. On points the continuation is no real rotor, as stored for the Euclidean rotor at the bifurcation sphere; on vector arguments the half period is the dual turn composed with the total inversion.

The KMS condition at period $2\pi$ is satisfied by a fermionic and a bosonic mode alike, so the stored local premise (R$_{\mathrm{loc}}$), which is stated on CAR windows, takes the statistics as given. Modular covariance of the wedge algebras with the boost acting on values would fix them: the imported theorem of Guido and Longo gives that the statistics grading is the rotation by $2\pi$, which is $(-1)^{2s}$ by representation theory and which the dual-plane form re-expresses as the continued boost over one modular period. The field theory's spin-statistics input could be traded for that premise, which the store does not adopt; it is not derived from the stored premises. For the attached free fields, locality with a positive norm fixes the statistics directly (\claimref{synthesis.locality-of-the-attached-free-fields-fixes-their-statistics}).

## lay
In this framework the imaginary unit of quantum theory is the four-dimensional volume element of spacetime. With that choice, letting a boost run for an imaginary amount, as one does to describe thermal states, turns into an ordinary rotation of the plane at right angles to the boost, as far as the values of fields are concerned. One full thermal period is then a full turn, which flips the sign of a fermion and leaves a boson unchanged.

The thermal condition alone does not care whether a particle is a fermion or a boson. What links spin to statistics is the stronger assumption that the vacuum's thermal flow in every wedge is the geometric boost, acting on the fields' values; a known theorem then gives the usual link. So the link could be traded for that assumption, but the framework's present assumptions do not supply it; for free fields a separate argument from locality does.

## one-liner
With $i = I_{4}$ the continued wedge boost on even values is the real rotor of the dual plane $I_{4}B$, so one modular period is $(-1)^{2s}$ and half a period the turn by $\pi$; KMS at $2\pi$ holds for CAR and CCR modes alike, so (R$_{\mathrm{loc}}$) does not fix statistics; they follow under modular covariance (not a store premise) via an imported theorem, the dual-plane form only re-expressing the representation-theoretic $(-1)^{2s}$.
