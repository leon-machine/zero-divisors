# Consistency pass, reader R12 (tower, one-relation)

## What was read

All 119 ids in read_R12.txt were read in dependency order. For every claim, object, question and prediction I read the
front matter (derivations, uses, assumes, pins, checked_by, extraction notes) and the formal, technical, lay and one-liner
levels. I read every proof-main.tex in full: 54 proofs, including the long ones of the synthesis twistor and tube-point
cluster and the tower-top cluster. I read the formal level of every note in full (50 notes).

I did not read: check.py files, except to settle one question about the third-constant lemma's signatures;
orig-proof-main.tex; coverage.yaml.

The exact computations behind the fixes are in
/tmp/claude-0/-home-claude/23cbb9be-73ca-5537-8211-47496476158a/scratchpad/R12/verify_r12.py (lib/GA.py, Fractions; all 44
checks pass).

## Fixed (16 version bumps, 1 change to lay level and one-liner only)
- hawking.imported-algebra-boundary-modes-car-algebra 5 -> 6:
  - The formal level and the proof glossed the charge as "the mod-8 invariant the tower's completions advance", which
    contradicts tower.rigidity-clock-frozen. It now reads "preserve".
  - The proof wrote $a_j = v_j$, $a_j^\dagger = v_j^*$, the reverse of the formal level and of the premise. It now uses the
    premise's labelling.
  - The technical level now names the complexification unit.
  - The lay level no longer claims more than the formal level does (boundary modes).
- tower.car-limit-even-charge 5 -> 6: the complexification unit ($1 \otimes I_4$ of a tensor factor, not the ground
  $\gamma_0\gamma_1\gamma_2\gamma_3$) is named.
- tower.structure-tower-c-norms 9 -> 10:
  - The formal level now distinguishes the scalar unit from the ground volume element $u_A$.
  - In the proof, $x = -y \otimes I_4$ (an ill-formed product) became $x = -y(1 \otimes I_4)$.
- odd-extensions.cosmological-constant-deforms-wall 2 -> 3: the proof displayed only $I$ (square $+\Lambda/3$), while the
  statement gives the generator the square $-\Lambda/3$. The proof now names that generator, $J = d e_+ + c e_-$, with
  $J^2 = -\Lambda/3$ and $J = \pm I$ at $\Lambda = 0$ (computed exactly).
- odd-extensions.four-extensions-oriented-pair 5 -> 6: the unit of the complexified rows ($\omega = \pm I_5$) is named.
- odd-extensions.mirror-inside-complexified-extension-absent-doubled 4 -> 5: the two units of (iii) and (iv) are named
  (the shadow's pseudoscalar against the central $\omega$) and kept distinct.
- tower.witt-index-quantum-capacity 4 -> 5: $Q(v,v)$ became $Q(v)$.
- rungs.rung-spinor-module-mixings 6 -> 7: the entity wrote the identity of $\C^3$ as $I_3$, beside the pseudoscalars
  $I_{13}$ and $I_{7+2n}$. It is now $1_3$.
- synthesis.de-sitter-field-fixes-the-observer-tube-point 3 -> 4: the formal level says it uses the labels of the
  Wick-rotation theorem, where $K = \tfrac12 e_1e_2$, and then sets $K = e_1e_2$. It now says "twice that theorem's
  generator", as the proof already did. Clause (iii) needs the unit-rapidity $K$: $Q(K\cdot x) = \rho^2$ for $K = e_1e_2$
  and $\rho^2/4$ for $\tfrac12 e_1e_2$ (computed).
- synthesis.plane-grading-records-residue-sign 3 -> 4: the proof's $N_j - \tfrac12 = K_j$ uses the atom labelling, in
  which $v$ annihilates. In the tower's labelling it is $-K_j$ (computed). The proof now says so; $m_j = -1$ is still odd,
  so nothing changes.
- one-relation.one-datum-not-two-imaginary-unit 3 -> 4: a "which unit acts where" sentence was added. $J$ is the right
  unit; $I_4$ satisfies $L_{I_4} = -\Gamma R_{I\sigma_3}$ (computed on all even blades).
- synthesis.positive-structure-is-twistor-form-at-imaginary-time 4 -> 5: the reading said
  synthesis.positive-null-energy-gives-r-premises was "not yet in the store". It is now in the store, and that remark is
  removed.
- pairing.imported-stabiliser-tangent-external 1 -> 2 and rungs.imported-fock-representation-bogoliubov-group-external
  1 -> 2: citation typography (stray apostrophes, doubled stops).
- note.odd-extensions.added-axis-pseudoscalar 3 -> 4 and note.odd-extensions.one-operator-sees-difference 3 -> 4: both use
  $\gamma_5 = \gamma_0\gamma_1\gamma_2\gamma_3$, which is not the store's Hermitian chiral-loop $\gamma_5$. Under the store's
  $\gamma_5$ the two readings exchange: $I_5\gamma_5 = -\omega'$ (computed). Both notes now state their convention.
- q.tower.odd-charge (lay level and one-liner only, v3): the one-liner said "Open question"; the question is settled by
  synthesis.tower-limit-forgets-residue.

Validation: python3 -m tp check --store store --layers 1,2,3 --keep-going --author leon, filtered by read_R12.txt. It reports
no error or warning on any changed entity. It does report W222 on one-relation.schr-odinger-slow-shadow (GA-owned, a cross
product; sent to the rewriters) and the five I213 subject notices that were already in the baseline.

## For Leon
1. **A wrong citation.** scrambling.pair-mode-qubit-one-object: the formal and technical levels attribute "one ladder pair
   per point of the exceptional set" to tower.witt-index-quantum-capacity, which states only the vector capacity
   $\min(p,q)$. The statement is T04 Thm 8.7 (sheaf.schwarzschild-degeneration-boundary-tame; quoted in
   singularity.c2-cell-density). Proposed fix: cite the T04 entity in both levels and add `uses:
   sheaf.schwarzschild-degeneration-boundary-tame@<current>`. This needs a new edge, so it is your decision. The same
   miscitation is in scrambling.epoch-modular-period-two-unknowns-become (cross-subject).
2. **Status stronger than the proof (candidates).**
   - one-relation.measure-indifference-borns-rule-located: the fine-graining and continuity steps are Zurek's envariance
     argument, "imported with its critique", but no imported entity carries it. Proposed: add an imported entity for
     Zurek (2005) and a `uses` edge.
   - one-relation.record-chain-votes-measurement-without-collapse and
     one-relation.character-experience-three-record-chain-theorems: both rest on "Remark rem:recording", which is not a store
     entity (it appears under unresolved_refs). Their proofs argue rather than derive. Proposed: enter the remark as a premise
     or a note that they cite, or record the level as structural-conditional in their status.
   - one-relation.overlap-table-sorted: its proof says clauses (ii) and (iii) and the constants clause are "proved to no
     standard beyond its own statement". Proposed: the same treatment.
3. **The odd-charge question in T03's running text.** These notes still call the odd-charge limit open:
   - note.tower.abstract, note.tower.setting-scope, note.tower.setting-introduction and note.tower.setting-contribution;
   - note.tower.what-completion-means-here-why-it, which says "the real limit remembers strictly more (its real K-theory)".
   synthesis.tower-limit-forgets-residue settles the question: every tower's algebraic limit is $\Mat_{2^\infty}$ and no
   invariant separates the cases. Proposed: a remark note commenting on q.tower.odd-charge that points to the settlement.
   The paper text should be left as written.
4. **Unit principle (conventions).** The tower limit uses a formal scalar unit $1 \otimes I_4$, not U3's odd extensions,
   which do not pass to the limit. For the physical ground the symbol $I_4$ clashes with the ground's own pseudoscalar.
   Proposed: add the case to conventions.md, and possibly give the scalar factor's unit its own symbol.
5. **GA language outside the owned set** (not pure notation, so not rewritten):
   - tower.structure-tower-c-norms: the proof's tensor-Pauli matrix representation, which could be replaced by a Fock
     construction over a complex Witt basis.
   - odd-extensions.two-towers-one-curved-universe: proof (i) works the tractor calculus in components
     ($g^{-1}(\mu,\mu)$, Laplacian, scale tractor) rather than with the GTG tractor gauge field
     (synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection).
   - odd-extensions.belongs-tower: the soldering form $e(TM)$, $g(v,v)$ and $\nabla V = e$.
   - note.pairing.abstract: Newman-Penrose tetrad coefficients.
   - note.one-relation.setting-spacetime-manifold-vacuum-lines: "$g_{ab}$ varies", in words.
6. **A stale typing note.** q.tower.odd-charge's extraction typing note still says "nothing in the store settles it". It
   is history, left in place.

## Duplicates
All of these are restatements under two ids. In each case the second-named entity is the better one:
- odd-extensions.imported-towers-clock repeats dark-matter.imported-eight-towers-mod-8-clock (T14a Fact 1.1 against T14
  Fact 2.5; the T14a entity cites the other). Keep dark-matter.imported-eight-towers-mod-8-clock.
- standard-model.imported-tower-commuting-copies-fock-module is a subset of rungs.imported-tower-one-qubit-per-rung, which
  adds the Witt index and the uniqueness of $*$. Keep rungs.imported-tower-one-qubit-per-rung.
- pairing.imported-stabiliser-tangent-external lists the same three sources as
  one-relation.imported-cartans-purity-theorem-thouless-form, which has the content. Keep the Cartan-purity entity.
- rungs.imported-fock-representation-bogoliubov-group-external has the same sources and content as
  standard-model.imported-fock-representation-clifford-algebra-bogoliubov. Keep the standard-model entity.

hawking.imported-algebra-boundary-modes-car-algebra restates tower.car-limit-even-charge. That is by design.

## Known open items
- The sign of $I_6$ on $\CS$: my twistor entities (synthesis.twistor-form-states-only-off-the-real-slice and
  synthesis.positive-structure-is-twistor-form-at-imaginary-time) write "acts as $I_6$ up to sign". That is consistent with
  R10's corrected correspondence.incidence-relation-chart (4)(iii): $-I_7$ for $I_6 = a_1a_2b_1b_2b_3b_4$, $+I_7$ for
  $I_6 = I_4E$. No change was needed in R12's entities.
- The other five items (quadratic flows, boost evolution, the real structure, Hadamard step 7, operator-join constants) are
  not in R12's list.

## Further checks (no defect found)
The following were recomputed by hand or exactly:
- commuting copies and the twist (centre $\R \oplus \R$ or $\C$ by $p - q \bmod 4$);
- the transported corrector and the stagewise intertwiners;
- the C*-norm uniqueness;
- the odd roots of $-1$ and the chiral phase;
- the one-datum commutant and $CJ = \gamma_0$;
- the forced square and Hestenes' factor;
- the third-constant rotor identities and the exponent determinant $-2$;
- the Witt pairs with $I_5$, and the capacities;
- the four extensions' $\omega^2$, residues and even parts;
- the two-towers presentations;
- the incidence thermofield computations, the boost-orbit occupations and the purity formula;
- the quarter-turn map and the $W_\theta$ eigenvalues;
- the tower-top reversal and the half-period identities;
- the rung dimensions and $I_{6+2n}^2 = -1$.

## Counts
- Entities read: 119 (69 claims, objects, questions and predictions; 50 notes).
- Changed: 17 (16 with a version bump, 1 in lay level and one-liner only).
- For Leon: 6 items.
- Duplicates: 4 pairs.
- Cross-subject: 5 items (xsubject-R12.md).
- GA issues for the owners: 4 entities (ga-issues-R12.md).
- Known open items settled in R12's subjects: 1 (the $I_6$ sign, no change needed).
- tp check runs used: 1.
