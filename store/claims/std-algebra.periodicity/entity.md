---
id: std-algebra.periodicity
kind: claim
version: 2
title: Periodicity and the table of real Clifford algebras
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- clifford-classification
- towers-by-residue
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
- name: Claude Opus 5.5
  role: 'consistency pass, idempotents of Cl(1,0) renamed P_pm; Hamilton units in bold'
  version: 2
  source: maintainer pass 2026-11-07 (consistency)
review: typed
trust: ai-proposed
about:
- obj.std-algebra.clifford-algebra
- obj.std-algebra.signature
derivations:
- name: main
  uses:
  - std-algebra.tensor-rules@1
  - std-algebra.cl11-matrix@2
  - std-algebra.blade-basis@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_small_tensor_identities
- kind: check
  ref: check.py::check_table_invariants
- kind: check
  ref: check.py::check_periodicity_of_the_invariant
locators:
  sources:
  - key: Lounesto2001
    locator: Ch. 16 (matrix representations and periodicity of 8)
  - key: Porteous1995
    locator: the tables of real Clifford algebras
  - key: ABS1964
    locator: the periodicity of Clifford algebras
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 1 -> 2. Notation: the base-case idempotents of Cl(1,0) were written e_+, e_-, the store''s names for the hyperbolic-plane generators (conventions); renamed P_pm (exact check in scratch: P_+^2 = P_+, P_+P_- = 0 in Cl(1,0)). Hamilton''s units written bold as in std-algebra.quaternions, so no roman i reads as an imaginary unit. Mathematics unchanged.'
  by: algebra-core-2026-10-26
---

## formal
\begin{enumerate}
\item[(i)] $\R \otimes \HH = \HH$, $\C \otimes \C \cong \C \oplus \C$, $\C \otimes \HH \cong \Mat_2(\C)$ and $\HH \otimes \HH \cong \Mat_4(\R)$ (all tensor products over $\R$).
\item[(ii)] For $k = 0, \dots, 8$:
\begin{center}
\begin{tabular}{c|ccccccccc}
$k$ & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 \\ \hline
$\Cl(k,0)$ & $\R$ & $\R^{2}$ & $\Mat_2(\R)$ & $\Mat_2(\C)$ & $\Mat_2(\HH)$ & $\Mat_2(\HH)^{2}$ & $\Mat_4(\HH)$ & $\Mat_8(\C)$ & $\Mat_{16}(\R)$ \\
$\Cl(0,k)$ & $\R$ & $\C$ & $\HH$ & $\HH^{2}$ & $\Mat_2(\HH)$ & $\Mat_4(\C)$ & $\Mat_8(\R)$ & $\Mat_8(\R)^{2}$ & $\Mat_{16}(\R)$
\end{tabular}
\end{center}
where $A^{2} = A \oplus A$.
\item[(iii)] $\Cl(p{+}1, q{+}1) \cong \Mat_2(\Cl(p,q))$ and $\Cl(p{+}8, q) \cong \Cl(p, q{+}8) \cong \Mat_{16}(\Cl(p,q))$. Hence $\Cl(p,q)$ is determined by $n = p + q$ and $p - q \bmod 8$, and is the algebra given in \claimref{primer.classification-real-clifford-algebras}, which this result proves.
\end{enumerate}

## technical
Four small tensor identities among $\R$, $\C$ and $\HH$, the base cases in dimensions one and two, and the tensor product rules give the algebras $\Cl(k, 0)$ and $\Cl(0, k)$ up to $k = 8$. At $k = 8$ both are $16 \times 16$ real matrices, so tensoring with them changes nothing but the matrix size, and adding a hyperbolic plane only doubles it. Every real Clifford algebra is therefore a matrix algebra over $\R$, $\C$ or $\HH$, or a sum of two, fixed by $p - q$ modulo $8$.

## lay
The algebras of all the different spaces fall into a repeating pattern of eight. Each is a table of real, complex or quaternion numbers, sometimes two such tables side by side, and which kind depends only on the difference between the number of space-like and time-like directions, counted round a clock of eight hours.

## one-liner
$\Cl(p{+}1,q{+}1) \cong \Mat_2(\Cl(p,q))$, $\Cl(p{+}8,q) \cong \Cl(p,q{+}8) \cong \Mat_{16}(\Cl(p,q))$, and the table for $k \le 8$ gives every $\Cl(p,q)$ by $p - q \bmod 8$.
