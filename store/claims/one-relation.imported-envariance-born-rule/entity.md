---
id: one-relation.imported-envariance-born-rule
kind: claim
version: 1
title: 'Imported: Born''s rule from envariance (Zurek 2005)'
status: imported
region: one-relation
subject: one-relation
tags: [measurement-and-records, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-11-07
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  version: 1
  source: maintainer pass 2026-11-07 (decisions)
review: draft
imported_from:
- citation: 'W. H. Zurek, Probabilities from entanglement, Born''s rule p_k = |psi_k|^2 from envariance, Phys. Rev. A 71 (2005), 052105; arXiv:quant-ph/0405161.'
  key: Zurek2005
  doi: 10.1103/PhysRevA.71.052105
extraction:
  note: >-
    Imported so that one-relation.measure-indifference-borns-rule-located can pin the envariance argument it
    transplants ("imported with its critique") instead of citing it from memory. Checked on 2026-11-07 against
    the OSTI record of the paper: the title, Phys. Rev. A 71, issue 5 (2005), DOI 10.1103/PhysRevA.71.052105,
    and the abstract (envariance of perfectly entangled states justifies complete ignorance of the outcome;
    for general states it yields Born's rule for the outcomes associated with Schmidt states). The steps
    (swaps of equal-modulus Schmidt states, fine-graining with an ancilla, continuity) and the additivity
    critique are stated from memory of the paper and of the discussion it prompted, not checked line by line.
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Created by the maintainer pass of 2026-11-07 (decision item B5, routine under POLICIES section 4: importing literature cited from memory), with the uses edge from one-relation.measure-indifference-borns-rule-located.'
---

## formal
Let a system $S$ be entangled with an environment $E$, the joint pure state written in Schmidt form $\ket{\psi_{SE}} = \sum_{k} a_{k}\ket{s_{k}}\ket{e_{k}}$ with orthonormal $\{\ket{s_{k}}\}$, $\{\ket{e_{k}}\}$; numbers, the amplitudes $a_{k}$ among them, are read in $\mathrm{span}\{1, I_{4}\}$, the default scalars of an abstract complex Hilbert space. A unitary $U_{S}$ acting on $S$ alone is \emph{envariant} for $\ket{\psi_{SE}}$ if some unitary $U_{E}$ on $E$ alone undoes it, $U_{E}U_{S}\ket{\psi_{SE}} = \ket{\psi_{SE}}$. Then: (i) the phases of the $a_{k}$ are envariant, so the probabilities of the outcomes $k$ can depend only on the moduli $|a_{k}|$; (ii) when $|a_{j}| = |a_{k}|$ the swap of $\ket{s_{j}}$ and $\ket{s_{k}}$ is envariant, so, if the probabilities of $S$ are determined by the state of $S$ and its local operations, the two outcomes have equal probability, and for $N$ Schmidt states of equal modulus each has probability $1/N$; (iii) for rational $|a_{k}|^{2} = m_{k}/M$, fine-graining each $\ket{e_{k}}$ through an ancilla into $m_{k}$ orthogonal states of equal amplitude $M^{-1/2}$ reduces to (ii) and gives $p_{k} = m_{k}/M = |a_{k}|^{2}$; (iv) continuity extends Born's rule $p_{k} = |a_{k}|^{2}$ to all amplitudes. \emph{Critique, as imported:} step (iii) uses that the probability of an outcome is the sum of the probabilities of the fine-grained alternatives composing it, so the derivation presupposes that probabilities exist and add, a fragment of the probabilistic reading it derives. \emph{Provenance:} \cite{Zurek2005}; the steps and the critique as remembered.

## technical
Zurek's envariance argument derives Born's rule from the symmetry of entangled states. When a system is entangled with an environment, an operation on the system that an operation on the environment alone can undo cannot change anything the system's own probabilities depend on. Phases of the Schmidt amplitudes can be undone that way, so probabilities depend only on their moduli; swaps of Schmidt states of equal modulus can too, so equal moduli give equal probabilities. Splitting each branch through an ancilla into equal-amplitude pieces then gives probability equal to the squared modulus for rational squared moduli, and continuity does the rest.

The critique imported with it: the splitting step assumes that the probability of an outcome is the sum of the probabilities of the pieces that compose it, so the argument presupposes that probabilities exist and add.

## lay
Quantum theory says the chance of an outcome is the square of the size of its part of the state, but does not explain why. Zurek showed how the rule can follow from a symmetry of entangled states: whatever can be undone by acting on the surroundings alone cannot affect the odds, which forces equal odds for equally sized parts, and splitting parts into equal pieces then gives the squared-size rule. Critics note that the argument assumes chances already exist and add up.

## one-liner
Imported (Zurek 2005): envariance of system-environment entangled states makes phases irrelevant and equal-modulus Schmidt outcomes equiprobable, and fine-graining with continuity gives Born's rule $p_{k} = |a_{k}|^{2}$, presupposing that probabilities exist and add.
