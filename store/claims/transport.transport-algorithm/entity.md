---
id: transport.transport-algorithm
kind: claim
version: 3
title: The transport algorithm
status: proved
region: transport
subject: completion
tags: [transport-algorithm, obstruction-types]
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
- obj.transport.obstruction-types
- obj.transport.null-lift-completion
- obj.transport.transport
- obj.transport.equivariance
derivations:
- name: main
  uses:
  - transport.classification-real-clifford-algebras@3
  - transport.cohomological-form-no-go@4
  - transport.descent-read-out-map@2
  - transport.door-one-way@5
  - transport.exhaustiveness-every-zero-divisor-annihilated-idempotent@3
  - transport.existence-classification-type-c@4
  - transport.existence-locus-type-n@5
  - transport.fusion-occurs-most-once@5
  - transport.minimality@4
  - transport.no-fourth-rule@4
  - transport.no-go-level-elements@4
  - transport.no-transport-terminates@4
  - transport.noinverse@4
  - transport.one-generator-minimal-minimal-completions-classified@5
  - transport.pinching-kernel@3
  - transport.representation-independent-minimality-completion@4
  - transport.rule-1-morita-trivial@5
  - transport.rule-2-ideal-fusion-sharp-form@4
  - transport.swap-rescale-normal-form@4
  - transport.totality@3
  - transport.type-p-self-repairing@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_step1_no_inverse_at_null_vectors_and_idempotents
- kind: check
  ref: check.py::check_step2_diagnosis_loci_and_cautions
- kind: check
  ref: check.py::check_step3_the_three_rules
- kind: check
  ref: check.py::check_steps4_and_5_compute_then_descend
- kind: check
  ref: check.py::check_step6_bookkeeping_and_no_termination
locators:
  paper: T01
  number: Sec 8.1
  label: sec:algorithm
  line: 1584
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the six steps: no inverse at null vectors, diagnosis loci for n <= 5 with the cautions, Rules 1 and 2 and type P, compute and descend in the completion, and the residue bookkeeping over all histories to n <= 5. Version 2 -> 3.'
  env: algorithm
  unresolved_refs:
  - ex:cl10
  - ex:cl20
  - rem:classical
  - rem:forgottenbit
  typing:
    by: ai-typing-pass
    added:
    - obj.transport.obstruction-types
    note: 'Kept all cited results, since each licenses a step of the procedure (the pinching kernel included,
      as part of what Step 5 states about descent); added an about edge to the obstruction types used
      in Step 2. Levels pass: conditions already kept.'
---

## formal
The Principle says what is true; practice needs to know what to do. The theorems distil into a six-step procedure, and every step names the theorem, proved above, that licenses it. Table \ref{tab:algorithm} is the one-page version: the theorems in operational form. That the steps form a decision procedure with no gaps is itself a theorem, Corollary \claimref{transport.no-fourth-rule}.




\begin{enumerate}
\item[\textbf{Step 1.}] \textbf{Locate the failure.} Identify the element at which invertibility fails, or, if the construction is a family, the locus at which it fails. Nothing later depends on how this is done; it is a computation in the case at hand. What the algebra guarantees is that the failure cannot be argued away: a null vector has no inverse in \emph{any} unital algebra containing the base (Lemma \claimref{transport.noinverse}), and neither has an idempotent.

\item[\textbf{Step 2.}] \textbf{Diagnose the type.} Ask, in order:
  \begin{itemize}
  \item Is the failing element a vector $v$ with $Q(v) = 0$? Then the obstruction is \textbf{type N}. These exist exactly in mixed signature, $pq \neq 0$ (Proposition \claimref{transport.existence-locus-type-n}).
  \item Is it a \emph{central} idempotent? Then \textbf{type C}. These exist exactly when $p - q \equiv 1 \pmod 4$, and are then exactly the two projectors $\tfrac12(1 \pm \omega)$ (Theorem \claimref{transport.existence-classification-type-c}); equivalently, exactly when the algebra is not simple (Theorem \claimref{transport.classification-real-clifford-algebras}).
  \item Otherwise \textbf{type P}: a non-central idempotent, or an element annihilated by one.
  \end{itemize}
  The trichotomy is exhaustive: every zero divisor of a nondegenerate real Clifford algebra is annihilated by a nontrivial idempotent, possibly central in the split signatures, and then exactly when the element lies in one ideal (Theorem \claimref{transport.exhaustiveness-every-zero-divisor-annihilated-idempotent}). Two cautions. The nilpotency locus is strictly larger than the type-N locus, and nilpotence alone does not diagnose N (Example \ref{ex:cl20}); and a single algebra may carry all three types at once (Example \ref{ex:cl10}).

\item[\textbf{Step 3.}] \textbf{Apply the rule.}
  \begin{itemize}
  \item \textbf{Type N, Rule 1.} Adjoin one hyperbolic plane: $\Cl(p,q) \to \Cl(p{+}1,q{+}1)$. Do not expect the element to be repaired: no equivariant assignment of a partner to $v$ exists, in this ascent or any other (Theorem \claimref{transport.no-go-level-elements}), and the obstruction is a cohomology class that every enlargement pulls back unchanged (Theorem \claimref{transport.cohomological-form-no-go}). What is repaired is the space of points (Step 4). The increment is forced: $(+1,+1)$, never $(+2,0)$ or $(0,+2)$, among null-lift completions (Theorem \claimref{transport.minimality}), and no algebra with a smaller or differently balanced quadric can host the resolution however the base is embedded in it (Theorem \claimref{transport.representation-independent-minimality-completion}).
  \item \textbf{Type C, Rule 2.} Adjoin one generator $\nu$ orthogonal to $\mathbb{V}$, of either nonzero square. The grade involution becomes inner, the two ideals fuse, and the completion is $\Mat_2(\Cl^0(p,q))$, simple (Theorem \claimref{transport.rule-2-ideal-fusion-sharp-form}). The null-generator ascent is not an option: it produces a square-zero ideal and never fuses (Theorem \claimref{transport.one-generator-minimal-minimal-completions-classified}(2)). The sign of $\nu^2$ is free and the algebra forgets it (Remark \ref{rem:forgottenbit}); if it matters for the application, it must be fixed by structure outside the algebra.
  \item \textbf{Type P.} Do nothing. The identity assignment $\sigma(e) = e$ is a total, fully equivariant von Neumann repair, at signature increment $(0,0)$ (Proposition \claimref{transport.type-p-self-repairing}).
  \end{itemize}

\item[\textbf{Step 4.}] \textbf{Compute in the completion.} For type N this is the substantive step, and it is where the classical formulas apply. Represent points, not elements: lift $x \in \mathbb{V}$ to the null ray of
  \[
  X(x) \;=\; \nO + x + \tfrac12 Q(x)\,\nInf ,
  \]
  which satisfies the incidence condition $Q(x) = 2st$ in the homogeneous coordinates $(s,x,t)$ of Proposition \claimref{transport.swap-rescale-normal-form}. The reciprocal is then the linear involution
  \[
  \iota(s,\,x,\,t) \;=\; (2t,\ x,\ \tfrac12 s),
  \]
  total on the quadric and never failing (Theorem \claimref{transport.totality}). All nonlinearity and all division have been deferred to a single read-out. This is the linearise-then-normalise pattern of homogeneous coordinates and M\"obius matrices, encountered here as forced rather than chosen (Remark \ref{rem:classical}).

\item[\textbf{Step 5.}] \textbf{Descend, and state what descent costs.} Return the answer to $\mathbb{V}$ with the read-out $\dsc[\,s\nO + x + t\nInf\,] = x/s$. On the invertible locus the composite gives exactly the classical answer (Lemma \claimref{transport.descent-read-out-map}(2)); where the first slot vanishes the answer is an ideal point and corresponds to no point of $\mathbb{V}$ (Lemma \claimref{transport.descent-read-out-map}(3)). \emph{The refusal of the read-out is information, not failure}: it says the answer exists and lies outside the original space. At the level of elements the corresponding statement is stronger and worth knowing before relying on any descent: the pinching onto the base is a conditional expectation whose kernel is exactly the adjoined ladder sector (Proposition \claimref{transport.pinching-kernel}), and there is no unital algebra homomorphism from either completion back to its base at all (Theorem \claimref{transport.door-one-way}). Descent is invertible on the transported elements and impossible on the elements the ascent adjoined.

\item[\textbf{Step 6.}] \textbf{Iterate, or stop.} Ask whether the completion carries an obstruction of its own. It does: no transport terminates in a division algebra (Proposition \claimref{transport.no-transport-terminates}). But the bookkeeping is finite in the following sense: Rule 1 fixes the mod-8 residue, so the taxonomy of the completion is that of the base and iterating changes nothing structural (Theorem \claimref{transport.rule-1-morita-trivial}), while Rule 2 moves the residue off the split classes and can therefore occur at most once in any transport history (Proposition \claimref{transport.fusion-occurs-most-once}). A transport history takes at most one step on the clock, and then remains fixed.
\end{enumerate}

## technical
The theorems distil into a six-step procedure, each step licensed by a proved result. Locate the failure: a null vector has no inverse in any unital algebra containing the base. Diagnose the type: a vector with $Q(v) = 0$ is type N, present exactly when $pq \neq 0$; a central idempotent is type C, present exactly when $p - q \equiv 1 \pmod 4$, which is when the algebra is not simple; anything else is type P; and the trichotomy is exhaustive. Apply the rule: for N adjoin one hyperbolic plane, $\Cl(p,q) \to \Cl(p{+}1,q{+}1)$, expecting a repair of points and not of elements; for C adjoin one generator of nonzero square, giving the simple $\Mat_2(\Cl^0(p,q))$; for P do nothing.

Compute in the completion, lifting $x$ to $X(x) = \nO + x + \frac12 Q(x)\,\nInf$ and using the total linear involution $\iota(s, x, t) = (2t, x, \frac12 s)$. Descend with $\dsc[s\,\nO + x + t\,\nInf] = x/s$, which gives the classical answer on the invertible locus and an ideal point elsewhere; no unital homomorphism takes a completion back to its base. Iterate or stop: every completion carries an obstruction of its own, but Rule 1 fixes the mod-8 residue and Rule 2 occurs at most once, so a history takes at most one step on the clock. That the steps leave no gaps is the no-fourth-rule corollary.

## lay
This is the series' recipe for what to do when division fails. Find where it fails, decide which of three kinds of failure it is, apply the matching fix (add a pair of dimensions, add one dimension, or do nothing), do the calculation in the enlarged setting, and bring the answer back, noting where it cannot come back. The recipe can be repeated, but its bookkeeping settles after at most one change.

## one-liner
The transport results assemble into a six-step procedure (locate, diagnose, apply the rule, compute, descend, iterate) in which every step is licensed by a proved result and no case is left uncovered.
