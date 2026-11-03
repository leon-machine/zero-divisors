---
id: correspondence.symmetrised-quadratics-palatial-algebra
kind: claim
version: 5
title: "Symmetrised quadratics of the palatial algebra"
status: proved
region: correspondence
subject: conformal-spacetime
tags: [conformal-spinors]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T09, deposited version
review: typed
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T09.py
  tags:
  - label:lem:weyl
- kind: check
  ref: check.py::check_adjoint_action_on_generators
- kind: check
  ref: check.py::check_lie_homomorphism_and_injective
- kind: check
  ref: check.py::check_symmetric_minus_normal_is_half_trace
locators:
  paper: T09
  number: Lem 5.5
  label: lem:weyl
  line: 693
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: in the polynomial realisation: the adjoint action of q(M) on Z and Zbar, [q(M), q(N)] = hbar q([M, N]), injectivity, and q(M) = normal ordering - (hbar/2) tr M. Version 3 -> 4. Sample inputs moved to module level; no change to what is tested (injectivity rows now read on the degree-preserved image space, with its support asserted). Version 4 -> 5.'
  small_findings_pass:
    by: ai-small-findings-pass
    date: 2026-10-22
    finding: STRUCTURE L5
    open_problem: op.small-findings
    note: 'The ordering shift is signed: q(id) = sum Z Zbar - 2 hbar, so the shift is -2 hbar (minus hbar/2 per complex dimension), as T07 Fact 2.6 restates it and as the homogeneity check in T9 Thm 5.7 uses.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: No edges; the symmetrised-quadratic computation is classical (Penrose and Rindler) but no imported
      claim for it is in the store, so no standard route.
  source_title: "Symmetrised quadratics of the palatial algebra"
  source_formal: |-
    For $M \in \mathfrak{gl}(4,\C)$ with entries $M^\beta{}_\alpha$ set
    \[
    q(M) \;:=\; \tfrac12 \sum_{\alpha,\beta} M^\beta{}_\alpha\,\bigl(Z^\alpha \bar Z_\beta + \bar Z_\beta Z^\alpha\bigr) \;\in\; \mathcal{P}.
    \]
    Then:
    \begin{enumerate}
    \item $[q(M), Z^\gamma] = -\hbar\,(MZ)^\gamma$ and $[q(M), \bar Z_\gamma] = +\hbar\,(M^{\mathsf T}\bar Z)_\gamma$: the adjoint action of $q(M)$ on the linear generators is the linear action of $M$ (in the dual pair of representations), times $\hbar$;
    \item $[q(M), q(N)] = \hbar\, q([M,N])$: the map $M \mapsto q(M)/\hbar$ is an injective Lie algebra homomorphism $\mathfrak{gl}(4,\C) \to \mathcal{P}$;
    \item $q(M) = \sum M^\beta{}_\alpha Z^\alpha \bar Z_\beta - \tfrac{\hbar}{2}\operatorname{tr} M$: the symmetric and normal orderings of a quadratic differ by the central element $\tfrac{\hbar}{2}\operatorname{tr}M$; for the distinguished generator $M = \mathrm{id}$ (the helicity/homogeneity direction) the shift is $2\hbar$: one half of $\hbar$ for each of the four complex dimensions of twistor space.
    \end{enumerate}
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: "Renamed twistor space to the conformal spinor space \\CS and the twistor operators to the palatial generators (the coordinates of a conformal spinor and their conjugates). Penrose's palatial algebra is kept by name, as his programme; the proof has no twistor wording and is unchanged."
---

## formal
For $M \in \mathfrak{gl}(4,\C)$ with entries $M^\beta{}_\alpha$ set
\[
q(M) \;:=\; \tfrac12 \sum_{\alpha,\beta} M^\beta{}_\alpha\,\bigl(Z^\alpha \bar Z_\beta + \bar Z_\beta Z^\alpha\bigr) \;\in\; \mathcal{P}.
\]
Then:
\begin{enumerate}
\item $[q(M), Z^\gamma] = -\hbar\,(MZ)^\gamma$ and $[q(M), \bar Z_\gamma] = +\hbar\,(M^{\mathsf T}\bar Z)_\gamma$: the adjoint action of $q(M)$ on the linear generators is the linear action of $M$ (in the dual pair of representations), times $\hbar$;
\item $[q(M), q(N)] = \hbar\, q([M,N])$: the map $M \mapsto q(M)/\hbar$ is an injective Lie algebra homomorphism $\mathfrak{gl}(4,\C) \to \mathcal{P}$;
\item $q(M) = \sum M^\beta{}_\alpha Z^\alpha \bar Z_\beta - \tfrac{\hbar}{2}\operatorname{tr} M$: the symmetric and normal orderings of a quadratic differ by the central element $\tfrac{\hbar}{2}\operatorname{tr}M$; for the distinguished generator $M = \mathrm{id}$ (the helicity/homogeneity direction) the shift is $-2\hbar$, that is $q(\mathrm{id}) = \sum_\alpha Z^\alpha\bar Z_\alpha - 2\hbar$: minus one half of $\hbar$ for each of the four complex dimensions of the conformal spinor space $\CS$ (twistor space).
\end{enumerate}

## technical
For $M \in \mathfrak{gl}(4,\C)$ the symmetrised quadratic $q(M) = \tfrac12\sum M^\beta{}_\alpha(Z^\alpha\bar Z_\beta + \bar Z_\beta Z^\alpha)$ in the palatial algebra $\mathcal{P}$ acts on the linear generators as $M$ times $\hbar$: $[q(M), Z^\gamma] = -\hbar\,(MZ)^\gamma$ and $[q(M), \bar Z_\gamma] = \hbar\,(M^{\mathsf T}\bar Z)_\gamma$. Moreover $[q(M), q(N)] = \hbar\,q([M,N])$, so $M \mapsto q(M)/\hbar$ is an injective Lie algebra homomorphism $\mathfrak{gl}(4,\C) \to \mathcal{P}$.

Symmetric and normal orderings differ by a central term, $q(M) = \sum M^\beta{}_\alpha Z^\alpha\bar Z_\beta - \tfrac{\hbar}{2}\operatorname{tr}M$; for the distinguished generator $M = \id$, the helicity or homogeneity direction, the shift is $-2\hbar$, minus one half of $\hbar$ for each of the four complex dimensions of the conformal spinor space.

## lay
In the palatial algebra, whose generators are the four coordinates of a conformal spinor and their conjugates promoted to operators, one can build quadratic combinations of generators, averaged over the two possible orders. These combinations reproduce the algebra of four-by-four complex matrices, acting on the generators just as matrices act on vectors. Averaging the order, instead of always putting one kind of operator first, shifts each combination by a fixed number, which for the generator tied to helicity is minus one half for each of the four dimensions of the spinor space.

## one-liner
The symmetrised quadratics of the palatial algebra realise $\mathfrak{gl}(4,\C)$ faithfully through commutators and equal the normal-ordered ones minus the central term $\tfrac{\hbar}{2}\operatorname{tr}M$, a shift of $-2\hbar$ for the helicity generator.
