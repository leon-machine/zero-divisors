# Maintainer pass after run 2026-11-09-bridges (acting for Leon, the maintainer)

Leon has accepted the thirteen proposals of the run (now in `store/claims/`: eleven new entities and version 4 of
synthesis.eviction-keeps-one-replica-saddle and synthesis.eviction-keeps-one-of-catalan-many-replica-saddles) and
approved the maintainer edits below (colony/runs/2026-11-09-bridges/DECISIONS.md, items 1 to 13). You are one of two
maintainer agents, each owning a disjoint set of files (your message says which). Edit `store/` directly in
LAB = /home/claude/phys-graph. Never touch the user's computer; never spawn agents; never commit or push; do not delete
files with shell removal commands (retirements are done as the rules below say, and the orchestrator removes folders).

Background to read: DECISIONS.md; the referee reports verify/R1.md, R2.md, R3.md (overlap rulings, "for the maintainer"
and "Only Leon can decide" items); the fixers' notes findings/fixes-*.md; findings/bridges.md.

## Rules
- Read `CONTRIBUTING.md`, `docs/CONTRIBUTING-rules.md`, `store/conventions.md`; copy the format of existing entities.
- Changing an existing entity: version + 1, keep every file in its folder (orig-proof-main.tex in particular), add a
  `maintainer_pass` entry under `extraction` with a key not already present (for example `maintainer_pass_2026_11_10`)
  with `by: maintainer-2026-11-10`, `date: '2026-11-10'` and a one-sentence note of what changed and why; keep
  `proposed_by` and `credit`. Add a credit entry {name: Claude Fable 5.2, role: <what changed>, version: <new>,
  source: maintainer pass of 2026-11-10} if the change is substantive (statement, premise wording, a bound), not for
  notes.
- An entity accepted in this run (version 1, or the two at version 4) edited only in its extraction note, uses/assumes
  edges or citations stays at its version if `tp check` layers 1-3 accept that; otherwise bump.
- assumes edges: the list `assumes:` under the derivation, pinned `id@version` (see
  store/claims/dark-energy.imported-walls-sphere-theorem/entity.md). When an in-statement hypothesis becomes an
  imported Fact, cite the Fact and keep the hypothesis's label in the text. If a check then has an untouched premise,
  record it under `untouched_premises` in coverage.yaml as earlier passes did.
- House style: no em dashes; never "honest"/"honestly"/"load-bearing"; Q(v); macros only from store/notation.yaml; no
  agent, run or method names in store text (`by:` fields excepted).
- After changing a check: `PYTHONDONTWRITEBYTECODE=1 python3 colony/runcheck.py <folder>/check.py` and
  `python3 colony/check4.py <folder>` (one at a time; 2 CPUs shared).
- Validation after your edits: `PYTHONDONTWRITEBYTECODE=1 python3 -m tp check --store store --layers 1,2,3 --keep-going
  --author leon 2>&1 | tail -40`; fix every error or new warning on YOUR files; ignore findings that are only the
  other agent's (it is editing at the same time, so references to its new Facts may be unresolved until it finishes:
  re-run at the end). Do not run the full check, `tp repin`, `tp lock` or `tp build` (the orchestrator does).
- Write colony/runs/2026-11-09-bridges/maintainer-<your name>.md: every entity changed (old -> new version, one line
  each), dependants whose CONTENT may be affected (not only pins), and anything not done and why. Your final reply is
  a short summary of that file including your layers 1-3 result.

Fixed ids for the new Facts (M1 creates them, M2 cites them; do not vary the spelling):
- synthesis.imported-steenrod-cup-one-square-is-a-natural-cohomology-operation
- synthesis.imported-local-covariance-with-scaling-of-time-ordered-products
The scaling-degree rules extend the existing synthesis.imported-epstein-glaser-extension-theorem-and-ward-preserving-time-ordered-products
(M1 bumps its version; M2 pins the new version: current version + 1).

## M1 owns: new Facts, the retirement, and every entity that existed before this run
1. New Fact synthesis.imported-steenrod-cup-one-square-is-a-natural-cohomology-operation (decision 6): state it in the
   exact form the hypothesis (S) of synthesis.no-quarter-turn-odd-map-from-the-five-sphere-to-four-components uses
   (read its formal statement; include the referee's attribution sentence: the equivariant form follows from the
   acyclic-carrier construction on regular complexes by carrying the deck group along, and that passage is part of the
   Fact). Provenance Steenrod, Annals of Mathematics 48 (1947); Steenrod and Epstein, Cohomology Operations (1962);
   flagged as cited from memory, primary texts not read. Copy the format of
   synthesis.imported-atiyah-hirzebruch-filtration-of-complex-k-theory.
2. Scaling (decision 1): bump synthesis.imported-epstein-glaser-extension-theorem-and-ward-preserving-time-ordered-products
   with the scaling-degree rules exactly as the curved-field kernel entity's extraction note lists them ((SD1)-(SD4));
   new Fact synthesis.imported-local-covariance-with-scaling-of-time-ordered-products in the form that note asks for
   (Hollands and Wald 2001, 2002; Brunetti and Fredenhagen 2000 for the microlocal setting; cited from memory, not
   checked). Do not import the first Hadamard transport equation or the protraction identity: they stay stated
   hypotheses of that entity (search the store first for the protraction identity under another name, for example in
   the algebra core or the GTG object: if it is stored, say where in your report so M2 can cite it).
3. Retire synthesis.imported-haar-average-purity (decision 2) in favour of
   synthesis.quarter-turn-rotors-of-the-even-subalgebra-form-a-state-design-of-order-three: follow the store's
   retirement procedure exactly (store/tombstones.yaml entry with replaced_by, merged_from on the kept entity only if
   the format asks for it for a non-duplicate, references repointed). Scope caveat that must be recorded in the
   tombstone note and wherever a reference is repointed: the derived result gives the value at dimensions that are
   powers of two; for general m, n the classical value (Lubkin 1978) is now prior art named in
   synthesis.imported-haar-moments-of-random-pure-state (whose formal text "At n = 2 this is Lubkin's ... (Fact ...)"
   you rewrite to carry the n = 2 value itself, version + 1). Repoint or remove every remaining reference in entities
   you own and report the ones in M2's files (the thirteen new entities, open_problems.yaml) for M2. Leave the folder
   in place and list it in your report under "folder to remove" (the orchestrator removes it with git).
4. Krein premise and the gauge parameter (decision 7): in
   synthesis.capacity-and-sakharov-readings-leave-the-generation-number-free (version + 1) add that under clause K1 of
   synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields the gauge parameter is one, so the zeros of B
   obtained by moving the gauge parameter are not admissible; restate clause (iv) and its count of rule variants
   accordingly without changing its conclusion (check its check still passes; if a check line counts those zeros,
   keep the arithmetic and change the label).
5. The stored reading of the doublets' curvature coupling (decision 10): a note (and a formal sentence if the statement
   is ambiguous) on synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations: the
   cancellation at three generations is a property of the attachment modules (xi = 1/6 by their spectrum), not of the
   content, whose rung doublets carry xi = 0 at tree level (cite the tree-level result the referee R2 names) so that
   B = 8 on the content at gauge parameter one. Version + 1 if the formal text changes.
6. Eviction side (decision 13 and R3): synthesis.eviction-deficit-against-page-deficit version + 1: clause (i) restated
   from clause (vii) of synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product: sector
   value first, abstract tensor-product value kept beside it; the stored lower bound (m-1)/(2n) holds for m >= 4 on a
   sector and fails at m = 2 (state the sector bound from (vii)); (ii), (iii) unchanged; check extended with the
   sector values if the check asserts the bound. singularity.eviction-window-thermal-product-radiation-entropy and
   singularity.assembled-page-curve-up-typicality: wording only (the tensor product of marginals is the product of
   commuting even elements; cite the mode-split entity), bump only if hashed text changes.
   descent-lift.imported-fermionic-operations-are-even-reduced: a note that its content is derived for mode algebras
   in the mode-split entity; do not retire it.
7. Notes, no content change: synthesis.tower-pairing-gap-at-fixed-charges-is-twice-the-quasiparticle-energy (its
   clause (iii) is a statement about a self pair term in the vocabulary of
   synthesis.mass-terms-are-pair-terms-of-the-arrays-and-only-the-charge-separates-majorana-from-dirac); the stored
   one-loop vacuum-polarisation extension result (find it: synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator...):
   a note on clause (v) that the new curved-field kernel entity supports its first half (rotor cancellation, first
   order Ricci only) and that the clause stays argued; synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial and
   synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height: a note citing the two new rung-count results
   (k >= 4 on every side from dimension five; k = 5 on the definite side of the L^5(4) walls) and, on the lay sentence
   of the first, nothing that contradicts them.
List in your report every dependant whose CONTENT changes.

## M2 owns: the thirteen entities accepted in this run, and store/open_problems.yaml (+ open_problems_settled.yaml)
1. Fact citations: synthesis.no-quarter-turn-odd-map-from-the-five-sphere-to-four-components cites the Steenrod Fact
   for (S), label kept; (G) and (P) stay in-statement. The curved-field kernel entity (id
   synthesis.vacuum-polarisation-kernel-on-a-gravitational-field-has-the-flat-leading-part-and-no-weyl-term-of-degree-four)
   cites the bumped Epstein-Glaser Fact for (SD1)-(SD4) and the local-covariance Fact where its clause (iv) names it;
   its clauses (iii), (iv) stay argued; its extraction note says the id's phrase "no weyl term of degree four" holds
   only in the stated scope.
2. Rung counts: synthesis.definite-side-rung-count-on-the-quarter-turn-lens-wall-of-dimension-five: clause (4) now
   cites the no-odd-map entity for the lower bound (so k = 5 on the definite side holds given the Steenrod Fact and
   the stated backgrounds), keeping the Thom-space argument as a second route conditional on (T); cite the three-rung
   entity for the twisted cohomology in place of the "intended citation" sentence. Both rung-count entities get
   `assumes: sheaf.tameness@<current version>` (decision 12). Replace every other "intended citation ... sibling"
   sentence across the thirteen entities by a plain cross-reference to the stored id (order-four and mass-terms cite
   each other; the finite-averages entity cites the design entity for its clause (ii); the two eviction entities and
   the mode-split entity: direction as R3 rules, the eviction entities self-contained, the mode-split entity citing
   them; the sector lemma lives in the finite-averages entity: cut the inline lemma in the mode-split entity's clause
   (vi) and in the two eviction proofs to a citation only if the proofs stay complete, otherwise leave it and say so).
   Repin synthesis.eviction-keeps-one-of-catalan-many-replica-saddles to version 4 of the one-saddle result.
3. The retired Haar mean-purity Fact: remove or repoint every reference to synthesis.imported-haar-average-purity in
   your thirteen entities (uses edges, premise() calls in checks, claimrefs, notes: the finite-averages entity and the
   design entity have them) and in open_problems.yaml, pointing to the design entity with the powers-of-two caveat.
   After changing a check run runcheck and check4 on it.
4. Curvature coupling (decisions 7, 10): synthesis.no-single-curvature-coupling-serves-the-sakharov-zero-and-the-kasner-tilt:
   add `assumes` to the Krein premise (synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields at its
   current version) with one sentence that under its clause K1 the gauge parameter is one, so the no-go is the stored
   statement and the free-gauge-parameter clause is recorded as the counter-statement outside the premise; record the
   stored reading xi = 0 for the rung doublets.
5. store/open_problems.yaml (header comment gives the format; look at how earlier problems were settled and moved to
   open_problems_settled.yaml and follow that exactly). Dated "(10 November.)" paragraphs in `known`, attack items
   marked or restated, `entities` and `source` extended:
   - op.wall-class-invariant: three rungs fail on every side of the quarter-turn lens walls from dimension five
     (dimension five given the spin class); on the L^5(4) walls 4 <= k <= 5 on every side and k = 5 on the definite
     side (explicit five-component odd map in Cl(6,0); no four-component odd map by an exact cup-one computation in
     the stored cell model, given the Steenrod Fact); L^7(4): 4 <= k <= 6, definite side 5 or 6 (6 by Stolz 1989 as
     prior art, secondary sources only); the equivariant-index item done as a reduction (proved) and restated to what
     remains: the indefinite side of L^5(4) (4 or 5, an unstable rank-three question), L^7(4) (needs a cup-two), the
     conjectured secondary obstruction x cup rho(a)^2 for 2a = beta x, and the general function of the ring data.
   - op.qft-loops-and-renormalisation: item 3: the leading parametrix trace on a torsion-free field (rotors cancel
     exactly; first order D_x U = +(1/12) Ric(xi) R, zero on a vacuum field; Weyl squared at degree 2 through the
     Van Vleck determinant); degree counting and the extension count argued; the freedom is 15 local terms per index
     pair with coefficient functions of x' unless local covariance with scaling (now an imported Fact) is used; what
     remains: the Ward identity on the curved field, the reduction of the freedom to a constant using the new Fact,
     the first Hadamard transport equation and the protraction identity (derive in the algebra core), a state's
     kernel rather than the parametrix.
   - op.order-four-anomaly-and-sixteen (decision 8): restate around the pseudoscalar omega of the ten Majoranas
     (omega = -I(-1)^N, the classical generator of the centre of Spin(10); the Klein twist is not a candidate); its
     first two items answered negatively (argued): every mass form anticommutes with omega, Dirac terms keep it only
     modulo the Standard Model group, the Majorana element breaks it to the grading, so in the stored chain there is
     no stage where it is an unbroken symmetry that is not a gauge transformation; the mod-16 statement is not
     imported; open only for a reading without the Majorana term; fifteen against sixteen is separated by parity alone.
   - op.dark-tower-running (decision 11): settle it (negative: not posed for the odd towers; the logarithm exists in
     four dimensions only, three-dimensional confinement is decided by the effective Chern-Simons level, a scale ratio
     needs three unstored inputs; the coefficient table is the record), following the store's procedure for settled
     problems.
   - op.curvature-coupling-across-subjects: the three appearances are three objects (attachment module, xi = 1/6 by
     its spectrum; rung doublets, xi = 0 at tree level, the stored reading by decision 10; the tilt's scalar, no stored
     field); at gauge parameter one (fixed by K1, decision 7) no single coupling of the doublets gives the Sakharov
     zero and the tilt; the maintainer's two figures confirmed by the referee; restate what remains: identify the
     tilt's scalar, or show no stored field can be it. Status reformulated.
   - op.island-dictionary: the GA mode split (sub-Clifford algebras, blade projection, Klein twist to the tensor
     product); the random-state column on a parity sector ((m+n)/(mn+2); genus weights 4^g; sector mean entropy as
     the two-block case of a published formula); leading terms of every eviction comparison unchanged; the finite
     quarter-turn averages (a design of order exactly three; Haar moments to order three derived at powers of two;
     the mean-purity import retired); item 3 unchanged otherwise.
   - op.qft-structural-inputs: the number-current lead closed (the 3 | n_g verdict is unchanged by Majorana terms,
     argued); the order-four result; under K1 the gauge-parameter zeros of B are not admissible.
   - op.pair-sector-current or the neutrino problem nearest to it (choose by content): mass terms as pair terms on
     four tower modes (charge and rank separating Majorana from Dirac; the seesaw quadratic for every K); Premise (M)
     untouched.
   - op.odd-towers and op.thickness-deposit-rule: one sentence each pointing at the dark-tower coefficient table and
     what it does not decide.
   Validate the YAML (python3 -c "import yaml; yaml.safe_load(open('store/open_problems.yaml'))").
