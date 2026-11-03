---
id: dark-tower-matter.imported-clifford-structure
kind: claim
version: 1
title: 'Imported: the structure of real Clifford algebras'
status: imported
region: dark-tower-matter
subject: dark-matter
tags: [classical-theorem, clifford-classification, idempotents]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T14c, the series'' standard disclaimer'
review: typed
imported_from:
- citation: C. Chevalley, The Algebraic Theory of Spinors, Columbia University Press (1954).
  key: Chevalley1954
- citation: P. Lounesto, Clifford Algebras and Spinors, 2nd ed., Cambridge University Press (2001).
  key: Lounesto2001
- citation: H. B. Lawson and M.-L. Michelsohn, Spin Geometry, Princeton University Press (1989).
  key: LawsonMichelsohn1989
locators:
  paper: T14c
  number: Fact 2.2
  label: fact:clifford
  line: 202
extraction:
  env: fact
  typing:
    by: ai-typing-pass
    note: 'Imported classical facts with their three sources; no edges. Levels pass: levels written from
      scratch, keeping every condition and level qualifier of the formal statement.'
---

## formal
(i) For $q \geq 1$, $\Cl^{0}(p,q) \cong \Cl(p,q-1)$, by $e_{a} \mapsto e_{a}e_{n}$ with $Q(e_{n}) = -1$; for $p \geq 1$, $\Cl^{0}(p,q) \cong \Cl(q, p-1)$. (ii) $\Cl(p,q)$ is a matrix algebra over $D \in \{\R, \C, \HH\}$, or a sum of two, with $D$ fixed by $p - q \bmod 8$: $\R$ at $0, 1, 2$; $\C$ at $3, 7$; $\HH$ at $4, 5, 6$. (iii) A minimal left ideal $Af$ of a simple or semisimple algebra $A$, $f$ a primitive idempotent, has commutant $\mathrm{End}_{A}(Af) \cong (fAf)^{\mathrm{op}}$, a division algebra (Schur), acting by right multiplication. Sources: \cite{Chevalley1954, Lounesto2001, LawsonMichelsohn1989}.

## technical
Three classical facts. (i) For $q \geq 1$, $\Cl^0(p,q) \cong \Cl(p,q-1)$ by $e_a \mapsto e_ae_n$ with $Q(e_n) = -1$, and for $p \geq 1$, $\Cl^0(p,q) \cong \Cl(q,p-1)$. (ii) $\Cl(p,q)$ is a matrix algebra over $D \in \{\R, \C, \HH\}$, or a sum of two, with $D$ fixed by $p - q \bmod 8$: $\R$ at $0, 1, 2$, $\C$ at $3, 7$, $\HH$ at $4, 5, 6$. (iii) A minimal left ideal $Af$ of a simple or semisimple algebra $A$, with $f$ a primitive idempotent, has commutant $(fAf)^{\mathrm{op}}$, a division algebra by Schur's lemma, acting by right multiplication.

## lay
These are textbook facts about Clifford algebras, the algebras of directions that underlie the series. They say how the even part of such an algebra matches a smaller algebra, which kind of number (real, complex or quaternionic) each algebra is built over according to its signature, and that the symmetries of its basic spinor spaces form a number system of that kind.

## one-liner
Imported: $\Cl^0(p,q) \cong \Cl(p,q-1)$, $\Cl(p,q)$ is a matrix algebra over $\R$, $\C$ or $\HH$ fixed by $p - q \bmod 8$, and a minimal left ideal's commutant is the division algebra $(fAf)^{\mathrm{op}}$.
