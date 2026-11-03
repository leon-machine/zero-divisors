---
id: obj.descent-lift.lift
kind: object
version: 2
title: Lift
status: defined
region: descent-lift
subject: descent
tags: [descent-map, ladder-pairs]
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
locators:
  paper: T05-descent-lift
  number: Def 4.1
  label: def:lift
  line: 202
extraction:
  env: definition
  typing:
    by: ai-typing-pass
    note: definition; levels written, nothing else changed.
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants:
    - descent-lift.classical-record-reproduces-descent-stores-nothing
    added_about: []
    verdict: connected
    note: A definition cannot carry uses or assumes; the added links are about edges from the claims whose
      statements use the defined notion.
---

## formal
A \emph{lift} of the descent on $\nu$ modes is an isometry $W : H_{S} \to H_{S} \otimes H_{R}$, $H_{R}$ the Fock space of $k$ rungs, that is even, $W\G_{S} = (\G_{S}\otimes\G_{R})W$, and induces the descent on the even sector: the restriction of $W\rho W^{\dagger}$ to the system's algebra equals $\EN(\rho)$ for every even $\rho$. A lift is \emph{realised} by an even unitary $U$ on $H_{S}\otimes H_{R}$ with $W = U(\,\cdot \otimes \ket{0_{R}})$.

## technical
A lift of the descent on $\nu$ modes is an isometry $W: H_{S}\to H_{S}\otimes H_{R}$, with $H_{R}$ the Fock space of $k$ rungs, that is even, $W\G_{S} = (\G_{S}\otimes\G_{R})W$, and induces the descent on the even sector: the restriction of $W\rho W^{\dagger}$ to the system's algebra equals $\EN(\rho)$ for every even $\rho$.

A lift is realised by an even unitary $U$ on $H_{S}\otimes H_{R}$ when $W = U(\,\cdot\otimes\ket{0_{R}})$, that is, when it is produced by an evolution acting on the system with the record starting in its vacuum.

## lay
A lift is a reversible way of carrying out the descent: instead of discarding information, it embeds the system in a larger space with extra record modes, so that the system on its own looks exactly as the descent leaves it. It must respect fermion parity, and it is called realised when an actual parity-respecting evolution, starting from an empty record, produces it.

## one-liner
A lift of the descent is an even isometry into the system tensored with a record of rungs whose restriction to the system reproduces the descent on even states.
