---
id: synthesis.flag-conjugate-antilinear-on-one-chirality-and-conjugation-reverses-jarlskog
kind: claim
version: 1
title: 'On one chirality the flag conjugate is antilinear; conjugating quark matrices reverses J'
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
quantities:
- quantity.jarlskog-invariant@1
checked_by:
- kind: check
  ref: check.py::check_only_the_total_exchange_reverses_the_charges_and_keeps_the_gauge_algebra
- kind: check
  ref: check.py::check_commutator_determinant_is_odd_under_conjugation
- kind: check
  ref: check.py::check_imported_identity_and_sign_of_j_on_a_rational_pair
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
    decision is the maintainer's. The statement is about one chirality half. In the five-mode algebra, on all 32
    states, the total exchange is linear and inner and reverses baryon number with no conjugation (the proposals
    synthesis.exchange-of-set-and-clear-is-inner-and-fixed-by-no-integer-state and
    synthesis.baryon-number-centraliser-in-the-five-mode-algebra of the same run); the two statements are
    compatible, and the joint one is that the exchange is a relabelling of the algebra, and of the laws only for
    orientation, sign of J and arrow taken together, the last part argued. The id names the earlier, stronger
    title; renaming the folder is left to the maintainer.
---

## formal
Under Hypothesis (S) (\claimref{standard-model.hyp-s-slot-statistics}) take the five-mode module with pair modes $1, 2, 3$ and slot modes $4, 5$, its occupation states $e_{S}$, the sixteen (the even states), and $\mathfrak{g} = \su(3) \oplus \su(2)_{L} \oplus \uu(1)_{Y}$ (\claimref{standard-model.automorphisms-preserve-slot-pair-split-are}). Write $k$ and $j$ for the pair and slot numbers of a state; on all $32$ states $B - L = 1 - \tfrac23 k$, $Y = \tfrac12(j - 1) + \tfrac12(B - L)$, and baryon number is $n_{B} = 0, \tfrac13, -\tfrac13, 0$ at $k = 0, 1, 2, 3$, which on the sixteen is the $n_{B}$ of Proposition \claimref{standard-model.proton-decay-only-through-slot-pair}. For $A \subseteq \{1, \dots, 5\}$ the \emph{partial exchange} $X_{A}$ exchanges set and clear, $v_{a} \leftrightarrow w_{a}$, on the modes of $A$ and fixes the others; on states it is $e_{S} \mapsto \pm e_{S \triangle A}$. Scalars of the family matrices are read in $\mathrm{span}\{1, I_{4}\}$ and $^{*}$ is $I_{4} \mapsto -I_{4}$, as in Fact \claimref{synthesis.imported-jarlskog-commutator-identity}.
\begin{enumerate}
\item[(i)] \emph{(Linear maps normalising the algebra fix baryon number.)} Let $g$ be an invertible linear map of the sixteen with $g\mathfrak{g}g^{-1} = \mathfrak{g}$. Then $g$ preserves each of the six species and commutes with every operator commuting with $\mathfrak{g}$; in particular $g\,n_{B}\,g^{-1} = n_{B}$. The same holds on the sixteen tensored with a family space, for $n_{B} \otimes 1$. This is the statement that the sixteen is not self-conjugate: no linear map compatible with $\mathfrak{g}$ carries a species to its conjugate. The hypothesis on $g$ is needed: the partial exchange on the modes $1, 2, 3, 4$ is a linear map of the sixteen to itself that reverses $n_{B}$ on every state, and it does not normalise $\mathfrak{g}$.
\item[(ii)] \emph{(The exchanges.)} Of the $32$ partial exchanges, four reverse $n_{B}$ on every state, those with $A \supseteq \{1, 2, 3\}$; two normalise $\mathfrak{g}$, the identity and the total exchange $A = \{1, \dots, 5\}$; and the total exchange alone reverses $Y$, $B - L$ and $n_{B}$ together. On the whole module it is linear, and it maps the sixteen onto the odd states. Hypothesis for the rest of this clause: the occupation states are orthonormal for a Hermitian form, so that $\mathfrak{g}$ acts by anti-Hermitian generators and the odd states are the complex conjugate of the sixteen as a module. Composed with that identification the total exchange is an antilinear map of the sixteen to itself normalising $\mathfrak{g}$. An antilinear $g$ normalising $\mathfrak{g}$ preserves every species and commutes with $n_{B}$ as an operator, and anticommutes with the unit of the module; so it does not reverse the operator $n_{B}$, it reverses the rotation generated by the unit times $n_{B}$. In the convention that the baryon charge of a field is its weight under that rotation, it carries a field of charge $b$ to one of charge $-b$; this is the sense of reversal used in (iv).
\item[(iii)] \emph{(Conjugation reverses the invariant.)} For $3 \times 3$ Hermitian $H_{u}$, $H_{d}$ put $D(H_{u}, H_{d}) = \det[H_{u}, H_{d}]$. Then $D^{*} = -D$; $D(UH_{u}U^{\dagger}, UH_{d}U^{\dagger}) = D(H_{u}, H_{d})$ for unitary $U$; $D(H_{u}^{*}, H_{d}^{*}) = -D(H_{u}, H_{d})$; and $D = 0$ when both are real symmetric. Hence, by the cited Fact, with the masses fixed and nondegenerate, a common unitary change of family basis fixes $J$, and entrywise conjugation followed by any such change sends $J$ to $-J$.
\item[(iv)] \emph{(Consequence; argued, not proved.)} Assume, and this is the assumption that is not derived, that a map acts on the sixteen tensored with the families, linearly or antilinearly, normalising $\mathfrak{g}$, and on $(H_{u}, H_{d})$ by a common unitary change of family basis in the linear case and by conjugation followed by one in the antilinear case. Then by (i) to (iii) the linear maps fix both the baryon charge and $J$, and the antilinear ones reverse both, the charge in the sense of (ii): the product of the sign of the baryon charge of a state and the sign of $J$ is invariant under every such map. So if $J \neq 0$, no map of this class is at once an automorphism of the laws, with their family matrices fixed up to a change of family basis, and a reversal of the baryon charge; if $H_{u}$ and $H_{d}$ are real in one family basis, conjugation in that basis is both.
\end{enumerate}
\emph{Reading (argued).} The argument that the orientation is initial data (\claimref{dark-matter.orientation-arrow-seventeenth-refutation}) uses a conjugation $C$ that is antilinear, fixes every translation, and is premised to leave every action functional and its parameters unchanged. The store holds a nonzero $J$ (the recorded value $3.12 \times 10^{-5}$) and a result that the Cabibbo element needs a relative phase between the up and down stages within $30^{\circ}$ of a quarter turn, real stages giving none (\claimref{synthesis.cabibbo-from-one-type-quark-stages-selects-near-quarter-turn-phase}); the real-breaking assumption is stated for the lepton matrices only. Two readings of $C$ on the family matrices are possible, and the store does not choose. If $C$ conjugates them, it is of the class of (iv): it carries the laws with $J$ to the laws with $-J$, and then (argued, conditional on this reading, and a matter for the maintainer) the action clause of the premise does not hold in the quark sector, and the two orientations are two solutions of two theories, the case in which the stored argument says its conclusion fails. If $C$ carries each family term to its adjoint, as the reversal in the stored composite suggests, the action clause can hold with $J \neq 0$, and then by Proposition \claimref{one-relation.arrow-frequency-are-one-bit-level} $C$ reverses the direction of time with the orientation: it relates a state with a baryon excess to one with the opposite excess and the opposite arrow. In both readings, on this argument, no stored automorphism exchanges two states of the same laws and the same arrow with opposite baryon charge. So, argued and not proved, the orientation is a label only jointly, with the sign of $J$ or with the arrow, and the sign of the baryon charge relative to $J$ and the arrow is not shown to be initial data by the exchange argument: with $J \neq 0$ it is of the kind a dynamics could fix. Whether any stored dynamics does is not decided here.

The algebra is standard and transport-absent. Not shown: how $C$ acts on spinor fields and family matrices; any statement about the lepton phases; any dynamics.

## technical
Three exact statements, on one chirality. First, any linear map of the sixteen that normalises the Standard Model algebra preserves each species, because the species have different dimensions or hypercharges and the quark doublet is the only one of dimension six; so no such map reverses baryon number. This says that the sixteen is a chiral representation; linear maps that do not normalise the algebra can reverse baryon number, and on the whole five-mode module the total exchange is itself linear. Second, among the 32 ways of exchanging set and clear on a subset of the five modes, only the identity and the total exchange normalise the gauge algebra, and the total exchange carries the sixteen to its conjugate: with the occupation states orthonormal, as a map of the sixteen it is antilinear, and it reverses the baryon rotation, not the operator. Third, entrywise conjugation of the two Hermitian quark matrices changes the sign of the determinant of their commutator, which is the Jarlskog invariant up to a factor fixed by the masses, and a change of family basis does not.

Argued, not proved: if the stored conjugation acts on the family matrices by conjugation, it is not a symmetry of laws with a nonzero Jarlskog invariant; if it carries each family term to its adjoint, it is, and it reverses the arrow too. On that argument the label argument for the orientation does not reach the sign of the baryon excess relative to the quark phase and the arrow. Which reading holds, and what follows for the premise of conjugation covariance, is for the maintainer.

## lay
The series argues that which kind of matter the universe is made of is an arbitrary label, because swapping matter and antimatter leaves all the laws unchanged. Two things are shown here exactly. For the particles of one handedness, the swap cannot be an ordinary linear relabelling that respects the forces; it has to involve complex conjugation. And complex conjugation of the two quark mass matrices changes the sign of the one number that measures the phase in the mixing of the quarks. What is argued, not shown: if the series' swap acts on those matrices by conjugation, it changes the laws; if it acts in the other possible way, it leaves them alone but reverses the direction of time as well. On that argument the free label is the kind of matter together with the sign of that number, or together with the direction of time, and the sign of the matter excess relative to them is not explained by the labelling argument. Nothing here shows that any process fixes it.

## one-liner
On one chirality, every invertible linear map normalising the Standard Model algebra preserves each species and fixes baryon number; of the 32 partial exchanges of set and clear only the total one normalises the algebra, and on the sixteen it is antilinear and reverses the baryon rotation; entrywise conjugation sends $\det[H_{u}, H_{d}]$ and so $J$ to its negative and a change of family basis does not; argued, not proved: the stored conjugation is then a symmetry of laws with $J \neq 0$ only if it also reverses the arrow.
