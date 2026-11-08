---
id: std-algebra.pure-spinors
kind: claim
version: 2
title: Pure spinors, Cartan's purity theorem and the Thouless form
status: imported
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- spinor-modules
- classical-theorem
- null-directions
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
  role: 'maintainer pass, foundation layer'
  version: 2
  source: run 2026-11-08-foundation-layer
review: typed
trust: ai-proposed
about:
- obj.std-algebra.minimal-left-ideal
imported_from:
- citation: E. Cartan, Lecons sur la theorie des spineurs, Hermann (1938).
  key: Cartan1938
  locator: pure spinors and their dimension count
- citation: C. Chevalley, The Algebraic Theory of Spinors, Columbia University Press (1954).
  key: Chevalley1954
  locator: Ch. III (pure spinors)
- citation: D. J. Thouless, Stability conditions and nuclear rotations in the Hartree-Fock theory, Nucl.
    Phys. 21 (1960) 225.
  key: Thouless1960
  locator: the Thouless form
founded_on:
- synthesis.continuum-completion-premise@2
checked_by:
- kind: check
  ref: check.py::check_annihilators_null_and_purity_in_low_dimension
- kind: check
  ref: check.py::check_thouless_form_is_pure
locators:
  sources:
  - key: Chevalley1954
    locator: Ch. II and III (spinors, pure spinors)
  - key: Cartan1938
    locator: pure spinors
extraction:
  maintainer_pass_2026_11_08_foundation:
    by: ai-maintainer-pass
    note: >-
      Version 1 -> 2. Leon's decision of 8 November 2026: the foundation layer. Founded on synthesis.continuum-completion-premise: the algebra it is stated in rests on the foundation. Foundation postulates are reported as what a result rests on, separately from the premises it holds given (store/conventions.md, "The foundation").
  by: algebra-core-2026-10-26
  note: 'Imported with a check: parts (ii)-(iv) are long classical proofs; part (i) is the two-line argument
    given in the technical level.'
---

## formal
In the Fock model of \claimref{std-algebra.fock-representation}, for a nonzero spinor $\psi \in \Lambda W$ let $N_\psi = \{x \in V : x \psi = 0\}$. Then:
\begin{enumerate}
\item[(i)] $N_\psi$ is totally null, so $\dim N_\psi \le k$; $\psi$ is \emph{pure} when $\dim N_\psi = k$;
\item[(ii)] every maximal totally null subspace of $V$ is $N_\psi$ for a pure $\psi$, unique up to a scalar;
\item[(iii)] (Cartan) for $k \le 3$ every nonzero spinor of definite parity is pure; for $k = 4$, $1 + w_1 w_2 w_3 w_4$ is not;
\item[(iv)] (Thouless form) for every antisymmetric $k \times k$ matrix $Z$, $\psi_Z = \exp\bigl(\sum_{i<j} Z_{ij}\, w_i \wedge w_j\bigr)$ is pure, with $N_{\psi_Z}$ spanned by $v_i - \sum_j Z_{ij} w_j$.
\end{enumerate}

## technical
The vectors that annihilate a spinor form a totally null subspace: if $x\psi = y\psi = 0$ then $(xy + yx)\psi = 2B(x,y)\psi = 0$. So at most $k$ independent vectors can annihilate a spinor, and a pure spinor is one annihilated by the maximum number. Every maximal null subspace arises from exactly one pure spinor line. In low dimension ($k \le 3$) every spinor of definite parity is pure; from $k = 4$ purity is a real condition. Near the vacuum, pure spinors have the Thouless form, the exponential of a quadratic in the creators.

## lay
A pure spinor is the most "focused" kind of spinor: as many arrows as possible annihilate it, and those arrows form a maximal family of zero-length directions. Each such family picks out one pure spinor. In small cases every spinor is pure; from eight dimensions on, most are not.

## one-liner
The annihilator of a spinor is totally null; pure spinors (annihilator of dimension $k$) correspond to maximal null subspaces, all definite-parity spinors are pure for $k \le 3$, and $\exp(\tfrac12 Z_{ij} w_i w_j)$ is pure.
