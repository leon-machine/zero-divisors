---
id: synthesis.self-adjoint-brst-charge-needs-a-krein-form-and-the-tower-supplies-the-ghosts
kind: claim
version: 3
title: 'A self-adjoint BRST charge needs a Krein form; the tower supplies the ghosts'
status: proved
region: synthesis
subject: quantum-fields
tags: [gauge-fields, car-algebra, no-go, recovers-known-physics]
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
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
review: draft
about:
- obj.field-theory.single-algebra-field
derivations:
- name: main
  uses:
  - field-theory.imported-tower-limit@3
  - field-theory.imported-statistics-no-go-palatial-algebra@2
  - field-theory.fock-space-maxwell-modes@4
  - standard-model.gauge-algebra-minimal-massive-composite@4
  - field-theory.twistor-attachment@6
  - field-theory.path-integral-inside-tower@3
  - synthesis.positive-structure-is-twistor-form-at-imaginary-time@3
  - synthesis.imported-brst-kugo-ojima-strocchi-and-gribov@1
  assumes:
  - synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_positive_forms_carry_no_self_adjoint_nilpotent
- kind: check
  ref: check.py::check_krein_brst_nilpotent_and_self_adjoint
- kind: check
  ref: check.py::check_cohomology_is_transverse_and_positive
- kind: check
  ref: check.py::check_cohomology_matches_the_photon_modes
- kind: check
  ref: check.py::check_derived_algebra_ghost_charge_is_nilpotent
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - field-theory.fock-space-maxwell-modes
  - field-theory.path-integral-inside-tower
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'By Leon''s ruling R3 (7 November 2026): the matter representation C^2 tensor C^3 of clause (v) is read over span{1, I_4}, on the tower''s floors where I_4 commutes with the tower vectors (stated once at the formal level; notational); the detector''s other hit is the index in ''mu = i''; no bare i remains, so no declaration.'
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 1 -> 2, by Leon''s decisions of 2026-11-01: an assumes edge to the Krein-form premise synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields@1, which this result states as the hypothesis of its reading (the gauge fields carry the indefinite form; now cited by claimref at every level that names it and in the proof); a uses edge to the imported Fact synthesis.imported-brst-kugo-ojima-strocchi-and-gribov@1 (BRST, Kugo-Ojima, Strocchi, Gribov), which replaces the citations from memory; the pin of field-theory.twistor-attachment moves to @6 (a marked spin-statistics note added there, content unchanged). Clause (i) and the computations (ii) to (v) unchanged.'
  open_problem: op.qft-non-abelian-gauge-fields
  note: >-
    Answers the problem's first attack line (gauge fixing and BRST in geometric algebra) in part. The
    store's representations carry positive forms, on which a self-adjoint nilpotent operator vanishes, so a
    self-adjoint BRST charge (the Kugo-Ojima framework) needs an indefinite inner product. Non-self-adjoint
    nilpotent charges on positive spaces exist, so the clause is about self-adjoint charges only; the general
    need for an indefinite metric for a local covariant vector potential is Strocchi's theorem (imported,
    synthesis.imported-brst-kugo-ojima-strocchi-and-gribov). The indefinite form used is the standard Gupta-Bleuler form, the
    Minkowski metric of the polarisations, the same in any formalism. With it and a pair of tower modes as
    ghosts, the free BRST charge at a null momentum is nilpotent and self-adjoint, and its cohomology is
    positive and equals the stored photon mode space; the constraint part of the non-abelian charge, standard
    for any Lie algebra, is nilpotent for the derived algebra on tower ghosts. BRST (Becchi, Rouet, Stora;
    Tyutin), the Kugo-Ojima quartet mechanism (Prog. Theor. Phys. Suppl. 66, 1979) and the Gribov ambiguity
    of non-abelian Coulomb gauge are the standard frame, imported in the same Fact; the results are recomputed
    exactly. The interacting field-level charge and confinement are not addressed; the sign of the beta
    coefficients is computed in synthesis.one-loop-running-coefficients-from-spacetime-algebra-spin-traces. Transport-absent (standard BRST structure), with
    the identification of the cohomology with the bivector modes transport-convenient.
---

## formal
Units and signature of the store; $k$ a null vector, $Q(k) = 0$. Polarisation modes $a_\mu = \partial/\partial z_\mu$ on the palatial polynomial representation (Fact \claimref{field-theory.imported-statistics-no-go-palatial-algebra}) with its positive form $\langle z^n, z^m\rangle = n!\,\delta_{nm}$; ghost modes $b, d$ on two tower planes with the CAR of Fact \claimref{field-theory.imported-tower-limit} and the floor's positive trace form.
\begin{enumerate}
\item[(i)] \emph{(A self-adjoint BRST charge needs an indefinite form; proved.)} On a space with a positive-definite form an operator $Q$ with $Q^{*} = Q$ and $Q^2 = 0$ is zero. The tower's trace form ($\langle x^{*}y\rangle_0$, the basis blades orthonormal) and the palatial form are positive definite, so a nonzero nilpotent charge is not self-adjoint for either, and the self-adjoint BRST charge of the Kugo-Ojima framework does not exist on them. Nilpotent charges that are not self-adjoint do exist on positive spaces; that a local covariant vector potential needs an indefinite metric in general is Strocchi's theorem (Fact \claimref{synthesis.imported-brst-kugo-ojima-strocchi-and-gribov}(iii)), not proved here.
\item[(ii)] \emph{(Gupta-Bleuler BRST at a null momentum; proved.)} Let $\eta = (-1)^{n_0} \otimes S$, with $S = 1 - (b^{*} - d^{*})(b - d)$ the inner involution of the ghost floor exchanging $b$ and $d$, and $\langle x, y\rangle_K = \langle x, \eta y\rangle$. Then $a_\mu^{\dagger} = -g_{\mu\mu}z_\mu$ and $b^{\dagger} = d^{*}$, so $[a(u), a(w)^{\dagger}] = -u\cdot w$ for polarisation vectors $u, w$: the one-particle Krein form is the Minkowski metric of the polarisations, the standard Gupta-Bleuler form, invariant under boost rotors (the positive form is not). With $L = \sum_\mu g_{\mu\mu}k^\mu a_\mu$, $Q = L^{\dagger}b + d^{*}L$ satisfies $Q^2 = 0$ and $Q^{\dagger} = Q$.
\item[(iii)] \emph{(Positive cohomology; computed up to three quanta.)} $Q$ preserves the total number $T$ (bosons plus ghosts). At ghost number $N_d - N_b = 0$ and $T = 0, 1, 2, 3$ the cohomology of $Q$ has dimensions $1, 2, 3, 4$, those of the symmetric powers of a two-dimensional space, and the Krein form restricted to $\ker Q$ has signature $(\dim H, 0, \dim \operatorname{im} Q)$: positive definite on the cohomology, with radical $\operatorname{im} Q$.
\item[(iv)] \emph{(The physical modes are the stored photon modes; proved.)} The one-particle cohomology is $k^{\perp}/\mathrm{span}\{k\}$, and $\epsilon \mapsto k\epsilon$ maps it isomorphically onto the bivectors $\{f : kf = 0\}$, the mode space of Proposition \claimref{field-theory.fock-space-maxwell-modes}(2).
\item[(v)] \emph{(The constraint charge of the derived algebra on tower ghosts; proved, standard for any Lie algebra.)} For the derived gauge algebra $\mathfrak{su}(2) \oplus \mathfrak{su}(3) \oplus \mathfrak{u}(1)$ of Theorem \claimref{standard-model.gauge-algebra-minimal-massive-composite} acting on the finite-dimensional matter representation $\C^{2} \otimes \C^{3}$ (numbers and the module's complex structure are read in $\mathrm{span}\{1, I_{4}\}$, the module read on the tower's floors, where $I_{4}$ commutes with the tower vectors), with ghosts $c^a$ and antighosts $\bar c_a$ the creation and annihilation operators of twelve tower planes, the charge $Q = c^aT_a - \tfrac12 f_{ab}{}^{c}\,c^ac^b\bar c_c$ satisfies $Q^2 = 0$; without the cubic ghost term $Q^2 \neq 0$, and changing one structure constant gives $Q^2 \neq 0$.
\end{enumerate}
\emph{Reading.} A self-adjoint BRST charge for the series' gauge fields needs an indefinite form, which the store's representations lack; the Gupta-Bleuler form of the polarisations supplies it in a Lorentz-invariant way, and under the premise that gauge fields carry this indefinite form, Premise \claimref{synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields}, the covariant route works at the free level with positive physical states. An indefinite form is already present at the one-particle level of the attachment: the conformal-group-invariant twistor form of signature $(2,2)$, whose positive polarisations alone carry states (Theorem \claimref{synthesis.positive-structure-is-twistor-form-at-imaginary-time}); this is a parallel, not the form used here. The ghosts are tower modes, as the Grassmann variables of Proposition \claimref{field-theory.path-integral-inside-tower} are rungs; they are scalar CAR modes, which the spin-statistics clause of Proposition \claimref{field-theory.twistor-attachment} excludes as local fields with positive weights, and which are local only with antiparticle weight $-1$, that is in the indefinite form (\claimref{synthesis.locality-of-the-attached-free-fields-fixes-their-statistics}); they appear only in zero-norm quartets. The sign of the one-loop beta coefficients of the non-abelian factors is computed in a result (\claimref{synthesis.one-loop-running-coefficients-from-spacetime-algebra-spin-traces}).

## technical
The store quantises the photon in Coulomb gauge on a positive polynomial representation, and the tower's floors carry a positive trace form. The covariant route to non-abelian gauge fields in the Kugo-Ojima form needs a nilpotent self-adjoint BRST charge, and on a positive-definite space $\langle Qx, Qx\rangle = \langle x, Q^2x\rangle = 0$ forces $Q = 0$. So, assuming the store's positive forms, that route cannot be taken on the store's representations as they stand; it needs an indefinite (Krein) form. Nilpotent charges that are not self-adjoint exist on positive spaces, so this is a statement about self-adjoint charges; the general need for an indefinite metric for a local covariant vector potential is Strocchi's theorem (\claimref{synthesis.imported-brst-kugo-ojima-strocchi-and-gribov}), not proved here.

The Minkowski metric of the polarisations offers one, the standard Gupta-Bleuler form. Give the polynomial representation the form twisted by $(-1)^{n_0}$ and the ghost floor the twist by the involution exchanging its two modes: the polarisation modes then obey $[a(u), a(w)^{\dagger}] = -u\cdot w$, which is boost-invariant, while the positive form singles out a frame. The free BRST charge at a null momentum, $Q = L^{\dagger}b + d^{*}L$ with $L = k\cdot a$, is nilpotent because $k$ is null and the ghosts anticommute, and self-adjoint for the Krein form. Its cohomology at ghost number zero, computed exactly with up to three quanta for two null momenta, is the symmetric algebra of a two-dimensional space with a positive-definite form: the transverse polarisations, which $\epsilon \mapsto k\epsilon$ identifies with the stored photon's bivector modes $\{f : kf = 0\}$.

For the derived gauge algebra, twelve tower planes carry the ghosts and antighosts, and the constraint charge $c^aT_a - \tfrac12 f_{ab}{}^{c}c^ac^b\bar c_c$ on the matter representation $\C^{2} \otimes \C^{3}$ squares to zero exactly, the cubic ghost term being forced by non-commutativity; this holds for any Lie algebra and is standard. The interacting field-level charge (with the covariant derivative of the ghost acting on the gauge field) and confinement are not computed here; the sign of the beta coefficients is computed in \claimref{synthesis.one-loop-running-coefficients-from-spacetime-algebra-spin-traces}.

## lay
Quantising force fields like the gluons in a way that respects relativity needs a way of removing their unphysical parts. The standard way introduces fictitious particles (ghosts) and an accounting operator that, in its usual form, only works if some states are allowed negative norm. The series' quantum spaces all have positive norms, and a short argument shows that this usual form of the accounting cannot exist on them. The standard remedy, an indefinite measure built from the spacetime metric of the force field's polarisations, works with ghosts taken from the tower's fermion modes: for a single light-like momentum the surviving states are the two transverse polarisations, the same states the series already uses for the photon, and for the series' gauge group the ghosts' accounting closes exactly. The indefinite measure is a premise for the series, not something it derives, and the series' covariant treatment of force fields holds under it.

## one-liner
A nonzero self-adjoint (Kugo-Ojima) BRST charge cannot exist on the positive forms of the tower and the palatial polynomials; with the standard Gupta-Bleuler form $[a(u), a(w)^{\dagger}] = -u\cdot w$ and a tower ghost pair the charge at a null $k$ is nilpotent and self-adjoint with positive cohomology (dimensions $1, 2, 3, 4$ up to three quanta) whose one-particle space is $\{f : kf = 0\}$, and for $\mathfrak{su}(2) \oplus \mathfrak{su}(3) \oplus \mathfrak{u}(1)$ the standard constraint charge on twelve tower ghost pairs squares to zero only with its cubic term; under the Krein-form premise this is the series' covariant gauge fixing at the free level; transport-absent.
