---
id: synthesis.switch-planes-on-a-two-state-space
kind: claim
version: 1
title: Planes of directions on a two-state space
status: proved
region: synthesis
subject: clifford-structure
tags: [hyperbolic-plane, ladder-pairs, null-directions, classification]
proposed_by:
  kind: ai
  session: 2026-11-12-bit-switch
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: observation and direction
- name: Claude Fable 5.2
  role: 'proposal, mathematics and drafting'
  source: run 2026-11-12-bit-switch
- name: Claude Opus 5.5
  role: independent review
  source: run 2026-11-12-bit-switch
review: draft
about:
- obj.std-algebra.hyperbolic-plane
founded_on:
- synthesis.premise-superposition-over-the-integers@2
lineage:
  motivated_by:
  - std-algebra.witt-basis-car
  - std-algebra.cl11-matrix
derivations:
- name: main
  uses:
  - synthesis.set-and-clear-of-a-bit-generate-the-hyperbolic-plane@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_scalar_square_planes_are_trace_free
- kind: check
  ref: check.py::check_form_on_trace_free_maps
- kind: check
  ref: check.py::check_planes_by_signature_and_nilpotent_lines
- kind: check
  ref: check.py::check_switch_planes_and_pairs_of_states
- kind: proof
  derivation: main
extraction:
  note: >-
    From the session of 12 November 2026 on Leon's observation about the bit and the on/off switch.
    Pre-registered as Claim P of preregistration_bit_switch.md (kill conditions K2, K3, not triggered)
    before any check ran, and written into the primer T0, Section 14, as Proposition 14.10. The
    independent referee found three gaps in the first printed proof (inertia used over an ordered
    field without proof; well-definedness of the map to pairs of lines; the totally-null step), all
    closed in the proof filed here, and checked clauses (i), (ii), (iv), (v) exhaustively over the
    fields with 3, 5 and 7 elements (6, 15 and 28 switch planes, the number of pairs of lines).
    The content is elementary linear algebra of 2 x 2 matrices (the trace-zero matrices with the form
    -det are the three-dimensional quadratic space of signature (2,1)); it is recorded for the reading:
    on two states the hyperbolic planes of directions are exactly the choices of what the two states
    are. Over the rationals a plane of signature (1,1) need not contain a nilpotent line (the check
    counts them), which is why clause (iii) asks for square roots of positive elements. Ledger:
    transport-convenient; not evidence for the transport postulate.
---

## formal
Let $F$ be a field in which $2 \ne 0$, $E = \mathrm{End}_{F}(F^{2})$, $E_{0} \subset E$ the maps of trace zero, and let a \emph{switch} be a pair $(a, b)$ in $E$ with $a^{2} = b^{2} = 0$, $ab + ba = 1$ (as in Theorem \claimref{synthesis.set-and-clear-of-a-bit-generate-the-hyperbolic-plane}).
\begin{enumerate}
\item[(i)] If $V \subseteq E$ is a subspace of dimension at least $2$ in which every element squares to a scalar, then $V \subseteq E_{0}$. On $E_{0}$, $x^{2} = -\det x =: Q(x)$, and in the basis $h = wv - vw$, $v + w$, $v - w$ of a fixed switch $(v,w)$, $Q = \alpha^{2} + \sigma^{2} - \tau^{2}$.
\item[(ii)] Let $V \subseteq E_{0}$ be a plane. Its nonzero elements of square zero form two lines exactly when $V$ is spanned by a switch, one line exactly when $Q|_{V}$ is degenerate, and no line otherwise. No plane of $E_{0}$ is totally null.
\item[(iii)] If $F$ is ordered, an orthogonal basis of $V$ has squares of signs $(+,+)$, $(+,-)$ or $(+,0)$, and no other. If moreover every positive element of $F$ is a square, $V$ is spanned by a switch exactly in the case $(+,-)$.
\item[(iv)] $V$ generates $E$ as an algebra when $Q|_{V}$ is nondegenerate, and a subalgebra of dimension $3$ (conjugate to the upper triangular matrices) when it is degenerate.
\item[(v)] $V \mapsto \{\ker a, \ker b\}$, for any switch $(a,b)$ spanning $V$, is a well-defined bijection from the planes spanned by a switch to the unordered pairs of distinct lines of $F^{2}$, and any two such planes are conjugate under $\mathrm{GL}_{2}(F)$.
\end{enumerate}

## technical
On a two-state system the operations whose squares are numbers are, apart from the numbers themselves, the trace-free ones, and they form a three-dimensional quadratic space with two positive directions and one negative. A plane of such directions contains two independent operations of square zero exactly when it is spanned by a set-and-clear pair; it contains one when the form degenerates on it, and none otherwise. Over the reals the three cases are the signatures $(2,0)$, $(1,1)$ and degenerate, so a plane of directions that generates all operations is either Euclidean, with no operation of square zero, or the hyperbolic plane of a switch. The switch planes correspond one to one with the unordered pairs of distinct lines, the two states.

## lay
Suppose a system has just two states, and you look for a pair of independent directions acting on it. There are only two kinds that produce everything: a pair of ordinary perpendicular directions, or a pair made of one direction that squares to plus one and one that squares to minus one. Only the second kind contains operations that, done twice, give nothing, like switching on. And each such pair corresponds to exactly one choice of what the two states are.

## one-liner
On a two-state space over a field with $2 \ne 0$, a plane of trace-free maps contains two nilpotent lines exactly when it is spanned by a switch (one when degenerate, none otherwise); over a Euclidean field that is signature $(1,1)$, and switch planes correspond bijectively to unordered pairs of distinct lines.
