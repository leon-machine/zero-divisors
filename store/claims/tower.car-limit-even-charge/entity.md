---
id: tower.car-limit-even-charge
kind: claim
version: 6
title: The CAR limit, even charge
status: proved
region: tower
subject: tower
tags: [car-algebra, limits]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T03, deposited version
- name: Claude Opus 5.5
  role: 'consistency pass, the complexification''s unit named in the technical level'
  version: 6
  source: maintainer pass 2026-11-07 (consistency)
review: typed
about:
- obj.tower.tower
derivations:
- name: main
  uses:
  - tower.algebraic-limit-even-charge@3
  - tower.fock-module-one-qubit-per-rung@6
  - tower.glimms-classification-car-uniqueness@1
  - tower.ladder-pairs-satisfy-car-vectors@4
  - tower.structure-tower-c-norms@10
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_tower_vectors_satisfy_the_car
- kind: check
  ref: check.py::check_fock_adjointness
- kind: check
  ref: check.py::check_ground_factor_commutes_and_correctors_unitary
- kind: proof
  derivation: main
locators:
  paper: T03
  number: Thm 5.6
  label: thm:carlimit
  line: 432
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 5 -> 6. The technical level now says which unit complexifies: the scalar 1 (x) I_4 of the tensor factor of tower.structure-tower-c-norms, central and not in any floor, and for the physical ground not its volume element gamma_0 gamma_1 gamma_2 gamma_3 (which anticommutes with the ground vectors); mathematics unchanged.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the CAR of a_j = w_j, a_j^dagger = v_j = a_j^*, the Fock adjointness with rho(x*) = rho(x)^T, and the commuting ground factor and unitary correctors. Version 2 -> 3. Sample inputs moved to module level; no change to what is tested. Version 3 -> 4. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 4 -> 5.'
  env: theorem
  typing:
    by: ai-typing-pass
    note: 'All five extracted edges are cited in the proof as premises; no context references to assess.'
---

## formal
Continue with $p - q$ even. Complexifying and completing in the unique C*-norm of the complexified limit (Lemma \claimref{tower.structure-tower-c-norms}): the result is
\[
\Cl(p,q)_\C \,\otimes\, \CAR,
\]
where $\CAR$ is the CAR algebra of countably many fermionic modes, the unique Glimm UHF algebra of type $2^\infty$; the mode operators are represented by the adjoined null vectors themselves via Proposition \claimref{tower.ladder-pairs-satisfy-car-vectors}, with $w_j = v_j^*$ both for the intrinsic *-structure of Lemma \claimref{tower.structure-tower-c-norms} and for the Fock inner product. The completed tower is the ground algebra tensored with the algebra of a free fermionic quantum field: iterated transport is second quantisation, one mode per rung.

## technical
For $p - q$ even, complexify the algebraic limit of the tower and complete it in its unique C*-norm. The complexification is that of the $*$-structure lemma: $\C$ is $\mathrm{span}\{1, I_4\}$ in a tensor factor, with unit $1 \otimes I_4$ central and in no floor; for the physical ground it is not the ground's own volume element $\gamma_0\gamma_1\gamma_2\gamma_3$, which anticommutes with the ground vectors. The result is $\Cl(p,q)_\C \otimes \CAR$, where $\CAR$ is the CAR algebra of countably many fermionic modes, the unique UHF algebra of type $2^\infty$.

The mode operators are the adjoined null vectors themselves, $a_j = w_j$ and $a_j^\dagger = v_j$, and $w_j = v_j^*$ holds both for the intrinsic *-structure of the tower and for the Fock inner product. The completed tower is thus the ground algebra tensored with the algebra of a free fermionic field: iterated transport is second quantisation, one mode per rung.

## lay
Repeatedly applying the transport step builds an infinite tower of algebras. When the signature difference is even and the tower is completed, it becomes the original algebra combined with the standard algebra of a free field of fermions with countably many modes. Each rung of the tower contributes exactly one fermionic mode, and the null vectors added at that rung act directly as its creation and annihilation operators.

## one-liner
For $p - q$ even, the C*-completion of the complexified tower limit is $\Cl(p,q)_\C \otimes \CAR$, with the adjoined null vectors as the fermionic mode operators.
