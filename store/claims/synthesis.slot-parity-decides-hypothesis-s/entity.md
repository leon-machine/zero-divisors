---
id: synthesis.slot-parity-decides-hypothesis-s
kind: claim
version: 4
title: 'Slot parity decides Hypothesis (S)'
status: proved
region: synthesis
subject: standard-model
tags: [hypotheses-s-r-c, spinor-modules, hypercharge-and-anomalies, no-go]
proposed_by:
  kind: ai
  session: 2026-10-22-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 4
  source: maintainer pass 2026-11-07 (GA units)
review: draft
derivations:
- name: main
  uses:
  - field-theory.no-canonical-commutation-relations-tower@3
  - standard-model.imported-pair-systems-two-chirality-halves@5
  - standard-model.imported-cauchy-decomposition-exterior-power@1
  - standard-model.imported-anomaly-coefficients@1
  - standard-model.global-form-quotient-determined@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_slot_parity_decides_s
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - standard-model.hyp-s-slot-statistics
  - field-theory.no-canonical-commutation-relations-tower
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'In the proof of (i) the complex rotation s'''' = c s_1 + I_4 d s_2 of the slot modes uses the unit of the tower''s canonical anticommutation algebra, the field theory''s I_4, which commutes with every tower mode operator; nothing stays.'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'The slot-module hypothesis was restated on 2026-10-23 (version 2: clauses (c), (d), (e) replaced by the generation clause (G) and chirality as a CPT halving); the clauses this result bears on are those of version 1, and its mathematics stands. Version 2 -> 3.'
  correction:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'W503: the one-liner now states as a condition (if) the reading of chirality as the tower grading under which clause (vi) holds. Version 1 -> 2.'
  open_problem: pr.hypothesis-s
  note: 'Answers the premise target in both directions. The statistics no-go excludes canonical bosonic slots but explicitly allows bosons made of fermions; an even (Klein-twisted) slot operator is such an object, satisfies every requirement short of (S), and is the independence model. What separates it from (S) is not the generation count but the hypercharge anomaly: with the tower grading as chirality, the even model puts doublets and singlets at opposite handedness and fails two of the four imported conditions. Transport-absent apart from the tower grading, which is the series object read as chirality. The cubic colour anomaly quoted in the proof (triplets minus antitriplets) is cited from memory and is not used. Not addressed: slots that are not two-level (parafermions of order two can be built in the tower and are a further alternative, with extra states); the three-constituent tension of op.hypothesis-s.'
---

## formal
Let the composite's three pair modes $b_{1}, b_{2}, b_{3}$ be the fermionic ladder pairs of Fact \claimref{standard-model.imported-pair-systems-two-chirality-halves}, odd elements of the tower's canonical anticommutation algebra, and let its two slot modes $s_{1}, s_{2}$ be elements of the same algebra such that: (a) each is homogeneous for the tower's grading, of parity $\pi \in \{0, 1\}$ (one for odd); (b) they are two-level, $s_{i}^{2} = 0$ and $s_{i}s_{i}^{*} + s_{i}^{*}s_{i} = 1$; (c) $U(2)$ acts on their span, $s_{i} \mapsto \sum_{l} A_{li}s_{l}$, preserving (b); (d) each slot operator commutes or anticommutes with each pair operator, and slot and pair annihilators share a vacuum $\lvert 0 \rangle$. Read the composite's chirality as the tower's grading, as Fact \claimref{standard-model.imported-pair-systems-two-chirality-halves} reads it on $\Lambda^{\bullet}W$. Write $(j, k)$ for the component with $j$ slot and $k$ pair modes occupied. Then:
\begin{enumerate}
\item[(i)] the slot modes satisfy the canonical anticommutation relations among themselves; two-level slots that commute with each other admit no such $U(2)$ action (a rotated slot squares to a nonzero multiple of $s_{1}s_{2}$, and the doubly occupied state is multiplied by the permanent of $A$, not its determinant);
\item[(ii)] for either parity the states $s_{J}^{*}b_{K}^{*}\lvert 0 \rangle$ are thirty-two independent vectors on which $U(2) \times U(3)$ acts as $\Lambda^{\bullet}A \otimes \Lambda^{\bullet}B \cong \Lambda^{\bullet}(A \oplus B)$ on $\Lambda^{\bullet}(\C^{2} \oplus W)$: the state space and group action of Hypothesis (S);
\item[(iii)] the tower parity of the component $(j, k)$ is $(-1)^{\pi j + k}$, whichever of the two mutual signs in (d) holds; it is the parity of the total mode number, the chirality of Hypothesis (S), if and only if $\pi = 1$;
\item[(iv)] for $\pi = 0$ the two chirality halves are $\bar{Q} \oplus \bar{L} \oplus u^{c} \oplus d^{c} \oplus e^{c} \oplus \nu^{c}$, the components $(1,2), (1,0), (0,2), (2,2), (2,0), (0,0)$, and its conjugate. For the hypercharge $Y = (3j - 2k)/6$ the $[SU(3)]^{2}U(1)$ sum of Fact \claimref{standard-model.imported-anomaly-coefficients} is $\mp\tfrac23$ and the $U(1)^{3}$ sum $\pm\tfrac49$, the other two vanishing; an abelian generator $\alpha j + \beta k + \gamma$ satisfies the three linear conditions if and only if $\beta = 0$ and $\gamma = -\alpha$, so none that tells a quark from a lepton is anomaly-free. For $\pi = 1$ the halves are the derived generation and its conjugate, and $Y$ passes all four conditions.
\end{enumerate}
Consequently: (v) the model with $\pi = 0$ has no pair with $[a, a^{*}] = 1$ (it lies in a finite floor, Proposition \claimref{field-theory.no-canonical-commutation-relations-tower}) and its slots are tower elements, yet the chirality clause of Hypothesis (S) fails in it, so (S) does not follow from the statistics no-go together with the requirement that the slots be tower elements; (vi) under (a) to (d), the tower grading as chirality, and the imported anomaly conditions for the hypercharge, the slots are odd and every clause of Hypothesis (S) holds, the mutual slot-pair sign being invisible to the state space, the group action and the grading.

## technical
Hypothesis (S) asks that the two slots of a composite be fermionic modes on the same footing as its three pairs, with chirality the parity of the total mode number. Take any two slot operators inside the tower's canonical anticommutation algebra that are two-level, carry a linear $U(2)$ action, have definite tower parity $\pi$, commute or anticommute with the pair modes and share their vacuum. The $U(2)$ action alone forces the slots to anticommute with each other: two commuting two-level slots are not $U(2)$ covariant, since the rotated slot fails to square to zero and the doubly occupied state transforms by a permanent.

Whatever the parity, the resulting thirty-two states carry exactly the state space $\Lambda^{\bullet}(\C^{2} \oplus W)$ and the $U(2) \times U(3)$ action of (S). The only thing the parity changes is the tower grading: the component with $j$ slots and $k$ pairs occupied has grading $(-1)^{\pi j + k}$. For odd slots this is the chirality (S) declares. For even slots, Klein-twisted fermions $s = cK$ that the no-canonical-commutation theorem explicitly allows as bosons made of fermions, the doublets land at the opposite handedness to the singlets. Each chirality half is then $\bar{Q} \oplus \bar{L} \oplus u^{c} \oplus d^{c} \oplus e^{c} \oplus \nu^{c}$ or its conjugate, which fails the $[SU(3)]^{2}U(1)$ condition by $\tfrac23$ and the cubic condition by $\tfrac49$ (the sums Theorem \claimref{standard-model.hypercharge-global-form-pair-counting-consistency}(3) records for doublets listed at the opposite handedness from the singlets); the only anomaly-free abelian generators are multiples of $j - 1$, which do not separate quarks from leptons.

So (S) is independent of the statistics no-go plus tower membership, with the even-slot model as witness, and the obstruction that removes the witness is anomaly cancellation of the hypercharge, not the generation count. Read the other way, the premises (a) to (d), the tower grading as chirality, and the imported anomaly conditions derive (S).

## lay
The framework's particle content rests on an assumption, called (S): the two places in a composite particle that its basic spinor states occupy behave like fermions, the same kind of quantum mode as the particle's internal pairs. It was hoped that a known result, that the framework has no room for elementary bosons, would force this. It does not: a slot can be built from two of the framework's fermions, which is allowed, and everything still works except one thing, which half of the states counts as left-handed. With such slots the left-handed states would have the weak doublets and the singlets at opposite handedness, and the resulting theory would be inconsistent, because its hypercharge would suffer a quantum anomaly. So (S) is a genuine extra assumption, but, if the slots are two-level and the framework's own grading is read as handedness, the requirement of an anomaly-free theory pins it down.

## one-liner
Two-level, $U(2)$-covariant slot modes in the tower carry the state space and group action of (S) at either tower parity; odd slots give (S)'s chirality, while even slots, which the no-CCR theorem allows, put doublets and singlets at opposite handedness and fail the hypercharge anomaly conditions, so (S) is independent of the statistics no-go and, if chirality is read as the tower grading, follows from anomaly cancellation.
