# Filer B: premise (C) and results B1 to B4, notes N1 and N2

Run 2026-11-07-bit-root. Work scripts: none beyond the proposal folders (all computation is in the
checks). Status: done. All six registered with propose_claim (proposal.json present); coverage.yaml copied
into the four claim folders by hand after registration, and the registered entity.md, proofs and
checks compared with the drafts (identical).

## Filed (proposal ids)
| id | what | gate |
|---|---|---|
| synthesis.continuum-completion-premise | postulate (C): an ordered field with the least-upper-bound property, the field of the store's definitions | check4 0/0 (no check: postulate); validate ok |
| synthesis.division-gives-the-rationals | B1 | check4 0 errors, 0 findings; validate ok |
| synthesis.completion-recovers-the-real-clifford-algebras | B2, Sylvester derived in GA | check4 0 errors, I405 only (functoriality excused in coverage.yaml); validate ok |
| synthesis.frobenius-and-universality-in-clifford-algebras | B3 + B4 merged | check4 0 errors, 0 findings; validate ok |
| note.synthesis.grading-of-the-bit-ladder | N1 | validate ok (notes carry no check) |
| note.synthesis.geometric-algebra-as-the-algebra-of-physics | N2, argued | validate ok |

A's ids (cited in text only): synthesis.premise-the-bit, synthesis.premise-minimal-non-commutativity,
synthesis.premise-superposition-over-the-integers, synthesis.signed-directions-and-the-integer-clifford-algebra.
B1 uses A's twisting function f(S,T) verbatim and does not refile A's clauses (rank, contraction rule,
universal property): it defines Cl_R(p,q) by the blade product in a setup sentence and proves only
what division adds.

## Gate constraint found (affects both filers)
validate_draft resolves every edge (uses, assumes, lineage, comments_on) against the STORE only
(tp/validate.py E201), so a proposal cannot cite another proposal, including the new postulates.
B2 and B3 therefore state their hypothesis inside the formal statement ("let R be a complete ordered
field, as premise (C) takes it"; B2 for an arbitrary ordered field F) and name (C) and A's results in
plain text. `uses -> postulate` is E203, so the link to (C) must be an `assumes` edge, which only a
maintainer may add (E601, layer 6, not run by validate_draft; so the postulate itself passes the gate).

## Pre-registered kill conditions (written before computing) and outcome
- B1: killed if a proper subring of Q inverts every non-null integer vector, or a non-null rational
  vector is not invertible over Q. Not killed: m e_1 has Q = +-m^2 and e_1 (m e_1)^{-1} = 1/m.
- B2: killed if diagonalisation needs more than square roots of positive elements, or the rational plane
  with squares 2, 3 has a rational zero divisor. Not killed: the proof uses only the Euclidean property;
  the norm a^2 - 2b^2 - 3c^2 + 6d^2 has no nontrivial rational zero (descent mod 3, checked on all
  residues mod 9).
- B3: killed if the GA argument let a dimension other than 1, 2, 4 survive, or if it did not need
  odd-degree roots. Not killed: k = 2 is excluded by e1e2 being pure and orthogonal to e1, e2; k >= 4
  by e_j = c_j e1e2 for j >= 3; odd-degree roots enter through Laplace's induction (completeness used).

## Proved / computed / argued
- proved (B1): v in V_Z invertible in Cl_R(p,q), R a subring of Q, iff Q(v) is a unit of R (the
  converse via gcd and Bezout, no localisation lemma needed); smallest such R is Q; zero divisors over
  Q exactly outside (0,0), (0,1), (0,2), integral witnesses; nonzero null vectors iff p, q >= 1.
- proved (B2): complete ordered field => Euclidean (lub argument); orthogonal (anticommuting) bases by
  GA rejection x - B(x,u) u^{-1} over any ordered field; Sylvester (r = dim rad, p = max positive definite
  dimension) over any ordered field, isometry classification over Euclidean fields; Cl_Q(p,q,r) (x) R =
  Cl(p,q,r); every real Clifford algebra is Cl_Q(p,q,r) (x) R inside Cl_Q(p+r,q+r) (x) R; over Q
  square classes remain (<2>, <2,3>).
- proved (B3): real fundamental theorem of algebra in Cl(0,1) (odd degree by lub, square roots in
  Cl(0,1), Laplace induction); Frobenius by the pure part as a negative definite quadratic space and the
  bivector e1e2. (B4): matrix units E_{I,J} = w_I f v_J^rev of Cl(k,k) and the corner embedding of every
  finite-dimensional associative real algebra; split-complex and dual numbers restated.
- computed: all checks exact (Fractions, GA.py, GA.ext_c for nondiagonal Gram matrices).
- argued (N2 only): geometric algebra as the algebra of physics, with the source's evidence and
  objections, plus two objections added: coverage was assembled knowing the physics; the containment is
  about finite-dimensional associative algebras, and bosons (CCR) enter only as a limit.

## Already stored (cited, not refiled)
std-algebra.inverse-of-vector (v^{-1} = v/Q(v)), transport.exceptional-division-algebras (the real list),
std-algebra.periodicity / primer.classification-real-clifford-algebras (types; Cl(1,0) = R + R),
std-algebra.complex-numbers, std-algebra.quaternions, std-algebra.fock-representation (Cl(k,k) = Mat),
std-algebra.matrix-units, std-algebra.witt-basis-car, conformal.minimal-nondegenerate-completion
(Cl(p,q,r) in Cl(p+r,q+r)), synthesis.nilpotent-steps-derivative-exponential-and-boost (finite exp).
Nothing in the store states Frobenius, FTA, Euclidean fields, rational square classes or a complete
ordered field; the store's R is undefined (used as the ambient field of obj.std-algebra.*).

## Corrections to the source document
- "Only signs survive in R": true already over any Euclidean ordered field (positive elements squares),
  far smaller than R; completeness is not what makes directions +-1. Stated in B2 (vi) and the premise.
- Frobenius needs more than Euclidean: odd-degree roots (real closedness), so completeness (or real
  closedness) is used there (from memory, not filed: over the constructible reals, adjoining a cube root
  of 2 gives a commutative division algebra of dimension 3).
- Ostrowski's "the completion is unique" and the uniqueness of complete ordered fields are kept out of
  the premise (prior art in its extraction note).

## Decisions for Leon
1. Adopt synthesis.continuum-completion-premise as postulate (C) (maintainer-only, E601). Recommendation:
   adopt; it states only an ordered field with least upper bounds.
2. Add `assumes: [synthesis.continuum-completion-premise]` to the main derivations of
   synthesis.completion-recovers-the-real-clifford-algebras (clause (iv)) and
   synthesis.frobenius-and-universality-in-clifford-algebras. Recommendation: yes for both; they
   already state the hypothesis in the formal text (W503-clean at every level).
3. std-algebra.sylvester-inertia (imported Fact) is now derived by B2 (ii)-(iii) over any Euclidean
   field. Recommendation: give the Fact a derivation citing B2, or retire it in favour of B2 (keep its
   statement as the real case).
4. Optional edges: B1 may `use` synthesis.signed-directions-and-the-integer-clifford-algebra (A) for the
   ring; B2 may use B1. Not needed by the proofs.
5. Re-rooting the store's real algebra on (C) (RUN.md: Leon's decision). Recommendation: do not add
   (C) to existing std-algebra results; most of them are algebraic and hold over Q or Z, so the natural
   root for them is (L) plus division, and only results using limits or Euclidean square roots need (C).

6. Letter clash (raised also by A): (C) here is T12's Hypothesis (C) elsewhere in the store
   (conventions.md "Same names"). The titles say what the premise is; rename only if Leon prefers.

## Overlap with A (read at the end of A's run)
- B2 (iv), first sentence (Cl_Q(p,q) (x) R = Cl(p,q) through e_S -> e_S) is the real case of A's
  clause (vii) (universal property over every commutative ring). B2 keeps it as one sentence of the
  bridge; if the maintainer prefers, it can cite A's result there after acceptance. B2's own content
  (Sylvester over ordered and Euclidean fields, square classes, degenerate forms) is not in A's result.
- A's unfiled A3 (no integral CAR pair; the unit pairing needs 1/2) is consistent with B1: the Witt
  vectors (e+ +- e-)/2 of Cl(1,1) live in Cl_R(1,1) for R = Z[1/2], a ring between Z and Q that
  division passes through. N1 places the Witt and Fock readings at steps 3 to 4 without claiming them over Z.
