---
id: transport.one-generator-minimal-minimal-completions-classified
kind: claim
version: 6
title: One generator is minimal; the minimal completions classified
status: proved
region: transport
subject: completion
tags: [refutation, transport-algorithm, classification]
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
- name: Claude Opus 5.5
  role: 'maintainer pass, citation of the retired imported Fact repointed to its derivation in geometric algebra'
  version: 6
  source: run 2026-11-07-bit-root
review: typed
about:
- obj.transport.obstruction-types
derivations:
- name: main
  uses:
  - transport.decomposition-commutation@3
  - transport.existence-classification-type-c@4
  - transport.rule-2-ideal-fusion-sharp-form@4
  - std-algebra.blade-basis@1
  - synthesis.completion-recovers-the-real-clifford-algebras@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T01.py
  tags:
  - num:5.7
- kind: check
  ref: check.py::check_no_ascent_not_simple
- kind: check
  ref: check.py::check_null_generator_thickens
- kind: check
  ref: check.py::check_nondegenerate_ascents_simple_isomorphic_not_isometric
- kind: check
  ref: check.py::check_two_directions_double_again
locators:
  paper: T01
  number: Thm 5.7
  label: thm:rule2min
  line: 1227
extraction:
  maintainer_pass_2026_11_08:
    by: ai-maintainer-pass
    note: >-
      Version 5 -> 6. Leon's decision of 7 November 2026: the imported Fact std-algebra.sylvester-inertia is retired, replaced by synthesis.completion-recovers-the-real-clifford-algebras, whose clause (iii) derives Sylvester's law of inertia in geometric algebra over any Euclidean field, the reals included; the citation and edge now point there.
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.blade-basis, synthesis.completion-recovers-the-real-clifford-algebras where the proof uses them. Version 4 -> 5.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: A split with no ascent, the null ascent a square-zero thickening with B_0/J = A, both nondegenerate ascents simple with Mat_2(Cl^0) corner, isomorphic but not isometric, and dimension 2^(n+2) for two adjoined directions. Version 2 -> 3. Check strengthened: eps_+ idempotent asserted; anticommutation over all ordered pairs; non-isometry signatures computed from the Gram matrices of the two ascents; samples moved to module level. Version 3 -> 4.'
  env: theorem
  typing:
    by: ai-typing-pass
    note: 'Kept all three premises, each invoked for a numbered clause.'
---

## formal
Let $A = \Cl(p,q)$, $p - q \equiv 1 \pmod 4$, and consider the Clifford algebras $\Cl(\mathbb{V}', Q')$ of arbitrary extensions $(\mathbb{V}', Q') \supseteq (\mathbb{V}, Q)$ of the quadratic space, $Q'$ possibly degenerate, each containing $A$ canonically and unitally. Then:
\begin{enumerate}
\item $\dim \mathbb{V}' = n$ (no ascent): $A$ itself is not simple (Theorem \claimref{transport.existence-classification-type-c}).
\item $\dim \mathbb{V}' = n + 1$, adjoined generator null ($\gamma = 0$): the fusion fails structurally. The subspace $J = A\nu$ is a nonzero proper two-sided ideal of $B_0$ with $J^2 = 0$, and $B_0 / J \cong A$: the degenerate ascent is an infinitesimal thickening of $A$, not a completion of it. (This square-zero ideal is the fibre-level germ of the degeneration sheaf of the series' sheaf-theoretic paper \cite{ButlerT4}.)
\item $\dim \mathbb{V}' = n + 1$, adjoined generator nondegenerate ($\gamma = \pm 1$ after rescaling): both ascents are simple and $\cong \Mat_2(\Cl^0(p,q))$ (Theorem \claimref{transport.rule-2-ideal-fusion-sharp-form}).
\item $\dim \mathbb{V}' \geq n + 2$: $\dim \Cl(\mathbb{V}') \geq 2^{n+2}$.
\end{enumerate}
Hence the minimal simple Clifford completions of $A$ are exactly the two one-generator ascents $\Cl(p{+}1,q)$ and $\Cl(p,q{+}1)$, of dimension $2^{n+1}$; they are inequivalent as quadratic data (the extensions $\langle +1 \rangle$ and $\langle -1 \rangle$ are non-isometric) but isomorphic as algebras; and so the minimal completion of a type-C obstruction is \emph{unique up to isomorphism}, with the residual geometric choice, the sign of the adjoined direction's square, not detected by the completed algebra.

## technical
Let $A = \Cl(p,q)$ with $p - q \equiv 1 \pmod 4$, and consider the Clifford algebras of arbitrary extensions $(\mathbb{V}', Q') \supseteq (\mathbb{V}, Q)$, $Q'$ possibly degenerate. With no ascent, $A$ is not simple. Adjoining one null generator ($\gamma = 0$) fails structurally: $J = A\nu$ is a nonzero proper two-sided ideal of $B_0$ with $J^2 = 0$ and $B_0/J \cong A$, an infinitesimal thickening rather than a completion. Adjoining one nondegenerate generator ($\gamma = \pm 1$ after rescaling) gives a simple algebra $\cong \Mat_2(\Cl^0(p,q))$. Adjoining two or more directions gives dimension at least $2^{n+2}$.

Hence the minimal simple Clifford completions of $A$ are exactly $\Cl(p{+}1,q)$ and $\Cl(p,q{+}1)$, of dimension $2^{n+1}$. They differ as quadratic data, since $\langle +1 \rangle$ and $\langle -1 \rangle$ are not isometric, but are isomorphic as algebras, so the minimal completion of a type-C obstruction is unique up to isomorphism and does not detect the sign of the adjoined direction.

## lay
When a Clifford algebra splits into two halves, one can try to repair it by adding directions. Adding nothing leaves it split; adding one direction of zero length only thickens the algebra without joining the halves; adding one direction of nonzero length joins them; adding more is larger than needed. The two possible single directions, of positive or negative square, give the same algebra, so the repair is unique and cannot tell which sign was used.

## one-liner
For $p - q \equiv 1 \pmod 4$, the minimal simple Clifford completions of $\Cl(p,q)$ are exactly the two one-generator ascents $\Cl(p{+}1,q)$ and $\Cl(p,q{+}1)$, isomorphic as algebras, while a null generator only thickens the algebra.
