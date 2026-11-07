---
id: hawking.imported-algebra-boundary-modes-car-algebra
kind: claim
version: 6
title: 'Imported: the algebra of the boundary modes is the CAR algebra'
status: proved
region: hawking
subject: tower
tags: [car-algebra, boundary-modes]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T07, deposited version
- name: Claude Opus 5.5
  role: 'consistency pass, the charge glossed as preserved (not advanced) by the completions, the proof''s mode labelling made the premise''s, the complexification unit named, and the lay level kept to the formal statement'
  version: 6
  source: maintainer pass 2026-11-07 (consistency)
review: typed
derivations:
- name: main
  uses:
  - tower.algebraic-limit-even-charge@3
  - tower.car-limit-even-charge@6
  - tower.ladder-pairs-satisfy-car-vectors@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_physical_lineage_has_even_charge_six
- kind: check
  ref: check.py::check_mode_operators_are_the_null_pairs
- kind: check
  ref: check.py::check_fock_adjointness
- kind: proof
  derivation: main
locators:
  paper: T07
  number: Fact 2.3
  label: fact:car
  line: 412
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 5 -> 6. The formal and proof glossed the transport charge as ''the mod-8 invariant the tower''s completions advance'', against tower.rigidity-clock-frozen and obj.tower.tower (d = p - q mod 8 is constant along the tower), now ''preserve''; the proof wrote a_j = v_j, a_j^dagger = v_j^*, the reverse of the formal level and of tower.car-limit-even-charge (a_j = w_j = v_j^*, a_j^dagger = v_j; w = (e - f)/2 annihilates the Fock vacuum, checked exactly with lib/GA.py: w^2 = 0, vw + wv = 1, v w = (1 - ef)/2), now the formal''s; the technical level names the complexification''s unit (1 (x) I_4 in a tensor factor, as in tower.structure-tower-c-norms); the lay level no longer says more than the formal (the identification with the Hawking paper''s boundary modes is that paper''s reading).'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Labelling corrected to the premise''s (a_j = w_j = v_j^* annihilates the vacuum, a_j^dagger = v_j); also own exact check added: charge 6 on the physical lineage, the CAR and v* = w of the adjoined null pairs commuting with the ground copy, and the Fock adjointness. Version 2 -> 3. check strengthened (coverage judge C05): floor spanned by ground copy times mode algebra (16 * 4^k blades, k <= 3); Fock representation of the Clifford elements v_j, w_j with rho(x^*) = rho(x)^T; stale docstring remark on a swapped labelling removed. Version 3 -> 4. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 4 -> 5.'
  env: fact
  context_refs:
  - tower.algebraic-limit-even-charge
  - tower.car-limit-even-charge
  - tower.ladder-pairs-satisfy-car-vectors
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: All three uses are the tower results the fact cites as provenance and are kept unchanged.
---

## formal
For even transport charge, the completed complexified limit of the tower of iterated completions is $\Cl(p,q)_\C \otimes \CAR$, the ground algebra tensored with the CAR algebra of countably many fermionic modes, and the mode operators are the adjoined null pairs themselves ($a_j = v_j^* = w_j$, $a_j^\dagger = v_j$, with the Fock adjointness). Here the \emph{transport charge} is the mod-8 invariant $p - q \bmod 8$, which the tower's completions preserve and the \emph{lineage} is the tower of iterated completions itself, both as in \cite{ButlerT3}; the physical lineage has charge six, so the theorem applies. \emph{Provenance:} the tower paper \cite[Prop.~4.1, Thms.~5.3 and 5.6]{ButlerT3}.

## technical
For even transport charge $d = p - q \bmod 8$, the tower of iterated completions $\Cl(p+k,q+k)$, complexified and completed in its C*-norm, has limit $\Cl(p,q)_\C \otimes \CAR$: the ground algebra tensored with the CAR algebra of countably many fermionic modes. The complexification is the tower's own: $\C$ is read as $\mathrm{span}\{1, I_4\}$ in a tensor factor, its unit $1 \otimes I_4$ central and not an element of any floor (Lemma \claimref{tower.structure-tower-c-norms}).

The mode operators are the adjoined null pairs themselves, $a_j = v_j^* = w_j$ and $a_j^\dagger = v_j$, with the adjointness of the Fock module. The physical lineage has charge six, which is even, so the result applies to it.

## lay
Each step of the series' completion adds one fermionic mode. Taking infinitely many steps, for towers of even charge, produces the algebra of a free fermion field with countably many modes, attached to the original algebra. Our world's tower has charge six, so the result covers it; the Hawking paper takes these modes of the tower as its boundary modes.

## one-liner
For even transport charge the completed complexified limit of the tower is $\Cl(p,q)_\C \otimes \CAR$, with the adjoined null pairs as its mode operators, and the physical lineage, of charge six, is covered.
