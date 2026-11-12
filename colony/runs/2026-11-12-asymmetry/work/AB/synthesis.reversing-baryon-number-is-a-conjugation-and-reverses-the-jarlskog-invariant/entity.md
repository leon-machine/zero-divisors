---
id: synthesis.reversing-baryon-number-is-a-conjugation-and-reverses-the-jarlskog-invariant
kind: claim
version: 1
title: 'Reversing baryon number needs a conjugation, which reverses the Jarlskog invariant'
status: proved
region: synthesis
subject: dark-matter
tags: [matter-asymmetry, flavour-and-mixing]
outside_ga:
  kind: imported
  why: 'the family matrices and their determinant are those of the imported Jarlskog identity, read as that Fact reads them, with entries in the span of 1 and I_4; the mode-algebra part is in the Clifford algebra of the ten'
proposed_by:
  kind: ai
  session: 2026-11-12-asymmetry
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-12-asymmetry
review: draft
derivations:
- name: main
  uses:
  - standard-model.hyp-s-slot-statistics@10
  - standard-model.automorphisms-preserve-slot-pair-split-are@7
  - standard-model.proton-decay-only-through-slot-pair@5
  - synthesis.imported-jarlskog-commutator-identity@2
  - dark-matter.orientation-arrow-seventeenth-refutation@10
  - synthesis.cabibbo-from-one-type-quark-stages-selects-near-quarter-turn-phase@4
  - one-relation.arrow-frequency-are-one-bit-level@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_only_the_total_exchange_reverses_the_charges_and_keeps_the_gauge_algebra
- kind: check
  ref: check.py::check_commutator_determinant_is_odd_under_conjugation
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - dark-matter.orientation-arrow-seventeenth-refutation
  - dark-matter.premise-cpt-covariance
  - dark-matter.premise-flag-as-datum
  - neutrino.real-breaking-assumption
extraction:
  open_problem: op.matter-asymmetry-origin
  note: >-
    Filed against the question whether the orientation of the asymmetry is a label, exchanged by an automorphism
    of all stored structure. The content is the standard analysis of charge conjugation with parity in the
    quark sector, and is transport-absent: that a universe of matter can be told from one of antimatter by the
    laws when the Jarlskog invariant is not zero is textbook (the charge asymmetry of the semileptonic decays
    of the long-lived neutral kaon; Sakharov 1967 for the use of it), cited from memory. What is new for the
    store is the form: over the whole group of set and clear exchanges on the five modes, and set against the
    action clause of the premise of conjugation covariance. Clause (iv) is the consequence for that premise and
    is argued, not proved, because the store does not say how the conjugation acts on the family matrices
    (the convention of the conjugation result does not cover spinor fields). No premise is changed here; the
    decision is the maintainer's.
---

## formal
Under Hypothesis (S) (\claimref{standard-model.hyp-s-slot-statistics}) take the five-mode module with pair modes $1, 2, 3$ and slot modes $4, 5$, its occupation states $e_{S}$, the sixteen (the even states), and $\mathfrak{g} = \su(3) \oplus \su(2)_{L} \oplus \uu(1)_{Y}$ (\claimref{standard-model.automorphisms-preserve-slot-pair-split-are}). Write $k$ and $j$ for the pair and slot numbers of a state; on all $32$ states $B - L = 1 - \tfrac23 k$, $Y = \tfrac12(j - 1) + \tfrac12(B - L)$, and baryon number is $n_{B} = 0, \tfrac13, -\tfrac13, 0$ at $k = 0, 1, 2, 3$, which on the sixteen is the $n_{B}$ of Proposition \claimref{standard-model.proton-decay-only-through-slot-pair}. For $A \subseteq \{1, \dots, 5\}$ the \emph{partial exchange} $X_{A}$ exchanges set and clear, $v_{a} \leftrightarrow w_{a}$, on the modes of $A$ and fixes the others; on states it is $e_{S} \mapsto \pm e_{S \triangle A}$. Scalars of the family matrices are read in $\mathrm{span}\{1, I_{4}\}$ and $^{*}$ is $I_{4} \mapsto -I_{4}$, as in Fact \claimref{synthesis.imported-jarlskog-commutator-identity}.
\begin{enumerate}
\item[(i)] \emph{(Linear automorphisms fix baryon number.)} Let $g$ be an invertible linear map of the sixteen with $g\mathfrak{g}g^{-1} = \mathfrak{g}$. Then $g$ preserves each of the six species and commutes with every operator commuting with $\mathfrak{g}$; in particular $g\,n_{B}\,g^{-1} = n_{B}$. The same holds on the sixteen tensored with a family space, for $n_{B} \otimes 1$.
\item[(ii)] \emph{(The exchanges.)} Of the $32$ partial exchanges, four reverse $n_{B}$ on every state, those with $A \supseteq \{1, 2, 3\}$; two normalise $\mathfrak{g}$, the identity and the total exchange $A = \{1, \dots, 5\}$; and the total exchange alone reverses $Y$, $B - L$ and $n_{B}$ together. It maps the sixteen onto the odd states, the conjugate sixteen. So the only exchange of set and clear that reverses baryon number and keeps the gauge algebra is the flag conjugate, and composed with the identification of the conjugate sixteen with the complex conjugate of the sixteen it is an antilinear map of the sixteen to itself. An antilinear $g$ normalising $\mathfrak{g}$ commutes with $n_{B}$ and anticommutes with the unit of the module, so it reverses the generator of the baryon rotation: it carries a field of baryon charge $b$ to one of charge $-b$.
\item[(iii)] \emph{(Conjugation reverses the invariant.)} For $3 \times 3$ Hermitian $H_{u}$, $H_{d}$ put $D(H_{u}, H_{d}) = \det[H_{u}, H_{d}]$. Then $D^{*} = -D$; $D(UH_{u}U^{\dagger}, UH_{d}U^{\dagger}) = D(H_{u}, H_{d})$ for unitary $U$; $D(H_{u}^{*}, H_{d}^{*}) = -D(H_{u}, H_{d})$; and $D = 0$ when both are real symmetric. Hence, by the cited Fact, with the masses fixed and nondegenerate, a common unitary change of family basis fixes $J$, and entrywise conjugation followed by any such change sends $J$ to $-J$.
\item[(iv)] \emph{(Consequence; argued.)} Let a map act on the sixteen tensored with the families, linearly or antilinearly, normalising $\mathfrak{g}$, and on $(H_{u}, H_{d})$ by a common unitary change of family basis in the linear case and by conjugation followed by one in the antilinear case. By (i) to (iii) the linear maps fix both the baryon charge and $J$, and the antilinear ones reverse both: the product of the sign of the baryon charge of a state and the sign of $J$ is invariant under every such map. So if $J \neq 0$, no map of this class is at once an automorphism of the laws, with their family matrices fixed up to a change of family basis, and a reversal of the baryon charge; if $H_{u}$ and $H_{d}$ are real in one family basis, conjugation in that basis is both.
\end{enumerate}
\emph{Reading (argued).} The argument that the orientation is initial data (\claimref{dark-matter.orientation-arrow-seventeenth-refutation}) uses a conjugation $C$ that is antilinear, fixes every translation, and is premised to leave every action functional and its parameters unchanged. The store holds a nonzero $J$ (the recorded value $3.12 \times 10^{-5}$) and a result that the Cabibbo element needs a relative phase between the up and down stages within $30^{\circ}$ of a quarter turn, real stages giving none (\claimref{synthesis.cabibbo-from-one-type-quark-stages-selects-near-quarter-turn-phase}); the real-breaking assumption is stated for the lepton matrices only. Two readings of $C$ on the family matrices are possible, and the store does not choose. If $C$ conjugates them, it is of the class of (iv): it carries the laws with $J$ to the laws with $-J$, the action clause of the premise fails in the quark sector, and the two orientations are two solutions of two theories, the case in which the stored argument says its conclusion fails. If $C$ carries each family term to its adjoint, as the reversal in the stored composite suggests, the action clause can hold with $J \neq 0$, and then by Proposition \claimref{one-relation.arrow-frequency-are-one-bit-level} $C$ reverses the direction of time with the orientation: it relates a state with a baryon excess to one with the opposite excess and the opposite arrow. In both readings no stored automorphism exchanges two states of the same laws and the same arrow with opposite baryon charge. The orientation is therefore a label only jointly, with the sign of $J$ or with the arrow, and the sign of the baryon charge relative to $J$ and the arrow is not shown to be initial data by the exchange argument: with $J \neq 0$ it is of the kind a dynamics could fix. Whether any stored dynamics does is not decided here.

The algebra is standard and transport-absent. Not shown: how $C$ acts on spinor fields and family matrices; any statement about the lepton phases; any dynamics.

## technical
Three exact statements. First, any linear map of the sixteen that normalises the Standard Model algebra preserves each species, because the species have different dimensions or hypercharges and the quark doublet is the only one of dimension six; so no linear symmetry reverses baryon number. Second, among the 32 ways of exchanging set and clear on a subset of the five modes, only the total exchange keeps the gauge algebra and reverses the charges, and it carries the sixteen to its conjugate: as a symmetry of the sixteen it is antilinear. Third, an antilinear map conjugates the family matrices, and the determinant of the commutator of the two Hermitian quark matrices, which is the Jarlskog invariant up to a factor fixed by the masses, changes sign under conjugation and is unchanged by any change of family basis.

So with a nonzero Jarlskog invariant, exchanging matter and antimatter is not an automorphism of the laws unless it also changes the sign of that invariant or the direction of time. The stored argument that the orientation is a free label uses a conjugation premised to leave all laws unchanged; in the quark sector that premise either fails or holds only for a conjugation that also reverses time. Either way the relative sign of the baryon excess, the quark phase and the arrow is a physical bit that the label argument does not reach.

## lay
The series argues that which kind of matter the universe is made of is an arbitrary label, because swapping matter and antimatter leaves all the laws unchanged. This result checks that against the one place where the laws are known not to be mirror-symmetric in this way: the mixing of the quarks carries a phase, measured by a single number, and that number changes sign under the swap. So the swap changes the laws unless time is reversed too. What remains a free label is the pair taken together, the kind of matter and the sign of that number, or the kind of matter and the direction of time. The sign of the matter excess relative to them is a physical fact that the labelling argument does not explain, and that a dynamical process could in principle fix.

## one-liner
Every linear automorphism of the sixteen normalising the Standard Model algebra fixes baryon number; of the 32 partial exchanges of set and clear only the total one, the antilinear flag conjugate, reverses the charges and keeps the algebra; conjugation sends $\det[H_{u}, H_{d}]$ and so $J$ to its negative; so with $J \neq 0$ the orientation is a label only jointly with the sign of $J$ or the arrow.
