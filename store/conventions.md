# Conventions of the Transport Lab store

Read this before working with the store. It says what the entities are, what
the links mean, which numbers the build computes for you, and the
conventions of notation and of the imaginary units that the texts assume.

## The model

- **Kinds.** `claim` (a result), `object` (a definition), `prediction` (with
  a kill condition), `question`, `note` (commentary: a `remark`, an `example`,
  or a `setting`, which is a run of a paper's own running text between its
  results). Nothing may use a note; notes `comments_on` the results they
  discuss.
- **Declared status.** Claims: `proved`, `imported` (from outside literature,
  with `imported_from`), `conjectured`, `refuted` (with `refuted_by`),
  `postulate` (taken as given: the series' hypotheses and premises).
  Predictions: `live`, `confirmed`, `killed`. Objects: `defined`.
- **Logical links.** A derivation lists `uses` (results it relies on) and
  `assumes` (postulates it takes as given). `about` points at definitions.
  Pinned links (`equivalent_to`, `contradicts`, `supports`, `tests`, `kills`,
  `specialises`) and lineage (`motivated_by`, `derived_from`, `supersedes`,
  `inverts`) are recorded too. A link is pinned to a version (`id@n`).
- **Derived by the build (never written by hand).** The *effective status*
  (a claim is as strong as its best derivation, a derivation as strong as its
  weakest premise), *holds given* (the postulates in a claim's past cone), the
  *ledger* (essential: needs the transport completion; convenient: also
  reachable by standard physics; absent: does not use it), *staleness* (a
  premise changed under a pinned link), the past and future *cones*, and the
  machine-check result (`pass-legacy` for tagged checks in the series' verify
  scripts, all run in exact rational arithmetic).
- **Subject and tags.** Each result has one `subject` (its home on the map,
  store/subjects.yaml) and up to four `tags` (cross-cutting themes,
  store/tags.yaml). A hypothesis tag marks results ABOUT a hypothesis; whether
  a result RESTS on one is its "holds given".
- **Ids.** An id's prefix is the region of the paper it came from
  (`singularity.*` from T05, `field-theory.*` from the note One Complex Unit;
  `list_papers` maps codes, titles and prefixes). It is not the subject: a T05
  result may live in the descent subject. Notes are `note.<region>.*`.
- **Evidence.** `pass-legacy`: tagged checks in a series verify script pass
  (exact arithmetic, run by the build). `proof-only`: the result is supported
  by its proof text alone (`checked_by: kind: proof`), not machine-checked.
  `none`: no evidence is declared (postulates, imports, predictions). A
  proof whose text only points to a verification run is reported by
  `get_proof` as a reference rather than proof text.
- **Predictions.** Their `effective_status` is their own (live, confirmed,
  killed); `basis_status` says how strongly the results they rest on hold.
- **Restatements.** A later paper often restates earlier results as a Fact
  ("Imported: ...", or a proof that says "Restated from"). The store keeps it
  as a proved claim that `uses` the originals; tools mark it
  `restates: [originals]` and each original `restated_by`. Count and rank
  with `exclude_restatements`, or read `future_cone_size_without_restatements`,
  when you want each result once.
- **Uncited premises.** `get_proof` reports premises a proof never cites with
  `\claimref`. Many papers cite by name or number in words, so this measures
  how tightly the links are drawn, not whether a proof is faulty.
- **Literal search.** `find_text` searches the LaTeX itself (formulas, exact
  phrases), including the papers' running text; `search_claims` ranks by
  meaning and words.
- **Same names.** The series reuses short names: (S) is T12's slot statistics
  and T14c's version carried to every tower; (U) is T14's equal rank-one
  eigenvalues and T14c's transposition rule (and the rate model's global
  purity in T05); (R) and (P) also recur; (R$_\Lambda$) is (R) transplanted to the cosmological horizon (`synthesis.r-lambda-regularity-cosmological-horizon`). `get_claim` lists a postulate's
  `namesakes`. Read the statement, not the letter.
- **Contradictions.** A pinned `contradicts` between two proved results would
  make the store inconsistent (error E303). Between hypotheses (at least one
  side a postulate) it records that they cannot both hold, for example T14's
  Hypothesis (U) and T12's Premise (EW): the store stays consistent, and the
  error (E307) is on any result that rests on both.
- **Retired ids.** A merged duplicate is listed in store/tombstones.yaml with
  `replaced_by`; `get_claim` on a retired id names its replacement. The kept
  entity records the merge under `extraction.merged_from`.
- **Text levels.** Every result has `formal` (the paper's statement, in
  geometric algebra), `technical`, `lay` and `one-liner`. Proofs are LaTeX.
  `\claimref{id}` marks a reference to another entity.

## Notation

- The square of a vector is written $Q(v)$; $v^2 = Q(v)$.
- $\Cl(p,q)$ has $p$ generators of square $+1$ and $q$ of square $-1$;
  spacetime is $\Cl(1,3)$, signature $(+,-,-,-)$, and the completion is
  $\Cl(2,4)$, adding the hyperbolic plane spanned by $e_+, e_-$
  ($e_+^2 = 1$, $e_-^2 = -1$).
- $n_0$ (`\nO`) and $n_\infty$ (`\nInf`) are the null vectors of the added
  plane; the point embedding is $X(x) = n_0 + x + \tfrac12 Q(x)\, n_\infty$ in
  T01. Several papers (T06, T09, T11, T16 and the pairing note) normalise
  $n_0\cdot n_\infty = +1$ and write $X(x) = n_0 + x - \tfrac12 Q(x)\, n_\infty$;
  both are consistent. T09's $n_0$ and $n_\infty$ are T01's $n_\infty$ and $n_0$
  (up to scale and sign), so T09 puts the $\pi$-plane at $E = -1/2$ where T12,
  its rungs note and the field-theory note put it at $E = +1$: read each
  paper's chirality halves in its own convention.
- Macros are in store/notation.yaml (the `notation` tool returns them).
  Conformal spinors: `\CS` $= \mathbb{S}^{+}$ (the even half of the Dirac
  module `\Sp` of $\Cl(2,4)$, the minimal left ideal $\Cl^+(2,4)P$; the papers'
  twistor space), `\CSm` $= \mathbb{S}^{-}$ (the odd half; the papers' dual
  twistor space), `\PCS` its projective space, `\Som`, `\Spi` the two chiral
  halves at a point.
- *Chirality halves* (T12, T14): `\CS`, `\CSm`, the four-dimensional halves
  of the $\Cl(2,4)$ Dirac module (Fock-grade parity). *Chiral halves at a
  point*: `\Som`, `\Spi`, the two-dimensional spacetime halves that split
  `\CS`. The two names are for different splittings.
- *The boost bivector of a null generator* has two signs in the store: the
  light-ray results write $B = n\gamma_0$ (so $L_B = +1$ on the modes of
  $k = \gamma_0 + n$), the wedge-reflection results and the massless
  frequency-sign result write $B_k = \gamma_0 n = -B$ (so $L_{B_k} = -1$
  there). Both are consistent; check which one an entity uses before
  combining signs.
- Ladder pairs are normalised $\langle v, v^{*}\rangle = 1$ in T09's
  Clifford-side proposition and $kk^{*} + k^{*}k = 1$ elsewhere (T03, T04,
  T07, T16). T14's $W$ annihilates the vacuum where T09's and T12's $W$
  creates.

## The language: geometric algebra

The graph's language is real geometric algebra. Statements (`formal`, `technical`),
proofs and checks are written in it: checks import `GA.py` (E403), and statements and
proofs use the algebra's own objects rather than the usual stand-ins for them: no Pauli
or Dirac (gamma) matrices where the vectors of $\Cl(3,0)$ or $\Cl(1,3)$ do the work, no
complex numbers where a bivector or pseudoscalar squares to $-1$, no cross product where
the outer product (or its dual) does. Ordinary scalar mathematics is geometric algebra
already (grade 0) and needs nothing; so do the Gram matrix of a form, a mass matrix, and
components such as $F^{\mu\nu}$ or structure constants $\epsilon_{ijk}$, which the
algebra uses too.

Where geometric algebra is not the right language, the entity says so:

```yaml
outside_ga:
  kind: imported            # imported | complex-analysis | bridge | other
  why: the classification is quoted as its source states it
```

- `imported`: a result taken from elsewhere, stated in its source's language;
- `complex-analysis`: analytic continuation, contour arguments, Hilbert-space structure
  (the next section lists where a bare $i$ stays);
- `bridge`: a result whose point is to connect geometric algebra with the standard
  formalism, such as a statement and its Dirac-matrix form side by side;
- `other`: anything else, with the reason judged in review.

The checks look for the unambiguous signs (Pauli or Dirac matrices named as such, a cross
product, $\mathbb{C}$, $\sqrt{-1}$, or a bare imaginary unit $i$ used as a number or a
complex structure rather than as an index) in a new or changed entity: E609 refuses a
contributor's that carries them without `outside_ga`; for a maintainer it is the warning
W222. The result's page shows the declaration. `python -m tp ga-report` lists the entities
already in the store that use such notation and declare nothing.

## The imaginary units

The store states results in real geometric algebra wherever the series
allows it. Two units, deliberately distinct (the working note "One Complex
Unit", 16 October 2026):

- **The field theory's unit is $i = I_4 = \gamma_0\gamma_1\gamma_2\gamma_3$.**
  $I_4^2 = -1$; it is central in the even spacetime algebra and commutes with
  every vector orthogonal to spacetime (the ascended plane, every tower plane,
  every tower mode operator); it anticommutes with the four spacetime vectors.
  Physical numbers are read in $\mathrm{span}\{1, I_4\} \cong \mathbb{C}$.
- **The conformal spinors' unit is right multiplication by
  $I_6 = I_4E$**, $E = e_+e_-$ (forced: it is the commutant of the conformal
  action). At a point $I_6 = +I_4$ on one chiral half and $-I_4$ on the other.
- Their relative sign carries T12's orientation bit, so they are never
  identified.
- A complexified plane orthogonal to spacetime is $H \oplus I_4H$. No
  pseudoscalar of $\Cl(2,4)$ commutes with the spacetime vectors, so
  $V_\mathbb{C}$, $\Cl(p,q)_\mathbb{C}$ and the Dirac module keep their plain
  complexification.
- **No bare imaginary unit where a pseudoscalar does the work (Leon's rule,
  7 November 2026).** A result never writes $i$ (or $\mathrm{i}$, $\sqrt{-1}$)
  where a geometric-algebra pseudoscalar can stand for it exactly: the field
  theory's unit is written $I_4$ on even values and as the right unit
  $x \mapsto xI_4$ on others; the conformal spinors' unit as right
  multiplication by $I_6$; a phase in a real two-plane as $e^{B\theta}$ with
  $B$ the plane's unit bivector (its pseudoscalar); a physical number in
  $\mathrm{span}\{1, I_4\}$; the complex structure of the series' own mode
  and Fock spaces as $I_4$ (so $e^{-I_4Ht}$, $\Delta^{I_4t}$); an imaginary
  rapidity as the rotation in the dual plane, $I_4B$. A bare $i$ stays only
  where no pseudoscalar can replace it: complex analysis in its own right
  (contours, theta functions, modular forms), a complexification that must
  commute with vectors (a complex null vector, $V_\mathbb{C}$), and an imported
  Fact quoted in its source's language. Such an entity declares
  `outside_ga` (kind `complex-analysis` or `imported`) with the reason, and the
  language check flags a bare $i$ in a new or changed entity that does not
  (E609 for a contributor, W222 for a maintainer). The store was converted to
  this rule on 7 November 2026.
- **Where the unit stands (1 November 2026).** The field theory's unit is
  $I_4$ on even values. On anything else, in particular on a massive Dirac
  line, whose numerator $k + m$ is not even, it sits outside the Clifford
  product: it is the right unit $x \mapsto xI_4$, equivalently a coefficient
  collected in front of the product. Left multiplication by $I_4$ there flips
  the relative sign of $k$ and $m$ and leaves a non-transverse vacuum
  polarisation on massive loops
  (`synthesis.one-loop-qed-in-the-spacetime-algebra`, clause (5)); the right
  unit commutes with every left action, and left and right multiplication by
  $I_4$ agree only on even elements. $I_4$ keeps its three properties
  ($I_4^2 = -1$, commuting with every bivector, anticommuting with every
  vector) only in dimension $0 \bmod 4$
  (`synthesis.unit-i4-keeps-its-three-properties-only-in-dimension-zero-mod-four`),
  so a continuation in dimension keeps the right unit, not the left one.
- **Chiral loops (2 November 2026).** The chirality element of a chiral loop is
  $\gamma_5 = iI_4$: the $I_4$ is the four-dimensional pseudoscalar
  $\gamma_0\gamma_1\gamma_2\gamma_3$ acting by left multiplication inside the
  Clifford product (in a continuation in dimension, the Breitenlohner-Maison-'t
  Hooft-Veltman element, anticommuting with the four spacetime directions and
  commuting with the evanescent ones), and the $i$ is the field theory's unit,
  standing outside the product as the right unit, a coefficient collected in
  front. So $P_{R,L} = \tfrac12(1 \pm iI_4)$ with the unit outside, and the two
  are never merged into one left multiplication
  (`synthesis.chiral-abelian-loops-with-i4-as-the-bmhv-gamma5-need-finite-symmetry-restoring-counterterms`;
  the triangle anomaly, `synthesis.triangle-anomaly-in-the-spacetime-algebra-is-the-pseudoscalar-part-of-the-field-square-and-cancels-per-generation`,
  reads the trace as $\mathrm{Tr}(\gamma_5X) = 4i\langle I_4X\rangle_0$, the unit in
  front). A
  vector-like loop has no $I_4$ at all.

Known limits of these conventions (recorded findings, not settled):

1. T05's atom is built in the spacetime radial plane $\sigma = e_0e_1$; $I_4$
   anticommutes with its mode operators, so "$I_4$ commutes with every mode"
   holds for tower planes, not for that atom.
2. The boundary-mode algebra is defined over $\mathbb{C}$ in the Hawking paper
   and as a real Clifford algebra (scalar centre) in the scrambling results.
3. T12's rungs note writes the Majorana generators $\gamma_{2i+1}$ with the
   opposite sign to T12's bidoublet and parity proofs; each is consistent
   within itself (the stored texts now carry $I_4$ for the unit).
4. The series calls two different flows "the boost flow": the real rotor
   flow $\exp(\lambda\sigma/2)$ of T05 and T08, which rescales the modes, and
   the phase flow $e^{-i\omega t}$ on the modes of T05 Thm 7.16 and T07, which
   T05 Prop 7.21 identifies as the Euclidean rotation. They share the
   generator $K = \sigma/2$ and are related by $\lambda = it$; the KMS and
   modular analysis uses the phase flow, the clock inventory and the
   scrambling law the rotor flow. The remark `note.decisions.two-boost-flows`
   states the distinction, and each result that speaks of the boost flow
   records which one it means under `extraction.flow_note` (rotor, phase, or
   both, with the reason). Which one is time is settled by
   `synthesis.phase-flow-is-time-rotor-flow-kms-continuation`: taking a time
   evolution to be a group of $*$-automorphisms preserving the states, the
   phase flow is the windows' time evolution and the rotor flow its KMS-strip
   continuation; real-time spreading for the scrambling law is left open.
5. "N" is the number of boundary modes in some T12 results and its square
   root in others; "empty conformal spinor" is a (1,0) doublet in T12 and the
   grade-zero singlet in T15.

## Gravity: Gauge Theory Gravity

- Gravity is stated in Gauge Theory Gravity: the background is flat spacetime, the vectors of
  $\Cl(1,3)$ with their fixed product; gravity is the pair of gauge fields $(\hb, \Omega)$;
  curvature is the field strength, $\mathcal{R}(B) = -R(\hb(B))$ in the store's sign; the metric
  $g(a,b) = \hb^{-1}(a)\cdot\hb^{-1}(b)$ is a derived reading, valid on the region where $\hb$
  is invertible. Definition: `obj.synthesis.gtg-flat-spacetime-gauge-fields`. Translation of
  curved-spacetime statements (physical vectors, Levi-Civita derivative, geodesics, Riemann,
  Ricci, Schouten, Weyl, Killing fields): `synthesis.imported-gtg-dictionary`; equivalence of the
  field equations: `singularity.imported-equivalence-einstein-equations`.
- "A curved spacetime with metric $g$" is written "a gravitational field $(\hb, \Omega)$ on flat
  spacetime whose derived metric is $g$"; a tensor expression stays only as a parenthetical
  reading.
- The series' $\hb$ is the map Lasenby, Doran and Gull (1998) write with an underbar; their
  overbarred map is the adjoint $\hb^{T}$. The sign of $\mathcal{R}$ is the store's curvature
  convention (de Sitter: $\Ric = \Lambda g$ in signature $(+,-,-,-)$, $\mathcal{R}(B) =
  \tfrac{\Lambda}{3}B$): the one sign flip against Doran and Lasenby (2003), ch. 14, and Lasenby,
  Doran and Gull, who write $R(\hb(B))$. A statement in their sign or in the round-sphere-positive
  one ($\Ric^{\circ} = -\Ric$) names it.
- The same holds in $d$ dimensions on flat $\R^{p,q}$ (the definition's $d$-dimensional clause).
  The tractor connection is, on flat spacetime, the $\Cl(2,4)$ gauge field
  $\Omega(a) - \nInf \wedge \hb^{-1}(a) + \nO \wedge \Sch(\hb^{-1}(a))$
  (`synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection`). Connection values computed
  from Cartan forms are the right-action ones, the negative of the definition's $\Omega$ on vectors;
  results that set them beside a GTG formula say so.
- Results that need more than one flat chart (closed or otherwise non-trivial topology, Euler
  characteristics of closed manifolds, second sheets and maximal extensions, conformal
  compactification) state their local content in this language and add a sentence beginning
  "Beyond one flat chart", naming the global ingredient; they carry the entry
  `beyond one flat chart: <ingredient>` under `extraction.flags`.

## Working with the store

- Start broad: `list_subjects`, `list_tags`, then `trail(subject)` for the
  guided walk, or `digest(subject)` for the whole subject in dependency order.
- Find: `search_claims(query)` (words, related wording, and a small preference
  for results much built upon; notes are excluded unless `include_notes`).
- List and rank across the whole store: `list_entities` (filters by subject,
  tag, status, kind, paper or proof hygiene; sorted, for example, by
  `future_cone_size` to find what is most built upon), and `get_claims` for
  many summaries at once. `list_papers` names the papers.
- Read: `get_claim(id)` (statement, levels, proofs, derived fields, the notes
  on it); `get_proof(id)` (the proof in steps, with the premises each step
  cites).
- Reason about dependence: `cone(id, "past")` (everything it rests on),
  `cone(id, "future")` (everything resting on it), `neighbourhood(id)`.
- Status words to trust: the derived `effective_status` and `holds_given`, not
  the declared status alone.
- Open problems: `list_open_problems` (filter by area, kind, difficulty, status or an
  entity) and `get_open_problem` give the curated problems to attack
  (store/open_problems.yaml): statement, why it matters, what is known, routes of
  attack, what would settle it, the entities to start from. Record the problem's id
  under `extraction.open_problem` in a draft that works on one.
- Contribute: write each new result as a folder (`entity.md`, a proof, a
  `check.py` in exact arithmetic that imports GA and reaches premises through
  `premise()`), and check it with `validate_draft` until it is clean.
  `validate_draft` runs layers 1 to 3 (and 5 on request); it never runs
  `check.py`, so run `python -m tp check --store store --layers 4` locally.
  From outside the repository the way in is a pull request adding the folders
  under `store/`, where CI runs all six layers; `propose_claim` only files the
  draft under `proposals/` in this copy, for a maintainer here to accept.
  Write `ai_involved` as `'yes'`, `'no'` or `'unknown'` in quotes. CONTRIBUTING.md
  in the repository has the full rules, and docs/example-contribution/ a worked
  example.
