---
id: synthesis.invariant-forms-on-the-fock-module-and-the-pair-counts-of-a-next-level
kind: claim
version: 1
title: 'Invariant forms on the Fock module and the pair counts they give a next level'
status: proved
region: synthesis
subject: tower
tags: [spinor-modules, witt-index, the-number-n, classical-theorem]
proposed_by:
  kind: ai
  session: 2026-11-10-phase2
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-10-phase2
review: draft
derivations:
- name: main
  uses:
  - tower.fock-module-one-qubit-per-rung@6
  - tower.witt-index-quantum-capacity@5
  - standard-model.trichotomy-what-kind-number@11
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_forms_are_invariant_and_unique
- kind: check
  ref: check.py::check_symmetry_law_neutral_signature_and_parity_pairing
- kind: check
  ref: check.py::check_counts_at_three_and_the_two_iterations
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - standard-model.why-large
  - refuted.the-number-n-is-a-mystery-of-largeness
  - standard-model.pair-count-dimension
  - standard-model.imported-pair-systems-two-chirality-halves
extraction:
  note: >-
    Adversarial test of the exponential reading of the tower carried by the observation on why $N$ is large
    (each level's objects the fermionic pairs of the level above, counts $3$, $8$, $256$, $2^{256}$). The
    question put: does the count at the second level depend on a choice. Kill condition registered before
    computing: if every construction that uses only structure stored for the tower (the Fock module, its parity
    halves, its invariant forms) gave eight pairs at the second level, the reading would be canonical there
    and that would be reported; it did not hold (the invariant symmetric form at three pairs has Witt index
    four). What is proved is classical: the bilinear forms on a spinor module that make every vector
    self-adjoint or anti-self-adjoint, their symmetry by the number of pairs modulo four, and their neutral
    signature (Chevalley, The Algebraic Theory of Spinors, 1954; Harvey, Spinors and Calibrations, 1990; both
    cited from memory and not imported). What is recorded beyond that is the statement in the series' algebra
    and its consequence for the reading: two rules with a claim to the stored wording give $3, 8, 256, 2^{256}$
    and $3, 4, 8, 128, 2^{127}$, and at three pairs the second rule gives the pair count of the tower's own
    next rung. The literal rule (states become creators, with its arithmetic and its relation to the proved
    ascent) is the subject of a sibling result of the same session, which is the intended citation for the
    reading itself and is not re-proved here; only its counts are quoted in clause (v). That no stored result
    selects either rule is argued from a search of the tower results, not audited over a full cone.
    Transport-absent: nothing here uses the transport rules beyond the pair structure of the rungs.
---

## formal
\emph{Setting.} Let $B_{k} = \Cl(k,k)$, $k \ge 1$, be the algebra of $k$ rungs with its null pairs $v_{j}, w_{j}$ ($j = 1, \ldots, k$), $v_{i}v_{j} + v_{j}v_{i} = 0$, $w_{i}w_{j} + w_{j}w_{i} = 0$, $v_{i}w_{j} + w_{j}v_{i} = \delta_{ij}$, over the rationals or any field of characteristic zero. Write $v_{S} = v_{s_{1}}\cdots v_{s_{r}}$ for a subset $S = \{s_{1} < \cdots < s_{r}\}$ of the rungs, $S^{c}$ for its complement, $p_{k} = \prod_{j} w_{j}v_{j}$ for the vacuum idempotent and $\Omega_{k} = v_{1}v_{2}\cdots v_{k}$. The left ideal $F_{k} = B_{k}p_{k}$ has the basis $v_{S}p_{k}$ and is the Fock module of Theorem \claimref{tower.fock-module-one-qubit-per-rung}, of dimension $2^{k}$, with $p_{k}$ the vacuum and $v_{S}p_{k}$ the state with the rungs of $S$ filled. Let $\tau_{+}$ be the reverse and $\tau_{-}$ the reverse composed with the grade involution, so that $\tau_{\epsilon}(a) = \epsilon a$ for every vector $a$, $\epsilon = \pm 1$.
\begin{enumerate}
\item[(i)] \emph{(The two forms.)} For $\psi, \phi \in F_{k}$ the product $\tau_{\epsilon}(\psi)\phi$ is a multiple of $\Omega_{k}$, and
\[
\tau_{\epsilon}(\psi)\,\phi \;=\; \beta_{\epsilon}(\psi, \phi)\,\Omega_{k}
\]
defines a nondegenerate bilinear form $\beta_{\epsilon}$ on $F_{k}$ with $\beta_{\epsilon}(a\psi, \phi) = \epsilon\,\beta_{\epsilon}(\psi, a\phi)$ for every vector $a$ of $B_{k}$. On the basis, $\beta_{\epsilon}(v_{S}p_{k}, v_{T}p_{k}) = \pm 1$ if $T = S^{c}$ and $0$ otherwise. Every bilinear form on $F_{k}$ with that adjoint property is a multiple of $\beta_{\epsilon}$.
\item[(ii)] \emph{(Symmetry.)} $\beta_{\epsilon}(\phi, \psi) = s_{\epsilon}(k)\,\beta_{\epsilon}(\psi, \phi)$ with $s_{\epsilon}(k) = \epsilon^{k}(-1)^{k(k-1)/2}$: $\beta_{+}$ is symmetric for $k \equiv 0, 1$ and antisymmetric for $k \equiv 2, 3 \pmod 4$; $\beta_{-}$ is symmetric for $k \equiv 0, 3$ and antisymmetric for $k \equiv 1, 2 \pmod 4$. So $F_{k}$ carries a symmetric form of this kind exactly when $k \not\equiv 2 \pmod 4$, and an antisymmetric one exactly when $k \not\equiv 0 \pmod 4$.
\item[(iii)] \emph{(Neutral, and the count of pairs.)} A symmetric $\beta_{\epsilon}$ is the orthogonal sum of the $2^{k-1}$ hyperbolic planes spanned by $v_{S}p_{k}$ and $v_{S^{c}}p_{k}$: the quadratic space $(F_{k}, \beta_{\epsilon})$ has signature $(2^{k-1}, 2^{k-1})$ and Witt index $2^{k-1}$, so by Theorem \claimref{tower.witt-index-quantum-capacity} its Clifford algebra carries exactly $2^{k-1}$ fermionic mode pairs realised by vectors, and no nondegenerate quadratic form on the $2^{k}$-dimensional space $F_{k}$ gives more. An antisymmetric $\beta_{\epsilon}$ is a symplectic form with the $2^{k-1}$ canonically conjugate pairs $(v_{S}p_{k}, \pm v_{S^{c}}p_{k})$. For odd $k$ the even and odd parity halves of $F_{k}$ are each totally null and are paired with each other; for even $k$ each half is nondegenerate.
\item[(iv)] \emph{(Three pairs, and two.)} At $k = 3$: $\beta_{+}$ is antisymmetric, $\beta_{-}$ is symmetric of signature $(4, 4)$, and the two four-dimensional parity halves are complementary totally null subspaces. Its Witt index is $4 = 3 + 1$, the pair count of the next rung: $(F_{3}, \beta_{-})$ is isometric to the vector space of $B_{4}$. The equality $2^{k-1} = k + 1$ holds for $k = 3$ and for no other $k \ge 1$. At $k = 2$ both forms are antisymmetric, so the four states carry no invariant quadratic form.
\item[(v)] \emph{(Two rules for a next level.)} Call the $2^{k}$ basis states of $F_{k}$ the objects of a level with $k$ pairs. If the objects are taken as the creators of the next level, with as many new annihilators adjoined (the hyperbolic space on $F_{k}$ and its dual), the next level has $2^{k}$ pairs, and from three the pair counts run $3, 8, 256, 2^{256}$. If the objects, with their invariant symmetric form, are taken as the generating vectors of the next level, it has $2^{k-1}$ pairs, and from three the pair counts run $3, 4, 8, 128, 2^{127}$ (every term after the first is divisible by four, so the form exists at each step), with state counts $8, 16, 256, 2^{128}$; from two this rule does not start. Both rules produce rungs of the tower and both use the stored words (objects of a level, fermionic pairs of the next); the numbers $8$ and $256$ occur in both, as pair counts of the second and third levels in the first and as state counts of the first and third levels in the second, and the next number is $2^{256} \approx 1.2 \times 10^{77}$ in the first and $2^{128} \approx 3.4 \times 10^{38}$ in the second. The horizon mode count, between $2^{407}$ and $2^{408}$ (Proposition \claimref{standard-model.trichotomy-what-kind-number}), lies between consecutive terms under either rule ($2^{256}$ and $2^{2^{256}}$; $2^{127}$ and $2^{2^{127} - 1}$). Argued, from a search of the stored tower results and not from an audit of a full cone: no stored result selects one rule, and the only growth the series proves is one pair per rung, which at three pairs agrees with the second rule and not with the first.
\end{enumerate}

## technical
Let $B_{k} = \Cl(k,k)$ be the algebra of $k$ rungs with null pairs $v_{j}, w_{j}$, vacuum idempotent $p_{k} = \prod_{j}w_{j}v_{j}$ and Fock module $F_{k} = B_{k}p_{k}$ of dimension $2^{k}$, with basis the states $v_{S}p_{k}$. With $\tau_{+}$ the reverse and $\tau_{-}$ the reverse composed with the grade involution, $\tau_{\epsilon}(\psi)\phi = \beta_{\epsilon}(\psi, \phi)\,v_{1}\cdots v_{k}$ defines the bilinear form on $F_{k}$, unique up to a factor, for which every vector is self-adjoint ($\epsilon = +1$) or anti-self-adjoint ($\epsilon = -1$). It pairs each state with its complement, and it is symmetric or antisymmetric by the sign $\epsilon^{k}(-1)^{k(k-1)/2}$, so a symmetric invariant form exists unless $k \equiv 2 \pmod 4$. A symmetric one is neutral, of Witt index $2^{k-1}$: given such a form, the $2^{k}$ states are the vectors of at most $2^{k-1}$ fermionic pairs, never of $2^{k}$.

At three pairs one form is antisymmetric and the other symmetric of signature $(4,4)$, with the two parity halves totally null, so the eight states carry four fermionic pairs, the pair count of the tower's next rung; $2^{k-1} = k + 1$ only at $k = 3$. At two pairs both forms are antisymmetric. Given the stored wording of the exponential reading, two rules follow: states as creators with new annihilators adjoined ($k \mapsto 2^{k}$: $3, 8, 256, 2^{256}$), and states as generating vectors under the invariant form ($k \mapsto 2^{k-1}$: $3, 4, 8, 128, 2^{127}$). The horizon mode count lies between consecutive terms under either, and no stored result is found that selects one (argued).

## lay
The framework's tower is built from pairs of raising and lowering operators, and a system of $k$ pairs has $2^{k}$ basic states. One unproved reading of the tower turns the states of each level into the pairs of the next, which gives the fast-growing counts $3$, $8$, $256$ and then a number near $10^{77}$. This result shows that the count depends on how that step is taken. The states of a level come with a natural way of measuring them against each other, fixed by the algebra itself. Given that structure, eight states make four pairs, not eight, because each pair needs two of them: the counts then run $3$, $4$, $8$, $128$. At the starting value three this is exactly the single step the proved tower takes. Assuming instead that each state becomes one half of a pair and its partner is added from outside gives the faster sequence. Both readings fit the words used, they disagree from the second level on, and the number of modes on the cosmic horizon falls between two steps of either, so it cannot tell them apart.

## one-liner
The Fock module of $k$ rungs carries two invariant bilinear forms, symmetric or antisymmetric by $k \bmod 4$ and neutral when symmetric, so given the invariant form $2^{k}$ states make $2^{k-1}$ fermionic pairs ($3, 4, 8, 128$ from three, the tower's own next rung at three), against $3, 8, 256, 2^{256}$ given the rule that adjoins new annihilators; the horizon count separates neither.
