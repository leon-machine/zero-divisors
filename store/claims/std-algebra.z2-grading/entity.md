---
id: std-algebra.z2-grading
kind: claim
version: 1
title: The even subalgebra and the Z2 grading
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- grading-and-parity
proposed_by:
  kind: ai
  session: algebra-core-2026-10-26
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: typed
trust: ai-proposed
about:
- obj.std-algebra.even-subalgebra
- obj.std-algebra.grade-involution
derivations:
- name: main
  uses:
  - std-algebra.involution-properties@1
  - std-algebra.grade-decomposition@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_parity_and_grade_range
locators:
  sources:
  - key: Lounesto2001
    locator: Ch. 14 (definitions of the Clifford algebra)
extraction:
  by: algebra-core-2026-10-26
---

## formal
$\Cl(V, Q) = \Cl^{+} \oplus \Cl^{-}$ with $\Cl^{i} \Cl^{j} \subseteq \Cl^{i+j}$ (indices mod $2$). So $\Cl^{+}$ is a subalgebra, of dimension $2^{n-1}$ for $n \ge 1$, and $\Cl^{-}$ is a $\Cl^{+}$-bimodule. More finely, $\Cl^{j}\Cl^{k} \subseteq \bigoplus_{m} \Cl^{|j-k| + 2m}$, $0 \le m \le \min(j,k)$.

## technical
The algebra splits into even and odd parts, and products obey the parity rule: even times even is even, even times odd is odd, odd times odd is even. So the even part is a subalgebra of half the dimension. A product of a $j$-vector and a $k$-vector has grades from $|j - k|$ to $j + k$ in steps of two.

## lay
Parity multiplies like signs: even with even or odd with odd gives even, mixed gives odd. A product of a $j$-grade and a $k$-grade element can only have grades between their difference and their sum, in steps of two.

## one-liner
$\Cl = \Cl^{+} \oplus \Cl^{-}$ is a $\mathbb{Z}_2$-grading, $\dim \Cl^{+} = 2^{n-1}$, and $\Cl^{j}\Cl^{k}$ has grades $|j-k|, |j-k|+2, \dots, j+k$.
