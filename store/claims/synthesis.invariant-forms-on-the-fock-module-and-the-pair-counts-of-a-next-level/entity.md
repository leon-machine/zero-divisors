---
id: synthesis.invariant-forms-on-the-fock-module-and-the-pair-counts-of-a-next-level
kind: claim
version: 1
title: 'The two invariant forms on the Fock module and the pair counts of a next level'
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
  - std-algebra.chevalley-pairing@1
  - std-algebra.fock-representation@1
  - synthesis.exponential-reading-of-the-tower-is-the-iterated-fock-functor-not-the-ascent@1
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
    four). What is restated and what is added: the form $\beta_{+}$, its nondegeneracy, its pairing of grades,
    its symmetry sign and the self-adjointness of vectors are the stored Chevalley pairing
    (std-algebra.chevalley-pairing, on the Fock model of std-algebra.fock-representation, where the roles of the
    two null families are exchanged), and are restated here in the notation of the rungs; the complex case of
    three pairs is correspondence.chevalley-pairing, and the stored neighbour for spinor ideals of the even
    algebra at causal signatures is synthesis.invariant-forms-on-spinor-ideal-factor-through-reversion. Added
    here: the second form $\beta_{-}$ with its symmetry sign, the uniqueness of each form up to a factor, the
    neutral signature and Witt index of a symmetric one, and the counts of clauses (iv) and (v). All of it is
    classical (Chevalley, The Algebraic Theory of Spinors, 1954, whose pairing and symmetry law for
    $\beta_{+}$ were confirmed on the web in review through Gualtieri, Generalized complex geometry, section 2.4;
    Harvey, Spinors and Calibrations, 1990, from memory). The equality $4 = 3 + 1$ at three pairs is an
    equality of counts and not an identification with the tower's ascent (clause (iv)). The literal rule (states
    become creators), its counts, its relation to the proved ascent and the place of the horizon count under it
    are the stored base result on the exponential reading, which is cited and not re-proved; this result adds
    only the second rule and its own terms. The base's four at three pairs is the ascent's pair count; the four
    here is a Witt index; clause (iv) keeps them apart. That the second rule is another reading of the stored
    phrase is a judgement, and that no stored result selects either rule is argued from a search of the tower
    results, not audited over a full cone. The bracket of the horizon count and its rider on units are quoted
    from the base's clause (v). Transport-absent: nothing here uses the transport rules beyond
    the pair structure of the rungs.
---

## formal
\emph{Setting.} Let $B_{k} = \Cl(k,k)$, $k \ge 1$, be the algebra of $k$ rungs with its null pairs $v_{j}, w_{j}$ ($j = 1, \ldots, k$), $v_{i}v_{j} + v_{j}v_{i} = 0$, $w_{i}w_{j} + w_{j}w_{i} = 0$, $v_{i}w_{j} + w_{j}v_{i} = \delta_{ij}$, over a field of characteristic zero (the rationals in the checks). Write $v_{S} = v_{s_{1}}\cdots v_{s_{r}}$ for a subset $S = \{s_{1} < \cdots < s_{r}\}$ of the rungs, $S^{c}$ for its complement, $p_{k} = \prod_{j} w_{j}v_{j}$ for the vacuum idempotent and $\Omega_{k} = v_{1}v_{2}\cdots v_{k}$. The left ideal $F_{k} = B_{k}p_{k}$ has the basis $v_{S}p_{k}$ and is the Fock module of Theorem \claimref{tower.fock-module-one-qubit-per-rung}, of dimension $2^{k}$, the minimal left ideal on the vacuum idempotent of Proposition \claimref{std-algebra.fock-representation} with the two null families exchanged. Let $\tau_{+}$ be the reverse and $\tau_{-}$ the reverse composed with the grade involution, so that $\tau_{\epsilon}(a) = \epsilon a$ for every vector $a$, $\epsilon = \pm 1$.
\begin{enumerate}
\item[(i)] \emph{(The two forms.)} For $\psi, \phi \in F_{k}$ the product $\tau_{\epsilon}(\psi)\phi$ is a multiple of $\Omega_{k}$, and
\[
\tau_{\epsilon}(\psi)\,\phi \;=\; \beta_{\epsilon}(\psi, \phi)\,\Omega_{k}
\]
defines a nondegenerate bilinear form $\beta_{\epsilon}$ on $F_{k}$ with $\beta_{\epsilon}(a\psi, \phi) = \epsilon\,\beta_{\epsilon}(\psi, a\phi)$ for every vector $a$ of $B_{k}$; on the basis, $\beta_{\epsilon}(v_{S}p_{k}, v_{T}p_{k}) = \pm 1$ if $T = S^{c}$ and $0$ otherwise. For $\epsilon = +1$ this restates Proposition \claimref{std-algebra.chevalley-pairing}: $\beta_{+}$ is its pairing up to a factor. Added here: $\beta_{-}(\psi, \phi) = \beta_{+}(\alpha\psi, \phi)$ up to a factor, with $\alpha$ the grade involution on the module (the sign $(-1)^{|S|}$ on $v_{S}p_{k}$), and uniqueness: every bilinear form on $F_{k}$ with the adjoint property for $\epsilon$ is a multiple of $\beta_{\epsilon}$.
\item[(ii)] \emph{(Symmetry.)} $\beta_{\epsilon}(\phi, \psi) = s_{\epsilon}(k)\,\beta_{\epsilon}(\psi, \phi)$ with $s_{\epsilon}(k) = \epsilon^{k}(-1)^{k(k-1)/2}$ (for $\epsilon = +1$ the stored law of Proposition \claimref{std-algebra.chevalley-pairing}(ii)): $\beta_{+}$ is symmetric for $k \equiv 0, 1$ and antisymmetric for $k \equiv 2, 3 \pmod 4$; $\beta_{-}$ is symmetric for $k \equiv 0, 3$ and antisymmetric for $k \equiv 1, 2 \pmod 4$. So $F_{k}$ carries a symmetric form of this kind exactly when $k \not\equiv 2 \pmod 4$, and an antisymmetric one exactly when $k \not\equiv 0 \pmod 4$.
\item[(iii)] \emph{(Neutral, and the count of pairs.)} A symmetric $\beta_{\epsilon}$ is the orthogonal sum of the $2^{k-1}$ hyperbolic planes spanned by $v_{S}p_{k}$ and $v_{S^{c}}p_{k}$: the quadratic space $(F_{k}, \beta_{\epsilon})$ is hyperbolic over any field of characteristic not two, of signature $(2^{k-1}, 2^{k-1})$ over an ordered field, with Witt index $2^{k-1}$. By Theorem \claimref{tower.witt-index-quantum-capacity} its Clifford algebra carries exactly $2^{k-1}$ fermionic mode pairs realised by vectors, and no nondegenerate quadratic form on the $2^{k}$-dimensional space $F_{k}$ gives more. An antisymmetric $\beta_{\epsilon}$ is a symplectic form with the $2^{k-1}$ canonically conjugate pairs $(v_{S}p_{k}, \pm v_{S^{c}}p_{k})$. For odd $k$ the even and odd parity halves of $F_{k}$ are each totally null and are paired with each other; for even $k$ each half is nondegenerate (the stored grade pairing, Proposition \claimref{std-algebra.chevalley-pairing}(i), which holds for both forms).
\item[(iv)] \emph{(Three pairs, and two.)} At $k = 3$: $\beta_{+}$ is antisymmetric, $\beta_{-}$ is symmetric of signature $(4, 4)$, and the two four-dimensional parity halves are complementary totally null subspaces. So under the invariant symmetric form the eight states of three pairs are the vectors of four pairs. This four is a Witt index. The four of Theorem \claimref{synthesis.exponential-reading-of-the-tower-is-the-iterated-fock-functor-not-the-ascent}(ii) is a different object, the pair count of the tower's next floor $B_{4}$ after one ascent; the two agree as numbers: an equality of counts, $2^{k-1} = k + 1$, which holds for $k = 3$ and for no other $k \ge 1$, and which is not an identification of the two constructions. $(F_{3}, \beta_{-})$ and the vector space of $B_{4}$ are isometric, as any two hyperbolic spaces of dimension eight are, but no isometry is compatible with the action of $B_{3}$: the bivectors of $B_{3}$ annihilate no nonzero vector of $F_{3}$, while in their commutator action on the vector space of $B_{4}$ they annihilate the plane of $v_{4}, w_{4}$; and from four the rule of (v) gives eight, not five. At $k = 2$ both forms are antisymmetric, so the four states carry no invariant quadratic form of this kind.
\item[(v)] \emph{(A second rule for a next level.)} Call the $2^{k}$ basis states of $F_{k}$ the objects of a level with $k$ pairs. The rule in which the objects become creators and as many annihilators are adjoined is Theorem \claimref{synthesis.exponential-reading-of-the-tower-is-the-iterated-fock-functor-not-the-ascent}(i), with the stored counts $3, 8, 256, 2^{256}$; it is not repeated here. Second rule: the objects, with an invariant symmetric form ($\beta_{-}$ at $k = 3$, the only one there; either form from $k = 4$ on, where both are symmetric), are the generating vectors of the next level, which is then the floor $B_{2^{k-1}}$ of the tower. From three the pair counts run $3, 4, 8, 128, 2^{127}$ (every term after the first is divisible by four, so a symmetric form exists at each step), with state counts $8, 16, 256, 2^{128}$; from two this rule does not start. It does not reproduce the stored counts: $8$ and $256$ recur in it only as state counts of its first and third levels, and its next number is $2^{128} \approx 3.4 \times 10^{38}$ against $2^{256}$. A judgement, not a result: the second rule is another reading of the stored phrase, objects of a level as the fermionic pairs of the next. Given the bracket $2^{407} < |J| < 2^{408}$ of the horizon count quoted in Theorem \claimref{synthesis.exponential-reading-of-the-tower-is-the-iterated-fock-functor-not-the-ascent}(v), and with its rider that the comparison is of sizes only (the stored count is of registered units, not of ladder pairs), $|J|$ lies between the consecutive terms $2^{127}$ and $2^{2^{127} - 1}$ of the second rule, as it lies between consecutive terms of the first. Argued, from a search of the stored tower results and not from an audit of a full cone: no stored result selects one rule. The only growth the series proves is one pair per rung, which neither rule is.
\end{enumerate}

## technical
Let $B_{k} = \Cl(k,k)$ be the algebra of $k$ rungs with null pairs $v_{j}, w_{j}$, vacuum idempotent $p_{k} = \prod_{j}w_{j}v_{j}$ and Fock module $F_{k} = B_{k}p_{k}$ of dimension $2^{k}$, with basis the states $v_{S}p_{k}$. With $\tau_{+}$ the reverse and $\tau_{-}$ the reverse composed with the grade involution, $\tau_{\epsilon}(\psi)\phi = \beta_{\epsilon}(\psi, \phi)\,v_{1}\cdots v_{k}$ defines a bilinear form on $F_{k}$ for which every vector is self-adjoint ($\epsilon = +1$, the stored Chevalley pairing) or anti-self-adjoint ($\epsilon = -1$); each is unique up to a factor. It pairs each state with its complement, and it is symmetric or antisymmetric by the sign $\epsilon^{k}(-1)^{k(k-1)/2}$, so a symmetric invariant form exists unless $k \equiv 2 \pmod 4$. A symmetric one is neutral, of Witt index $2^{k-1}$: given such a form, the $2^{k}$ states are the vectors of at most $2^{k-1}$ fermionic pairs, never of $2^{k}$.

At three pairs one form is antisymmetric and the other symmetric of signature $(4,4)$, with the two parity halves totally null, so under that form the eight states are the vectors of four pairs. This four is a Witt index; the tower's next floor after one ascent also has four pairs (Theorem \claimref{synthesis.exponential-reading-of-the-tower-is-the-iterated-fock-functor-not-the-ascent}(ii)), an equality of counts that holds only at $k = 3$ and is not an identification: no isometry with the next floor's vector space is compatible with the action of the three-pair algebra, and from four the rule gives eight, not five. At two pairs both forms are antisymmetric. Beside the stored rule of states as creators with new annihilators adjoined ($3, 8, 256, 2^{256}$, Theorem \claimref{synthesis.exponential-reading-of-the-tower-is-the-iterated-fock-functor-not-the-ascent}(i)) this gives a second rule, states as generating vectors under an invariant symmetric form ($k \mapsto 2^{k-1}$: $3, 4, 8, 128, 2^{127}$), which is another reading of the stored phrase (a judgement) and does not reproduce the stored counts. Given the stored bracket of the horizon count, it lies in size between the terms $2^{127}$ and $2^{2^{127}-1}$ of the second rule, a comparison of sizes only, and no stored result is found that selects one (argued, from a search and not an audit).

## lay
The framework's tower is built from pairs of raising and lowering operators, and a system of $k$ pairs has $2^{k}$ basic states. One unproved reading of the tower turns the states of each level into the pairs of the next, which gives the fast-growing counts $3$, $8$, $256$ and then a number near $10^{77}$. This result shows that the count depends on how that step is taken. The states of a level come with a natural way of measuring them against each other, fixed by the algebra itself up to an overall factor. Given that structure, eight states make four pairs, not eight, because each pair needs two of them: the counts then run $3$, $4$, $8$, $128$. The proved tower also goes from three pairs to four, but that is only the same number, and only at three: it is a different construction, and its next step is five where this rule gives eight. Assuming instead that each state becomes one half of a pair and its partner is added from outside gives the faster sequence, which is the one the stored reading quotes. Calling the slower rule a second reading of the same words is a judgement. The two disagree from the second level on. The number of modes on the cosmic horizon is larger than three steps of either and smaller than the next, a comparison of sizes only (that number does not count pairs of this kind), so it cannot tell the rules apart; and, as far as a search of the stored results shows (argued, not a full audit), nothing in the framework selects one.

## one-liner
The Fock module of $k$ rungs carries two invariant bilinear forms, each unique up to a factor (one the stored Chevalley pairing), symmetric or antisymmetric by $k \bmod 4$ and neutral when symmetric, so given such a form $2^{k}$ states make $2^{k-1}$ fermionic pairs ($3, 4, 8, 128$ from three; the $4$ equals the tower's next pair count as a number only, at $k = 3$ only), against the stored $3, 8, 256, 2^{256}$ given the rule that adjoins new annihilators; that the first is a reading of the stored phrase is a judgement, and no stored result is found to select either (argued).
