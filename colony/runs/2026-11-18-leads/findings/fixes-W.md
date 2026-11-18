# Fix round, cluster W (referee report verify/R-C.md)

All three proposals: SOUND WITH FIXES. Every listed fix applied in place under proposals/<id>/ (entity.md,
proof-main.tex, check.py, coverage.yaml; proposal.json carries no copies). No conclusion reversed. Nothing declined.
runcheck: C1 7/7, C2 5/5, C3 3/3 pass. check4: pending (orchestrator). validate_draft: pending (orchestrator).

## C1 synthesis.position-vector-eigenbundle-in-codimension-three-has-a-class-of-order-two
- Lifting lemma closed and promoted to a clause (L) of the statement, in the form C2 needs (the lifted family
  exists, closes, and is constant where the loop is). New proof paragraph: in Cl(n,0), Spin = Spin^+ and
  SO^+ = SO (every unit vector has square one); the closed set S of even R with R R~ = 1 preserving vectors is the
  group of rotors: for R in S take a versor g with the same twisted adjoint action (Pin onto O(n), cited theorem);
  y = g^-1 R is odd and anticommutes with every vector (then y = 0, the kernel step of the cited proof) or even
  and central (then a scalar, primer.centre); so R = +-g. Unit norm of rotors stated.
- uses: primer.centre@3 added. New check check_elements_commuting_or_anticommuting_with_every_vector (n = 1..6;
  touches primer.centre; also that the plane rotor is a product of two unit vectors).
- Clause (6) reworded: (4) with W0 = 0 rules out every repair on S; the linear system shows only that none of the
  form x + b E exists. Proof and coverage say the same.
- "Order two": the group is named (stable classes of real vector bundles over the two-sphere under direct sum),
  with the argument that the order is exactly two ((3) and (5)); formal, technical, one-liner.
- Extraction note: the infinite order in codimension five is marked as from memory; the stored result cites only
  non-removability.
- Coverage: the rotor check is said to test the rotor in the algebra of the stabilised fibre, not on the module
  frames (referee's remark).
The slug still describes the result.

## C2 synthesis.fixed-form-completion-over-a-ball-exists-iff-the-eigenbundle-is-stably-trivial
- Fix 1: clause (2) now states K0 = 1_c (+) (-1_c') (+) 1_N exactly, as the seam needs. Widened by what can be
  proved: every nondegenerate form of signature (c + N, c') on W0 is L^T K0 L for a constant invertible L
  (Sylvester), and (1 + L)^T h (1 + L) is a completion for it. Stated in formal and technical, proved, and checked
  exactly on the worked family with a non-orthogonal L (perturbing the expected exterior form fails the check).
- Fix 2: the lifting lemma is no longer proved here. The proof cites clause (L) of C1, and
  C1@1 is a uses edge. ORDER OF ACCEPTANCE: C1 must be accepted before C2 (validate_draft on C2 will not resolve
  the premise until then). coverage.yaml excuses the premise under untouched_premises (a statement about
  continuous maps; no check can call premise() on an entity that is not yet stored).
- Note says the completions built are continuous, not smooth.
The slug still describes the result.

## C3 synthesis.eigenbundle-class-of-a-corank-one-wall-is-the-dying-line
- One-liner, technical (3), formal (3), extraction note: the claim that this is the stored necessity clause "with N
  identified" is removed. Now: a two-sided necessary condition of the same form as the stored one-sided clause,
  with N the far form's negative eigenbundle; the stored clause has no far form; neither is derived from the
  other; the relation to the one-sided count k(Sigma) is not decided.
- Lay: both overclaims removed (the earlier wall results do not all follow; the invariant of the conjecture is not
  shown to be this class: naturality and conservation are not shown).
- Reading: "the number of flat directions needed to cancel the class" is marked argued, for the two-sided count,
  with its dependence on G-bar_- (on q) stated; the list of stored results that do not follow is given.
- Hypotheses: "every tame wall satisfies (W)" replaced by: a degeneration satisfying the hypotheses of the
  one-rung theorem, with a collar thin enough, given homotopy invariance of bundles (cited from memory, not in the
  store; in (W) the pull-back is a hypothesis); the side signatures are named as hypotheses of that theorem.
- Clause (1) and (5): the class is "relative across the collar", local to it; the stored transfer class relative
  to the base can carry exterior information, not addressed.
- Reading of w(Sigma): the clock mismatch of the one-rung theorem; the Stiefel-Whitney reading of the lens-space
  entity is named as not the one used.
- Proof: Weyl's inequality flagged; the dimension axiom of Stiefel-Whitney classes flagged as used and as absent
  from the imported Fact's text (the Fact itself is the maintainer's to amend); the one-rung exclusions are stated
  for a constant hyperbolic form.
- Extraction note lists the overlap with the store (k = 1; the two instances in clause (4)) and what is new.
- Title: "...; two-sided rungs by transfer" (89 characters). The slug still describes the result.

## Restatement draft of sheaf.wall-class (work/W/wall_class_restatement_draft.md)
Made consistent with C3 as restated: clause (c) is no longer recorded as proved. The draft replaces the reference
to the refuted conjecture by the transfer class, says that across the collar the class is the dying line with the
information of the pair (proved), and leaves the class relative to the base, naturality and conservation
conjectured. The closing sentence keeps "or a finer torsion-sensitive class".
