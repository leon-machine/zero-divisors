# Geometric algebra conversion: dictionary and instructions

Leon's direction (21 October 2026): "The Transport Lab should be all Geometric
Algebra where possible. So twistors should be converted to GA." The store is
the living record; the papers stay as published. So the store's text moves to
geometric algebra, and the paper's original wording is kept as provenance.

The ground for the conversion is the run `twistor_ga_2026-10-16` (findings in
`../Claude outputs/twistor_ga_2026-10-16/TWGA_findings_2026-10-16.md`, 55 exact
checks, all passing, reviewed). Its result: the twistor route goes through in
real geometric algebra with no complex numbers; each imaginary unit it needs is
an element of the algebra. Read that file's sections E1 to E4 before you start.

## Conventions (from TWGA, adopted in the working note "One Complex Unit")

- $I_4$ is the spacetime pseudoscalar of $\Cl(1,3)$; the centre of $\Cl^+(1,3)$
  is $\mathrm{span}\{1, I_4\}$, $I_4^2 = -1$.
- $E = e_+e_-$ is the bivector of the ascended $(1,1)$ plane, $E^2 = +1$,
  $[I_4, E] = 0$.
- $I_6 = I_4E$ is the conformal pseudoscalar of $\Cl(2,4)$; the centre of
  $\Cl^+(2,4)$ is $\mathrm{span}\{1, I_6\}$, $I_6^2 = -1$.
- The complex unit of the spinor space of the conformal algebra is forced to be
  $\pm I_6$ (it is the commutant of the action, E1.3d), acting by right
  multiplication so that it commutes with Clifford multiplication (One Complex
  Unit, Section 10).
- Two units, deliberately distinct (One Complex Unit, 16 October): the field
  theory's unit is $i = I_4$; the twistor's unit is right multiplication by
  $I_6$. Their relative sign carries T12's orientation bit, so never identify them.
- At a point, the spinor space splits as $L_0 \oplus L_\infty$, the
  $E = +1$ and $E = -1$ eigenspaces; $I_6 = +I_4$ on $L_0$ and $-I_4$ on
  $L_\infty$. These are the two chiral doublets (E1.6). The chirality inside a
  conformal spinor is the eigenvalue of the ascent plane's bivector.
- A massless field's complex unit is $\pm I_4$ by helicity sector; on chiral
  Weyl spinors $I_4$ agrees with Hestenes' $I\sigma_3$ up to the chirality sign
  (E3). The series' chosen unit is $i = I_4$ (One Complex Unit, 16 October).
- The tower's ladder pairs, dressed by $I_4$, are Majorana pairs; $\pm I_4$ is
  the unique Lorentz-invariant such choice inside $\Cl(1,3)$ (E4.1).

## Dictionary

| Twistor language (paper) | Geometric algebra (store) |
|---|---|
| twistor space $\T$, $\mathbb{T} \cong \C^4$ | the conformal spinor space $\CS = \Cl^+(2,4)P$, the minimal left ideal of the even conformal algebra, a 4-dimensional module over the complex unit $I_6$ |
| a twistor $Z$ | a conformal spinor $Z \in \CS$ |
| projective twistor space $\PT$ | the projective spinor space $\PCS$ (the $I_6$-complex lines of $\CS$) |
| $\PT^\pm$, $\mathbb{PN}$ | the parts of $\PCS$ where the reversion form is positive, negative, zero |
| the twistor form, signature $(2,2)$ | the reversion form $h$ on $\CS$: $\tilde Z_1 Z_2 = (a + bI_6)P$ gives $h = a + bI_6$; Hermitian, of signature $(2,2)$, the unique invariant one (E1.4) |
| the factor $i$ in the twistor form or in the incidence relation | $I_6$ (E1.3d, E1.7) |
| Penrose's incidence relation $\omega = i x \pi$ | $\omega = \tfrac12 n_\infty x\, \pi$, real-linear in $x$ with no $i$; a spinor on the line of $x$ is $Z = T_x\pi$ with the translation rotor $T_x = 1 + \tfrac12 n_\infty x$ (E1.5e) |
| the line $L_x$ of a point $x$ | $L_x = \ker X(x)$ in $\CS$, the kernel of the point's null vector, $L_x = T_x L_0$ (E1.5c) |
| $\omega$ and $\pi$ parts, $\T = \Som \oplus \Spi$ | the $E = -1$ and $E = +1$ eigenspaces at the origin (keep the series' $\Som$, $\Spi$ symbols) |
| primed and unprimed spinors, the chiral doublets | the two $E$-eigenspaces, with $I_6 = \pm I_4$ there |
| $x^{AA'}$, $q_x = i x^{AA'}$ | $H_x$, with $q_x = I_6 H_x$ (E1.7) |
| complexification $V_\C$, $\Cl(2,4)_\C$, $\otimes\C$ | on the conformal spinor space only: the same space with complex unit $I_6$ (central in the even algebra). Not on $V_\C$, the full complexified algebra or the 8-dimensional Dirac module: $I_6$ anticommutes with vectors in six dimensions, so there the complexification stays as written |
| a complexified plane orthogonal to spacetime ($H_1\otimes\C$, a tower or ascended plane) | $H \oplus I_4H$ with complex unit $I_4$: $I_4$ commutes with every vector orthogonal to spacetime, and $(h + I_4k)^2 = Q(h) - Q(k) + 2I_4\,h\cdot k$ is the complex-bilinear extension of $Q$ (seed/ga_units_check.py). $I_6$ does not do this |
| dual twistor space $\T'$, $\Lambda^{\mathrm{odd}}W$ | the odd half $\CSm$ of the Dirac module |
| local twistor transport, the local twistor connection | the conformal spinor connection (the tractor connection acting on $\CS$) |
| twistor charge, twistor helicity | the charge and helicity read on $\CS$; helicity is the $\pm I_4$ sector |
| Penrose transform | the Penrose transform, with kernels in the spacetime algebra: $x\psi_0\gamma_0/x^4$ (spin 1/2), $xBx/x^6$ (Maxwell), $1/x^2$ (scalar) (E2) |
| Jost's complex Lorentz path | conjugation by $E$ (the total inversion $x \mapsto -x$ on the conformal model), reached by turning one chirality through $2\pi$: $(1-\Pi) + \Pi\exp(\theta\gamma_1\gamma_2)$ (E2.4); not $\exp(\theta I_4)$ |
| palatial twistor theory, the googly problem | keep the names (they are Penrose's programmes); say what the algebra does in GA |
| Klein quadric, Pl\"ucker bivector | keep (these are conformal-model geometry, already GA); note that the point embedding is $X(x) = n_0 + x + \tfrac12 x^2 n_\infty$ |

New notation (declared in store/notation.yaml): `\CS` = $\mathbb{S}^{+}$ (the even
half of the Dirac module `\Sp`, which T09 writes $\T$) and `\PCS` = $\mathbb{P}\mathbb{S}^{+}$. `\CSm` = $\mathbb{S}^{-}$ is the odd half. Do not reuse `\T` or `\PT` in converted text.

## What to convert, entity by entity

You are given a list of entity ids. For each:

1. Read store/<kind dir>/<id>/entity.md and its proof-*.tex files.
2. **Title.** Rewrite in GA terms. Twistor words may stay only as a dictionary
   aside in parentheses ("the conformal spinor space (twistor space)").
3. **Formal level.** Rewrite in GA. The mathematics must be exactly the same
   statement: same hypotheses, same clauses, same numbers, same conclusions.
   Change the language and the notation, never the content. At the first
   mention of a converted object you may add the twistor name once, in
   parentheses, so a reader of the paper can match it. Where a clause is
   genuinely about twistor theory as a subject (for example "this is Penrose's
   palatial programme"), keep the reference and say what it is in GA.
4. **Technical, lay, one-liner levels.** Rewrite likewise. The plain levels
   should not need the word twistor at all. Keep every condition visible (the
   levels pass made these faithful; do not drop a hypothesis while rewording).
5. **Proofs.** Convert the language and notation wherever the step is a pure
   renaming under the dictionary. Where a proof step genuinely uses complex
   twistor machinery that the dictionary does not cover, keep the step and add
   a short GA reading in parentheses if one is available from TWGA; otherwise
   leave it as is and say so in the typing note. Never change a computation.
6. **Keep the original.** Before your first edit, copy the formal level
   verbatim into the front matter as `extraction.source_formal` (a YAML block
   string) and the title as `extraction.source_title`, and copy each proof file
   proof-NAME.tex to orig-proof-NAME.tex in the same folder (the toolkit reads
   only proof-*.tex, so the copy is inert provenance).
7. **Version.** If you changed the formal level or any proof, increase
   `version` by 1. Edits to the title, technical, lay and one-liner levels
   alone are cosmetic and need no bump. Do not touch pins (`id@n` in other
   entities); the maintainer repins after the pass.
8. **Record.** Add `extraction.ga_conversion:` with `by: ai-ga-pass`, `date:
   2026-10-21`, and `note:` one or two sentences: what was converted, and what
   (if anything) was kept in twistor form and why.
9. Notes (kind note, folder store/notes/) have only a formal level (the others
   are `pending`); convert the formal level and title. Notes need no version
   bump for a formal edit beyond the rule above (apply it anyway; it is cheap).

House style: no em dashes; never "honest" or "honestly"; British spelling;
$Q(v)$ for the square of a vector where a square of a vector is meant.

Check your work: after each batch of about ten entities run

    python3 -m tp check --store store --layers 1-3,5

from /home/claude/suite/transport_lab and fix every error on your entities
(E110 structure, E111 macros, E113 banned words, E116 schema). Expect E206
"changed without a version bump" only if you forgot a bump. Other agents are
editing other entities at the same time: ignore findings on ids not in your
list, and never edit an entity outside your list.

Scratch files go in
/tmp/claude-0/-home-claude/f5c21aa3-33bd-54d7-a8e9-4d9b5d6a3726/scratchpad/ga-<your group>/.

Report: the ids you converted, the ids you left unchanged (and why), every
place you kept twistor machinery in a proof, and any statement where the
conversion made you doubt the original (do not fix those; list them).
