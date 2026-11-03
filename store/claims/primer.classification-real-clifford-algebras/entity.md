---
id: primer.classification-real-clifford-algebras
kind: claim
version: 3
title: Classification of the real Clifford algebras
status: proved
region: primer
programme: standard
subject: standard-algebra
tags: [clifford-classification, classical-theorem]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T00, deposited version
review: typed
derivations:
- name: main
  proof: proof-main.tex
- name: via-periodicity
  uses:
  - std-algebra.periodicity@1
  proof: proof-via-periodicity.tex
checked_by:
- kind: proof
  derivation: main
- kind: proof
  derivation: via-periodicity
- kind: check
  ref: check.py::check_classification_table
- kind: check
  ref: check.py::check_split_summands_isomorphic_and_simple
locators:
  paper: T00
  number: Thm 9.3
  label: tk:classification
  line: 482
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Second derivation via std-algebra.periodicity, which supplies the induction the primer proof leaves out (referee, 2026-10-26). Version 2 -> 3.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: Wedderburn type of Cl(p,q) from exact invariants for all 36 signatures with n <= 7, and the split summands. Version 1 -> 2.'
  env: theorem
  typing:
    by: ai-typing-pass
    note: Status left as proved, but the source's proof only points to the classical literature (ABS,
      Porteous, Lounesto) without repeating the induction; a reviewer may prefer status imported.
---

## formal
Let $d \equiv p - q \pmod 8$. Then $\Cl(p,q)$ is isomorphic, as a real associative algebra, to the entry of the table of Section \ref{sec:clock}: $\Mat_k(\R)$ for $d \in \{0, 2\}$, $\Mat_k(\C)$ for $d \in \{3, 7\}$, $\Mat_k(\HH)$ for $d \in \{4, 6\}$, $\Mat_k(\R) \oplus \Mat_k(\R)$ for $d = 1$, and $\Mat_k(\HH) \oplus \Mat_k(\HH)$ for $d = 5$, with $k$ fixed in each case by $\dim_\R \Cl(p,q) = 2^n$. In particular $\Cl(p,q)$ is simple except when $p - q \equiv 1 \pmod 4$, where it is the direct sum of two isomorphic simple algebras.

## technical
The real Clifford algebra $\Cl(p,q)$ is, as a real associative algebra, a full matrix algebra over $\R$, $\C$ or $\HH$, or a direct sum of two copies of one, and which case occurs depends only on $d \equiv p - q \pmod 8$: $\Mat_k(\R)$ for $d = 0, 2$; $\Mat_k(\R) \oplus \Mat_k(\R)$ for $d = 1$; $\Mat_k(\C)$ for $d = 3, 7$; $\Mat_k(\HH)$ for $d = 4, 6$; and $\Mat_k(\HH) \oplus \Mat_k(\HH)$ for $d = 5$. The size $k$ is fixed by $\dim_\R \Cl(p,q) = 2^n$.

In particular $\Cl(p,q)$ is simple except when $p - q \equiv 1 \pmod 4$, where it is the direct sum of two isomorphic simple algebras.

## lay
Clifford algebras built from a space with p positive and q negative directions turn out to be familiar objects in disguise: square tables of numbers whose entries are real numbers, complex numbers or quaternions, or a pair of such tables side by side. Which one appears depends only on p minus q, in a pattern that repeats every eight steps. The algebra splits into two identical pieces exactly when p minus q leaves remainder 1 on division by four.

## one-liner
$\Cl(p,q)$ is a matrix algebra over $\R$, $\C$ or $\HH$, or a sum of two such, according to $p - q \bmod 8$, and it is simple except when $p - q \equiv 1 \pmod 4$.
