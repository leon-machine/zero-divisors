---
id: synthesis.fock-slot-module-is-cpt-closed-only-over-one-doublet
kind: claim
version: 1
title: 'A Fock slot module is CPT-closed only as the exterior algebra of one doublet'
status: proved
region: synthesis
subject: standard-model
tags: [hypotheses-s-r-c, car-algebra, representation-theory, forcing-and-uniqueness]
proposed_by:
  kind: ai
  session: 2026-11-07-ga-units
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: run 2026-11-07-ga-units
review: draft
derivations:
- name: main
  uses:
  - synthesis.cpt-closure-forces-slot-module-and-chirality@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_exterior_fock_module_is_cpt_closed_only_for_one_doublet
- kind: check
  ref: check.py::check_symmetric_fock_module_is_never_cpt_closed
- kind: check
  ref: check.py::check_weak_triplet_in_the_two_slot_space_by_null_pairs
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - standard-model.slot-module-hypothesis
  - synthesis.cpt-closure-forces-slot-module-and-chirality
extraction:
  open_problem: op.hypothesis-s
  note: >-
    Reduces clause (G) of the slot-module hypothesis (unique vacuum, one doublet of creation operators) to a
    structural clause: if the slot module is a Fock module of either statistics over its one-slot space, CPT
    closure (clause (1) of synthesis.cpt-closure-forces-slot-module-and-chirality) forces the exterior algebra
    of one doublet. The statistics and the number of doublets are derived; the Fock clause is a hypothesis of
    the statement, not a new postulate, and it remains a premise if adopted in place of (G). Pre-registered kill
    condition: a stored result needing a generated, non-Fock slot module, or a one-slot multiplicity label that
    the Fock clause would wrongly exclude; none was found in the survey that suggested it (a search of the store,
    not a proof). General b by the decomposition of Lambda^2(V (x) W); exact checks for b = 1..4 and a
    null-pair realisation for b = 1, 2. Numbers are read in span{1, I4}, so the doublet is a two-dimensional
    module over span{1, I4} and no bare complex field appears. Holds given what that theorem holds given
    (nothing). Transport-absent: the tower supplies Fock modules, but so does standard second quantisation.
---

## formal
Let $W$, $F = \bigoplus_{n \ge 0}F_{n}$, $V = F \otimes \Lambda^{\bullet}W$, the action of $S(U(2) \times U(3))$, the hypercharge and CPT closure be as in Theorem \claimref{synthesis.cpt-closure-forces-slot-module-and-chirality} and clauses (a), (b) of Premise \claimref{standard-model.slot-module-hypothesis}, with numbers read in $\mathrm{span}\{1, I_{4}\}$ and all powers taken over it; let $D$ be the slot doublet, the defining module of the slot $U(2)$ (the theorem's $\Lambda^{1}$ of the doublet), and $F_{(\lambda_{1}, \lambda_{2})}$ the irreducibles, of weak spin $\tfrac12(\lambda_{1} - \lambda_{2})$. Call $F$ a \emph{Fock module over its one-slot space} if $F = \Lambda^{\bullet}F_{1}$ (exterior) or $F = \mathrm{Sym}^{\bullet}F_{1}$ (symmetric), graded by degree, with $U(2)$ acting through its action on $F_{1}$; equivalently, $F$ is generated from one vacuum by creation operators $a^{\dagger}(u)$, $u \in F_{1}$, that anticommute (respectively commute) and obey no further relation.
\begin{enumerate}
\item[(i)] \emph{(The one-slot space; proved.)} $F_{1} \cong D \otimes M$ for a multiplicity space $M$ of some dimension $b \ge 0$ on which $U(2)$ acts trivially.
\item[(ii)] \emph{(Exterior case; proved.)} $\Lambda^{2}(D \otimes M) \cong \mathrm{Sym}^{2}D \otimes \Lambda^{2}M \oplus \Lambda^{2}D \otimes \mathrm{Sym}^{2}M = \binom{b}{2}F_{(2,0)} \oplus \binom{b+1}{2}F_{(1,1)}$. Hence $\Lambda^{\bullet}F_{1}$ is CPT-closed if and only if $b = 1$: for $b \ge 2$ its two-slot space carries weak spin one, which clause (1) of the theorem excludes, and for $b = 0$ it has no two-slot state.
\item[(iii)] \emph{(Symmetric case; proved.)} $\mathrm{Sym}^{\bullet}F_{1}$ is never CPT-closed: for $b \ge 1$ it is infinite-dimensional and its two-slot space contains $\binom{b+1}{2}$ copies of $F_{(2,0)}$; for $b = 0$ it has no two-slot state.
\item[(iv)] \emph{(Consequence; proved.)} If the slot module is a Fock module over its one-slot space and $V$ is CPT-closed, then $F = \Lambda^{\bullet}D$: the slot vacuum is unique, the slot module is generated from it by one doublet of creation operators (clause (G)), and slot creation obeys exclusion. The statistics and the number of doublets are derived; the Fock clause is a hypothesis of this statement, a structural replacement for (G), not derived and not a new postulate.
\end{enumerate}
The result holds given what the theorem holds given. Transport-absent.

## technical
Clause (G) of the slot-module hypothesis assumes two numbers, a unique slot vacuum and a single doublet of slot creation operators, and the stored theorem shows that, with (G), CPT closure makes the slot module fermionic. This result trades (G) for a structural clause: the slot module is the Fock module, of either statistics, over its own one-slot space, the second quantisation of the slot labels. The one-slot space is automatically $b$ copies of the doublet. For the exterior module the two-slot space splits as $\mathrm{Sym}^{2}D \otimes \Lambda^{2}M \oplus \Lambda^{2}D \otimes \mathrm{Sym}^{2}M$, so for $b \ge 2$ it contains a weak triplet, which CPT closure forbids, and for $b = 0$ it is empty; only $b = 1$ survives, giving $\Lambda^{\bullet}D$. The symmetric module is infinite-dimensional and also carries weak triplets. So, given the Fock clause, CPT closure alone fixes the statistics (fermionic), the number of doublets (one) and the unique vacuum. The Fock clause is still a premise if adopted: it would hold if the slot quanta were tower modes, which the store does not derive. Checked exactly for $b \le 4$, with the two-slot weak content also computed from null-pair vectors in geometric algebra. Transport-absent.

## lay
In the series' account of quarks and leptons, each particle is built from a few "slots" that can be filled, combined with a colour part. One assumption says the slots form a single pair (a doublet) and start from one empty state. This result shows that a more natural assumption does the same job: that the slot states are just all ways of putting identical quanta into the one-slot states, for either kind of quantum statistics. A symmetry requirement already in the theory (that the states come with their antiparticle mirror images) then rules out boson-like slots and any number of slot pairs other than one: with two or more pairs some two-slot states would carry weak spin one, which the mirror symmetry forbids.

## one-liner
If the slot module is a Fock module of either statistics over its one-slot space $D \otimes M$, $\dim M = b$, CPT closure forces $b = 1$ and the exterior algebra $\Lambda^{\bullet}D$, because $\Lambda^{2}(D \otimes M) \supseteq \mathrm{Sym}^{2}D \otimes \Lambda^{2}M$ carries weak spin one for $b \ge 2$ and the symmetric module is infinite-dimensional: the statistics and the single doublet are derived, the Fock clause assumed.
