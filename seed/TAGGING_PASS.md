# Tagging pass

You are tagging a slice of the Transport Lab store,
/home/claude/suite/transport_lab/store. Each result already has exactly one
`subject` (store/subjects.yaml), which colours the 3D map. Tags add themes
that cut ACROSS subjects: a bridging result stays in its home subject and
carries a tag for the other side, and selecting a tag on the site lights up
every result that carries it.

The vocabulary is store/tags.yaml: 77 tags in five groups (structures,
methods, physics, hypotheses, record). Read it in full before you start (it is
short), and keep it open. Each tag's `about` line is the test you apply.

You never edit the store. You write one answer file (section 4).

## 1. Your slice

Your brief gives you a list of ids and a slice name `<group>` (for example
`metric`, `algebra`, `car`, `matter-a`). Tag every id on the list and nothing
else.

Notes are not tagged. If an id on your list starts with `note.`, lives under
store/notes/, or has `kind: note`, leave it out of your answer file.

## 2. Reading an entity

Open store/<kind>/<id>/entity.md, where <kind> is claims, objects,
predictions or questions. Read, in this order:

1. Front matter: `title`, `kind`, `status`, `subject`, `locators.paper`.
   Also look at `derivations` (its `uses` and `assumes` show what the result
   is built from), `refuted_by` (on refuted claims), `kill_condition` (on
   predictions) and `imported_from` (on imported results).
2. `## one-liner`: the result in one sentence.
3. `## formal`: the precise statement. This is the authority when the
   one-liner and the formal level seem to differ.
4. `## technical`, only if the formal level is too terse to decide. Refuted
   claims are table rows whose formal level is just the title: for those,
   read `## technical` and `## lay`, which say what was refuted and what
   replaced it.

Do not read proof-*.tex files or the papers. If title, one-liner and formal
level do not settle a tag, the result does not clearly meet it: leave it off.

Grep, do not load: to see several entities quickly,
`grep -A3 '^## one-liner' store/claims/<id>/entity.md`.

## 3. The rules

1. **1 to 4 tags per result, and none is allowed.** Give a tag only if the
   result clearly meets its `about` line. Most results need one to three.
   An empty list `[]` is a correct answer for a result whose themes are all
   inside its subject.
2. **Tag what the result is about, not what it mentions.** A passing
   reference to the frozen point does not earn `frozen-point`; a result
   whose statement is about the frozen point does.
3. **Prefer tags that add information beyond the subject.** A tag that only
   restates the subject (for example `seesaw-and-majorana` on a neutrino
   result that is simply about neutrinos in general) is weak; use it when the
   result is specifically about the seesaw. A tag that carries the result to
   another side of the map (for example `cosmological-constant` on a walls
   result) is the most valuable kind.
4. **Do not tag what the build derives.** The build already computes, and
   the site already shows:
   - which postulates a result rests on (its "holds given" set);
   - its two-ledger class (essential, convenient, absent);
   - its status and kind (proved, imported, refuted, live, open, ...).
   So the **hypotheses** tags go only on results ABOUT the hypothesis:
   the postulate itself, and results that state, translate, test, weaken,
   discharge or refute it. A result titled "Under (S), ..." holds given (S);
   it does NOT get `hypotheses-s-r-c`. Likewise `recovers-known-physics` is
   about content (the statement is a known law or value), never about the
   ledger class.
5. **Record tags.** `refutation` goes on refuted claims, on the results their
   `refuted_by` names, and on results that perform or count a refutation.
   `live-prediction` goes on prediction entities and on results that register
   a prediction or compute the value it quotes. `classical-theorem` goes on
   standard results of the literature, whether `status: imported` or
   re-proved; a title starting "Imported:" with `status: proved` is usually a
   restatement of an earlier Transport Paper and is tagged by its content,
   like any other result.
6. **Watch the letter collisions.** The series reuses letters:

   | Letter | Meanings, and the tag each belongs to |
   |---|---|
   | (S) | slot statistics: `hypotheses-s-r-c`. S1 to S5 (simulations): `halos-and-clusters` |
   | (R) | rung reading: `hypotheses-s-r-c`. Regularity at the fixed locus: `thermal-premises`. R (reheating): `neutrino-premises`. R1 to R3: `counting-rules` |
   | (C) | constituent hypothesis: `hypotheses-s-r-c`. C (odd towers collisionless): `halos-and-clusters`. C1 to C3 and the rate model's (C): `entropy-premises` |
   | (U) | equal rank-one eigenvalues: `hypothesis-u`. Premise U (transposition rule): `dark-tower-premises`. The rate model's (U): `entropy-premises` |
   | H | H (hierarchical second stage): `neutrino-premises`. H1, H2: `dark-tower-premises` |
   | (P) | univalence: `univalence`. P1 to P5: `premises-p1-p5` |
   | (I) | interface identification: `thermal-premises`. The rate model's (I): `entropy-premises` |
   | (L_E) | boundary-mode locality and ledger locality: `entropy-premises` |

7. **Missing tags.** If a result clearly needs a theme the vocabulary lacks,
   do not invent a tag in your answers. Add a comment line at the end of your
   file: `# suggest: <proposed-id>: <one line>: <ids it would cover>`.

## 4. Your answer file

Write seed/tag_assignment_<group>.yaml: a YAML mapping from id to a flow list
of tag ids, one line per id, in the order of your slice, every id present
exactly once (empty list allowed):

```yaml
sheaf.weights-are-forced-are-kasner-exponents: [kasner, schwarzschild, forcing-and-uniqueness]
three-routes.function-linear-maps-preserve-supports: []
```

Before you finish, check the file:

```bash
cd /home/claude/suite/transport_lab
python3 - seed/tag_assignment_<group>.yaml <<'EOF'
import sys, yaml, os
vocab = {t["id"] for t in yaml.safe_load(open("store/tags.yaml"))}
ans = yaml.safe_load(open(sys.argv[1]))
for eid, tags in ans.items():
    assert isinstance(tags, list) and len(tags) <= 4, eid
    assert len(set(tags)) == len(tags), eid
    bad = [t for t in tags if t not in vocab]
    assert not bad, (eid, bad)
    assert not eid.startswith("note."), eid
    assert any(os.path.isdir(f"store/{k}/{eid}") for k in
               ("claims", "objects", "predictions", "questions")), eid
print(len(ans), "ids,", sum(map(len, ans.values())), "tags, all valid")
EOF
```

## 5. Worked examples

These are real ids. The reasoning is the part to copy.

- **sheaf.weights-are-forced-are-kasner-exponents** (subject walls). "Among
  diagonal rescalings of the Schwarzschild coframe, each prescribed limit at
  the singularity forces unique weights, and the exceptional weights are the
  Kasner exponents." `[kasner, schwarzschild, forcing-and-uniqueness]`. The
  checker lists this as a bridge into `interior`; `kasner` is what carries it
  there.
- **tower.witt-index-quantum-capacity** (subject tower). The maximal number of
  fermionic mode pairs in Cl(p,q) is the Witt index min(p,q), rising by one at
  each rung. `[witt-index, ladder-pairs, two-readings]`: a metric invariant
  read as a CAR capacity is exactly what `two-readings` is for.
- **rungs.r-s-are-one-hypothesis-two** (subject standard-model). (R) and (S)
  are equivalent at two conformal spinors, and under either Spin(10) is the
  Bogoliubov group. `[hypotheses-s-r-c, spinor-modules, pairing-and-bogoliubov]`.
  It is about the hypotheses (it shows two are one), so the hypothesis tag
  applies.
- **standard-model.under-s-mirror-inherits-desert** (subject dark-matter).
  Under (S) the mirror's one-loop running is this tower's, so the desert is
  duplicated in the mirror. `[running-and-unification, mirror-sector]`, and
  NOT `hypotheses-s-r-c`: it holds under (S), which the build records.
- **singularity.r-regularity-fixed-locus** (postulate, subject thermality).
  The premise that each single-mode marginal is KMS at the period 2 pi /
  kappa fixed by regularity of the Euclidean section.
  `[thermal-premises, hawking-temperature, modular-theory]`. This is the
  regularity (R), not the rung reading (R).
- **dark-matter.mirror-share-one-how-fragile** (subject dark-matter). The
  mirror share is one, and over the ceiling range of Hypothesis (U) a small
  change would move it far from one. `[dark-matter-ratio, mirror-sector,
  hypothesis-u]`: it tests how fragile a conclusion is to (U), which the
  `about` line names.
- **refuted.the-number-n-is-a-coincidence-dirac** (refuted, subject
  standard-model). Formal level is only the title; technical says N is one
  number in every smallness problem. `[refutation, the-number-n]`.
- **pred.neutrino-mass-sum-floor** (prediction, live). Under (H) the mass sum
  sits at the normal-ordering floor, about 0.059 eV.
  `[live-prediction, seesaw-and-majorana]`, and not `neutrino-premises`: it
  holds given (H), it is not about (H).
- **correspondence.imported-weyls-theorem** (imported, subject einstein).
  Conformal flatness iff the Weyl tensor vanishes, in dimension four or more.
  `[classical-theorem, curvature-and-field-equations]`.
- **standard-model.what-derived-what-not** (subject standard-model). The Higgs
  doublet's representation and Yukawa pattern are derived; its scale and its
  dynamics are not. `[ledger-audit, symmetry-breaking, undetermined-input]`.
- **angle.hop-across-cut** (subject thermality). A two-mode generator with a
  hop has a unique entangled ground state whose marginal is Gibbs at the
  sample point. `[finite-models, entanglement]`; not `hawking-temperature`,
  because the sample point is a toy value, not a derivation of the
  temperature.
- **primer.commutation-rule** (subject clifford-structure). v x equals x-hat v
  for x built from vectors orthogonal to v. `[grading-and-parity]`: one tag is
  enough.
- **three-routes.function-linear-maps-preserve-supports** (subject walls). A
  function-linear map on sections never enlarges a support. `[]`: a
  sheaf-internal lemma; no tag adds anything beyond its subject.
