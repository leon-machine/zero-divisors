---
id: descent-lift.kraus-form-descent-even-states
kind: claim
version: 6
title: Kraus form of the descent on even states
status: proved
region: descent-lift
subject: descent
tags: [descent-map, mode-counting]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-descent-lift, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - descent-lift.imported-descent-modes-univalence-supplied-class@8
  - descent-lift.imported-stinespring-kraus-choi@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_kraus_sum_is_pinching
- kind: check
  ref: check.py::check_kraus_rank_is_choi_rank
- kind: check
  ref: check.py::check_even_sector_monomials_pair_up
- kind: check
  ref: check.py::check_pair_example
locators:
  paper: T05-descent-lift
  number: Prop 3.1
  label: prop:kraus
  line: 188
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the Kraus sum as the pinching for nu = 1-3, Choi ranks 2^nu and 2^(nu-1), the pairing-up of parity monomials on the even sector, and the pair example diag(16/25, 9/25). Version 3 -> 4. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 4 -> 5. Sample inputs moved to module level; no change to what is tested. Version 5 -> 6.'
  env: proposition
  typing:
    by: ai-typing-pass
    added:
    - descent-lift.imported-stinespring-kraus-choi
    note: 'added the Stinespring-Kraus-Choi fact, since the Kraus-rank clauses rest on identifying the
      Kraus rank with the Choi rank, which the proof uses without citing it; the series'' descent fact
      is a real premise and is kept. Levels pass: the lay level no longer equates physically allowed states
      with even states (the univalence rule also admits odd states); it now states the even-sector restriction
      as such.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - descent-lift.imported-stinespring-kraus-choi
---

## formal
Let $\G_{k} = (-1)^{N_{k}}$ be the parity of mode $k$ and $\G^{\kappa} = \prod_{k}\G_{k}^{\kappa_{k}}$ the parity monomials, $\kappa \in \{0,1\}^{\nu}$. On the full Fock space of $\nu$ modes the descent is $\EN(\rho) = 2^{-\nu}\sum_{\kappa}\G^{\kappa}\rho\,\G^{\kappa}$, of Kraus rank $2^{\nu}$. On the even sector, where $\G_{\mathrm{tot}} = \prod_{k}\G_{k} = 1$, the monomials pair up and the descent is $\EN(\rho) = 2^{1-\nu}\sum_{\kappa_{\nu} = 0}\G^{\kappa}\rho\,\G^{\kappa}$, of Kraus rank $2^{\nu - 1}$, every Kraus operator even and number-diagonal. For $\nu = 1$ it is the identity. For $\nu = 2$ it is $\EN(\rho) = \tfrac12(\rho + \G_{0}\rho\,\G_{0})$ on $\operatorname{span}\{\ket{00}, \ket{11}\}$, which kills exactly the pairing coherence: $c\ket{00} + s\ket{11} \mapsto \operatorname{diag}(c^{2}, s^{2})$.

## technical
With mode parities $\G_{k} = (-1)^{N_{k}}$ and parity monomials $\G^{\kappa} = \prod_{k}\G_{k}^{\kappa_{k}}$, $\kappa\in\{0,1\}^{\nu}$, the descent on the full Fock space of $\nu$ modes is $\EN(\rho) = 2^{-\nu}\sum_{\kappa}\G^{\kappa}\rho\,\G^{\kappa}$, of Kraus rank $2^{\nu}$. On the even sector, where $\prod_{k}\G_{k} = 1$, the monomials pair up and $\EN(\rho) = 2^{1-\nu}\sum_{\kappa_{\nu}=0}\G^{\kappa}\rho\,\G^{\kappa}$, of Kraus rank $2^{\nu-1}$, with every Kraus operator even and number-diagonal.

For $\nu = 1$ the descent is the identity on even states. For $\nu = 2$ it is $\tfrac12(\rho + \G_{0}\rho\,\G_{0})$ on $\operatorname{span}\{\ket{00}, \ket{11}\}$, which removes exactly the pairing coherence: $c\ket{00} + s\ket{11}\mapsto\operatorname{diag}(c^{2}, s^{2})$.

## lay
The descent can be written as an average of a state over a set of parity flips. On states of even fermion parity, half of those flips are redundant, so only half as many are needed. For a single mode nothing changes, and for a pair the descent erases precisely the coherence that makes the pair entangled.

## one-liner
On even states of $\nu$ modes the descent is an average over $2^{\nu-1}$ even, number-diagonal parity monomials, so its Kraus rank is $2^{\nu-1}$, and on the pair it removes exactly the pairing coherence.
