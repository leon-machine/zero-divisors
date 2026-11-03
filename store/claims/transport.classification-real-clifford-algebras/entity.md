---
id: transport.classification-real-clifford-algebras
kind: claim
version: 3
title: Classification of the real Clifford algebras
status: proved
region: transport
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T01, deposited version
review: typed
derivations:
- name: main
  uses:
  - primer.classification-real-clifford-algebras@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_eight_entry_table
- kind: check
  ref: check.py::check_matrix_sizes_sample
locators:
  paper: T01
  number: Thm 2.5
  label: thm:classification
  line: 520
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the eight-entry d-table on all 45 signatures with n <= 8 and twelve matrix sizes. Version 2 -> 3.'
  env: theorem
  typing:
    by: ai-typing-pass
    note: 'Re-reviewed: the single edge to the primer classification it restates is kept; levels from
      the earlier pass kept. The primer proof itself only cites the classical literature.'
  repair:
    note: restatement of the T0 result primer.classification-real-clifford-algebras; derivation and proof
      text supplied by the store
subject: clifford-structure
tags: [clifford-classification, classical-theorem]
equivalent_to:
- primer.classification-real-clifford-algebras@3
imported_from:
- citation: M. F. Atiyah, R. Bott and A. Shapiro, Clifford modules (1964)
  key: ABS1964
- citation: I. R. Porteous, Clifford Algebras and the Classical Groups (1995)
  key: Porteous1995
- citation: P. Lounesto, Clifford Algebras and Spinors (2001)
  key: Lounesto2001
---

## formal
Let $d \equiv p - q \pmod 8$. Then $\Cl(p,q)$ is isomorphic, as a real associative algebra, to
\[
\begin{array}{llll}
d = 0:\ \Mat_{k}(\R), &
d = 1:\ \Mat_{k}(\R) \oplus \Mat_{k}(\R), &
d = 2:\ \Mat_{k}(\R), &
d = 3:\ \Mat_{k}(\C), \\[2pt]
d = 4:\ \Mat_{k}(\HH), &
d = 5:\ \Mat_{k}(\HH) \oplus \Mat_{k}(\HH), &
d = 6:\ \Mat_{k}(\HH), &
d = 7:\ \Mat_{k}(\C),
\end{array}
\]
with $k$ in each case determined by $\dim_\R \Cl(p,q) = 2^n$. In particular $\Cl(p,q)$ is a simple algebra except when $d \in \{1, 5\}$, i.e.\ except when $p - q \equiv 1 \pmod 4$, where it is the direct sum of two isomorphic simple algebras.

## technical
The real Clifford algebra $\Cl(p,q)$ is, as a real associative algebra, a full matrix algebra over $\R$, $\C$ or $\HH$, or a direct sum of two copies of one, and which case occurs depends only on $d \equiv p - q \pmod 8$: $\Mat_k(\R)$ for $d = 0, 2$; $\Mat_k(\R) \oplus \Mat_k(\R)$ for $d = 1$; $\Mat_k(\C)$ for $d = 3, 7$; $\Mat_k(\HH)$ for $d = 4, 6$; and $\Mat_k(\HH) \oplus \Mat_k(\HH)$ for $d = 5$. In each case the size $k$ is fixed by $\dim_\R \Cl(p,q) = 2^n$.

Consequently $\Cl(p,q)$ is a simple algebra except when $d \in \{1, 5\}$, that is when $p - q \equiv 1 \pmod 4$, where it is the direct sum of two isomorphic simple algebras.

## lay
Clifford algebras built from a space with p positive and q negative directions turn out to be familiar objects in disguise: square tables of numbers (matrices) whose entries are real numbers, complex numbers or quaternions, or a pair of such tables side by side. Which of these appears depends only on p minus q, in a pattern that repeats every eight steps. Usually the algebra is a single indivisible block; it splits into two identical pieces exactly when p minus q leaves remainder 1 on division by four.

## one-liner
The real Clifford algebra $\Cl(p,q)$ is a matrix algebra over $\R$, $\C$ or $\HH$, or a sum of two such, according to $p - q \bmod 8$, and it is simple except when $p - q \equiv 1 \pmod 4$.
