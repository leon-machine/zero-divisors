---
id: synthesis.neutral-singlet-bit-decided-by-gauge-algebra-leaving-u5
kind: claim
version: 2
title: 'A gauge algebra decides the neutral-singlet bit exactly when it leaves $\uu(5)$'
status: proved
region: synthesis
subject: standard-model
tags: [hypotheses-s-r-c, spinor-modules, hypercharge-and-anomalies, chirality]
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
  - standard-model.hyp-s-slot-statistics@9
  - synthesis.cpt-closure-forces-slot-module-and-chirality@1
  - synthesis.spin10-clause-content-is-the-neutral-singlet-choice@2
  - standard-model.invariant-pairing-five-modes@5
  - standard-model.automorphisms-preserve-slot-pair-split-are@6
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_hypercharge_grading_splits_so10
- kind: check
  ref: check.py::check_swapped_halving_fails_on_every_element_of_p
- kind: check
  ref: check.py::check_neutral_block_fixed_by_one_pair_of_p
- kind: check
  ref: check.py::check_intermediate_gauge_algebras
- kind: check
  ref: check.py::check_yukawa_forms_see_the_bit
- kind: check
  ref: check.py::check_clifford_cpt_antiunitary_is_blind
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.spin10-clause-content-is-the-neutral-singlet-choice
  - standard-model.slot-module-hypothesis
  - standard-model.chain
extraction:
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Version 2, wording only: the closing sentence now names the grading form as the earlier version of the chirality clause and the Pati-Salam form as its current version (version 4 of the slot-module premise), and makes explicit that the equivalence uses anomaly freedom, as (iii) assumes. Mathematics unchanged.'
  open_problem: op.hypothesis-s
  note: >-
    The problem's third line of attack (structure outside the gauge quantum numbers that sees the neutral
    singlets). The stored ladder tested only the Standard Model gauge algebra, u(5) and so(10); the
    intermediate algebras, among them the Pati-Salam stage of the stored chain, were not tested. Result:
    a dichotomy. Hypercharge grades so(10) with disjoint eigenvalue sets on u(5) and on the pair-creation
    and pair-annihilation parts, so any algebra containing the Standard Model either lies in u(5), and then
    the vacuum-swapped halving commutes with it, or contains one pair-creation element and its adjoint,
    and then that pair alone, with the stored anomaly-free charged chirality, fixes the halving to
    (-1)^N up to the overall label, without number conservation. Pati-Salam (the split-preserving 21),
    left-right, su(4) x su(2)_L x u(1) and flipped u(5) decide the bit; Georgi-Glashow u(5), and the
    Standard Model with B - L or with the total mode number, do not. Two further sightings: the stored
    Yukawa pairing (the 10, 120 and 126 forms are odd-grade Clifford elements) couples the swapped half's
    neutral singlet to nothing else in its half, so the rung coupling then gives no Dirac neutrino
    coupling (only a grade-four element links it to the lepton doublet); and the Clifford CPT antiunitary
    (a Majorana product times complex conjugation, the five-mode analogue of the stored pseudoscalar-rotor
    form) commutes with the swap and reverses both candidates, so it is blind to the bit. Reading: the
    grading clause is equivalent, given the other clauses, to the chirality commuting with any gauge
    algebra that leaves u(5), for instance the Pati-Salam algebra of the stored chain; since the chain is
    itself stated under (S), this is an exchange of the clause for structure the series registers, not a
    derivation of it. See \claimref{synthesis.slot-module-light-ray-arrays-are-weyl-components}: the
    light-ray array count is sixteen per generation for every halving, so the light-ray chirality channels
    are blind to the bit. See \claimref{synthesis.georgi-jarlskog-is-rung-vector-times-pair-part-of-majorana-square}
    and synthesis.up-down-split-under-conjugate-reading-needs-su2r-odd-weighting: their Dirac-neutrino clauses
    use the halving (-1)^N that (iii) shows the Pati-Salam stage forces. In the restated slot-module premise the
    grading clause reads: the chirality commutes with the Pati-Salam algebra of the chain; by (iii), given the
    other clauses, that form and the grading form are equivalent. Transport-absent in content (finite
    Clifford algebra on the series' module).
---

## formal
Let $V = \Lambda^{\bullet}\C^{5}$ be the five-mode module of Theorem \claimref{standard-model.hyp-s-slot-statistics}, modes $1, 2$ the slots and $3, 4, 5$ the pairs, $N$ the total mode number, $Y = (3n - 2k)/6$, $\Omega$ the empty and $\Omega^{\top}$ the full state. Let $\so(10)$ be the span of all bilinears, $\uu(5)$ that of the number-conserving ones $a^{\dagger}_{i}a_{j}$, and $\mathfrak{p}$ that of the pair-creation and pair-annihilation bilinears $a^{\dagger}_{i}a^{\dagger}_{j}$, $a_{i}a_{j}$, so $\so(10) = \uu(5) \oplus \mathfrak{p}$. Let $\Gamma' = (-1)^{N} - 2P_{\Omega} + 2P_{\Omega^{\top}}$ be the vacuum-swapped halving of Theorem \claimref{synthesis.spin10-clause-content-is-the-neutral-singlet-choice}, and call a gauge-commuting CPT halving anomaly-free when it agrees with $\pm(-1)^{N}$ on the charged states (Theorem \claimref{synthesis.cpt-closure-forces-slot-module-and-chirality}(4)).
\begin{enumerate}
\item[(i)] \emph{(Hypercharge grading.)} $\mathrm{ad}\,Y$ is diagonal on the bilinear basis with eigenvalues $\{0, \pm\tfrac56\}$ on $\uu(5)$, $\{1, \tfrac16, -\tfrac23\}$ on pair creation and $\{-1, -\tfrac16, \tfrac23\}$ on pair annihilation, three disjoint sets. Hence every subspace $\mathfrak{g} \subseteq \so(10)$ stable under $\mathrm{ad}\,Y$ is $(\mathfrak{g} \cap \uu(5)) \oplus (\mathfrak{g} \cap \mathfrak{p})$, and $\mathfrak{g} \cap \mathfrak{p}$ is spanned by pure creation and pure annihilation elements.
\item[(ii)] \emph{(One pair decides.)} $(-1)^{N}$ commutes with $\so(10)$; $\Gamma'$ commutes with $\uu(5)$, and $x \mapsto [\Gamma', x]$ is injective on $\mathfrak{p}$. For an involution equal to $s(-1)^{N}$ ($s = \pm1$) on the charged states and arbitrary on the neutral block, commuting with one nonzero pure creation element $x \in \mathfrak{p}$ forces $\Gamma\Omega^{\top} = -s\Omega^{\top}$ and $\Gamma\Omega \in s\Omega + \C\Omega^{\top}$, and commuting with $x$ and $x^{\dagger}$ forces $\Gamma = s(-1)^{N}$.
\item[(iii)] \emph{(Dichotomy.)} Let $\mathfrak{g}$ be closed under adjoints with $\mathfrak{s}(\uu(2) \oplus \uu(3)) \subseteq \mathfrak{g} \subseteq \so(10)$. If $\mathfrak{g} \subseteq \uu(5)$, the vacuum-swapped halving commutes with $\mathfrak{g}$ and the bit is free. If $\mathfrak{g} \not\subseteq \uu(5)$, the anomaly-free gauge-commuting CPT halvings that commute with $\mathfrak{g}$ are exactly $\pm(-1)^{N}$, with no use of number conservation or of the grading clause. In particular the Pati-Salam algebra $\so(4) \oplus \so(6)$ of the split-preserving bivectors (Proposition \claimref{standard-model.automorphisms-preserve-slot-pair-split-are}), the left-right algebra $\su(3) \oplus \su(2)_{L} \oplus \su(2)_{R} \oplus \uu(1)_{B - L}$, $\su(4) \oplus \su(2)_{L} \oplus \uu(1)$ and the flipped $\uu(5)$ fix the bit; the Georgi-Glashow $\uu(5)$, and the Standard Model algebra with $B - L$ or with $N$ adjoined, do not.
\item[(iv)] \emph{(Yukawa forms.)} With the invariant pairing $B$ of Lemma \claimref{standard-model.invariant-pairing-five-modes}: for $(-1)^{N}$ the slot vectors pair the lepton doublet (one slot, three pairs) with $\Omega$; for $\Gamma'$ the full state $\Omega^{\top}$ has $B(\Omega^{\top}, X\psi) = B(\psi, X\Omega^{\top}) = 0$ for every other state $\psi$ of its half and every Clifford element $X$ of grade $1$, $3$ or $5$, keeps a nonzero self-pairing $B(\Omega^{\top}, X\Omega^{\top})$, and meets the lepton doublet only through grade four. The charged states of the two halves coincide. Hence, for Yukawa couplings that are odd-grade forms $B(\psi, X\varphi)$ (the $10$, $120$ and $126$ forms of the stored mass relations; under $\Gamma'$ the particle half is not an $\so(10)$ module, so these forms are an assumption there, not singled out), the rung coupling gives the particle half's neutral singlet a Dirac coupling to the lepton doublet under $(-1)^{N}$ and none under $\Gamma'$.
\item[(v)] \emph{(CPT blindness.)} $\Theta = U\kappa$, with $U = \prod_{k}(a^{\dagger}_{k} + a_{k})$ and $\kappa$ complex conjugation in the occupation basis, commutes with all ten Hermitian Majoranas, so with $\Spin(10)$, carries $\Omega$ to $\pm\Omega^{\top}$, commutes with the swap $S$ of $\Omega$ and $\Omega^{\top}$, and satisfies $\Theta(-1)^{N}\Theta^{-1} = -(-1)^{N}$ and $\Theta\Gamma'\Theta^{-1} = -\Gamma'$.
\end{enumerate}
Hence, given the other clauses of the slot-module hypothesis (\claimref{standard-model.slot-module-hypothesis}) and anomaly freedom, the grading form of its chirality clause (its earlier version) is equivalent to the chirality commuting with some gauge algebra between the Standard Model and $\so(10)$ that leaves $\uu(5)$, the Pati-Salam algebra of the chain among them (the clause's current form), and is not implied by any that stays inside it.

## technical
The stored ladder showed that symmetry, CPT and anomaly freedom leave one binary choice in the composite's chirality, whether the empty or the full five-mode state is the particle half's sterile singlet, and that only operators of $\so(10)$ that create or destroy two modes see it. This result asks which gauge algebras between the Standard Model and $\so(10)$ contain such operators. Hypercharge sorts $\so(10)$ into three eigenvalue families that never overlap (number-conserving, pair-creating, pair-annihilating), so any gauge algebra containing hypercharge either stays entirely inside the number-conserving $\uu(5)$ or contains a pair-creation operator and its adjoint. One such pair, with the anomaly-fixed signs on the charged states, already pins the neutral block, and number conservation is not needed. So the Pati-Salam, left-right and flipped stages decide the bit and the Georgi-Glashow stage cannot. Two cross-checks: under the swapped choice the stored Yukawa forms (all of odd Clifford grade) leave the particle half's singlet uncoupled from the rest of the half, so the rung coupling gives no Dirac neutrino coupling; and the Clifford CPT antiunitary treats both choices alike. Since the stored chain, stated under (S), runs through Pati-Salam, the clause can be read as the chirality commuting with the chain's intermediate gauge algebra: an exchange of premises onto registered structure, not a derivation from nothing.

## lay
Each matter particle of one family is a pattern of five filled or empty slots, and one yes-or-no choice in sorting patterns into particles and antiparticles had been left as an assumption: whether the completely empty pattern goes with the particles. This result shows which larger symmetries can settle that choice. Any symmetry that can create or remove two slots at once settles it, and the symmetries that only move slots around never do. The intermediate symmetry stage the series already uses, Pati-Salam, is of the first kind, so if the sorting respects that symmetry, the choice is fixed; this trades the assumption for that requirement rather than removing it. With the other choice, and mass couplings of the usual kind, the neutrino partner would have no ordinary mass coupling to the rest of its family.

## one-liner
$\mathrm{ad}\,Y$ separates $\so(10)$ into $\uu(5)$ and pair creation and annihilation with disjoint eigenvalues, so a gauge algebra between the Standard Model and $\so(10)$ either lies in $\uu(5)$, leaving the neutral-singlet bit free, or contains one pair bilinear and its adjoint, which with the anomaly-fixed charged chirality forces $\pm(-1)^{N}$: Pati-Salam, left-right and flipped stages decide the bit, Georgi-Glashow does not; under the swapped choice the singlet has no odd-grade Yukawa pairing in its half, and the Clifford CPT antiunitary is blind to the bit.
