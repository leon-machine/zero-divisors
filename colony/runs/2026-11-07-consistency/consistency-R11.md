# Consistency pass R11: completion, clifford-structure, standard-algebra, zero-divisors

Reader R11, 7 November 2026. 339 entities (150 claims, 31 objects, 158 notes) from read_R11.txt.

## What was read in full
Every entity on the list, in dependency order (objects, then claims, then notes): the formal, technical,
lay and one-liner levels, every proof file (all derivations, including the second derivations of
primer.classification-real-clifford-algebras and synthesis.blade-square-signs-f2-quadratic-form), the
uses / assumes / about / comments_on / equivalent_to / specialises pins with their current versions, and
the extraction block of every entity. Dumps were made by script (14 chunks, about 930 KB, plus a 139 KB
extraction dump) and each chunk was then read through completely; scripted scans (house style,
undeclared macros, pins, galang) were used as aids only. Every sign and constant slip reported below
was recomputed by hand and, where it bears on a statement, in exact arithmetic with lib/GA.py
(scratch: R11/v/verify_r11.py).

## Fixed (24 entities; 23 with version + 1, 1 one-liner only)
- obj.transport.equivariance 1 -> 2: tau was used undefined; its definition (T01 eq. tau, stored as primer.twisted-adjoint-action) stated and cited, formal and technical.
- sheaf.blade-basis-degenerate-forms-included 4 -> 5: "blades e_I" of a non-orthogonal basis named as ordered products (obj.std-algebra.blade reserves blade for outer products); proof: "both operations are anti-derivations" corrected (only contraction is).
- conformal.blade-basis-persists-under-degeneracy 4 -> 5: same notation clarification.
- std-algebra.bivector-exponential 3 -> 4: unit vectors written hat-a, hat-b (hat is the grade involution) renamed a_1, b_1.
- transport.no-go-level-elements 4 -> 5: proof declared hat the grade involution and then wrote the normalised u as hat-u; renamed u_1.
- std-algebra.periodicity 1 -> 2: Cl(1,0) idempotents written e_+, e_- (the store's hyperbolic-plane vectors) renamed P_pm; Hamilton units in bold (roman i read as a bare imaginary unit).
- dark-matter.two-families-are-two-chiralities 6 -> 7: proof (i) "U(Rf) = +-R(Wf)R^{-1}R" garbled, now +-(RWR^{-1})(Rf) = +-R(Wf) = 0; clause added that here w_i annihilate and v_i create, the reverse of std-algebra.witt-basis-car's reading.
- transport.corner-even-subalgebra 4 -> 5: formal level used A, eps_pm, B_gamma with no hypotheses; the standing hypothesis p - q = 1 mod 4 (already in technical and one-liner) stated. No edge.
- std-algebra.complexification-is-the-odd-extension 1 -> 2: even subalgebra written Cl^0(W) against obj.std-algebra (Cl^0 = R, Cl^+ even); now Cl^+.
- transport.rule-1-morita-trivial 5 -> 6: proof chain "ff* f ff* = f f* Q(f) f* = f ff*" had a wrong middle term, now (ff*f) ff* = f ff* = 0 (GA check: E11 f E11 = 0, ff*f = f); "ff* a = a ff* (evenness)" now says the evenness is that of ff*.
- transport.group-null-rotations 4 -> 5: proof cited no-go Step 2 for Spin^0 membership, which covers Q(u) != 0 only; null u covered by the group law.
- odd-extensions.doubling-or-complexification 5 -> 6: bare i in the proof ("x (x) (a + bi)") and abstract C in (ii) written with the central omega (U3, span{1, omega}); GA check omega central, square -1 in Cl(1,2).
- one-relation.imported-square-roots-real-clifford-algebras 1 -> 2: citation typos (Abamowicz -> Ablamowicz, Birkh"auser -> Birkhaeuser).
- one-relation.imported-witts-extension-theorem 2 -> 3: citation typo K"orpern -> Koerpern.
- std-algebra.rotors-beyond-exponentials 2 -> 3: proof (ii) named e_1e_2e_3e_4 of a (2,2) block I_4 (store's reserved unit, square -1; this element squares to +1, GA check); renamed omega_4.
- sheaf.imported-classification-values 4 -> 5: \mathbb{C} -> declared macro \C (it names an algebra type).
- rule2.rule-2-plane 3 -> 4: convention mixing (time of square -1 here, "spacelike" = square -1 in the cited theorem) said in technical level and proof; outside_ga bridge declared (the existing "time gamma matrix" comparison, W222 once touched), as in rule2.rule-2-kaluza-klein-algebra.
- obj.singularity.fibrewise-conformal-lift 2 -> 3: still (T_pM, g_p), Q_p = g_p(x,x) while its user singularity.transport-schwarzschild-fibre is in GTG; restated with Q_p(x) = Q(hb^{-1}x), Q*_p = Q(hb^T xi), g_p as the derived reading.
- note.primer.setting-blades-grades 1 -> 2: "a fact the series needs exactly once" stale (T1 twice, T2 and T4 throughout).
- note.transport.setting-quadratic-spaces-clifford-algebras 1 -> 2: "which we need once" stale (also the gamma = 0 ascent).
- note.conformal.setting-position-series 1 -> 2: "No later paper depends on this note's theorems" stale (T14a Fact 8.1, synthesis.nilpotent-steps).
- note.rule2.setting-position-series 1 -> 2: "Nothing downstream depends on this note" stale (five synthesis results use rule2.*).
- note.rule2.setting-what-has-been-exercised-what 1 -> 2: pointer added to the later conditional answer on the sign of nu^2.
- std-algebra.even-subalgebra-isomorphism (no bump): one-liner dropped the hypotheses q >= 1, p >= 1.

Validation: tp check layers 1-3 after the edits: no error or warning on any R11 entity (the one W222 the
first run showed, rule2.rule-2-plane, is fixed by its declaration); only I213 informational lines remain,
as in the baseline. The version bumps leave pins behind on dependents; all changes above are wording or
proof repairs with the statements unchanged, so every dependent still holds and the pins can be moved
(`tp repin`) after Leon's review. Dependents outside R11 that pin a bumped entity: see the list at the end.

## For Leon
1. rule2.where-obstruction-sits-commuting-square (c), formal and technical: "f = 1/2(nu +- e_{n+1}), f* = 1/2(nu -+ e_{n+1}) (signs chosen so that each is null)". In the timelike case (nu^2 = -1, e_{n+1}^2 = +1) this gives ff* + f*f = -1, not 1 (GA.py: -1 with nu first, +1 with e_{n+1} first; spacelike case +1); its own proof uses f = 1/2(e_{n+1} + nu). Your wording fix of 2026-10-23 corrected exactly this in the equivalent transport.where-obstruction-lies-commuting-square (c); the rule2 twin was not updated. Proposed fix: copy the transport text, "f = 1/2(u +- w), f* = 1/2(u -+ w), with u the adjoined generator of square +1 and w that of square -1 (both combinations are null; the opposite signs make ff* + f*f = 1)", formal and technical; version 5 -> 6.
2. Store-wide notation: about 25 T01/T03/T14a/T17-rule2-region entities write Cl^0(p,q) for the even subalgebra, while obj.std-algebra.grade-projection defines Cl^0 = R (grade zero) and obj.std-algebra.even-subalgebra writes Cl^+. Proposed: one sentence in store/conventions.md (Notation): "The T01-derived regions write Cl^0(p,q) for the even subalgebra Cl^+(p,q); Cl^0 for grade zero is the standard-algebra objects' usage." (cheaper and safer than renaming 25 entities).
3. Duplicates without links (see below): proposed equivalent_to edges, a Leon decision.
4. tower.morita-equivalence-algebra-amplification is imported (Lam) although std-algebra.morita-amplification (iii) proves the same statement in the store: proposed a derivation from std-algebra.morita-amplification@1 (status imported -> proved), or equivalent_to.
5. one-relation.imported-square-roots-real-clifford-algebras: "in Cl(1,3) every square root of -1 is conjugate to one of a short list" is vaguer than what the store proves (std-algebra.square-roots-of-minus-one: one class, all conjugate to I). Proposed: "... is conjugate to the pseudoscalar (one class; std-algebra.square-roots-of-minus-one)".
6. note.conformal.abstract comments only on conformal.blade-basis-persists-under-degeneracy; proposed comments_on conformal.minimal-nondegenerate-completion (the abstract's subject).
7. singularity.transport-schwarzschild-fibre still uses differential forms (dr, dt_s, dt_PG, the weighted coframe) and cometric components (g^{-1})^{tt} in formal (4) and the proof, but is on no GA list (the detector missed it); see ga-issues-R11.md. Needs a GA rewrite or an outside_ga declaration.
8. Undeclared GA stand-ins in entities not owned by the rewriters (galang unexcused, warning only for a maintainer): rule2.imported-gamma-matrices-odd-dimension and rule2.imported-graphenes-two-valleys-doubling (proposed outside_ga imported), note.rule2.what-planar-obstruction-physically, note.rule2.setting-machine-verification, note.rule2.setting-setting-what-imported, note.rule2.three-dimensions-matter-below, note.transport.three-dimensions (proposed outside_ga bridge: they name the gamma matrices of the physics they compare with).
9. Minor naming clashes left as they are (not worth a version each, listed for a later notation sweep): synthesis.cpt-conjugation-pseudoscalar-rotor-times-complex-conjugation and synthesis.positive-energy-selects-rule-2-sign use J for a complex structure (conventions reserve J = e_2e_3) and the cpt result uses bare I for a vector; rule2.rule-2-kaluza-klein-algebra and note.rule2.setting-five-dimensional-kaluza-klein-algebra write gamma for the spacetime pseudoscalar (the store's I_4; gamma_mu are frame vectors); transport.totality's proof uses J for a map; dark-matter.residue-soldered-invariant-not-algebraic-one writes Mat(2, \mathbb{H}) for \Mat_2(\HH); singularity.pseudo-inverse-identities-hyperbolic-atom's extraction unit_note still says "the imaginary unit here stays a scalar i", though no i remains in its levels.

## Duplicates
- conformal.witt-extension-theorem (T02 Fact 2.2, imported) = std-algebra.witt-extension (imported) = one-relation.imported-witts-extension-theorem (already equivalent_to std). Keep std-algebra.witt-extension; add equivalent_to std-algebra.witt-extension@1 on the conformal entry.
- std-algebra.complexification (ii) = odd-extensions.doubling-or-complexification (i), (ii) (odd n, omega^2 = +-1); no link. Keep both (paper result and core result); add equivalent_to or a restatement edge.
- odd-extensions.doubling-or-complexification (iii) = std-algebra.even-subalgebra-isomorphism = transport.even-subalgebra-one-dimensional-extension = rule2.even-subalgebra-one-dimensional-extension (the last three linked; the first not).
- odd-extensions.volume-element-odd-dimension restates primer.centre and primer.sign for odd n without a link (its typing note says so).
- std-algebra.zero-divisors-annihilated (d), (e) = transport.exhaustiveness-every-zero-divisor-annihilated-idempotent (1) and the consequence clause of transport.regularity-localises-zero-divisors-idempotents; no link. The std-algebra version is the better general statement; the T01 ones carry the explicit e = xa.
- tower.morita-equivalence-algebra-amplification (imported) = std-algebra.morita-amplification (iii) (proved): see For Leon 4.
- Restatement chains already linked and fine: blade basis (std -> sheaf -> conformal), splitting (primer -> transport), centre, sign, classification (primer -> transport; std-algebra.periodicity proves it), Rule 2 facts (transport -> rule2).

## Known open items
None of the six listed open items falls in R11's subjects (they are on R01, R02, R08 and R10's lists).
note.correspondence.abstract, which is on R11's list, says Penrose's unit is written I_6, which is
consistent with the orientation statement now in correspondence.incidence-relation-chart (R10).

## Checks made with no defect found (selection)
Signs and constants recomputed: conformal lift conventions (n0.ninf = -1 in T01/T02/primer with
n0 = (e_- - e_+)/2, ninf = e_- + e_+, e_+ n0 e_+ = -ninf/2; T09 setting n0.ninf = +1 noted in its own
note); the no-go shear R w0 R^{-1} = w0 - u - Q(u)v and every Step 3 term; Gauss-sum table of
synthesis.blade-square-signs (both scalar-part tables); positive-energy centres; cpt Witt flag Gram
diag(4,-4,-4) and the exchange component -3/4 I_7 e_1; rotors-beyond eigenvalues 1/4, 4; Schwarzschild
Q*_p(k) = -r and k^sharp = -sqrt r e_r; density paths; embedding-independent minimality case analysis;
classification tables; Fock and Chevalley pairing signs; pure-spinor Thouless annihilators; matrix-unit
relations (Rule 1, Rule 2, Cl(1,1)); exotic embedding H -> Mat_2(span{1, I_5}).

## Counts
Read 339 (150 claims, 31 objects, 158 notes). Changed 24 (17 claims, 2 objects, 5 notes; 23 versioned,
1 one-liner only). For Leon 9. Duplicates 6 groups. Open items settled 0 (none in subject).
GA issues recorded 3 (ga-issues-R11.md). Cross-subject items 0 conflicts (xsubject-R11.md).

## Dependents outside R11 that pin a bumped entity (for repin after review)
transport.group-null-rotations: angle.imported-conformal-model-null-rotations, synthesis.kerr-ring-connection-limit-null-rotation-winding-three, synthesis.killing-horizon-value-factor-is-the-generator-boost.
std-algebra.complexification-is-the-odd-extension: angle.wedge-reflection-translations-are-ascent, singularity.euclidean-rotor-where-it-lies, synthesis.collar-isotropy-selects-t-boost.
sheaf.blade-basis-degenerate-forms-included: sheaf.degeneration-sheaf, sheaf.exceptional-algebra-deformation-normal-cone, sheaf.function-linearity-tame-constructions, sheaf.local-freeness-constant-rank, sheaf.localised-transport.
transport.no-go-level-elements: correspondence.imported-stabilisers-flat-model.
dark-matter.two-families-are-two-chiralities: dark-matter.flag-bit-exists-exactly-tower-dimension, dark-tower-matter.three-dimensional-content, synthesis.oriented-causal-towers-mirror-pair-every-window, synthesis.z-adapted-witt-flags-energy-sign-follows-the-flag-bit.
transport.rule-1-morita-trivial: tower.commuting-copies, tower.compatibility-connecting-maps-transported, tower.grade-twist-when-it-inner, tower.structure-tower-c-norms, transport.pinching-kernel.
std-algebra.bivector-exponential: hawking.modular-structure-completed-pair, odd-extensions.boost-dilation-ratio-gauge, one-relation.third-constant-conversion-constant-between-charts, singularity.modular-structure-completed-pair, synthesis.boost-stationary-incidence-vacua-read-interval, synthesis.de-sitter-horizon-translation-is-conformal-null-rotation, synthesis.positive-conformal-energy-gives-positive-null-translations, synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom.
odd-extensions.doubling-or-complexification: odd-extensions.four-extensions-oriented-pair, odd-extensions.mirror-inside-complexified-extension-absent-doubled, odd-extensions.twistor-algebra, odd-extensions.two-towers-one-curved-universe, synthesis.mirror-extensions-causal-convention.
std-algebra.periodicity: one-relation.overlap-table-sorted. one-relation.imported-witts-extension-theorem: one-relation.spacetime-manifold-vacuum-lines, one-relation.third-constant-conversion-constant-between-charts, one-relation.two-capacities-three-consequences. sheaf.imported-classification-values: sheaf.degeneration-sheaf. rule2.rule-2-plane: synthesis.mirror-extensions-causal-convention.
(Within R11 the same holds for about 35 pins; all safe to move for the same reason.)
