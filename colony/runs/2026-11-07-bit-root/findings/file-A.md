# Filer A: premises (B), (S), (L) and results A1 to A3

Run 2026-11-07-bit-root. Work scripts: colony/runs/2026-11-07-bit-root/work/A/ (check.py, the draft of
the result's check). Gate outputs: colony/runs/2026-11-07-bit-root/verify/final/<id>.draft.json and
<id>.validate.json. Status: done; four proposals registered (proposal.json present in each). Fix round after referee Z applied:
see findings/fixes-A.md (the result now has no uses edge; existence by a bilinear cocycle added).

## Ids (B: cite these in text; edges are a maintainer decision)
- synthesis.premise-the-bit (postulate (B))
- synthesis.premise-minimal-non-commutativity (postulate (S))
- synthesis.premise-superposition-over-the-integers (postulate (L))
- synthesis.signed-directions-and-the-integer-clifford-algebra (A1 + A2 merged)

Why A1 and A2 are one entity: the cap is 4 proposals and RUN.md asks for one entity per postulate,
which leaves one slot for the results. A1's new content (the order clause forced for n >= 2, the
normal form and presentation, the centre, extraspecial, the classification of the groups by q) is
short, and A2's last clause (isomorphism classes of the algebras) uses it, so they read best as one
statement. Cost: the group clauses (i) to (iv) need only (S), not (L); the statement says so by
stating each hypothesis where it enters ((S) before clause (i), (L) before clause (v)).

## Gate results
| id | runcheck | check4 | validate_draft | registered |
|---|---|---|---|---|
| synthesis.premise-the-bit | no check (postulate) | exit 0, 0 findings | ok, no codes | yes |
| synthesis.premise-minimal-non-commutativity | no check | exit 0, 0 findings | ok, no codes | yes |
| synthesis.premise-superposition-over-the-integers | no check | exit 0, 0 findings | ok, no codes | yes |
| synthesis.signed-directions-and-the-integer-clifford-algebra | 6/6 pass (about 7 s) | exit 0, 0 findings, check pass | ok, no codes | yes |

Mutation test of the result (tp mutants): no W413; survivors are sample inputs only (one signature
tuple entry or loop bound per function, at most 3 of 8 sampled in the universal-property check).
propose_claim does not copy coverage.yaml; it was copied into the registered folder by hand, and the
registered entity.md, proof-main.tex and check.py were compared byte for byte with the drafts (same).

## Pre-registered kill conditions (fixed at planning, before the checks were written)
- A1: killed if a group with (S2), (S3) and n >= 2 could have c^2 != 1, or if the centre for odd n
  were not of order 4, or if the squares of G were not {1, c} for n >= 2. Not killed.
- A2: killed if Z[G]/(c + 1) had torsion or rank other than 2^n, if v^2 = Q(v) needed 1/2, or if
  some f with f(x)^2 = Q(x) failed to extend. Not killed.
- Classification: killed if two signatures of the same n <= 6 with equal Gauss sums had inequivalent
  F_2 forms (or unequal sums equivalent forms). Not killed: (90 equivalent, 104 inequivalent) ordered
  pairs, all matching the Gauss sums.

## What the result proves (labels)
- proved: (i) c^2 = 1 forced for n >= 2 (the sign-from-symmetry argument of the stored theorem, read
  in the group; cited, not refiled); independent for n = 1 (Z_{2m}, c = e^2); normal form c^a e_S,
  |G| = 2^{n+1}, and a presentation of G.
- proved: (ii) squares and commutators in {1, c}; the forms q, b are the stored ones (cited); for
  n >= 2, c is the only non-identity square and the only non-identity commutator.
- proved: (iii) centre {1, c} (n even: extraspecial of order 2^{1+n}), {1, c, e_full, c e_full}
  (n odd).
- proved: (iv) groups of signed directions classified by the equivalence class of q.
- proved: (v) Z[G]/(c + 1) free of rank 2^n on the blades, integral structure constants.
- proved: (vi) v^2 = Q(v) for integer vectors, with no 1/2.
- proved: (vii) universal property over every commutative ring R; A = Cl_Z(p, q); over R = the reals
  it is the store's Cl(p, q) (Definition obj.std-algebra.clifford-algebra); in characteristic 2 it
  is the commutative group algebra of the configurations.
- proved: (viii) for fixed n: forms equivalent <=> groups isomorphic <=> algebras isomorphic over
  every R <=> over one R mapping to an ordered field (Z, Q, R) <=> equal Gauss sums (Arf's
  classification derived in the proof; the Gauss sum shown intrinsic as the signature of the trace
  form 2^{-n} Tr(L_{xy}) = <xy>_0, with the inertia argument done inline for that form).

## Correction to the brief (for Leon)
RUN.md's A1 says "c is the unique non-trivial central square root of 1 in G". That is false in
general: for n odd with e_full^2 = 1 (exactly p - q = 1 mod 4, e.g. Cl(1,0), Cl(2,1), Cl(0,3)),
e_full and c e_full are central of order 2 too. True statements, filed: c is the only non-identity
square and the only non-identity commutator (n >= 2); c is the only central involution exactly when
n is even or p - q = 3 mod 4. The document's Step 2 sentence "c is the one non-trivial square root
of the identity" should be read in the first sense.

## Found already stored (cited, not refiled)
- synthesis.blade-square-signs-f2-quadratic-form: c^2 = 1 from symmetry (its (i)), the forms q, b
  (its (ii)), the radical (its (iii)), the Gauss-sum table (its (iv)). Cited at @2.
- note.one-relation.two-presentations-differ-over-the-integers and one-relation.two-presentations:
  the integer orders of the (1,1) plane. Named in the result's extraction note only.

## A3 (null pairs over Z): not filed
- proved (one line, also checked numerically for (1,1), (2,1), (2,2), (1,3) on boxes): in every
  Cl_Z(p, q) the anticommutator of two integral vectors is uv + vu = 2 sum (+-) u_i v_i, an even
  integer. So no two integral vectors form a CAR pair (aa' + a'a = 1); the integral null pair
  e+ + e-, e+ - e- of (1,1) has anticommutator 4. The unit pairing of the Witt presentation needs
  1/2, i.e. the coefficient ring Z[1/2] (which B1's division supplies). This generalises the stored
  note from (1,1) to every (p, q) but is a one-line consequence of v^2 = Q(v); recorded here only.
- proved: for (p, q) = (1, 1), Z[G]/(c + 1) is the stored note's orthogonal order (index 4 in
  Mat_2(Z), no idempotents but 0, 1), so premise (L) over Z yields that order, not Mat_2(Z). Stated
  in the result's extraction note.
Nothing else new and exact remained, so no A3 entity.

## Relation to the imported Fact (for the maintainer)
synthesis.imported-real-clifford-algebras-as-twisted-group-algebras-and-the-arf-invariant:
- its (a) (Cl(p,q) is a twisted group algebra of F_2^n with the stated twisting): derived, over every
  commutative ring (result (v), (vii)).
- its (b) (isomorphic iff forms equivalent): derived for the Clifford twisting functions (result
  (viii), over every ordered field and over Z); NOT derived for general bilinear twisting functions
  (arbitrary alternating polar forms), which the store does not use.
- its (c) (Arf separates real from quaternionic): already clause (iv) of the stored theorem.
Named in the result's extraction note; what happens to the Fact is the maintainer's decision.

## Overlap with filer B (for the orchestrator and referees)
- B2 (synthesis.completion-recovers-the-real-clifford-algebras), clause (iv) first sentence
  (Cl_Q(p,q) (x) R = Cl(p,q) via e_S -> e_S): this is the R = the reals case of my clause (vii),
  which holds for every commutative ring and needs no completeness. B2's own content (Sylvester,
  Euclidean fields, square classes, degenerate forms) is not in my result. My (viii) uses an inline
  inertia argument for the trace form over an ordered field; it is a proof step, not a filed
  Sylvester theorem.
- B1 defines Cl_R(p, q) (R a subring of Q) by the blade product; it is my A_R, consistent.

## Decisions for Leon
1. Adopt the three postulates (B), (S), (L) (new postulates are Leon's). Recommendation: adopt;
   each is short, mathematical, and says so in its lay level.
2. Edges: the result states (S) and (L) as hypotheses inside the theorem, so it is unconditional and
   proved. Recommendation: link it to the postulates by lineage (motivated_by: the three premises),
   not by assumes, unless Leon adopts the re-rooting; with assumes it would hold given (B), (S), (L)
   although it does not need them. The postulates' motivated_by currently point at the stored
   blade-square-signs theorem ((B), (S)) and the twisted-group-algebra Fact ((L)).
3. Order clause: (S) keeps c^2 = 1 because it is independent at n = 1 (proved). Alternative: state
   (S) for n >= 2 only and drop the clause.
4. Letters: (S) clashes with T12's slot statistics (S) and T14c's (S) (conventions.md "Same names");
   (C) (B's) with T12's Hypothesis (C). Keep the document's letters (titles say what each is), or
   rename.
5. The Fact above: keep as prior art for the general case, or retire in favour of this result plus
   the stored theorem; and whether the stored theorem's standard-route derivation should cite the
   new result instead.
