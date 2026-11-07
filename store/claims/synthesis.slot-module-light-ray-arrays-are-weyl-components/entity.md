---
id: synthesis.slot-module-light-ray-arrays-are-weyl-components
kind: claim
version: 3
title: 'Light-ray arrays of the slot module are its Weyl components'
status: proved
region: synthesis
subject: entropy
tags: [boundary-modes, mode-counting, counting-rules]
proposed_by:
  kind: ai
  session: 2026-10-31-all-open
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: clause (i) split out into synthesis.canonical-part-of-a-spinor-on-a-null-plane, which the proof now cites; notation declaration
  version: 2
  source: maintainer pass 2026-11-07
- name: Claude Opus 5.5
  role: unit conventions per Leon's rulings of 7 November 2026 (R3)
  version: 2
  source: maintainer pass 2026-11-07 (unit rulings)
- name: Claude Opus 5.5
  role: 'GA rewrite (the two units of proof (i) named, at reader R08''s request)'
  version: 3
  source: maintainer pass 2026-11-07 (consistency)
review: draft
derivations:
- name: main
  uses:
  - synthesis.canonical-part-of-a-spinor-on-a-null-plane@1
  - synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays@5
  - field-theory.second-quantisation@6
  - synthesis.cpt-closure-forces-slot-module-and-chirality@1
  - synthesis.spin10-clause-content-is-the-neutral-singlet-choice@2
  - synthesis.half-integer-weight-array-carries-half-ln2@5
  - standard-model.majorana-element@7
  - synthesis.lowest-causal-residues-zero-four-content@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_mass_terms_enter_only_the_constraint
- kind: check
  ref: check.py::check_canonical_projector_is_residue_zero_ideal
- kind: check
  ref: check.py::check_sixteen_weyl_components_every_halving
- kind: check
  ref: check.py::check_particle_half_is_chiral
- kind: check
  ref: check.py::check_electroweak_pairing_and_neutrino_cases
- kind: check
  ref: check.py::check_generations
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays
  - standard-model.slot-module-hypothesis
  - synthesis.residue-from-mode-entropy
  - pred.boundary-mode-density
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 2 -> 3. Reader issue (ga-issues-R08.md): proof (i) now says which unit acts where: Hestenes'' right unit I_4 sigma_3 on the spinor values, span{1, I_4} on the slot module''s numbers and internal index, not identified, and the channel count (half the real dimension) independent of the choice. No change to the mathematics; the matrices in this entity are mass matrices and the Majorana symmetric matrix on the internal index, which the conventions allow, and stay.'
  maintainer_pass_unit_rulings:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Leon''s rulings R1-R4 of 7 November 2026, folded into version 2 of this pass: R3: the slot module V and its CPT halvings are read over span{1, I_4} on the tower floors (stated once in the formal level); no bare i remains, declaration removed'
  open_problem: op.residue-killing-weights
  maintainer_pass_clause_split:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Referee fix folded into version 2: (i) now records the one boundary value of Lambda(k) psi per generator that the constraint leaves free, as in the cited result. Version 1 -> 2, at Leon''s decision of 7 November 2026: the algebra of clause (i) (mass terms reach only the constraint) is now the separate result synthesis.canonical-part-of-a-spinor-on-a-null-plane, its clause (iv), with the flux identity its clause (ii), and the proof of (i) cites it; the pin to the light-ray result moves to its version 3 (the same split, statement unchanged). The two checks of (i) are kept and record the new premise in place of the light-ray result, which the check of (iv) still records. Statement unchanged. Notation: no bare imaginary unit; the complex field stays in the slot module V and is declared under outside_ga. Pins moved to current versions (statements unchanged): synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays 3 -> 4.'
  note: >-
    The problem's first line of attack, with the field content imported from the Standard Model
    subject: compute the light-ray array content of the series' matter per generation from the slot
    module and compare with the registered unit. Two findings. First, the light-ray count does not
    see whether a species is Dirac or Weyl: the canonical part on a null plane is fixed by the flux of
    the current, an algebraic identity, and every Lorentz-covariant mass term is a right multiplier,
    which reaches only the constraint that fixes the other component; so the arrays are the Weyl
    components, whatever the mass matrix, and 2 n_D + n_W of the light-ray result is their number.
    Second, every CPT halving of the slot module has a particle half of dimension sixteen, so a
    generation gives sixteen arrays and eight registered units, an integer, for every choice of the
    neutral singlet; and the particle half is chiral in every halving (only the neutral singlet is
    self-conjugate), so a generation's content cannot be grouped into gauge-covariant Dirac fields,
    and under a nonzero Majorana term it is seven Dirac species and two Majorana neutrals after
    electroweak breaking. The problem's clause "each counted species is a Dirac species" is
    therefore false for the series' matter on both readings; what holds is the count. Also bears on
    op.helicity-per-boundary-mode, second half. Transport-absent. Literature cited from memory as
    orientation only: light-front quantisation (Kogut and Soper 1970) for the mass independence of
    the null-plane data; Garcia-Etxebarria and Montero 2018 (Dai-Freed anomalies) for sixteen Weyl
    fermions per generation from a different premise.
---

## formal
Work as in Theorem \claimref{synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays}: the spacetime algebra $\Cl(1,3)$, a horizon's null plane $N_{k}$ with generators along $k = \gamma_{0} + \gamma_{3}$ and second null direction $m = \gamma_{0} - \gamma_{3}$, $B = \gamma_{3}\gamma_{0}$, $\Lambda(k) = \tfrac12(1 + B)$, $\Lambda(m) = \tfrac12(1 - B)$, so that the canonical part of a spinor on $N_{k}$ is $\Lambda(m)\psi$, one complex channel per chirality. Let $V = \Lambda^{\bullet}\C^{5}$ be the fermionic slot module (numbers and the module's complex structure are read in $\mathrm{span}\{1, I_{4}\}$, the module read on the tower's floors, where $I_{4}$ commutes with the tower vectors) (modes $1, 2$ the slots, $3, 4, 5$ the pairs) with the gauge algebra $\mathfrak{s}(\uu(2) \oplus \uu(3))$ and $Y = (3n - 2k)/6$ on states with $n$ slots and $k$ pairs (Theorem \claimref{synthesis.cpt-closure-forces-slot-module-and-chirality}), and call a CPT halving any involution $\Gamma$ commuting with the gauge algebra whose $-1$ eigenspace $V_{-}$ is isomorphic to the conjugate of its $+1$ eigenspace $V_{+}$ (Theorem \claimref{synthesis.spin10-clause-content-is-the-neutral-singlet-choice}). Read one generation as the left-handed Weyl fields valued in $V_{+}$, its antiparticles in $V_{-}$. Then:
\begin{enumerate}
\item[(i)] \emph{(Mass terms reach only the constraint.)} With $\ip{k}{m} = 2$, every vector splits as $a = \tfrac12 m\,\ip{k}{a} + \tfrac12 k\,\ip{m}{a} + a_{\perp}$, so $k\nabla = \tfrac12 km\,(k\cdot\nabla) + k\nabla_{\perp}$ contains no derivative off $N_{k}$; $km = 4\Lambda(k)$, $k$ anticommutes with $\gamma_{1}, \gamma_{2}$, and $k\Lambda(k) = 0$, so $k\psi X = k\Lambda(m)\psi X$ for every multivector $X$ acting from the right, and $L_{k}$ is injective on the image of $\Lambda(m)$. Every Lorentz-covariant mass term, of Dirac or of Majorana type, acts from the right, so on $N_{k}$ it enters only the equation that fixes $\Lambda(k)\psi$ from $\Lambda(m)\psi$: the free data on $N_{k}$ are $\Lambda(m)\psi$, with one boundary value of $\Lambda(k)\psi$ per generator, for every mass matrix (Theorem \claimref{synthesis.canonical-part-of-a-spinor-on-a-null-plane}(iv)), one complex channel per Weyl component. In the count of the light-ray result, $2n_{D} + n_{W}$ is the number of Weyl components, and whether they are grouped as Dirac or Majorana species is a property of the mass matrix that the count does not see.
\item[(ii)] \emph{(Sixteen per generation.)} The gauge-commuting CPT halvings are the $2^{5}$ choices of one member from each of the five conjugate pairs of non-neutral isotypic components of $V$, times a line in the two-dimensional neutral block; for each of them $\dim_{\C}V_{+} = 16$ and the weights of $V_{-}$ are the negatives of those of $V_{+}$. So a generation supplies $16$ arrays per light ray, $8\ln 2$ at the Hawking temperature with one (Q) version 3 array per channel (Theorem \claimref{synthesis.half-integer-weight-array-carries-half-ln2}(i)), that is $8$ registered units of two arrays, an integer, for every choice of the neutral singlet; $N_{g}$ generations give $16N_{g}$ arrays and $8N_{g}$ units. A generation without the neutral singlet, fifteen components, is not a CPT halving of $V$; it would give $\tfrac{15}{2}$ units.
\item[(iii)] \emph{(The particle half is chiral.)} In every such halving no nonzero weight of $V_{+}$ under the Cartan algebra of $\mathfrak{s}(\uu(2) \oplus \uu(3))$ has its negative in $V_{+}$, and the zero weight occurs once (the neutral singlet). A Hestenes spinor field valued in a representation $R$ carries $R$ on both chiralities, so its left-handed content is $R \oplus \bar{R}$; hence no gauge-covariant Dirac field can be formed from a generation except from neutral singlets, and among $N_{g}$ generations at most $\lfloor N_{g}/2 \rfloor$ such pairs. At the anomaly-free halving $\pm(-1)^{n + k}$ the hypercharges of $V_{+}$ are $0$ (once), $-\tfrac23$ (three times), $\tfrac16$ (six), $-\tfrac12$ (two), $1$ (once), $\tfrac13$ (three), and no nonzero value occurs with its negative.
\item[(iv)] \emph{(After electroweak breaking.)} Labelled by electric charge $T_{3} + Y$ and colour, the half $V_{+}$ of the halving $(-1)^{n + k}$ pairs into exactly $7$ charged Dirac species (up and down quarks in three colours, the electron) and $2$ neutral components. With a nonzero Majorana term, the $\nu^{c}\nu^{c}$ entry of Theorem \claimref{standard-model.majorana-element}(1), the neutral components are two Majorana species, $n_{D} = 7$ and $n_{W} = 2$; with none, and a Dirac entry pairing the neutral singlet with the doublet's neutral member, they form one Dirac species, $n_{D} = 8$; both give $16$ arrays. This clause is stated for the halvings $\pm(-1)^{n + k}$ only: whether such a Dirac entry exists in the halving with the other neutral line is not decided here, and if it does not, $n_{D} = 7$, $n_{W} = 2$ there too, again $16$ arrays.
\end{enumerate}
Hence for the series' matter the clause that each counted species is a Dirac species with both chiralities fails on the gauge-covariant reading in every halving, and under a nonzero Majorana term also on the mass reading; what is derived is the count: the CAR content of a light ray is the number of Weyl components, sixteen per generation, eight registered units. Integer-weight fields lie outside this count. The count is per four-dimensional field; a five-dimensional field contributes one array set per Kaluza-Klein level, equivalently per resolution cell of the fifth direction. This is consistent with the common count of the dark-matter premise P1 (one frozen point, one count for every tower) when that count fixes the number of light rays, the arrays per light ray being tower-dependent; if instead every tower had the same number of boundary modes, a five-dimensional tower's cells per Planck area would have to be smaller by its level count. The count of Kaluza-Klein levels as emission channels of the exterior is a different count and is not constrained by this. The projector $\Lambda(m)$ is the idempotent $f = \tfrac12(1 + e_{t}e_{a})$, $e_{t} = \gamma_{0}$, $e_{a} = \gamma_{3}$, of the residue-$0$ signature $(1,1)$ in Theorem \claimref{synthesis.lowest-causal-residues-zero-four-content}(ii): the canonical part is one chiral ideal of the even algebra of the plane of $k$ and $m$, and a mass couples it to the complementary ideal, as there.

## technical
The registered residue needs a counted unit of two s-wave arrays, and the stored light-ray result reads two arrays as one massless Dirac species. The open problem asks for a derivation that the horizon's counted species are Dirac species. This result takes the field content from the Standard Model subject, the slot module, and counts. Two points come out. The null-plane count does not see the Dirac or Weyl character of a species: the canonical part is fixed by the flux of the current, an algebraic identity, and mass terms, which in the spacetime algebra act from the right, reach only the equation that fixes the other component along the plane. So the arrays are the Weyl components, whatever the masses. And every CPT halving of the slot module has sixteen states in its particle half, so a generation gives sixteen arrays, eight units of $\ln 2$: an integer number of registered units, whichever line of the neutral block is chosen; the Standard Model without a right-handed neutrino, fifteen components, is not a halving. The particle half is chiral in every halving: apart from the neutral singlet no representation occurs with its conjugate, so the content cannot be grouped into gauge-covariant Dirac fields, and after electroweak breaking with the Majorana term it is seven Dirac species and two Majorana neutrals. The problem's Dirac clause therefore fails for the series' own matter; the count it was meant to secure holds without it. The area law still fixes only the product of arrays per light ray and cells per Planck area, so the residue is not derived here.

## lay
The series counts quantum ladders on a black hole's horizon, and a counted unit has to be two ladders. An earlier result showed that one electron-like particle, which comes in two handednesses, supplies exactly two ladders, and the open question was whether every counted particle is of that kind. This result counts the particles the series itself predicts, one generation of sixteen handed components from its slot construction. Each component supplies one ladder whatever its mass, so a generation gives sixteen ladders, eight units, a whole number. But the series' matter is handed: almost no component has a mirror partner with the same charges, so the particles cannot be grouped into two-handed ones in a way the forces respect, and with the series' neutrino mass the neutrinos are one-handed. The count works; the reason offered for it does not.

## one-liner
On a horizon's null plane mass terms reach only the constraint, so the arrays of a light ray are the Weyl components; every CPT halving of the slot module has sixteen per generation (eight registered units, for either neutral singlet), and its particle half is chiral in every halving, so the series' matter cannot be grouped into gauge-covariant Dirac species and, with a nonzero Majorana term, is seven Dirac species and two Majorana neutrals per generation.
