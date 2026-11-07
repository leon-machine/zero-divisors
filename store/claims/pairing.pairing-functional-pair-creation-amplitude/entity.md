---
id: pairing.pairing-functional-pair-creation-amplitude
kind: claim
version: 6
title: The pairing functional is the pair-creation amplitude
status: proved
region: pairing
subject: thermality
tags: [pairing-and-bogoliubov, spinor-modules]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-pairing, the series'' standard disclaimer'
- name: Claude Opus 5.5
  role: 'unit resolution pass, the Fock module scalars written with the central unit I_5 of Cl(2,3)'
  version: 6
  source: maintainer pass 2026-11-07 (resolve units)
review: typed
derivations:
- name: main
  uses:
  - std-algebra.fock-representation@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_vacuum_to_pair_amplitude_is_minus_pv
- kind: check
  ref: check.py::check_even_sector_two_by_two_structure
locators:
  paper: T05-pairing
  number: Prop 3.3
  label: prop:dictionary
  line: 259
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Unit principle U3: the two-mode Fock module carries a complexification that commutes with e_0, ..., e_3, so its scalars are span{1, I_5} with I_5 = I_4 e the central unit of Cl(2,3) (std-algebra.complexification-is-the-odd-extension, cited as a mention); so(4, C) is read as the bivectors complexified by I_5, and the proof''s entries 0, -1, -i, 1, i, 0 are written with I_5. Declaration removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: the i of so(4, C) and of the matrix entries is the plain complexification of the Clifford algebra on the Fock module, which must commute with the vectors. Declared other.'
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.fock-representation where the proof uses them. Version 4 -> 5.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: <12|B|0> = -pv(B) on the six basis bivectors and combinations, and the 2 x 2 structure of the even sector. Version 1 -> 2. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 2 -> 3. Check maintenance: comparisons over zip now also compare lengths, so a length mismatch cannot pass on a shorter prefix; no change to what is claimed. Version 3 -> 4.'
  env: proposition
  typing:
    by: ai-typing-pass
    removed:
    - pairing.imported-stabiliser-tangent
    note: Removed the stabiliser-tangent Fact, which the proof cites only as a reading of the computed
      matrix entries; the basis values of the pairing functional are taken as its defining formula, so
      the stabiliser proposition was not added either (a judgement call).
  i4_conversion:
    by: ai-i4-pass
    date: '2026-10-21'
    converted: []
    kept:
    - '$0, \pm i$ entries: complex numbers from the complex matrices of $e_0, \dots, e_3$ on the module,
      $\so(4, \C)$ (numbers, complexified algebra)'
---

## formal
On the two-mode Fock module of Section \ref{sec:setting}, with $\ket{12} = a_{1}^{\dagger}a_{2}^{\dagger}\ket{0}$, every bivector $B$ of $\so(4,\C)$, a complexified bivector $B_{1} + I_{5}B_{2}$ with $I_{5} = I_{4}e$ the central unit of the odd extension $\Cl(2,3)$, the module's scalars being $\mathrm{span}\{1, I_{5}\}$ (\claimref{std-algebra.complexification-is-the-odd-extension}), satisfies
\[
\bra{12}\,B\,\ket{0} \;=\; -\,\pv(B) .
\]
On the even sector $\operatorname{span}\{\ket{0}, \ket{12}\}$ at $\nu = 2$ a bivector is a $2 \times 2$ matrix: the hops $a_{1}^{\dagger}a_{2}$, $a_{2}^{\dagger}a_{1}$ kill both states, the annihilation $a_{1}a_{2}$ kills $\ket{0}$ and sends $\ket{12}$ to $-\ket{0}$, the creation $a_{1}^{\dagger}a_{2}^{\dagger}$ sends $\ket{0}$ to $\ket{12}$, and the Cartan elements are diagonal. On the vacuum, therefore, a bivector acts through its Cartan scalar and its pairing class alone.

## technical
On the two-mode Fock module with $\ket{12} = a_1^\dagger a_2^\dagger\ket{0}$, every bivector $B$ of $\so(4,\C)$, complexified with the central unit $I_{5}$ of $\Cl(2,3)$, has pair-creation amplitude $\bra{12}B\ket{0} = -\pv(B)$. On the even sector $\operatorname{span}\{\ket{0}, \ket{12}\}$ at $\nu = 2$ a bivector is a $2 \times 2$ matrix: the hops $a_1^\dagger a_2$ and $a_2^\dagger a_1$ kill both states, the annihilation $a_1 a_2$ kills $\ket{0}$ and sends $\ket{12}$ to $-\ket{0}$, the creation $a_1^\dagger a_2^\dagger$ sends $\ket{0}$ to $\ket{12}$, and the Cartan elements are diagonal.

On the vacuum, therefore, a bivector acts only through its Cartan scalar and its pairing class.

## lay
In a system of two fermion modes, an infinitesimal rotation or boost of spacetime can act on the empty state in only two ways: it can multiply it by a number, or it can create a pair of particles. The amplitude for creating the pair is exactly the pairing functional, up to a sign. Everything else the transformation does leaves the empty state alone.

## one-liner
On the two-mode Fock module every bivector satisfies $\bra{12}B\ket{0} = -\pv(B)$, so on the vacuum a bivector acts only through its Cartan scalar and its pairing class.
