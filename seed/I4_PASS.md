# The quantum unit as I4: instructions

Leon's decision (One Complex Unit, 16 October 2026; confirmed for the store on
21 October): the series' field theory uses the spacetime pseudoscalar as its
imaginary unit, $i = I_4$. Read the field-theory note's own statement of it
before you start:

    grep -n 'I_4' "../Claude outputs/ga_field_theory_note_2026-10-16/FT_one_complex_unit.tex" | head -60

and seed/GA_DICTIONARY.md (the earlier pass, which converted twistor language;
it fixed the twistor's unit as right multiplication by $I_6$ and kept the two
units distinct).

## What $I_4$ is and where it can stand for i

- $I_4 = \gamma_0\gamma_1\gamma_2\gamma_3$, $I_4^2 = -1$. It is central in the
  even spacetime algebra $\Cl^+(1,3)$ and commutes with every vector orthogonal
  to spacetime (the ascended plane, every tower plane, every mode operator).
  So it commutes with every mode operator of the tower and with the CAR
  algebra the tower builds.
- It ANTICOMMUTES with the four spacetime vectors. A factor i multiplying a
  spacetime vector or an odd element cannot simply become $I_4$: the product
  becomes sesquilinear (One Complex Unit: "the geometric product of complex
  vectors is sesquilinear, because $I_4$ anticommutes with vectors"; it writes
  complex coefficients on the LEFT).
- Physical numbers are read by projecting onto $\mathrm{span}\{1, I_4\}
  \cong \mathbb{C}$.

## Convert (i becomes $I_4$)

The quantum-mechanical unit acting on the series' own operators and states:
time evolution $e^{-iHt}$ with $H$ built from modes or rungs; phases on mode
operators, ladder pairs and Witt pairs of tower planes ($e^{i\theta}$,
$w = (e + if)/2$ on a plane orthogonal to spacetime); $i[H, X]$; the
Heisenberg and CAR relations where an i appears; plane-wave mode functions of
a field ($e^{-ik\cdot x}$, written with the coefficient on the left as One
Complex Unit does); U(1) charges and helicity phases on modes; Hermitian and
unitary conditions read in $\mathrm{span}\{1, I_4\}$.

## Do not convert (leave i, and say why in the record)

- an index $i$ (sums, components $x_i$, matrix entries);
- complex analysis as such: the KMS strip, $z = x + iy$, analytic
  continuation, Wick rotation and imaginary time as a complex parameter,
  contour integrals, Fourier transforms over the reals;
- abstract complex Hilbert spaces of imported theorems (Tomita-Takesaki
  $\Delta^{it}$, Bisognano-Wichmann, Wightman axioms, Stone's theorem),
  unless the store's statement is about the tower's own algebra;
- complexified vector spaces $V_\mathbb{C}$, $\Cl(p,q)_\mathbb{C}$,
  matrix algebras over $\mathbb{C}$, $\mathbb{C}^n$ as a multiplicity space;
- the twistor's or conformal spinors' unit (that is $I_6$ acting on the
  right, set by the earlier pass);
- complex numbers used as numbers: roots of unity, complex weights such as
  $-\tfrac32 \pm i\nu$, Gaussian rationals in the checks, quaternion units
  $i, j, k$, Pauli or gamma matrices written as complex matrices;
- complex geometry of metrics (Kerr's complex shifts, complexified
  coordinates, Newman-Janis);
- any i next to a spacetime vector or odd element, unless One Complex Unit
  itself writes that very expression with $I_4$ (then copy its convention).

When in doubt, leave it and list the case in your report. A wrong
conversion is worse than a missed one.

## Mechanics, entity by entity

You are given a list of candidate ids (entities whose maths contains a bare
"i"; many are indices or complex analysis and need no change). For each:

1. Read store/<kind>/<id>/entity.md and its proof-*.tex files.
2. Decide for every i in maths: convert or leave, by the rules above.
3. If you convert anything in the formal level or a proof: first, if the
   front matter has no `extraction.source_formal` yet, copy the formal level
   verbatim there (a YAML block string) and, for each proof you will change,
   copy proof-NAME.tex to orig-proof-NAME.tex unless that file already exists
   (an earlier pass may have saved the paper's original: never overwrite it).
   Then edit, and increase `version` by 1 (once per entity, however many
   edits). Technical, lay and one-liner edits alone need no bump.
4. Add one convention sentence at the first converted place in a proof when
   it helps, e.g. "Here the imaginary unit is $I_4$, which commutes with every
   mode operator."
5. Record under `extraction:` a key `i4_conversion:` with `by: ai-i4-pass`,
   `date: 2026-10-21`, `converted:` a short list of what became $I_4$, and
   `kept:` a short list of the i's left and why. Record it also when you
   changed nothing but the entity had a quantum-unit-looking i you kept on
   purpose; skip the record when every i was plainly an index.
6. Keep pins (`id@n` in other entities) untouched; the maintainer repins.

House style: no em dashes; never "honest" or "honestly"; British spelling.

Check after each batch of about ten:

    python3 -m tp check --store store --layers 1-3,5

from /home/claude/suite/transport_lab, and fix every finding on your ids.
Other agents edit other ids at the same time (and new note folders appear
under store/notes/): ignore findings on ids not in your list and never edit
outside your list. Do not run verify scripts or layer 4.

Report: ids converted (with a few words on what), ids examined and left
unchanged by class (index, complex analysis, imported Hilbert space, numbers,
geometry), the doubtful cases you left, and anything in a statement that
looked wrong to you (do not fix those; list them).
