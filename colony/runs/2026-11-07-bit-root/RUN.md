# Run 2026-11-07-bit-root: what is specific to this run

LAB = /home/claude/phys-graph. Run folder: colony/runs/2026-11-07-bit-root/ (findings/, work/<name>/, verify/).
Read colony/BRIEF.md and colony/POLICIES.md; this file overrides them where they differ. Baseline (store at 9562306):
0 errors, 0 warnings (baseline.log).

## Aim
Leon (7 November 2026): file "the bit assumption that drives direction and difference leading to scalars" into the graph
as its root: the bit as the root premise, the Clifford algebra over Z and Q derived from it, the continuum as one named
premise, and the existing algebra results re-rooted underneath. Source: Leon's working document "From the Bit to the
Numbers" (text in work/bit_doc.txt). It grades its steps: four CHOSEN primitives, PROVED steps, ARGUED readings.
Only proved steps become claims; chosen primitives become postulates; argued readings become notes.

## Leon's standing rules (binding)
- Everything in geometric algebra (Clifford-algebra objects, not matrices or index tensors, where a GA form exists).
- Derive, do not import: a result that would otherwise be imported is derived inside the entity; literature is prior
  art in the extraction note only. Do not create imported Facts. Where this run derives what an existing imported Fact
  states, say so in the extraction note (name the Fact); the maintainer decides what happens to the Fact.
- No imaginary unit: use the unit principle (store/conventions.md, "The imaginary units", U1 to U6).
- House style: no em dashes; never "honest"/"honestly"; never "load-bearing"; Q(v) for squares; no agent or run names
  in store text. Abstracts are not needed; levels formal, technical, lay, one-liner as in BRIEF.md.

## The four primitives (postulates, status: postulate; each its own entity, short, exact)
- (B) The bit: a distinction, two states 0 and 1, combined by comparison (1 + 1 = 0): the group Z_2, and with "both"
  the field F_2. Independence: n distinctions, configurations F_2^n under symmetric difference.
- (S) Minimal non-commutativity: the directions generate a group G with a central element c of order dividing 2 such
  that G/<c> = F_2^n (S -> e_S), and distinct directions do not commute (e_i e_j = c e_j e_i, c != 1).
- (L) Superposition: configurations add; the algebra is the group ring of G with the sign bit acting as -1, over the
  integers (Z[G]/(c + 1)). (Choose the coefficient ring carefully: the doc says "over its coefficients"; this run
  starts with Z, the ring the unit generates, and reaches Q by a theorem, below.)
- (C) Completion: the coefficients are completed to the real numbers (with the store's existing real definition
  recovered). State exactly what is assumed (an ordered field that is complete) and nothing more.
Phrase each postulate so that it is a mathematical primitive of the series' foundation, not a physical postulate, and
say so in its lay level. NOTHING already in the store may cite these postulates in `uses` in this run (that would change
every premise count in the store); the link to the existing algebra is made by the bridge result below and by lineage
(motivated_by) only. Re-rooting through `uses` is a decision for Leon at close-out.

## Results to derive (proved, exact checks with lib/GA.py and Fractions; integer arithmetic where the claim is over Z)
Filer A (premises B, S, L; results A1 to A3):
- A1. From (B) and (S): c^2 = 1 and c is the unique non-trivial central square root of 1 in G; every e_i^2 is 1 or c and
  central; the squaring map is a quadratic form q on F_2^n with polar form the commutator form; for even n, G is an
  extraspecial 2-group (centre = commutator subgroup = {1, c}); for odd n the centre is {1, c, e_N, c e_N}. Check the
  store first: synthesis.blade-square-signs-f2-quadratic-form already proves clause (i) (c^2 = 1 from symmetry) and the
  F_2 form; do not refile it: cite it and add only what is new (the group-theoretic premise form, extraspecial, centre).
- A2. From (L): the ring Z[G]/(c + 1) is free over Z of rank 2^n with basis the blades e_S; for v = sum a_i e_i with
  a_i in Z, v^2 = Q(v) = sum a_i^2 e_i^2 (the contraction rule as a theorem); it has the universal property of the
  Clifford algebra of the diagonal form <+-1, ..., +-1> over Z (and over any commutative ring R, after base change): so
  it is Cl_Z(p, q). This derives the first part of the imported Fact
  synthesis.imported-real-clifford-algebras-as-twisted-group-algebras-and-the-arf-invariant; check whether
  synthesis.blade-square-signs-f2-quadratic-form plus A2 derive the whole Fact (the isomorphism classification by the
  quadratic form and the Arf invariant); if so, state it.
- A3. Null pairs over Z: in Cl_Z(1,1) the null vectors n = (e+ + e-)/2 need 1/2; with integer coefficients the null
  direction e+ + e- and its partner give the Witt presentation; cite note.one-relation.two-presentations-differ-over-the-
  integers and one-relation.two-presentations, do not refile. File A3 only if something new and exact remains; else
  record in findings.
Filer B (premise C; results B1 to B4):
- B1. Division gives Q: in Cl_Z(p, q) (n >= 1) the smallest localisation S^{-1}Z of the coefficients in which every
  non-null vector of the Z-span of the directions is invertible is Q (v^{-1} = v/Q(v); m e_1 needs 1/m^2); over Q every
  non-null vector is invertible while null vectors and zero divisors remain (n >= 2 indefinite: exhibit them); grade 0 of
  Cl_Q(p, q) is Q. State precisely and keep it exact; it may be short.
- B2. The completion recovers the store's algebra: under (C), Cl_Q(p, q) (x)_Q R is the Clifford algebra of
  obj.std-algebra.clifford-algebra for the diagonal +-1 form, and every real quadratic space (degenerate included) has an
  orthogonal basis of squares 1, -1, 0 with invariant counts (Sylvester), so every real Clifford algebra of the store is
  one of the ladder's (with degenerate directions realised as null vectors of a larger Cl(p, q) where the store does so).
  Derive Sylvester in GA (the imported std-algebra.sylvester-inertia is then derived; say so). State exactly which
  property of R is used where: diagonalisation to +-1 needs only square roots of positive elements (a Euclidean field),
  not completeness; over Q square classes remain (example: a direction of square 2, and the plane with squares 2 and 3 is
  a division algebra over Q; see synthesis.blade-square-signs-f2-quadratic-form and the store's square-class results).
  So completeness is needed for limits (pi, exp: synthesis.nilpotent-steps-derivative-exponential-and-boost), not for
  the signs. Do not overstate the doc's "Only signs survive in R".
- B3. Frobenius derived in GA: a finite-dimensional associative real division algebra is R, C (= Cl(0,1)) or H
  (= Cl(0,2)). The GA route: the elements of zero trace square to non-positive reals, form a negative definite space,
  generate a quotient of Cl(0, k), and only k <= 2 (or the H quotient of Cl(0,3)) is a division algebra. Exact checks
  where possible (finite instances); the general proof in the proof file.
- B4. Every number system inside: Cl(0,1) = C, Cl(1,0) split-complex, the null direction of Cl(1,1) gives the dual
  numbers, Cl(0,2) = H, Cl(k, k) = M_{2^k}(R); every finite-dimensional associative real algebra embeds in some Cl(k, k)
  (regular representation as a corner). Cite stored results (primer.classification-real-clifford-algebras,
  std-algebra.periodicity, std-algebra.cl11-matrix, std-algebra.matrix-units, std-algebra.complex-clifford-algebra);
  file only what is new. B3 and B4 may be one entity if that reads better.
Notes (filer B writes them, kind note): N1, the grading of the ladder (four primitives, what each step adds, where each
stored result sits); N2, the argued reading "geometric algebra is the algebra of physics" with the doc's evidence table
and its objections, clearly marked argued. Notes carry no checks beyond what BRIEF.md requires for notes.

## Gate and rules
As BRIEF.md: exact arithmetic (Fractions; lib/GA.py; integers where over Z), import GA, premise() per premise,
mutation-sensitive checks (check4 must show no W413); check4.py exits 0 (environmental E401 acceptable) and
validate_draft ok (helper: colony/runs/2026-11-06-edge-normality/verify/final/validate_one.py <proposal dir> <out dir>);
register each proposal with `python3 colony/labcli.py propose_claim @<abs path to draft json>` so it carries
proposal.json. Up to 4 proposals per filer. Credit {name: Claude Opus 5.5, role: proposal and drafting, source: run
2026-11-07-bit-root}. Read your sibling's findings file midway and at the end; never file what they filed (A owns the
premises B, S, L; B owns C). One gate process at a time; 2 CPUs shared; never kill other processes; do not edit store/,
commit, push or spawn agents. Findings: findings/file-A.md, findings/file-B.md (labels proved / computed / argued).
