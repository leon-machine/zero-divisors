# Bridge survey: op.hypothesis-s (are a composite's twistor slots fermionic modes)

Labels: **proved** (in store), **computed** (exact, by me; script `/tmp/claude-0/-home-claude/23cbb9be-73ca-5537-8211-47496476158a/scratchpad/bridges/work_hs/screen.py`, Fractions, imports GA), **argued**, **speculative**. Nothing was filed or edited.

## 1. The residual

`synthesis.cpt-closure-forces-slot-module-and-chirality` (proved) takes as inputs the shape (a), the hypercharge from the centre (b), a unique slot vacuum, generation by one doublet, a CPT halving, and anomaly freedom (the imported Fact). From these it delivers the fermionic slot module, exclusion, and the chirality ±(-1)^{n+k} away from the neutral-singlet block. It leaves four things open.

- **(i) The neutral-singlet line.** Once the total mode number is conserved, this is one bit: is Ω or Ω^⊤ the particle half's singlet? CPT, anomaly freedom, (G), the light-ray count, the Clifford CPT antiunitary and the Yukawa forms all fail to decide it (`synthesis.spin10-clause-content-is-the-neutral-singlet-choice`, `synthesis.neutral-singlet-bit-decided-by-gauge-algebra-leaving-u5`, `synthesis.slot-module-light-ray-arrays-are-weyl-components`). For now it is premised as "commutes with the Pati-Salam algebra of the chain".
- **(ii) Clause (G) itself**, meaning the unique vacuum and b = 1. Without generation, part (2) of the theorem allows any odd b, with the extra doublets in vectorlike pairs.
- **(iii) Clause (f), the joint Clifford system.** The theorem never touches it.
- **(iv) The shape (a) and the hypercharge clause (b).** These are untouched too.

The overall orientation sign ε is a separate bit. `dark-matter.orientation-arrow-seventeenth-refutation` shows it is solution data, not something the kinematics can fix.

## 2. Leads, best first

### Lead A. (G) as "the slot module is a Fock module over its one-slot space" (STRONG as a reduction)
- **Entities:** `synthesis.cpt-closure-forces-slot-module-and-chirality`(1), `synthesis.slot-module-makes-the-faces-separate-composites-and-leaves-the-generation-number-free`(1), `tower.fock-module-one-qubit-per-rung`, `std-algebra.fock-representation`, `field-theory.second-quantisation`, `field-theory.no-canonical-commutation-relations-tower`. Subjects: tower, quantum-fields, standard-algebra.
- **What it supplies (computed for b = 1..4, argued for all b).** Suppose F is the Fock module of either statistics over its one-slot space F_1 = bC^2. (F_1 is forced to be a sum of doublets by stored result (1).)
  - With CAR statistics: for b ≥ 2, Λ²(C²⊗C^b) contains Sym²C²⊗Λ²C^b, which has weak spin one. CPT closure (1) then fails. The computed content for b = 2 is F_2 = F_(2,0) ⊕ 3F_(1,1) and F_3 ≠ 0.
  - With CCR statistics: Sym^n never vanishes, so the module is infinite-dimensional. The stored no-go also excludes it.
  - Conclusion: CPT closure plus "Fock over the one-slot space" gives b = 1, F ≅ Λ•C², a unique vacuum and exclusion. The statistics, the vacuum count and the doublet count are all derived; none is assumed.
- **What remains.** (G) becomes a structural clause, the second quantisation of the slot labels, instead of a count. That clause is still a premise. It holds automatically if the slot quanta are tower modes, which is the "each twistor a rung" theorem that `note.rungs.abstract` names as missing.
- **Store check:** I found no existing statement of this (searched for b doublets, "one-slot space", Fock-over-slot phrases).
- **Kill condition (pre-registered):** the lead dies if some stored result needs a generated, non-Fock slot module (relations beyond statistics), or a one-slot space with a multiplicity label that the Fock clause would wrongly exclude.
- **Ledger:** convenient. The tower supplies Fock modules, but so does standard second quantisation.

### Lead B. The Pati-Salam clause as conformal (twistor) invariance of the chirality on the pair factor (PLAUSIBLE; structures match exactly)
- **Entities:**
  - `standard-model.pair-mixing-not-colour`(i),(ii) (proved, holds_given empty; its past cone has no slot-module premise, checked)
  - `correspondence.spin-representation`
  - `standard-model.imported-pair-systems-two-chirality-halves`
  - `field-theory.orientation-relocated`, `field-theory.second-quantisation`(4)
  - `lepton.relative-handedness-slotted-free-sectors`
  - `dark-matter.two-families-are-two-chiralities`
  - Subjects: conformal-spacetime, quantum-fields, standard-model, lepton, clifford-structure.
- **The match.** Pati-Salam su(4) on the pair factor is the compact real form of so(6,C) = Λ²V_C. The conformal algebra so(2,4) on the same Fock module is another real form of the same complex algebra, and `pair-mixing-not-colour`(i) says exactly this. A complex-linear Γ commutes with one real form iff it commutes with the other. By (ii) of that result, the commutant of so(2,4) on ΛW is span{P_CS, P_CS-}.
- **Computed.**
  - The commutant of gauge plus the even pair algebra on Λ•C⁵ has dimension 6: the blocks F_n⊗CS and F_n⊗CS-.
  - It contains 8 CPT halvings, exactly 2 of them anomaly-free, namely ±(-1)^N.
  - The vacuum-swapped halving is a CPT halving and anomaly-free, but it does not commute with the even pair algebra.
  - The product form Γ = f(n)·w(k) (chirality factorising across the tensor shape (a)) also leaves only ±(-1)^N among the anomaly-free CPT halvings.
- **Why the computed restriction to the U(2)×U(3) torus loses nothing (argued).** Under the full S(U(2)×U(3)) the result is the same, because F_0⊗CS and F_2⊗CS- are inequivalent under Spin(6).
- **Reading.** The bit is decided once the composite's chirality on each slot sector depends on its pair state only through the twistor/dual-twistor half. That holds if handedness is read on the conformal spinor through i = I4: by `field-theory.orientation-relocated`(2), J = +I4 on T and -I4 on T'. On the free sector it means Ω and u^c (both in CS = twistor space, one irreducible SU(2,2) module) share a half. `lepton.relative-handedness-slotted-free-sectors` lists the free sector by halves in exactly this way, so it uses the clause implicitly. In the 10-mode reading the clause is Cartan's family rule: the particle half is one family of pure spinors (`dark-matter.two-families-are-two-chiralities`). Ω and Ω^⊤ have annihilators that form a Witt pair, so they lie in opposite families because 5 is odd.
- **What remains.** The pair factor of V is the label copy H, and colour acts on H (`pair-mixing-not-colour`(iii)). The lead needs the label copy's parity to be identified with the twistor's parity. `note.field-theory.what-does-t12` and `note.standard-model.setting-two-flags-resolved-2` call this "the same missing theorem as (S)". The note says the same identification, together with the relative unit sign, also fixes ε. So one identification would decide both bits.
- **Consistency (computed).** Identifying only the parities, and not the spaces, avoids the category error: (-1)^k commutes with both U(3) and so(2,4).
- **Kill condition (pre-registered):** the lead dies if no stored or derivable map carries the twistor chirality of the conformal spinor's own Fock module to the label copy's k-parity, or if the composite's spacetime handedness on the n = 0 sector is shown to come from a conformal spinor other than its pair factor. In either case Lead B only restates the su(4) clause.
- **Gain even if killed.** Lead B removes the circular-looking dependence on "the chain, derived under (S)". The su(4) half of Pati-Salam suffices (computed), and the store already lists su(4)⊕su(2)_L⊕u(1) as deciding.
- **Ledger:** essential. The twistor halves come from the completion's Cl(2,4) Fock model.

### Lead C. Clause (f) is a Klein convention on V (STRONG for (f); computed plus argued; standard Klein transformation, cited from memory: Klein 1938, Araki 1961)
- **Entities:** `synthesis.even-slots-need-a-spectator-generator`(iii) (already uses the replacement s_i → s_iΓ_W), `standard-model.automorphisms-preserve-slot-pair-split-are`, `standard-model.slot-module-hypothesis`(f). Subjects: standard-model, tower, standard-algebra.
- **What it supplies.**
  - Under (a), the slot operators a and the Klein-twisted operators a(-1)^k obey the same CAR, U(2) covariance and generation.
  - Computed:
    - Jordan-Wigner slot Majoranas anticommute with the pair Majoranas.
    - The untwisted ones commute.
    - The slot-slot and pair-pair bivectors (the 21 Pati-Salam generators) are identical in both conventions.
    - (-1)^N anticommutes with both conventions' slot operators.
  - Argued: the twist factor is unique up to sign. K(-1)^k commutes with End(F)⊗End(ΛW) = End(V), so it is a scalar.
  - So on V, "slots and pairs form one Clifford system" is an existence statement that holds canonically. Cl(10), Spin(10) and the cross bivectors are the operators built from the twisted slots, and every operator on V is the same set in both conventions.
  - The Pati-Salam clause and the grading clause are Klein-invariant, so the qualifier "once the slots are fermionic, so that (f) applies" can be dropped.
- **What remains.** (f) still has content relative to an embedding of the slot operators in the tower (tower parity, the no-spectator route), but not on V.
- **Kill condition (pre-registered):** some result in the future cone of (f) whose statement changes, beyond an overall sign, under a → a(-1)^k (that is, one that uses the slot operators as tower elements).
- **Ledger:** absent.

### Lead D. Rung-2 spinor module (PLAUSIBLE, already known to the store)
- **Entities:** `rungs.rung-spinor-module-mixings`(1)-(3), `note.rungs.abstract`.
- **What it supplies.** Λ•(W⊕C²) is the irreducible module of the second rung above Cl(2,4). It would supply (a), the unique vacuum, (G), (f) (all ten generators are vectors) and the chirality as the rung pseudoscalar's grading.
- **Obstruction.** That reading puts colour on the twistor's own pairs, which `pair-mixing-not-colour`(ii) forbids. The note also records that the rung's U(2) mixes chirality. It survives only in the parity-only form of Lead B. I list it so that it is not re-proposed.

## 3. Obstructions and independence evidence
- **Proved.** The vacuum-swapped halving satisfies CPT, anomaly freedom, (G), the light-ray count and the CPT antiunitary. The bit is therefore independent of those clauses.
- **Computed.** With the gauge group alone there are 4 anomaly-free halvings that conserve N. Adding either su(2)_R or the even pair algebra cuts this to 2.
- **Argued; the Z2 analogue of the seventeenth refutation.** The swap Ω↔Ω^⊤ commutes with every structure that is blind to the bit. The bit is derivable exactly from structures the swap breaks: pair creation in the slot or the pair factor, the conformal action on the pair factor, or the joint grading. No structure in thermality, entropy, descent or the walls subjects breaks the swap, because all of them see only N-conserving or count data.
- **Obstruction to Leads B and D.** `pair-mixing-not-colour`(ii) forbids identifying the colour space with the twistor's own pair space. Only a parity identification is open.

## 4. Links
- **op.r-premises-external, op.deposit-state-is-hadamard:** no bridge found. Their (N+) ground states and Hadamard selection involve only N-conserving quasi-free data, which is swap-invariant and statistics-neutral; `field-theory.twistor-attachment` notes that KMS does not fix statistics.
- **op.helicity-per-boundary-mode, op.residue-killing-weights:** the count is blind to the bit (proved). Lead A shows these counts carry no b > 1 vectorlike doublets.
- **op.qft-structural-inputs:** Lead A turns "one doublet" into the Fock structure of second quantisation, and the generation number stays free (`slot-module-makes-the-faces...`). Attack route 4 (Spin(12) 32 at three constituents) is already answered by CPT closure (1), which excludes n ≥ 3, and by the stored faces results.
- **The orientation bit (dark-matter, quantum-fields):** Lead B's parity identification is the same missing theorem that fixes ε, given the unit sign.

## 5. Rejected candidates
- Univalence superselection (`singularity.p-univalence`, `synthesis.univalence-from-even-stationary-dynamics`): this grading is (-1)^N, but chirality is not superselected (mass terms are odd), so it cannot be imposed as a selection rule. It only restates the grading clause.
- Spin-statistics (`synthesis.locality-of-the-attached-free-fields-fixes-their-statistics`, wedge reflections): it would give slot exclusion, which (G) plus CPT already force. Nothing missing is supplied.
- Graded vs ungraded KMS (`singularity.two-kms-functionals-sign`): swap-invariant.
- The Krein form (`synthesis.krein-form-premise-...`): it concerns gauge fields and ghosts, with no halving content.
- Walls and residue gradings (`sheaf.*`, `odd-extensions.*`): these concern signature and orientation of degenerations. No map to the five-mode module.
- Light-ray and entropy counts: blind to the bit (stored).
- A rotor clause ("Γ in Spin(10) up to phase"): it is inside the u(5) torus, which is blind. Not pursued.

## 6. Subjects walked
standard-model, tower, quantum-fields, conformal-spacetime, descent (singularity, univalence), thermality, entropy, clifford-structure, completion, one-relation, walls, generations, dark-matter, standard-algebra, lepton (constituent hypothesis).

## Memory
I used no facts from memory.
