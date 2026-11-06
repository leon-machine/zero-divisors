# Fixes, filer S (referee report verify/G.md, sections 1-3, overlaps, recommendation)

check4: pending (orchestrator). Only `colony/runcheck.py` was run on the checks (all PASS);
validate_draft was run once on the new note draft (ok, info I305 only) and propose_claim filed it.

## synthesis.blade-square-signs-f2-quadratic-form (SOUND WITH FIXES): all fixes applied in place
- extraction.note: cites V. Ovsienko, arXiv:1601.07664, and A. Elduque and A. Rodrigo-Escudero, Adv.
  Appl. Clifford Algebras (2018), arXiv:1801.07002, for (ii)-(iv) (referee-verified), with "Classical,
  restated"; adds the trace-form reading of the Gauss sum (+k, 0, -2k on Mat_k(R), Mat_k(C), Mat_k(H));
  says (v) is tower.commuting-copies at one plane with the type statement of tower.rigidity-clock-frozen
  and (i) is a classical remark. Salingaros, Lounesto, Arf, Quillen stay flagged as from memory.
- formal (i): last two sentences replaced by the referee's wording (single relation x1 x2 = c x2 x1,
  c != 0; characteristic other than 2; symmetry and centrality each force c in {1, -1}). Proof (i)
  rewritten to match. Technical paragraph adjusted ("c = -1 needs the separate input c != 1").
- formal (v): \claimref{tower.commuting-copies} and \claimref{tower.rigidity-clock-frozen} cited at the
  points used; appended "adding it is not an orthogonal sum ... Cl(p, q+2) carries q_(q,p) perp q_(0,2)".
  Same sentence in the technical level.
- lay: last sentence replaced by the referee's text (the false "switches real and quaternionic" is gone).
- proof (iv): added "(1 + j)^8 = 16, so for |r| + 1 >= 8 the value is 16^m times the tabulated one".
- proof (v): added the anisotropic-plane argument ((x omega')^2 = -x^2, isometry q_(q,p) perp q_(0,2) ->
  q_(p,q+2); Cl(2,0) -> Cl(2,2) real, Cl(0,2) -> Cl(0,4) quaternionic).
- check: new function check_anisotropic_plane_exchanges_p_and_q (declared in checked_by): builds the
  twisted products in Cl(p,q+2) for (p,q) = (2,0), (0,2), (1,3), (1,2), verifies the squares against
  q_(q,p) perp q_(0,2) with the reordering, the commutation and the bijection, and the referee's line
  Arf(q_(2,2)) = Arf(q_(0,2)) + Arf(q_(0,2)) = 0 = Arf(q_(2,0)), Arf(q_(0,4)) = 1, and
  Arf(q_(2,0)) + 1 != Arf(q_(2,2)). runcheck: 5/5 PASS.

## synthesis.hyperbolic-plane-integral-orders-and-partner-inverse (SOUND WITH FIXES, not to stand): dropped
- Folder moved to colony/runs/2026-11-06-edge-normality/work/S/dropped/synthesis.hyperbolic-plane-integral-orders-and-partner-inverse/
  (kept with its check, which verified (i)-(ii) exactly).
- (i)-(ii) became the note proposals/note.one-relation.two-presentations-differ-over-the-integers
  (kind note, status remark, comments_on one-relation.two-presentations and std-algebra.cl11-matrix;
  format copied from note.standard-model.second-doublet-coupling-is-a-second-family-matrix). The lattice
  sentence uses the referee's wording: II_{1,1} (even unimodular, polar normalisation, the hyperbolic
  quadratic module) versus I_{1,1} (odd, unimodular only for the half-polar form B, singular at 2 as a
  quadratic module, polar determinant -4); same in technical and one-liner. A note carries no check;
  the note's extraction says where the exact verification lives and that the referee recomputed it.
  validate_draft ok; filed with propose_claim.
- (iii) dropped as a duplicate of singularity.pseudo-inverse-identities-hyperbolic-atom (plus
  std-algebra.witt-basis-car, note.transport.setting-hyperbolic-atom-matrix-algebra-moore,
  descent-lift.pairing-creator-under-transport-algorithm (ii)); the one sentence still needed is cited
  from that entity in the third proposal.
- (iv)-(v) moved into synthesis.limits-as-null-steps (ii), with the referee's generalisation (any
  generalised inverse g, idempotent gn; the partner is the one with self-adjoint idempotent), the
  radical-vector argument as the referee wrote it, and "regular by Lemma transport.regularity-..." only.

## synthesis.limits-as-null-steps (OVERSTATED): restated, narrowed, merged
- Restated at every level to the referee's weaker statement. Title: "Nilpotent steps: dual-number
  derivative, nilpotent exponential and nilpotent boost". One-liner: the referee's text plus the
  generalised-inverse clause absorbed from the dropped proposal. Technical first sentence and lay
  sentence: the referee's replacements. Formal ends with "No limit is removed: ...". The id is unchanged
  (folder kept in place as instructed); the maintainer may rename it, since "limits-as-null-steps" echoes
  the old wording.
- Narrowed to the old (i)-(iii); old (iv) (half-angle rotors, Archimedes) and (v) (tan denominators)
  removed, not moved to a note (they share nothing with nilpotent steps; a note would carry no check).
  The as-filed version with their exact checks (nested-root field class) is archived at
  work/S/dropped/limits-as-null-steps-as-filed/. Tag needs-continuum removed (no pi left);
  std-algebra.bivector-exponential removed from uses.
- New clause (ii): radical vector rho x rho = 0 (no generalised inverse); g(f(x + n) - f(x)) = f'(x) gn
  for any generalised inverse g; the Witt partner via singularity.pseudo-inverse-identities-hyperbolic-atom@4,
  minimal completion conformal.minimal-nondegenerate-completion@6, regularity
  transport.regularity-localises-zero-divisors-idempotents@2 (all added to uses and touched).
- (iii) realisations: the Cl(2N,2N) "correction" is replaced by the referee's statement (disjoint pairs
  of one orthogonal null family need Cl(2N,2N); Jordan-Wigner steps b_i = v_i pi_1 ... pi_{i-1} already in
  Cl(N,N)). Added to formal, proof and check (N = 2, 3 in Cl(N,N), nonzero product asserted for every
  realisation). My earlier finding that the source's Cl(N,N) was wrong is withdrawn: it was false in
  general.
- (iv) (old (iii)), the boost: citation fixed (the series stops because d is central with d^2 = 0, so
  (dB)^2 = 0; bivector-exponential no longer cited); formal adds the referee's sentence on R[d]/(d^2),
  the inverse exp(-dB/2) and the reversion of Cl(1,1,2) fixing dB; proof computes
  (1 + dB/2) l_+ (1 - dB/2) = (1 - d/2)^2 l_+ = (1 - d) l_+ directly and states R~ = R, R R~ = 1 + dB.
  Check asserts reverse(R) == R, R reverse(R) != 1, and R l_+ reverse(R) = l_+.
- extraction.note rewritten: restatement recorded, absorbed clauses named, withdrawn clauses named,
  the referee's Cl(N,N) construction credited, ledger per clause.
- check: rewritten (four functions, declared): dual-number derivative; derivative through a generalised
  inverse (partner and g = m + 3n + 2nm, hand-stated values, self-adjointness distinguishes them,
  rho x rho = 0 on five degenerate signatures); nilpotent exponential (three realisations); boost.
  runcheck: 4/4 PASS.

## Not changed
- Referee's observation that P1 (v) duplicates stored results: kept as a corollary and said so in the note.
- Leon's DECISIONS.md item 4: these proposals go to Leon individually at close-out; nothing here assumes
  acceptance.
