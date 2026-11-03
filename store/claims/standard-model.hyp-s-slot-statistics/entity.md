---
id: standard-model.hyp-s-slot-statistics
kind: claim
version: 9
title: 'Hypothesis (S): slot statistics, derived from the slot-module hypothesis'
status: proved
region: standard-model
subject: standard-model
tags: [hypotheses-s-r-c, spinor-modules, hypercharge-and-anomalies]
proposed_by:
  kind: human
  author: leon (stated in the paper); entered by the build
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T12, deposited version
review: typed
derivations:
- name: main
  uses:
  - synthesis.cpt-closure-forces-slot-module-and-chirality@1
  - standard-model.imported-anomaly-coefficients@1
  - standard-model.global-form-quotient-determined@3
  - standard-model.imported-pair-systems-two-chirality-halves@5
  - standard-model.imported-fock-representation-clifford-algebra-bogoliubov@1
  assumes:
  - standard-model.slot-module-hypothesis@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_equivariant_slot_creation_is_exclusive
- kind: check
  ref: check.py::check_five_mode_content
- kind: check
  ref: check.py::check_chirality_is_total_mode_parity
- kind: check
  ref: check.py::check_one_clifford_system
- kind: check
  ref: check.py::check_particle_half_anomaly_free
locators:
  paper: T12
  number: Hypothesis (S)
  label: ''
  line: 1092
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: equivariant slot creation on Lambda C^2 is anticommuting, the five-mode particle half, the Spin(10)-commuting chirality as total mode parity with odd slot parity, one Clifford system of five modes, and anomaly freedom. Version 4 -> 5. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 5 -> 6. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 6 -> 7.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Converted the twistor slots to conformal-spinor slots at every level. The five-mode Fock space, U(2) x U(3) and the complex modes are the tower''s Fock structure, not twistor language, and are kept as they are.'
  source_title: |-
    Hypothesis (S): slot statistics
  source_formal: |-
    \emph{Hypothesis (S), slot statistics.} The twistor slots of the composite are fermionic modes on the same footing as its pairs: the composite's state space is the Fock space $\Lambda^{\bullet}(\C^{2} \oplus W)$ of five modes, two slot modes and three pair modes, a state being a set of occupied slots and occupied pairs, on which $(A, B) \in U(2) \times U(3)$ acts as $\Lambda^{\bullet}(A \oplus B)$; and, as in Fact \claimref{standard-model.imported-pair-systems-two-chirality-halves} for the three-mode Fock space $\Lambda^{\bullet}W$, the chirality of a state is the parity of its total mode number (Fact \claimref{standard-model.imported-fock-representation-clifford-algebra-bogoliubov} supplies the structure: $\Lambda^{\bullet}\C^{5}$ is the spinor module of $\Cl(10)$ and its parity grading is that module's chirality).
  env: hypothesis
  typing:
    by: ai-typing-pass
    note: Stated in a quote block as a declared structural premise, not a theorem; formal text is the
      quote verbatim with its two Fact references written as claimrefs.
  maintainer_pass_2026_10_31:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Version 9 repins the premise to version 4 of the slot-module hypothesis, whose chirality clause now reads "the chirality commutes with the Pati-Salam algebra of the chain" (Leon''s decision of 2026-10-31). The proof of (iii) is rewritten: anomaly freedom of the particle half (the consistency condition of the imported anomaly Fact, now used) gives the chirality +-(-1)^(j+k) off the neutral block through synthesis.cpt-closure-forces-slot-module-and-chirality (4), and commuting with the two-slot creation operator and its adjoint, both in the Pati-Salam algebra, fixes the neutral block; the step is written out. The sentences saying anomaly freedom is not used are removed, the formal summary, technical and lay levels reworded, and check_chirality_is_total_mode_parity now tests the Pati-Salam commutant (dimension 4), the two CPT halvings in it, anomaly freedom selecting the total parity, and the neutral-block step. Statements (i) to (v) unchanged.'
  maintainer_pass_2026_10_26:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Version 8 repins the premise to version 3 of the slot-module hypothesis, whose Spin(10) sentence of clause (CPT) is restated as "the chirality is the grading of the joint Clifford system" (proved equivalent for a CPT halving by synthesis.spin10-clause-content-is-the-neutral-singlet-choice). The formal summary of the premise, the technical level and the proof are reworded to the grading form, and the proof of (iii) gains one sentence: a grading anticommutes with every Majorana generator gamma_p, so it commutes with the bivectors gamma_p gamma_q, which generate Spin(10), and the Schur step stands as before. No clause, check or premise other than the pin changes; content unchanged.'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Version 4 rederives (S) from version 2 of the slot-module hypothesis (Leon''s decision 4 of 2026-10-23), whose clauses (c), (d), (e) were replaced by the generation clause and the chirality as a CPT halving commuting with Spin(10): the old route through synthesis.anomaly-freedom-forces-slot-content needed the tower grading as chirality and no longer applies, so the proof now goes through synthesis.cpt-closure-forces-slot-module-and-chirality (3) for the slot content and exclusion and Schur''s lemma for the chirality; anomaly freedom is no longer used and holds as a consequence. Clauses (ii) to (v) are unchanged in content; clause (i), odd slots, is now conditional (if the slot quanta are tower elements of one parity whose tower grading is the chirality, the parity is odd), since the premise no longer has a slot parity. Version 3 note follows. Version 3 restates Hypothesis (S) as a derived claim, status proved by maintainer change (Leon''s decision to adopt the weaker constituent hypothesis): it now assumes the new postulate standard-model.slot-module-hypothesis and uses synthesis.anomaly-freedom-forces-slot-content with the imported anomaly Fact, whose past cone was checked and does not contain (S). The theorem at m = 1 gives odd slots, the slot content (state space and particle half) and exclusion statistics among the slots, with chirality the parity of the total mode number; the version 2 clause that the slots are fermionic modes on the same footing as the pairs (slot and pair operators forming one Clifford system, on which Cl(10) acts) is kept as clause (v) and comes from clause (f) of the postulate, not from the theorem, so dependants that use Cl(10) on slots and pairs together rest on a premise that states it. The paper''s wording is kept under source_formal. Dependants keep their pins until repinned.'
---

## formal
\emph{Hypothesis (S), slot statistics.} Under the slot-module hypothesis (Premise \claimref{standard-model.slot-module-hypothesis}: the composite space $V = F \otimes \Lambda^{\bullet}W$, a graded $U(2)$ slot module tensored with one pair system, with hypercharge from the centre of $S(U(2) \times U(3))$, the slot module generated from a unique vacuum by one doublet of slot creation operators, the chirality a CPT halving that commutes with the Pati-Salam algebra of the chain once the slots are fermionic, and slot and pair operators one Clifford system):
\begin{enumerate}
\item[(i)] \emph{(Odd slots.)} If the slot quanta are tower elements of one tower parity $\pi$ whose tower grading $(-1)^{\pi n + k}$ is the chirality, then $\pi = 1$.
\item[(ii)] \emph{(Slot content.)} $F \cong \Lambda^{\bullet}\C^{2}$ as a graded $U(2)$-module, so the composite's state space is the Fock space $\Lambda^{\bullet}\C^{2} \otimes \Lambda^{\bullet}W = \Lambda^{\bullet}(\C^{2} \oplus W)$ of five modes, two slot modes and three pair modes, a state being a set of occupied slots and occupied pairs, on which $(A, B) \in U(2) \times U(3)$ acts as $\Lambda^{\bullet}(A \oplus B)$; its particle half is $(1,1)_{0} \oplus (1,\bar{3})_{-2/3} \oplus (2,3)_{1/6} \oplus (2,1)_{-1/2} \oplus (1,1)_{1} \oplus (1,\bar{3})_{1/3}$.
\item[(iii)] \emph{(Chirality.)} As in Fact \claimref{standard-model.imported-pair-systems-two-chirality-halves} for the three-mode Fock space $\Lambda^{\bullet}W$, the chirality of a state is the parity of its total mode number.
\item[(iv)] \emph{(Exclusion statistics.)} Every $U(2)$-equivariant slot creation map $a^{\dagger} : \C^{2} \otimes F_{n} \to F_{n+1}$ satisfies $a^{\dagger}(u)a^{\dagger}(u') = -a^{\dagger}(u')a^{\dagger}(u)$ for all $u, u' \in \C^{2}$; in particular $a^{\dagger}(u)^{2} = 0$.
\item[(v)] \emph{(One Clifford system.)} The slots are fermionic modes on the same footing as the pairs: the two slot modes and the three pair modes satisfy the canonical anticommutation relations as one system of five modes, so that, by Fact \claimref{standard-model.imported-fock-representation-clifford-algebra-bogoliubov}, their Majorana combinations generate $\Cl(10)$ acting on $\Lambda^{\bullet}\C^{5}$, its spinor module, whose parity grading is that module's chirality.
\end{enumerate}
Clauses (ii) and (iv) are Theorem \claimref{synthesis.cpt-closure-forces-slot-module-and-chirality}(3) under the premise's generation clause and CPT halving, with no anomaly condition; (v) is the premise's clause (f), applied once (ii) has made the slot module fermionic; (iii) follows from anomaly freedom of the particle half, the consistency condition of Fact \claimref{standard-model.imported-anomaly-coefficients}, through Theorem \claimref{synthesis.cpt-closure-forces-slot-module-and-chirality}(4), together with the premise's requirement that the chirality commute with the Pati-Salam algebra, whose two-slot creation operator and its adjoint fix the neutral-singlet line; (i) compares (iii) with a tower grading. Anomaly freedom is used as that consistency condition, not as a clause of the premise.

## technical
Hypothesis (S) was a premise of the Standard-Model paper: the two slots of a composite, the places its two conformal spinors occupy, are fermionic modes like its three pairs. It is now derived from the weaker slot-module hypothesis, which assumes the shape (a representation of the slot mixing $U(2)$, graded by slot number, tensored with one system of three pair modes), the hypercharge from the centre, slot states built from a unique empty state by one doublet of slot creation operators, and a chirality that splits the states into a left-handed half and its CPT conjugate and, once the slots are fermionic, commutes with the Pati-Salam algebra of the series' chain. CPT closure then forces the fermionic slot module with exclusion. Anomaly freedom of the particle content, the standard consistency condition, fixes the chirality as the parity of the total mode number except on the two neutral singlets, the empty and the full five-mode state; the Pati-Salam algebra contains the operator that creates both slots at once, and commuting with it and its adjoint puts the empty state in the particle half. Without anomaly freedom the pair-number parity would also commute with Pati-Salam.

What follows is exactly (S)'s content and statistics: the state space is the five-mode Fock space $\Lambda^{\bullet}(\C^{2} \oplus W)$, a state being a set of occupied slots and occupied pairs, with $(A, B) \in U(2) \times U(3)$ acting as $\Lambda^{\bullet}(A \oplus B)$; the chirality of a state is the parity of its total mode number; slot creation obeys the exclusion principle; and slots and pairs together form one system of five fermionic modes. Since $\Lambda^{\bullet}\C^{5}$ is the spinor module of $\Cl(10)$, with chirality its parity grading, the composite's states lie in that spinor module. That the slot and pair operators together form one Clifford system is supplied by the slot-module hypothesis, which assumes it once the slots are fermionic. The slot parity is no longer assumed: if the slots are tower elements of one parity whose grading is the chirality, that parity is odd.

## lay
The framework's account of quarks and leptons rested on an assumption, called (S), that two particular ingredients of each particle behave like fermions, the kind of particle that obeys the exclusion principle. It is now a consequence of a weaker assumption: that a particle's states are built from one empty state by adding quanta of a single two-state kind, and that handedness splits them into particles and their mirror-image antiparticles in a way that respects the intermediate Pati-Salam symmetry the framework uses. Under that assumption, with the standard requirement that the theory be free of anomalies, the ingredients must be fermions, and the possible states of a particle form exactly the standard quantum state space of five fermionic modes, with the right handedness for the particles of the Standard Model.

## one-liner
Under the slot-module hypothesis, the composite's slots are fermionic modes obeying exclusion and forming one Clifford system with its pairs, its state space is the five-mode Fock space $\Lambda^{\bullet}(\C^{2} \oplus W)$ with $U(2) \times U(3)$ acting as $\Lambda^{\bullet}(A \oplus B)$, chirality is the parity of the mode number, and slots of one tower parity whose grading is the chirality are odd.
