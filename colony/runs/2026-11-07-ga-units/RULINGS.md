# Leon's rulings on the GA-units sweep (7 November 2026), and the consistency pass

Read SWEEP.md first: its bookkeeping rules (version + 1 when formal or proofs change, credit entry,
extraction note, keep every file, no change of mathematics, no change of links, statuses or ledgers,
validation with tp check layers 1-3) apply unchanged. outside_ga is not a substantive field: adding or
removing it alone needs no version bump. The sweep reports sweep-*.md (in this folder) list what each group
did and its "Unsure" items; this pass makes the store follow the rulings below, one reading everywhere.

R1. Boundary-mode, atom and window flows keep i. The Hawking boundary-mode algebra
    (obj.hawking.boundary-mode-algebra-windows-boost-dynamics), the completed-pair atom of T05
    (singularity.modular-structure-completed-pair and its users), window algebras and the flows on them
    (Ad(e^{itK}), Ad(e^{it sigma/2}), their modular groups and KMS continuations) keep the bare i, declared
    `outside_ga: {kind: complex-analysis, why: ...}` (their mode operators anticommute with I_4, conventions
    known limits 1 and 2, so a left I_4 is wrong there and the store does not fix their unit). Revert every
    conversion of these to I_4 made by the sweep (known: synthesis.point-spectrum-boost-admits-no-half-sided-
    translations, the s-wave entity and synthesis.q-splits-maximum-entropy-affine-weights from sweep-A2,
    synthesis.quadratic-flows-cannot-thermalise-descent from sweep-D1; find any others), restoring the
    original text of those passages exactly (git show 8eef5a4:<path>) and keeping any unrelated conversion in
    the same entity that the other rulings allow. If an entity ends with its formal level and proofs identical
    to 8eef5a4, set its version back to the 8eef5a4 version and drop the credit entry and maintainer_pass note
    the sweep added (declaration only).

R2. The horizon's continuum mode space and the Hadamard chain carry I_4 throughout. The modes of a horizon
    generator in (N+) (synthesis.n-plus-null-ground-state), obj.hawking.continuum-mode-space, the null vacuum
    and its kernel, the generator kernels and the Dirac Hadamard chain (the restricted Dirac field, whose
    values are even with unit I_4, obj.field-theory.single-algebra-field): write I_4 everywhere, the
    momentum P = I_4 d/du, W_0 = (I_4/2 pi)(u - v + I_4 0)^{-1}, modular groups Delta^{I_4 t}, Klein twists
    (1 + I_4 Theta)/(1 + I_4), one unit per entity. On a Dirac numerator that is not even ((I_4 D + m_0) on a
    bispinor kernel) the unit is the right unit: write it on the right, as SWEEP rule 1 says. Keep i only in
    an i0 shift of a spacetime vector (Q(y - y' - i0 e_0)), declared complex-analysis with that reason. Where
    obj.hawking.continuum-mode-space is described as having the boundary-mode algebra as its countable case,
    say that the boundary-mode algebra keeps its own unit (R1). synthesis.modular-data-on-a-generator-fix-
    neither-the-translation-lift-nor-the-sign-of-i: write I_4 and reframe its "if the field's i is read as J"
    wording as a statement about J = I_4 B without changing what is claimed.

R3. The T12 slot and pair module, the families' face space and the palatial Fock space are written over
    span{1, I_4}, read on tower floors (where I_4 commutes with every tower-plane vector). State once per
    entity: "numbers and the module's complex structure are read in span{1, I_4}, the module read on the
    tower's floors, where $I_4$ commutes with the tower vectors". This reading is notational; do not claim that
    it derives anything about Hypothesis (S). Convert the entities that were declared only because of the
    plain complexification of this module (sweep-C1's seven `other` declarations, sweep-C2's palatial
    positive-energy and seed entities, note.dark-tower-matter.neutral-row, the Majorana generator of the
    quasi-free deposit if its modes are tower modes) and remove their declarations if no bare i remains.
    Twistor components keep the conformal-spinor unit, right multiplication by I_6 (do not change those).

R4. One unit per entity: contour integrals, Fourier kernels, scalar mode functions (Bunch-Davies, Hankel
    Wronskians, the normalisation phi phi-dot* - phi* phi-dot), Mellin inversions and KMS strips inside an
    entity whose results use I_4 are written with I_4 too (span{1, I_4} is the complex numbers, so this is
    exact). Keep i only for complex analysis in its own right (theta functions, modular forms, the Jacobi
    q = e^{2 pi i tau}) and for the cases R1 and R2 keep. Remove sentences like "written with i for the unit
    I_4" once the entity is converted.

Not changed by this pass: complexifications that must commute with spacetime vectors (complex null
vectors, Cl(2,4)_C tube points m = x + iy, V_C of spacetime), imported Facts quoted in their source's
language, Penrose's bridge notes, the Pati-Salam defining-representation phases declared bridge.

Report: colony/runs/2026-11-07-ga-units/consistency-<name>.md, one line per entity touched (old -> new
version, which ruling, what changed), and anything that could not be done exactly.
