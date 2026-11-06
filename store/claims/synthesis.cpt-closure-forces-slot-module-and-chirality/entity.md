---
id: synthesis.cpt-closure-forces-slot-module-and-chirality
kind: claim
version: 1
title: 'CPT closure forces the slot module; anomaly freedom, the chirality'
status: proved
region: synthesis
subject: standard-model
tags: [hypotheses-s-r-c, hypercharge-and-anomalies, chirality, classification]
proposed_by:
  kind: ai
  session: 2026-10-23-toe
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
  - standard-model.imported-pair-systems-two-chirality-halves@5
  - standard-model.global-form-quotient-determined@3
  - standard-model.imported-anomaly-coefficients@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_cpt_closure_classification
- kind: check
  ref: check.py::check_generation_forces_fermionic_slots
- kind: check
  ref: check.py::check_anomaly_free_halvings
- kind: check
  ref: check.py::check_chirality_is_mode_parity
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - standard-model.slot-module-hypothesis
  - synthesis.anomaly-freedom-forces-slot-content
  - field-theory.assignments-survive
extraction:
  open_problem: op.hypothesis-s
  note: 'Bears on the reformulated problem by replacing clauses (c), (d) and (e) of the slot-module hypothesis by a CPT halving (the standard structure of a theory of Weyl fermions, entered here as a hypothesis of the theorem, not as a premise of the register) and the generation clause (which contains (e), the unique slot vacuum, and fixes the one-slot space to a single doublet), with anomaly freedom: (d) is recovered up to a line in the neutral-singlet block, and (c) is no longer needed (if the slots are tower elements of one parity whose grading is the chirality, that parity is odd); and by deriving the fermionic slot content and exclusion from CPT closure and generation without the anomaly conditions. It does not use the slot-module hypothesis or Hypothesis (S); its past cone is that of synthesis.anomaly-freedom-forces-slot-content, which fixes the chirality grading and derives the content, while here the grading is derived. Clause (4) for F = Lambda C^2 agrees with the count of four anomaly-free conjugation patterns of field-theory.assignments-survive, which is stated for the (S) listing and is not used. The generation clause was added after the pre-registered form of the route (CPT halving with a unique slot vacuum only) was killed by the counter-model of clause (2) at b = 3; the general classification for dim F_0 = a > 1 (net chiralities equal to one integer s with s, a, b of one parity and |s| at most min(a, b)) was computed in parallel in the same run and is not part of this statement. Transport-absent beyond the pair system and the global form. Imported from memory, not as store entities, and used only in the proof - the Pieri rule for U(2), Schur''s lemma, and the CPT theorem''s statement that the antiparticle states of left-handed Weyl fermions are right-handed in the conjugate representation (R. F. Streater and A. S. Wightman, PCT, Spin and Statistics, and All That, 1964), which motivates the halving hypothesis. Suggested decision for Leon (not a store change) - restate the slot-module hypothesis with clauses (c), (d) and (e) replaced by the generation clause and the CPT halving, keeping the unique slot vacuum (multiplicity one) stated explicitly, and fix the line in the neutral-singlet block by requiring the chirality to commute with Spin(10).'
---

## formal
Let $W$ be the pair space of Fact \claimref{standard-model.imported-pair-systems-two-chirality-halves}, let $F = \bigoplus_{n \ge 0}F_{n}$ be a finite-dimensional polynomial representation of $U(2)$ graded by the slot number $n$, and let $(A, B) \in S(U(2) \times U(3))$ act on $V = F \otimes \Lambda^{\bullet}W$ as $A \otimes \Lambda^{\bullet}B$, so that the hypercharge of Theorem \claimref{standard-model.global-form-quotient-determined} is $Y = (3n - 2k)/6$ on $F_{n} \otimes \Lambda^{k}W$. A \emph{CPT halving} is a decomposition $V = V_{+} \oplus V_{-}$ into subrepresentations with $V_{-}$ isomorphic to the complex conjugate of $V_{+}$; $V_{+}$ is \emph{anomaly-free} when it satisfies the four conditions of Fact \claimref{standard-model.imported-anomaly-coefficients}. $F$ is \emph{generated} when $F_{0} = \C$ and some $U(2)$-equivariant slot creation map $a^{\dagger} : \C^{2} \otimes F_{n} \to F_{n+1}$ is onto for every $n$. Write $F_{(\lambda_{1}, \lambda_{2})}$ for the irreducibles, so $\Lambda^{0}\C^{2} = F_{(0,0)}$, $\Lambda^{1}\C^{2} = F_{(1,0)}$, $\Lambda^{2}\C^{2} = F_{(1,1)}$.
\begin{enumerate}
\item \emph{(CPT closure.)} $V$ is isomorphic to its complex conjugate, equivalently $V$ admits a CPT halving, if and only if $F \cong a\,\Lambda^{0}\C^{2} \oplus b\,\Lambda^{1}\C^{2} \oplus a\,\Lambda^{2}\C^{2}$ as graded $U(2)$-modules for some $a, b \ge 0$. In particular CPT closure excludes every $F_{n}$ with $n \ge 3$ and every slot state of weak spin one or more.
\item \emph{(Unique slot vacuum.)} For $a = 1$ an anomaly-free CPT halving exists if and only if $b$ is odd; then $V_{+}$ is one generation together with $\tfrac{b-1}{2}$ vectorlike pairs $(2,3)_{1/6} \oplus (2,\bar{3})_{-1/6}$ and $\tfrac{b-1}{2}$ vectorlike pairs $(2,1)_{1/2} \oplus (2,1)_{-1/2}$, or the conjugate of this.
\item \emph{(Generation.)} If $F$ is generated, $V$ is CPT-closed if and only if $F \cong \Lambda^{\bullet}\C^{2}$, and then $a^{\dagger}(u)a^{\dagger}(u') = -a^{\dagger}(u')a^{\dagger}(u)$ for all $u, u' \in \C^{2}$: the slot module is the fermionic one and slot creation obeys exclusion, with no anomaly condition used.
\item \emph{(Chirality.)} For $F = \Lambda^{\bullet}\C^{2}$ the anomaly-free CPT halvings are exactly those with $V_{+}$ equal, on every isotypic component other than the twice-occurring neutral singlet $(1,1)_{0}$ (the components $n = k = 0$ and $n = 2$, $k = 3$), to the sum of the $F_{n} \otimes \Lambda^{k}W$ with $n + k$ even, or to the sum of those with $n + k$ odd; on the neutral singlet block $V_{+}$ is any line. The even choice is one generation, $Q, u^{c}, d^{c}, L, e^{c}$ and a neutral singlet. So the chirality is $\pm(-1)^{n + k}$, the parity of the total mode number, away from the neutral singlets; it equals the tower grading $(-1)^{\pi n + k}$ for slot parity $\pi = 1$, and for $\pi = 0$ neither half of the tower grading is anomaly-free.
\end{enumerate}
Consequently, for a composite space $F \otimes \Lambda^{\bullet}W$ with hypercharge from the centre, a slot module generated from a unique vacuum and a chirality that is an anomaly-free CPT halving, the fermionic slot module, exclusion and the chirality of Hypothesis (S), the parity of the total mode number, all follow, the last up to the choice of a line in the neutral singlet block; and if the slots are tower elements of one parity whose grading is the chirality, that parity is odd.

## technical
Take the composite space as a slot module tensored with one pair system and the hypercharge from the centre, as the slot-module hypothesis does, but do not assume a slot parity or that the chirality is the tower grading. Ask only what a theory of Weyl fermions requires, that the state space split into a left-handed half and its CPT conjugate. The colour triplets decide the slot module: a triplet with $n$ slots and its conjugate antitriplet must occur with the same multiplicity, which pairs $F_{n}$ with $F_{2 - n}$ and so leaves only slot numbers $0, 1, 2$, with no weak triplet and as many two-slot singlets as slot vacua. With one vacuum, anomaly freedom then allows any odd number of slot doublets, the extra ones entering in vectorlike pairs. If the slot module is generated from its vacuum by one doublet of slot creation operators, as a Fock-type module is, CPT closure alone leaves exactly the fermionic module $\Lambda^{\bullet}\C^{2}$, with exclusion. For that module the four anomaly conditions select exactly two halvings, the even and the odd parity of the total mode number, apart from a free line in the block of the two neutral singlets. So the chirality of Hypothesis (S) and the odd slot parity are consequences, not premises.

## lay
The series builds each particle from two kinds of internal slot, and the most-used assumption in the store says, among other things, which states are left-handed and that the slot quanta behave like fermions. This result shows that part of that assumption can be derived. Requiring only what every theory of fermions has, that each particle's antiparticle be present with the opposite handedness, already forces the slot quanta to be fermion-like, provided the slot states are built from one empty state by adding quanta of a single two-state kind. Requiring further that the theory be free of quantum anomalies then forces the handedness to be the even-or-odd count of occupied modes, exactly as the assumption states, except for the choice within the pair of neutral states that would be the right-handed neutrino.

## one-liner
For $V = F \otimes \Lambda^{\bullet}W$ with $Y = (3n - 2k)/6$, CPT closure holds iff $F = a\Lambda^{0} \oplus b\Lambda^{1} \oplus a\Lambda^{2}$; with one vacuum anomaly-free halvings need $b$ odd, and with $F$ generated from its vacuum CPT closure forces $F = \Lambda^{\bullet}\C^{2}$ with exclusion and anomaly freedom forces the chirality $\pm(-1)^{n + k}$ off the neutral singlets.
