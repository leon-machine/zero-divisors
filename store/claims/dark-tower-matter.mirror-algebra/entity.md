---
id: dark-tower-matter.mirror-algebra
kind: claim
version: 4
title: The mirror's even algebra as a real isomorphism
status: proved
region: dark-tower-matter
subject: dark-matter
tags:
- mirror-sector
- grading-and-parity
- pseudoscalar-and-centre
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
derivations:
- name: main
  uses:
  - dark-tower-matter.imported-clifford-structure@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_T14c.py
  tags:
  - id:I1
  - id:I2
  - id:I3
- kind: check
  ref: check.py::check_even_isomorphism_reversed_signature
- kind: check
  ref: check.py::check_pseudoscalars
- kind: check
  ref: check.py::check_full_algebras_differ
locators:
  paper: T14c
  number: Thm 8.1
  label: thm:mirror
  line: 723
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the sign map is multiplicative between even algebras of reversed signatures for all p + q <= 6; I4'' -> I4, I6'' -> -I6; Cl(1,3) and Cl(3,1) module commutants H (dim 8) and R (dim 4) computed. Version 2 -> 3. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 3 -> 4.'
  env: theorem
  typing:
    by: ai-typing-pass
    note: 'Kept the Clifford-structure fact, cited for the commutants in (iii). The isomorphism of even
      algebras of reversed signature is classical (the source credits Porteous and Lounesto), but that
      statement is not in the store as an imported claim apart from the Clifford fact already used, so
      no standard-route derivation was added. Levels pass: levels written from scratch, keeping every
      condition and level qualifier of the formal statement.'
about:
- obj.dark-matter.spinor-module-type
---

## formal
\begin{enumerate}
\item[(i)] The linear map $e_{K} \mapsto (-1)^{|K|/2}e_{K}$ on even basis blades is an algebra isomorphism from the even algebra of a signature onto the even algebra of the reversed signature (every $Q(e_{a})$ negated); in particular $\Cl^{0}(3,1) \cong \Cl^{0}(1,3)$ and $\Cl^{0}(4,2) \cong \Cl^{0}(2,4)$.
\item[(ii)] It carries the mirror's pseudoscalar $I_{4}'$ to $+I_{4}$ and its conformal pseudoscalar $I_{6}'$ to $-I_{6}$.
\item[(iii)] The full algebras differ: $\Cl(1,3)$ has quaternionic irreducible modules and $\Cl(3,1)$ real ones.
\end{enumerate}

## technical
The linear map $e_K \mapsto (-1)^{|K|/2}e_K$ on even basis blades is an algebra isomorphism from the even algebra of a signature onto the even algebra of the reversed signature, with every $Q(e_a)$ negated; in particular $\Cl^0(3,1) \cong \Cl^0(1,3)$ and $\Cl^0(4,2) \cong \Cl^0(2,4)$. It carries the mirror's pseudoscalar $I_4'$ to $+I_4$ and its conformal pseudoscalar $I_6'$ to $-I_6$. The full algebras differ: $\Cl(1,3)$ has quaternionic irreducible modules and $\Cl(3,1)$ real ones.

## lay
The mirror tower has the opposite signature to ours, with the signs of space and time swapped in its metric. This theorem gives an explicit sign rule that identifies the even part of its algebra, where spinors and rotations live, with ours, using real numbers only. Under it the mirror's spacetime volume element matches ours while its conformal one comes out reversed, and the full algebras, which include vectors, still differ.

## one-liner
The sign rule $e_K \mapsto (-1)^{|K|/2}e_K$ identifies the mirror's even algebras with ours, sending $I_4'$ to $I_4$ and $I_6'$ to $-I_6$, while $\Cl(1,3)$ and $\Cl(3,1)$ differ.
