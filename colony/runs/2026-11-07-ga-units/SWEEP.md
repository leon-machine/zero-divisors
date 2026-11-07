# Maintainer pass 2026-11-07: the imaginary unit replaced by the GA pseudoscalar

You act for Leon (the maintainer) on a disjoint set of entities. LAB = /home/claude/phys-graph (a git
clone on branch ga-units-and-bridge-survey). Edit store/ directly, only the entities on your list. Never
commit, never touch anything outside LAB except your scratch, never spawn agents, never kill processes.

## Leon's rule (7 November 2026)
"I don't want the imaginary unit in the results anywhere when it can be replaced by a GA pseudoscalar."
The graph's language is real geometric algebra (store/conventions.md, sections "The language: geometric
algebra" and "The imaginary units": read both in full before starting). Every bare imaginary unit i (also
\mathrm{i}, \sqrt{-1}) in the formal, technical, lay and one-liner levels and in the proofs is to be
replaced by the pseudoscalar that it stands for, wherever that replacement is exact. Where it is not, it
stays and the entity declares why.

## How to replace (decide per occurrence; the meaning must be exactly preserved)
1. The field theory's unit. On even values (spinors as even multivectors, even operators, numbers read in
   span{1, I_4}) the unit is $I_4$: write $I_4$ (phases $e^{-I_4 k\cdot x}$, $e^{I_4\theta}$, $\pm I_4$,
   $I_4\hbar\partial_t$, and so on). $I_4$ is central in the even algebra, so its position among even factors
   does not matter. On values that are not even (a massive Dirac numerator $k + m$, vectors, odd elements)
   the unit is the RIGHT unit $x \mapsto xI_4$ (conventions, "Where the unit stands"): write it explicitly on
   the right of the product, or say "with the unit acting on the right" once and write $I_4$ on the right.
   Never move a right unit to the left of an odd factor. In $\gamma_5 = iI_4$ the $i$ is that right unit:
   write the chirality as $x \mapsto I_4 x I_4$ (left and right), never one merged left multiplication.
2. The conformal spinors' unit is right multiplication by $I_6$ (conventions): write it so ($\psi I_6$, or
   $J$ where the text already names $J = R_{I_6}$). Keep the two units distinct: never identify $I_4$ and
   $I_6$ (their relative sign is a datum).
3. A phase in a named plane: $e^{i\theta}$ acting as a rotation of a real two-plane is $e^{B\theta}$ with $B$
   the unit bivector (the pseudoscalar of that plane, $B^2 = -1$) acting on it; name $B$ if the text does
   not. A complex number that is a physical number (a mass-matrix entry, a CKM phase, a root of unity in a
   circulant) is read in span{1, I_4} unless the text puts it on a different plane: write it with $I_4$ and,
   on first use in the entity, say "numbers are read in span{1, I_4}". $\mathbb{Q}(i)$ becomes
   $\mathbb{Q}(I_4) = \mathrm{span}_{\mathbb{Q}}\{1, I_4\}$ where it is that field of numbers.
4. Hilbert spaces and operator theory. Where the Hilbert space is the series' own mode or Fock space built
   from geometric-algebra modes (the field theory's one-particle spaces, the continuum mode space of a
   horizon, the tower and boundary-mode CAR algebras carried in that space), its complex structure is the
   field's unit $I_4$: write $U(t) = e^{-I_4 H t}$, $\mathrm{Ad}(e^{I_4 tH})$, $\Delta^{I_4 t}$, KMS
   $\omega(A\,\alpha_{I_4\beta}(B))$, and so on. If you cannot tell from the store that the space is a
   GA-built one with unit $I_4$, leave the $i$ and declare (rule 6). An imported Fact quoted from the
   literature is stated as its source states it (keep $i$, declare `kind: imported`) unless a GA statement
   is exactly equivalent and the entity already gives its source's form.
5. Analytic continuation. Imaginary rapidity: a boost $e^{B\theta}$ continued to $\theta = i\varphi$ is the
   rotation in the dual plane, $I_4B$ (the stored identity $I_4 B = J$, synthesis.wedge-reflections-compose-
   to-the-two-pi-rotor-...): write the rotation. A complex time or rapidity $t + i\tau$ in a KMS strip whose
   unit is the field's unit may be written $t + I_4\tau$ in span{1, I_4}. Contour arguments, theta functions,
   modular forms, Fourier analysis of scalar functions in their own right, and complexifications that must
   commute with vectors (a complex null vector $e_1 \pm i e_2$, $V_{\mathbb C}$, $\Cl(p,q)_{\mathbb C}$, the
   Dirac module's plain complexification: no pseudoscalar commutes with the spacetime vectors) keep $i$
   (rule 6).
6. What stays, and how it is declared. If any bare $i$ (or $\mathbb{C}$, $\sqrt{-1}$) remains after your
   pass, add to the front matter
   `outside_ga: {kind: complex-analysis | imported | bridge | other, why: <one sentence naming where i
   stays and why no pseudoscalar can replace it, at least 20 characters>}`. If the entity already has
   outside_ga, update its `why` if needed. Do not declare an entity whose i you replaced completely.
7. Index letters are not units: $e_i$, $\sum_i$, $x^i$, $i = 1, \dots, n$, $(i)$ clause labels, $i_*$
   (pushforward) are left alone. The inventory line counts are from a detector with some false positives;
   check each.

## Bookkeeping for each entity you change (copy the pattern of store/claims/synthesis.n-plus-null-ground-state/entity.md)
- `version` + 1 (the formal level and proofs are substantive). Keep every file in the folder
  (orig-proof-main.tex in particular). Do not edit check.py files.
- Append to `credit`: `- name: Claude Opus 5.5` / `role: notation pass, imaginary unit written as the
  geometric-algebra pseudoscalar` / `version: <new>` / `source: maintainer pass 2026-11-07 (GA units)`.
  Keep every existing credit entry unchanged.
- Under `extraction` add `maintainer_pass_ga_units: {by: maintainer-2026-11-07, date: '2026-11-07', note:
  <one sentence: which units became which pseudoscalar, and what stays and why>}`.
- Do not change statuses, links, `uses`/`assumes`, pins or ledgers. Do not change mathematics: if you find
  an error, record it in your report instead of fixing it.
- Notes (store/notes/...) follow the same rules: notes are versioned too; check how their front matter
  differs and copy it.
- House style: no em dashes; never "honest"/"honestly"/"load-bearing"; Q(v) for the square of a vector;
  macros only from store/notation.yaml (I_4 is written $I_4$ or $I_{4}$; check notation.yaml for \Cl, \R and
  the like before using a macro).

## Validation
After every 10 or so entities, and at the end, run (at most one such process at a time; other agents
share the 2 CPUs):
  cd /home/claude/phys-graph && python3 -m tp check --store store --layers 1,2,3 --keep-going --author leon 2>&1 | grep -F -f <your id list file> | head -60
Fix every error or warning on your entities (other agents are editing other entities at the same time;
ignore findings on entities not on your list). W222 on one of your entities means a bare $\mathbb{C}$ or
$\sqrt{-1}$ remains without a declaration.
To re-scan your entities for a bare i, use the detector:
  python3 - <<'EOF'
  import sys; sys.path.insert(0, '/home/claude/phys-graph'); sys.path.insert(0, '/tmp/claude-0/-home-claude/23cbb9be-73ca-5537-8211-47496476158a/scratchpad/handedness')
  from bare_i import bare_i_hits
  from tp.model import load_store
  st = load_store('/home/claude/phys-graph/store')
  for eid in [l.split('\t')[0] for l in open('<your group file>')]:
      e = st.entities[eid]
      t = '\n'.join([e.levels.get(k) or '' for k in ('formal', 'technical', 'lay', 'one-liner')] + list((e.proofs or {}).values()))
      h = bare_i_hits(t)
      if h: print(eid, e.meta.get('outside_ga') is not None, h[:8])
  EOF
Every entity still listed must either carry outside_ga or have only index-letter false positives.

## Report
Write colony/runs/2026-11-07-ga-units/sweep-<group>.md: one line per entity (id, old -> new version, what
was replaced, what stays and the declared kind), then "Possible errors found" and "Unsure" (occurrences
you left with a reason, for Leon to rule on). Your final reply: the counts (entities changed, declared,
unchanged) and the Unsure list.
