# GA rewrite round 2, kind = matrices

**List.** ga2_matrices.txt has 33 ids. I added 22 reader-named ids:
- R11: note.rule2.setting-machine-verification.
- R06: field-theory.mass.
- R04: the four synthesis.rung-field-* entities.
- R08: synthesis.eviction-deficit-against-page-deficit, synthesis.imported-haar-average-purity, synthesis.imported-haar-moments-of-random-pure-state, singularity.l-stabiliser-tangent.
- R09: singularity.p-reduced-metric-level-reading-many, obj.singularity.multi-mode-descent, the two T05 notes, the two three-routes entities.
- R05: note.dark-matter.r1-against-series-mass-formulas.
- R02: the five entities with \C stand-ins.

That makes 55 in all. rule2.imported-gamma-matrices-odd-dimension is on ga2_gravity.txt, so I left it to that rewriter.

**Checks.** galang.scan finds no unexcused stand-in on any of the 55, and latexcheck finds no structural or macro problem.

The filtered `tp check --layers 1,2,3 --author leon` reported five E206 errors. These entities had been bumped before this run (in the units pass), not in this run, so the version-keeping rule did not apply to them. I fixed them by bumping their versions: singularity.l-stabiliser-tangent 6 -> 7, synthesis.majorana-scale-free-on-pati-salam-route 4 -> 5, synthesis.rung-field-d-term-... 4 -> 5, synthesis.rung-field-level-needed-... 3 -> 4, synthesis.rung-field-on-the-lift-locus 3 -> 4. The lock comparison behind E206, re-run on every id, is now clean. Apart from those, only I213 findings remained.

The rule I used: "kept" means the version is already above the store lock, that is, the entity was bumped in this run.

## Rewritten

- **Weak generators as Clifford elements.** synthesis.rung-field-on-the-lift-locus 3 -> 4, rung-field-d-term-action-and-tree-masses 4 -> 5, rung-field-level-needed-off-balance 3 -> 4. The weak generators written with Pauli matrices become elements of the algebra built from the slot generators E_ab = v_a w_b: T_1 = (I_4/2)(E_45 + E_54), T_2 = (1/2)(E_45 - E_54), T_3 = (I_4/2)(E_44 - E_55), Y = (I_4/2)(E_44 + E_55). This is R04's proposal. The matrices on the coefficient doublet stay as a labelled reading, and the d-term proof's moment maps stay in that reading. Verified in Cl(2,2) and by the matrix identities.
- **Graphene Fact restated.** rule2.imported-graphenes-two-valleys-doubling 1 -> 2 (imported, kept): the two valleys are the two inequivalent representations of Cl(1,2). Their frames differ by the sign of one spatial vector, equivalently by the sign of the central pseudoscalar I_3. The source's form is in source_formal. Verified.
- **Pauli strings written in the mode algebra.** singularity.p-reduced-metric-level-reading-many 6 -> 7 and note.singularity.setting-step-5-descend-state-what-2 1 -> 2: X_{R1}X_{L1}Z_{L2} becomes (v_{R1} + v_{R1}*)(v_{L1} + v_{L1}*) sigma_{L2}, keeping the qubit label as a reading up to the Jordan-Wigner string. obj.singularity.multi-mode-descent 1 -> 2: Z_{R_k}Z_{L_k} becomes sigma_{R_k} sigma_{L_k}, which is exact because Z = -sigma. Verified in Cl(3,3).
- **The complex field tied to its unit.** One parenthetical at the first use of \C:
  - span{1, I_4}: synthesis.eviction-deficit 3 -> 4, eviction-keeps-one-replica-saddle 2 -> 3, imported-haar-average-purity 1 -> 2, imported-haar-moments 1 -> 2 (both imported; the formulas are unchanged), majorana-scale-free-on-pati-salam 4 -> 5, geometric-modular-conjugations (5, kept), note.neutrino.setting-introduction 1 -> 2, note.standard-model.setting-levels-results-successor-problems 1 -> 2.
  - span{1, J}: point-spectrum (5, kept), q-splits (6, kept), r-le-i (5, kept), singularity.l-stabiliser-tangent 6 -> 7.
- **field-theory.mass 4 -> 5:** the epsilon pairing lambda^T epsilon lambda is labelled "in two-component form, a labelled reading" (R06).

## Declared, text unchanged

- **Bridge, as R11 proposed** (each 1 -> 2): note.rule2.setting-setting-what-imported, note.rule2.three-dimensions-matter-below, note.transport.three-dimensions, note.rule2.what-planar-obstruction-physically, note.rule2.setting-machine-verification. The last one is flagged only because it cites the gamma-matrices Fact by its id.
- **Bridge:** note.dark-matter.r1-against-series-mass-formulas 1 -> 2. It computes explicitly with Hermitian gamma matrices; the GA current would be a different computation.
- **Bridge:** tower.structure-tower-c-norms (10, kept). The C*-norm comes from the tensor-Pauli matrix representation, and R12's Fock route would be a different proof.

## Not rewritten

- **Mass, family, density and numerical matrices, which the conventions allow.** Here "Dirac matrix" means the Dirac mass matrix and "Fermi-Dirac" is a name.
  - hawking.imported-modular-descent-premises-geometric-normalisation, singularity.modular-descent, neutrino.breaking-relation
  - standard-model.fits-record-level, standard-model.neutrino-dirac-matrix-charged-fermions
  - synthesis.circulant-charged-leptons-..., synthesis.hypothesis-u-readings-..., synthesis.hypothesis-u-under-ew-...
  - synthesis.majorana-scale-free-input, synthesis.stored-fits-are-models-of-not-u, synthesis.untuned-fit-caps-...
  - synthesis.cabibbo-... (R08 already wrote the Pauli reading as a paravector)
  - synthesis.phase-flow-... (a 2 x 2 numerical matrix of ad_H)
  - synthesis.twistor-form-states-... (a numerical model matrix)
  - note.standard-model.setting-contribution, note.state-selection.setting-gap-stated-exactly
- **Already GA, or the name is not a stand-in.**
  - field-theory.second-quantisation ("Pauli-Jordan" is a function's name)
  - synthesis.series-content-... (Pauli-Villars), synthesis.imported-free-field-spin-statistics-... (Pauli the person; I_5 is named)
  - synthesis.massive-dirac-..., synthesis.eviction-keeps-one-of-catalan-... (the "Pauli algebra" is Cl(3,0); the unit is named)
  - synthesis.boost-evolution-... (says which unit acts)
  - odd-extensions.mirror-inside-complexified-... (the complexification is its subject, and the unit is named)
  - rule2.rule-2-plane (declared bridge by R11)
  - synthesis.rung-field-charged-pair-... (\C = span{1, I_4} is already defined)
  - synthesis.phase-flow-... (V_\C = V + JV is defined in place; that answers R02's item)
  - three-routes.class-relative-no-go, three-routes.support-preserving-families-quantise-without-hopping (sigma_x, sigma_y are the parity sections at the points x, y, not Pauli matrices)
  - note.singularity.setting-machine-verification (describes the script's qubit simulator)

## Reader items on round-1 entities (written after ga-matrices.md)

- **R11 item 1, std-algebra.sta-matrix** (2, kept): the Pauli blocks are now sigma^P_k, distinct from the relative vectors sigma_k, and the pseudoscalar is I_4.
- **R11 item 2, obj.std-algebra.spacetime-algebra** (2, kept): the pseudoscalar is I_4 in the formal level and the one-liner.
- **R02 item 2, synthesis.normality-...** (4, kept): the inversion rotor J is renamed R_inv. I left nu as it is; renaming it needs the attachment's frame (for Leon). R02 item 1 is an edge change, for Leon.
- **R07, note.mass.what-nullity-fixes:** consistent as it stands. It uses I_6 only, and makes no claim about the I_6/I_7 sign.
- **R12, tower.compatibility-connecting-maps-transported:** kept as declared bridge. The candidate corrector in T_{k+1} would need its own verification. Its users quote V_k.
- **R06:** no item on my round-1 entities.
