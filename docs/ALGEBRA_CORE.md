# The algebra core: plan

Status: built 2026-10-26 on branch algebra-core (see Outcome at the end); not yet merged or locked.

## Purpose

A rigorous geometric algebra section at the centre of the graph: the algebra the
series actually uses, stated once, proved in the store with exact checks, and cited
by the programme's results through ordinary `uses` edges. It is the first content
of the `standard-algebra` subject of the `standard` programme (docs/PROGRAMMES.md),
which is empty today.

Not in scope now: geometric calculus (a second pass, once the algebra is in),
KMS and modular theory (`standard-qft`), GTG (`standard-gr`).

## Baseline (build of 2026-10-26, commit 6f878c0)

- 1,081 claims and objects. 446 (41%) reach an algebra node (the 32 nodes of the
  `clifford-structure` subject and the T00 primer) by a logical path.
- 116 isolated (no logical edge either way); 119 weak components, the largest 959.
- 315 claims have no premise at all: 135 imports, 86 proofs, 53 postulates,
  25 conjectures, 16 refutations.
- Of the 86 premise-free proofs, about 30 use only standard algebra that has no
  store entity. The connect pass said so in plain words, for example on
  `primer.commutation-rule`: "the anticommutation of orthogonal vectors and the
  grade involution, which are not store entities".
- 204 distinct import sources; the algebraic ones (Chevalley, Lounesto, Lam,
  Lawson-Michelsohn, Fulton-Harris, Cartan, Thouless, Porteous, ABS, Witt) recur
  across papers as separate records.

## Standard of rigour

- **Own words.** Every statement and proof is written for the store. Textbooks are
  cited as the source in `locators` (book, section, equation), never transcribed.
- **Proved where the proof is short**, which is most of the algebra: status
  `proved`, a `proof-main.tex`, and a `check.py`.
- **Imported, with a check, where the proof is long** (Cartan-Dieudonne, Witt
  extension, Sylvester inertia): status `imported` with `imported_from`, plus a
  check of the finite core, as docs/PROGRAMMES.md asks.
- **Checks are exact and exhaustive over small cases.** Every signature
  (p,q,r) with p+q+r <= 5 (6 where cheap), degenerate forms included, using
  `lib/GA.py`. A check is evidence for the instances it runs, the proof for the
  general statement; coverage.yaml says which.
- **The core checks GA.py.** The first section's checks test the library's
  product, involutions and grading against the definitions, so the library every
  other check imports is itself grounded.
- **Conventions.** Signature order (p,q,r), left contraction as the inner product,
  reversion as the tilde. Each source's conventions are recorded where they differ
  (Doran and Lasenby use the symmetric inner product and their own curvature sign;
  the store's sign stays as decided on 2026-10-23).

## Ids

New entities: `std-algebra.<name>` (claims) and `obj.std-algebra.<name>`
(definitions), `programme: standard`, `subject: standard-algebra`.
The seven `primer.*` results are standard algebra already proved in the store:
they move into the subject (a cosmetic change, no version bump) and keep their ids.

## The entities (about 65)

Listed in dependency order. "Absorbs" means the existing entity moves here;
"links" means it stays where it is and gains an `equivalent_to` or `uses` edge.

### 1. Quadratic spaces
| id | kind | status | existing |
|---|---|---|---|
| obj.std-algebra.quadratic-space | object | defined | links obj.transport.extension-quadratic-spaces |
| obj.std-algebra.signature | object | defined | |
| obj.std-algebra.radical | object | defined | |
| std-algebra.sylvester-inertia | claim | imported + check | |
| std-algebra.polarisation | claim | proved | |

### 2. The Clifford algebra
| id | kind | status | existing |
|---|---|---|---|
| obj.std-algebra.clifford-algebra | object | defined (universal property) | |
| std-algebra.existence-uniqueness | claim | proved (tensor algebra quotient) | |
| std-algebra.blade-basis | claim | proved | links sheaf.blade-basis-degenerate-forms-included, conformal.blade-basis-persists-under-degeneracy |
| std-algebra.vector-squares | claim | proved: v^2 = Q(v), uv + vu = 2B(u,v) | |
| std-algebra.orthogonal-anticommute | claim | proved | |
| std-algebra.functoriality | claim | proved: isometries extend to algebra maps | |
| std-algebra.ga-py-product | claim | proved by check: GA.py's product satisfies the defining relations | |

### 3. Grading and involutions
| id | kind | status | existing |
|---|---|---|---|
| obj.std-algebra.grade-projection | object | defined | |
| obj.std-algebra.even-subalgebra | object | defined | |
| obj.std-algebra.grade-involution | object | defined | |
| obj.std-algebra.reversion | object | defined | |
| obj.std-algebra.clifford-conjugation | object | defined | |
| std-algebra.involution-properties | claim | proved: automorphism, anti-automorphisms, signs on grade k | |
| std-algebra.z2-grading | claim | proved | |
| primer.commutation-rule | claim | proved | absorbs |

### 4. Products and blades
| id | kind | status | existing |
|---|---|---|---|
| obj.std-algebra.outer-product | object | defined | |
| obj.std-algebra.left-contraction | object | defined | |
| std-algebra.product-decomposition | claim | proved: ab = a.b + a^b | |
| std-algebra.contraction-expansion | claim | proved | |
| std-algebra.exterior-isomorphism | claim | proved (Chevalley) | |
| obj.std-algebra.blade | object | defined | |
| std-algebra.blade-subspace | claim | proved | |
| obj.std-algebra.outermorphism | object | defined | |
| std-algebra.determinant-pseudoscalar | claim | proved: f(I) = det(f) I | |

### 5. The pseudoscalar
| id | kind | status | existing |
|---|---|---|---|
| obj.std-algebra.pseudoscalar | object | defined | |
| primer.sign | claim | proved | absorbs; links transport.sign |
| primer.centre | claim | proved | absorbs; links transport.centre |
| std-algebra.pseudoscalar-commutation | claim | proved | links odd-extensions.volume-element-odd-dimension |
| std-algebra.duality | claim | proved | |

### 6. Versors, Pin and Spin
| id | kind | status | existing |
|---|---|---|---|
| std-algebra.inverse-of-vector | claim | proved: v invertible iff Q(v) != 0 | links transport.noinverse |
| std-algebra.reflection | claim | proved | |
| std-algebra.cartan-dieudonne | claim | imported + check | |
| obj.std-algebra.clifford-group | object | defined | |
| primer.twisted-adjoint-action | claim | proved | absorbs |
| obj.std-algebra.pin-spin | object | defined | |
| obj.std-algebra.rotor | object | defined | |
| std-algebra.spin-double-cover | claim | proved | |
| std-algebra.bivector-lie-algebra | claim | proved | |
| std-algebra.bivector-exponential | claim | proved: elliptic, hyperbolic, null cases | |

### 7. Null vectors and the Witt decomposition
| id | kind | status | existing |
|---|---|---|---|
| obj.std-algebra.hyperbolic-plane | object | defined | |
| primer.splitting-along-hyperbolic-plane | claim | proved | absorbs; links transport.splitting-along-hyperbolic-plane |
| std-algebra.witt-decomposition | claim | proved | |
| obj.std-algebra.witt-index | object | defined | links tower.witt-index-quantum-capacity |
| std-algebra.witt-extension | claim | imported + check | links conformal.witt-extension-theorem, one-relation.imported-witts-extension-theorem |
| std-algebra.cl11-matrix | claim | proved: Cl(1,1) = M2(R) | |

### 8. Classification and periodicity
| id | kind | status | existing |
|---|---|---|---|
| std-algebra.tensor-rules | claim | proved | |
| std-algebra.periodicity | claim | proved (mod 8 real, mod 2 complex) | |
| primer.classification-real-clifford-algebras | claim | proved | absorbs; links transport.classification-real-clifford-algebras, sheaf.imported-classification-values(-external), rule2.imported-classification-centre-type-c(-external) |
| std-algebra.even-subalgebra-isomorphism | claim | proved | links transport.even-subalgebra-one-dimensional-extension, rule2.even-subalgebra-one-dimensional-extension |
| std-algebra.square-roots-of-minus-one | claim | proved for small n; imported in general | links one-relation.imported-square-roots-real-clifford-algebras |
| std-algebra.complexification | claim | proved | links odd-extensions.doubling-or-complexification |

### 9. Idempotents, ideals and spinors
| id | kind | status | existing |
|---|---|---|---|
| obj.std-algebra.primitive-idempotent | object | defined | |
| std-algebra.matrix-units | claim | proved | links transport.matrix-units-peirce-isomorphism |
| obj.std-algebra.minimal-left-ideal | object | defined (spinor space) | |
| std-algebra.morita-amplification | claim | imported + check | links tower.morita-equivalence-algebra-amplification, tower.matrix-amplification-structural-properties |
| std-algebra.zero-divisors-annihilated | claim | proved: every zero divisor is annihilated by an idempotent (semisimple case) | links transport.exhaustiveness-every-zero-divisor-annihilated-idempotent |

### 10. Fock and CAR
| id | kind | status | existing |
|---|---|---|---|
| std-algebra.witt-basis-car | claim | proved: null pairs give the CAR | links tower.ladder-pairs-satisfy-car-vectors |
| std-algebra.fock-representation | claim | proved for small n; imported in general | links standard-model.imported-fock-representation-clifford-algebra-bogoliubov, rungs.imported-fock-representation-bogoliubov-group(-external), correspondence.imported-ladder-pairs-fock-modules-over |
| std-algebra.pure-spinors | claim | imported + check (Cartan, Chevalley) | links one-relation.imported-cartans-purity-theorem-thouless-form |
| std-algebra.chevalley-pairing | claim | proved | links correspondence.chevalley-pairing |

### 11. The named algebras
| id | kind | status | existing |
|---|---|---|---|
| std-algebra.complex-numbers | claim | proved: Cl(0,1), and the even part of Cl(2,0) | |
| std-algebra.quaternions | claim | proved: even part of Cl(3,0), and Cl(0,2) | |
| std-algebra.pauli-algebra | claim | proved: Cl(3,0) = M2(C), Pauli matrices as a reading | |
| obj.std-algebra.spacetime-algebra | object | defined: Cl(1,3) | |
| std-algebra.sta-matrix | claim | proved: Cl(1,3) = M2(H) in the store's (+,-,-,-) signature (M4(R) is Cl(3,1)); its complexification M4(C) carries the Dirac matrices as a reading; Cl+(1,3) = Cl(3,0) | |
| obj.std-algebra.conformal-algebra | object | defined: Cl(4,1) and Cl(2,4) | links obj.transport.normalised-conformal-chart |
| obj.std-algebra.projective-algebra | object | defined: Cl(3,0,1) | |

## The grounding pass (after the core is in)

For each programme claim with no premise, and each listed above under "links":
read its proof, and add a `uses` edge to the core results the proof invokes. An
edge goes in only if the proof cites it (`\claimref`); proofs that cite in words
get the `\claimref` added. No edge is added to raise the count.

Expected result: the 7 primer results and about 25 new entities become the most
used nodes of the graph; reach to the core rises from 41%. I make no forecast of
the final figure until the pass has run, because some proofs will turn out to use
nothing from the algebra.

## Then the page

Radial layout: radius is derivation depth from the core, angle is the subject
sector, standard results muted and the programme's own results bright, ungrounded
claims in a band outside, and a path-to-core highlight on click. Notes off the map.

## Outcome (2026-10-26)

- **The core.** 67 new entities (43 results, 24 definitions) in `standard-algebra`, plus the six
  `primer.*` results moved in. Four results are imported with a check of their finite core
  (Sylvester inertia, Cartan-Dieudonne, Witt extension, pure spinors); the rest are proved in the
  store with their own exact checks. `lib/stdalg.py` holds the shared check helpers.
- **Corrections on the way.** Cl(1,3) = M2(H) in the store's signature, not M4(R) as this plan said
  (M4(R) is Cl(3,1)); one rotor factorisation was wrong for Q(a) = -1 (caught by its check);
  `stdalg.sample` ignored its seed, so a section 1-3 check was partly vacuous (fixed and pinned
  by a test).
- **Referees.** Two independent referees read every core proof: no statement wrong; two gaps
  (`ga-py-product` now has a direct proof, `existence-uniqueness` says representation, faithful by
  the blade basis) and twelve smaller points, all fixed. `primer.classification-real-clifford-algebras`
  gained a second derivation through `std-algebra.periodicity` (version 3).
- **Grounding.** 263 programme results read; 118 changed (about 150 `uses` edges, each cited with
  `\claimref` where the proof uses it, plus `specialises`, `equivalent_to` and `about` links);
  the rest use nothing from the algebra and were left alone. The 241 dependants of these bumps were
  repinned; every stale pin came from this branch.
- **Reach.** Programme results reaching the core by a chain of premises: 39.8% before (counting the
  old clifford-structure subject as core) to 61.5% after (counting only the new core).
- **Page.** A Foundations arrangement beside the existing one: core at the centre, radius by premise
  steps to the core, unconnected results in an outer band, standard results muted, the path to the
  core drawn on selection. It costs neighbourhood fidelity (neighbours recovered 0.61 to 0.29;
  global order 0.50 to 0.61), so the neighbourhood layout stays one click away.
- **Full check.** 0 errors, 8 warnings (the same 8 as before this work).

### Follow-ups found by the grounding pass

1. Complex Clifford algebras, `Cl(V_C)`: several correspondence proofs work over C and cite real
   core results read over C; `correspondence.chevalley-pairing` has no exact core counterpart.
2. exp of a general bivector lies in Spin (the core states the exponential only for bivectors whose
   square is a scalar); needed by `correspondence.spin-representation`.
3. The ideal generated by the radical squares to zero and the quotient is Cl(V/rad V)
   (`sheaf.degeneration-sheaf`).
4. Maintainer decisions: `one-relation.imported-square-roots-real-clifford-algebras` and
   `tower.morita-equivalence-algebra-amplification` are imports whose content the core now proves;
   `conformal.witt-extension-theorem` and `conformal.blade-basis-persists-under-degeneracy` duplicate
   core results.
5. `tp lock` after review; I305 notes 54 stored documents depend on changed entities and may need
   regenerating.
6. (2026-11-10) Outside the core's scope (GTG), recorded here because results cite it as algebra: the protraction identity of the curvature operator of a torsion-free field, `d_a ^ R(a ^ b) = 0` (the first Bianchi identity; the converse fails), is `synthesis.protraction-identity-of-the-curvature-operator-from-vanishing-torsion`.

### Page revision (2026-10-27, after Leon's review)

- Zoom buttons (+, -, Fit) on the canvas; scroll and pinch still work.
- Foundations layout recalibrated: shells are equal-volume by population with gaps between them;
  the core takes its own directions from a stress layout of the core alone and is ordered by
  depth within the core (core radius 0.32, was 0.16); results resting on the programme's
  postulates and imported physics but on no core result form an outer zone ordered by their own
  depth. Only logical links within a zone are drawn faintly; cross-zone links show for a
  selected result. Neighbours recovered 0.32 (neighbourhood layout 0.61).
- Layer slider (core only, then one shell at a time, out to everything) and an outer-zone switch;
  selecting a hidden result reveals its layer.
- The Tags panel is gone from the rail; tags remain as chips on each result and as collections.
- Trails: new "The algebra core" (trail-standard-algebra, 10 steps) first in Foundations;
  trail-clifford-structure retired (its results moved into the core); the tour and every other
  trail regenerated against the current store, all audits D110 only.
