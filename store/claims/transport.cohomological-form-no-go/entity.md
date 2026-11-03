---
id: transport.cohomological-form-no-go
kind: claim
version: 4
title: Cohomological form of the no-go
status: proved
region: transport
subject: zero-divisors
tags: [no-go, null-directions, rotors-and-stabilisers]
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
about:
- obj.transport.equivariance
- obj.transport.extension-quadratic-spaces
derivations:
- name: main
  uses:
  - transport.group-null-rotations@4
  - transport.pseudo-inverse-torsor@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T01.py
  tags:
  - num:4.8
- kind: check
  ref: check.py::check_trivial_coefficients_and_tautological_class
- kind: check
  ref: check.py::check_class_vanishes_exactly_at_the_atom
- kind: check
  ref: check.py::check_levi_equivariance
locators:
  paper: T01
  number: Thm 4.8
  label: thm:cohomological
  line: 820
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: translation part of R_u on classes independent of the class and equal to -u, theta additive; the joint system v s v = v, R_u s R_u^-1 = s inconsistent in nine settings (extensions, degenerate included), consistent at the atom Cl(1,1); Levi equivariance g R_u g^-1 = R_{g u g^-1}. Version 2 -> 3. Check strengthened: R_u asserted in N_v (inverse and fixes v); base system and each fixed-point condition asserted consistent alone; Levi step count (5) pinned. Version 3 -> 4.'
  env: theorem
  context_refs:
  - transport.no-go-level-elements
  unresolved_refs:
  - rem:atom
  typing:
    by: ai-typing-pass
    note: 'Edges kept; the element-level no-go is named only as the result this one restates cohomologically,
      so it was not added. Levels pass: conditions already kept.'
---

## formal
With trivial coefficients, $H^1(N_v;\, U) = \mathrm{Hom}(N_v, U)$, one-coboundaries vanishing; and the class of the pseudo-inverse torsor is the tautological homomorphism $\theta$, which is nonzero whenever $U \neq 0$. An $N_v$-invariant pseudo-inverse of $v$ exists, in the given extension, if and only if this class vanishes, if and only if $U = 0$, i.e.\ $n = 2$: the hyperbolic atom of Remark \ref{rem:atom} is recovered as the exact vanishing locus of the class. Three consequences:
\begin{enumerate}
\item \emph{Enlargement-independence, cohomologically.} The group $N_v$, the coefficient module $U$, and the class $\theta$ are all constructed inside $\Cl(\mathbb{V})$ and act identically in every extension; the obstruction is pulled back unchanged along every ascent, which is the cohomological restatement of the quantification over all ascents in Theorem \claimref{transport.no-go-level-elements}.
\item \emph{Levi equivariance.} By Lemma \claimref{transport.group-null-rotations}, $\theta$ intertwines the conjugation action of $\Spin(U)$ on $N_v$ with its vector action on $U$: the class is equivariant for the Levi factor of the stabiliser.
\item \emph{The full stabiliser.} A pseudo-inverse selection equivariant under any subgroup of the stabiliser of $v$ containing $N_v$, in particular under the full parabolic stabiliser of the null direction, would restrict to an $N_v$-fixed point; nonvanishing of $\theta$ on the radical therefore obstructs every enlargement of the symmetry group at once.
\end{enumerate}

## technical
Let $v$ be a null vector with hyperbolic partner, $U$ the orthogonal complement of the hyperbolic plane in $\mathbb{V}$, and $N_v \cong (U, +)$ the group of null rotations fixing $v$. With trivial coefficients $H^1(N_v; U) = \mathrm{Hom}(N_v, U)$, and the class of the pseudo-inverse torsor is the tautological homomorphism $\theta$, nonzero whenever $U \neq 0$. An $N_v$-invariant pseudo-inverse of $v$ exists in a given extension if and only if this class vanishes, if and only if $U = 0$, that is $n = 2$, the hyperbolic atom.

Three consequences follow. $N_v$, $U$ and $\theta$ are built inside $\Cl(\mathbb{V})$, so the obstruction is pulled back unchanged along every ascent; $\theta$ intertwines the conjugation action of $\Spin(U)$ on $N_v$ with its vector action on $U$; and any subgroup of the stabiliser of $v$ containing $N_v$, including the full parabolic stabiliser of $[v]$, is obstructed at once.

## lay
Earlier results show that the symmetries fixing a light-like direction slide every candidate partial inverse along by a definite amount. This theorem packages that sliding as a single algebraic invariant, which vanishes only in the smallest case of one space and one time direction. Because the invariant is built inside the original algebra, enlarging the algebra or the symmetry group cannot remove it.

## one-liner
The obstruction to an invariant pseudo-inverse of a null vector is the tautological class $\theta \in \mathrm{Hom}(N_v, U)$, which vanishes exactly when $U = 0$ and persists unchanged through every ascent and every larger symmetry group containing $N_v$.
